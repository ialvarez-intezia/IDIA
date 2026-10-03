#!/usr/bin/env bash
# Lista todos los PDFs dentro del proyecto Intezia Propuestas,
# con tamaño, fecha de modificación y ruta relativa.
#
# Uso:
#   ./scripts/listar-pdfs.sh
#   ./scripts/listar-pdfs.sh fuentes/        # solo en una subcarpeta
#   ./scripts/listar-pdfs.sh -- liderazgo    # filtra por término en el nombre

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

scope="."
filter=""

while [ $# -gt 0 ]; do
  case "$1" in
    --) shift; filter="${1:-}"; shift || true ;;
    -h|--help)
      sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      if [ -d "$1" ]; then
        scope="$1"
      else
        echo "Aviso: '$1' no es un directorio, ignorado." >&2
      fi
      shift
      ;;
  esac
done

echo "PDFs en: $ROOT/$scope"
[ -n "$filter" ] && echo "Filtro: *$filter*"
echo ""

count=0
total_bytes=0

while IFS= read -r -d '' pdf; do
  if [ -n "$filter" ] && [[ "$(basename "$pdf")" != *"$filter"* ]]; then
    continue
  fi
  size_h=$(du -h "$pdf" | cut -f1)
  size_b=$(stat -f "%z" "$pdf")
  date=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$pdf")
  rel="${pdf#./}"
  printf "  %-8s  %s  %s\n" "$size_h" "$date" "$rel"
  count=$((count + 1))
  total_bytes=$((total_bytes + size_b))
done < <(find "$scope" -type f \( -iname "*.pdf" \) -print0 2>/dev/null | sort -z)

echo ""
if [ "$count" -eq 0 ]; then
  echo "  (sin PDFs todavía)"
  echo ""
  echo "Para subir uno desde tu Mac:"
  echo "  cp ~/Downloads/archivo.pdf \"$ROOT/fuentes/\""
else
  total_mb=$(echo "scale=2; $total_bytes / 1048576" | bc)
  echo "Total: $count PDF(s) — ${total_mb} MB"
fi
