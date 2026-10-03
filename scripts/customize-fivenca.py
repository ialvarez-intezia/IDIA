#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Fivenca · Plan Integral IA (CAP-039).
Pre-llena Entregables + Acreditacion (slide Beneficios) y los 6 campos de
«Próximos pasos» con contenido real listo-para-entregar, tras la corrida del
script canónico de AcroForms.

Apartado comercial (Programa, Notas, precio): NO se pre-llena, queda vacío para
que ventas lo escriba en Adobe Reader.

Los campos quedan EDITABLES: solo se reescribe /V y /DV.

Uso:
    python customize-fivenca.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

# Títulos de «Próximos pasos» a 14 pt para que el texto completo quepa.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-fivenca.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — destacados de la capacitación + institucionales fijos.
        "Entregables": "\r".join([
            "Biblioteca de prompts de Fivenca.",
            "Cheatsheet de prompting RCTF.",
            "Manual digital por participante.",
            "Panel de progreso individual.",
            "Certificado de participación INTEZIA.",
        ]),
        # Acreditacion — 3 líneas estándar; [CÓDIGO] → CAP-039.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-039.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Programa y Notas — apartado comercial: NO se pre-llenan.
        # Próximos pasos — logística, sin acuerdos económicos (§4.15).
        "Paso01Titulo": "Aprueban la capacitación",
        "Paso01Body": (
            "Confirmamos las fechas y la zona horaria, y definimos los 2 grupos "
            "de 20 colaboradores para las dos sesiones de Fundamentos."
        ),
        "Paso02Titulo": "Coordinamos acceso y logística",
        "Paso02Body": (
            "Coordinamos el acceso a las herramientas de IA (Claude, Gemini "
            "y Copilot), la lista de participantes y la agenda de las "
            "sesiones presenciales."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunion de unos 30 minutos con el equipo de Fivenca para alinear "
            "el enfoque y curar los primeros casos reales de productividad."
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

    print(f"Fivenca CAP-039 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
