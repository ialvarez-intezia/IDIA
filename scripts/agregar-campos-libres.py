#!/usr/bin/env python3
"""
agregar-campos-libres.py — Campos editables en cualquier lugar del deck compacto (CAI-079 Viva, 2026-11-04).

En el HTML un espacio en blanco se marca con <span class="campo-libre" data-campo="Nombre" data-tip="Ayuda" [data-calc="A+B-C"]>.
Este script mide su caja en Chrome (scripts/medir-campos-libres.js, media print, el mismo tamaño que la impresión), la convierte a puntos del
PDF y añade un campo de texto editable en esa posición, sin coordenadas escritas a mano:

  Hoja de inversión con tabla (inversion.desglose): ValorFila1..N, Subtotal, DescuentoPrograma, TotalAntesImpuestos, IVA, TotalConImpuestos.
  Páginas de respuesta a la solicitud: tokens [[CAMPO:Nombre|Ayuda]] en los puntos (p. ej. ImpactoSugerenciaA).

data-calc: suma y resta de otros campos por nombre («Subtotal-DescuentoPrograma»); el resto resta en valor absoluto (el descuento se puede teclear
con o sin signo). Lee «1.200,50», «1200» y «2.250 REF»; escribe con punto de miles y coma decimal. Si el cálculo da 0 no escribe nada, así que un
monto tecleado a mano en un total sobrevive hasta que se llene alguno de sus componentes.

Correr DESPUÉS de generar-pdf.sh y customize-acroforms.py (lo hace pdf-habilidades-compacto.sh). Sin campos libres en el HTML no hace nada.

Uso:
    python3 scripts/agregar-campos-libres.py <slug>
    python3 scripts/agregar-campos-libres.py "<ruta al PDF>" "<ruta al index.html>"
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, BooleanObject, DictionaryObject, NameObject, TextStringObject

RAIZ = Path(__file__).resolve().parent.parent
PROPUESTAS = RAIZ / "clientes" / "propuestas"


def _cargar_precio():
    sp = importlib.util.spec_from_file_location("agregar_campo_precio", RAIZ / "scripts" / "agregar-campo-precio.py")
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


def js_calculo(expr: str) -> str:
    """JS de cálculo para «A+B-C»: suma los positivos y resta el valor absoluto de los negativos; escribe 1.234,50."""
    import re
    terminos = re.findall(r"([+-]?)\s*([A-Za-z0-9_]+)", expr)
    partes = []
    for signo, nombre in terminos:
        v = f'nv(this.getField("{nombre}").value)'
        partes.append(f"-Math.abs({v})" if signo == "-" else v)
    return (
        'function nv(v){var s=String(v).replace(/[^0-9.,\\-]/g,"");'
        'if(/^-?\\d{1,3}(\\.\\d{3})+(,\\d+)?$/.test(s)){s=s.replace(/\\./g,"").replace(",",".");}'
        'else{s=s.replace(",",".");}return parseFloat(s)||0;}'
        f"var t={'+'.join(partes)};"
        'if(t!==0){var s=(Math.round(t*100)/100).toFixed(2).split(".");'
        's[0]=s[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g,".");event.value=s[0]+","+s[1];}'
    )


def medir(html: Path) -> list:
    r = subprocess.run(["node", str(RAIZ / "scripts" / "medir-campos-libres.js"), str(html)], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("ERROR al medir los campos libres: " + (r.stderr.strip() or r.stdout.strip()))
    return json.loads(r.stdout or "[]")


def main() -> None:
    if len(sys.argv) == 2:
        carpeta = Path(sys.argv[1])
        if not carpeta.is_dir():
            carpeta = PROPUESTAS / sys.argv[1]
        pdfs = sorted(carpeta.glob("*.pdf"))
        if len(pdfs) != 1:
            sys.exit(f"ERROR: la carpeta {carpeta} tiene {len(pdfs)} PDF(s); se necesita exactamente 1")
        pdf, html = pdfs[0], carpeta / "index.html"
    elif len(sys.argv) == 3:
        pdf, html = Path(sys.argv[1]), Path(sys.argv[2])
    else:
        sys.exit(__doc__)
    if "campo-libre" not in html.read_text(encoding="utf-8"):
        print("Sin campos libres en el HTML: nada que añadir.")
        return
    campos = medir(html)
    if not campos:
        sys.exit("ERROR: el HTML declara campos libres pero Chrome no encontró ninguno")
    ap = _cargar_precio()
    reader = PdfReader(str(pdf))
    writer = PdfWriter(clone_from=reader)
    catalog = writer._root_object
    acro = catalog.get(NameObject("/AcroForm")) or DictionaryObject()
    catalog[NameObject("/AcroForm")] = acro
    if NameObject("/Fields") not in acro:
        acro[NameObject("/Fields")] = ArrayObject()
    if NameObject("/DR") not in acro:
        acro[NameObject("/DR")] = ap.make_dr(writer)
    if NameObject("/DA") not in acro:
        acro[NameObject("/DA")] = TextStringObject("/Helv 12 Tf 0 g")
    existentes = set()
    for ref in acro[NameObject("/Fields")]:
        n = ref.get_object().get("/T")
        if n is not None:
            existentes.add(str(n))
    calc_refs, resumen = [], []
    for c in campos:
        if c["name"] in existentes:
            sys.exit(f"ERROR: ya existe un campo llamado {c['name']} en el PDF")
        if c["slide"] >= len(writer.pages):
            sys.exit(f"ERROR: el campo {c['name']} está en la slide {c['slide'] + 1} y el PDF solo tiene {len(writer.pages)} páginas")
        page = writer.pages[c["slide"]]
        W, H = float(page.mediabox.width), float(page.mediabox.height)
        sx, sy = W / c["sw"], H / c["sh"]
        x1, x2 = c["x"] * sx, (c["x"] + c["w"]) * sx
        y2, y1 = H - c["y"] * sy, H - (c["y"] + c["h"]) * sy
        grande = c["h"] >= 31
        spec = {"name": c["name"], "tooltip": c["tip"] or "Valor en USD (lo escribe Ventas).", "rect": (round(x1, 2), round(y1, 2), round(x2, 2), round(y2, 2)),
                "font_size": 13 if c["w"] > 120 else 11, "font_color": "0 g", "quadding": 1 if c["w"] > 120 else 0, "multiline": False, "readonly": False,
                "default": "", "calc_action": False}
        if grande:
            spec["font_size"] = 14
        field = ap.build_field(spec)
        if c["calc"]:
            ap.add_calculation_action(field, js_calculo(c["calc"]))
        ref = writer._add_object(field)
        field[NameObject("/P")] = page.indirect_reference
        if "/Annots" in page:
            page[NameObject("/Annots")].append(ref)
        else:
            page[NameObject("/Annots")] = ArrayObject([ref])
        acro[NameObject("/Fields")].append(ref)
        if c["calc"]:
            calc_refs.append((c["calc"], ref))
        resumen.append(f"  página {c['slide'] + 1}: {c['name']}" + (f" (= {c['calc']})" if c["calc"] else ""))
    if calc_refs:
        # Orden de cálculo: un campo va después de los que lee (Subtotal → TotalAntesImpuestos → TotalConImpuestos)
        nombres = {str(r.get_object()["/T"]): r for _, r in calc_refs}
        ordenados, hechos = [], set()
        pendientes = list(calc_refs)
        while pendientes:
            avance = False
            for item in list(pendientes):
                expr, r = item
                import re
                dep = [n for n in re.findall(r"[A-Za-z0-9_]+", expr) if n in nombres and nombres[n] is not r]
                if all(n in hechos for n in dep):
                    ordenados.append(r); hechos.add(str(r.get_object()["/T"])); pendientes.remove(item); avance = True
            if not avance:
                ordenados += [r for _, r in pendientes]; break
        co = acro.get(NameObject("/CO")) or ArrayObject()
        for r in ordenados:
            co.append(r)
        acro[NameObject("/CO")] = co
    with open(pdf, "wb") as f:
        writer.write(f)
    print(f"Campos libres añadidos a {pdf.name}: {len(campos)}")
    for l in resumen:
        print(l)


if __name__ == "__main__":
    main()
