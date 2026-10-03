# Rediseño Catálogo de Talleres — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rediseñar el deck `Catalogo Talleres 2026` al lenguaje visual "HUD Tecnológico", añadiendo botones de video y "aplica aquí" por taller y 5 separadoras de sección.

**Architecture:** Se edita en sitio el deck del catálogo (`index.html` + `styles.css`). Las fuentes, tokens de marca, dimensiones de `.slide` y reglas de impresión se conservan; los estilos por tipo de slide se reemplazan por un sistema HUD nuevo en un archivo `hud.css`. Cada apartado se construye, se previsualiza en un servidor local y se aprueba antes de continuar. Las 3 slides imagen no se tocan.

**Tech Stack:** HTML + CSS (container queries, unidad `cqw`), fuente Graphit, Chrome headless `--print-to-pdf` para el PDF final, `python3 -m http.server` para previsualización.

**Spec de referencia:** `docs/superpowers/specs/2026-05-17-rediseno-catalogo-talleres-design.md`

**Maquetas aprobadas (fuente visual de verdad):** `.superpowers/brainstorm/26262-1779075058/content/` — archivos `programa-hud-v3.html`, `apartados-portada-seccion-v2.html`, `apartados-narrativa.html`, `apartados-rutas-v2.html`, `apartados-rutas-cta.html`. El CSS de cada apartado se toma de su maqueta aprobada (clases `.pg`, `.sl`, `.cov`, `.sec`, `.stmt`, `.rt`, `.cta`, etc.) y se traslada a `hud.css` sin alterarlo.

**Directorio de trabajo:** `clientes/propuestas/catalogo/Catalogo Talleres 2026/`

---

## Notas sobre verificación

Este rediseño es trabajo de diseño visual; no hay tests unitarios. La verificación de cada apartado es:
1. **Preview** en el servidor local — el agente confirma que renderiza sin errores y que coincide con la maqueta aprobada.
2. **Checkpoint del usuario** — el usuario revisa el apartado en el navegador y aprueba antes de commitear.
3. **Commit** del apartado.

---

## Task 1: Fundación HUD + servidor local

**Files:**
- Create: `clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css`
- Modify: `clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html` (head: `<link>` y bloque `<style>`)
- Read-only: `clientes/propuestas/catalogo/Catalogo Talleres 2026/styles.css` (líneas 15-66 — fuentes, tokens, `.slide`)

- [ ] **Step 1: Leer la base de `styles.css`**

Confirmar: `@font-face` Graphit (líneas 15-16), tokens `--black/--yellow/--orange/--white/--gradient-warm` (líneas 21-27), `.slide { aspect-ratio: 1123/794 }` (línea 58). Estos NO se modifican.

- [ ] **Step 2: Habilitar container queries en `.slide`**

En `styles.css`, añadir a la regla `.slide` (≈línea 55): `container-type: inline-size;`. Esto hace que la unidad `cqw` de las maquetas equivalga a 1% del ancho de la slide.

- [ ] **Step 3: Crear `hud.css` con la base HUD compartida**

Crear `hud.css` con la base reutilizable por todos los apartados rediseñados (tomada de las maquetas):

```css
/* hud.css — lenguaje visual HUD del catálogo de talleres */

/* Base de toda slide rediseñada */
.sl-hud{ background:#050505; color:#fff; position:relative; overflow:hidden; }
.sl-hud::before{ content:""; position:absolute; inset:0; pointer-events:none;
  background-image:
    linear-gradient(rgba(244,186,26,.055) 1px,transparent 1px),
    linear-gradient(90deg,rgba(244,186,26,.055) 1px,transparent 1px);
  background-size:3.4cqw 3.4cqw; }
/* Brackets en las 4 esquinas */
.sl-hud .crn{ position:absolute; width:2.4cqw; height:2.4cqw;
  border:.22cqw solid var(--yellow); z-index:3; }
.sl-hud .c1{ top:1.6cqw; left:1.6cqw; border-right:0; border-bottom:0; }
.sl-hud .c2{ top:1.6cqw; right:1.6cqw; border-left:0; border-bottom:0; }
.sl-hud .c3{ bottom:1.6cqw; left:1.6cqw; border-right:0; border-top:0; }
.sl-hud .c4{ bottom:1.6cqw; right:1.6cqw; border-left:0; border-top:0; }
/* Eyebrow monoespaciado y contador */
.sl-hud .eye{ font-family:ui-monospace,SFMono-Regular,monospace; font-weight:700;
  font-size:1.25cqw; letter-spacing:.16em; text-transform:uppercase; color:var(--yellow); }
.sl-hud .cnt{ font-family:ui-monospace,monospace; font-size:1.15cqw;
  color:#666; letter-spacing:.1em; }
```

- [ ] **Step 4: Enlazar `hud.css` y vaciar el bloque `<style>` inline**

En `index.html` `<head>`: añadir `<link rel="stylesheet" href="hud.css">` después del link a `styles.css`. Vaciar el bloque `<style>` inline (líneas ≈13-153 actuales) — su contenido se reemplaza apartado por apartado en las tareas siguientes. Conservar solo la regla `.s-img-page` (slides imagen intactas):

```css
.s-img-page { background: var(--black); padding: 0; }
.s-img-page img { width: 100%; height: 100%; object-fit: contain; display: block; }
```

- [ ] **Step 5: Levantar el servidor local de previsualización**

Run: `cd "clientes/propuestas/catalogo/Catalogo Talleres 2026" && python3 -m http.server 8080`
Expected: servidor sirviendo en `http://localhost:8080`. Abrir `index.html` — el deck carga; las 3 slides imagen y la estructura siguen visibles (los apartados aún sin estilo HUD se verán planos, es esperado).

- [ ] **Step 6: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/styles.css"
git commit -m "feat(catalogo): fundación HUD — hud.css + container queries"
```

---

## Task 2: Apartado Portada

**Files:**
- Modify: `hud.css` (añadir estilos `.cov`)
- Modify: `index.html` (slide 1)
- Maqueta: `.superpowers/brainstorm/26262-1779075058/content/apartados-portada-seccion-v2.html` (clase `.cov`)

- [ ] **Step 1: Añadir estilos `.cov` a `hud.css`**

Copiar el bloque CSS `.cov ...` de la maqueta `apartados-portada-seccion-v2.html` a `hud.css`. Las clases base (`.crn`, `.eye`, `.cnt`) ya existen en `.sl-hud` — no duplicarlas.

- [ ] **Step 2: Reescribir la slide 1 en `index.html`**

Reemplazar `<section class="slide s-cat-cover">` por `<section class="slide sl-hud cov">` con la estructura de la maqueta. Diferencias con la maqueta:
- El placeholder de texto `intez·ia` se sustituye por el logo real: `<img src="../../../../logos/educacion/BLANCO.png" alt="Intezia Educación" class="cov-logo">` (añadir `.cov-logo{ height:7cqw; width:auto; }` a `hud.css`).
- Contenido textual: idéntico al de la slide 1 actual (eyebrow, h1 "Catálogo de / talleres 2026", lead, badge).
- Contador: `01 / 33`.

- [ ] **Step 3: Preview**

Refrescar `http://localhost:8080`. Verificar slide 1: logo real visible, título con aire entre líneas, badge inferior, rejilla y brackets.

- [ ] **Step 4: Checkpoint del usuario**

Pedir al usuario que revise la portada en el navegador y apruebe.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — portada"
```

---

## Task 3: Apartado Separadora de sección (×5)

**Files:**
- Modify: `hud.css` (añadir estilos `.sec`)
- Modify: `index.html` (insertar 5 nuevas `<section>`)
- Maqueta: `apartados-portada-seccion-v2.html` (clase `.sec`)

- [ ] **Step 1: Añadir estilos `.sec` a `hud.css`**

Copiar el bloque CSS `.sec ...` de la maqueta a `hud.css`.

- [ ] **Step 2: Insertar las 5 separadoras en `index.html`**

Insertar una `<section class="slide sl-hud sec">` antes del primer taller de cada sección, con la estructura de la maqueta. Contenido de cada una (número, nombre, descripción, lista de talleres con sus códigos):

- **Sección 1 · Cultura y Estrategia** — antes de TA-003. Talleres: TA-003, TA-017, TA-004, TA-001, TA-019.
- **Sección 2 · Especialización Funcional** — antes de TA-005. Talleres: TA-005, TA-006, TA-007, TA-008, TA-009, TA-010, TA-011, TA-013, TA-002.
- **Sección 3 · Claude Deep-Dive** — antes de TA-016. Talleres: TA-016, TA-018.
- **Sección 4 · Stack Microsoft** — antes de TA-020. Talleres: TA-020.
- **Sección 5 · Bootcamps Técnicos** — antes de TA-012. Talleres: TA-012, TA-014, TA-015.

Los nombres de los talleres se copian de los `<h2>` actuales del `index.html`. Descripción breve de cada sección: redactarla a partir del enfoque de la sección (nivelación/estrategia, especialización por área, deep-dive en Claude, herramientas Microsoft, bootcamps técnicos). Contadores se ajustan en Task 10.

- [ ] **Step 3: Preview**

Refrescar. Verificar las 5 separadoras: número gigante, lista de talleres con chips de código.

- [ ] **Step 4: Checkpoint del usuario** — el usuario aprueba.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — 5 separadoras de sección"
```

---

## Task 4: Apartado Manifiesto

**Files:**
- Modify: `hud.css` (añadir estilos `.stmt`)
- Modify: `index.html` (slide Manifiesto)
- Maqueta: `apartados-narrativa.html` (clase `.stmt`)

- [ ] **Step 1: Añadir estilos `.stmt` a `hud.css`**

Copiar el bloque CSS `.stmt ...` de la maqueta (sirve para Manifiesto y Conclusión).

- [ ] **Step 2: Reescribir la slide Manifiesto en `index.html`**

Reemplazar `<section class="slide s-manifesto">` por `<section class="slide sl-hud stmt">` con la estructura de la maqueta: eyebrow "El manifiesto Intezia", h2, párrafos y `.closing`. Texto: la versión condensada aprobada en la maqueta `apartados-narrativa.html`.

- [ ] **Step 3: Preview** — refrescar, verificar el Manifiesto.

- [ ] **Step 4: Checkpoint del usuario** — el usuario aprueba.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — manifiesto"
```

---

## Task 5: Apartado Slide de programa — base + primer taller

**Files:**
- Modify: `hud.css` (añadir estilos `.pg`)
- Modify: `index.html` (slide TA-008)
- Maqueta: `programa-hud-v3.html` (clase `.pg`)

- [ ] **Step 1: Añadir estilos `.pg` a `hud.css`**

Copiar el bloque CSS `.pg ...` completo de `programa-hud-v3.html`. Incluye: rejilla de módulos, recuadro `.mod`, numeral `.rom`, botón `.video`, banda `.cta`. Añadir variantes de rejilla por cantidad de módulos:

```css
.pg .grid.m4{ grid-template-columns:1fr 1fr; }              /* 4 módulos: 2×2 */
.pg .grid.m5{ grid-template-columns:repeat(6,1fr); }        /* 5 módulos: 3+2 */
.pg .grid.m5 .mod:nth-child(1),
.pg .grid.m5 .mod:nth-child(2),
.pg .grid.m5 .mod:nth-child(3){ grid-column:span 2; }
.pg .grid.m5 .mod:nth-child(4){ grid-column:2/4; }
.pg .grid.m5 .mod:nth-child(5){ grid-column:4/6; }
/* 6 módulos: la regla base 3×2 ya aplica */
```

- [ ] **Step 2: Reescribir la slide TA-008 en `index.html`**

Reemplazar `<section class="slide s-program">` de TA-008 por `<section class="slide sl-hud pg">` con la estructura de la maqueta:
- Eyebrow: `TA-008 · Sección 2 · Especialización Funcional · Ventas`.
- Título con palabra clave en `<b>`.
- Botón video: `<a class="video" href="#" data-taller="TA-008"><span class="pico">▶</span> Más información</a>` — `href="#"` placeholder hasta tener URLs.
- 6 módulos: numeral, título, objetivo, temas — contenido idéntico al TA-008 actual.
- Banda: `<a class="cta" href="#" data-aplica="TA-008">…</a>` — `href="#"` placeholder.
- Footer con logo y código (patrón actual).

- [ ] **Step 3: Preview** — refrescar, verificar TA-008: 6 módulos sin huecos, botón "Más información", banda "Aplica aquí".

- [ ] **Step 4: Checkpoint del usuario** — el usuario aprueba el patrón de slide de programa.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — slide de programa (TA-008)"
```

---

## Task 6: Aplicar slide de programa a los 19 talleres restantes

**Files:**
- Modify: `index.html` (19 slides de programa)
- Maqueta: `programa-hud-v3.html`

- [ ] **Step 1: Convertir los 19 talleres restantes**

Para cada uno de TA-003, TA-017, TA-004, TA-001, TA-019, TA-005, TA-006, TA-007, TA-009, TA-010, TA-011, TA-013, TA-002, TA-016, TA-018, TA-020, TA-012, TA-014, TA-015: reemplazar su `<section class="slide s-program">` por la estructura `sl-hud pg`, igual que TA-008. Reglas:
- El contenido (eyebrow, título, módulos con objetivo y temas) se copia **verbatim** del taller actual — no se altera.
- Aplicar la clase de rejilla según cantidad de módulos: `grid m4` (4 módulos), `grid m5` (5 módulos), `grid` (6 módulos).
- Cada botón video: `href="#" data-taller="TA-###"`. Cada banda aplica: `href="#" data-aplica="TA-###"`.

- [ ] **Step 2: Preview** — refrescar, recorrer los 20 talleres. Verificar especialmente un taller de 4 módulos y uno de 5 (rejilla correcta, sin desbordes).

- [ ] **Step 3: Checkpoint del usuario** — el usuario revisa los 20 talleres y aprueba.

- [ ] **Step 4: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — 19 talleres restantes"
```

---

## Task 7: Apartado Rutas Diamond

**Files:**
- Modify: `hud.css` (añadir estilos `.rt`)
- Modify: `index.html` (slide Rutas Diamond)
- Maqueta: `apartados-rutas-v2.html` (clase `.rt` — versión de bandas horizontales)

- [ ] **Step 1: Añadir estilos `.rt` a `hud.css`**

Copiar el bloque CSS `.rt ...` de `apartados-rutas-v2.html` (la versión de 3 bandas horizontales, NO la de columnas).

- [ ] **Step 2: Reescribir la slide Rutas Diamond en `index.html`**

Reemplazar `<section class="slide s-routes">` por `<section class="slide sl-hud rt">` con la estructura de bandas de la maqueta: 3 bandas (`.bd`) con número, contenido y resultado. Texto: el de la slide Rutas Diamond actual (condensado como en la maqueta). Conservar el footer.

- [ ] **Step 3: Preview** — refrescar, verificar las 3 bandas sin huecos.

- [ ] **Step 4: Checkpoint del usuario** — el usuario aprueba.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — Rutas Diamond"
```

---

## Task 8: Apartado Conclusión

**Files:**
- Modify: `index.html` (slide Conclusión)
- Maqueta: `apartados-narrativa.html` (clase `.stmt` — ya en `hud.css` desde Task 4)

- [ ] **Step 1: Reescribir la slide Conclusión en `index.html`**

Reemplazar `<section class="slide s-conclusion">` por `<section class="slide sl-hud stmt">` con la estructura de la maqueta: eyebrow "Conclusión", h2 "Su traje a la medida", párrafos y `.quote`. Texto: la versión condensada aprobada en la maqueta. No requiere CSS nuevo (`.stmt` ya existe).

- [ ] **Step 2: Preview** — refrescar, verificar la Conclusión.

- [ ] **Step 3: Checkpoint del usuario** — el usuario aprueba.

- [ ] **Step 4: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — conclusión"
```

---

## Task 9: Apartado CTA de cierre

**Files:**
- Modify: `hud.css` (añadir estilos `.cta` de cierre — usar prefijo `.end` para no chocar con la banda `.cta` del slide de programa)
- Modify: `index.html` (slide CTA)
- Maqueta: `apartados-rutas-cta.html` (clase `.cta` de cierre)

- [ ] **Step 1: Añadir estilos a `hud.css`**

Copiar el bloque CSS de la slide de cierre de `apartados-rutas-cta.html`. **Renombrar la clase `.cta` de cierre a `.endcta`** en el CSS para evitar colisión con la banda `.cta` del slide de programa (Task 5). Ajustar también `.cta .in`, `.cta .logo`, `.cta .msg`, `.cta .btn`, `.cta .foot`, `.cta .scan`, `.cta .scan2` → prefijo `.endcta`.

- [ ] **Step 2: Reescribir la slide CTA en `index.html`**

Reemplazar `<section class="slide s-cat-cta">` por `<section class="slide sl-hud endcta">` con la estructura de la maqueta:
- Logo real: `<img src="../../../../logos/educacion/BLANCO.png" alt="Intezia Educación">` en lugar del placeholder de texto.
- Mensaje "Rellena el formulario y empieza a ver cambios en tu empresa".
- Botón: `<a class="btn" href="#" data-aplica="cierre">▸ Aplica Aquí</a>` — `href="#"` placeholder.
- Footer institucional: `INTEZIA.COM · info@intezia.com · J-505657950 · Respaldados por Microsoft for Startups`.

- [ ] **Step 3: Preview** — refrescar, verificar la slide de cierre.

- [ ] **Step 4: Checkpoint del usuario** — el usuario aprueba.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/hud.css" \
        "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): rediseño HUD — CTA de cierre"
```

---

## Task 10: Integración final — contadores y orden

**Files:**
- Modify: `index.html` (todos los `.cnt` / `.counter`)

- [ ] **Step 1: Verificar el orden de las 33 slides**

Confirmar el orden contra la tabla §5 del spec: portada, detrás (img), rueda (img), manifiesto, ecosistema (img), separadora S1, 5 talleres S1, separadora S2, 9 talleres S2, separadora S3, 2 talleres S3, separadora S4, 1 taller S4, separadora S5, 3 talleres S5, Rutas Diamond, conclusión, CTA = 33.

- [ ] **Step 2: Renumerar todos los contadores a `NN / 33`**

Actualizar cada contador (`.cnt` en slides HUD, `.counter` en las 3 slides imagen si lo tienen) con su número correlativo `01 / 33` … `33 / 33`. Comentario del `<head>` de `index.html` actualizado (33 slides).

- [ ] **Step 3: Preview** — refrescar, recorrer el deck completo. Verificar numeración correlativa 01→33 y orden.

- [ ] **Step 4: Checkpoint del usuario** — el usuario revisa el deck completo y aprueba.

- [ ] **Step 5: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html"
git commit -m "feat(catalogo): integración final — contadores NN/33 y orden"
```

---

## Task 11: Generar el PDF y verificar hipervínculos

**Files:**
- Create/replace: `clientes/propuestas/catalogo/Catalogo Talleres 2026/Catalogo Talleres Intezia 2026.pdf`

- [ ] **Step 1: Generar el PDF con Chrome headless**

Run:
```bash
cd "clientes/propuestas/catalogo/Catalogo Talleres 2026"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf-no-header \
  --virtual-time-budget=15000 \
  --print-to-pdf="Catalogo Talleres Intezia 2026.pdf" \
  "file://$(pwd)/index.html"
```
Expected: PDF de 33 páginas generado sin errores.

- [ ] **Step 2: Verificar el PDF**

Abrir el PDF. Confirmar: 33 páginas, marca correcta, las 3 slides imagen intactas, fuentes Graphit embebidas. Los botones (`<a href="#">`) aparecen como hipervínculos — el destino real se actualizará cuando lleguen las URLs (no bloquea esta entrega).

- [ ] **Step 3: Checkpoint del usuario** — el usuario revisa el PDF final y aprueba.

- [ ] **Step 4: Commit**

```bash
git add "clientes/propuestas/catalogo/Catalogo Talleres 2026/Catalogo Talleres Intezia 2026.pdf"
git commit -m "feat(catalogo): regenerar PDF del catálogo rediseñado (33 páginas)"
```

---

## Task 12: Registrar el aprendizaje

**Files:**
- Modify: `aprendizajes.md`

- [ ] **Step 1: Registrar en `aprendizajes.md`**

Añadir una entrada fechada (2026-05-18): el catálogo de talleres adopta el lenguaje visual HUD; los botones de video y "aplica aquí" son `<a href>` por taller; quedan pendientes 20 URLs de video + 1 URL de herramienta. Referenciar el spec.

- [ ] **Step 2: Commit**

```bash
git add aprendizajes.md
git commit -m "docs: registrar rediseño HUD del catálogo de talleres"
```

---

## Self-Review — cobertura del spec

- §2 Alcance (7 apartados rediseñados): Tasks 2,3,4,5+6,7,8,9. ✔
- §2 Alcance (3 slides imagen intactas): no se tocan; Task 1 Step 4 conserva `.s-img-page`. ✔
- §3 Sistema HUD: Task 1 (base) + cada apartado. ✔
- §4 Apartados (7): Tasks 2-9. ✔
- §5 Estructura 33 slides + separadoras: Task 3 (inserción) + Task 10 (orden y contadores). ✔
- §6 Elementos interactivos (botones como `<a href>` con `data-*`, placeholder `#`): Tasks 5,6,9. ✔
- §7 Generación PDF (Chrome headless, links): Task 11. ✔
- §9 Pendientes (URLs): los `href="#"` + `data-*` dejan los botones listos para actualizar. ✔
- §10 Cumplimiento marca: logos reales (Tasks 2,9), tokens/fuentes conservados (Task 1). ✔

Pendiente conocido y aceptado por el spec: las 21 URLs reales (20 video + 1 herramienta) — fuera del alcance de este plan.
