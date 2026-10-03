#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta ESTEI CAP-044
(Claude, de los Fundamentos al Co-working).

Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos con
contenido real listo-para-entregar, tras la corrida del script canónico de
AcroForms (generar-pdf.sh). Los campos quedan EDITABLES — solo se reescribe
/V y /DV; ventas ajusta en Adobe Reader si hace falta.

Los campos de precio (s-price) se dejan VACÍOS a propósito: los llena ventas.

Uso:
    python customize-estei.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-estei.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Biblioteca de prompts del rol (RCTF)",
            "Primer asistente personal (Project)",
            "Workspace Cowork del equipo",
            "Plan de adopcion a 30 dias",
            "Politica de Uso Aceptable (AUP)",
            "Certificado de participacion.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-044.",
            "Cumple con el modelo pedagogico oficial (ABR).",
            "Material curado y revisado por el equipo academico.",
        ]),
        "Paso01Titulo": "Participantes y fechas",
        "Paso01Body": (
            "ESTEI define el grupo de 20 colaboradores y proponemos "
            "fechas para las 5 sesiones del taller."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos accesos a Claude, la lista de participantes "
            "y la agenda de las sesiones."
        ),
        "Paso03Titulo": "Kick-off y curaduría",
        "Paso03Body": (
            "Reunión de 30 minutos con ESTEI para alinear los casos "
            "reales que entran al taller."
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

    print(f"ESTEI CAP-044 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
