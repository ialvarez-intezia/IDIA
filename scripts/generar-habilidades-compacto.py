#!/usr/bin/env python3
"""
generar-habilidades-compacto.py — Genera la propuesta compacta de Habilidades (5 slides) desde datos.json.

Plantilla genérica nacida de clientes/propuestas/dusa-cai035 (CAI-035, 2026-10-04). Especificación
completa: plantillas/habilidades-compacto.md. Esquema de datos: plantillas/habilidades-compacto-canonico/
datos.plantilla.json (anotado) y datos.ejemplo-dusa.json (instancia real).

Qué hace
  1. Lee clientes/propuestas/<slug>/datos.json (o --datos).
  2. VALIDA: tipos, estructura, ids únicos, horas, sumas, cobertura, dolor de portada dentro del alcance,
     marcadores de AcroForm, guiones largos, fechas calendario, siglas, **negrita**/{tokens} sin resolver y
     capacidad estimada de cada caja. Errores = no escribe nada.
  3. CALCULA todas las cifras (soluciones, áreas, horas por área/frente/fase/celda, totales). Ninguna cifra
     se escribe a mano: se usan tokens {n_total}, {h_f1}, {n_areas_txt}... dentro de los textos.
  4. ESCRIBE en la carpeta de salida: index.html, habilidades-compacto.css (copia congelada), overrides.css
     (stub vacío, solo si no existe), acroforms.json, programa.md (siempre regenerado), meta.json (se
     actualiza sin tocar estado ni fecha_entrega) y brief.md (se crea una vez; su bloque automático se refresca).

Uso
    python3 scripts/generar-habilidades-compacto.py <slug>
    python3 scripts/generar-habilidades-compacto.py <slug> --solo-validar
    python3 scripts/generar-habilidades-compacto.py --datos ruta/datos.json --salida /tmp/prueba
Opciones: --forzar-brief · --forzar-overrides · --actualizar-css (refresca la copia del CSS)
          --medir (corre verificar-habilidades-compacto.js al terminar) · --depurar (muestra el traceback)
          --borrador (escribe aunque haya errores de validación no estructurales; para depurar)

Después: bash scripts/pdf-habilidades-compacto.sh <slug>   (verifica, genera el PDF y ajusta los campos).
Compatible con Python 3.9 (sin dependencias externas).
"""
import argparse
import difflib
import html as _html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANTILLA = ROOT / "plantillas" / "habilidades-compacto-canonico"
PROPUESTAS = ROOT / "clientes" / "propuestas"

try:  # métricas exactas del horneado de campos (requiere pypdf); sin él se usa un estimador
    sys.path.insert(0, str(ROOT / "scripts"))
    from acroform_appearance import (_wrap as _wrap_pdf, _WIDTHS_BOLD as _WB, _DEFAULT_W_BOLD as _DWB,
                                     _WIDTHS_REGULAR as _WR, _DEFAULT_W_REGULAR as _DWR)
    PDF_EXACTO = True
except Exception:  # noqa
    PDF_EXACTO = False

# Cajas multilínea del PDF: (ancho pt, tamaño pt, negrita, líneas máximas). Ver customize-habilidades-compacto.py y
# agregar-campo-precio.py (Programa/Notas 360×79 pt a 11 pt; Entregables/Acreditacion 337,1×51 pt a 10,5 pt en negrita).
CAJAS_PDF = {
    "Entregables": (337.125, 10.5, True, 4), "Acreditacion": (337.125, 10.5, True, 4),
    "Programa": (360.0, 11.0, False, 6), "Notas": (360.0, 11.0, False, 6),
}

CSS_NAME = "habilidades-compacto.css"
VERSION_PLANTILLA = "1.3 (2026-10-05)"

DIVISIONES = {
    "educacion": ("Educación", "educacion"),
    "fundacion": ("Fundación", "fundacion"),
}
COLORES = {"amarillo": "acc-y", "naranja": "acc-o"}
FASES_VALIDAS = ("F0", "F1", "F2", "F3")

# Frases que agregar-campo-precio.py usa para ubicar cada grupo de campos AcroForm por página.
MARCA_PRECIO = "propuesta económica"
MARCA_BENEF = "lo que se llevan"
MARCAS_PROHIBIDAS = ("cómo arrancamos", "inversión por fases", "inversión por permanencia")

SIGLAS_OK = {"TOTAL", "IA", "USD", "CV", "RRHH", "S", "TI", "PDF", "SEO", "API", "VPN", "IVA", "ISLR", "CAI", "TA", "CU", "DIP", "CH", "DET", "INN", "ALL"}
PALABRAS_FRENTES = {1: "Un frente", 2: "Dos frentes en paralelo", 3: "Tres frentes en paralelo"}
MESES = r"(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)"
# Fechas reales: dd/mm[/aaaa] con día 1-31 y mes 1-12, aaaa-mm-dd, dd-mm-aaaa (año de 4 cifras), «12 de marzo», o un nombre de mes.
# No debe casar con «30-60-90» (marco de seguimiento) ni con «24/7».
RE_FECHA = re.compile(
    r"\b(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[0-2])/\d{2,4}\b|\b(0?[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])\b(?!/)|\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b|"
    r"\b(0?[1-9]|[12]\d|3[01])-(0?[1-9]|1[0-2])-\d{4}\b|\b\d{1,2}\s+(de\s+)?" + MESES + r"\b|\b" + MESES + r"\b",
    re.I,
)
RE_GUION_LARGO = re.compile("[\u2014\u2015\u2012\u2212\u2E3A\u2E3B]|-{2,}")
# El guion mediano solo se tolera entre dos cifras (rangos como 10–15); «S1–S11» o «A – B» no.
RE_GUION_MEDIO = re.compile("(?<!\\d)\u2013|\u2013(?!\\d)")
RE_PLACEHOLDER = re.compile(r"por[_ \-]?definir|\bTBD\b|lorem ipsum|\bx{3,}\b|^\s*(?:\.{3}|…)\s*$|(?-i:\bTODO(?:[:_\-]|\s*$))", re.I)

# Titular de portada: frase-objetivo estilo título de tesis. (máx. de caracteres del titular completo, px del h1, caracteres por línea)
FONT_TITULO = ((44, 64, 25), (60, 54, 30), (82, 46, 35), (9999, 42, 38))
RE_RET_ERR = re.compile(
    r"https?:|www\.|\.(?:com|org|net|edu|gov)\b|\bgarantiz\w*|\bgarant[ií]a de retorno\b|\bbenchmark\b|\breferente del sector\b"
    r"|\bseg[uú]n un (?:estudio|informe|an[aá]lisis)\b|\binformes? (?:de|del) (?-i:[A-ZÁÉÍÓÚ])\w+|\binvestigaci[oó]n(?:es)? (?:de|del|publicada)\b"
    r"|\bestudios? (?:de(?! tiempos)|del|realizado|publicado|cient[ií]fic\w*|acad[eé]mic\w*)\b", re.I)
RE_RET_AV = re.compile(r"\bestudios?\b|\bweb\b|\binternet\b|\d[\d.,]*\s?%|(?:USD|US\$|\$)\s?\d")
RE_PROHIBIDO_RETORNO = RE_RET_ERR  # alias de compatibilidad
TIPOS_DATO = {"medido": "medido", "declarado": "declarado por el área", "estimacion": "estimación"}

PASOS_BASE = [
    ("Volumen mensual", "Cuántas veces se ejecuta el proceso al mes, por ejemplo solicitudes, registros o reportes."),
    ("Tiempo actual por ejecución", "Se mide en la semana 1 con el líder de cada área y es la **línea base**."),
    ("Tiempo con la solución", "Horas por ejecución una vez que la solución está adoptada."),
    ("Horas recuperadas al mes", "Volumen mensual multiplicado por la diferencia entre el tiempo actual y el tiempo con la solución."),
]
PASO_DINERO = ("Valor en dinero", "Horas recuperadas multiplicadas por el costo hora de referencia, más el costo del retrabajo, de los errores y de los pagos o cobros tardíos, cuando exista el dato.")
PASO_CAPACIDAD = ("Capacidad liberada", "Las horas recuperadas se expresan en capacidad para la misión: más beneficiarios atendidos y menos tiempo en tareas administrativas.")
PASO_POSICIONES = ("Posiciones y costo anual", "Horas recuperadas divididas entre las horas productivas de una posición: cuántas se reducen o no será necesario contratar, con su costo anual según las escalas de {cliente_corto}.")
METAS_BASE = [("30 días", "Soluciones en uso real y línea base validada con el líder de cada área."),
              ("60 días", "Horas recuperadas medidas contra la línea base, por área y por proceso.")]
META90 = {(False, True): "Medición del retorno en dinero y en posiciones, con el costo anual de cada una.",
          (False, False): "Medición del retorno en dinero, con el valor de las horas recuperadas de cada área.",
          (True, True): "Medición del retorno en dinero y en posiciones, con el costo anual de cada una.",
          (True, False): "Horas recuperadas y capacidad liberada para la misión, por área."}
DESTINO_EDU = [
    ("Mismo equipo, más volumen", "Si el tiempo se libera, el mismo equipo puede **procesar más trabajo** sin contratar más personal."),
    ("Trabajo reenfocado", "Si el tiempo se libera, el equipo puede dedicarlo a validar resultados, analizar información y tomar decisiones."),
    ("Otras áreas y líneas de negocio", "Con el retorno medido, {cliente_corto} decide si lleva este mismo ciclo de construir, probar y adoptar a **otras áreas y líneas de negocio**."),
]
DESTINO_FUND = [
    ("Mismo equipo, más alcance", "Si el tiempo se libera, el mismo equipo puede **atender a más personas** sin ampliar la plantilla."),
    ("Trabajo reenfocado", "Si el tiempo se libera, el equipo puede dedicarlo a revisar resultados, preparar informes y estar más cerca de los beneficiarios."),
    ("Otros programas y áreas", "Con el retorno medido, {cliente_corto} decide si lleva este mismo ciclo de construir, probar y adoptar a **otros programas y áreas**."),
]

SUB_ENTREGABLES = "Lo que se llevan: **{n_entregables_txt}**, uno por cada solución construida, probada y adoptada, más el seguimiento a {rango_seguimiento} que mide su efecto."

# ----------------------------------------------------------------------------------------------
# Esquema de tipos (valida antes de calcular: evita tracebacks por datos mal formados)
# ----------------------------------------------------------------------------------------------
ESQUEMAS = {
    "raiz": {"version": "int", "cliente": "dict:cliente", "division": "str", "alianza": "bool", "eje": "str", "origen": "str",
             "fuente_insumo": "str", "portada": "dict:portada", "carriles": "list:dict:carril", "areas": "list:dict:area",
             "alcance": "dict:alcance", "fases": "list:dict:fase", "frentes": "list:dict:frente", "ruta": "dict:ruta",
             "seguimiento": "dict:seguimiento", "inversion": "dict:inversion", "entregables": "dict:entregables",
             "retorno": "dict:retorno", "siglas_ok": "list:str", "supuestos": "list:str", "pendientes": "list:str"},
    "cliente": {"nombre": "str", "slug": "str", "codigo": "str", "nombre_pie": "str"},
    "portada": {"eyebrow": "str", "titulo_lineas": "list:str", "titulo_linea1": "str", "titulo_destacado": "str", "lead": "str",
                "hechos": "list:dict:hecho", "fuente": "str"},
    "hecho": {"num": "str", "texto": "str", "resuelto_por": "list:str"},
    "carril": {"id": "str", "nombre": "str", "nombre_corto": "str", "color": "str"},
    "area": {"id": "str", "nombre": "str", "carril": "str", "frente": "str", "nombre_frente": "str", "nombre_catalogo": "str",
             "proceso_base": "bool", "soluciones": "list:dict:solucion"},
    "solucion": {"id": "str", "entregable": "str", "C": "num", "T": "num", "A": "num", "h": "num", "fase": "str",
                 "detalle": "str", "_revisar": "bool"},
    "alcance": {"titulo": "str", "subtitulo": "str", "pasos": "list:str", "quien_construye": "str", "fuera_alcance": "list:str",
                "compacto": "bool", "etiqueta_proceso_base": "str", "etiqueta_pasos": "str", "etiqueta_quien": "str",
                "etiqueta_fuera": "str"},
    "fase": {"id": "str", "titulo": "str", "rango": "str", "descripcion": "str", "destacada": "bool"},
    "frente": {"id": "str", "carril": "str", "semanas": "str", "celdas": "dict:str", "areas_html": "str"},
    "ruta": {"semanas_total": "int", "tope_h_semana": "int", "hitos": "list:dict:hito", "titulo": "str", "subtitulo": "str", "nota": "str"},
    "hito": {"titulo": "str", "texto": "str"},
    "seguimiento": {"rango": "str", "texto": "str", "items": "list:dict:item", "etiqueta": "str"},
    "item": {"dias": "str", "texto": "str"},
    "inversion": {"notas": "list:str", "licencias": "dict:licencias", "titulo": "str", "duracion": "str", "programa": "list:str",
                  "garantia_texto": "str"},
    "licencias": {"titulo": "str", "tarjetas": "list:dict:tarjeta", "nota": "str"},
    "tarjeta": {"nombre": "str", "color": "str", "texto": "str"},
    "retorno": {"modo": "str", "titulo": "str", "subtitulo": "str", "posiciones": "bool", "pasos": "list:dict:paso_retorno",
                "etiqueta_pasos": "str", "metas": "list:dict:meta_retorno", "etiqueta_metas": "str", "destino": "list:dict:destino_retorno",
                "etiqueta_destino": "str", "gancho": "str", "semana_medicion": "int", "costo_hora_usd": "num",
                "areas": "list:dict:retorno_area", "nota_datos": "str", "origen_datos": "dict:origen_datos",
                "horas_por_posicion": "num", "aval_posiciones": "dict:aval_posiciones"},
    "origen_datos": {"documento": "str", "fecha": "str", "validado_por": "str"},
    "aval_posiciones": {"quien": "str", "fecha": "str", "medio": "str"},
    "paso_retorno": {"titulo": "str", "texto": "str"},
    "meta_retorno": {"dias": "str", "texto": "str"},
    "destino_retorno": {"rotulo": "str", "texto": "str"},
    "retorno_area": {"area": "str", "etiqueta": "str", "tipo_dato": "str", "tipo_dato_posiciones": "str", "posiciones_evitables": "num", "horas_actuales": "num", "horas_con_solucion": "num", "retrabajo_usd": "num",
                     "tardios_usd": "num", "posiciones_hoy": "num", "posiciones_reducibles": "num", "costo_anual_usd": "num"},
    "entregables": {"transversales": "list:str", "valor_inmediato": "list:str", "compacto": "bool", "columnas_por_carril": "list:int",
                    "titulo": "str", "subtitulo": "str", "etiqueta_transversales": "str", "etiqueta_valor": "str"},
}


class Reporte:
    def __init__(self):
        self.errores = []
        self.avisos = []

    def err(self, donde, msg):
        self.errores.append("%s: %s" % (donde, msg))

    def aviso(self, donde, msg):
        self.avisos.append("%s: %s" % (donde, msg))


class Ctx:
    pass


ESTADO = {"rep": None}  # reporte en curso (para mostrar lo acumulado si hay un error interno)


# ----------------------------------------------------------------------------------------------
# Utilidades de texto
# ----------------------------------------------------------------------------------------------
def esc(t):
    return _html.escape(t, quote=False)


def sin_marcado(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", t)


def md(t):
    """Escapa HTML y convierte **x** en <strong>x</strong>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", esc(t))


def cm(t):
    """Texto seguro dentro de un comentario HTML (sin «--» ni «<», «>»)."""
    return re.sub(r"-{2,}", "-", str(t)).replace("<", "(").replace(">", ")").replace("\n", " ")


def cel(t):
    """Texto seguro dentro de una celda de tabla Markdown."""
    return re.sub(r"\s+", " ", str(t)).replace("|", "/")


def plural(n, uno, varios):
    return uno if n == 1 else varios


def lineas_wrap(texto, cpl):
    """Líneas estimadas con corte por palabras a `cpl` caracteres por línea."""
    cpl = max(8, int(cpl))
    n, ancho = 1, 0
    for w in texto.split():
        l = len(w)
        if ancho == 0:
            ancho = l
        elif ancho + 1 + l <= cpl:
            ancho += 1 + l
        else:
            n += 1
            ancho = l
    return n


class Tokens:
    PAT = re.compile(r"\{\s*([^{}\s]+)\s*\}")

    def __init__(self, ctx, rep):
        self.ctx = ctx
        self.rep = rep
        self.vistos = set()

    def __call__(self, texto, donde):
        if not isinstance(texto, str):
            return texto

        def r(m):
            k = m.group(1)
            if k in self.ctx:
                return str(self.ctx[k])
            if (donde, k) not in self.vistos:
                self.vistos.add((donde, k))
                self.rep.err(donde, "token desconocido {%s} (usar minúsculas; ver la lista de tokens en plantillas/habilidades-compacto.md §5)" % k)
            return m.group(0)

        return self.PAT.sub(r, texto)


# ----------------------------------------------------------------------------------------------
# Validación de tipos
# ----------------------------------------------------------------------------------------------
def _tipo_ok(v, kind):
    if kind == "str":
        return isinstance(v, str)
    if kind == "int":
        return isinstance(v, int) and not isinstance(v, bool)
    if kind == "num":
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    if kind == "bool":
        return isinstance(v, bool)
    return True


_NOMBRE_TIPO = {"str": "texto", "int": "un entero", "num": "un número de horas", "bool": "true/false"}


def chequear_tipos(nodo, esquema, ruta, rep):
    """Valida tipos recursivamente según ESQUEMAS. Avisa de claves desconocidas (con sugerencia)."""
    if not isinstance(nodo, dict):
        rep.err(ruta or "datos.json", "debe ser un objeto { }")
        return
    spec = ESQUEMAS[esquema]
    for k, v in nodo.items():
        if str(k).startswith("_ayuda") or (str(k).startswith("_") and k not in spec):
            continue
        donde = "%s.%s" % (ruta, k) if ruta else k
        if k not in spec:
            sug = difflib.get_close_matches(k, list(spec), n=1)
            rep.aviso(donde, "clave desconocida (se ignora)%s" % (" ¿quisiste decir '%s'?" % sug[0] if sug else ""))
            continue
        kind = spec[k]
        if isinstance(v, str) and RE_PLACEHOLDER.search(v):
            continue  # lo reporta buscar_pendientes
        if v is None:
            rep.err(donde, "no puede ser null (borrar la clave si es opcional)")
            continue
        if kind.startswith("dict:"):
            sub = kind.split(":", 1)[1]
            if sub == "str":
                if not isinstance(v, dict):
                    rep.err(donde, "debe ser un objeto { }, recibido %s" % type(v).__name__)
                else:
                    for kk, vv in v.items():
                        if not isinstance(vv, str):
                            rep.err("%s.%s" % (donde, kk), "debe ser texto, recibido %s" % type(vv).__name__)
            else:
                chequear_tipos(v, sub, donde, rep)
        elif kind.startswith("list:"):
            if not isinstance(v, list):
                rep.err(donde, "debe ser una lista [ ], recibido %s" % type(v).__name__)
                continue
            partes = kind.split(":")
            for i, x in enumerate(v):
                if partes[1] == "dict":
                    chequear_tipos(x, partes[2], "%s[%d]" % (donde, i), rep)
                elif isinstance(x, str) and RE_PLACEHOLDER.search(x):
                    continue
                elif not _tipo_ok(x, partes[1]):
                    rep.err("%s[%d]" % (donde, i), "debe ser %s, recibido %s" % (_NOMBRE_TIPO.get(partes[1], partes[1]), type(x).__name__))
                elif partes[1] == "str" and not x.strip():
                    rep.err("%s[%d]" % (donde, i), "no puede estar vacío")
        else:
            if not _tipo_ok(v, kind):
                rep.err(donde, "debe ser %s, recibido %s (%r)" % (_NOMBRE_TIPO.get(kind, kind), type(v).__name__, v))
            elif kind == "str" and not v.strip() and k != "nombre_pie":
                rep.err(donde, "no puede estar vacío (borrar la clave si es opcional)")


def buscar_pendientes(nodo, ruta, acum, saltar=()):
    """Reúne las rutas con POR_DEFINIR o textos de ayuda «(opcional ...» sin completar."""
    if isinstance(nodo, dict):
        for k, v in nodo.items():
            if str(k).startswith(("_ayuda", "_ejemplo")) or k in saltar:
                continue
            buscar_pendientes(v, ruta + ("." if ruta else "") + str(k), acum)
    elif isinstance(nodo, list):
        for i, v in enumerate(nodo):
            buscar_pendientes(v, "%s[%d]" % (ruta, i), acum)
    elif isinstance(nodo, str):
        try:
            nodo.encode("utf8")
        except UnicodeEncodeError:
            acum.append((ruta, "contiene un carácter no válido en UTF-8 (sustituto suelto): reescribir el texto"))
            return
        if RE_PLACEHOLDER.search(nodo):
            acum.append((ruta, "tiene un texto provisional sin completar (POR_DEFINIR, TODO, TBD, xxx, lorem ipsum o «...»)"))
        elif nodo.lstrip().lower().startswith("(opcional"):
            acum.append((ruta, "es un texto de ayuda de la plantilla («(opcional ...»): completarlo o borrar la clave"))


# ----------------------------------------------------------------------------------------------
# Cálculo
# ----------------------------------------------------------------------------------------------
def unicos(lista, ruta, rep, clave="id"):
    vistos = {}
    for i, x in enumerate(lista):
        k = x.get(clave) if isinstance(x, dict) else None
        if k in vistos:
            rep.err("%s[%d].%s" % (ruta, i, clave), "id duplicado '%s' (ya usado en %s[%d])" % (k, ruta, vistos[k]))
        vistos.setdefault(k, i)


def entero_horas(v, donde, rep):
    """Devuelve las horas como entero >= 0, o -1 si hay error (ya reportado)."""
    if isinstance(v, float):
        if not v.is_integer():
            rep.err(donde, "las horas deben ser enteras, recibido %r" % v)
            return -1
        v = int(v)
    if not isinstance(v, int) or v < 0:
        rep.err(donde, "las horas deben ser un entero >= 0, recibido %r" % (v,))
        return -1
    if v > 500:
        rep.err(donde, "%d h en una sola solución parece un error de tipeo (máx. 500)" % v)
        return -1
    return v


def calcular(d, rep):
    """Valida estructura y devuelve (ctx, agg). Supone tipos ya validados."""
    agg = {"n_total": 0, "h_total": 0, "n_areas": 0, "n_bases": 0, "fase": {}, "frente": {}, "celda": {}, "carril": {}, "area": {}}
    carriles = d.get("carriles") or []
    if not (1 <= len(carriles) <= 2):
        rep.err("carriles", "se soportan 1 o 2 carriles (herramientas/plataformas); hay %d" % len(carriles))
    unicos(carriles, "carriles", rep)
    car_ids = set()
    for i, c in enumerate(carriles):
        for k in ("id", "nombre"):
            if not c.get(k):
                rep.err("carriles[%d]" % i, "falta %s" % k)
        if c.get("id") and not re.match(r"^[a-z0-9_]+$", c["id"]):
            rep.err("carriles[%d].id" % i, "el id '%s' debe usar solo minúsculas, números y _ (se usa en tokens {n_carril_<id>})" % c["id"])
        c.setdefault("nombre_corto", c.get("nombre", ""))
        c.setdefault("color", "amarillo" if i == 0 else "naranja")
        if c["color"] not in COLORES:
            rep.err("carriles[%d].color" % i, "debe ser 'amarillo' o 'naranja'")
        car_ids.add(c.get("id"))

    fases = d.get("fases") or []
    unicos(fases, "fases", rep)
    fase_ids = [f.get("id") for f in fases]
    for i, f in enumerate(fases):
        if f.get("id") not in FASES_VALIDAS:
            rep.err("fases[%d].id" % i, "falta o no es válido (debe ser F0, F1, F2 o F3; recibido %r)" % (f.get("id"),))
    cols = [f for f in fases if f.get("id") != "F0"]
    if not (2 <= len(cols) <= 3):
        rep.err("fases", "se soportan 2 o 3 fases en columna (F1..F3, más F0 opcional para el arranque); hay %d" % len(cols))
    for f in cols:
        for k in ("titulo", "rango", "descripcion"):
            if not f.get(k):
                rep.err("fases[%s]" % f.get("id"), "falta %s" % k)
    dest = [f for f in cols if f.get("destacada")]
    if cols and not dest:
        cols[0]["destacada"] = True
    elif len(dest) > 1:
        rep.aviso("fases", "hay más de una fase destacada; se resaltarán todas (normalmente solo la de más horas)")

    frentes = d.get("frentes") or []
    if not (1 <= len(frentes) <= 3):
        rep.err("frentes", "se soportan 1 a 3 frentes; hay %d" % len(frentes))
    unicos(frentes, "frentes", rep)
    fr_ids = [f.get("id") for f in frentes]
    for i, f in enumerate(frentes):
        for k in ("id", "carril", "semanas"):
            if not f.get(k):
                rep.err("frentes[%d]" % i, "falta %s" % k)
        if f.get("carril") not in car_ids:
            rep.err("frentes[%s].carril" % f.get("id"), "no existe en carriles")
        if f.get("id") and not re.match(r"^[A-Za-z0-9_]+$", f["id"]):
            rep.err("frentes[%d].id" % i, "usar solo letras, números y _")

    areas = d.get("areas") or []
    unicos(areas, "areas", rep)
    ids = {}
    for area in areas:
        aid = area.get("id")
        donde = "areas[%s]" % aid
        for k in ("id", "nombre", "carril", "frente"):
            if not area.get(k):
                rep.err(donde, "falta %s" % k)
        if aid and not re.match(r"^[A-Za-z0-9_]+$", aid):
            rep.err(donde + ".id", "usar solo letras, números y _")
        if area.get("carril") not in car_ids:
            rep.err(donde + ".carril", "no existe en carriles")
        if area.get("frente") not in fr_ids:
            rep.err(donde + ".frente", "no existe en frentes")
        else:
            fr = [f for f in frentes if f.get("id") == area["frente"]][0]
            if fr.get("carril") != area.get("carril"):
                rep.err(donde, "el frente %s es del carril %s pero el área es del carril %s" % (fr["id"], fr.get("carril"), area.get("carril")))
        sols = area.get("soluciones") or []
        if not sols:
            rep.err(donde, "sin soluciones")
        an, ah = 0, 0
        for s in sols:
            sd = "%s.%s" % (donde, s.get("id"))
            if not s.get("id"):
                rep.err(donde, "solución sin id")
                continue
            if s["id"] in ids:
                rep.err(sd, "id de solución duplicado (ya está en el área %s)" % ids[s["id"]])
            ids[s["id"]] = aid
            if not s.get("entregable"):
                rep.err(sd, "falta el nombre corto del entregable (campo 'entregable')")
            malo = False
            if all(k in s for k in ("C", "T", "A")):
                c = entero_horas(s["C"], sd + ".C", rep)
                t = entero_horas(s["T"], sd + ".T", rep)
                a = entero_horas(s["A"], sd + ".A", rep)
                if min(c, t, a) < 0:
                    malo, h = True, 0
                else:
                    h = c + t + a
                    if "h" in s and entero_horas(s["h"], sd + ".h", rep) != h:
                        rep.err(sd, "h=%s no coincide con C+T+A=%s" % (s["h"], h))
            elif "h" in s:
                h = entero_horas(s["h"], sd + ".h", rep)
                if h < 0:
                    malo, h = True, 0
            else:
                rep.err(sd, "falta C/T/A (o 'h' total)")
                malo, h = True, 0
            if h < 1 and not malo:
                rep.err(sd, "la solución tiene 0 horas")
            s["_h"] = h
            ff = s.get("fase")
            if ff not in fase_ids:
                rep.err(sd + ".fase", "fase '%s' no está definida en fases (para F0 hay que declararla)" % ff)
            n_h = agg["fase"].setdefault(ff, [0, 0]); n_h[0] += 1; n_h[1] += h
            cc = agg["celda"].setdefault((area.get("frente"), ff), [0, 0]); cc[0] += 1; cc[1] += h
            fa = agg["frente"].setdefault(area.get("frente"), [0, 0]); fa[0] += 1; fa[1] += h
            ca = agg["carril"].setdefault(area.get("carril"), {"n": 0, "h": 0, "areas": 0, "bases": 0}); ca["n"] += 1; ca["h"] += h
            an += 1; ah += h
            agg["n_total"] += 1; agg["h_total"] += h
        agg["area"][aid] = [an, ah]
        ca = agg["carril"].setdefault(area.get("carril"), {"n": 0, "h": 0, "areas": 0, "bases": 0})
        if area.get("proceso_base"):
            ca["bases"] += 1; agg["n_bases"] += 1
        else:
            ca["areas"] += 1; agg["n_areas"] += 1

    cl = d.get("cliente") or {}
    ruta = d.get("ruta") or {}
    seg = d.get("seguimiento") or {}
    tope = ruta.get("tope_h_semana", 20)
    if not isinstance(tope, int) or isinstance(tope, bool) or tope < 1:
        rep.err("ruta.tope_h_semana", "debe ser un entero >= 1 (por defecto 20)")
        tope = 20
    sem = ruta.get("semanas_total")
    if not isinstance(sem, int) or isinstance(sem, bool) or sem < 1:
        rep.err("ruta.semanas_total", "falta o no es un entero >= 1 (número de semanas de trabajo)")
        sem = ""
    for c in carriles:
        if c.get("id") and not any(a.get("carril") == c["id"] for a in areas):
            rep.aviso("carriles[%s]" % c["id"], "no tiene áreas: se ignora (borrarlo si sobra)")
    corto = cl.get("nombre_pie") or cl.get("nombre", "")
    ctx = {
        "cliente": cl.get("nombre", ""), "cliente_corto": corto, "codigo": cl.get("codigo", ""),
        "n_total": agg["n_total"], "h_total": agg["h_total"], "n_areas": agg["n_areas"], "n_bases": agg["n_bases"],
        "n_total_txt": "%d %s" % (agg["n_total"], plural(agg["n_total"], "solución", "soluciones")),
        "n_entregables_txt": "%d %s" % (agg["n_total"], plural(agg["n_total"], "entregable", "entregables")),
        "n_areas_txt": "%d %s" % (agg["n_areas"], plural(agg["n_areas"], "área", "áreas")),
        "semanas": sem, "semanas_txt": ("%d %s" % (sem, plural(sem, "semana", "semanas"))) if isinstance(sem, int) else "", "tope_h_semana": tope, "tope_h_dia": int(round(tope / 5.0)),
        "rango_seguimiento": seg.get("rango", ""),
    }
    sem_med = (d.get("retorno") or {}).get("semana_medicion")
    if not isinstance(sem_med, int) or isinstance(sem_med, bool):
        sem_med = (sem + 13) if isinstance(sem, int) else ""  # cierre de la construcción + 90 días de seguimiento (~13 semanas)
    ctx["semana_medicion"] = sem_med
    for fid in FASES_VALIDAS:
        n, h = agg["fase"].get(fid, [0, 0])
        ctx["n_%s" % fid.lower()] = n
        ctx["h_%s" % fid.lower()] = h
    for fr in fr_ids:
        if fr:
            n, h = agg["frente"].get(fr, [0, 0])
            ctx["n_frente_%s" % str(fr).lower()] = n
            ctx["h_frente_%s" % str(fr).lower()] = h
    for cid in car_ids:
        if cid:
            c = agg["carril"].get(cid, {"n": 0, "h": 0})
            ctx["n_carril_%s" % cid] = c["n"]
            ctx["h_carril_%s" % cid] = c["h"]
    return ctx, agg


def validar_semantica(d, ctx, agg, rep, silent):
    def rs(x):
        return sin_marcado(silent(x, "_")) if isinstance(x, str) else ""

    if d.get("division") not in DIVISIONES:
        rep.err("division", "debe ser 'educacion' o 'fundacion' (no se infiere: preguntar y guardar, CLAUDE.md §4.1)")
    if not isinstance(d.get("alianza"), bool):
        rep.err("alianza", "debe ser true o false (confirmar con el usuario, CLAUDE.md §4.1a punto 2)")
    cl = d.get("cliente") or {}
    for k in ("nombre", "slug", "codigo"):
        if not cl.get(k):
            rep.err("cliente.%s" % k, "falta")
    if cl.get("slug") and not re.match(r"^[a-z0-9][a-z0-9-]*$", cl["slug"]):
        rep.err("cliente.slug", "usar solo minúsculas, números y guiones, sin tildes ni espacios (carpeta clientes/propuestas/<slug>); recibido %r" % cl["slug"])
    if cl.get("codigo") and not re.match(r"^[A-Z]{2,4}-\d{1,4}$", cl["codigo"]):
        rep.aviso("cliente.codigo", "formato inusual %r (esperado p. ej. CAI-035)" % cl["codigo"])
    all_ids = set()
    revisar = []
    for a in d.get("areas") or []:
        for s in a.get("soluciones") or []:
            all_ids.add(s.get("id"))
            if s.get("_revisar"):
                revisar.append(s.get("id"))
    if revisar:
        rep.err("areas", "%d soluciones siguen marcadas _revisar (nombres propuestos por el importador): %s. Revisar cada nombre y borrar la marca" % (len(revisar), ", ".join(revisar[:12]) + ("..." if len(revisar) > 12 else "")))

    p = d.get("portada") or {}
    for k in ("titulo_destacado", "lead"):
        if not p.get(k):
            rep.err("portada.%s" % k, "falta")
    if not (p.get("titulo_lineas") or p.get("titulo_linea1")):
        rep.err("portada.titulo_lineas", "falta: el titular es una frase-objetivo de 1 a 3 líneas (más la franja amarilla de titulo_destacado)")
    if p.get("titulo_lineas") and p.get("titulo_linea1"):
        rep.aviso("portada.titulo_linea1", "se ignora porque existe titulo_lineas")
    if len(p.get("titulo_lineas") or []) > 3:
        rep.err("portada.titulo_lineas", "máximo 3 líneas antes de la franja amarilla; hay %d" % len(p["titulo_lineas"]))
    if p.get("eyebrow") and "habilidades" not in p["eyebrow"].lower():
        rep.err("portada.eyebrow", "debe nombrar el servicio («Servicio de Habilidades»): CLAUDE.md §4.1a punto 4 es bloqueante")
    lin_t, dest_t, px_t, cpl_t, tot_t = titulo_portada(p, rs)
    maxnom = 90 - len(cl.get("codigo") or "") - 1
    if tot_t > maxnom:
        rep.aviso("portada.titulo", "el titular completo mide %d caracteres: generar-pdf.sh nombra el PDF «<CÓDIGO> <titular>» y lo corta a 90, así que el nombre del archivo quedaría cortado a media palabra (máx. %d con el código %s). Acortar o aceptar el corte" % (tot_t, maxnom, cl.get("codigo")))
    if [x.lower() for x in lin_t[:2]] == ["optimización de procesos y datos", "con inteligencia artificial"] and cl.get("slug") != "dusa-cai035":
        rep.aviso("portada.titulo", "el titular es idéntico al del ejemplo de DUSA: nombrar al menos un proceso o dominio del cliente en la línea 1 o 2 (p. ej. «registros y reportes a donantes»)")
    for x in lin_t + [dest_t]:
        if len(x) > cpl_t:
            rep.aviso("portada.titulo", "la línea «%s» mide %d caracteres y a %d px caben ~%d: se partirá en 2 líneas" % (x[:30], len(x), px_t, cpl_t))
    if (lin_t + [dest_t]) and (lin_t + [dest_t])[-1].endswith("."):
        rep.aviso("portada.titulo", "el titular termina en punto: el nombre del PDF quedaría «...pdf» con doble punto; el estilo de título (tesis) no lleva punto final")
    if sum(1 for x in lin_t + [dest_t] if len(x) > cpl_t) + len(lin_t) + 1 > 5:
        rep.aviso("portada.titulo", "el titular ocupa más de 5 líneas y puede chocar con el lead")
    if len(rs(p.get("lead"))) > 260:
        rep.aviso("portada.lead", "%d caracteres: máx. ~230 (3 líneas); podría chocar con la franja de datos" % len(rs(p["lead"])))
    hechos = p.get("hechos") or []
    if not (2 <= len(hechos) <= 4):
        rep.err("portada.hechos", "se necesitan 2 a 4 datos de dolor; hay %d" % len(hechos))
    for i, h in enumerate(hechos):
        donde = "portada.hechos[%d]" % i
        if not h.get("num") or not h.get("texto"):
            rep.err(donde, "faltan num/texto")
        else:
            if len(rs(h["texto"])) > 100:
                rep.aviso(donde, "texto de %d caracteres: máx. ~95 (3 líneas)" % len(rs(h["texto"])))
            if len(rs(h["num"])) > 9:
                rep.aviso(donde, "num de %d caracteres (%r): máx. ~9; se parte en 2 líneas y descuadra la franja" % (len(rs(h["num"])), h["num"]))
        rp = h.get("resuelto_por") or []
        if not rp:
            rep.err(donde, "falta 'resuelto_por' (ids de las soluciones que atienden ese dolor). Un dolor que la propuesta no resuelve (o que queda fuera del alcance) no va en la portada")
        for sid in rp:
            if sid not in all_ids:
                rep.err(donde, "resuelto_por: la solución '%s' no existe" % sid)
    al = d.get("alcance") or {}
    pasos = al.get("pasos") or []
    if not (2 <= len(pasos) <= 4):
        rep.err("alcance.pasos", "se necesitan 2 a 4 pasos; hay %d" % len(pasos))
    for x in pasos:
        if len(rs(x)) > 70:
            rep.aviso("alcance.pasos", "paso de %d caracteres (máx. ~70): %s" % (len(rs(x)), rs(x)[:30]))
    if not al.get("subtitulo"):
        rep.err("alcance.subtitulo", "falta")
    elif len(rs(al["subtitulo"])) > 118:
        rep.aviso("alcance.subtitulo", "%d caracteres: máx. ~115 para una línea" % len(rs(al["subtitulo"])))
    if len(rs(al.get("quien_construye"))) > 200:
        rep.aviso("alcance.quien_construye", "%d caracteres: máx. ~200" % len(rs(al["quien_construye"])))
    fa = al.get("fuera_alcance") or []
    if len(fa) > 5:
        rep.aviso("alcance.fuera_alcance", "%d puntos: máx. 5" % len(fa))
    fases_cols = [f for f in (d.get("fases") or []) if f.get("id") != "F0"]
    ids_cols = [f.get("id") for f in fases_cols]
    for fr in d.get("frentes") or []:
        celdas = fr.get("celdas") or {}
        for k in celdas:
            if k not in ids_cols:
                rep.aviso("frentes[%s].celdas.%s" % (fr.get("id"), k), "no corresponde a ninguna fase en columna (se ignora)")
        for f in fases_cols:
            n = agg["celda"].get((fr.get("id"), f.get("id")), [0, 0])[0]
            txt = celdas.get(f.get("id"))
            if n and not txt:
                rep.err("frentes[%s].celdas.%s" % (fr.get("id"), f.get("id")), "hay %d soluciones en esa celda y falta el texto" % n)
            if txt and not n:
                rep.aviso("frentes[%s].celdas.%s" % (fr.get("id"), f.get("id")), "hay texto pero no hay soluciones en esa celda (se mostrará vacía)")
            if txt and len(rs(txt)) > 90:
                rep.aviso("frentes[%s].celdas.%s" % (fr.get("id"), f.get("id")), "texto de %d caracteres: máx. ~90 (4 líneas); acortar" % len(rs(txt)))
    if len(rs((d.get("ruta") or {}).get("nota"))) > 510:
        rep.aviso("ruta.nota", "%d caracteres: máx. ~510 (3 líneas); una cuarta línea deja menos de 8 px contra el pie" % len(rs(d["ruta"]["nota"])))
    if len(rs((d.get("ruta") or {}).get("titulo"))) > 46:
        rep.aviso("ruta.titulo", "%d caracteres: puede pasar a 2 líneas y desplazar la grilla" % len(rs(d["ruta"]["titulo"])))
    hitos = (d.get("ruta") or {}).get("hitos") or []
    if not (3 <= len(hitos) <= 5):
        rep.err("ruta.hitos", "se necesitan 3 a 5 hitos; hay %d" % len(hitos))
    for i, h in enumerate(hitos):
        if not h.get("titulo") or not h.get("texto"):
            rep.err("ruta.hitos[%d]" % i, "faltan titulo/texto")
        elif len(rs(h["texto"])) > 95:
            rep.aviso("ruta.hitos[%d]" % i, "texto de %d caracteres: máx. ~90 (3 líneas)" % len(rs(h["texto"])))
    # Rótulos del frente y herramientas
    for c in d.get("carriles") or []:
        if len(c.get("nombre_corto") or "") > 22:
            rep.aviso("carriles[%s].nombre_corto" % c.get("id"), "%d caracteres: el rótulo «Frente X · …» no admite más de ~22; definir nombre_corto" % len(c["nombre_corto"]))
    sem_tot = (d.get("ruta") or {}).get("semanas_total")
    maxsem = 0
    for fr in d.get("frentes") or []:
        if fr.get("id") and not any(a.get("frente") == fr["id"] for a in d.get("areas") or []):
            rep.err("frentes[%s]" % fr["id"], "no tiene áreas asignadas (borrar el frente o asignarle áreas): una fila de la ruta quedaría vacía")
        nums = [int(x) for x in re.findall(r"\bS\s*(\d+)", fr.get("semanas") or "")] + [int(x) for x in re.findall(r"(?<=[-–])\s*(\d+)", fr.get("semanas") or "")]
        if nums:
            maxsem = max(maxsem, max(nums))
    if isinstance(sem_tot, int) and maxsem and maxsem != sem_tot:
        rep.aviso("ruta.semanas_total", "vale %d pero los frentes llegan hasta la semana %d: unificar (el título y la duración usan semanas_total)" % (sem_tot, maxsem))
    for fr in d.get("frentes") or []:
        nombres = [(a.get("nombre_frente") or a.get("nombre") or "") for a in d.get("areas") or [] if a.get("frente") == fr.get("id")]
        largos = [n for n in nombres if len(n) > 33]
        if largos and not fr.get("areas_html"):
            rep.aviso("frentes[%s]" % fr.get("id"), "el nombre «%s» (%d car.) se usa sin cortar línea en el rótulo del frente y puede salirse de la tarjeta: definir areas[].nombre_frente ≤ 33 caracteres (ancho de la tarjeta ≈ 193 px)" % (largos[0], len(largos[0])))
        tope_rot = {1: 330, 2: 165, 3: 100}.get(len(d.get("frentes") or []), 100)
        if sum(len(n) + 2 for n in nombres) > tope_rot and not fr.get("areas_html"):
            rep.aviso("frentes[%s]" % fr.get("id"), "el rótulo de áreas suma ~%d caracteres (máx. ~%d con %d frente(s)): acortar nombre_frente o repartir las áreas en otro frente" % (sum(len(n) + 2 for n in nombres), tope_rot, len(d.get("frentes") or [])))
        if fr.get("areas_html"):
            for tag in ("span", "b", "i", "em", "strong"):
                if len(re.findall(r"<%s[ >]" % tag, fr["areas_html"])) != len(re.findall(r"</%s>" % tag, fr["areas_html"])):
                    rep.err("frentes[%s].areas_html" % fr.get("id"), "etiquetas <%s> sin balancear" % tag)
        dec = fr.get("_horas_fuente")
        if isinstance(dec, str):
            mm = re.match(r"\s*(\d+)", dec)
            if mm and agg["frente"].get(fr.get("id")) and int(mm.group(1)) != agg["frente"][fr["id"]][1]:
                rep.aviso("frentes[%s]" % fr.get("id"), "el insumo declaraba %s h y datos.json suma %d h (¿cambio intencional? borrar _horas_fuente si sí)" % (mm.group(1), agg["frente"][fr["id"]][1]))
    sg = d.get("seguimiento") or {}
    its = sg.get("items") or []
    if not (2 <= len(its) <= 3):
        rep.err("seguimiento.items", "se necesitan 2 o 3 check-ins (30/60/90 días); hay %d" % len(its))
    for it in its:
        if not it.get("dias") or not it.get("texto"):
            rep.err("seguimiento.items", "cada check-in necesita dias y texto")
    for k in ("rango", "texto"):
        if not sg.get(k):
            rep.err("seguimiento.%s" % k, "falta")
    en = d.get("entregables") or {}
    for k in ("transversales", "valor_inmediato"):
        if not en.get(k):
            rep.err("entregables.%s" % k, "falta (lista de 2 a 4 viñetas)")
    for a in d.get("areas") or []:
        for s in a.get("soluciones") or []:
            e = s.get("entregable") or ""
            if len(e) > 99:
                rep.err("areas[%s].%s" % (a.get("id"), s.get("id")), "nombre de entregable de %d caracteres (máx. 99 = 3 líneas)" % len(e))
            elif len(e) > 72:
                rep.aviso("areas[%s].%s" % (a.get("id"), s.get("id")), "nombre de %d caracteres: se renderiza a 3 líneas; preferible ≤ 72 (ideal ≤ 36 en una línea)" % len(e))
    transv_txt = " ".join(x for x in (en.get("transversales") or []) if isinstance(x, str)).lower()
    for a in d.get("areas") or []:
        for s_ in a.get("soluciones") or []:
            if s_.get("fase") == "F0" and "línea base" in (s_.get("entregable") or "").lower() and "línea base" in transv_txt:
                rep.aviso("areas[%s].%s" % (a.get("id"), s_.get("id")), "la línea base ya es un entregable transversal: no duplicarla como solución F0 (cuenta en {n_total} y aparece dos veces)")
    n_rows = len(d.get("areas") or [])
    if n_rows > 13:
        rep.err("areas", "%d filas de área: máximo 13 en la slide 2 (con alcance.compacto; con 14 la holgura contra el pie queda en ~5 px). Agrupar áreas" % n_rows)
    elif n_rows > 11 and not al.get("compacto"):
        rep.aviso("areas", "%d filas de área: con más de 11 usar alcance.compacto=true y verificar holguras" % n_rows)
    inv = d.get("inversion") or {}
    lic = inv.get("licencias") or {}
    tars = lic.get("tarjetas") or []
    if len(tars) > 2:
        rep.err("inversion.licencias.tarjetas", "máximo 2 tarjetas")
    if d.get("division") != "fundacion":
        for i, c in enumerate(tars):
            for k in ("nombre", "texto"):
                if not c.get(k):
                    rep.err("inversion.licencias.tarjetas[%d]" % i, "falta %s" % k)
            if len(rs(c.get("texto"))) > 255:
                rep.aviso("inversion.licencias.tarjetas[%d]" % i, "tarjeta de %d caracteres: máx. ~250; la sección podría chocar con el pie" % len(rs(c["texto"])))
            if c.get("color") and c["color"] not in COLORES:
                rep.err("inversion.licencias.tarjetas[%d].color" % i, "debe ser 'amarillo' o 'naranja'")
        if len(rs(inv.get("duracion") or "")) > 112:
            rep.aviso("inversion.duracion", "%d caracteres: máx. ~110 (2 líneas)" % len(rs(inv["duracion"])))
    if d.get("division") == "fundacion":
        if inv:
            rep.aviso("inversion", "se ignora en Fundación (no hay slide de inversión); llevar licencias y notas a otra parte si hacen falta")
    else:
        if tars and not inv.get("notas"):
            rep.aviso("inversion.notas", "hay licenciamiento pero no hay notas: aclarar si se contrata aparte (confirmar quién lo contrata)")
        if not inv.get("notas"):
            rep.aviso("inversion.notas", "sin notas: el campo Notas del PDF queda en blanco para que ventas lo llene")
    validar_retorno(d, ctx, agg, rep, rs)


# ----------------------------------------------------------------------------------------------
# Slide 5: reparto de áreas en columnas (estimador calibrado con mediciones reales, 2026-10-05)
# ----------------------------------------------------------------------------------------------
def nombre_catalogo(a):
    n = a.get("nombre_catalogo") or a["nombre"]
    if a.get("proceso_base") and "proceso base" not in n.lower():
        n += " (proceso base)"
    return n


def ancho_col(ncols):
    return (1011.0 - 16 * (ncols - 1)) / ncols - 40


def alto_area(a, ncols, compacto):
    w = ancho_col(ncols)
    cpl = 36.0 * w / 200.75 * (1.05 if compacto else 1.0)
    cpn = (w - 30) / 6.4
    lh = 13.3 if compacto else 14.3
    pad = 3 if compacto else 4
    nl = lineas_wrap(nombre_catalogo(a), cpn)
    h = max(22, nl * (14.4 if compacto else 15)) + 3
    for s in a["soluciones"]:
        h += lineas_wrap(s["entregable"], cpl) * lh + pad
    return h


def mejor_particion(areas, k, ncols, compacto):
    n = len(areas)
    k = min(k, n)
    hs = [alto_area(a, ncols, compacto) for a in areas]
    sep = 10.0 if compacto else 14.0  # margen + relleno + borde (+ holgura)
    pref = [0.0]
    for h in hs:
        pref.append(pref[-1] + h)

    def costo(i, j):
        return pref[j] - pref[i] + sep * max(0, (j - i - 1))

    INF = 1e9
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    cut = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for j in range(1, n + 1):
        for c in range(1, k + 1):
            for i in range(c - 1, j):
                v = max(dp[i][c - 1], costo(i, j))
                if v < dp[j][c]:
                    dp[j][c] = v
                    cut[j][c] = i
    grupos = []
    j, c = n, k
    while c > 0:
        i = cut[j][c]
        grupos.append(areas[i:j])
        j, c = i, c - 1
    grupos.reverse()
    return dp[n][k], grupos


def repartir_columnas(d, rep):
    """Devuelve (columnas, ncols, alto_max_estimado). Cada columna: {'carril': c, 'areas': [...]}."""
    compacto = bool((d.get("entregables") or {}).get("compacto"))
    por_carril = [(c, [a for a in d["areas"] if a["carril"] == c["id"]]) for c in d["carriles"]]
    por_carril = [(c, a) for c, a in por_carril if a]
    if not por_carril:
        return [], 0, 0
    cfg = (d.get("entregables") or {}).get("columnas_por_carril")
    if cfg:
        if len(cfg) != len(por_carril) or any(k < 1 for k in cfg) or sum(cfg) > 4:
            rep.err("entregables.columnas_por_carril", "debe ser una lista con un valor >= 1 por carril (en orden), de suma <= 4; hay %d carril(es) con áreas" % len(por_carril))
            return [], 0, 0
        for (c, areas), k in zip(por_carril, cfg):
            if k > len(areas):
                rep.err("entregables.columnas_por_carril", "el carril '%s' tiene %d área(s) y se piden %d columnas" % (c["id"], len(areas), k))
                return [], 0, 0
        opciones = [tuple(cfg)]
    elif len(por_carril) == 1:
        opciones = [(k,) for k in range(1, min(4, len(por_carril[0][1])) + 1)]
    else:
        n0, n1 = len(por_carril[0][1]), len(por_carril[1][1])
        opciones = [(a, b) for a in range(1, min(3, n0) + 1) for b in range(1, min(3, n1) + 1) if a + b <= 4]
    mejor = None
    for op in opciones:
        ncols = sum(op)
        peor, cols = 0, []
        for (c, areas), k in zip(por_carril, op):
            h, grupos = mejor_particion(areas, k, ncols, compacto)
            peor = max(peor, h)
            for g in grupos:
                cols.append({"carril": c, "areas": g})
        clave = (round(peor), -ncols)
        if mejor is None or clave < mejor[0]:
            mejor = (clave, cols, ncols, peor)
    if mejor is None:
        rep.err("entregables", "no se pudo repartir las áreas en columnas")
        return [], 0, 0
    return mejor[1], mejor[2], mejor[3]


def estimar_s2_derecha(d, R):
    """(alto estimado en px de la columna derecha de la slide 2, cupo en px). Calibrado con DUSA 2026-10-05:
    tarjeta = 63,5 px fijos + contenido; líneas de 17,5 px; anchos útiles 274 (pasos), 302 (quién), 288 (fuera) px a ~6 px/car (≈45, 46 y 46 car. por línea: ligeramente conservador, el texto en negrita ocupa más)."""
    al = d["alcance"]
    sub = sin_marcado(R.t(al.get("subtitulo") or "", "alcance.subtitulo"))
    lsub = lineas_wrap(sub, 120) if sub else 1
    cupo = 600.8 - 21.0 * lsub
    quita = lambda x: sin_marcado(R.t(x, "alcance"))
    h = 63.5 + sum(lineas_wrap(quita(x), 45) * 17.5 + 6 for x in al.get("pasos") or [])
    n = 1
    if al.get("quien_construye"):
        h += 63.5 + lineas_wrap(quita(al["quien_construye"]), 46) * 17.5
        n += 1
    if al.get("fuera_alcance"):
        h += 63.5 + sum(lineas_wrap(quita(x), 46) * 17.5 + 5 for x in al["fuera_alcance"])
        n += 1
    return h + 12.0 * (n - 1), cupo


def cupo_catalogo(d, R):
    """Cupo en px de la columna más alta: depende del alto de la cabecera (título + subtítulo)."""
    en = d["entregables"]
    titulo = R.t(en.get("titulo") or "Todo lo que {cliente_corto} recibe.", "entregables.titulo")
    sub = sin_marcado(R.t(en.get("subtitulo") or SUB_ENTREGABLES, "entregables.subtitulo"))
    h2_ancho = min(560.0, len(titulo) * 19.0)
    lh2 = lineas_wrap(titulo, 560 / 19.0)
    ancho_sub = max(300.0, min(520.0, 1011 - 28 - h2_ancho))
    lsub = lineas_wrap(sub, ancho_sub / 6.3)
    cab = max(lh2 * 37.8, lsub * 18.0)
    cols_top = 44 + 23.4 + cab + 10 + 34
    # La última área debe terminar >= 14 px antes de la franja (top 610): 596 - cols_top - (borde 4 + relleno 8).
    return 596 - cols_top - 12


# ----------------------------------------------------------------------------------------------
# Render
# ----------------------------------------------------------------------------------------------
def foot(R, variante):
    # Fondo claro -> logo NEGRO; fondo oscuro -> logo BLANCO (CLAUDE.md §4.1).
    logo = "NEGRO" if variante == "claro" else "BLANCO"
    return (
        '      <div class="foot">\n'
        '        <img src="%s/%s.png" alt="">\n'
        '        <span class="meta">%s · %s</span>\n'
        "      </div>\n" % (R.rel_logos, logo, R.T(R.pie, "cliente.nombre_pie"), esc(R.codigo))
    )


def s1_portada(d, R):
    p = d["portada"]
    T, M = R.T, R.M
    eyebrow = p.get("eyebrow") or "Propuesta de proyecto · Servicio de Habilidades"
    hechos = "".join(
        '          <div class="pain-item">\n'
        '            <span class="pain-num">%s</span>\n'
        '            <span class="pain-lbl">%s</span>\n'
        "          </div>\n" % (T(h["num"], "portada.hechos.num"), M(h["texto"], "portada.hechos.texto"))
        for h in p.get("hechos", [])
    )
    fuente = ('        <p class="pain-src">%s</p>\n' % T(p["fuente"], "portada.fuente")) if p.get("fuente") else ""
    lineas, dest, px, _cpl, _tot = titulo_portada(p, lambda x: sin_marcado(R.t(x, "portada.titulo")))
    h1 = "".join("          %s<br>\n" % esc(x) for x in lineas) + '          <span class="hl">%s</span>\n' % esc(dest)
    return (
        '    <!-- 1 · Portada con punto de dolor -->\n'
        '    <section class="slide s-cover">\n'
        '      <span class="counter">%s</span>\n'
        '      <div class="logo-big">\n'
        '        <img src="%s/BLANCO.png" alt="Intezia %s">\n'
        "      </div>\n"
        '      <div class="body">\n'
        '        <p class="eyebrow">%s</p>\n'
        '        <h1 style="font-size:%dpx">\n'
        "%s"
        "        </h1>\n"
        '        <p class="lead">\n'
        "          %s\n"
        "        </p>\n"
        '        <div class="pain-strip">\n%s        </div>\n%s'
        "      </div>\n"
        '      <div class="id-line">\n'
        '        <span class="codigo">Código: %s</span>\n'
        '        <span class="cliente">%s</span>\n'
        "      </div>\n"
        "    </section>\n"
        % (R.contador(1), R.rel_logos, R.div_nombre, T(eyebrow, "portada.eyebrow"),
           px, h1,
           M(p["lead"], "portada.lead"), hechos, fuente, esc(R.codigo), T(R.pie, "cliente.nombre_pie"))
    )


def titulo_portada(p, tok):
    """(líneas, destacado, px del h1, caracteres por línea, total) del titular de la portada.
    tok convierte cada texto (tokens y negrita ya resueltos). Acepta titulo_linea1 como alias de una sola línea."""
    lineas = p.get("titulo_lineas")
    if not lineas and isinstance(p.get("titulo_linea1"), str):
        lineas = [p["titulo_linea1"]]
    lineas = [tok(x) for x in (lineas or []) if isinstance(x, str)]
    dest = tok(p.get("titulo_destacado") or "") if isinstance(p.get("titulo_destacado"), str) else ""
    total = len(" ".join(lineas + [dest]).strip())
    for tope, px, cpl in FONT_TITULO:
        if total <= tope:
            return lineas, dest, px, cpl, total
    return lineas, dest, FONT_TITULO[-1][1], FONT_TITULO[-1][2], total


def titulo_alcance_defecto(R):
    return "%s en %s de {cliente_corto}." % (R.ctx["n_total_txt"], R.ctx["n_areas_txt"])


def s2_alcance(d, R):
    T, M = R.T, R.M
    al = d["alcance"]
    titulo = al.get("titulo") or titulo_alcance_defecto(R)
    paneles = ""
    for c in d["carriles"]:
        areas = [a for a in d["areas"] if a["carril"] == c["id"]]
        if not areas:
            continue
        ca = R.agg["carril"][c["id"]]
        base = ""
        if ca["bases"] == 1:
            base = " y un proceso base"
        elif ca["bases"] > 1:
            base = " y %d procesos base" % ca["bases"]
        filas = ""
        for a in areas:
            n = R.agg["area"][a["id"]][0]
            em = ""
            if a.get("proceso_base"):
                em = " <em>(%s)</em>" % T(al.get("etiqueta_proceso_base") or "proceso base", "alcance.etiqueta_proceso_base")
            uw = ""
            if n > 12:
                uw = ";--uw:%dpx" % max(4, int(240 / n) - 4)
            filas += (
                '              <li><span class="area">%s%s</span><span class="units" style="--n:%d%s"></span><span class="n">%d</span></li>\n'
                % (T(a["nombre"], "areas.nombre"), em, n, uw, n)
            )
        paneles += (
            '          <div class="scope-panel %s">\n'
            '            <div class="scope-head">\n'
            '              <span class="scope-tag">%s</span>\n'
            '              <span class="scope-total"><b>%d</b> %s · %d %s%s</span>\n'
            "            </div>\n"
            '            <ul class="scope-rows">\n%s            </ul>\n'
            "          </div>\n\n"
            % (COLORES[c["color"]], T(c["nombre"], "carriles.nombre"), ca["n"], plural(ca["n"], "solución", "soluciones"),
               ca["areas"], plural(ca["areas"], "área", "áreas"), base, filas)
        )
    pasos = "".join("              <li>%s</li>\n" % M(x, "alcance.pasos") for x in al["pasos"])
    num = {2: "dos", 3: "tres", 4: "cuatro"}[len(al["pasos"])]
    cards = (
        '          <div class="scope-card">\n'
        '            <p class="scope-card-label">%s</p>\n'
        '            <ol class="scope-steps">\n%s            </ol>\n'
        "          </div>\n" % (T(al.get("etiqueta_pasos") or ("Cada solución, %s pasos" % num), "alcance.etiqueta_pasos"), pasos)
    )
    if al.get("quien_construye"):
        cards += (
            '          <div class="scope-card">\n'
            '            <p class="scope-card-label">%s</p>\n'
            "            <p>%s</p>\n"
            "          </div>\n" % (T(al.get("etiqueta_quien") or "Quién construye", "alcance.etiqueta_quien"), M(al["quien_construye"], "alcance.quien_construye"))
        )
    if al.get("fuera_alcance"):
        li = "".join("              <li>%s</li>\n" % M(x, "alcance.fuera_alcance") for x in al["fuera_alcance"])
        cards += (
            '          <div class="scope-card scope-out">\n'
            '            <p class="scope-card-label">%s</p>\n'
            "            <ul>\n%s            </ul>\n"
            "          </div>\n" % (T(al.get("etiqueta_fuera") or "Fuera de este alcance", "alcance.etiqueta_fuera"), li)
        )
    return (
        '    <!-- 2 · Alcance -->\n'
        '    <section class="slide s-scope%s">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">02 · Alcance</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="scope-body">\n'
        '        <div class="scope-left">\n\n%s        </div>\n\n'
        '        <div class="scope-right">\n%s        </div>\n'
        "      </div>\n\n%s"
        "    </section>\n"
        % (" compact" if al.get("compacto") else "", R.contador(2), T(titulo, "alcance.titulo"),
           M(al["subtitulo"], "alcance.subtitulo"), paneles, cards, foot(R, "claro"))
    )


def lista_areas(nombres):
    items = ['<span class="nw">%s</span>' % esc(n) for n in nombres]
    if len(items) <= 1:
        return "".join(items)
    if " y " in nombres[-1]:  # evita «A, B y Compras y Logística» ambiguo
        return ", ".join(items)
    return ", ".join(items[:-1]) + " y " + items[-1]


def s3_ruta(d, R):
    T, M = R.T, R.M
    ruta = d["ruta"]
    seg = d["seguimiento"]
    fases_cols = [f for f in d["fases"] if f.get("id") != "F0"]
    nf = len(d["frentes"])
    ncols = len(fases_cols)
    rowh = {1: 214, 2: 130, 3: 104}[nf]
    titulo = ruta.get("titulo") or ("%s, {semanas_txt}." % PALABRAS_FRENTES[nf])
    sub = ruta.get("subtitulo") or "Semanas de trabajo desde el arranque, con **seguimiento a {rango_seguimiento}** desde el cierre de cada área."
    hdr = '        <div class="rg-corner"></div>\n'
    for i, f in enumerate(fases_cols, 1):
        n, h = R.agg["fase"].get(f["id"], [0, 0])
        hi = bool(f.get("destacada"))
        etiqueta = "<b>%d de %d h</b>" % (h, R.agg["h_total"]) if hi else "<b>%d h</b>" % h
        hdr += (
            '        <div class="rg-phase rg-ph-%d%s">\n'
            '          <span class="rg-phase-tag">%s</span>\n'
            '          <span class="rg-phase-date">%s</span>\n'
            '          <span class="rg-phase-txt">%s · %s</span>\n'
            "        </div>\n" % (i, " hi" if hi else "", T(f["titulo"], "fases.titulo"), T(f["rango"], "fases.rango"), etiqueta, M(f["descripcion"], "fases.descripcion"))
        )
    hdr += (
        '        <div class="rg-phase rg-fu">\n'
        '          <span class="rg-phase-tag">%s</span>\n'
        '          <span class="rg-phase-date">%s</span>\n'
        '          <span class="rg-phase-txt">%s</span>\n'
        "        </div>\n" % (T(seg.get("etiqueta") or "Seguimiento", "seguimiento.etiqueta"), T(seg["rango"], "seguimiento.rango"), M(seg["texto"], "seguimiento.texto"))
    )
    cuerpo = ""
    carriles = dict((c["id"], c) for c in d["carriles"])
    for fr in d["frentes"]:
        n, h = R.agg["frente"].get(fr["id"], [0, 0])
        car = carriles[fr["carril"]]
        nombres = [sin_marcado(R.t(a.get("nombre_frente") or a["nombre"], "areas.nombre_frente")) for a in d["areas"] if a["frente"] == fr["id"]]
        areas_html = fr.get("areas_html") or lista_areas(nombres)
        cuerpo += (
            '        <div class="rg-front %s">\n'
            '          <span class="rg-front-tag">Frente %s · %s</span>\n'
            '          <span class="rg-front-h"><b>%d h</b> · %s</span>\n'
            '          <span class="rg-front-areas">%s</span>\n'
            "        </div>\n" % (COLORES[car["color"]], T(fr["id"], "frentes.id"), T(fr["semanas"], "frentes.semanas"), h, T(car["nombre_corto"], "carriles.nombre_corto"), areas_html)
        )
        for f in fases_cols:
            nn, hh = R.agg["celda"].get((fr["id"], f["id"]), [0, 0])
            hi = " hi" if f.get("destacada") else ""
            txt = (fr.get("celdas") or {}).get(f["id"], "")
            if nn:
                cuerpo += (
                    '        <div class="rg-cell%s"><span class="rg-h"><b>%d</b> h <i>%d %s</i></span><p>%s</p></div>\n'
                    % (hi, hh, nn, plural(nn, "solución", "soluciones"), M(txt, "frentes.celdas"))
                )
            else:
                cuerpo += '        <div class="rg-cell empty%s"><p>Sin entregas en esta fase.</p></div>\n' % hi
    items = "".join(
        "            <li><b>%s</b><span>%s</span></li>\n" % (T(i["dias"], "seguimiento.items.dias"), M(i["texto"], "seguimiento.items")) for i in seg["items"]
    )
    follow = (
        '        <div class="rg-follow" style="grid-column:%d; grid-row:2 / span %d">\n'
        "          <ul>\n%s          </ul>\n"
        "        </div>\n" % (ncols + 2, nf, items)
    )
    hitos = ruta["hitos"]
    mil = "".join(
        '        <div class="mile"><span class="mile-d"></span><b>%s</b><p>%s</p></div>\n'
        % (T(h["titulo"], "ruta.hitos.titulo"), M(h["texto"], "ruta.hitos.texto")) for h in hitos
    )
    nums = [f["id"][1:] for f in fases_cols]  # números reales de las fases (F1, F3 -> «1 y 3»)
    nota = ruta.get("nota") or (
        "S = semana de trabajo desde el arranque. Las {h_total} h son una proyección: "
        + ("{h_f0} h de arranque más " if R.ctx.get("h_f0") else "")
        + ", ".join("{h_%s}" % f["id"].lower() for f in fases_cols[:-1])
        + " y {h_%s} h de las fases " % fases_cols[-1]["id"].lower()
        + ", ".join(nums[:-1]) + " y %s. " % nums[-1]
        + "Cada frente trabaja hasta {tope_h_semana} h de sesión por semana ({tope_h_dia} h por día). "
        + "Las fases se traslapan: un frente pasa a la siguiente cuando quien ejecuta el proceso ya opera lo anterior."
    )
    return (
        '    <!-- 3 · Ruta -->\n'
        '    <section class="slide s-route">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">03 · Ruta</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="route-grid" style="--cols:%d; --rows:%d; --rowh:%dpx">\n\n%s\n%s\n%s      </div>\n\n'
        '      <div class="route-miles" style="grid-template-columns:repeat(%d,1fr)">\n%s      </div>\n'
        '      <p class="route-note">%s</p>\n\n%s'
        "    </section>\n"
        % (R.contador(3), T(titulo, "ruta.titulo"), M(sub, "ruta.subtitulo"), ncols, nf, rowh,
           hdr, cuerpo, follow, len(hitos), mil, M(nota, "ruta.nota"), foot(R, "oscuro"))
    )


def programa_auto(d, R):
    t = R.t
    carriles = dict((c["id"], c) for c in d["carriles"])
    una = len(d["carriles"]) == 1
    lineas = ["Servicio de Habilidades · {cliente_corto}, {n_areas_txt} ({codigo})."]
    partes = []
    for fr in d["frentes"]:
        h = R.agg["frente"].get(fr["id"], [0, 0])[1]
        partes.append("Frente %s%s: %d h" % (fr["id"], "" if una else " (%s)" % carriles[fr["carril"]]["nombre"], h))
    actual = ""
    for p in partes:
        if actual and len(actual) + 3 + len(p) > 66:
            lineas.append(actual)
            actual = p
        else:
            actual = (actual + " · " + p) if actual else p
    if actual:
        lineas.append(actual)
    if una:
        lineas.append("Herramienta: %s." % carriles[d["frentes"][0]["carril"]]["nombre"])
    lineas.append("Horas de sesión: trabajo conjunto con quien ejecuta cada proceso.")
    lineas.append("{n_total_txt} construidas, probadas y adoptadas.")
    return [t(x, "inversion.programa") for x in lineas]


def s4_inversion(d, R, idx):
    T, M = R.T, R.M
    inv = d.get("inversion") or {}
    titulo = inv.get("titulo") or "Inversión por horas de sesión."
    dur = inv.get("duracion") or "Proyección de {h_total} h de sesión en {semanas_txt} de trabajo desde el arranque, más seguimiento a {rango_seguimiento}."
    garantia = inv.get("garantia_texto") or "Estamos contigo hasta que la habilidad quede instalada."
    lic = inv.get("licencias") or {}
    lic_html = ""
    if lic.get("tarjetas"):
        cards = ""
        for c in lic["tarjetas"]:
            col = COLORES.get(c.get("color") or "naranja", "acc-o")
            cards += (
                '          <div class="lic-card %s">\n'
                '            <span class="lic-name">%s</span>\n'
                "            <p>%s</p>\n"
                "          </div>\n" % (col, T(c["nombre"], "licencias.nombre"), M(c["texto"], "licencias.texto"))
            )
        nota = ('        <p class="lic-note">%s</p>\n' % T(lic["nota"], "licencias.nota")) if lic.get("nota") else ""
        lic_html = (
            '      <div class="lic-wrap">\n'
            '        <span class="lic-eyebrow">%s</span>\n'
            '        <div class="lic-cards">\n%s        </div>\n%s'
            "      </div>\n\n" % (T(lic.get("titulo") or "Licenciamiento · aparte de esta inversión", "licencias.titulo"), cards, nota)
        )
    return (
        '    <!-- 4 · Inversión (hoja de cotización estándar, por horas) -->\n'
        '    <section class="slide s-price">\n'
        '      <span class="counter">%s</span>\n'
        '      <h2 class="title">%s</h2>\n'
        '      <p class="price-intro">Propuesta Económica · Servicio de Habilidades</p>\n\n'
        '      <div class="block">\n'
        '        <span class="block-eyebrow">Duración</span>\n'
        '        <p class="block-value">%s</p>\n'
        "      </div>\n\n"
        '      <div class="block block-programa">\n'
        '        <span class="block-eyebrow">Programa</span>\n'
        "      </div>\n"
        '      <div class="multi-box programa-box" data-field="Programa"></div>\n\n'
        '      <div class="block block-cotizacion">\n'
        '        <span class="block-eyebrow">Cotización</span>\n'
        "      </div>\n\n"
        '      <span class="cot-label cot-label-base">Propuesta + Inversión</span>\n'
        '      <div class="cot-frame base-frame"></div>\n\n'
        '      <span class="cot-label cot-label-discount">Descuento</span>\n'
        '      <span class="cot-sign-minus">&minus;$</span>\n'
        '      <div class="cot-frame discount-frame"></div>\n'
        '      <span class="cot-urgent-note">Descuento válido por 15 días</span>\n\n'
        '      <span class="cot-label cot-label-total">TOTAL</span>\n'
        '      <div class="cot-frame total-frame"></div>\n\n'
        '      <p class="cot-validity">Cotización válida por 30 días.</p>\n'
        '      <div class="cot-terms-box">\n'
        '        <span class="cot-terms-label">Importante</span>\n'
        '        <p class="cot-terms-text">Este servicio se presta bajo nuestros <a href="https://drive.google.com/file/d/1PA-ZSt4KnyY5dpxXzgkIk6-yfGlV2eF8/view?usp=drive_link" target="_blank" rel="noopener">términos y condiciones</a>. Al avanzar con esta propuesta, ambas partes los aceptan.</p>\n'
        "      </div>\n\n"
        '      <div class="cot-garantia-badge">\n'
        '        <span class="cot-garantia-tag">Garantía 30-60-90</span>\n'
        '        <p class="cot-garantia-text">%s</p>\n'
        "      </div>\n\n"
        '      <div class="block block-notes-container">\n'
        '        <span class="block-eyebrow">Notas</span>\n'
        "      </div>\n"
        '      <div class="multi-box notas-box" data-field="Notas"></div>\n\n%s%s'
        "    </section>\n"
        % (R.contador(idx), T(titulo, "inversion.titulo"), M(dur, "inversion.duracion"), T(garantia, "inversion.garantia_texto"), lic_html, foot(R, "claro"))
    )


def s5_entregables(d, R, idx, columnas, ncols):
    T, M = R.T, R.M
    en = d["entregables"]
    titulo = en.get("titulo") or "Todo lo que {cliente_corto} recibe."
    sub = en.get("subtitulo") or SUB_ENTREGABLES
    compacto = bool(en.get("compacto"))
    sub_html = M(sub, "entregables.subtitulo")
    sub_html = re.sub(r"(Lo que se llevan)", r'<span class="nw">\1</span>', sub_html, count=1, flags=re.I)
    barras = ""
    por_car = {}
    orden = []
    for col in columnas:
        if col["carril"]["id"] not in por_car:
            por_car[col["carril"]["id"]] = [col["carril"], 0]
            orden.append(col["carril"]["id"])
        por_car[col["carril"]["id"]][1] += 1
    for cid in orden:
        c, k = por_car[cid]
        n = R.agg["carril"][cid]["n"]
        barras += '        <span class="dc %s" style="grid-column: span %d">%s · %d %s</span>\n' % (
            COLORES[c["color"]], k, T(c["nombre"], "carriles.nombre"), n, plural(n, "entregable", "entregables"))
    min_first = {}
    idx_cols = {}
    for i, col in enumerate(columnas):
        idx_cols.setdefault(col["carril"]["id"], []).append(i)
    cpn = (ancho_col(ncols) - 30) / 6.4
    for cid, lst in idx_cols.items():
        ls = [lineas_wrap(nombre_catalogo(columnas[i]["areas"][0]), cpn) for i in lst]
        if len(set(ls)) > 1:
            mx = max(ls)
            for i, l in zip(lst, ls):
                if l < mx:
                    min_first[i] = True
    cols_html = ""
    for i, col in enumerate(columnas):
        areas_html = ""
        for j, a in enumerate(col["areas"]):
            n = R.agg["area"][a["id"]][0]
            style = ' style="min-height:2.4em"' if (j == 0 and min_first.get(i)) else ""
            li = "".join("              <li>%s</li>\n" % T(s["entregable"], "areas.soluciones.entregable") for s in a["soluciones"])
            areas_html += (
                '          <div class="da">\n'
                '            <p class="da-name"%s>%s <i>%d</i></p>\n'
                "            <ul>\n%s            </ul>\n"
                "          </div>\n" % (style, T(nombre_catalogo(a), "areas.nombre"), n, li)
            )
        cols_html += '        <div class="deliv-col %s">\n%s        </div>\n\n' % (COLORES[col["carril"]["color"]], areas_html)
    return (
        '    <!-- 5 · Entregables (catálogo + piezas transversales) -->\n'
        '    <section class="slide s-deliv%s">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Entregables</p>\n'
        '      <div class="deliv-head">\n'
        "        <h2>%s</h2>\n"
        '        <p class="deliv-sub">%s</p>\n'
        "      </div>\n\n"
        '      <div class="deliv-carriles" style="--ncols:%d">\n%s      </div>\n\n'
        '      <div class="deliv-cols" style="--ncols:%d">\n\n%s      </div>\n\n'
        '      <div class="deliv-band">\n'
        '        <div class="db-card db-1">\n'
        '          <span class="db-label">%s</span>\n'
        "        </div>\n"
        '        <div class="db-card db-2">\n'
        '          <span class="db-label">%s</span>\n'
        "        </div>\n"
        "      </div>\n"
        "      <!-- Cajas multiline editables (vacías en HTML: el contenido vive dentro del AcroForm /V). -->\n"
        '      <div class="multi-box db-box db-box-1" data-field="Entregables"></div>\n'
        '      <div class="multi-box db-box db-box-2" data-field="Acreditacion"></div>\n\n%s'
        "    </section>\n"
        % (" compact" if compacto else "", R.contador(idx), idx, T(titulo, "entregables.titulo"), sub_html,
           ncols, barras, ncols, cols_html, T(en.get("etiqueta_transversales") or "Entregables transversales", "entregables.etiqueta_transversales"),
           T(en.get("etiqueta_valor") or "Valor inmediato", "entregables.etiqueta_valor"), foot(R, "oscuro"))
    )


# ----------------------------------------------------------------------------------------------
# Slide de retorno esperado (opcional): método de cálculo o cifras por área. Sin estudios ni citas de la web.
# ----------------------------------------------------------------------------------------------
def fmt_es(x):
    """Número con separador de miles «.» y decimal «,» (1 decimal si no es entero)."""
    txt = "{:,.0f}".format(x) if abs(x - round(x)) < 1e-9 else "{:,.1f}".format(x)
    return txt.replace(",", "X").replace(".", ",").replace("X", ".")


def es_num(v, minimo=None):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v == v and abs(v) != float("inf") and (minimo is None or v >= minimo)


def cfg_retorno(d):
    """Configuración resuelta del módulo retorno (textos aún con tokens). None si el módulo no está activo."""
    r = d.get("retorno")
    if not isinstance(r, dict):
        return None
    fund = d.get("division") == "fundacion"
    pos = bool(r.get("posiciones"))
    modo = r.get("modo") or "metodo"
    if r.get("pasos"):
        pasos = [(x.get("titulo") or "", x.get("texto") or "") for x in r["pasos"] if isinstance(x, dict)]
    else:
        pasos = list(PASOS_BASE) + [PASO_CAPACIDAD if fund else PASO_DINERO] + ([PASO_POSICIONES] if pos else [])
    if r.get("metas"):
        metas = [(x.get("dias") or "", x.get("texto") or "") for x in r["metas"] if isinstance(x, dict)]
    else:
        metas = list(METAS_BASE) + [("90 días", META90[(fund, pos)])]
    destino_def = not r.get("destino")
    if destino_def:
        destino = list(DESTINO_FUND if fund else DESTINO_EDU)
    else:
        destino = [(x.get("rotulo") or "", x.get("texto") or "") for x in r["destino"] if isinstance(x, dict)]
    if pos:
        titulo = "Retorno esperado: tiempo, posiciones y dinero."
        resto = "el tiempo recuperado medido, su valor en dinero y las posiciones equivalentes, área por área."
    elif fund:
        titulo = "Retorno esperado: tiempo y capacidad."
        resto = "el tiempo recuperado medido y la capacidad liberada, área por área."
    else:
        titulo = "Retorno esperado: tiempo y dinero."
        resto = "el tiempo recuperado medido y su valor en dinero, área por área."
    gancho_def = "Hacia la semana {semana_medicion} ({semanas_txt} de construcción más 90 días de seguimiento), {cliente_corto} contará con " + resto
    return {
        "modo": modo, "pos": pos, "fund": fund, "pasos": pasos, "metas": metas, "destino": destino, "destino_def": destino_def,
        "pasos_def": not r.get("pasos"),
        "titulo": r.get("titulo") or titulo,
        "subtitulo": r.get("subtitulo") or (
            "Cifras de {cliente_corto} por área, a confirmar con la línea base de la semana 1, con metas a 30, 60 y 90 días."
            if modo == "cifras" else
            "Se calcula con los datos de cada área, se confirma con la línea base de la semana 1 y se mide con metas a 30, 60 y 90 días."),
        "etiqueta_pasos": r.get("etiqueta_pasos") or "Cómo se calcula, por área y por proceso",
        "etiqueta_metas": r.get("etiqueta_metas") or "Metas, desde el cierre de cada área",
        "etiqueta_destino": r.get("etiqueta_destino") or "Hacia dónde va el tiempo recuperado",
        "gancho": r.get("gancho") or gancho_def, "gancho_def": not r.get("gancho"),
        "nota_datos": r.get("nota_datos") or "",
    }


def filas_cifras(d):
    """Filas y totales de la tabla del modo cifras (números ya calculados a partir de los datos)."""
    r = d.get("retorno") or {}
    costo = r.get("costo_hora_usd") if es_num(r.get("costo_hora_usd")) else 0
    nombres = {}
    for a in d.get("areas") or []:
        if isinstance(a, dict):
            nombres[a.get("id")] = a.get("nombre")
            nombres[a.get("nombre")] = a.get("nombre")
    filas = []
    for x in r.get("areas") or []:
        if not isinstance(x, dict):
            continue
        num = lambda k: x.get(k) if es_num(x.get(k)) else 0
        ha, hc = num("horas_actuales"), num("horas_con_solucion")
        rec = ha - hc
        filas.append({"nombre": x.get("etiqueta") or nombres.get(x.get("area"), x.get("area")), "tipo": x.get("tipo_dato"),
                      "tipo_pos": x.get("tipo_dato_posiciones") or x.get("tipo_dato"), "extra": num("retrabajo_usd") + num("tardios_usd"),
                      "ha": ha, "hc": hc, "rec": rec, "valor": rec * costo + num("retrabajo_usd") + num("tardios_usd"),
                      "pos_hoy": num("posiciones_hoy"), "pos_red": num("posiciones_reducibles"), "pos_evi": num("posiciones_evitables"),
                      "costo_anual": num("costo_anual_usd")})
    tot = dict((k, sum(f[k] for f in filas)) for k in ("ha", "hc", "rec", "valor", "pos_hoy", "pos_red", "pos_evi", "costo_anual"))
    return filas, tot


def etiqueta_fila(f, pos):
    """Nombre del área con su marca de estimación (dentro del mismo paréntesis si ya trae cobertura)."""
    nombre = str(f["nombre"])
    marca = None
    if f["tipo"] == "estimacion":
        marca = "estimación"
    elif pos and f["tipo_pos"] == "estimacion":
        marca = "posiciones: estimación"
    if not marca:
        return esc(nombre)
    if nombre.endswith(")"):
        return esc(nombre[:-1] + ", " + marca + ")")
    return esc(nombre) + " <em>(%s)</em>" % marca


def nota_auto(d, c, filas):
    """Línea de base bajo la tabla: con qué costo hora se calculó el valor, qué tipo de dato es cada fila y qué decide el cliente."""
    r = d["retorno"]
    partes = ["Valor del tiempo recuperado a USD %s por hora; no es ahorro en caja." % fmt_es(r.get("costo_hora_usd") or 0)]
    n_ext = sum(1 for f in filas if f["extra"] > 0)
    if n_ext:
        partes.append("Incluye retrabajo y pagos o cobros tardíos en %d %s." % (n_ext, plural(n_ext, "área", "áreas")))
    cuenta = dict((k, sum(1 for f in filas if f["tipo"] == k)) for k in TIPOS_DATO)
    etiquetas = {"medido": ("medida", "medidas"), "declarado": ("declarada por el área", "declaradas por el área"), "estimacion": ("estimación", "estimaciones")}
    trozos = ["%d %s" % (cuenta[k], plural(cuenta[k], *etiquetas[k])) for k in ("medido", "declarado", "estimacion") if cuenta[k]]
    if trozos:
        partes.append("Filas: " + ", ".join(trozos) + ".")
    if c["pos"]:
        hpp = r.get("horas_por_posicion")
        partes.append("Una posición equivale a %s h productivas al mes. El tiempo recuperado puede reasignarse, absorber más volumen o evitar contrataciones: lo decide {cliente_corto}." % fmt_es(hpp) if es_num(hpp) else
                      "El tiempo recuperado puede reasignarse, absorber más volumen o evitar contrataciones: lo decide {cliente_corto}.")
    return " ".join(partes)


def estimar_s6(d, R):
    """Holgura estimada (px) entre el último bloque y la banda final de la slide de retorno. Calibrado con DUSA 2026-10-05
    (6 pasos: panel 333 px; franja de destino 101 px; holgura real ~30 px) y con tablas de 3 a 11 filas."""
    c = cfg_retorno(d)
    tk = lambda x: sin_marcado(R.t(x, "retorno"))
    cabecera = 150 + 38 * (lineas_wrap(tk(c["titulo"]), 52) - 1) + 21 * (lineas_wrap(tk(c["subtitulo"]), 126) - 1)
    if c["modo"] == "cifras":
        filas, _ = filas_cifras(d)

        def alto_fila(f):
            etq = str(f["nombre"]) + (" " + "x" * 11 if f["tipo"] == "estimacion" else "")
            return 8 + 17.4 * lineas_wrap(etq, 30)
        cab_t = 44 if c["pos"] else 33
        nota = tk(nota_auto(d, c, filas)) + " " + tk(c["nota_datos"])
        panel = 54 + cab_t + sum(alto_fila(f) for f in filas) + 25.4 + 13.5 * max(1, lineas_wrap(nota, 118))
    else:
        panel = 41 + 17 + sum(26.6 + lineas_wrap(tk(x), 100) * 15.64 for _t, x in c["pasos"])
    cpl_meta = 45 if c["modo"] == "cifras" else 53
    metas = 15 + 20 + sum(max(78, 47 + lineas_wrap(tk(x), cpl_meta) * 16.6) for _t, x in c["metas"]) + 10 * len(c["metas"])
    cuerpo = max(panel, metas)
    dest = 0
    if c["modo"] != "cifras":
        dest = 18 + 20 + 4 + 8 + 9 + 15.2 + 3 + max(lineas_wrap(tk(x), 52) for _r, x in c["destino"]) * 15.64
    gancho_h = 28 + lineas_wrap(tk(c["gancho"]), 102) * 23.75
    return (794 - 62 - gancho_h) - (cabecera + cuerpo + dest)


def validar_retorno(d, ctx, agg, rep, rs):
    r = d.get("retorno")
    if r is None or not isinstance(r, dict):
        return
    c = cfg_retorno(d)
    modo = c["modo"]
    if modo not in ("metodo", "cifras"):
        rep.err("retorno.modo", "debe ser 'metodo' o 'cifras'; recibido %r" % (r.get("modo"),))
        return
    if not isinstance(ctx.get("semana_medicion"), int):
        rep.err("retorno", "no se pudo calcular la semana de medición porque falta ruta.semanas_total (o define retorno.semana_medicion)")
    elif "{semana_medicion}" in c["gancho"] or "semana" in c["gancho"].lower():
        if es_num(r.get("semana_medicion")):
            rep.aviso("retorno.semana_medicion", "semana de medición fijada a mano en %s: confirmarla con el equipo de servicio antes de enviar" % ctx.get("semana_medicion"))
        else:
            rep.aviso("retorno", "«Hacia la semana %s» es aritmética (semanas de construcción + 90 días de seguimiento, ~13 semanas): confirmarla con el equipo de servicio antes de enviar" % ctx.get("semana_medicion"))
    for nombre, lst, n_ok in (("pasos", r.get("pasos"), None), ("metas", r.get("metas"), 3), ("destino", r.get("destino"), 3)):
        if lst is not None and n_ok and len(lst) != n_ok:
            rep.err("retorno.%s" % nombre, "debe tener exactamente %d elementos; hay %d" % (n_ok, len(lst)))
    if r.get("pasos") is not None and not (4 <= len(r["pasos"]) <= 7):
        rep.err("retorno.pasos", "se necesitan 4 a 7 pasos; hay %d" % len(r["pasos"]))
    for nombre, par in (("pasos", c["pasos"]), ("metas", c["metas"]), ("destino", c["destino"])):
        for i, (a, b) in enumerate(par):
            if not a or not b:
                rep.err("retorno.%s[%d]" % (nombre, i), "faltan los dos textos (%s)" % ("titulo y texto" if nombre == "pasos" else "dias y texto" if nombre == "metas" else "rotulo y texto"))
    # Textos: sin estudios ni referencias a la web (decisión del 2026-10-05), sin «garantizado» y límites de caja
    textos = [("titulo", c["titulo"]), ("subtitulo", c["subtitulo"]), ("gancho", c["gancho"]), ("nota_datos", c["nota_datos"])]
    textos += [("pasos[%d]" % i, t + " " + x) for i, (t, x) in enumerate(c["pasos"])]
    textos += [("metas[%d]" % i, t + " " + x) for i, (t, x) in enumerate(c["metas"])]
    textos += [("destino[%d]" % i, t + " " + x) for i, (t, x) in enumerate(c["destino"])]
    for donde, x in textos:
        m = RE_RET_ERR.search(rs(x))
        if m:
            rep.err("retorno.%s" % donde, "la slide de retorno no cita estudios, informes ni referencias de la web, ni promete retorno («%s»): usar solo el método y los datos del cliente" % m.group(0))
            continue
        m = RE_RET_AV.search(rs(x))
        if m and (modo == "metodo" or not re.match(r"\d|USD|US\$|\$", m.group(0))):
            rep.aviso("retorno.%s" % donde, "«%s»: en el modo método no van cifras ni porcentajes propios, y «estudio»/«web»/«internet» solo se admiten como vocabulario del cliente (p. ej. «estudio de tiempos»)" % m.group(0))
    if len(rs(c["titulo"])) > 52:
        rep.aviso("retorno.titulo", "%d caracteres: máx. ~50 para una línea" % len(rs(c["titulo"])))
    if len(rs(c["subtitulo"])) > 126:
        rep.aviso("retorno.subtitulo", "%d caracteres: máx. ~125 para una línea" % len(rs(c["subtitulo"])))
    if len(rs(c["gancho"])) > 200:
        rep.aviso("retorno.gancho", "%d caracteres: máx. ~190 (2 líneas)" % len(rs(c["gancho"])))
    for i, (t, x) in enumerate(c["pasos"]):
        if len(rs(t)) > 40:
            rep.aviso("retorno.pasos[%d]" % i, "título de %d caracteres: máx. ~40" % len(rs(t)))
        if len(rs(x)) > 190:
            rep.aviso("retorno.pasos[%d]" % i, "texto de %d caracteres: máx. ~190 (2 líneas)" % len(rs(x)))
    for i, (t, x) in enumerate(c["metas"]):
        tope_meta = 90 if modo == "cifras" else 110
        if len(rs(x)) > tope_meta:
            rep.aviso("retorno.metas[%d]" % i, "texto de %d caracteres: máx. ~%d (2 líneas)" % (len(rs(x)), tope_meta))
    for i, (t, x) in enumerate(c["destino"]):
        if len(rs(t)) > 34:
            rep.aviso("retorno.destino[%d]" % i, "rótulo de %d caracteres: máx. ~34" % len(rs(t)))
        if len(rs(x)) > 200:
            rep.aviso("retorno.destino[%d]" % i, "texto de %d caracteres: máx. ~200 (4 líneas)" % len(rs(x)))
    # Posiciones y nómina: solo con aval registrado
    if c["pos"]:
        av = r.get("aval_posiciones")
        if not isinstance(av, dict) or not all(isinstance(av.get(k), str) and av.get(k).strip() for k in ("quien", "fecha", "medio")):
            rep.err("retorno.aval_posiciones", "con posiciones=true hace falta registrar el aval del cliente: aval_posiciones = {quien, fecha, medio} (quién lo aceptó, cuándo y por qué medio)")
        else:
            rep.aviso("retorno.posiciones", "posiciones=true plantea reducir o evitar posiciones; aval registrado: %s, %s (%s). Confirmar que sigue vigente antes de enviar" % (av["quien"], av["fecha"], av["medio"]))
    if modo == "metodo":
        if r.get("areas") or r.get("costo_hora_usd") is not None:
            rep.aviso("retorno", "areas/costo_hora_usd se ignoran en modo 'metodo' (usar modo 'cifras' para mostrar la tabla)")
        if c["destino_def"]:
            rep.aviso("retorno.destino", "se usan los textos genéricos: citar al menos un ejemplo real de reenfoque con las cifras del levantamiento (portada.hechos) en la tarjeta «Trabajo reenfocado»")
        if c["pasos_def"] and (d.get("portada") or {}).get("hechos"):
            rep.aviso("retorno.pasos", "pasos genéricos: los mismos para cualquier cliente; considerar un ejemplo propio en el paso 1 (un proceso real de portada.hechos)")
    else:
        if c["destino_def"] is False:
            rep.aviso("retorno.destino", "en modo 'cifras' no se muestra la franja de destino (la tabla ocupa su lugar): se ignora")
        costo = r.get("costo_hora_usd")
        if not es_num(costo) or costo <= 0:
            rep.err("retorno.costo_hora_usd", "en modo 'cifras' hace falta el costo hora de referencia (USD, > 0) validado con el cliente")
        if len(rs(c["nota_datos"])) < 30:
            rep.err("retorno.nota_datos", "en modo 'cifras' hace falta una nota que diga de dónde salen los datos y cuáles son estimaciones (≥ 30 caracteres)")
        if len(rs(c["nota_datos"])) > 230:
            rep.aviso("retorno.nota_datos", "%d caracteres: máx. ~210" % len(rs(c["nota_datos"])))
        od = r.get("origen_datos")
        if not isinstance(od, dict) or not all(isinstance(od.get(k), str) and len(od.get(k).strip()) >= 3 for k in ("documento", "fecha", "validado_por")):
            rep.err("retorno.origen_datos", "en modo 'cifras' hace falta la procedencia verificable: origen_datos = {documento, fecha, validado_por} (qué documento o sesión, cuándo y quién del cliente lo validó)")
        hpp = r.get("horas_por_posicion")
        if c["pos"] and (not es_num(hpp) or hpp <= 0):
            rep.err("retorno.horas_por_posicion", "con posiciones=true en modo 'cifras' hace falta las horas productivas de una posición al mes (> 0, validadas con el cliente)")
        filas = r.get("areas") or []
        if not filas:
            rep.err("retorno.areas", "en modo 'cifras' hace falta al menos un área con datos")
        if len(filas) > 11:
            rep.err("retorno.areas", "máximo 11 filas; hay %d" % len(filas))
        conocidos = set()
        for a in d.get("areas") or []:
            if isinstance(a, dict):
                conocidos.add(a.get("id"))
                conocidos.add(a.get("nombre"))
        vistas = set()
        claves_pos = ("posiciones_hoy", "posiciones_reducibles", "costo_anual_usd")
        for i, x in enumerate(filas):
            if not isinstance(x, dict):
                continue
            donde = "retorno.areas[%d]" % i
            if x.get("area") not in conocidos:
                rep.err(donde, "el área %r no existe en areas (usar el id o el nombre exacto)" % (x.get("area"),))
            if x.get("area") in vistas:
                rep.err(donde, "área repetida: %r" % (x.get("area"),))
            vistas.add(x.get("area"))
            if x.get("tipo_dato") not in TIPOS_DATO:
                rep.err(donde, "tipo_dato debe ser 'medido', 'declarado' o 'estimacion' (las estimaciones se indican como tales); recibido %r" % (x.get("tipo_dato"),))
            if x.get("tipo_dato_posiciones") is not None and x.get("tipo_dato_posiciones") not in TIPOS_DATO:
                rep.err(donde, "tipo_dato_posiciones debe ser 'medido', 'declarado' o 'estimacion'; recibido %r" % (x.get("tipo_dato_posiciones"),))
            for k in ("horas_actuales", "horas_con_solucion"):
                if not es_num(x.get(k), 0):
                    rep.err(donde + "." + k, "debe ser un número finito >= 0 (horas al mes); recibido %r" % (x.get(k),))
            ha, hc = x.get("horas_actuales"), x.get("horas_con_solucion")
            if es_num(ha) and es_num(hc):
                if hc > ha:
                    rep.err(donde, "las horas con la solución (%s) no pueden superar a las horas actuales (%s)" % (hc, ha))
                elif ha > 0 and hc == 0:
                    rep.aviso(donde, "horas con la solución = 0: ¿el proceso desaparece por completo? Confirmar la meta")
                elif ha > 0 and (ha - hc) / ha > 0.9:
                    rep.aviso(donde, "se recupera más del 90 %% de las horas (%.0f %%): revisar unidades (horas vs minutos) y que sea una meta realista" % (100 * (ha - hc) / ha))
            for k in ("retrabajo_usd", "tardios_usd", "posiciones_evitables") + claves_pos:
                if k in x and not es_num(x[k], 0):
                    rep.err(donde + "." + k, "debe ser un número finito >= 0; recibido %r" % (x[k],))
            tiene = [k for k in claves_pos if k in x]
            if c["pos"] and len(tiene) != 3:
                rep.err(donde, "con retorno.posiciones=true cada área necesita posiciones_hoy, posiciones_reducibles y costo_anual_usd")
            if not c["pos"] and (tiene or "posiciones_evitables" in x):
                rep.aviso(donde, "posiciones_* y costo_anual_usd se ignoran porque retorno.posiciones es false")
            if "posiciones_hoy" in x and es_num(x.get("posiciones_reducibles")) and x["posiciones_reducibles"] > x["posiciones_hoy"]:
                rep.err(donde, "las posiciones que se reducen no pueden superar las posiciones que representa hoy el trabajo manual")
            if c["pos"] and es_num(hpp) and hpp > 0 and es_num(ha) and es_num(hc):
                equiv = (ha - hc) / hpp
                total_pos = (x.get("posiciones_reducibles") or 0) + (x.get("posiciones_evitables") or 0)
                if es_num(total_pos) and equiv > 0 and total_pos > equiv * 1.25:
                    rep.aviso(donde, "se plantean %s posiciones a reducir o evitar y las horas recuperadas equivalen a %.1f (a %s h por posición): conciliar" % (fmt_es(total_pos), equiv, fmt_es(hpp)))
        sin_dato = [a.get("nombre") for a in d.get("areas") or [] if isinstance(a, dict) and a.get("nombre") not in vistas and a.get("id") not in vistas]
        if filas and sin_dato:
            rep.aviso("retorno.areas", "áreas sin fila de datos (no aparecerán en la tabla; el total se rotula con la cobertura): %s" % ", ".join(sin_dato[:6]) + ("..." if len(sin_dato) > 6 else ""))


def s6_retorno(d, R, idx):
    c = cfg_retorno(d)
    T, M = R.T, R.M
    modo = c["modo"]
    if modo == "cifras":
        filas, tot = filas_cifras(d)
        pos = c["pos"]
        cab = ["Área", "Horas actuales al mes", "Horas con la solución (meta)", "Horas recuperadas al mes", "Valor del tiempo (USD/mes)"]
        if pos:
            cab += ["Posiciones hoy", "A reducir o evitar", "Costo anual (USD)"]
        th = "".join("<th>%s</th>" % esc(x) for x in cab)
        trs = ""
        for f in filas:
            celdas = [fmt_es(f["ha"]), fmt_es(f["hc"]), "<b>%s</b>" % fmt_es(f["rec"]), fmt_es(f["valor"])]
            if pos:
                celdas += [fmt_es(f["pos_hoy"]), fmt_es(f["pos_red"] + f["pos_evi"]), fmt_es(f["costo_anual"])]
            trs += "              <tr><td>%s</td>%s</tr>\n" % (etiqueta_fila(f, pos), "".join("<td>%s</td>" % x for x in celdas))
        n_areas = len([a for a in d.get("areas") or [] if isinstance(a, dict)])
        rotulo_tot = "Total" if len(filas) >= n_areas else "Total (%d de %d áreas)" % (len(filas), n_areas)
        celdas = [fmt_es(tot["ha"]), fmt_es(tot["hc"]), fmt_es(tot["rec"]), fmt_es(tot["valor"])]
        if pos:
            celdas += [fmt_es(tot["pos_hoy"]), fmt_es(tot["pos_red"] + tot["pos_evi"]), fmt_es(tot["costo_anual"])]
        trs += '              <tr class="tot"><td>%s</td>%s</tr>\n' % (esc(rotulo_tot), "".join("<td>%s</td>" % x for x in celdas))
        etq = "Retorno esperado por área" if c["etiqueta_pasos"] == "Cómo se calcula, por área y por proceso" else c["etiqueta_pasos"]
        nota = nota_auto(d, c, filas) + (" " + c["nota_datos"] if c["nota_datos"] else "")
        izq = (
            '        <div class="roi-panel">\n'
            '          <p class="roi-panel-title">%s</p>\n'
            '          <table class="roi-tabla">\n            <thead><tr>%s</tr></thead>\n            <tbody>\n%s            </tbody>\n          </table>\n'
            '          <p class="roi-nota-datos">%s</p>\n'
            "        </div>\n" % (T(etq, "retorno.etiqueta_pasos"), th, trs, T(nota, "retorno.nota_datos"))
        )
        dest = ""
    else:
        li = "".join("            <li><b>%s</b><span>%s</span></li>\n" % (T(t, "retorno.pasos.titulo"), M(x, "retorno.pasos")) for t, x in c["pasos"])
        izq = (
            '        <div class="roi-panel">\n'
            '          <p class="roi-panel-title">%s</p>\n'
            '          <ol class="roi-steps">\n%s          </ol>\n'
            "        </div>\n" % (T(c["etiqueta_pasos"], "retorno.etiqueta_pasos"), li)
        )
        items = "".join(
            '          <div class="rd-item"><b>%s</b><p>%s</p></div>\n' % (T(t, "retorno.destino.rotulo"), M(x, "retorno.destino"))
            for t, x in c["destino"]
        )
        dest = (
            '      <div class="roi-dest-wrap">\n'
            '        <p class="roi-dest-title">%s</p>\n'
            '        <div class="roi-dest">\n%s        </div>\n'
            "      </div>\n\n" % (T(c["etiqueta_destino"], "retorno.etiqueta_destino"), items)
        )
    metas = "".join(
        '          <div class="roi-card">\n            <b>%s</b>\n            <p>%s</p>\n          </div>\n' % (T(t, "retorno.metas.dias"), M(x, "retorno.metas"))
        for t, x in c["metas"]
    )
    return (
        '    <!-- %d · Retorno esperado (%s). Sin estudios ni citas externas. -->\n'
        '    <section class="slide s-roi%s">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Retorno</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="roi-body">\n%s\n'
        '        <div class="roi-right">\n'
        '          <p class="roi-right-title">%s</p>\n%s        </div>\n'
        "      </div>\n\n%s"
        '      <div class="roi-hook"><p>%s</p></div>\n\n%s'
        "    </section>\n"
        % (idx, "método de cálculo" if modo == "metodo" else "cifras por área", " roi-cifras" if modo == "cifras" else "", R.contador(idx), idx,
           T(c["titulo"], "retorno.titulo"), M(c["subtitulo"], "retorno.subtitulo"), izq,
           T(c["etiqueta_metas"], "retorno.etiqueta_metas"), metas, dest, T(c["gancho"], "retorno.gancho"), foot(R, "claro"))
    )


def render_html(d, R, columnas, ncols):
    total = R.total
    cab = (
        "<!doctype html>\n<!--\n"
        "  Propuesta · %s · Servicio de Habilidades (%s)\n"
        "  División: %s · Servicio: Habilidades (§4.1a) · Alianza: %s\n"
        "  GENERADO por scripts/generar-habilidades-compacto.py (plantilla %s) desde datos.json.\n"
        "  No editar a mano: editar datos.json y regenerar. Estilos propios del deck: overrides.css.\n"
        "  Fuente del insumo: %s\n\n"
        "  Formato compacto de %d slides (distinto del deck canónico de ~13):\n"
        "    1 Portada con punto de dolor · 2 Alcance · 3 Ruta · %s%s\n"
        "  Marcadores de detección de AcroForms (agregar-campo-precio.py), por página: «Propuesta Económica»\n"
        "  solo en la slide de inversión; «Lo que se llevan» y «Entregables» solo en la de entregables.\n"
        "  Campos AcroForm: %s. Se reposicionan con scripts/customize-habilidades-compacto.py.\n"
        "-->\n"
        % (cm(d["cliente"]["nombre"]), cm(d["cliente"]["codigo"]), R.div_nombre, "sí" if d.get("alianza") else "no", VERSION_PLANTILLA,
           cm(d.get("fuente_insumo") or "(no indicado)"), total, "4 Inversión · 5 Entregables" if R.con_precio else "4 Entregables",
           (" · %d Retorno esperado" % total) if d.get("retorno") else "",
           "Programa, Notas, PrecioBase, Descuento, PrecioTotal (inversión) y Entregables, Acreditacion (entregables)" if R.con_precio
           else "Entregables, Acreditacion (entregables); sin hoja de inversión por ser Fundación")
    )
    head = (
        '<html lang="es">\n<head>\n  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "  <title>Propuesta · %s · Intezia %s</title>\n"
        '  <link rel="stylesheet" href="%s">\n'
        '  <link rel="stylesheet" href="%s">\n'
        '  <link rel="stylesheet" href="overrides.css">\n'
        "</head>\n<body>\n\n  <main class=\"deck\">\n\n" % (esc(d["cliente"]["nombre"]), R.div_nombre, R.rel_base, CSS_NAME)
    )
    cuerpo = s1_portada(d, R) + "\n" + s2_alcance(d, R) + "\n" + s3_ruta(d, R) + "\n"
    idx = 4
    if R.con_precio:
        cuerpo += s4_inversion(d, R, 4) + "\n"
        idx = 5
    cuerpo += s5_entregables(d, R, idx, columnas, ncols)
    if d.get("retorno"):
        cuerpo += "\n" + s6_retorno(d, R, idx + 1)
    return cab + head + cuerpo + "\n  </main>\n</body>\n</html>\n"


# ----------------------------------------------------------------------------------------------
# AcroForms, programa.md, meta, brief
# ----------------------------------------------------------------------------------------------
def con_vineta(x):
    x = x.strip()
    return x if x.startswith("•") else "• " + x


def construir_acroforms(d, R):
    t = R.t
    en = d["entregables"]
    out = {
        "Entregables": [con_vineta(sin_marcado(t(x, "entregables.transversales"))) for x in en["transversales"]],
        "Acreditacion": [con_vineta(sin_marcado(t(x, "entregables.valor_inmediato"))) for x in en["valor_inmediato"]],
    }
    if R.con_precio:
        inv = d.get("inversion") or {}
        out["Programa"] = [sin_marcado(t(x, "inversion.programa")) for x in (inv.get("programa") or programa_auto(d, R))]
        out["Notas"] = [sin_marcado(t(x, "inversion.notas")) for x in (inv.get("notas") or [])] or ""
    return out


def lineas_caja(items, nombre):
    """Líneas que ocupa la lista en la caja del PDF (exacto con las métricas de acroform_appearance si hay pypdf)."""
    ancho, size, bold, _ = CAJAS_PDF[nombre]
    util = ancho - 4.0  # 2 pt de margen por lado
    if PDF_EXACTO:
        W, D = (_WB, _DWB) if bold else (_WR, _DWR)
        return sum(len(_wrap_pdf(x, util, size, W, D)) for x in items)
    cpl = util / (size * (0.524 if bold else 0.50))
    return sum(lineas_wrap(x, cpl) for x in items)


def validar_acroforms(af, rep):
    for k, v in af.items():
        for x in (v if isinstance(v, list) else [v]):
            if not isinstance(x, str):
                continue
            if re.search(r"[\x00-\x1f\x7f]", x):
                rep.err("acroforms.%s" % k, "contiene un salto de línea o carácter de control (cada línea va como un elemento aparte de la lista): «%s»" % x[:40].replace("\n", "\\n"))
            try:
                x.encode("cp1252")
            except UnicodeEncodeError as e:
                rep.err("acroforms.%s" % k, "carácter no imprimible en el PDF (%r): usar solo caracteres Latin-1/WinAnsi" % x[e.start:e.start + 1])
            if re.search(r"[{}]|\*\*", x):
                rep.err("acroforms.%s" % k, "quedó un {token}, una llave suelta o «**» sin resolver en «%s»" % x[:50])
            if RE_GUION_LARGO.search(x) or RE_GUION_MEDIO.search(x):
                rep.err("acroforms.%s" % k, "guion largo/mediano en «%s» (§4.13)" % x[:40])
            if re.search(r"\bcohorts?\b", x, re.I):
                rep.err("acroforms.%s" % k, "anglicismo «cohort» (usar «grupos»)")
            if RE_FECHA.search(x):
                rep.aviso("acroforms.%s" % k, "contiene una fecha o mes calendario: «%s»" % x[:50])
    for k, (ancho, size, bold, maxl) in CAJAS_PDF.items():
        v = af.get(k)
        if not v:
            continue
        items = v if isinstance(v, list) else [v]
        if any(re.search(r"[\x00-\x1f\x7f]", x) for x in items):
            continue
        n = lineas_caja(items, k)
        if n > maxl:
            rep.err("acroforms.%s" % k, "ocupa %s%d líneas: la caja admite %d (%s). %s" % (
                "" if PDF_EXACTO else "~", n, maxl, "exacto, métricas del PDF" if PDF_EXACTO else "estimado; instalar pypdf para la medida exacta",
                {"Programa": "Definir inversion.programa más corto", "Notas": "Acortar inversion.notas"}.get(k, "Acortar las viñetas (3 viñetas de ≤ 60 caracteres es lo ideal)")))
        elif k in ("Entregables", "Acreditacion"):
            for x in items:
                if lineas_caja([x], k) > 1:
                    rep.aviso("acroforms.%s" % k, "la viñeta se parte en 2 líneas (%d caracteres): %s" % (len(x), x[:40]))


def construir_programa_md(d, R):
    t = R.t
    L = []
    L.append("# Programa interno · %s · Servicio de Habilidades (%s)\n" % (d["cliente"]["nombre"], d["cliente"]["codigo"]))
    L.append("> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.")
    if d.get("fuente_insumo"):
        L.append("> Fuente del insumo: %s." % d["fuente_insumo"])
    L.append("")
    L.append("## 1. Resumen\n")
    L.append("- **%s en %s%s**, **%d h** de sesión, más seguimiento a %s." % (
        R.ctx["n_total_txt"], R.ctx["n_areas_txt"], (" (más %d %s)" % (R.agg["n_bases"], plural(R.agg["n_bases"], "proceso base", "procesos base"))) if R.agg["n_bases"] else "",
        R.agg["h_total"], d["seguimiento"]["rango"]))
    for c in d["carriles"]:
        ca = R.agg["carril"].get(c["id"])
        if ca:
            L.append("- Carril **%s**: %d %s, %d h." % (c["nombre"], ca["n"], plural(ca["n"], "solución", "soluciones"), ca["h"]))
    L.append("- Horas por fase: " + " · ".join("%s %d h (%d sol.)" % (f["id"], R.agg["fase"].get(f["id"], [0, 0])[1], R.agg["fase"].get(f["id"], [0, 0])[0]) for f in d["fases"]) + ".")
    L.append("")
    L.append("## 2. Frentes y ruta\n")
    L.append("| Frente | Carril | Áreas | Semanas | Horas | Soluciones |\n|---|---|---|---|---|---|")
    carr = dict((c["id"], c) for c in d["carriles"])
    for fr in d["frentes"]:
        n, h = R.agg["frente"].get(fr["id"], [0, 0])
        nombres = ", ".join(a["nombre"] for a in d["areas"] if a["frente"] == fr["id"])
        L.append("| %s | %s | %s | %s | %d | %d |" % (cel(fr["id"]), cel(carr[fr["carril"]]["nombre"]), cel(nombres), cel(fr["semanas"]), h, n))
    L.append("")
    fcols = [f for f in d["fases"] if f.get("id") != "F0"]
    L.append("| Frente | " + " | ".join(cel("%s (%s)" % (f["titulo"], f["rango"])) for f in fcols) + " |")
    L.append("|---|" + "---|" * len(fcols))
    for fr in d["frentes"]:
        celdas = []
        for f in fcols:
            n, h = R.agg["celda"].get((fr["id"], f["id"]), [0, 0])
            celdas.append("%d h · %d sol." % (h, n))
        L.append("| %s | %s |" % (fr["id"], " | ".join(celdas)))
    L.append("")
    for h in d["ruta"]["hitos"]:
        L.append("- **%s**: %s" % (sin_marcado(t(h["titulo"], "ruta.hitos")), sin_marcado(t(h["texto"], "ruta.hitos"))))
    L.append("")
    L.append("## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)\n")
    for a in d["areas"]:
        n, h = R.agg["area"][a["id"]]
        L.append("### %s · %d %s · %d h · carril %s · frente %s%s\n" % (
            cel(a["nombre"]), n, plural(n, "solución", "soluciones"), h, carr[a["carril"]]["nombre"], a["frente"], " · proceso base" if a.get("proceso_base") else ""))
        L.append("| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |\n|---|---|---|---|---|---|---|---|")
        for s in a["soluciones"]:
            L.append("| %s | %s | %s | %s | %s | %s | %d | %s |" % (
                cel(s["id"]), cel(s["entregable"]), cel(s.get("detalle") or ""), s.get("C", "-"), s.get("T", "-"), s.get("A", "-"), s["_h"], cel(s["fase"])))
        L.append("")
    if (d.get("alcance") or {}).get("fuera_alcance"):
        L.append("## 4. Fuera de alcance\n")
        for x in d["alcance"]["fuera_alcance"]:
            L.append("- " + sin_marcado(t(x, "alcance.fuera_alcance")))
        L.append("")
    if d.get("supuestos"):
        L.append("## 5. Supuestos a confirmar\n")
        for x in d["supuestos"]:
            L.append("- " + x)
        L.append("")
    c6 = cfg_retorno(d)
    if c6:
        r6 = d["retorno"]
        L.append("## 6. Retorno esperado (slide %d)\n" % R.total)
        L.append("Modo **%s**. La slide no cita estudios ni referencias de la web ni promete retorno." % c6["modo"])
        if "{semana_medicion}" in c6["gancho"] or "semana" in c6["gancho"].lower():
            if es_num(r6.get("semana_medicion")):
                L.append("Semana de medición fijada a mano: %s. Confirmar con servicio." % R.ctx.get("semana_medicion"))
            else:
                L.append("Hacia la semana %s: construcción (%s semanas) más 90 días de seguimiento; aritmética a confirmar con servicio." % (R.ctx.get("semana_medicion"), R.ctx.get("semanas")))
        L.append("")
        if c6["pos"]:
            av = r6.get("aval_posiciones") or {}
            L.append("**Posiciones y nómina (planteadas de frente).** Aval registrado: %s · %s · %s. Confirmar que sigue vigente antes de enviar y antes de circular el documento entre líderes de área." % (av.get("quien"), av.get("fecha"), av.get("medio")))
            L.append("")
        if c6["modo"] == "cifras":
            od = r6.get("origen_datos") or {}
            L.append("Procedencia de los datos: %s · %s · validado por %s." % (od.get("documento"), od.get("fecha"), od.get("validado_por")))
            if c6["pos"]:
                L.append("Una posición equivale a %s h productivas al mes." % fmt_es(r6.get("horas_por_posicion") or 0))
            L.append("")
            filas6, tot6 = filas_cifras(d)
            L.append("| Área | Dato | Horas actuales/mes | Con la solución | Recuperadas | Valor del tiempo (USD/mes) | Posiciones hoy | A reducir | A evitar | Costo anual (USD) |\n|---|---|---|---|---|---|---|---|---|---|")
            for f in filas6:
                pp = c6["pos"]
                L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                    cel(f["nombre"]), TIPOS_DATO.get(f["tipo"], f["tipo"]), fmt_es(f["ha"]), fmt_es(f["hc"]), fmt_es(f["rec"]), fmt_es(f["valor"]),
                    fmt_es(f["pos_hoy"]) if pp else "-", fmt_es(f["pos_red"]) if pp else "-", fmt_es(f["pos_evi"]) if pp else "-", fmt_es(f["costo_anual"]) if pp else "-"))
            pp = c6["pos"]
            L.append("| **Total** | | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                fmt_es(tot6["ha"]), fmt_es(tot6["hc"]), fmt_es(tot6["rec"]), fmt_es(tot6["valor"]),
                fmt_es(tot6["pos_hoy"]) if pp else "-", fmt_es(tot6["pos_red"]) if pp else "-", fmt_es(tot6["pos_evi"]) if pp else "-", fmt_es(tot6["costo_anual"]) if pp else "-"))
            L.append("")
            L.append("Costo hora de referencia: USD %s. %s" % (fmt_es(r6.get("costo_hora_usd") or 0), sin_marcado(t(c6["nota_datos"], "retorno.nota_datos"))))
            L.append("")
        else:
            L.append("Pasos del método: " + "; ".join(sin_marcado(t(a, "retorno.pasos")) for a, _b in c6["pasos"]) + ".")
            L.append("")
    return "\n".join(L) + "\n"


def datos_meta(d, R):
    return {
        "codigo": d["cliente"]["codigo"],
        "cliente": d["cliente"]["nombre"],
        "tipo": "Capacitación In-Company · Servicio de Habilidades · %s en %s · %d h de sesión · %s semanas + seguimiento %s"
                % (R.ctx["n_total_txt"], R.ctx["n_areas_txt"], R.agg["h_total"], d["ruta"]["semanas_total"], d["seguimiento"]["rango"]),
        "eje": sin_marcado(R.t(d.get("eje") or "", "eje")),
        "servicio": "habilidades",
        "alianza": bool(d.get("alianza")),
    }


def preparar_meta(path, d, R):
    """Devuelve el texto de meta.json: lo crea o lo actualiza SIN tocar estado ni fecha_entrega (append-only, CLAUDE.md §4.19.3).
    Si el meta.json existente es ilegible aborta (no se pisa un registro de entrega)."""
    nuevo = datos_meta(d, R)
    if path.exists():
        try:
            viejo = json.loads(path.read_text(encoding="utf-8-sig"))
            if not isinstance(viejo, dict):
                raise ValueError("no es un objeto { }")
        except ValueError as e:
            sys.exit("ERROR: %s existe pero no se puede leer (%s). Corregirlo o moverlo antes de generar: contiene el estado y la fecha de entrega y no se sobrescribe." % (path, e))
        viejo.update(nuevo)
        viejo.setdefault("estado", "Borrador")
        viejo.setdefault("fecha_entrega", None)
        nuevo = viejo
    else:
        nuevo["estado"] = "Borrador"
        nuevo["fecha_entrega"] = None
    return json.dumps(nuevo, ensure_ascii=False, indent=2) + "\n"


def escribir_atomico(path, texto):
    """Escribe en un temporal del mismo directorio y reemplaza (nunca deja un archivo a medio escribir)."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(texto, encoding="utf8")
    os.replace(str(tmp), str(path))


BRIEF_AUTO = re.compile(r"<!--auto:inicio-->.*?<!--auto:fin-->", re.S)


def construir_brief(d, R):
    plantilla = (PLANTILLA / "brief.plantilla.md").read_text(encoding="utf8")
    sup = "\n".join("- " + x for x in d.get("supuestos") or ["(ninguno registrado)"])
    pen = "\n".join("- " + x for x in d.get("pendientes") or ["(ninguno registrado)"])
    sub = {
        "CLIENTE": d["cliente"]["nombre"], "CODIGO": d["cliente"]["codigo"], "SLUG": d["cliente"]["slug"],
        "DIVISION": d["division"], "ALIANZA": "sí" if d.get("alianza") else "no", "EJE": sin_marcado(R.t(d.get("eje") or "", "eje")),
        "ORIGEN": d.get("origen") or "", "FUENTE_INSUMO": d.get("fuente_insumo") or "",
        "N_TOTAL": str(R.agg["n_total"]), "N_AREAS": str(R.agg["n_areas"]), "H_TOTAL": str(R.agg["h_total"]),
        "N_TOTAL_TXT": R.ctx["n_total_txt"], "N_AREAS_TXT": R.ctx["n_areas_txt"],
        "NOTA_PRECIO": ("Precios de inversión, descuento y total: vacíos, los llena ventas." if R.con_precio
                        else "Sin hoja de inversión (Fundación): el deck no lleva precios ni campos de cotización."),
        "SEMANAS": str(d["ruta"]["semanas_total"]), "SEGUIMIENTO": d["seguimiento"]["rango"],
        "SUPUESTOS": sup, "PENDIENTES": pen, "SLIDES": str(R.total),
        "PRECIO": "con hoja de inversión (campos de precio vacíos para ventas)" if R.con_precio else "sin hoja de inversión (Fundación)",
    }
    for k, v in sub.items():
        plantilla = plantilla.replace("{{%s}}" % k, v)
    return plantilla


def bloque_auto(texto):
    m = BRIEF_AUTO.search(texto)
    return m.group(0) if m else None


# ----------------------------------------------------------------------------------------------
# Chequeos sobre el HTML generado
# ----------------------------------------------------------------------------------------------
def chequeos_html(html, d, rep):
    secciones = re.findall(r'<section class="slide ([^"]*)">(.*?)</section>', html, re.S)
    textos = []
    textos_fecha = {}
    for cls, cuerpo in secciones:
        cf = re.sub(r'<p class="(?:pain-src|lic-note)">.*?</p>', " ", cuerpo, flags=re.S)
        cf = re.sub(r"<!--.*?-->", "", cf, flags=re.S)
        cf = re.sub(r"<[^>]+>", " ", cf)
        textos_fecha[cls.split()[0]] = _html.unescape(re.sub(r"\s+", " ", cf)).strip()
        t = re.sub(r"<!--.*?-->", "", cuerpo, flags=re.S)
        t = re.sub(r'<span class="cot-sign-minus">.*?</span>', " ", t)  # «−$» de la hoja de cotización no es un guion
        t = re.sub(r"<[^>]+>", " ", t)
        textos.append((cls.split()[0], _html.unescape(re.sub(r"\s+", " ", t)).strip()))
    for cls, txt in textos:
        low = txt.lower()
        if MARCA_PRECIO in low and cls != "s-price":
            rep.err("slide " + cls, "contiene «Propuesta Económica» fuera de la slide de inversión (rompe la detección de AcroForms)")
        if MARCA_BENEF in low and cls != "s-deliv":
            rep.err("slide " + cls, "contiene «Lo que se llevan» fuera de la slide de entregables")
        for m in MARCAS_PROHIBIDAS:
            if m in low:
                rep.err("slide " + cls, "contiene «%s»: marcador de otra variante de AcroForms" % m)
        if re.search(r"\bcohorts?\b", low):
            rep.err("slide " + cls, "anglicismo «cohort» (usar «grupos»)")
        mg = RE_GUION_LARGO.search(txt)
        if mg:
            rep.err("slide " + cls, "guion largo o raya «%s» cerca de «%s» (§4.13: usar coma, paréntesis, dos puntos o punto)" % (mg.group(0), txt[max(0, mg.start() - 20):mg.end() + 20]))
        mg = RE_GUION_MEDIO.search(txt)
        if mg:
            rep.err("slide " + cls, "guion mediano «–» cerca de «%s» (§4.13; solo se tolera entre dos cifras)" % txt[max(0, mg.start() - 20):mg.end() + 20])
        if cls == "s-roi":
            mm = RE_RET_ERR.search(txt)
            if mm:
                rep.err("slide " + cls, "la slide de retorno no cita estudios ni referencias de la web («%s» cerca de «%s»)" % (mm.group(0), txt[max(0, mm.start() - 25):mm.end() + 25]))
        if "**" in txt:
            i = txt.index("**")
            rep.err("slide " + cls, "quedó «**» sin procesar (negrita mal cerrada) cerca de «%s»" % txt[max(0, i - 20):i + 20])
        m = re.search(r"\{[^{}]*\}", txt)
        if m:
            rep.err("slide " + cls, "quedó una llave sin resolver «%s»" % m.group(0))
        elif "{" in txt or "}" in txt:
            i = min(x for x in (txt.find("{"), txt.find("}")) if x >= 0)
            rep.err("slide " + cls, "llave suelta «{» o «}» cerca de «%s»" % txt[max(0, i - 20):i + 20])
        if RE_FECHA.search(textos_fecha.get(cls, txt)):
            rep.aviso("slide " + cls, "contiene una fecha o mes calendario. El insumo vigente de Habilidades es relativo al arranque (semanas); si es una fecha de fuente/precio está bien, si es del cronograma confirmar con el usuario")
    ids_sol = set(x.get("id") for a in d.get("areas") or [] if isinstance(a, dict) for x in a.get("soluciones") or [] if isinstance(x, dict) and x.get("id"))
    for cls, txt in textos:
        vis = sorted(i for i in ids_sol if re.search(r"(?<![A-Za-z0-9-])%s(?![A-Za-z0-9-])" % re.escape(i), txt))
        if vis:
            rep.aviso("slide " + cls, "el texto del cliente nombra ids internos de solución (%s): ninguna slide los define; reescribir con el nombre del entregable" % ", ".join(vis[:5]))
    tds = dict((c, t) for c, t in textos)
    if MARCA_BENEF not in tds.get("s-deliv", "").lower():
        rep.err("slide s-deliv", "falta la frase «Lo que se llevan» (marcador de las cajas Entregables/Acreditacion); el subtítulo por defecto la incluye")
    if "entregables" not in tds.get("s-deliv", "").lower():
        rep.err("slide s-deliv", "falta la palabra «Entregables» (la exige agregar-campo-precio.py)")
    if "s-price" in tds and MARCA_PRECIO not in tds["s-price"].lower():
        rep.err("slide s-price", "falta «Propuesta Económica» (marcador de campos de precio)")
    for cls, cuerpo in secciones:
        n = len(re.findall(r"<strong>", cuerpo))
        if n > 3:
            rep.aviso("slide " + cls, "%d resaltados <strong>: la regla §4.8 pide ~2-3 por slide" % n)
    permitidas = SIGLAS_OK | set(d.get("siglas_ok") or []) | set(re.findall(r"[A-Z]{2,}", d["cliente"].get("nombre", "")))
    for cls, txt in textos:
        sin_codigos = re.sub(r"\b[A-Z]{2,4}-\d+\b", " ", txt)
        sin_codigos = re.sub(r"\bS\d+(-S\d+)?\b", " ", sin_codigos)
        encontradas = set(re.findall(r"\b[A-Z]{2,6}\b", sin_codigos)) - permitidas
        encontradas = set(x for x in encontradas if "(%s)" % x not in txt)
        if encontradas:
            rep.aviso("slide " + cls, "siglas posibles sin glosar (§4.12: expandir en el primer uso o agregar a siglas_ok si son del cliente): " + ", ".join(sorted(encontradas)))


# ----------------------------------------------------------------------------------------------
# Principal
# ----------------------------------------------------------------------------------------------
def _imprimir(rep, ctx):
    if ctx:
        d, agg = ctx
        print("== Habilidades compacto · %s (%s) ==" % ((d.get("cliente") or {}).get("nombre", "?"), (d.get("cliente") or {}).get("codigo", "?")))
        print("   %d %s · %d %s · %d h · frentes %s · fases %s" % (
            agg["n_total"], plural(agg["n_total"], "solución", "soluciones"), agg["n_areas"], plural(agg["n_areas"], "área", "áreas"), agg["h_total"],
            ", ".join("%s=%dh" % (k, v[1]) for k, v in sorted(agg["frente"].items(), key=lambda kv: str(kv[0]))),
            ", ".join("%s=%dh" % (k, v[1]) for k, v in sorted(agg["fase"].items(), key=lambda kv: str(kv[0])))))
    for a in rep.avisos:
        print("⚠ " + a)
    for e in rep.errores:
        print("✗ " + e)


def ejecutar(args):
    if not args.slug and not args.datos:
        sys.exit("ERROR: indica <slug> o --datos")
    datos_path = Path(args.datos).resolve() if args.datos else PROPUESTAS / args.slug / "datos.json"
    if not datos_path.exists():
        sys.exit("ERROR: no existe %s (copiar plantillas/habilidades-compacto-canonico/datos.plantilla.json)" % datos_path)
    if args.salida:
        out = Path(args.salida).resolve()
    elif args.slug:
        out = PROPUESTAS / args.slug
    elif datos_path.parent.parent.resolve() == PROPUESTAS.resolve():
        out = datos_path.parent
    elif args.solo_validar:
        out = datos_path.parent  # no se escribe nada
    else:
        sys.exit("ERROR: con --datos fuera de clientes/propuestas/<slug>/ hay que indicar --salida (para no escribir junto al archivo de datos)")
    claves_dup = []

    def sin_duplicados(pares):
        vistos = set()
        for k, _ in pares:
            if k in vistos:
                claves_dup.append(k)
            vistos.add(k)
        return dict(pares)

    try:
        d = json.loads(datos_path.read_text(encoding="utf-8-sig"), object_pairs_hook=sin_duplicados)
    except UnicodeDecodeError:
        sys.exit("ERROR: datos.json no está en UTF-8 (re-guardarlo como UTF-8 desde el editor)")
    except ValueError as e:
        sys.exit("ERROR: datos.json no es JSON válido: %s" % e)
    if not isinstance(d, dict):
        sys.exit("ERROR: datos.json debe ser un objeto { }")

    rep = Reporte()
    ESTADO["rep"] = rep
    for k in sorted(set(claves_dup)):
        rep.err("datos.json", "la clave «%s» aparece repetida en el mismo objeto (JSON se queda con la última y pierde la anterior): borrar el duplicado" % k)
    # 1) Estructura: pendientes, tipos y secciones obligatorias (siempre abortan)
    saltar = ("inversion",) if d.get("division") == "fundacion" else ()
    pend = []
    buscar_pendientes(d, "", pend, saltar)
    for ruta_ph, msg in pend:
        rep.err(ruta_ph, msg)
    chequear_tipos(d if d.get("division") != "fundacion" else dict((k, v) for k, v in d.items() if k != "inversion"), "raiz", "", rep)
    for k in ("cliente", "portada", "carriles", "areas", "fases", "frentes", "ruta", "seguimiento", "alcance", "entregables"):
        if not d.get(k):
            rep.err(k, "falta la sección obligatoria")
    if rep.errores:
        _imprimir(rep, None)
        print("\n%d error(es) de estructura: no se escribió nada." % len(rep.errores))
        sys.exit(1)

    # 2) Cálculo y reglas de negocio
    ctx, agg = calcular(d, rep)
    validar_semantica(d, ctx, agg, rep, Tokens(ctx, Reporte()))
    if rep.errores and not args.borrador:
        _imprimir(rep, (d, agg))
        print("\n%d error(es): no se escribió nada." % len(rep.errores))
        sys.exit(1)

    R = Ctx()
    R.ctx, R.agg = ctx, agg
    R.t = Tokens(ctx, rep)
    R.T = lambda x, donde: esc(sin_marcado(R.t(x, donde)))
    R.M = lambda x, donde: md(R.t(x, donde))
    div_nombre, div_dir = DIVISIONES.get(d.get("division"), ("Educación", "educacion"))
    R.div_nombre = div_nombre
    R.con_precio = d.get("division") != "fundacion"
    R.total = (5 if R.con_precio else 4) + (1 if d.get("retorno") else 0)
    R.contador = lambda i: "%02d / %02d" % (i, R.total)
    R.codigo = d["cliente"].get("codigo", "")
    R.pie = d["cliente"].get("nombre_pie") or d["cliente"].get("nombre", "")
    R.rel_base = os.path.relpath(str(PROPUESTAS / "_base" / "styles.css"), str(out))
    R.rel_logos = os.path.relpath(str(ROOT / "logos" / div_dir), str(out))

    columnas, ncols, alto_max = repartir_columnas(d, rep)
    html = af = None
    if columnas:
        cupo = cupo_catalogo(d, R)
        compacto = bool(d["entregables"].get("compacto"))
        if alto_max > cupo * 1.15:
            detalle = "; ".join(
                "columna %d (%s): ~%d px" % (i + 1, "+".join(a["id"] for a in c["areas"]),
                                             sum(alto_area(a, ncols, compacto) for a in c["areas"]) + 14 * (len(c["areas"]) - 1))
                for i, c in enumerate(columnas))
            rep.err("entregables", "el catálogo estimado mide ~%d px en su columna más alta y el cupo es ~%d px (%s). Opciones: acortar los nombres más largos a ≤ 36 caracteres (1 línea), entregables.compacto=true, un título/subtítulo más cortos, o entregables.columnas_por_carril" % (alto_max, cupo, detalle))
        elif alto_max > cupo - 8:
            rep.aviso("entregables", "el catálogo estimado mide ~%d px en su columna más alta (cupo ~%d px): puede no caber; medir con verificar-habilidades-compacto.js (el estimador varía ±10 %%)" % (alto_max, cupo))
    alto_s2, cupo_s2 = estimar_s2_derecha(d, R)
    if alto_s2 > cupo_s2 + 12:
        rep.err("alcance", "la columna derecha de la slide 2 (pasos, quién construye, fuera de alcance) mide ~%d px y el cupo es ~%d px: acortar pasos, quien_construye o fuera_alcance (o el subtítulo, que libera 21 px por línea)" % (alto_s2, cupo_s2))
    elif alto_s2 > cupo_s2 - 5:
        rep.aviso("alcance", "la columna derecha de la slide 2 mide ~%d px (cupo ~%d px): puede chocar con el pie; medir con verificar-habilidades-compacto.js" % (alto_s2, cupo_s2))
    if d.get("retorno") and isinstance(d["retorno"], dict) and (d["retorno"].get("modo") or "metodo") in ("metodo", "cifras"):
        holg6 = estimar_s6(d, R)
        if holg6 < -10:
            rep.err("retorno", "la slide de retorno estimada excede la página en ~%d px: acortar pasos, metas, destino, gancho o (modo cifras) reducir filas" % -holg6)
        elif holg6 < 12:
            rep.aviso("retorno", "holgura estimada contra la banda final de ~%d px (mín. 8): puede no caber; medir con verificar-habilidades-compacto.js" % holg6)
    titulo5 = R.t(d["entregables"].get("titulo") or "Todo lo que {cliente_corto} recibe.", "entregables.titulo")
    if len(titulo5) > 28:
        rep.aviso("entregables.titulo", "el titular de %d caracteres ocupa 2 líneas y quita ~40 px al catálogo: usar un nombre_pie corto o definir entregables.titulo (≤ 28)" % len(titulo5))
    titulo2 = R.t(d["alcance"].get("titulo") or titulo_alcance_defecto(R), "alcance.titulo")
    if len(titulo2) > 50:
        rep.aviso("alcance.titulo", "el titular de %d caracteres pasa a 2 líneas: usar un nombre_pie corto o definir alcance.titulo" % len(titulo2))
    sub5 = sin_marcado(R.t(d["entregables"].get("subtitulo") or SUB_ENTREGABLES, "entregables.subtitulo"))
    if MARCA_BENEF not in sub5.lower():
        rep.err("entregables.subtitulo", "debe contener la frase «Lo que se llevan» (marcador de las cajas de formulario)")

    if columnas and (not rep.errores or args.borrador):
        html = render_html(d, R, columnas, ncols)
        af = construir_acroforms(d, R)
        validar_acroforms(af, rep)
        chequeos_html(html, d, rep)

    _imprimir(rep, (d, agg))
    if rep.errores and not args.borrador:
        print("\n%d error(es): no se escribió nada." % len(rep.errores))
        sys.exit(1)
    if args.solo_validar:
        print("✓ Validación OK (%d aviso(s))." % len(rep.avisos))
        return
    if html is None:
        sys.exit(1)

    # Todo lo que puede fallar se prepara ANTES de escribir el primer archivo (no deja la carpeta a medias).
    meta_path = out / "meta.json"
    meta_txt = preparar_meta(meta_path, d, R)
    programa_txt = construir_programa_md(d, R)
    af_txt = json.dumps(af, ensure_ascii=False, indent=2) + "\n"
    brief = out / "brief.md"
    nuevo = construir_brief(d, R)
    brief_txt = None
    if args.forzar_brief or not brief.exists():
        brief_txt = nuevo
    else:
        actual = brief.read_text(encoding="utf-8-sig")
        ba, bn = bloque_auto(actual), bloque_auto(nuevo)
        if ba and bn and ba != bn:
            brief_txt = actual.replace(ba, bn)
        elif not ba:
            print("⚠ brief.md no tiene el bloque <!--auto:inicio-->...<!--auto:fin-->: su resumen de alcance no se refrescó (usar --forzar-brief para recrearlo).")
    out.mkdir(parents=True, exist_ok=True)
    escribir_atomico(out / "index.html", html)
    css_dst = out / CSS_NAME
    if args.actualizar_css or not css_dst.exists():
        escribir_atomico(css_dst, (PLANTILLA / CSS_NAME).read_text(encoding="utf8"))
    ov = out / "overrides.css"
    if args.forzar_overrides or not ov.exists():
        escribir_atomico(ov, "/* Ajustes propios de esta propuesta (se enlaza después de habilidades-compacto.css). */\n")
    escribir_atomico(out / "acroforms.json", af_txt)
    escribir_atomico(out / "programa.md", programa_txt)
    escribir_atomico(meta_path, meta_txt)
    if brief_txt is not None:
        escribir_atomico(brief, brief_txt)
    print("✓ Escrito en %s (index.html, %s, overrides.css, acroforms.json, programa.md, meta.json, brief.md)" % (out, CSS_NAME))
    if args.medir:
        node = shutil.which("node")
        sys.stdout.flush()
        if node:
            r = subprocess.run([node, str(ROOT / "scripts" / "verificar-habilidades-compacto.js"), str(out / "index.html")])
            if r.returncode != 0:
                sys.exit(r.returncode)
        else:
            print("⚠ node no disponible: no se pudo medir.")
    elif args.slug:
        print("  Siguiente: bash scripts/pdf-habilidades-compacto.sh %s" % args.slug)
    else:
        print("  Siguiente: node scripts/verificar-habilidades-compacto.js %s" % (out / "index.html"))


def main():
    ap = argparse.ArgumentParser(description="Genera la propuesta compacta de Habilidades desde datos.json")
    ap.add_argument("slug", nargs="?", help="slug de clientes/propuestas/<slug> (lee datos.json de ahí)")
    ap.add_argument("--datos", help="ruta a datos.json (en vez del slug)")
    ap.add_argument("--salida", help="carpeta de salida (por defecto clientes/propuestas/<slug>)")
    ap.add_argument("--solo-validar", action="store_true")
    ap.add_argument("--forzar-brief", action="store_true", help="reescribe brief.md aunque exista")
    ap.add_argument("--forzar-overrides", action="store_true", help="reescribe overrides.css (borra ajustes propios)")
    ap.add_argument("--actualizar-css", action="store_true", help="refresca la copia de habilidades-compacto.css")
    ap.add_argument("--medir", action="store_true", help="corre verificar-habilidades-compacto.js al terminar")
    ap.add_argument("--depurar", action="store_true", help="muestra el traceback de errores internos")
    ap.add_argument("--borrador", action="store_true", help="escribe aunque haya errores no estructurales (depuración)")
    args = ap.parse_args()
    try:
        ejecutar(args)
    except SystemExit:
        raise
    except Exception as e:  # noqa
        if args.depurar:
            raise
        if ESTADO["rep"] is not None and (ESTADO["rep"].errores or ESTADO["rep"].avisos):
            _imprimir(ESTADO["rep"], None)
        print("✗ Error interno inesperado (%s: %s). Casi siempre es un valor mal formado en datos.json; "
              "repetir con --depurar para ver el detalle." % (type(e).__name__, e))
        sys.exit(1)


if __name__ == "__main__":
    main()
