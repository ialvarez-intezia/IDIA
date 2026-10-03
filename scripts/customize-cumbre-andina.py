#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta canónica Cumbre Andina (TA-001).
Pre-llena los 6 campos de la slide «Próximos pasos» + el campo «Acreditacion»
de la slide «Beneficios» con contenido real listo-para-entregar, tras la
corrida del script canónico de AcroForms.

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el
texto en Adobe Reader si hace falta. Sirve de referencia para el equipo de
ventas: el deck llega con los pasos redactados, no con placeholders.

Uso:
    python customize-cumbre-andina.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-cumbre-andina.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    # Próximos pasos — 3 cards × (título single-line + body multiline).
    # Acreditacion — 3 líneas estandarizadas; el único token variable es el
    # código del programa ([CÓDIGO] → TA-001 en la canónica). Las otras dos
    # líneas (ABR · material curado) son fijas. El campo sigue editable.
    # Contenido listo-para-entregar del demo canónico.
    updates = {
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como TA-001.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmas fechas",
        "Paso01Body": (
            "Validamos las fechas de las 3 sesiones del taller "
            "y la zona horaria."
        ),
        "Paso02Titulo": "Firmamos acuerdo",
        "Paso02Body": "Contrato simple + factura del 50 % de anticipo.",
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de 30 minutos con el equipo de Cumbre Andina para "
            "alinear los casos reales que entrarán al taller."
        ),
    }

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    for name, value in updates.items():
        for page in writer.pages:
            if "/Annots" not in page:
                continue
            for annot_ref in page["/Annots"]:
                obj = annot_ref.get_object()
                if obj.get("/T") == name:
                    obj[NameObject("/V")] = TextStringObject(value)
                    obj[NameObject("/DV")] = TextStringObject(value)

    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    # Re-hornea la apariencia en negrita de Acreditación con el /V actualizado.
    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"Cumbre Andina — Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
