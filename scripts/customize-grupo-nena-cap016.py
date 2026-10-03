#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Grupo Nena · Equipo Aumentado con
Google AI (CAP-016) · 4 módulos (I, II, III y IV-A/IV-B).

Deck: I-III núcleo común a los 40 · IV diferenciado por grupo (IV-A sin código
con Douglas para Grupo A · IV-B Apps Script con Rafael Carreño para Grupo B).
El cliente pidió retirar el módulo de Ética y Gobernanza de IA, así que la
capacitación cierra en el Módulo IV (automatización).

Pre-llena Entregables + Acreditacion (slide Beneficios) y los 6 campos de
«Próximos pasos». Programa y Notas (apartado comercial) NO se pre-llenan.
Campos EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-grupo-nena-cap016.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-grupo-nena-cap016.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — destacados de los 4 módulos + institucionales.
        "Entregables": "\r".join([
            "5 Gems sectoriales por área.",
            "Automatizaciones con y sin código según grupo.",
            "Workbook digital por participante.",
            "Informe de desempeño individual.",
            "Certificado de participación INTEZIA.",
        ]),
        # Acreditacion — 3 líneas estándar; [CÓDIGO] → CAP-016.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-016.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos — logística, sin acuerdos económicos (§4.15).
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Acordamos la fecha de inicio, la zona horaria y el calendario: "
            "4 sesiones por participante en 5 semanas (solo el Módulo IV se "
            "dicta dos veces, una por grupo)."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos accesos al Workspace, los participantes de las 5 áreas "
            "dentro de los 40 y la agenda, con 3-5 tareas reales por área."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de unos 45 minutos con Douglas, Rafael Carreño y el "
            "referente del cliente para alinear los casos reales por área y "
            "la composición de los Grupos A y B."
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
                    if name in TITLE_FIELDS:
                        obj[NameObject("/DA")] = TextStringObject(TITLE_DA)
                        if NameObject("/AP") in obj:
                            del obj[NameObject("/AP")]

    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"Grupo Nena CAP-016 (4 módulos, IV-A/IV-B) — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
