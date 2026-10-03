#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Empresas Polar (CAP-011).

Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos con
contenido real listo-para-entregar, tras la corrida del script canónico de
AcroForms (generar-pdf.sh). Los campos quedan EDITABLES — solo se reescribe
/V y /DV; ventas ajusta en Adobe Reader si hace falta.

Los campos de precio (s-price) y el apartado comercial (Programa, Notas) se
dejan VACÍOS a propósito: los llena ventas.

Refleja el programa agéntico avanzado de 10 h (4 sesiones de 2.5 h, 8 módulos),
proyecto final = automatización de un flujo real con Antigravity.

Uso:
    python customize-empresas-polar.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-empresas-polar.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Agente funcional conectado al rol",
            "Flujo orquestado en Antigravity",
            "Piloto de automatización operativo",
            "Workbook y plantillas del programa",
            "Acompañamiento post-curso (30 días)",
            "Certificado de participación INTEZIA.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-011.",
            "Cumple con el modelo pedagógico oficial de Aprendizaje Basado en Retos.",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirman herramientas",
        "Paso01Body": (
            "Polar valida qué herramientas agénticas tiene habilitadas y "
            "gestiona los accesos a Gemini, NotebookLM y Antigravity."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Definimos los participantes del área de Control, la modalidad, "
            "el calendario de las 4 sesiones de 2.5 h y la agenda."
        ),
        "Paso03Titulo": "Kick-off técnico",
        "Paso03Body": (
            "Reunión técnica con Andres Fornerino para elegir los procesos "
            "reales que se automatizarán en el piloto con Antigravity."
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

    print(f"Empresas Polar CAP-011 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
