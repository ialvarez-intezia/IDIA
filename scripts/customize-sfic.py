#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta SFIC × Intezia (DIP-006)
(Diplomado para Aumentar la Productividad del Negocio).

Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos con
contenido listo-para-entregar. Los campos económicos (PrecioBase, PrecioTotal,
Programa, Notas) se dejan VACÍOS a propósito: los llena ventas en Adobe Reader.
Los campos quedan EDITABLES (solo /V y /DV).

Uso:
    python customize-sfic.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-sfic.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Roadmap de Transformación con IA (proyecto final)",
            "Librería de Blueprints de Automatización",
            "Manual de Prompts Executive 2026",
            "Asistentes propios (GPTs, Gems, NotebookLM)",
            "Manual digital por participante.",
            "Certificado: doble aval SFIC + INTEZIA.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como DIP-006.",
            "Doble certificación: SFIC + INTEZIA.",
            "Cumple con el modelo pedagógico oficial (ABR).",
        ]),
        # Económico (PrecioBase, PrecioTotal, Programa, Notas): VACÍO a
        # propósito. Lo llena ventas en Adobe Reader (decisión del director).
        # Próximos pasos
        "Paso01Titulo": "Fechas y cohorte",
        "Paso01Body": (
            "Definimos la fecha de inicio, el calendario de sesiones online "
            "y el grupo de participantes de la cohorte."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Habilitamos acceso a la plataforma, participantes y agenda de "
            "sesiones junto al equipo de SFIC."
        ),
        "Paso03Titulo": "Kick-off",
        "Paso03Body": (
            "Reunión breve con el equipo INTEZIA para personalizar casos y "
            "ejemplos al negocio de los participantes."
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

    print(f"SFIC DIP-006 — AcroForms (entregables, acreditación, económico, pasos) customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
