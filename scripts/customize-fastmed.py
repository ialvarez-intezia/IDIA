#!/usr/bin/env python3
"""
customize-fastmed.py — Ajuste especial CAI-030 FastMed · Agente conversacional para atención
al paciente (Habilidades + Innovación, equipo de 8 personas, 6 sesiones de 2h + ciclo mensual
de 3 meses).

Clonado de scripts/customize-luis-sosa-cerebro-digital.py (CAI-029) — mismo mecanismo; solo
cambian los textos por defecto de Cierre. Mismo NeedAppearances=False que Luis Sosa/Banco
Plaza (bug corregido 2026-08-31, ver memoria bug-needappearances-cliente-regenera-campos.md).

Tres cosas que el flujo estándar (generar-pdf.sh + customize-acroforms.py) no cubre:

1. **Hoja de precio "Inversión por fases": Fase 1 (Habilidades) + Fase 2 (Innovación,
   agregada 2026-09-30)**, mismo patrón que customize-corporaciones-easyaccess.py /
   customize-go-pharma-cap030.py / customize-simple-tv-det002.py. `agregar-campo-precio.py`
   siempre crea 3 slots (PrecioFase1-3) para el marcador "Inversión por fases"; este deck solo
   usa 2 fases, así que se elimina el campo huérfano PrecioFase3 y se recalcula PrecioBase
   para que sea PrecioFase1 + PrecioFase2.

2. **Slide de Cierre tipo escalera**: 4 cajas AcroForm editables (CierreResultado +
   CierrePaso1..3) que ningún grupo de agregar-campo-precio.py inyecta. Se agregan en la
   última página, con su texto por defecto.

3. **Beneficios v3, layout ampliado**: las cajas `Entregables` y `Acreditacion` (repurpuesta
   como "Valor inmediato") viven sobre tarjetas OSCURAS con acento de marca. El genérico
   `customize-acroforms.py` ya las horneó con el default de siempre (fondo blanco, texto
   negro, tamaño de campo chico). Este script las re-hornea con fondo oscuro, texto blanco,
   /Rect agrandado y fuente más grande. **No se toca `FIELD_COLORS` global**.

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-fastmed.py "<ruta al PDF>"
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
    NumberObject,
    TextStringObject,
)


def make_fase_subtotal_js(fase_count: int) -> str:
    terms, lines = [], []
    for i in range(1, fase_count + 1):
        lines.append(
            f'var f{i}=parseFloat(String(this.getField("PrecioFase{i}").value)'
            '.replace(/[^0-9.\\-]/g,""))||0;'
        )
        terms.append(f"f{i}")
    lines.append(f'var t={"+".join(terms)};')
    lines.append('event.value=isNaN(t)?"":t.toFixed(0);')
    return "".join(lines)


FIELD_FLAG_MULTILINE = 1 << 12

CIERRE_FIELDS = [
    {
        "name": "CierreResultado",
        "tooltip": "Resultado / gran promesa del cierre (editable). Ventas lo redacta por cliente.",
        "rect": (193.5, 391.0, 649.5, 421.0),
        "font_size": 14,
        "font_color": "0 g",
        "default": "Un agente conversacional propio, en producción, que su equipo sostiene con doble autenticación y seguridad.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Paso 1 de la ruta (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Diseño del agente",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Paso 2 de la ruta (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Construcción del agente",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Paso 3 de la ruta (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Producción y continuidad",
    },
]

# Beneficios v3 — fondo oscuro (~ .rmx-card sobre negro) + texto blanco.
BENEFICIOS_V3_BG = (0.06, 0.06, 0.06)
BENEFICIOS_V3_TEXT = (1.0, 1.0, 1.0)

BENEFICIOS_LAYOUT = {
    "Entregables":  {"rect": (445.5, 81.0, 590.25, 436.5), "font_size": 13},
    "Acreditacion": {"rect": (637.5, 81.0, 782.25, 436.5), "font_size": 13},
}


def build_cierre_field(spec: dict) -> DictionaryObject:
    return DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/FT"): NameObject("/Tx"),
            NameObject("/T"): TextStringObject(spec["name"]),
            NameObject("/TU"): TextStringObject(spec["tooltip"]),
            NameObject("/V"): TextStringObject(spec["default"]),
            NameObject("/DV"): TextStringObject(spec["default"]),
            NameObject("/Rect"): ArrayObject([FloatObject(c) for c in spec["rect"]]),
            NameObject("/F"): NumberObject(4),
            NameObject("/DA"): TextStringObject(
                f"/HeBO {spec['font_size']} Tf {spec['font_color']}"
            ),
            NameObject("/Q"): NumberObject(0),
            NameObject("/Ff"): NumberObject(FIELD_FLAG_MULTILINE),
            NameObject("/MaxLen"): NumberObject(2000),
            NameObject("/BS"): DictionaryObject(
                {
                    NameObject("/Type"): NameObject("/Border"),
                    NameObject("/W"): NumberObject(0),
                    NameObject("/S"): NameObject("/S"),
                }
            ),
        }
    )


def rebake_dark(writer: PdfWriter, field_names: set, layout: dict = None) -> int:
    """Re-hornea el /AP de los campos indicados con fondo oscuro + texto blanco
    (Beneficios v3). No usa acroform_appearance.FIELD_COLORS (global) — los
    colores viven solo aquí, aislados a este deck."""
    layout = layout or {}
    count = 0
    for page in writer.pages:
        if "/Annots" not in page:
            continue
        for annot in page["/Annots"]:
            obj = annot.get_object()
            name = obj.get("/T")
            if name is None or str(name) not in field_names:
                continue
            base_name = str(name)
            spec = layout.get(base_name)
            if spec is not None:
                obj[NameObject("/Rect")] = ArrayObject(
                    [FloatObject(c) for c in spec["rect"]]
                )
            rect = [float(c) for c in obj["/Rect"]]
            text = str(obj.get("/V", "") or "")
            da = str(obj.get("/DA", "/HeBO 10 Tf 1 g"))
            if spec is not None and "font_size" in spec:
                da = f"/HeBO {spec['font_size']} Tf 1 g"
            obj[NameObject("/MK")] = DictionaryObject(
                {
                    NameObject("/BG"): ArrayObject(
                        [FloatObject(c) for c in BENEFICIOS_V3_BG]
                    ),
                    NameObject("/BC"): ArrayObject(),
                }
            )
            obj[NameObject("/DA")] = TextStringObject(
                da if "1 g" in da else (da.replace("0 g", "1 g") if "0 g" in da else da)
            )
            ap_ref = _make_appearance(
                writer, rect, da, text,
                base_font="/Helvetica-Bold",
                font_key="HeBO",
                widths=_WIDTHS_BOLD,
                default_w=_DEFAULT_W_BOLD,
                bg_rgb=BENEFICIOS_V3_BG,
                text_rgb=BENEFICIOS_V3_TEXT,
            )
            obj[NameObject("/AP")] = DictionaryObject({NameObject("/N"): ap_ref})
            count += 1
    return count


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 customize-fastmed.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]

    # --- 1. Hoja de precio: quitar PrecioFase3 (huérfano) y recalcular subtotal a 2 fases ---
    to_remove = {"PrecioFase3"}
    removed = set()
    base_field = None
    existing_names = set()
    kept_fields = ArrayObject()
    for ref in fields:
        obj = ref.get_object()
        name = str(obj.get("/T"))
        existing_names.add(name)
        if name in to_remove:
            removed.add(name)
            continue
        if name == "PrecioBase":
            base_field = obj
        kept_fields.append(ref)
    acro[NameObject("/Fields")] = kept_fields
    # Reapunta la variable local al array YA ATTACHADO a /AcroForm/Fields — si el bloque de
    # Cierre de abajo siguiera usando `fields` (el array viejo, huérfano tras la reasignación
    # de arriba), sus fields.append(ref) nunca llegarían al /Fields real del PDF (ver memoria
    # bug-fields-kept-fields-divorcio).
    fields = kept_fields

    for page in writer.pages:
        if "/Annots" not in page:
            continue
        page[NameObject("/Annots")] = ArrayObject(
            a for a in page["/Annots"] if str(a.get_object().get("/T")) not in to_remove
        )

    if removed:
        print(f"✓ Campo huérfano eliminado: {', '.join(sorted(removed))}.")
    else:
        print("Aviso: no se encontró PrecioFase3 — ¿ya se corrió este script antes?")

    if base_field is not None:
        base_field[NameObject("/AA")] = DictionaryObject(
            {
                NameObject("/C"): DictionaryObject(
                    {
                        NameObject("/Type"): NameObject("/Action"),
                        NameObject("/S"): NameObject("/JavaScript"),
                        NameObject("/JS"): TextStringObject(make_fase_subtotal_js(2)),
                    }
                )
            }
        )
        print("✓ Subtotal (PrecioBase) recalculado: Fase 1 + Fase 2.")

    last_page = writer.pages[-1]
    if "CierreResultado" in existing_names:
        print("Aviso: campos de Cierre ya presentes — no se re-agregan.")
    else:
        for spec in CIERRE_FIELDS:
            field = build_cierre_field(spec)
            ref = writer._add_object(field)
            field[NameObject("/P")] = last_page.indirect_reference
            if "/Annots" in last_page:
                last_page[NameObject("/Annots")].append(ref)
            else:
                last_page[NameObject("/Annots")] = ArrayObject([ref])
            fields.append(ref)
        print(f"✓ {len(CIERRE_FIELDS)} cajas de Cierre (escalera) agregadas.")

    rebake_bold_fields(writer)

    n = rebake_dark(writer, {"Entregables", "Acreditacion"}, layout=BENEFICIOS_LAYOUT)
    print(f"✓ Beneficios v3: {n} caja(s) re-horneada(s) con fondo oscuro y layout ampliado.")

    acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"✓ Guardado: {pdf_path}")


if __name__ == "__main__":
    main()
