#!/usr/bin/env bash
# PDF de la propuesta única INN-006 (no usa pdf-habilidades-compacto.sh porque ese regenera index.html desde datos.json).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
SLUG=zoom-inn006-union-abc
DIR="$ROOT/clientes/propuestas/$SLUG"
cd "$ROOT"
bash scripts/verificar-propuesta.sh "$SLUG"
node scripts/verificar-habilidades-compacto.js "$SLUG"
mkdir -p "$DIR/_pdf-anteriores"
SELLO="$(date +%Y%m%d-%H%M%S)"
for f in "$DIR"/*.pdf; do [ -e "$f" ] && mv "$f" "$DIR/_pdf-anteriores/$(basename "$f" .pdf).$SELLO.pdf"; done
bash scripts/generar-pdf.sh "$SLUG"
python3 scripts/customize-acroforms.py "$SLUG"
PDF="$(find "$DIR" -maxdepth 1 -name '*.pdf' | head -1)"
python3 scripts/customize-habilidades-compacto.py "$PDF"
# generar-pdf.sh estampa «Enviada»; la propuesta sigue en borrador hasta que Ivana la envíe
python3 - <<PY
import json
p="$DIR/meta.json"; m=json.load(open(p,encoding="utf-8")); m["estado"]="Borrador"; m["fecha_entrega"]=None
json.dump(m,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2); open(p,"a").write("\n")
PY
python3 scripts/indexar.py >/dev/null 2>&1 || true
echo "✓ Listo: $PDF"
