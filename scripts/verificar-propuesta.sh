#!/usr/bin/env bash
# verificar-propuesta.sh <slug>
# Comprueba las reglas bloqueantes automáticamente verificables.
# Ejecutar ANTES de generar el PDF y ANTES de declarar un trabajo entregado.
#
# Uso:    ./scripts/verificar-propuesta.sh <slug-cliente>
# Salida: 0 = sin errores bloqueantes | 1 = hay errores que corregir
#
# Detecta automáticamente:
#   §4.13 Guiones largos/medianos (— –) en contenido visible (no en comentarios HTML ni panel-source)
#   §4.4  Anglicismo «cohort/cohorts» en HTML o acroforms*.json (usar «grupos»)
#   Comillas tipográficas usadas como delimitadores de atributos HTML (rompen el CSS completo)
#   Placeholders sin llenar ([CÓDIGO]) en index.html
#   Ausencia de customize-<slug>.py cuando existe propuesta.pdf

set -euo pipefail

SLUG="${1:?Uso: $0 <slug-cliente> [archivo.html]}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/clientes/propuestas/$SLUG"
# 2º arg opcional: nombre del HTML dentro de la carpeta del slug (default index.html).
# Permite varios decks por carpeta, p.ej.: verificar-propuesta.sh venemergencia index-completo.html
HTML="$DIR/${2:-index.html}"

if [[ ! -f "$HTML" ]]; then
  echo "ERROR: No se encontró $HTML" >&2
  exit 1
fi

ERRORS=0
WARNINGS=0

echo "== Verificando propuesta: $SLUG =="
echo ""

# ── §4.13 Sin guión largo ni mediano ──────────────────────────────────────────
# Excluye: líneas de comentarios HTML y panel-source (citas verbatim, §4.13 excepción)
EM_DASH_ISSUES=$(python3 - "$HTML" <<'PYEOF'
import sys

html_path = sys.argv[1]
with open(html_path, encoding='utf-8') as f:
    lines = f.readlines()

in_comment = False
results = []
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if '<!--' in line:
        in_comment = True
    if '-->' in line:
        in_comment = False
        continue
    if in_comment:
        continue
    # Skip source citations (verbatim, §4.13 exception)
    if 'panel-source' in stripped:
        continue
    if '—' in line:
        results.append(f'  Línea {i}: {stripped[:120]}')
    elif '–' in line:
        # En-dash entre dígitos = rango numérico aceptable (ej. 2–4 sem, 1–2 h)
        # En-dash entre texto = separador prohibido por §4.13
        import re as _re
        if _re.search(r'(?<!\d)–(?!\d)', line):
            results.append(f'  Línea {i}: {stripped[:120]}')

print('\n'.join(results))
PYEOF
)

if [[ -n "$EM_DASH_ISSUES" ]]; then
  echo "❌ §4.13 Guión largo/mediano en contenido visible (reemplazar con coma, paréntesis, dos puntos o punto):"
  echo "$EM_DASH_ISSUES" | head -10
  echo ""
  ERRORS=$((ERRORS+1))
else
  echo "✓  §4.13 Sin guión largo en contenido"
fi

# ── Comillas tipográficas como delimitadores de atributos HTML ─────────────────
# Solo marca el caso peligroso: comilla curva usada como delimitador de atributo
# (causa el bug donde el CSS de una slide entera deja de aplicar).
# No marca comillas curvas en texto de contenido (quote-mark, citas, etc.)
ATTR_SMART_QUOTES=$(python3 - "$HTML" <<'PYEOF'
import re, sys

html_path = sys.argv[1]
with open(html_path, encoding='utf-8') as f:
    lines = f.readlines()

# Pattern: smart quote used as attribute delimiter or adjacent to =
pattern = re.compile(r'=\s*[“”‘’]|[“”‘’]\s*=')
results = []
for i, line in enumerate(lines, 1):
    if pattern.search(line):
        results.append(f'  Línea {i}: {line.strip()[:120]}')
print('\n'.join(results))
PYEOF
)

if [[ -n "$ATTR_SMART_QUOTES" ]]; then
  echo "❌ Comillas tipográficas como delimitadores de atributos HTML (rompen el CSS — reemplazar con \"):"
  echo "$ATTR_SMART_QUOTES" | head -10
  echo ""
  ERRORS=$((ERRORS+1))
else
  echo "✓  Sin comillas tipográficas en atributos HTML"
fi

# ── §4.4 Sin anglicismo «cohort/cohorts» (usar «grupos») ───────────────────────
# El usuario no quiere ver «cohort/cohorts» en ninguna propuesta. Se chequea el HTML
# y los acroforms*.json (ambos de cara al cliente). Internos (brief/programa) no bloquean.
COHORT_FILES=("$HTML")
if compgen -G "$DIR/acroforms*.json" > /dev/null; then
  COHORT_FILES+=("$DIR"/acroforms*.json)
fi
COHORT_HITS=$(grep -niE '\bcohorts?\b' "${COHORT_FILES[@]}" 2>/dev/null || true)
if [[ -n "$COHORT_HITS" ]]; then
  echo "❌ §4.4 Anglicismo «cohort/cohorts» (no se usa en español — reemplazar por «grupos»):"
  echo "$COHORT_HITS" | head -10
  echo ""
  ERRORS=$((ERRORS+1))
else
  echo "✓  §4.4 Sin anglicismo «cohort/cohorts»"
fi

# ── Placeholders sin llenar ────────────────────────────────────────────────────
PLACEHOLDERS=$(grep -n "\[CÓDIGO\]\|\[código\]" "$HTML" 2>/dev/null || true)
if [[ -n "$PLACEHOLDERS" ]]; then
  echo "⚠️  Placeholder [CÓDIGO] sin reemplazar en index.html:"
  echo "$PLACEHOLDERS" | head -5
  echo ""
  WARNINGS=$((WARNINGS+1))
fi

# ── §4.15 Sin acuerdos económicos en «Cómo arrancamos» ─────────────────────────
# Los pasos de la slide .s-steps describen logística, no la transacción comercial.
# Marca términos económicos en los bloques acro-paso-*.
STEPS_ECON=$(python3 - "$HTML" <<'PYEOF'
import re, sys

html_path = sys.argv[1]
with open(html_path, encoding='utf-8') as f:
    lines = f.readlines()

# Términos económicos prohibidos en los pasos (§4.15)
econ = re.compile(r'\b(factura\w*|anticipo\w*|adelanto\w*|contrato\w*|acuerdo\w*'
                  r'|pago\w*|pagar|abono\w*|50\s*%|50\s*por\s*ciento|cotiza\w*)\b',
                  re.IGNORECASE)
results = []
for i, line in enumerate(lines, 1):
    if 'acro-paso-' in line and econ.search(line):
        m = econ.search(line)
        results.append(f'  Línea {i} ({m.group(0)}): {line.strip()[:120]}')
print('\n'.join(results))
PYEOF
)

if [[ -n "$STEPS_ECON" ]]; then
  echo "❌ §4.15 Término económico en «Cómo arrancamos» (logística, no transacción — quitar factura/anticipo/acuerdo/contrato/pago):"
  echo "$STEPS_ECON" | head -10
  echo ""
  ERRORS=$((ERRORS+1))
else
  echo "✓  §4.15 Sin acuerdos económicos en los pasos de arranque"
fi

# ── Par PDF-customize: verificar que existe la fuente de pre-llenado ──────────
# El PDF ya no se llama siempre propuesta.pdf: se nombra "<CÓDIGO> <Título>.pdf".
# Fuente válida: acroforms*.json en la carpeta (estándar, vía customize-acroforms.py)
# o un scripts/customize-<slug>*.py (caso especial / propuestas previas).
PDF_COUNT=$(find "$DIR" -maxdepth 1 -name "*.pdf" 2>/dev/null | wc -l | tr -d ' ')
if [[ "$PDF_COUNT" -gt 0 ]]; then
  JSON_COUNT=$(find "$DIR" -maxdepth 1 -name "acroforms*.json" 2>/dev/null | wc -l | tr -d ' ')
  CUSTOMIZE_COUNT=$(find "$ROOT/scripts" -maxdepth 1 -name "customize-${SLUG}*.py" 2>/dev/null | wc -l | tr -d ' ')
  if [[ "$JSON_COUNT" -eq 0 && "$CUSTOMIZE_COUNT" -eq 0 ]]; then
    echo "⚠️  Hay un PDF generado pero no hay acroforms*.json en la carpeta ni scripts/customize-${SLUG}*.py"
    echo "     Si los AcroForms tienen campos pre-llenados, el PDF puede estar vacío."
    echo ""
    WARNINGS=$((WARNINGS+1))
  else
    echo "✓  Fuente de pre-llenado AcroForms encontrada (${JSON_COUNT} json, ${CUSTOMIZE_COUNT} script(s))"
  fi
fi

# ── §4.15 también en acroforms*.json (los pasos pre-llenados viven ahí) ────────
# Solo se filtran los campos Paso01-03 (Titulo/Body): son los únicos sujetos a
# §4.15 (logística de «Cómo arrancamos», no transacción). Notas/Programa SÍ
# pueden llevar términos económicos a propósito — viven en la slide de
# Propuesta Económica, donde corresponden (vigencia, anticipo, cancelación).
if compgen -G "$DIR/acroforms*.json" > /dev/null; then
  JSON_ECON=$(python3 - "$DIR"/acroforms*.json <<'PYEOF'
import json, re, sys

econ = re.compile(r'\b(factura\w*|anticipo\w*|adelanto\w*|contrato\w*|acuerdo\w*'
                  r'|pago\w*|pagar|abono\w*|50\s*%|50\s*por\s*ciento|cotiza\w*)\b',
                  re.IGNORECASE)
results = []
for path in sys.argv[1:]:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    for key, value in data.items():
        if not re.match(r'^Paso\d\d(Titulo|Body)$', key):
            continue
        text = value if isinstance(value, str) else '\n'.join(value)
        m = econ.search(text)
        if m:
            results.append(f'  {path} · {key} ({m.group(0)}): {text.strip()[:120]}')
print('\n'.join(results))
PYEOF
)
  if [[ -n "$JSON_ECON" ]]; then
    echo "❌ §4.15 Término económico en acroforms*.json (Paso0N: logística, no transacción):"
    echo "$JSON_ECON" | head -10
    echo ""
    ERRORS=$((ERRORS+1))
  else
    echo "✓  §4.15 Sin acuerdos económicos en los Pasos de acroforms*.json"
  fi
fi

# ── §4.10 Desborde visual (detector automático) ────────────────────────────────
# Renderiza el deck en Chrome headless y detecta contenido que se sale de la slide
# o que una caja recorta. Reemplaza la revisión a ojo, slide por slide.
if command -v node >/dev/null 2>&1; then
  if OVERFLOW_OUT=$(node "$ROOT/scripts/verificar-overflow.js" "$HTML" 2>/dev/null); then
    echo "✓  §4.10 Sin desbordes (detector automático)"
  else
    echo "❌ §4.10 Desborde visual detectado:"
    echo "$OVERFLOW_OUT" | grep '•' | head -12
    echo ""
    ERRORS=$((ERRORS+1))
  fi
else
  echo "⚠️  node no disponible: no se pudo correr el detector de desborde (§4.10)."
  echo "     Revisa el PDF slide por slide manualmente."
  WARNINGS=$((WARNINGS+1))
fi

# ── Decks de la plantilla compacta de Habilidades: holguras exactas (plantillas/habilidades-compacto.md) ──
# Detecta colisiones entre bloques con posición absoluta que verificar-overflow.js no ve.
if [[ -f "$DIR/habilidades-compacto.css" ]] && command -v node >/dev/null 2>&1; then
  if COMPACTO_OUT=$(node "$ROOT/scripts/verificar-habilidades-compacto.js" "$HTML" 2>/dev/null); then
    echo "✓  Holguras del deck compacto de Habilidades (verificar-habilidades-compacto.js)"
  else
    echo "❌ Holguras del deck compacto de Habilidades:"
    echo "$COMPACTO_OUT" | grep -E '✗|→' | head -14
    echo ""
    ERRORS=$((ERRORS+1))
  fi
fi

# ── §4.23 Sin semanas ni sesiones (Keiber, 2026-10-08) en los decks compactos v3 ─────────────────────────────
# El generador ya lo bloquea; esto atrapa una edición a mano del index.html después de generar. Solo decks con CSS v3+
# (los v1/v2 ya entregados no se revisan por esto). Las fuentes citadas (pain-src, mp-src, lic-note) y los comentarios
# no cuentan; las tasas del cliente («12 h por semana», «cada semana») sí se permiten.
if [[ -f "$DIR/habilidades-compacto.css" ]] && grep -q 'CSS genérico (v[3-9]' "$DIR/habilidades-compacto.css" 2>/dev/null; then
  CAL_HITS=$(python3 - "$HTML" <<'PYEOF'
import html, re, sys
t = open(sys.argv[1], encoding="utf-8").read()
t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
t = re.sub(r'<(p|span) class="(?:pain-src|mp-src|lic-note)">.*?</\1>', " ", t, flags=re.S)
rx = re.compile(r"(?<!por )(?<!cada )(?<!a la )\bsemanas?\b|\bsesi[oó]n(?:es)?\b", re.I)
out = []
for cls, cuerpo in re.findall(r'<section class="slide ([^"]*)">(.*?)</section>', t, re.S):
    txt = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", cuerpo)))
    for m in rx.finditer(txt):
        out.append("  %s: «…%s…»" % (cls.split()[0], txt[max(0, m.start() - 35):m.end() + 25].strip()))
print("\n".join(out[:10]))
PYEOF
)
  if [[ -n "$CAL_HITS" ]]; then
    echo "❌ §4.23 La propuesta no lleva semanas ni sesiones (se acuerdan en el kickoff): corregir datos.json y regenerar"
    echo "$CAL_HITS"
    echo ""
    ERRORS=$((ERRORS+1))
  else
    echo "✓  §4.23 Sin semanas ni sesiones en el deck compacto"
  fi
fi

# ── Servicio de Habilidades: plantilla compacta como único formato (CLAUDE.md §4.21) ──
# Aviso (no bloqueante, para no estorbar cambios puntuales en decks ya entregados): una propuesta registrada como
# servicio «habilidades» en meta.json cuyo deck no es el compacto (no tiene habilidades-compacto.css).
if [[ -f "$DIR/meta.json" && ! -f "$DIR/habilidades-compacto.css" ]]; then
  SERV_META=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1], encoding='utf-8-sig')).get('servicio',''))" "$DIR/meta.json" 2>/dev/null || true)
  if [[ "$SERV_META" == "habilidades" ]]; then
    echo "⚠️  Propuesta de Habilidades fuera de la plantilla compacta (CLAUDE.md §4.21): toda charla, taller, capacitación, curso o diplomado"
    echo "     de Habilidades se entrega con plantillas/habilidades-compacto.md (recetas por categoría en su §1b). Si esto es un cambio puntual"
    echo "     sobre un deck ya entregado puede seguir así; si es una propuesta nueva o se pidió rehacerla, hay que armarla con la plantilla."
    echo ""
    WARNINGS=$((WARNINGS+1))
  fi
fi

# ── Resultado ──────────────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [[ $ERRORS -gt 0 ]]; then
  echo "❌ $ERRORS error(es) bloqueante(s). Corrige antes de generar el PDF."
  exit 1
fi

if [[ $WARNINGS -gt 0 ]]; then
  echo "⚠️  Sin errores bloqueantes, pero hay $WARNINGS advertencia(s) a revisar."
fi

echo "✅ Verificación automática OK."
echo ""
echo "Revisar MANUALMENTE antes de entregar (§10 CLAUDE.md):"
echo "  §4.10  Overflow ya cubierto por el detector. Ojea logos solapados o desalineados"
echo "  §4.11  Ninguna slide afirma que el cliente migra o ya adoptó la herramienta enseñada"
echo "  §4.12  Todo acrónimo de jerga glosado en su primera aparición de CADA slide"
echo "  §4.14  AcroForms pre-llenados: Entregables · Acreditación · Paso01-03 Titulo/Body"
echo "  PAR    Si se regeneró el PDF, se volvió a correr customize-acroforms.py <slug> (o el customize-<slug>.py) inmediatamente"
echo ""
exit 0
