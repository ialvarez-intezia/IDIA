#!/usr/bin/env python3
"""
customize-maurel-prom.py — Ajuste especial ALL-003 Maurel & Prom Venezuela (Plan Estratégico
Integral: Detección + Habilidades + Políticas cotizadas, Innovación estimada). Clonado de
customize-simple-tv-all002.py — mismo mecanismo, contenido de cierre propio del cliente.

Tres cosas que el flujo estándar (generar-pdf.sh + customize-acroforms.py) no cubre:

1. **Slide de Cierre tipo escalera** (esquema 2026-08-26): 4 cajas AcroForm editables
   (CierreResultado + CierrePaso1..3) que ningún grupo de agregar-campo-precio.py inyecta. Se
   agregan en la última página, con las mismas coordenadas /Rect que el resto de los decks de
   este linaje, y se hornean con el color de cada escalón vía acroform_appearance.FIELD_COLORS.

2. **Beneficios v3**: las cajas `Entregables` y `Acreditacion` (repurpuesta como "Valor
   inmediato") viven sobre tarjetas OSCURAS con acento de marca. El genérico
   `customize-acroforms.py` ya las horneó con el default de siempre (fondo blanco, texto
   negro). Este script las re-hornea con fondo oscuro y texto blanco. **No se toca
   `FIELD_COLORS` global**.

3. **Campo `InnovacionEstimado`** (nuevo, 2026-09-07): a diferencia de ALL-001 (hoja de precio
   estándar, 1 sola fase) y de CAI-013 (2 fases, ambas dentro de FASE_PRICE_FIELDS), este deck
   usa el marcador "Inversión por fases" con sus 3 slots de fábrica (PrecioFase1/2/3 = Detección
   / Habilidades / Políticas — calzan exacto, no sobra ninguno) MÁS un 4to campo que
   `agregar-campo-precio.py` (compartido, no se modifica) no crea: el estimado de Innovación.
   Se agrega a mano aquí, como campo de una sola línea centrado (mismo estilo que PrecioFase1-3),
   en un callout visualmente aparte (columna derecha, debajo de la caja de términos) — y
   deliberadamente NO se suma a PrecioBase/PrecioTotal, porque es un estimado, no una cotización
   cerrada (retainer mensual de Innovación).

Correr SIEMPRE como 3er paso del trío, después de generar-pdf.sh y customize-acroforms.py
(CLAUDE.md §4.14).

Uso:
    python3 scripts/customize-maurel-prom.py "<ruta al PDF>"
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
        "default": "Maurel & Prom, con Detección, Habilidades y Políticas cotizadas, e Innovación estimada.",
    },
    {
        "name": "CierrePaso1",
        "tooltip": "Paso 1 de la ruta (editable).",
        "rect": (190.5, 229.0, 322.5, 266.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Diagnóstico de 8 áreas",
    },
    {
        "name": "CierrePaso2",
        "tooltip": "Paso 2 de la ruta (editable).",
        "rect": (355.5, 229.0, 487.5, 304.0),
        "font_size": 13,
        "font_color": "1 g",
        "default": "Habilidades y Políticas cotizadas",
    },
    {
        "name": "CierrePaso3",
        "tooltip": "Paso 3 de la ruta (editable).",
        "rect": (520.5, 229.0, 652.5, 341.5),
        "font_size": 13,
        "font_color": "0 g",
        "default": "Innovación estimada, camino completo",
    },
]

# Beneficios v3 — fondo oscuro (~ .rmx-card sobre negro) + texto blanco.
BENEFICIOS_V3_BG = (0.06, 0.06, 0.06)
BENEFICIOS_V3_TEXT = (1.0, 1.0, 1.0)

# Layout ampliado (2026-08-28) — mismo estándar aplicado al resto de las cuentas integral (§4.1b).
BENEFICIOS_LAYOUT = {
    "Entregables":  {"rect": (445.5, 81.0, 590.25, 436.5), "font_size": 13},
    "Acreditacion": {"rect": (637.5, 81.0, 782.25, 436.5), "font_size": 13},
}

# Campo InnovacionEstimado — CSS: .innovacion-row (top=592,left=580,w=487,h=96) con el
# .fase-price-frame hijo en (top:14,right:18,w:140,h:40) relativo al padding-box del
# contenedor. Absoluto en página: top=592+14=606, bottom=646; right=580+487-18=1049,
# left=1049-140=909. PDF pt (factor px→pt ×0.75, y_pt=595-y_css×0.75):
#   x1=909×0.75=681.75  x2=1049×0.75=786.75
#   y1=595-646×0.75=110.5  y2=595-606×0.75=140.5
INNOVACION_FIELD = {
    "name": "InnovacionEstimado",
    "tooltip": "Estimado de Innovación (retainer mensual, ciclo 3/6/12 meses) — NO se suma al total; ventas lo redacta como cifra de referencia.",
    "rect": (681.75, 110.5, 786.75, 140.5),
    "font_size": 13,
    "font_color": "0.898 0.518 0.137 rg",
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


def build_precio_field(spec: dict) -> DictionaryObject:
    """Campo de una sola línea, centrado, mismo estilo visual que PrecioFase1-3
    (fuente regular /Helv, no bold — a diferencia de las cajas de Cierre)."""
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
            NameObject("/Q"): NumberObject(1),  # centrado
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
        sys.exit("Uso: python3 customize-maurel-prom.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    acro = writer._root_object["/AcroForm"]
    fields = acro["/Fields"]
    existing_names = {str(r.get_object().get("/T")) for r in fields}

    # --- 1. Slide de precio: agregar el campo InnovacionEstimado (no lo crea el script
    #    compartido) — la página que contiene "Inversión por fases" es la última página con
    #    ese contenido; la localizamos por presencia de los campos PrecioFase1-3 ya creados.
    precio_page = None
    for page in writer.pages:
        if "/Annots" not in page:
            continue
        names_on_page = {
            str(a.get_object().get("/T")) for a in page["/Annots"]
        }
        if "PrecioFase1" in names_on_page:
            precio_page = page
            break

    if precio_page is None:
        print("Aviso: no se encontró la página de 'Inversión por fases' — ¿cambió el deck?")
    elif "InnovacionEstimado" in existing_names:
        print("Aviso: campo InnovacionEstimado ya presente — no se re-agrega.")
    else:
        field = build_precio_field(INNOVACION_FIELD)
        ref = writer._add_object(field)
        field[NameObject("/P")] = precio_page.indirect_reference
        precio_page[NameObject("/Annots")].append(ref)
        fields.append(ref)
        print("✓ Campo InnovacionEstimado agregado (no sumado al total).")

    # --- 2. Slide de Cierre: agregar las 4 cajas editables tipo escalera ---
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

    # Hornea Cierre (vía FIELD_COLORS global, ya registrado para estos 4 nombres).
    rebake_bold_fields(writer)

    # Re-hornea Beneficios v3 (Entregables/Acreditacion) con fondo oscuro y el
    # layout ampliado (rect más grande + fuente más grande) — aislado a este
    # script, no toca el default global de las demás propuestas.
    n = rebake_dark(writer, {"Entregables", "Acreditacion"}, layout=BENEFICIOS_LAYOUT)
    print(f"✓ Beneficios v3: {n} caja(s) re-horneada(s) con fondo oscuro y layout ampliado.")

    # /NeedAppearances=False: todos los campos horneados por este script y por
    # customize-acroforms.py ya tienen /AP fresco — Adobe Reader/Preview.app deben
    # respetarlo en vez de regenerarlo con su propio wrap (ver memoria
    # bug-needappearances-cliente-regenera-campos; a diferencia de
    # customize-simple-tv-all001.py, que quedó con /NeedAppearances=True por ser anterior
    # al fix, este script nace ya corregido).
    acro[NameObject("/NeedAppearances")] = BooleanObject(False)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"✓ Guardado: {pdf_path}")


if __name__ == "__main__":
    main()
