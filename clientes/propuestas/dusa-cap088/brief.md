# Brief — DUSA · Auditoría de automatización, caso por caso (CAP-088)

## Datos administrativos

- **Cliente**: DUSA
- **Sector**: industrial · bebidas / licores
- **Slug**: `dusa-cap088`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-088`)
- **Naturaleza**: Capacitación in-company · **evaluación caso por caso de dónde Claude puede ayudar a 2 áreas de prioridad alta (Comercial y Finanzas)** cuando Copilot, por ser un asistente genérico, se queda corto. No se promete un agente fijo de antemano: cada caso se audita, se prioriza y se activa (o no) según el resultado de la evaluación. Proyecto de 2 fases: Auditoría diagnóstica → Implementación. Logística y Talento Humano quedan como fase de continuación futura, fuera de este alcance (ver *Decisión de alcance* más abajo).
- **Programa**: Auditoría de automatización, caso por caso — DUSA
- **Eje temático**: identificar y evaluar, caso por caso, dónde Claude puede ayudar a resolver el dolor operativo real de Comercial y Finanzas, complementando el Copilot que DUSA ya usa dentro de Microsoft 365, sobre la base del Manual de Políticas y Gobernanza Ética de IA ya construido en `CAP-087`.
- **Modalidad**: Online síncrono (mismo patrón que `dusa-cap087` y `pago-tronic`; confirmar con Wilmer si cambia).
- **Duración**: ver Estructura del proyecto.
- **Fecha del brief**: 2026-08-03 · **Revisión 2026-08-12** (observaciones confirmadas del cliente, ver *Giro de posicionamiento*) · **Revisión 2026-08-12 (b)** (encuadre caso por caso + Términos y condiciones en cotización, ver *Ajuste de encuadre*) · **Revisión 2026-08-12 (c)** (título de portada corregido, roadmap y cronograma a 3 fases explícitas, construcción principalmente en Copilot, entregables documento semilla y hoja de ruta, ver *Segunda vuelta de encuadre*) · **Revisión 2026-08-12 (d)** (Claude deja de ser protagonista del deck, título de portada sin nombrar herramientas, cotización se acota a Fase 1 · Auditoría, ver *Tercera vuelta de encuadre*) · **Revisión 2026-08-12 (e)** (sin nombres de herramientas en ningún punto de la propuesta, ver *Cuarta vuelta de encuadre*) · **Revisión 2026-08-12 (f)** (cotización sin mencionar Fases 2-3, proceso de auditoría y entregables explicados de forma literal, ver *Quinta vuelta de encuadre*) · **Revisión 2026-08-12 (g)** (cotización vuelve a las 3 fases combinadas, ver *Sexta vuelta de encuadre*) · **Revisión 2026-08-12 (h)** (propuesta enfocada en Fase 1, Fases 2-3 solo como pinceladas, cotización vuelve a ser solo Fase 1, ver *Séptima vuelta de encuadre*).
- **Estado**: `Enviada` (revisión (f) completa y verificada, 2026-08-12; ver `meta.json`)

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414 0570056 · miribarren@intezia.com (asignada 2026-08-12, mismo patrón que `dusa-cap087`) — visible en el cierre del deck (`.end-contact`).
- **Consultor / Facilitador**: NO se asigna en la propuesta inicial — INTEZIA designa un consultor con perfil de automatización de negocio con Claude al confirmar el kick-off.
- **Contacto DUSA**: Wilmer (patrocinador interno; apellido y correo pendientes de confirmar, igual que en `CH-007` y `CAP-087`).

## Giro de posicionamiento (2026-08-12, observaciones confirmadas del cliente)

Esta revisión reemplaza el enfoque original de "Skills y Projects de Claude" por un proyecto de **agentes de IA a medida**, con 3 cambios de fondo confirmados por el cliente:

1. **DUSA está comprometida con Copilot**, exigido por su matriz interna de seguridad/gobierno de TI (integración M365 + seguridad corporativa). Claude **no compite ni reemplaza** ese compromiso — entra a evaluar, caso por caso, las tareas donde Copilot, por ser un asistente genérico, se queda corto (ver *Ajuste de encuadre* más abajo — esta evaluación caso por caso reemplaza la primera redacción, que hablaba de "agente a medida"). **Nunca se afirma que DUSA migra o migrará de Copilot** (§4.11): el deck nombra a Copilot explícitamente y enmarca a Claude como complemento dentro del mismo entorno Microsoft 365 que ya usan.
2. **DUSA ya tiene alfabetización en IA previa** (programa con otro proveedor — el mismo antecedente ya documentado como "Fase 1 de fundamentos, con otro proveedor" en la versión original de este brief). La propuesta **no repite fundamentos**: va directo a lo aplicado (auditoría + evaluación de casos).
3. **Estructura validada con el cliente: proyecto de 2 fases** (no 3 etapas por área como en la versión original):
   - **Fase 1 — Auditoría diagnóstica**: mapeo de los procesos de Comercial y Finanzas → **mapa de calor de oportunidades de automatización con IA** + **generador de prompts de uso inmediato**.
   - **Fase 2 — Implementación**: construcción de **agentes de IA a medida** para esas 2 áreas, con **transferencia de conocimiento** para que DUSA los mantenga de forma independiente (sin depender de que otro equipo lo resuelva).
4. **Cotización por área, no por fase**: 2 hojas de Propuesta Económica separadas — una para Comercial, una para Finanzas — cada una cubriendo sus 2 fases (Auditoría + Implementación) combinadas en un solo total. Antes este deck no llevaba slide de Propuesta Económica; esa instrucción original queda **revertida** por esta revisión.

## Ajuste de encuadre (2026-08-12, segunda vuelta — bloqueante)

El usuario pidió corregir el tono de compromiso del deck: **no decir que Claude va a construir agentes fijos con funciones predefinidas** — el mensaje correcto es que **Claude ayuda en los casos donde Copilot se queda corto, y cada caso se evalúa**, no se promete de antemano.

1. **Ningún deliverable se presenta como un agente ya definido.** Se retira toda frase tipo "construimos un agente con visibilidad de cliente, inventario y cobro" (compromiso cerrado) y se reemplaza por "evaluamos, caso por caso, si Claude puede ayudar con..." (compromiso condicionado al resultado de la auditoría). Las funciones concretas (visibilidad de cliente desde el celular, aprobación con trazabilidad, etc.) se mantienen como **ejemplos ilustrativos de casos candidatos**, nunca como features garantizadas.
2. **Fase 2 pasa de "construcción de un agente a medida" a "evaluación e implementación caso por caso"**: Intezia evalúa cada caso priorizado en el mapa de calor y activa el apoyo de Claude únicamente donde corresponde. El nombre de la fase (`Fase 2 · Implementación`) no cambia, pero su contenido sí: ya no es la construcción garantizada de una herramienta fija.
3. **Terminología**: "agente a medida" (como sustantivo de un entregable fijo) se retira del copy de cara al cliente. Se usa "apoyo de Claude", "caso evaluado", "caso priorizado" — siempre condicionados a la evaluación, nunca como compromiso cerrado.
4. **Mapa de calor**: se resignifica de "qué construye el agente" a "caso a evaluar" — coherente con el encuadre evaluativo (el mapa de calor siempre fue el output de una auditoría, nunca una lista de construcción garantizada).
5. **Términos y condiciones en las 2 hojas de cotización**: se agrega el bloque estándar `cot-terms-box` (mismo patrón que `canguro`, `aerocentro`, `agromundial`, `ioed`) con el enlace institucional a los términos y condiciones de Intezia, en ambas slides `.s-price` (Comercial y Finanzas).

> Caso base de este patrón (evitar compromisos de alcance cerrado antes de auditar): mismo espíritu que §4.11 (no afirmar migración de stack) — aquí se extiende a no afirmar un entregable de producto fijo antes de la evaluación caso por caso.

## Segunda vuelta de encuadre (2026-08-12, tercera revisión — bloqueante)

El usuario pidió una tercera pasada sobre este deck: el título de portada sonaba peyorativo
hacia Copilot, las 3 etapas del proyecto no se veían resaltadas, y faltaban 2 entregables ya
anticipados en el proyecto (documento semilla, hoja de ruta) sin reflejo en el AcroForm de
Entregables.

1. **Título de portada corregido.** "Agentes de Claude para lo que Copilot no cubre" posicionaba
   a Copilot como algo insuficiente por defecto (además de contradecir el punto 3 del *Ajuste de
   encuadre* arriba, que retira "agente(s) a medida" del copy — la portada original seguía
   usando "Agentes de Claude"). Nuevo h1: "Claude, junto a Copilot, caso por caso" — nombra el
   programa real, sin restarle valor a Copilot.
2. **Roadmap y cronograma vuelven a 3 fases explícitas y resaltadas**: Fase 1 · Diagnóstico →
   Fase 2 · Construcción (Intezia) → Fase 3 · Implementación. Esto revierte la reducción de 3 a
   2 etapas hecha en la revisión (b) — aquí el pedido es el opuesto: dejar las 3 etapas visibles
   (roadmap de 3 rutas, cronograma de 3 columnas por área), alineado con el estándar de la casa
   para propuestas multi-fase (memoria `roadmap-default-3-etapas`). La carga horaria total no
   cambia: sigue siendo 8h de sesiones por área (4h diagnóstico + 4h transferencia) + 1 semana de
   construcción intermedia sin sesiones — solo se nombra y se muestra la etapa de construcción
   que antes vivía implícita dentro de "Fase 2 · Implementación".
3. **La Fase 2 · Construcción se enmarca como "principalmente en Copilot"**: Intezia construye
   cada caso priorizado aprovechando el ecosistema Microsoft 365 que DUSA ya tiene, y solo suma
   Claude en los casos donde el diagnóstico (Fase 1) señaló que Copilot, por ser un asistente
   genérico, no alcanza. Ningún texto trata a Copilot como una herramienta insuficiente por
   defecto — se define primero, y Claude es la excepción justificada por datos, no la regla.
4. **2 entregables nuevos, ya documentados en `Entregables consolidados` pero sin reflejo en el
   AcroForm `Entregables`**: **Documento semilla** (por área) — consolida los hallazgos de la
   auditoría (procesos, datos, reglas del área) y sirve de base de contenido para construir los
   casos en la Fase 2. **Hoja de ruta priorizada** — ya estaba en el brief, ahora también en el
   campo `Entregables` del PDF.

> Caso base de este patrón (no tratar la herramienta que el cliente ya tiene como algo
> insuficiente por defecto): mismo espíritu que §4.11, extendido aquí al tono, no solo al hecho
> de la migración de stack.

## Tercera vuelta de encuadre (2026-08-12, cuarta revisión — bloqueante)

El usuario pidió una cuarta pasada tras revisar el deck de la revisión (c): todavía había
demasiado foco en nombrar Claude y Copilot como tema central, cuando el cliente hoy mismo
confirmó que sigue con Copilot y no conviene abrir con Claude como protagonista.

1. **Claude deja de ser el protagonista del deck.** El hilo conductor pasa a ser la
   **auditoría**: qué se audita, qué se entrega, y la Fase 2/3 de implementación en base a lo
   que esa auditoría detecte, siempre enfocada en Comercial y Finanzas. Claude ya no encabeza
   frases como "dónde Claude puede ayudar" en cada slide — esa función pasa a la auditoría y
   la hoja de ruta.
2. **Título de portada sin nombrar ninguna herramienta** (instrucción explícita del usuario,
   2026-08-12): nuevo h1 "Auditoría de automatización, caso por caso" — ni Claude ni Copilot
   aparecen en el título. El lead (subtítulo) sí nombra a **Copilot** primero, como el
   ecosistema donde DUSA ya trabaja, y menciona a **Claude** solo como apoyo puntual
   condicionado al diagnóstico, nunca como punto de partida.
3. **Ambos nombres se mantienen en el deck** (decisión del usuario, con base en la
   conversación con el cliente del 2026-08-12): se retiran del título y de la apertura, pero
   siguen apareciendo más adelante para que el cliente se sienta cómodo viendo nombrados los
   dos productos con los que ya trabaja o evalúa. Copilot lidera la narrativa (es el
   compromiso ya definido); Claude aparece siempre condicionado ("si el diagnóstico lo
   justifica", "cuando la auditoría detecta una oportunidad real"), nunca prometido de
   antemano.
4. **Estructura narrativa reforzada**: Fase 1 · Auditoría (diagnóstico + mapa de calor +
   documento semilla + generador de prompts + hoja de ruta) → Fase 2 · Construcción, hecha
   principalmente desde el ecosistema Copilot de DUSA; como producto también de la propia
   auditoría, Intezia identifica además oportunidades adicionales de automatización
   construibles directamente en Copilot, presentadas como **oportunidad de reconsumo** (valor
   adicional que DUSA puede activar más adelante, fuera del alcance ya cotizado) → Fase 3 ·
   Implementación/adopción de lo construido en Copilot, con transferencia de conocimiento.
   Claude se suma a la Fase 2 únicamente en el caso puntual donde el diagnóstico lo señale.
5. **La propuesta se posiciona como el primer paso de arranque**: el objetivo comercial de
   este deck es que DUSA apruebe y arranque con la estructura propuesta (empezando por la
   auditoría), no cerrar de antemano todo el proyecto de 3 fases. Por eso la cotización
   (punto 6) se acota a Fase 1.
6. **Cotización acotada a Fase 1 · Auditoría** (mismo patrón que `aerocentro`/`pago-tronic`,
   ver `plantillas/propuesta-comercial.md` → *Roadmap*): las 2 hojas de Propuesta Económica
   (Comercial, Finanzas) cotizan solo la Fase 1; se agrega la nota
   `Las fases 2 y 3 se cotizarán de forma progresiva, según lo que arroje el diagnóstico.`
   (clase `.cot-progressive`, copiada de `aerocentro/styles.css`) entre `cot-validity` y
   `cot-terms-box`. Revierte la nota comercial anterior de "2 hojas ... cada una cubriendo sus
   3 fases combinadas en un solo total".
7. **Roadmap y cronograma se mantienen en 3 fases explícitas** (no se revierte la revisión
   (c)) — el pedido de esta vuelta es de tono y de cotización, no de estructura de fases.

> Caso base de este patrón (no abrir con la herramienta nueva como protagonista cuando el
> cliente ya tiene un compromiso definido con otra): mismo espíritu que §4.11 y que la
> *Segunda vuelta de encuadre* de arriba, llevado ahora también al título de portada y a la
> cotización.

## Cuarta vuelta de encuadre (2026-08-12, quinta revisión — bloqueante)

Instrucción adicional del usuario, mientras se aplicaba la revisión (d): **no mencionar
ninguna herramienta a lo largo de la propuesta** (deck, PDF, AcroForms y `programa.md`).
Esto va más allá del punto 3 de la *Tercera vuelta* arriba (que aún permitía nombrar Copilot
y Claude fuera del título, "para que el cliente se sienta cómodo") — esta revisión lo retira
también.

1. **Cero nombres de producto en el material de cara al cliente**: ni "Claude", ni "Copilot",
   ni "Microsoft 365" aparecen en `index.html`, el PDF resultante, `acroforms.json` ni
   `programa.md` (documento oficial de diseño, potencialmente compartible). Se reemplazan por
   lenguaje genérico: "el entorno/ecosistema que ya usan", "su plataforma actual", "un
   asistente de IA adicional", "apoyo complementario de IA", "asistente conversacional
   adicional".
2. **La lógica de negocio no cambia, solo el nombre**: la auditoría sigue siendo el primer
   paso; la construcción sigue siendo principalmente sobre el ecosistema que DUSA ya tiene
   instalado; el apoyo de IA adicional solo se recomienda si el diagnóstico detecta una
   oportunidad real. Internamente (en este `brief.md`, documento interno) se mantiene el dato
   de que ese ecosistema es Copilot/Microsoft 365 y que el asistente adicional evaluado es
   Claude, para contexto de diseño y para que ventas sepa a qué se refiere cada mención
   genérica al conversar con el cliente.
3. **`brief.md` es la única excepción**: como documento interno (§4.14, nunca va al cliente),
   conserva los nombres reales de las herramientas para trazabilidad y contexto de decisión.
   Todo lo demás (`programa.md`, `acroforms.json`, `index.html`, PDF) queda libre de nombres
   de producto.
4. **Verificación**: antes de entregar, grepear `index.html`, `acroforms*.json` y
   `programa.md` por "Claude", "Copilot" y "Microsoft 365" — cero resultados esperados.

## Quinta vuelta de encuadre (2026-08-12, sexta revisión — bloqueante)

Dos ajustes adicionales del usuario tras generar el primer PDF de la revisión (e):

1. **La hoja de cotización no menciona las Fases 2 y 3.** Se retira la nota
   `.cot-progressive` ("las fases 2 y 3 se cotizarán de forma progresiva...") de ambas hojas
   de Propuesta Económica y del campo `Programa`/`Programa_2` — revierte el punto 6 de la
   *Tercera vuelta de encuadre*. La cotización queda enfocada solo en lo que se cotiza (Fase
   1 · Auditoría), sin adelantar al cliente que hay fases futuras todavía sin costo. El resto
   del deck (roadmap, cronograma) sigue mostrando las 3 fases del proyecto completo; solo la
   hoja de cotización omite la mención.
2. **El proceso de auditoría se explica más literal**: se pidió que el deck muestre el
   "cómo" (qué hacemos cuando llegamos a la empresa, paso a paso) y que los entregables que
   se prometieron al cliente en la reunión aparezcan nombrados de forma explícita:
   **hoja de ruta, logros inmediatos y documento semilla**. Se ajustó:
   - Roadmap (slide 7), facet "Qué pasa" de Fase 1: ahora narra el proceso
     (entrevistas → mapeo → construcción del mapa de calor) en vez de una frase genérica.
   - Roadmap, entregable insignia: la lista ahora nombra "Documento semilla y logros
     inmediatos por área" en vez de solo "documento semilla".
   - Cronograma (slides 5 y 6), línea "Entrega" de Fase 1: nombra los 3 entregables
     literalmente ("mapa de calor, documento semilla, logros inmediatos y hoja de ruta") en
     vez de "generador de prompts".
   - AcroForm `Entregables`: se agrega la línea "Logros inmediatos por área." (antes solo
     estaba implícito en el generador de prompts).
   - "Generador de prompts de uso inmediato" queda retirado del copy de cara al cliente,
     reemplazado por "logros inmediatos" (mismo concepto, término que usó el usuario en la
     reunión con el cliente).

> Caso base: refuerza que la cotización debe ser legible por sí sola (§4.10, capacidad de
> cajas) y que los entregables prometidos verbalmente al cliente deben quedar en el material
> escrito, no solo en la conversación.

## Sexta vuelta de encuadre (2026-08-12, séptima revisión — revisión (g))

El usuario pidió agregar de vuelta las 3 fases en las 2 hojas de Propuesta Económica —
revierte el acotamiento a Fase 1 de la *Tercera vuelta de encuadre* (punto 6) y de la
*Quinta vuelta de encuadre*. Cada hoja vuelve a cubrir **las 3 fases combinadas en un solo
total** (mismo patrón que antes de la revisión (d)):

1. `block-eyebrow` vuelve a ser solo el nombre del área ("Comercial" / "Finanzas"), sin
   sufijo "· Fase 1".
2. `block-value` vuelve a "Diagnóstico 4h + construcción 1 sem + transferencia 4h."
3. El campo `Programa`/`Programa_2` lista las 3 fases (Diagnóstico, Construcción,
   Implementación) en vez de solo la Fase 1.
4. `Notas`/`Notas_2` vuelve a "Alcance de [área]: las 3 fases incluidas."
5. Sigue sin mencionar nombres de herramientas (revisión (e) se mantiene) y sigue sin la
   nota `.cot-progressive` (ya no aplica: al cotizar las 3 fases juntas no hay fases futuras
   pendientes de cotizar).

## Séptima vuelta de encuadre (2026-08-12, octava revisión — revisión (h))

El usuario pidió enfocar toda la propuesta en la Fase 1 (auditoría), dejando las Fases 2 y 3
como "pinceladas" (mención breve, sin el mismo nivel de detalle), y que la cotización vuelva
a decir explícitamente que cubre solo la Fase 1 — revierte la *Sexta vuelta de encuadre*.

1. **Cronograma (slides 5 y 6)**: las columnas de Fase 2 · Construcción y Fase 3 ·
   Implementación bajan de 3 viñetas a **1 viñeta breve cada una** (pincelada); la columna
   Fase 1 · Diagnóstico mantiene sus 3 viñetas completas — es la única con detalle real, para
   que quede claro que es el foco de la propuesta.
2. **Propuesta Económica (slides 13-14)**: vuelve a cubrir **solo Fase 1** — `block-eyebrow`
   con sufijo "· Fase 1", `block-value` describe solo la auditoría (4h), `Programa`/
   `Programa_2` listan solo la Fase 1, y `Notas`/`Notas_2` dicen explícitamente **"Este monto
   cubre únicamente la Fase 1..."** (sin usar la palabra "cotiza\w*", bloqueada por el
   detector §4.15 — ver memoria `verificador-acroforms-economicos`). No se nombra a las
   Fases 2-3 en la hoja (se mantiene el punto de la *Quinta vuelta de encuadre*).
3. **Roadmap (slide 7)** se deja sin cambios: sus facets de Fase 2/3 ya eran breves respecto
   a Fase 1, no hacía falta recortarlos más.

> Nota para el próximo ciclo: este deck ha oscilado varias veces entre "cotizar solo Fase 1"
> y "cotizar las 3 fases combinadas" (revisiones d, f, g, h). Antes de otra vuelta, confirmar
> con el usuario cuál es el estado definitivo que se entrega al cliente.

## Octava vuelta de encuadre (2026-08-12, novena revisión — revisión (i))

El usuario pidió retirar la **cantidad** de sesiones del copy de cara al cliente: en vez de
"2 sesiones de 2h", el deck ahora dice solo **"sesiones de 2h"** (sin número). Aplicado en:
`index.html` (label de Fase 1 en cronograma x2, `rmx-card-name` del roadmap, `block-value`
de ambas hojas de Propuesta Económica), `acroforms.json` (`Programa`/`Programa_2`) y
`programa.md` (duración, tabla §5.1, nota §5.2). Se retiró también el paréntesis "(4h total)"
donde acompañaba a la mención de sesiones, porque revelaba la cantidad por cálculo implícito
(4h ÷ 2h = 2 sesiones). Las entradas de `brief.md` anteriores a esta revisión conservan la
cifra "2 sesiones de 2h" como registro histórico de lo decidido en su momento — no se
reescriben.

## Novena vuelta de encuadre (2026-08-12, décima revisión — revisión (j))

El usuario pidió retirar también la **duración** de Fase 2 y Fase 3 del copy de cara al
cliente (mismo espíritu que la revisión (i) con las sesiones): ya no se dice "1 semana" para
Construcción ni "4h" para Implementación. Aplicado en `index.html` (labels de cronograma x2
por área, `rmx-card-name` del roadmap) y `programa.md` (Duración, tabla §5.1, tabla §5.2,
nota §5.2). Fase 1 conserva su duración ("sesiones de 2h") porque es el foco cotizado del
deck; Fase 2/3 quedan como mención breve sin cifras de tiempo.

## Décima vuelta de encuadre (2026-08-12, undécima revisión — revisión (k))

Dos pedidos del usuario:

1. **Se retira la slide de Mapa de Calor** (era la slide 11 · `.s-heatmap`, eyebrow
   "07 · Mapa de Calor"). El deck baja de 16 a **15 slides**; se renumeraron todos los
   `counter` y los eyebrows numerados que venían después (Impacto pasa de "08" a "07",
   Próximos pasos de "09" a "08"). El concepto "mapa de calor" **se mantiene como nombre de
   entregable** en el resto del deck (Fase 1 "Entrega", roadmap, AcroForm `Entregables`) —
   solo se retiró la slide-tabla que lo mostraba en detalle (con casos, puntuación y
   prioridad por área), coherente con no adelantar hallazgos específicos antes de la
   auditoría real.
2. **El roadmap (slide 7, card Fase 2 · Construcción) menciona que el equipo del cliente
   participa en la construcción** — reemplaza "Sin sesiones con el cliente" /
   "no requiere tiempo del cliente" por "Con participación del equipo" /
   "con el equipo del área participando en la construcción". **Esta mención vive solo en el
   roadmap**, a pedido explícito del usuario: el cronograma (slides 5-6) y `programa.md`
   conservan su descripción de Fase 2 sin cambios (Intezia construye, sin detallar
   participación del cliente ahí).

## Undécima vuelta de encuadre (2026-08-13, duodécima revisión — revisión (l))

El usuario pidió **unificar la hoja de Propuesta Económica**: de 2 slides `.s-price`
separadas (una por área, con AcroForms `Programa`/`Notas` y `Programa_2`/`Notas_2`) a **1 sola
slide** que cubre Comercial y Finanzas juntas.

1. Se eliminó la 2ª slide `.s-price` (Finanzas) y se fusionó su contenido en la 1ª: el deck
   baja de 15 a **14 slides**, con todos los `counter` renumerados en cascada.
2. `block-eyebrow` de la slide pasa a "Comercial y Finanzas · Fase 1"; `block-value` a
   "Auditoría diagnóstica: sesiones de 2h por área."
3. AcroForms: se retiraron `Programa_2` y `Notas_2` de `acroforms.json`. El campo `Programa`
   único ahora dice "Auditoría de automatización · Comercial y Finanzas" + "Fase 1 ·
   Diagnóstico: sesiones de 2h por área" + "Entrega: ... por área". `Notas` dice "Este monto
   cubre únicamente la Fase 1 · Auditoría, para ambas áreas." — sigue habiendo **un solo
   total** (`PrecioBase`/`Descuento`/`PrecioTotal`, sin sufijo `_2`), ya que
   `agregar-campo-precio.py` inyecta los 5 campos de precio solo donde detecta el marker
   "Propuesta Económica" — ahora aparece una sola vez.
4. `foot .meta` de la slide vuelve a "DUSA · CAP-088" (sin sufijo de área, ya que cubre
   ambas).

> Nota: esto revierte el patrón "una hoja de cotización por área" documentado en la memoria
> `multi-track-una-propuesta` — aplicable cuando el cliente pide una sola cifra en vez de
> cotizaciones separadas por departamento.

## Antecedente — por qué este es "CAP-088" y no el primer proyecto de DUSA

DUSA ya vivió una **Fase 1 de fundamentos de IA con otro proveedor** (no Intezia): la convicción cultural de los líderes ya está instalada, pero Intezia entra como proveedor nuevo, sin historial propio en esta cuenta salvo dos entregas previas:

1. `CH-007` — charla de primer acercamiento ("La Próxima Destilación"), sin propuesta económica, que abrió la conversación con Wilmer y priorizó Comercial y Finanzas.
2. `CAP-087` — Manual de Políticas y Gobernanza Ética de IA de DUSA, primer proyecto formal de Intezia con el cliente. Ese brief ya anticipaba una **"Fase 2"**: construir herramientas propias con Claude usando la información levantada en el manual. **`CAP-088` es esa Fase 2.**

Este proyecto asume que `CAP-087` (o un proceso de gobernanza equivalente) ya está en marcha o cerrado: cualquier caso de Claude que se evalúe y active aquí se diseña **dentro de las reglas de uso responsable** que ese manual define, no antes ni en paralelo sin marco.

## Contexto del cliente (para diseño interno, no aparece como afirmación de stack en el deck — §4.11)

- Compañía industrial del sector bebidas / licores. ~500 colaboradores a nivel internacional · 360 en plantas · 85% del headcount en Venezuela.
- **Copilot es un compromiso ya definido**, exigido por la matriz interna de seguridad/gobierno de TI de DUSA (referida internamente como "matriz DUC") — integración nativa con Microsoft 365 y estándar de seguridad corporativa. No es negociable ni el eje de este proyecto: es el punto de partida. El rol de Claude es complementar, evaluando caso por caso en Comercial y Finanzas dónde un asistente genérico como Copilot no resuelve el dolor operativo real — nunca se compromete de antemano una lista fija de funciones.
- **Alfabetización en IA ya instalada**: DUSA pasó por un programa externo de fundamentos de IA (con otro proveedor, antes de Intezia) — la convicción cultural del liderazgo y el vocabulario básico de IA ya están presentes. Esta propuesta no reintroduce fundamentos: el diseño instruccional arranca directo en auditoría aplicada.
- Talento Humano: ~15 personas para 5 sub-áreas (Relaciones Laborales, Compensación, Seguridad, Servicio Médico, Talento).
- Ecosistema actual: Microsoft (Word / Excel / Copilot) + sistema aparte para contabilidad ("GDL").
- **Comercial**: no existe un CRM real. El desarrollo a la medida hecho por una empresa colombiana no funciona; ya lo intentaron parchar sin éxito. El vendedor cobra y vende en la calle, pero debe volver a la oficina a cargar los datos desde su laptop porque el celular no lo soporta — tiempo de campo perdido en trabajo administrativo. Wilmer quiere ver desde el celular el estado de cada cliente (compra habitual, inventario pendiente, conexión despacho↔cobro) con recordatorios automáticos del plazo de pago de 21 días. Cita: *"Quiero que mi vendedor esté feliz. Y que venda [...] No lo puedo tener haciendo trabajo administrativo porque lo estoy desviando."* Wilmer conecta esta agilidad con crecimiento, no solo eficiencia: *"Hay más flujo, entonces puedes hacerlo en otras empresas, eso justifica mucho."*
- **Finanzas**: sistema "arcaico", mucho papel y registro manual. Cobro 100% manual, sin recordatorio del plazo de 21 días (mismo dato que Comercial — para Wilmer venta y cobro son un solo proceso que hoy falla igual). La aprobación de facturas es un circuito físico completo de firmas: *"Es un proceso militar. Si no está firmado, estás violando la política de la empresa."* — riesgo real de cumplimiento cada vez que una factura se traba. **Dato sensible, NO mencionar en el deck**: DUSA evalúa migrar su sistema de contabilidad actual ("GDL") a Odoo por su cuenta — cualquier agente de Finanzas debe complementar esa evaluación, nunca competir con ella ni nombrarla (§4.11).
- **Logística**: falta de conexión entre inventario, despacho y estado de cuenta del cliente — mencionado por Wilmer, no profundizado en la reunión; candidato natural del mismo proyecto por su cercanía con Comercial y Finanzas (la brecha entre lo despachado y lo cobrado es el mismo dato de los 21 días).
- **Talento Humano**: no es el dolor prioritario para Wilmer ("rotación no es un dolor grande para ellos"), pero el equipo de 15 personas cubre 5 sub-áreas sin poder escalar su carga administrativa sin contratar más gente. Se incluye como 4ª área porque cumple lo que ya se prometió como ejemplo de autonomía en el módulo 4 de `CH-007` ("Cada Líder, su Claude").
- **Legal / Contabilidad quedan fuera de esta propuesta**: el propio Wilmer anticipó resistencia ahí (*"mi equipo de contabilidad se va a quedar con lo mismo [...] el tema legal..."*) — no se incluyen como área de prioridad alta en este proyecto, igual que Desarrollo y Auditorías quedaron fuera del alcance de Pago Tronic.
- **Cómo decide la directiva**: retorno de negocio, no reducción de costos. Cita: *"Si no tiene impacto en el negocio, no vamos a hacer el trabajo."* Cada caso evaluado debe mostrar un movimiento de negocio concreto (menos tiempo administrativo, más trazabilidad, más ventas) antes de activarse, no solo justificarse como herramienta técnica.
- Wilmer ya quiere que **cada líder de área sea autónomo** para crear sus propias automatizaciones sin depender de que otro equipo lo resuelva — esa autonomía es, literalmente, el objetivo de este proyecto. **No se nombra ningún departamento interno de DUSA como bloqueador** (mismo aprendizaje aplicado en `CAP-087` el 2026-08-04, extendido aquí).

## Decisión de alcance (2026-08-04, confirmada 2026-08-12)

Wilmer fue directo: el dolor prioritario ahorita está en Comercial y Finanzas, y sumar Logística y Talento Humano a la propuesta activa diluye el foco justo donde el cliente ya dio la prioridad. Por eso **CAP-088 se acota a Comercial y Finanzas**, plasmadas como **áreas separadas** en todo el deck (slide 4, roadmap, mapa de calor y ahora también en la cotización — 2 hojas de Propuesta Económica independientes).

Logística y Talento Humano no desaparecen del proyecto: siguen documentados abajo (diagnóstico original, contexto de cliente) y aparecen en el deck como **slide 8 · Continuación** — la extensión natural del mismo sistema, presentada explícitamente como fuera de este alcance, para cuando el negocio lo pida.

## Diagnóstico (4 puntos — uno por área, ver Decisión de alcance arriba)

1. **Comercial** no tiene un CRM real: el desarrollo a la medida sigue sin funcionar pese a varios intentos de ajuste, y el vendedor pierde tiempo de calle cargando datos manualmente al volver a la oficina.
2. **Finanzas** aprueba cada factura con un circuito físico de firmas y cobra sin ningún recordatorio del plazo de pago de 21 días, con papel y registro manual como la norma.
3. **Logística** no tiene una vista que conecte el inventario, el despacho y lo que el cliente ya pagó — la brecha entre lo que salió y lo que se cobró se pierde entre sistemas separados.
4. **Talento Humano** cubre 5 sub-áreas con solo 15 personas, y cada automatización pequeña sigue dependiendo de que otro equipo la resuelva.

## Estructura del proyecto

### Apoyo de Claude evaluado caso por caso · 2 áreas de prioridad alta (alcance activo)

En cada área se evalúa, caso por caso, dónde Claude puede ayudar donde Copilot no llega — no se compromete un agente fijo de antemano:

1. **Comercial** — de llamadas y carga manual en la oficina a evaluar casos como visibilidad de cliente, inventario y cobro desde el celular.
2. **Finanzas** — de firma en papel a evaluar casos como aprobación y seguimiento del cobro con trazabilidad.

**Continuación (fuera de este alcance, slide 8):**

3. **Logística** — de sistemas sueltos a evaluar si Claude puede conectar inventario, despacho y estado de cuenta.
4. **Talento Humano** — de depender de otro equipo a evaluar casos propios para sostener 5 sub-áreas con el mismo equipo.

### Proyecto de 3 fases (revisión 2026-08-12 (c): las 3 etapas vuelven a mostrarse explícitas)

- **Fase 1 · Diagnóstico** — 2 sesiones de 2h por área (4h total por área). Auditamos los procesos reales de Comercial y Finanzas y entregamos, por área: un **mapa de calor de oportunidades de automatización con IA**, un **documento semilla** con los hallazgos de la auditoría, y un **generador de prompts de uso inmediato**, sin esperar a la Fase 2.
- **Fase 2 · Construcción (Intezia)** — 1 semana por área, sin sesiones con el cliente: Intezia construye cada caso priorizado, **principalmente en Copilot**, aprovechando el ecosistema Microsoft 365 que DUSA ya tiene, y suma Claude únicamente en los casos donde el diagnóstico señaló que Copilot no alcanza. Nunca como paquete cerrado de antemano.
- **Fase 3 · Implementación** — 4h de **transferencia de conocimiento** por área: activamos los casos construidos en el día a día del equipo y dejamos a cada líder capacitado para evaluar y mantener nuevos casos de forma independiente.

Total por área activa: 8h de sesiones (4h diagnóstico + 4h transferencia) × 2 áreas = 16h, más 1 semana de construcción intermedia por área, repartidas en el tiempo. (Mismo total de horas que las revisiones anteriores — la Fase 2 · Construcción, que antes vivía implícita dentro de "Implementación", ahora se nombra y se muestra como su propia etapa.)

## Especificaciones del programa

- **Duración**: por área, diagnóstico 2 sesiones de 2h + transferencia 4h; entre ambas, 1 semana de construcción (principalmente en Copilot) a cargo de Intezia (fechas exactas a confirmar).
- **Modalidad**: Online síncrono.
- **Audiencia**: líderes de Comercial y Finanzas; número de participantes a confirmar con Wilmer. Ya alfabetizados en IA — el diseño no incluye módulo de fundamentos. (Logística y Talento Humano quedan fuera de este alcance, ver Decisión de alcance).
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.
- **Con slide de Propuesta Económica** (revierte la instrucción original de 2026-08-03): 2 hojas independientes, una por área (Comercial, Finanzas), cada una con sus 2 fases combinadas en un solo total y su bloque de Términos y condiciones. Ver *Notas comerciales*.

## Entregables consolidados

- Casos construidos y activados donde corresponda en las 2 áreas de prioridad alta (Comercial, Finanzas) — principalmente en Copilot, complementando con Claude solo donde el diagnóstico lo señaló necesario. No un agente fijo garantizado de antemano.
- Mapa de calor de oportunidades de automatización con IA, por área.
- Documento semilla por área — hallazgos de la auditoría, base de contenido para la Fase 2 · Construcción.
- Generador de prompts de uso inmediato, por área.
- Hoja de ruta de implementación priorizada.
- Transferencia de conocimiento documentada — equipo capacitado para evaluar y mantener nuevos casos por su cuenta.
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-088** en INTEZIA Education al cerrar el acuerdo.
- **1 hoja unificada de Propuesta Económica** (revisión (l), 2026-08-13, undécima vuelta — revierte las 2 hojas separadas por área de las revisiones anteriores): campos canónicos únicos `PrecioBase`/`Descuento`/`PrecioTotal`/`Programa`/`Notas`, cubriendo Comercial y Finanzas juntas en un solo total.
- **Cotización acotada a Fase 1 · Auditoría, de forma explícita** (revisión (h), 2026-08-12, séptima vuelta — estado final tras varias idas y vueltas d→f→g→h): cada hoja cotiza solo la Fase 1 por su área; `Programa`/`Programa_2` describen solo la Fase 1, y `Notas`/`Notas_2` dicen explícitamente "Este monto cubre únicamente la Fase 1..." (sin usar "cotiza\w*", bloqueado por el detector). No se nombran las Fases 2-3 en la hoja.
- **Términos y condiciones** (instrucción del usuario 2026-08-12, segunda vuelta): ambas hojas llevan el bloque `cot-terms-box` con enlace a los términos y condiciones institucionales de Intezia (mismo enlace y texto que `canguro`, `aerocentro`, `agromundial`, `ioed`), debajo de `cot-validity`.

## Notas de diseño

- **Se mantiene el clon de `pago-tronic/` (CAP-081)** como base estructural. El roadmap **vuelve a 3 rutas** en la revisión (c) (revierte la reducción a 2 de la revisión (b)): Fase 1 Diagnóstico (`.rmx-node-f2`, amarillo) → Fase 2 Construcción/Intezia (`.rmx-node-f4`, negro/blanco) → Fase 3 Implementación (`.rmx-node-f3`, naranja), con `.rmx-mid` recto en el fork/merge y nodos a 16.667%/50%/83.333% — geometría idéntica a `pago-tronic/` (caso base original de la memoria `roadmap-3-etapas-flex-minheight`, ya trae `min-height:0` en `.rmx-route`).
- **Se conserva el `styles.css` local completo** (no `../_base/`), igual que `dusa-cap087`.
- **`.s-heatmap` retirada del deck** (revisión (k), 2026-08-12, décima vuelta — revierte la nota anterior de esta sección, que la daba por conservada). El deck queda en 15 slides.
- **`.s-schedule`, una por área**: 3 columnas (`.ses-cols`) — Fase 1 Diagnóstico (2 sesiones de 2h), Fase 2 Construcción (1 semana, estilo `.block-rec` fondo negro para marcar "sin sesiones con el cliente") y Fase 3 Implementación (4h de transferencia), con la `.ruta` marcando el índice del área (1 de 2 … 2 de 2). La columna "Recursos y entornos" que ocupaba el 3er lugar en la revisión (b) se plegó en una línea `.ses-resources` bajo los chips de "Temas" para hacer espacio a la Fase 2 · Construcción sin exceder las 3 columnas de capacidad (`plantillas/capacidad-cajas.md`).
- **1 slide `.s-price` unificada** (revisión (l) — antes eran 2, marker "Propuesta Económica" detectado 2 veces; ahora 1 sola vez, solo campos canónicos, sin sufijo `_2`). Va entre Impacto y Próximos pasos. Incluye `cot-terms-box` (Términos y condiciones, segunda vuelta 2026-08-12); no lleva nota de Fases 2-3 (revertido en la quinta vuelta, 2026-08-12 (f)).
- **Terminología de producto retirada del copy de cara al cliente**: "Skill"/"Project"/"Artifact", "agente a medida" como sustantivo de entregable fijo, y desde la quinta vuelta (2026-08-12 (e)) también los nombres propios de herramientas, se reemplazan por "apoyo de IA adicional" / "caso evaluado" / "caso priorizado" — siempre condicionado a la evaluación de la auditoría, nunca como compromiso cerrado de antemano (ver *Ajuste de encuadre*).
- **Sin nombres de herramientas en toda la propuesta** (revisión (e) 2026-08-12, quinta vuelta — reemplaza la decisión anterior de nombrar Copilot explícitamente): ni "Claude", ni "Copilot", ni "Microsoft 365" aparecen en el deck, el PDF, `acroforms.json` ni `programa.md`. El hilo conductor es la auditoría (qué se hace, qué se entrega) y la Fase 2/3 de implementación en base a lo detectado. Se usa lenguaje genérico ("el entorno que ya usan", "un asistente de IA adicional") — los nombres reales quedan solo en `brief.md` como contexto interno.
- **Sin mención de "Tecnología" como departamento bloqueador** (aplica el aprendizaje de `CAP-087` 2026-08-04 también aquí — la versión original de este deck todavía lo nombraba en la slide 8 de Continuación; corregido en esta revisión): se usa "sin depender de que otro equipo lo resuelva".
- **Sin dato de Odoo/GDL, sin migración de stack (§4.11)**: el deck nunca dice que DUSA cambia su sistema de contabilidad, su CRM o su entorno de trabajo actual — el apoyo de IA adicional, donde se active, se enmarca como algo que opera junto a lo que el cliente ya usa.
- **Slide de Impacto**: se conservan los 2 estudios reales ya validados (McKinsey 2023 para Comercial, Ardent Partners 2025 para Finanzas) — no requieren cambio, ninguno menciona Skill/Project ni contradice el nuevo posicionamiento.
- **Equipo no nombrado**: "Consultor Intezia" (perfil de automatización de negocio con Claude) + "Coordinación Intezia Education" — mismo patrón que `CAP-087` y `pago-tronic`.
- **Asesora comercial visible en el cierre**: María Iribarren, mismo formato que `dusa-cap087` (`.end-contact`).
- **Sin acuerdos económicos en "Cómo arrancamos"** (§4.15): los 3 pasos son solo logística.
- **Sin guion largo** (§4.13).
- **Acrónimos**: "CRM" es de uso general y no requiere expansión (§4.12, excepción de sigla de uso general). Ningún nombre de producto ("Copilot", "Claude", "Microsoft 365") aparece en el deck desde la revisión (e) — ver *Cuarta vuelta de encuadre*.

## Notas internas (NO van al deck ni al cliente)

- Este proyecto asume que `CAP-087` (Manual de Gobernanza) está aprobado o en curso — si DUSA todavía no lo firmó, validar con Wilmer si CAP-088 puede arrancar en paralelo o debe esperar el cierre de CAP-087.
- Vigilar la evaluación interna de DUSA de migrar de "GDL" a Odoo (mencionada en `CAP-087`): cualquier caso de Claude evaluado en Finanzas debe diseñarse para complementar esa migración cuando ocurra, no competir con ella.
- "Matriz DUC" es la matriz interna de gobierno de TI/seguridad de DUSA que exige Copilot — dato de contexto interno para justificar el tono del deck (Copilot no se cuestiona, se complementa), nunca se nombra el acrónimo "DUC" de cara al cliente.
- El programa de alfabetización previa de DUSA fue con Grupo Marna (proveedor externo, no Intezia) — dato interno para justificar por qué se salta fundamentos; no se nombra al proveedor en el deck.

## Pendientes

- Confirmar apellido, correo y teléfono de Wilmer.
- Confirmar número de participantes por área.
- Confirmar fechas tentativas y zona horaria.
- Confirmar estado real de `CAP-087` (aprobado / en curso / pendiente) antes de fijar el arranque de CAP-088.
- Confirmar presupuesto indicativo (no discutido aún) — ahora relevante porque el deck ya lleva slide de Propuesta Económica.
