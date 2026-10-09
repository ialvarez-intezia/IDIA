#!/usr/bin/env python3
"""
migrar-datos-v3.py — Migra un datos.json de la plantilla compacta v2 a la v3 (2026-10-08).

La v3 aplica las correcciones de Keiber Quintana del 2026-10-08: ninguna propuesta lleva semanas, sesiones ni fechas
(el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque). Este script hace lo
mecánico y lista lo que hay que reescribir a mano:

  1. "version": 2 -> 3.
  2. Quita ruta.semanas_total, ruta.tope_h_semana, frentes[].semanas, fases[].rango y retorno.semana_medicion.
  3. Limpia el prefijo de semanas de los títulos de hito («Semana 1 · Arranque» -> «Arranque»).
  4. Lista (no reescribe) los textos de cara al cliente que todavía dicen «semana», «sesión» o usan los tokens
     retirados ({semanas_txt}, {semana_medicion}, {tope_h_semana}…): el generador los bloquea hasta que se reescriban.

No toca las fuentes citadas (portada.fuente, portada.contratacion.fuente, metodo.ejemplos[].fuente,
retorno.origen_datos), que van tal cual.

Uso
    python3 scripts/migrar-datos-v3.py <slug | ruta/datos.json>            # migra en su lugar y deja copia .v2.<sello>.bak
    python3 scripts/migrar-datos-v3.py <slug | ruta> --salida otro.json    # escribe en otro archivo
    python3 scripts/migrar-datos-v3.py <slug | ruta> --solo-revisar        # no escribe: solo informa
Después: python3 scripts/generar-habilidades-compacto.py <slug> (y --actualizar-css: la v3 trae CSS nuevo).
"""
import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPUESTAS = ROOT / "clientes" / "propuestas"

RE_SEMANA = re.compile(r"(?<!por )(?<!cada )(?<!a la )\bsemanas?\b", re.I)   # las tasas del cliente («12 h por semana») sí van
RE_SESION = re.compile(r"\bsesi[oó]n(?:es)?\b", re.I)
RE_TOKEN_RET = re.compile(r"\{\s*(semanas|semanas_txt|semana_medicion|tope_h_semana|tope_h_dia)\s*\}")
# «Semana 1 · », «Semanas 1 a 5 · », «Semanas 3 y 4 · », «S1-S3 · », «Antes de la semana 5: » …
RE_PREFIJO_HITO = re.compile(
    r"^\s*(?:semanas?\s+\d+(?:\s*(?:a|al|y|-|–)\s*\d+)?|s\d{1,2}(?:\s*-\s*s?\d{1,2})?)\s*(?:·|:|-|–)\s*", re.I)
FUENTES = ("portada.fuente", "portada.contratacion.fuente", "retorno.origen_datos")
INTERNOS = ("supuestos", "pendientes", "origen", "fuente_insumo", "eje", "meta_tipo", "retorno.aval_posiciones")   # no van al deck


def es_fuente(ruta):
    return ruta.startswith(FUENTES) or ruta.startswith(INTERNOS) or re.match(r"^metodo\.ejemplos\[\d+\]\.fuente$", ruta) is not None


def recorrer(nodo, ruta, acum):
    """Rutas de los textos de cara al cliente que mencionan semanas o sesiones (o tokens retirados)."""
    if isinstance(nodo, dict):
        for k, v in nodo.items():
            if str(k).startswith("_"):
                continue
            recorrer(v, "%s.%s" % (ruta, k) if ruta else str(k), acum)
    elif isinstance(nodo, list):
        for i, v in enumerate(nodo):
            recorrer(v, "%s[%d]" % (ruta, i), acum)
    elif isinstance(nodo, str) and not es_fuente(ruta):
        if RE_SEMANA.search(nodo) or RE_SESION.search(nodo) or RE_TOKEN_RET.search(nodo):
            acum.append((ruta, nodo))


def migrar(d):
    """Aplica los cambios mecánicos. Devuelve la lista de cambios hechos."""
    hechos = []
    d["version"] = 3
    hechos.append("version: 2 -> 3")
    ruta = d.get("ruta") if isinstance(d.get("ruta"), dict) else {}
    for k in ("semanas_total", "tope_h_semana"):
        if k in ruta:
            hechos.append("ruta.%s: quitado (era %r)" % (k, ruta.pop(k)))
    for i, fr in enumerate(d.get("frentes") or []):
        if isinstance(fr, dict) and "semanas" in fr:
            hechos.append("frentes[%d].semanas: quitado (era %r)" % (i, fr.pop("semanas")))
    for i, f in enumerate(d.get("fases") or []):
        if isinstance(f, dict) and "rango" in f:
            hechos.append("fases[%d].rango: quitado (era %r)" % (i, f.pop("rango")))
    if "anunciar_duracion" in d:   # v2.1 (Ivana, 2026-10-08): en la v3 ninguna propuesta anuncia semanas ni sesiones
        hechos.append("anunciar_duracion: quitado (era %r)" % d.pop("anunciar_duracion"))
    ret = d.get("retorno") if isinstance(d.get("retorno"), dict) else {}
    if "semana_medicion" in ret:
        hechos.append("retorno.semana_medicion: quitado (era %r)" % ret.pop("semana_medicion"))
    for i, h in enumerate(ruta.get("hitos") or []):
        if isinstance(h, dict) and isinstance(h.get("titulo"), str):
            nuevo = RE_PREFIJO_HITO.sub("", h["titulo"]).strip()
            if nuevo and nuevo != h["titulo"]:
                hechos.append("ruta.hitos[%d].titulo: %r -> %r" % (i, h["titulo"], nuevo[:1].upper() + nuevo[1:]))
                h["titulo"] = nuevo[:1].upper() + nuevo[1:]
    return hechos


def main():
    ap = argparse.ArgumentParser(description="Migra un datos.json de la plantilla compacta v2 a la v3 (sin semanas ni sesiones)")
    ap.add_argument("objetivo", help="slug de clientes/propuestas/<slug> o ruta a un datos.json")
    ap.add_argument("--salida", help="escribir el resultado en otro archivo (por defecto, en su lugar con copia .bak)")
    ap.add_argument("--solo-revisar", action="store_true", help="no escribe: informa los cambios y lo que queda a mano")
    a = ap.parse_args()
    p = Path(a.objetivo)
    if not p.suffix:
        p = PROPUESTAS / a.objetivo / "datos.json"
    if not p.exists():
        sys.exit("ERROR: no existe %s" % p)
    try:
        d = json.loads(p.read_text(encoding="utf-8-sig"))
    except ValueError as e:
        sys.exit("ERROR: %s no es JSON válido: %s" % (p, e))
    v = d.get("version") if isinstance(d, dict) else None
    if v == 3:
        print("✓ %s ya está en la v3: nada que migrar." % p)
        pend = []
        recorrer(d, "", pend)
        for ruta, txt in pend:
            print("  ⚠ %s: %s" % (ruta, txt[:110]))
        return
    if v != 2:
        sys.exit("ERROR: %s declara version %r: este script migra de la v2 a la v3. Un datos.json v1 se migra antes a la v2 "
                 "(plantillas/habilidades-compacto.md §13)." % (p, v))
    hechos = migrar(d)
    pend = []
    recorrer(d, "", pend)
    print("== Migración v2 -> v3 · %s ==" % p)
    for h in hechos:
        print("  ✓ " + h)
    if pend:
        print("\nReescribir a mano (la propuesta no lleva semanas ni sesiones; el generador los bloquea):")
        for ruta, txt in pend:
            print("  ✗ %s: %s" % (ruta, txt[:140]))
        print("  Ideas: hitos y cuotas por evento («Arranque», «Fase 1 adoptada», «Cierre de la construcción», «+30 días del cierre»);"
              " duración en horas; «jornadas», «horas de trabajo», «módulos» o «etapas» en vez de «sesiones».")
    else:
        print("\n✓ No quedan textos con semanas ni sesiones.")
    if a.solo_revisar:
        print("\n(--solo-revisar: no se escribió nada)")
        return
    destino = Path(a.salida) if a.salida else p
    if not a.salida:
        sello = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        bak = p.with_name("%s.v2.%s.bak" % (p.name, sello))
        shutil.copy2(str(p), str(bak))
        print("\nCopia de la v2: %s" % bak)
    destino.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("Escrito: %s" % destino)
    print("Siguiente: corregir lo marcado con ✗ y regenerar con --actualizar-css (python3 scripts/generar-habilidades-compacto.py <slug> --actualizar-css).")


if __name__ == "__main__":
    main()
