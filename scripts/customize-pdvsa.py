#!/usr/bin/env python3
"""
Customizador de AcroForms para propuestas PDVSA.

Aplica el contenido específico de Entregables, Acreditación y títulos de
Próximos pasos que se repite en todas las propuestas PDVSA. Hardcodea los
strings con acentos correctos (UTF-8) para evitar problemas de encoding
al pasarlos por la línea de comandos de PowerShell.

Uso:
    python customize-pdvsa.py <pdf> <codigo>

Ejemplo:
    python customize-pdvsa.py propuesta.pdf CU-006
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("Uso: customize-pdvsa.py <pdf> <codigo>")

    pdf_path = Path(sys.argv[1])
    codigo = sys.argv[2]

    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "Workbook de Prompting Avanzado\rDashboard de progreso",
        "Acreditacion": (
            f"Programa registrado como {codigo} en INTEZIA Education\r"
            "Doble certificación: INTEZIA - Universidad Venezolana de los Hidrocarburos\r"
            "Modelo pedagógico oficial (ABR)"
        ),
        "Paso01Titulo": "Confirmar fechas y modalidad",
        "Paso02Titulo": "Firma de acuerdo",
        "Paso03Titulo": "Kick-off",
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

    print(f"PDVSA AcroForms customizados ({codigo}) en {pdf_path.name}")


if __name__ == "__main__":
    main()
