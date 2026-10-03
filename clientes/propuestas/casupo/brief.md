# Brief — Casupo · Auditoría de Procesos Internos con IA (CAP-108)

## Datos administrativos

- **Cliente**: Casupo
- **Slug**: `casupo`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación in-company · proyecto de **2 fases**: Fase 1 (Auditoría, cotizada en esta propuesta) + Fase 2 (Capacitación, plan abierto)
- **Programa**: Auditoría de Procesos Internos con IA
- **Eje temático**: automatización de procesos internos del equipo (administrativos y operativos) con IA — **excluye deliberadamente el área creativa** (diseño, video), donde Casupo mantiene el enfoque humano de cara a sus clientes
- **Fecha del brief**: 2026-08-17
- **Estado**: `Borrador`

## Contacto

- **Cliente referente**: Luis, uno de los dueños de Casupo. Conoce bien el potencial de la IA; gran parte de su propia operatividad ya la resuelve apoyándose en IA.
- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
- **Consultor / Facilitador**: NO se asigna en la propuesta inicial — INTEZIA designa un consultor senior al confirmar el kick-off.

## Por qué este proyecto

Casupo ya tiene liderazgo con criterio sobre IA: Luis conoce su potencial y ya la usa activamente en su propia operatividad. Pero esa adopción no ha bajado al resto del equipo con ningún criterio común. Hace unos meses intentaron adquirir licencias corporativas de herramientas de IA y el proceso no se concretó; hoy cada persona usa IA por su cuenta, de forma aislada, con niveles de conocimiento distintos entre sí (algunos más avanzados que otros, pero todos con algo de experiencia).

Casupo no quiere apurar pasos: ve a Intezia como un aliado de largo plazo, no como una implementación de una sola vez. Por eso primero quiere auditar antes de capacitar: entender qué procesos son automatizables, en qué orden y con qué nivel de esfuerzo y riesgo, antes de decidir cómo capacitar a su equipo.

## Diagnóstico (5 puntos)

1. El liderazgo de Casupo (Luis) conoce bien el potencial de la IA y ya la usa activamente en su propia operatividad diaria.
2. Hace unos meses intentaron adquirir licencias corporativas de herramientas de IA, pero el proceso no se concretó.
3. Hoy cada persona del equipo usa IA por su cuenta, de forma aislada y sin un criterio común, con niveles de conocimiento distintos entre sí.
4. La prioridad son los procesos internos del equipo (administrativos y operativos): el área creativa (diseño, video) mantiene, de forma deliberada, el enfoque humano de cara a los clientes de Casupo.
5. Casupo prefiere pasos firmes y seguros: busca un aliado de largo plazo, no una implementación de una sola vez.

## Estructura del proyecto (acordada con el cliente)

### Fase 1 · Auditoría — la única fase que se cotiza en esta propuesta

- **Modalidad**: presencial, en las oficinas de Casupo.
- **Audiencia**: los 4 líderes de la organización.
- **Objetivo**: levantar los procesos internos del equipo y priorizar qué es automatizable, en qué orden y con qué nivel de esfuerzo y riesgo.
- **Alcance**: no se fija de antemano. Casupo ya intuye algunos procesos con potencial (ej. el análisis de las cuentas de cada cliente, que le toma mucho tiempo a sus líderes de proyecto; el envío y análisis de correos; la redacción; tareas manuales del área administrativa), pero esto se **confirma y profundiza durante el levantamiento mismo**, no se cierra hoy.
- **Estimado de sesiones (pedido explícito de Luis)**: 4 sesiones individuales, una por cada líder de área, de **2 horas cada una** (≈8 horas en total) como punto de partida. Se deja explícito en la propuesta que el número y la duración de las sesiones **puede variar según la complejidad de los procesos** y la información que se levante en el camino — Luis necesita saber cuánto tiempo le pide a su equipo, sin comerse la agenda de sus 4 líderes sin límite.
- **Sin mención de herramientas**: esta propuesta no recomienda ni nombra ninguna herramienta de IA. La recomendación de ecosistema es un resultado de la Fase 1, no un punto de partida.

### Fase 2 · Capacitación — plan abierto, no cotizado en esta propuesta

- Se estructura con base en los insights que resulten de la Fase 1.
- **Se cotiza después de completada la Fase 1** — pedido explícito del cliente, no se cotiza junto con la Fase 1.
- Su alcance, formato y módulos se definen a partir de lo que arroje la auditoría.

## Especificaciones del programa

- **Duración**: Fase 1 · estimado inicial de 4 sesiones de 2h (≈8h), variable según complejidad. Fase 2: sin horas impuestas, a definir tras la auditoría.
- **Modalidad**: Fase 1 presencial, en las oficinas de Casupo.
- **Audiencia**: los 4 líderes de la organización de Casupo.
- **Acreditación**: constancia de participación INTEZIA Education.

## Entregables consolidados

- Plan de priorización de procesos automatizables (esfuerzo y riesgo, orden recomendado).
- Informe de auditoría de los procesos internos levantados con los 4 líderes.
- Alcance definido para la Fase 2 (Capacitación) — cotizada aparte.
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-108** en INTEZIA Education al cerrar el acuerdo.
- **Solo se cotiza la Fase 1 (Auditoría).** La Fase 2 (Capacitación) se cotiza por separado, después de completada la Fase 1, según pedido explícito del cliente.

## Notas de diseño

- Clonado de `pilotes-perforados/` (CAP-021) — patrón CLAUDE.md §6 para "Taller/Capacitación multi-fase con roadmap de 2 etapas (caso puntual sin fase de construcción propia)": Casupo no separa una fase de construcción propia, la Fase 2 completa se define a partir de la Fase 1.
- **Roadmap simplificado a 2 nodos** (no fork/merge de sesiones ni 3 etapas): Fase 1 · Auditoría → Resultado (Plan de priorización), con nota de que la Fase 2 se cotiza aparte. No se forzó un fork de 4 rutas (una por líder) para no artificializar contenido que aún no existe — las 4 sesiones son homogéneas en método (entrevista individual), no en área temática conocida de antemano.
- **Sin slide de Mapa de Calor con datos de ejemplo**: a diferencia de `pilotes-perforados/`, no se incluyó la slide `.s-heatmap` porque mostraría procesos y herramientas inventadas antes de que exista el levantamiento real — se prefirió mantener el entregable mencionado en Beneficios/Roadmap sin tabla de ejemplo.
- **Cotización progresiva**: `pilotes-perforados/styles.css` es anterior al patrón `.cot-terms-box`/`.cot-progressive` (estándar desde `aerocentro/`, 2026-07-23) — se portaron esas reglas CSS desde `corporaciones-easyaccess/styles.css` (posiciones correctas: `cot-validity` 504px, `cot-progressive` 528px, `cot-terms-box` 556px — sin el bug de colisión de `fasto/`, ver memoria `bug-cot-progressive-terms-box-collision`).
- **Sin nombres de herramientas de IA en todo el deck** (pedido explícito): ni en diagnóstico, ni en roadmap, ni en programa. La única mención genérica es "herramientas de IA" al describir el intento fallido de licencias corporativas y el uso aislado actual.
- **Asesora comercial**: Flavia Martínez (misma que en `pilotes-perforados/`).
- Slide de Impacto con datos reales de McKinsey, fuente citada verbatim (§4.9): *The economic potential of generative AI: The next productivity frontier* (2023) y *Agents, robots, and us: Skill partnerships in the age of AI* (McKinsey Global Institute, 2025).

## Pendientes

- Confirmar fechas y calendario de las 4 sesiones de Auditoría.
- Confirmar nombres/cargos de los 4 líderes de la organización.
- Confirmar presupuesto indicativo de la Fase 1.
- Asignar consultor/facilitador senior al cerrar el acuerdo.
