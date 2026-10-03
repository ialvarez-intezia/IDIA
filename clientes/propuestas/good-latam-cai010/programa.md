# Documento Oficial de Diseño Curricular e Instruccional

**[LOGO INTEZIA — `logos/educacion/NEGRO.png`]**  /  **[LOGO Good Latam]**

# Capacitación In-Company
## Administración + Digital — Fundamentals, Auditoría y Automatización con IA

**Código**: CAI-010
**Versión**: Propuesta fusionada (Administración + Digital, cotización única)
**Elaborado por**: Coordinación INTEZIA · Dirección de Productos y Servicios
**Fecha de elaboración**: 2026-09-09 (fusiona el contenido ya diseñado de CAP-109/Administración
y de la CAI-010 original/Digital, entonces llamada "Creación")

---

## 1. Información general

- **Servicio**: Habilidades — capacitación in-company, con una etapa interna de auditoría
  antes de construir (patrón ABR "diagnóstico antes de construir") en ambas áreas.
- **Cliente**: Good Latam, agencia de marketing.
- **Alcance**: **2 áreas, un solo programa y un solo monto**: Administración y Digital.
  Compras queda fuera del alcance de este documento.
- **Herramientas**: Gemini (ya en uso por el cliente, sin cambio de herramienta) + Google AI
  Studio (asistentes de texto de Digital) + Google Apps Script (automatización de sistema de
  Digital) + Basecamp (herramienta ya en uso de Digital, API sujeta a confirmación de acceso).
- **Duración**: Administración 5 sesiones/10h + Digital 4 sesiones/8h = **9 sesiones, 18
  horas académicas totales**.
- **Modalidad**: Híbrida.

---

## 2. Planteamiento de la necesidad

Good Latam quiere **escalar la operación con IA en lugar de contratar más personal**, y
Administración y Digital son las dos áreas listas para avanzar ahora mismo, cada una desde su
propio punto de partida:

- **Administración** (hoy sobre Excel y sistemas desactualizados como Profit) es la que menos
  contacto directo tiene con la IA — antes de auditar y automatizar sus procesos, necesita
  perder el temor y entender cómo funciona.
- **Digital** ya documentó su proceso de grillas paso a paso: 12 pasos, desde la configuración
  del cronograma hasta la aprobación final del cliente, sobre Basecamp y Google Sheets. Gran
  parte de ese proceso es coordinación repetitiva (armar carpetas, subir contenido, notificar,
  traducir feedback en tareas) que se rehace a mano cada mes. No todo es automatizable: la
  redacción y el diseño siguen siendo trabajo creativo del equipo, y 3 puntos de aprobación
  (revisión de contenido, revisión final interna, revisión del cliente) son gates de calidad
  que dependen de criterio humano.

## 2.1 Enfoque pedagógico (Modelo INTEZIA)

Aprendizaje Basado en Retos (ABR) — tres pilares, aplicados en cada área sobre sus propios
casos:

- **Tutoría activa**: el consultor conduce cada sesión con feedback en tiempo real sobre los
  procesos reales de cada área, no un formato genérico.
- **Nivelación antes de construir**: Administración recibe Fundamentals de IA antes de que se
  toquen sus procesos; Digital ya tiene el proceso mapeado, así que su nivelación ocurre
  dentro de la misma primera sesión (Módulo I).
- **Transferibilidad inmediata**: cada ejercicio se hace sobre el trabajo real del área. Lo
  que se practica en sesión queda funcionando.
- **Curaduría de contenidos**: solo lo que cada área va a usar, sin teoría desconectada.

---

## 3. Objetivos

### 3.1 Objetivo general

Formar a Administración en los fundamentos de la IA y construir la automatización priorizada
de sus procesos, y auditar y automatizar el proceso real de grillas de Digital con Gemini y
Google Workspace, para que Good Latam escale su operación con IA.

### 3.2 Objetivos específicos

1. Formar a Administración en los fundamentos de la IA: qué es, cómo funciona y cómo mejora
   su trabajo diario.
2. Auditar los procesos, tareas manuales y nivel de adopción de IA de Administración, y
   construir la automatización priorizada a la medida de sus procesos reales.
3. Automatizar la configuración inicial del proceso de grillas de Digital (documento,
   carpetas, cronograma) y construir con Gemini un asistente de redacción que acelere el
   primer borrador, sin reemplazar el criterio editorial del equipo.
4. Conectar Basecamp en un solo flujo de Digital (carga, notificación, actualización de
   estado) con Google Apps Script, sujeto a la disponibilidad de su API, y estructurar el
   feedback del cliente en tareas accionables con un asistente de Google AI Studio.

> Cada específico responde al objetivo general → al perfil de egreso de su área → al
> planteamiento de la necesidad.

---

## 4. Perfiles académicos

> **Capacitación In-Company**: no exige Perfil de ingreso. Administración no requiere
> conocimiento previo de IA — el programa lo cubre desde cero con Fundamentals. Digital
> parte de su propio proceso ya documentado.

### Perfil de egreso · Administración

- **Saber**: entiende qué es la IA, cómo funciona y cómo aplicarla a su trabajo diario.
- **Saber hacer**: opera con una automatización construida a la medida de sus procesos
  reales, priorizada durante su propia auditoría.
- **Saber ser**: usa la IA con criterio propio, sin depender de Intezia para seguir
  escalando.

### Perfil de egreso · Digital

- **Saber**: distingue Gemini, Google AI Studio y Google Apps Script, y qué herramienta usar
  en cada paso de su proceso de grillas.
- **Saber hacer**: opera un proceso de grillas conectado de punta a punta, con asistentes de
  redacción y de estructuración de feedback ya construidos.
- **Saber ser**: mantiene el criterio editorial y los puntos de aprobación humano, usando la
  IA para acelerar lo repetitivo, no para reemplazar el juicio creativo.

---

## 5. Estructura curricular y diseño instruccional

### 5.1 Estructura modular · Administración (2 módulos · 5 sesiones · 10h)

| Módulo | Objetivo Instructivo | Temas | Elaboración (Trabajo del equipo) |
|---|---|---|---|
| **I: Fundamentals** | Explica qué es la IA, cómo funciona y cómo mejora el trabajo diario, sin asumir ninguna herramienta todavía. | 1.1 Qué es la IA y cómo funciona<br>1.2 IA aplicada a tareas administrativas<br>1.3 Automatización sin perder el control<br>1.4 Casos propios del área | El equipo trae ejemplos reales de sus tareas en Excel y Profit para trabajarlos en sesión. |
| **II: Auditoría + Desarrollo** | Con los fundamentos cubiertos, mapea los procesos contables/administrativos y construye la automatización priorizada. | 2.1 Procesos contables en Excel y Profit<br>2.2 Automatización del flujo priorizado<br>2.3 Validación con casos reales<br>2.4 Entrega funcional | El equipo describe sus procesos, valida qué ya usa y prueba la automatización sobre sus propios cuadros. |

### 5.2 Desglose instructivo · Administración

| M | Sesión(es) | Temas y subtemas | Tiempo | Estrategias de enseñanza | Estrategias de aprendizaje | Recursos y entornos |
|---|---|---|---|---|---|---|
| I | Sesión 1-2 (2×2h) | Tema 1: Fundamentals<br>1.1-1.4 | 4h (explicación guiada, demostración en vivo sobre Excel/Profit, práctica con ejemplos, preguntas) | Explicación guiada sin jerga técnica, demostración en vivo, casos aplicados al área | El equipo identifica tareas donde la IA puede ayudar, practica con ejemplos guiados | Guía Fundamentals de IA Intezia, ejemplos con datos reales, Google Meet |
| II | Sesión 3-5 (3×2h) | Tema 2: Auditoría + Desarrollo<br>2.1-2.4 | 6h (Sesión 1: entrevista y auditoría · Sesiones 2-3: construcción guiada) | Entrevista con guion de auditoría, construcción guiada de la automatización | El equipo describe su proceso, prueba y ajusta la automatización, se queda con una herramienta lista | Guion de auditoría Intezia, cuadros y documentos reales, Google Meet |

### 5.3 Estructura modular · Digital (4 módulos · 4 sesiones · 8h)

Fuente: documento de proceso real "GOOD _ PROCESO DE GRILLAS.pdf" (12 pasos, Basecamp +
Google Sheets). Clasificación usada para diseñar el programa: automatizables de punta a
punta (pasos 1, 6, 7, 9, 11, 12), asistibles con IA sin reemplazar criterio humano (pasos 2,
4, 10), puntos de aprobación 100% humanos (pasos 3, 5, 8, no se automatizan).

| Módulo | Título | Pasos del proceso que cubre | Duración |
|---|---|---|---|
| I | Diagnóstico y Fundamentals aplicados | Mapeo de los 12 pasos, qué se automatiza vs. qué queda humano | 2h |
| II | Arranque automatizado + redacción con Gemini | Pasos 1 (config. inicial) y 2 (redacción, asistida) | 2h |
| III | Automatización de Basecamp | Pasos 6, 7, 11, 12 (comparten el mismo sistema) | 2h |
| IV | Feedback estructurado + integración final | Paso 9 (feedback) + integración de las 3 automatizaciones anteriores | 2h |

### 5.4 Desglose instructivo · Digital

- **Sesión 1 (Módulo I)**: 30' revisión del proceso paso a paso, 45' fundamentos de Gemini y
  Google Apps Script aplicados a coordinación, 30' qué se automatiza vs. qué queda humano,
  15' cierre y plan.
- **Sesión 2 (Módulo II)**: 45' construcción guiada del flujo de arranque con Google Apps
  Script, 45' construcción del asistente de redacción en Google AI Studio con la voz de marca,
  20' prueba con un caso real, 10' cierre.
- **Sesión 3 (Módulo III)**: 60' conexión de Google Apps Script a Basecamp (API o alternativa
  asistida), 40' automatización de carga y notificación al cliente, 20' automatización de
  estado y aprobación.
- **Sesión 4 (Módulo IV)**: 40' asistente en Google AI Studio que estructura el feedback en
  tareas, 50' integración de las automatizaciones en un solo flujo, 30' prueba de punta a
  punta y plan de continuidad.

---

## 6. Garantía de calidad y mejora continua

- **Construcción curricular**: el programa se adapta a los procesos reales de Administración
  (Excel, Profit) y de Digital (proceso de grillas, Basecamp, Google Sheets).
- **Encuesta de satisfacción**: monitoreo de la experiencia al cierre de cada módulo.
- **Entregables**: automatización a la medida de Administración + informe de auditoría del
  área + Administración formada en Fundamentals de IA; proceso de grillas de Digital
  conectado de punta a punta + asistentes de redacción y feedback en Google AI Studio.
  Certificado de participación INTEZIA para ambas áreas.
- **Beneficio del programa formativo**: al finalizar, Good Latam tiene dos áreas operando con
  automatizaciones propias — Administración con fundamentos y una herramienta a la medida,
  Digital con su proceso de grillas conectado de punta a punta — sin depender de Intezia para
  seguir escalando.

---

## 7. Perfil del equipo facilitador

- **Ambas áreas**: facilitadas por un consultor Intezia con dominio de fundamentals de IA,
  auditoría de procesos y desarrollo de automatizaciones sobre Google Workspace (Gemini,
  Google AI Studio, Google Apps Script).
- **Asesora comercial**: Verónica Rubio.
- **Competencias pedagógicas**: facilitación introductoria sin base técnica (Fundamentals de
  Administración), entrevista de auditoría, construcción guiada de automatizaciones,
  feedback con lista de cotejo.
