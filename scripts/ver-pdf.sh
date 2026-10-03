#!/usr/bin/env bash
# Abre uno o varios PDFs del proyecto en Preview (macOS).
# Acepta nombre exacto, parcial o ruta. Si hay varias coincidencias, las muestra
# y abre la primera; pasa el flag --all para abrirlas todas.
#
# Uso:
#   ./scripts/ver-pdf.sh catalogo.pdf
#   ./scripts/ver-pdf.sh catalogo            # busca por término
#   ./scripts/ver-pdf.sh --all liderazgo     # abre todas las coincidencias
#   ./scripts/ver-pdf.sh --quicklook x.pdf   # vista rápida (espacio) en vez de Preview

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

open_all=false
quicklook=false
target=""

while [ $# -gt 0 ]; do
  case "$1" in
    --all) open_all=true; shift ;;
    --quicklook|-q) quicklook=true; shift ;;
    -h|--help)
      sed -n '2,11p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *) target="$1"; shift ;;
  esac
done

if [ -z "$target" ]; then
  echo "Falta argumento. Uso: $0 [--all] [--quicklook] <archivo-o-termino>"
  echo ""
  echo "Tip: corre primero ./scripts/listar-pdfs.sh para ver qué PDFs hay."
  exit 1
fi

# 1) Si es ruta válida tal cual, ábrela.
if [ -f "$target" ]; then
  matches=("$target")
else
  # 2) Buscar por coincidencia en el nombre dentro del proyecto.
  mapfile -t matches < <(find "$ROOT" -type f -iname "*.pdf" -iname "*$target*")
fi

if [ "${#matches[@]}" -eq 0 ]; then
  echo "No encontré ningún PDF que coincida con: $target"
  exit 1
fi

if [ "${#matches[@]}" -gt 1 ] && [ "$open_all" = false ]; then
  echo "Encontré ${#matches[@]} coincidencias:"
  for i in "${!matches[@]}"; do
    printf "  [%d] %s\n" "$((i + 1))" "${matches[$i]#$ROOT/}"
  done
  echo ""
  echo "Abriendo la primera. Usa --all para abrir todas."
  matches=("${matches[0]}")
fi

for pdf in "${matches[@]}"; do
  echo "Abriendo: ${pdf#$ROOT/}"
  if [ "$quicklook" = true ]; then
    qlmanage -p "$pdf" >/dev/null 2>&1 &
  else
    open -a Preview "$pdf"
  fi
done
