#!/usr/bin/env bash
# Genera el PDF del workbook del participante para un cliente.
#
# Uso:
#   ./scripts/generar-workbook.sh <slug-cliente>
#
# Ejemplo:
#   ./scripts/generar-workbook.sh cumbre-andina
#
# Asume estructura: clientes/propuestas/<slug>/{workbook.html, workbook.css}
# Genera:           clientes/propuestas/<slug>/workbook.pdf
#
# Reglas del workbook: ver plantillas/diseno-workbook.md.
# Plantilla canónica:  plantillas/workbook-canonico/{index.html, workbook.css}.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Uso: $0 <slug-cliente>" >&2
  echo "Ejemplo: $0 cumbre-andina" >&2
  exit 1
fi

SLUG="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/clientes/propuestas/$SLUG"
HTML="$DIR/workbook.html"
PDF="$DIR/workbook.pdf"

if [ ! -f "$HTML" ]; then
  echo "ERROR: no existe $HTML" >&2
  echo "       Cloná plantillas/workbook-canonico/ a clientes/propuestas/$SLUG/ y" >&2
  echo "       renombrá index.html → workbook.html antes de generar." >&2
  exit 1
fi

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "ERROR: Chrome no encontrado en $CHROME" >&2
  exit 1
fi

echo "→ Generando workbook PDF (A4 vertical) con Chrome headless..."
rm -f "$PDF"
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf-no-header \
  --virtual-time-budget=15000 \
  --print-to-pdf="$PDF" \
  "file://$HTML" 2>&1 | tail -2

if [ ! -f "$PDF" ]; then
  echo "ERROR: el PDF no se generó" >&2
  exit 1
fi

# Si el inyector de AcroForms existe, añade los campos editables del participante.
INJECT="$ROOT/scripts/agregar-campos-workbook.py"
if [ -f "$INJECT" ]; then
  echo "→ Añadiendo campos editables (MI PROMPT)..."
  python3 "$INJECT" "$PDF"
fi

echo ""
echo "✓ Listo: $PDF"
echo "  Tamaño: $(du -h "$PDF" | cut -f1)"
echo "  Abrí el PDF con Adobe Reader o Preview para verificar los campos editables."
