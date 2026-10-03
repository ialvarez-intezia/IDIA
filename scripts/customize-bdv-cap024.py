#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta BDV · Plan Integral IA (CAP-024).
Pre-llena Entregables + Acreditacion (slide Beneficios), Programa + Notas
(slide Propuesta Económica) y los 6 campos de «Próximos pasos» con contenido
real listo-para-entregar, tras la corrida del script canónico de AcroForms.

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el
texto en Adobe Reader si hace falta.

Uso:
    python customize-bdv-cap024.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

# Títulos de «Próximos pasos» — se les reduce el cuerpo de letra para que el
# texto completo quepa en el campo single-line (a 18 pt los títulos largos se
# recortaban al abrir el PDF). 14 pt entra holgado en el ancho del campo.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-bdv-cap024.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — 3 destacados del desglose + 3 institucionales fijos.
        # Líneas cortas (una sola línea cada una) para que no desborden la caja.
        "Entregables": "\r".join([
            "Biblioteca de prompts del BDV.",
            "Política de Uso Aceptable (AUP) firmable.",
            "8 proyectos finales por área.",
            "Manual digital por participante.",
            "Panel de progreso individual.",
            "Certificado de participación INTEZIA.",
        ]),
        # Acreditacion — 3 líneas estándar; [CÓDIGO] → CAP-024. Líneas 2-3 fijas.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-024.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Programa y Notas — apartado comercial: NO se pre-llenan. Quedan con los
        # placeholders neutros entre corchetes del script canónico para que el
        # equipo de ventas escriba el contenido sin confundirse con texto pre-hecho.
        # Próximos pasos — 3 cards × (título single-line + body multiline).
        "Paso01Titulo": "Aprueban el plan CAP-024",
        "Paso01Body": (
            "Maria Iribarren coordina con el comite del BDV el cronograma macro "
            "de 6 meses, se confirman las 8 areas con el sponsor y se solicita "
            "acceso a Workspace + Gemini para el primer cohort de 100 colaboradores."
        ),
        "Paso02Titulo": "Firma y anticipo del 50 %",
        "Paso02Body": (
            "Se firma el acuerdo del plan integral y se emite la factura del 50% "
            "de anticipo aplicado a Fase 1. INTEZIA designa al consultor lider y "
            "lanza el cuestionario de levantamiento por area."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunion de ~30 minutos con el sponsor ejecutivo del BDV para alinear "
            "el cronograma, confirmar los sponsors por area y definir los primeros "
            "cohorts de Fase 1."
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
                        # Cuerpo de letra más pequeño + se descarta el /AP
                        # horneado para que el lector lo regenere a 14 pt.
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

    print(f"BDV CAP-024 — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
