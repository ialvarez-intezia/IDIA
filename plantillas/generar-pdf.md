# Generar PDF de propuesta — Reglas 4.4, 4.5 y 4.6

## Regla 4.5 — Formato horizontal obligatorio

Toda propuesta usa A4 landscape (1123×794 px @ 96 dpi → 842×595 pt PDF). El CSS declara `@page { size: A4 landscape }` y usa `--slide-w: 1123px; --slide-h: 794px`. Si sale en vertical, detener y regenerar.

**Comando único:**

```bash
./scripts/generar-pdf.sh <empresa-slug>
```

Chrome headless genera el PDF → Python añade los 13 AcroForms → `clientes/propuestas/<slug>/<CÓDIGO> <Título>.pdf`.

> El nombre del PDF se deriva de la portada (código + título del `<h1>`), p. ej.
> `TA-001 Inteligencia Artificial aplicada con Claude.pdf`. `generar-pdf.sh` lo imprime al
> final junto al comando `customize` con ese path. Los ejemplos de abajo usan `propuesta.pdf`
> solo como marcador: pasa el path real que imprime el script.

---

## Regla 4.4 — Campos AcroForm (3 slides, 13 campos)

Gestiona `scripts/agregar-campo-precio.py` con estructura `PAGE_GROUPS` × marker de página. Filosofía: 1 caja multiline por bloque — ventas escribe libremente.

| Slide | Marker | Campos | Tipo | Pre-fill |
|---|---|---|---|---|
| 8 — Beneficios | `Lo que se llevan` | `Entregables`, `Acreditacion` | multiline libre | sí (Entregables: ver nota) |
| 10 — Propuesta Económica | `Propuesta Económica` | `PrecioBase`, `Descuento` | single-line | vacíos |
| 10 — Propuesta Económica | `Propuesta Económica` | `PrecioTotal` | editable + auto-calc JS (`base − |descuento|`) | vacío |
| 10 — Propuesta Económica | `Propuesta Económica` | `Programa`, `Notas` | multiline libre | sí |
| 11 — Próximos pasos | `Cómo arrancamos` | `Paso{01,02,03}Titulo` | single-line | sí |
| 11 — Próximos pasos | `Cómo arrancamos` | `Paso{01,02,03}Body` | multiline | sí |

> **Números de slide nominales**: el desglose instructivo aporta 1 slide por sesión, así que «Slide 8/10/11» se desplazan según el nº de sesiones. La detección es por **marcador de texto**, nunca por índice de página — el desplazamiento no afecta a los AcroForms.
>
> **Slide de Impacto** (`.s-impact`, eyebrow `07 · Impacto`, entre Beneficios y Propuesta Económica): es **contenido estático** — gráficas en CSS puro, **sin campos AcroForm**. Su inserción no afecta a la detección por marcador ni a los 13 campos. Su copy NO debe contener las frases marcador (`Lo que se llevan`, `Propuesta Económica`, `Cómo arrancamos`) para no provocar detección duplicada.

**Estilo visual:**
- Slide 8 (Beneficios): sin cuadritos amarillos. Texto plano. `<li>` de Perfil de Egreso flush left.
- Slide 10 (Propuesta Económica): un cuadrito de acento por bloque (■ amarillo en Programa, ■ naranja en Notas) como `::before` del `.block-eyebrow`.

**Compatibilidad:**
- ✅ Adobe Acrobat/Reader: campos editables + cálculo automático del total.
- ⚠️ Preview macOS / Chrome: campos editables sí; JS de cálculo NO corre. Ventas escribe el total a mano.

**Detalles de implementación:**
- Conversión CSS → pt: factor 0.75. `y_pt = 595 − (y_top_css × 0.75 + h_css × 0.75)`.
- `/Ff` flags: bit 1 = readonly, bit 13 (4096) = multiline.
- `/MK /BG` con `FloatObject` (no `NumberObject` — trunca floats a int).
- Saltos de línea en defaults: `\r` (estándar AcroForm).
- Detección de página: case-insensitive del marker.
- Fuentes: la AcroForm lleva un `/DR` con `/Helv` (Helvetica) y `/HeBO` (Helvetica-Bold). Los campos `Entregables` y `Acreditacion` usan `/HeBO`; el resto, `/Helv`.
- **Negrita de `Entregables` / `Acreditacion`**: no basta con el `/DA` + `/DR` — Preview y PDF.js (visor de VS Code) no regeneran la apariencia y pintan un fallback regular. Por eso `acroform_appearance.py` **hornea el `/AP`** (Form XObject) de esos dos campos: dibuja el texto en Helvetica-Bold, partido por palabras al ancho del campo. Así la negrita se ve idéntica en todo lector. Cada script que toca su `/V` (`agregar-campo-precio.py`, `customize-acroforms.py`, `customize-<slug>.py`) llama a `rebake_bold_fields(writer)` antes de escribir. El campo sigue editable.
- **`Programa` y `Notas` también necesitan `/AP` horneado (bug real, corregido 2026-09-23)**:
  mismo problema que Entregables/Acreditacion, pero en regular — `REGULAR_BAKED_FIELDS` de
  `acroform_appearance.py` ahora incluye `Programa` y `Notas` además de `Paso01-03
  Titulo/Body`. Antes del fix, estos 2 campos tenían `/V` correcto pero sin `/AP`: con
  `/NeedAppearances=False` (regla de abajo), Adobe Reader y Preview los mostraban **en
  blanco** pese al valor correcto — el extractor de PDF de Claude no lo detecta porque
  regenera apariencias solo (punto ciego del QA visual normal). Verificar con pypdf directo
  (`campo.get('/AP')`) si hay dudas, no solo abriendo el PDF con las herramientas de Claude.
  Campos de precio (`PrecioBase`/`Descuento`/`PrecioTotal`, variantes Fase/Ciclo) quedan
  fuera de este set a propósito: nacen vacíos, no tienen texto pre-llenado que ocultar.

**Pre-llenado del campo `Entregables` (por propuesta):**

**Flujo estándar de pre-llenado — `acroforms.json` (propuestas nuevas):**

La propuesta declara TODOS sus valores pre-llenados en
`clientes/propuestas/<slug>/acroforms.json` ({campo: string | lista}; las listas se
unen con `\r`) y se aplica con el genérico, que localiza el PDF único de la carpeta:

```bash
python3 scripts/customize-acroforms.py <slug>
# multi-deck (varios PDFs en la carpeta): PDF y JSON explícitos por deck
python3 scripts/customize-acroforms.py "clientes/propuestas/<slug>/<PDF>" \
  clientes/propuestas/<slug>/acroforms-<variante>.json
```

El genérico aplica el comportamiento estándar completo: `/V`+`/DV`, títulos de pasos
a 14 pt, re-horneado de negrita y `/NeedAppearances`. Los campos **siguen editables**.
**Ya no se clona un `customize-<slug>.py` por propuesta**: un script propio solo se
justifica para casos especiales (resize de `/Rect`, lógica condicional) — los
existentes se conservan y siguen funcionando.

**Campo `Entregables`:**

`agregar-campo-precio.py` carga `ENTREGABLES_DEFAULT` — 3 entregables institucionales
fijos. En el `acroforms.json`, combínalos con 2–4 entregables destacados deducidos del
**desglose instructivo** de `programa.md` (analiza temas, estrategias de aprendizaje y
recursos de cada módulo).

- Orden: destacados de la propuesta primero, institucionales después.
- Máx. ~2–4 destacados, líneas cortas de un renglón (la caja admite ~9 líneas a 10 pt).

**`Programa` y `Notas` no cambian**: siguen vacíos para ventas — ni cifras ni condiciones de
pago pre-llenadas. `Programa` es nombre del programa + cantidad de participantes que cubre
la cotización; `Notas` es libre (ventas lo redacta en Adobe Reader según la negociación).

**Vigencia de la cotización y bloque de términos y condiciones — estándar único, 30 días
(caso base 2026-08-13 Servicom CAP-102, corrigiendo un intento previo equivocado de
pre-llenar `Notas` con anticipo/cancelación — eso NO va ahí):**

Toda slide de Propuesta Económica (`.s-price`) lleva, debajo del bloque de Cotización:

```html
<p class="cot-validity">Cotización válida por 30 días.</p>
<div class="cot-terms-box">
  <span class="cot-terms-label">Importante</span>
  <p class="cot-terms-text">Este servicio se presta bajo nuestros <a href="https://drive.google.com/file/d/1PA-ZSt4KnyY5dpxXzgkIk6-yfGlV2eF8/view?usp=drive_link" target="_blank" rel="noopener">términos y condiciones</a>. Al avanzar con esta propuesta, ambas partes los aceptan.</p>
</div>
```

- **`.cot-validity` siempre dice 30 días** — igual que `empresa/politicas-comerciales.md`
  ("Vigencia de la cotización: 30 días desde la fecha de emisión."). El clon canónico
  mono-fase (`cumbre-andina/`) tenía hardcodeado **7 días** por un error de plantilla previo
  al enlace de términos — ya corregido en el canónico y en `_base/styles.css`
  (`.cot-terms-box`/`.cot-terms-label`/`.cot-terms-text`, agregadas 2026-08-13). Los clones
  multi-fase (`aerocentro/`, `pago-tronic/`, `pilotes-perforados/`) ya tenían el patrón
  completo (30 días + link) desde antes — ese es el estándar a seguir, no se inventa nada
  nuevo. Si un deck clonado de una propuesta antigua (no del canónico) todavía dice 7 días o
  no tiene el bloque de términos, agrégalo al tocar esa slide.
- **El link es institucional y fijo** (mismo documento en los 8+ decks que ya lo usan) — no
  varía por cliente, no se pregunta.
- **Nunca en `Notas` ni como texto libre**: anticipo, saldo, %, factura o cancelación son
  contenido comercial que ventas negocia caso por caso — no se pre-llenan en el deck (§4.15
  extiende el mismo criterio de «logística, no transacción» a toda slide de cara al
  cliente, no solo a «Cómo arrancamos»).

**Descuento con urgencia, ROI y garantía — bloques estáticos nuevos junto a la Cotización
(2026-09-23, ver `propuesta-comercial.md` → *Propuesta Económica — descuento urgente, ROI y
garantía* para el copy completo):**

- **Ninguno de los 3 es un campo AcroForm nuevo.** El conteo de 13 campos no cambia. Son
  HTML/CSS estático que rodea a los campos existentes:
  - Prefijo `−$` fijo antes de `.discount-frame` (no toca el campo `Descuento`, que sigue
    vacío y editable) + etiqueta `.cot-urgent-note` con texto fijo "Descuento válido por 15
    días" (o "Beneficio válido por 15 días" en la variante Innovación, junto a cada
    `Descuento{N}m`) — `font-size: 13px`, corregido 2026-09-23 (antes 9px + "por aprobación
    en", texto más largo y letra chica para su función de urgencia).
  - `.cot-roi-box`: párrafo redactado por Claude caso por caso a partir de `brief.md` /
    Ficha Comercial. Se omite el bloque entero (no se deja vacío ni con placeholder) cuando
    no hay dato de qué resultado espera el cliente.
  - `.cot-garantia-badge`: solo cuando `servicio: habilidades`. Ausente en el resto de
    servicios hasta que tengan su propio marco de seguimiento.
- **Compatibilidad con el cálculo existente**: `make_calc_js` (`agregar-campo-precio.py`)
  ya aplica `String(d).replace(/[^0-9.\-]/g,"")` seguido de `Math.abs()` sobre el valor de
  `Descuento` — que ventas escriba "400" o "-400" en el campo da el mismo resultado. El
  prefijo visual `−$` es puramente estático (fuera del campo); **no requiere ningún cambio
  en `agregar-campo-precio.py`**.
- Aplica igual a las 3 variantes de cotización (por horas / "Inversión por fases" /
  "Inversión por Permanencia") — el prefijo y la etiqueta de urgencia se repiten junto a
  cada campo `Descuento`/`Descuento{N}m` que exista en la slide.

**Pre-llenado del campo `Acreditacion` (por propuesta):**

`agregar-campo-precio.py` carga `ACREDITACIONES_DEFAULT` — 3 líneas fijas, idénticas
en toda propuesta con código (Taller, Capacitación, Curso, Diplomado):

```
Programa registrado en INTEZIA Education como [CÓDIGO].
Cumple con el modelo pedagógico oficial (ABR).
Material curado y revisado por el equipo académico.
```

En el `acroforms.json`, sustituye **solo** el token `[CÓDIGO]` por el código real del
programa (lo aporta el usuario / la línea «Tipo de documento» del `brief.md`):

```json
"Acreditacion": ["Programa registrado en INTEZIA Education como TA-001.",
                 "Cumple con el modelo pedagógico oficial (ABR).",
                 "Material curado y revisado por el equipo académico."]
```

- Las líneas 2 y 3 (ABR · material curado) son **fijas** — nunca cambian.
- El campo **sigue editable** tras la sustitución.

**Pre-llenado de los campos `Paso*` (por propuesta):**

`agregar-campo-precio.py` carga `PASOS_DEFAULTS` — placeholders entre corchetes.
**Claude redacta los 3 pasos «Cómo arrancamos» listos-para-entregar** en el
`acroforms.json` (`Paso01Titulo`, `Paso01Body`, … `Paso03Body`); los campos **siguen
editables** — el equipo de ventas solo necesita una referencia ya redactada, no un
placeholder. El genérico pone los títulos a 14 pt automáticamente para que quepan.

- **Pauta estándar de los 3 pasos (§4.15 — solo logística, nunca acuerdos económicos)**:
  1) confirmar fechas y zona horaria · 2) coordinar acceso, participantes y agenda de
  sesiones («Acceso y logística») · 3) reunión de arranque (~30 min) para alinear los
  casos reales. Adaptar al tipo de programa y al cliente del brief. Prohibido mencionar
  acuerdo, contrato, factura, anticipo o pago en cualquiera de los pasos.
- Títulos cortos (caben en una línea); bodies de 1–2 frases.
- **Tamaño de letra estándar** (en `agregar-campo-precio.py`, `/DA` del campo → aplica al
  texto pre-llenado y al que escribe ventas): título **15 pt**, body **12 pt** (corregido
  2026-09-23 — antes 18/15 pt, cuando el `.step-card` era el doble de alto). Preview HTML
  sincronizada en `styles.css` (`.s-steps .acro-title/.acro-body` → 20 px / 16 px).
- **Cards compactas + calendario de inicio (2026-09-23)**: `.step-card` bajó a
  `min-height: 200px` (antes 400px) para dejar espacio a `.steps-calendar` — lista de 2
  columnas con **todas** las sesiones de la propuesta (incluido kick-off), cuando se conoce
  la fecha real de arranque. Rects de `Paso01-03` recalculados en cascada (ver comentario en
  `_base/styles.css` → *.acro-area*). Detalle: `propuesta-comercial.md` → *Próximos pasos —
  calendario de inicio*.
- El demo canónico se reproduce con `scripts/customize-cumbre-andina.py` (dict hardcodeado).

**Variante opcional — "Inversión por fases" (cotización por fase + total, 1 sola slide):**

Para propuestas multi-fase donde el cliente pide **cotizar cada fase por separado y un
total** (en vez del default de aerocentro "solo Fase 1, resto progresivo" — ver
`propuesta-comercial.md` → *Roadmap*), la slide `.s-price` cambia su H2 a **"Inversión por
fases"** (texto literal — es el marker que activa la variante) y usa el grupo
`FASE_PRICE_FIELDS` de `agregar-campo-precio.py` en vez de `PRECIO_FIELDS`:

- `PrecioFase1`, `PrecioFase2`, `PrecioFase3` (… `PrecioFaseN`): un campo editable por fase,
  alineado a la derecha de la fila de cada fase (columna izquierda de la slide).
- `PrecioBase` reutilizado como **subtotal auto-calculado** = suma de todas las
  `PrecioFaseN` (JS generado por `make_fase_subtotal_js(N)`).
- `Descuento` y `PrecioTotal` sin cambios de comportamiento (`PrecioTotal` = `PrecioBase` −
  `Descuento`), solo reposicionados en la columna derecha.
- `Notas` sin cambios. **Sin `Programa`**: las filas de fase ya comunican el alcance; un
  bloque `Programa` aparte sería redundante.
- El marker "Inversión por fases" **no colisiona** con "Propuesta Económica" — cada PDF se
  procesa por separado, así que esto no afecta a ningún otro deck del sistema.
- Fases sin alcance aún definido (ej. una Fase 2/3 que depende de un diagnóstico) llevan la
  **misma** caja vacía que las demás, sin distinción visual — ventas decide qué escribir.
- Referencia: `clientes/propuestas/ioed/` (CAP-098, 2026-08-11) — inspirado en el layout de
  cotización de la propuesta de Cinex (CAP-072, deck externo, no en este repo).

**Variante "Inversión por Permanencia" (cuota mensual × duración de ciclo, servicio
Innovación — `empresa/tipos-de-documento.md §0`):**

Para el servicio Innovación (acompañamiento continuo con cadencia mensual, sin "N módulos ·
X horas" ni fases con fin), la slide `.s-price` cambia su H2 a **"Inversión por
Permanencia"** (texto literal, es el marker) y usa el grupo `CICLO_PRICE_FIELDS` de
`agregar-campo-precio.py`:

- 3 columnas independientes de duración de ciclo (3 / 6 / 12 meses), cada una con
  `Cuota{N}m` (cuota mensual, editable) + `Descuento{N}m` (beneficio por permanencia,
  editable) — 6 campos en total, sin auto-cálculo entre columnas: cada plan es
  independiente, no hay un total único que sumar.
- `Notas` sin cambios (misma posición estándar). **Sin `Programa`**: las 3 columnas ya
  comunican el alcance (igual criterio que "Inversión por fases").
- Todo el layout de esta variante usa **posicionamiento absoluto explícito** (no flujo de
  documento) para que la caja CSS visible coincida pixel a pixel con el `/Rect` del AcroForm
  — ver el bloque de comentarios en `overrides.css` del deck de origen con la conversión
  px→pt de cada fila/columna.
- La columna de mayor duración (12 meses) se resalta visualmente como "mayor beneficio"
  (tarjeta oscura con badge) para reforzar el incentivo comercial de permanencia — no fija
  un porcentaje de descuento en el HTML, ambos campos (cuota y beneficio) quedan vacíos para
  que ventas los complete igual que el resto de campos de precio.
- Referencia: `clientes/propuestas/zoom-innovacion/` (INN-001, 2026-08-30) — primer piloto
  del servicio Innovación, ver `CLAUDE.md §4.1a`.

---

## Regla 4.6 — Plantilla canónica congelada

**Referencia**: `clientes/propuestas/cumbre-andina/`. Para propuesta nueva: clonar esa carpeta → editar solo contenido estático.

**Lo que nunca cambia (bloqueante):**
- Formato A4 landscape, paleta, tipografía Graphit.
- Orden de los bloques del deck (Portada → … → Cierre). El **desglose instructivo aporta 1 slide por sesión**, así que el total de slides es **variable**; el `.counter` global `NN / TT` se recalcula a mano al construir.
- Posiciones absolutas, clases `.multi-box`, `.cot-frame`, `.s-*`.
- 13 campos AcroForm: tipos, nombres, posiciones, defaults.
- Slide de Impacto (`.s-impact`): contenido estático, gráficas en CSS puro, sin AcroForms.
- `Entregables` y `Acreditacion` en negrita — apariencia `/AP` horneada (`acroform_appearance.py`).
- Sin cuadritos en slide 7. Un cuadrito de acento por bloque en slide 8. Sin texto fantasma detrás de AcroForms.
- CTA de cierre (`.s-end .cta`) = botón-hipervínculo `<a class="cta" href="https://calendly.com/intezia/30min?month=YYYY-MM" target="_blank">` — nunca `<span>`. Chrome headless lo conserva como enlace clicable en el PDF. **Siempre añadir `?month=YYYY-MM` con el mes de entrega** (ej. `?month=2026-05`); sin el parámetro Calendly puede mostrar un mes sin disponibilidad.

**Lo que sí cambia:** título, eyebrow, audiencia, módulos, facilitador, asesora, slug.

**Bloqueante:** cualquier cambio estructural (paleta, tipografía, cantidad/posición de AcroForms) exige confirmación explícita y actualización en cascada: `cumbre-andina/`, `plantillas/propuesta-comercial.md`, `scripts/agregar-campo-precio.py`, `scripts/acroform_appearance.py`, `CLAUDE.md`, `aprendizajes.md` y memoria persistente.
