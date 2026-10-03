#!/usr/bin/env python3
"""
Customizador de AcroForms para propuestas MiCasino (CAP-007 Media Buyer +
CAP-008 Telemarketing). Aplica los entregables y acreditación específicos
de la cuenta MiCasino tras la corrida del script canónico de AcroForms.

Uso:
    python customize-micasino.py <pdf>
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-micasino.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": (
            "Workbook\r"
            "Manual de prompt\r"
            "Presentaciones"
        ),
        "Acreditacion": "Certificado avalado por Intezia",
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

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"MiCasino AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
