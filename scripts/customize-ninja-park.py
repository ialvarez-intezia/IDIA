#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Ninja Park Barquisimeto · TA-025
(Intezia Fundamentals · IA + Productividad para reportes y datos).

Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos con
contenido real listo-para-entregar, tras la corrida del script canónico de
AcroForms (generar-pdf.sh). Los campos quedan EDITABLES — solo se reescribe
/V y /DV; ventas ajusta en Adobe Reader si hace falta.

Los campos de precio (s-price) y las cajas Programa/Notas se dejan VACÍOS a
propósito: los llena ventas.

Uso:
    python customize-ninja-park.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-ninja-park.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables: 4 destacados del desglose instructivo (programa.md §5.2/§6)
        # + 3 institucionales (los 3 que pidió la ficha: workbook, informe de
        # desempeño, certificado). Cada línea de UN renglón para no desbordar la
        # caja (memoria project_entregables_lineas_cortas · ~8-9 líneas máx).
        "Entregables": "\r".join([
            "Plantilla de reporte mensual",
            "Asistente de reportes (Gem)",
            "Biblioteca de prompts",
            "Plan de adopción a 30 días",
            "Workbook digital",
            "Informe de desempeño",
            "Certificado INTEZIA",
        ]),
        # Acreditación: 3 líneas estándar. [CÓDIGO] → TA-025.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como TA-025.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos: logística pura (§4.15 — sin acuerdo económico).
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 3 sesiones del taller y la "
            "zona horaria."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos el acceso de los 4 participantes, los enlaces "
            "de las sesiones y la agenda."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de 30 minutos con Ninja Park para alinear los "
            "reportes y casos reales que entran al taller."
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

    print(f"Ninja Park TA-025 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
