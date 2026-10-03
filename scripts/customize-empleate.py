#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Empléate TA-030.
Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos
con contenido real listo-para-entregar, tras la corrida del script canónico.

Esta propuesta NO lleva slide de precio (alianza): solo 8 campos no-precio.
Los campos quedan EDITABLES: solo se reescribe /V y /DV.

Uso:
    python customize-empleate.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-empleate.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Biblioteca de prompts del rol",
            "Cheatsheets de Gemini y Copilot",
            "Checklist de verificación y datos",
            "Plan de adopción de 30 días",
            "Manual digital por participante.",
            "Panel de progreso individual.",
            "Certificado digital INTEZIA.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como TA-030.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos la fecha del taller de 4 h y la zona horaria de los "
            "cinco equipos de Empléate."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos la sede presencial, los participantes de los cinco "
            "equipos y la agenda del taller."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kick-off de 30 min con Anthony para elegir los casos reales de "
            "cada equipo que entran al taller."
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

    print(f"Empléate TA-030 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
