#!/usr/bin/env python3
"""
Customizador de AcroForms para la capacitación interna Claude para Ventas
(CAP-INT-01). Pre-llena Entregables, Acreditacion y los 6 campos de Próximos
pasos con contenido real listo-para-entregar, tras la corrida del script canónico.

Esta capacitación NO lleva slide de precio: solo 8 campos no-precio.
Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-intezia-ventas-claude.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-intezia-ventas-claude.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Plantilla de prompt RCTF",
            "Biblioteca de prompts de ventas",
            "Proyecto de ventas configurado",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-INT-01.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmamos fecha",
        "Paso01Body": (
            "Validamos la fecha y hora de la sesión de 2 h con el "
            "equipo comercial."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos sala y proyector, y que cada quien llegue con su "
            "cuenta de Claude.ai lista."
        ),
        "Paso03Titulo": "Casos reales",
        "Paso03Body": (
            "Cada asesora trae un prospecto y un seguimiento reales para "
            "trabajarlos en vivo en el hands-on."
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

    print(f"Claude para Ventas CAP-INT-01 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
