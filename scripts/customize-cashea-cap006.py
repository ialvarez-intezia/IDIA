#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Cashea CAP-006
(Cashea AI Adoption Stack).
Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos
con contenido real listo-para-entregar, tras la corrida del script canónico.

Los campos quedan EDITABLES: solo se reescribe /V y /DV.

Uso:
    python customize-cashea-cap006.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-cashea-cap006.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Nivelación de 1.000 colaboradores",
            "Masterclass para 50 directivos",
            "Mapa de Calor de oportunidades",
            "MaratonIA con branding Cashea",
            "Panel ejecutivo de avance",
            "Kit de prompts por rol",
            "Certificado de asistencia INTEZIA",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-006.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Alcance y fechas",
        "Paso01Body": (
            "Definimos el alcance, la modalidad y el calendario de las "
            "sesiones, más la zona horaria si es online."
        ),
        "Paso02Titulo": "Firmar el acuerdo",
        "Paso02Body": (
            "Firmamos el acuerdo con el 50% de anticipo y coordinamos el "
            "arranque. Intezia te acompaña en cada paso."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kickoff de unos 30 minutos para alinear casos reales por rol y "
            "preparar las cohortes y MaratonIA."
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

    print(f"Cashea CAP-006 · Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
