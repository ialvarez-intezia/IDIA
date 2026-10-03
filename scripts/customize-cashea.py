#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Cashea CAP-005.
Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos
con contenido real listo-para-entregar, tras la corrida del script canónico.

Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-cashea.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-cashea.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Matriz de selección de modelos (Claude / ChatGPT / Gemini)",
            "Kit de prompts del rol propio",
            "Custom GPT personal del área",
            "Borrador de Política de Uso Aceptable (AUP) del equipo",
            "Manual digital por participante.",
            "Panel de progreso individual.",
            "Certificado de participación INTEZIA.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-005.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Definimos modalidad",
        "Paso01Body": (
            "Acordamos el formato (presencial u online), el calendario de las "
            "6 sesiones de 2.5 h y la sede si es presencial."
        ),
        "Paso02Titulo": "Formalización",
        "Paso02Body": (
            "Firmamos el contrato de servicio y coordinamos el arranque. "
            "El equipo de Intezia te acompaña en cada paso."
        ),
        "Paso03Titulo": "Kick-off con Consultor",
        "Paso03Body": (
            "Sesión de 30 min con Isaac Rodriguez para alinear los casos del "
            "aula a flujos reales de Cashea: correos, documentos y seguridad."
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

    print(f"Cashea CAP-005 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
