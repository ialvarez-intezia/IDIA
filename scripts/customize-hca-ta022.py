#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta HCA · Executive AI Mastery (TA-022).

Pre-llena Entregables + Acreditacion (slide Beneficios) y los 6 campos de
«Próximos pasos» con contenido real listo-para-entregar, tras la corrida del
script canónico de AcroForms. Programa, Notas y Cotización (apartado
comercial) NO se pre-llenan: HCA define precio y márgenes en su esquema.

Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-hca-ta022.py <pdf>
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

# Cajas Programa y Notas agrandadas a petición de ventas (solo HCA): más alto
# para escribir más, misma fuente 11 pt. El script canónico las crea con el
# rect estándar; aquí se reescribe /Rect para matchear el CSS local de HCA
# (programa-box top=222 h=160 · notas-box top=432 h=160). Conversión px→pt:
# factor 0.75, y_pt = 595 - y_css·0.75. Al cambiar el rect se borra /AP para
# que el visor regenere la apariencia al nuevo tamaño (NeedAppearances=True).
RESIZE_RECTS = {
    "Programa": (42, 308, 402, 429),   # top=222 h=160 → bottom css 382
    "Notas": (42, 151, 402, 271),      # top=432 h=160 → bottom css 592
}


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-hca-ta022.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — 4 destacados ejecutivos + 3 institucionales (workbook, dashboard, certificado).
        # Lineas cortas para que la caja no se desborde (memoria project_entregables_lineas_cortas).
        "Entregables": "\r".join([
            "Sparring Project ejecutivo.",
            "Reporte para directorio.",
            "Politica de Uso Aceptable (AUP).",
            "Roadmap 90 dias con metricas.",
            "Workbook ejecutivo digital.",
            "Dashboard individual.",
            "Certificado INTEZIA.",
        ]),
        # Acreditacion — 3 lineas estandar; [CODIGO] -> TA-022. Lineas 2-3 fijas.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como TA-022.",
            "Cumple con el modelo Aprendizaje Basado en Retos (ABR).",
            "Material curado y revisado por el equipo academico.",
        ]),
        # Programa, Notas y Cotizacion — apartado comercial: NO se pre-llenan.
        # Proximos pasos — 3 cards x (titulo single-line + body multiline).
        "Paso01Titulo": "Reservan su cupo",
        "Paso01Body": (
            "El directivo confirma su cupo a traves de HCA, recibe la "
            "fecha del cohort mensual asignado, la zona horaria y el "
            "instructivo de alta de Claude Pro o Max."
        ),
        "Paso02Titulo": "Pre-sesion ejecutiva",
        "Paso02Body": (
            "Cada participante envia un caso real anonimizado del comite "
            "(pricing, expansion, talento o reestructuracion) para "
            "trabajarlo en el sparring de la sesion 1."
        ),
        "Paso03Titulo": "Sprint de 8 horas",
        "Paso03Body": (
            "2 sesiones online sincronas (4 h + 4 h) en una semana. Al "
            "cierre cada directivo se lleva su Sparring Project, su "
            "reporte ejecutivo, su Politica de Uso Aceptable (AUP) "
            "firmada y su roadmap 90 dias."
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

    # Reposiciona (agranda) los rects de Programa y Notas — solo HCA.
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

    print(f"HCA TA-022 — Entregables + Acreditacion + Proximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
