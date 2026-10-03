#!/usr/bin/env bash
# Genera el Dashboard de Impacto Edu-Trace de un cliente: procesa el CSV y
# renderiza el PDF de cara al cliente (salida única) desde su HTML. SIN AcroForms
# (el dashboard no es editable por ventas, a diferencia de las propuestas).
#
# Desde 2026-06-10 no se emite deck interno: la única salida es el dashboard cliente.
#
# Uso:
#   ./scripts/generar-dashboard.sh <slug>
#
# Ejemplo:
#   ./scripts/generar-dashboard.sh apb-group
#
# Asume estructura: clientes/dashboards/<slug>/{encuesta.csv, mapeo.json,
#                   index-cliente.html, overrides.css}
# Genera:           clientes/dashboards/<slug>/resultados.json
#                   clientes/dashboards/<slug>/Dashboard de Impacto · <Cliente>.pdf

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Uso: $0 <slug>" >&2
  echo "Ejemplo: $0 apb-group" >&2
  exit 1
fi

SLUG="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/clientes/dashboards/$SLUG"
HTML_CLI="$DIR/index-cliente.html"

if [ ! -f "$DIR/encuesta.csv" ]; then
  echo "ERROR: no existe $DIR/encuesta.csv" >&2
  exit 1
fi

# 1 · Procesar el CSV → resultados.json (descarta PII, calcula el Índice)
echo "→ Procesando encuesta Edu-Trace..."
python3 "$ROOT/scripts/edutrace-procesar.py" "$DIR/"

# 2 · Nombre de los PDF a partir del cliente (resultados.json)
CLIENTE="$(python3 - "$DIR/resultados.json" <<'PYEOF'
import json, sys, re
d = json.load(open(sys.argv[1], encoding='utf-8'))
c = d.get('capacitacion', {}).get('cliente', 'Cliente')
print(re.sub(r'[\\/:*?"<>|\r\n]+', ' ', c).strip())
PYEOF
)"
PDF_CLI="$DIR/Dashboard de Impacto · $CLIENTE.pdf"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "ERROR: Chrome no encontrado en $CHROME" >&2
  exit 1
fi

render() {  # <html> <pdf>
  rm -f "$2"
  "$CHROME" \
    --headless=new \
    --disable-gpu \
    --no-pdf-header-footer \
    --print-to-pdf-no-header \
    --virtual-time-budget=15000 \
    --print-to-pdf="$2" \
    "file://$1" 2>&1 | tail -1
}

echo "→ Renderizando PDF del cliente (entregable)..."
render "$HTML_CLI" "$PDF_CLI"

echo ""
echo "✓ Listo:"
echo "  Entregable: $PDF_CLI"
echo ""
echo "→ Revisa visualmente cada slide del PDF antes de entregar (§4.10)."
echo "  El dashboard NO lleva AcroForms: no requiere customize (a diferencia de las propuestas)."
