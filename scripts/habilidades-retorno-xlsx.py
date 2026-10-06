#!/usr/bin/env python3
"""
habilidades-retorno-xlsx.py — Hoja de captura del retorno esperado y su lectura hacia datos.json.

Parte de la plantilla compacta de Habilidades (plantillas/habilidades-compacto.md §7). Cierra el circuito de datos de la
slide opcional «Retorno esperado» en modo «cifras»:

    datos.json ──crear──► retorno-captura.xlsx ──(las personas completan las celdas azules)──► leer ──► datos.json["retorno"]

  crear <slug | datos.json> [--salida ruta.xlsx] [--forzar]
      Genera la hoja: Léame, Parámetros, Retorno por proceso (una fila por solución), Resumen por área (fórmulas) y Dotación y
      nómina, más una pestaña oculta _control (código del cliente y huella de los ids de solución). Celdas azules = datos a
      completar; grises = fórmulas. Con --forzar mueve la hoja anterior a retorno-captura.AAAAMMDD-HHMMSS.xlsx.
  leer <retorno-captura.xlsx> --datos <slug | datos.json> --origen "documento; fecha; validado por" --nota "..."
        [--posiciones --aval "quién; fecha; medio"] [--quitar-destino] [--forzar]
      Lee SOLO las celdas de entrada (recalcula aquí; no depende de que Excel haya guardado los resultados), valida todo y escribe
      el bloque retorno (modo «cifras») en datos.json. NO inventa ni adivina:
        · una celda con contenido no interpretable (texto, fórmula sin valor guardado, separador de miles ambiguo, nan, inf) es un
          ERROR con su coordenada, nunca una celda vacía ni un 0;
        · un id de solución repetido con datos es un ERROR;
        · una solución sin tiempo actual, ejecuciones y tiempo con la solución no cuenta; un área con cobertura parcial se rotula
          «(n de m procesos)» y se marca estimación;
        · la hoja debe corresponder a ese datos.json (código y huella de ids);
        · el resultado se valida con el generador ANTES de escribir (si falla, no se toca datos.json).
      Guarda copia datos.json.AAAAMMDD-HHMMSS.bak (byte a byte) y escribe de forma atómica.

Reglas del sistema que respeta: nada de cifras inventadas (§4.9); las estimaciones se indican como tales; la slide no cita
estudios ni referencias de la web; posiciones y nómina solo con aval registrado.

Requiere openpyxl (pip install openpyxl; en un entorno virtual aparte si el Python del sistema no lo trae).
Compatible con Python 3.9.
"""
import argparse
import datetime
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path

try:
    from openpyxl import Workbook, load_workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:  # pragma: no cover
    sys.exit("ERROR: falta openpyxl. Instalarlo en un entorno aparte: python3 -m venv ~/.venv-propuestas && ~/.venv-propuestas/bin/pip install openpyxl")

ROOT = Path(__file__).resolve().parent.parent
PROPUESTAS = ROOT / "clientes" / "propuestas"
GENERADOR = ROOT / "scripts" / "generar-habilidades-compacto.py"

AZUL = PatternFill("solid", fgColor="DDEBF7")
GRIS = PatternFill("solid", fgColor="D9D9D9")
AMAR = PatternFill("solid", fgColor="FFF2CC")
APOYO = PatternFill("solid", fgColor="F7F7F7")  # celda de apoyo: se llena pero no alimenta el deck
NEG = Font(bold=True)
BORDE = Border(*(Side(style="thin", color="BFBFBF"),) * 4)
WRAP = Alignment(wrap_text=True, vertical="top")


def norm(t):
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", t.lower()).strip()


_TIPOS_BRUTO = {"medido": "medido", "declarado por el área": "declarado", "estimación conservadora": "estimacion",
                "declarado": "declarado", "estimacion": "estimacion", "estimación": "estimacion"}
TIPOS = dict((norm(k), v) for k, v in _TIPOS_BRUTO.items())

# Encabezados de «Retorno por proceso» (el lector los busca por texto; no cambiarlos sin cambiar leer)
H_ID = "ID"
H_TACT, H_EJEC, H_TCON = "Tiempo actual por ejecución (h)", "Ejecuciones al mes", "Tiempo con la solución por ejecución (h)"
H_RETR, H_TARD, H_TIPO = "Retrabajo y errores (USD/mes)", "Pagos o cobros tardíos (USD/mes)", "Tipo de dato"
ENC_PROC = ["Área", "Carril", "Frente", "ID", "Solución / proceso (resumen)", "Horas de sesión (Intezia)", "Fase",
            "Volumen mensual (apoyo)", "Unidad del volumen (apoyo)", "Qué se sabe hoy (apoyo)", "Fuente (apoyo)",
            H_TACT, H_EJEC, "Horas actuales al mes", H_TCON, "Horas con la solución al mes", "Horas recuperadas al mes",
            "Valor de las horas recuperadas (USD/mes)", H_RETR, H_TARD, "Retorno mensual (USD)", H_TIPO,
            "Meta a 30 días (apoyo)", "Meta a 60 días (apoyo)", "Meta a 90 días (apoyo)", "Observación (apoyo)"]
COLS_ENTRADA = (12, 13, 15, 19, 20, 22)       # alimentan el deck
COLS_APOYO = (8, 9, 10, 11, 23, 24, 25, 26)   # se llenan pero NO alimentan el deck
H_D_AREA, H_D_PERS = "Área", "Personas hoy en el área"
H_D_HOY = "Posiciones que representa hoy el trabajo manual"
H_D_RED = "Posiciones que se reducen con las soluciones"
H_D_EVI = "Posiciones que no hará falta contratar"
H_D_ID = "ID área"
ENC_DOT = ["Área", H_D_PERS + " (apoyo)", "Equivalencia: personas que haría falta para procesar la data a mano (apoyo)", "Fuente de la equivalencia (apoyo)",
           H_D_HOY, H_D_RED, H_D_EVI, "Costo anual por posición (escala salarial, USD)", "Costo anual de las posiciones reducidas (USD)",
           "Costo anual de las contrataciones evitadas (USD)", "Total anual (USD)", H_TIPO, "Observación (apoyo)", H_D_ID]
TS = lambda: datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


def limpio(t):
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", t) if isinstance(t, str) else t


def poner(ws, fila, col, valor):
    """Escribe texto sin que Excel lo interprete como fórmula y sin caracteres de control."""
    c = ws.cell(row=fila, column=col, value=limpio(valor))
    if isinstance(valor, str) and valor[:1] in "=+-@":
        c.data_type = "s"
    return c


def cargar_datos(arg):
    p = Path(arg)
    if not p.suffix:
        p = PROPUESTAS / arg / "datos.json"
    if not p.exists():
        sys.exit("ERROR: no existe %s" % p)
    dup = []

    def sin_dup(pares):
        vistos = set()
        for k, _ in pares:
            if k in vistos:
                dup.append(k)
            vistos.add(k)
        return dict(pares)

    try:
        d = json.loads(p.read_text(encoding="utf-8-sig"), object_pairs_hook=sin_dup)
    except UnicodeDecodeError:
        sys.exit("ERROR: %s no está en UTF-8" % p)
    except ValueError as e:
        sys.exit("ERROR: %s no es JSON válido: %s" % (p, e))
    if not isinstance(d, dict):
        sys.exit("ERROR: %s debe ser un objeto { }" % p)
    if dup:
        sys.exit("ERROR: %s tiene claves repetidas en el mismo objeto (%s): corregir antes de seguir (JSON se quedaría con la última)." % (p, ", ".join(sorted(set(dup)))))
    for a in d.get("areas") or []:
        if not isinstance(a, dict) or not a.get("id"):
            sys.exit("ERROR: hay un área sin «id» en %s" % p)
        for s in a.get("soluciones") or []:
            if not isinstance(s, dict) or not s.get("id"):
                sys.exit("ERROR: el área %s tiene una solución sin «id»" % a["id"])
    return p.resolve(), d


def nombre_area(a):
    n = a.get("nombre_catalogo") or a.get("nombre") or a.get("id")
    if a.get("proceso_base") and "proceso base" not in n.lower():
        n += " (proceso base)"
    return n


def huella(d):
    ids = sorted(s["id"] for a in d.get("areas") or [] for s in a.get("soluciones") or [])
    return hashlib.sha1("|".join(ids).encode("utf8")).hexdigest()[:12]


def crear(args):
    ruta, d = cargar_datos(args.datos)
    salida = Path(args.salida) if args.salida else ruta.parent / "retorno-captura.xlsx"
    if not salida.parent.exists():
        sys.exit("ERROR: la carpeta de salida %s no existe" % salida.parent)
    if salida.exists():
        if not args.forzar:
            sys.exit("✗ %s ya existe: usa --forzar para reemplazarlo (la anterior se conserva con fecha y hora)." % salida)
        ant = salida.with_name("%s.%s%s" % (salida.stem, TS(), salida.suffix))
        shutil.move(str(salida), str(ant))
        print("(la hoja anterior quedó en %s)" % ant)
    carriles = dict((c.get("id"), c.get("nombre_corto") or c.get("nombre")) for c in d.get("carriles") or [])
    filas = []
    for a in d.get("areas") or []:
        for s in a.get("soluciones") or []:
            h = s.get("h")
            if h is None:
                h = (s.get("C") or 0) + (s.get("T") or 0) + (s.get("A") or 0)
            filas.append((nombre_area(a), carriles.get(a.get("carril"), a.get("carril")), a.get("frente"), s["id"], s.get("entregable") or "", h, s.get("fase"), a["id"]))
    if not filas:
        sys.exit("ERROR: datos.json no tiene soluciones")
    cliente = (d.get("cliente") or {}).get("nombre", "")
    wb = Workbook()
    ws = wb.active
    ws.title = "Léame"
    ws.column_dimensions["A"].width = 125
    lineas = [
        ("HOJA DE CAPTURA · RETORNO ESPERADO · %s (interna, no se entrega al cliente)" % cliente, True),
        ("", False),
        ("Para qué sirve: reunir por área y proceso el volumen, el tiempo actual y el tiempo con la solución, el dinero y la dotación que alimentan la slide «Retorno esperado» (modo cifras).", False),
        ("Colores: AZUL = dato que alimenta el deck (en «Retorno por proceso»: tiempo actual por ejecución, ejecuciones al mes, tiempo con la solución, retrabajo, pagos o cobros tardíos y tipo de dato; en «Dotación y nómina»: posiciones, costo y tipo de dato). BLANCO/GRIS MUY CLARO con «(apoyo)» = contexto que se anota pero NO llega al deck. GRIS = fórmula.", False),
        ("Escribir los números sin separador de miles ni unidades: 1200 o 0,5 (no «1.200», «12 h» ni «30 %»). Las horas van en horas decimales (30 minutos = 0,5). Una celda con texto no numérico o fórmula sin valor guardado detiene la lectura.", False),
        ("Regla de oro: no se completa nada por intuición. Sin dato, la celda queda vacía y esa solución no cuenta. Las estimaciones se marcan «Estimación conservadora» y la slide las rotula como tales. «Horas con la solución» es siempre una meta.", True),
        ("No repetir ni cambiar los ID de solución (la hoja se liga al datos.json por código del cliente y huella de ids).", False),
        ("Cierre del circuito: python3 scripts/habilidades-retorno-xlsx.py leer retorno-captura.xlsx --datos <slug> --origen \"documento; fecha; validado por\" --nota \"...\" [--posiciones --aval \"quién; fecha; medio\"]", False),
    ]
    for i, (t, b) in enumerate(lineas, 1):
        c = ws.cell(row=i, column=1, value=t)
        c.alignment = WRAP
        if b:
            c.font = NEG
    wp = wb.create_sheet("Parámetros")
    wp.column_dimensions["A"].width = 58
    wp.column_dimensions["B"].width = 22
    wp.column_dimensions["C"].width = 70
    wp.append(["Parámetro", "Valor", "Cómo se obtiene / quién lo valida"])
    for c in wp[1]:
        c.font, c.fill, c.border = NEG, AMAR, BORDE
    wp.append(["Costo hora de referencia (USD por hora)", None, "Se valida con el cliente. Sin este dato no se calcula el valor de las horas recuperadas."])
    wp.append(["Horas productivas por posición al mes", None, "Convierte horas recuperadas en posiciones equivalentes y concilia las posiciones planteadas. Validar con Recursos Humanos del cliente (no se asume)."])
    for r in (2, 3):
        wp.cell(row=r, column=2).fill = AZUL
        for col in (1, 2, 3):
            wp.cell(row=r, column=col).border = BORDE
            wp.cell(row=r, column=col).alignment = WRAP
    COSTO, HPOS = "Parámetros!$B$2", "Parámetros!$B$3"

    wr = wb.create_sheet("Retorno por proceso")
    wr.append(ENC_PROC)
    for c in wr[1]:
        c.font, c.fill, c.border, c.alignment = NEG, AMAR, BORDE, Alignment(wrap_text=True, vertical="center")
    wr.row_dimensions[1].height = 62
    for i, (area, carril, frente, sid, corto, horas, fase, _aid) in enumerate(filas, start=2):
        for j, v in enumerate([area, carril, frente, sid, corto, horas, fase], start=1):
            poner(wr, i, j, v)
        for col, f in ((14, f'=IF(AND(ISNUMBER(L{i}),ISNUMBER(M{i})),L{i}*M{i},"")'), (16, f'=IF(AND(ISNUMBER(O{i}),ISNUMBER(M{i})),O{i}*M{i},"")'),
                       (17, f'=IF(AND(ISNUMBER(N{i}),ISNUMBER(P{i})),N{i}-P{i},"")'), (18, f'=IF(AND(ISNUMBER(Q{i}),ISNUMBER({COSTO})),Q{i}*{COSTO},"")'),
                       (21, f'=IF(COUNT(R{i}:T{i})=0,"",SUM(R{i}:T{i}))')):
            wr.cell(row=i, column=col, value=f).fill = GRIS
        for col in COLS_ENTRADA:
            wr.cell(row=i, column=col).fill = AZUL
        for col in COLS_APOYO:
            wr.cell(row=i, column=col).fill = APOYO
        for col in range(1, len(ENC_PROC) + 1):
            wr.cell(row=i, column=col).border = BORDE
            wr.cell(row=i, column=col).alignment = WRAP
    last = 1 + len(filas)
    dv = DataValidation(type="list", formula1='"Medido,Declarado por el área,Estimación conservadora"', allow_blank=True, showErrorMessage=True,
                        errorTitle="Tipo de dato", error="Elegir de la lista: Medido, Declarado por el área o Estimación conservadora.")
    wr.add_data_validation(dv)
    dv.add("V2:V%d" % last)
    dvn = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True, showErrorMessage=True,
                         errorTitle="Número", error="Escribir un número >= 0 sin separador de miles ni unidades (horas decimales: 30 min = 0,5).")
    wr.add_data_validation(dvn)
    for col in ("L", "M", "O", "S", "T"):
        dvn.add("%s2:%s%d" % (col, col, last))
    for i, w in enumerate([24, 11, 7, 7, 46, 11, 6, 13, 16, 40, 30, 13, 12, 13, 14, 13, 13, 16, 14, 14, 14, 22, 14, 12, 12, 30], 1):
        wr.column_dimensions[get_column_letter(i)].width = w
    wr.freeze_panes = "F2"

    areas = []
    for f in filas:
        if f[0] not in [a[0] for a in areas]:
            areas.append((f[0], f[7]))
    wa = wb.create_sheet("Resumen por área")
    enc2 = ["Área", "Soluciones", "Horas actuales al mes", "Horas con la solución al mes", "Horas recuperadas al mes", "Valor de las horas (USD/mes)",
            "Retrabajo y errores (USD/mes)", "Pagos o cobros tardíos (USD/mes)", "Retorno mensual (USD)", "Retorno anual (USD)",
            "Posiciones equivalentes a las horas recuperadas"]
    wa.append(enc2)
    for c in wa[1]:
        c.font, c.fill, c.border, c.alignment = NEG, AMAR, BORDE, Alignment(wrap_text=True, vertical="center")
    wa.row_dimensions[1].height = 48
    R = "'Retorno por proceso'!"
    for i, (a, _aid) in enumerate(areas, start=2):
        sm = lambda col: f"=SUMIFS({R}${col}$2:${col}${last},{R}$A$2:$A${last},$A{i})"
        poner(wa, i, 1, a)
        for col, v in enumerate([f"=COUNTIFS({R}$A$2:$A${last},$A{i})", sm("N"), sm("P"), sm("Q"), sm("R"), sm("S"), sm("T"), sm("U"),
                                 f'=IF(I{i}=0,"",I{i}*12)', f'=IF(AND(ISNUMBER(E{i}),ISNUMBER({HPOS}),{HPOS}>0),E{i}/{HPOS},"")'], start=2):
            wa.cell(row=i, column=col, value=v).fill = GRIS
        for col in range(1, len(enc2) + 1):
            wa.cell(row=i, column=col).border = BORDE
    wa.column_dimensions["A"].width = 38
    for i in range(2, len(enc2) + 1):
        wa.column_dimensions[get_column_letter(i)].width = 16

    wd = wb.create_sheet("Dotación y nómina")
    wd.append(ENC_DOT)
    for c in wd[1]:
        c.font, c.fill, c.border, c.alignment = NEG, AMAR, BORDE, Alignment(wrap_text=True, vertical="center")
    wd.row_dimensions[1].height = 62
    for i, (a, aid) in enumerate(areas, start=2):
        poner(wd, i, 1, a)
        wd.cell(row=i, column=14, value=aid)
        for col, v in ((9, f'=IF(AND(ISNUMBER(F{i}),ISNUMBER(H{i})),F{i}*H{i},"")'), (10, f'=IF(AND(ISNUMBER(G{i}),ISNUMBER(H{i})),G{i}*H{i},"")'),
                       (11, f'=IF(COUNT(I{i}:J{i})=0,"",SUM(I{i}:J{i}))')):
            wd.cell(row=i, column=col, value=v).fill = GRIS
        for col in (5, 6, 7, 8, 12):
            wd.cell(row=i, column=col).fill = AZUL
        for col in (2, 3, 4, 13):
            wd.cell(row=i, column=col).fill = APOYO
        for col in range(1, len(ENC_DOT) + 1):
            wd.cell(row=i, column=col).border = BORDE
            wd.cell(row=i, column=col).alignment = WRAP
    dv2 = DataValidation(type="list", formula1='"Medido,Declarado por el área,Estimación conservadora"', allow_blank=True, showErrorMessage=True,
                         errorTitle="Tipo de dato", error="Elegir de la lista: Medido, Declarado por el área o Estimación conservadora.")
    wd.add_data_validation(dv2)
    dv2.add("L2:L%d" % (1 + len(areas)))
    for i, w in enumerate([34, 12, 22, 40, 18, 18, 18, 20, 18, 18, 16, 22, 50, 10], 1):
        wd.column_dimensions[get_column_letter(i)].width = w
    wd.freeze_panes = "B2"

    wc = wb.create_sheet("_control")
    wc.append(["codigo", (d.get("cliente") or {}).get("codigo", "")])
    wc.append(["cliente", cliente])
    wc.append(["huella_ids", huella(d)])
    wc.append(["creada", datetime.datetime.now().isoformat(timespec="seconds")])
    wc.sheet_state = "hidden"
    tmp = salida.with_name(salida.name + ".tmp")
    wb.save(str(tmp))
    os.replace(str(tmp), str(salida))
    print("✓ Hoja creada: %s (%d soluciones, %d áreas)" % (salida, len(filas), len(areas)))


# ----------------------------------------------------------------------------------------------
# Lectura
# ----------------------------------------------------------------------------------------------
RE_NUM = re.compile(r"^[+-]?\d+(?:[.,]\d+)?$")
RE_MILES = re.compile(r"^[+-]?\d{1,3}(?:[.,]\d{3})+(?:[.,]\d+)?$")


def fmt_n(x):
    return ("%d" % x) if abs(x - round(x)) < 1e-9 else ("%.1f" % x).replace(".", ",")


def num_celda(v, cache, ref):
    """(número | None, problema | None). Vacío -> (None, None). Contenido no interpretable -> problema (nunca vacío ni 0)."""
    if v is None or (isinstance(v, str) and not v.strip()):
        return None, None
    if isinstance(v, bool):
        return None, "%s: valor lógico, se esperaba un número" % ref
    if isinstance(v, (int, float)):
        if not math.isfinite(v):
            return None, "%s: número no finito" % ref
        return float(v), None
    if isinstance(v, datetime.datetime):
        return None, "%s: fecha y hora, se esperaba un número de horas" % ref
    if isinstance(v, datetime.time):
        return v.hour + v.minute / 60.0 + v.second / 3600.0, None
    if isinstance(v, datetime.timedelta):
        return v.total_seconds() / 3600.0, None
    if isinstance(v, str):
        t = v.strip()
        if t.startswith("="):
            if isinstance(cache, (int, float)) and not isinstance(cache, bool) and math.isfinite(cache):
                return float(cache), None
            return None, "%s: fórmula «%s» sin valor guardado (abrir la hoja en Excel y guardarla, o escribir el número)" % (ref, t[:30])
        if RE_MILES.match(t) and not t.lstrip("+-").startswith("0"):
            return None, "%s: «%s» tiene un separador de miles o decimal ambiguo: escribir 1200 o 1200,5" % (ref, t)
        if RE_NUM.match(t):
            return float(t.replace(",", ".")), None
        return None, "%s: «%s» no es un número (sin unidades ni texto: 0,5 y no «30 min»)" % (ref, t[:30])
    return None, "%s: tipo de celda no soportado (%s)" % (ref, type(v).__name__)


def partir(txt, claves, opcion):
    partes = [x.strip() for x in str(txt).split(";")]
    if len(partes) != len(claves) or not all(partes):
        sys.exit("✗ %s debe traer %d partes separadas por «;»: %s" % (opcion, len(claves), "; ".join(claves)))
    return dict(zip(claves, partes))


def leer(args):
    ruta, d = cargar_datos(args.datos)
    xlsx = Path(args.xlsx)
    if not xlsx.exists():
        sys.exit("ERROR: no existe %s" % xlsx)
    try:
        wb = load_workbook(str(xlsx), data_only=False)
        wbv = load_workbook(str(xlsx), data_only=True)
    except (zipfile.BadZipFile, KeyError, OSError, ValueError) as e:
        sys.exit("ERROR: %s no es un .xlsx legible (%s)" % (xlsx, e))
    except Exception as e:  # InvalidFileException y similares
        sys.exit("ERROR: %s no se pudo abrir como hoja de captura (%s: %s)" % (xlsx, type(e).__name__, e))
    for hoja in ("Parámetros", "Retorno por proceso"):
        if hoja not in wb.sheetnames:
            sys.exit("ERROR: falta la pestaña «%s» (¿es la hoja generada por «crear»?)" % hoja)
    avisos, errores = [], []

    def terminar(msg=None):
        for v in avisos:
            print("⚠ " + v)
        for v in errores[:40]:
            print("✗ " + v)
        if len(errores) > 40:
            print("✗ ... y %d error(es) más" % (len(errores) - 40))
        if msg:
            print(msg)
        sys.exit(1)

    # --- firma de la hoja
    if "_control" in wb.sheetnames:
        ctl = dict((str(r[0].value), r[1].value) for r in wb["_control"].iter_rows(min_row=1, max_col=2) if r[0].value)
        cod = (d.get("cliente") or {}).get("codigo", "")
        if ctl.get("codigo") != cod or ctl.get("huella_ids") != huella(d):
            sys.exit("✗ La hoja no corresponde a este datos.json (código %r / huella %r en la hoja; %r / %r en datos.json). Regenerar la hoja con «crear» o usar el datos.json con el que se creó."
                     % (ctl.get("codigo"), ctl.get("huella_ids"), cod, huella(d)))
    else:
        avisos.append("la hoja no trae la pestaña _control (se creó con una versión anterior): no se pudo comprobar que corresponda a este datos.json")

    # --- parámetros (por etiqueta de la columna A)
    wp, wpv = wb["Parámetros"], wbv["Parámetros"]
    par = {}
    for r in range(2, wp.max_row + 1):
        et = norm(wp.cell(row=r, column=1).value)
        if et:
            v, pr = num_celda(wp.cell(row=r, column=2).value, wpv.cell(row=r, column=2).value, "Parámetros!B%d" % r)
            if pr:
                errores.append(pr)
            par[et] = v
    costo = next((v for k, v in par.items() if k.startswith("costo hora")), None)
    hpos = next((v for k, v in par.items() if k.startswith("horas productivas")), None)

    # --- retorno por proceso
    ws, wsv = wb["Retorno por proceso"], wbv["Retorno por proceso"]
    enc = [c.value for c in ws[1]]

    def col(h):
        if h not in enc:
            sys.exit("ERROR: no se encontró la columna «%s» en «Retorno por proceso». No cambiar los encabezados de la hoja." % h)
        return enc.index(h) + 1
    cID, cTA, cEJ, cTC, cRT, cTD, cTP = (col(h) for h in (H_ID, H_TACT, H_EJEC, H_TCON, H_RETR, H_TARD, H_TIPO))
    sol_area, area_nombre, area_total = {}, {}, {}
    for a in d.get("areas") or []:
        area_nombre[a["id"]] = a.get("nombre") or a["id"]
        area_total[a["id"]] = len(a.get("soluciones") or [])
        for s in a.get("soluciones") or []:
            sol_area[s["id"]] = a["id"]
    acum, vistos, desconocidos = {}, {}, []
    for r in range(2, ws.max_row + 1):
        sid = ws.cell(row=r, column=cID).value
        if sid is None or str(sid).strip() == "":
            continue
        sid = str(sid).strip()
        ref = lambda c, r=r: "Retorno por proceso!%s%d" % (get_column_letter(c), r)
        vals = {}
        for nombre, c in (("ta", cTA), ("ej", cEJ), ("tc", cTC), ("rt", cRT), ("td", cTD)):
            v, pr = num_celda(ws.cell(row=r, column=c).value, wsv.cell(row=r, column=c).value, ref(c))
            if pr:
                errores.append("%s (solución %s)" % (pr, sid))
            elif v is not None and v < 0:
                errores.append("%s: valor negativo (%s) en la solución %s" % (ref(c), fmt_n(v), sid))
            vals[nombre] = v
        tipo_raw = ws.cell(row=r, column=cTP).value
        tiene_datos = any(vals[k] is not None for k in ("ta", "ej", "tc", "rt", "td"))
        if sid not in sol_area:
            if tiene_datos:
                desconocidos.append("%s (fila %d)" % (sid, r))
            continue
        if tiene_datos:
            if sid in vistos:
                errores.append("el id %s aparece repetido con datos en las filas %d y %d: dejar una sola fila por solución" % (sid, vistos[sid], r))
                continue
            vistos[sid] = r
        completa = vals["ta"] is not None and vals["ej"] is not None and vals["tc"] is not None
        if tiene_datos and not completa and any(vals[k] is not None for k in ("ta", "ej", "tc")):
            faltan = [n for n, k in (("tiempo actual", "ta"), ("ejecuciones", "ej"), ("tiempo con la solución", "tc")) if vals[k] is None]
            avisos.append("solución %s (fila %d): faltan %s; la fila no cuenta" % (sid, r, ", ".join(faltan)))
        if not completa:
            if vals["rt"] or vals["td"]:
                avisos.append("solución %s (fila %d): hay monto de retrabajo o pagos tardíos (%s) pero faltan los tiempos; el monto no entra en la tabla" % (sid, r, fmt_n((vals["rt"] or 0) + (vals["td"] or 0))))
            continue
        ta, ej, tc = vals["ta"], vals["ej"], vals["tc"]
        if ta < 0 or ej < 0 or tc < 0 or (vals["rt"] or 0) < 0 or (vals["td"] or 0) < 0:
            continue  # ya reportado como error
        if ej == 0:
            avisos.append("solución %s (fila %d): ejecuciones al mes = 0; la fila no cuenta" % (sid, r))
            continue
        if tc > ta:
            errores.append("%s: el tiempo con la solución (%s) supera al tiempo actual (%s) en la solución %s" % (ref(cTC), fmt_n(tc), fmt_n(ta), sid))
            continue
        tipo = TIPOS.get(norm(tipo_raw)) if tipo_raw else None
        if tipo is None:
            avisos.append("solución %s (fila %d): sin «Tipo de dato» válido; se trata como estimación" % (sid, r))
            tipo = "estimacion"
        a = acum.setdefault(sol_area[sid], {"ha": 0.0, "hc": 0.0, "retr": 0.0, "tard": 0.0, "n": 0, "tipos": set()})
        a["ha"] += ta * ej
        a["hc"] += tc * ej
        a["retr"] += vals["rt"] or 0.0
        a["tard"] += vals["td"] or 0.0
        a["n"] += 1
        a["tipos"].add(tipo)
    if desconocidos:
        avisos.append("filas con datos cuyo id no existe en datos.json (se ignoraron): %s" % ", ".join(desconocidos[:10]))
    if not acum and not errores:
        terminar("✗ La hoja no tiene ninguna solución con tiempo actual, ejecuciones y tiempo con la solución. No hay nada que llevar a datos.json "
                 "(las fichas de levantamiento suelen decir «No declarado»: completar primero la hoja).")
    if costo is None or costo <= 0:
        errores.append("falta el costo hora de referencia en Parámetros (USD > 0, validado con el cliente)")
    if args.posiciones and (hpos is None or hpos <= 0):
        errores.append("con --posiciones falta «Horas productivas por posición al mes» en Parámetros (> 0, validadas con el cliente)")

    # --- dotación y nómina (solo con --posiciones)
    dot = {}
    if args.posiciones:
        if "Dotación y nómina" not in wb.sheetnames:
            sys.exit("ERROR: --posiciones pide la pestaña «Dotación y nómina»")
        wd, wdv = wb["Dotación y nómina"], wbv["Dotación y nómina"]
        encd = [c.value for c in wd[1]]

        def idx(prefijo, obligatorio=True):
            for i, h in enumerate(encd, 1):
                if str(h or "").startswith(prefijo):
                    return i
            if obligatorio:
                sys.exit("ERROR: no se encontró la columna «%s…» en «Dotación y nómina»" % prefijo)
            return None
        cdA, cdH, cdR, cdE, cdC, cdT = idx(H_D_AREA), idx(H_D_HOY), idx(H_D_RED), idx(H_D_EVI), idx("Costo anual por posición"), idx(H_TIPO)
        cdI = idx(H_D_ID, False)
        nombres_n = {}
        for a in d.get("areas") or []:
            for n in (nombre_area(a), a.get("nombre"), a.get("nombre_catalogo")):
                if n:
                    nombres_n[re.sub(r"\s*\(proceso base\)", "", norm(n))] = a["id"]
        for r in range(2, wd.max_row + 1):
            nombre = wd.cell(row=r, column=cdA).value
            if not nombre:
                continue
            aid = wd.cell(row=r, column=cdI).value if cdI else None
            if aid not in area_nombre:
                aid = nombres_n.get(re.sub(r"\s*\(proceso base\)", "", norm(nombre)))
            if aid is None:
                avisos.append("dotación: el área «%s» no coincide con ningún área de datos.json (fila %d)" % (nombre, r))
                continue
            vals = {}
            for k, c in (("hoy", cdH), ("red", cdR), ("evi", cdE), ("cst", cdC)):
                v, pr = num_celda(wd.cell(row=r, column=c).value, wdv.cell(row=r, column=c).value, "Dotación y nómina!%s%d" % (get_column_letter(c), r))
                if pr:
                    errores.append(pr)
                elif v is not None and v < 0:
                    errores.append("Dotación y nómina!%s%d: valor negativo" % (get_column_letter(c), r))
                vals[k] = v
            if vals["hoy"] is None or vals["cst"] is None or (vals["red"] is None and vals["evi"] is None):
                if any(v is not None for v in vals.values()):
                    avisos.append("dotación del área %s: datos incompletos (hacen falta posiciones hoy, costo anual por posición y al menos reducen o evitan); se omite" % aid)
                continue
            tp = wd.cell(row=r, column=cdT).value
            tipo_p = TIPOS.get(norm(tp)) if tp else None
            if tipo_p is None:
                avisos.append("dotación del área %s: sin «Tipo de dato» válido; las posiciones se rotulan como estimación" % aid)
                tipo_p = "estimacion"
            red, evi = vals["red"] or 0.0, vals["evi"] or 0.0
            if red > vals["hoy"]:
                errores.append("dotación del área %s: se reducen %s posiciones y hoy el trabajo manual equivale a %s" % (aid, fmt_n(red), fmt_n(vals["hoy"])))
            dot[aid] = (vals["hoy"], red, evi, (red + evi) * vals["cst"], tipo_p)

    # --- origen, aval y nota
    ret_prev = d.get("retorno") if isinstance(d.get("retorno"), dict) else {}
    origen = None
    if args.origen:
        origen = partir(args.origen, ("documento", "fecha", "validado_por"), "--origen")
    elif isinstance(ret_prev.get("origen_datos"), dict):
        origen = ret_prev["origen_datos"]
        print("(se reutiliza el origen de datos anterior: %s; %s; %s)" % (origen.get("documento"), origen.get("fecha"), origen.get("validado_por")))
    else:
        errores.append("falta --origen \"documento; fecha; validado por\" (procedencia verificable de las cifras)")
    aval = None
    if args.posiciones:
        if args.aval:
            aval = partir(args.aval, ("quien", "fecha", "medio"), "--aval")
        elif isinstance(ret_prev.get("aval_posiciones"), dict):
            aval = ret_prev["aval_posiciones"]
            print("(se reutiliza el aval de posiciones anterior: %s; %s; %s)" % (aval.get("quien"), aval.get("fecha"), aval.get("medio")))
        else:
            errores.append("con --posiciones falta --aval \"quién; fecha; medio\" (quién del cliente aceptó plantear la reducción o evitar contrataciones)")
    nota = ""
    if args.nota:
        nota = args.nota
    elif args.reusar_nota and ret_prev.get("nota_datos"):
        nota = ret_prev["nota_datos"]
        print("(se reutiliza la nota de datos anterior: «%s»)" % nota)
    else:
        errores.append("falta --nota \"...\" (de dónde salen las cifras y cuáles son estimaciones); con --reusar-nota se conserva la anterior")
    if nota and len(nota) < 30:
        errores.append("la nota de datos es muy corta (%d caracteres; mínimo 30)" % len(nota))
    if errores:
        terminar("✗ No se escribió nada: corregir los errores de arriba.")

    # --- áreas de salida
    areas_out = []
    prev_areas = dict((x.get("area"), x) for x in (ret_prev.get("areas") or []) if isinstance(x, dict))
    sin_dato = []
    for a in d.get("areas") or []:
        acc = acum.get(a["id"])
        if not acc:
            sin_dato.append("%s (0 de %d)" % (a["id"], area_total[a["id"]]))
            continue
        tot = area_total[a["id"]]
        tipos = acc["tipos"]
        tipo = "estimacion" if "estimacion" in tipos else ("declarado" if "declarado" in tipos else "medido")
        fila = {"area": a["id"], "tipo_dato": tipo, "horas_actuales": round(acc["ha"], 2), "horas_con_solucion": round(acc["hc"], 2)}
        if acc["retr"]:
            fila["retrabajo_usd"] = round(acc["retr"], 2)
        if acc["tard"]:
            fila["tardios_usd"] = round(acc["tard"], 2)
        if acc["n"] < tot:
            fila["etiqueta"] = "%s (%d de %d procesos)" % (area_nombre[a["id"]], acc["n"], tot)
            if tipo == "medido":
                fila["tipo_dato"] = "estimacion"
            sin_dato.append("%s (%d de %d)" % (a["id"], acc["n"], tot))
            avisos.append("área %s: datos en %d de %d procesos; la fila se rotula con la cobertura y se marca estimación" % (a["id"], acc["n"], tot))
        elif prev_areas.get(a["id"], {}).get("etiqueta"):
            fila["etiqueta"] = prev_areas[a["id"]]["etiqueta"]  # se conserva la etiqueta manual
        if args.posiciones:
            dd = dot.get(a["id"])
            if dd is None:
                avisos.append("área %s: sin datos de dotación; se omite de la tabla con posiciones" % a["id"])
                continue
            fila["posiciones_hoy"], fila["posiciones_reducibles"], fila["costo_anual_usd"] = round(dd[0], 2), round(dd[1], 2), round(dd[3], 2)
            if dd[2]:
                fila["posiciones_evitables"] = round(dd[2], 2)
            fila["tipo_dato_posiciones"] = dd[4]
            if acc["n"] < tot:
                avisos.append("área %s: las horas son de %d de %d procesos pero las posiciones y el costo anual son de toda el área" % (a["id"], acc["n"], tot))
            if hpos and fila["horas_actuales"] > 0:
                eq = (fila["horas_actuales"] - fila["horas_con_solucion"]) / hpos
                if eq > 0 and dd[1] + dd[2] > eq * 1.25:
                    avisos.append("área %s: se plantean %s posiciones a reducir o evitar y las horas recuperadas equivalen a %.1f (a %s h por posición)" % (a["id"], fmt_n(dd[1] + dd[2]), eq, fmt_n(hpos)))
        areas_out.append(fila)
    if not areas_out:
        terminar("✗ Ningún área quedó con datos completos para la tabla.")

    if ret_prev.get("modo") == "cifras" and not args.forzar:
        sys.exit("✗ datos.json ya tiene un retorno en modo cifras: usa --forzar para reemplazarlo (se guarda copia con fecha y hora).")
    ret = dict(ret_prev)
    ret["modo"] = "cifras"
    ret["costo_hora_usd"] = costo
    ret["areas"] = areas_out
    ret["posiciones"] = bool(args.posiciones)
    ret["nota_datos"] = nota
    ret["origen_datos"] = origen
    if args.posiciones:
        ret["horas_por_posicion"] = hpos
        ret["aval_posiciones"] = aval
    else:
        ret.pop("horas_por_posicion", None)
        ret.pop("aval_posiciones", None)
    ret.pop("_horas_por_posicion", None)
    if args.quitar_destino:
        ret.pop("destino", None)
    nuevo = dict(d)
    nuevo["retorno"] = ret
    sup = [x for x in (nuevo.get("supuestos") or []) if not str(x).startswith(("Retorno en modo método", "Retorno en modo cifras"))]
    sup.append("Retorno en modo cifras: datos de «%s» (%s), validados por %s; las filas marcadas (estimación) se confirman con la línea base de la semana 1." % (origen["documento"], origen["fecha"], origen["validado_por"]))
    nuevo["supuestos"] = sup

    # --- validar con el generador ANTES de escribir
    texto = json.dumps(nuevo, ensure_ascii=False, indent=1) + "\n"
    with tempfile.TemporaryDirectory() as td:
        tmpj = Path(td) / "datos.json"
        tmpj.write_text(texto, encoding="utf8")
        pr = subprocess.run([sys.executable, str(GENERADOR), "--datos", str(tmpj), "--solo-validar"], capture_output=True, text=True)
    sal = [l for l in (pr.stdout + pr.stderr).splitlines() if l[:1] in "✗⚠"]
    for l in sal:
        if l.startswith("⚠") and any(x in l for x in ("retorno", "areas[")):
            avisos.append(l[2:])
    if pr.returncode != 0:
        for v in avisos:
            print("⚠ " + v)
        print("✗ El resultado no pasa la validación del generador; no se tocó datos.json:")
        for l in sal:
            if l.startswith("✗"):
                print("  " + l)
        sys.exit(1)
    bak = ruta.with_name("%s.%s.bak" % (ruta.name, TS()))
    shutil.copy2(str(ruta), str(bak))
    tmp = ruta.with_name(ruta.name + ".tmp")
    tmp.write_text(texto, encoding="utf8")
    os.replace(str(tmp), str(ruta))
    for v in avisos:
        print("⚠ " + v)
    print("✓ %s actualizado: %d de %d áreas en modo cifras (copia en %s)." % (ruta, len(areas_out), len(d.get("areas") or []), bak.name))
    if sin_dato:
        print("  Cobertura incompleta o sin datos: " + ", ".join(sin_dato))
    print("  Siguiente: python3 scripts/generar-habilidades-compacto.py <slug>")


def main():
    ap = argparse.ArgumentParser(description="Hoja de captura del retorno esperado (Habilidades compacto)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("crear", help="genera retorno-captura.xlsx desde datos.json")
    c.add_argument("datos", help="slug de clientes/propuestas/<slug> o ruta a datos.json")
    c.add_argument("--salida")
    c.add_argument("--forzar", action="store_true")
    c.set_defaults(fn=crear)
    l = sub.add_parser("leer", help="lleva la hoja completada a datos.json (retorno, modo cifras)")
    l.add_argument("xlsx")
    l.add_argument("--datos", required=True, help="slug o ruta a datos.json")
    l.add_argument("--origen", help="procedencia de las cifras: \"documento o sesión; fecha; quién del cliente las validó\"")
    l.add_argument("--nota", help="nota bajo la tabla: de dónde salen las cifras y cuáles son estimaciones")
    l.add_argument("--reusar-nota", action="store_true", help="conserva la nota de datos anterior (se imprime)")
    l.add_argument("--posiciones", action="store_true", help="incluye posiciones y costo anual (solo si el cliente avala plantearlo)")
    l.add_argument("--aval", help="aval de posiciones: \"quién; fecha; medio\"")
    l.add_argument("--quitar-destino", action="store_true", help="elimina retorno.destino (en modo cifras la franja no se muestra)")
    l.add_argument("--forzar", action="store_true", help="reemplaza un retorno que ya está en modo cifras")
    l.set_defaults(fn=leer)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
