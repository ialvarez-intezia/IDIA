# Brief — Banco Activo · Detección + Habilidades Fase 1, Vicepresidencia de Negocios (DET-021)

## Corrección 2026-10-01 (3ra vuelta) — color de texto en "Inversión total del proyecto"

Instrucción directa del usuario: el monto de "Inversión total del proyecto" se veía en naranja
y no se leía. Causa: al quitar Descuento/TOTAL (corrección anterior, mismo día), ese recuadro
pasó a llevar el fondo amarillo sólido que antes tenía "TOTAL" (`overrides.css`), pero el `/DA`
del campo `PrecioBase` sigue siendo el naranja por defecto de `agregar-campo-precio.py`
(pensado para el fondo crema claro del diseño estándar) — naranja sobre amarillo sólido no
contrasta.

- `scripts/customize-banco-activo-deteccion-negocios.py` ahora corrige el `/DA` de `PrecioBase`
  a `/Helv 26 Tf 0 g` (negro, 26pt) — mismo tratamiento que tenía el recuadro "TOTAL" antes de
  eliminarse.
- Verificado simulando un valor de prueba ("2.400 USD") horneado con `acroform_appearance.py`:
  se lee bien, negro sobre amarillo.

## Datos administrativos

- **Empresa**: Banco Activo
- **Sector**: Banca / servicios financieros, entidad regulada, más de 250 empleados
- **Slug**: `banco-activo-deteccion-negocios`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — es un combo Detección + Habilidades (Fase 1), y por
  regla del sistema el `servicio` de `meta.json` sigue la taxonomía del combo aunque el código
  no lleve el prefijo DET- por default (aquí sí, `DET-021`, dado directo por el usuario). Ver
  memoria `combo-deteccion-habilidades-codigo-vs-servicio`.
- **Tipo de documento**: Detección multi-gerencia + Habilidades In-Company combinadas.
- **Fuente**: Ficha de Levantamiento Banco Activo (Verónica Rubio, elaborada 2026-09-22,
  registrada 2026-09-23) + instrucción directa del usuario (2026-09-24).
- **Base estructural**: clonado de `la-tienda-del-blumer/` (DET-020) — el precedente de
  Detección multi-área con roadmap `.rmx-linear` de 3 etapas + slide `.s-vision` ("La ruta
  completa"). A diferencia de Blumer (Detección pura, Habilidades 100% a futuro y no
  cotizada), este deck extiende el patrón a un combo real: Detección + Habilidades Fase 1
  ambas cotizadas, con solo la EXPANSIÓN de Habilidades a más gerencias quedando "a futuro, no
  cotizada".

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
  (misma asesora que la Propuesta A, `banco-activo-cerebros-digitales/` CAI-027 — mismo
  levantamiento).
- **Contacto cliente**: Nahir, VP Vicepresidencia de Negocios (líder de la iniciativa,
  entrevistada en el levantamiento). Patrocinador y decisor final de la contratación:
  Giancarlo, Presidente — Nahir debe validar con él antes de avanzar.
- **CORRECCIÓN 2026-10-01 (instrucción directa del usuario, anula lo anterior)**: Intezia **NO**
  ha trabajado antes con Banco Activo. El dato original de este punto ("ya tuvo un servicio
  previo de Habilidades, Bloque A de la ficha") era incorrecto — se usó por error para
  respaldar la slide de Impacto de esta propuesta y de CAI-027, y se retiró de ambos decks. No
  reintroducir esta afirmación en ninguna propuesta de Banco Activo.

## Dos propuestas en paralelo, mismo levantamiento

Ver también `banco-activo-cerebros-digitales/brief.md` (Propuesta A, CAI-027, ya construida).
Esta es la **Propuesta B**: Detección + Fase 1 de Habilidades para la Vicepresidencia de
Negocios de Nahir (13 gerencias en total, incluye Adquirencia y Medios de Pago bajo su tutela
temporal).

## Qué pide el cliente (mensaje directo del usuario, 2026-09-24)

> "Propuesta B — Detección + Fase 1 de Habilidades: Para la Vicepresidencia de Negocios de
> Nahir (13 gerencias en total, cubre también Adquirencia y Medios de Pago, que ella tutela
> temporalmente). El dolor que Nahir dejó clarísimo, y donde debe quedar el foco fuerte de
> Habilidades, es puntos de venta y medios de pago: no tiene visibilidad de facturación,
> churn ni instalaciones pendientes, y el proceso de activación de puntos de venta es lento y
> sin trazabilidad. Además, le gustaría que Habilidades pudiera abarcar algunas gerencias
> prioritarias adicionales — mencionó que serían unas 3, sin comprometerse a cuáles — que se
> van a terminar de definir con lo que arroje la Detección (que sí cubre las 13 gerencias
> completas). Tengámoslo anotado como algo a considerar en el alcance, no como decidido
> todavía."

Y, sobre el calendario (mensaje posterior): "coloca el calendario igual el kick off para
esta fecha y las sesiones a partir del 12 lunes y miercoles" — "esta fecha" se interpretó
como el mismo kick-off que la Propuesta A (jueves 8 de octubre), por ser el mismo
levantamiento y presumiblemente presentado en la misma ventana de tiempo. **Sin confirmar
explícitamente por el usuario** — señalar si el kick-off de esta propuesta debe ser una fecha
distinta.

## Decisiones de diseño (2026-09-24) — dimensionamiento

Todas siguen `empresa/politicas-comerciales.md` → "Dimensionamiento por servicio".

1. **Detección — 13 gerencias, 54h**: la ficha (Bloque específico · Detección) confirma
   explícitamente el alcance: "Vicepresidencia de Negocios de Nahir, sus 13 gerencias
   regionales/líderes, incluyendo Adquirencia y Medios de Pago bajo su tutela" y "13 personas
   (las 13 gerencias/líderes de su vicepresidencia)" a entrevistar. Regla: 4h por área + 2h de
   Fundamentals grupal (13 personas, bajo el máximo de 25) → 13×4h = 52h + 2h = **54h**.
2. **Nombres de las 13 gerencias — solo 2 se conocen**: la ficha nombra explícitamente
   "Adquirencia (puntos de venta)" y "Medios de Pago (tarjetas de crédito)" como áreas
   priorizadas bajo tutela de Nahir; las otras 11 solo se describen como "10 gerencias
   regionales además de la sede central" — sin nombres individuales. Se usa "Gerencia
   regional 1" a "11" en vez de inventar nombres (regla "Omitir, no inventar placeholder").
3. **Habilidades Fase 1 — 1 área combinada, no 2 separadas**: la ficha lista Adquirencia y
   Medios de Pago como 2 "Área priorizada" distintas (Bloque A), pero el usuario las encuadra
   como un solo dolor continuo ("el foco fuerte de Habilidades... es puntos de venta y medios
   de pago", en singular). Se optó por tratarlas como **1 área combinada** para Habilidades
   (ambas bajo la misma tutela temporal de Nahir, procesos operativamente entrelazados:
   activación → facturación → seguimiento) en vez de cotizar 2 áreas separadas (que hubiera
   duplicado el rango 8-12h a 16-24h). **Esta es una interpretación, no una instrucción
   explícita del usuario** — confirmar antes de enviar si el cliente espera 2 áreas
   cotizadas por separado.
4. **Habilidades Fase 1 — 12h (extremo superior de la banda 8-12h)**: 3 procesos
   identificados de la ficha (Tareas reales del día a día + Bloque C):
   - Activación end-to-end de puntos de venta (Proceso 1 de la ficha).
   - Seguimiento de facturación y churn (Proceso 2 de la ficha).
   - Reportes directos de Nahir / consolidación de data dispersa.
   3 procesos ≤ 5 → banda 8-12h de `empresa/politicas-comerciales.md`. Se usó el extremo
   superior (12h = 4h por proceso × 3) dado que la ficha marca la urgencia como máxima
   ("para ayer") y el área combina 2 sub-equipos con datos dispersos en varios sistemas.
   **También una interpretación dentro del rango permitido — no un número dado por el
   usuario**, confirmar antes de enviar.
5. **~3 gerencias adicionales — documentadas, NO cotizadas**: instrucción explícita del
   usuario ("tengámoslo anotado... como algo a considerar en el alcance, no como decidido
   todavía"). Se representó como el 3er paso de la slide `.s-vision` ("Expansión de
   Habilidades", tag "a definir con los hallazgos, no cotizado") y en la nota de la hoja de
   cotización — nunca como horas ya incluidas en las 66h totales.
6. **Total combo: 66h** (54h Detección + 12h Habilidades Fase 1).
7. **Con certificado de participación INTEZIA** para Habilidades Fase 1 únicamente — la
   Detección (incluida Fundamentals) sigue sin certificado, es auditoría no curso (ver
   memoria `deteccion-sin-certificado`).
8. **Con garantía 30-60-90 + slide de Seguimiento** (`.s-followup`) — a diferencia de Blumer
   (Detección pura, sin este componente), aquí SÍ hay un componente real de Habilidades que lo
   justifica. CSS copiado de `banco-activo-cerebros-digitales/overrides.css` a este deck.
9. **Sin afirmar migración de stack (§4.11)**: Banco Activo opera Google Workspace con
   licencias corporativas de Copilot y Gemini.
10. **Cita real de Nahir en la slide de dolor**: "Yo hoy no tengo cómo hacerle seguimiento...
    yo no tengo visibilidad en nada de eso" (Bloque D de la ficha) — se usó recortada:
    "No tengo visibilidad en nada de eso."
11. **Impacto (§4.9)**: se reutilizaron 2 fuentes bancarias ya verificadas en otros decks del
    sistema — EY-Parthenon (Encuesta de IA Generativa en Banca 2025, ya usada en
    `venezolano-de-credito/`) para adopción/expectativa de ingresos, y Anthropic Economic
    Index (2025, ya usado en `banco-activo-cerebros-digitales/`) para el dato de adopción
    2.6×. No se usó el stat de JPMorgan/marketing de `venezolano-de-credito/` por no ser
    relevante al eje de esta propuesta (visibilidad operativa, no mercadeo).

## Calendario de inicio (agregado 2026-09-24)

Instrucción directa del usuario: *"coloca el calendario igual el kick off para esta fecha y
las sesiones a partir del 12 lunes y miercoles"*.

- **Kick-off**: jueves 8 de octubre de 2026, 10-11 (misma fecha que la Propuesta A — ver nota
  de ambigüedad arriba).
- **Fundamentals**: lunes 12 de octubre, 10-12 (2h).
- **13 sesiones de gerencia** (4h cada una, 10-14): lunes y miércoles, desde el miércoles 14
  de octubre hasta el miércoles 25 de noviembre (~7 semanas). Nótese que el patrón de días es
  distinto al de la Propuesta A (CAI-027 usa martes/jueves) — instrucción explícita y
  diferenciada del usuario para cada propuesta.
- **Compresión visual**: 15 filas totales (kick-off + Fundamentals + 13 gerencias) — se
  extendió `.steps-calendar-grid` a **3 columnas** (5+5+5) en vez de las 2 columnas
  habituales, ya que 15 filas superan el máximo ya probado sin desborde en 2 columnas (9
  filas, `la-tienda-del-blumer/`). Cada fila es una sola fecha (no requiere combinar varias
  fechas por fila, a diferencia de `banco-activo-cerebros-digitales/` CAI-027 donde cada
  fila agrupó 3 fechas). Ver memoria `calendario-inicio-comprimir-filas-muchas-sesiones`.
  Verificado con `node scripts/verificar-overflow.js banco-activo-deteccion-negocios`.
- **Habilidades Fase 1 SIN fechas todavía**: la ficha indica explícitamente que la Fase 1 de
  Habilidades se diseña "a medida" con los hallazgos del Índice de Madurez de la Detección —
  se omite del calendario en vez de inventar fechas (regla "Omitir, no inventar placeholder").
  Se menciona en el resumen del calendario ("Habilidades Fase 1 se agenda con el alcance que
  confirme el Reporte Final").

## Corrección 2026-10-01 — slide de Impacto sin estadísticas externas

Instrucción directa del usuario: retirar las gráficas con fuente EY-Parthenon de la slide de
Impacto (11/15, `.s-impact`). Mismo criterio y mismo día que la corrección equivalente en
`../banco-activo-cerebros-digitales/brief.md` (CAI-027).

- Se quitó `.chart-panel` (barras 61%/77% adopción bancaria) y `.gauge-panel` (58% incremento de
  ingresos), ambos con fuente EY-Parthenon 2025.
- **Primer reemplazo (mismo día, luego corregido)**: un bloque `.proof-panel` apoyado en "Banco
  Activo ya confió antes en Intezia" (servicio previo de Habilidades, dato que esta misma ficha
  traía en el punto de arriba, "Contacto"). **El usuario confirmó que ese dato es FALSO** —
  Intezia nunca ha trabajado con Banco Activo; se retractó el punto de "Contacto" arriba.
- **Reemplazo final**: referencia anónima real y verificada — cliente del sector financiero
  (procesamiento y adquirencia de medios de pago, caso Credicard CAP-041, no se nombra en el
  deck), Índice de Impacto 86/100 (`clientes/dashboards/credicard/resultados.json`, cruzado con
  `clientes/banco-casos-de-exito/index.html`). Credicard es un caso de Habilidades/capacitación,
  no de Detección — se cita como prueba de experiencia/competencia en el sector financiero, no
  como precedente de un servicio de Detección ya ejecutado.
- `.hook-text` se reescribió sin la cifra EY citada y sin `<strong>` (el contenedor
  `.impact-hook .hook-text` tiene un glitch de renderizado confirmado con `<strong>` — ver
  memoria `bug-strong-glitch-impact-hook-text`; el texto original ya lo usaba, corregido de
  paso).
- Título de la slide (`h2`) ajustado dos veces: de "La banca ya avanza con IA, la visibilidad es
  lo que falta." a "Ya trabajamos juntos. Ahora, visibilidad real." (1er reemplazo, también
  retractado por implicar relación previa con Banco Activo) a "La experiencia ya está probada.
  Ahora, visibilidad real." (final).
- Sin cifras inventadas (§4.9).
- **Alerta sobre `banco-casos-de-exito/index.html`**: ese catálogo interno tiene AL MENOS 3
  entradas bancarias con el mismo patrón de dato falso (Banco Activo, Banco Plaza, Banco de
  Venezuela). No usar ese documento como fuente de un caso de banca sin cruzarlo primero contra
  un `meta.json` en estado "Aprobada" o un `resultados.json` real.
- Pendiente de correr el trío `verificar-propuesta.sh` → `generar-pdf.sh` →
  `customize-acroforms.py` tras esta corrección. `estado` en `meta.json` se puso en
  `En corrección`; vuelve a `Enviada` automáticamente al regenerar el PDF (§4.19).

## Pendiente de confirmar antes de enviar

- **Fecha del kick-off de esta propuesta específica**: se asumió la misma que CAI-027 (jueves
  8 de octubre) por ser el mismo levantamiento — el usuario no lo confirmó explícitamente para
  esta propuesta en particular.
- **Habilidades Fase 1 como 1 área combinada (12h) vs. 2 áreas separadas** (Adquirencia +
  Medios de Pago, potencialmente 16-24h) — ver decisión #3 arriba.
- **12h como extremo superior de la banda 8-12h** — ver decisión #4 arriba; podría ajustarse a
  8-10h si el cliente busca un punto de entrada más económico para esta primera fase.

## Cotizaciones separadas (agregado 2026-09-29, a pedido explícito del usuario)

Instrucción directa del usuario: separar la cotización de Detección de la de Habilidades Fase
1, que hasta ahora vivían en una sola hoja combinada (66h). Se dividió la slide "Propuesta
Económica" en 2 hojas independientes, usando el mecanismo multi-página nativo de
`agregar-campo-precio.py` (2 slides `.s-price` con el mismo `h2.title` "Propuesta Económica":
la 1ª recibe los campos estándar, la 2ª recibe `PrecioBase_2`/`Descuento_2`/`PrecioTotal_2`/
`Programa_2`/`Notas_2` automáticamente — ver memoria `multi-track-una-propuesta.md`, mismo
patrón ya usado en `hjb-quimica/CAI-031`).

- **Hoja 1 · Detección (54h)**: Duración, Programa y Notas propios, con nota cruzada avisando
  que Habilidades Fase 1 se cotiza aparte. **Sin garantía 30-60-90**: por regla del sistema
  (`hoja-cotizacion-cierre-venta.md`), esa garantía aplica solo al servicio Habilidades — no
  correspondía en la hoja de Detección.
- **Hoja 2 · Habilidades Fase 1 (12h)**: Duración, `Programa_2` y `Notas_2` propios, con su
  propio ROI enfocado en el dolor de Adquirencia/Medios de Pago, y la garantía 30-60-90 (que sí
  aplica aquí).
- El resto del deck (roadmap operativo, `.s-vision` "La ruta completa", los 3 cronogramas,
  Beneficios, Impacto, Seguimiento 30-60-90, calendario de inicio, Cierre) no cambió de
  contenido — solo se renumeraron los contadores y las 3 slides finales (Seguimiento, Próximos
  pasos, Cierre) al insertar la hoja nueva. Deck: 15 → **16 slides**.
- Verificado sin desbordes (`verificar-overflow.js`) y revisado visualmente slide por slide del
  PDF regenerado.

## Corrección 2026-09-29 (mismo día) — vuelta a 1 sola hoja "Inversión por fases"

Instrucción directa del usuario, el mismo día que el cambio anterior: volver a **una sola
hoja de cotización**, con los recuadros de Detección y Habilidades del lado izquierdo, "como
lo hemos venido haciendo" — el patrón **"Inversión por fases"** (marker propio, grupo
`FASE_PRICE_FIELDS` de `agregar-campo-precio.py`, origen CAP-098 IOED 2026-08-11), ya usado en
`go-pharma/CAP-030`, `maurel-prom/ALL-003`, `ioed/`, `simple-tv-det002/`, entre otros — no el
mecanismo multi-página de "2 hojas Propuesta Económica" recién aplicado.

- **1 sola slide** `.s-price` con `h2.title` = "Inversión por fases": 2 recuadros
  (`.fase-price-row`) del lado izquierdo, Fase 1 · Detección (54h) y Fase 2 · Habilidades
  (12h), cada uno con su propia caja editable (`PrecioFase1`/`PrecioFase2`) y una descripción
  estática de 1 línea. Debajo, Notas (única, restaurada al contenido combinado original), ROI
  estimado y Garantía 30-60-90 — ambos NO forman parte del patrón "Inversión por fases"
  original (anterior al 2026-09-23), así que se agregaron a mano, reposicionados en la única
  franja libre que quedaba (debajo de Notas).
- **Sin campo `Programa`**: el grupo `FASE_PRICE_FIELDS` no lo incluye — su contenido vive en
  la descripción estática de cada recuadro (`.fase-price-desc`).
- **`FASE_PRICE_FIELDS` está fijo a 3 fases** (no 2): queda un campo huérfano `PrecioFase3`,
  eliminado por `scripts/customize-banco-activo-deteccion-negocios.py` (ajuste nuevo,
  portado de `customize-go-pharma-cap030.py`), que también reescribe el JS de `PrecioBase`
  para sumar solo Fase 1 + Fase 2.
- **Coordenadas CSS exactas portadas de `go-pharma/styles.css`**: los recuadros de fase y la
  columna de Cotización (base/descuento/total) usan posiciones DISTINTAS a las del layout
  estándar de "Propuesta Económica" — son las que matchean los `/Rect` fijos de
  `FASE_PRICE_FIELDS` en Python. Ver el bloque nuevo en `overrides.css`.
- Deck: 16 → **15 slides** (mismo conteo que antes del split de la mañana, pero con el layout
  "Inversión por fases" en vez del "Propuesta Económica" combinado original de un solo bloque
  Duración+Programa).
- Verificado sin desbordes (`verificar-overflow.js`) y revisado visualmente el PDF regenerado
  — los 2 recuadros, Notas, ROI y Garantía caben sin solaparse ni desbordar.

## Trío ejecutado y verificado (2026-09-24)

`verificar-propuesta.sh` OK (sin desbordes) → `generar-pdf.sh` → `customize-acroforms.py` →
`customize-banco-activo-deteccion-negocios.py`. Revisión visual de las 15 slides sin
defectos. PDF: "DET-021 De no tener visibilidad, a decidir con datos en tiempo real..pdf".

**Ajustes de overflow aplicados durante la construcción** (detectados por
`verificar-overflow.js`, corregidos acortando contenido, nunca el diseño):
- Slide 4 (Programa, 5 módulos): sin `<p class="obj">`, títulos ≤14 caracteres y máx. 2
  temas por módulo — el modo "5-6 módulos" de `.s-program .modules` solo baja `min-height`,
  no reduce fuente/padding (ver memoria `bug-program-modules-5-6-no-compact`).
- Slides 2, 5 y 10: recortado el copy más largo (diagnóstico, facetas del roadmap, viñetas de
  Beneficios) a longitudes cercanas a las de `la-tienda-del-blumer/`.
- Slide 12 (Propuesta Económica): el texto de "Duración" a 3 líneas montaba el rótulo
  "PROGRAMA" encima (bug ya documentado, `bug-price-block-programa-absolute` — el detector
  automático no lo detecta, se vio en la revisión visual del PDF). Se acortó a una sola frase
  de ~93 caracteres.
