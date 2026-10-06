# Plantilla: Propuesta comercial (slides HTML/PDF)

> **FORMATO HORIZONTAL — PERMANENTE**: A4 landscape (1123×794 px @ 96 dpi → 842×595 pt PDF). No revertir a vertical sin instrucción explícita.
> **REFERENCIA CANÓNICA**: `clientes/propuestas/cumbre-andina/` (taller mono-fase) · `clientes/propuestas/pilotes-perforados/` (multi-fase). Para propuesta nueva → clonar la más parecida y editar solo el contenido.
> **Detalle por slide**: cargar `plantillas/propuesta-comercial-ref.md` solo para dudas puntuales o construcción desde cero sin clon disponible.
> **Habilidades (desde 2026-10-05)**: este documento describe el deck canónico de ~13 slides. El servicio de Habilidades se entrega por defecto con la **plantilla compacta** (`plantillas/habilidades-compacto.md`, `CLAUDE.md §4.21`); este deck solo se usa en los demás servicios y en los casos de la guardia de §4.21 punto 5. Las *Reglas de copy* de abajo (guion largo, siglas, anglicismos, eyebrow con servicio) siguen aplicando a ambos.

---

## Pre-requisitos antes de generar (bloqueantes)

1. **División confirmada**: `brief.md` con `division: fundacion | educacion`. Sin división → detente y pregunta.
2. **Tipo de documento**: charla / taller / capacitación / curso / diplomado.
3. **Marca**: paleta `#000000` / `#F4BA1A` / `#E58423` / `#FFFFFF` · logo `logos/{division}/{BLANCO|NEGRO}.png` · Graphit Bold/Regular (fallback Inter).

---

## Estructura del deck

| # | Slide | Clase CSS | Aplica a |
|---|---|---|---|
| 1 | Portada | `.s-cover` | Todos |
| 2 | Punto de dolor + Diagnóstico | `.s-pain` | Todos |
| 3 | Objetivos estratégicos | `.s-goals` | Todos (Charla: objetivo único) |
| 4 | Programa | `.s-program` | Todos |
| 5…N | Desglose instructivo — **1 slide por sesión** | `.s-schedule` | Todos (Charla: tabla de contenido) |
| — | Sistema de evaluación | `.s-eval` | **Solo Curso / Diplomado** |
| ~~—~~ | ~~Metodología ABR~~ | ~~`.s-orange`~~ | **Retirada del deck visual — §4.10a CLAUDE.md (2026-08-26).** Ventas ya la cubre en el Levantamiento; el enfoque ABR sigue documentado en `programa.md` interno. |
| — | Beneficios | `.s-benefits` | Todos — **sin bloque de Equipo facilitador** (§4.10a). Contenido variable por servicio, ver *Beneficios por servicio* abajo |
| — | Impacto / estudios | `.s-impact` | Todos |
| — | Propuesta Económica | `.s-price` | Todos (**omitir** en Fundación) — variantes por servicio, ver *Propuesta Económica por servicio* abajo |
| — | Próximos pasos | `.s-steps` | Todos |
| — | Cierre | `.s-end` | Todos |

**El deck no tiene número fijo de slides.** El desglose aporta 1 slide por sesión; el contador `NN / TT` se recalcula al construir.

---

## Reglas de layout

- Slides con varios elementos (Programa, ABR, Beneficios, Próximos pasos) usan **grids horizontales**.
- Slide Objetivos: Objetivo General arriba a ancho completo; Específicos debajo apilados.
- Slide Propuesta Económica: **2 columnas** (izquierda: Duración + Programa + Notas · derecha: Cotización).
- Cards (módulos, pilares, pasos): número decorativo en la parte **superior**, no al lado.
- **Cronograma (`.s-schedule`) — los 5 elementos, siempre** (bloqueante, reforzado 2026-09-23
  tras un caso real donde se omitió): Temas (chips), **Tiempo** (`.timebar`, segmentos
  `style="flex:<minutos>"`), y Estrategias de enseñanza / Estrategias de aprendizaje /
  Recursos (`.ses-cols`, 3 columnas). **Nunca omitir el `.timebar`** — sin él, `.ses-body`
  deja un vacío grande y feo entre Temas y las columnas (el `justify-content` de
  `.ses-body` reparte el aire sobrante entre los 3 bloques; con solo 2, el vacío se
  concentra en uno). Detalle completo: `plantillas/propuesta-comercial-ref.md` → sección de
  Cronograma. Caso base del olvido: `amv-tecnologia-cerebro-digital/` (CAI-023, 2026-09-23).

---

## Beneficios — formato v3 (estándar vigente, 2026-08-28)

> Ver `empresa/tipos-de-documento.md §0` para el eje de servicio. **Reemplaza por completo**
> el formato viejo (Perfil de egreso / Beneficio del programa / Entregables / Acreditación)
> — ya no se usa en ninguna propuesta nueva, de ningún servicio, incluida Habilidades.
> v3 reemplaza a v2 (2026-08-27, vida corta: un día) porque v2 "solo cambiaba el color" y no
> se veía lo bastante impactante. Caso base v3: Simple TV DET-002 (2026-08-28). **Nota de
> exactitud**: v3 (a diferencia de v2, que sí se propagó el mismo día) NO se retroaplicó de
> inmediato a Cavedatos CAI-001, Go Pharma CAP-030 ni Amcor DET-001 — esos 3 decks quedaron en
> v2 y siguen pendientes de ese retrofit (confirmar con el usuario antes de tocarlos, ya
> preguntado una vez — respuesta: "más tarde, no ahora", 2026-08-28).

**Los 4 bloques, siempre en este orden:**

| # | Bloque | Contenido |
|---|---|---|
| 1 | **Resultados** | 3 líneas cortas y concretas de lo que el cliente logra — el "qué", no el "cómo". Lista `<ul>`, primera línea con 1-2 palabras clave en `<strong>`. |
| 2 | **Por qué [Servicio]** | 1 párrafo (`<p>`) que responde por qué este servicio es el correcto — ej. "Por qué Habilidades", "Por qué Detección". Nunca el nombre del programa, siempre el nombre del servicio (§4.1a). |
| 3 | **Entregables** | Caja AcroForm `Entregables` — piezas tangibles entregadas (workbook, certificado, informe, lo que aplique). |
| 4 | **Valor inmediato** | Caja AcroForm `Acreditacion` (nombre de campo conservado por compatibilidad con `agregar-campo-precio.py` — su contenido ya NO es una acreditación) — quick wins / logros aplicables desde el primer contacto. |

**Visual v3 — reusa la DNA visual del roadmap (`.rmx-card`/`.rmx-result-card`), no cuadros
blancos serios (obligatorio):**

- `<section class="slide s-benefits s-benefits-v2">` — la clase se mantiene `s-benefits-v2`
  por continuidad de nombre aunque el CSS ya sea la versión v3. Fondo negro, acento amarillo
  en `::before` y en el h2 (`<h2>Lo que <span class="hl">se llevan</span>.</h2>`).
- **Las 4 tarjetas van oscuras** (a diferencia de v2, donde 3-4 eran blancas): fondo
  `rgba(255,255,255,0.045)`, borde `rgba(255,255,255,0.10)`, **borde superior de 4px** de
  acento (amarillo en 1/3/4, naranja en 2), `border-radius: 13px`. El label de cada tarjeta es
  un **pill-tag** (fondo tintado + texto de color, `border-radius: 999px`), no texto plano
  uppercase — mismo lenguaje visual que `.rmx-card-tag`.
- Listas `<ul><li>` dentro de las tarjetas 1-2: sin bullet CSS, con `border-bottom` sutil
  entre ítems (efecto checklist), igual que `.rmx-result-card ul li`.
- **Cajas AcroForm de Entregables/Valor inmediato (tarjetas 3-4)**: se hornean con **fondo
  oscuro + texto blanco**, no con el blanco/negro por defecto de `acroform_appearance.py`. El
  contenido usa bullet `•` tipeado directo en el texto (carácter válido en WinAnsiEncoding;
  un `::before` de CSS no existe dentro de un campo de formulario horneado). **Esto exige un
  paso extra en el `customize-<slug>.py` del deck** — ver *Mecánica AcroForm* abajo. No tocar
  `acroform_appearance.FIELD_COLORS` (global): un override ahí para "Entregables"/
  "Acreditacion" rompería el fondo blanco por defecto en las demás ~80 propuestas que usan
  esos mismos nombres de campo.
- CSS de referencia completo: `clientes/propuestas/simple-tv-det002/styles.css` (buscar
  "Beneficios v3"). Para clones mono-fase con `_base` + `overrides.css` (tipo cumbre-andina),
  el mismo bloque va en el `overrides.css` local.
- El pie de la slide (`.foot img`) usa el logo **BLANCO** (fondo oscuro), no NEGRO.

**Layout ampliado (2026-08-28) — ESTÁNDAR para toda propuesta nueva, no un ajuste opcional.**
El v3 original (`.grid { height: 250px }`) dejaba ~300px de negro vacío debajo de las 4
tarjetas — desperdicia la mitad de la slide. Caso base: CAI-002 (Simple TV), retroaplicado el
mismo día a DET-002. Toda propuesta que se construya de aquí en adelante nace directamente
con estos valores — no con los 250px originales:

- `.grid { height: 570px; gap: 16px; }` (antes 250px).
- `.block { padding: 26px 24px 24px; }` (antes `18px 20px 16px`).
- `.label { font-size: 13px; padding: 6px 14px; margin-bottom: 18px; }` (antes `9.5px` / `4px 10px` / `10px`).
- `.block ul li`, `.block p` → `font-size: 16px; line-height: 1.6;` (antes `12px` / `1.4`).
- **Los 4 bloques arrancan su contenido en el mismo punto — nunca centrar verticalmente por
  bloque.** El primer intento (CAI-002) centraba las tarjetas 1-2 (Resultados / Por qué
  [Servicio]) con `justify-content: center` para que no quedaran pegadas arriba en una
  tarjeta alta — pero cada tarjeta tiene distinta cantidad de texto, así que cada una
  centraba a una altura distinta y se veía un desnivel entre las 4 tarjetas. Fix: sin
  `display:flex`/`justify-content` en los bloques — todos en flujo normal, alineados por
  `padding-top`. El aire extra de la tarjeta más corta queda abajo, no repartido arriba/abajo.
- Tarjetas 3-4 (Entregables/Valor inmediato): su `.label` va `position: absolute; top: 26px;
  left: 24px;` para que arranque exactamente al mismo nivel que el `padding-top` de las
  tarjetas 1-2 (que no tienen posicionamiento absoluto porque son flujo normal).
- **Cajas AcroForm de Entregables/Valor inmediato — /Rect agrandado, no solo la apariencia.**
  El `/Rect` por defecto que inyecta `agregar-campo-precio.py` (158×117pt) queda chico para
  el grid de 570px. Se agranda a **145×355pt** (`(445.5, 81.0, 590.25, 436.5)` para
  Entregables, `(637.5, 81.0, 782.25, 436.5)` para Acreditacion — mismo cálculo px→pt ×0.75
  del resto del sistema) y la fuente horneada sube de 10 a 13pt. **Si no se agranda también
  el `/Rect` real del campo** (no solo el tamaño pasado a `_make_appearance`), el visor de
  PDF escala el `/AP` horneado para que quepa en el rect chico original y el texto sale
  distorsionado — por eso `rebake_dark()` ahora acepta un parámetro `layout` que reescribe
  `obj["/Rect"]` antes de hornear. Ver implementación en `customize-simple-tv-cai002.py` o
  `customize-simple-tv-det002.py` (diccionario `BENEFICIOS_LAYOUT`).
- CSS de referencia con el layout ampliado ya aplicado:
  `clientes/propuestas/simple-tv-cai002/overrides.css` (clones con `_base`) o
  `clientes/propuestas/simple-tv-det002/styles.css` (decks con hoja local completa).

**Mecánica AcroForm (bake oscuro de Entregables/Valor inmediato)** — 3 pasos en el
`customize-<slug>.py` del deck, después de que `customize-acroforms.py` ya puso el `/V`:

1. Importar directo de `acroform_appearance.py`: `_make_appearance`, `_WIDTHS_BOLD`,
   `_DEFAULT_W_BOLD` (nombres con guion bajo, pero importables).
2. Por cada campo (`Entregables`, `Acreditacion`): actualizar su `/MK /BG` a un tono oscuro
   (ej. `(0.06, 0.06, 0.06)`) y su `/DA` a texto blanco (`1 g`), para que un re-edit en Adobe
   Reader no vuelva a fondo blanco.
3. Llamar `_make_appearance(writer, rect, da, text, base_font="/Helvetica-Bold",
   font_key="HeBO", widths=_WIDTHS_BOLD, default_w=_DEFAULT_W_BOLD, bg_rgb=(0.06,0.06,0.06),
   text_rgb=(1,1,1))` y asignar el resultado a `/AP /N` del campo — esto sobreescribe el bake
   blanco/negro que el genérico ya había hecho.

Ver implementación completa: `scripts/customize-simple-tv-det002.py` (función `rebake_dark`).

**Cómo aplicar**: quitar del `.grid` los bloques viejos (Perfil de egreso, Beneficio del
programa, Acreditación como tal) y los campos `Saber/Saber hacer/Saber ser` del
`acroforms.json`; redactar los 4 bloques nuevos por servicio, con bullet `•` en las líneas de
Entregables/Valor inmediato.

---

## Propuesta Económica por servicio

> Mecánica AcroForm existente en `scripts/agregar-campo-precio.py` — ver también
> `plantillas/generar-pdf.md` → *Regla 4.4*.

| Servicio | Variante de `.s-price` | Mecánica |
|---|---|---|
| Habilidades | Por horas (default) | `PRECIO_FIELDS` — Duración + Programa + Notas / Cotización, como siempre |
| Detección / propuestas multi-fase | "Inversión por fases" | `FASE_PRICE_FIELDS` — ya existe, ver *Roadmap* abajo y `clientes/propuestas/ioed/`, `clientes/propuestas/go-pharma/` (2 fases) |
| Políticas | Por entregable | **Pendiente de construir** — cotizar por pieza (Manual de políticas, Brújula IA, Matriz de riesgos) en vez de por hora o por fase. Sin campo AcroForm propio todavía |
| Innovación | "Inversión por Permanencia" | `CICLO_PRICE_FIELDS` — ya existe, ver `plantillas/generar-pdf.md` → *Regla 4.4* y `clientes/propuestas/zoom-innovacion/` (INN-001, primer piloto, 2026-08-30) |

---

## Propuesta Económica — descuento urgente, ROI y garantía (2026-09-23)

> Origen: pedido de convertir la hoja de cotización en cierre de venta, no solo tabla de
> precio. Aplica a las **3 variantes de cotización que ya existen** (por horas, Inversión
> por fases, Inversión por Permanencia) — no espera a que Políticas tenga la suya. La
> **garantía** es la única pieza que NO aplica a todos los servicios todavía (ver más abajo).
> **La hoja de cotización debe responder de un vistazo**: qué se hace, cuánto dura, cuánto
> cuesta, qué descuento, qué ROI, qué garantía (si el servicio la tiene).

### 1. Descuento con urgencia de aprobación

Reemplaza el campo `Descuento` "cosmético" (una caja vacía neutral) por una palanca de
cierre. Ver el patrón visual completo (incluida la excepción de color) en
`empresa/marca-visual.md` → *Descuento con urgencia — excepción de color explícita* y la
política en `empresa/politicas-comerciales.md` → *Vigencia y cancelación*.

- **Colores — excepción explícita a la paleta oficial** (pedido directo del usuario,
  2026-09-23, tras rechazar la alternativa en naranja de marca): rojo `#D32F2F` (texto) +
  rosado `#FCE4EC` (fondo), tokens `--discount-urgent-red` / `--discount-urgent-pink-bg`.
  **Acotada a este único elemento** — el resto del deck sigue 100% en paleta oficial
  (`#000000`/`#F4BA1A`/`#E58423`/`#FFFFFF`); no usar este rojo/rosado en ningún otro bloque.
- Prefijo estático `−$` (rojo `#D32F2F`, bold) inmediatamente antes de `.discount-frame` —
  el campo AcroForm sigue vacío, ventas solo escribe el número.
- Etiqueta `.cot-urgent-note`: **"Descuento válido por 15 días"** (corregido 2026-09-23 —
  antes decía "por aprobación en 15 días", más largo sin agregar claridad) — fondo rosado
  `#FCE4EC`, texto rojo `#D32F2F` bold, `font-size: 13px` (corregido 2026-09-23, antes 9px:
  muy chico para una etiqueta que debe notarse). Plazo **fijo**, no editable por ventas (a
  diferencia del monto). Convive con `.cot-validity` ("Cotización válida por 30 días") — no
  lo reemplaza, son plazos distintos.
- Aplica a **toda propuesta con campo `Descuento` visible** (los 3 variantes): en "Inversión
  por fases" el prefijo/etiqueta van junto al `Descuento` único de la columna derecha; en
  "Inversión por Permanencia" se repite junto a cada `Descuento{N}m` de las 3 columnas,
  entendiendo que ahí el descuento es "beneficio por permanencia" — la etiqueta se adapta a
  "Beneficio válido por 15 días" en ese caso (el naming "descuento" no aplica literalmente a
  un beneficio de fidelidad).

### 2. ROI estimado

Bloque estático nuevo junto a la Cotización (`.cot-roi-box`, label `.cot-roi-label` = "ROI
estimado"), redactado **por el consultor caso por caso** — no es un campo AcroForm ni una
fórmula automática:

- **Fuente**: lo que el cliente dice que quiere lograr en la **Ficha Comercial**
  (Levantamiento), cruzado con los demás datos disponibles del brief (tamaño de equipo,
  eje temático, alcance contratado). Sin Ficha Comercial ni respuesta directa del cliente a
  "qué resultados esperan" → **se omite el bloque completo**, no se inventa un ROI genérico
  (mismo criterio de "omitir, no placeholder" del resto del sistema).
- **Redacción**: 1-2 frases en lenguaje de **proyección/estimación**, nunca de garantía
  matemática — "con base en lo que [Cliente] busca lograr, el equipo puede esperar..." Evita
  cifras exactas de ROI financiero (%, $ recuperado) salvo que el propio cliente haya dado
  los números para calcularlo (horas actuales, costo hora, tamaño de equipo) — si no los
  dio, se habla en términos de tiempo/productividad, no de retorno monetario preciso.
  Mismo espíritu de honestidad que §4.17 (Dashboards): no afirmar una medición donde solo
  hay una proyección.
- Para Habilidades, enlaza naturalmente con el marco de `empresa/tipos-de-documento.md §0.2`
  (30 días uso, 60 días construcciones nuevas, 90 días tiempo/productividad) — el ROI puede
  citar ese horizonte. Para otros servicios, proyecta en los términos propios de ese
  servicio (ej. Detección: hallazgos accionables; Innovación: adopción sostenida).

### 3. Garantía 30-60-90 (solo Habilidades, por ahora)

- **Dónde**: sello/badge estático en la hoja de cotización (`.cot-garantia-badge`), visible
  únicamente cuando `brief.md → servicio: habilidades` — los otros servicios no muestran
  este bloque hasta que tengan su propio marco de seguimiento especificado.
- **Copy fijo** (tono "sello", no párrafo largo):
  ```html
  <div class="cot-garantia-badge">
    <span class="cot-garantia-tag">Garantía 30-60-90</span>
    <p class="cot-garantia-text">Estamos contigo hasta que la habilidad quede instalada.</p>
  </div>
  ```
- **Sin emoji ni ícono literal** (tono premium del sistema, `empresa/identidad.md`) — el
  "sello" se logra con tipografía (pill-tag `.cot-garantia-tag`, mismo lenguaje visual que
  `.rmx-card-tag`/`.label` de Beneficios v3) y un borde de acento, no con un glifo de escudo.
- **Deliberadamente sin mecanismo específico**: no promete reembolso ni repetición gratuita
  de una sesión — es un mensaje de **acompañamiento**, no una cláusula financiera. Si más
  adelante el equipo comercial define un mecanismo concreto (reembolso parcial, refuerzo sin
  costo, etc.), se agrega aquí y en `empresa/politicas-comerciales.md` explícitamente — no
  asumir uno mientras tanto.
- El pitch de ventas que explica qué se hace en cada check-in (30/60/90) lo actualiza el
  equipo comercial por su cuenta — el deck solo necesita el sello, no el detalle operativo
  (ese vive en `empresa/tipos-de-documento.md §0.2`).

---

## Slide "Seguimiento 30-60-90" — garantía explicada + ROI expandido (2026-09-23, solo Habilidades)

> Opcional, a pedido del cliente/usuario — no es parte fija del deck todavía. Va **después
> de Propuesta Económica**, antes de Próximos pasos. Solo tiene sentido cuando
> `servicio: habilidades` (mismo criterio que el badge `.cot-garantia-badge` de la Cotización
> — ver sección de arriba): expande esa garantía en una slide propia, con el texto completo
> de `empresa/tipos-de-documento.md §0.2` y un ROI más desarrollado que el de la Cotización.

- **Estructura**: `<section class="slide s-roadmap s-followup">` — reutiliza el fondo negro +
  eyebrow + h2 de `.s-roadmap` (sin nodos ni flechas, no es una secuencia temporal sino 3
  check-ins independientes):
  1. `.followup-intro` — 1 párrafo de encuadre (por qué existe el seguimiento).
  2. `.followup-cards` — 3 `.rmx-card` en fila (`rmx-card-f2`/`-f3`/`-f4` = amarillo/naranja/
     blanco, igual progresión que la escalera de Cierre), cada una con `.rmx-card-tag` ("30
     días"/"60 días"/"90 días"), `.rmx-card-name` (la pregunta que responde) y 2
     `.rmx-facets` (Medimos / Aportamos) tomados literal de `empresa/tipos-de-documento.md
     §0.2`.
  3. `.followup-roi` — caja destacada con ROI **expandido**: a diferencia del ROI compacto de
     la Cotización (una proyección corta), acá se conecta explícitamente la curva 30-60-90
     con el retorno ("a 30 días... a 60... a 90..."). No repetir el mismo texto en ambos
     lugares — son dos niveles de detalle, no una duplicación.
- **CSS**: vive en el `overrides.css` del deck (no en `_base/`), reutilizando `.rmx-card`/
  `.rmx-facets` ya definidas ahí para el roadmap — solo se agregan `.followup-intro`,
  `.followup-cards` (flex row, sin `.rmx-lcol`/nodos) y `.followup-roi`.
- **Sin campos AcroForm nuevos** — todo estático, redactado por Claude a partir del §0.2 y
  del ROI ya construido para la Cotización. No afecta el conteo de 13 campos.
- **Renumeración**: al insertar esta slide entre Cotización y Próximos pasos, corren tanto el
  `.counter` global (`NN/TT`) como el eyebrow numerado de Próximos pasos (ej. `07`→`08`, el
  que corresponda) — no el del Cierre, que no lleva número.
- Primer uso real: `clientes/propuestas/amv-tecnologia-cerebro-digital/` (CAI-023,
  2026-09-23).

---

## Slide de Cierre — ruta/escalera editable (2026-08-26)

> Reemplaza el cierre viejo (`.end-message` fijo "De X a Y" + CTA con link). Caso base:
> Go Pharma CAP-030. **Pendiente de propagar** a los canónicos y demás decks (no se tocan
> retroactivamente — se adopta al regenerar cada uno).

- **Forma**: cinta de "Resultado" a ancho completo arriba (`.end-summit`) + 3 escalones
  ascendentes (`.stair-1/2/3`, amarillo → naranja → blanco, alturas 90/140/190px) que leen
  como progresión hacia el siguiente nivel. Metáfora **genérica de pasos al éxito** — NO
  menciona los 4 servicios del Modelo Intezia (no es gancho de upsell).
- **Todo editable**: 4 cajas AcroForm (`CierreResultado`, `CierrePaso1..3`) para que ventas
  redacte y personalice por cliente. El texto por defecto vive en el `customize-<slug>.py`
  y en los `<span class="acro-default-text">` del HTML (ocultos en print vía `@media print`).
- **CTA sin link**: "Esperamos tu respuesta" es `<span class="cta">`, no `<a>` (decisión
  2026-08-26 — el CTA de Calendly se retiró del cierre).
- **Correo de la empresa en `.end-contact`**: `servicio@intezia.com` (decisión 2026-08-27,
  reemplaza `info@intezia.com` en toda propuesta nueva — el de la asesora de ventas no
  cambia, sigue siendo el personal de cada asesora).
- **Mecánica AcroForm**: estas 4 cajas NO las inyecta `agregar-campo-precio.py` (ese solo
  cubre Propuesta Económica / Inversión por fases / Lo que se llevan / Cómo arrancamos).
  Se agregan en el `customize-<slug>.py` del deck, que además hornea su apariencia con el
  color de fondo de cada escalón vía `acroform_appearance.FIELD_COLORS` (amarillo/naranja/
  blanco). Al propagar a un canónico, esto tendrá que moverse a `agregar-campo-precio.py`
  como grupo propio (marker del H2/estructura del cierre) para no depender de un script por
  deck.

---

## Slide 4 — Programa: distribución adaptable de módulos

| Volumen | Layout | h3 | obj | chip |
|---|---|---|---|---|
| 1-3 módulos | 3 cols × 1 fila, cards grandes | ≤ 30 ch | ≤ 110 ch | ≤ 38 ch |
| 4 módulos | 2×2, cards medianas | ≤ 26 ch | ≤ 90 ch | ≤ 30 ch |
| **5-6 módulos** | **3×2, modo compacto** | **≤ 22 ch** | **≤ 80 ch** | **≤ 28 ch** |
| 7-9 módulos | 3×3, compacto agresivo | ≤ 20 ch | ≤ 70 ch | ≤ 26 ch |
| 10+ módulos | 4 cols, mínimo | ≤ 18 ch | ≤ 60 ch | ≤ 22 ch |

Si una idea no cabe en el chip → acortarla. No reactivar tamaños grandes para 5+ módulos.

**Título de Programa**: `N módulos · X horas.` — solo aquí van las cifras.
**`.meta`**: frase-síntesis del hilo conductor, ≈ 60 chars, una sola línea, sin repetir conteo ni horas.

**Corrección 2026-09-23 — tarjetas no se estiran a llenar la slide**: antes, `.s-program
.modules` tenía `flex:1`, que hacía crecer la grilla (y cada `.module` dentro, vía
`align-items:stretch`) hasta ocupar TODO el alto restante de la slide — con pocos temas (1-2
chips) la tarjeta quedaba con un vacío enorme debajo del contenido, sin relación con su
capacidad real (hasta 7 temas para 3 módulos, ver `capacidad-cajas.md`). Caso base:
`amv-tecnologia/` (4 módulos, 2 chips c/u) y `amv-tecnologia-cerebro-digital/` (2 módulos, 2
chips c/u). Fix: se quitó el `flex:1` de `.modules` y se fijó `min-height:320px` en la
tarjeta base (1-3 módulos) — el resto de anchos por volumen (4/5-6/7-9/10+) ya traían su
propio `min-height` menor vía `:has()`, sin cambios ahí. El sobrante de alto ahora queda como
aire debajo del grid completo, no repartido dentro de cada tarjeta — más armónico con poco
contenido, sin perder tamaño cuando el contenido sí llena la capacidad documentada.

---

## Roadmap — patrón de 3 etapas (Diagnóstico → Construcción → Implementación)

> **Default desde 2026-07-23** para toda propuesta multi-fase / capacitación con `.s-roadmap`. Reemplaza el patrón anterior de 2 etapas (Diagnóstico / Implementación agrupadas).

El roadmap (`.s-roadmap`) presenta el proyecto como **3 etapas secuenciales**, no 2:

1. **Etapa 1 · Diagnóstico** — hasta 2 sesiones (por área/frente del cliente). Se entiende la necesidad real antes de construir nada.
2. **Etapa 2 · Construcción (Intezia)** — Intezia arma la solución con los hallazgos del diagnóstico. **Sin sesiones con el cliente** — no consume su tiempo.
3. **Etapa 3 · Implementación** — 2 sesiones (por área/frente). Se activa la solución construida y se enseña al equipo a usarla.

**Por qué**: separar «Intezia construye» de «el cliente aprende a usar» dentro del roadmap deja claro que la construcción no le consume tiempo al cliente, y que la implementación llega ya con el trabajo hecho, no en paralelo con el diseño.

**Implementación técnica** (el componente `.rmx-*` nace pensado para 2 rutas — extenderlo a 3 exige):

- `.rmx-route` necesita `min-height: 0` — sin eso, `flex:1` en un flex container columna no encoge los items por debajo de su alto de contenido, y con 3 filas el contenido natural desborda la altura fija de `.rmx-journey` **sin que `verificar-overflow.js` lo detecte** (colisión interna entre bloques, no desborde de página — exige revisión visual).
- Compactar `.rmx-card` (padding), `.rmx-card-name` (margin) y `.rmx-facets li` (padding) ~15% para que 3 filas quepan en el espacio que antes usaban 2.
- 3er acento de color para la etapa de Construcción **dentro de la paleta oficial**: negro/blanco (`.rmx-node-f4`, `.rmx-card-f4`), no un color nuevo. Diagnóstico sigue en amarillo, Implementación en naranja.
- Conectores del fork/merge: con 2 rutas los centros están a 25%/75%; con 3 pasan a 16.667% / 50% / 83.333%. La fila del medio (exactamente en el centro) usa un **conector recto** (`.rmx-mid`, barra sin curva), no el truco de esquina con `border-top/left` + `border-radius` que usan las filas de arriba/abajo.
- Ajustar `.rmx-journey` height lo mínimo necesario (probar primero solo con la compactación + `min-height:0`, antes de agrandar la caja) para no empujar el bloque de metodología/footer fuera de la slide.

**Referencia**: `clientes/propuestas/pago-tronic/` (CAP-081, slide 11) — primer deck con las 3 etapas, `styles.css` local con la extensión completa del componente. Clonar desde ahí (o portar su CSS) cuando el roadmap necesite esta estructura. `pilotes-perforados/` sigue siendo válido como referencia de 2 etapas si un proyecto puntual no separa una fase de construcción propia.

---

## Próximos pasos — calendario de inicio (2026-09-23)

> Objetivo: eliminar la objeción de tiempo ("¿cuándo empezamos?") mostrando fechas
> concretas y qué logra el cliente en ese plazo, sin tocar los 3 campos AcroForm existentes
> (`Paso01–03`) ni violar §4.15 (nunca acuerdos económicos en esta slide).

- **Fuente del dato**: `brief.md → fecha_arranque_deseada` y `resultados_esperados`. Se
  toman de la **Ficha Comercial** cuando existe (de ahora en adelante, la mayoría de
  propuestas nuevas debería tenerla — ver `CLAUDE.md §6 Paso 3`); sin Ficha Comercial,
  **se pregunta directo al usuario** antes de generar esta pieza — nunca se inventa una
  fecha ni un resultado. Sin respuesta, se omite el bloque de calendario/proyección y la
  slide se queda con los 3 pasos de logística de siempre, sin ese agregado.
- **Dónde vive**: dentro de `.s-steps` (no es una slide nueva) — **dos variantes**, elegidas
  según cuánto dato de fecha se tenga:

  **Variante A — resumen simple** (`.steps-projection`): un solo "próximo arranque", sin
  detallar cada sesión. Úsala cuando solo se conoce una fecha de referencia, no la agenda
  completa.
  ```html
  <div class="steps-projection">
    <span class="steps-projection-tag">Próximo arranque disponible</span>
    <span class="steps-projection-dates">Martes 6 y jueves 8 de octubre · semana del 5 al 9</span>
    <p class="steps-projection-result">[proyección de resultado en ese plazo]</p>
  </div>
  ```

  **Variante B — calendario completo** (`.steps-calendar`, agregada 2026-09-23): lista **todas**
  las sesiones de la propuesta, kick-off incluido, en 2 columnas. Úsala cuando el usuario da una
  cadencia recurrente (ej. "martes y jueves de 10 a 12 desde tal semana") y pide ver la agenda
  entera, no solo la primera fecha.
  ```html
  <div class="steps-calendar">
    <span class="steps-calendar-tag">Calendario de inicio · próxima fecha: martes 29 de septiembre</span>
    <p class="steps-calendar-result">[proyección de resultado — cuándo queda el entregable listo]</p>
    <div class="steps-calendar-grid">
      <div class="cal-col">
        <div class="cal-row"><span class="cal-date">Mar 29 sep</span><span class="cal-time">10-11</span><span class="cal-title">Kick-off</span></div>
        <!-- ...una .cal-row por sesión... -->
      </div>
      <div class="cal-col"><!-- segunda columna, resto de las sesiones --></div>
    </div>
  </div>
  ```
  - Reparte las sesiones ~50/50 entre las 2 columnas, en orden cronológico (primera mitad
    columna 1, segunda mitad columna 2) — no por tipo de sesión.
  - **Sesiones de más de 2h en una cadencia de slots fijos** (ej. "4h por área" con slots de
    2h): se **parten** en tantas filas como slots necesite, tituladas `(1/2)`, `(2/2)`, etc. —
    nunca se fuerza una sesión larga dentro de un slot corto.
  - **Etapas sin sesión con el cliente** (ej. "Construcción, 1 semana, Intezia"): se incluyen
    igual como fila marcadora `cal-row cal-marker`, sin `.cal-time`, en itálica atenuada — da
    continuidad narrativa al calendario sin fingir que hay una sesión ahí. Si esa semana cae
    justo en un slot Tue/Thu que tocaría, ese slot se salta (no se agenda sesión encima).
  - **Cards `.step-card` compactas** (2026-09-23): para dejarle espacio a esta variante, las 3
    tarjetas de Paso01–03 bajan de `min-height:400px` a `200px` (ver *Slide 4* más abajo, mismo
    principio de "no forzar cajas a llenar el resto de la slide"). Esto exigió recalcular los
    rects AcroForm de `Paso01–03` en `scripts/agregar-campo-precio.py` — cascada obligatoria,
    ver comentario en `_base/styles.css` → `.acro-area`.
  - **Tamaño (corregido 2026-09-23 — se veía "muy pequeño")**: `.steps-calendar` sube a
    `padding: 22px 30px 24px`, tag/fecha/hora/título en fuente más grande
    (`.steps-calendar-tag` 12.5px, `.cal-date` 14.5px, `.cal-title` 14px). `.cal-row`
    padding vertical queda en **5px** (no más — a 8px desbordaba la slide con 7 filas por
    columna, el calendario más largo del sistema hasta ahora, CAI-023: 14 sesiones). Si un
    futuro caso tiene más de ~7 filas por columna, correr `verificar-overflow.js` antes de
    entregar — este es el límite ya probado, no uno teórico.
- **Visual — dentro de la paleta oficial en ambas variantes** (a diferencia del descuento
  urgente, este bloque **no** usa la excepción roja/rosada — esa está acotada solo al badge de
  descuento): franja negra de ancho completo, borde izquierdo amarillo de 8px, tag en amarillo
  mayúsculas, fechas/día en amarillo bold (variante B) o blanco bold grande (variante A). El
  contraste negro/amarillo sobre el fondo blanco de la slide ya transmite urgencia sin salir de
  marca.
- **Fuente de la proyección de resultado** (ambas variantes): redactada a partir de
  `resultados_esperados` cruzado con el marco de seguimiento del servicio contratado
  (Habilidades: 30-60-90 de `empresa/tipos-de-documento.md §0.2`; otros servicios: sus propios
  hitos). Mismo lenguaje de proyección/estimación que el ROI de la Cotización — nunca una cifra
  garantizada. Sin `resultados_esperados` explícito, redactar desde el alcance/logro ya
  establecido en el brief (no inventar un dato nuevo) — no es motivo para omitir el bloque si sí
  hay `fecha_arranque_deseada`.
- **Nunca economía**: igual que el resto de `.s-steps`, cero menciones de anticipo, firma,
  factura o pago — es agenda y expectativa de resultado, no transacción (§4.15).
- Primer uso real: `clientes/propuestas/amv-tecnologia/` (DET-019) y
  `clientes/propuestas/amv-tecnologia-cerebro-digital/` (CAI-023), 2026-09-23 — ambas terminaron
  usando la Variante B (calendario completo) tras un ajuste pedido por el usuario el mismo día.

---

## Campos AcroForm — 13 campos en 3 slides

> Tabla única de campos (slide, marker, tipo, pre-fill): `plantillas/generar-pdf.md` →
> *Regla 4.4*. Resumen: Beneficios (`Entregables`, `Acreditacion` — pre-llenados) ·
> Propuesta Económica (3 de precio + `Programa` + `Notas` — todos vacíos para ventas) ·
> Próximos pasos (`Paso01–03 Titulo/Body` — redactados listos-para-entregar).
> Los valores se declaran en `acroforms.json` y se aplican con `customize-acroforms.py <slug>`.

**Reglas de AcroForm**:
- El `<div class="multi-box">` detrás de cada caja editable se queda **vacío** — sin texto fantasma.
- Cajas Entregables y Acreditación siempre en **negrita** (fuente `/HeBO`).
- Los 3 campos de precio llegan vacíos; Programa y Notas también (ventas los llena en Reader).
- Adobe Reader: 5 campos + cálculo JS completos. Preview macOS: 4 campos editables, TOTAL sin cálculo.

---

## Reglas de copy

- **Portada — el eyebrow debe nombrar el servicio (bloqueante — CLAUDE.md §4.1a punto 4,
  2026-09-01)**: `.s-cover .eyebrow` dice el/los servicio(s) reales de `brief.md → servicio`,
  no solo el tipo de documento. El tipo de documento (Charla, Taller, Capacitación
  in-company, Curso, Diplomado) puede seguir apareciendo, pero el servicio no puede faltar.
  - ✗ Evitar: «Propuesta formativa · Capacitación in-company» (no dice qué servicio es).
  - ✓ Por servicio: `habilidades` → «Servicio de Habilidades»; `deteccion` (standalone) →
    «Servicio de Detección»; `deteccion` con Habilidades cotizada en el mismo documento
    (ej. DET-xxx tipo Amcor/Simple TV) → «Servicio de Detección y Habilidades»; `politicas`
    → «Servicio de Políticas»; `innovacion` → «Servicio de Innovación» (o «Plan de
    Innovación», ya usado en Zoom INN-001); `integral` → nombra las fases reales del plan,
    no los 4 servicios genéricos (ej. «Plan Integral · 4 fases»).
  - Ejemplo aplicado: «Propuesta formativa · Servicio de Habilidades» (deck canónico:
    Charla/Taller/Capacitación/Curso/Diplomado solo-Habilidades) · **«Propuesta de proyecto ·
    Servicio de Habilidades»** (plantilla compacta de Habilidades, `CLAUDE.md §4.21`: se
    presenta como proyecto, no como capacitación; dirección 2026-10-05, DUSA CAI-035) ·
    «Propuesta de negocio · Servicio de Detección y Habilidades» (combo cotizado junto,
    estilo DET-002 Simple TV).
  - Caso base: 2026-09-01, Simple TV CAI-002 («Capacitación in-company» → «Servicio de
    Habilidades»).
- **No centrar la venta en un ejemplo anecdótico único (2026-09-23)**: si el brief trae un
  caso puntual que el cliente mencionó en vivo (ej. "yo mismo probé X y me tomó 10 minutos en
  vez de 8 horas"), **no lo uses como título, hook de Impacto ni hilo conductor del deck**.
  Es un dato de contexto que da fuerza puntual, no el proyecto completo — sobre-enfocarse en
  un solo caso genera disonancia si no se repite igual con el resto del alcance.
  - ✗ Evitar: título/H1 nombrando el proceso específico («De 8 horas a 10 minutos.»), o
    repetir la misma cifra en Diagnóstico + Beneficios + Impacto + ROI.
  - ✓ Preferir: una mención **genérica y breve**, una sola vez («el equipo ya probó por su
    cuenta que la IA funciona/reduce tiempo real»), sin nombrar el proceso ni las cifras — y
    vender el resto del deck sobre el alcance completo (todas las áreas/funciones, no el
    caso aislado).
  - Caso base: AMV Tecnología, DET-019 y CAI-023 (2026-09-23) — título original «De 8 horas a
    10 minutos.» reemplazado por «Del criterio manual a la decisión con datos.» tras
    instrucción directa del usuario.
- Una idea por slide. Si tiene más → dividir.
- Tono según `empresa/identidad.md`.
- **Cliente primero**: "ustedes" / nombre empresa antes que "Intezia".
- Verbos en activa. Datos concretos antes que adjetivos vagos.
- No usar "IA" como default — el eje temático lo define el brief.
- **Negrita**: `<strong>` en nombres propios (herramientas, plataformas), términos técnicos del eje temático y frases clave. Solo primera aparición por slide · ~2–3 por slide · en cuerpo (`<p>`, `<li>`), no en títulos ni AcroForms.
- **Impacto**: toda cifra proviene de estudio real con fuente citada verbatim. Nunca inventar datos.
- **Sin afirmar migración de stack del cliente (bloqueante — CLAUDE.md §4.11)**: Intezia se ajusta al stack del cliente, no lo cambia. Nunca escribir que la empresa migra / migrará / está migrando a otro stack, suite o plataforma (Google Workspace, Microsoft 365, etc.).
  - ✗ Evitar: «la migración a Workspace está en curso», «cuando adopten [plataforma]», «el banco migrará a [suite]».
  - ✓ Reencuadrar al entorno que el cliente **ya usa** y a herramientas que **se integran** a él: «el plan se apoya en el entorno Google del banco y en herramientas que operan sin VPN».
  - El stack del cliente es contexto interno del `brief.md` para diseñar, no una afirmación de cara al cliente en el deck.
  - **Elección de herramienta en positivo**: si el deck justifica por qué se usa una herramienta (ej. Gemini), encuádralo como **facilidades/ventajas que ofrece** en el contexto del cliente, nunca como restricción ni como que las otras «no sirven» o «están bloqueadas». ✓ «el plan se construye sobre Gemini porque ofrece facilidades que otras herramientas no: vive dentro del entorno Google que el banco ya usa y opera sin VPN».
- **Acrónimos y siglas explicados en el primer uso (bloqueante — CLAUDE.md §4.12)**: el equipo de ventas no puede vender lo que no entiende. Ninguna sigla de jerga aparece sin explicar.
  - ✗ Evitar: «AUP corporativo», «prompting RCTF», «usan GenAI» sueltos, sin decir qué son.
  - ✓ Expandir en el primer uso de **cada slide**: «Política de Uso Aceptable (AUP)», «marco RCTF (Rol, Contexto, Tarea, Formato)», «IA generativa». La expansión va en un elemento con espacio (`<p>`, `<li>`), no en chips ni timebars.
  - Si la expansión no cabe (chip, segmento de barra), usa el término en lenguaje natural en vez de la sigla cruda («Política de Uso Aceptable» en vez de «AUP»).
  - **Excepciones** (no expandir): sigla del cliente que él conoce (BDV, BCV), siglas de uso general en su sector (VPN, API en módulo técnico), códigos de catálogo (CAP-, TA-, CU-…). En duda, expande.
- **Sin guion largo como separador (bloqueante — CLAUDE.md §4.13)**: la redacción debe sonar humana y natural. `—` (em-dash) y `–` (en-dash) están prohibidos como separador en todo output cara al cliente.
  - ✗ Evitar: «sin método ni criterio común — los resultados dependen…», «el plan se apoya en el entorno Google del banco — adopción sin fricción…», «BDV — organización con implementación exitosa».
  - ✓ Reemplazo natural según el rol del guion: **coma** o **paréntesis** (aposición), **dos puntos** (contraste o desarrollo), **punto + nueva oración** (idea relacionada), `·` middle dot (separador de listas o metadatos). Ej.: «no es un taller por semana: es construir una arquitectura», «sin método ni criterio común. Los resultados dependen de quién escriba el prompt», «BDV, organización con implementación exitosa».
  - Excepción: si una **fuente verbatim** (cita, título de estudio) contiene `—` original, se respeta dentro de las comillas.
- **Posicionamiento — construimos, no solo enseñamos (2026-09-23, propuestas nuevas de aquí
  en adelante, no retroactivo)**: el cliente contrata una solución, no solo formación —
  responde de entrada la pregunta recurrente **"¿ustedes lo hacen o lo hacemos nosotros?"**.
  - Donde el impacto sea correcto (típicamente Objetivos y el bloque "Por qué [Servicio]"
    de Beneficios v3), suma verbos de construcción junto a los de enseñanza: **"construimos,
    probamos y dejamos instalado"**, no solo "capacitamos" o "enseñamos". Intezia arma el
    proceso junto al equipo del cliente, no se limita a explicarlo.
  - **No es un reemplazo total de "capacitación"**: los nombres de categoría del catálogo
    (Charla, Taller, **Capacitación In-Company**, Curso, Diplomado, códigos `CAI-`/`TA-`/
    `CU-`/`DIP-`) y cualquier lugar donde el término sea estructural o legal (Acreditación,
    títulos de programa) se quedan igual — el cambio es de tono en el copy de venta, no de
    taxonomía.
  - **Encuadre de fondo**: Intezia no es una casa de software — integra IA en los procesos
    reales del cliente y entrega un producto tangible (el skill, la política, el sistema),
    no solo una sesión de contenido. Útil para reforzar el "Por qué [Servicio]" y el bloque
    de Entregables de Beneficios v3.
  - ✗ Evitar como único framing: «los capacitamos en el uso de [herramienta]» (suena a
    curso, no a solución).
  - ✓ Preferir: «construimos junto a su equipo el [entregable concreto], lo probamos con
    casos reales y lo dejamos instalado y en uso» — la capacitación es el vehículo, no el
    resultado que se vende.

---

## Checklist final (antes de entregar)

- [ ] Formato A4 landscape verificado (`@page { size: A4 landscape }`, PDF horizontal)
- [ ] División correcta confirmada (logo Fundación o Educación según `brief.md`)
- [ ] Logo presente en TODAS las slides (variante por contraste)
- [ ] Solo paleta oficial (`#000000`, `#F4BA1A`, `#E58423`, `#FFFFFF`) — **única excepción
      aprobada**: rojo/rosado (`#D32F2F`/`#FCE4EC`) en el badge de descuento urgente
      (`.cot-urgent-note`/`.cot-sign-minus`), ver *Descuento con urgencia de aprobación*
      arriba. Rojo/rosado en cualquier otro elemento del deck sí es una violación de marca.
- [ ] Tipografía Graphit aplicada (Inter como fallback)
- [ ] Slide `.s-eval` **solo** si tipo = curso o diplomado
- [ ] Slide `.s-orange` (ABR) **omitida** si tipo = charla
- [ ] Slide `.s-price` **omitida** si división = fundacion
- [ ] Slide 4 — título con `N módulos · X horas`; `.meta` = frase-síntesis ≤ 60 chars
- [ ] **Cronograma con los 5 elementos (bloqueante, 2026-09-23)**: cada `.s-schedule` tiene
      Temas + `.timebar` (Tiempo) + las 3 columnas de `.ses-cols`. Sin `.timebar` = vacío feo
      entre Temas y las columnas — ver *Reglas de layout*.
- [ ] Slide Impacto: gráficas CSS (barras + gauge), cifras de estudio real con fuente verbatim, hook de ventas, slide negra con logo BLANCO, sin campos AcroForm
- [ ] Cajas multiline (Entregables, Acreditacion, Programa, Notas) = HTML vacío detrás, contenido solo en AcroForm /V
- [ ] **`/AP` horneado en Programa y Notas (bloqueante, bug real 2026-09-23)**: no basta con
      que el extractor de PDF de Claude los muestre bien — regenera apariencias solo y no
      detecta este bug. Verificar con pypdf: `campo.get('/AP')` debe existir (no `None`) para
      Programa y Notas — si falta, Adobe Reader y Preview los muestran en blanco pese al
      valor correcto. Ver `plantillas/generar-pdf.md` → *Negrita de Entregables/Acreditacion*.
- [ ] Campo Entregables pre-llenado: 2–4 destacados + 3 institucionales (via `customize-acroforms.py`)
- [ ] Campo Acreditacion: `[CÓDIGO]` sustituido; líneas 2-3 intactas
- [ ] Slide Próximos pasos pre-llenada: 3 pasos «Cómo arrancamos» listos-para-entregar, bodies ≤ 130 chars
- [ ] **Sin link de Calendly en el cierre (bloqueante, 2026-09-14)**: el CTA de `.s-end` va
      sin `<a href="calendly...">` — ni el cierre viejo (CTA con link) ni el escalera (ya usa
      `<span class="cta">` desde 2026-08-26) enlazan a Calendly en propuestas nuevas o
      regeneradas. El contacto es la asesora comercial en `.end-contact`. Misma regla en
      Dashboards (`plantillas/dashboard-edutrace.md`). No retroactivo.
- [ ] Palabras clave resaltadas con `<strong>` en cuerpo de slides (primera aparición, sin saturar)
- [ ] **Sin afirmar migración de stack del cliente (bloqueante — CLAUDE.md §4.11)**: ninguna slide dice que la empresa migra/migrará a otra suite o plataforma; se enmarca en su entorno actual
- [ ] **Acrónimos explicados (bloqueante — CLAUDE.md §4.12)**: cada sigla de jerga (AUP, RCTF, GenAI…) está expandida en su primer uso por slide; ninguna sigla cruda en chips/timebars sin contexto
- [ ] **Sin guion largo (bloqueante — CLAUDE.md §4.13)**: `grep -nE "—|–"` en `index.html` y en placeholders de scripts da cero ocurrencias (excepto dentro de citas verbatim). Reemplazo con coma, paréntesis, dos puntos, punto o `·`.
- [ ] Sin placeholders `{{...}}` sin llenar (excepto precio — intencional)
- [ ] **Hoja de cotización completa (bloqueante, 2026-09-23)**: `.s-price` responde qué se
      hace, cuánto dura, cuánto cuesta, descuento (con `.cot-urgent-note` "15 días" + prefijo
      `−$`), ROI estimado (o explícitamente omitido por falta de dato — nunca inventado), y
      garantía **solo si** `servicio: habilidades`. Ver `propuesta-comercial.md` →
      *Propuesta Económica — descuento urgente, ROI y garantía*.
- [ ] **Calendario de inicio en "Cómo arrancamos" (bloqueante, 2026-09-23)**: si `brief.md`
      tiene `fecha_arranque_deseada`/`resultados_esperados`, `.s-steps` incluye
      `.steps-projection` (una fecha resumen) o `.steps-calendar` (agenda completa con todas
      las sesiones, si el usuario dio una cadencia recurrente). Si esos datos no existen y no
      se preguntaron, el bloque se omite — no se inventa fecha ni resultado.
- [ ] **Sin ejemplo anecdótico centrando el deck (bloqueante, 2026-09-23)**: título, hook de
      Impacto, ROI y Beneficios no repiten un caso puntual que el cliente mencionó en vivo
      (cifras/proceso específico) como hilo conductor — se vende el alcance completo. Ver
      *Reglas de copy* → "No centrar la venta en un ejemplo anecdótico único".
- [ ] **Sanity check visual (bloqueante — CLAUDE.md §4.10)**: abrir PDF en Preview y revisar slide por slide. Sin overflow, sin chips truncados con `...`, sin texto cortado, sin solapamientos footer/contador/logo.
