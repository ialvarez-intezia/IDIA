# Brief — Robin Agency · IA Aplicada por Áreas (CAP-080)

## Datos administrativos

- **Cliente**: Robin Agency · agencia de marketing y publicidad
- **Naturaleza**: Capacitación in-company · **3 formaciones en una sola propuesta**, una por departamento. No es un proyecto por fases: las 3 pueden dictarse en simultáneo o escalonadas, según agenda.
- **Slug**: `robin-agency-cap080`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-080`)
- **Programa**: IA Aplicada por Áreas
- **Eje temático**: IA aplicada a la productividad de una agencia de marketing · multi-departamento · multi-herramienta (Gemini + Claude)
- **Modalidad**: Híbrido
- **Duración**: 8 h por área (a confirmar por departamento en el kick-off)
- **Participantes**: 40 en total, en 3 departamentos
- **Ecosistema preferido**: Google (Gemini) y Claude. La agencia ya tiene algunas licencias de Gemini y pidió orientación de Intezia sobre la mejor opción de licenciamiento.
- **Fechas**: sin fechas tentativas al momento del levantamiento; se confirman en el arranque.
- **Fecha del brief**: 2026-07-21
- **Estado**: `Enviada` · `fecha_entrega: 2026-07-20` (registro previo, no se sobrescribe — §4.19).
- **Antecedente**: existe una propuesta previa para el mismo cliente (`robin-agency`, CAP-032, otro requerimiento). Esta es una solicitud independiente.

## Contacto

- **Solicitante / Asesora comercial Intezia**: **Flavia Martínez** · +58 414-5756615 · fmartinez@intezia.com
- **Cliente referente**: líder de cada departamento (Medios Digitales, Cuentas, Talento Humano) — se identifican en el kick-off.

## Por qué este proyecto

Robin Agency ya usa IA de forma individual y aislada, sin un ecosistema centralizado ni un criterio común entre sus equipos. El objetivo es nivelar a cada área bajo un mismo estándar y liberar tiempo hoy consumido en tareas manuales y repetitivas ("trabajo de carpintería"), para que los equipos se enfoquen en lo estratégico. Cada departamento tiene retos y flujos propios, así que la formación no puede ser genérica: se diseña una ruta por área, sobre sus procesos reales.

## Diagnóstico

1. El uso de la IA es aislado e individual: no hay ecosistema centralizado ni criterio común entre equipos.
2. Las tareas manuales y repetitivas consumen horas que deberían ir a lo estratégico.
3. El nivel de partida es de principiante: manejan la IA a título personal, sin método ni eficiencia.
4. El análisis de datos y el envío de reportes se hacen a mano, con poca capacidad de escalar.
5. Cada área enfrenta un reto distinto (pauta, cuentas, RRHH) que un curso genérico no resuelve.

## Estructura del proyecto — kick-off + 3 formaciones

El cliente pidió expresamente una sesión previa de levantamiento con los líderes, porque aunque cada área tiene claras sus carencias, saben que hay brechas que se les escapan. Por eso el proyecto arranca con un **kick-off conjunto (Sesión 01)** con los líderes de las 3 áreas, y luego cada departamento recorre su propia ruta de nivelación → profundización.

- **Sesión 01 · Kick-off** — con los líderes de las 3 áreas, antes de que arranque cualquier formación.
- **Sesión 02 · Formación 1** · Medios Digitales.
- **Sesión 03 · Formación 2** · Cuentas (2 grupos de 15).
- **Sesión 04 · Formación 3** · Talento Humano.

### Formación 1 · Medios Digitales
- **Participantes**: 6.
- **Foco**: ingeniería de prompts y optimización de pauta con IA.
- **Objetivo**: prompts avanzados para el día a día; análisis de métricas y rendimiento, segmentación inteligente de audiencias, optimización de ad copy y decisiones basadas en datos para mejorar la eficiencia de presupuestos y campañas.

### Formación 2 · Cuentas (Client Partners, Project Managers)
- **Participantes**: 30, en 2 grupos de 15.
- **Foco**: IA aplicada a la gestión de cuentas y a la productividad de agencia.
- **Objetivo**: reducir a la mitad el tiempo en tareas operativas — automatización de minutas y procesos diarios, generación ágil de pre-briefs de marca, análisis de performance de campañas y reportes de inteligencia de mercado.

### Formación 3 · Talento Humano
- **Participantes**: 4.
- **Foco**: transformación y optimización de RRHH con IA.
- **Objetivo**: aplicar la IA en los subsistemas del área — automatización de filtros de Reclutamiento y Selección (R&S), análisis de datos de compensación y nómina, y estructuración de métricas de evaluación de desempeño.

## Ecosistema y herramientas

- El plan se apoya en el entorno **Google (Gemini)** que la agencia ya usa y suma **Claude**. Intezia orienta sobre licenciamiento; no se afirma migración de stack (§4.11).

## Entregables solicitados

- **Workbook** por formación (pauta / cuentas / RRHH).
- **Informe de desempeño** por equipo.
- **Certificado de participación** INTEZIA.
- Institucionales: manual digital por participante · panel de progreso individual.

## Propuesta económica

- **3 hojas de cotización independientes, una por formación** — requisito explícito del cliente. El deck lleva 3 slides `.s-price`; la primera con campos canónicos (`PrecioBase`, `Descuento`, `PrecioTotal`, `Programa`, `Notas`) y la 2ª/3ª con sufijo `_2`/`_3` (`agregar-campo-precio.py` soporta multi-página de forma nativa). Ventas cotiza cada formación por separado; `PrecioTotal_N` autocalcula base menos descuento por instancia.
- **4ª hoja · Total consolidado**: suma automáticamente los 3 `PrecioTotal` anteriores en `PrecioBase_4` (vía JS añadido por `scripts/robin-agency-cap080-total-calc.py`, tercer paso que corre después del par estándar — nombre sin prefijo `customize-` a propósito, para no chocar con la detección automática de `generar-pdf.sh`), permite un descuento adicional de combo en `Descuento_4`, y `PrecioTotal_4` (fórmula genérica ya existente) calcula el total final. Solo funciona el cálculo en vivo en Adobe Reader (no en Preview), igual que el resto de campos de precio.
- **Orden de regeneración de esta propuesta (3 pasos, no el par estándar)**: `generar-pdf.sh` → `customize-acroforms.py` → `robin-agency-cap080-total-calc.py`.
- Cada formación puede contratarse por separado o en conjunto.

## Notas comerciales

- Pago en Bolívares a tasa BCV.
- Vigencia de la cotización: 30 días.
- Programa registrado como **CAP-080** en INTEZIA Education al cerrar el acuerdo.

## Notas de diseño

- Formato canónico de **17 slides** A4 landscape, clon multi-fase de `pilotes-perforados`, reutilizando `.s-schedule` (una ruta por sesión: kick-off + 3 formaciones) y `.s-orange` en su variante estándar de 3 pilares (Kick-off · Formaciones por área · Entrega y seguimiento).
- Slide `10 · Impacto` con datos de estudios reales: McKinsey (2023), Federal Reserve Bank of St. Louis (2025), ITIF (2025).
- Equipo facilitador por rol (sin nombre propio sin confirmar).
- `[CÓDIGO]` sustituido por CAP-080 en Acreditación.

## Pendientes

- Confirmar facilitador asignado.
- Confirmar líderes referentes por departamento y sus datos de contacto.
- Confirmar fechas de inicio/cierre y si las 3 formaciones corren en simultáneo.
- Orientación final de licencias (Gemini y/o Claude).
