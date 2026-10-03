# Brief — AMV Tecnología · Cerebro Digital (Propuesta 2 · CAI-023)

---

## REESCRITURA 2026-09-24 (3ra corrección del mismo día) — LEER PRIMERO

Todo lo que sigue debajo de esta sección describe la **versión original** de CAI-023 (patrón
"sistema por funciones": Compras Inteligentes + Memoria de Servicio Técnico, 24h, roadmap de
4 etapas) — se conserva como **historial**, no como estado vigente del documento.

El usuario pidió, en 3 mensajes sucesivos el mismo día, reconstruir el deck completo:

1. *"vamos a corregir la CAI-023 y hagamos esa propuesta de cerebro digital como la acabamos
   de hacer con banco plaza dejando en claro que hace el cerebro y como los puede ayuda en su
   caso"* → 1ra corrección: se agregó una slide nueva explicando el mecanismo, con 2 tarjetas
   por función (Compras Inteligentes / Servicio Técnico).
2. *"no, en este caso tiene que ser generico porque lo que quieren saber es que hace el
   cerebro no apliques temas al cerebro hazlo como la propuesta de banco plaza"* → 2da
   corrección: la slide se rehizo genérica (sin nombrar funciones), pero el resto del deck
   (roadmap de 4 etapas, 24h, Compras/Servicio Técnico) seguía igual.
3. *"no menciones los departamentos ni menciones personas deja claro que hace un cerebro
   digital que son 6h por persona y ya esta"* → 3ra corrección (esta reescritura): el usuario
   dejó claro que el deck ENTERO debía dejar de estar organizado por función/persona nombrada
   y pasar al patrón **"asistente personal"** genérico ya usado en
   `banco-plaza-cerebros-digitales/` (CAI-025) — **6 horas por Cerebro Digital** (excepción de
   `empresa/politicas-comerciales.md`), no el patrón "sistema por funciones" de 24h.

**Decisión de número de personas**: el usuario no dio un número explícito en la 3ra
corrección. Se usó **2** (interpretación, no dato dado) porque es el número de necesidades
reales ya identificadas en el levantamiento original de este documento (las 2 funciones que
ahora ya no se nombran) — **confirmar con el usuario si el número correcto es otro**. Total:
2 personas × 6h = **12h de propuesta** (antes: 24h).

**Qué cambió en la práctica**: `index.html`, `programa.md`, `acroforms.json`, `meta.json` y
`scripts/customize-amv-tecnologia-cerebro-digital.py` se reescribieron siguiendo casi
literalmente `banco-plaza-cerebros-digitales/` como plantilla (mismo Programa de 3 módulos,
misma slide "Su segundo cerebro" genérica, mismas 3 sesiones, mismos Beneficios/Impacto,
mismo formato de cotización con 12h) — cambiando solo cliente, asesora (María Iribarren,
+58 414-0570056, miribarren@intezia.com) y el número de personas (2 en vez de 5). El roadmap
de 4 etapas, las 2 funciones nombradas y los nombres Juan/Yamil ya **no aparecen** en el
documento.

## Calendario agregado (2026-09-24, mismo día — instrucción directa del usuario)

*"por favor coloca el calendario empezando el 29 y teniendo las sesiones lunes y miercoles
desde el 5"* → mismas fechas ya usadas para `amv-tecnologia/` (DET-019): martes 29 de
septiembre de 2026 es el kick-off; el 5 de octubre de 2026 es lunes, así que "lunes y
miércoles desde el 5" da 6 sesiones de 2h (= 12h totales, coincide con el total ya fijado):
lunes 5, miércoles 7, lunes 12, miércoles 14, lunes 19 y miércoles 21 de octubre.

**Decisiones sin dato explícito del usuario, documentadas para confirmar**:
- **Numeración de sesiones**: se etiquetaron genéricamente "Sesión 1" a "Sesión 6", sin
  asignarlas a "Persona 1" / "Persona 2" — mismo criterio de "no menciones personas" ya
  aplicado en el resto del deck. La asignación real de qué sesiones corresponden a cada
  participante (¿secuencial, 3 sesiones seguidas por persona, o alternado?) queda para
  coordinar en el kick-off, no se fija aquí.
- **Horario**: no se especificó hora exacta ni para el kick-off ni para las sesiones — se usó
  10-11 (kick-off) y 10-12 (sesiones, 2h) por consistencia con el resto de calendarios de
  esta sesión de trabajo (mismo horario usado en `amv-tecnologia/` DET-019 y en las
  propuestas de Banco Plaza). Confirmar con María antes de enviar.

---

## Relación con `amv-tecnologia/` (DET-019 · Propuesta 1)

Este es el **segundo de los 2 caminos pedidos en paralelo** por el cliente (Bloque F de la
ficha): *"El cliente pidió explícitamente DOS propuestas en paralelo: (1) Detección para los 3
grupos definidos, y (2) un proyecto aparte de Cerebro Digital."*

- **Propuesta 1** (`amv-tecnologia/`, DET-019): Detección de Logística, Comercialización y
  Administrativo — construida el 2026-09-23.
- **Propuesta 2** (este documento, `amv-tecnologia-cerebro-digital/`, CAI-023): el Cerebro
  Digital. **Documento separado, con código propio** — mismo criterio que las 2 propuestas de
  Dumogas y que la Propuesta 1 de AMV: cada documento queda autocontenido, **sin referencias
  cruzadas visibles al cliente** entre ambos.

Todos los datos administrativos, de contacto y de stack tecnológico son los mismos que en
`amv-tecnologia/brief.md` (misma Ficha de Levantamiento,
`Levantamiento_AMV_Tecnologia_2026-09-22.pdf`) — no se repiten en detalle aquí, solo lo que
cambia por ser un servicio distinto.

## Datos administrativos

- **Empresa**: AMV Tecnología · **Slug**: `amv-tecnologia-cerebro-digital` · **División**:
  `educacion`
- **Servicio (§4.1a)**: `habilidades` — el Cerebro Digital **no es un 5to servicio ni tiene
  código de catálogo propio**: es un formato de entregable dentro de Habilidades (confirmado
  revisando `empresa/politicas-comerciales.md`, `empresa/catalogo.md` y
  `empresa/tipos-de-documento.md` — ninguno de los tres define "Cerebro Digital" como servicio
  ni como subtipo de catálogo con prefijo propio). El código `CAI-023` que dio el usuario
  (Capacitación In-Company) confirma esta clasificación.
- **Tipo de documento**: Capacitación In-Company (`CAI-023`).
- **Asesora comercial**: María Iribarren.

## Qué es "Cerebro Digital" en este documento — decisión de encuadre

El sistema ya construyó Cerebro Digital antes, con **2 patrones distintos** (investigado en
`empresa/politicas-comerciales.md`, `grupo-corpos/DET-009`, `dhl-cerebro-digital/`,
`grupo-ferrara-cai007/`, `grupo-osorio/`, `pago-tronic/`):

1. **Patrón "asistente personal"** (DHL/Miguel, Ferrara, Osorio, y el objetivo de Grupo Corpos
   DET-009): un Cerebro Digital = un clon/asistente de IA para 1 persona o 1 rol, sobre Claude +
   grafo relacional en Obsidian. Dimensionamiento: **6h por Cerebro Digital** (excepción
   documentada en `politicas-comerciales.md → Dimensionamiento por servicio → Habilidades`).
2. **Patrón "sistema de negocio por áreas"** (`pago-tronic/`, CAP-081): un Cerebro Digital = un
   sistema central de IA que conecta y ordena varias funciones/áreas de la operación real de la
   empresa (no un asistente personal). Estructura propia: diagnóstico por función + construcción
   a cargo de Intezia (sin sesiones) + adopción por función. Cotización única consolidada, no
   por persona.

**AMV pide explícitamente el patrón 2** (cita del contexto de la asesora, no de la ficha
directamente — la ficha solo registra el interés y el pedido de cotización): *"Lo que busca
concretamente es que ese cerebro se conecte con su sistema de gestión propio para sacarle
provecho real a la información que ya tienen [...] y que ahí mismo se centralice el conocimiento
disperso de Servicio Técnico."* Esto es un sistema conectado a datos operativos reales
(inventario, proveedores) y a una base de conocimiento compartida — no un asistente personal
para 1 persona. **Se usa el patrón `pago-tronic/` como precedente estructural**, no la regla de
6h/Cerebro Digital (esa regla se diseñó para el patrón 1, asistentes por persona — aplicarla
aquí forzaría una unidad de cobro que no corresponde al tipo de entregable pedido).

`pago-tronic/` es un deck **legacy** (anterior a §4.10a: CSS local, Beneficios viejo sin v3,
Cierre sin escalera, con slide de Metodología ABR y Equipo facilitador expuestos) — **no se
clona directamente** (CLAUDE.md §6: "Nunca clonar un deck legacy"). Se usa su estructura de
contenido (diagnóstico + construcción + adopción por función, roadmap de 3 etapas, cotización
única) sobre el shell canónico actual (`toyocentro/`, `../_base/styles.css`, Beneficios v3,
Cierre escalera, sin ABR ni Equipo facilitador).

## Las 2 funciones del Cerebro Digital (dato directo de la ficha)

1. **Compras Inteligentes** (Logística) — sugerencia de orden de compra para lentes
   intraoculares, cruzando proveedor, tiempo de entrega, forma de pago, ciudad de origen y
   consumo promedio (últimos 3 meses). Contexto real: 7 modelos de lentes intraoculares, cada
   uno con ~50-65 variantes (cada lente es personalizado a la fórmula del paciente, sin
   estándar posible — se necesita stock amplio para cubrir todas las combinaciones). Hoy
   depende del criterio manual del comprador, sin agente ni análisis automatizado (Bloque C,
   Proceso 2 de la ficha).
2. **Memoria de Servicio Técnico** — centraliza manuales de servicio extensos, service
   bulletins que actualizan procedimientos, y tips no documentados de los propios ingenieros.
   Cuello de botella real: el conocimiento es tácito, vive en la cabeza de cada ingeniero — si
   la persona no está o no comparte cómo resolvió un caso, el conocimiento se pierde y el
   problema se repite (Bloque C, Proceso 3 de la ficha).

**Nota de alcance importante**: Servicio Técnico fue el **4to grupo excluido de la Detección**
(Propuesta 1) — este documento es, en la práctica, lo que le da alcance propio a esa necesidad,
sin necesidad de que la Detección lo cubra. No se menciona esta relación en el deck de cara al
cliente (evita referencias cruzadas entre las 2 propuestas, por decisión ya tomada con el
usuario en la Propuesta 1).

## Dimensionamiento — precedente `pago-tronic/`, adaptado a 2 funciones (no 4 áreas)

> **Actualizado 2026-09-23** (instrucción directa del usuario, al repetir esta propuesta con
> el formato nuevo de cotización): se agrega una **4ta etapa, Implementación**, además de las
> 3 que ya existían. Diagnóstico y Adopción no cambian.

- **Diagnóstico**: 2 sesiones de 2h por función (4h) × 2 funciones = **8h**.
- **Construcción del cerebro digital**: 1 semana, a cargo de Intezia, sin sesiones con el
  cliente — arma el sistema con los hallazgos del diagnóstico y la conexión al sistema de
  gestión de AMV.
- **Adopción**: 4h por función × 2 funciones = **8h**. Activación del cerebro digital en el
  día a día — el equipo aprende a leerlo y ajustarlo.
- **Implementación** (nueva, 2026-09-23): 2 sesiones de 2h por función × 2 funciones = **8h**.
  Profundiza la Adopción con casos reales de trabajo — deja el cerebro digital funcionando
  dentro de la operación diaria, no solo activado.
- **Total de sesiones con el cliente: 24h**, más 1 semana de construcción intermedia.
- **Modalidad**: remota (no hay dato explícito de modalidad para este proyecto en la ficha —
  a diferencia de la Detección, que sí especificó modalidad mixta con kick-off presencial en
  Valencia; se asume remota por defecto, ya que no involucra el mismo tipo de levantamiento
  presencial inicial. Confirmar con María antes de enviar si el cliente prefiere algún tramo
  presencial).
- **Cotización única consolidada**: el Cerebro Digital se cotiza como un sistema completo de 2
  funciones, no como 2 entregables independientes (mismo criterio que `pago-tronic/`).

## Conexión con el sistema de gestión — cómo se presenta (§4.11)

AMV ya tiene un sistema de gestión propio a la medida, en la nube, y están integrando APIs con
bancos activamente (capacidad técnica real confirmada en la ficha). El deck presenta el Cerebro
Digital como algo que **se conecta a** ese sistema existente, nunca como un reemplazo o una
migración — mismo criterio que toda propuesta del sistema (§4.11, "Intezia se ajusta al stack
del cliente, no lo cambia").

## Stack y herramientas — qué se nombra y qué no

- **Claude**: ya probado por Juan con resultado real (facturas). Se puede mencionar como
  contexto (igual que en la Propuesta 1), sin comprometerlo como la única herramienta del
  Cerebro Digital — el diagnóstico confirma el ecosistema final.
- **Sistema de gestión de AMV**: se habla de "su sistema de gestión", sin nombrar la sigla ERP
  de cara al cliente (mismo criterio que la Propuesta 1).
- **Obsidian / grafo relacional**: mecanismo típico de otros Cerebro Digital del sistema (DHL,
  Ferrara), pero **no aplica aquí** — el patrón de AMV es "sistema conectado a datos
  operativos + base de conocimiento", no "clon personal con grafo de notas". No se menciona
  Obsidian en este deck.

## Decisiones confirmadas / sin ambigüedad

1. **Servicio = Habilidades**, código `CAI-023` (dado por el usuario) — no es un 5to servicio.
2. **Patrón "sistema por funciones"** (`pago-tronic/`), no "asistente personal" — decisión
   basada en la descripción explícita del cliente (conexión a datos reales + centralización de
   conocimiento compartido, no un clon individual).
3. **2 funciones**: Compras Inteligentes (Logística) y Memoria de Servicio Técnico — ambas con
   contenido real y específico de la ficha (Bloque C, Procesos 2 y 3).
4. **Sin referencias cruzadas** a la Propuesta 1 (Detección) dentro de este deck.
5. **Sin certificado de participación estándar de Detección** — este es un proyecto de
   Habilidades (construcción real), sí incluye constancia de participación INTEZIA (mismo
   criterio que `pago-tronic/`: "Workbook digital y constancia de participación INTEZIA").
6. **Cotización única consolidada**, no desglosada por función.

## Impacto (§4.9, verificado por WebSearch 2026-09-23)

- **Gartner (comunicado de prensa, 16 de septiembre de 2025)**: *"Gartner Predicts 70% of Large
  Organizations Will Adopt AI-Based Supply Chain Forecasting to Predict Future Demand by
  2030"* — el 70% de las grandes organizaciones adoptará pronósticos de cadena de suministro
  basados en IA para predecir la demanda futura hacia 2030. Verificado directamente en el título
  y la URL de gartner.com (el fetch completo del cuerpo del comunicado dio timeout, pero el
  título/URL de la fuente primaria es suficiente para citar el dato verbatim, sin intermediarios
  de blogs de proveedores). Usado para **Compras Inteligentes**.
- **McKinsey Global Institute — The social economy: Unlocking value and productivity through
  social technologies (2012)**: 20% de la semana de un equipo se va buscando y organizando
  información dispersa. Cita real, **ya usada y verificada en `pago-tronic/`** (mismo dato,
  mismo criterio de reutilización que Dumogas/Andrómeda con sus propias fuentes ya validadas).
  Usado para **Memoria de Servicio Técnico** — encaja directo con el conocimiento tácito disperso
  entre ingenieros.
- Se descartaron varias cifras de "reducción de quiebres de stock" atribuidas a McKinsey
  (65% menos quiebres de stock, 20-50% menos inventario) encontradas solo en blogs agregadores
  (groupbwt.com, openskygroup.com, gitnux.org) sin poder confirmar el informe original exacto —
  mismo criterio de descarte que en Dumogas y la Propuesta 1 de AMV.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: María Iribarren.

## Corrección de lenguaje (2026-09-23, instrucción directa del usuario)

Se retiró la mención "Juan consolidó 80 facturas en 10 minutos" del pain y del ROI de este
deck — mismo criterio aplicado en `amv-tecnologia/` (DET-019): es un ejemplo puntual, no debe
centrar la venta del proyecto (riesgo de disonancia). Se conserva la mención genérica "AMV ya
probó por su cuenta que la IA funciona", sin nombrar el proceso ni las cifras.

## Corrección 2026-09-24 — slide nueva "Así funciona el cerebro digital"

Instrucción directa del usuario: *"vamos a corregir la CAI-023 y hagamos esa propuesta de
cerebro digital como la acabamos de hacer con banco plaza dejando en claro que hace el
cerebro y como los puede ayuda en su caso."*

**Diagnóstico del problema**: el deck explicaba el RESULTADO de cada función (qué logra
Compras Inteligentes / Memoria de Servicio Técnico: "sugiere la orden de compra", "centraliza
el conocimiento") pero no el MECANISMO — qué hace el cerebro digital concretamente, con qué
datos, paso a paso. `banco-plaza-cerebros-digitales/` (CAI-025) sí tenía esa claridad, con su
slide dedicada "Su segundo cerebro" (`.s-graph`) explicando el grafo relacional de Obsidian.

**Importante — no se copió el mecanismo de Banco Plaza, se copió el ESTÁNDAR DE CLARIDAD**:
el patrón "asistente personal" de Banco Plaza (Claude + Projects + grafo de Obsidian) no
aplica aquí — AMV pidió explícitamente el patrón "sistema por funciones" conectado a su
sistema de gestión real (ver "Qué es 'Cerebro Digital' en este documento" arriba). Se
construyó una slide nueva y propia, con la misma función comunicativa (explicar el mecanismo,
no solo el resultado) pero con contenido 100% específico de AMV.

**Solución implementada**: nueva slide 05 (`.s-explain`, "Así funciona el cerebro digital"),
insertada justo después de la slide de las 2 funciones (04) y antes del roadmap (ahora 06-07).
Dos tarjetas en paralelo, una por función, cada una con 3 facetas:

- **Datos que usa**: qué información real de AMV consume el cerebro digital (inventario,
  consumo de 3 meses, proveedores, tiempos de entrega para Compras Inteligentes; manuales,
  boletines técnicos y casos documentados por los ingenieros para Memoria de Servicio
  Técnico).
- **Qué hace**: el mecanismo concreto (cruza los datos y prioriza qué reponer / centraliza el
  conocimiento y responde con contexto real).
- **Cómo te ayuda**: el beneficio anclado a la complejidad real de AMV (7 modelos × 50-65
  variantes cada uno para Compras; dependencia de personas específicas para Servicio Técnico).

Deck pasa de 16 a 17 slides — todo lo posterior a la slide 4 se corrió un lugar. Sin cambios
de horas, precio ni estructura del roadmap: es una corrección de claridad de contenido, no de
alcance.

## Notas internas

- Caso base estructural de **contenido**: `pago-tronic/` (CAP-081, legacy — no se clona
  directamente, ver arriba). Shell canónico clonado: `toyocentro/` (CSS compartido, Beneficios
  v3, Cierre escalera, sin ABR ni Equipo facilitador).
- **Pendiente de confirmar con María antes de enviar**: modalidad (se asumió remota, sin dato
  explícito de la ficha para este proyecto específico), fechas del diagnóstico y disponibilidad
  del equipo técnico de AMV para las sesiones de Servicio Técnico.
- **`fecha_arranque_deseada`** (dato directo del usuario, 2026-09-23, no de la ficha): Kick-off
  martes 29 de septiembre de 2026, 10:00-11:00. Sesiones siguientes: martes y jueves de 10:00 a
  12:00, a partir de la semana del 5 al 9 de octubre. Con las 12 sesiones de 2h (Diagnóstico,
  Adopción e Implementación × 2 funciones) más 1 semana de Construcción sin sesión (19-23 oct,
  cae justo donde tocarían 2 slots Tue/Thu, se saltan), el calendario completo de "Cómo
  arrancamos" (`.steps-calendar`) corre de fines de septiembre a mediados de noviembre. Detalle
  fecha por fecha en `index.html` → `.steps-calendar`. `resultados_esperados`: sin dato
  explícito del cliente — la proyección se redactó desde el alcance ya definido (cerebro digital
  operando hacia mediados de noviembre).
