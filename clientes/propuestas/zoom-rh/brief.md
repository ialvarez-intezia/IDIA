# Brief — Zoom · Gestión Humana

---

## Datos administrativos

- **Empresa**: Zoom (Gestión Humana: 4 áreas independientes)
- **Sector**: Servicios / corporativo
- **Slug**: `zoom-rh`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-050`, Fase 2 Zoom) · **5 formaciones en
  una sola propuesta** (multi-track, patrón `zoom-comercial/` CAP-058, extendido a 5 tracks):
  Compensación y Beneficios · Estadística Organizacional · Seguridad y Salud Laboral (SSL) ·
  Selección · Capacitación. Cada área ve su formación por separado. Las 5 son uniformes: 2
  módulos / 1 sesión / 4 horas cada una (a pedido explícito del cliente, 2026-08-17).
- **Eje temático** (por track):
  - **Compensación y Beneficios**: consolidación de la evaluación 360°, redacción de cartas de
    resultados con Generación de Lenguaje Natural (NLG) y notificaciones masivas
    personalizadas, con Gemini.
  - **Estadística Organizacional**: Maestro de Datos, validación de expedientes de onboarding,
    descriptivos de cargo desde la entrevista grabada y organigramas vivos, con Gemini.
  - **Seguridad y Salud Laboral (SSL)**: análisis de evidencia fotográfica de inspección,
    generación de riesgo por cargo con sustento normativo y control de vencimientos legales,
    con Gemini.
  - **Selección, Evaluación y Potencial**: traducción de informes técnicos a lenguaje de
    negocio, estandarización por familia de cargo y Gap Analysis para desarrollo, con Gemini.
  - Las 4 formaciones comparten stack (Google Workspace + Gemini + Gems + NotebookLM) y la
    regla transversal de la ruta Zoom: ningún Gem decide sobre personas.
- **Fecha del brief**: 2026-07-28 (reconstruida como multi-track de 4 áreas el 2026-08-17)
- **Estado**: propuesta en formato canónico (deck HUD, patrón multi-track de `zoom-comercial/`),
  sin slide de precio

## Contacto

- **Asesora de ventas**: María Iribarren — +58 414 0570056 — miribarren@intezia.com

## Necesidad detectada

Gestión Humana de Zoom no es una unidad homogénea: son 4 áreas con procesos manuales propios,
detectados en reuniones de diagnóstico por área (2026-08-17):

- **Compensación y Beneficios**: un equipo de 3 personas gestiona el ciclo de vida de 1.200
  empleados (relación 1:400). La evaluación 360° corre por Google Forms (10-15 evaluadores por
  persona, 7 competencias, ponderación por objetivos de cargo, datos segmentados en pestañas
  por grupo). El mayor cuello de botella es la carta de resultados: redacción narrativa manual
  por cada persona, más el envío manual de más de 500 correos informativos.
- **Estadística Organizacional**: sostiene el Maestro de Datos nacional en Google Sheets
  (fuente de la verdad de la organización, actualización semanal de ingresos y egresos). Es un
  equipo *power user* (fórmulas y extensiones avanzadas). El mayor retrabajo está en el
  onboarding: revisión manual de expedientes (cédulas, títulos, referencias) enviados desde
  sucursales, y la redacción manual de descriptivos de cargo tras cada entrevista.
- **Seguridad y Salud Laboral (SSL)**: usa Google Forms como checklist de inspección nacional
  (sucursales reportan estatus y adjuntan fotos), pero debe descargar cada imagen a mano para
  verificar el reporte. La generación de notificaciones de riesgo por cargo (físico, químico,
  ergonómico) es manual, igual que el control de vencimientos legales (elecciones de
  delegados, comités, trámites ante la Inspectoría), donde un plazo vencido es multa.
- **Selección, Evaluación y Potencial**: los informes técnicos de evaluación de candidatos son
  extensos y técnicos; el equipo hace *copy-paste* de resultados que los supervisores no saben
  interpretar, generando decisiones por prejuicio. No hay plantillas diferenciadas por familia
  de cargo (un analista, un gerente, un chofer y un vigilante no se leen igual), y el análisis
  para promociones internas no cruza sistemáticamente las funciones del cargo con los
  resultados de la persona.

Esta Fase 2 abre **4 formaciones independientes**, una por área, cada una con protocolo de
protección de datos y una regla explícita de decisión humana sobre las personas.

## Especificaciones del programa

- **Duración**: 5 formaciones × 4 horas (1 sesión × 4 horas) cada una = 20 horas académicas
  totales. No son fases secuenciales: se dictan a cada equipo por separado, en simultáneo o
  escalonadas.
- **Modalidad**: In-Company (sin afirmar presencial/online).
- **Audiencia**: equipo de cada área (Compensación y Beneficios · Estadística Organizacional ·
  Seguridad y Salud Laboral · Selección, Evaluación y Potencial) de Zoom.
- **Stack**: Google Workspace + Gemini + Gems + NotebookLM (las 4 formaciones). **Sin
  herramientas de desarrollo ni de automatización por código** (ver restricciones abajo).

## Equipo asignado

- **Facilitación**: Equipo Education (genérico, sin nombres, consistente con el resto de la
  ruta Zoom).

## Restricciones explícitas del cliente (2026-08-17) — bloqueantes para esta propuesta

El usuario indicó tres límites de contenido, aplicados a las 5 formaciones:

1. **Sin desarrollo ni herramientas de código**: ningún módulo enseña ni menciona AppSheet,
   n8n, Apps Script, APIs (p. ej. "Gemini API") ni ninguna otra herramienta de automatización
   por código. Todo el uso de IA queda dentro de la capa **sin código** de Gemini nativo en
   Google Workspace (Sheets, Docs, Drive, Meet), Gems y NotebookLM — igual que el resto de la
   ruta Zoom. Esto recorta directamente el material fuente de Estadística Organizacional
   (n8n/AppSheet, "Gemini API + Drive + Forms", control de versiones automático de
   organigramas) y de SSL (Apps Script para el tablero de vencimientos): se reformulan como
   uso directo de Gemini multimodal en Drive/Docs y tableros en Sheets con alertas redactadas
   por Gemini, revisadas por el equipo, no disparadas por script.
2. **Sin cálculo de nómina ni contenido salarial**: el eje de Compensación y Beneficios se
   enfoca en el **ciclo de evaluación de desempeño y su comunicación** (evaluación 360°,
   redacción de cartas de resultados, notificaciones masivas), no en analítica salarial,
   auditoría de fórmulas de nómina ni equidad de compensación. El material fuente original
   mencionaba "ajustes salariales" y "auditoría de anomalías salariales"; se generalizó a
   "resultados de evaluación" en todo el deck para no tocar nómina.
3. **Sin pruebas psicométricas**: el track de Selección, Evaluación y Potencial no nombra
   psicometría, pruebas psicométricas ni herramientas de psicometría (el material fuente
   mencionaba una herramienta específica de pruebas técnicas). Se generalizó a "informes
   técnicos de evaluación de candidatos" y "resultados de evaluación de la persona", que
   sostienen igual el problema real (lenguaje técnico sin traducir, sin estandarizar por
   familia de cargo) sin nombrar el instrumento de origen.

## Notas internas — reconstrucción como multi-track de 5 áreas (2026-08-17)

- **Reemplaza la Fase 2 enviada el 2026-07-28** (3 módulos genéricos de RRHH: Analítica
  Salarial y Protección de Datos · Screening y Gestión Documental · Gems de RRHH con Criterio
  Humano). Esa versión trataba a Gestión Humana como una sola unidad; el diagnóstico por área
  del 2026-08-17 mostró procesos independientes con volumen propio que no cabían con
  profundidad en un solo programa de 4 horas. Se reconstruyó como formaciones separadas
  (patrón multi-track con currículo interno completo, tomado de `zoom-comercial/` CAP-058 §
  *variante — track con currículo interno completo*), en dos pasadas el mismo día:
  1. Primera pasada: 4 tracks (Compensación y Beneficios, Estadística Organizacional, SSL con
     4 módulos/2 sesiones/8h cada uno; Selección/Evaluación/Potencial con 4 módulos/8h).
  2. **Ajuste final del usuario**: (a) separar Selección de Evaluación/Potencial en dos tracks
     propios, **Selección** (con filtrado de CVs agregado como tarea, más el contenido de
     descriptivos/guías/entrevista grabada/Gem de apoyo del PDF legacy de Fase 2) y
     **Capacitación** (Gap Analysis, plan de capacitación, criterio humano); (b) uniformar
     **las 5 formaciones a 2 módulos / 1 sesión / 4 horas cada una** — Compensación y
     Beneficios, Estadística Organizacional y SSL se comprimieron de 4 módulos/2
     sesiones/8h fusionando pares de módulos (ver `programa.md` §5.1 para el mapeo exacto de
     qué subtemas se fusionaron en cada módulo condensado).
- **Puntos transversales de la ruta Zoom**, replicados en las 5 formaciones:
  - **Reto IA ZOOM**: cierre del último módulo de cada track (presentación cruzada de 3
    minutos).
  - **Expectativas realistas sobre los Gems**: sin lenguaje de autonomía; un Gem traduce o
    consolida información, la decisión sobre una persona (ascensos, evaluación, notificaciones
    de riesgo) la toma siempre el equipo humano.
  - **Medición de tiempo ahorrado (antes/después, 30 días)**: línea base en el Paso 03 de
    "Cómo arrancamos" + remedición a los 30 días, en las 5 formaciones.
  - **Protección de datos por diseño**: cada track expone qué información personal o sensible
    de su propio proceso (identidad en expedientes, evidencia de inspección, informes de
    evaluación) no debe cargarse sin anonimizar a una IA pública.
- **Sin slide de Propuesta Económica**: esta Fase 2 se cotiza dentro del acuerdo marco ya en
  curso con Zoom (mismo criterio que `zoom-comercial/` y `zoom-operaciones/`). Los 8 campos
  AcroForm no económicos siguen siendo obligatorios; los 5 campos de precio no aplican
  (§4.14).
- **Overflow no detectado automáticamente**: al comprimir contenido en los cronogramas de 1
  sesión, listas de "Estrategias de enseñanza" demasiado largas empujaban el `.foot` fuera de
  vista sin que `verificar-overflow.js` lo marcara (colisión interna, no desborde de página
  total) — se corrigió acortando bullets a ≤2 líneas por ítem. Revisar visualmente cualquier
  cronograma nuevo, no solo correr el script.
- Slug `zoom-rh` distinto de `zoom-miami/`, `zoom-comercial/`, `zoom-operaciones/` y `zoom/`
  (Legal, CAP-029): mismo cliente, cursos independientes.
