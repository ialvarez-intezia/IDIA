#!/usr/bin/env python3
"""
generar-habilidades-compacto.py — Genera la propuesta de Habilidades (formato compacto, v2) desde datos.json.

Plantilla genérica nacida de clientes/propuestas/dusa-cai035 (CAI-035, 2026-10-04) y reordenada el 2026-10-07 según el
feedback consolidado de Ventas: la propuesta responde, en orden, las preguntas del cliente (problema, cómo lo
resolvemos, con qué se queda, qué gana, logística, inversión, próximos pasos) y habla en su idioma. Slides (Educación):
Portada · Alcance · Ruta · Cómo trabajamos · Entregables · Retorno · Inversión · Facilidad de pago · Próximos pasos
(Fundación: sin Inversión ni Facilidad de pago). Especificación completa: plantillas/habilidades-compacto.md.
Esquema de datos: plantillas/habilidades-compacto-canonico/datos.plantilla.json (anotado) y datos.ejemplo-dusa.json.

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
VERSION_PLANTILLA = "2.0 (2026-10-07)"
VERSION_DATOS = 2   # datos.json debe declarar "version": 2

DIVISIONES = {
    "educacion": ("Educación", "educacion"),
    "fundacion": ("Fundación", "fundacion"),
}
COLORES = {"amarillo": "acc-y", "naranja": "acc-o"}
FASES_VALIDAS = ("F0", "F1", "F2", "F3")

# Frases que agregar-campo-precio.py usa para ubicar cada grupo de campos AcroForm por página.
MARCA_PRECIO = "propuesta económica"
MARCA_BENEF = "lo que se llevan"
MARCA_PAGO = "facilidad de pago"
MARCAS_PROHIBIDAS = ("cómo arrancamos", "inversión por fases", "inversión por permanencia")

SIGLAS_OK = {"TOTAL", "IA", "USD", "CV", "RRHH", "TI", "PDF", "SEO", "API", "VPN", "IVA", "ISLR", "CAI", "TA", "CU", "DIP", "CH", "DET", "INN", "ALL"}
PALABRAS_FRENTES = {1: "Una línea de trabajo", 2: "Dos líneas de trabajo en paralelo", 3: "Tres líneas de trabajo en paralelo"}
MESES = r"(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)"
# Fechas reales: dd/mm[/aaaa] con día 1-31 y mes 1-12, aaaa-mm-dd, dd-mm-aaaa (año de 4 cifras), «12 de marzo», o un nombre de mes.
# No debe casar con «30-60-90» (marco de seguimiento) ni con «24/7».
RE_FECHA = re.compile(
    r"\b(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[0-2])/\d{2,4}\b|\b(0?[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])\b(?!/)|\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b|"
    r"\b(0?[1-9]|[12]\d|3[01])-(0?[1-9]|1[0-2])-\d{4}\b|\b\d{1,2}\s+(de\s+)?" + MESES + r"\b|\b" + MESES + r"\b",
    re.I,
)
# Conteo de sesiones («6 sesiones», «dos sesiones», «una sesión», «sesión única»): se avisa si anunciar_duracion = false.
RE_SESIONES = re.compile(r"\b(\d+|una|un|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|doce)\s+sesi(?:ón|on|ones)\b|\bsesi[óo]n\s+[úu]nica\b", re.I)
RE_GUION_LARGO = re.compile("[\u2014\u2015\u2012\u2212\u2E3A\u2E3B]|-{2,}")
# El guion mediano solo se tolera entre dos cifras (rangos como 10–15); «S1–S11» o «A – B» no.
RE_GUION_MEDIO = re.compile("(?<!\\d)\u2013|\u2013(?!\\d)")
# Lenguaje del cliente (feedback de Ventas, 2026-10-07): lo que el cliente no entiende o es código interno.
JERGA_ERR = [
    (re.compile(r"\bprocesos? base\b", re.I), "«proceso base» no lo entiende el cliente: decir qué es («paso previo», «punto de partida»)"),
    (re.compile(r"\bFrente\s+[A-Z0-9]\b"), "«Frente A» es un código interno: usar el nombre de la línea de trabajo"),
    (re.compile(r"\bS\d{1,2}\b"), "«S1», «S1-S3» es un código interno: escribir «semana 1» o «semanas 1 a 3» (o «sesión 1» si es una sesión)"),
    (re.compile(r"\bF[0-3]\b"), "«F1» es un código interno de fase: escribir «fase 1»"),
    (re.compile(r"\bcarriles?\b", re.I), "«carril» es jerga interna: nombrar la herramienta (p. ej. «Claude Team»)"),
    (re.compile(r"(?<!\by )(?<!sesión )(?<!sesiones )(?<!módulo )(?<!módulos )\b\d+\s+de\s+\d+\s*h\b", re.I), "«8 de 15 h» no dice de qué: escribir «8 de las 15 horas del programa son ...»"),
    (re.compile(r"\binversi[oó]n por horas?\b", re.I), "cobramos por proyecto, no por hora: «Inversión del proyecto»"),
    (re.compile(r"\bprecios?\b", re.I), "usar «valor» (o «inversión»), nunca «precio»"),
]
JERGA_AVISO = [
    (re.compile(r"\bcostos?\b", re.I), "«costo»: para lo que paga el cliente usar «valor» o «inversión» (solo se tolera para el costo interno del propio cliente, como la hora de su equipo)"),
]
# Palabras de compromiso económico que no van en los próximos pasos (CLAUDE.md §4.15)
RE_ECONOMICO = re.compile(r"\b(?:firm\w*|contrato|factur\w*|anticipo|adelanto|pago|pagar)\b|50\s?%", re.I)
# Lenguaje no comprometedor para hablar de contratación evitada (Ventas y dirección, 2026-10-06)
RE_PROBABILIDAD = re.compile(r"probabilidad|podr[ií]a|puede|posible|es probable|se espera", re.I)
RE_COMPROMISO = re.compile(r"garantiz\w*|\bse reducir[aá]n?\b|\bse eliminar[aá]n?\b|\bsin duda\b|\bseguro que\b|\bsiempre\b", re.I)
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
PASO_DINERO = ("Valor en dinero", "Horas recuperadas multiplicadas por el valor de la hora de referencia, más el valor del retrabajo, de los errores y de los pagos o cobros tardíos, cuando exista el dato.")
PASO_CAPACIDAD = ("Capacidad liberada", "Las horas recuperadas se expresan en capacidad para la misión: más beneficiarios atendidos y menos tiempo en tareas administrativas.")
PASO_POSICIONES = ("Posiciones y valor anual", "Horas recuperadas divididas entre las horas productivas de una posición: cuántas se reducen o no será necesario contratar, con su valor anual según las escalas de {cliente_corto}.")
METAS_BASE = [("30 días", "Soluciones en uso real y línea base validada con el líder de cada área."),
              ("60 días", "Horas recuperadas medidas contra la línea base, por área y por proceso.")]
META90 = {(False, True): "Medición del retorno en dinero y en posiciones, con el valor anual de cada una.",
          (False, False): "Medición del retorno en dinero, con el valor de las horas recuperadas de cada área.",
          (True, True): "Medición del retorno en dinero y en posiciones, con el valor anual de cada una.",
          (True, False): "Horas recuperadas y capacidad liberada para la misión, por área."}
DESTINO_EDU = [
    ("Mismo equipo, más volumen", "Si el tiempo se libera, el mismo equipo puede **procesar más trabajo** sin contratar más personal."),
    ("Trabajo reenfocado", "Con el tiempo liberado, las personas de cada área dejan de armar y consolidar a mano para validar resultados, analizar y decidir, y sus posiciones se reenfocan hacia trabajo más estratégico."),
    ("Otras áreas y líneas de negocio", "Con el retorno medido, {cliente_corto} decide si lleva este ciclo a **otras áreas y líneas de negocio** y avanza hacia una empresa inteligente, con la inteligencia artificial en el centro de su operación."),
]
DESTINO_FUND = [
    ("Mismo equipo, más alcance", "Si el tiempo se libera, el mismo equipo puede **atender a más personas** sin ampliar la plantilla."),
    ("Trabajo reenfocado", "Con el tiempo liberado, el equipo puede dedicarse a revisar resultados, preparar informes y estar más cerca de los beneficiarios."),
    ("Otros programas y áreas", "Con el retorno medido, {cliente_corto} decide si lleva este mismo ciclo a **otros programas y áreas** y llega a más personas con el mismo equipo."),
]

PASOS_METODO = [
    {"titulo": "Construimos", "texto": "Junto a quien ejecuta el proceso, con sus casos reales."},
    {"titulo": "Probamos", "texto": "Con ese equipo y con el equipo de tecnología de {cliente_corto}."},
    {"titulo": "Adoptamos", "texto": "El equipo la usa en su trabajo diario."},
    {"titulo": "Medimos", "texto": "El retorno en tiempo y las oportunidades de optimización para la empresa."},
]
PASOS_PROXIMOS = [
    {"titulo": "Fecha de arranque", "texto": "Confirmamos la fecha de arranque y la zona horaria de las sesiones."},
    {"titulo": "Accesos y agenda", "texto": "Coordinamos los accesos, los participantes de cada área y la agenda de sesiones."},
    {"titulo": "Reunión de arranque", "texto": "Una reunión de unos 30 minutos para alinear los casos reales y medir la línea base."},
]
# Plan de pago estándar de empresa/politicas-comerciales.md (anticipo 50 % y saldo 50 % al cierre) cuando la propuesta no define otro
PAGO_ESTANDAR = [
    {"cuando": "Al aprobar", "hito": "Anticipo al aprobar la propuesta", "pct": 50},
    {"cuando": "Al cierre", "hito": "Saldo al cierre del proyecto", "pct": 50},
]
# Vocabulario de la propuesta. Por defecto el de Habilidades; otro servicio (p. ej. Detección: entregables, frentes, etapa previa) lo declara en
# datos.json → vocabulario = {solucion, area, proceso_base}: [singular, plural]. «Proceso base» es jerga interna: el cliente ve «paso previo».
VOC_DEF = {"solucion": ("solución", "soluciones"), "area": ("área", "áreas"), "proceso_base": ("paso previo", "pasos previos")}
VOC = dict(VOC_DEF)
OMITIBLES = ("metodo", "retorno", "proximos", "inversion", "pago")   # slides que datos.json → omitir puede quitar (el resto es el núcleo)
PALABRA_N = {1: "una", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis"}
NOMBRES_SLIDE = {"portada": "Portada", "alcance": "Alcance", "ruta": "Ruta", "metodo": "Cómo trabajamos", "entregables": "Entregables",
                 "retorno": "Retorno", "inversion": "Inversión", "pago": "Facilidad de pago", "proximos": "Próximos pasos"}
ORDEN_EDUCACION = ["portada", "alcance", "ruta", "metodo", "entregables", "retorno", "inversion", "pago", "proximos"]

SUB_ENTREGABLES = "Lo que se llevan: **{n_entregables_txt}**, uno por cada solución construida, probada y adoptada, más el seguimiento a {rango_seguimiento} que mide su efecto."
SUB_ENTREGABLES_SIN_SEG = "Lo que se llevan: **{n_entregables_txt}**, uno por cada solución construida, probada y adoptada."
SUB_ENTREGABLES_VOC = "Lo que se llevan: **{n_entregables_txt}**, todos los del programa, más el seguimiento a {rango_seguimiento} que mide su efecto."
SUB_ENTREGABLES_VOC_SIN_SEG = "Lo que se llevan: **{n_entregables_txt}**, todos los del programa."

# ----------------------------------------------------------------------------------------------
# Esquema de tipos (valida antes de calcular: evita tracebacks por datos mal formados)
# ----------------------------------------------------------------------------------------------
ESQUEMAS = {
    "raiz": {"version": "int", "cliente": "dict:cliente", "division": "str", "alianza": "bool", "eje": "str", "origen": "str",
             "fuente_insumo": "str", "portada": "dict:portada", "carriles": "list:dict:carril", "areas": "list:dict:area",
             "alcance": "dict:alcance", "metodo": "dict:metodo", "fases": "list:dict:fase", "frentes": "list:dict:frente",
             "ruta": "dict:ruta", "logistica": "dict:logistica", "seguimiento": "dict:seguimiento", "inversion": "dict:inversion",
             "pago": "dict:pago", "entregables": "dict:entregables", "retorno": "dict:retorno",
             "proximos_pasos": "dict:proximos_pasos", "siglas_ok": "list:str", "frases_ok": "list:str", "supuestos": "list:str", "pendientes": "list:str",
             "servicio_rotulo": "str", "meta_servicio": "str", "meta_tipo": "str", "vocabulario": "dict:vocabulario", "sin_hoja_cotizacion": "bool",
             "omitir": "list:str", "anunciar_duracion": "bool"},
    "vocabulario": {"solucion": "list:str", "area": "list:str", "proceso_base": "list:str"},
    "cliente": {"nombre": "str", "slug": "str", "codigo": "str", "nombre_pie": "str"},
    "portada": {"eyebrow": "str", "titulo_lineas": "list:str", "titulo_linea1": "str", "titulo_destacado": "str", "lead": "str",
                "hechos": "list:dict:hecho", "fuente": "str", "contratacion": "dict:contratacion"},
    "hecho": {"num": "str", "texto": "str", "resuelto_por": "list:str"},
    "contratacion": {"num": "str", "texto": "str", "fuente": "str"},
    "carril": {"id": "str", "nombre": "str", "nombre_corto": "str", "color": "str"},
    "area": {"id": "str", "nombre": "str", "carril": "str", "frente": "str", "para_que": "str", "nombre_catalogo": "str",
             "proceso_base": "bool", "composicion": "str", "soluciones": "list:dict:solucion"},
    "solucion": {"id": "str", "entregable": "str", "C": "num", "T": "num", "A": "num", "h": "num", "fase": "str",
                 "detalle": "str", "_revisar": "bool"},
    "alcance": {"titulo": "str", "subtitulo": "str", "fuera_alcance": "list:str", "compacto": "bool",
                "etiqueta_proceso_base": "str", "etiqueta_fuera": "str"},
    "metodo": {"titulo": "str", "subtitulo": "str", "pasos": "list:dict:paso", "por_que_orden": "str", "quien_construye": "str",
               "practica": "list:dict:practica", "datos": "str", "ejemplos": "list:dict:ejemplo", "etiqueta_ejemplos": "str",
               "nota_ejemplos": "str"},
    "paso": {"titulo": "str", "texto": "str"},
    "practica": {"titulo": "str", "texto": "str"},
    "ejemplo": {"area": "str", "titulo": "str", "antes": "str", "despues": "str", "texto": "str", "fuente": "str"},
    "fase": {"id": "str", "titulo": "str", "rango": "str", "descripcion": "str", "destacada": "bool"},
    "frente": {"id": "str", "carril": "str", "nombre": "str", "semanas": "str", "celdas": "dict:str"},
    "ruta": {"semanas_total": "int", "tope_h_semana": "int", "hitos": "list:dict:hito", "titulo": "str", "subtitulo": "str",
             "nota": "str", "siguiente_etapa": "dict:siguiente_etapa"},
    "siguiente_etapa": {"titulo": "str", "texto": "str"},
    "hito": {"titulo": "str", "texto": "str"},
    "logistica": {"modalidad": "str", "participantes": "str", "arranque": "str", "ritmo": "str"},
    "seguimiento": {"rango": "str", "texto": "str", "items": "list:dict:item", "etiqueta": "str", "tipo": "str"},
    "item": {"dias": "str", "texto": "str"},
    "inversion": {"notas": "list:str", "licencias": "dict:licencias", "titulo": "str", "duracion": "str", "programa": "list:str",
                  "garantia_texto": "str", "sin_garantia": "bool", "partes": "list:dict:parte", "etiqueta_partes": "str",
                  "etiqueta_suma": "str"},
    "parte": {"nombre": "str", "detalle": "str"},
    "licencias": {"titulo": "str", "tarjetas": "list:dict:tarjeta", "nota": "str"},
    "tarjeta": {"nombre": "str", "color": "str", "texto": "str"},
    "pago": {"titulo": "str", "subtitulo": "str", "cuotas": "list:dict:cuota", "mensaje": "str", "facturacion": "str"},
    "cuota": {"cuando": "str", "hito": "str", "pct": "num"},
    "proximos_pasos": {"titulo": "str", "subtitulo": "str", "pasos": "list:dict:paso", "asesora": "dict:asesora", "etiqueta_contacto": "str"},
    "asesora": {"nombre": "str", "cargo": "str", "correo": "str", "telefono": "str"},
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


ESTADO = {"rep": None, "etq_base": None}  # reporte en curso (para mostrar lo acumulado si hay un error interno)


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
    set_vocab(d)
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
        for k in ("id", "carril", "nombre", "semanas"):
            if not f.get(k):
                rep.err("frentes[%d]" % i, "falta %s%s" % (k, " (el nombre de la línea de trabajo que ve el cliente, p. ej. «Recursos Humanos»)" if k == "nombre" else ""))
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
        "n_total_txt": "%d %s" % (agg["n_total"], plural(agg["n_total"], *VOC["solucion"])),
        "n_entregables_txt": "%d %s" % (agg["n_total"], plural(agg["n_total"], "entregable", "entregables")),
        "n_areas_txt": "%d %s" % (agg["n_areas"], plural(agg["n_areas"], *VOC["area"])),
        "semanas": sem, "semanas_txt": ("%d %s" % (sem, plural(sem, "semana", "semanas"))) if isinstance(sem, int) else "", "tope_h_semana": tope, "tope_h_dia": int(round(tope / 5.0)),
        "rango_seguimiento": seg.get("rango", ""),
    }
    n_fr = len(d.get("frentes") or [])
    ctx["n_frentes_txt"] = "%d %s" % (n_fr, plural(n_fr, "línea de trabajo", "líneas de trabajo"))
    cuotas_d = (d.get("pago") or {}).get("cuotas")
    n_c = len(cuotas_d) if isinstance(cuotas_d, list) and cuotas_d else len(PAGO_ESTANDAR)
    ctx["n_cuotas"] = n_c
    ctx["n_cuotas_palabra"] = PALABRA_N.get(n_c, str(n_c))
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


def semanas_numeros(txt):
    """Números de semana que aparecen en un rótulo como «1 a 11», «Semanas 7-11» o «semana 5»."""
    return [int(x) for x in re.findall(r"\d+", txt or "")]


def txt_semanas(txt):
    """«semana 5» / «semanas 1 a 11» a partir del rótulo de la línea de trabajo."""
    t = re.sub(r"(?i)^\s*semanas?\s*", "", (txt or "").strip())
    return ("semana %s" if re.match(r"^\d+$", t) else "semanas %s") % t


def cap1(t):
    """Mayúscula inicial (solo si el texto empieza con una letra minúscula; respeta tokens y negritas)."""
    m = re.match(r"^(\W*)([a-záéíóúñ])", t)
    return t[:m.start(2)] + m.group(2).upper() + t[m.end(2):] if m else t


def cuotas_pago(d):
    """Cuotas del plan de pago: las del datos.json o el plan estándar de la política comercial."""
    c = (d.get("pago") or {}).get("cuotas")
    return c if isinstance(c, list) and c else PAGO_ESTANDAR


def validar_semantica(d, ctx, agg, rep, silent):
    def rs(x):
        return sin_marcado(silent(x, "_")) if isinstance(x, str) else ""

    con_precio = not sin_inversion(d)
    orden = orden_slides(d)
    if d.get("division") not in DIVISIONES:
        rep.err("division", "debe ser 'educacion' o 'fundacion' (no se infiere: preguntar y guardar, CLAUDE.md §4.1)")
    if not isinstance(d.get("alianza"), bool):
        rep.err("alianza", "debe ser true o false (confirmar con el usuario, CLAUDE.md §4.1a punto 2)")
    for _k, _v in ((d.get("vocabulario") or {}).items() if isinstance(d.get("vocabulario"), dict) else []):
        if _k in VOC_DEF and not (isinstance(_v, list) and len(_v) == 2 and all(isinstance(i, str) and i.strip() for i in _v)):
            rep.err("vocabulario.%s" % _k, "debe ser [singular, plural], dos textos no vacíos")
    if d.get("meta_servicio") and d["meta_servicio"] not in ("habilidades", "deteccion", "politicas", "innovacion", "integral"):
        rep.err("meta_servicio", "valor inválido «%s»: usar habilidades | deteccion | politicas | innovacion | integral (CLAUDE.md §4.19)" % d["meta_servicio"])
    if "anunciar_duracion" in d and not isinstance(d["anunciar_duracion"], bool):
        rep.err("anunciar_duracion", "debe ser true o false (preguntar al usuario si la propuesta anuncia las semanas y las sesiones)")
    elif not anuncia_duracion(d):
        for _donde, _txt in (("ruta.titulo", (d.get("ruta") or {}).get("titulo")), ("inversion.duracion", (d.get("inversion") or {}).get("duracion"))):
            if isinstance(_txt, str) and re.search(r"\{semanas(?:_txt)?\}", _txt):
                rep.err(_donde, "usa {semanas} o {semanas_txt} pero anunciar_duracion = false: quitar el número de semanas del texto")
            elif isinstance(_txt, str) and re.search(r"semanas?\b", _txt, re.I):
                rep.aviso(_donde, "nombra las semanas pero anunciar_duracion = false: confirmar que es intencional")
        _quedan = ["el rango de cada fase y de cada línea de trabajo (slide 3)"]
        if "retorno" in orden:
            _quedan.append("el «Hacia la semana N» del retorno (slide 6)")
        rep.aviso("anunciar_duracion", "false: el titular de la ruta y la Duración de la inversión no nombran las semanas, pero siguen visibles %s. Confirmar con el usuario si también deben ocultarse; sin número de sesiones en textos libres (composicion, hitos, descripciones)" % " y ".join(_quedan))
    for _x in (d.get("omitir") or []):
        if _x not in OMITIBLES:
            rep.err("omitir", "«%s» no se puede omitir: se admiten %s (portada, alcance, ruta y entregables son el núcleo de toda propuesta)" % (_x, ", ".join(OMITIBLES)))
    _om = [k for k in (d.get("omitir") or []) if k in ("metodo", "retorno", "proximos")]
    if _om:
        rep.aviso("omitir", "se omiten las slides %s: el criterio de Ventas (2026-10-07) pide estas láminas en toda propuesta; confirmar que aquí no aplican (charla, sesión única, etc.)"
                  % ", ".join("«%s»" % NOMBRES_SLIDE[k] for k in _om))
    if d.get("sin_hoja_cotizacion") and d.get("division") != "fundacion":
        rep.aviso("sin_hoja_cotizacion", "el deck no lleva inversión ni facilidad de pago: el valor se comunica por otro medio; confirmar con ventas")
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

    # ---------------------------------------------------------------- 1 · Portada: ¿cuál es mi problema?
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
    _corto = re.sub(r"^servicio de ", "", rotulo_servicio(d).lower())
    if p.get("eyebrow") and "habilidades" not in p["eyebrow"].lower() and _corto not in p["eyebrow"].lower():
        rep.err("portada.eyebrow", "debe nombrar el servicio («%s»): CLAUDE.md §4.1a punto 4 es bloqueante" % rotulo_servicio(d))
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
    cont = p.get("contratacion")
    if cont is not None:
        for k in ("num", "texto", "fuente"):
            if not cont.get(k):
                rep.err("portada.contratacion.%s" % k, "falta (el dato de contratación exige la fuente documentada: informe, ficha o sesión y fecha)")
        txt = rs(cont.get("texto"))
        if txt and not RE_PROBABILIDAD.search(txt):
            rep.err("portada.contratacion.texto", "la contratación evitada se plantea como probabilidad, no como compromiso (p. ej. «es alta la probabilidad de no tener que contratarlas»): decisión de dirección del 2026-10-06")
        m = RE_COMPROMISO.search(txt)
        if m:
            rep.err("portada.contratacion.texto", "promete o garantiza («%s»): usar lenguaje de probabilidad" % m.group(0))
        if re.search(r"\d\s?%", txt):
            rep.aviso("portada.contratacion.texto", "un porcentaje de probabilidad solo va si tiene base documentada; no inventarlo")
        if len(txt) > 200:
            rep.aviso("portada.contratacion.texto", "%d caracteres: máx. ~190 (2 líneas)" % len(txt))
        if len(rs(cont.get("num"))) > 6:
            rep.aviso("portada.contratacion.num", "num de %d caracteres: máx. ~6" % len(rs(cont["num"])))

    # ---------------------------------------------------------------- 2 · Alcance: qué vamos a hacer y para qué
    al = d.get("alcance") or {}
    if not al.get("subtitulo"):
        rep.err("alcance.subtitulo", "falta")
    elif len(rs(al["subtitulo"])) > 118:
        rep.aviso("alcance.subtitulo", "%d caracteres: máx. ~115 para una línea" % len(rs(al["subtitulo"])))
    fa = al.get("fuera_alcance") or []
    if len(fa) > 5:
        rep.aviso("alcance.fuera_alcance", "%d puntos: máx. 5" % len(fa))
    for i, x in enumerate(fa):
        if len(rs(x)) > 135:
            rep.aviso("alcance.fuera_alcance[%d]" % i, "%d caracteres: máx. ~130 (2 líneas)" % len(rs(x)))
    n_carr = len(set(a.get("carril") for a in d.get("areas") or []))
    lim_pq, lim_nom = (95, 38) if n_carr == 1 else (78, 46)
    for a in d.get("areas") or []:
        donde = "areas[%s]" % a.get("id")
        pq = rs(a.get("para_que"))
        if not pq:
            rep.err(donde + ".para_que", "falta: la slide de alcance debe decir qué resolvemos en cada área y para qué, en una frase corta con las palabras del cliente (Ventas, 2026-10-07)")
        elif len(pq) > 150:
            rep.err(donde + ".para_que", "%d caracteres: máx. 150 (2 líneas); lo ideal es ≤ %d (1 línea)" % (len(pq), lim_pq))
        elif len(pq) > lim_pq:
            rep.aviso(donde + ".para_que", "%d caracteres: se parte en 2 líneas y la fila crece; lo ideal es ≤ %d" % (len(pq), lim_pq))
        if len(rs(a.get("nombre"))) > lim_nom:
            rep.aviso(donde + ".nombre", "%d caracteres: máx. ~%d para no partirse junto a «N soluciones»" % (len(rs(a["nombre"])), lim_nom))

    # ---------------------------------------------------------------- 3 · Ruta: qué pasa en cada fase (una sola línea de tiempo)
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
    ruta = d.get("ruta") or {}
    if len(rs(ruta.get("nota"))) > 340:
        rep.aviso("ruta.nota", "%d caracteres: máx. ~340 (2 líneas); una tercera línea deja poca holgura contra el pie" % len(rs(ruta["nota"])))
    if len(rs(ruta.get("titulo"))) > 46:
        rep.aviso("ruta.titulo", "%d caracteres: puede pasar a 2 líneas y desplazar la grilla" % len(rs(ruta["titulo"])))
    hitos = ruta.get("hitos") or []
    if not (3 <= len(hitos) <= 5):
        rep.err("ruta.hitos", "se necesitan 3 a 5 hitos; hay %d" % len(hitos))
    for i, h in enumerate(hitos):
        if not h.get("titulo") or not h.get("texto"):
            rep.err("ruta.hitos[%d]" % i, "faltan titulo/texto")
        elif len(rs(h["texto"])) > 95:
            rep.aviso("ruta.hitos[%d]" % i, "texto de %d caracteres: máx. ~90 (3 líneas)" % len(rs(h["texto"])))
    se = ruta.get("siguiente_etapa")
    if se is not None:
        for k in ("titulo", "texto"):
            if not se.get(k):
                rep.err("ruta.siguiente_etapa.%s" % k, "falta")
        if len(rs(se.get("texto"))) > 230:
            rep.aviso("ruta.siguiente_etapa.texto", "%d caracteres: máx. ~220 (2 líneas)" % len(rs(se["texto"])))
    for c in d.get("carriles") or []:
        if len(c.get("nombre_corto") or "") > 22:
            rep.aviso("carriles[%s].nombre_corto" % c.get("id"), "%d caracteres: el rótulo de la herramienta en la línea de trabajo no admite más de ~22; definir nombre_corto" % len(c["nombre_corto"]))
    sem_tot = ruta.get("semanas_total")
    maxsem = 0
    for fr in d.get("frentes") or []:
        if fr.get("id") and not any(a.get("frente") == fr["id"] for a in d.get("areas") or []):
            rep.err("frentes[%s]" % fr["id"], "no tiene áreas asignadas (borrar la línea de trabajo o asignarle áreas): una fila de la ruta quedaría vacía")
        nums = semanas_numeros(fr.get("semanas"))
        if nums:
            maxsem = max(maxsem, max(nums))
        elif fr.get("semanas"):
            rep.err("frentes[%s].semanas" % fr.get("id"), "debe indicar las semanas con números, p. ej. «1 a 11» (recibido %r)" % fr.get("semanas"))
        nf_ = len(d.get("frentes") or [])
        fs_nom = {1: 19.0, 2: 16.5}.get(nf_, 15.0)  # letra del nombre según cuántas líneas de trabajo hay (CSS: .rg-front-h)
        if lineas_wrap(rs(fr.get("nombre")), 194.0 / (0.56 * fs_nom)) > 2:
            rep.aviso("frentes[%s].nombre" % fr.get("id"), "«%s» (%d caracteres) ocupa más de 2 líneas en la tarjeta; con %d %s caben ~%d caracteres" % (
                rs(fr["nombre"]), len(rs(fr["nombre"])), nf_, plural(nf_, "línea de trabajo", "líneas de trabajo"), int(2 * 194.0 / (0.56 * fs_nom) * 0.85)))
        dec = fr.get("_horas_fuente")
        if isinstance(dec, str):
            mm = re.match(r"\s*(\d+)", dec)
            if mm and agg["frente"].get(fr.get("id")) and int(mm.group(1)) != agg["frente"][fr["id"]][1]:
                rep.aviso("frentes[%s]" % fr.get("id"), "el insumo declaraba %s h y datos.json suma %d h (¿cambio intencional? borrar _horas_fuente si sí)" % (mm.group(1), agg["frente"][fr["id"]][1]))
    if isinstance(sem_tot, int) and maxsem and maxsem != sem_tot:
        rep.aviso("ruta.semanas_total", "vale %d pero las líneas de trabajo llegan hasta la semana %d: unificar (el título y la duración usan semanas_total)" % (sem_tot, maxsem))
    sg = d.get("seguimiento") or {}
    its = sg.get("items") or []
    if seg_tipo(d) not in ("seguimiento", "cierre", "ninguno"):
        rep.err("seguimiento.tipo", "debe ser 'seguimiento' (por defecto), 'cierre' o 'ninguno'")
    if seg_hay_columna(d):
        if not (2 <= len(its) <= 3):
            rep.err("seguimiento.items", "se necesitan 2 o 3 check-ins (30/60/90 días); hay %d" % len(its))
        for it in its:
            if not it.get("dias") or not it.get("texto"):
                rep.err("seguimiento.items", "cada check-in necesita dias y texto")
        for k in ("rango", "texto"):
            if not sg.get(k):
                rep.err("seguimiento.%s" % k, "falta")
    elif its or sg.get("rango"):
        rep.aviso("seguimiento", "tipo = «ninguno»: se ignoran rango, texto y items (la ruta termina en la última fase)")

    # ---------------------------------------------------------------- 4 · Cómo trabajamos: metodología, práctica, datos y ejemplos reales
    if "metodo" in orden:
        mt = d.get("metodo")
        if not isinstance(mt, dict):
            rep.err("metodo", "falta la sección «metodo» (slide «Cómo trabajamos»): Ventas pide explicar cómo se trabaja, cómo funciona en la práctica y cómo se cuidan los datos")
            mt = {}
        pasos_m = mt.get("pasos")
        if pasos_m is not None:
            if not (3 <= len(pasos_m) <= 4):
                rep.err("metodo.pasos", "se necesitan 3 o 4 pasos; hay %d" % len(pasos_m))
            for i, x in enumerate(pasos_m):
                if not x.get("titulo") or not x.get("texto"):
                    rep.err("metodo.pasos[%d]" % i, "faltan titulo/texto")
                else:
                    if len(rs(x["titulo"])) > 18:
                        rep.aviso("metodo.pasos[%d]" % i, "título de %d caracteres: máx. ~18" % len(rs(x["titulo"])))
                    if len(rs(x["texto"])) > 95:
                        rep.aviso("metodo.pasos[%d]" % i, "texto de %d caracteres: máx. ~90 (3 líneas)" % len(rs(x["texto"])))
        prac = mt.get("practica")
        if not prac:
            rep.err("metodo.practica", "falta: «cómo funciona en la práctica» (límites de licencias o de uso, cómo se trabaja con ellos, ventanas de prueba). Si el cliente va a preguntarlo y no está escrito, asume que no funciona (Ventas, 2026-10-07)")
        else:
            if len(prac) > 3:
                rep.err("metodo.practica", "máximo 3 puntos; hay %d" % len(prac))
            for i, x in enumerate(prac):
                if not x.get("titulo") or not x.get("texto"):
                    rep.err("metodo.practica[%d]" % i, "faltan titulo/texto")
                elif len(rs(x["texto"])) > 175:
                    rep.aviso("metodo.practica[%d]" % i, "texto de %d caracteres: máx. ~170 (4 líneas)" % len(rs(x["texto"])))
        if not mt.get("datos"):
            rep.err("metodo.datos", "falta: cómo se cuidan los datos sensibles (p. ej. casos reales anonimizados, accesos que autoriza el área de tecnología). TI del cliente lo va a preguntar (Ventas, 2026-10-07)")
        elif len(rs(mt["datos"])) > 260:
            rep.aviso("metodo.datos", "%d caracteres: máx. ~250 (5 líneas)" % len(rs(mt["datos"])))
        if len(rs(mt.get("quien_construye"))) > 230:
            rep.aviso("metodo.quien_construye", "%d caracteres: máx. ~220" % len(rs(mt["quien_construye"])))
        if len(rs(mt.get("por_que_orden"))) > 310:
            rep.aviso("metodo.por_que_orden", "%d caracteres: máx. ~300 (2 líneas)" % len(rs(mt["por_que_orden"])))
        eje = mt.get("ejemplos")
        if eje is not None:
            if not (1 <= len(eje) <= 3):
                rep.err("metodo.ejemplos", "se admiten 1 a 3 ejemplos (borrar la clave si no hay casos documentados); hay %d" % len(eje))
            for i, x in enumerate(eje):
                donde = "metodo.ejemplos[%d]" % i
                for k in ("area", "titulo", "texto", "fuente"):
                    if not x.get(k):
                        rep.err(donde, "falta %s%s" % (k, " (documento y fecha de donde sale el caso: nunca se inventan casos de éxito)" if k == "fuente" else ""))
                if bool(x.get("antes")) != bool(x.get("despues")):
                    rep.err(donde, "«antes» y «despues» van juntos (o ninguno)")
                for k, lim in (("titulo", 40), ("antes", 26), ("despues", 26), ("texto", 150), ("area", 34)):
                    if len(rs(x.get(k))) > lim:
                        rep.aviso(donde + "." + k, "%d caracteres: máx. ~%d" % (len(rs(x[k])), lim))
        lg = d.get("logistica")
        if not isinstance(lg, dict):
            rep.err("logistica", "falta la sección «logistica» (modalidad, participantes, arranque): Ventas pide que el cliente vea la logística antes de la inversión")
        else:
            for k in ("modalidad", "participantes", "arranque"):
                if not lg.get(k):
                    rep.err("logistica.%s" % k, "falta")
                elif len(rs(lg[k])) > 105:
                    rep.aviso("logistica.%s" % k, "%d caracteres: máx. ~100 (3 líneas)" % len(rs(lg[k])))
            if len(rs(lg.get("ritmo"))) > 105:
                rep.aviso("logistica.ritmo", "%d caracteres: máx. ~100" % len(rs(lg["ritmo"])))

    # ---------------------------------------------------------------- 5 · Entregables: ¿con qué me quedo?
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
        rep.err("areas", "%d filas de área: máximo 13 en la slide de alcance (con alcance.compacto). Agrupar áreas" % n_rows)
    elif n_rows > 11 and not al.get("compacto"):
        rep.aviso("areas", "%d filas de área: con más de 11 usar alcance.compacto=true y verificar holguras" % n_rows)

    # ---------------------------------------------------------------- 7 y 8 · Inversión y facilidad de pago (solo Educación)
    inv = d.get("inversion") or {}
    lic = inv.get("licencias") or {}
    tars = lic.get("tarjetas") or []
    if len(tars) > 2:
        rep.err("inversion.licencias.tarjetas", "máximo 2 tarjetas")
    if "inversion" in orden:
        for i, c in enumerate(tars):
            for k in ("nombre", "texto"):
                if not c.get(k):
                    rep.err("inversion.licencias.tarjetas[%d]" % i, "falta %s" % k)
            if len(rs(c.get("texto"))) > 255:
                rep.aviso("inversion.licencias.tarjetas[%d]" % i, "tarjeta de %d caracteres: máx. ~250; la sección podría chocar con el pie" % len(rs(c["texto"])))
            if c.get("color") and c["color"] not in COLORES:
                rep.err("inversion.licencias.tarjetas[%d].color" % i, "debe ser 'amarillo' o 'naranja'")
        if len(rs(inv.get("duracion") or "")) > 140:
            rep.aviso("inversion.duracion", "%d caracteres: máx. ~135 (3 líneas)" % len(rs(inv["duracion"])))
        # Cotización por partes (opcional): una caja de valor por parte a la izquierda y la suma (PrecioBase) a la derecha.
        partes = inv.get("partes") or []
        if partes:
            if tars:
                rep.err("inversion.partes", "comparte la zona inferior izquierda con inversion.licencias: usar una de las dos (el licenciamiento puede ir en inversion.notas)")
            if not (2 <= len(partes) <= 3):
                rep.err("inversion.partes", "se necesitan 2 o 3 partes; hay %d" % len(partes))
            for i, p in enumerate(partes):
                if not p.get("nombre"):
                    rep.err("inversion.partes[%d]" % i, "falta nombre")
                elif len(rs(p["nombre"])) > 26:
                    rep.aviso("inversion.partes[%d].nombre" % i, "%d caracteres: máx. ~26 (una línea en la tarjeta)" % len(rs(p["nombre"])))
                if len(rs(p.get("detalle"))) > 75:
                    rep.aviso("inversion.partes[%d].detalle" % i, "%d caracteres: máx. ~70 (2 líneas en la tarjeta)" % len(rs(p["detalle"])))
        if tars and not inv.get("notas"):
            rep.aviso("inversion.notas", "hay licenciamiento pero no hay notas: se usan las de garantía y términos; aclarar si el licenciamiento se contrata aparte (confirmar quién lo contrata)")
    if "pago" in orden:
        pg = d.get("pago") or {}
        cuotas = pg.get("cuotas")
        if cuotas is None:
            rep.aviso("pago", "sin plan de pago propio: se usa el estándar de empresa/politicas-comerciales.md (anticipo 50 % al aprobar y saldo 50 % al cierre). Confirmar con ventas si hay una facilidad distinta (cuotas ligadas a hitos)")
        else:
            if not (2 <= len(cuotas) <= 6):
                rep.err("pago.cuotas", "se necesitan 2 a 6 cuotas; hay %d" % len(cuotas))
            total = 0.0
            for i, c in enumerate(cuotas):
                donde = "pago.cuotas[%d]" % i
                if not c.get("cuando") or not c.get("hito"):
                    rep.err(donde, "faltan cuando/hito")
                if not es_num(c.get("pct")) or c.get("pct") <= 0:
                    rep.err(donde + ".pct", "debe ser un porcentaje > 0 (recibido %r)" % (c.get("pct"),))
                else:
                    total += c["pct"]
                if len(rs(c.get("cuando"))) > 16:
                    rep.aviso(donde + ".cuando", "%d caracteres: máx. ~16 (una línea en la tarjeta)" % len(rs(c["cuando"])))
                if cuotas and lineas_wrap(rs(c.get("hito")), ((1011.0 - 14.0 * (len(cuotas) - 1)) / len(cuotas) - 38) / 6.3) > 4:
                    rep.aviso(donde + ".hito", "%d caracteres: ocupa más de 4 líneas en la tarjeta (con %d cuotas caben ~%d caracteres); acortar el hito" % (
                        len(rs(c["hito"])), len(cuotas), int(4 * ((1011.0 - 14.0 * (len(cuotas) - 1)) / len(cuotas) - 38) / 6.3 * 0.9)))
            if cuotas and abs(total - 100) > 0.01:
                rep.err("pago.cuotas", "los porcentajes suman %s %% y deben sumar 100" % fmt_es(total))
        if not pg.get("facturacion"):
            rep.aviso("pago.facturacion", "sin «facturacion»: el cliente no verá en qué moneda ni a qué tasa se factura (moneda e impuestos siguen pendientes en empresa/politicas-comerciales.md): confirmar con ventas")
        if len(rs(pg.get("mensaje"))) > 230:
            rep.aviso("pago.mensaje", "%d caracteres: máx. ~220 (2 líneas)" % len(rs(pg["mensaje"])))
        if len(rs(pg.get("facturacion"))) > 200:
            rep.aviso("pago.facturacion", "%d caracteres: máx. ~190" % len(rs(pg["facturacion"])))
    _por = ("en Fundación" if d.get("division") == "fundacion" else ("porque sin_hoja_cotizacion = true" if d.get("sin_hoja_cotizacion") else "porque está en omitir"))
    if "inversion" not in orden and inv:
        rep.aviso("inversion", "se ignora %s (no hay slide de inversión); llevar licencias y notas a otra parte si hacen falta" % _por)
    if "pago" not in orden and d.get("pago"):
        rep.aviso("pago", "se ignora %s (no hay slide de facilidad de pago)" % _por)

    # ---------------------------------------------------------------- 6 · Retorno: ¿qué gano con esto?
    if "retorno" in orden:
        validar_retorno(d, ctx, agg, rep, rs)

    # ---------------------------------------------------------------- 9 · Próximos pasos: llamado a la acción y a quién escribir
    if "proximos" in orden:
        pp = d.get("proximos_pasos")
        if not isinstance(pp, dict):
            rep.err("proximos_pasos", "falta la sección «proximos_pasos» con la asesora comercial: la última slide dice qué hacer y a quién escribir (Ventas, 2026-10-07)")
            pp = {}
        ase = pp.get("asesora")
        if not isinstance(ase, dict):
            rep.err("proximos_pasos.asesora", "falta: nombre y correo de la asesora comercial (cargo y teléfono opcionales)")
        else:
            for k in ("nombre", "correo"):
                if not ase.get(k):
                    if k == "correo" and ase.get("telefono"):
                        rep.aviso("proximos_pasos.asesora.correo", "sin correo: la slide muestra solo el teléfono y el correo general de Intezia; confirmar el correo del contacto antes de enviar")
                    else:
                        rep.err("proximos_pasos.asesora.%s" % k, "falta (el correo puede omitirse solo si hay teléfono)")
            if ase.get("correo") and not re.match(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$", ase["correo"]):
                rep.err("proximos_pasos.asesora.correo", "no parece un correo válido: %r" % ase["correo"])
        pasos_p = pp.get("pasos")
        if pasos_p is not None:
            if len(pasos_p) != 3:
                rep.err("proximos_pasos.pasos", "deben ser exactamente 3 pasos; hay %d" % len(pasos_p))
            for i, x in enumerate(pasos_p):
                if not x.get("titulo") or not x.get("texto"):
                    rep.err("proximos_pasos.pasos[%d]" % i, "faltan titulo/texto")
                else:
                    m = RE_ECONOMICO.search(rs(x["titulo"]) + " " + rs(x["texto"]))
                    if m:
                        rep.err("proximos_pasos.pasos[%d]" % i, "«%s»: los próximos pasos describen logística, nunca acuerdos económicos (CLAUDE.md §4.15)" % m.group(0))
                    if len(rs(x["texto"])) > 130:
                        rep.aviso("proximos_pasos.pasos[%d]" % i, "texto de %d caracteres: máx. ~120 (4 líneas)" % len(rs(x["texto"])))
                    if len(rs(x["titulo"])) > 24:
                        rep.aviso("proximos_pasos.pasos[%d]" % i, "título de %d caracteres: máx. ~22" % len(rs(x["titulo"])))


def set_vocab(d):
    """Vocabulario de la propuesta (ver VOC_DEF): el de Habilidades salvo que datos.json → vocabulario diga otro."""
    VOC.clear()
    VOC.update(VOC_DEF)
    v = d.get("vocabulario") if isinstance(d.get("vocabulario"), dict) else {}
    for k in VOC_DEF:
        x = v.get(k)
        if isinstance(x, list) and len(x) == 2 and all(isinstance(i, str) and i.strip() for i in x):
            VOC[k] = (x[0].strip(), x[1].strip())


def vocab_por_defecto():
    return VOC == VOC_DEF


def sub_entregables_defecto(d):
    """Subtítulo por defecto de la slide de entregables. Con otro vocabulario (curso, charla, Detección…) no se habla de «soluciones
    construidas, probadas y adoptadas» y con tipo de seguimiento distinto de «seguimiento» no se promete el seguimiento 30-60-90."""
    if vocab_por_defecto():
        return SUB_ENTREGABLES if seg_es_seguimiento(d) else SUB_ENTREGABLES_SIN_SEG
    return SUB_ENTREGABLES_VOC if seg_es_seguimiento(d) else SUB_ENTREGABLES_VOC_SIN_SEG


def seg_tipo(d):
    return (d.get("seguimiento") or {}).get("tipo") or "seguimiento"


def seg_es_seguimiento(d):
    """True salvo que seguimiento.tipo = «cierre» (la última columna de la ruta muestra el cierre, no un seguimiento) o «ninguno»."""
    return seg_tipo(d) not in ("cierre", "ninguno")


def seg_hay_columna(d):
    """False si seguimiento.tipo = «ninguno»: la ruta termina en la última fase y no se exigen rango, texto ni check-ins."""
    return seg_tipo(d) != "ninguno"


def sin_inversion(d):
    """True si el deck no lleva hoja de inversión ni de pago: Fundación, datos.json → sin_hoja_cotizacion = true, u omitir con «inversion»."""
    return d.get("division") == "fundacion" or bool(d.get("sin_hoja_cotizacion")) or "inversion" in (d.get("omitir") or [])


def anuncia_duracion(d):
    """False si datos.json → anunciar_duracion = false: el titular de la ruta y la Duración de la inversión no nombran el número de semanas.
    Por defecto se anuncian (las propuestas anteriores no llevan la clave y no cambian)."""
    return d.get("anunciar_duracion") is not False


def con_garantia(d):
    """La garantía 30-60-90 vive en la hoja de inversión: solo hay garantía con seguimiento, con cotización y sin inversion.sin_garantia."""
    return seg_es_seguimiento(d) and not sin_inversion(d) and not (d.get("inversion") or {}).get("sin_garantia")


def rotulo_servicio(d):
    """Servicio que se nombra en el deck. Por defecto «Servicio de Habilidades»; un combo (Detección + Habilidades) o Detección lo declara en
    datos.json → servicio_rotulo (CLAUDE.md §4.1a punto 4: nombrar los servicios reales)."""
    return (d.get("servicio_rotulo") or "Servicio de Habilidades").strip()


def orden_slides(d):
    """Orden de las slides: el de las preguntas del cliente, sin las que la propuesta omite (Fundación y «sin cotización» no llevan inversión ni pago)."""
    omitir = set(x for x in (d.get("omitir") or []) if isinstance(x, str))
    if sin_inversion(d):
        omitir |= {"inversion", "pago"}
    return [k for k in ORDEN_EDUCACION if k not in omitir]


# ----------------------------------------------------------------------------------------------
# Slide 5: reparto de áreas en columnas (estimador calibrado con mediciones reales, 2026-10-05)
# ----------------------------------------------------------------------------------------------
def nombre_catalogo(a):
    n = a.get("nombre_catalogo") or a["nombre"]
    if a.get("proceso_base"):
        etq = ESTADO.get("etq_base") or VOC["proceso_base"][0]
        if etq.lower() not in n.lower() and "proceso base" not in n.lower():
            n += " (%s)" % etq
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


def cupo_catalogo(d, R):
    """Cupo en px de la columna más alta: depende del alto de la cabecera (título + subtítulo)."""
    en = d["entregables"]
    titulo = R.t(en.get("titulo") or "Todo lo que {cliente_corto} recibe.", "entregables.titulo")
    sub = sin_marcado(R.t(en.get("subtitulo") or sub_entregables_defecto(d), "entregables.subtitulo"))
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


def s_portada(d, R):
    p = d["portada"]
    T, M = R.T, R.M
    eyebrow = p.get("eyebrow") or ("Propuesta de proyecto · " + rotulo_servicio(d))
    hechos = "".join(
        '          <div class="pain-item">\n'
        '            <span class="pain-num">%s</span>\n'
        '            <span class="pain-lbl">%s</span>\n'
        "          </div>\n" % (T(h["num"], "portada.hechos.num"), M(h["texto"], "portada.hechos.texto"))
        for h in p.get("hechos", [])
    )
    cc = p.get("contratacion")
    contratacion = ""
    if cc:
        contratacion = (
            '        <div class="hire-note">\n'
            '          <span class="hire-num">%s</span>\n'
            "          <p>%s</p>\n"
            "        </div>\n" % (T(cc["num"], "portada.contratacion.num"), M(cc["texto"], "portada.contratacion.texto"))
        )
    fuente = ('        <p class="pain-src">%s</p>\n' % T(p["fuente"], "portada.fuente")) if p.get("fuente") else ""
    lineas, dest, px, _cpl, _tot = titulo_portada(p, lambda x: sin_marcado(R.t(x, "portada.titulo")))
    h1 = "".join("          %s<br>\n" % esc(x) for x in lineas) + '          <span class="hl">%s</span>\n' % esc(dest)
    return (
        '    <!-- 1 · Portada: ¿cuál es mi problema? -->\n'
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
        '        <div class="pain-strip">\n%s        </div>\n%s%s'
        "      </div>\n"
        '      <div class="id-line">\n'
        '        <span class="codigo">Código: %s</span>\n'
        '        <span class="cliente">%s</span>\n'
        "      </div>\n"
        "    </section>\n"
        % (R.contador("portada"), R.rel_logos, R.div_nombre, T(eyebrow, "portada.eyebrow"),
           px, h1,
           M(p["lead"], "portada.lead"), hechos, contratacion, fuente, esc(R.codigo), T(R.pie, "cliente.nombre_pie"))
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


def alcance_roomy(d):
    """Pocas filas de área: la slide de alcance usa más aire y letra más grande."""
    al = d["alcance"]
    carr = [c for c in d["carriles"] if any(a["carril"] == c["id"] for a in d["areas"])]
    max_filas = max(len([a for a in d["areas"] if a["carril"] == c["id"]]) for c in carr) if carr else 0
    return (not al.get("compacto")) and ((len(carr) == 1 and max_filas <= 7) or (len(carr) == 2 and max_filas <= 4))


def estimar_alcance(d, R):
    """Holgura estimada (px) de la slide de alcance contra el pie (modo normal o compacto). Calibrada con DUSA v2, 2026-10-07:
    filas de 52,7 px con dos paneles, panel de 5 y 6 filas = 324,5 y 377,2 px, franja «fuera de alcance» = 103,2 px, holgura = 97,4 px."""
    al = d["alcance"]
    tk = lambda x: sin_marcado(R.t(x or "", "alcance"))
    carr = [c for c in d["carriles"] if any(a["carril"] == c["id"] for a in d["areas"])]
    compacto = bool(al.get("compacto"))
    uno = len(carr) == 1
    paneles = []
    for c in carr:
        h = (13.0 if compacto else 27.0) + 34.8
        for a in [a for a in d["areas"] if a["carril"] == c["id"]]:
            lp = lineas_wrap(tk(a.get("para_que")), 92 if uno else 80)
            base = (34.7 if uno else 53.0) - (5.0 if compacto else 0.0)
            h += base + 15.5 * (lp - 1) + (14.0 if a.get("composicion") else 0.0)
        paneles.append(h)
    fuera = al.get("fuera_alcance") or []
    h_out = 0.0
    if fuera:
        hs = [lineas_wrap(tk(x), 62) * 16.8 + 5.0 for x in fuera]
        mejor = min(max(sum(hs[:k]), sum(hs[k:])) for k in range(len(hs) + 1))
        h_out = 14.0 + 26.0 + mejor
    cab = 150.2 + (37.8 if len(tk(al.get("titulo") or titulo_alcance_defecto(R))) > 50 else 0) + (21.0 if len(tk(al.get("subtitulo"))) > 118 else 0)
    return 742.0 - (cab + max(paneles + [0.0]) + h_out)


def s_alcance(d, R):
    """2 · Alcance: qué vamos a hacer y para qué (cada área dice qué resuelve), más lo que queda fuera."""
    T, M = R.T, R.M
    al = d["alcance"]
    titulo = al.get("titulo") or titulo_alcance_defecto(R)
    carr = [c for c in d["carriles"] if any(a["carril"] == c["id"] for a in d["areas"])]
    etq_base = T(al.get("etiqueta_proceso_base") or VOC["proceso_base"][0], "alcance.etiqueta_proceso_base")
    paneles = ""
    for c in carr:
        areas = [a for a in d["areas"] if a["carril"] == c["id"]]
        ca = R.agg["carril"][c["id"]]
        filas = ""
        for a in areas:
            n = R.agg["area"][a["id"]][0]
            em = (" <em>(%s)</em>" % etq_base) if a.get("proceso_base") else ""
            comp = (' <small class="comp">%s</small>' % T(a["composicion"], "areas.composicion")) if a.get("composicion") else ""
            filas += (
                '              <li><span class="area">%s%s%s</span><span class="n">%d %s</span><span class="para">%s</span></li>\n'
                % (T(a["nombre"], "areas.nombre"), em, comp, n, plural(n, *VOC["solucion"]), T(a["para_que"], "areas.para_que"))
            )
        paneles += (
            '        <div class="scope-panel %s">\n'
            '          <div class="scope-head">\n'
            '            <span class="scope-tag">%s</span>\n'
            '            <span class="scope-total"><b>%d</b> %s · %d %s</span>\n'
            "          </div>\n"
            '          <ul class="scope-rows">\n%s          </ul>\n'
            "        </div>\n"
            % (COLORES[c["color"]], T(c["nombre"], "carriles.nombre"), ca["n"], plural(ca["n"], *VOC["solucion"]),
               ca["areas"], plural(ca["areas"], *VOC["area"]), filas)
        )
    roomy = alcance_roomy(d)  # pocas filas: más aire y letra más grande
    fuera = ""
    if al.get("fuera_alcance"):
        li = "".join("          <li>%s</li>\n" % M(x, "alcance.fuera_alcance") for x in al["fuera_alcance"])
        fuera = (
            '      <div class="scope-out">\n'
            '        <p class="scope-card-label">%s</p>\n'
            "        <ul>\n%s        </ul>\n"
            "      </div>\n\n" % (T(al.get("etiqueta_fuera") or "Fuera de este alcance", "alcance.etiqueta_fuera"), li)
        )
    return (
        '    <!-- 2 · Alcance: qué vamos a hacer y para qué -->\n'
        '    <section class="slide s-scope%s%s">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Alcance</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="scope-panels%s" style="--np:%d">\n%s      </div>\n\n%s%s'
        "    </section>\n"
        % (" compact" if al.get("compacto") else "", " roomy" if roomy else "", R.contador("alcance"), R.idx["alcance"], T(titulo, "alcance.titulo"),
           M(al["subtitulo"], "alcance.subtitulo"), " one" if len(carr) == 1 else "", len(carr), paneles, fuera, foot(R, "claro"))
    )


def s_ruta(d, R):
    """3 · Ruta: qué pasa en cada fase. Una sola línea de tiempo, con las soluciones primero y las horas en pequeño."""
    T, M = R.T, R.M
    ruta = d["ruta"]
    seg = d["seguimiento"]
    fases_cols = [f for f in d["fases"] if f.get("id") != "F0"]
    nf = len(d["frentes"])
    ncols = len(fases_cols)
    rowh = {1: 214, 2: 130, 3: 104}[nf]
    titulo = ruta.get("titulo") or (("%s, {semanas_txt}." if anuncia_duracion(d) else "%s.") % PALABRAS_FRENTES[nf])
    if con_garantia(d):
        sub_def = "Semanas de trabajo desde el arranque. La **garantía y el seguimiento** a {rango_seguimiento} corren desde el cierre de cada área."
    elif seg_es_seguimiento(d):
        sub_def = "Semanas de trabajo desde el arranque. El **seguimiento** a {rango_seguimiento} corre desde el cierre de cada área."
    else:
        sub_def = "Semanas de trabajo desde el arranque."
    sub = ruta.get("subtitulo") or sub_def
    hdr = '        <div class="rg-corner"></div>\n'
    for i, f in enumerate(fases_cols, 1):
        n, h = R.agg["fase"].get(f["id"], [0, 0])
        hi = bool(f.get("destacada"))
        hdr += (
            '        <div class="rg-phase rg-ph-%d%s">\n'
            '          <span class="rg-phase-top"><span class="rg-phase-tag">%s</span><b class="rg-phase-n">%d %s</b></span>\n'
            '          <span class="rg-phase-date">%s</span>\n'
            '          <span class="rg-phase-txt">%s</span>\n'
            "        </div>\n" % (i, " hi" if hi else "", T(f["titulo"], "fases.titulo"), n, plural(n, *VOC["solucion"]),
                                 T(f["rango"], "fases.rango"), md(cap1(R.t(f["descripcion"], "fases.descripcion"))))
        )
    if seg_hay_columna(d):
        etq_seg = seg.get("etiqueta") or ("Garantía" if con_garantia(d) else ("Seguimiento" if seg_es_seguimiento(d) else "Cierre"))
        hdr += (
            '        <div class="rg-phase rg-fu">\n'
            '          <span class="rg-phase-top"><span class="rg-phase-tag">%s</span></span>\n'
            '          <span class="rg-phase-date">%s</span>\n'
            '          <span class="rg-phase-txt">%s</span>\n'
            "        </div>\n" % (T(etq_seg, "seguimiento.etiqueta"), T(seg["rango"], "seguimiento.rango"), M(seg["texto"], "seguimiento.texto"))
        )
    cuerpo = ""
    carriles = dict((c["id"], c) for c in d["carriles"])
    for fr in d["frentes"]:
        n, h = R.agg["frente"].get(fr["id"], [0, 0])
        car = carriles[fr["carril"]]
        cuerpo += (
            '        <div class="rg-front %s">\n'
            '          <span class="rg-front-h">%s</span>\n'
            '          <span class="rg-front-row"><span class="rg-front-tool">%s</span><b class="rg-front-n">%d %s</b></span>\n'
            '          <span class="rg-front-meta">%s · %d h</span>\n'
            "        </div>\n" % (COLORES[car["color"]], T(fr["nombre"], "frentes.nombre"), T(car["nombre_corto"], "carriles.nombre_corto"),
                                 n, plural(n, *VOC["solucion"]), esc(txt_semanas(R.t(fr["semanas"], "frentes.semanas"))), h)
        )
        for f in fases_cols:
            nn, hh = R.agg["celda"].get((fr["id"], f["id"]), [0, 0])
            hi = " hi" if f.get("destacada") else ""
            txt = (fr.get("celdas") or {}).get(f["id"], "")
            if nn:
                cuerpo += (
                    '        <div class="rg-cell%s"><span class="rg-h"><b>%d</b> %s <i>%d h</i></span><p>%s</p></div>\n'
                    % (hi, nn, plural(nn, *VOC["solucion"]), hh, M(txt, "frentes.celdas"))
                )
            else:
                cuerpo += '        <div class="rg-cell empty%s"><p>Sin entregas en esta fase.</p></div>\n' % hi
    follow = ""
    if seg_hay_columna(d):
        items = "".join(
            "            <li><b>%s</b><span>%s</span></li>\n" % (T(i["dias"], "seguimiento.items.dias"), M(i["texto"], "seguimiento.items")) for i in seg["items"]
        )
        follow = (
            '        <div class="rg-follow" style="grid-column:%d; grid-row:2 / span %d">\n'
            "          <ul>\n%s          </ul>\n"
            "        </div>\n" % (ncols + 2, nf, items)
        )
    grid_cols = "" if seg_hay_columna(d) else "; grid-template-columns:226px repeat(%d,1fr)" % ncols  # sin quinta columna: la grilla acaba en la última fase
    hitos = ruta["hitos"]
    mil = "".join(
        '        <div class="mile"><span class="mile-d"></span><b>%s</b><p>%s</p></div>\n'
        % (T(h["titulo"], "ruta.hitos.titulo"), M(h["texto"], "ruta.hitos.texto")) for h in hitos
    )
    nums = [f["id"][1:] for f in fases_cols]  # números reales de las fases (F1, F3 -> «1 y 3»)
    nota = ruta.get("nota") or (
        "Las fases se traslapan: cada línea de trabajo pasa a la siguiente cuando quien ejecuta el proceso ya opera lo anterior. "
        + ("Las {h_total} horas de trabajo son una proyección: {h_f0} h de arranque más " if R.ctx.get("h_f0") else "Las {h_total} horas de trabajo son una proyección: ")
        + ", ".join("{h_%s}" % f["id"].lower() for f in fases_cols[:-1])
        + " y {h_%s} h de las fases " % fases_cols[-1]["id"].lower()
        + ", ".join(nums[:-1]) + " y %s." % nums[-1]
    )
    sig = ""
    if ruta.get("siguiente_etapa"):
        se = ruta["siguiente_etapa"]
        sig = '      <p class="route-next"><b>%s</b> %s</p>\n' % (T(se["titulo"], "ruta.siguiente_etapa.titulo"), M(se["texto"], "ruta.siguiente_etapa.texto"))
    return (
        '    <!-- 3 · Ruta: qué pasa en cada fase -->\n'
        '    <section class="slide s-route">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Ruta</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="route-grid n%d" style="--cols:%d; --rows:%d; --rowh:%dpx%s">\n\n%s\n%s\n%s      </div>\n\n'
        '      <div class="route-miles" style="grid-template-columns:repeat(%d,1fr)">\n%s      </div>\n'
        '      <p class="route-note">%s</p>\n%s\n%s'
        "    </section>\n"
        % (R.contador("ruta"), R.idx["ruta"], T(titulo, "ruta.titulo"), M(sub, "ruta.subtitulo"), nf, ncols, nf, rowh, grid_cols,
           hdr, cuerpo, follow, len(hitos), mil, M(nota, "ruta.nota"), sig, foot(R, "oscuro"))
    )

def por_que_defecto(d):
    """«Por qué en este orden»: se arma con la descripción de cada fase."""
    fc = [f for f in d["fases"] if f.get("id") != "F0"]
    ds = [(f["id"][1:], (f.get("descripcion") or "").strip().rstrip(".")) for f in fc]
    partes = []
    for i, (n, ds_) in enumerate(ds):
        lead = "primero" if i == 0 else ("al final" if i == len(ds) - 1 else "después")
        partes.append("%s la fase %s (%s)" % (lead, n, ds_))
    return cap1("; ".join(partes)) + "."

def metodo_roomy(d):
    """Sin casos ya logrados y con textos cortos: la slide «Cómo trabajamos» usa letra más grande y más aire."""
    mt = d["metodo"]
    largo = sum(len(sin_marcado(x.get("texto") or "")) + len(x.get("titulo") or "") for x in mt["practica"])
    return (not mt.get("ejemplos")) and largo <= 330 and len(mt["datos"]) <= 260 and len(mt.get("quien_construye") or "") <= 200


def estimar_metodo(d, R):
    """Holgura estimada (px) de la slide «Cómo trabajamos» contra el pie (modo normal). Calibrada con DUSA (11,6 px medidos) y
    el ejemplo de Fundación, 2026-10-07: cada bloque suma su alto fijo más sus líneas de texto por el alto de línea."""
    mt = d["metodo"]
    rs = lambda x: sin_marcado(R.t(x or "", "metodo"))
    pasos = mt.get("pasos") or PASOS_METODO
    h_steps = max(72.0, 45.0 + 15.64 * max(lineas_wrap(rs(p["texto"]), 178 / 5.75) for p in pasos))
    quien = mt.get("quien_construye")
    por_que = rs(mt.get("por_que_orden") or por_que_defecto(d))
    l_why = lineas_wrap("Por qué en este orden " + por_que, ((555 if quien else 1011) - 32) / 5.75)
    l_who = lineas_wrap("Quién construye " + rs(quien), (444 - 32) / 5.75) if quien else 0
    h_strips = 16.0 + 16.1 * max(l_why, l_who)
    eje = mt.get("ejemplos") or []
    h_proof = 0.0
    if eje:
        l_caso = max(lineas_wrap(rs(x["texto"]), 218 / 5.2) for x in eje)
        h_casos = (73.0 if any(x.get("antes") for x in eje) else 52.0) + 14.96 * l_caso
        fuentes = "; ".join(sorted(set(rs(x["fuente"]) for x in eje)))
        h_head = 36.0 + 6.0 + 14.3 * lineas_wrap(rs(mt.get("nota_ejemplos")) + " Fuente: " + fuentes + ".", 214 / 5.25)
        h_proof = max(h_casos, h_head) + 23.8
    prac = sum(lineas_wrap(rs(x["titulo"]) + ". " + rs(x["texto"]), (569 - 12) / 5.75) * 16.1 + 3 for x in mt["practica"])
    h_info = max(48.0 + prac, 48.0 + 16.1 * lineas_wrap(rs(mt["datos"]), 340 / 5.75))
    lg = d["logistica"]
    ritmo = lg.get("ritmo") or "Hasta {tope_h_semana} horas de trabajo por semana en cada línea de trabajo ({tope_h_dia} por día)."
    l_tile = max(lineas_wrap(rs(v), (221 - 24) / 5.5) for v in (lg["modalidad"], lg["participantes"], ritmo, lg["arranque"]))
    h_logi = 30.0 + 14.5 * l_tile
    h_cab = 150.2 + (37.8 if len(rs(mt.get("titulo") or "Así trabajamos cada solución.")) > 40 else 0) + (21.0 if len(rs(mt.get("subtitulo") or "x" * 100)) > 118 else 0)
    base = h_cab + h_steps + 10 + h_strips + 10 + h_proof + 10 + h_info + 10 + h_logi
    if os.environ.get("HAB_DEBUG"):
        print("[estimador] metodo partes: cab %.1f steps %.1f strips %.1f proof %.1f info %.1f logi %.1f" % (h_cab, h_steps, h_strips, h_proof, h_info, h_logi))
    return 742.0 - base


def s_metodo(d, R):
    """4 · Cómo trabajamos: los pasos de cada solución y por qué en ese orden, quién construye, casos reales ya logrados,
    cómo funciona en la práctica, cómo se cuidan los datos y la logística."""
    T, M = R.T, R.M
    mt = d["metodo"]
    titulo = mt.get("titulo") or ("Así trabajamos cada %s." % VOC["solucion"][0])
    sub = mt.get("subtitulo") or "Trabajamos junto a quien ejecuta cada proceso, con sus casos reales, y dejamos medido el resultado."
    pasos = mt.get("pasos") or PASOS_METODO
    li = "".join(
        "          <li><b>%s</b><span>%s</span></li>\n" % (T(p["titulo"], "metodo.pasos.titulo"), M(p["texto"], "metodo.pasos")) for p in pasos
    )
    por_que = mt.get("por_que_orden") or por_que_defecto(d)
    por_que_cls = "mt-why" if mt.get("por_que_orden") else "mt-why auto"
    franjas = '        <p class="%s"><b>Por qué en este orden</b> %s</p>\n' % (por_que_cls, M(por_que, "metodo.por_que_orden"))
    if mt.get("quien_construye"):
        franjas += '        <p class="mt-who"><b>Quién construye</b> %s</p>\n' % M(mt["quien_construye"], "metodo.quien_construye")
    proof = ""
    eje = mt.get("ejemplos") or []
    if eje:
        casos = ""
        for x in eje:
            ba = ""
            if x.get("antes"):
                ba = '            <span class="mc-ba"><i>%s</i><u>→</u><i class="ok">%s</i></span>\n' % (T(x["antes"], "metodo.ejemplos.antes"), T(x["despues"], "metodo.ejemplos.despues"))
            casos += (
                '          <div class="mt-case">\n'
                '            <span class="mc-area">%s</span>\n'
                "            <b>%s</b>\n%s"
                "            <p>%s</p>\n"
                "          </div>\n" % (T(x["area"], "metodo.ejemplos.area"), T(x["titulo"], "metodo.ejemplos.titulo"), ba, M(x["texto"], "metodo.ejemplos.texto"))
            )
        fuentes = []
        for x in eje:
            if x["fuente"] not in fuentes:
                fuentes.append(x["fuente"])
        nota_e = (T(mt["nota_ejemplos"], "metodo.nota_ejemplos") + " ") if mt.get("nota_ejemplos") else ""
        proof = (
            '      <div class="mt-proof">\n'
            '        <div class="mp-head">\n'
            '          <span class="mp-tag">%s</span>\n'
            '          <p>%s<span class="mp-src">Fuente: %s.</span></p>\n'
            "        </div>\n"
            '        <div class="mp-cases" style="--n:%d">\n%s        </div>\n'
            "      </div>\n\n"
            % (T(mt.get("etiqueta_ejemplos") or "Casos reales ya logrados", "metodo.etiqueta_ejemplos"), nota_e,
               "; ".join(T(f, "metodo.ejemplos.fuente") for f in fuentes), len(eje), casos)
        )
    tarjetas = [
        ("Cómo funciona en la práctica", "<ul>%s</ul>" % "".join(
            "<li><b>%s.</b> %s</li>" % (T(x["titulo"].rstrip(".:; "), "metodo.practica.titulo"), M(x["texto"], "metodo.practica")) for x in mt["practica"])),
        ("Cómo cuidamos sus datos", "<p>%s</p>" % M(mt["datos"], "metodo.datos")),
    ]
    info = "".join(
        '        <div class="mt-card">\n          <p class="mt-card-label">%s</p>\n          %s\n        </div>\n' % (esc(e), h) for e, h in tarjetas
    )
    lg = d["logistica"]
    ritmo = lg.get("ritmo") or "Hasta {tope_h_semana} horas de trabajo por semana en cada línea de trabajo ({tope_h_dia} por día)."
    tiles = "".join(
        '        <div class="mt-tile"><span>%s</span><b>%s</b></div>\n' % (esc(e), M(v, "logistica"))
        for e, v in (("Modalidad", lg["modalidad"]), ("Participantes", lg["participantes"]), ("Ritmo de trabajo", ritmo), ("Arranque", lg["arranque"]))
    )
    roomy = metodo_roomy(d)  # sin casos ya logrados y con textos cortos: más aire y letra más grande
    return (
        '    <!-- 4 · Cómo trabajamos: pasos, por qué en ese orden, casos reales, práctica, datos y logística -->\n'
        '    <section class="slide s-method%s">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Cómo trabajamos</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <ol class="mt-steps" style="--n:%d">\n%s      </ol>\n'
        '      <div class="mt-strips%s">\n%s      </div>\n\n%s'
        '      <div class="mt-info">\n%s      </div>\n\n'
        '      <div class="mt-logi">\n%s      </div>\n\n%s'
        "    </section>\n"
        % (" roomy" if roomy else "", R.contador("metodo"), R.idx["metodo"], T(titulo, "metodo.titulo"), M(sub, "metodo.subtitulo"), len(pasos), li,
           "" if mt.get("quien_construye") else " one", franjas, proof, info, tiles, foot(R, "claro"))
    )


def programa_auto(d, R):
    """Líneas por defecto del campo Programa: soluciones primero y horas en pequeño (criterio de Ventas, 2026-10-06).
    Se elige la versión más completa que quepa en la caja del PDF (6 líneas)."""
    t = R.t
    cab = rotulo_servicio(d) + " · {cliente_corto}, {n_areas_txt} ({codigo})."
    por_frente = []
    for fr in d["frentes"]:
        n, h = R.agg["frente"].get(fr["id"], [0, 0])
        por_frente.append("%s: %d %s, %d h" % (sin_marcado(t(fr["nombre"], "frentes.nombre")), n, plural(n, *VOC["solucion"]), h))
    cierre = "Horas de sesión: trabajo con quien ejecuta cada proceso."
    resumen = "{n_total_txt} en {n_frentes_txt}, {h_total} h de sesión."
    maxl = CAJAS_PDF["Programa"][3]
    for cand in ([cab] + por_frente + [cierre], [cab] + por_frente, [cab, resumen]):
        lineas = [t(x, "inversion.programa") for x in cand]
        if lineas_caja(lineas, "Programa") <= maxl:
            break
    return lineas


def s_inversion(d, R):
    """7 · Inversión (antepenúltima): hoja de cotización estándar. Se cobra por proyecto, no por hora."""
    T, M = R.T, R.M
    inv = d.get("inversion") or {}
    titulo = inv.get("titulo") or "Inversión del proyecto."
    en_semanas = " a realizar en un total de {semanas_txt}" if anuncia_duracion(d) else ""
    if con_garantia(d):
        dur_def = "Proyecto de {n_total_txt}" + en_semanas + ", con seguimiento y garantía a {rango_seguimiento}. {h_total} horas de trabajo."
    elif seg_es_seguimiento(d):
        dur_def = "Proyecto de {n_total_txt}" + en_semanas + ", con seguimiento a {rango_seguimiento}. {h_total} horas de trabajo."
    else:
        dur_def = "Proyecto de {n_total_txt}" + en_semanas + ". {h_total} horas de trabajo."
    dur = inv.get("duracion") or dur_def
    garantia = inv.get("garantia_texto") or "Estamos contigo hasta que la habilidad quede instalada."
    garantia_html = ("" if not con_garantia(d) else (
        '      <div class="cot-garantia-badge">\n'
        '        <span class="cot-garantia-tag">Garantía 30-60-90</span>\n'
        '        <p class="cot-garantia-text">%s</p>\n'
        "      </div>\n\n" % T(garantia, "inversion.garantia_texto")))
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
    # Cotización por partes (opcional): una caja de valor por parte (PrecioParte1..N) en la zona del licenciamiento y la
    # suma en la caja base de la derecha. La geometría DEBE coincidir con scripts/agregar-campo-precio.py → partes_fields().
    partes = inv.get("partes") or []
    label_base = "Propuesta + Inversión"
    if partes:
        label_base = T(inv.get("etiqueta_suma") or "Suma de las partes", "inversion.etiqueta_suma")
        tarjetas = ""
        for i, p_ in enumerate(partes, 1):
            det = ('            <p class="parte-det">%s</p>\n' % T(p_["detalle"], "inversion.partes.detalle")) if p_.get("detalle") else ""
            tarjetas += (
                '          <div class="parte-card %s">\n'
                '            <span class="parte-tag">Parte %d</span>\n'
                '            <b class="parte-name">%s</b>\n%s'
                '            <div class="parte-frame"></div>\n'
                "          </div>\n" % ("acc-y" if i % 2 else "acc-o", i, T(p_["nombre"], "inversion.partes.nombre"), det)
            )
        lic_html = (
            '      <div class="partes-wrap">\n'
            '        <span class="partes-eyebrow">%s</span>\n'
            '        <div class="partes-cards">\n%s        </div>\n'
            "      </div>\n\n" % (T(inv.get("etiqueta_partes") or "Valor por parte", "inversion.etiqueta_partes"), tarjetas)
        )
    return (
        '    <!-- 7 · Inversión (hoja de cotización estándar; antepenúltima slide) -->\n'
        '    <section class="slide s-price">\n'
        '      <span class="counter">%s</span>\n'
        '      <h2 class="title">%s</h2>\n'
        '      <p class="price-intro">Propuesta Económica · %s</p>\n\n'
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
        '      <span class="cot-label cot-label-base">%s</span>\n'
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
        '%s'
        '      <div class="block block-notes-container">\n'
        '        <span class="block-eyebrow">Notas</span>\n'
        "      </div>\n"
        '      <div class="multi-box notas-box" data-field="Notas"></div>\n\n%s%s'
        "    </section>\n"
        % (R.contador("inversion"), T(titulo, "inversion.titulo"), T(rotulo_servicio(d), "servicio_rotulo"), M(dur, "inversion.duracion"), label_base, garantia_html, lic_html, foot(R, "claro"))
    )


def s_entregables(d, R, columnas, ncols):
    """5 · Entregables: ¿con qué me quedo? Catálogo de todo lo que recibe (uno por solución) y cómo se mide el resultado."""
    T, M = R.T, R.M
    en = d["entregables"]
    titulo = en.get("titulo") or "Todo lo que {cliente_corto} recibe."
    sub = en.get("subtitulo") or sub_entregables_defecto(d)
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
            style = ' style="min-height:2.4em"' if (j == 0 and min_first.get(i)) else ""
            li = "".join("              <li>%s</li>\n" % T(s["entregable"], "areas.soluciones.entregable") for s in a["soluciones"])
            areas_html += (
                '          <div class="da">\n'
                '            <p class="da-name"%s>%s</p>\n'
                "            <ul>\n%s            </ul>\n"
                "          </div>\n" % (style, T(nombre_catalogo(a), "areas.nombre"), li)
            )
        cols_html += '        <div class="deliv-col %s">\n%s        </div>\n\n' % (COLORES[col["carril"]["color"]], areas_html)
    return (
        '    <!-- 5 · Entregables: ¿con qué me quedo? (catálogo + piezas transversales) -->\n'
        '    <section class="slide s-deliv%s%s">\n'
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
        % (" compact" if compacto else "", " roomy" if getattr(R, "deliv_roomy", False) else "", R.contador("entregables"), R.idx["entregables"], T(titulo, "entregables.titulo"), sub_html,
           ncols, barras, ncols, cols_html, T(en.get("etiqueta_transversales") or "Para todas las áreas", "entregables.etiqueta_transversales"),
           T(en.get("etiqueta_valor") or "Valor inmediato", "entregables.etiqueta_valor"), foot(R, "oscuro"))
    )

def geometria_pago(n):
    """Posición de las tarjetas de cuota (px de la slide). DEBE coincidir con scripts/agregar-campo-precio.py → plan_pago_fields()."""
    gap = 14.0
    w = (1011.0 - gap * (n - 1)) / n
    return [(56.0 + i * (w + gap), w) for i in range(n)]

def s_pago(d, R):
    """8 · Facilidad de pago (penúltima): cuotas ligadas a hitos. Los montos son campos vacíos y editables (PagoCuota1..N)."""
    T, M = R.T, R.M
    pg = d.get("pago") or {}
    cuotas = cuotas_pago(d)
    n = len(cuotas)
    titulo = pg.get("titulo") or "Facilidad de pago: {n_cuotas} cuotas ligadas a hitos."
    sub = pg.get("subtitulo") or "Cada cuota se paga al cumplirse un hito del proyecto, y las {n_cuotas_palabra} suman el **100%** de la inversión."
    colores = ["acc-y", "acc-o", "acc-y", "acc-o", "acc-w", "acc-y"]
    fs_cuando = {2: 28, 3: 26, 4: 24, 5: 24, 6: 20}.get(n, 24)
    cards = frames = ""
    for i, (c, (left, w)) in enumerate(zip(cuotas, geometria_pago(n)), 1):
        pct = fmt_es(c["pct"]) + "%"
        cards += (
            '        <div class="pay-step %s%s" style="left:%.2fpx; width:%.2fpx">\n'
            '          <span class="ps-d"></span>\n'
            '          <span class="ps-tag">Cuota %d</span>\n'
            '          <b class="ps-when" style="font-size:%dpx">%s</b>\n'
            '          <p class="ps-hito">%s</p>\n'
            '          <span class="ps-pct">%s</span>\n'
            '          <span class="ps-lbl">Monto</span>\n'
            "        </div>\n" % (colores[(i - 1) % len(colores)], " first" if i == 1 else "", left, w, i, fs_cuando,
                                 T(c["cuando"], "pago.cuotas.cuando"), T(c["hito"], "pago.cuotas.hito"), pct)
        )
        frames += '      <div class="pay-frame" style="left:%.2fpx; width:%.2fpx"></div>\n' % (left + 16, w - 32)
    nota = ""
    if pg.get("mensaje") or pg.get("facturacion"):
        nota = (
            '      <div class="pay-note">\n'
            + ('        <p class="pn-main">%s</p>\n' % M(pg["mensaje"], "pago.mensaje") if pg.get("mensaje") else "")
            + ('        <p class="pn-sub">%s</p>\n' % M(pg["facturacion"], "pago.facturacion") if pg.get("facturacion") else "")
            + "      </div>\n\n"
        )
    return (
        '    <!-- 8 · Facilidad de pago: cuotas ligadas a hitos (penúltima slide). Montos vacíos y editables (AcroForm PagoCuota1..N). -->\n'
        '    <section class="slide s-pay">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Pago</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="pay-line"></div>\n'
        '      <div class="pay-route">\n%s      </div>\n%s\n%s%s'
        "    </section>\n"
        % (R.contador("pago"), R.idx["pago"], T(titulo, "pago.titulo"), M(sub, "pago.subtitulo"), cards, frames, nota, foot(R, "oscuro"))
    )

def s_proximos(d, R):
    """9 · Próximos pasos (última): llamado a la acción y a quién escribir (la asesora comercial)."""
    T, M = R.T, R.M
    pp = d["proximos_pasos"]
    titulo = pp.get("titulo") or "Tres pasos para arrancar."
    sub = pp.get("subtitulo") or "Esto es lo que sigue cuando {cliente_corto} confirme la propuesta."
    pasos = pp.get("pasos") or PASOS_PROXIMOS
    colores = ["acc-y", "acc-o", "acc-w"]
    cards = "".join(
        '        <div class="nx-step %s">\n'
        '          <span class="nx-num">%d</span>\n'
        "          <b>%s</b>\n"
        "          <p>%s</p>\n"
        "        </div>\n" % (colores[i % 3], i + 1, T(x["titulo"], "proximos_pasos.pasos.titulo"), M(x["texto"], "proximos_pasos.pasos"))
        for i, x in enumerate(pasos)
    )
    a = pp["asesora"]
    lineas = ""
    if a.get("cargo"):
        lineas += '          <span class="nx-role">%s</span>\n' % T(a["cargo"], "proximos_pasos.asesora.cargo")
    if a.get("correo"):
        lineas += '          <p class="nx-line"><a href="mailto:%s">%s</a></p>\n' % (esc(a["correo"]), T(a["correo"], "proximos_pasos.asesora.correo"))
    if a.get("telefono"):
        lineas += '          <p class="nx-line">%s</p>\n' % T(a["telefono"], "proximos_pasos.asesora.telefono")
    return (
        '    <!-- 9 · Próximos pasos: qué hacer y a quién escribir (última slide) -->\n'
        '    <section class="slide s-next">\n'
        '      <span class="counter">%s</span>\n'
        '      <p class="eyebrow">%02d · Próximos pasos</p>\n'
        "      <h2>%s</h2>\n"
        '      <p class="sub">%s</p>\n\n'
        '      <div class="nx-steps">\n%s      </div>\n\n'
        '      <div class="nx-contact">\n'
        '        <div class="nx-card nx-ase">\n'
        '          <span class="nx-label">%s</span>\n'
        '          <b class="nx-name">%s</b>\n%s'
        "        </div>\n"
        '        <div class="nx-card nx-emp">\n'
        '          <span class="nx-label">Intezia</span>\n'
        '          <p class="nx-line">Intezia C.A J-505657950</p>\n'
        '          <p class="nx-line"><a href="mailto:servicio@intezia.com">servicio@intezia.com</a></p>\n'
        "        </div>\n"
        "      </div>\n\n%s"
        "    </section>\n"
        % (R.contador("proximos"), R.idx["proximos"], T(titulo, "proximos_pasos.titulo"), M(sub, "proximos_pasos.subtitulo"), cards,
           T(pp.get("etiqueta_contacto") or "¿Dudas? Escribe a tu asesora comercial", "proximos_pasos.etiqueta_contacto"),
           T(a["nombre"], "proximos_pasos.asesora.nombre"), lineas, foot(R, "oscuro"))
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
    seg = seg_es_seguimiento(d)
    gar = con_garantia(d)
    if r.get("metas"):
        metas = [(x.get("dias") or "", x.get("texto") or "") for x in r["metas"] if isinstance(x, dict)]
    elif seg:
        metas = list(METAS_BASE) + [("90 días", META90[(fund, pos)])]
    else:
        metas = []   # sin seguimiento 30-60-90 el calendario no aplica: validar_retorno exige retorno.metas propios
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
    if seg:
        gancho_def = "Hacia la semana {semana_medicion} ({semanas_txt} de construcción más 90 días de seguimiento), {cliente_corto} contará con " + resto
    else:
        gancho_def = "Al cierre de las {semanas_txt} de trabajo, {cliente_corto} contará con la línea base y el método para medir " + resto.replace("el tiempo recuperado medido", "el tiempo recuperado", 1)
    return {
        "modo": modo, "pos": pos, "fund": fund, "pasos": pasos, "metas": metas, "destino": destino, "destino_def": destino_def,
        "pasos_def": not r.get("pasos"),
        "titulo": r.get("titulo") or titulo,
        "subtitulo": r.get("subtitulo") or (
            "Cifras de {cliente_corto} por área, a confirmar con la línea base de la semana 1 y medidas a 30, 60 y 90 días."
            if modo == "cifras" else
            ("Se calcula con los datos de cada área, se confirma con la línea base de la semana 1 y se mide a 30, 60 y 90 días." if seg else
             "Se calcula con los datos de cada área y se confirma con la línea base de la semana 1.")),
        "etiqueta_pasos": r.get("etiqueta_pasos") or "Cómo se calcula, por área y por proceso",
        "etiqueta_metas": r.get("etiqueta_metas") or (
            "Calendario de garantía y cálculo del retorno" if gar else ("Calendario de seguimiento y cálculo del retorno" if seg else "Qué queda al cerrar")),
        "sub_metas": "" if (r.get("etiqueta_metas") or not seg) else "Desde el cierre de cada área",
        "etiqueta_destino": r.get("etiqueta_destino") or "Hacia dónde va el proyecto",
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
        partes.append("Incluye retrabajo y pagos o cobros tardíos en %d %s." % (n_ext, plural(n_ext, *VOC["area"])))
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
    """Holgura estimada (px) entre el último bloque y la banda final de la slide de retorno. Calibrado con DUSA v2 y el ejemplo de
    Fundación, 2026-10-07 (medidas: DUSA 6 pasos, panel 333,5 px, destino 124,4 px, holgura 30,4 px; Fundación 5 pasos, holgura 59,1 px)
    y con tablas de 3 a 11 filas (2026-10-05)."""
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
        panel = 44 + sum(27.6 + lineas_wrap(tk(x), 100) * 15.64 for _t, x in c["pasos"])
    cpl_meta = 45 if c["modo"] == "cifras" else 53
    metas = 50 + sum(max(78, 47 + lineas_wrap(tk(x), cpl_meta) * 16.6) for _t, x in c["metas"]) + 10 * len(c["metas"])
    cuerpo = max(panel, metas)
    dest = 0
    if c["modo"] != "cifras":
        dest = 18 + 20 + 4 + 8 + 9 + 15.2 + 3 + max(lineas_wrap(tk(x), 58) for _r, x in c["destino"]) * 15.64
    gancho_h = 28 + lineas_wrap(tk(c["gancho"]), 108) * 23.75
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
    if not seg_es_seguimiento(d) and not r.get("metas"):
        rep.err("retorno.metas", "con seguimiento.tipo = «%s» el calendario 30-60-90 no aplica: definir retorno.metas (3 hitos de lo que queda definido al cerrar, con su etiqueta en retorno.etiqueta_metas) o activar el seguimiento" % seg_tipo(d))
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


def s_retorno(d, R):
    """6 · Retorno: ¿qué gano con esto? (obligatoria: método de cálculo o cifras del propio cliente; sin estudios ni citas de la web)."""
    c = cfg_retorno(d)
    T, M = R.T, R.M
    modo = c["modo"]
    if modo == "cifras":
        filas, tot = filas_cifras(d)
        pos = c["pos"]
        cab = ["Área", "Horas actuales al mes", "Horas con la solución (meta)", "Horas recuperadas al mes", "Valor del tiempo (USD/mes)"]
        if pos:
            cab += ["Posiciones hoy", "A reducir o evitar", "Valor anual (USD)"]
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
        '    <!-- %d · Retorno: ¿qué gano? (%s). Sin estudios ni citas externas. -->\n'
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
        % (R.idx["retorno"], "método de cálculo" if modo == "metodo" else "cifras por área", " roi-cifras" if modo == "cifras" else "", R.contador("retorno"), R.idx["retorno"],
           T(c["titulo"], "retorno.titulo"), M(c["subtitulo"], "retorno.subtitulo"), izq,
           T(c["etiqueta_metas"], "retorno.etiqueta_metas") + (("<small>%s</small>" % T(c["sub_metas"], "retorno.sub_metas")) if c.get("sub_metas") else ""),
           metas, dest, T(c["gancho"], "retorno.gancho"), foot(R, "claro"))
    )


def render_html(d, R, columnas, ncols):
    total = R.total
    cab = (
        "<!doctype html>\n<!--\n"
        "  Propuesta · %s · %s (%s)\n"
        "  División: %s · Servicio: %s (§4.1a) · Alianza: %s\n"
        "  GENERADO por scripts/generar-habilidades-compacto.py (plantilla %s) desde datos.json.\n"
        "  No editar a mano: editar datos.json y regenerar. Estilos propios del deck: overrides.css.\n"
        "  Fuente del insumo: %s\n\n"
        "  Formato compacto de %d slides, en el orden de las preguntas del cliente (Ventas, 2026-10-07):\n"
        "    %s\n"
        "  Marcadores de detección de AcroForms (agregar-campo-precio.py), por página: «Propuesta Económica» solo en la slide de\n"
        "  inversión; «Lo que se llevan» y «Entregables» solo en la de entregables; «Facilidad de pago» solo en la de pago.\n"
        "  Campos AcroForm: %s. Se reposicionan con scripts/customize-habilidades-compacto.py.\n"
        "-->\n"
        % (cm(d["cliente"]["nombre"]), cm(rotulo_servicio(d)), cm(d["cliente"]["codigo"]), R.div_nombre,
           cm(re.sub(r"^Servicio de ", "", rotulo_servicio(d))), "sí" if d.get("alianza") else "no", VERSION_PLANTILLA,
           cm(d.get("fuente_insumo") or "(no indicado)"), total,
           " · ".join("%d %s" % (R.idx[k], NOMBRES_SLIDE[k]) for k in R.orden),
           ("%s%s y Entregables, Acreditacion (entregables)" % (
               "Programa, Notas, PrecioBase, Descuento, PrecioTotal (inversión)" if "inversion" in R.orden else "sin hoja de inversión",
               (", PagoCuota1..%d (pago)" % len(cuotas_pago(d))) if "pago" in R.orden else ""))
           if "inversion" in R.orden else "Entregables, Acreditacion (entregables); sin hoja de inversión ni de pago (%s)" % (
               "Fundación" if d.get("division") == "fundacion" else "sin_hoja_cotizacion / omitir"))
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
    fns = {
        "portada": lambda: s_portada(d, R), "alcance": lambda: s_alcance(d, R), "ruta": lambda: s_ruta(d, R),
        "metodo": lambda: s_metodo(d, R), "entregables": lambda: s_entregables(d, R, columnas, ncols), "retorno": lambda: s_retorno(d, R),
        "inversion": lambda: s_inversion(d, R), "pago": lambda: s_pago(d, R), "proximos": lambda: s_proximos(d, R),
    }
    cuerpo = "\n".join(fns[k]() for k in R.orden)
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
        notas = inv.get("notas") or (
            (["Garantía 30-60-90: seguimiento a {rango_seguimiento} desde el cierre de cada área, con las soluciones en uso."] if con_garantia(d) else [])
            + ["Términos y condiciones: los del enlace de «Importante», que ambas partes aceptan al avanzar con esta propuesta."])
        out["Notas"] = [sin_marcado(t(x, "inversion.notas")) for x in notas]
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
    L.append("# Programa interno · %s · %s (%s)\n" % (d["cliente"]["nombre"], rotulo_servicio(d), d["cliente"]["codigo"]))
    L.append("> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.")
    if d.get("fuente_insumo"):
        L.append("> Fuente del insumo: %s." % d["fuente_insumo"])
    L.append("")
    L.append("## 1. Resumen\n")
    L.append("- **%s en %s%s**, **%d h** de sesión%s." % (
        R.ctx["n_total_txt"], R.ctx["n_areas_txt"], (" (más %d %s)" % (R.agg["n_bases"], plural(R.agg["n_bases"], *VOC["proceso_base"]))) if R.agg["n_bases"] else "",
        R.agg["h_total"], (", más seguimiento a %s" % d["seguimiento"]["rango"]) if seg_es_seguimiento(d) else ""))
    for c in d["carriles"]:
        ca = R.agg["carril"].get(c["id"])
        if ca:
            L.append("- Herramienta **%s**: %d %s, %d h." % (c["nombre"], ca["n"], plural(ca["n"], *VOC["solucion"]), ca["h"]))
    L.append("- Horas por fase: " + " · ".join("%s %d h (%d sol.)" % (f["id"], R.agg["fase"].get(f["id"], [0, 0])[1], R.agg["fase"].get(f["id"], [0, 0])[0]) for f in d["fases"]) + ".")
    L.append("")
    L.append("## 2. Líneas de trabajo y ruta\n")
    L.append("| Línea de trabajo | Herramienta | Áreas | Semanas | Horas | Soluciones |\n|---|---|---|---|---|---|")
    carr = dict((c["id"], c) for c in d["carriles"])
    for fr in d["frentes"]:
        n, h = R.agg["frente"].get(fr["id"], [0, 0])
        nombres = ", ".join(a["nombre"] for a in d["areas"] if a["frente"] == fr["id"])
        L.append("| %s | %s | %s | %s | %d | %d |" % (cel(fr["nombre"]), cel(carr[fr["carril"]]["nombre"]), cel(nombres), cel(fr["semanas"]), h, n))
    L.append("")
    fcols = [f for f in d["fases"] if f.get("id") != "F0"]
    L.append("| Línea de trabajo | " + " | ".join(cel("%s (%s)" % (f["titulo"], f["rango"])) for f in fcols) + " |")
    L.append("|---|" + "---|" * len(fcols))
    for fr in d["frentes"]:
        celdas = []
        for f in fcols:
            n, h = R.agg["celda"].get((fr["id"], f["id"]), [0, 0])
            celdas.append("%d h · %d sol." % (h, n))
        L.append("| %s | %s |" % (cel(fr["nombre"]), " | ".join(celdas)))
    L.append("")
    for h in d["ruta"]["hitos"]:
        L.append("- **%s**: %s" % (sin_marcado(t(h["titulo"], "ruta.hitos")), sin_marcado(t(h["texto"], "ruta.hitos"))))
    L.append("")
    L.append("## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)\n")
    for a in d["areas"]:
        n, h = R.agg["area"][a["id"]]
        L.append("### %s · %d %s · %d h · %s · línea %s%s\n" % (
            cel(a["nombre"]), n, plural(n, *VOC["solucion"]), h, carr[a["carril"]]["nombre"], a["frente"], (" · " + VOC["proceso_base"][0]) if a.get("proceso_base") else ""))
        L.append("Para qué (lo que ve el cliente): %s\n" % sin_marcado(t(a.get("para_que") or "", "areas.para_que")))
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
        L.append("## 5. Supuestos a confirmar (antes del método)\n")
        for x in d["supuestos"]:
            L.append("- " + x)
        L.append("")
    if "metodo" in R.orden:
        mt = d.get("metodo") or {}
        L.append("## 6. Cómo trabajamos (slide %d)\n" % R.idx["metodo"])
        L.append("**Por qué en este orden:** %s\n" % sin_marcado(t(mt.get("por_que_orden") or por_que_defecto(d), "metodo.por_que_orden")))
        for x in (mt.get("pasos") or PASOS_METODO):
            L.append("- **%s**: %s" % (sin_marcado(t(x["titulo"], "metodo.pasos")), sin_marcado(t(x["texto"], "metodo.pasos"))))
        L.append("")
        for x in mt.get("practica") or []:
            L.append("- En la práctica, **%s**: %s" % (sin_marcado(t(x["titulo"], "metodo.practica")), sin_marcado(t(x["texto"], "metodo.practica"))))
        L.append("- Datos: %s" % sin_marcado(t(mt.get("datos") or "", "metodo.datos")))
        if mt.get("quien_construye"):
            L.append("- Quién construye: %s" % sin_marcado(t(mt["quien_construye"], "metodo.quien_construye")))
        L.append("")
        if mt.get("ejemplos"):
            L.append("Casos reales mostrados (cada uno con su fuente; nunca se inventan casos de éxito):\n")
            for x in mt["ejemplos"]:
                L.append("- **%s** · %s%s. Fuente: %s." % (sin_marcado(t(x["area"], "metodo.ejemplos")), sin_marcado(t(x["titulo"], "metodo.ejemplos")),
                                                           (" (antes: %s; después: %s)" % (x["antes"], x["despues"])) if x.get("antes") else "", sin_marcado(t(x["fuente"], "metodo.ejemplos"))))
            L.append("")
        lg = d.get("logistica") or {}
        L.append("**Logística:** modalidad: %s · participantes: %s · arranque: %s." % (sin_marcado(t(lg.get("modalidad") or "", "logistica")), sin_marcado(t(lg.get("participantes") or "", "logistica")), sin_marcado(t(lg.get("arranque") or "", "logistica"))))
        L.append("")
    c6 = cfg_retorno(d) if "retorno" in R.orden else None
    if c6:
        r6 = d["retorno"]
        L.append("## 7. Retorno esperado (slide %d)\n" % R.idx["retorno"])
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
    if "pago" in R.orden:
        L.append("## 8. Facilidad de pago (slide %d)\n" % R.idx["pago"])
        L.append("| Cuota | Cuándo | Hito | %% |\n|---|---|---|---|")
        for i, c in enumerate(cuotas_pago(d), 1):
            L.append("| %d | %s | %s | %s |" % (i, cel(c["cuando"]), cel(c["hito"]), fmt_es(c["pct"])))
        L.append("")
        L.append("Los montos van vacíos en el PDF (campos `PagoCuota1..%d`): los escribe ventas y deben sumar el total de la slide de inversión. No se anotan en este repositorio." % len(cuotas_pago(d)))
        if not (d.get("pago") or {}).get("cuotas"):
            L.append("Plan estándar de `empresa/politicas-comerciales.md` (anticipo 50 %, saldo 50 % al cierre): confirmar con ventas si hay una facilidad distinta.")
        L.append("")
    if "proximos" in R.orden:
        a_ = (d.get("proximos_pasos") or {}).get("asesora") or {}
        L.append("## 9. Próximos pasos (slide %d)\n" % R.idx["proximos"])
        L.append("Asesora comercial que ve el cliente: %s%s · %s%s." % (a_.get("nombre", ""), (", " + a_["cargo"]) if a_.get("cargo") else "", a_.get("correo", ""), (" · " + a_["telefono"]) if a_.get("telefono") else ""))
        L.append("")
    return "\n".join(L) + "\n"


def tipo_meta_defecto(d, R):
    base = "Capacitación In-Company · %s · %s en %s · %d h de sesión · %s semanas" % (
        rotulo_servicio(d), R.ctx["n_total_txt"], R.ctx["n_areas_txt"], R.agg["h_total"], d["ruta"]["semanas_total"])
    if seg_es_seguimiento(d):
        return base + " + seguimiento %s" % d["seguimiento"].get("rango", "")
    return base + ", sin seguimiento"


def datos_meta(d, R):
    return {
        "codigo": d["cliente"]["codigo"],
        "cliente": d["cliente"]["nombre"],
        "tipo": d.get("meta_tipo") or tipo_meta_defecto(d, R),
        "eje": sin_marcado(R.t(d.get("eje") or "", "eje")),
        "servicio": d.get("meta_servicio") or "habilidades",
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


def version_css(texto):
    """Versión de la plantilla que declara el CSS en su primer comentario («CSS genérico (v2.0, …)»)."""
    m = re.search(r"CSS gen[eé]rico \(v(\d+(?:\.\d+)*)", texto[:800])
    return m.group(1) if m else None


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
    ms = (d.get("meta_servicio") or "habilidades").strip()
    pp = d.get("proximos_pasos") or {}
    ase = pp.get("asesora") or {}
    asesora = (("%s%s" % (ase.get("nombre", ""), (", " + ase["cargo"]) if ase.get("cargo") else "")
                + "".join(" · " + ase[k] for k in ("correo", "telefono") if ase.get(k))) if "proximos" in R.orden
               else "(esta propuesta omite la slide de próximos pasos)")
    if "retorno" not in R.orden:
        regla_retorno = "Sin slide de retorno (`omitir`): confirmar con ventas que aquí no aplica (charla, sesión única); si el cliente es directivo, el retorno estimado es lo que decide."
    elif ms == "habilidades":
        regla_retorno = ("Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; "
                         "en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. "
                         "Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).")
    else:
        regla_retorno = ("Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad "
                         "y qué decide el cliente con el Reporte Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).")
    if "inversion" in R.orden:
        nota_precio = "Montos de inversión, descuento, total%s: vacíos, los llena ventas." % (" y cuotas" if "pago" in R.orden else "")
        precio = "con hoja de inversión%s (campos de monto vacíos para ventas)" % (" y de pago" if "pago" in R.orden else "")
    else:
        por = "Fundación" if d.get("division") == "fundacion" else "sin_hoja_cotizacion / omitir"
        nota_precio = "Sin hoja de inversión ni de pago (%s): el deck no lleva montos ni campos de cotización." % por
        precio = "sin hoja de inversión ni de pago (%s)" % por
    tipo_doc = (("categoría de catálogo Capacitación In-Company (`%s`), presentada al cliente como **propuesta de proyecto**" % d["cliente"]["codigo"]) if ms == "habilidades"
                else "%s (`%s`)" % (d.get("meta_tipo") or rotulo_servicio(d), d["cliente"]["codigo"]))
    sem = d["ruta"]["semanas_total"]
    sub = {
        "CLIENTE": d["cliente"]["nombre"], "CODIGO": d["cliente"]["codigo"], "SLUG": d["cliente"]["slug"],
        "SERVICIO_ROTULO": rotulo_servicio(d), "SERVICIO": ms, "TIPO_DOC": tipo_doc,
        "DIVISION": d["division"], "ALIANZA": "sí" if d.get("alianza") else "no", "EJE": sin_marcado(R.t(d.get("eje") or "", "eje")),
        "ORIGEN": d.get("origen") or "", "FUENTE_INSUMO": d.get("fuente_insumo") or "",
        "N_TOTAL": str(R.agg["n_total"]), "N_AREAS": str(R.agg["n_areas"]), "H_TOTAL": str(R.agg["h_total"]),
        "N_TOTAL_TXT": R.ctx["n_total_txt"], "N_AREAS_TXT": R.ctx["n_areas_txt"],
        "SEMANAS_TXT": "%s %s" % (sem, plural(sem, "semana", "semanas")),
        "SEGUIMIENTO_TXT": (" · seguimiento a %s" % d["seguimiento"]["rango"]) if seg_es_seguimiento(d) else " · sin seguimiento",
        "ORDEN": " · ".join("%d %s" % (R.idx[k], NOMBRES_SLIDE[k]) for k in R.orden),
        "REGLA_RETORNO": regla_retorno, "NOTA_PRECIO": nota_precio, "PRECIO": precio,
        "SUPUESTOS": sup, "PENDIENTES": pen, "SLIDES": str(R.total), "ASESORA": asesora,
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
def chequear_repeticion(textos, rep, minimo=9):
    """Avisa cuando dos slides repiten la misma frase (Ventas, 2026-10-07: «cada página tiene que aportar algo nuevo»)."""
    pal = {}
    for cls, txt in textos:
        pal[cls] = re.findall(r"[\wáéíóúñü%$]+", txt.lower())
    claves = [c for c, _ in textos]
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            a_, b_ = pal[claves[i]], pal[claves[j]]
            m = difflib.SequenceMatcher(None, a_, b_, autojunk=False).find_longest_match(0, len(a_), 0, len(b_))
            if m.size >= minimo:
                rep.aviso("slides %s y %s" % (claves[i], claves[j]), "repiten %d palabras seguidas: «%s». Si algo ya se dijo no se repite; cada página aporta algo nuevo" % (m.size, " ".join(a_[m.a:m.a + min(m.size, 14)])))


def chequeos_html(html, d, rep):
    secciones = re.findall(r'<section class="slide ([^"]*)">(.*?)</section>', html, re.S)
    textos = []
    textos_rep = []
    textos_fecha = {}
    frases_ok = sorted((x for x in (d.get("frases_ok") or []) if isinstance(x, str) and x.strip()), key=len, reverse=True)
    for cls, cuerpo in secciones:
        cf = re.sub(r'<p class="(?:pain-src|lic-note)">.*?</p>', " ", cuerpo, flags=re.S)
        cf = re.sub(r'<span class="mp-src">.*?</span>', " ", cf, flags=re.S)
        cf = re.sub(r"<!--.*?-->", "", cf, flags=re.S)
        cf = re.sub(r"<[^>]+>", " ", cf)
        textos_fecha[cls.split()[0]] = _html.unescape(re.sub(r"\s+", " ", cf)).strip()
        t = re.sub(r"<!--.*?-->", "", cuerpo, flags=re.S)
        t = re.sub(r'<span class="cot-sign-minus">.*?</span>', " ", t)  # «−$» de la hoja de cotización no es un guion
        textos_rep.append((cls.split()[0], _html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r'<p class="mt-why auto">.*?</p>', " ", t, flags=re.S)))).strip()))
        t = re.sub(r"<[^>]+>", " ", t)
        textos.append((cls.split()[0], _html.unescape(re.sub(r"\s+", " ", t)).strip()))
    for cls, txt in textos:
        low = txt.lower()
        if MARCA_PRECIO in low and cls != "s-price":
            rep.err("slide " + cls, "contiene «Propuesta Económica» fuera de la slide de inversión (rompe la detección de AcroForms)")
        if MARCA_PAGO in low and cls != "s-pay":
            rep.err("slide " + cls, "contiene «Facilidad de pago» fuera de la slide de pago (rompe la detección de los campos PagoCuota)")
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
        txt_j = txt
        for fr_ok in frases_ok:  # nombres de soluciones o procesos del cliente que llevan «costo» o «precio» (p. ej. «tablas de precios»)
            txt_j = re.sub(re.escape(fr_ok), " ", txt_j, flags=re.I)
        for rx, sugerencia in JERGA_ERR:
            mj = rx.search(txt_j)
            if mj:
                rep.err("slide " + cls, "«%s» cerca de «%s»: %s (Ventas, 2026-10-07: hablar en el idioma del cliente; si es el nombre de una solución del cliente, agregarlo a frases_ok)" % (mj.group(0), txt_j[max(0, mj.start() - 25):mj.end() + 25], sugerencia))
        for rx, sugerencia in JERGA_AVISO:
            mj = rx.search(txt_j)
            if mj:
                rep.aviso("slide " + cls, "«%s» cerca de «%s»: %s; si es el nombre de una solución del cliente, agregarlo a frases_ok" % (mj.group(0), txt_j[max(0, mj.start() - 25):mj.end() + 25], sugerencia))
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
        if not anuncia_duracion(d):
            _ts = textos_fecha.get(cls, txt)
            _ms = RE_SESIONES.search(_ts)
            if _ms:
                rep.aviso("slide " + cls, "anunciar_duracion = false pero el texto cuenta sesiones «%s» cerca de «%s»: reescribir sin el conteo o confirmar que es intencional" % (_ms.group(0), _ts[max(0, _ms.start() - 25):_ms.end() + 25]))
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
    if "s-pay" in tds and MARCA_PAGO not in tds["s-pay"].lower():
        rep.err("slide s-pay", "falta «Facilidad de pago» en el título (marcador de los campos PagoCuota)")
    if "s-price" in tds and "s-pay" not in tds and "pago" in orden_slides(d):
        rep.err("slide s-pay", "falta la slide de pago: la inversión debe ser la antepenúltima y la siguiente ayuda a decidir (Ventas, 2026-10-07)")
    chequear_repeticion(textos_rep, rep)
    for cls, cuerpo in secciones:
        n = len(re.findall(r"<strong>", cuerpo))
        if n > 3:
            rep.aviso("slide " + cls, "%d resaltados <strong>: la regla §4.8 pide ~2-3 por slide" % n)
    permitidas = SIGLAS_OK | set(d.get("siglas_ok") or []) | set(re.findall(r"[A-Z]{2,}", d["cliente"].get("nombre", "")))
    for cls, txt in textos:
        sin_codigos = re.sub(r"\b[A-Z]{2,4}-\d+\b", " ", txt)
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
            agg["n_total"], plural(agg["n_total"], *VOC["solucion"]), agg["n_areas"], plural(agg["n_areas"], *VOC["area"]), agg["h_total"],
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
    if d.get("version") != VERSION_DATOS:
        sys.exit("ERROR: este datos.json declara version %r y el generador v2 (plantilla %s) pide \"version\": %d. "
                 "Es de la plantilla 1.x: migrarlo con plantillas/habilidades-compacto.md → «Migración desde la v1» "
                 "(nuevos campos obligatorios: areas[].para_que, frentes[].nombre, metodo, logistica, proximos_pasos.asesora; "
                 "alcance.pasos y alcance.quien_construye pasaron a metodo)." % (d.get("version"), VERSION_PLANTILLA, VERSION_DATOS))
    for viejo in ("pasos", "quien_construye", "etiqueta_pasos", "etiqueta_quien"):
        if viejo in (d.get("alcance") or {}):
            rep.aviso("alcance.%s" % viejo, "esta clave pasó a la sección «metodo» (slide «Cómo trabajamos»): se ignora aquí")
    orden = orden_slides(d)
    if "retorno" in orden and not isinstance(d.get("retorno"), dict):
        d["retorno"] = {}   # la slide de retorno responde «¿qué gano?» y va en toda propuesta salvo omitir: por defecto, modo método
    for k in sorted(set(claves_dup)):
        rep.err("datos.json", "la clave «%s» aparece repetida en el mismo objeto (JSON se queda con la última y pierde la anterior): borrar el duplicado" % k)
    # 1) Estructura: pendientes, tipos y secciones obligatorias (siempre abortan)
    claves_de = {"inversion": ("inversion",), "pago": ("pago",), "metodo": ("metodo", "logistica"), "retorno": ("retorno",), "proximos": ("proximos_pasos",)}
    saltar = tuple(c for k, cs in claves_de.items() if k not in orden for c in cs)   # las secciones de slides omitidas no se revisan
    pend = []
    buscar_pendientes(d, "", pend, saltar)
    for ruta_ph, msg in pend:
        rep.err(ruta_ph, msg)
    chequear_tipos(dict((k, v) for k, v in d.items() if k not in saltar), "raiz", "", rep)
    for k in ("cliente", "portada", "carriles", "areas", "fases", "frentes", "ruta", "seguimiento", "alcance", "entregables") + tuple(
            c for k2 in ("metodo", "proximos") if k2 in orden for c in claves_de[k2]):
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

    ESTADO["etq_base"] = sin_marcado(Tokens(ctx, Reporte())(d["alcance"].get("etiqueta_proceso_base") or VOC["proceso_base"][0], "alcance.etiqueta_proceso_base"))
    R = Ctx()
    R.ctx, R.agg = ctx, agg
    R.t = Tokens(ctx, rep)
    R.T = lambda x, donde: esc(sin_marcado(R.t(x, donde)))
    R.M = lambda x, donde: md(R.t(x, donde))
    div_nombre, div_dir = DIVISIONES.get(d.get("division"), ("Educación", "educacion"))
    R.div_nombre = div_nombre
    R.orden = orden
    R.con_precio = "inversion" in R.orden
    R.idx = dict((k, i + 1) for i, k in enumerate(R.orden))
    R.total = len(R.orden)
    R.contador = lambda k: "%02d / %02d" % (R.idx[k], R.total)
    R.codigo = d["cliente"].get("codigo", "")
    R.pie = d["cliente"].get("nombre_pie") or d["cliente"].get("nombre", "")
    R.rel_base = os.path.relpath(str(PROPUESTAS / "_base" / "styles.css"), str(out))
    R.rel_logos = os.path.relpath(str(ROOT / "logos" / div_dir), str(out))

    columnas, ncols, alto_max = repartir_columnas(d, rep)
    html = af = None
    R.deliv_roomy = False
    if columnas:
        cupo = cupo_catalogo(d, R)
        compacto = bool(d["entregables"].get("compacto"))
        R.deliv_roomy = (not compacto) and alto_max < cupo * 0.55  # pocas áreas: letra más grande para que la slide no quede vacía
        if alto_max > cupo * 1.15:
            detalle = "; ".join(
                "columna %d (%s): ~%d px" % (i + 1, "+".join(a["id"] for a in c["areas"]),
                                             sum(alto_area(a, ncols, compacto) for a in c["areas"]) + 14 * (len(c["areas"]) - 1))
                for i, c in enumerate(columnas))
            rep.err("entregables", "el catálogo estimado mide ~%d px en su columna más alta y el cupo es ~%d px (%s). Opciones: acortar los nombres más largos a ≤ 36 caracteres (1 línea), entregables.compacto=true, un título/subtítulo más cortos, o entregables.columnas_por_carril" % (alto_max, cupo, detalle))
        elif alto_max > cupo - 8:
            rep.aviso("entregables", "el catálogo estimado mide ~%d px en su columna más alta (cupo ~%d px): puede no caber; medir con verificar-habilidades-compacto.js (el estimador varía ±10 %%)" % (alto_max, cupo))
    if not alcance_roomy(d):
        holg2 = estimar_alcance(d, R)
        if os.environ.get("HAB_DEBUG"):
            print("[estimador] alcance: holgura %.1f px" % holg2)
        if holg2 < -10:
            rep.err("alcance", "la slide de alcance estimada excede la página en ~%d px: usar alcance.compacto, acortar para_que o fuera_alcance, o repartir áreas" % -holg2)
        elif holg2 < 8:
            rep.aviso("alcance", "holgura estimada contra el pie de ~%d px (mín. 8): puede no caber; medir con verificar-habilidades-compacto.js" % holg2)
    if "metodo" in R.orden and not metodo_roomy(d):
        holg4 = estimar_metodo(d, R)
        if os.environ.get("HAB_DEBUG"):
            print("[estimador] metodo: holgura %.1f px" % holg4)
        if holg4 < -10:
            rep.err("metodo", "la slide «Cómo trabajamos» estimada excede la página en ~%d px: acortar pasos, prácticas, datos, casos ya logrados o la logística" % -holg4)
        elif holg4 < 6:
            rep.aviso("metodo", "holgura estimada contra el pie de ~%d px (mín. 8): puede no caber; medir con verificar-habilidades-compacto.js" % holg4)
    if "retorno" in R.orden and (d["retorno"].get("modo") or "metodo") in ("metodo", "cifras"):
        holg6 = estimar_s6(d, R)
        if os.environ.get("HAB_DEBUG"):
            print("[estimador] retorno: holgura %.1f px" % holg6)
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
    sub5 = sin_marcado(R.t(d["entregables"].get("subtitulo") or sub_entregables_defecto(d), "entregables.subtitulo"))
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
    css_dst = out / CSS_NAME
    css_tpl = (PLANTILLA / CSS_NAME).read_text(encoding="utf8")
    if css_dst.exists() and not args.actualizar_css:
        v_deck, v_tpl = version_css(css_dst.read_text(encoding="utf8")), version_css(css_tpl)
        if v_deck != v_tpl:
            sys.exit("ERROR: el CSS congelado de esta propuesta es de la plantilla v%s y la actual es la v%s: el HTML nuevo no se ve igual con el CSS viejo. "
                     "Regenerar con --actualizar-css y revisar el overrides.css del deck (las clases de la ruta y del alcance cambiaron; plantillas/habilidades-compacto.md §13). "
                     "No se escribió nada." % (v_deck or "desconocida", v_tpl or "desconocida"))
    out.mkdir(parents=True, exist_ok=True)
    escribir_atomico(out / "index.html", html)
    if args.actualizar_css or not css_dst.exists():
        escribir_atomico(css_dst, css_tpl)
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
