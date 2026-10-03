#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta de catálogo TA-023
(IA para Emprendedores · De la Idea al MVP · División Fundación).

Pre-llena tras la corrida de agregar-campo-precio.py:
  - Entregables (8 líneas cortas — destacados del journey + institucionales)
  - Acreditacion (3 líneas estandarizadas; [CÓDIGO] = TA-023)
  - 3 pasos × título + body de "Cómo arrancamos" (catálogo Fundación)

Los campos quedan EDITABLES — solo se reescribe /V y /DV. Sigue siendo
ajustable por ventas en Adobe Reader.

Uso:
    python customize-ta-023.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-ta-023.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    # Entregables: 4 destacados del journey (uno por sesión / hito) + 3
    # institucionales. Líneas cortas de un renglón (memoria
    # project_entregables_lineas_cortas: ~8-9 líneas visuales máx).
    # Orden: del entregable más concreto al más institucional.
    entregables = "\r".join([
        "Canvas de propuesta de valor validado",
        "Mini brand-book con identidad por IA",
        "Landing page funcional publicada",
        "Calendario de contenido 30 días",
        "Asistente IA configurado y probado",
        "Workbook digital del emprendedor",
        "Dashboard de progreso del participante",
        "Certificado de participación INTEZIA",
    ])

    # Acreditación: 3 líneas estándar; [CÓDIGO] → TA-023.
    acreditacion = "\r".join([
        "Programa registrado en INTEZIA Fundación como TA-023.",
        "Cumple con el modelo pedagógico oficial (ABR).",
        "Material curado y revisado por el equipo académico.",
    ])

    # Próximos pasos: 3 pasos × (título corto + descripción adaptada al
    # producto de catálogo Fundación · emprendedores).
    updates = {
        "Entregables": entregables,
        "Acreditacion": acreditacion,
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 4 sesiones del taller "
            "y la zona horaria del grupo de emprendedores."
        ),
        "Paso02Titulo": "Firmamos acuerdo",
        "Paso02Body": (
            "Acuerdo simple + factura del 50 % de anticipo para "
            "reservar al facilitador y la logística."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de 30 minutos para alinear los perfiles de los "
            "emprendedores y las ideas que entrarán al taller."
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
