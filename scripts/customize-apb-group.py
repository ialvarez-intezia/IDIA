#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta APB Group (CAP-033).
Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos.
Sin campos de precio: la slide de Propuesta Económica no existe (es un regalo).
Los campos quedan EDITABLES (solo se reescribe /V y /DV).

Uso:
    python customize-apb-group.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-apb-group.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Gema de cargo y vacante",
            "Gema de screening de CVs",
            "Gema de entrevistas",
            "Kit de bienvenida y manual",
            "Gema de pruebas por cargo",
            "Banco de pruebas por área",
            "Certificado de asistencia",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-033.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 3 sesiones de 2 horas y la "
            "zona horaria si es online."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos el acceso de los participantes, la agenda de las "
            "sesiones y el entorno presencial u online."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kickoff de unos 30 minutos para alinear los casos reales de "
            "RRHH que entrarán a la práctica."
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

    print(f"APB Group CAP-033 · Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
