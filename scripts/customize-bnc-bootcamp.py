#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta BNC CAP-001
(IA Bootcamp con Microsoft Copilot · Fase 2).

Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos con
contenido real listo-para-entregar, tras la corrida del script canónico de
AcroForms (generar-pdf.sh). Los campos quedan EDITABLES — solo se reescribe
/V y /DV; ventas ajusta en Adobe Reader si hace falta.

Los campos de precio (s-price) se dejan VACÍOS a propósito: los llena ventas.

Uso:
    python customize-bnc-bootcamp.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-bnc-bootcamp.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Workbook avanzado de protocolos",
            "Plantilla de prompt ejecutivo",
            "Copilot Agent propio del área",
            "Mapa de automatización del rol",
            "Medición Mentimeter + quiz final.",
            "Certificado de participación.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-001.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Participantes y fechas",
        "Paso01Body": (
            "El BNC define el grupo objetivo (tamaño y roles) y propone "
            "fechas para las dos sesiones del bootcamp."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Definimos la lista de participantes, los accesos a la "
            "plataforma y la agenda de sesiones."
        ),
        "Paso03Titulo": "Kick-off y curaduría",
        "Paso03Body": (
            "Reunión con el BNC para validar y anonimizar los casos y "
            "documentos que se usarán en las dos sesiones."
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

    print(f"BNC CAP-001 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
