#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de catálogo TA-005
(Marketing Estratégico y Generativo · División Educación).

Pre-llena tras la corrida de agregar-campo-precio.py:
  - Entregables (7 líneas cortas: 4 destacados del programa + 3 institucionales)
  - Acreditacion (3 líneas estandarizadas; [CÓDIGO] = TA-005)
  - 3 pasos × título + body de "Cómo arrancamos"

Los campos quedan EDITABLES — solo se reescribe /V y /DV. Sigue siendo
ajustable por ventas en Adobe Reader.

Uso:
    python customize-ta005-marketing.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-ta005-marketing.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    # Entregables: 4 destacados por módulo + 3 institucionales.
    # Líneas cortas de un renglón (memory project_entregables_lineas_cortas).
    entregables = "\r".join([
        "Mapa de audiencia generado con IA",
        "Calendario editorial de 30 días",
        "Banco de copies listos para publicar",
        "Set de creatividades adaptadas por canal",
        "Workbook digital del participante",
        "Acceso a la grabación de las sesiones",
        "Certificado de participación INTEZIA",
    ])

    # Acreditación: 3 líneas estándar; [CÓDIGO] → TA-005.
    acreditacion = "\r".join([
        "Programa registrado en INTEZIA Educación como TA-005.",
        "Cumple con el modelo pedagógico oficial (ABR).",
        "Material curado y revisado por el equipo académico.",
    ])

    # Próximos pasos: bodies ≤ 130 chars (memory project_pasos_body_max_chars).
    updates = {
        "Entregables": entregables,
        "Acreditacion": acreditacion,
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 2 sesiones del taller "
            "y la zona horaria del equipo de marketing."
        ),
        "Paso02Titulo": "Firmamos acuerdo",
        "Paso02Body": (
            "Acuerdo de servicio más factura del 50 % de anticipo "
            "para reservar al facilitador y la logística."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Sesión de 30 minutos con Juan para alinear los casos "
            "reales de marketing de la empresa que entrarán al taller."
        ),
    }

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    summary = []
    for name, value in updates.items():
        updated = 0
        for page in writer.pages:
            if "/Annots" not in page:
                continue
            for annot_ref in page["/Annots"]:
                obj = annot_ref.get_object()
                if obj.get("/T") == name:
                    obj[NameObject("/V")] = TextStringObject(value)
                    obj[NameObject("/DV")] = TextStringObject(value)
                    updated += 1
        summary.append(f"  {name}: {updated} campo(s)")

    # /NeedAppearances=True para regenerar apariencias con nuevo /V.
    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    # Re-hornea negrita en Entregables / Acreditación.
    baked = rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"AcroForms personalizados en {pdf_path.name}:")
    for line in summary:
        print(line)
    print(f"  Apariencia en negrita re-horneada: {baked} campo(s).")


if __name__ == "__main__":
    main()
