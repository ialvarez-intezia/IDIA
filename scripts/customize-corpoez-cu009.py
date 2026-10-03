#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Corpoez · CU-009
(Inteligencia Artificial para Líderes · IESA In Company).

Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos con
contenido real listo-para-entregar, tras la corrida del script canónico de
AcroForms (generar-pdf.sh). Los campos quedan EDITABLES — solo se reescribe
/V y /DV; ventas ajusta en Adobe Reader si hace falta.

Los campos de precio (s-price) y las cajas Programa/Notas se dejan VACÍOS a
propósito: los llena ventas.

Uso:
    python customize-corpoez-cu009.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-corpoez-cu009.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables: 4 destacados del desglose instructivo (programa.md §6)
        # + 3 institucionales. Líneas cortas de un renglón (memoria).
        "Entregables": "\r".join([
            "Biblioteca de prompts del líder",
            "Asistente IA configurado",
            "Sparring Project + roadmap 90 días",
            "Borrador de uso aceptable de IA",
            "Workbook digital por persona",
            "Panel de progreso individual",
            "Certificado INTEZIA + IESA",
        ]),
        # Acreditación: doble certificación INTEZIA + IESA. [CÓDIGO] → CU-009.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CU-009.",
            "Doble certificación INTEZIA Education + IESA.",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos: logística pura (§4.15 — sin acuerdo económico).
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 3 sesiones entre el 13 y el "
            "27 de junio, la zona horaria y la sede presencial."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos la lista de los 14 participantes, los accesos a "
            "Claude y Gemini y la agenda de las sesiones."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de 30 minutos con Corpoez para alinear los casos "
            "reales de cada área que entrarán al curso."
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

    print(f"Corpoez CU-009 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
