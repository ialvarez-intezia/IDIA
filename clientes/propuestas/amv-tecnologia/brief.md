# Brief — AMV Tecnología

---

## Datos administrativos

- **Empresa**: AMV Tecnología (distribución de dispositivos e insumos médicos oftalmológicos —
  óptica, incluye lentes intraoculares)
- **Sector**: Distribución médica especializada (oftalmología)
- **Tamaño**: Micro / Pyme (menos de 50 empleados) — 20 personas en total
- **Slug**: `amv-tecnologia`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — servicio de interés único declarado en la ficha (no combo).
- **Tipo de documento**: Detección (`DET-019`) · Fundamentals (2h grupal, presencial) +
  auditoría de 3 áreas (Logística, Comercialización y Venta, Administrativo), 4 horas por área
  (12h, remoto), 14h totales, modalidad mixta.
- **Eje temático**: Auditar Logística, Comercialización y Administrativo con un logro inmediato
  en cada área, empezando por lo que AMV ya validó por su cuenta: consolidar facturas en minutos,
  no en horas.
- **Fecha del brief**: 2026-09-23
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento AMV Tecnología**
(`Levantamiento_AMV_Tecnologia_2026-09-22.pdf`, registrada 2026-09-22), elaborada por la asesora
**María Iribarren**, más el contexto adicional que la asesora aportó directamente sobre la
reunión (tono, matices de cada socio, y las 2 propuestas paralelas pedidas por el cliente).

## Contacto

- **Asesora comercial**: María Iribarren.
- **Contacto / decisor principal**: Juan Vázquez, Socio — lidera el proyecto, fue "la voz
  cantante" de la reunión, decisor principal en esta conversación.
- **Co-contacto**: Yamil Yaguas, Socio — contacto original (conoció a María en una rueda de
  negocios del IESA), presente en la reunión.
- **Tercer socio**: no participó en la reunión, sin nombre registrado en la ficha.
- **Servicio previo con Intezia**: ninguno — primer contacto. Sin propuesta previa de Intezia
  (sí hubo una charla/demo informal de un freelancer de redes sociales, sin metodología).

## Decisión de alcance — bloqueante, confirmada con el usuario (2026-09-23)

La ficha (Bloque F) y el mensaje de la asesora piden explícitamente **2 propuestas en
paralelo**, cita: *"El cliente pidió explícitamente DOS propuestas en paralelo: (1) Detección
para los 3 grupos definidos, y (2) un proyecto aparte de Cerebro Digital."*

**Este documento es únicamente la Propuesta 1 (Detección)**, por instrucción explícita del
usuario ("vamos a hacer la propuesta 1"). Antes de construir, se preguntó al usuario (vía
`AskUserQuestion`) cómo manejar 2 puntos que afectaban directamente el contenido de este deck:

1. **¿Mencionar el Cerebro Digital dentro de este deck?** → **Respuesta: no, completamente
   aparte.** Mismo criterio ya usado con las 2 propuestas de Dumogas (DET-017/DET-018): cada
   documento queda autocontenido, sin referencias cruzadas visibles al cliente. El Cerebro
   Digital **no aparece en ningún lugar de este deck** (ni en Notas, ni en Próximos pasos).
2. **¿Adelantar ya una recomendación de licencias Claude Teams?** → **Respuesta: sí, pero como
   nota aparte, no como AcroForm de propuesta.** Se preparó por separado:
   `clientes/propuestas/amv-tecnologia/recomendacion-licencias-claude.md` — documento corto,
   con datos reales de pricing verificados por WebSearch (claude.com/pricing), sin mezclarse con
   este deck ni presuponer su aprobación.

**El Cerebro Digital y la recomendación de licencias NO se construyen como propuesta formal
todavía** — quedan documentados aquí como contexto para cuando el usuario pida construirlos.

## 3 grupos de Detección (dato directo de la ficha, sin ambigüedad)

1. **Logística** — compras internacionales, importación, almacén y despacho.
2. **Comercialización y Venta** — incluye Customer Service, gerencia y vendedores (~7-8
   personas, contando a los socios que también venden).
3. **Administrativo** — facturación, cuentas por pagar/cobrar, tesorería, contabilidad.
   Responsable: Jorge (administrativo-contable).

**Servicio Técnico queda explícitamente FUERA de este alcance** — la ficha lo declara "4to
grupo pendiente para una fase posterior, no incluido en este primer alcance". El `Proceso 3`
de la ficha (transferencia de conocimiento técnico) pertenece a este grupo excluido — **no se
usa en el deck**, y de hecho es parte de lo que después alimentaría al Cerebro Digital
("centralizar conocimiento disperso... en un 'cerebro digital' consultable").

**Headcount**: 20 personas en la organización en total. La ficha no da headcount exacto por
área salvo Comercialización (~7-8). No hace falta una cifra exacta por área para dimensionar
las sesiones (no dependen del headcount, solo Fundamentals tiene tope de 25, y 20 personas está
cómodamente debajo).

## Dimensionamiento (lineamiento por defecto — sin instrucción de acortar horas)

- **4 horas por área** × 3 áreas = **12 horas**.
- **+ 2 horas de Fundamentals grupal** (20 personas, dentro del máximo de 25).
- **Total: 14 horas.**
- **Modalidad mixta** (dato explícito de la ficha y del mensaje de la asesora): **Fundamentals
  presencial en Valencia** (sede principal, "primer contacto presencial" pedido por el cliente)
  + **las 3 sesiones de área en remoto** ("el resto remoto"). Interpretación razonable no
  cuestionada por el usuario al invitar preguntas — si la lectura correcta fuera otra
  combinación presencial/remoto, ajustar antes de enviar.

## Logro inmediato — con precedente real y validado (a diferencia de Andrómeda)

A diferencia de Andrómeda (DET-016, donde el cliente pidió explícitamente evitar automatizar
procesos triviales), aquí el cliente **ya probó y validó un logro inmediato por su cuenta**:

> *"Juan probó Claude él mismo con una tarea típica: separar productos y precios de 80 facturas
> con miles de items para consolidar documentos de 8 horas manuales a 10 minutos."* (Bloque D,
> cita textual; repetido como "quick win" ya identificado en Bloque específico Detección).

Se usa el patrón `toyocentro/velas-3n` (auditoría + construcción de un logro tangible en la
misma sesión de 4h), **no** el patrón `pilotes-perforados/andromeda` (auditoría pura). El logro
de facturas se ancla explícitamente al grupo **Administrativo** (el proceso pertenece a "Equipo
de administración/facturación", Bloque C). Logística y Comercialización también prometen un
logro inmediato (mismo patrón general), pero sin un caso pre-validado específico — se define en
la propia sesión de 4h de cada área, igual que Toyocentro con su segundo proceso (WhatsApp).

**Nota**: la ficha también documenta un candidato de automatización para Logística (sugerencia
de orden de compra por rotación de inventario de lentes intraoculares, Bloque C Proceso 2) —
pero el propio Bloque F indica que ese caso específico es el que alimenta el **Cerebro Digital**
("sugerencia automática de orden de compra según rotación de inventario..."), no el logro
inmediato de la sesión de Detección. Se menciona en el Diagnóstico del deck como hallazgo real
de Logística, sin prometerlo como el logro inmediato de esa sesión (para no pisar el alcance de
la Propuesta 2, que no se construye aquí).

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: mixto (Google Workspace + Microsoft 365).
- **Uso de IA hoy**: licencias de Microsoft 365 con Copilot y Google Workspace con Gemini, pero
  uso real básico (redacción de correos, cálculos simples). Jorge (administrativo-contable) es
  quien más lo usa — hizo diplomados y lo aplica con Power BI para análisis contable más técnico.
- **Sistema de gestión**: ERP propio a la medida del sector, ya en la nube — se habla de "su
  sistema de gestión" en el deck, sin usar la sigla ERP de cara al cliente (§4.12, evitar jerga
  innecesaria cuando hay alternativa en lenguaje natural).
- **Capacidad técnica real**: están integrando APIs con bancos activamente — señal de que hay
  capacidad interna real para integraciones futuras (dato de contexto, no se promete nada sobre
  integraciones en este documento de Detección).
- **Cuál les gustaría incorporar**: Claude (Anthropic) — Juan ya lo probó con resultado medible.
  Se menciona como contexto real (no como recomendación previa al diagnóstico — Metodología ABR,
  mismo criterio que toyocentro/andromeda): el Reporte Final es quien entrega la recomendación
  formal de ecosistema de IA.
- **Sin política de datos/seguridad formal aún.** Preocupación real por seguridad: evalúan
  migrar su servidor actual a uno propio; sin VPN corporativo (Juan usa un VPN personal).
- **Regulación sectorial**: auditorías externas de marcas como Johnson & Johnson que exigen
  acuerdo de calidad (trazabilidad, condiciones de ambiente, entrenamiento documentado). Contexto
  interno únicamente — no se nombra la marca en el deck; se refleja de forma genérica como
  necesidad de procesos trazables y documentados (conecta con su propia expectativa de "dejar
  procesos documentados que no dependan de una sola persona").

## Objetivo final esperado del Reporte Final (Bloque G)

Detectar oportunidades de optimización y reducción de costos por área, evitando seguir
creciendo en headcount operativo; priorizar la inversión en licencias/herramientas con datos
reales en vez de comprar a ciegas. Éxito declarado ("esto es exactamente lo que
necesitábamos"): base objetiva para decidir qué licencias comprar + procesos documentados que
no dependan de una sola persona (continuidad del negocio).

## Decisiones confirmadas / sin ambigüedad

1. **3 grupos de Detección** (Logística, Comercialización y Venta, Administrativo) — dato
   directo de la ficha, Servicio Técnico explícitamente fuera.
2. **Con logro inmediato por sesión** — a diferencia de Andrómeda, el cliente ya validó uno
   (facturas) y busca explícitamente automatizar tareas repetitivas.
3. **Modalidad mixta**: Fundamentals presencial en Valencia, sesiones de área remotas.
4. **Sin Cerebro Digital ni recomendación de licencias dentro de este deck** — confirmado con
   el usuario, cada uno queda como entregable aparte.
5. **Sin certificado de participación** en Entregables — Detección es una auditoría, no un
   curso (`deteccion-sin-certificado.md`).
6. **Sin nombrar la sigla ERP** ni la marca J&J de cara al cliente.
7. **Sin pre-recomendar Claude** como herramienta antes del diagnóstico — se menciona como
   contexto real (Juan ya lo probó), la recomendación formal llega en el Reporte Final.

## Impacto (§4.9, verificado por WebSearch 2026-09-23)

**Ardent Partners — Accounts Payable Metrics That Matter (2025)**: la tasa promedio de
procesamiento de facturas sin intervención manual (touchless) es 32.6% en la industria, contra
49.2% en las organizaciones de mejor clase (best-in-class); el mejor de su clase procesa una
factura en 3.1 días contra 17.4 días del promedio (~5.6× más rápido); el costo promedio por
factura es $9.40 contra $2.78 del mejor de su clase (~70% menos costo); la tasa de excepciones
que requieren revisión manual es 22% en el promedio, contra 9% en el mejor de su clase. Fuente
verificada de forma cruzada (ardentpartners.com directamente + una distribución del reporte vía
Pagero) — se descartaron cifras similares de blogs de proveedores (stealthagents.com,
parseur.com) que no permiten confirmar el estudio original citado, mismo criterio que en
Dumogas DET-017/018. Elegido específicamente porque conecta directo con el propio quick win
validado del cliente (facturas).

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: María Iribarren.

## Corrección de lenguaje (2026-09-23, instrucción directa del usuario)

El deck original centraba el título, el hook de Impacto, el ROI y varios bullets en el
ejemplo puntual que Juan dio en vivo ("consolidar 80 facturas, de 8 horas a 10 minutos").
El usuario pidió **retirar esa mención específica de todo el deck** (título incluido): fue
un ejemplo anecdótico de algo que él ya hizo solo, no debe centrar la venta del proyecto
completo — riesgo de disonancia si se sobre-enfoca en un solo caso. Se conserva la mención
**genérica** ("el equipo ya probó por su cuenta que la IA reduce tiempo real / funciona"),
sin nombrar el proceso ni las cifras. Título nuevo: "Del criterio manual a la decisión con
datos." (antes: "De 8 horas a 10 minutos."). El detalle sigue documentado en la sección
*"Logro inmediato — con precedente real y validado"* de este brief como contexto interno —
no aparece en el deck de cara al cliente.

## Notas internas

- Caso base estructural: `toyocentro/` (DET-014) — mismo patrón de Fundamentals + N áreas a 4h
  con logro inmediato, roadmap `.rmx-linear` de 3 etapas, Beneficios v3, Cierre escalera, precio
  estándar. Adaptado de 2 a 3 áreas, de presencial puro a modalidad mixta.
- **Jorge (administrativo-contable)**: identificado en la ficha como posible IA Champion (el
  más avanzado internamente, diplomados + Power BI), no asistió a la reunión. Se omite su
  nombre del deck de cara al cliente (mismo criterio "omitir, no inventar"/sin nombres de staff
  que HCA CAI-022 y otros decks de esta sesión) — queda solo como contexto interno aquí, útil
  para que Verónica/María lo sumen a la sesión de Fundamentals si el cliente lo confirma.
- **Pendientes (a confirmar con María antes de enviar)**: fecha exacta del encuentro presencial
  en Valencia y de las 3 sesiones remotas — no se inventan, se coordinan en "Cómo arrancamos".
  El cliente pidió la propuesta "para el día siguiente" de la reunión (urgencia real) — priorizar
  envío rápido una vez revisada.
- **`fecha_arranque_deseada`** (dato directo del usuario, 2026-09-23, no de la ficha):
  Kick-off martes 29 de septiembre de 2026, 10:00-11:00. Sesiones siguientes: martes y
  jueves de 10:00 a 12:00, a partir de la semana del 5 al 9 de octubre. Con la sesión de
  4h/área partida en 2 bloques de 2h, el calendario completo de "Cómo arrancamos"
  (`.steps-calendar`) queda: Fundamentals mar 6 oct, Auditoría Logística jue 8 + mar 13 oct,
  Auditoría Comercialización jue 15 + mar 20 oct, Auditoría Administrativo jue 22 + mar 27
  oct. `resultados_esperados`: sin dato explícito del cliente — la proyección de resultado
  se redactó desde el alcance ya establecido (3 áreas auditadas con logro inmediato en 4
  semanas), sin nombrar el caso puntual de facturas (ver corrección de lenguaje abajo).
