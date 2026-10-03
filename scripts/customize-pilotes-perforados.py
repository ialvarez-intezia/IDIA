#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de Pilotes Perforados C.A. (CAP-021).

Pre-llena, tras la corrida del script canónico de AcroForms, los campos editables
de la propuesta «Diagnóstico de Digitalización Operativa con IA» con contenido
real listo-para-entregar:

- Entregables / Acreditacion (slide Beneficios)
- Paso0NTitulo / Paso0NBody   (slide Próximos pasos)

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el texto
en Adobe Reader si hace falta.

El apartado comercial / slide Propuesta Económica (Programa, Notas, PrecioBase,
Descuento, PrecioTotal) NO se toca: se deja con los placeholders neutros del
script canónico para que ventas lo complete sin confundir texto demo con final.

Uso:
    python customize-pilotes-perforados.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-pilotes-perforados.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Beneficios — destacados del diagnóstico + institucionales (brief §Entregables).
        "Entregables": "\r".join([
            "Mapa de Calor de oportunidades de IA.",
            "Informe de diagnóstico de procesos.",
            "Recomendación de ecosistema de IA.",
            "Plan de acción por fases.",
            "Workbook digital y constancia INTEZIA.",
        ]),
        # Acreditacion — 3 líneas fijas; [CÓDIGO] → CAP-021.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-021.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos — 3 cards × (título single-line + body ≤130 chars).
        "Paso01Titulo": "Confirmar la Fase 1",
        "Paso01Body": (
            "Validen la cotización. Flavia coordina las 2 sesiones con los "
            "líderes de área e Intezia prepara el guion de auditoría."
        ),
        "Paso02Titulo": "Sesiones de diagnóstico",
        "Paso02Body": (
            "Douglas Vasquez conduce las 2 sesiones con los líderes de "
            "Procura, CxP, Finanzas y Licitaciones, sobre sus procesos reales."
        ),
        "Paso03Titulo": "Mapa de Calor y plan",
        "Paso03Body": (
            "Intezia entrega el Mapa de Calor, el informe y el plan por fases. "
            "La Fase 2 (aplicación de IA) se cotiza aparte."
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

    print(f"Pilotes Perforados — AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
