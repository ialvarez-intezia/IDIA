#!/usr/bin/env python3
"""Estampa la fecha de envío y avanza el estado en el meta.json de una propuesta.

Lo invoca scripts/generar-pdf.sh tras generar el PDF: como toda entrega pasa por ese
script, el registro queda actualizado sin depender de que alguien lo recuerde.

Modelo de estados (flujo real del usuario, §4.19): en cuanto una propuesta queda
terminada se envía al cliente ese mismo instante — no existe limbo "generada pero sin
enviar". Por eso al generar el PDF el estado de reposo es **Enviada**, no "Entregada".
El único hueco lo abre una corrección: el usuario marca "En corrección" cuando la
propuesta vuelve a revisión, y al regenerar (cerrada la corrección) regresa a "Enviada".

Uso:
  python3 scripts/estampar-entrega.py <ruta/meta.json> <YYYY-MM-DD>

Reglas (append-only, nunca pisa el resultado de venta):
  - fecha_entrega vacía/null        -> se fija a la fecha de hoy (= fecha de envío original).
  - estado "Borrador" o "En corrección" -> sube a "Enviada" (terminado = enviado).
  - estado manual (Enviada / Aprobada / Perdida) -> NO se toca.
  - fecha_entrega ya puesta          -> NO se sobrescribe (se conserva la fecha de envío original).
  - meta.json ausente                -> advertencia visible en stderr (exit 0, no falla la entrega).
"""
import json
import os
import sys

# "Entregada" se conserva solo como valor legacy tolerado (≈ Enviada); ya no se produce.
ESTADOS_VALIDOS = {"Borrador", "En corrección", "Enviada", "Aprobada", "Perdida", "Entregada"}


def main():
    if len(sys.argv) < 3:
        print("Uso: estampar-entrega.py <ruta/meta.json> <YYYY-MM-DD>", file=sys.stderr)
        return 2

    meta_path = sys.argv[1]
    hoy = sys.argv[2]

    if not os.path.exists(meta_path):
        carpeta = os.path.dirname(meta_path) or "."
        print(
            f"\n  ⚠️  ADVERTENCIA: esta carpeta no tiene meta.json — la entrega NO quedó "
            f"registrada.\n      Crea {meta_path} (codigo, cliente, tipo, eje, "
            f"estado, fecha_entrega).\n      Carpeta: {carpeta}\n",
            file=sys.stderr,
        )
        return 0

    with open(meta_path, encoding="utf-8") as f:
        data = json.load(f)

    estado_prev = data.get("estado")
    cambios = []

    if not data.get("fecha_entrega"):
        data["fecha_entrega"] = hoy
        cambios.append(f"fecha_entrega={hoy}")

    if estado_prev in ("Borrador", "En corrección"):
        data["estado"] = "Enviada"
        cambios.append(f"estado: {estado_prev} → Enviada")

    if cambios:
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print(f"  → Registro actualizado: {' · '.join(cambios)}")
    else:
        print(
            f"  → Registro sin cambios (estado={estado_prev}, "
            f"fecha_entrega={data.get('fecha_entrega')}) — se respeta lo manual."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
