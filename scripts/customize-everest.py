#!/usr/bin/env python3
"""
customize-everest.py — Ajuste especial DET-006 Everest (Detección pura + hoja de ruta de
3 servicios + 2 hojas de cotización).

Tres cosas que el flujo estándar (generar-pdf.sh + customize-acroforms.py) no cubre:

1. **Slide de Cierre tipo escalera**: 4 cajas AcroForm editables (CierreResultado +
   CierrePaso1..3), igual que el resto de decks de este linaje.

2. **Beneficios v3, layout ampliado**: `Entregables`/`Acreditacion` re-horneadas con fondo
   oscuro y layout ampliado — igual que el resto de decks de este linaje.

3. **Hoja "Cotización · Detección" (2ª ronda, 2026-09-03)**: el usuario volvió a pedir 2
   hojas de precio (revierte la consolidación de la 1ª ronda). La hoja "Inversión por
   fases" (3 fases: Detección/Habilidades/Políticas) sigue usando el marker y los campos
   ESTÁNDAR de agregar-campo-precio.py — no necesita lógica propia. Pero la nueva hoja
   "Cotización · Detección" (SOLO Detección, standalone) tiene un título que NO coincide
   con ningún marker a propósito, para que agregar-campo-precio.py la ignore y evitar la
   colisión de nombres de campo documentada en la memoria
   `patron-dos-slides-precio-mismo-deck` (ambos markers reales reutilizan PrecioBase/
   Descuento/PrecioTotal/Notas — si el deck tuviera 2 slides con el marker real, esos
   campos quedarían sincronizados entre páginas). Sus 4 campos se agregan aquí a mano, con
   nombres propios (DetPrecioBase/DetDescuento/DetPrecioTotal/DetNotas) y las MISMAS
   coordenadas por defecto de `_base/styles.css` .s-price (sin modificar — la hoja de
   Detección usa el layout estándar de una sola línea, sin overrides propios). Se ubica en
   la página fija donde vive esa slide en el deck (índice hardcodeado, ver DET_PRICE_PAGE
   abajo), no por búsqueda de marker.

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-everest.py "<ruta al PDF>"
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

# La slide "Cotización · Detección" es la 9ª del deck (1-indexed) — ver index.html,
# <span class="counter">09 / 12</span>. Página fija porque el título no matchea ningún
# marker de agregar-campo-precio.py (a propósito, ver docstring del módulo).
DET_PRICE_PAGE = 8  # 0-indexed → página 9

# Coordenadas DEFAULT de _base/styles.css .s-price (patrón estándar de una sola línea,
# sin overrides — la hoja de Detección no tiene namespace propio, hereda tal cual):
#   base-frame     top=220,left=580,w=487,h=52  → rect (435, 391, 800, 430)
#   discount-frame top=318,left=580,w=487,h=44  → rect (435, 323, 800, 357)
#   total-frame    top=414,left=580,w=487,h=76  → rect (435, 227, 800, 285)
#   notas-box      top=392,left=56, w=480,h=110 → rect (42,  219, 402, 301)
DET_PRICE_FIELDS = [
    {
        "name": "DetPrecioBase",
        "tooltip": "Precio de la Detección (editable).",
        "rect": (435, 391, 800, 430),
        "font_size": 18,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "default": "",
    },
    {
        "name": "DetDescuento",
        "tooltip": "Descuento aplicado a la Detección (editable).",
        "rect": (435, 323, 800, 357),
        "font_size": 14,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "default": "",
    },
    {
        "name": "DetPrecioTotal",
        "tooltip": "Total de la Detección. Autocalculado; editable a mano para overrides.",
        "rect": (435, 227, 800, 285),
        "font_size": 26,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": True,
    },
    {
        "name": "DetNotas",
        "tooltip": "DetNotas (editable, multilínea; usa Enter para nueva línea).",
        "rect": (42, 219, 402, 301),
        "font_size": 11,
        "font_color": "0 g",
        "quadding": 0,
        "multiline": True,
        "default": (
            "Servicio de Detección para las áreas administrativas de Everest "
            "(~20-25 personas)."
        ),
    },
]


def make_det_calc_js() -> str:
    return (
        'var b=this.getField("DetPrecioBase").value;'
        'var d=this.getField("DetDescuento").value;'
        'var bn=parseFloat(String(b).replace(/[^0-9.\\-]/g,""))||0;'
        'var dn=parseFloat(String(d).replace(/[^0-9.\\-]/g,""))||0;'
        'var t=bn-Math.abs(dn);'
        'event.value=isNaN(t)?"":t.toFixed(0);'
    )


def build_det_price_field(spec: dict) -> DictionaryObject:
    field = DictionaryObject(
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
                f"/Helv {spec['font_size']} Tf {spec['font_color']}"
            ),
            NameObject("/Q"): NumberObject(spec["quadding"]),
            NameObject("/BS"): DictionaryObject(
                {
                    NameObject("/Type"): NameObject("/Border"),
                    NameObject("/W"): NumberObject(0),
                    NameObject("/S"): NameObject("/S"),
                }
            ),
        }
    )
    if spec.get("multiline"):
        field[NameObject("/Ff")] = NumberObject(FIELD_FLAG_MULTILINE)
        field[NameObject("/MaxLen")] = NumberObject(2000)
    return field


def add_calculation_action(field: DictionaryObject, js: str) -> None:
    field[NameObject("/AA")] = DictionaryObject(
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

CIERRE_FIELDS = [
    {
        "name": "CierreResultado",
        "tooltip": "Resultado / gran promesa del cierre (editable). Ventas lo redacta por cliente.",
        "rect": (193.5, 391.0, 649.5, 421.0),
        "font_size": 14,
        "font_color": "0 g",
        "default": "Everest, con un roadmap priorizado y base de gobernanza para su certificación ISO 9001.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Paso 1 de la ruta (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Diagnóstico de 3 áreas",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Paso 2 de la ruta (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Gobernanza para ISO 9001",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Paso 3 de la ruta (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Roadmap de adopción de IA",
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
        sys.exit("Uso: python3 customize-everest.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(r.get_object().get("/T")) for r in fields}

    # --- 1. Hoja "Cotización · Detección": 4 campos custom en página fija ---
    if "DetPrecioBase" in existing_names:
        print("Aviso: campos de Cotización · Detección ya presentes — no se re-agregan.")
    else:
        det_page = writer.pages[DET_PRICE_PAGE]
        det_calc_refs = []
        for spec in DET_PRICE_FIELDS:
            field = build_det_price_field(spec)
            if spec.get("calc_action"):
                add_calculation_action(field, make_det_calc_js())
            ref = writer._add_object(field)
            field[NameObject("/P")] = det_page.indirect_reference
            if "/Annots" in det_page:
                det_page[NameObject("/Annots")].append(ref)
            else:
                det_page[NameObject("/Annots")] = ArrayObject([ref])
            fields.append(ref)
            if spec.get("calc_action"):
                det_calc_refs.append(ref)
        # Se AGREGA (no reemplaza) al /CO ya existente — agregar-campo-precio.py ya puso
        # ahí el PrecioTotal de "Inversión por fases" (ver memoria
        # patron-dos-slides-precio-mismo-deck, punto 3).
        existing_co = acro.get(NameObject("/CO"))
        co_list = list(existing_co) if existing_co else []
        co_list.extend(det_calc_refs)
        acro[NameObject("/CO")] = ArrayObject(co_list)
        print(f"✓ {len(DET_PRICE_FIELDS)} campos de 'Cotización · Detección' agregados (página {DET_PRICE_PAGE + 1}).")

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

    # /NeedAppearances=False como último paso: todos los campos horneados por este
    # script y por customize-acroforms.py ya tienen /AP fresco — Adobe Reader/
    # Preview.app deben respetarlo en vez de regenerarlo con su propio wrap (ver
    # memoria bug-needappearances-cliente-regenera-campos).
    acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"✓ Guardado: {pdf_path}")


if __name__ == "__main__":
    main()
