#!/usr/bin/env python3
"""
customize-dusa-cai035.py — Ajuste especial CAI-035 DUSA (Habilidades, 44 soluciones en 10 áreas).

Deck compacto de 6 slides (la 6, Retorno, no lleva campos; la lógica sigue operando solo en la 5). Lo que el flujo estándar (generar-pdf.sh + customize-acroforms.py)
no cubre:

  Slide 5 («¿Qué tendrás a cambio?», catálogo de entregables): las dos cajas AcroForm
  `Entregables` (usada como «Entregables transversales») y `Acreditacion` (usada como «Valor
  inmediato», nombre conservado por compatibilidad con agregar-campo-precio.py) NO van en las
  4 tarjetas de Beneficios v3, sino en una franja inferior de 2 tarjetas oscuras. Este script:
    1. las reposiciona (/Rect) sobre esa franja,
    2. les re-hornea la apariencia con fondo oscuro y texto blanco (negrita, 10,5 pt).

Coordenadas: px del overrides.css (.db-box-1 / .db-box-2) × 0,75 → pt; y_pt = 595 − (top+h)·0,75.
  .db-box-1: left 80    · top 659 · 449.5 × 64 px   → (60,      52.75, 397.125, 100.75)
  .db-box-2: left 593.5 · top 659 · 449.5 × 64 px   → (445.125, 52.75, 782.25 , 100.75)
Si se mueven las cajas en overrides.css, recalcular aquí.

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-dusa-cai035.py "<ruta al PDF>"
"""
import sys
from pathlib import Path

from acroform_appearance import (
    _DEFAULT_W_BOLD,
    _WIDTHS_BOLD,
    _make_appearance,
    rebake_bold_fields,
)
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    BooleanObject,
    DictionaryObject,
    FloatObject,
    NameObject,
    TextStringObject,
)

# ≈ rgba(244,186,26,.06) sobre negro: el mismo tono que la tarjeta .db-card, para que la caja se funda con ella.
DARK_BG = (0.057, 0.045, 0.008)
DARK_TEXT = (1.0, 1.0, 1.0)

DELIV_LAYOUT = {
    "Entregables":  {"rect": (60.0, 52.75, 397.125, 100.75), "font_size": 10.5},
    "Acreditacion": {"rect": (445.125, 52.75, 782.25, 100.75), "font_size": 10.5},
}


def rebake_dark(writer: PdfWriter, layout: dict) -> int:
    """Reposiciona y re-hornea /AP (fondo oscuro + texto blanco en negrita)."""
    count = 0
    for page in writer.pages:
        if "/Annots" not in page:
            continue
        for annot in page["/Annots"]:
            obj = annot.get_object()
            name = obj.get("/T")
            if name is None or str(name) not in layout:
                continue
            spec = layout[str(name)]
            obj[NameObject("/Rect")] = ArrayObject([FloatObject(c) for c in spec["rect"]])
            rect = [float(c) for c in obj["/Rect"]]
            text = str(obj.get("/V", "") or "")
            da = f"/HeBO {spec['font_size']} Tf 1 g"
            obj[NameObject("/DA")] = TextStringObject(da)
            obj[NameObject("/MK")] = DictionaryObject(
                {
                    NameObject("/BG"): ArrayObject([FloatObject(c) for c in DARK_BG]),
                    NameObject("/BC"): ArrayObject(),
                }
            )
            ap_ref = _make_appearance(
                writer, rect, da, text,
                base_font="/Helvetica-Bold",
                font_key="HeBO",
                widths=_WIDTHS_BOLD,
                default_w=_DEFAULT_W_BOLD,
                bg_rgb=DARK_BG,
                text_rgb=DARK_TEXT,
            )
            obj[NameObject("/AP")] = DictionaryObject({NameObject("/N"): ap_ref})
            count += 1
    return count


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 customize-dusa-cai035.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    # Re-hornea el resto de campos en negrita/regular con su /V actual y luego sobreescribe
    # Entregables / Acreditacion con la versión oscura y el nuevo /Rect.
    rebake_bold_fields(writer)
    n = rebake_dark(writer, DELIV_LAYOUT)
    print(f"✓ Slide 5: {n} caja(s) reposicionada(s) y re-horneada(s) con fondo oscuro.")

    acro = writer._root_object["/AcroForm"]
    acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)
    print(f"✓ Guardado: {pdf_path}")


if __name__ == "__main__":
    main()
