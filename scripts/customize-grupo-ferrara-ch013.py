#!/usr/bin/env python3
"""
customize-grupo-ferrara-ch013.py — Ajuste especial CH-013 Grupo Ferrara (Charla, CON
propuesta económica desde 2026-09-11, sin recuadro de Descuento desde 2026-09-14).

Tres cosas que el flujo estándar (generar-pdf.sh + customize-acroforms.py) no cubre:

1. **Slide de Cierre tipo escalera** (esquema 2026-08-26): 4 cajas AcroForm editables
   (CierreResultado + CierrePaso1..3) que ningún grupo de agregar-campo-precio.py inyecta. Se
   agregan en la última página, con su texto por defecto.

2. **Beneficios v3, layout ampliado**: las cajas `Entregables` y `Acreditacion` (repurpuesta
   como "Valor inmediato") viven sobre tarjetas OSCURAS con acento de marca. El genérico
   `customize-acroforms.py` ya las horneó con el default de siempre (fondo blanco, texto
   negro, tamaño de campo chico). Este script las re-hornea con fondo oscuro, texto blanco,
   /Rect agrandado y fuente más grande. **No se toca `FIELD_COLORS` global**.

3. **Cotización sin Descuento** (ajuste 2026-09-14, a pedido del usuario): el HTML de este
   deck ya no tiene el recuadro visual de Descuento (label + frame retirados, ver
   index.html/overrides.css), pero `agregar-campo-precio.py` sigue inyectando el campo
   AcroForm "Descuento" en toda página con marker "Propuesta Económica" — es el grupo
   PRECIO_FIELDS compartido por todo el sistema, no se toca ese script global. Este script
   elimina el campo "Descuento" del PDF final (de /AcroForm/Fields y de los /Annots de su
   página) y reposiciona/agranda "PrecioTotal" para ocupar la caja ampliada, con un /AA/C
   nuevo que ya no referencia a Descuento (Total = Base, sin resta) — evita el error de
   JavaScript que lanzaría el cálculo original al buscar un campo que ya no existe.

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-grupo-ferrara-ch013.py "<ruta al PDF>"
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

CIERRE_FIELDS = [
    {
        "name": "CierreResultado",
        "tooltip": "Resultado / gran promesa del cierre (editable). Ventas lo redacta por cliente.",
        "rect": (193.5, 391.0, 649.5, 421.0),
        "font_size": 14,
        "font_color": "0 g",
        "default": "Creadores de contenido de Grupo Ferrara con un método propio para idear y crear con Gemini, sin perder su voz.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Paso 1 de la ruta (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Método de prompt aprendido",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Paso 2 de la ruta (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Calendario de contenido armado",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Paso 3 de la ruta (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Caption y guion listos para publicar",
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


# Cotización sin Descuento — caja de TOTAL agrandada (ver overrides.css:
# .s-price .total-frame top=344/height=130, left=580/width=487 sin cambios).
# Conversión px→pt (factor 0.75): x1=580×0.75=435; x2=(580+487)×0.75≈800;
# y2=595-344×0.75=337; y1=595-(344+130)×0.75=239.5.
TOTAL_RECT_SIN_DESCUENTO = (435, 239.5, 800, 337)
TOTAL_FONT_SIZE_SIN_DESCUENTO = 32
TOTAL_JS_SIN_DESCUENTO = (
    'var b=this.getField("PrecioBase").value;'
    'var bn=parseFloat(String(b).replace(/[^0-9.\\-]/g,""))||0;'
    'event.value=bn?bn.toFixed(0):"";'
)


def remove_field(writer: PdfWriter, name: str) -> bool:
    """Elimina un campo de /AcroForm/Fields y de los /Annots de su página."""
    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    target_ref = None
    for ref in fields:
        if str(ref.get_object().get("/T")) == name:
            target_ref = ref
            break
    if target_ref is None:
        return False
    fields.remove(target_ref)
    target_obj = target_ref.get_object()
    for page in writer.pages:
        if "/Annots" not in page:
            continue
        annots = page["/Annots"]
        for a in list(annots):
            if a.get_object() == target_obj:
                annots.remove(a)
    return True


def update_total_field(writer: PdfWriter, rect: tuple, font_size: int, js: str) -> bool:
    """Reposiciona PrecioTotal y reemplaza su /AA/C para que ya no reste Descuento."""
    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    for ref in fields:
        obj = ref.get_object()
        if str(obj.get("/T")) != "PrecioTotal":
            continue
        obj[NameObject("/Rect")] = ArrayObject([FloatObject(c) for c in rect])
        da_parts = str(obj.get("/DA", "/Helv 26 Tf 0 g")).split()
        if len(da_parts) >= 3 and da_parts[2] == "Tf":
            da_parts[1] = str(font_size)
        obj[NameObject("/DA")] = TextStringObject(" ".join(da_parts))
        obj[NameObject("/AA")] = DictionaryObject(
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
        return True
    return False


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
        sys.exit("Uso: python3 customize-grupo-ferrara-ch013.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(ref.get_object().get("/T")) for ref in fields}

    # --- Cotización sin Descuento: eliminar el campo y reacomodar el Total ---
    if remove_field(writer, "Descuento"):
        print("✓ Campo 'Descuento' eliminado (recuadro retirado de la cotización).")
    else:
        print("Aviso: campo 'Descuento' no encontrado — ¿ya se había eliminado?")

    if update_total_field(
        writer, TOTAL_RECT_SIN_DESCUENTO, TOTAL_FONT_SIZE_SIN_DESCUENTO, TOTAL_JS_SIN_DESCUENTO
    ):
        print("✓ Campo 'PrecioTotal' reposicionado y recalculado (Total = Base, sin descuento).")
    else:
        print("Aviso: campo 'PrecioTotal' no encontrado.")

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
