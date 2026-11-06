#!/usr/bin/env python3
"""
generar-kickoff.py — Genera el Brief de Kick-off (v2) de una propuesta compacta de Detección o Habilidades.

El kick-off es la puerta de entrada del cliente al servicio (acuerdos del 26/10/2026): se muestra la ruta, se marca con el
cliente el checklist técnico y se agenda en vivo al menos el 50 % de las horas (mejor el 60 %). Un solo documento sirve
para enviar a Ventas el brief de una página 48 horas hábiles antes, para compartir pantalla en la llamada y para dar al
cliente el PDF con lo acordado.

Lee
  clientes/propuestas/<slug>/datos.json   (la propuesta compacta: etapas, áreas, horas, asesora; no se modifica)
  clientes/propuestas/<slug>/kickoff.json (lo propio del kick-off: checklist, fechas tentativas, sesiones propuestas, dudas)
Escribe
  clientes/propuestas/<slug>/kickoff.html (autocontenido: logos incrustados; se abre con doble clic)

Las horas salen del mismo cálculo que el generador de la propuesta (scripts/generar-habilidades-compacto.py): nunca se
escriben a mano. El checklist técnico varía por propuesta: se define con el usuario y se escribe en kickoff.json.

Uso
    python3 scripts/generar-kickoff.py <slug> --aprobada        # escribe clientes/propuestas/<slug>/kickoff.html
    python3 scripts/generar-kickoff.py <slug> --salida RUTA     # prueba: otra ruta, sin exigir --aprobada
    --datos RUTA / --kickoff RUTA   usar otros archivos de entrada
    --forzar                        sobrescribir un kickoff.html que no fue generado por este script

--aprobada es la confirmación del usuario de que la propuesta está aprobada (plantillas/brief-kickoff.md §1, bloqueante).
Plantilla del HTML: plantillas/kickoff-canonico/kickoff-v2.template.html. Plantilla del kickoff.json:
plantillas/kickoff-canonico/kickoff.plantilla.json.
"""
import argparse
import base64
import hashlib
import importlib.util
import json
import re
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA = RAIZ / "plantillas" / "kickoff-canonico" / "kickoff-v2.template.html"
ESTILO_CANONICO = RAIZ / "plantillas" / "kickoff-canonico" / "kickoff-estilo.css"
MARCA_GENERADO = "generado-por: scripts/generar-kickoff.py"
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
HORA = re.compile(r"^\d{2}:\d{2}$")
# El kick-off es logística y narrativa de la ruta: sin términos económicos (CLAUDE.md §4.15) ni guion largo (§4.13).
MODALIDADES = ("Presencial", "Online")
ECONOMICOS = re.compile(r"\b(precio|costo|factura|anticipo|pago|cuota|cobro|descuento)s?\b", re.I)


def cargar_generador():
    sp = importlib.util.spec_from_file_location("gen_compacto", RAIZ / "scripts" / "generar-habilidades-compacto.py")
    g = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(g)
    return g


def md(t):
    """Escapa HTML y convierte **x** en <strong>x</strong>."""
    import html
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html.escape(str(t), quote=False))


def plano(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", str(t))


def resolver(texto, ctx, donde, errores):
    """Sustituye {tokens} del contexto de la propuesta; un token desconocido es un error."""
    def r(m):
        k = m.group(1)
        if k in ctx:
            return str(ctx[k])
        errores.append("%s: token desconocido {%s}" % (donde, k))
        return m.group(0)
    return re.sub(r"\{\s*([^{}\s]+)\s*\}", r, texto) if isinstance(texto, str) else texto


def recorrer(nodo, ruta=""):
    """Todas las cadenas de un JSON con su ruta."""
    if isinstance(nodo, str):
        yield ruta, nodo
    elif isinstance(nodo, dict):
        for k, v in nodo.items():
            if not str(k).startswith("_"):
                yield from recorrer(v, "%s.%s" % (ruta, k) if ruta else k)
    elif isinstance(nodo, list):
        for i, v in enumerate(nodo):
            yield from recorrer(v, "%s[%d]" % (ruta, i))


def logo(nombre):
    p = RAIZ / "logos" / "intezia" / nombre
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode("ascii")


def etapa_de_detalle(e):
    return {"titulo": e["titulo"], "texto": e["texto"], "horas": e.get("horas")}


def armar_deteccion(g, d, ctx, k, errores):
    det = d["deteccion"]
    areas = [a for a in det.get("areas") or [] if isinstance(a, str)]
    deptos = [x for x in det.get("departamentos") or [] if isinstance(x, str)]
    h_lev, h_niv = ctx["h_levantamiento"], ctx["h_nivelacion"]
    etapas, tiene_arranque = [], False
    for e in det.get("etapas") or []:
        t = e.get("titulo", "")
        low = t.lower()
        et = {"titulo": t, "texto": plano(resolver(e.get("texto", ""), ctx, "deteccion.etapas", errores)), "horas": None, "badge": None, "now": False}
        if "arranque" in low:
            tiene_arranque, et["now"], et["badge"] = True, True, "Hoy"
        elif "nivelaci" in low:
            et["horas"] = h_niv or None
        elif "levantamiento" in low:
            et["horas"] = h_lev
        elif "priorizaci" in low:
            et["badge"] = "Automático"
        etapas.append(et)
    if not tiene_arranque:
        etapas.insert(0, {"titulo": "Kick-off", "texto": ("Presentamos la ruta y agendamos el calendario." if k.get("sin_checklist") else "Presentamos la ruta, marcamos lo técnico y agendamos el calendario."), "horas": None, "badge": "Hoy", "now": True})
    grupos = []
    if h_niv:
        grupos.append({"id": "niv", "titulo": "Nivelación en IA", "horas": h_niv, "sub": "Fundamentos de IA para todo el equipo.", "chips": ["Nivelación del equipo"]})
    grupos.append({"id": "lev", "titulo": "Levantamiento por departamento", "horas": h_lev, "sub": "Un espacio por departamento, con su líder y su mano derecha.", "chips": areas})
    grupos.append({"id": "inf", "titulo": "Informe Final", "horas": None, "sin_horas": True, "sub": "Presentación a la dirección.", "chips": [], "fijas": ["Presentación del Informe Final a la dirección"], "dur_fija": 1})
    total = h_lev + h_niv
    se_llevan = [plano(x.get("titulo", "")) for x in (det.get("entregables") or []) if isinstance(x, dict) and x.get("titulo")]
    resumen = ["Áreas del levantamiento: " + ", ".join(areas),
               "Horas: %d h de levantamiento%s" % (h_lev, (" y %d h de nivelación en IA" % h_niv) if h_niv else ""),
               "Logros inmediatos: al menos %s en el proyecto" % ctx["logros_minimos_palabra"]]
    return etapas, grupos, total, sorted(set(deptos + areas), key=str.lower), se_llevan, resumen


def armar_habilidades(g, d, ctx, agg, k, errores):
    etapas = [{"titulo": "Kick-off", "texto": ("Presentamos la ruta y agendamos el calendario." if k.get("sin_checklist") else "Presentamos la ruta, marcamos lo técnico y agendamos el calendario."), "horas": None, "badge": "Hoy", "now": True}]
    grupos, sugerencias = [], []
    areas = d.get("areas") or []
    for f in d.get("fases") or []:
        fid = f.get("id")
        h = agg["fase"].get(fid, [0, 0])[1]
        # El generador de la propuesta solo admite horas enteras: una fase con medias horas se corrige aquí (kickoff.json → horas_por_fase).
        h = (k.get("horas_por_fase") or {}).get(fid, h)
        titulo = f.get("titulo") or ("Arranque" if fid == "F0" else fid)
        desc = plano(resolver(f.get("descripcion", ""), ctx, "fases[%s].descripcion" % fid, errores))
        etapas.append({"titulo": titulo, "texto": desc[:1].upper() + desc[1:] if desc else "", "horas": h or None, "badge": None, "now": False})
        nombres = [a["nombre"] for a in areas if any(s.get("fase") == fid for s in a.get("soluciones") or [])]
        sugerencias += nombres
        grupos.append({"id": str(fid).lower(), "titulo": titulo, "horas": h, "sub": desc, "chips": nombres})
    if k.get("cierre_medicion", True):
        etapas.append({"titulo": "Cierre y medición", "texto": "72 horas después de la última sesión: Edu-Trace, certificados y dashboard de impacto. No requiere agenda propia.", "horas": None, "badge": "Automático", "now": False})
    seg = d.get("seguimiento") or {}
    if g.seg_hay_columna(d) and g.seg_es_seguimiento(d):
        # El seguimiento se menciona en la ruta, pero no se agenda en el kick-off: sin fechas ni sesiones (Ivana, 28/10/2026).
        items = [x for x in (seg.get("items") or []) if isinstance(x, dict)]
        texto = "El servicio incluye check-ins de seguimiento a %s%s. No se agendan hoy." % (seg.get("rango", ""), (": " + "; ".join("%s, %s" % (x.get("dias", ""), x.get("texto", "").lower()) for x in items)) if items else "")
        if k.get("seguimiento_texto"):   # kickoff.json → seguimiento_texto: redacción propia (p. ej. «tres encuentros de 30 minutos»)
            texto = str(k["seguimiento_texto"])
        etapas.append({"titulo": "Seguimiento", "texto": texto, "horas": None, "badge": None, "now": False})
    total = ctx["h_total"]
    resumen = ["Áreas: " + ", ".join(dict.fromkeys(a["nombre"] for a in areas)),
               "Horas de trabajo del proyecto: %d h" % total]
    return etapas, grupos, total, sorted(set(sugerencias), key=str.lower), [], resumen


def construir(slug, datos_p, kick_p):
    errores, avisos = [], []
    g = cargar_generador()
    d = json.loads(datos_p.read_text(encoding="utf-8"))
    k = json.loads(kick_p.read_text(encoding="utf-8")) if kick_p.exists() else {}
    rep = g.Reporte()
    es_det = g.es_deteccion(d)
    if es_det:
        g.aplicar_defaults_det(d)
        ctx, agg = g.calcular_det(d, rep)
    else:
        ctx, agg = g.calcular(d, rep)
    if rep.errores:
        errores += ["datos.json (corre el generador de la propuesta): " + e for e in rep.errores]
        return None, errores, avisos

    cl = d.get("cliente") or {}
    corto = cl.get("nombre_pie") or cl.get("nombre", "")
    rotulo = (d.get("servicio_rotulo") or ("Servicio de Detección" if es_det else "Servicio de Habilidades")).strip()
    if es_det:
        etapas, grupos, total, sugerencias, se_llevan, resumen = armar_deteccion(g, d, ctx, k, errores)
    else:
        etapas, grupos, total, sugerencias, se_llevan, resumen = armar_habilidades(g, d, ctx, agg, k, errores)
    # Grupos de sesiones extra (kickoff.json → grupos_extra), p. ej. las sesiones de quick wins de FUTVE después del
    # levantamiento: {"id": "qw", "titulo": "Quick wins", "sesiones": 5, "duracion": 2, "despues_de": "lev", "sub": "..."}.
    # Nacen sin fecha («Por agendar») y, por defecto, sin horas: no cuentan para la barra del 50 % (sin_horas).
    for i, ge in enumerate(k.get("grupos_extra") or []):
        donde = "kickoff.json → grupos_extra[%d]" % i
        if not isinstance(ge, dict) or not ge.get("id") or not ge.get("titulo"):
            errores.append("%s: falta id o titulo" % donde)
            continue
        if any(x["id"] == ge["id"] for x in grupos):
            errores.append("%s.id: «%s» ya existe" % (donde, ge["id"]))
            continue
        n = ge.get("sesiones", 0)
        if not isinstance(n, int) or n < 0 or n > 20:
            errores.append("%s.sesiones: debe ser un entero entre 0 y 20" % donde)
            continue
        nuevo = {"id": ge["id"], "titulo": ge["titulo"], "horas": ge.get("horas"), "sin_horas": ge.get("sin_horas", True),
                 "sub": ge.get("sub", ""), "chips": ge.get("chips") or [],
                 "fijas": ["%s · sesión %d" % (ge.get("prefijo", ge["titulo"]), j + 1) for j in range(n)],
                 "dur_fija": ge.get("duracion", k.get("duracion_defecto", 2))}
        ref = ge.get("despues_de", "lev")
        pos = next((j for j, x in enumerate(grupos) if x["id"] == ref), None)
        if pos is None:
            errores.append("%s.despues_de: el grupo «%s» no existe (grupos: %s)" % (donde, ref, ", ".join(x["id"] for x in grupos)))
            continue
        grupos.insert(pos + 1, nuevo)
    if isinstance(k.get("se_llevan"), list):
        se_llevan = [str(x) for x in k["se_llevan"]]
    if k.get("horas_a_agendar") is not None:
        total = k["horas_a_agendar"]
    if not isinstance(total, (int, float)) or total <= 0:
        errores.append("horas a agendar: debe ser un número mayor que 0 (kickoff.json → horas_a_agendar)")

    # --- checklist técnico: varía por propuesta, lo define el usuario ---
    sin_ck = bool(k.get("sin_checklist"))   # kickoff.json → "sin_checklist": true quita las validaciones técnicas (FUTVE, 2026-10-29)
    ck = k.get("checklist")
    if sin_ck:
        ck = []
    elif not isinstance(ck, list) or not ck:
        errores.append("kickoff.json → checklist: falta. El checklist técnico varía por propuesta: pregúntaselo al usuario antes de generar (plantillas/brief-kickoff.md §9)")
        ck = []
    checklist = []
    for i, it in enumerate(ck):
        if not isinstance(it, dict) or not it.get("titulo"):
            errores.append("kickoff.json → checklist[%d]: falta titulo" % i)
            continue
        checklist.append({"id": "c%d" % (i + 1), "titulo": it["titulo"], "detalle": it.get("detalle", "")})

    # --- sesiones propuestas (a partir de las fechas tentativas de Ventas) ---
    ids = {x["id"] for x in grupos}
    dur = k.get("duracion_defecto", 2)
    propuestas = []
    for i, p in enumerate(k.get("sesiones_propuestas") or []):
        donde = "kickoff.json → sesiones_propuestas[%d]" % i
        if p.get("grupo") not in ids:
            errores.append("%s.grupo: «%s» no existe (grupos: %s)" % (donde, p.get("grupo"), ", ".join(sorted(ids))))
            continue
        if p.get("fecha") and not FECHA.match(p["fecha"]):
            errores.append("%s.fecha: debe ser AAAA-MM-DD" % donde)
        if p.get("hora") and not HORA.match(p["hora"]):
            errores.append("%s.hora: debe ser HH:MM" % donde)
        if p.get("modalidad") and p["modalidad"] not in MODALIDADES:
            errores.append("%s.modalidad: debe ser Presencial u Online" % donde)
        propuestas.append({"g": p["grupo"], "t": p.get("titulo", ""), "f": p.get("fecha", ""), "h": p.get("hora", ""), "du": p.get("duracion", dur), "mo": p.get("modalidad", "")})
    prop_h = sum(p["du"] for p in propuestas if p["f"] and not next(x for x in grupos if x["id"] == p["g"]).get("sin_horas"))
    if prop_h > total:
        avisos.append("las sesiones propuestas suman %s h, más que las %s h a agendar" % (prop_h, total))
    if k.get("modalidad") and k["modalidad"] not in MODALIDADES:
        errores.append("kickoff.json → modalidad: debe ser Presencial u Online")
    kk = k.get("kickoff") or {}
    for campo, rx in (("fecha", FECHA), ("hora", HORA)):
        if kk.get(campo) and not rx.match(kk[campo]):
            errores.append("kickoff.json → kickoff.%s: formato inválido" % campo)

    asesora = ((d.get("proximos_pasos") or {}).get("asesora")) if isinstance(d.get("proximos_pasos"), dict) else None
    dudas = [str(x) for x in (k.get("dudas") or [])]
    # Quien resuelve dudas y preguntas del cliente durante el servicio (puede no ser la asesora comercial).
    consultas = k.get("contacto_dudas") if isinstance(k.get("contacto_dudas"), dict) and k["contacto_dudas"].get("nombre") else None
    if not asesora:
        avisos.append("datos.json no trae proximos_pasos.asesora: el kick-off no mostrará contacto comercial")

    # --- higiene de texto (§4.13, §4.15) ---
    for ruta, t in recorrer(k):
        if "—" in t or "–" in t:
            errores.append("kickoff.json → %s: guion largo (§4.13)" % ruta)
        if ECONOMICOS.search(t):
            errores.append("kickoff.json → %s: término económico (§4.15): el kick-off es logística, no cierre comercial" % ruta)
        if "info@intezia.com" in t:
            errores.append("kickoff.json → %s: usar servicio@intezia.com" % ruta)

    bienv = k.get("bienvenida") or (
        "Hoy les mostramos cómo vamos a trabajar juntos en {c}: la ruta del servicio%s y el calendario. "
        "Ya contamos con lo que nos compartieron en la venta, así que no vamos a volver a preguntarlo.").replace("{c}", corto)
    if not k.get("bienvenida"):
        bienv = bienv % ("" if sin_ck else ", lo que necesitamos de ustedes") if "%s" in bienv else bienv
    gracias = k.get("gracias") or "Gracias por confiar en Intezia. Nos alegra acompañar a %s en este camino y estamos listos para empezar." % corto
    callout = ("Estudia antes la propuesta (<b>%s</b>), la Ficha Comercial, los correos y la transcripción del levantamiento. "
               "Lo que el cliente ya dijo en la venta no se vuelve a preguntar: solo se valida y se cierra lo operativo. "
               "Lleva una propuesta de calendario hecha con las fechas tentativas de Ventas y la ruta%s. "
               "La consultoría asignada se presenta y no hace preguntas técnicas que ya se respondieron. Ventas participa como oyente cuando pueda." % (md(cl.get("codigo", "")), "" if sin_ck else " y el checklist técnico"))
    if dudas:
        callout += "<br><br><b>Por confirmar en la llamada:</b> " + "; ".join(md(x) for x in dudas) + "."

    cfg = {
        "slug": slug, "cliente": cl.get("nombre", ""), "cliente_corto": corto, "codigo": cl.get("codigo", ""),
        "servicio": rotulo, "servicio_corto": re.sub(r"^Servicio de ", "", rotulo), "formato": "deteccion" if es_det else "habilidades",
        "lugar": "Según lo acordado con el cliente",
        "kickoff": {"fecha": kk.get("fecha", ""), "hora": kk.get("hora", ""), "consultor": kk.get("consultor", ""),
                    "lider": kk.get("lider", ""), "participantes": kk.get("participantes_cliente", "")},
        "modalidad": k.get("modalidad", ""), "asesora": asesora, "consultas": consultas, "horas_total": total, "dur": dur, "grupos": grupos, "propuestas": propuestas,
        "checklist": checklist, "dudas": dudas, "fechas_tentativas": k.get("fechas_tentativas", ""),
        "etapas": [{"titulo": e["titulo"], "texto": e["texto"], "horas": e["horas"]} for e in etapas],
        "sugerencias": sugerencias, "resumen": resumen,
    }
    cfg["huella"] = hashlib.sha1(json.dumps(cfg, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()[:10]

    # --- HTML estático: ruta, personas, textos ---
    route = []
    for i, e in enumerate(etapas, 1):
        cls = "stage" + (" now" if e["now"] else "") + (" auto" if e["badge"] == "Automático" else "")
        badge = '<span class="badge">%s</span>' % e["badge"] if e["badge"] else ""
        hrs = '\n      <span class="hrs">%s h</span>' % str(e["horas"]).replace(".", ",") if e["horas"] else ""
        route.append('    <div class="%s">\n      <span class="sn">Etapa %d</span>%s\n      <h3>%s</h3>\n      <p>%s</p>%s\n    </div>' % (cls, i, badge, md(e["titulo"]), md(e["texto"]), hrs))
    llevan = ""
    if se_llevan:
        llevan = '  <div class="llevan"><p class="lt">Lo que se llevan</p><div class="chips">%s</div></div>' % "".join('<span class="chip">%s</span>' % md(x) for x in se_llevan)
    persona = ""

    def tarjeta(rol, p):
        linea = " · ".join(x for x in (p.get("correo"), p.get("telefono")) if x)
        return ('<div class="person"><p class="role">%s</p><p class="nm">%s</p><p class="ct">%s%s</p></div>'
                % (rol, md(p.get("nombre", "")), md(p.get("cargo", "")), ("<br>" + md(linea)) if linea else ""))
    if asesora:
        persona = tarjeta("Contacto comercial", asesora)
    if consultas:
        persona += tarjeta("Dudas y preguntas", consultas)
    html = PLANTILLA.read_text(encoding="utf-8")
    mapa = {
        "TITLE": "Intezia · Kick-off · %s · %s" % (corto, rotulo), "LOGO_BLANCO": logo("BLANCO.png"), "LOGO_NEGRO": logo("NEGRO.png"),
        "CLIENTE_CORTO": md(corto), "SERVICIO_PILL": md(rotulo), "CODIGO": md(cl.get("codigo", "")), "CODIGO_OCULTO": "" if cl.get("codigo") else ' hidden',
        "BIENVENIDA": md(bienv), "GRACIAS": md(gracias), "CALLOUT": callout, "RUTA_TITULO": "Así vamos a trabajar, etapa por etapa",
        "ROUTE": "\n".join(route), "SE_LLEVAN": llevan, "PERSONA_ASESORA": persona,
        "VERSION": "%s · generada el %s" % (cfg["huella"], datetime.now().strftime("%d/%m/%Y %H:%M")),
        "CFG": json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/"),
    }
    for clave, valor in mapa.items():
        html = html.replace("{{%s}}" % clave, valor)
    if sin_ck:
        # Sin validaciones técnicas (kickoff.json → sin_checklist): se oculta la sección (los elementos siguen para el JS) y se
        # quitan el enlace, la tarjeta de portada, el minuto de la agenda, el bloque de acuerdos y las tablas de los dos PDF.
        def quita(txt, ini, fin=None, incluye_fin=False):
            i = txt.find(ini)
            if i < 0:
                errores.append("sin_checklist: la plantilla cambió y no se encontró «%s…»" % ini[:40])
                return txt
            if fin is None:
                return txt[:i] + txt[i + len(ini):]
            j = txt.find(fin, i)
            if j < 0:
                errores.append("sin_checklist: la plantilla cambió y no se encontró «%s…»" % fin[:40])
                return txt
            return txt[:i] + txt[j + (len(fin) if incluye_fin else 0):]
        html = quita(html, '<a href="#checklist">Checklist</a>')
        html = quita(html, '<span>Checklist · 7 min</span>')
        html = quita(html, '      <div class="h"><b>2 · Lo que necesitamos</b>', '</div>\n', True)
        html = html.replace("<b>3 · El calendario</b>", "<b>2 · El calendario</b>", 1)
        i0 = html.find("  <!-- ============ 3 · CHECKLIST ============ -->")
        i1 = html.find("  <!-- ============ 4 · CALENDARIO")
        if i0 < 0 or i1 < 0:
            errores.append("sin_checklist: la plantilla cambió y no se encontró la sección del checklist")
        else:
            html = html[:i0] + '  <div hidden aria-hidden="true">\n' + html[i0:i1] + '  </div>\n\n' + html[i1:]
        html = quita(html, "    h += '<div class=\"ac\"><p class=\"at\">Checklist técnico</p>", "    h += '</div>';\n", True)
        html = quita(html, "    h += '<div class=\"p-t\">Checklist técnico</div>' + tablaCk();\n", None)
        html = quita(html, "    h += '<div class=\"p-t\">Checklist técnico a validar con el cliente</div>", "    h += '<div class=\"p-t\">Propuesta de calendario</div>';")
        html = html.replace("['bienvenida','ruta','checklist','calendario','cierre']", "['bienvenida','ruta','calendario','cierre']", 1)
        html = html.replace(", lo que necesitamos de ustedes y el calendario que acordamos", " y el calendario que acordamos", 1)
        html = html.replace("se marca el checklist técnico y se agenda", "se agenda", 1)
        html = html.replace("(con la ruta, el checklist y el calendario acordados)", "(con la ruta y el calendario acordados)", 1)

    # Estilo propio del cliente (opcional): kickoff.json → "estilo_css": "archivo.css" (en la carpeta del cliente). Se inyecta
    # al final del <head> y pisa la hoja de la plantilla sin tocarla (ESTEI, 2026-10-29: Brand Kit v2.1).
    # Desde 2026-11-03 (Ivana) el estilo del Brand Kit v2.1 de Robin Agency es el de TODOS los kick-offs: si kickoff.json no trae
    # "estilo_css", se usa plantillas/kickoff-canonico/kickoff-estilo.css. "estilo_css": "ninguno" deja la plantilla oscura anterior.
    estilo = k.get("estilo_css", "canonico")
    if estilo in ("ninguno", False):
        estilo = None
    if estilo:
        ruta_css = ESTILO_CANONICO if estilo == "canonico" else kick_p.parent / estilo
        if not ruta_css.exists():
            errores.append("kickoff.json → estilo_css: no existe %s" % ruta_css)
        else:
            html = html.replace("</head>", '<style id="estilo-cliente">\n%s\n</style>\n</head>' % ruta_css.read_text(encoding="utf-8"), 1)
    sobran = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if sobran:
        errores.append("la plantilla tiene marcadores sin resolver: %s" % ", ".join(sorted(set(sobran))))
    return {"html": html, "cfg": cfg, "total": total, "prop_h": prop_h}, errores, avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("--datos")
    ap.add_argument("--kickoff")
    ap.add_argument("--salida")
    ap.add_argument("--aprobada", action="store_true", help="el usuario confirmó que la propuesta está aprobada (bloqueante)")
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    carpeta = RAIZ / "clientes" / "propuestas" / a.slug
    datos_p = Path(a.datos) if a.datos else carpeta / "datos.json"
    kick_p = Path(a.kickoff) if a.kickoff else carpeta / "kickoff.json"
    salida = Path(a.salida) if a.salida else carpeta / "kickoff.html"
    if not datos_p.exists():
        sys.exit("✗ No existe %s: el kick-off parte de la propuesta compacta (datos.json)." % datos_p)
    if not a.salida and not a.aprobada:
        sys.exit("✗ Bloqueante (plantillas/brief-kickoff.md §1): confirma con el usuario que la propuesta está APROBADA y vuelve a correr con --aprobada.\n"
                 "  Para una prueba sin tocar la carpeta del cliente: --salida RUTA.")
    if salida.exists() and not a.forzar and MARCA_GENERADO not in salida.read_text(encoding="utf-8", errors="ignore")[:400]:
        sys.exit("✗ %s ya existe y no lo generó este script (kick-off anterior hecho a mano). Usa --forzar para sobrescribirlo o --salida para otra ruta." % salida)
    res, errores, avisos = construir(a.slug, datos_p, kick_p)
    for av in avisos:
        print("⚠ " + av)
    if errores:
        for e in errores:
            print("✗ " + e)
        sys.exit("✗ %d error(es): no se escribió nada." % len(errores))
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(res["html"], encoding="utf-8")
    c = res["cfg"]
    print("✓ %s" % salida)
    print("  %s · %s · %s h a agendar (50 %% = %s h, 60 %% = %s h)" % (c["servicio"], c["codigo"], res["total"], res["total"] * 0.5, res["total"] * 0.6))
    print("  %d etapas · %d grupos de sesiones · %d sesiones propuestas (%s h) · %d puntos de checklist" % (len(c["etapas"]), len(c["grupos"]), len(c["propuestas"]), res["prop_h"], len(c["checklist"])))


if __name__ == "__main__":
    main()
