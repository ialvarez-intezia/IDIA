#!/usr/bin/env python3
"""
Añade los AcroForm fields editables del workbook del participante.

Filosofía: una caja multiline por práctica. El participante escribe sus prompts
y respuestas directamente en el PDF (compatible con Adobe Reader y Preview).

Detección por marcador de texto — no por índice de página, así el script no
depende del número de sesiones del programa.

- Marcador: ``MI PROMPT:`` (uppercase exacto en el HTML, detección case-insensitive).
- Una ocurrencia por página de sesión (regla del canónico — ver
  ``plantillas/diseno-workbook.md`` §4).
- Naming canónico: primera ocurrencia ``MiPrompt``; sucesivas ``MiPrompt_2``,
  ``MiPrompt_3``… (patrón del repo — ver ``agregar-campo-precio.py``).

Coordenadas del campo (PDF pt, A4 vertical = 595×842 pt). Derivadas del CSS
canónico (``plantillas/workbook-canonico/workbook.css``):

    .practice  abs top: 680 px, left: 56 px, right: 56 px
    .prompt-box (dentro de .practice) abs top: 80 px (= 760 px del page top),
                left: 14 px (= 70 px del page), right: 14 px (= 70 px del page),
                height: 130 px (= bottom 890 px del page top)

CSS px → PDF pt: factor 0.75. Eje Y invertido con page-h = 842:
    x1 = 70  · 0.75 = 52.5  → 52
    x2 = 724 · 0.75 = 543
    y2 = 842 - 760 · 0.75 = 272
    y1 = 842 - 890 · 0.75 = 174.5 → 175

→ rect = (52, 175, 543, 272)

Si el canónico cambia esas coordenadas, actualizalas aquí EN SINCRONÍA con
``workbook.css``.

Uso:
    python3 agregar-campos-workbook.py <ruta-al-pdf>
"""
import sys
from pathlib import Path

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
FIELD_FLAG_MULTILINE = 1 << 12  # bit 13

# --- Marcador y coords del campo MI PROMPT ---
MARKER = "MI PROMPT:"
BASE_NAME = "MiPrompt"
PROMPT_RECT = (52, 175, 543, 272)
PROMPT_FONT_SIZE = 11
PROMPT_FONT_COLOR = "0 g"  # negro

# Texto sugerido en blanco — el participante lo borra al escribir.
PROMPT_DEFAULT = ""


def find_pages_with_marker(reader: PdfReader, marker: str) -> list:
    """Devuelve los índices de página (0-based) que contienen ``marker``.

    Búsqueda case-insensitive — el HTML canónico usa ``MI PROMPT:`` en
    mayúsculas pero algunos lectores normalizan a mixed-case.
    """
    target = marker.casefold()
    pages = []
    for idx, page in enumerate(reader.pages):
        try:
            text = (page.extract_text() or "").casefold()
        except Exception:
            text = ""
        if target in text:
            pages.append(idx)
    return pages


def build_field(name: str, rect, default: str = "") -> DictionaryObject:
    """Widget anotación / form field: caja multilínea, sin borde, fondo blanco."""
    flags = FIELD_FLAG_MULTILINE
    return DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/FT"): NameObject("/Tx"),
            NameObject("/T"): TextStringObject(name),
            NameObject("/TU"): TextStringObject(
                f"{name} — escribí tu respuesta acá (Enter para nueva línea)."
            ),
            NameObject("/V"): TextStringObject(default),
            NameObject("/DV"): TextStringObject(default),
            NameObject("/Rect"): ArrayObject([NumberObject(c) for c in rect]),
            NameObject("/F"): NumberObject(4),  # printable
            NameObject("/DA"): TextStringObject(
                f"/Helv {PROMPT_FONT_SIZE} Tf {PROMPT_FONT_COLOR}"
            ),
            NameObject("/Q"): NumberObject(0),  # left aligned
            NameObject("/Ff"): NumberObject(flags),
            NameObject("/MaxLen"): NumberObject(5000),
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
                    NameObject("/BG"): ArrayObject(
                        [FloatObject(1), FloatObject(1), FloatObject(1)]
                    ),
                }
            ),
        }
    )


def make_dr(writer: PdfWriter) -> DictionaryObject:
    """``/DR`` (Default Resources) con Helvetica regular para los ``/DA``.

    Sin ``/DR`` los lectores no resuelven el nombre de fuente del ``/DA`` y
    caen a un fallback — por eso lo declaramos explícito. Helvetica es Type1
    estándar: no requiere incrustación.
    """
    helv = writer._add_object(
        DictionaryObject(
            {
                NameObject("/Type"): NameObject("/Font"),
                NameObject("/Subtype"): NameObject("/Type1"),
                NameObject("/BaseFont"): NameObject("/Helvetica"),
                NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
            }
        )
    )
    return DictionaryObject(
        {
            NameObject("/Font"): DictionaryObject(
                {NameObject("/Helv"): helv}
            )
        }
    )


def add_fields(pdf_path: Path) -> None:
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    page_indices = find_pages_with_marker(reader, MARKER)
    if not page_indices:
        print(
            f"  (omitido) no se encontró el marcador '{MARKER}' en ninguna página."
        )
        print("  El workbook no tiene prácticas editables — nada que inyectar.")
        return

    all_field_refs = []
    summary_lines = []

    for instance, page_idx in enumerate(page_indices):
        suffix = "" if instance == 0 else f"_{instance + 1}"
        name = BASE_NAME + suffix
        page = writer.pages[page_idx]

        field = build_field(name, PROMPT_RECT, PROMPT_DEFAULT)
        ref = writer._add_object(field)
        field[NameObject("/P")] = page.indirect_reference

        if "/Annots" in page:
            page[NameObject("/Annots")].append(ref)
        else:
            page[NameObject("/Annots")] = ArrayObject([ref])

        all_field_refs.append(ref)
        summary_lines.append(f"  página {page_idx + 1}: {name}")

    # AcroForm root
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
    acro[NameObject("/DA")] = TextStringObject(f"/Helv {PROMPT_FONT_SIZE} Tf 0 g")
    acro[NameObject("/DR")] = make_dr(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"  Total: {len(all_field_refs)} campo(s) MI PROMPT añadido(s).")
    for line in summary_lines:
        print(line)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: agregar-campos-workbook.py <ruta-al-pdf>")
    add_fields(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
