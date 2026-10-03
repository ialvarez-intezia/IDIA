#!/usr/bin/env bash
# Genera el PDF de una propuesta a partir de su index.html y añade el
# campo de precio editable (AcroForm) que rellenará el equipo de ventas.
#
# Uso:
#   ./scripts/generar-pdf.sh <slug-cliente>
#
# Ejemplo:
#   ./scripts/generar-pdf.sh cumbre-andina
#
# Asume estructura: clientes/propuestas/<slug>/{index.html, styles.css}
# Genera:           clientes/propuestas/<slug>/<CÓDIGO> <Título>.pdf
#                   (el código y el título se leen de la portada del index.html)

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Uso: $0 <slug-cliente>" >&2
  echo "Ejemplo: $0 cumbre-andina" >&2
  exit 1
fi

SLUG="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/clientes/propuestas/$SLUG"
# 2º arg opcional: nombre del HTML dentro de la carpeta del slug (default index.html).
# Permite varios decks por carpeta, p.ej.: generar-pdf.sh venemergencia index-completo.html
HTML="$DIR/${2:-index.html}"

if [ ! -f "$HTML" ]; then
  echo "ERROR: no existe $HTML" >&2
  exit 1
fi

# Nombre del PDF = "<CÓDIGO> <Título>" leído de la portada (span.codigo + h1).
# Si no hay código, usa solo el título; si no hay nada, cae a "propuesta".
PDFNAME="$(python3 - "$HTML" <<'PYEOF'
import re, sys
html = open(sys.argv[1], encoding='utf-8').read()
codigo = ''
m = re.search(r'class="codigo"[^>]*>(.*?)</span>', html, re.S)
if m:
    codigo = re.sub(r'<[^>]+>', '', m.group(1))
    codigo = re.sub(r'(?i)c[óo]digo\s*:?\s*', '', codigo).strip()
titulo = ''
m2 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)
if m2:
    titulo = re.sub(r'<[^>]+>', ' ', m2.group(1))
    titulo = re.sub(r'\s+', ' ', titulo).strip()
name = (codigo + ' ' + titulo).strip() if codigo else titulo
name = re.sub(r'[\\/:*?"<>|\r\n]+', ' ', name)
name = re.sub(r'\s+', ' ', name).strip()[:90]
print(name or 'propuesta')
PYEOF
)"
PDF="$DIR/$PDFNAME.pdf"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "ERROR: Chrome no encontrado en $CHROME" >&2
  exit 1
fi

echo "→ Generando PDF base con Chrome headless..."
rm -f "$PDF" "$DIR/propuesta.pdf"  # limpia el target y el nombre legacy
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf-no-header \
  --virtual-time-budget=15000 \
  --print-to-pdf="$PDF" \
  "file://$HTML" 2>&1 | tail -2

echo "→ Añadiendo campo editable de precio..."
python3 "$ROOT/scripts/agregar-campo-precio.py" "$PDF"

echo ""
echo "✓ Listo: $PDF"
echo "  Tamaño: $(du -h "$PDF" | cut -f1)"
echo "  El equipo de ventas puede abrirlo con Adobe Reader o Preview y escribir el valor."
echo ""

# Registro de entrega (§ meta.json): estampa la fecha y avanza el estado del deck.
# Como toda entrega pasa por aquí, el registro es infalible. Append-only: respeta el
# estado puesto a mano (Aprobada/Perdida/Enviada). Sin meta.json -> advertencia visible.
echo "→ Actualizando registro de entrega (meta.json)..."
python3 "$ROOT/scripts/estampar-entrega.py" "$DIR/meta.json" "$(date +%Y-%m-%d)"

# Columna vertebral relacional: regenera clientes/INDEX.{json,md} con la entrega ya
# estampada. Así el índice nunca queda como foto vieja. No bloquea la entrega si falla.
echo "→ Reindexando columna vertebral (clientes/INDEX)..."
python3 "$ROOT/scripts/indexar.py" || echo "  ⚠️  indexar.py falló (no bloquea la entrega)"
echo ""
echo "→ Siguiente paso (par PDF-customize, §10): correr el customize con ESTE path:"
CUST="$(find "$ROOT/scripts" -maxdepth 1 -name "customize-${SLUG}.py" | head -1)"
if [ -n "$CUST" ]; then
  # Propuesta con script propio (caso especial o anterior al flujo acroforms.json)
  echo "    python3 \"$CUST\" \"$PDF\""
elif [ -f "$DIR/acroforms.json" ]; then
  echo "    python3 scripts/customize-acroforms.py \"$PDF\" \"$DIR/acroforms.json\""
else
  echo "    Crea clientes/propuestas/${SLUG}/acroforms.json y corre:"
  echo "    python3 scripts/customize-acroforms.py ${SLUG}"
fi
