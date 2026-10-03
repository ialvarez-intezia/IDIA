#!/usr/bin/env python3
"""
Customizador de AcroForms — SFIC · Diplomado en Comunicación, IA y Marketing
Exponencial (DIP-007). Pre-llena Entregables, Acreditación y los 6 campos de
«Próximos pasos» con contenido real listo-para-entregar, tras la corrida del
script canónico de AcroForms (agregar-campo-precio.py vía generar-pdf.sh).

Apartado comercial (Programa · Notas · PrecioBase · Descuento · PrecioTotal):
SE DEJA VACÍO a propósito (decisión del usuario 2026-05-27). Ventas lo llena en
Adobe Reader. Referencia interna: 800 USD/participante, reparto 50% SFIC / 50%
Intezia (ver brief.md).

Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python3 customize-sfic-comunicacion-marketing.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-sfic-comunicacion-marketing.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    # Entregables — 4 destacados del desglose instructivo (programa.md §5.2) +
    # 3 institucionales. Líneas cortas de un renglón (caja ~8-9 líneas máx).
    # Acreditacion — 3 líneas estandarizadas; [CÓDIGO] → DIP-007.
    # Pasos — logística del arranque, sin acuerdo económico (§4.15);
    #   paso 02 = «Acceso y logística». Bodies ≤ ~130 chars.
    updates = {
        "Entregables": "\r".join([
            "Manual de Voz de Marca con IA",
            "Asistente Creativo + 3 avatares",
            "Spot de 15 s + campaña Meta Ads",
            "Roadmap con ROI + Campaña 360°",
            "Manual digital por participante.",
            "Panel de progreso individual.",
            "Certificado doble aval INTEZIA + SFIC.",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como DIP-007.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmamos alianza",
        "Paso01Body": (
            "Alineamos con SFIC el modelo de doble certificación, las "
            "fechas del cohort y la distribución de las 40 horas online."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos acceso a la plataforma, participantes (30 a 40), "
            "agenda de sesiones y la convocatoria del primer grupo."
        ),
        "Paso03Titulo": "Kick-off del cohort",
        "Paso03Body": (
            "Apertura con la dirección académica de SFIC, los instructores "
            "designados y el primer grupo. Entrega del workbook digital."
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

    # Re-hornea la apariencia en negrita de Entregables / Acreditación.
    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"SFIC Comunicación/Marketing — Entregables + Acreditación + Pasos customizados en {pdf_path.name}")
    print("  (Apartado comercial intencionalmente VACÍO — lo llena ventas.)")


if __name__ == "__main__":
    main()
