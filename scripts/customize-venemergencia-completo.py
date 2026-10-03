#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Venemergencia · DECK B · Adopción de
Claude · Fases 1 + 2 (CAP-047 · Fases 1+2).

Igual que customize-venemergencia.py (Deck A · solo Fase 1), pero los Entregables
suman los de la Fase 2 (clon digital con Claude Code) y los Próximos pasos cubren
las dos fases (11 sesiones).

Apartado comercial (Programa, Notas, precio): NO se pre-llena, queda vacío para
que ventas lo escriba en Adobe Reader.

Los campos quedan EDITABLES: solo se reescribe /V y /DV.

Uso:
    python customize-venemergencia-completo.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

# Títulos de «Próximos pasos» a 14 pt para que el texto completo quepa.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-venemergencia-completo.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        # Entregables — Fase 1 (Skill + proceso automatizado) + Fase 2 (clon
        # digital + agente conectado) + institucionales fijos.
        "Entregables": "\r".join([
            "Skill funcional propia.",
            "Proceso automatizado real.",
            "Clon digital en Claude Code.",
            "Agente conectado a tus apps.",
            "Workbook digital.",
            "Certificado INTEZIA.",
        ]),
        # Acreditacion — 3 líneas estándar; [CÓDIGO] → CAP-047.
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-047.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        # Programa y Notas — apartado comercial: NO se pre-llenan.
        # Próximos pasos — logística, sin acuerdos económicos (§4.15). Cubren las 2 fases.
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 11 sesiones de las dos fases, la "
            "modalidad y la zona horaria con Venemergencia."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos el acceso a las cuentas, los participantes de la "
            "cohorte gerencial y la agenda de las sesiones."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Reunión de unos 30 minutos para alinear los casos y las decisiones "
            "reales de cada líder que entrarán a la formación."
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

    print(f"Venemergencia CAP-047 Fases 1+2 (Deck B) — Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
