#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Tealca · IA para Líderes:
Productividad, Visión y Estrategia (CAP-038).

Capacitación in-company mono-fase · 6 horas · 2 bloques de 3h · presencial ·
líderes y mandos medios · entorno Google (Gemini + Gems).

Pre-llena Entregables + Acreditacion (slide Beneficios) y los 6 campos de
«Próximos pasos» con contenido real listo-para-entregar, tras la corrida del
script canónico de AcroForms. Programa, Notas y precio (apartado comercial) NO
se pre-llenan: quedan vacíos para que ventas cargue las dos cotizaciones (25 y
60 personas).

Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-tealca.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

# Títulos de «Próximos pasos» — cuerpo de letra reducido a 14 pt para que el
# texto completo quepa en el campo single-line.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-tealca.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — destacados del desglose §5.2 + 3 institucionales.
        # Líneas cortas de un renglón (la caja rinde ~8-9 líneas visuales).
        "Entregables": "\r".join([
            "Estrategia de IA por área.",
            "Un Gem personalizado operando.",
            "Biblioteca de prompts (entorno Google).",
            "Workbook digital por participante.",
            "Informe de desempeño individual.",
            "Certificado de participación INTEZIA.",
        ]),
        # Acreditacion — 3 líneas estándar; [CÓDIGO] → CAP-038. Líneas 2-3 fijas.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-038.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Programa y Notas — apartado comercial: NO se pre-llenan.
        # Próximos pasos — logística, sin acuerdos económicos (§4.15).
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Acordamos la fecha de inicio, la zona horaria y el calendario de "
            "los 2 bloques presenciales de 3 horas."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos la sala, los participantes (líderes y mandos medios) y "
            "la agenda, con 3 a 5 casos reales por área."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de unos 30 minutos con Douglas y el referente de Tealca "
            "para alinear los casos reales y los Gems que cada líder construirá."
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

    print(f"Tealca CAP-038 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
