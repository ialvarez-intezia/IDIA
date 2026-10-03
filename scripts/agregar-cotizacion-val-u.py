#!/usr/bin/env python3
"""
Añade los 3 campos AcroForm (Inversion, Descuento, Total) a la Hoja de
Cotización del documento curricular branded de Val-U × Intezia (CU-005).

Caso especial (no es el deck canónico de 16 slides horizontal): el PDF es un
documento A4 vertical generado desde clientes/propuestas/val-u/documento.html.
Los rects se midieron empíricamente sobre el render a 150dpi de la página
"Hoja de Cotización" (ver conversión px→pt: factor 0.48 = 72/150).

Uso:
    python3 scripts/agregar-cotizacion-val-u.py "<ruta-al-pdf>"
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject, BooleanObject, DictionaryObject, FloatObject,
    NameObject, NumberObject, TextStringObject,
)

MARKER = "Hoja de Cotización"

FIELDS = [
    {
        "name": "Inversion",
        "tooltip": "Inversión del programa (ej. 1.200 USD).",
        "rect": (342, 565, 540, 604),
        "font_size": 13,
        "calc_action": False,
    },
    {
        "name": "Descuento",
        "tooltip": "Descuento aplicado, si lo hay (ej. -100 USD).",
        "rect": (342, 521, 540, 560),
        "font_size": 13,
        "calc_action": False,
    },
    {
        "name": "Total",
        "tooltip": "Total. Autocalculado al cambiar Inversión o Descuento; editable a mano para overrides.",
        "rect": (342, 479, 540, 517),
        "font_size": 15,
        "calc_action": True,
    },
]

CALC_JS = (
    'var b=this.getField("Inversion").value;'
    'var d=this.getField("Descuento").value;'
    'var bn=parseFloat(String(b).replace(/[^0-9.\\-]/g,""))||0;'
    'var dn=parseFloat(String(d).replace(/[^0-9.\\-]/g,""))||0;'
    'var t=bn-Math.abs(dn);'
    'event.value=isNaN(t)?"":t.toFixed(0);'
)


def find_page(reader: PdfReader, marker: str) -> int:
    target = marker.casefold()
    for idx, page in enumerate(reader.pages):
        text = (page.extract_text() or "").casefold()
        if target in text:
            return idx
    sys.exit(f"ERROR: no se encontró la página con el marcador '{marker}'")


def build_field(spec: dict) -> DictionaryObject:
    field = DictionaryObject({
        NameObject("/Type"): NameObject("/Annot"),
        NameObject("/Subtype"): NameObject("/Widget"),
        NameObject("/FT"): NameObject("/Tx"),
        NameObject("/T"): TextStringObject(spec["name"]),
        NameObject("/TU"): TextStringObject(spec["tooltip"]),
        NameObject("/V"): TextStringObject(""),
        NameObject("/DV"): TextStringObject(""),
        NameObject("/Rect"): ArrayObject([NumberObject(c) for c in spec["rect"]]),
        NameObject("/F"): NumberObject(4),
        NameObject("/DA"): TextStringObject(f"/Helv {spec['font_size']} Tf 0 g"),
        NameObject("/Q"): NumberObject(1),  # right-aligned (columna Monto)
        NameObject("/Ff"): NumberObject(0),
        NameObject("/MaxLen"): NumberObject(40),
        NameObject("/BS"): DictionaryObject({
            NameObject("/Type"): NameObject("/Border"),
            NameObject("/W"): NumberObject(0),
            NameObject("/S"): NameObject("/S"),
        }),
        NameObject("/MK"): DictionaryObject({NameObject("/BC"): ArrayObject()}),
    })
    return field


def add_calc_action(field: DictionaryObject) -> None:
    js_action = DictionaryObject({
        NameObject("/Type"): NameObject("/Action"),
        NameObject("/S"): NameObject("/JavaScript"),
        NameObject("/JS"): TextStringObject(CALC_JS),
    })
    field[NameObject("/AA")] = DictionaryObject({NameObject("/C"): js_action})


def make_dr(writer: PdfWriter) -> DictionaryObject:
    font = writer._add_object(DictionaryObject({
        NameObject("/Type"): NameObject("/Font"),
        NameObject("/Subtype"): NameObject("/Type1"),
        NameObject("/BaseFont"): NameObject("/Helvetica"),
        NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
    }))
    return DictionaryObject({NameObject("/Font"): DictionaryObject({NameObject("/Helv"): font})})


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: agregar-cotizacion-val-u.py <ruta-al-pdf>")
    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)
    page_idx = find_page(reader, MARKER)
    page = writer.pages[page_idx]

    all_refs = []
    calc_refs = []
    for spec in FIELDS:
        field = build_field(spec)
        if spec["calc_action"]:
            add_calc_action(field)
        ref = writer._add_object(field)
        field[NameObject("/P")] = page.indirect_reference
        if "/Annots" in page:
            page[NameObject("/Annots")].append(ref)
        else:
            page[NameObject("/Annots")] = ArrayObject([ref])
        all_refs.append(ref)
        if spec["calc_action"]:
            calc_refs.append(ref)

    catalog = writer._root_object
    acro = catalog.get(NameObject("/AcroForm"), DictionaryObject())
    catalog[NameObject("/AcroForm")] = acro
    fields_arr = acro.get(NameObject("/Fields"), ArrayObject())
    for ref in all_refs:
        fields_arr.append(ref)
    acro[NameObject("/Fields")] = fields_arr
    acro[NameObject("/NeedAppearances")] = BooleanObject(True)
    acro[NameObject("/DA")] = TextStringObject("/Helv 12 Tf 0 g")
    acro[NameObject("/DR")] = make_dr(writer)
    if calc_refs:
        acro[NameObject("/CO")] = ArrayObject(calc_refs)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"  página {page_idx + 1} ('{MARKER}'): {', '.join(s['name'] for s in FIELDS)}")


if __name__ == "__main__":
    main()
