#!/usr/bin/env python3
"""
habilidades-importar-insumo.py — Extrae un borrador de datos.json desde el docx de insumo de Habilidades.

El insumo estándar que Productos y Servicios entrega tras la Detección («<CLIENTE>_Habilidades_Procesos_
Ruta_y_Horas.docx») trae por área una tabla ID / Solución y entregable / C / T / A / Total / Fase, los
encabezados «Carril <herramienta> — N soluciones, M horas» y «<Área> — N h», y la tabla «Resumen de horas»
con los frentes. Este script los lee y arma el esqueleto de datos.json para
scripts/generar-habilidades-compacto.py.

Qué extrae (de forma literal): carriles, áreas (con proceso base si el encabezado es «Proceso base — …»),
soluciones (id, texto completo → `detalle`, C/T/A, fase) y frentes (id, carril, áreas, horas). Desde la plantilla v3
(2026-10-08) la propuesta no lleva semanas ni sesiones: si el docx dice cuántas semanas de trabajo son o un tope de horas
por semana, eso queda como supuesto interno (`supuestos`), nunca en el deck; el calendario se acuerda en el kickoff.
Qué NO puede extraer y deja como POR_DEFINIR (el generador se niega a publicar mientras existan):
datos del cliente, división, textos de portada/alcance/ruta, la descripción de cada fase, hitos y, desde la
plantilla v2 (2026-10-07), lo que pide Ventas: areas[].para_que (qué resuelve cada área, con palabras del cliente),
frentes[].nombre (nombre de la línea de trabajo que ve el cliente), metodo (quién construye, cómo funciona en la
práctica, cómo se cuidan los datos), logistica (modalidad, participantes, arranque) y proximos_pasos.asesora.
Los nombres cortos de entregable se proponen acortando el texto del insumo y quedan marcados `_revisar`
(el generador también bloquea hasta que se revisen y se borre la marca).

Lectura: el docx se lee por PÁRRAFOS y FILAS DE TABLA (no aplanado a líneas), de modo que celdas vacías o con
varios párrafos no desplazan las columnas. Se ignora el texto borrado de control de cambios.

Validaciones cruzadas contra lo que declara el propio docx: horas por área, por carril y por frente; total de
cada fila (C+T+A); cobertura (filas con id en el docx frente a filas importadas). Sale con código 1 si no
reconoce ningún carril o ninguna solución.

Uso:
    python3 scripts/habilidades-importar-insumo.py <insumo.docx> --nombre "Cliente" --slug cliente-cai0NN --codigo CAI-0NN
        [--salida clientes/propuestas/<slug>/datos.json] [--forzar]
No sobrescribe un --salida existente salvo con --forzar (re-importar una versión nueva del insumo destruiría el
trabajo manual: copiar a mano las soluciones nuevas o importar a otra ruta y comparar).
Compatible con Python 3.9, sin dependencias (lee el .docx con zipfile).
"""
import argparse
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

PD = "POR_DEFINIR"
DASH = r"[—–-]"
STOP = {"de", "del", "la", "el", "los", "las", "y", "e", "en", "por", "para", "a", "con", "rrhh"}


def norm(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t.lower().replace(" ", " ")).strip()


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", norm(t)).strip("-")


def tokens(t):
    return {w for w in slugify(t).split("-") if w and w not in STOP}


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _texto(nodo):
    """Texto de un nodo w:p / w:tc: ignora lo borrado con control de cambios (w:del, también autocerrado) y
    convierte tabuladores y saltos en espacio."""
    partes = []

    def rec(n):
        for ch in n:
            if ch.tag == W + "del":
                continue
            if ch.tag == W + "t":
                partes.append(ch.text or "")
            elif ch.tag in (W + "tab", W + "br", W + "cr"):
                partes.append(" ")
            elif ch.tag == W + "noBreakHyphen":
                partes.append("-")
            else:
                rec(ch)
                if ch.tag == W + "p":
                    partes.append(" ")

    rec(nodo)
    return re.sub(r"\s+", " ", "".join(partes).replace("\u00a0", " ")).strip()


def _bloques(nodo):
    """Párrafos y tablas del cuerpo, en orden, incluso dentro de controles de contenido (w:sdt) o inserciones."""
    for ch in nodo:
        if ch.tag in (W + "p", W + "tbl"):
            yield ch
        elif ch.tag in (W + "sdt", W + "sdtContent", W + "ins", W + "customXml", W + "smartTag"):
            for x in _bloques(ch):
                yield x


def leer_eventos(docx):
    """Lista ordenada de ('p', texto) y ('fila', [celdas])."""
    try:
        z = zipfile.ZipFile(docx)
        raiz = ET.fromstring(z.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as e:
        sys.exit("ERROR: %s no es un .docx legible (%s)" % (docx, e))
    body = raiz.find(W + "body")
    eventos = []
    for b in _bloques(body if body is not None else raiz):
        if b.tag == W + "tbl":
            for tr in b.findall(W + "tr"):
                celdas = [_texto(tc) for tc in tr.findall(W + "tc")]
                if any(celdas):
                    eventos.append(("fila", celdas))
        else:
            t = _texto(b)
            if t:
                eventos.append(("p", t))
    return eventos


def acortar(texto, maximo=64):
    """Propuesta de nombre corto: primera cláusula del texto del insumo, sin cortar a media frase."""
    t = texto.strip()
    if len(t) > maximo:
        t = re.split(r":| con la | con el | que | con ", t)[0]
    t = t.strip(" ,;.")
    if len(t) > maximo:
        t = t[:maximo].rsplit(" ", 1)[0]
    while t.count("(") > t.count(")") and "(" in t:
        t = t[:t.rindex("(")].rstrip(" ,;")
    palabras = t.split()
    while len(palabras) > 2 and palabras[-1].lower() in ("de", "del", "la", "el", "los", "las", "para", "con", "y", "o", "en", "por", "a", "al"):
        palabras.pop()
    t = " ".join(palabras).strip(" ,;.")
    return t[:1].upper() + t[1:]


def resolver_carril(tag, carriles):
    """Carril al que se refiere el texto «tag» de la tabla de frentes: igualdad exacta, luego contención, luego id."""
    for criterio in (lambda c: norm(c["nombre"]) == tag,
                     lambda c: tag in norm(c["nombre"]) or norm(c["nombre"]) in tag,
                     lambda c: c["id"] in tag):
        cand = [c for c in carriles if criterio(c)]
        if len(cand) == 1:
            return cand[0]
        if len(cand) > 1:
            return None
    return None


def primer_numero(texto):
    m = re.search(r"\d+", texto or "")
    return int(m.group(0)) if m else None


def horas_fila(sol):
    return sol["h"] if "h" in sol else sol["C"] + sol["T"] + sol["A"]


def main():
    ap = argparse.ArgumentParser(description="Borrador de datos.json desde el docx de insumo de Habilidades")
    ap.add_argument("docx")
    ap.add_argument("--nombre", default=PD)
    ap.add_argument("--slug", default=PD)
    ap.add_argument("--codigo", default=PD)
    ap.add_argument("--salida")
    ap.add_argument("--forzar", action="store_true", help="sobrescribe --salida si ya existe")
    a = ap.parse_args()

    if not Path(a.docx).exists():
        sys.exit("ERROR: no existe %s" % a.docx)
    if a.salida and Path(a.salida).exists() and not a.forzar:
        sys.exit("✗ %s ya existe: usa --forzar para sobrescribirlo (se perdería el trabajo manual) o --salida otra ruta." % a.salida)

    ev = leer_eventos(a.docx)
    id_re = re.compile(r"^[A-Z][A-Z0-9]{1,5}-\d+[a-z]?$")
    carril_re = re.compile(r"^Carril (.+?)\s+" + DASH + r"\s+(\d+) soluciones?(?:,| y)\s+(\d+) horas?$", re.I)
    area_re = re.compile(r"^(.+?)\s+" + DASH + r"\s+(\d+) h(?:oras)?$", re.I)
    frente_re = re.compile(r"^Frente ([A-Z]) · (.+)$")

    avisos = []
    carriles, areas, frentes = [], [], []
    declarado_carril, declarado_area = {}, {}
    ids_carril, ids_area = set(), set()
    carril_act = area_act = None
    filas_con_id = 0
    texto_total = " ".join(e[1] if e[0] == "p" else " ".join(e[1]) for e in ev)

    for tipo, v in ev:
        if tipo == "p":
            m = carril_re.match(v)
            if m:
                nombre = m.group(1).strip()
                palabras = [w for w in nombre.split() if norm(w) not in ("microsoft", "365", "de", "team", "en")]
                base = slugify(palabras[0] if palabras else nombre) or "carril"
                cid, n = base, 2
                while cid in ids_carril:
                    cid = "%s%d" % (base, n)
                    n += 1
                if cid != base:
                    avisos.append("carril «%s»: id repetido, se usó «%s»" % (nombre, cid))
                ids_carril.add(cid)
                carril_act = {"id": cid.replace("-", "_"), "nombre": nombre, "nombre_corto": nombre, "color": "amarillo" if not carriles else "naranja"}
                carriles.append(carril_act)
                declarado_carril[carril_act["id"]] = (int(m.group(2)), int(m.group(3)))
                area_act = None
                continue
            if norm(v).startswith("carril ") and len(v) < 140:
                avisos.append("encabezado «%s» parece un carril pero no coincide con «Carril <herramienta> — N soluciones, M horas»: sus áreas no se asignarán a él" % v[:80])
            m = area_re.match(v)
            if m and not carril_act and not norm(v).startswith("total"):
                avisos.append("«%s» parece un área pero aparece antes de cualquier carril reconocido: se ignoró" % v[:60])
            if m and carril_act and not norm(v).startswith("total"):
                nombre = m.group(1).strip()
                base_flag = False
                if norm(nombre).startswith("proceso base"):
                    base_flag = True
                    nombre = re.sub(r"^Proceso base\s*" + DASH + r"\s*", "", nombre, flags=re.I)
                    nombre = nombre[:1].upper() + nombre[1:]
                area_act = {"id": None, "nombre": nombre, "carril": carril_act["id"], "frente": PD, "para_que": PD, "soluciones": []}
                if base_flag:
                    area_act["proceso_base"] = True
                areas.append(area_act)
                declarado_area[len(areas) - 1] = int(m.group(2))
            continue
        # fila de tabla
        c = v
        if c and id_re.match(c[0]):
            filas_con_id += 1
            if area_act is None:
                avisos.append("fila %s fuera de un área reconocida: se ignoró" % c[0])
                continue
            if len(c) < 7:
                avisos.append("fila %s con %d celdas (se esperaban 7: id, solución, C, T, A, total, fase): se ignoró" % (c[0], len(c)))
                continue
            rid, texto, cc, tt, ai, tot, fase = [x.strip() for x in c[:7]]
            sol = {"id": rid, "entregable": acortar(texto), "_revisar": True, "detalle": texto}
            if cc.isdigit() and tt.isdigit() and ai.isdigit():
                sol.update({"C": int(cc), "T": int(tt), "A": int(ai)})
                if tot.isdigit() and int(tot) != int(cc) + int(tt) + int(ai):
                    avisos.append("solución %s: el total declarado (%s) no coincide con C+T+A (%d)" % (rid, tot, int(cc) + int(tt) + int(ai)))
            elif tot.isdigit():
                sol["h"] = int(tot)
                avisos.append("solución %s: C/T/A vacías o no numéricas (C=%r, T=%r, A=%r): se usó solo el total (%s h)" % (rid, cc, tt, ai, tot))
            else:
                avisos.append("solución %s: sin horas legibles (C=%r, T=%r, A=%r, total=%r)" % (rid, cc, tt, ai, tot))
                continue
            sol["fase"] = fase
            area_act["soluciones"].append(sol)
            if area_act["id"] is None:
                base = re.sub(r"[^A-Za-z0-9]", "", rid.split("-")[0])
                aid, n = base, 2
                while aid in ids_area:
                    aid = "%s%d" % (base, n)
                    n += 1
                if aid != base:
                    avisos.append("área «%s»: el prefijo %s ya existía, id «%s»" % (area_act["nombre"], base, aid))
                ids_area.add(aid)
                area_act["id"] = aid
            continue
        m = frente_re.match(c[0]) if c else None
        if m and len(c) >= 2:
            tag = norm(m.group(2))
            cand = resolver_carril(tag, carriles)
            if cand is None:
                avisos.append("frente %s: no se pudo asociar «%s» a un carril; asignarlo a mano" % (m.group(1), m.group(2)))
            frentes.append({"id": m.group(1), "carril": cand["id"] if cand else PD, "nombre": PD,
                            "_alcance_fuente": c[1] if len(c) > 1 else "", "_horas_fuente": (c[2] if len(c) > 2 else ""), "celdas": {}})

    # Asignar frente por coincidencia de NOMBRE COMPLETO (tokens), no por primera palabra
    for ar in areas:
        if not ar["soluciones"]:
            avisos.append("área «%s» sin soluciones reconocidas" % ar["nombre"])
        candidatos = []
        for fr in frentes:
            if fr["carril"] != ar["carril"]:
                continue
            partes = [p.strip() for p in re.split(r",|;|\sy\s", fr["_alcance_fuente"]) if p.strip()]
            if any(tokens(ar["nombre"]) == tokens(p) or tokens(p) <= tokens(ar["nombre"]) and tokens(p) for p in partes):
                candidatos.append(fr)
        if len(candidatos) == 1:
            ar["frente"] = candidatos[0]["id"]
        elif len(candidatos) > 1:
            avisos.append("área «%s»: coincide con varios frentes (%s); asignar a mano" % (ar["nombre"], ", ".join(f["id"] for f in candidatos)))

    if not carriles or not any(x["soluciones"] for x in areas):
        print("✗ No se reconoció ningún carril o ninguna solución. Formato esperado: encabezados «Carril <herramienta> — N soluciones, M horas»,")
        print("  «<Área> — N h» y tablas con filas «ID | Solución | C | T | A | Total | Fase». Revisa el docx o el formato de los guiones.")
        sys.exit(1)

    # Validaciones cruzadas
    n_import = sum(len(x["soluciones"]) for x in areas)
    if filas_con_id != n_import:
        avisos.append("cobertura: el docx tiene %d filas con id y se importaron %d" % (filas_con_id, n_import))
    for idx, ar in enumerate(areas):
        h = sum(horas_fila(s) for s in ar["soluciones"])
        if idx in declarado_area and declarado_area[idx] != h:
            avisos.append("área «%s»: el docx declara %d h y la suma de sus filas es %d h" % (ar["nombre"], declarado_area[idx], h))
    for c in carriles:
        n = sum(len(x["soluciones"]) for x in areas if x["carril"] == c["id"])
        h = sum(horas_fila(s) for x in areas if x["carril"] == c["id"] for s in x["soluciones"])
        dn, dh = declarado_carril.get(c["id"], (None, None))
        if (dn, dh) != (n, h):
            avisos.append("carril «%s»: el docx declara %s soluciones / %s h y la suma es %d / %d" % (c["nombre"], dn, dh, n, h))
    for fr in frentes:
        h = sum(horas_fila(s) for x in areas if x["frente"] == fr["id"] for s in x["soluciones"])
        dec = primer_numero(fr["_horas_fuente"])
        if dec is not None and dec != h:
            avisos.append("frente %s: el docx declara %s h y las áreas asignadas suman %d h (revisar la asignación de áreas)" % (fr["id"], dec, h))
    sin_frente = [x["nombre"] for x in areas if x["frente"] == PD]
    if sin_frente:
        avisos.append("áreas sin frente asignado (completar a mano): " + ", ".join(sin_frente))
    if not frentes:
        avisos.append("no se encontró la tabla «Resumen de horas» con filas «Frente X · …»: definir los frentes a mano")

    m = (re.search(r"tope de (\d+)\s*(?:h|horas)?\s*(?:de sesi[oó]n\s*)?(?:por|a la|/)\s*semana", texto_total, re.I)
         or re.search(r"(?:hasta|m[aá]ximo de)\s+(\d+)\s*(?:h|horas)\s*(?:de sesi[oó]n\s*)?(?:por|a la|/)\s*semana", texto_total, re.I))
    supuestos = []
    if m:
        supuestos.append("El insumo fija un tope de %s h de trabajo por semana: referencia interna para el kickoff; la propuesta no lo muestra (v3)." % m.group(1))
    m = re.search(r"toma (\d+) semanas de trabajo|durante (\d+) semanas de trabajo|(\d+) semanas de trabajo", texto_total)
    if m:
        supuestos.append("El insumo habla de %s semanas de trabajo: la propuesta no lleva semanas ni sesiones (Keiber, 2026-10-08); el calendario se acuerda en el kickoff." % next(g for g in m.groups() if g))

    fases_usadas = sorted({s["fase"] for ar in areas for s in ar["soluciones"]})
    fases = []
    for f in fases_usadas:
        if f == "F0":
            fases.append({"id": "F0", "descripcion": PD})
        else:
            fases.append({"id": f, "titulo": "Fase " + f[1:], "descripcion": PD})
    d = {
        "version": 3,
        "cliente": {"nombre": a.nombre, "slug": a.slug, "codigo": a.codigo},
        "division": PD,
        "alianza": "POR_DEFINIR",
        "eje": PD,
        "origen": PD,
        "fuente_insumo": Path(a.docx).name,
        "portada": {"titulo_lineas": [PD, PD], "titulo_destacado": PD, "lead": PD,
                    "hechos": [{"num": PD, "texto": PD, "resuelto_por": []} for _ in range(3)], "fuente": PD},
        "carriles": carriles,
        "areas": areas,
        "alcance": {"subtitulo": PD, "fuera_alcance": [PD]},
        "metodo": {"quien_construye": PD, "practica": [{"titulo": PD, "texto": PD}], "datos": PD},
        "fases": fases,
        "frentes": [{k: v for k, v in fr.items() if not k.startswith("_")} for fr in frentes],
        "ruta": {"hitos": [{"titulo": PD, "texto": PD} for _ in range(4)]},
        "logistica": {"modalidad": PD, "participantes": PD, "arranque": PD},
        "seguimiento": {"rango": "30, 60 y 90 días", "texto": "Desde el cierre de cada área",
                        "items": [{"dias": "30 días", "texto": PD}, {"dias": "60 días", "texto": PD}, {"dias": "90 días", "texto": PD}]},
        "entregables": {"transversales": [PD], "valor_inmediato": [PD]},
        "proximos_pasos": {"asesora": {"nombre": PD, "correo": PD}},
        "supuestos": supuestos, "pendientes": []}
    # Referencias de la fuente para el humano que completa (el generador las ignora: empiezan con _)
    for fr, orig in zip(d["frentes"], frentes):
        fr["_alcance_fuente"] = orig["_alcance_fuente"]
        fr["_horas_fuente"] = orig["_horas_fuente"]
    for fr in d["frentes"]:
        for f in fases_usadas:
            if f != "F0":
                fr["celdas"][f] = PD
    txt = json.dumps(d, ensure_ascii=False, indent=1)
    out = sys.stdout if a.salida else sys.stderr  # sin --salida el JSON va a stdout y el estado a stderr
    print("Importado: %d carril(es), %d área(s), %d solución(es), %d frente(s)." % (len(carriles), len(areas), n_import, len(frentes)), file=out)
    for v in avisos:
        print("⚠ " + v, file=out)
    if a.salida:
        salida = Path(a.salida)
        salida.parent.mkdir(parents=True, exist_ok=True)
        tmp = salida.with_name(salida.name + ".tmp")
        tmp.write_text(txt + "\n", encoding="utf8")
        tmp.replace(salida)
        print("✓ Borrador escrito en %s. Completar todos los POR_DEFINIR y revisar los nombres de entregable (_revisar)." % salida)
    else:
        print(txt)
    if any(x.startswith(("cobertura", "área «", "carril «", "frente ")) and "declara" in x for x in avisos):
        print("⚠ Hay diferencias contra las horas que declara el docx: no continuar sin resolverlas.", file=out)


if __name__ == "__main__":
    main()
