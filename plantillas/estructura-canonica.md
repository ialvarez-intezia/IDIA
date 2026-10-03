# Estructura Canónica de Decks — Referencia Técnica

Resumen de la arquitectura HTML/CSS de los dos decks de referencia del sistema. Para verificar conformidad estructural sin leer archivos completos.

---

## 1. Cumbre Andina (Mono-fase)

**Archivo:** `clientes/propuestas/cumbre-andina/index.html` (13 slides)
**Tipo:** Taller/Capacitación mono-sesión (3 módulos de 2–4 h cada uno)
**División:** Educación · Eje: IA aplicada con Claude

### Secuencia de slides

| # | Clase | Eyebrow | Titulo corto | Bloques clave |
|---|---|---|---|---|
| 01 | `.s-cover` | (sin eyebrow) | Portada + proposición | `.logo-big`, `.body h1`, `.id-line` (código + cliente) |
| 02 | `.s-pain` | (sin eyebrow) | Punto de dolor / Diagnóstico | `.quote-mark`, `.body h2`, `.context <p>`, `.diag-title`, `<ol>` 5 items |
| 03 | `.s-goals` | `02 · Objetivos` | Objetivos estratégicos | `.columns` 2 bloques (`.general`, `.specifics`), `<ol>` 3 items específicos |
| 04 | `.s-program` | `03 · Programa` | 3 módulos · 8 horas | `.modules` 3× `.module` (`.roman`, `h3`, `.obj <p>`, `.topics <ul>` 7 items) |
| 05 | `.s-schedule` | `04 · Cronograma · Ruta` | Sesión 1 de 3 · Módulo I | `.ruta` (nodo, track, step), `.ses-head`, `.ses-body` 3× `.ses-block`, `.chips` 4 items, `.timebar` 4 `.seg`, `.ses-cols` 3 bloques |
| 06 | `.s-schedule` | `04 · Cronograma · Ruta` | Sesión 2 de 3 · Módulo II | idem (ruta nodo 2, `.ses-body` 3 bloques) |
| 07 | `.s-schedule` | `04 · Cronograma · Ruta` | Sesión 3 de 3 · Módulo III | idem (ruta nodo 3, `.ses-body` 2 bloques sin `.timebar`) |
| 08 | `.s-orange` | `05 · Metodología` | ABR · Modelo Intezia | `.pillars` 3× `.pillar` (`.num`, `h3`, `<p>`) |
| 09 | `.s-benefits` | `06 · Beneficios` | Perfil egreso + beneficio | `.grid` 4 `.block` (label/contenido), `.multi-box` Entregables/Acreditación, `.team` 2× `.person` (avatar, h4, role, p) |
| 10 | `.s-impact` | `07 · Impacto` | Evidencia — estudios reales | `.chart-panel` (barras 3 rows), `.gauge-panel` (gauge `--pct`, 2 chips), `.impact-hook` |
| 11 | `.s-price` | (sin eyebrow) | Propuesta Económica | `.block` duración, programa, cotización (3 `.cot-frame`), notas. `.multi-box` Programa/Notas |
| 12 | `.s-steps` | `08 · Próximos pasos` | Cómo arrancamos | `.step-cards` 3× fantasma, `.acro-area` 6× (3 pasos × título + body) |
| 13 | `.s-end` | (sin eyebrow) | Cierre · CTA + contacto | `.end-logo`, `.end-message`, `.cta-wrap`, `.end-contact` 2 líneas |

### Estructura de cajas por slide clave

**Slide 04 (Programa):** `.modules` > 3× `.module` > (`.roman`, `h3`, `.obj`, `.topics li`) — sin modo compacto en _base; los 3 módulos se renderizan a tamaño regular. Chips de temas sin truncar (white-space: normal).

**Slide 05–07 (Cronogramas):** `.ruta` (visual de progreso), `.ses-head`, `.ses-body` con estructura flexible:
- `.ses-block` × N (label + contenido: `.chips`, `.timebar`, `.ses-cols`)
- `.timebar` = `.seg` × N con `flex: valor` (alineación por proporción)
- `.ses-cols` = 3× `.ses-block` (side-by-side)

**Slide 09 (Beneficios):** `.multi-box` (`data-field="Entregables"` y `data-field="Acreditacion"`) — cajas vacías en HTML, contenido pre-llena via AcroForm. `.team .members` = 2× `.person`.

**Slide 10 (Impacto):** `.chart-panel` (barras 3 rows con `--w:pct` inline), `.gauge-panel` (`.gauge` con `--pct`, 2 `.chip`), `.impact-hook`, `.panel-source` con fuente verbatim.

**Slide 11 (Precio):** `.block` × 4 (duración, programa, cotización, notas). `.cot-frame` × 3 (base, descuento, total) — posición absolute para sincronizar con PDF. `.multi-box` Programa/Notas.

**Slide 12 (Pasos):** `.step-cards` 3× (visual fantasma), `.acro-area` × 6 (`data-field` para AcroForm: Paso01Titulo, Paso01Body, Paso02Titulo, Paso02Body, Paso03Titulo, Paso03Body).

### Elementos transversales

- **Footer:** `.foot` (logo NEGRO 24×24, `.meta` "Cliente · Propuesta") — presente en todas slides (salvo portada/cierre)
- **Counter:** `.counter` "XX / 13" — presente todas slides
- **Logo portada:** `.logo-big` BLANCO sobre fondo oscuro (`.s-cover`)
- **Logo cierre:** `.end-logo` BLANCO sobre fondo oscuro (`.s-end`)
- **CSS:** enlaza `href="../_base/styles.css"` — define paleta (#F4BA1A, #E58423, #000, #FFF), tipografía, grid general
- **Campos AcroForm:** 8 campos editables pre-llenables (todos EXCEPTO precio):
  - Entregables (multiline, .multi-box)
  - Acreditacion (multiline, .multi-box)
  - Paso01Titulo, Paso01Body, Paso02Titulo, Paso02Body, Paso03Titulo, Paso03Body (6 campos)
  - **Campos precio:** 5 campos AcroForm (Programa, Base, Descuento, Total, Notas) — dejados vacíos; ventas rellena en Adobe Reader

---

## 2. Pilotes Perforados (Multi-fase)

**Archivo:** `clientes/propuestas/pilotes-perforados/index.html` (14 slides)
**Tipo:** Diagnóstico + Plan (Fase 1 cotizada, Fase 2 abierta)
**División:** Educación · Eje: Digitalización operativa con IA

### Secuencia de slides

| # | Clase | Eyebrow | Titulo corto | Bloques clave |
|---|---|---|---|---|
| 01 | `.s-cover` | (sin eyebrow) | Portada + propuesta | `.logo-big`, `.body h1`, `.id-line` |
| 02 | `.s-pain` | (sin eyebrow) | Dolor / Diagnóstico | `.quote-mark`, `.body h2`, `.context`, `<ol>` 5 items |
| 03 | `.s-goals` | `02 · Objetivos` | Objetivos operativos | `.columns` 2 bloques, `<ol>` 3 items |
| 04 | `.s-program` | `03 · El proyecto` | 2 fases · una decisión | `.modules` 2× `.module` (Fase 1, Fase 2; `.topics` 5 items cada una) |
| 05 | `.s-schedule` | `04 · Diagnóstico · Ruta` | Sesión 1 · Procura + CxP | `.ruta` nodo 1, `.ses-head`, `.ses-body` (sin `.timebar`; 3 bloques) |
| 06 | `.s-schedule` | `04 · Diagnóstico · Ruta` | Sesión 2 · Finanzas + Licitaciones | `.ruta` nodo 2, `.ses-body` idem |
| 07 | `.s-roadmap` | `04 · Roadmap · Plan` | Mapa de dos fases | `.rmx-field` con `.rmx-journey` (`.rmx-origin`, `.rmx-fork`, `.rmx-routes` 2 branches, `.rmx-merge`, `.rmx-result`). `.rmx-ethics` bloque metodológico |
| 08 | `.s-orange` | `05 · Metodología` | ABR · Diagnóstico antes | `.pillars` 3× `.pillar` |
| 09 | `.s-benefits` | `06 · Beneficios` | Perfil egreso + beneficio | `.grid` 4 `.block`, `.multi-box` × 2, `.team` × 2 |
| 10 | `.s-heatmap` | `07 · Mapa de Calor` | Dónde automatizar primero | `.hm-wrap` > `table.hm` 6 cols, 11 `.proc-row` (4 areas + 7 procesos), `.hm-legend` 5 items |
| 11 | `.s-impact` | `08 · Impacto` | Evidencia — estudios reales | `.chart-panel` (barras 3 rows), `.gauge-panel` (gauge, 2 chips), `.impact-hook` |
| 12 | `.s-price` | (sin eyebrow) | Propuesta Económica · Fase 1 | idem slide 11 de cumbre |
| 13 | `.s-steps` | `09 · Próximos pasos` | Cómo arrancamos | `.step-cards` 3×, `.acro-area` × 6 |
| 14 | `.s-end` | (sin eyebrow) | Cierre · CTA | idem slide 13 de cumbre |

### Estructura de cajas por slide clave

**Slide 04 (Proyecto):** `.modules` 2× (Fase 1, Fase 2). Cada `.module` sin modo compacto — se renderizan a tamaño regular con 5 items en `.topics`.

**Slide 07 (Roadmap):** Estructura exclusiva del multi-fase. `.rmx-journey` = diagrama Damasco (origen → bifurcación → rutas → convergencia → resultado):
- `.rmx-origin` (nodo F1, badge, meta de diagnóstico)
- `.rmx-fork` (visual de bifurcación con 2 `.rmx-branch`)
- `.rmx-routes` 2× `.rmx-route` (S1 y S2: nodo, card con tag/name/facets)
- `.rmx-merge` (convergencia visual)
- `.rmx-result` (nodo ★, card insignia del Mapa de Calor)
- `.rmx-ethics` (metodología ABR)

**Slide 10 (Heatmap):** `.hm-wrap` > `table.hm`:
- 6 cols: Proceso, Puntuación, Herramienta, Plazo, Frecuencia, Prioridad
- 1 `.area-row` (encabezado de área, colspan=6) × 4 áreas
- `.proc-row` × 7 (una por tarea de automatización)
- `.hm-scores` con `.score-pills` (3 pills: Impacto, Esfuerzo, Riesgo — colores: p-alto, p-ef-bajo, p-ri-med)
- `.hm-tool` con `.tool-tag` × 1–2 (herramientas recomendadas)
- `.hm-frec` con `.frec-main` y `.frec-sub` (frecuencia y horas)
- `.hm-pri` con `.hm-badge` (Alta / Media)
- `.hm-legend` 5 items (escala de puntuación + prioridad)

**Slide 11 (Impacto):** idem cumbre (barras 3 rows, gauge, chips, hook).

**Slides 12–13 (Precio, Pasos):** idénticas a cumbre (estructuralmente).

### Elementos transversales

- **Footer:** `.foot` (logo NEGRO, `.meta`) — todas slides salvo portada/cierre
- **Counter:** `.counter` "XX / 14"
- **CSS:** enlaza `href="styles.css"` local (no `../_base/`) — incluye los estilos propios del heatmap y el roadmap multi-fase
- **Campos AcroForm:** 8 campos (Entregables, Acreditacion, Paso01–03 Titulo/Body) idénticos a cumbre

---

## 3. Diferencias Clave: Mono-fase vs Multi-fase

| Aspecto | Cumbre (Mono) | Pilotes (Multi) |
|---|---|---|
| **Slides totales** | 13 | 14 |
| **Estructura slide 04** | `.s-program` 3 módulos taller | `.s-program` 2 fases proyecto |
| **Cronogramas** | 3× `.s-schedule` (sesiones 1–3) | 2× `.s-schedule` (sesiones 1–2 de diagnóstico) |
| **Slide 07** | `.s-orange` ABR | `.s-roadmap` diagrama Damasco (NUEVA slide) |
| **Slide 08** | `.s-orange` ABR | `.s-orange` ABR (adelantada) |
| **Heatmap** | NO | Slide 10 `.s-heatmap` (tabla 7 procesos × 6 cols) |
| **Impacto** | Slide 10 | Slide 11 |
| **Precio** | Slide 11 | Slide 12 |
| **Pasos** | Slide 12 | Slide 13 |
| **Cierre** | Slide 13 | Slide 14 |
| **CSS** | Enlaza `../_base/styles.css` | Enlaza `styles.css` local |
| **Metodología/Narrativa** | Taller con tutoría activa + transferencia + curaduría | Diagnóstico antes de invertir + trabajo en procesos reales + decisión informada |

---

## 4. Marcadores AcroForm (PDF Editable)

### Cumbre & Pilotes — Campos identicos (8 obligatorios + 5 precio)

**Slide de Beneficios (09/cumbre, 09/pilotes):**
- `Entregables` (multiline) — `.multi-box.entregables-box`
- `Acreditacion` (multiline) — `.multi-box.acreditaciones-box`

**Slide de Precio (11/cumbre, 12/pilotes):**
- `Programa` (multiline) — `.multi-box.programa-box`
- Precio: `cot-base`, `cot-descuento`, `cot-total` (5 campos, vacíos intencionales para ventas)
- `Notas` (multiline) — `.multi-box.notas-box`

**Slide de Pasos (12/cumbre, 13/pilotes):**
- `Paso01Titulo`, `Paso01Body`
- `Paso02Titulo`, `Paso02Body`
- `Paso03Titulo`, `Paso03Body`

**Total:** 8 campos pre-llenables + 5 campos de precio = 13 campos AcroForm.

---

## 5. Verificación de Conformidad

Para cualquier nuevo deck clonable:

1. **Secuencia de slides:** Verificar eyebrows y contadores en orden (01/N, 02/N, etc.)
2. **Clase por slide:** Confirmar `.s-cover`, `.s-pain`, `.s-goals`, `.s-program`, `.s-schedule` (×N), `.s-orange`, `.s-benefits`, `.s-impact`, `.s-price`, `.s-steps`, `.s-end`
3. **Bloques estructurales:**
   - `.modules` con `.roman` + `.topics <ul>` en `.s-program`
   - `.ruta` + `.ses-head` + `.ses-body` en `.s-schedule`
   - `.chart-panel` + `.gauge-panel` en `.s-impact`
   - `.step-cards` + `.acro-area` × 6 en `.s-steps`
4. **Campos AcroForm:** 8 campos obligatorios + 5 precio = 13 total (salvo si cliente sin slide precio)
5. **CSS:** Mono-fase enlaza `../_base/styles.css`; multi-fase puede enlazar local `styles.css` con overrides
6. **Overflow:** Chips ≤ 28 caracteres; sin `text-overflow: ellipsis`; revisar visual en PDF

---

## 6. Notas de Implementación

- **_base:** compartido entre clones mono-fase (cumbre-andina como origen). Define paleta, tipografía, resets, grid general.
- **Overrides:** Si hay customización visual (heatmap compacto, módulos extra), crear `overrides.css` local en la carpeta del cliente y enlazar DESPUÉS de `../_base/styles.css`.
- **Multi-fase roadmap:** Usar siempre `.rmx-*` clases (no reinventar diagrama). Slide 07, eyebrow `04 · Roadmap`, estructura Damasco: origen → bifurcación → rutas → convergencia → resultado.
- **Heatmap (multi-fase):** 4 áreas (filas encabezado `area-row`) + 7 procesos (`.proc-row`). Verificar con `verificar-overflow.js` — el heatmap es propenso a desborde (+44px si no está compacto).
