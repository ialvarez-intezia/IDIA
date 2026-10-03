#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta BDV · Charla Ejecutiva CH-004
(IA Ejecutiva con Gemini para Banca).

Es una Charla de cortesía: no tiene slide de Propuesta Económica ni bloques
Entregables/Acreditación. Solo lleva los 6 campos de «Próximos pasos»
(3 cards × título single-line + body multiline). Este script los pre-llena
con el contenido real listo-para-entregar, tras la corrida del script
canónico agregar-campo-precio.py.

Los campos quedan EDITABLES — solo se reescribe /V y /DV; ventas ajusta el
texto en Adobe Reader si hace falta.

Uso:
    python customize-bdv-ch004.py <pdf>
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

# Títulos de «Próximos pasos» — 14 pt entra holgado en el campo single-line
# (a 18 pt los títulos se recortaban al abrir el PDF).
TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-bdv-ch004.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Paso01Titulo": "Confirmamos sala y fecha",
        "Paso01Body": (
            "María coordina con BDV la sala ejecutiva, fecha y hora · BDV "
            "confirma audiencia (5-15 vicepresidentes) y duración disponible "
            "(60-90 min) · Intezia prepara escenario hipotético del sector banca."
        ),
        "Paso02Titulo": "Entrega de la charla",
        "Paso02Body": (
            "Equipo INTEZIA Education entrega la charla ejecutiva en sala BDV · "
            "3 documentos firmables presentados · escenario hipotético discutido "
            "en vivo · espacio de preguntas y respuestas con el comité."
        ),
        "Paso03Titulo": "Captura y cierre",
        "Paso03Body": (
            "María captura los leads del comité y abre las cotizaciones de "
            "CAP-023 (cohort 70 personas) y CAP-024 (plan integral 6 meses) · "
            "sesión con el sponsor para construir la política de uso aceptable de IA del BDV."
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

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"BDV CH-004 — 6 campos de Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
