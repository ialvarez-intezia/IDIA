#!/usr/bin/env python3
"""Roadmap visual de la CAI-045 (Simple TV), Brand Kit Intezia v2.1. Fuente de fechas, grupos y horas.
Uso: python3 _construir.py   (escribe index.html y el PDF con Chrome headless en esta carpeta)."""
import html, subprocess, pathlib

AQUI = pathlib.Path(__file__).resolve().parent
PDF = AQUI / "CAI-045 Roadmap Simple TV.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves"]

# Escenario A: una sesión semanal por grupo (IT lunes, Corporativo A martes, Ingeniería miércoles, Corporativo B jueves).
CAB_A = ["IT e Ingeniería (28)", "Corporativo A", "Sin sesión de grupo", "Corporativo B"]
ITE, CA, CB = ("it", "IT e Ing. · 3 h"), ("ca", "Corp. A · 2 h"), ("cb", "Corp. B · 2 h")
FILAS_A = [
    dict(sem="26 al 29 oct", fechas=["26 oct", "27", "28", "29"],
         txt="<b>Kick-off de la CAI-045:</b> hasta 1 h, fuera de las horas de la propuesta. Con la dirección del proyecto y 1 o 2 líderes: presentamos al líder de proyecto y al consultor, curamos los temarios y cerramos el calendario.",
         barra=("kick", "Kick-off de la CAI-045 · hasta 1 h"), celdas=[[], [], [("hito", "Comité")], []]),
    dict(sem="2 al 5 nov", fechas=["2 nov", "3", "4", "5"],
         txt="<b>Alineación con líderes:</b> 6 sesiones de 1 h en formato entrevista, de lunes a jueves; IT e Ingeniería por separado. <b>Webinar de lanzamiento</b> (2 h) el miércoles 4 o el jueves 5, por la tarde.",
         barra=("ali", "Alineación con líderes · 6 sesiones de 1 h"), celdas=[[], [], [("web", "Webinar · 2 h")], [("web", "Webinar · 2 h")]]),
    dict(sem="9 al 12 nov", fechas=["9 nov", "10", "11", "12"],
         txt="<b>Arrancan las sesiones:</b> una por grupo, en su día fijo.", barra=None, celdas=[[ITE], [CA], [], [CB]]),
    dict(sem="16 al 19 nov", fechas=["16 nov", "17", "18", "19"],
         txt="Una sesión por grupo.", barra=None, celdas=[[ITE], [CA], [], [CB]]),
    dict(sem="23 al 26 nov", fechas=["23 nov", "24", "25", "26"],
         txt="Una sesión por grupo.", barra=None, celdas=[[ITE], [CA], [], [CB]]),
    dict(sem="30 nov al 3 dic", fechas=["30 nov", "1 dic", "2", "3"],
         txt="<b>Última sesión</b> de cada grupo.", barra=None, celdas=[[ITE], [CA], [], [CB]]),
]

# Escenario B: dos sesiones semanales de 2 h. IT e Ingeniería comparten sesiones (mismo temario).
CAB_B = ["Corporativo", "IT e Ingeniería", "Corporativo", "IT e Ingeniería"]
ITI = ("iti", "IT e Ing. · 2 h")
FILAS_B = [
    dict(sem="9 al 12 nov", fechas=["9 nov", "10", "11", "12"],
         txt="<b>Arrancan las sesiones:</b> Corporativo A los lunes y miércoles; IT e Ingeniería los martes y jueves.",
         barra=None, celdas=[[CA], [ITI], [CA], [ITI]]),
    dict(sem="16 al 19 nov", fechas=["16 nov", "17", "18", "19"], txt="Dos sesiones por semana por grupo.",
         barra=None, celdas=[[CA], [ITI], [CA], [ITI]]),
    dict(sem="23 al 26 nov", fechas=["23 nov", "24", "25", "26"],
         txt="<b>Termina IT e Ingeniería</b> (6 sesiones). Corporativo B arranca los lunes y miércoles.",
         barra=None, celdas=[[CB], [ITI], [CB], [ITI]]),
    dict(sem="30 nov al 3 dic", fechas=["30 nov", "1 dic", "2", "3"], txt="<b>Última sesión</b> de Corporativo B.",
         barra=None, celdas=[[CB], [], [CB], []]),
]

GRUPOS = [
    ("IT e Ingeniería (un solo grupo)", "IT (17) e Ingeniería (11): mismo temario", 28, "4 sesiones de 3 h (o 6 de 2 h)", 12),
    ("Corporativo A (negocio)", "Customer Experience (10), Comercial (1), Mercadeo, Comunicaciones y Producto (5), Programación y Curaduría (1)", 17, "4 sesiones de 2 h", 8),
    ("Corporativo B (administrativo y numérico)", "Nuevos Negocios y Planificación Financiera (8), Finanzas (1), Legal (2), Talento (5), Dirección Ejecutiva, Auditoría, Riesgo y Compliance (4), PMO (5)", 25, "4 sesiones de 2 h", 8),
]
OTROS = [
    ("Kick-off de la CAI-045", "Dirección del proyecto y 1 o 2 líderes", "hasta 1 h", "no suma a las horas"),
    ("Alineación con líderes", "Líderes que defina el cliente; IT e Ingeniería por separado", "6 sesiones de 1 h", "6 h"),
    ("Webinar de lanzamiento", "Toda la organización", "1 sesión de 2 h", "2 h"),
    ("Entrenamiento de Claude", "12 directivos, presencial", "1 grupo de 3 h", "3 h"),
]

e = html.escape


def calendario(filas, cab, extra=""):
    out = [f'<div class="cal{extra}">', '<div class="ch">Semana</div>', '<div class="ch dh">']
    for d, c in zip(DIAS, cab):
        out.append(f'<div><b>{d}</b><span>{e(c)}</span></div>')
    out.append('</div><div class="ch">Qué pasa esta semana</div>')
    for f in filas:
        out.append(f'<div class="cw">{e(f["sem"])}</div><div class="cd">')
        if f["barra"]:
            out.append(f'<div class="barra {f["barra"][0]}">{e(f["barra"][1])}</div>')
        out.append('<div class="dias">')
        for fecha, cel in zip(f["fechas"], f["celdas"]):
            chips = "".join(f'<span class="chip {c}">{e(t)}</span>' for c, t in cel)
            out.append(f'<div class="dia"><i>{e(fecha)}</i>{chips}</div>')
        out.append('</div></div>')
        out.append(f'<div class="ct">{f["txt"]}</div>')
    out.append('</div>')
    return "".join(out)


def tabla():
    r = ['<table class="horas"><thead><tr><th>Grupo</th><th>Áreas</th><th class="n">Personas</th><th>Sesiones</th><th class="n">Horas</th></tr></thead><tbody>']
    for g, a, p, s, h in GRUPOS:
        r.append(f'<tr><td><b>{e(g)}</b></td><td class="ar">{e(a)}</td><td class="n">{p}</td><td>{e(s)}</td><td class="n"><b>{h} h</b></td></tr>')
    r.append('<tr class="sub"><td colspan="2">Sesiones con los grupos</td><td class="n">70</td><td></td><td class="n"><b>28 h</b></td></tr>')
    r.append('</tbody></table>')
    r.append('<table class="horas otros"><thead><tr><th>Otros momentos</th><th>Quiénes</th><th>Formato</th><th class="n">Horas</th></tr></thead><tbody>')
    for n, q, f, h in OTROS:
        r.append(f'<tr><td><b>{e(n)}</b></td><td class="ar">{e(q)}</td><td>{e(f)}</td><td class="n"><b>{e(h)}</b></td></tr>')
    r.append('</tbody></table>')
    return "".join(r)


CSS = """
@font-face { font-family:'Poppins'; src:url('../../_base/fonts/poppins-400.woff2') format('woff2'); font-weight:400; }
@font-face { font-family:'Poppins'; src:url('../../_base/fonts/poppins-600.woff2') format('woff2'); font-weight:600; }
@font-face { font-family:'Poppins'; src:url('../../_base/fonts/poppins-700.woff2') format('woff2'); font-weight:700; }
@font-face { font-family:'Poppins'; src:url('../../_base/fonts/poppins-800.woff2') format('woff2'); font-weight:800; }
:root { --black:#0A0A0A; --yellow:#FFD300; --orange:#E58423; --white:#FFFFFF; --line:rgba(255,255,255,.16); --soft:rgba(255,255,255,.06); --mute:rgba(255,255,255,.74); }
@page { size: 297mm 210mm; margin: 0; }
* { box-sizing:border-box; margin:0; padding:0; }
html, body { background:var(--black); font-family:'Poppins','Inter',system-ui,sans-serif; color:var(--white); -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.page { width:297mm; height:210mm; padding:24px 38px 20px; position:relative; overflow:hidden; page-break-after:always; display:flex; flex-direction:column; }
.page:last-child { page-break-after:auto; }
.top { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }
.top img { height:58px; margin:-16px 0 -16px -8px; }
.eyebrow { font-size:10.5px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--yellow); }
h1 { font-size:24px; line-height:1.15; font-weight:800; letter-spacing:-.015em; margin-bottom:3px; }
h1 em { font-style:normal; color:var(--yellow); }
.sub1 { font-size:12px; color:var(--mute); margin-bottom:9px; }
.fases { display:grid; grid-template-columns:1fr 1.5fr; gap:10px; margin-bottom:10px; }
.fase { border-radius:8px; padding:7px 14px; font-size:11px; line-height:1.35; color:var(--black); }
.fase b { display:block; font-size:12.5px; font-weight:800; letter-spacing:.06em; text-transform:uppercase; }
.fase.act { background:var(--yellow); } .fase.apr { background:var(--orange); }

.cal { display:grid; grid-template-columns:92px 1fr 270px; column-gap:0; }
.ch { font-size:9.5px; text-transform:uppercase; letter-spacing:.1em; color:var(--yellow); font-weight:700; padding:0 8px 5px; border-bottom:1px solid var(--line); align-self:end; }
.ch.dh { display:grid; grid-template-columns:repeat(4,1fr); padding:0; }
.ch.dh div { padding:0 8px 5px; display:flex; flex-direction:column; }
.ch.dh b { font-size:10px; letter-spacing:.1em; }
.ch.dh span { font-size:9px; color:var(--mute); font-weight:400; letter-spacing:.02em; text-transform:none; }
.cw { font-size:11.5px; font-weight:700; padding:9px 8px; border-bottom:1px solid var(--line); display:flex; align-items:flex-start; }
.cd { border-bottom:1px solid var(--line); display:flex; flex-direction:column; padding:5px 0; gap:4px; }
.dias { display:grid; grid-template-columns:repeat(4,1fr); gap:5px; flex:1; padding:0 4px; }
.dia { background:var(--soft); border-radius:5px; padding:4px 6px; min-height:36px; display:flex; flex-direction:column; gap:3px; }
.dia i { font-style:normal; font-size:8.5px; color:var(--mute); letter-spacing:.02em; }
.ct { font-size:10px; line-height:1.38; color:var(--mute); padding:8px 4px 8px 12px; border-bottom:1px solid var(--line); }
.ct b { color:var(--white); font-weight:700; }
.barra { margin:0 4px; border-radius:5px; padding:4px 10px; font-size:10.5px; font-weight:700; color:var(--black); }
.barra.kick { background:var(--yellow); } .barra.ali { background:var(--orange); }
.chip { font-size:10px; font-weight:700; border-radius:4px; padding:2px 6px; display:inline-block; align-self:flex-start; }
.chip.it { background:var(--yellow); color:var(--black); }
.chip.ing { background:var(--white); color:var(--black); }
.chip.ca { background:var(--orange); color:var(--black); }
.chip.cb { background:transparent; color:var(--yellow); border:1.5px solid var(--yellow); }
.chip.iti { background:var(--white); color:var(--black); }
.chip.web { background:transparent; color:var(--yellow); border:1.5px dashed var(--yellow); }
.chip.hito { background:var(--white); color:var(--black); }
.compact .dia { min-height:0; flex-direction:row; align-items:center; gap:6px; padding:4px 6px; }
.compact .cw { padding:7px 8px; } .compact .ct { padding:6px 4px 6px 12px; }
.claude { margin-top:10px; border:1.5px solid var(--yellow); border-radius:8px; padding:8px 14px; font-size:11px; line-height:1.4; display:flex; gap:14px; align-items:center; }
.claude b { color:var(--yellow); font-weight:700; }
.equipo { margin-top:8px; display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; }
.eq { font-size:10px; line-height:1.4; color:var(--mute); padding:0 2px; }
.eq b { color:var(--white); display:block; font-size:10.5px; }
.pie { margin-top:auto; display:flex; justify-content:space-between; font-size:9px; color:var(--mute); padding-top:8px; }

h2 { font-size:16px; font-weight:800; color:var(--yellow); letter-spacing:-.005em; margin:8px 0 5px; }
.nota { font-size:10px; color:var(--mute); margin-top:6px; }
table.horas { width:100%; border-collapse:collapse; font-size:11.5px; line-height:1.35; margin-bottom:12px; }
table.horas td:nth-child(4) { white-space:nowrap; }
table.horas th { text-align:left; color:var(--yellow); font-size:10px; text-transform:uppercase; letter-spacing:.1em; padding:0 8px 5px; border-bottom:1px solid var(--line); }
table.horas td { padding:8px 8px; border-bottom:1px solid var(--line); vertical-align:top; }
table.horas td.ar { color:var(--mute); }
table.horas .n { text-align:right; white-space:nowrap; }
table.horas td b { color:var(--white); }
table.horas tr.sub td { background:var(--soft); font-weight:700; }
"""


def pagina(cuerpo, n):
    return f"""<section class="page">
  <div class="top"><img src="../../../../logos/educacion/BLANCO.png" alt="Intezia Educación"><span class="eyebrow">Roadmap · CAI-045 · Simple TV</span></div>
{cuerpo}
  <div class="pie"><span>Intezia Educación · CAI-045</span><span>Horas de 60 minutos · {n} / 2</span></div>
</section>"""


def main():
    p1 = f"""  <h1>Roadmap de la CAI-045 en Simple TV, <em>de octubre a diciembre de 2026</em></h1>
  <p class="sub1">Escenario A: una sesión semanal por grupo, en su día fijo, de lunes a jueves, desde las 3 p. m.</p>
  <div class="fases">
    <div class="fase act"><b>Activa</b>Comunicación, webinar de lanzamiento y entrenamiento de directivos</div>
    <div class="fase apr"><b>Aprende</b>Sesiones por grupo: IT e Ingeniería (un solo grupo de 28) y Corporativo A y B</div>
  </div>
  {calendario(FILAS_A, CAB_A)}
  <div class="claude"><span><b>Entrenamiento de Claude para 12 directivos</b> · 3 h · presencial · en noviembre o diciembre, con fecha por acordar (o en enero, según la aprobación de la gerencia general).</span></div>
  <div class="equipo">
    <div class="eq"><b>Horario</b>IT e Ingeniería, de 3 a 6 p. m.; Corporativo, de 3 a 5 p. m. Sin viernes.</div>
    <div class="eq"><b>Líder de proyecto</b>Coordina con el cliente el calendario y los cambios de sesiones.</div>
    <div class="eq"><b>Consultor</b>Facilita los encuentros y cura los temarios con el cliente.</div>
  </div>"""
    p2 = f"""  <h1>Escenario B: <em>dos sesiones por semana</em>, de 2 h cada una</h1>
  <p class="sub1">Corporativo A los lunes y miércoles; IT e Ingeniería los martes y jueves; Corporativo B toma los lunes y miércoles cuando termina el A. Desde las 3 p. m.</p>
  {calendario(FILAS_B, CAB_B, ' compact')}
  <p class="nota">IT e Ingeniería son un solo grupo de 28 con el mismo temario: 6 sesiones de 2 h. Sus alineaciones con líderes van por separado, igual que en el escenario A.</p>
  <h2>Distribución de horas por grupo</h2>
  {tabla()}"""
    doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><title>CAI-045 Roadmap del proyecto de inteligencia artificial en Simple TV</title>
<style>{CSS}</style></head><body>
{pagina(p1, 1)}
{pagina(p2, 2)}
</body></html>"""
    (AQUI / "index.html").write_text(doc, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={PDF}", f"file://{AQUI / 'index.html'}"], check=True, capture_output=True)
    print("OK", PDF)


if __name__ == "__main__":
    main()
