#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Dr. Care TA-024.
Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos
con contenido real listo-para-entregar, tras la corrida del script canónico.

Esta propuesta NO lleva slide de precio: solo 8 campos no-precio.
Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-dr-care.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-dr-care.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Biblioteca de prompts del rol",
            "Cheatsheets de Claude y Gemini",
            "Informe de datos con IA",
            "Concepto de producto con IA",
            "Manual digital por participante.",
            "Panel de progreso individual.",
            "Certificado digital INTEZIA.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como TA-024.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 2 sesiones de 2 h y la zona "
            "horaria del equipo de Dr. Care."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos sede presencial, participantes y agenda de las "
            "2 sesiones del taller."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kick-off de 30 min con Douglas para alinear los datos, campañas "
            "y productos reales que entran al taller."
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

    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"Dr. Care TA-024 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
