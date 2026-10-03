#!/usr/bin/env python3
"""
customize-hjb-quimica.py — Ajuste especial CAI-031 HJB Química (combo Detección de 15
áreas + Habilidades directivas). Hoja "Inversión por fases" — 2 recuadros (Detección,
Habilidades) del lado izquierdo.

Reestructuración 2026-10-02: deck de 21 a 12 slides (ver brief.md). Mismo mecanismo que
la versión anterior, con 2 ajustes de coordenadas por el nuevo layout:
- Entregables/Acreditacion ahora son 2 tarjetas lado a lado (Fase 1 | Fase 2), no 4
  bloques — BENEFICIOS_LAYOUT usa los nuevos rects.
- PrecioFase2 se movió de fila (la Fase 1 ahora lleva desglose por componente, más alta)
  — se reposiciona su /Rect tras el paso genérico de agregar-campo-precio.py.

Clonado originalmente de scripts/customize-banco-activo-deteccion-negocios.py (DET-021).

Tres cosas que el flujo estándar (generar-pdf.sh + customize-acroforms.py) no cubre:

1. **Slide de Cierre tipo escalera** (esquema 2026-08-26): 4 cajas AcroForm editables
   (CierreResultado + CierrePaso1..3) que ningún grupo de agregar-campo-precio.py inyecta.

2. **Beneficios v3, 2 tarjetas por fase**: las cajas `Entregables` y `Acreditacion` viven
   sobre tarjetas OSCURAS con acento de marca, una por fase. Re-hornea con fondo oscuro,
   texto blanco, /Rect reposicionado y fuente más grande.

3. **Hoja de precio de 2 fases (no 3).** FASE_PRICE_FIELDS está fijo a 3 fases. Este deck usa
   solo Fase 1 · Detección + Fase 2 · Habilidades: se elimina el campo huérfano PrecioFase3,
   se reescribe el JS de PrecioBase para sumar solo Fase 1 + Fase 2, y se reposiciona
   PrecioFase2 (la fila de Fase 1 creció por el desglose de componentes).

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-hjb-quimica.py "<ruta al PDF>"
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

FIELD_FLAG_MULTILINE = 1 << 12


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


CIERRE_FIELDS = [
    {
        "name": "CierreResultado",
        "tooltip": "Resultado / gran promesa del cierre (editable). Ventas lo redacta por cliente.",
        "rect": (193.5, 391.0, 649.5, 421.0),
        "font_size": 14,
        "font_color": "0 g",
        "default": "Las 15 áreas de HJB Química auditadas, con los 15 responsables operando con su propio Cerebro Digital.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Paso 1 de la ruta (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Detección de las 15 áreas",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Paso 2 de la ruta (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Recomendación de licencias",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Paso 3 de la ruta (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Habilidades con Cerebro Digital",
    },
]

# Beneficios v3 — fondo oscuro (~ .rmx-card sobre negro) + texto blanco.
BENEFICIOS_V3_BG = (0.06, 0.06, 0.06)
BENEFICIOS_V3_TEXT = (1.0, 1.0, 1.0)

# 2026-10-02 (d): el texto horneado SIEMPRE arranca arriba del rect (sin
# centrado vertical propio, ver acroform_appearance._build_stream) — una
# caja más alta que el contenido deja vacío abajo DENTRO de la caja, así que
# en vez de agrandar la caja se centra la unidad completa (etiqueta+caja,
# h=320, antes 420) en el espacio disponible entre el header y el footer.
# CSS .entregables-box top=296 left=56 w=480 h=320 / .acreditaciones-box
# top=296 left=580 w=487 h=320. Texto 17pt (sin cambio) ya llena la caja.
# pt: x1=px*0.75; x2=(px+w)*0.75; y2=595-top*0.75; y1=595-(top+h)*0.75.
BENEFICIOS_LAYOUT = {
    "Entregables":  {"rect": (42.0, 133.0, 402.0, 373.0), "font_size": 17},
    "Acreditacion": {"rect": (435.0, 133.0, 800.25, 373.0), "font_size": 17},
}

# 2026-10-02: la fila de Fase 1 ahora lleva desglose por componente (más
# alta) — Fase 2 se corrió de CSS top=240 a top=288 (frame top=300 abs).
# pt: x1=297 x2=402 (sin cambio, mismo left/width de siempre); y2=595-300*0.75=370;
# y1=595-(300+40)*0.75=340.
PRECIO_FASE2_RECT = (297.0, 340.0, 402.0, 370.0)


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
        sys.exit("Uso: python3 customize-hjb-quimica.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(ref.get_object().get("/T")) for ref in fields}

    # --- Hoja de precio: quitar PrecioFase3 y recalcular subtotal a 2 fases ---
    fase3_ref = None
    base_field = None
    fase2_field = None
    for ref in fields:
        obj = ref.get_object()
        name = obj.get("/T")
        if name == "PrecioFase3":
            fase3_ref = ref
        elif name == "PrecioBase":
            base_field = obj
        elif name == "PrecioFase2":
            fase2_field = obj

    if fase3_ref is None:
        print("Aviso: no se encontró PrecioFase3 — ¿ya se corrió este script antes?")
    else:
        fields.remove(fase3_ref)
        for page in writer.pages:
            if "/Annots" not in page:
                continue
            kept = ArrayObject(
                a for a in page["/Annots"] if a.get_object().get("/T") != "PrecioFase3"
            )
            page[NameObject("/Annots")] = kept
        print("✓ Campo huérfano PrecioFase3 eliminado.")

    if fase2_field is None:
        print("Aviso: no se encontró PrecioFase2 — no se pudo reposicionar su /Rect.")
    else:
        fase2_field[NameObject("/Rect")] = ArrayObject(
            [FloatObject(c) for c in PRECIO_FASE2_RECT]
        )
        print("✓ /Rect de PrecioFase2 reposicionado (fila de Fase 1 con desglose).")

    if base_field is None:
        print("Aviso: no se encontró PrecioBase — no se pudo corregir el JS de subtotal.")
    else:
        js = make_fase_subtotal_js(2)
        base_field[NameObject("/AA")] = DictionaryObject(
            {
                NameObject("/C"): DictionaryObject(
                    {
                        NameObject("/Type"): NameObject("/Action"),
                        NameObject("/S"): NameObject("/JavaScript"),
                        NameObject("/JS"): TextStringObject(js),
                    }
                )
            }
        )
        print("✓ JS de PrecioBase corregido: suma solo Fase 1 + Fase 2.")

    # --- Slide de Cierre: agregar las 4 cajas editables tipo escalera ---
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
