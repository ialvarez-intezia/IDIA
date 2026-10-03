# Venemergencia · Dos decks (Fase 1 práctica + Fases 1+2 clon digital) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convertir CAP-047 en dos decks que conviven en `clientes/propuestas/venemergencia/`: Deck A (Fase 1 práctica, `index.html`) y Deck B (Fases 1+2 con clon digital, `index-completo.html`).

**Architecture:** Dos HTML independientes en la misma carpeta (sin sub-subcarpetas). Fase 1 se construye en Deck A y se clona en Deck B; Deck B añade 6 sesiones de Fase 2. Los scripts `generar-pdf.sh` y `verificar-propuesta.sh` se generalizan (aditivo) para apuntar a un HTML distinto de `index.html`. Las "pruebas" del dominio son `verificar-overflow.js` + `verificar-propuesta.sh` (gates bloqueantes §4.10/§4.13) + revisión visual del PDF.

**Tech Stack:** HTML/CSS estático (`../_base/styles.css` + `overrides.css`), Chrome headless (PDF), Python (AcroForms / customize), Node (verificar-overflow.js), Bash.

**Spec:** `docs/superpowers/specs/2026-06-09-venemergencia-cap047-dos-decks-clon-digital-design.md`

**Regla transversal §4.14:** antes de editar cada archivo, LEERLO en su estado actual. Antes de tocar la propuesta, releer `brief.md`, `programa.md`, `index.html`.

---

## Task 0: Generalizar scripts para multi-deck (§8, aditivo, ya confirmado)

**Files:**
- Modify: `scripts/generar-pdf.sh:26`
- Modify: `scripts/verificar-propuesta.sh:20` y la llamada a `verificar-overflow.js` (~línea 169)

- [ ] **Step 1: `generar-pdf.sh` — aceptar 2º arg opcional con el HTML**

Leer el archivo. Cambiar la línea 26:

```bash
# Antes:
HTML="$DIR/index.html"
# Después:
HTML="$DIR/${2:-index.html}"
```

- [ ] **Step 2: Verificar sintaxis y retrocompat**

Run: `bash -n scripts/generar-pdf.sh && echo SINTAXIS_OK`
Expected: `SINTAXIS_OK`. Sin 2º arg, `HTML` sigue resolviendo a `index.html` (cero regresión).

- [ ] **Step 3: `verificar-propuesta.sh` — aceptar 2º arg opcional**

Leer el archivo. Cambiar la línea ~20:

```bash
# Antes:
HTML="$DIR/index.html"
# Después:
HTML="$DIR/${2:-index.html}"
```

Y cambiar la llamada a overflow (~línea 169) para que verifique el HTML elegido en vez del slug:

```bash
# Antes:
if OVERFLOW_OUT=$(node "$ROOT/scripts/verificar-overflow.js" "$SLUG" 2>/dev/null); then
# Después:
if OVERFLOW_OUT=$(node "$ROOT/scripts/verificar-overflow.js" "$HTML" 2>/dev/null); then
```

(`verificar-overflow.js` ya acepta una ruta `.html` además del slug; pasar `$HTML` cubre ambos casos.)

- [ ] **Step 4: Verificar sintaxis**

Run: `bash -n scripts/verificar-propuesta.sh && echo SINTAXIS_OK`
Expected: `SINTAXIS_OK`

- [ ] **Step 5: Commit**

```bash
git add scripts/generar-pdf.sh scripts/verificar-propuesta.sh
git commit -m "feat(scripts): generar-pdf y verificar-propuesta aceptan HTML opcional (multi-deck)"
```

---

## Task 1: Deck A — reescribir Fase 1 a temario práctico en `index.html`

**Files:**
- Modify: `clientes/propuestas/venemergencia/index.html` (slides 3, 4, 5, 7, 8, 9, 10, 12)
- Modify: `clientes/propuestas/venemergencia/overrides.css` (roadmap simplificado, sin bifurcación F3)

Nuevo set de 5 módulos (orden final): I Fundamentos · II Ecosistema+Claude Design · III Cowork+Skills · IV Conectores/Plugins/integraciones · V Seguridad. La cascada deja de ser módulo; vive como narrativa.

- [ ] **Step 1: Slide 4 (s-program "El plan") — Fase 1 + teaser Fase 2, sin F3**

Sustituir las 3 cards (I Fase 1 / II Fase 2 / III Fase 3) por 2 cards: card I = Fase 1 (con los 5 chips de módulo nuevos: `Fundamentos y prompting`, `Ecosistema + Claude Design`, `Cowork y Skills`, `Conectores y Plugins`, `Seguridad`), card II = Fase 2 como continuación (clon digital, "se cotiza en la propuesta ampliada"). Chips ≤ ~28 chars (§4.10). Actualizar `.meta` a "Fase 1 cotizada hoy · Fase 2 (clon digital) como continuación".

- [ ] **Step 2: Slide 5 (s-roadmap) — simplificar a F1 → F2 ★, sin bifurcación**

En `index.html` quitar la ruta F3 (`.rmx-route-f3`) y la bifurcación doble; dejar journey lineal: ORIGEN F1 → RUTA F2 (clon digital) → ★ resultado. Ajustar textos: F2 = "Automatización + clon digital con Claude Code". En `overrides.css` neutralizar/retirar las reglas de la 2ª rama del fork (`.rmx-branch.rmx-dn` en fork/merge) para que el trazo quede lineal sin huecos. Verificar con overflow en Step 9.

- [ ] **Step 3: Slide 7 (Sesión 2 · Módulo II) — añadir Claude Design**

Título → "Módulo II: Ecosistema + Claude Design". Chips: `2.1 Projects: memoria de trabajo`, `2.2 Artifacts: entregables`, `2.3 Claude Design`, `2.4 Análisis de documentos`. Recursos: añadir "Claude Design". Resaltar `<strong>Claude Design</strong>` en cuerpo (primera aparición, §4.8).

- [ ] **Step 4: Slide 8 (Sesión 3 · Módulo III) — Cowork + Skills**

Título → "Módulo III: Cowork y Skills". Chips: `3.1 Qué es una Skill`, `3.2 Cowork: tareas asistidas`, `3.3 Construir tu Skill`, `3.4 Prueba e iteración`. Entregable: "Skill funcional propia + tarea automatizada en Cowork".

- [ ] **Step 5: Slide 9 (Sesión 4) — cambiar de Seguridad a Módulo IV Conectores/Plugins**

Reemplazar el contenido de Seguridad por "Módulo IV: Conectores, Plugins e integraciones". Chips: `4.1 Conectores a tus herramientas`, `4.2 Plugins`, `4.3 MCP (Model Context Protocol)`, `4.4 Automatización de un proceso`. Glosar MCP en un `<li>`/`<p>` (§4.12: "Model Context Protocol (MCP)"). Entregable: "1 proceso automatizado conectado a una herramienta que ya usan". Mención de "toque de Claude Code dentro de la app de Claude" en estrategias de enseñanza (sin terminal). `ruta-fill` width 80%, "Sesión 4 de 5".

- [ ] **Step 6: Slide 10 (Sesión 5) — Seguridad pasa a Módulo V (era cascada)**

Reemplazar "Módulo V: Modelo cascada" por "Módulo V: Seguridad e información sensible" (mover aquí el contenido de seguridad que estaba en slide 9: protocolos reales de Anthropic, qué compartir/qué no, criterio de uso seguro). Cierre con nota de cascada como narrativa ("queda listo para replicar a su equipo"). `ruta-fill` 100%, "Sesión 5 de 5".

- [ ] **Step 7: Slide 3 (Objetivos) — actualizar específicos**

Objetivo específico 2 → "Integrar el ecosistema de Claude (Projects, Artifacts, Claude Design) y crear una Skill propia". Añadir/ajustar uno a "Conectar Claude a sus herramientas y dejar al menos un proceso automatizado". El objetivo de "replicar al equipo" se mantiene como cierre (cascada = porqué). General intacto.

- [ ] **Step 8: Slide 12 (Beneficios) — perfil egreso + entregables prácticos**

Perfil "Saber hacer" → "aplica prompting, usa Projects/Artifacts/Claude Design, construye una Skill y automatiza un proceso con conectores". Beneficio: mencionar "entregables útiles desde la Fase 1: una Skill, un proceso automatizado y un caso real". (El AcroForm `Entregables` se rellena en Task 2.)

- [ ] **Step 9: Gate de overflow Deck A**

Run: `node scripts/verificar-overflow.js venemergencia`
Expected: `0 problemas` / sin TEXTO TRUNCADO, sin desbordes. Si hay desborde → acortar copy (chips ≤28 chars), no ensanchar cajas. Repetir hasta limpio.

- [ ] **Step 10: Commit**

```bash
git add clientes/propuestas/venemergencia/index.html clientes/propuestas/venemergencia/overrides.css
git commit -m "feat(venemergencia): Fase 1 práctica (Cowork, Conectores, Plugins, Claude Design) + roadmap sin F3"
```

---

## Task 2: Deck A — verificar, generar PDF y customize

**Files:**
- Modify: `scripts/customize-venemergencia.py` (Entregables, Acreditación, pasos)

- [ ] **Step 1: Gate completo Deck A**

Run: `./scripts/verificar-propuesta.sh venemergencia`
Expected: `0 errores bloqueantes` (sin guion largo, sin smart-quotes en atributos, sin `[CÓDIGO]` suelto, sin términos económicos en pasos, overflow OK).

- [ ] **Step 2: Generar PDF base**

Run: `./scripts/generar-pdf.sh venemergencia`
Expected: `✓ Listo: …/CAP-047 Adopción de Claude en cascada.pdf`

- [ ] **Step 3: Actualizar `customize-venemergencia.py`**

Leer el script actual. Ajustar el valor `/V` de:
- `Entregables`: 2–4 destacados del desglose práctico (`Skill funcional`, `Proceso automatizado con conectores`, `Caso real de su área`, `Criterio de uso seguro`) + los 3 institucionales (`ENTREGABLES_DEFAULT`). Líneas cortas de un renglón (≤8–9 líneas visuales).
- `Acreditacion`: `[CÓDIGO]` → `CAP-047`.
- `Paso01–03 Titulo/Body`: logística (§4.15), body ≤130 chars. (Confirmar que ya están; ajustar si el contenido cambió.)

- [ ] **Step 4: Correr customize (par PDF↔customize §10)**

Run: `python3 scripts/customize-venemergencia.py "clientes/propuestas/venemergencia/CAP-047 Adopción de Claude en cascada.pdf"`
Expected: confirma campos `/V` escritos.

- [ ] **Step 5: Revisión visual del PDF Deck A** (no automatizable, §4.10)

Abrir el PDF, revisar slide por slide: logos, alineación, cajas Programa/Entregables completas, sin "…", pasos con texto real.

- [ ] **Step 6: Commit**

```bash
git add scripts/customize-venemergencia.py "clientes/propuestas/venemergencia/CAP-047 Adopción de Claude en cascada.pdf"
git commit -m "feat(venemergencia): Deck A Fase 1 — PDF + AcroForms pre-llenados"
```

---

## Task 3: Deck B — scaffold `index-completo.html` desde Deck A

**Files:**
- Create: `clientes/propuestas/venemergencia/index-completo.html`

- [ ] **Step 1: Clonar Deck A**

Run: `cp clientes/propuestas/venemergencia/index.html clientes/propuestas/venemergencia/index-completo.html`

- [ ] **Step 2: Portada (slide 1) — alcance Fases 1+2 y hero clon digital**

`span.codigo` → "Código: CAP-047 · Fases 1+2". `h1` mantiene "Adopción de Claude<br><span class="hl">en cascada</span>" pero el `.lead` añade la Fase 2: "…​y construyen su <strong>clon digital</strong>: un segundo cerebro que les ayuda a decidir mejor." Comentario de cabecera del archivo: anotar "Deck B · Fases 1+2 · 22 slides".

- [ ] **Step 3: Slide 4 (El plan) — 2 fases reales (no teaser)**

Card I = Fase 1 (5 chips) · card II = Fase 2 "Clon digital con Claude Code · 6 sesiones / 12 h · cotizada en esta propuesta". `.meta` → "Programa completo: Fase 1 (10 h) + Fase 2 (12 h)".

- [ ] **Step 4: Slide 5 (Roadmap) — F1 → F2 → ★ clon digital**

ORIGEN F1 → RUTA F2 (Claude Code, terminal/IDE, clon digital) → ★ "Cada directivo con su segundo cerebro operativo". Sin F3.

- [ ] **Step 5: Slide 3 (Objetivos) — cubrir ambas fases**

Añadir objetivo general/específico de Fase 2: "Construir un agente personal (clon digital) en Claude Code que apoye decisiones y automatice trabajo en varias áreas".

- [ ] **Step 6: Commit (scaffold, contadores aún sin renumerar)**

```bash
git add clientes/propuestas/venemergencia/index-completo.html
git commit -m "feat(venemergencia): scaffold Deck B (index-completo) con portada/plan/roadmap de 2 fases"
```

---

## Task 4: Deck B — insertar 6 sesiones de Fase 2 + renumerar + CSS

**Files:**
- Modify: `clientes/propuestas/venemergencia/index-completo.html`
- Modify: `clientes/propuestas/venemergencia/overrides.css` (acento visual Fase 2, si hace falta)

- [ ] **Step 1: Insertar 6 slides `s-schedule` de Fase 2**

Tras el slide de Fase 1 · Sesión 5 (Módulo V Seguridad) y antes de Metodología, insertar 6 secciones `.slide.s-schedule` con eyebrow "04 · Fase 2 · Clon digital". Contenido por sesión (Temas/Tiempo/Estrategias/Recursos), `ruta-step` "Sesión N de 6", `ruta-fill` width 17/33/50/67/83/100%:

1. **Claude Code a fondo** — entorno real (terminal + IDE), proyectos, archivos, contexto, CLAUDE.md.
2. **Diseño del clon digital** — qué decisiones apoya, fuentes de conocimiento, alcance del segundo cerebro.
3. **Construcción del agente** — memoria persistente, conocimiento del área, documentos, subagentes.
4. **Conexión a herramientas** — MCP (Model Context Protocol) + conectores; el clon actúa dentro de las herramientas que ya usa (§4.11, no migración).
5. **Automatización de flujos de decisión** — el agente facilita trabajo en varias áreas (multi-paso).
6. **Seguridad, gobernanza y puesta en producción** — uso responsable del clon, datos sensibles, mantenimiento.

Glosar MCP en cada slide donde aparezca (§4.12). Chips ≤ ~28 chars. Resaltar `<strong>clon digital</strong>`, `<strong>Claude Code</strong>` en primera aparición por slide (§4.8).

- [ ] **Step 2: Renumerar contadores de TODO el deck a `NN / 22`**

Actualizar todos los `<span class="counter">NN / 16</span>` a `/ 22` y la numeración secuencial 01–22. Slides Fase 1 conservan eyebrow "04 · Fase 1 · Ruta de aprendizaje"; Fase 2 usa "04 · Fase 2 · Clon digital".

- [ ] **Step 3: CSS Fase 2 (si necesario)**

Si se quiere distinguir Fase 2, añadir en `overrides.css` un acento (p.ej. borde/eyebrow), reutilizando `.s-schedule` de `_base`. Mínimo cambio; no romper Fase 1.

- [ ] **Step 4: Gate de overflow Deck B**

Run: `node scripts/verificar-overflow.js clientes/propuestas/venemergencia/index-completo.html`
Expected: sin desbordes ni "…". Ajustar copy hasta limpio.

- [ ] **Step 5: Commit**

```bash
git add clientes/propuestas/venemergencia/index-completo.html clientes/propuestas/venemergencia/overrides.css
git commit -m "feat(venemergencia): Deck B — 6 sesiones Fase 2 (clon digital) + contadores /22"
```

---

## Task 5: Deck B — verificar, generar PDF y customize

**Files:**
- Create: `scripts/customize-venemergencia-completo.py`

- [ ] **Step 1: Gate completo Deck B**

Run: `./scripts/verificar-propuesta.sh venemergencia index-completo.html`
Expected: `0 errores bloqueantes`.

- [ ] **Step 2: Generar PDF Deck B**

Run: `./scripts/generar-pdf.sh venemergencia index-completo.html`
Expected: `✓ Listo: …/CAP-047 · Fases 1+2 ….pdf` (nombre distinto del Deck A).

- [ ] **Step 3: Crear `customize-venemergencia-completo.py`**

Partir de `customize-venemergencia.py`. Ajustar: `Entregables` añade los de Fase 2 (`Clon digital funcional en Claude Code`, `Agente conectado a sus herramientas`) además de los de Fase 1; `Acreditacion` `[CÓDIGO]` → `CAP-047`; pasos logísticos (§4.15) cubren las dos fases. Apuntar al PDF de Deck B.

- [ ] **Step 4: Correr customize Deck B**

Run: `python3 scripts/customize-venemergencia-completo.py "clientes/propuestas/venemergencia/CAP-047 · Fases 1+2 ….pdf"`
(Usar el nombre exacto que imprimió generar-pdf en Step 2.)

- [ ] **Step 5: Revisión visual del PDF Deck B** (§4.10) — 22 slides, énfasis en las 6 de Fase 2.

- [ ] **Step 6: Commit**

```bash
git add scripts/customize-venemergencia-completo.py "clientes/propuestas/venemergencia/CAP-047 · Fases 1+2 ".*.pdf
git commit -m "feat(venemergencia): Deck B Fases 1+2 — PDF + AcroForms pre-llenados"
```

---

## Task 6: Cierre — brief y aprendizajes

**Files:**
- Modify: `clientes/propuestas/venemergencia/brief.md`
- Modify: `aprendizajes.md`

- [ ] **Step 1: Actualizar `brief.md`**

Reflejar: dos decks (Fase 1 / Fases 1+2), Fase 1 temario práctico (5 módulos nuevos), Fase 2 = 6 sesiones/12 h clon digital con Claude Code (terminal/IDE) ahora **cotizada en deck B**, **F3 retirada**, mismo CAP-047 con dos alcances, archivos `index.html` + `index-completo.html`.

- [ ] **Step 2: Registrar en `aprendizajes.md`** (antepuesto arriba, §9)

Entrada 2026-06-09: dos decks en una carpeta (multi-deck en `generar-pdf.sh`/`verificar-propuesta.sh` vía 2º arg HTML), patrón clon digital/segundo cerebro como Fase 2 técnica.

- [ ] **Step 3: Commit**

```bash
git add clientes/propuestas/venemergencia/brief.md aprendizajes.md
git commit -m "docs(venemergencia): brief de dos alcances + aprendizaje multi-deck"
```

---

## Self-Review (cobertura del spec)

- §3.1 generalizar `generar-pdf.sh` → Task 0 ✓; (extra) `verificar-propuesta.sh` → Task 0 ✓
- §4 Deck A Fase 1 práctica (5 módulos nuevos, deliverables) → Task 1 + Task 2 ✓
- §5 Deck B Fases 1+2 + 6 sesiones clon digital → Task 3 + Task 4 + Task 5 ✓
- §6 reglas (§4.9/4.10/4.11/4.12/4.13/4.14/4.15) → gates en Task 1.9, 2.1, 4.4, 5.1 + revisión visual ✓
- §7 par PDF↔customize en ambos decks → Task 2 + Task 5 ✓
- Duplicación Fase 1 (clonar en Deck B) → Task 3.1 ✓
- §8 fuera de alcance (F3, calendario, precio) → respetado ✓

**Pendiente de dato en ejecución:** el nombre exacto del PDF de Deck B (depende del `span.codigo`/`h1`) se captura del output de `generar-pdf.sh` en Task 5.2 y se usa literal en 5.4.
