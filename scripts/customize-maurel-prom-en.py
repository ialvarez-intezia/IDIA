#!/usr/bin/env python3
"""
customize-maurel-prom-en.py — Ajuste especial ALL-003 Maurel & Prom Venezuela, VERSIÓN EN
INGLÉS (clientes/propuestas/maurel-prom-en/). Traducción 1:1 del deck en español
(customize-maurel-prom.py), mismo código, mismo cliente.

**Por qué este script hace TODO el trabajo de personalización (no solo el "extra" que hacía
la versión en español):**

El deck en inglés usa marcadores H2 en inglés ("Phased Investment", "What you'll walk away
with", "How we get started") que NO coinciden con los strings Spanish-literal que
scripts/agregar-campo-precio.py busca ("Inversión por fases", "Lo que se llevan", "Cómo
arrancamos"). Ese script es COMPARTIDO y nunca se modifica por deck (CLAUDE.md) — así que
para este deck, generar-pdf.sh crea el /AcroForm vacío (0 campos, los 3 grupos "omitido")
pero SÍ deja listo el /DR (fuentes /Helv y /HeBO) porque agregar-campo-precio.py lo hace
incondicionalmente. customize-acroforms.py NO debe correr para este deck: no encontraría
ningún campo que pre-llenar.

Este script construye entonces, en un solo paso:
1. Los 3 grupos estándar que agregar-campo-precio.py habría creado por marcador (aquí por
   ÍNDICE DE PÁGINA fijo, ya que la estructura del deck es conocida y fija):
   - Página 10 (0-indexed) — "Phased Investment": PrecioFase1-3 + PrecioBase (subtotal
     auto-calculado) + Descuento + PrecioTotal (auto-calculado) + Notas.
   - Página 8 — "What you'll walk away with": Entregables + Acreditacion (bold, contenido en
     inglés).
   - Página 11 — "How we get started": Paso01-03 Titulo/Body (contenido en inglés).
2. Lo que YA era especial en la versión en español (sin cambios de mecánica, solo de
   contenido): InnovacionEstimado (página 10, mismo /Rect que PrecioFase1-3), Cierre
   escalera (última página), Beneficios v3 (fondo oscuro + layout ampliado).

Los nombres de campo (/T) se mantienen en ESPAÑOL (PrecioBase, Entregables,
CierreResultado, etc.) — son identificadores internos invisibles al usuario final; mantenerlos
permite reutilizar acroform_appearance.rebake_bold_fields() (que matchea por esos nombres)
sin tocar ese módulo compartido.

Trío correcto para este deck (SIN customize-acroforms.py en medio):
    bash scripts/generar-pdf.sh maurel-prom-en
    python3 scripts/customize-maurel-prom-en.py "clientes/propuestas/maurel-prom-en/<pdf>"

Uso:
    python3 scripts/customize-maurel-prom-en.py <ruta-al-pdf>
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

# --- Fixed page indices (0-based) — this deck's structure is fixed, 13 slides ---
PAGE_BENEFITS = 8   # "What you'll walk away with" (Entregables + Acreditacion)
PAGE_PRICE = 10      # "Phased Investment" (PrecioFase1-3 + PrecioBase/Descuento/PrecioTotal + Notas + InnovacionEstimado)
PAGE_STEPS = 11      # "How we get started" (Paso01-03)
# Close (Cierre escalera) always goes on the last page — writer.pages[-1]

NOTAS_DEFAULT = "\r".join([
    "Phases 1 to 3 (Detection, Skills, Policy) are quoted in this document.",
    "Phase 4 (Innovation) is presented as an estimate, given its nature as a monthly retainer.",
])
ENTREGABLES_DEFAULT = "\r".join([
    "• AI usage report + Strategy by area (Phase 1).",
    "• Complete Skills package by area, 8-12h (Phase 2).",
    "• Policy manual aligned with the European framework, AI Compass, and Risk Matrix (Phase 3).",
    "• Ongoing support estimate for Innovation (Phase 4).",
])
ACREDITACION_DEFAULT = "\r".join([
    "• Actionable assessment from Phase 1.",
    "• Skills quoted as a complete package, not introductory.",
    "• Policy backed by the parent company's regulatory framework.",
])
PASOS_DEFAULTS = {
    "Paso01Titulo": "We confirm scope",
    "Paso01Body": "We define with Maurel & Prom the priority order of the 8 areas for Phase 1.",
    "Paso02Titulo": "Access and logistics",
    "Paso02Body": "We coordinate Microsoft 365 access, schedule, and leaders for each area, Caracas and Maracaibo.",
    "Paso03Titulo": "Integral plan kick-off",
    "Paso03Body": "Kick-off meeting (~30 min) to align the 4 phases with Legal & Compliance.",
}

CIERRE_FIELDS = [
    {
        "name": "CierreResultado",
        "tooltip": "Closing result / big promise (editable). Sales drafts it per client.",
        "rect": (193.5, 391.0, 649.5, 421.0),
        "font_size": 14,
        "font_color": "0 g",
        "default": "Maurel & Prom, with Detection, Skills, and Policy quoted, and Innovation estimated.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Step 1 of the path (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "8 areas assessed",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Step 2 of the path (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Skills and Policy quoted",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Step 3 of the path (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Innovation estimated, complete path",
    },
]

# Beneficios v3 — dark background + white text.
BENEFICIOS_V3_BG = (0.06, 0.06, 0.06)
BENEFICIOS_V3_TEXT = (1.0, 1.0, 1.0)

BENEFICIOS_LAYOUT = {
    "Entregables":  {"rect": (445.5, 81.0, 590.25, 436.5), "font_size": 13},
    "Acreditacion": {"rect": (637.5, 81.0, 782.25, 436.5), "font_size": 13},
}

# InnovacionEstimado — same /Rect as the Spanish deck (identical CSS layout).
INNOVACION_FIELD = {
    "name": "InnovacionEstimado",
    "tooltip": "Innovation estimate (monthly retainer, 3/6/12-month cycle) — NOT added to the total; sales drafts it as a reference figure.",
    "rect": (681.75, 110.5, 786.75, 140.5),
    "font_size": 13,
    "font_color": "0.898 0.518 0.137 rg",
}

# --- "Phased Investment" page: PrecioFase1-3 + PrecioBase (auto subtotal) +
# Descuento + PrecioTotal (auto) + Notas. Same /Rect as agregar-campo-precio.py's
# FASE_PRICE_FIELDS (fase_count=3) — geometry is language-independent.
FASE_PRICE_FIELDS = [
    {
        "name": "PrecioFase1",
        "tooltip": "Phase 1 amount (e.g. 1,200 REF).",
        "rect": (297, 430, 402, 460),
        "font_size": 13,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioFase2",
        "tooltip": "Phase 2 amount (e.g. 1,200 REF).",
        "rect": (297, 376, 402, 406),
        "font_size": 13,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioFase3",
        "tooltip": "Phase 3 amount (e.g. 1,200 REF).",
        "rect": (297, 322, 402, 352),
        "font_size": 13,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioBase",
        "tooltip": "Total plan investment. Auto-calculated as the sum of the phases; editable by hand for overrides.",
        "rect": (435, 428.5, 800, 467.5),
        "font_size": 18,
        "font_color": "0.898 0.518 0.137 rg",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": True,
        "calc_js": (
            'var f1=parseFloat(String(this.getField("PrecioFase1").value).replace(/[^0-9.\\-]/g,""))||0;'
            'var f2=parseFloat(String(this.getField("PrecioFase2").value).replace(/[^0-9.\\-]/g,""))||0;'
            'var f3=parseFloat(String(this.getField("PrecioFase3").value).replace(/[^0-9.\\-]/g,""))||0;'
            'var t=f1+f2+f3;'
            'event.value=isNaN(t)?"":t.toFixed(0);'
        ),
    },
    {
        "name": "Descuento",
        "tooltip": "Discount applied (e.g. -450 REF).",
        "rect": (435, 361, 800, 394),
        "font_size": 14,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioTotal",
        "tooltip": "Total. Auto-calculated when the subtotal or discount changes; editable by hand for overrides.",
        "rect": (435, 268, 800, 325),
        "font_size": 26,
        "font_color": "0 g",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": True,
        "calc_js": (
            'var b=this.getField("PrecioBase").value;'
            'var d=this.getField("Descuento").value;'
            'var bn=parseFloat(String(b).replace(/[^0-9.\\-]/g,""))||0;'
            'var dn=parseFloat(String(d).replace(/[^0-9.\\-]/g,""))||0;'
            'var t=bn-Math.abs(dn);'
            'event.value=isNaN(t)?"":t.toFixed(0);'
        ),
    },
    {
        "name": "Notas",
        "tooltip": "Notas (editable, multiline; use Enter for a new line).",
        "rect": (42, 191.5, 402, 274),
        "font_size": 11,
        "font_color": "0 g",
        "font": "Helv",
        "quadding": 0,
        "multiline": True,
        "default": NOTAS_DEFAULT,
        "calc_action": False,
    },
]

# --- Benefits page: Entregables + Acreditacion (bold, same /Rect as agregar-campo-precio.py). ---
BENEFITS_FIELDS = [
    {
        "name": "Entregables",
        "tooltip": "Entregables (editable, multilínea; usa Enter para nueva línea).",
        "rect": (438, 338, 596, 455),
        "font_size": 10,
        "font_color": "0 g",
        "font": "HeBO",
        "quadding": 0,
        "multiline": True,
        "default": ENTREGABLES_DEFAULT,
        "calc_action": False,
    },
    {
        "name": "Acreditacion",
        "tooltip": "Acreditacion (editable, multilínea; usa Enter para nueva línea).",
        "rect": (630, 338, 788, 455),
        "font_size": 10,
        "font_color": "0 g",
        "font": "HeBO",
        "quadding": 0,
        "multiline": True,
        "default": ACREDITACION_DEFAULT,
        "calc_action": False,
    },
]

# --- Next steps page: Paso01-03 Titulo/Body (same /Rect as agregar-campo-precio.py). ---
def _paso_title(name, x_left, x_right):
    return {
        "name": name,
        "tooltip": f"{name} (editable, single-line).",
        "rect": (x_left, 366, x_right, 396),
        "font_size": 18,
        "font_color": "0 g",
        "font": "Helv",
        "quadding": 0,
        "multiline": False,
        "default": PASOS_DEFAULTS[name],
        "calc_action": False,
    }


def _paso_body(name, x_left, x_right):
    return {
        "name": name,
        "tooltip": f"{name} (editable, multiline).",
        "rect": (x_left, 202, x_right, 360),
        "font_size": 13,
        "font_color": "0 g",
        "font": "Helv",
        "quadding": 0,
        "multiline": True,
        "default": PASOS_DEFAULTS[name],
        "calc_action": False,
    }


STEPS_FIELDS = [
    _paso_title("Paso01Titulo", 63, 266),
    _paso_body("Paso01Body", 63, 266),
    _paso_title("Paso02Titulo", 320, 522),
    _paso_body("Paso02Body", 320, 522),
    _paso_title("Paso03Titulo", 576, 779),
    _paso_body("Paso03Body", 576, 779),
]


def build_field(spec: dict) -> DictionaryObject:
    """Generic /Tx widget builder — geometry/logic only, no language baked in
    (ported from agregar-campo-precio.py's build_field(), not imported due to
    the hyphenated module filename)."""
    flags = 0
    if spec.get("multiline"):
        flags |= FIELD_FLAG_MULTILINE
    font_name = spec.get("font", "Helv")
    default_value = spec.get("default", "") or ""

    field = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/FT"): NameObject("/Tx"),
            NameObject("/T"): TextStringObject(spec["name"]),
            NameObject("/TU"): TextStringObject(spec["tooltip"]),
            NameObject("/V"): TextStringObject(default_value),
            NameObject("/DV"): TextStringObject(default_value),
            NameObject("/Rect"): ArrayObject([FloatObject(c) for c in spec["rect"]]),
            NameObject("/F"): NumberObject(4),
            NameObject("/DA"): TextStringObject(
                f"/{font_name} {spec['font_size']} Tf {spec['font_color']}"
            ),
            NameObject("/Q"): NumberObject(spec.get("quadding", 0)),
            NameObject("/Ff"): NumberObject(flags),
            NameObject("/MaxLen"): NumberObject(2000 if spec.get("multiline") else 80),
            NameObject("/BS"): DictionaryObject(
                {
                    NameObject("/Type"): NameObject("/Border"),
                    NameObject("/W"): NumberObject(0),
                    NameObject("/S"): NameObject("/S"),
                }
            ),
            NameObject("/MK"): DictionaryObject(
                {
                    NameObject("/BC"): ArrayObject(),
                    **(
                        {NameObject("/BG"): ArrayObject(
                            [FloatObject(1), FloatObject(1), FloatObject(1)]
                        )}
                        if spec.get("multiline")
                        else {}
                    ),
                }
            ),
        }
    )
    return field


def add_calculation_action(field: DictionaryObject, js: str) -> None:
    js_action = DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Action"),
            NameObject("/S"): NameObject("/JavaScript"),
            NameObject("/JS"): TextStringObject(js),
        }
    )
    field[NameObject("/AA")] = DictionaryObject({NameObject("/C"): js_action})


def add_field_group(writer: PdfWriter, page, specs: list, fields, existing_names) -> list:
    added = []
    for spec in specs:
        if spec["name"] in existing_names:
            continue
        field = build_field(spec)
        if spec.get("calc_action"):
            add_calculation_action(field, spec["calc_js"])
        ref = writer._add_object(field)
        field[NameObject("/P")] = page.indirect_reference
        if "/Annots" in page:
            page[NameObject("/Annots")].append(ref)
        else:
            page[NameObject("/Annots")] = ArrayObject([ref])
        fields.append(ref)
        existing_names.add(spec["name"])
        added.append(spec["name"])
    return added


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


def build_precio_field(spec: dict) -> DictionaryObject:
    """Single-line, centered field, same visual style as PrecioFase1-3
    (regular /Helv font, not bold — unlike the Cierre boxes)."""
    return DictionaryObject(
        {
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Widget"),
            NameObject("/FT"): NameObject("/Tx"),
            NameObject("/T"): TextStringObject(spec["name"]),
            NameObject("/TU"): TextStringObject(spec["tooltip"]),
            NameObject("/V"): TextStringObject(""),
            NameObject("/DV"): TextStringObject(""),
            NameObject("/Rect"): ArrayObject([FloatObject(c) for c in spec["rect"]]),
            NameObject("/F"): NumberObject(4),
            NameObject("/DA"): TextStringObject(
                f"/Helv {spec['font_size']} Tf {spec['font_color']}"
            ),
            NameObject("/Q"): NumberObject(1),
            NameObject("/Ff"): NumberObject(0),
            NameObject("/MaxLen"): NumberObject(80),
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
    (Beneficios v3). No usa acroform_appearance.FIELD_COLORS (global)."""
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
        sys.exit("Uso: python3 customize-maurel-prom-en.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(ref.get_object().get("/T")) for ref in fields}

    if len(writer.pages) != 13:
        print(f"Aviso: se esperaban 13 páginas, el PDF tiene {len(writer.pages)} — revisar índices fijos.")

    # --- 1. Benefits page: Entregables + Acreditacion ---
    benefits_page = writer.pages[PAGE_BENEFITS]
    added = add_field_group(writer, benefits_page, BENEFITS_FIELDS, fields, existing_names)
    print(f"✓ Benefits (page {PAGE_BENEFITS + 1}): {', '.join(added) if added else 'ya presentes'}")

    # --- 2. Phased Investment page: PrecioFase1-3 + PrecioBase/Descuento/PrecioTotal + Notas ---
    price_page = writer.pages[PAGE_PRICE]
    added = add_field_group(writer, price_page, FASE_PRICE_FIELDS, fields, existing_names)
    print(f"✓ Phased Investment (page {PAGE_PRICE + 1}): {', '.join(added) if added else 'ya presentes'}")

    # --- 3. InnovacionEstimado (same page as Phased Investment) ---
    if "InnovacionEstimado" in existing_names:
        print("Aviso: InnovacionEstimado ya presente — no se re-agrega.")
    else:
        field = build_precio_field(INNOVACION_FIELD)
        ref = writer._add_object(field)
        field[NameObject("/P")] = price_page.indirect_reference
        price_page[NameObject("/Annots")].append(ref)
        fields.append(ref)
        existing_names.add("InnovacionEstimado")
        print("✓ InnovacionEstimado agregado (no sumado al total).")

    # --- 4. Next steps page: Paso01-03 Titulo/Body ---
    steps_page = writer.pages[PAGE_STEPS]
    added = add_field_group(writer, steps_page, STEPS_FIELDS, fields, existing_names)
    print(f"✓ Next steps (page {PAGE_STEPS + 1}): {', '.join(added) if added else 'ya presentes'}")

    # --- 5. Close: 4-box editable stairway ---
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

    # --- 6. Bake bold/regular appearances (Entregables/Acreditacion/Cierre + Paso01-03) ---
    baked = rebake_bold_fields(writer)
    print(f"✓ Apariencia horneada: {baked} campo(s).")

    # --- 7. Beneficios v3: dark rebake (must run AFTER rebake_bold_fields) ---
    n = rebake_dark(writer, {"Entregables", "Acreditacion"}, layout=BENEFICIOS_LAYOUT)
    print(f"✓ Beneficios v3: {n} caja(s) re-horneada(s) con fondo oscuro y layout ampliado.")

    acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"✓ Guardado: {pdf_path}")


if __name__ == "__main__":
    main()
