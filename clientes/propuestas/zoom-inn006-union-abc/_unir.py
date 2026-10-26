#!/usr/bin/env python3
"""Une las tres opciones de Zoom INN-006 (A Bootcamp, B Por área, C Híbrido) en UNA sola propuesta (código INN-006, sin sufijo).

Pedido de Ivana (26/10/2026): las láminas comunes quedan una sola vez; las tres alternativas se muestran en una sola propuesta, con su
hoja de inversión y su facilidad de pago cada una; los cálculos de personas son por opción (A 510; B y C con los totales por área).

Fuente de las láminas: los index.html ya generados de zoom-inn006-a, -b y -c (a su vez salen de zoom-inn006-a/_construir-opciones.py).
Por eso el orden es: 1) regenerar las tres con _construir-opciones.py, 2) correr este script, 3) correr _pdf.sh.

Uso (desde la raíz del repositorio):  python3 clientes/propuestas/zoom-inn006-union-abc/_unir.py
"""
import importlib.util
import json
import re
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PROP = AQUI.parent
FUENTES = {k: PROP / ("zoom-inn006-%s" % k.lower()) for k in "ABC"}
NOMBRE = {"A": "Bootcamp de varias áreas", "B": "Un encuentro por área", "C": "Por área y bootcamp abierto"}

# Números por opción: se leen del builder de las tres opciones (fuente única).
_spec = importlib.util.spec_from_file_location("opciones", FUENTES["A"] / "_construir-opciones.py")
_op = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_op)
_ses, _total_areas, R = _op.calcular()

# Orden de la propuesta única: (clave de la lámina, opción de la que se toma)
ORDEN = [("s-cover", "A"), ("s-chg", "A"), ("s-cmp", None),
         ("s-scope", "A"), ("s-route", "A"), ("s-cal", "A"),
         ("s-scope", "B"), ("s-route", "B"), ("s-cal", "B"),
         ("s-scope", "C"), ("s-route", "C"), ("s-cal", "C"),
         ("s-method", "A"), ("s-roi", "A"),
         ("s-price", "A"), ("s-price", "B"), ("s-price", "C"),
         ("s-pay", "A"), ("s-pay", "B"), ("s-pay", "C"),
         ("s-next", "A")]
N = len(ORDEN)
CON_OPCION = {"s-scope", "s-route", "s-cal", "s-price", "s-pay"}


def secciones(opc):
    s = (FUENTES[opc] / "index.html").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<section class="slide ([^"]*)">(.*?)</section>', s, re.S):
        clave = m.group(1).split()[0]
        out[clave] = (m.group(1), m.group(2))
    return out


def comparativa(n):
    h = R
    tarjetas = [
        ("A", NOMBRE["A"], [
            ("Personas", "510 personas, en bootcamps de hasta 25."),
            ("Encuentros", "%d de 2 horas: %d en noviembre y %d de margen en enero y febrero." % (h["A"]["n"], h["A"]["nov"], h["A"]["ene"])),
            ("Horas de encuentro", "%d h, con 2 facilitadores por encuentro." % h["A"]["h_ses"]),
            ("Horas de trabajo", "%d h en total." % h["A"]["total"]),
            ("Cuotas", "40 %, 30 % y 30 %, ligadas a hitos."),
        ]),
        ("B", NOMBRE["B"], [
            ("Personas", "%d personas en seis áreas, en grupos de hasta 25." % _total_areas),
            ("Encuentros", "%d de 2 horas, todos antes de diciembre." % h["B"]["n"]),
            ("Horas de encuentro", "%d h, con 1 facilitador por encuentro." % h["B"]["h_ses"]),
            ("Horas de trabajo", "%d h en total." % h["B"]["total"]),
            ("Cuotas", "50 % y 50 %, ligadas a hitos."),
        ]),
        ("C", NOMBRE["C"], [
            ("Personas", "%d personas en seis áreas, más un bootcamp para quienes no estuvieron (se estima el 15 %%: %d personas)." % (_total_areas, h["C"]["ausentes"])),
            ("Encuentros", "%d de 2 horas: %d por área en noviembre y %d bootcamp en enero." % (h["C"]["n"], h["C"]["n_areas"], h["C"]["n_boot"])),
            ("Horas de encuentro", "%d h, con 1 facilitador por área y 2 en el bootcamp." % h["C"]["h_ses"]),
            ("Horas de trabajo", "%d h en total." % h["C"]["total"]),
            ("Cuotas", "40 %, 30 % y 30 %, ligadas a hitos."),
        ]),
    ]
    cols = ""
    for letra, nom, filas in tarjetas:
        li = "".join("            <li><span>%s</span><b>%s</b></li>\n" % (a, b) for a, b in filas)
        cols += (
            '        <div class="cmp-card acc-%s">\n'
            '          <div class="cmp-head"><span class="cmp-letra">%s</span><span class="cmp-nom">%s</span></div>\n'
            '          <ul>\n%s          </ul>\n'
            "        </div>\n" % ("y" if letra != "B" else "o", letra, nom, li)
        )
    return (
        '    <section class="slide s-cmp">\n'
        '      <span class="counter">03 / %d</span>\n'
        '      <p class="eyebrow">03 · Las tres opciones</p>\n'
        "      <h2>Tres alternativas para llevar los Gems a Skills.</h2>\n"
        '      <p class="sub">Cada opción tiene su propio cálculo de personas, encuentros y horas. El detalle está en su alcance, su calendario y su inversión.</p>\n\n'
        '      <div class="cmp-grid">\n%s      </div>\n\n'
        '      <div class="foot">\n'
        '        <img src="../../../logos/educacion/NEGRO.png" alt="">\n'
        '        <span class="meta">Zoom · INN-006</span>\n'
        "      </div>\n"
        "    </section>\n" % (N, cols)
    )


def adaptar(clave, opc, clase, cuerpo, pos):
    """Renumera, rotula la opción y ajusta lo que era propio de una sola opción."""
    num = "%02d" % pos
    cuerpo = re.sub(r'<span class="counter">\d+ / \d+</span>', '<span class="counter">%s / %d</span>' % (num, N), cuerpo)
    etiqueta = (" · Opción %s" % opc) if clave in CON_OPCION else ""
    cuerpo = re.sub(r'(<p class="eyebrow">)\d+ · ([^<]*)(</p>)', lambda m: '%s%s · %s%s%s' % (m.group(1), num, m.group(2), etiqueta, m.group(3)), cuerpo)
    meta = "Zoom · INN-006 · Opción %s" % opc if clave in CON_OPCION else "Zoom · INN-006"
    cuerpo = re.sub(r'Zoom · INN-006-[ABC]', meta, cuerpo)
    if clave == "s-cover":
        cuerpo = re.sub(r'<h1 style="font-size:54px">.*?</h1>',
                        '<h1 style="font-size:54px">\n          Gems a Skills en tres<br>\n          alternativas para<br>\n          <span class="hl">Zoom</span>\n        </h1>', cuerpo, flags=re.S)
        cuerpo = re.sub(r'<p class="lead">.*?</p>',
                        '<p class="lead">\n          Zoom puede llevar sus <strong>Gems</strong> a <strong>Skills</strong> de tres maneras: un bootcamp de varias áreas, un encuentro por área o un encuentro por área con un bootcamp abierto, antes de que Google deje de ofrecer los Gems.\n        </p>',
                        cuerpo, count=1, flags=re.S)
        cuerpo = cuerpo.replace("Código: INN-006-A", "Código: INN-006")
    if clave == "s-method":
        cuerpo = cuerpo.replace("La misma agenda en las tres opciones: se llega con el inventario hecho y las 2 horas son de práctica.",
                                "La misma agenda en las tres opciones: se llega con el inventario hecho y las 2 horas son de práctica.")
        cuerpo = re.sub(r'(<span>Participantes</span><b>)[^<]*(</b>)', r'\1Hasta 25 personas por encuentro; el total de cada opción está en su alcance.\2', cuerpo)
    if clave == "s-price":
        cuerpo = cuerpo.replace("Inversión del proyecto.", "Inversión de la opción %s." % opc)
    if clave == "s-next":
        cuerpo = cuerpo.replace("<b>Fecha y asistentes</b>", "<b>Opción y asistentes</b>")
        cuerpo = cuerpo.replace("Confirmamos con Zoom el arranque a partir del 2 de noviembre y quiénes asisten a cada encuentro.",
                                "Confirmamos con Zoom cuál de las tres opciones sigue, el arranque a partir del 2 de noviembre y quiénes asisten.")
        cuerpo = cuerpo.replace("Esto es lo que sigue cuando Zoom confirme la propuesta.", "Esto es lo que sigue cuando Zoom elija una opción.")
    return '    <section class="slide %s">%s</section>\n' % (clase, cuerpo)


def programa(opc):
    ac = json.loads((FUENTES[opc] / "acroforms.json").read_text(encoding="utf-8"))
    pr = [re.sub(r"INN-006-[ABC]", "INN-006, opción %s" % opc, x) for x in ac["Programa"]]
    return pr, ac["Notas"]


def main():
    ssec = {k: secciones(k) for k in "ABC"}
    html = ""
    for pos, (clave, opc) in enumerate(ORDEN, 1):
        if clave == "s-cmp":
            html += comparativa(pos) + "\n"
            continue
        clase, cuerpo = ssec[opc][clave]
        html += adaptar(clave, opc, clase, cuerpo, pos) + "\n"

    cabecera = (FUENTES["A"] / "index.html").read_text(encoding="utf-8")
    cabecera = cabecera[:cabecera.index("<main class=\"deck\">")]
    cabecera = re.sub(r"<!--.*?-->", "<!--\n  Propuesta · Zoom · Servicio de Innovación (INN-006): las tres alternativas A, B y C en una sola propuesta.\n"
                      "  División: Educación · Servicio: Innovación (§4.1a) · Alianza: no\n"
                      "  ARMADO por _unir.py a partir de las láminas generadas de zoom-inn006-a, -b y -c (no editar a mano: regenerar).\n"
                      "  Marcadores de AcroForms (agregar-campo-precio.py): «Propuesta Económica» en las 3 hojas de inversión y «Facilidad de pago» en las 3 de pago;\n"
                      "  los campos de la 2.ª y 3.ª instancia llevan el sufijo _2 y _3.\n-->", cabecera, count=1, flags=re.S)
    doc = cabecera + '<main class="deck">\n\n' + html + "  </main>\n\n</body>\n</html>\n"
    (AQUI / "index.html").write_text(doc, encoding="utf-8")

    # CSS: el del compacto de A (misma marca) y los overrides de A más la lámina comparativa.
    shutil.copyfile(FUENTES["A"] / "habilidades-compacto.css", AQUI / "habilidades-compacto.css")
    css = (FUENTES["A"] / "overrides.css").read_text(encoding="utf-8") + CSS_CMP
    (AQUI / "overrides.css").write_text(css, encoding="utf-8")

    # AcroForms: Programa y Notas de cada hoja de inversión (la 1.ª sin sufijo, la 2.ª con _2, la 3.ª con _3).
    ac = {}
    for i, k in enumerate("ABC"):
        suf = "" if i == 0 else "_%d" % (i + 1)
        pr, nt = programa(k)
        ac["Programa" + suf], ac["Notas" + suf] = pr, nt
    (AQUI / "acroforms.json").write_text(json.dumps(ac, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # datos.json mínimo: lo leen el verificador (frases_ok) y customize-habilidades-compacto.py (omitir). No lo lee el generador.
    base = json.loads((FUENTES["A"] / "datos.json").read_text(encoding="utf-8"))
    mini = {"_nota": "Propuesta armada con _unir.py; este archivo solo declara lo que leen los verificadores. La fuente son las tres opciones (zoom-inn006-a, -b, -c).",
            "omitir": ["entregables"], "frases_ok": base.get("frases_ok", [])}
    (AQUI / "datos.json").write_text(json.dumps(mini, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("OK: %d láminas en %s" % (N, AQUI / "index.html"))


CSS_CMP = """

/* ===========================================================================
   Lámina comparativa de las tres opciones (propuesta única INN-006, 26/10/2026)
   =========================================================================== */
.s-cmp { background: var(--white); color: var(--black); padding: 44px 56px 0; }
.s-cmp .counter { color: var(--black); }
.s-cmp .eyebrow { color: var(--orange); margin-bottom: 6px; }
.s-cmp h2 { font-family: var(--font-display); font-weight: 700; font-size: 36px; line-height: 1.05; margin-bottom: 8px; }
.s-cmp .sub { font-family: var(--font-body); font-size: 18px; line-height: 1.4; max-width: 980px; color: rgba(10, 10, 10, 0.8); }
.s-cmp .foot .meta { color: var(--black); }
.s-cmp .cmp-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 16px; }
.s-cmp .cmp-card { --c: var(--yellow); border: 1px solid rgba(0, 0, 0, 0.14); border-top: 5px solid var(--c); border-radius: 13px; padding: 16px 22px 6px; background: var(--white); }
.s-cmp .cmp-card.acc-o { --c: var(--orange); }
.s-cmp .cmp-head { display: flex; align-items: center; gap: 14px; margin-bottom: 14px; }
.s-cmp .cmp-letra { flex: none; width: 46px; height: 46px; border-radius: 50%; background: var(--c); color: var(--black); font-family: var(--font-display); font-weight: 800; font-size: 24px; line-height: 46px; text-align: center; }
.s-cmp .cmp-nom { font-family: var(--font-display); font-weight: 700; font-size: 23px; line-height: 1.15; }
.s-cmp .cmp-card ul { list-style: none; margin: 0; padding: 0; }
.s-cmp .cmp-card li { padding: 10px 0 11px; border-top: 1px solid rgba(0, 0, 0, 0.12); }
.s-cmp .cmp-card li span { display: block; font-family: var(--font-display); font-weight: 700; font-size: 12.5px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--orange); margin-bottom: 5px; }
.s-cmp .cmp-card li b { display: block; font-family: var(--font-body); font-weight: 500; font-size: 16.5px; line-height: 1.38; color: var(--black); }
"""

if __name__ == "__main__":
    main()
