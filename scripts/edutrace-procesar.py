#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
edutrace-procesar.py — Pipeline de datos del Dashboard de Impacto Edu-Trace.

Lee el export del Google Form "Encuesta Edu-Trace" (encuesta.csv) + el mapeo de
bloques (mapeo.json) de un cliente, calcula el Índice de Impacto y sus 4 ejes, y
escribe resultados.json — el artefacto intermedio que alimenta los dos decks.

USO:
    python3 scripts/edutrace-procesar.py clientes/dashboards/<slug>/

ENTRADA  (en el directorio del cliente):
    encuesta.csv   export crudo del Google Form (CON datos personales)
    mapeo.json     declara qué columna es qué bloque + la CLAVE del Bloque C

SALIDA:
    resultados.json   SIN datos personales (sin cédula, sin correo) — versionable

PRIVACIDAD (CLAUDE.md §4.16 — bloqueante):
    La cédula y el correo se leen solo para deduplicar en memoria; NUNCA se
    escriben en resultados.json. La lista de participación lleva nombre +
    departamento, sin puntaje individual.

ÍNDICE DE IMPACTO (0-100) — pesos "priorizar lo medido" (CLAUDE.md §4.17):
    Índice = 0.30·E1 + 0.35·E2 + 0.20·E3 + 0.15·E4
      E1 Competencia percibida   = norm(media "Competencia Adquirida")     · Bloque B
      E2 Retención objetiva      = % de aciertos global                    · Bloque C
      E3 Aplicabilidad e impacto = norm(media de Aplicabilidad+Productividad) · Bloque B
      E4 Calidad de experiencia  = norm(media de los 4 ítems de facilitador)  · Bloque D
    norm(x) = (x - 1) / 4 * 100   (Likert 1-5 → 0-100)
"""

import csv
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

PESOS = {"E1": 0.30, "E2": 0.35, "E3": 0.20, "E4": 0.15}


# ── utilidades ────────────────────────────────────────────────────────────────
def norm_texto(s):
    """minúsculas + sin acentos + espacios colapsados — para comparar/agrupar."""
    s = (s or "").strip().lower()
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn")
    return " ".join(s.split())


def norm_likert(media):
    """Likert 1-5 → 0-100. None si no hay datos."""
    if media is None:
        return None
    return round((media - 1) / 4 * 100, 1)


def a_entero(v):
    """'5' → 5 ; vacío/no-numérico → None (se excluye del promedio)."""
    try:
        n = int(str(v).strip())
        return n if 1 <= n <= 5 else None
    except (ValueError, TypeError):
        return None


def media(valores):
    vals = [v for v in valores if v is not None]
    return round(sum(vals) / len(vals), 2) if vals else None


# ── carga ───────────────────────────────────────────────────────────────────
def cargar(directorio):
    d = Path(directorio)
    mapeo = json.loads((d / "mapeo.json").read_text(encoding="utf-8"))
    with (d / "encuesta.csv").open(encoding="utf-8-sig", newline="") as f:
        filas = list(csv.DictReader(f))
    return mapeo, filas


def col(fila, nombre_col):
    """Lee una columna por su header exacto; error claro si falta."""
    if nombre_col not in fila:
        raise SystemExit(
            f"ERROR: la columna '{nombre_col}' del mapeo.json no existe en encuesta.csv.\n"
            f"       Columnas disponibles: {list(fila.keys())}"
        )
    return fila[nombre_col]


# ── calificación del Bloque C ─────────────────────────────────────────────────
def califica_c(respuesta, keywords, modo):
    """True si la respuesta contiene las keywords correctas (deducidas por lógica)."""
    r = norm_texto(respuesta)
    presentes = [k for k in keywords if norm_texto(k) in r]
    if modo == "alguna":
        return len(presentes) >= 1
    return len(presentes) == len(keywords)  # modo "todas" (default)


# ── cálculo principal ─────────────────────────────────────────────────────────
def procesar(mapeo, filas):
    n = len(filas)
    if n == 0:
        raise SystemExit("ERROR: encuesta.csv no tiene respuestas.")

    idmap = mapeo["identidad"]
    b = mapeo["bloque_b"]
    d = mapeo["bloque_d"]

    # --- Bloque B: medias por ítem (escala 1-5) ---
    def serie(colname):
        return [a_entero(col(fila, colname)) for fila in filas]

    m_brecha = media(serie(b["brecha"]["col"]))
    m_comp = media(serie(b["competencia"]["col"]))
    m_aplic = media(serie(b["aplicabilidad"]["col"]))
    m_prod = media(serie(b["productividad"]["col"]))

    # --- Bloque D: medias por ítem ---
    m_d = {k: media(serie(d[k]["col"])) for k in ("claridad", "acompanamiento", "tiempo", "dominio")}

    # --- Bloque C: calificación bien/mal ---
    c_detalle = []
    aciertos_tot = intentos_tot = 0
    for q in mapeo["bloque_c"]:
        aciertos = 0
        contestadas = 0
        for fila in filas:
            resp = col(fila, q["col"]).strip()
            if not resp:
                continue
            contestadas += 1
            if califica_c(resp, q["keywords_correctas"], q.get("modo", "todas")):
                aciertos += 1
        pct = round(aciertos / contestadas * 100, 1) if contestadas else None
        c_detalle.append({
            "alias": q["alias"],
            "aciertos": aciertos,
            "contestadas": contestadas,
            "pct": pct,
            "clave": q["keywords_correctas"],
        })
        aciertos_tot += aciertos
        intentos_tot += contestadas
    pct_global_c = round(aciertos_tot / intentos_tot * 100, 1) if intentos_tot else None

    # --- Ejes del Índice (0-100) ---
    E1 = norm_likert(m_comp)
    E2 = pct_global_c
    E3 = norm_likert(media([m_aplic, m_prod]))
    E4 = norm_likert(media([m_d["claridad"], m_d["acompanamiento"], m_d["tiempo"], m_d["dominio"]]))

    def ponderar(ejes):
        usados = {k: v for k, v in ejes.items() if v is not None}
        peso = sum(PESOS[k] for k in usados)
        if not peso:
            return None
        return round(sum(PESOS[k] * v for k, v in usados.items()) / peso)

    indice = ponderar({"E1": E1, "E2": E2, "E3": E3, "E4": E4})

    # --- Satisfacción general en estrellas (1-5) — resume TODO el Índice ---
    # Mapea el Índice 0-100 a estrellas con medias (nearest 0.5).
    estrellas = round(int(indice / 10 + 0.5) / 2, 1) if indice is not None else None
    if estrellas is None:
        satisfaccion = None
    elif estrellas >= 4.5:
        satisfaccion = "Excelente"
    elif estrellas >= 3.5:
        satisfaccion = "Muy buena"
    elif estrellas >= 2.5:
        satisfaccion = "Buena"
    elif estrellas >= 1.5:
        satisfaccion = "Regular"
    else:
        satisfaccion = "Baja"

    # --- Salto de aprendizaje percibido (retrospectivo, escala 1-5) ---
    salto = round(m_comp - m_brecha, 2) if (m_comp is not None and m_brecha is not None) else None

    # --- Segmentación por departamento ---
    grupos = defaultdict(list)
    etiquetas = defaultdict(Counter)
    for fila in filas:
        bruto = col(fila, idmap["departamento"]).strip() or "Sin asignar"
        clave = norm_texto(bruto)
        grupos[clave].append(fila)
        etiquetas[clave][bruto] += 1

    por_departamento = []
    for clave, fs in grupos.items():
        display = etiquetas[clave].most_common(1)[0][0]
        comp = media([a_entero(col(x, b["competencia"]["col"])) for x in fs])
        aplic = media([a_entero(col(x, b["aplicabilidad"]["col"])) for x in fs])
        prod = media([a_entero(col(x, b["productividad"]["col"])) for x in fs])
        d_vals = []
        for k in ("claridad", "acompanamiento", "tiempo", "dominio"):
            d_vals.append(media([a_entero(col(x, d[k]["col"])) for x in fs]))
        # Retención objetiva del grupo
        ac = it = 0
        for q in mapeo["bloque_c"]:
            for x in fs:
                resp = col(x, q["col"]).strip()
                if not resp:
                    continue
                it += 1
                if califica_c(resp, q["keywords_correctas"], q.get("modo", "todas")):
                    ac += 1
        e2g = round(ac / it * 100, 1) if it else None
        e1g, e3g, e4g = norm_likert(comp), norm_likert(media([aplic, prod])), norm_likert(media(d_vals))
        ind_g = None
        usados = {k: v for k, v in {"E1": e1g, "E2": e2g, "E3": e3g, "E4": e4g}.items() if v is not None}
        if usados:
            peso = sum(PESOS[k] for k in usados)
            ind_g = round(sum(PESOS[k] * v for k, v in usados.items()) / peso)
        por_departamento.append({
            "departamento": display,
            "n": len(fs),
            "indice": ind_g,
            "ejes": {
                "E1_competencia_percibida": round(e1g) if e1g is not None else None,
                "E2_retencion_objetiva": e2g,
                "E3_aplicabilidad_impacto": round(e3g) if e3g is not None else None,
                "E4_calidad_experiencia": round(e4g) if e4g is not None else None,
            },
        })
    por_departamento.sort(key=lambda x: (-(x["indice"] or 0), x["departamento"]))

    # --- Lista de participación (SIN cédula, SIN correo, SIN puntaje) ---
    participacion = [{
        "nombre": col(fila, idmap["nombre"]).strip().title(),
        "departamento": (col(fila, idmap["departamento"]).strip() or "Sin asignar"),
    } for fila in filas]

    # --- Bloque E: textos abiertos por pregunta (opiniones, sin vincular a nombre) ---
    bloque_e = []
    for q in mapeo["bloque_e"]:
        respuestas = [col(fila, q["col"]).strip() for fila in filas if col(fila, q["col"]).strip()]
        bloque_e.append({"alias": q["alias"], "respuestas": respuestas})

    return {
        "capacitacion": mapeo["capacitacion"],
        "n_respuestas": n,
        "indice": indice,
        "estrellas": estrellas,
        "satisfaccion": satisfaccion,
        "ejes": {
            "E1_competencia_percibida": {"valor": E1, "peso": PESOS["E1"], "fuente": "Bloque B · Competencia Adquirida"},
            "E2_retencion_objetiva":    {"valor": E2, "peso": PESOS["E2"], "fuente": "Bloque C · % aciertos (medido)"},
            "E3_aplicabilidad_impacto": {"valor": E3, "peso": PESOS["E3"], "fuente": "Bloque B · Aplicabilidad + Productividad"},
            "E4_calidad_experiencia":   {"valor": E4, "peso": PESOS["E4"], "fuente": "Bloque D · Facilitador"},
        },
        "bloque_b_medias": {
            "brecha_antes": m_brecha, "competencia_despues": m_comp,
            "aplicabilidad": m_aplic, "productividad": m_prod,
        },
        "salto_aprendizaje_percibido": salto,
        "bloque_c": {"global_pct": pct_global_c, "preguntas": c_detalle},
        "bloque_d_medias": m_d,
        "por_departamento": por_departamento,
        "participacion": participacion,
        "bloque_e": bloque_e,
        "_aviso": "Datos B y D son AUTOPERCIBIDOS; el salto es RETROSPECTIVO. "
                  "Solo el Bloque C (E2) es medición objetiva. Cédula y correo excluidos (§4.16).",
    }


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Uso: python3 scripts/edutrace-procesar.py clientes/dashboards/<slug>/")
    directorio = sys.argv[1]
    mapeo, filas = cargar(directorio)
    res = procesar(mapeo, filas)
    salida = Path(directorio) / "resultados.json"
    salida.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")

    e = res["ejes"]
    print(f"✓ resultados.json escrito en {salida}")
    print(f"  Respuestas (N): {res['n_respuestas']}")
    print(f"  ÍNDICE DE IMPACTO: {res['indice']}/100")
    print(f"  SATISFACCIÓN GENERAL: {res['estrellas']}/5 estrellas ({res['satisfaccion']})")
    print(f"    E1 Competencia percibida : {e['E1_competencia_percibida']['valor']}")
    print(f"    E2 Retención objetiva    : {e['E2_retencion_objetiva']['valor']}%  (medido)")
    print(f"    E3 Aplicabilidad/impacto : {e['E3_aplicabilidad_impacto']['valor']}")
    print(f"    E4 Calidad/facilitador   : {e['E4_calidad_experiencia']['valor']}")
    print(f"  Salto percibido (retrospectivo): +{res['salto_aprendizaje_percibido']} en escala 1-5")
    print(f"  Departamentos: {len(res['por_departamento'])}")
    print(f"  Bloque C por pregunta: " +
          " · ".join(f"{q['alias'][:24]}={q['pct']}%" for q in res['bloque_c']['preguntas']))


if __name__ == "__main__":
    main()
