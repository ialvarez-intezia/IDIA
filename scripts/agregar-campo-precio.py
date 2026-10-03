#!/usr/bin/env python3
"""
Añade los AcroForm fields a las slides editables del PDF.

Tres grupos de páginas, detectados por marker de texto en la página:

- Slide Propuesta Económica — 5 campos
    PrecioBase, Descuento, PrecioTotal (auto-calc)
    Programa, Notas (multiline libre, ventas escribe lo que quiera)
- Slide Beneficios (marker "Lo que se llevan") — 2 campos
    Entregables, Acreditacion — multiline libre, sin viñetas fijas.
    Van SIEMPRE en negrita: apariencia /AP horneada en Helvetica-Bold
    (ver acroform_appearance.py).
- Slide Próximos pasos (marker "Cómo arrancamos") — 6 campos
    3 pasos × (título single-line + body multiline)

Total canónico: 13 campos AcroForm. Defaults pre-cargados como placeholders
entre corchetes; cada propuesta clona el deck y los reemplaza.

Multi-page (multi-tier pricing): si una propuesta tiene VARIAS slides con
el mismo marker (ej. 3 'Propuesta Económica' para tiers de pricing), el
script añade fields a todas. La 1ª instancia mantiene los nombres canónicos
(PrecioBase, Descuento, ...), las siguientes reciben sufijo `_N`
(PrecioBase_2, Descuento_2, PrecioTotal_2 ...). El JS de cálculo se genera
por-instancia para que cada PrecioTotal_N referencie su propio par
PrecioBase_N / Descuento_N. Backward-compatible: propuestas con 1 sola
slide por marker mantienen comportamiento idéntico.

Variante "Inversión por fases" (cotización por fase + total, UNA sola
página): marker propio "Inversión por fases" (el H2 de la slide), grupo
FASE_PRICE_FIELDS — PrecioFase1..N (editable) + PrecioBase (subtotal
auto-calculado como suma de las PrecioFaseN, vía spec["calc_js"]) +
Descuento + PrecioTotal (Base − Descuento, sin cambios) + Notas. El campo
opcional `calc_js` en un spec sobrescribe el JS por defecto (make_calc_js)
de `calc_action`. No colisiona con "Propuesta Económica": cada PDF se
procesa por separado, así que esto no afecta a ningún otro deck existente.
Origen: CAP-098 IOED (2026-08-11).

Variante "Inversión por Permanencia" (cuota mensual × duración de ciclo,
servicio Innovación — empresa/tipos-de-documento.md §0): marker propio
"Inversión por Permanencia" (el H2 de la slide), grupo CICLO_PRICE_FIELDS —
3 columnas de duración (Cuota3m/Descuento3m, Cuota6m/Descuento6m,
Cuota12m/Descuento12m, todas editables, sin auto-cálculo) + Notas. Sin
PrecioBase/PrecioTotal: cada columna es un plan independiente (cuota mensual
+ beneficio por permanencia), no hay un total único que sumar entre
columnas. No colisiona con "Propuesta Económica" ni "Inversión por fases":
cada PDF se procesa por separado. Origen: INN-001 Zoom (2026-08-30, primer
piloto del servicio Innovación).

Compatibilidad de lectores:
- Adobe Reader: todos los campos editables + cálculo automático del total
- Preview macOS: campos editables funcionan; el JS de cálculo no se ejecuta

Uso:
    python3 agregar-campo-precio.py <ruta-al-pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    BooleanObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    NumberObject,
    TextStringObject,
)

# --- Field-flag bits (PDF 1.7 §12.7.4.1) ---
FIELD_FLAG_READONLY = 1 << 0   # bit 1
FIELD_FLAG_MULTILINE = 1 << 12  # bit 13

# --- JS de cálculo del total (slide 8) ---
# Multi-page support: cuando una propuesta tiene varias slides con el mismo
# marker (ej. 3 "Propuesta Económica" para tiers de pricing), las instancias
# 2+ reciben sufijo _N en los field names. El JS de cálculo se genera
# por-instancia para que cada PrecioTotal_N referencie su propio par
# PrecioBase_N / Descuento_N.
def make_calc_js(suffix: str = "") -> str:
    return (
        f'var b=this.getField("PrecioBase{suffix}").value;'
        f'var d=this.getField("Descuento{suffix}").value;'
        'var bn=parseFloat(String(b).replace(/[^0-9.\\-]/g,""))||0;'
        'var dn=parseFloat(String(d).replace(/[^0-9.\\-]/g,""))||0;'
        'var t=bn-Math.abs(dn);'
        'event.value=isNaN(t)?"":t.toFixed(0);'
    )


# JS de subtotal para el patrón "Inversión por fases" (cotización por fase +
# total): PrecioBase actúa como subtotal auto-calculado a partir de N cajas
# PrecioFaseN. PrecioTotal sigue usando make_calc_js (PrecioBase − Descuento)
# sin cambios — el /CO coloca este cálculo ANTES para que Total ya vea el
# subtotal actualizado.
def make_fase_subtotal_js(fase_count: int) -> str:
    terms = []
    lines = []
    for i in range(1, fase_count + 1):
        lines.append(
            f'var f{i}=parseFloat(String(this.getField("PrecioFase{i}").value)'
            '.replace(/[^0-9.\\-]/g,""))||0;'
        )
        terms.append(f'f{i}')
    lines.append(f'var t={"+".join(terms)};')
    lines.append('event.value=isNaN(t)?"":t.toFixed(0);')
    return "".join(lines)

# Defaults canónicos.
# - ENTREGABLES y ACREDITACIONES traen contenido institucional FIJO
#   (decisión 2026-05-05 — siempre se entregan estos tres bullets, sin
#   variar por cliente). El único token sustituible es [CÓDIGO] en
#   Acreditación: se pre-llena por propuesta tras generar el PDF
#   (customize-acroforms.py / customize-<slug>.py) sustituyéndolo por el
#   código real del programa (TA-NNN, CU-NNN, CAP-NNN, DIP-NNN). Las otras
#   dos líneas (ABR · material curado) son fijas. El campo sigue editable.
# - PROGRAMA y NOTAS siguen siendo placeholders entre corchetes:
#   ventas/CAO los redacta en Adobe Reader sobre el PDF ya generado.
# - PASOS arrancan como placeholders, pero se PRE-LLENAN por propuesta tras
#   generar el PDF (customize-acroforms.py / customize-<slug>.py) con los 3
#   pasos listos-para-entregar — los campos siguen editables. Igual que
#   Entregables. Ver plantillas/generar-pdf.md.
# - Cada caja multiline usa "\r" como separador de línea (estándar AcroForm).
ENTREGABLES_DEFAULT = "\r".join([
    "Manual digital por participante.",
    "Panel de progreso individual.",
    "Certificado de participación INTEZIA.",
])
ACREDITACIONES_DEFAULT = "\r".join([
    "Programa registrado en INTEZIA Education como [CÓDIGO].",
    "Cumple con el modelo pedagógico oficial (ABR).",
    "Material curado y revisado por el equipo académico.",
])
PROGRAMA_DEFAULT = "\r".join([
    "[Nombre del programa formativo]",
    "[Cantidad de participantes que cubre la propuesta]",
])
NOTAS_DEFAULT = "\r".join([
    "[Condiciones de pago: moneda, tasa, anticipo]",
    "[Cláusula legal de garantía / devolución]",
])
PASOS_DEFAULTS = {
    "Paso01Titulo": "[Paso 01 · título corto]",
    "Paso01Body": "[Describe el paso 01: qué hace el cliente, fecha límite, responsable]",
    "Paso02Titulo": "[Paso 02 · título corto]",
    "Paso02Body": "[Describe el paso 02: qué hace el cliente, fecha límite, responsable]",
    "Paso03Titulo": "[Paso 03 · título corto]",
    "Paso03Body": "[Describe el paso 03: qué hace el cliente, fecha límite, responsable]",
}


# Helper para cajas multiline (sin viñetas fijas — ventas escribe libre).
# Fondo blanco implícito (build_field lo aplica cuando multiline=True
# sin bg_color explícito) → tapa el texto demo del HTML al editar.
# font: nombre de fuente del /DR — "Helv" (Helvetica regular) o
# "HeBO" (Helvetica-Bold). Ver make_dr().
def _multibox(name, default, rect, font_size=10, font="Helv"):
    return {
        "name": name,
        "tooltip": f"{name} (editable, multilínea; usa Enter para nueva línea).",
        "rect": rect,
        "font_size": font_size,
        "font_color": "0 g",
        "font": font,
        "quadding": 0,            # left aligned
        "multiline": True,
        "readonly": False,
        "default": default,
        "calc_action": False,
    }


# --- Grupos de campos por página ---
# Slide 8: Propuesta Económica
PRECIO_FIELDS = [
    {
        "name": "PrecioBase",
        "tooltip": "Precio base de la propuesta (ej. 2.250 REF).",
        # CSS: top=220 left=580 w=487 h=52
        "rect": (435, 391, 800, 430),
        "font_size": 18,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "Descuento",
        "tooltip": "Descuento aplicado (ej. -450 REF).",
        # CSS: top=318 left=580 w=487 h=44
        "rect": (435, 323, 800, 357),
        "font_size": 14,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioTotal",
        "tooltip": "Total. Autocalculado al cambiar precio o descuento; editable a mano para overrides.",
        # CSS: top=414 left=580 w=487 h=76
        "rect": (435, 227, 800, 285),
        "font_size": 26,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "readonly": False,        # editable a mano; el JS recalcula al cambiar base/descuento
        "default": "",
        "calc_action": True,
    },
    # Programa (multiline editable). CSS top=222, h=105, left=56, w=480.
    # PDF: y2=595-222·0.75=428.5≈429; y1=595-(222+105)·0.75=349.75≈350.
    # x1=56·0.75=42; x2=(56+480)·0.75=402.
    # font_size 11 (un poco más grande que slide 7 — el bloque es más ancho).
    {
        **_multibox("Programa", PROGRAMA_DEFAULT, (42, 350, 402, 429), font_size=11),
    },
    # Notas (multiline editable). CSS top=392, h=110, left=56, w=480.
    # PDF: y2=595-392·0.75=301; y1=595-(392+110)·0.75=218.5≈219.
    {
        **_multibox("Notas", NOTAS_DEFAULT, (42, 219, 402, 301), font_size=11),
    },
]

# Variante "Inversión por fases": cotización por fase (N cajas PrecioFaseN)
# + subtotal auto-calculado (PrecioBase) + Descuento + Total. Solo se activa
# en páginas cuyo H2 dice literalmente "Inversión por fases" (marker propio,
# no colisiona con "Propuesta Económica" de las demás propuestas — cada PDF
# se procesa por separado, así que esto no afecta a ningún otro deck).
# Origen: CAP-098 IOED, plan de 3 fases cotizadas + total (2026-08-11).
FASE_PRICE_FIELDS = [
    {
        "name": "PrecioFase1",
        "tooltip": "Monto de la Fase 1 (ej. 1.200 REF).",
        # CSS: top=180 left=396 w=140 h=40 (row 1, top=168 + 12)
        "rect": (297, 430, 402, 460),
        "font_size": 13,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioFase2",
        "tooltip": "Monto de la Fase 2 (ej. 1.200 REF).",
        # CSS: top=252 left=396 w=140 h=40 (row 2, top=240 + 12)
        "rect": (297, 376, 402, 406),
        "font_size": 13,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioFase3",
        "tooltip": "Monto de la Fase 3 (ej. 1.200 REF).",
        # CSS: top=324 left=396 w=140 h=40 (row 3, top=312 + 12)
        "rect": (297, 322, 402, 352),
        "font_size": 13,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioBase",
        "tooltip": "Inversión total del plan. Autocalculado como suma de las fases; editable a mano para overrides.",
        # CSS: top=170 left=580 w=487 h=52 (base-frame reposicionado)
        "rect": (435, 428.5, 800, 467.5),
        "font_size": 18,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": True,
        "calc_js": make_fase_subtotal_js(3),
    },
    {
        "name": "Descuento",
        "tooltip": "Descuento aplicado (ej. -450 REF).",
        # CSS: top=268 left=580 w=487 h=44 (discount-frame reposicionado)
        "rect": (435, 361, 800, 394),
        "font_size": 14,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioTotal",
        "tooltip": "Total. Autocalculado al cambiar el subtotal o el descuento; editable a mano para overrides.",
        # CSS: top=360 left=580 w=487 h=76 (total-frame reposicionado)
        "rect": (435, 268, 800, 325),
        "font_size": 26,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": True,
    },
    # Notas (multiline editable). CSS top=428, h=110, left=56, w=480.
    # PDF: y2=595-428·0.75=274; y1=595-(428+110)·0.75=191.5.
    {
        **_multibox("Notas", NOTAS_DEFAULT, (42, 191.5, 402, 274), font_size=11),
    },
]

# Variante "Inversión por Permanencia": cuota mensual × duración de ciclo
# (servicio Innovación). 3 columnas independientes (3/6/12 meses), cada una
# con Cuota{N}m (editable) + Descuento{N}m (beneficio por permanencia,
# editable) — sin auto-cálculo, ventas escribe el monto final de cada celda.
# Coordenadas sincronizadas con overrides.css del deck (.tier-col top=222,
# todo hijo position:absolute con top relativo — factor px→pt ×0.75):
#   Columna   left_css  w_css  →  x1_pt    x2_pt
#   3 meses   580       149       435.00   546.75
#   6 meses   749       149       561.75   673.50
#   12 meses  918       149       688.50   800.25
#   Fila (top absoluto = 222 + offset)      top_abs  h_css  →  y1_pt   y2_pt
#   tier-frame-cuota      (offset 42)        264      44        364.00  397.00
#   tier-frame-descuento  (offset 112)       334      38        316.00  344.50
# Origen: INN-001 Zoom (2026-08-30, primer piloto del servicio Innovación).
def _cuota_field(name, x1, x2, tooltip):
    return {
        "name": name,
        "tooltip": tooltip,
        "rect": (x1, 364, x2, 397),
        "font_size": 15,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    }


def _descuento_field(name, x1, x2, tooltip):
    return {
        "name": name,
        "tooltip": tooltip,
        "rect": (x1, 316, x2, 344.5),
        "font_size": 13,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "readonly": False,
        "default": "",
        "calc_action": False,
    }


CICLO_PRICE_FIELDS = [
    _cuota_field("Cuota3m", 435, 546.75, "Cuota mensual del ciclo de 3 meses (ej. 450 REF/mes)."),
    _descuento_field("Descuento3m", 435, 546.75, "Beneficio por permanencia del ciclo de 3 meses (si aplica)."),
    _cuota_field("Cuota6m", 561.75, 673.5, "Cuota mensual del ciclo de 6 meses (ej. 400 REF/mes)."),
    _descuento_field("Descuento6m", 561.75, 673.5, "Beneficio por permanencia del ciclo de 6 meses."),
    _cuota_field("Cuota12m", 688.5, 800.25, "Cuota mensual del ciclo de 12 meses (ej. 350 REF/mes)."),
    _descuento_field("Descuento12m", 688.5, 800.25, "Beneficio por permanencia del ciclo de 12 meses."),
    # Notas (multiline editable) — misma posición estándar que PRECIO_FIELDS.
    {
        **_multibox("Notas", NOTAS_DEFAULT, (42, 219, 402, 301), font_size=11),
    },
]

# Slide 7: Beneficios → 1 caja multiline para Entregables + 1 para Acreditación.
# Sin viñetas fijas: el equipo de ventas escribe la cantidad de líneas que
# necesite, separadas con Enter. CSS px → pt PDF (factor 0.75).
#
# Cada caja cubre el área completa del bloque (sin offset — ya no hay
# cuadrito amarillo que reservar) para que el /BG blanco tape el texto
# demo del HTML que queda detrás:
# - CSS top=187, height=156, left=584 (entregables) / 840 (acreditación)
# - PDF y2 = 595 - 187·0.75 = 454.75 ≈ 455
# - PDF y1 = 595 - (187+156)·0.75 = 337.75 ≈ 338
# - PDF x1 entregables = 584·0.75 = 438
# - PDF x2 entregables = (584+210)·0.75 = 595.5 ≈ 596
# - PDF x1 acreditación = 840·0.75 = 630
# - PDF x2 acreditación = (840+210)·0.75 = 787.5 ≈ 788
# Entregables y Acreditación van SIEMPRE en negrita (font="HeBO" →
# Helvetica-Bold del /DR). Aplica al texto pre-llenado y al que escriba
# ventas en Reader. El resto de campos usa "Helv" (regular) por defecto.
BENEFITS_FIELDS = [
    _multibox("Entregables",  ENTREGABLES_DEFAULT,    (438, 338, 596, 455), font="HeBO"),
    _multibox("Acreditacion", ACREDITACIONES_DEFAULT, (630, 338, 788, 455), font="HeBO"),
]

# Slide 9: Próximos pasos → 3 cards × (título + body)
# Tamaños estándar (el font_size vive en el /DA → aplica al texto pre-llenado
# por Claude y al que escribe ventas en Reader): título 18 pt, body 15 pt.
# Sincronizado con la preview HTML en cumbre-andina/styles.css (24 px / 20 px).
def _paso_title(name, x_left, x_right):
    return {
        "name": name,
        "tooltip": f"{name} (editable, single-line).",
        # 2026-09-23: recalculado para el .step-card compacto (padding-top
        # 60px, antes 110px) — ver _base/styles.css → .acro-paso-NN-titulo.
        "rect": (x_left, 412, x_right, 433),
        "font_size": 15,
        "font_color": "0 g",
        "quadding": 0,
        "multiline": False,
        "readonly": False,
        "default": PASOS_DEFAULTS[name],
        "calc_action": False,
    }


def _paso_body(name, x_left, x_right):
    return {
        "name": name,
        "tooltip": f"{name} (editable, multiline).",
        # 2026-09-23: recalculado para el .step-card compacto (min-height
        # 200px, antes 400px) — ver _base/styles.css → .acro-paso-NN-body.
        "rect": (x_left, 338.5, x_right, 407.5),
        "font_size": 12,
        "font_color": "0 g",
        "quadding": 0,
        "multiline": True,
        "readonly": False,
        "default": PASOS_DEFAULTS[name],
        "calc_action": False,
    }


# Coordenadas pt PDF de las 3 cards (CSS left 84/426/768 → pt 63/320/576)
STEPS_FIELDS = [
    _paso_title("Paso01Titulo", 63, 266),
    _paso_body("Paso01Body", 63, 266),
    _paso_title("Paso02Titulo", 320, 522),
    _paso_body("Paso02Body", 320, 522),
    _paso_title("Paso03Titulo", 576, 779),
    _paso_body("Paso03Body", 576, 779),
]


PAGE_GROUPS = [
    {"marker": "Propuesta Económica", "fields": PRECIO_FIELDS},
    {"marker": "Inversión por fases", "fields": FASE_PRICE_FIELDS},
    {"marker": "Inversión por Permanencia", "fields": CICLO_PRICE_FIELDS},
    # 'requires': la slide de Beneficios de un Taller/Curso lleva los bloques
    # 'Entregables' y 'Acreditación'; la de una Charla comparte el h2 'Lo que
    # se llevan' pero NO tiene esos bloques (es contenido estático). El extra
    # marker evita añadirle campos editables a la slide de Beneficios de una
    # Charla.
    {"marker": "Lo que se llevan", "requires": ["Entregables"], "fields": BENEFITS_FIELDS},
    {"marker": "Cómo arrancamos",     "fields": STEPS_FIELDS},
]


def find_pages_by_marker(reader: PdfReader, marker: str, requires=None) -> list:
    """Búsqueda case-insensitive del texto en el PDF (uppercase via CSS).

    Retorna TODAS las páginas que contienen el marker — necesario para soportar
    propuestas con múltiples instancias del mismo bloque (ej. 3 'Propuesta
    Económica' para tiers de pricing).

    `requires`: lista opcional de substrings que TAMBIÉN deben aparecer en la
    misma página. Filtra falsos positivos (ej. la slide de Beneficios de una
    Charla, que comparte el h2 'Lo que se llevan' con la de un Taller pero no
    tiene los bloques Entregables/Acreditación).

    Si no hay coincidencias retorna [] — el grupo se omite sin abortar. Esto
    permite generar Charlas, que no tienen slide de Propuesta Económica.
    """
    target = marker.casefold()
    extra = [r.casefold() for r in (requires or [])]
    pages = []
    for idx, page in enumerate(reader.pages):
        try:
            text = (page.extract_text() or "").casefold()
        except Exception:
            text = ""
        if target in text and all(r in text for r in extra):
            pages.append(idx)
    return pages


def build_field(spec: dict) -> DictionaryObject:
    """Construye el dictionary del widget annotation / form field."""
    flags = 0
    if spec["readonly"]:
        flags |= FIELD_FLAG_READONLY
    if spec.get("multiline"):
        flags |= FIELD_FLAG_MULTILINE

    default_value = spec.get("default", "") or ""
    # Fuente del /DA — debe existir en el /DR de la AcroForm (ver make_dr).
    font_name = spec.get("font", "Helv")

    field = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/FT"): NameObject("/Tx"),
            NameObject("/T"): TextStringObject(spec["name"]),
            NameObject("/TU"): TextStringObject(spec["tooltip"]),
            NameObject("/V"): TextStringObject(default_value),
            NameObject("/DV"): TextStringObject(default_value),
            NameObject("/Rect"): ArrayObject(
                [NumberObject(c) for c in spec["rect"]]
            ),
            NameObject("/F"): NumberObject(4),  # printable
            NameObject("/DA"): TextStringObject(
                f"/{font_name} {spec['font_size']} Tf {spec['font_color']}"
            ),
            NameObject("/Q"): NumberObject(spec["quadding"]),
            NameObject("/Ff"): NumberObject(flags),
            NameObject("/MaxLen"): NumberObject(2000 if spec.get("multiline") else 80),
            # Sin borde dibujado por el lector PDF
            NameObject("/BS"): DictionaryObject(
                {
                    NameObject("/Type"): NameObject("/Border"),
                    NameObject("/W"): NumberObject(0),
                    NameObject("/S"): NameObject("/S"),
                }
            ),
            NameObject("/MK"): DictionaryObject(
                {
                    NameObject("/BC"): ArrayObject(),
                    # /BG (fondo del campo):
                    #  - bg_color explícito → ese color (ej. amarillo de tags slide 7)
                    #  - multiline sin bg_color → blanco (enmascara cualquier
                    #    texto demo subyacente al editar)
                    #  - resto sin bg_color → sin fondo
                    **(
                        {NameObject("/BG"): ArrayObject(
                            [FloatObject(c) for c in spec["bg_color"]]
                        )}
                        if spec.get("bg_color")
                        else (
                            {NameObject("/BG"): ArrayObject(
                                [FloatObject(1), FloatObject(1), FloatObject(1)]
                            )}
                            if spec.get("multiline")
                            else {}
                        )
                    ),
                }
            ),
        }
    )
    return field


def add_calculation_action(field: DictionaryObject, js: str) -> None:
    """Adjunta la acción JS /AA/C (solo para PrecioTotal).

    Recibe el JS como parámetro para soportar multi-page (cada PrecioTotal_N
    debe referenciar su propio PrecioBase_N / Descuento_N).
    """
    js_action = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Action"),
            NameObject("/S"): NameObject("/JavaScript"),
            NameObject("/JS"): TextStringObject(js),
        }
    )
    aa = DictionaryObject({NameObject("/C"): js_action})
    field[NameObject("/AA")] = aa


def make_dr(writer: PdfWriter) -> DictionaryObject:
    """Construye el /DR (Default Resources) de la AcroForm.

    Define las dos fuentes que referencian los /DA de los campos:
      /Helv → Helvetica       (regular — la mayoría de campos)
      /HeBO → Helvetica-Bold  (negrita — Entregables y Acreditación)

    Sin /DR, los lectores no resuelven el nombre de fuente del /DA y caen
    a un fallback regular — por eso la negrita no se aplicaba. Ambas son
    fuentes estándar Type1 (las «14 estándar»): no requieren incrustación
    ni descriptor.
    """
    def _font(base_font: str) -> DictionaryObject:
        return writer._add_object(DictionaryObject({
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject(base_font),
            NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
        }))

    return DictionaryObject({
        NameObject("/Font"): DictionaryObject({
            NameObject("/Helv"): _font("/Helvetica"),
            NameObject("/HeBO"): _font("/Helvetica-Bold"),
        })
    })


def add_fields(pdf_path: Path) -> None:
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    all_field_refs = []
    calc_order_refs = []
    summary_lines = []

    for group in PAGE_GROUPS:
        page_indices = find_pages_by_marker(
            reader, group["marker"], group.get("requires")
        )
        if not page_indices:
            summary_lines.append(
                f"  (omitido) '{group['marker']}' — no presente en este deck"
            )
            continue
        for instance, page_idx in enumerate(page_indices):
            # 1ª instancia → sufijo vacío (canónico). 2ª, 3ª, … → "_2", "_3", …
            suffix = "" if instance == 0 else f"_{instance + 1}"
            page = writer.pages[page_idx]
            names_in_page = []

            for spec in group["fields"]:
                # Clona el spec con el name sufijado
                new_spec = {**spec, "name": spec["name"] + suffix}
                field = build_field(new_spec)
                if new_spec.get("calc_action"):
                    add_calculation_action(field, new_spec.get("calc_js") or make_calc_js(suffix))

                ref = writer._add_object(field)
                field[NameObject("/P")] = page.indirect_reference

                if "/Annots" in page:
                    page[NameObject("/Annots")].append(ref)
                else:
                    page[NameObject("/Annots")] = ArrayObject([ref])

                all_field_refs.append(ref)
                if new_spec.get("calc_action"):
                    calc_order_refs.append(ref)
                names_in_page.append(new_spec["name"])

            label_extra = "" if instance == 0 else f" #{instance + 1}"
            summary_lines.append(
                f"  página {page_idx + 1} ('{group['marker']}'{label_extra}): {', '.join(names_in_page)}"
            )

    # Catálogo / AcroForm
    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
    else:
        acro = DictionaryObject()
        catalog[NameObject("/AcroForm")] = acro

    if NameObject("/Fields") not in acro:
        acro[NameObject("/Fields")] = ArrayObject()
    for ref in all_field_refs:
        acro[NameObject("/Fields")].append(ref)

    acro[NameObject("/NeedAppearances")] = BooleanObject(True)
    acro[NameObject("/DA")] = TextStringObject("/Helv 12 Tf 0 g")
    acro[NameObject("/DR")] = make_dr(writer)

    # /CO = orden de cálculo (solo PrecioTotal lo usa)
    if calc_order_refs:
        acro[NameObject("/CO")] = ArrayObject(calc_order_refs)

    # Hornea la apariencia en negrita de Entregables / Acreditación a partir
    # de su /V por defecto (ver acroform_appearance.py).
    baked = rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"  Total: {len(all_field_refs)} campos AcroForm añadidos.")
    print(f"  Apariencia en negrita horneada: {baked} campo(s).")
    for line in summary_lines:
        print(line)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: agregar-campo-precio.py <ruta-al-pdf>")
    add_fields(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
