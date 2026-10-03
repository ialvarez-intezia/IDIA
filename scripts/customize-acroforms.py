#!/usr/bin/env python3
"""
Post-procesador genérico de AcroForms: pre-llena los /V de los campos
editables de un PDF ya generado por agregar-campo-precio.py.

Es el camino ESTÁNDAR para propuestas nuevas: en lugar de clonar un
customize-<slug>.py, la propuesta declara sus valores en un archivo
`acroforms.json` dentro de su carpeta y este script los aplica.
Los customize-<slug>.py existentes siguen funcionando (no se migran);
un customize-<slug>.py propio solo se justifica para casos especiales
(resize de /Rect, lógica condicional).

Formato de `acroforms.json` — {campo: valor}; el valor puede ser:
  - string  → se aplica tal cual.
  - lista   → se une con "\r" (multilínea estándar AcroForm).

Ejemplo:
    {
      "Entregables": ["Biblioteca de prompts.", "Workbook digital.",
                      "Certificado de participación INTEZIA."],
      "Acreditacion": ["Programa registrado en INTEZIA Education como CAP-048.",
                       "Cumple con el modelo pedagógico oficial (ABR).",
                       "Material curado y revisado por el equipo académico."],
      "Paso01Titulo": "Confirmamos fechas",
      "Paso01Body": "Validamos fechas, modalidad y zona horaria."
    }

Comportamiento estándar (idéntico al de los customize-<slug>.py):
  - Paso01/02/03Titulo → /DA a 14 pt (el título completo cabe en su línea)
    y se borra el /AP viejo; rebake_bold_fields lo regenera de inmediato.
  - Tras escribir los /V se re-hornea la apariencia (negrita para
    Entregables/Acreditación, regular para Paso0XTitulo/Body) vía
    acroform_appearance.rebake_bold_fields — los 8 campos estándar quedan
    con /AP fresco y correctamente ajustado a su caja.
  - /NeedAppearances = False (como último paso, tras el rebake). Adobe
    Reader y Preview.app respetan entonces el /AP ya horneado en vez de
    regenerarlo con su propio motor de wrap — que no usa las mismas
    métricas que el script y puede cortar texto que sí cabía (caso base:
    2026-08-31 DUSA CH-007/CH-010, ver memoria
    bug-needappearances-cliente-regenera-campos). Los campos de precio
    (fuera de este JSON) siguen editables: cualquier visor regenera la
    apariencia de un campo en el momento en que su valor cambia, sin
    depender de este flag global.
  - El apartado comercial (Programa, Notas, precios) NO se incluye en el
    JSON: queda vacío para ventas (regla del sistema).

Uso:
    # Modo carpeta (estándar): localiza el único PDF y el acroforms.json
    python3 scripts/customize-acroforms.py <slug | clientes/propuestas/<slug>>

    # Multi-deck o JSON con otro nombre: PDF y JSON explícitos
    python3 scripts/customize-acroforms.py <ruta.pdf> <ruta.json>

    # Retro-compatible: JSON inline como string
    python3 scripts/customize-acroforms.py <ruta.pdf> '{"Entregables": "..."}'
"""
import json
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

TITLE_FIELDS = {"Paso01Titulo", "Paso02Titulo", "Paso03Titulo"}
TITLE_DA = "/Helv 14 Tf 0 g"

ROOT = Path(__file__).resolve().parent.parent
PROPUESTAS = ROOT / "clientes" / "propuestas"


def normalize(value) -> str:
    """Lista → multilínea con \\r; string → tal cual."""
    if isinstance(value, list):
        return "\r".join(str(v) for v in value)
    return str(value)


def update_field(writer: PdfWriter, name: str, value: str) -> int:
    """Actualiza /V (y /DV) de TODOS los widgets cuyo /T == name. Retorna count."""
    updated = 0
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
                updated += 1
    return updated


def customize(pdf_path: Path, updates: dict) -> None:
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    summary = []
    for name, raw in updates.items():
        n = update_field(writer, name, normalize(raw))
        summary.append(f"  {name}: {n} campo(s) actualizado(s)")
        if n == 0:
            summary[-1] += "  ⚠️ campo no encontrado en el PDF"

    # Re-hornea la apariencia en negrita de Entregables / Acreditación con
    # el /V ya actualizado (ver acroform_appearance.py).
    baked = rebake_bold_fields(writer)

    # /NeedAppearances=False como último paso: los 8 campos estándar ya
    # tienen /AP fresco (rebake_bold_fields los acaba de regenerar), así
    # que Adobe Reader/Preview.app deben respetarlo tal cual en vez de
    # recalcularlo con su propio wrap (que puede cortar texto que sí cabía
    # — ver memoria bug-needappearances-cliente-regenera-campos).
    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"AcroForms personalizados en {pdf_path}:")
    for line in summary:
        print(line)
    print(f"  Apariencia en negrita re-horneada: {baked} campo(s).")


def resolve_folder_mode(arg: str) -> tuple[Path, dict]:
    """<slug> o <ruta de carpeta> → (pdf único de la carpeta, acroforms.json)."""
    folder = Path(arg)
    if not folder.is_dir():
        folder = PROPUESTAS / arg
    if not folder.is_dir():
        sys.exit(f"ERROR: no existe la carpeta {arg} (ni clientes/propuestas/{arg})")

    json_path = folder / "acroforms.json"
    if not json_path.exists():
        sys.exit(f"ERROR: no existe {json_path}. Créalo o pasa <pdf> <json> explícitos.")

    pdfs = sorted(folder.glob("*.pdf"))
    if len(pdfs) != 1:
        listado = "\n".join(f"  {p.name}" for p in pdfs) or "  (ninguno)"
        sys.exit(
            f"ERROR: la carpeta tiene {len(pdfs)} PDF(s); el modo carpeta exige exactamente 1.\n"
            f"{listado}\nUsa la forma explícita: customize-acroforms.py <pdf> <json>"
        )
    return pdfs[0], json.loads(json_path.read_text(encoding="utf-8"))


def main() -> None:
    if len(sys.argv) == 2:
        pdf_path, updates = resolve_folder_mode(sys.argv[1])
    elif len(sys.argv) == 3:
        pdf_path = Path(sys.argv[1])
        arg = sys.argv[2]
        if arg.lstrip().startswith("{"):
            updates = json.loads(arg)
        else:
            json_path = Path(arg)
            if not json_path.exists():
                sys.exit(f"ERROR: no existe {json_path}")
            updates = json.loads(json_path.read_text(encoding="utf-8"))
    else:
        sys.exit("Uso: customize-acroforms.py <slug|carpeta>  |  <pdf> <json-archivo-o-string>")
    customize(pdf_path, updates)


if __name__ == "__main__":
    main()
