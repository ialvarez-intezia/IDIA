#!/usr/bin/env python3
"""
Customizador de AcroForms para PDVSA CAP-012 · Auditoría y Consultoría de IA.

A diferencia de las otras propuestas PDVSA (CU-006/DIP-002/CU-007 que son
capacitaciones formativas), CAP-012 es un proyecto consultivo con
entregables corporativos distintos. Hardcodea los strings UTF-8 con
acentos correctos.

Uso:
    python customize-pdvsa-cap012.py <pdf>
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-pdvsa-cap012.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": (
            "Reporte de Auditoría con calificación objetiva por área y Mapa de Calor\r"
            "Manual oficial de Políticas de Uso de IA de PDVSA (construido conjuntamente)\r"
            "Asesoría técnica documentada del Conjunto Tecnológico por proceso\r"
            "Plan de Digitalización por fases con indicadores comparativos antes y después\r"
            "Tablero institucional de seguimiento PDVSA × INTEZIA"
        ),
        "Acreditacion": (
            "Programa registrado como CAP-012 en INTEZIA Education\r"
            "Doble certificación: INTEZIA - Universidad Venezolana de los Hidrocarburos\r"
            "Modelo pedagógico oficial (ABR) aplicado a contexto consultivo"
        ),
        "Paso01Titulo": "Confirmar fechas y modalidad",
        "Paso02Titulo": "Firma de acuerdo",
        "Paso03Titulo": "Arranque formal",
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

    print(f"PDVSA CAP-012 AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
