# Brief — Luppro · Asesoría Técnica en APIs de Modelos de IA (CAP-103)

## Datos administrativos

- **Cliente**: Luppro
- **Sector**: sin definir (no se conoce aún; genérico a propósito)
- **Slug**: `luppro`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-103`) — formato asesoría técnica / diagnóstico, sin desarrollo
- **Programa**: Asesoría Técnica en Integración, Costos y Optimización de APIs de Modelos de IA
- **Eje temático**: cómo integrar las APIs de distintos modelos de IA (GPT y otros) al bot de atención al cliente que el propio equipo técnico de Luppro ya construyó; cómo funciona la estructura de costos de cada proveedor; cómo optimizar el consumo (tokens, razonamiento, orquestación de mensajes) para controlar el gasto al escalar.
- **Modalidad**: sin afirmar — se confirma en el arranque (Paso 01). El deck usa "sesión de asesoría" en genérico.
- **Duración**: sin cifra de horas de cara al cliente (instrucción del usuario, 2026-08-13) — el deck describe el formato como "2 módulos, sesión técnica única" sin comprometer horas totales ni por módulo. Internamente sigue siendo 1 sesión de 2 bloques (ver programa.md §5.2 para el detalle de contenidos por bloque, ya sin minutos).
- **Participantes**: equipo de tecnología de Luppro (los responsables del bot). Número sin definir — no se compromete cifra, se acota en el kick-off.
- **Fecha del brief**: 2026-08-13
- **Estado**: `Borrador`

## Contacto

- **Persona/empresa contacto**: Luppro — datos de contacto directo por confirmar.
- **Asesora comercial Intezia**: María Iribarren · +58 414-0570056 · miribarren@intezia.com (asumida por convención — es la asesora comercial por defecto en la mayoría de las propuestas activas; confirmar con el usuario si es otra "María").
- **Consultor / Facilitador**: NO se asigna en la propuesta inicial — INTEZIA designa un consultor senior con perfil técnico en integración de APIs de IA y arquitectura de costos al confirmar el kick-off.

## Contexto (fuente: nota de voz del usuario, 2026-08-13 — muy poco contexto, propuesta deliberadamente genérica)

1. **Luppro ya construyó su propio bot de atención al cliente** con su equipo técnico interno. **Intezia no construye ni interviene el bot** — no hace falta, ya existe.
2. **Lo que piden es asesoría**, no desarrollo: que el equipo de tecnología de Luppro entienda cómo conectar e integrar las APIs de los distintos modelos de IA (GPT y otros) al bot que ya tienen.
3. **Punto de dolor central**: el equipo no sabe cómo funciona la estructura de costos de esas APIs — cuánto cobra cada proveedor, qué modelo conviene según el caso de uso, cómo se factura el consumo (tokens de entrada, salida, razonamiento).
4. **Riesgo que quieren evitar**: escalar el bot a un volumen alto de usuarios (la cifra que se mencionó como ejemplo fue ~40.000 personas) y recibir una factura de API muy por encima de lo esperado, por no saber gestionar créditos, distribuir modelos o controlar el consumo.
5. **No se sabe con qué stack está construido el bot** (podría ser n8n u otra herramienta) — el equipo técnico de Luppro lo tiene armado; ese dato no es necesario para diseñar esta asesoría, que es agnóstica de la herramienta de orquestación.
6. **Encaje**: diagnóstico y acompañamiento técnico — Intezia asesora, Luppro decide e implementa con su propio equipo.

## Diagnóstico

1. El equipo técnico de Luppro construyó su bot de atención al cliente, pero no tiene claridad sobre cómo integrar las APIs de los distintos modelos de IA disponibles en el mercado.
2. No conocen a fondo la estructura de costos de cada proveedor (tokens de entrada, salida y razonamiento), lo que dificulta elegir el modelo que más conviene según el volumen y el caso de uso.
3. Sin un criterio de optimización de consumo, el gasto del bot puede dispararse al escalar a un volumen alto de conversaciones.
4. Hoy no existe un mecanismo que anticipe o controle el gasto antes de que llegue la factura.

## Estructura de la sesión (propuesta, deliberadamente genérica)

Sesión única de 8 h, dividida en 2 módulos:

- **Módulo I — Integración y arquitectura de APIs de modelos de IA (4h)**: panorama de proveedores (GPT y otros), arquitectura de integración al bot ya construido, autenticación y buenas prácticas de seguridad, criterios técnicos para elegir el modelo según el caso de uso, revisión guiada de la integración actual de Luppro.
- **Módulo II — Estructura de costos y optimización de consumo (4h)**: cómo se cobra una API de IA (tokens de entrada, salida, razonamiento), comparativa de precios entre proveedores, proyección de costos a escala, técnicas de optimización de consumo, monitoreo y control de gasto, plan de acción para Luppro.

## Decisiones de diseño

- **Clonado de `puro-lomo-bajo-auditoria/` (CAP-091)**: clon canónico mono-fase (linaje cumbre→anabella→puro-lomo, Educación, enlaza `_base/styles.css`), mismo formato de 12 slides, sesión única en 2 bloques. Se retiró el bloque de Notas de traslado del facilitador (era específico de Puro Lomo/Villa de Cura) — el AcroForm `Notas` queda con `""` explícito en `acroforms.json` (no aplica ningún caso especial para Luppro; ver aprendizaje `bug-notas-acroform-placeholder-visible` — omitir la clave deja visible el placeholder de plantilla).
- **Sin cifra de horas (2026-08-13, instrucción del usuario)**: se retiraron todos los números de horas/minutos de cara al cliente — portada, `.s-program` (h2 "2 módulos." sin sufijo de horas), badges `.ses-dur` de las 2 slides de cronograma (eliminados), etiqueta "Tiempo · Total 4 h" → "Ruta del bloque", minutos de cada segmento del `.timebar` (se conserva el `flex` proporcional, solo se quitó el número del texto), campo `Programa` del AcroForm, y bloque "Duración" de `.s-price` → renombrado a "Formato" ("2 módulos, en una sesión técnica única."). Aplicado también en `programa.md` (Duración, tabla §5.2) para no dejar el documento oficial desincronizado. `brief.md` conserva la nota de por qué, como registro interno (§4.14).
- **Términos y condiciones en la cotización (2026-08-13, instrucción del usuario)**: se agregó el bloque `cot-terms-box` (mismo patrón y mismo enlace institucional que `canguro`, `aerocentro`, `agromundial`, `ioed`, `dusa-cap088`) debajo de `cot-validity` en `.s-price`, con el texto estándar (sin la cláusula de confidencialidad de `ioed`, que es específica de un diagnóstico con información sensible).
- **Sin nombre de plataforma de orquestación del bot**: no se sabe con qué está construido (n8n u otra herramienta) y no hace falta saberlo — la asesoría es agnóstica a esa capa.
- **Proveedores de IA sí se nombran de forma neutral** (OpenAI/GPT, Anthropic/Claude, Google/Gemini, entre otros) porque es el objeto mismo de la asesoría — comparar costos y capacidades entre ellos, sin inclinar la recomendación hacia uno en particular.
- **Modalidad sin afirmar** (mismo patrón que `fivenca-acompanamiento`): el deck no compromete presencial/online, se confirma en el Paso 01 de "Cómo arrancamos".
- **Slide de Impacto** (`.s-impact`): 2 estudios reales citados verbatim — Stanford HAI (2025) sobre la caída del costo de inferencia, y Harness (2026) sobre sobrecostos y falta de previsión de gasto en IA a nivel empresarial. Ver detalle en `index.html` y fuentes abajo.
- **Equipo facilitador**: "Equipo INTEZIA Education" (consultor con perfil técnico en integración de APIs de IA, a designar en el kick-off) + María Iribarren como asesora comercial.

## Fuentes de la slide de Impacto (§4.9)

1. **Stanford HAI — The 2025 AI Index Report (2025)**: el costo de consultar un modelo con el desempeño equivalente a GPT-3.5 (64.8% en MMLU) cayó de $20 a $0.07 por millón de tokens entre noviembre 2022 y octubre 2024 — una reducción de más de 280 veces en año y medio.
2. **Harness — 2026 State of AI in FinOps (2026, 700 líderes y practicantes de ingeniería de software en 5 países — EE.UU., Reino Unido, Francia, Alemania, India)**: el 72% de las empresas sufrió un pico de gasto en IA inesperado en el último año; el 56% dice que anticipar el gasto en IA es cuestión de instinto, no de datos; se estima que el 26% del gasto en IA es desperdicio, sin retorno medible.

## Pendientes / por confirmar

- Confirmar si la asesora comercial es efectivamente María Iribarren (asumida por convención).
- Confirmar nombre y datos de contacto de la persona en Luppro.
- Confirmar modalidad (presencial / online), fechas y número de participantes del equipo técnico.
- Confirmar sector/industria de Luppro (sin dato aún).
- Confirmar presupuesto indicativo (no discutido).
