#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de Sura Venezuela (CAP-031).

Pre-llena, tras la corrida del script canónico de AcroForms, los campos
editables de la propuesta «Visión, Estrategia y Diagnóstico de Inteligencia
Artificial para la Alta Gerencia» con contenido real listo-para-entregar:

- Entregables / Acreditacion (slide Beneficios)
- Paso0NTitulo / Paso0NBody   (slide Próximos pasos)

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el
texto en Adobe Reader si hace falta.

Notas de redacción para esta propuesta:
- Sin acrónimos sin justificación previa (directriz del cliente, 2026-05-20).
  «Aprendizaje Basado en Retos» se escribe completo en la línea de
  acreditación. «IA» se usa solo donde «Inteligencia Artificial» ya quedó
  definida en la misma slide del deck.
- Tono neutro: la recomendación de ecosistema de IA se entrega como
  resultado del diagnóstico — no se afirma que Sura cambie de stack
  (CLAUDE.md §4.11).

El apartado comercial / slide Propuesta Económica (Programa, Notas,
PrecioBase, Descuento, PrecioTotal) NO se toca: se deja con los
placeholders neutros del script canónico para que ventas lo complete.

Uso:
    python customize-sura-venezuela.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-sura-venezuela.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Beneficios — destacados de la Fase 1 + institucionales.
        # ≤ 9 líneas visuales; cada línea cabe en un renglón de la caja.
        "Entregables": "\r".join([
            "Roadmap priorizado de adopción de IA.",
            "Recomendación de ecosistema de IA.",
            "Informe de diagnóstico por área.",
            "Workbook digital por participante.",
            "Constancia de participación Intezia.",
        ]),
        # Acreditacion — 3 líneas estandarizadas; [CÓDIGO] → CAP-031.
        # «ABR» se expande a «Aprendizaje Basado en Retos» (directriz 2026-05-20).
        "Acreditacion": "\r".join([
            "Programa registrado en Intezia Education como CAP-031.",
            "Cumple con el modelo pedagógico Aprendizaje Basado en Retos.",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Próximos pasos — 3 cards × (título single-line + body multiline).
        # Bodies ≤ ~130 chars (memoria project_pasos_body_max_chars).
        "Paso01Titulo": "Aprueban la Fase 1",
        "Paso01Body": (
            "Validan la cotización. Flavia Martínez coordina las 2 sesiones "
            "e Intezia prepara el guion de diagnóstico y los casos del sector."
        ),
        "Paso02Titulo": "Sesiones con los líderes",
        "Paso02Body": (
            "Douglas Vasquez conduce las 2 sesiones de visión, estrategia y "
            "diagnóstico con los 8 líderes, sobre procesos y tareas reales."
        ),
        "Paso03Titulo": "Roadmap y Fase 2",
        "Paso03Body": (
            "Intezia entrega el roadmap priorizado. Sobre esa base se propone "
            "la Fase 2 (aplicación de IA) con alcance y herramientas a medida."
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

    print(f"Sura Venezuela CAP-031 — AcroForms customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
