#!/usr/bin/env python3
"""Columna vertebral relacional del sistema de propuestas Intezia.

Recorre clientes/propuestas/*/meta.json (la fuente fechada, §4.19) y los enlaza en un
modelo relacional: Propuestas <-> Clientes <-> Dashboards. Escribe dos archivos en
clientes/:
  - INDEX.json  -> fuente legible por máquina (para futuros scripts / consultas).
  - INDEX.md    -> vista relacional legible por el equipo e IDIA (pipeline + rollups).

No inventa datos: la división sale de brief.md (o, en su defecto, de la ruta del logo en
index.html); si no hay señal, queda "?". Las 46 propuestas legacy sin meta.json NO se
fuerzan al grafo: se listan aparte como "pendiente backfill" para que queden visibles.

Uso:
  python3 scripts/indexar.py            # regenera clientes/INDEX.{json,md}
  python3 scripts/indexar.py --check    # solo reporta, no escribe (para verificación)

Diseñado para correrse en cada entrega (se puede enganchar a generar-pdf.sh) o a mano.
"""
from __future__ import annotations

import datetime
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_PROPUESTAS = os.path.join(RAIZ, "clientes", "propuestas")
DIR_DASHBOARDS = os.path.join(RAIZ, "clientes", "dashboards")
SALIDA_JSON = os.path.join(RAIZ, "clientes", "INDEX.json")
SALIDA_MD = os.path.join(RAIZ, "clientes", "INDEX.md")

COTIZACION_DIAS = 30  # §3 políticas comerciales: cotizaciones válidas 30 días

# Carpetas que no son propuestas de cliente (plantillas / internas de catálogo).
IGNORAR = {"_base"}


def detectar_division(carpeta: str) -> str:
    """educacion / fundacion / '?' — best-effort, nunca inventa."""
    brief = os.path.join(carpeta, "brief.md")
    if os.path.isfile(brief):
        with open(brief, encoding="utf-8", errors="ignore") as f:
            txt = f.read()
        m = re.search(r"divisi[oó]n[^\n]*?(fundaci[oó]n|educaci[oó]n)", txt, re.IGNORECASE)
        if m:
            return "fundacion" if m.group(1).lower().startswith("fundaci") else "educacion"
    # Respaldo: la ruta del logo en index.html delata la división.
    html = os.path.join(carpeta, "index.html")
    if os.path.isfile(html):
        with open(html, encoding="utf-8", errors="ignore") as f:
            txt = f.read()
        m = re.search(r"logos/(fundacion|educacion)/", txt)
        if m:
            return m.group(1)
    return "?"


def cargar_meta(ruta: str) -> dict | None:
    try:
        with open(ruta, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  ⚠️  meta.json ilegible en {ruta}: {e}", file=sys.stderr)
        return None


def dias_desde(fecha_iso: str, hoy: datetime.date) -> int | None:
    try:
        d = datetime.date.fromisoformat(fecha_iso)
    except (ValueError, TypeError):
        return None
    return (hoy - d).days


def construir(hoy: datetime.date) -> dict:
    registradas: list[dict] = []
    backfill: list[dict] = []

    for carpeta in sorted(glob.glob(os.path.join(DIR_PROPUESTAS, "*"))):
        if not os.path.isdir(carpeta):
            continue
        slug = os.path.basename(carpeta)
        if slug in IGNORAR or slug.startswith("_"):
            continue
        tiene_deck = os.path.isfile(os.path.join(carpeta, "index.html"))
        tiene_pdf = bool(glob.glob(os.path.join(carpeta, "*.pdf")))
        meta_path = os.path.join(carpeta, "meta.json")

        if not os.path.isfile(meta_path):
            backfill.append({"slug": slug, "tiene_deck": tiene_deck, "tiene_pdf": tiene_pdf})
            continue

        meta = cargar_meta(meta_path) or {}
        division = detectar_division(carpeta)
        dias = dias_desde(meta.get("fecha_entrega"), hoy)
        vigente = None
        if dias is not None:
            vigente = dias <= COTIZACION_DIAS
        registradas.append({
            "codigo": meta.get("codigo") or "(sin código)",
            "slug": slug,
            "cliente": meta.get("cliente") or "(sin cliente)",
            "tipo": meta.get("tipo", ""),
            "eje": meta.get("eje", ""),
            "estado": meta.get("estado", "?"),
            "fecha_entrega": meta.get("fecha_entrega"),
            "division": division,
            "dias_desde_entrega": dias,
            "cotizacion_vigente": vigente,
            "tiene_deck": tiene_deck,
            "tiene_pdf": tiene_pdf,
        })

    # Relación Clientes <- Propuestas (el pago de lo relacional: agrupar por cliente).
    clientes: dict[str, dict] = {}
    for p in registradas:
        c = clientes.setdefault(p["cliente"], {
            "cliente": p["cliente"], "propuestas": [], "slugs": [], "estados": {}})
        c["propuestas"].append(p["codigo"])
        c["slugs"].append(p["slug"])
        c["estados"][p["estado"]] = c["estados"].get(p["estado"], 0) + 1
    clientes_lista = sorted(clientes.values(),
                            key=lambda c: (-len(c["slugs"]), c["cliente"]))
    for c in clientes_lista:
        c["total"] = len(c["slugs"])

    # Dashboards Edu-Trace.
    dashboards = []
    if os.path.isdir(DIR_DASHBOARDS):
        for d in sorted(glob.glob(os.path.join(DIR_DASHBOARDS, "*"))):
            if os.path.isdir(d):
                slug = os.path.basename(d)
                dashboards.append({
                    "slug": slug,
                    "tiene_resultados": os.path.isfile(os.path.join(d, "resultados.json")),
                    "tiene_deck": os.path.isfile(os.path.join(d, "index-cliente.html")),
                })

    por_estado: dict[str, int] = {}
    por_division: dict[str, int] = {}
    for p in registradas:
        por_estado[p["estado"]] = por_estado.get(p["estado"], 0) + 1
        por_division[p["division"]] = por_division.get(p["division"], 0) + 1

    return {
        "generado": hoy.isoformat(),
        "resumen": {
            "propuestas_total": len(registradas) + len(backfill),
            "registradas": len(registradas),
            "sin_registrar": len(backfill),
            "dashboards": len(dashboards),
            "por_estado": por_estado,
            "por_division": por_division,
        },
        "clientes": clientes_lista,
        "propuestas": sorted(registradas,
                             key=lambda p: (p["fecha_entrega"] or "", p["codigo"]),
                             reverse=True),
        "dashboards": dashboards,
        "pendiente_backfill": sorted(backfill, key=lambda b: b["slug"]),
    }


def render_md(idx: dict) -> str:
    r = idx["resumen"]
    L = []
    L.append("# Índice relacional — Sistema de Propuestas Intezia\n")
    L.append(f"> Generado por `scripts/indexar.py` el **{idx['generado']}**. "
             "No editar a mano: se regenera. Fuente fechada = los `meta.json` (§4.19).\n")
    L.append(f"**{r['propuestas_total']} propuestas** · "
             f"{r['registradas']} registradas · "
             f"{r['sin_registrar']} pendientes de backfill · "
             f"{r['dashboards']} dashboards\n")

    estados = " · ".join(f"{k}: {v}" for k, v in sorted(r["por_estado"].items()))
    divs = " · ".join(f"{k}: {v}" for k, v in sorted(r["por_division"].items()))
    L.append(f"**Pipeline:** {estados or '—'}  \n**División:** {divs or '—'}\n")

    # Propuestas en corrección (vuelven a revisión antes de reenviarse): reloj de
    # cotización en pausa, no entran en la ventana de 30 días.
    encorreccion = [p for p in idx["propuestas"] if p["estado"] == "En corrección"]
    if encorreccion:
        L.append("## 🔧 En corrección (reenvío pendiente)\n")
        for p in encorreccion:
            L.append(f"- **{p['codigo']}** · {p['cliente']} — vuelve a revisión; "
                     "regresa a «Enviada» al cerrarse.")
        L.append("")

    # Señal de OS: cotizaciones por vencer / vencidas (válidas 30 días desde el envío).
    porvencer = [p for p in idx["propuestas"]
                 if p["dias_desde_entrega"] is not None
                 and p["estado"] in ("Enviada", "Entregada")]
    if porvencer:
        L.append("## ⏱️ Cotizaciones — ventana de 30 días\n")
        L.append("| Código | Cliente | Entregada | Días | Estado cotización |")
        L.append("|---|---|---|---|---|")
        for p in sorted(porvencer, key=lambda x: x["dias_desde_entrega"], reverse=True):
            d = p["dias_desde_entrega"]
            rest = COTIZACION_DIAS - d
            if rest < 0:
                tag = f"⚠️ vencida hace {-rest}d"
            elif rest <= 7:
                tag = f"🔸 vence en {rest}d"
            else:
                tag = f"✅ vigente ({rest}d)"
            L.append(f"| {p['codigo']} | {p['cliente']} | {p['fecha_entrega']} | {d} | {tag} |")
        L.append("")

    L.append("## 📋 Propuestas registradas\n")
    L.append("| Código | Cliente | Tipo | Estado | Entrega | Div | PDF |")
    L.append("|---|---|---|---|---|---|---|")
    for p in idx["propuestas"]:
        pdf = "✓" if p["tiene_pdf"] else "—"
        L.append(f"| {p['codigo']} | {p['cliente']} | {p['tipo']} | "
                 f"{p['estado']} | {p['fecha_entrega'] or '—'} | {p['division']} | {pdf} |")
    L.append("")

    multi = [c for c in idx["clientes"] if c["total"] > 1]
    if multi:
        L.append("## 🔗 Clientes con varias propuestas\n")
        for c in multi:
            L.append(f"- **{c['cliente']}** ({c['total']}): "
                     + ", ".join(c["propuestas"]))
        L.append("")

    if idx["dashboards"]:
        L.append("## 📊 Dashboards Edu-Trace\n")
        for d in idx["dashboards"]:
            L.append(f"- `{d['slug']}`")
        L.append("")

    if idx["pendiente_backfill"]:
        L.append(f"## 🌑 A oscuras — pendiente backfill ({len(idx['pendiente_backfill'])})\n")
        L.append("> Carpetas sin `meta.json`: invisibles a las consultas deterministas. "
                 "Backfill ligero pendiente (código · cliente · tipo · estado).\n")
        slugs = ", ".join(f"`{b['slug']}`" for b in idx["pendiente_backfill"])
        L.append(slugs + "\n")

    return "\n".join(L)


def main() -> int:
    check = "--check" in sys.argv
    hoy = datetime.date.today()
    idx = construir(hoy)
    md = render_md(idx)

    r = idx["resumen"]
    print(f"Índice: {r['registradas']} registradas · "
          f"{r['sin_registrar']} pendientes · {r['dashboards']} dashboards "
          f"({r['propuestas_total']} carpetas).")

    if check:
        print("(--check: no se escribió nada)")
        return 0

    with open(SALIDA_JSON, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(SALIDA_MD, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Escrito: {os.path.relpath(SALIDA_JSON, RAIZ)} + "
          f"{os.path.relpath(SALIDA_MD, RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
