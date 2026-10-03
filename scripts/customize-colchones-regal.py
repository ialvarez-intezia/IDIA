#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta Colchones Regal · CAP-043.
Propuesta de DOS FASES (Marketing 8 h + Desarrollo 10 h), con COTIZACIÓN ÚNICA.

Pre-llena, tras la corrida del script canónico de AcroForms:
  - Entregables (de ambas fases) + Acreditacion (slide Beneficios).
  - Los 6 campos de «Próximos pasos» con contenido listo-para-entregar.
(Estos campos los CREA el script compartido agregar-campo-precio.py; aquí solo
se reescribe /V y /DV. Siguen editables.)

Apartado comercial (PrecioBase, Descuento, PrecioTotal, Programa, Notas): NO se
pre-llena. La slide 20 es la canónica s-price (cotización única de ambas fases) y
sus 5 campos los crea el script compartido al detectar el marker "Propuesta
Económica"; ventas los llena en Adobe Reader.

Uso:
    python3 customize-colchones-regal.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

# Títulos de «Próximos pasos» a 14 pt para que el texto completo quepa.
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"

# ---------------------------------------------------------------------------
# Valores pre-llenados de los campos existentes (Beneficios + Pasos).
# ---------------------------------------------------------------------------
UPDATES = {
    # Entregables — destacados de AMBAS fases + institucionales fijos. (<=8-9 líneas)
    "Entregables": "\r".join([
        "Kit de contenido con IA (Fase 1).",
        "Bot de Instagram en producción (Fase 1).",
        "Agente omnicanal con n8n (Fase 2).",
        "Biblioteca de flujos y automatizaciones.",
        "Manual digital por participante.",
        "Certificado de participación INTEZIA.",
    ]),
    # Acreditacion — 3 líneas estándar; [CÓDIGO] → CAP-043.
    "Acreditacion": "\r".join([
        "Programa registrado en INTEZIA Education como CAP-043.",
        "Cumple con el modelo pedagógico oficial (ABR).",
        "Material curado y revisado por el equipo académico.",
    ]),
    # Próximos pasos — logística, sin acuerdos económicos (§4.15).
    "Paso01Titulo": "Fechas y modalidad",
    "Paso01Body": (
        "Definimos fechas, zona horaria y modalidad de cada fase antes "
        "de arrancar."
    ),
    "Paso02Titulo": "Acceso y logística",
    "Paso02Body": (
        "Coordinamos el acceso a las cuentas, los participantes de cada "
        "fase y la agenda de sesiones."
    ),
    "Paso03Titulo": "Reunión de arranque",
    "Paso03Body": (
        "Reunión de unos 30 minutos para alinear casos reales, canales "
        "y prioridades de cada fase."
    ),
}


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-colchones-regal.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    # pre-llenar campos existentes (Beneficios + Pasos)
    for name, value in UPDATES.items():
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

    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(
        "Colchones Regal CAP-043 (cotización única) — Entregables + "
        "Acreditación + Próximos pasos pre-llenados. Apartado económico vacío "
        "(lo llena ventas)."
    )


if __name__ == "__main__":
    main()
