#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de DAMASCO (CAP-037).

Pre-llena, tras la corrida del script canónico de AcroForms, los campos editables
de la Capacitación in-company «IA aplicada a la operación retail · Fase 1» con
contenido real listo-para-entregar:

- Entregables / Acreditacion (slide Beneficios)
- Paso0NTitulo / Paso0NBody   (slide Próximos pasos)

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el texto
en Adobe Reader si hace falta.

El apartado comercial / slide Propuesta Económica (Programa, Notas, PrecioBase,
Descuento, PrecioTotal) NO se toca: se deja vacío con los placeholders neutros del
script canónico para que ventas lo complete.

Uso:
    python customize-damasco.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-damasco.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Beneficios — destacados del desglose instructivo (programa.md §6) + institucionales.
        "Entregables": "\r".join([
            "Un proceso real automatizado",
            "Agente o flujo (Desarrollo)",
            "Asistente de soporte (Soporte)",
            "Workbooks digitales",
            "Informe de desempeño por área",
            "Certificado INTEZIA",
        ]),
        # Acreditacion — 3 líneas fijas; [CÓDIGO] → CAP-037.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-037.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos — 3 cards × (título single-line + body ≤130 chars). Sin acuerdo económico (§4.15).
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Acordamos las fechas de las 2 rutas y la disponibilidad de "
            "cada equipo."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos sala, participantes por departamento y accesos de "
            "prueba para las prácticas."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Sesión de 30 minutos con los líderes de área para elegir los "
            "procesos reales que entran a cada ruta."
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

    print(f"DAMASCO CAP-037 — AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
