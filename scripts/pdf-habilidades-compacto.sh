#!/usr/bin/env bash
# pdf-habilidades-compacto.sh <slug>
# Flujo completo para una propuesta compacta de Habilidades (plantillas/habilidades-compacto.md):
#   1. regenera index.html desde datos.json (si existe)      generar-habilidades-compacto.py
#   2. verificadores del sistema                              verificar-propuesta.sh + verificar-habilidades-compacto.js
#   3. PDF + campos AcroForm                                  generar-pdf.sh
#   4. par obligatorio de campos                              customize-acroforms.py + customize-habilidades-compacto.py
# Se detiene en el primer error. Si falla DESPUÉS de que generar-pdf.sh estampó la entrega, restaura meta.json
# (estado y fecha) y reindexa, para no dejar la propuesta marcada «Enviada» con un PDF a medias.
# Nota: cuando todo sale bien, generar-pdf.sh deja meta.json en «Enviada» con la fecha de hoy (convención del
# sistema: terminado = enviado) y regenera clientes/INDEX.*; si aún no se envía, corregir a mano.
set -euo pipefail

SLUG="${1:?Uso: $0 <slug-cliente>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/clientes/propuestas/$SLUG"
[ -d "$DIR" ] || { echo "ERROR: no existe $DIR" >&2; exit 1; }

if ! python3 -c "import pypdf" 2>/dev/null; then
  echo "ERROR: falta pypdf en este Python (los scripts de AcroForms lo necesitan)." >&2
  echo "  Crea un entorno aparte y relanza con él en el PATH:" >&2
  echo "    python3 -m venv ~/.venv-propuestas && ~/.venv-propuestas/bin/pip install pypdf" >&2
  echo "    PATH=~/.venv-propuestas/bin:\$PATH bash scripts/pdf-habilidades-compacto.sh $SLUG" >&2
  exit 1
fi

cd "$ROOT"
if [ -f "$DIR/datos.json" ]; then
  echo "== 1/4 Generando index.html desde datos.json =="
  python3 scripts/generar-habilidades-compacto.py "$SLUG"
fi
echo "== 2/4 Verificando =="
bash scripts/verificar-propuesta.sh "$SLUG"
node scripts/verificar-habilidades-compacto.js "$SLUG"

# PDF previos: generar-pdf.sh nombra el PDF «<CÓDIGO> <titular>.pdf» y solo borra el del mismo nombre;
# customize-acroforms.py exige exactamente 1 PDF en la carpeta. Los anteriores se apartan a _pdf-anteriores/ con
# sello de fecha y hora (nunca se pisa uno ya apartado) y, si el flujo falla, se devuelven a su lugar.
MOVIDOS=""
META_BAK=""
if [ -f "$DIR/meta.json" ]; then
  META_BAK="$(mktemp)"
  cp "$DIR/meta.json" "$META_BAK"
fi
restaurar() {
  trap - ERR INT TERM
  if [ -n "$MOVIDOS" ]; then
    find "$DIR" -maxdepth 1 -name '*.pdf' -delete   # PDF a medias de este intento
    while IFS='|' read -r orig dest; do
      if [ -n "$orig" ] && [ -f "$dest" ]; then mv "$dest" "$orig"; fi
    done <<FIN
$MOVIDOS
FIN
    echo "  (falló el flujo: se devolvieron los PDF previos a su lugar)" >&2
  fi
  if [ -n "$META_BAK" ] && [ -f "$META_BAK" ]; then
    cp "$META_BAK" "$DIR/meta.json"
    python3 "$ROOT/scripts/indexar.py" >/dev/null 2>&1 || true
    echo "  (falló el flujo: meta.json restaurado a su estado anterior)" >&2
  fi
}
trap 'restaurar' ERR
trap 'restaurar; exit 130' INT TERM

SELLO="$(date +%Y%m%d-%H%M%S)"
PREVIOS=$(find "$DIR" -maxdepth 1 -name '*.pdf' | wc -l | tr -d ' ')
if [ "$PREVIOS" -gt 0 ]; then
  mkdir -p "$DIR/_pdf-anteriores"
  while IFS= read -r f; do
    destino="$DIR/_pdf-anteriores/$(basename "$f" .pdf).$SELLO.pdf"
    mv "$f" "$destino"
    MOVIDOS="${MOVIDOS}${f}|${destino}"$'\n'
  done < <(find "$DIR" -maxdepth 1 -name '*.pdf')
  echo "  (se apartaron $PREVIOS PDF previo(s) en $DIR/_pdf-anteriores/ con sello $SELLO)"
fi

echo "== 3/4 Generando PDF =="
bash scripts/generar-pdf.sh "$SLUG"
echo "== 4/4 Campos AcroForm (par obligatorio) =="
python3 scripts/customize-acroforms.py "$SLUG"
PDF="$(find "$DIR" -maxdepth 1 -name '*.pdf' | head -1)"
python3 scripts/customize-habilidades-compacto.py "$PDF"
trap - ERR INT TERM
[ -n "$META_BAK" ] && rm -f "$META_BAK"
echo
echo "✓ Listo: $PDF"
echo "  Revisa visualmente cada slide del PDF (§4.10) antes de entregar."
