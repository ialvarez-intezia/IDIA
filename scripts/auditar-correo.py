#!/usr/bin/env python3
"""
Auditoría semanal de correo + propuestas pendientes para irodriguez@intezia.com

Qué hace (cruce de TRES fuentes):
  1. Lee la bandeja de entrada de los últimos N días buscando solicitudes de propuesta.
  2. Cruza con clientes/INDEX.json (base de conocimiento) y con la hoja
     "Control de codificación" (Sheets) para clasificar cada cliente.
  3. Genera un reporte curado y priorizado:
       - Solicitudes NUEVAS (sin código y sin deck)
       - Backlog: código asignado en el Sheet pero SIN deck construido
       - Activas ya construidas
       - Posibles cambios de estado (aprobada / perdida)
       - Próximos códigos libres por categoría
  4. Opcionalmente envía el reporte por correo (--email) usando la Gmail API.
     El correo va en HTML (con fallback de texto) y todas las fechas en español,
     hora de Venezuela.

Uso:
    python3 scripts/auditar-correo.py                 # imprime el reporte
    python3 scripts/auditar-correo.py --dias 7
    python3 scripts/auditar-correo.py --email         # además lo envía por correo
    python3 scripts/auditar-correo.py --email --para otra@intezia.com

Requiere autenticación previa (una sola vez):
    python3 scripts/google-auth-intezia.py
"""

import re
import json
import html
import base64
import argparse
import unicodedata
from pathlib import Path
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# ──────────────────────────────────────────────
# CONFIGURACIÓN
# ──────────────────────────────────────────────
SHEET_ID = "1JmbFMoZNhx3nj8oZ32A-breJmXqTtInyuhN8gTloyYw"   # Control de codificación
SHEET_RANGO = "A:Z"
DIAS = 10
DESTINATARIO = "irodriguez@intezia.com"

# ──────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
TOKEN_FILE = BASE_DIR / "scripts" / "token-intezia.json"
CREDENTIALS_FILE = BASE_DIR / "scripts" / "credentials.json"
INDEX_FILE = BASE_DIR / "clientes" / "INDEX.json"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
]

PALABRAS_PROPUESTA = [
    "propuesta", "cotización", "cotizacion", "capacitación", "capacitacion",
    "taller", "curso", "diplomado", "formación", "formacion", "entrenamiento",
    "precio", "presupuesto", "información", "informacion", "programa",
    "solicitud", "interesado", "interesada", "bootcamp", "consultor",
    "kick-off", "kickoff", "aprobada", "aprobado",
]

# Remitentes que se ignoran (marketing, notificaciones automáticas)
REMITENTES_IGNORAR = [
    "linkedin.com", "skool.com", "udemy.com", "amazon.com", "kajabimail.net",
    "miscursosbaratos.com", "fireflies.ai", "heygen.com", "pinterest.com",
    "semrush.com", "transkriptor.com", "manychat.com", "mentimeter.com",
    "circle.so", "substack.com", "iesa.edu.ve", "surfshark.com",
    "mailer-daemon", "noreply", "no-reply", "no_reply",
    "calendly.com", "discord.com",
]

# Asuntos puramente operativos (calendario, reportes internos) → no son solicitudes
ASUNTOS_IGNORAR = [
    "evento cancelado", "invitación:", "invitacion:", "reporte semanal",
    "se ha programado un evento", "nuevo proceso operativo",
]


def normalizar(s: str) -> str:
    """Minúsculas, sin tildes, solo alfanumérico separado por espacios."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return s.strip()

# Mapa de columnas del Sheet: tipo -> índice de la columna "Código"
# (Código, Programa, Link van en triplete: col, col+1, col+2)
SHEET_COLS = {"CU": 0, "DIP": 3, "TA": 6, "CAP": 9, "CH": 12}
ETIQUETA_TIPO = {"CU": "Curso", "DIP": "Diplomado", "TA": "Taller",
                 "CAP": "Capacitación", "CH": "Charla"}


# ──────────────────────────────────────────────
# Fechas en español (hora de Venezuela)
# ──────────────────────────────────────────────
VET = timezone(timedelta(hours=-4))   # Venezuela (UTC-4, sin horario de verano)

DIAS_SEMANA_ES = ["lunes", "martes", "miércoles", "jueves",
                  "viernes", "sábado", "domingo"]
DIAS_SEMANA_ABBR = ["lun", "mar", "mié", "jue", "vie", "sáb", "dom"]
MESES_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MESES_ABBR = ["ene", "feb", "mar", "abr", "may", "jun",
              "jul", "ago", "sep", "oct", "nov", "dic"]


def formatear_fecha_es(date_str: str) -> str:
    """Fecha RFC-2822 del correo → español, hora de Venezuela.
    Ej: 'Fri, 20 Jun 2026 14:30:00 -0400' → 'vie 20 jun 2026 · 14:30'."""
    if not date_str:
        return "fecha desconocida"
    try:
        dt = parsedate_to_datetime(date_str)
    except (TypeError, ValueError, IndexError):
        return date_str[:16]
    if dt is None:
        return date_str[:16]
    if dt.tzinfo is not None:
        dt = dt.astimezone(VET)
    return (f"{DIAS_SEMANA_ABBR[dt.weekday()]} {dt.day} "
            f"{MESES_ABBR[dt.month - 1]} {dt.year} · {dt:%H:%M}")


def fecha_larga_es(dt: datetime) -> str:
    """'viernes 20 de junio de 2026 · 14:30'."""
    return (f"{DIAS_SEMANA_ES[dt.weekday()]} {dt.day} de "
            f"{MESES_ES[dt.month - 1]} de {dt.year} · {dt:%H:%M}")


# ──────────────────────────────────────────────
# Autenticación
# ──────────────────────────────────────────────
def cargar_credenciales(requiere_envio: bool = False):
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(TOKEN_FILE, "w") as f:
                f.write(creds.to_json())
        else:
            print("Token no encontrado o inválido.")
            print("Corre primero: python3 scripts/google-auth-intezia.py")
            raise SystemExit(1)
    if requiere_envio and "https://www.googleapis.com/auth/gmail.send" not in (creds.scopes or []):
        print("ADVERTENCIA: el token no tiene permiso gmail.send.")
        print("Re-autoriza para poder enviar correo: python3 scripts/google-auth-intezia.py")
    return creds


# ──────────────────────────────────────────────
# Gmail
# ──────────────────────────────────────────────
def es_remitente_ignorar(sender: str) -> bool:
    s = sender.lower()
    return any(ig in s for ig in REMITENTES_IGNORAR)


def es_asunto_ignorar(subject: str) -> bool:
    s = subject.lower()
    return any(ig in s for ig in ASUNTOS_IGNORAR)


def contiene_palabra_propuesta(texto: str) -> bool:
    t = texto.lower()
    return any(p in t for p in PALABRAS_PROPUESTA)


def leer_gmail(service, dias: int) -> list:
    query = f"newer_than:{dias}d in:inbox"
    resultados = []
    response = service.users().threads().list(
        userId="me", q=query, maxResults=80
    ).execute()
    for thread in response.get("threads", []):
        t = service.users().threads().get(
            userId="me", id=thread["id"], format="metadata",
            metadataHeaders=["Subject", "From", "Date"],
        ).execute()
        messages = t.get("messages", [])
        if not messages:
            continue
        # Asunto/remitente del PRIMER mensaje (define el tema/origen);
        # fecha y snippet del ÚLTIMO (refleja la actividad reciente del hilo).
        h0 = {h["name"]: h["value"] for h in messages[0].get("payload", {}).get("headers", [])}
        hN = {h["name"]: h["value"] for h in messages[-1].get("payload", {}).get("headers", [])}
        sender = h0.get("From", "")
        subject = h0.get("Subject", "")
        date = hN.get("Date", "") or h0.get("Date", "")
        snippet = messages[-1].get("snippet", "")
        if es_remitente_ignorar(sender) or es_asunto_ignorar(subject):
            continue
        if contiene_palabra_propuesta(subject) or contiene_palabra_propuesta(snippet):
            resultados.append({
                "date": date, "sender": sender, "subject": subject,
                "snippet": snippet[:220],
            })
    return resultados


# ──────────────────────────────────────────────
# Base de conocimiento + Sheet
# ──────────────────────────────────────────────
def cargar_index() -> dict:
    if not INDEX_FILE.exists():
        return {}
    with open(INDEX_FILE) as f:
        return json.load(f)


def leer_sheet(service, sheet_id: str, rango: str) -> list:
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=sheet_id, range=rango,
        ).execute()
        return result.get("values", [])
    except Exception as e:
        print(f"  ERROR al leer el Sheet: {e}")
        return []


def parsear_sheet(filas: list) -> dict:
    """{tipo: [{codigo, programa, link}]} solo con filas que tienen programa."""
    out = {t: [] for t in SHEET_COLS}
    for fila in filas[2:]:
        for tipo, i in SHEET_COLS.items():
            cod = (fila[i] if len(fila) > i else "").strip()
            prog = (fila[i + 1] if len(fila) > i + 1 else "").strip()
            link = (fila[i + 2] if len(fila) > i + 2 else "").strip()
            if prog:
                out[tipo].append({"codigo": cod, "programa": prog, "link": bool(link)})
    return out


def proximo_codigo(filas: list) -> dict:
    libres = {}
    for tipo, i in SHEET_COLS.items():
        nums = []
        for fila in filas[2:]:
            cod = (fila[i] if len(fila) > i else "").strip()
            prog = (fila[i + 1] if len(fila) > i + 1 else "").strip()
            m = re.match(rf"{tipo}-(\d+)", cod)
            if m and prog:
                nums.append(int(m.group(1)))
        siguiente = (max(nums) + 1) if nums else 1
        libres[tipo] = f"{tipo}-{siguiente:03d}"
    return libres


def codigos_repo() -> dict:
    """{CODIGO: slug} según los PDF construidos en clientes/propuestas/."""
    base = BASE_DIR / "clientes" / "propuestas"
    mapa = {}
    if not base.exists():
        return mapa
    for d in sorted(base.iterdir()):
        if not d.is_dir():
            continue
        for f in d.iterdir():
            if f.suffix.lower() == ".pdf":
                m = re.match(r"((?:CAP|TA|CU|DIP|CH)-[A-Z0-9]+)", f.name, re.I)
                if m:
                    mapa[m.group(1).upper()] = d.name
    return mapa


# ──────────────────────────────────────────────
# Cruce / clasificación
# ──────────────────────────────────────────────
def nombre_cliente_sheet(programa: str) -> str:
    """Extrae el nombre corto del cliente desde el título del programa del Sheet."""
    base = programa.split(":")[0].strip()
    base = re.sub(r"\s*[-/].*$", "", base).strip()  # corta tras guion o barra
    return base


# Nombres del Sheet que NO son clientes externos (aparecen en casi todo correo
# interno o son títulos genéricos de catálogo) → nunca se usan para emparejar.
NOMBRES_GENERICOS = {
    "intezia", "fundacion", "intezia fundamentals", "fundamentos de ia aplicado",
    "marketing estrategico y generativo", "automatizacion avanzada con ia",
    "docencia con ia", "legaltech con ia", "marketing con claude",
    "finanzas y administracion con ia", "creacion del clon digital",
}


def registro_unificado(sheet: dict, repo: dict) -> list:
    """Lista de clientes conocidos con su código y si tienen deck en el repo."""
    reg = []
    for tipo, items in sheet.items():
        for it in items:
            nombre = nombre_cliente_sheet(it["programa"])
            clave = normalizar(nombre)
            if len(clave) < 4 or clave in NOMBRES_GENERICOS:
                continue
            reg.append({
                "nombre": nombre,
                "clave": clave,
                "codigo": it["codigo"],
                "tipo": tipo,
                "link": it["link"],
                "en_repo": it["codigo"] in repo,
            })
    return reg


def detectar_estado(subject: str) -> str:
    s = subject.lower()
    if "aprobad" in s:
        return "Aprobada"
    if "perdid" in s or "no aprob" in s or "declin" in s or "rechaz" in s:
        return "Perdida"
    return ""


def emparejar(texto: str, registro: list) -> dict:
    """Busca el cliente más específico (nombre más largo) presente en el texto.

    Empareja por secuencia de tokens normalizada (sin tildes), acotada por
    espacios, para no confundir 'valu' con 'evaluación' ni perder 'Corporación
    Bel' por la tilde.
    """
    t = f" {normalizar(texto)} "
    mejor = None
    for r in registro:
        if f" {r['clave']} " in t and (mejor is None or len(r["clave"]) > len(mejor["clave"])):
            mejor = r
    return mejor


# ──────────────────────────────────────────────
# Clasificación en buckets
# ──────────────────────────────────────────────
def clasificar(solicitudes, sheet, repo):
    """Reparte las solicitudes en (nuevas, backlog, construidas, cambios)."""
    registro = registro_unificado(sheet, repo)
    nuevas, backlog, construidas, cambios = [], [], [], []
    vistos_backlog = set()

    for s in solicitudes:
        texto = f"{s['subject']} {s['snippet']}"
        m = emparejar(texto, registro)
        estado = detectar_estado(s["subject"])
        remitente = s["sender"].split("<")[0].strip().strip('"')
        fila = {
            "asunto": s["subject"].strip(),
            "snippet": s.get("snippet", ""),
            "de": remitente,
            "fecha": formatear_fecha_es(s["date"]),
            "match": m,
        }
        if estado and m:
            cambios.append({**fila, "estado": estado})
        elif m is None:
            nuevas.append(fila)
        elif m["en_repo"]:
            construidas.append(fila)
        else:
            backlog.append(fila)
            vistos_backlog.add(m["codigo"])

    return nuevas, backlog, construidas, cambios, vistos_backlog


def mostrar_asunto(f) -> str:
    """Asunto legible; si el correo no trae asunto, cae al snippet o a un marcador."""
    if f["asunto"]:
        return f["asunto"]
    snip = (f.get("snippet") or "").strip()
    if snip:
        return f"(sin asunto) {snip[:70]}…"
    return "(sin asunto)"


def backlog_extra(sheet, repo, vistos_backlog):
    """Backlog adicional del Sheet (CAP/TA recientes sin deck ni link) no visto por correo.
    Se limita a CAP/TA (pipeline In-Company); CU/DIP son catálogo académico aparte."""
    extra = []
    for tipo in ("CAP", "TA"):
        for it in sheet.get(tipo, [])[-10:]:
            cod = it["codigo"]
            if cod and cod not in repo and cod not in vistos_backlog and not it["link"]:
                extra.append((cod, nombre_cliente_sheet(it["programa"])))
    return extra


# ──────────────────────────────────────────────
# Reporte · texto plano (consola + fallback del correo)
# ──────────────────────────────────────────────
def generar_reporte_texto(buckets, extra, index, sheet, libres, repo, dias, generado_str) -> str:
    nuevas, backlog, construidas, cambios, _ = buckets

    L = []
    L.append("AUDITORÍA DE CORREO · PROPUESTAS · CODIFICACIÓN")
    L.append(f"Cuenta: {DESTINATARIO} · Ventana: últimos {dias} días")
    L.append(f"Generado: {generado_str} (hora de Venezuela)")
    L.append("Cruce de 3 fuentes: bandeja de entrada → INDEX.json → Control de codificación")
    L.append("=" * 64)

    L.append("\n🔴 1. SOLICITUDES NUEVAS (sin código y sin propuesta)")
    if nuevas:
        for f in nuevas:
            L.append(f"   • {mostrar_asunto(f)}")
            L.append(f"     {f['de']} · {f['fecha']}")
    else:
        L.append("   (ninguna esta semana)")

    L.append("\n🟠 2. BACKLOG · código asignado en el Sheet, SIN deck construido")
    if backlog:
        for f in backlog:
            m = f["match"]
            warn = "" if m["link"] else "  ⚠ sin link en el Sheet"
            L.append(f"   • [{m['codigo']}] {m['nombre']}{warn}")
            L.append(f"     correo: {mostrar_asunto(f)} ({f['de']}, {f['fecha']})")
    else:
        L.append("   (sin backlog detectado por correo)")
    if extra:
        L.append("   Otros códigos CAP/TA recientes sin deck ni link (revisar):")
        for cod, nom in extra:
            L.append(f"   • [{cod}] {nom}")

    L.append("\n🟢 3. ACTIVAS · ya construidas (sin acción de diseño)")
    if construidas:
        for f in construidas:
            m = f["match"]
            L.append(f"   • [{m['codigo']}] {m['nombre']} · {mostrar_asunto(f)} ({f['fecha']})")
    else:
        L.append("   (ninguna)")

    L.append("\n🔵 4. POSIBLES CAMBIOS DE ESTADO (revisar y registrar a mano)")
    if cambios:
        for f in cambios:
            m = f["match"]
            L.append(f"   • {m['nombre']} [{m['codigo']}] → {f['estado']}  ({mostrar_asunto(f)})")
    else:
        L.append("   (ninguno detectado)")

    L.append("\n📐 PRÓXIMOS CÓDIGOS LIBRES")
    L.append("   " + "  ·  ".join(f"{libres[t]} ({ETIQUETA_TIPO[t]})" for t in SHEET_COLS))

    resumen = index.get("resumen", {})
    L.append("\n" + "-" * 64)
    L.append(f"INDEX: {index.get('generado','?')} · "
             f"{resumen.get('propuestas_total','?')} propuestas "
             f"({resumen.get('registradas','?')} registradas)")
    L.append(f"Sheet: {sum(len(v) for v in sheet.values())} códigos asignados · "
             f"Repo: {len(repo)} decks construidos")
    L.append("Generado por scripts/auditar-correo.py")
    return "\n".join(L)


# ──────────────────────────────────────────────
# Reporte · HTML (cuerpo del correo)
# ──────────────────────────────────────────────
def generar_reporte_html(buckets, extra, index, sheet, libres, repo, dias, generado_str) -> str:
    nuevas, backlog, construidas, cambios, _ = buckets
    resumen = index.get("resumen", {})

    # Marca Intezia para el chrome + colores semánticos por bucket (correo interno).
    NEGRO, AMARILLO, NARANJA = "#0a0a0a", "#F4BA1A", "#E58423"
    ROJO, VERDE, AZUL = "#dc2626", "#16a34a", "#2563eb"
    BORDE, GRIS_TXT, GRIS_BG, TXT = "#e5e7eb", "#6b7280", "#f3f4f6", "#111827"

    def esc(x):
        return html.escape(str(x))

    def chip(texto, bg, fg=NEGRO):
        return (f'<span style="display:inline-block;background:{bg};color:{fg};'
                f'font-family:Menlo,Consolas,monospace;font-size:12px;font-weight:700;'
                f'padding:2px 8px;border-radius:5px;white-space:nowrap;">{esc(texto)}</span>')

    def nombre(txt):
        return (f'<span style="font-weight:700;color:{TXT};font-size:14px;">{esc(txt)}</span>')

    def card(inner, accent):
        return (f'<div style="background:#ffffff;border:1px solid {BORDE};'
                f'border-left:3px solid {accent};border-radius:8px;'
                f'padding:11px 14px;margin:0 0 8px 0;">{inner}</div>')

    def titulo_card(txt):
        return (f'<div style="color:{TXT};font-size:14px;font-weight:700;'
                f'line-height:1.45;">{esc(txt)}</div>')

    def meta(html_inner):
        return (f'<div style="color:{GRIS_TXT};font-size:13px;line-height:1.55;'
                f'margin-top:4px;">{html_inner}</div>')

    def vacio(txt):
        return (f'<div style="color:{GRIS_TXT};font-size:13px;font-style:italic;'
                f'padding:2px 2px 6px;">{esc(txt)}</div>')

    def seccion(emoji, titulo, n, accent):
        badge = ""
        if n:
            badge = (f'<span style="display:inline-block;background:{accent};color:#ffffff;'
                     f'font-size:12px;font-weight:700;border-radius:11px;min-width:18px;'
                     f'text-align:center;padding:1px 7px;margin-left:8px;">{n}</span>')
        return (f'<div style="margin:24px 0 10px;font-size:11px;font-weight:800;'
                f'letter-spacing:1px;text-transform:uppercase;color:{TXT};">'
                f'{emoji}&nbsp; {esc(titulo)}{badge}</div>')

    # ── Sección 1 · NUEVAS ──────────────────────
    s = seccion("🔴", "Solicitudes nuevas", len(nuevas), ROJO)
    if nuevas:
        for f in nuevas:
            inner = titulo_card(mostrar_asunto(f)) + meta(f"{esc(f['de'])} &middot; {esc(f['fecha'])}")
            s += card(inner, ROJO)
    else:
        s += vacio("Ninguna esta semana.")
    sec_nuevas = s

    # ── Sección 2 · BACKLOG ─────────────────────
    s = seccion("🟠", "Backlog · código asignado, sin deck", len(backlog), NARANJA)
    if backlog:
        for f in backlog:
            m = f["match"]
            warn = "" if m["link"] else f' &nbsp;{chip("⚠ sin link", "#fef3c7", "#92400e")}'
            top = f'{chip(m["codigo"], NARANJA, "#ffffff")} &nbsp;{nombre(m["nombre"])}{warn}'
            inner = top + meta(f'Correo: {esc(mostrar_asunto(f))}<br>'
                               f'{esc(f["de"])} &middot; {esc(f["fecha"])}')
            s += card(inner, NARANJA)
    else:
        s += vacio("Sin backlog detectado por correo.")
    if extra:
        s += (f'<div style="color:{GRIS_TXT};font-size:12px;margin:8px 2px 6px;">'
              f'Otros códigos CAP/TA recientes sin deck ni link (revisar):</div>')
        for cod, nom in extra:
            s += (f'<div style="font-size:13px;color:{TXT};margin:0 0 5px;padding-left:2px;">'
                  f'{chip(cod, "#fff7ed", NARANJA)} &nbsp;{esc(nom)}</div>')
    sec_backlog = s

    # ── Sección 3 · ACTIVAS ─────────────────────
    s = seccion("🟢", "Activas · ya construidas", len(construidas), VERDE)
    if construidas:
        for f in construidas:
            m = f["match"]
            top = f'{chip(m["codigo"], VERDE, "#ffffff")} &nbsp;{nombre(m["nombre"])}'
            inner = top + meta(f'{esc(mostrar_asunto(f))} &middot; {esc(f["fecha"])}')
            s += card(inner, VERDE)
    else:
        s += vacio("Ninguna.")
    sec_activas = s

    # ── Sección 4 · CAMBIOS DE ESTADO ───────────
    s = seccion("🔵", "Posibles cambios de estado", len(cambios), AZUL)
    if cambios:
        for f in cambios:
            m = f["match"]
            col = VERDE if f["estado"] == "Aprobada" else ROJO
            badge = (f'<span style="display:inline-block;background:{col};color:#ffffff;'
                     f'font-size:12px;font-weight:700;padding:2px 9px;border-radius:5px;">'
                     f'{esc(f["estado"])}</span>')
            top = (f'{nombre(m["nombre"])} &nbsp;{chip(m["codigo"], "#e5e7eb", TXT)} '
                   f'&nbsp;&rarr;&nbsp; {badge}')
            inner = top + meta(f'Detectado en: {esc(mostrar_asunto(f))} &middot; {esc(f["fecha"])}')
            s += card(inner, AZUL)
    else:
        s += vacio("Ninguno detectado. Los cambios de estado se registran a mano.")
    sec_cambios = s

    # ── Sección 5 · PRÓXIMOS CÓDIGOS LIBRES ─────
    s = seccion("📐", "Próximos códigos libres", 0, AMARILLO)
    fila_cod = ""
    for t in SHEET_COLS:
        fila_cod += (f'<span style="display:inline-block;margin:0 10px 8px 0;white-space:nowrap;">'
                     f'{chip(libres[t], AMARILLO)} '
                     f'<span style="color:{GRIS_TXT};font-size:12px;">{ETIQUETA_TIPO[t]}</span>'
                     f'</span>')
    s += f'<div style="line-height:2;">{fila_cod}</div>'
    sec_codigos = s

    # ── Barra resumen (conteos) ─────────────────
    def stat(num, label, color):
        return (f'<td align="center" style="padding:8px 4px;">'
                f'<div style="font-size:26px;font-weight:800;color:{color};line-height:1;">{num}</div>'
                f'<div style="font-size:10px;color:{GRIS_TXT};text-transform:uppercase;'
                f'letter-spacing:.5px;margin-top:5px;">{label}</div></td>')

    resumen_bar = (
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        f'style="background:#ffffff;border:1px solid {BORDE};border-radius:10px;margin:0 0 6px;">'
        '<tr>'
        + stat(len(nuevas), "Nuevas", ROJO)
        + stat(len(backlog), "Backlog", NARANJA)
        + stat(len(construidas), "Activas", VERDE)
        + stat(len(cambios), "Cambios", AZUL)
        + '</tr></table>'
    )

    # ── Encabezado ──────────────────────────────
    header = (
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        f'style="background:{NEGRO};border-radius:12px 12px 0 0;">'
        '<tr><td style="padding:26px 28px;">'
        f'<div style="color:{AMARILLO};font-size:12px;font-weight:800;letter-spacing:3px;">'
        'IDIA &middot; INTEZIA</div>'
        '<div style="color:#ffffff;font-size:22px;font-weight:800;margin-top:6px;">'
        'Auditoría de propuestas</div>'
        f'<div style="color:#9ca3af;font-size:13px;margin-top:8px;line-height:1.55;">'
        f'{esc(DESTINATARIO)} &middot; últimos {dias} días<br>'
        f'Generado: {esc(generado_str)} (hora de Venezuela)</div>'
        '</td></tr></table>'
    )

    # ── Pie ─────────────────────────────────────
    footer = (
        f'<div style="border-top:1px solid {BORDE};margin-top:26px;padding-top:14px;'
        f'color:{GRIS_TXT};font-size:12px;line-height:1.7;">'
        f'<strong style="color:{TXT};">Fuentes cruzadas:</strong> '
        'bandeja de entrada &rarr; INDEX.json &rarr; Control de codificación<br>'
        f'INDEX {esc(index.get("generado", "?"))} &middot; '
        f'{esc(resumen.get("propuestas_total", "?"))} propuestas '
        f'({esc(resumen.get("registradas", "?"))} registradas) &middot; '
        f'Sheet {sum(len(v) for v in sheet.values())} códigos &middot; '
        f'Repo {len(repo)} decks<br>'
        '<span style="color:#9ca3af;">Generado automáticamente por '
        'scripts/auditar-correo.py</span></div>'
    )

    cuerpo = (
        header
        + '<div style="padding:22px 24px 26px;">'
        + resumen_bar
        + sec_nuevas + sec_backlog + sec_activas + sec_cambios + sec_codigos
        + footer
        + '</div>'
    )

    preheader = (f'{len(nuevas)} nuevas, {len(backlog)} en backlog, '
                 f'{len(cambios)} cambios de estado.')

    return (
        '<!DOCTYPE html><html lang="es"><head>'
        '<meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        '</head>'
        f'<body style="margin:0;padding:0;background:{GRIS_BG};">'
        f'<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{esc(preheader)}</div>'
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" '
        f'style="background:{GRIS_BG};padding:24px 12px;"><tr><td align="center">'
        '<table role="presentation" width="640" cellpadding="0" cellspacing="0" '
        'style="max-width:640px;width:100%;background:#ffffff;border-radius:12px;'
        'overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.08);'
        'font-family:-apple-system,BlinkMacSystemFont,Roboto,Helvetica,Arial,sans-serif;">'
        f'<tr><td>{cuerpo}</td></tr>'
        '</table></td></tr></table></body></html>'
    )


def enviar_correo(service, destinatario: str, asunto: str,
                  cuerpo_texto: str, cuerpo_html: str):
    """Envía un correo multipart/alternative (texto + HTML)."""
    msg = MIMEMultipart("alternative")
    msg["to"] = destinatario
    msg["from"] = destinatario
    msg["subject"] = asunto
    msg.attach(MIMEText(cuerpo_texto, "plain", "utf-8"))
    msg.attach(MIMEText(cuerpo_html, "html", "utf-8"))
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    service.users().messages().send(userId="me", body={"raw": raw}).execute()


# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dias", type=int, default=DIAS)
    parser.add_argument("--email", action="store_true", help="envía el reporte por correo")
    parser.add_argument("--para", default=DESTINATARIO, help="destinatario del correo")
    args = parser.parse_args()

    ahora = datetime.now(VET)
    generado_str = fecha_larga_es(ahora)

    creds = cargar_credenciales(requiere_envio=args.email)
    gmail = build("gmail", "v1", credentials=creds)
    sheets = build("sheets", "v4", credentials=creds)

    solicitudes = leer_gmail(gmail, args.dias)
    index = cargar_index()
    filas = leer_sheet(sheets, SHEET_ID, SHEET_RANGO)
    sheet = parsear_sheet(filas)
    repo = codigos_repo()

    buckets = clasificar(solicitudes, sheet, repo)
    extra = backlog_extra(sheet, repo, buckets[4])
    libres = proximo_codigo(filas)

    reporte_txt = generar_reporte_texto(buckets, extra, index, sheet, libres,
                                        repo, args.dias, generado_str)
    print(reporte_txt)

    if args.email:
        reporte_html = generar_reporte_html(buckets, extra, index, sheet, libres,
                                            repo, args.dias, generado_str)
        asunto = f"[Intezia] Auditoría de propuestas · {ahora:%Y-%m-%d}"
        try:
            enviar_correo(gmail, args.para, asunto, reporte_txt, reporte_html)
            print(f"\n✓ Reporte enviado a {args.para}")
        except Exception as e:
            print(f"\n✗ No se pudo enviar el correo: {e}")
            raise SystemExit(1)


if __name__ == "__main__":
    main()
