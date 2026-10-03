#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de Simple TV (CAP-035).

Pre-llena, tras la corrida del script canónico de AcroForms, los campos editables
de la propuesta «Fundamentos de IA · Nivelación corporativa (Fase 1)» con contenido
real listo-para-entregar:

- Entregables / Acreditacion (slide Beneficios)
- Paso0NTitulo / Paso0NBody   (slide Próximos pasos)

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el texto
en Adobe Reader si hace falta.

El apartado comercial / slide Propuesta Económica (Programa, Notas, PrecioBase,
Descuento, PrecioTotal) NO se toca: se deja con los placeholders neutros del
script canónico para que ventas lo complete sin confundir texto demo con final.

Uso:
    python customize-simple-tv.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-simple-tv.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Beneficios — destacados de la Fase 1 + institucionales (brief §Entregables).
        "Entregables": "\r".join([
            "Workbook digital con ejemplos de prompts.",
            "Informe de desempeño por cohorte.",
            "Dashboard de resultados de impacto.",
            "Panel de progreso individual.",
            "Certificado de participación INTEZIA.",
        ]),
        # Acreditacion — 3 líneas fijas; [CÓDIGO] → CAP-035.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-035.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos — 3 cards × (título single-line + body ≤130 chars).
        # Solo logística, sin acuerdos económicos (§4.15).
        "Paso01Titulo": "Fechas y cohortes",
        "Paso01Body": (
            "Coordinamos el calendario de junio o julio, la zona horaria y la "
            "conformación de las cohortes mixtas (presencial y online)."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos accesos, la lista de participantes por cohorte y la "
            "agenda de las 4 sesiones de la nivelación."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Sesión breve para alinear los casos reales de Simple que se "
            "trabajarán en cada sesión y resolver dudas del Comité de IA."
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

    # Re-hornea la apariencia en negrita de Entregables y Acreditación.
    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"Simple TV — AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
