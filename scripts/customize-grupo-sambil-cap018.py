#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Grupo Sambil · Marketing con
Claude · Sprint Ágil (CAP-018).

Formato ágil: 6 horas · 3 sesiones de 2 horas · enfoque 100% práctico
(Stack y Cowork · Brand Voice y Skills · Conectores y Plugins).

Pre-llena Entregables + Acreditacion (slide Beneficios) y los 6 campos de
«Próximos pasos» con contenido real listo-para-entregar, tras la corrida del
script canónico de AcroForms (agregar-campo-precio.py). Programa y Notas
(apartado comercial) NO se pre-llenan: quedan con los placeholders neutros
para que ventas escriba.

Los campos quedan EDITABLES — solo se reescribe /V y /DV.

Uso:
    python customize-grupo-sambil-cap018.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

# Títulos de «Próximos pasos» — cuerpo de letra reducido a 14 pt para que el
# texto completo quepa en el campo single-line.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-grupo-sambil-cap018.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — 2 destacados del Sprint (≤24 chars c/u → 1 línea visual)
        # + 3 institucionales fijos. Caja admite ~8-9 líneas a 10 pt.
        "Entregables": "\r".join([
            "Workspace de Marketing activo.",
            "Skill de Brand Voice Sambil.",
            "Kit de Artifacts y Conectores.",
            "Workbook digital por participante.",
            "Panel de progreso individual.",
            "Certificado de participación INTEZIA.",
        ]),
        # Acreditacion — 3 líneas fijas; [CÓDIGO] → CAP-018. Líneas 2-3 fijas.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-018.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Programa y Notas — apartado comercial: NO se pre-llenan.
        # Próximos pasos — patrón canónico: confirmar · firmar · arrancar.
        # Bodies ≤ 130 chars para que quepan en la caja sin clip (≈5 líneas).
        "Paso01Titulo": "Confirmar el programa",
        "Paso01Body": (
            "Alineamos alcance y objetivos con el equipo de Marketing Sambil. "
            "Confirmamos fechas, zona horaria y ubicación en la sede."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos accesos a Claude, participantes y la agenda de las sesiones. "
            "Sambil comparte materiales para preparar los casos prácticos."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de 30 minutos con Isaac para alinear los casos del equipo, "
            "confirmar acceso a Claude y fechas de las 3 sesiones."
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

    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(
        f"Grupo Sambil CAP-018 — Entregables + Acreditación + "
        f"Próximos pasos customizados en {pdf_path.name}"
    )


if __name__ == "__main__":
    main()
