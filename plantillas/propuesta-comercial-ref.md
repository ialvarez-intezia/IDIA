# Referencia de slides — Propuesta comercial

> Archivo de referencia detallado. **Cargar solo cuando haya una duda puntual sobre una slide específica o se esté construyendo un tipo de propuesta completamente nuevo (sin clon disponible).**
> Reglas, tablas y checklist están en `plantillas/propuesta-comercial.md`.

---

## Detalle por slide

### 1. Portada (`.s-cover`)

- **Fondo negro** + **rectángulo decorativo** en la esquina superior derecha (gradiente cálido amarillo→naranja, rotado 45°). Cuadrante inferior izquierdo libre (no decorar ahí — el CAO pidió evitarlo).
- **Logo Intezia grande** (220 px alto), variante BLANCO según división. **`margin-left: -28px`** para compensar el padding interno del PNG y alinear "Education" con el inicio de los textos siguientes.
- **Eyebrow**: *"Propuesta formativa"* en amarillo (NO incluir fecha).
- **Título grande** (72 px, Graphit Bold) del programa con `.hl` amarillo en una palabra/frase clave.
- **Lead descriptivo** (~17 px) bajo el título: 1-2 líneas que resuman el qué y para qué del programa, sin listas.
- **Línea media** (`bottom: 56px`): a la izquierda `Código: XX-NNN` en amarillo, a la derecha el nombre de la empresa cliente en blanco.
- **Sin footer** (no se incluye logo ni "Intezia Education — Propuesta Única"; sería redundante con el logo grande arriba).

### 2. Punto de dolor + Diagnóstico (`.s-pain`)

- **Sin eyebrow numerado**: abre con una **frase poderosa** como `<h2>` que reformula el problema.
- **Contexto**: párrafo corto con el contexto/necesidad del cliente.
- **5 ítems de diagnóstico** numerados (sin subtítulos extra, lista limpia).
- Pie de página estándar.

### 3. Objetivos estratégicos (`.s-goals`)

- **Eyebrow**: "02 · Objetivos".
- **Bloque negro destacado** con el **objetivo general** (label "OBJETIVO GENERAL" en amarillo + texto en blanco grande).
- **Lista numerada** de **objetivos específicos** (3 típicamente, con badges amarillos).

### 4. Programa (`.s-program`)

- **Eyebrow**: "03 · Programa".
- **Título (`<h2>`)**: `N módulos · X horas.` — conteo de módulos + duración total en horas. Es el **único** lugar donde van las cifras.
- **Descripción general (`.meta`)**: una frase que sintetiza el hilo conductor — lo más destacable que se lleva el participante. **Una sola línea**, presupuesto ≈ 60 caracteres. No repite el conteo ni las horas. Se renderiza en mayúsculas + tracking. Ej: *"Fundamentos, uso diario y adopción responsable de Claude"*.
- Por cada módulo: número romano grande en naranja (I, II, III...) · título del módulo · objetivo instructivo en cursiva (una línea) · **lista de títulos de temas** como tags amarillos (1.1, 1.2, etc.).
- Sin descripciones largas (esa info va al cronograma).

### 5. Desglose instructivo / cronograma (`.s-schedule`) — 1 slide por sesión

Desde 2026-05-16 el desglose es **una sesión por slide**. 3 sesiones → 3 slides; diplomado de 9 módulos → 9 slides.

- **Un `<section class="slide s-schedule">` por sesión.**
- Cada slide lleva, de arriba abajo:
  - **Ruta de aprendizaje** (`.ruta`): nodo numerado + cinta de progreso con gradiente amarillo→naranja rellena a `(X/N)·100%` + rótulo «Sesión X de N».
  - **Identidad de la sesión** (`.ses-head`): `.ses-mod` (módulo + modalidad) + `<h2>` con «Módulo N: nombre del módulo» (números romanos — **nunca «Tema N»**) + `.ses-dur` (duración).
  - **Los 5 elementos** en `.ses-body` (flexbox, sin alturas fijas): Temas (chips con `flex-wrap`), Tiempo (`.timebar` con segmentos `style="flex:<minutos>"`), y Estrategias de enseñanza / Estrategias de aprendizaje / Recursos en 3 columnas (`.ses-cols`; Recursos en `.block-rec` negro).
- **No omitir ningún elemento.** Los 5 siempre presentes.
- Si una sesión excede una página A4, se añade a mano un slide hermano `s-schedule s-schedule-cont` («Sesión X · continuación»). Nunca se corta contenido.
- **Columnas ajustadas al contenido (estándar)**: las 3 columnas no se estiran hasta el fondo — toman la altura de su contenido y se igualan a la más alta. El `.ses-body` reparte el aire sobrante entre Temas, Tiempo y las columnas (`justify-content: space-between`). Dentro de cada columna, cada ítem es una **fila de igual alto con divisor sutil** (`<li>` flex con `border-bottom` rgba).

### 6. Sistema de evaluación (`.s-eval`) — CONDICIONAL

- **Solo si tipo = curso o diplomado.** Para Taller/Capacitación/Charla, **omitir esta slide** del HTML.
- Tabla con tres filas: Formativa (30 %), Sumativa parcial (50 %), Sumativa final (20 %).
- Última fila destacada en amarillo: Total 100 %.
- Bloque negro inferior: "Mín **70/100** para certificación".

### 7. Metodología ABR (`.s-orange`) — FIJA

- **No se modifica** según el CAO ("hoja por defecto").
- Fondo naranja completo + triángulo negro en esquina.
- Tres pilares con números amarillos gigantes: Tutoría activa, Transferibilidad inmediata, Curaduría de contenidos.
- **Omitir** esta slide solo para Charla (no usa ABR).

### 8. Beneficios + Equipo (`.s-benefits`)

Cuatro bloques en grid horizontal (4 columnas) + bloque negro inferior con el equipo:

1. **Perfil de egreso** (estático): `<ul><li>` con Saber / Saber hacer / Saber ser, una línea cada uno. **Sin cuadritos amarillos** — texto flush left, fluye hacia abajo.
2. **Beneficio del programa formativo** (estático): párrafo que parametriza el `[Eje temático del programa]`.
3. **Entregables** (editable AcroForm `Entregables`): caja multiline tipo textarea. El `<div class="multi-box">` se queda **vacío** (sin texto fantasma). Pre-llenado con `customize-acroforms.py` tras generar el PDF: 2–4 entregables destacados deducidos del desglose instructivo + los 3 institucionales fijos (`ENTREGABLES_DEFAULT`). Orden: destacados primero, institucionales después.
4. **Acreditación** (editable AcroForm `Acreditacion`): 3 líneas fijas (`ACREDITACIONES_DEFAULT`): 1) `Programa registrado en INTEZIA Education como [CÓDIGO].` 2) `Cumple con el modelo pedagógico oficial (ABR).` 3) `Material curado y revisado por el equipo académico.` — solo `[CÓDIGO]` es variable.

**Reglas visuales no negociables**:
- Cajas Entregables y Acreditación siempre en **negrita** (fuente `/HeBO`).
- No poner contenido HTML detrás de las cajas editables.
- No restituir cuadritos amarillos a Perfil de Egreso ni a las cajas editables.
- Coordenadas pt PDF: Entregables `(438, 338, 596, 455)`, Acreditacion `(630, 338, 788, 455)`.

**Equipo facilitador** (bloque negro inferior): cards con avatar circular. Avatar usa **iniciales** por defecto (`<div class="avatar" data-photo="">AV</div>`).

### 9. Impacto / estudios (`.s-impact`)

**Slide negra** — rompe el ritmo del deck para que "golpee" justo antes del precio.

- **Cabecera**: eyebrow `07 · Impacto` + titular con resaltado amarillo.
- **Gráfica de barras** (panel izquierdo): 3–5 filas «área → valor». Cada barra fija su valor en el texto visible y en `--w` (mismo número, escala 0–100). Eje 0–100 fijo.
- **Gauge radial** (panel derecho): un dato headline en `conic-gradient`. Editar el número visible y `--pct` (mismo valor).
- **Chips**: 1–3 métricas secundarias.
- **Hook de ventas** (banda inferior a todo el ancho): frase que convierte la evidencia en urgencia comercial.
- **Fuente citada**: línea con los estudios usados, verbatim, dentro del panel.

**Reglas visuales**: slide negra → logo BLANCO y contador blanco. Gráficas en CSS puro (`conic-gradient`, barras con `--w`); nada de imágenes ni JS. El copy NO debe contener las frases marcador de AcroForm. Sin campos AcroForm en esta slide.

### 10. Propuesta Económica (`.s-price`) — 5 campos AcroForm

Estructura en dos columnas: izquierda (Duración + Programa + Notas), derecha (Cotización).

**Columna izquierda:**
- **Duración** (estático): etiqueta `Duración:` + valor parametrizado (`{{duracion_total}}`).
- **Programa** (editable `Programa`, multiline): label con cuadrito amarillo 8×8 px `::before`. Coordenadas: CSS `top: 195px, left: 56px, width: 480px`; AcroForm `(42, 350, 402, 429)` pt.
- **Notas** (editable `Notas`, multiline): label con cuadrito **naranja** 8×8 px. CSS `top: 365px`; AcroForm `(42, 219, 402, 301)` pt. Gap ~40 px vs. Programa.

**Columna derecha (Cotización):**
- `PrecioBase` editable + `Descuento` editable + `PrecioTotal` editable con **cálculo automático JS** (`base − |descuento|`), fondo amarillo.
- Subtexto fijo: *"Válido únicamente por 7 días en divisas."*

**Detección de página**: el script Python busca *"Propuesta Económica"* (case-insensitive).

**Compatibilidad**: Adobe Reader = 5 campos + cálculo completos. Preview macOS = 4 campos editables, TOTAL vacío (no ejecuta JS de PDF).

**Si cambia la maqueta**: sincronizar coordenadas entre `styles.css` (px) y `agregar-campo-precio.py` (`PRECIO_FIELDS` en pt). Factor conversión landscape: 0.75 px→pt; `y_pt = 595 - (y_top_css × 0.75 + h_css × 0.75)`.

### 11. Próximos pasos (`.s-steps`)

- 3 cards con número fantasma 01–03 detrás del texto.
- 2 campos AcroForm por card: título single-line (`PasoNNTitulo`) + body multiline (`PasoNNBody`) — 6 campos totales.
- Pre-llenado con `customize-acroforms.py`: los 3 pasos «Cómo arrancamos» redactados listos-para-entregar. **Pauta estándar**: 1) Confirmar fechas y zona horaria · 2) Firmar acuerdo + factura 50 % anticipo · 3) Reunión de arranque (~30 min) para alinear los casos reales.
- Bodies ≤ ~130 chars para que no se corten sin click en el PDF.

### 12. Cierre (`.s-end`)

Hero negro con cintas de gradiente cálido (arriba completa, abajo 60% derecha). Estructura centrada:

1. **Logo Intezia grande (220 px)** centrado horizontalmente, variante BLANCO.
2. **Mensaje** (38 px Graphit Bold, line-height 1.15, max 600 px): *"Danos la oportunidad de llevarte al [siguiente nivel] con [eje temático]."* — "siguiente nivel" en `.hl-orange`, eje temático en `.hl-yellow` (bloque amarillo, texto negro).
3. **CTA "Esperamos tu Respuesta"** — `<a class="cta" href="…" target="_blank" rel="noopener">` (nunca `<span>`). URL canónica: `https://calendly.com/intezia/30min?month=YYYY-MM` — siempre con `?month=` del mes actual. Estilo neo-brutalista: rectángulo amarillo + texto blanco + sombra dura naranja 10 px + outline negro 1 px.
4. **Bloque de contacto al pie** (`bottom: 56px`): Línea 1: `ASESORA DE VENTAS:` (amarillo bold) + datos comercial separados por `·` en naranja. Línea 2: `EMPRESA:` + razón social + RIF/CIF + correo institucional.

---

## Implementación de referencia

`clientes/propuestas/cumbre-andina/` es la **implementación canónica** (taller mono-fase). `clientes/propuestas/pilotes-perforados/` es la referencia para propuestas multi-fase. Si hay duda sobre clases CSS, estructura de bloques o anidamiento HTML, leer el deck correspondiente.
