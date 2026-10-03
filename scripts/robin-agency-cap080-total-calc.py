#!/usr/bin/env python3
"""
Caso especial CAP-080 (Robin Agency): la 4ª hoja de Propuesta Económica
("Total consolidado") debe reflejar la SUMA de las 3 hojas anteriores en
lugar del cálculo genérico base-descuento que agregar-campo-precio.py le
da por defecto a toda instancia adicional.

En vez de tocar el script genérico (afectaría a todas las propuestas
multi-página existentes), este script corre como tercer paso, después del
par estándar (generar-pdf.sh + customize-acroforms.py), y solo:

  1. Añade una acción /AA/C a PrecioBase_4 que suma PrecioTotal +
     PrecioTotal_2 + PrecioTotal_3 (cada uno tratado como número, 0 si está
     vacío o no numérico).
  2. Inserta esa acción en /AcroForm/CO justo antes de PrecioTotal_4, para
     que el orden de recálculo de Adobe Reader sea:
     PrecioTotal → PrecioTotal_2 → PrecioTotal_3 → PrecioBase_4 → PrecioTotal_4
     (así PrecioTotal_4 = PrecioBase_4 - Descuento_4 ya usa la suma fresca).

Caso especial autorizado por CLAUDE.md §6 paso 6 (lógica condicional).
Sin PrecioBase_4/PrecioTotal_4 en el AcroForm, no hace nada.

Nombre del archivo deliberadamente SIN el prefijo "customize-<slug>": ese
patrón lo detecta generar-pdf.sh (`customize-${SLUG}*.py`) como si fuera el
customize COMPLETO de la propuesta y dejaría de sugerir el paso estándar
`customize-acroforms.py` (que este script no reemplaza — solo lo complementa).

Orden de ejecución para esta propuesta (tres pasos, no el par estándar):
    ./scripts/generar-pdf.sh robin-agency-cap080
    python3 scripts/customize-acroforms.py "<ruta-al-pdf>" "<ruta-al-acroforms.json>"
    python3 scripts/robin-agency-cap080-total-calc.py "<ruta-al-pdf>"
"""
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject, TextStringObject

SUM_JS = (
    'var t1=this.getField("PrecioTotal").value;'
    'var t2=this.getField("PrecioTotal_2").value;'
    'var t3=this.getField("PrecioTotal_3").value;'
    'var n1=parseFloat(String(t1).replace(/[^0-9.\\-]/g,""))||0;'
    'var n2=parseFloat(String(t2).replace(/[^0-9.\\-]/g,""))||0;'
    'var n3=parseFloat(String(t3).replace(/[^0-9.\\-]/g,""))||0;'
    'event.value=(n1+n2+n3).toFixed(0);'
)


def find_field(writer: PdfWriter, name: str):
    fields = writer._root_object["/AcroForm"]["/Fields"]
    for ref in fields:
        obj = ref.get_object()
        if obj.get("/T") == name:
            return ref, obj
    return None, None


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-robin-agency-cap080.py <ruta-al-pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    base4_ref, base4 = find_field(writer, "PrecioBase_4")
    total4_ref, total4 = find_field(writer, "PrecioTotal_4")
    if base4 is None or total4 is None:
        sys.exit("ERROR: PrecioBase_4 / PrecioTotal_4 no existen en este PDF.")

    js_action = DictionaryObject({
        NameObject("/Type"): NameObject("/Action"),
        NameObject("/S"): NameObject("/JavaScript"),
        NameObject("/JS"): TextStringObject(SUM_JS),
    })
    base4[NameObject("/AA")] = DictionaryObject({NameObject("/C"): js_action})

    co = writer._root_object["/AcroForm"]["/CO"]
    co_list = list(co)
    # Quita cualquier referencia previa a PrecioBase_4 (reruns idempotentes)
    co_list = [r for r in co_list if r.get_object().get("/T") != "PrecioBase_4"]
    idx_total4 = next(
        i for i, r in enumerate(co_list) if r.get_object().get("/T") == "PrecioTotal_4"
    )
    co_list.insert(idx_total4, base4_ref)
    writer._root_object["/AcroForm"][NameObject("/CO")] = writer._root_object["/AcroForm"]["/CO"].__class__(co_list)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"PrecioBase_4: cálculo de suma (PrecioTotal + _2 + _3) añadido en {pdf_path}")


if __name__ == "__main__":
    main()
