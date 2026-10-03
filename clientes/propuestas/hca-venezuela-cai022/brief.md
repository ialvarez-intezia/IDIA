# Brief — HCA Venezuela · Sesión de prueba (CAI-022)

## Datos administrativos

- **Empresa**: HCA Venezuela (Hubbard College of Administration)
- **Sector**: Consultoría y formación gerencial, con área de Academia/Performance propia.
- **Slug**: `hca-venezuela-cai022` (verificado con `ls` antes de clonar — ya existen
  `hca-venezuela-cap015/` y `hca-executive-ai-mastery/` para el mismo cliente/aliado, sin
  relación directa con esta propuesta).
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades` — construcción de una skill puntual, en una sola
  sesión. Código `CAI-` asignado directamente por el usuario.
- **Tipo de documento**: Capacitación In-Company (`CAI-022`) · 1 sesión de 2h, modalidad
  online síncrono. **Sin hoja de cotización** — instrucción explícita del usuario: esta es
  una sesión de prueba del servicio, no una cotización cerrada.
- **Eje temático**: Construcción de skills en Claude conectadas a las bases de Google Sheets
  del área de consultoría, para automatizar los informes que hoy se cuentan a mano.
- **Fecha del brief**: 2026-09-18
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de las notas de preparación del usuario para una sesión de
prueba de 2 horas con HCA Venezuela ("Solución Propuesta para la Sesión de 2 Horas" +
"Cuellos de Botella Identificados"), sin ficha de levantamiento formal independiente — HCA
Venezuela ya es cliente conocido del sistema (ver `hca-venezuela-cap015/`, CAP-015, Claude
Cowork Dominio Corporativo, 2026-05-05).

## Decisiones confirmadas con el usuario (2026-09-18)

Antes de construir, se preguntó y se confirmó:

1. **Alcance de las 2 horas**: la sesión construye, en vivo, **solo** las skills de reportes
   operativos del área de consultoría (informes de consultorías entregadas, nómina, deudas,
   sesiones restantes), conectadas a Google Sheets. **No se construye en vivo** el hilo de
   Marketing/MCP para redes sociales de Virginia — se **menciona** cómo funciona la conexión,
   para que Marketing pueda iniciar por su cuenta con el mismo patrón más adelante.
2. **Participantes — recomendación abierta, no lista cerrada**: la propuesta presenta a las
   dos asistentes (consultoría y academia/performance) como participantes clave, porque son
   quienes operarán las herramientas. Se **sugiere** sumar a Melissa (tesorería) y a los
   directores como observadores, para que entiendan el funcionamiento sin operar la
   herramienta — la decisión final de a quién invitar queda en manos de HCA.
3. **Modalidad**: Online síncrono (videollamada).
4. **Framing de "sesión gratuita"**: se mantiene **implícito**. El deck no dice "gratis",
   "cortesía" ni menciona que después se evaluará una propuesta más amplia — simplemente no
   hay hoja de cotización, sin explicar el porqué en el documento.

## Nombres reales — omitidos del deck, por precedente del propio cliente

El usuario nombró directores y responsables específicos (Bellatrix, Virginia, Alberto,
Melissa) y dos asistentes sin nombrar. **Se decidió no nombrar a ninguna persona específica
en el deck** (sí quedan aquí, en este brief, como contexto interno) — se refiere a roles
genéricos: "el área de consultoría", "el área de academia/performance", "el equipo de
tesorería", "los directores", "Marketing". Esta decisión sigue el precedente ya documentado
para este mismo cliente en `hca-venezuela-cap015/brief.md`: *"Sin nombre del cliente
referente en el deck: la propuesta apela a HCA Venezuela como organización; el referente
interno se gestiona en la conversación comercial"* — decisión explícita del cliente en esa
propuesta anterior. No se volvió a preguntar en esta ocasión porque es el mismo cliente y el
mismo patrón de discreción; **si el usuario prefiere nombrar a las personas en este deck
puntual, es reversible.**

## Contexto — cuellos de botella por área (todos, aunque las 2h solo resuelven consultoría)

1. **Consultoría (entrega)**: seguimiento manual en Excel por consultor, empresa y agenda
   semanal. Informes semanales contados a mano: consultorías entregadas, nómina, sesiones
   acumuladas, deudas, recompras. Alto margen de error y tiempo excesivo en el cálculo de
   nómina. **Este es el foco de la sesión de 2h.**
2. **Academia**: seguimiento de estudiantes por sede (Maracay, Valencia, Caracas),
   completaciones, puntos y pagos a supervisores — manual.
3. **Performance**: ciclos de reclutamiento, evaluaciones de candidatos, licencias activas —
   sin sistematizar.
4. **Tesorería**: conciliaciones bancarias, clientes en deuda, comisiones — todo manual.
5. **Directores**: necesitan información integrada (estado de servicios, pagos y nómina) en
   un solo lugar, sobre todo para el plan de ingresos semanal que se presenta los viernes y
   requiere seguimiento diario.

Los puntos 2-5 se usan como contexto de diagnóstico (por qué HCA necesita esto en general),
no como alcance cotizado de esta sesión — "omitir, no inventar" aplicado a cualquier detalle
de esas áreas que no esté confirmado.

## Solución de la sesión (Bloque C)

- **Enfoque**: construcción de una skill en Claude conectada a las bases de Google Sheets de
  consultoría. La skill genera el informe automático: consultorías entregadas, nómina,
  deudas, sesiones restantes.
- **Por qué importa**: reemplaza el conteo manual y reduce el margen de error, apoyado en la
  capa de razonamiento avanzado de Claude. (No se afirma una cifra exacta de "99.9%" sin
  fuente verificable — ver nota abajo.)
- **Entregables**: workbook con el paso a paso, generador de skills y prompts para que HCA
  replique el proceso sin depender de Intezia, y una guía breve de cómo aplicar el mismo
  patrón de conexión en Marketing.

### Nota sobre la cifra "~99.9%" de reducción de margen de error

El usuario mencionó una reducción de margen de error "a ~99.9%" con la capa avanzada de
Claude. **No se incluyó esa cifra exacta en el deck** — no hay una fuente externa verificable
que la respalde (§4.9 exige estudios reales y citables para la slide de Impacto, y esto no es
una cifra de estudio sino una proyección interna). En su lugar, la slide de Impacto usa datos
reales y citables sobre el problema que se resuelve (errores en hojas de cálculo manuales) y
sobre la ganancia de productividad con asistentes de IA — ver sección Impacto abajo. Si el
usuario quiere sostener la cifra 99.9% verbalmente en la sesión (no en el documento), es una
decisión de venta en vivo, no del deck.

## Impacto (§4.9) — datos reales verificados por WebSearch

- **Panko — "What We Know About Spreadsheet Errors"** (revisión de 13 estudios de hojas de
  cálculo operativas, 1995-2004): 94% de las hojas de cálculo estudiadas (88 en total) tenía
  al menos un error; tasa promedio de error por celda de 5.2% en las hojas revisadas. Conecta
  directo con el seguimiento manual en Excel de HCA.
- **Microsoft — Work Trend Index 2024** ("What Can Copilot's Earliest Users Teach Us About
  Generative AI at Work?"): 77% de los usuarios de un asistente de IA reportó un aumento
  medible de productividad; 29% más rápidos en búsqueda, redacción y resumen. Ya usado en
  otras propuestas de este sistema (mismo estudio, mismo eje temático de productividad con
  IA) — no se reinventa la cita.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: María Iribarren (misma "María" que aparece como asesora comercial
  en el resto del sistema — se asume la misma persona salvo corrección del usuario).

## Pendientes

- Confirmar fecha y hora de la sesión online.
- Confirmar con HCA a quién finalmente invitan (recomendación queda abierta en el deck).
- Confirmar si el usuario quiere nombrar a personas específicas en una versión futura de
  este deck (por ahora, roles genéricos — ver sección arriba).
