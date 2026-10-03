#!/usr/bin/env python3
"""
customize-maurel-prom-copilot-en.py — Ajuste especial CAI-021 Maurel & Prom Venezuela
(Copilot for Your Team), VERSIÓN EN INGLÉS (clientes/propuestas/maurel-prom-copilot-en/).
Traducción 1:1 del deck en español (customize-maurel-prom-copilot.py), mismo código, mismo
cliente, incluye el Módulo IV "Agents and Flows" agregado el mismo día.

**Por qué este script hace TODO el trabajo de personalización:**

El deck en inglés usa marcadores H2 en inglés ("What you'll walk away with", "Economic
Proposal", "How we get started") que NO coinciden con los strings Spanish-literal que
scripts/agregar-campo-precio.py busca ("Lo que se llevan", "Propuesta Económica", "Cómo
arrancamos"). Ese script es COMPARTIDO y nunca se modifica por deck (CLAUDE.md) — así que
para este deck, generar-pdf.sh crea el /AcroForm vacío (0 campos, los 3 grupos "omitido")
pero SÍ deja listo el /DR (fuentes /Helv y /HeBO) porque agregar-campo-precio.py lo hace
incondicionalmente. customize-acroforms.py NO debe correr para este deck.

Este script construye, en un solo paso, los 3 grupos estándar (por ÍNDICE DE PÁGINA fijo,
ya que la estructura del deck de 14 slides es conocida y fija):
- Página 9 (0-indexed) — "What you'll walk away with": Entregables + Acreditacion (bold).
- Página 11 — "Economic Proposal": PrecioBase (editable) + Descuento + PrecioTotal
  (auto-calculado) + Programa (multiline) + Notas (multiline).
- Página 12 — "How we get started": Paso01-03 Titulo/Body.
Más lo que ya era especial en la versión en español: Cierre escalera (última página) y
Beneficios v3 (fondo oscuro + layout ampliado).

Los nombres de campo (/T) se mantienen en ESPAÑOL (PrecioBase, Entregables,
CierreResultado, etc.) — identificadores internos invisibles al usuario final; mantenerlos
permite reutilizar acroform_appearance.rebake_bold_fields() sin tocar ese módulo compartido.

Trío correcto para este deck (SIN customize-acroforms.py en medio):
    bash scripts/generar-pdf.sh maurel-prom-copilot-en
    python3 scripts/customize-maurel-prom-copilot-en.py "clientes/propuestas/maurel-prom-copilot-en/<pdf>"

Uso:
    python3 scripts/customize-maurel-prom-copilot-en.py <ruta-al-pdf>
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

# --- Fixed page indices (0-based) — this deck's structure is fixed, 14 slides ---
PAGE_BENEFITS = 9    # "What you'll walk away with" (Entregables + Acreditacion)
PAGE_PRICE = 11      # "Economic Proposal" (PrecioBase/Descuento/PrecioTotal + Programa + Notas)
PAGE_STEPS = 12      # "How we get started" (Paso01-03)
# Close (Cierre escalera) always goes on the last page — writer.pages[-1]

PROGRAMA_DEFAULT = "\r".join([
    "Copilot for Your Team (CAI-021)",
    "5 modules · 15 hours · In-person, 2 groups (Caracas and Maracaibo)",
    "5 sessions of 3h each, within Maurel & Prom's Microsoft 365 environment",
])
NOTAS_DEFAULT = "General-scope proposal: number of participants per site to be confirmed with the client."
ENTREGABLES_DEFAULT = "\r".join([
    "• Personal kit of instructions (prompts) for Copilot Chat.",
    "• An agent of your own, built in Copilot, with area-specific knowledge.",
    "• Responsible Copilot usage protocol at Maurel & Prom.",
    "• Personal 30-day adoption plan per participant.",
    "• Digital workbook and INTEZIA certificate of participation.",
])
ACREDITACION_DEFAULT = "\r".join([
    "• First draft written with Copilot from session 1.",
    "• Instruction method applicable right away in Word and Excel.",
    "• Meeting minutes solved in minutes, not hours.",
    "• A first simple flow built on a real repetitive task.",
])
PASOS_DEFAULTS = {
    "Paso01Titulo": "We confirm dates",
    "Paso01Body": "We define the dates for the 5 in-person sessions in Caracas and Maracaibo.",
    "Paso02Titulo": "Access and logistics",
    "Paso02Body": "We coordinate space, participants, and schedule for the 5 sessions at each site.",
    "Paso03Titulo": "Kick-off meeting",
    "Paso03Body": "30-minute meeting to align the training's real cases with the team.",
}

CIERRE_FIELDS = [
    {
        "name": "CierreResultado",
        "tooltip": "Closing result / big promise (editable). Sales drafts it per client.",
        "rect": (193.5, 391.0, 649.5, 421.0),
        "font_size": 14,
        "font_color": "0 g",
        "default": "Maurel & Prom, with its team using Copilot with method, agents, and flows of its own.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Step 1 of the path (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Fundamentals and prompting",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Step 2 of the path (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Daily use, agents, and flows",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Step 3 of the path (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Responsible usage protocol",
    },
]

# Beneficios v3 — dark background + white text.
BENEFICIOS_V3_BG = (0.06, 0.06, 0.06)
BENEFICIOS_V3_TEXT = (1.0, 1.0, 1.0)

BENEFICIOS_LAYOUT = {
    "Entregables":  {"rect": (445.5, 81.0, 590.25, 436.5), "font_size": 13},
    "Acreditacion": {"rect": (637.5, 81.0, 782.25, 436.5), "font_size": 13},
}

# --- "Economic Proposal" page: standard PRECIO_FIELDS pattern (same /Rect as
# agregar-campo-precio.py's PRECIO_FIELDS — geometry is language-independent). ---
PRECIO_FIELDS = [
    {
        "name": "PrecioBase",
        "tooltip": "Base price of the proposal (e.g. 2,250 REF).",
        "rect": (435, 391, 800, 430),
        "font_size": 18,
        "font_color": "0.898 0.518 0.137 rg",
        "font": "Helv",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "Descuento",
        "tooltip": "Discount applied (e.g. -450 REF).",
        "rect": (435, 323, 800, 357),
        "font_size": 14,
        "font_color": "0 g",
        "font": "Helv",
        "quadding": 1,
        "multiline": False,
        "default": "",
        "calc_action": False,
    },
    {
        "name": "PrecioTotal",
        "tooltip": "Total. Auto-calculated when price or discount changes; editable by hand for overrides.",
        "rect": (435, 227, 800, 285),
        "font_size": 26,
        "font_color": "0 g",
        "font": "Helv",
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
        "name": "Programa",
        "tooltip": "Programa (editable, multilínea; usa Enter para nueva línea).",
        "rect": (42, 350, 402, 429),
        "font_size": 11,
        "font_color": "0 g",
        "font": "Helv",
        "quadding": 0,
        "multiline": True,
        "default": PROGRAMA_DEFAULT,
        "calc_action": False,
    },
    {
        "name": "Notas",
        "tooltip": "Notas (editable, multilínea; usa Enter para nueva línea).",
        "rect": (42, 219, 402, 301),
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
        sys.exit("Uso: python3 customize-maurel-prom-copilot-en.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(ref.get_object().get("/T")) for ref in fields}

    if len(writer.pages) != 14:
        print(f"Aviso: se esperaban 14 páginas, el PDF tiene {len(writer.pages)} — revisar índices fijos.")

    # --- 1. Benefits page: Entregables + Acreditacion ---
    benefits_page = writer.pages[PAGE_BENEFITS]
    added = add_field_group(writer, benefits_page, BENEFITS_FIELDS, fields, existing_names)
    print(f"✓ Benefits (page {PAGE_BENEFITS + 1}): {', '.join(added) if added else 'ya presentes'}")

    # --- 2. Economic Proposal page: PrecioBase/Descuento/PrecioTotal + Programa + Notas ---
    price_page = writer.pages[PAGE_PRICE]
    added = add_field_group(writer, price_page, PRECIO_FIELDS, fields, existing_names)
    print(f"✓ Economic Proposal (page {PAGE_PRICE + 1}): {', '.join(added) if added else 'ya presentes'}")

    # --- 3. Next steps page: Paso01-03 Titulo/Body ---
    steps_page = writer.pages[PAGE_STEPS]
    added = add_field_group(writer, steps_page, STEPS_FIELDS, fields, existing_names)
    print(f"✓ Next steps (page {PAGE_STEPS + 1}): {', '.join(added) if added else 'ya presentes'}")

    # --- 4. Close: 4-box editable stairway ---
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

    # --- 5. Bake bold/regular appearances (Entregables/Acreditacion/Cierre + Paso01-03) ---
    baked = rebake_bold_fields(writer)
    print(f"✓ Apariencia horneada: {baked} campo(s).")

    # --- 6. Beneficios v3: dark rebake (must run AFTER rebake_bold_fields) ---
    n = rebake_dark(writer, {"Entregables", "Acreditacion"}, layout=BENEFICIOS_LAYOUT)
    print(f"✓ Beneficios v3: {n} caja(s) re-horneada(s) con fondo oscuro y layout ampliado.")

    acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"✓ Guardado: {pdf_path}")


if __name__ == "__main__":
    main()
