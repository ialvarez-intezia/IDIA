#!/usr/bin/env python3
"""
customize-banco-activo-deteccion-negocios.py — Ajuste especial DET-021 Banco Activo (combo
Detección + Habilidades Fase 1: 13 gerencias + Fundamentals = 54h, más Adquirencia y Medios de
Pago = 12h, 66h totales). Hoja "Inversión por fases" (vuelta a 1 sola hoja, 2026-09-29, a
pedido del usuario) — 2 recuadros (Detección, Habilidades) del lado izquierdo.

Clonado de scripts/customize-la-tienda-del-blumer.py (DET-020) — mismo mecanismo, solo
cambian los textos por defecto de Cierre. Se le sumó (2026-09-29) el ajuste de
FASE_PRICE_FIELDS de customize-go-pharma-cap030.py (ver punto 3 abajo).

Tres cosas que el flujo estándar (generar-pdf.sh + customize-acroforms.py) no cubre:

1. **Slide de Cierre tipo escalera** (esquema 2026-08-26): 4 cajas AcroForm editables
   (CierreResultado + CierrePaso1..3) que ningún grupo de agregar-campo-precio.py inyecta. Se
   agregan en la última página, con su texto por defecto.

2. **Beneficios v3, layout ampliado**: las cajas `Entregables` y `Acreditacion` (repurpuesta
   como "Valor inmediato") viven sobre tarjetas OSCURAS con acento de marca. El genérico
   `customize-acroforms.py` ya las horneó con el default de siempre (fondo blanco, texto
   negro, tamaño de campo chico). Este script las re-hornea con fondo oscuro, texto blanco,
   /Rect agrandado y fuente más grande. **No se toca `FIELD_COLORS` global**.

3. **Hoja de precio de 2 fases (no 3).** FASE_PRICE_FIELDS de agregar-campo-precio.py está
   fijo a 3 fases (origen: IOED CAP-098). Este deck usa solo Fase 1 · Detección + Fase 2 ·
   Habilidades: queda un campo huérfano PrecioFase3 y el subtotal suma 3 fases. Se elimina
   PrecioFase3 y se reescribe el JS de PrecioBase para sumar solo Fase 1 + Fase 2 (mismo
   ajuste que customize-go-pharma-cap030.py).

4. **Sin Descuento (2026-10-01, instrucción directa del usuario).** La fila "Descuento" y la
   caja "TOTAL" (PrecioTotal, que FASE_PRICE_FIELDS calcula por defecto como
   PrecioBase − Descuento) se quitaron del HTML — la cotización queda completa con solo
   Fase 1 + Fase 2 + "Inversión total del proyecto" (PrecioBase). Se eliminan ambos campos del
   PDF (huérfanos, mismo mecanismo que PrecioFase3): dejarlos habría roto el JS de PrecioTotal
   (referencia a un campo "Descuento" que ya no existe) y habría mostrado una caja sin label
   visible en las coordenadas fijas de agregar-campo-precio.py. Como "Inversión total del
   proyecto" pasó a llevar el fondo amarillo sólido que antes tenía "TOTAL" (overrides.css), se
   corrige también su /DA a texto negro 26pt — el naranja por defecto de PrecioBase
   (agregar-campo-precio.py, pensado para el fondo crema) no se lee ahí.

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-banco-activo-deteccion-negocios.py "<ruta al PDF>"
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
        "default": "Las 13 gerencias auditadas, con Adquirencia y Medios de Pago ya trabajando con visibilidad en tiempo real.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Paso 1 de la ruta (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Fundamentals y trabajo por gerencia",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Paso 2 de la ruta (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Mapa de oportunidades priorizado",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Paso 3 de la ruta (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Habilidades Fase 1 en marcha",
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
        sys.exit("Uso: python3 customize-banco-activo-deteccion-negocios.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(ref.get_object().get("/T")) for ref in fields}

    # --- Hoja de precio: quitar PrecioFase3, Descuento y PrecioTotal (huérfanos,
    #     §4 del docstring) y recalcular subtotal a 2 fases ---
    ORPHAN_FIELDS = {"PrecioFase3", "Descuento", "PrecioTotal"}
    orphan_refs = []
    base_field = None
    for ref in fields:
        obj = ref.get_object()
        name = obj.get("/T")
        if name in ORPHAN_FIELDS:
            orphan_refs.append((str(name), ref))
        elif name == "PrecioBase":
            base_field = obj

    if not orphan_refs:
        print("Aviso: no se encontraron campos huérfanos (PrecioFase3/Descuento/PrecioTotal) — ¿ya se corrió este script antes?")
    else:
        removed_names = {name for name, _ in orphan_refs}
        for _, ref in orphan_refs:
            fields.remove(ref)
        for page in writer.pages:
            if "/Annots" not in page:
                continue
            kept = ArrayObject(
                a for a in page["/Annots"] if a.get_object().get("/T") not in removed_names
            )
            page[NameObject("/Annots")] = kept
        if "/CO" in acro:
            acro[NameObject("/CO")] = ArrayObject(
                r for r in acro["/CO"] if r.get_object().get("/T") not in removed_names
            )
        print(f"✓ Campo(s) huérfano(s) eliminado(s): {', '.join(sorted(removed_names))}.")

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

        # 2026-10-01: el texto que escribe ventas en PrecioBase se ve con el
        # /DA de agregar-campo-precio.py (naranja 0.898 0.518 0.137, pensado
        # para el fondo crema claro de base-frame). Este deck le dio a
        # base-frame el fondo amarillo sólido que antes tenía el recuadro
        # "TOTAL" (ver overrides.css) — naranja sobre amarillo sólido no se
        # lee. Se cambia a negro, mismo tratamiento que tenía PrecioTotal
        # (26pt, "0 g") antes de eliminarse.
        base_field[NameObject("/DA")] = TextStringObject("/Helv 26 Tf 0 g")
        print("✓ /DA de PrecioBase corregido: texto negro (antes naranja, ilegible sobre el fondo amarillo sólido).")

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
