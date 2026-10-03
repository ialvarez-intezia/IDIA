#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de Inversiones Romitec (CAP-034).

Pre-llena, tras la corrida del script canónico de AcroForms, los campos editables
de la Capacitación «Automatización de Tesorería con Claude» con contenido real
listo-para-entregar:

- Entregables / Acreditacion (slide Beneficios)
- Paso0NTitulo / Paso0NBody   (slide Próximos pasos)

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el texto
en Adobe Reader si hace falta.

El apartado comercial / slide Propuesta Económica (Programa, Notas, PrecioBase,
Descuento, PrecioTotal) NO se toca: se deja vacío con los placeholders neutros del
script canónico para que ventas lo complete (requiere aprobación de junta directiva).

Uso:
    python customize-inversiones-romitec.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-inversiones-romitec.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Beneficios — destacados del desglose instructivo + institucionales (brief §Entregables).
        "Entregables": "\r".join([
            "Biblioteca de prompts de tesorería",
            "Flujo de trabajo en Cowork",
            "Skill propia (conciliación o cierre)",
            "Proceso estandarizado y documentado",
            "Workbooks digitales",
            "Informes de desempeño",
            "Certificado de asistencia INTEZIA",
        ]),
        # Acreditacion — 3 líneas fijas; [CÓDIGO] → CAP-034.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-034.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos — 3 cards × (título single-line + body ≤130 chars).
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 7 sesiones (16 horas) y el "
            "calendario presencial en Caracas con el equipo de tesorería."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos el acceso de los participantes, la agenda de las "
            "sesiones y la sala presencial."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kickoff de unos 30 minutos para alinear los casos reales de "
            "tesorería que entrarán a la práctica."
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

    print(f"Inversiones Romitec CAP-034 — AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
