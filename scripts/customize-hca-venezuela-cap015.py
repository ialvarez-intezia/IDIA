#!/usr/bin/env python3
"""
Customizador de AcroForms para HCA Venezuela · Claude Cowork (CAP-015).

Tras la corrida del script canónico (generar-pdf.sh, que reinicia todos los
AcroForms), este script:

1. Pre-llena Entregables + Acreditacion (slide Beneficios) y los 6 campos de
   «Próximos pasos» con contenido real listo-para-entregar (§4.14 / §4.15).
2. Reposiciona (agranda) las cajas editables Programa y Notas — petición de
   ventas: más espacio para escribir sobre el programa y las notas sin tener
   que scrollear dentro del campo, y más separación entre ambas. El script
   canónico las crea con el rect estándar; aquí se reescribe su /Rect para
   matchear el CSS local (programa-box top=222 h=185 · notas-box top=467
   h=185). Conversión px→pt: factor 0.75, y_pt = 595 - y_css·0.75.

Programa, Notas y Cotización (apartado comercial) NO se pre-llenan de contenido:
HCA define precio y márgenes. Los campos quedan EDITABLES.

Uso (siempre inmediatamente después de generar-pdf.sh — par §10):
    python customize-hca-venezuela-cap015.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    BooleanObject,
    FloatObject,
    NameObject,
    TextStringObject,
)

# Títulos de «Próximos pasos» — cuerpo de letra a 14 pt para single-line.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"

# Cajas agrandadas y más separadas (solo esta propuesta). Rect (x1, y1, x2, y2) pt:
#   Programa: CSS top=222 h=185 → bottom 407  → (42, 290, 402, 429)
#   Notas:    CSS top=467 h=185 → bottom 652  → (42, 106, 402, 245)
RESIZE_RECTS = {
    "Programa": (42, 290, 402, 429),
    "Notas": (42, 106, 402, 245),
}


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-hca-venezuela-cap015.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — 3 institucionales (workbook, dashboard, certificado).
        "Entregables": "\r".join([
            "Workbook digital por participante.",
            "Dashboard de progreso individual.",
            "Certificado de participacion INTEZIA.",
        ]),
        # Acreditacion — 3 lineas estandar; [CODIGO] -> CAP-015.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-015.",
            "Cumple con el modelo Aprendizaje Basado en Retos (ABR).",
            "Material curado y revisado por el equipo academico.",
        ]),
        # Proximos pasos — logistica de arranque (§4.15: sin acuerdo/anticipo).
        "Paso01Titulo": "Confirmas fechas",
        "Paso01Body": (
            "Validamos las fechas de los 3 dias del sprint, la modalidad "
            "(presencial u online) y la zona horaria del equipo."
        ),
        "Paso02Titulo": "Acceso y logistica",
        "Paso02Body": (
            "Coordinamos accesos a Claude, la lista de participantes por "
            "area operativa y la agenda de las 3 sesiones."
        ),
        "Paso03Titulo": "Reunion de arranque",
        "Paso03Body": (
            "Reunion de ~30 minutos para alinear los casos reales de cada "
            "area que entraran a la practica del sprint."
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

    # Reposiciona (agranda) los rects de Programa y Notas — solo esta propuesta.
    for page in writer.pages:
        if "/Annots" not in page:
            continue
        for annot_ref in page["/Annots"]:
            obj = annot_ref.get_object()
            name = obj.get("/T")
            if name in RESIZE_RECTS:
                obj[NameObject("/Rect")] = ArrayObject(
                    [FloatObject(c) for c in RESIZE_RECTS[name]]
                )
                if NameObject("/AP") in obj:
                    del obj[NameObject("/AP")]

    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"HCA Venezuela CAP-015 — campos customizados + cajas agrandadas en {pdf_path.name}")


if __name__ == "__main__":
    main()
