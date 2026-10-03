#!/usr/bin/env python3
"""
Apariencias horneadas (/AP) para los campos AcroForm que van en negrita
y para los campos con contenido pre-llenado por el sistema en regular
(Próximos pasos, Programa, Notas — ver REGULAR_BAKED_FIELDS).

Problema: los campos declarados con /DA solo (+ NeedAppearances=True) no
siempre se renderizan al descargar el PDF — Preview macOS y Chrome no
regeneran la apariencia desde /DA + /DR al guardar. Resultado: el texto
pre-llenado es invisible en el PDF descargado.

Solución: este módulo hornea un stream de apariencia /AP /N (Form XObject)
con el texto ya dibujado en la fuente correcta, partido en líneas para que
quepa en el ancho del campo. Así el texto se ve idéntico en TODOS los
lectores, sin depender de que regeneren nada. El campo sigue editable: al
editarlo en Adobe Reader, Adobe regenera la apariencia desde /DA.

Uso: cada script que toque el /V de estos campos llama a
`rebake_bold_fields(writer)` justo antes de `writer.write()`.
"""
from pypdf import PdfWriter
from pypdf._codecs.core_font_metrics import CORE_FONT_METRICS
from pypdf.generic import (
    ArrayObject,
    DecodedStreamObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    NumberObject,
)

# Campos en Helvetica-Bold (Entregables y Acreditación, + Cierre tipo escalera 2026-08-26)
BOLD_FIELDS = {
    "Entregables", "Acreditacion",
    "CierreResultado", "CierrePaso1", "CierrePaso2", "CierrePaso3",
}

# Fondo/texto por campo, para BOLD_FIELDS que viven sobre una caja de color de
# marca (no blanco) — ej. la escalera de Cierre (2026-08-26). Sin entrada aquí,
# _build_stream usa el default de siempre: fondo blanco, texto negro.
FIELD_COLORS = {
    "CierreResultado": ((0.9569, 0.7294, 0.1020), (0, 0, 0)),  # amarillo / negro
    "CierrePaso1":     ((0.9569, 0.7294, 0.1020), (0, 0, 0)),  # amarillo / negro
    "CierrePaso2":     ((0.898, 0.5176, 0.1373), (1, 1, 1)),   # naranja / blanco
    "CierrePaso3":     ((1, 1, 1), (0, 0, 0)),                 # blanco / negro
}

# Campos con contenido PRE-LLENADO por el sistema (no vacíos para que ventas
# escriba) que se hornean en Helvetica regular para que sean visibles al
# descargar el PDF (mismo problema que BOLD_FIELDS). Bug real 2026-09-23:
# "Programa" y "Notas" tenían /V correcto pero SIN /AP horneado — con
# /NeedAppearances=False (fix de 2026-08-31 para otro bug), Adobe Reader y
# Preview los mostraban en BLANCO pese a tener el texto correcto en /V (el
# extractor de PDF de Claude sí los regenera solo, por eso no se detectó antes
# — confirmado con pypdf: /AP ausente en ambos campos, en DET-019 y CAI-023).
# Campos de precio (PrecioBase/Descuento/PrecioTotal y sus variantes Fase/
# Ciclo) NO están acá a propósito: nacen vacíos por diseño (ventas los llena
# en Adobe), así que no hay texto pre-llenado que pueda quedar invisible.
REGULAR_BAKED_FIELDS = {
    "Paso01Titulo", "Paso02Titulo", "Paso03Titulo",
    "Paso01Body",   "Paso02Body",   "Paso03Body",
    "Programa", "Notas",
}

_PAD_X = 2.0          # margen horizontal interno (pt)
_PAD_TOP = 2.0        # margen superior interno (pt)
_LEADING_FACTOR = 1.19  # interlineado / tamaño de fuente
_ASCENT = 0.718       # ascendente Helvetica Bold y Regular (idéntico en AFM)

# Anchos de glifo Helvetica-Bold y Helvetica-Regular (1/1000 em)
_WIDTHS_BOLD    = CORE_FONT_METRICS["Helvetica-Bold"].character_widths
_DEFAULT_W_BOLD = _WIDTHS_BOLD.get("default", 556)

_WIDTHS_REGULAR    = CORE_FONT_METRICS["Helvetica"].character_widths
_DEFAULT_W_REGULAR = _WIDTHS_REGULAR.get("default", 556)


def _is_bold(name) -> bool:
    """True si el campo (con o sin sufijo `_N`) debe ir en negrita."""
    if name is None:
        return False
    base = str(name).split("_")[0]
    return base in BOLD_FIELDS


def _is_regular_baked(name) -> bool:
    """True si el campo es un paso que debe hornearse en regular."""
    if name is None:
        return False
    base = str(name).split("_")[0]
    return base in REGULAR_BAKED_FIELDS


def _text_width(s: str, size: float, widths: dict, default_w: float) -> float:
    """Ancho en pt de la cadena `s` en la fuente dada."""
    return sum(widths.get(ch, default_w) for ch in s) * size / 1000.0


def _wrap(text: str, max_w: float, size: float, widths: dict, default_w: float) -> list:
    """Parte `text` en líneas que quepan en `max_w`. Respeta los saltos
    explícitos (`\\r` / `\\n`) y envuelve por palabras las líneas largas."""
    lines = []
    paragraphs = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    for para in paragraphs:
        words = para.split(" ")
        current = ""
        for word in words:
            trial = word if not current else current + " " + word
            if not current or _text_width(trial, size, widths, default_w) <= max_w:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def _parse_font_size(da: str) -> float:
    """Extrae el tamaño de fuente del `/DA` (ej. '/HeBO 10 Tf 0 g')."""
    tokens = da.split()
    for i, tok in enumerate(tokens):
        if tok == "Tf" and i >= 1:
            try:
                return float(tokens[i - 1])
            except ValueError:
                break
    return 10.0


def _escape(s: str) -> str:
    """Escapa los caracteres especiales de un literal de cadena PDF."""
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _build_stream(rect, da: str, text: str,
                  font_key: str = "HeBO",
                  widths: dict = None,
                  default_w: float = None,
                  bg_rgb: tuple = (1, 1, 1),
                  text_rgb: tuple = (0, 0, 0)) -> bytes:
    """Construye el contenido del Form XObject de apariencia.

    `bg_rgb`/`text_rgb`: default blanco/negro (enmascara cualquier texto demo
    subyacente). Campos sobre una caja de color de marca (ver `FIELD_COLORS`)
    pasan su propio par para que el fondo horneado combine con la caja CSS."""
    if widths is None:
        widths = _WIDTHS_BOLD
    if default_w is None:
        default_w = _DEFAULT_W_BOLD

    w = abs(rect[2] - rect[0])
    h = abs(rect[3] - rect[1])
    size = _parse_font_size(da)
    leading = size * _LEADING_FACTOR
    first_baseline = h - _PAD_TOP - size * _ASCENT
    lines = _wrap(text, w - 2 * _PAD_X, size, widths, default_w)

    bg_r, bg_g, bg_b = bg_rgb
    tx_r, tx_g, tx_b = text_rgb
    parts = [
        "/Tx BMC",
        "q",
        f"{bg_r:g} {bg_g:g} {bg_b:g} rg",  # fondo (enmascara lo que haya detrás)
        f"0 0 {w:.2f} {h:.2f} re f",
        f"{tx_r:g} {tx_g:g} {tx_b:g} rg",  # color de texto
        "BT",
        f"/{font_key} {size:g} Tf",
        f"{leading:.2f} TL",
        f"{_PAD_X:.2f} {first_baseline:.2f} Td",
    ]
    for i, line in enumerate(lines):
        literal = f"({_escape(line)})"
        parts.append(f"{literal} Tj" if i == 0 else f"T* {literal} Tj")
    parts += ["ET", "Q", "EMC"]
    return "\n".join(parts).encode("cp1252", errors="replace")


def _make_appearance(writer: PdfWriter, rect, da: str, text: str,
                     base_font: str = "/Helvetica-Bold",
                     font_key: str = "HeBO",
                     widths: dict = None,
                     default_w: float = None,
                     bg_rgb: tuple = (1, 1, 1),
                     text_rgb: tuple = (0, 0, 0)):
    """Crea el Form XObject `/AP /N` y devuelve su referencia indirecta."""
    w = abs(rect[2] - rect[0])
    h = abs(rect[3] - rect[1])

    font = writer._add_object(DictionaryObject({
        NameObject("/Type"): NameObject("/Font"),
        NameObject("/Subtype"): NameObject("/Type1"),
        NameObject("/BaseFont"): NameObject(base_font),
        NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
    }))

    xobj = DecodedStreamObject()
    xobj.set_data(_build_stream(rect, da, text,
                                font_key=font_key,
                                widths=widths,
                                default_w=default_w,
                                bg_rgb=bg_rgb,
                                text_rgb=text_rgb))
    xobj[NameObject("/Type")] = NameObject("/XObject")
    xobj[NameObject("/Subtype")] = NameObject("/Form")
    xobj[NameObject("/FormType")] = NumberObject(1)
    xobj[NameObject("/BBox")] = ArrayObject([
        FloatObject(0), FloatObject(0), FloatObject(w), FloatObject(h),
    ])
    xobj[NameObject("/Resources")] = DictionaryObject({
        NameObject("/Font"): DictionaryObject({NameObject(f"/{font_key}"): font}),
    })
    return writer._add_object(xobj)


def rebake_bold_fields(writer: PdfWriter) -> int:
    """Hornea el `/AP` de:
    - BOLD_FIELDS (Entregables, Acreditacion): Helvetica-Bold
    - REGULAR_BAKED_FIELDS (Paso01-03 Titulo/Body): Helvetica regular

    Idempotente — llamar justo antes de `writer.write()`. Devuelve el número
    de campos horneados."""
    count = 0
    for page in writer.pages:
        if "/Annots" not in page:
            continue
        for annot in page["/Annots"]:
            obj = annot.get_object()
            name_val = obj.get("/T")
            if name_val is None:
                continue
            base_name = str(name_val).split("_")[0]

            rect = [float(c) for c in obj["/Rect"]]
            text = str(obj.get("/V", "") or "")

            if base_name in BOLD_FIELDS:
                da = str(obj.get("/DA", "/HeBO 10 Tf 0 g"))
                bg_rgb, text_rgb = FIELD_COLORS.get(base_name, ((1, 1, 1), (0, 0, 0)))
                ap_ref = _make_appearance(
                    writer, rect, da, text,
                    base_font="/Helvetica-Bold",
                    font_key="HeBO",
                    widths=_WIDTHS_BOLD,
                    default_w=_DEFAULT_W_BOLD,
                    bg_rgb=bg_rgb,
                    text_rgb=text_rgb,
                )
                obj[NameObject("/AP")] = DictionaryObject({NameObject("/N"): ap_ref})
                count += 1

            elif base_name in REGULAR_BAKED_FIELDS:
                da = str(obj.get("/DA", "/Helv 12 Tf 0 g"))
                ap_ref = _make_appearance(
                    writer, rect, da, text,
                    base_font="/Helvetica",
                    font_key="Helv",
                    widths=_WIDTHS_REGULAR,
                    default_w=_DEFAULT_W_REGULAR,
                )
                obj[NameObject("/AP")] = DictionaryObject({NameObject("/N"): ap_ref})
                count += 1

    return count
