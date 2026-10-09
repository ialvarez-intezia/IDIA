# Brief · Marcelo Restrepo · Servicio de Habilidades (CAI-040)

## Actualización 2026-10-08 · CAI-040 y CAI-041 unificadas en una sola propuesta (8 slides, plantilla v2) · VIGENTE

Instrucción directa del usuario: «ajustar la CAI-040 y la CAI-041, unificarlas y en la hoja de cotización un solo
espacio para sumar ambos precios». Las dos se habían pedido juntas por la asesora y salieron el 06/10/2026 por
separado. Ahora hay **una sola propuesta bajo el código CAI-040**, en la plantilla v2 (8 slides: portada · alcance ·
ruta · cómo trabajamos · entregables · retorno · inversión · próximos pasos). La carpeta de la CAI-041 quedó archivada
en `_anterior-cai041/` (no se borró; ya no aparece en `clientes/INDEX`) y el `datos.json` v1.4 de la CAI-040 en
`_anterior-cai040/`. Los PDF originales están en `_pdf-anteriores/` y en `_anterior-cai041/`.

### Decisiones del usuario al preguntar

| Pregunta | Respuesta |
|---|---|
| Código | **CAI-040 para las dos** |
| Calendario | **Una tras otra, 6 semanas**: mensajes en las semanas 1 a 3 (2 sesiones por semana, 12 h) y Cerebro Digital en las 4 a 6 (1 sesión por semana, 6 h). Total 18 h, igual a la suma de las dos. El orden (mensajes primero) lo propuso el sistema: confirmar |
| Hoja de cotización | **Hoja estándar más un espacio para sumar ambos presupuestos**: a la izquierda dos cajas, «Clon digital» y «Redes sociales»; a la derecha una caja que suma ambas, más Descuento y TOTAL como siempre |
| Facilidad de pago | **Omitirla** (`omitir: ["pago"]`), como en la CAI-032 y la DET-024 |

### Cómo quedó la hoja de cotización (slide 7)

- Izquierda, bajo «Notas»: «Valor por parte» con dos tarjetas (Parte 1 «Clon digital», Parte 2 «Redes sociales»), cada
  una con su caja editable vacía (`PrecioParte1`, `PrecioParte2`). El licenciamiento ya no lleva tarjeta propia (compartía
  esa zona): pasó a la primera línea de `Notas`.
- Derecha: la caja base se llama «Suma de ambas partes» y **suma sola las dos cajas** en Adobe Reader (entiende «1.200»,
  «1.200,50» y «2.250 REF»; si las partes están vacías respeta un monto tecleado a mano). Descuento y TOTAL (base menos
  descuento) quedan como en la hoja estándar. Todos vacíos para ventas.
- Preview macOS no ejecuta el JavaScript de cálculo: la suma funciona solo en Adobe Reader (igual que el TOTAL de siempre).
- «Clon digital» es la palabra del usuario para el Cerebro Digital. El resto del deck dice «Cerebro Digital»; la
  tarjeta dice «Clon digital · Cerebro Digital de marca personal · 3 sesiones» para unir las dos.
- Es una **opción nueva del generador** (`inversion.partes`, `inversion.etiqueta_suma`), sin efecto si no se usa. Ver
  `aprendizajes.md` (2026-10-08).

### Cómo se unificó el contenido

- 9 entregables en 6 bloques (Criterio y aviso, Instagram, TikTok, Marca, Video, Diseño) y una línea de trabajo, 2 fases
  (Mensajes, Cerebro). Las sesiones y entregables son los de cada propuesta original, sin cambios.
- **Un solo kick-off de 1 h** (aparte, sin horas): antes había uno por propuesta. Reúne los dos objetivos.
- Mensajes (CAI-040): Claude solo lee y avisa. Cerebro (CAI-041): Claude prepara, Marcelo monta y publica. Las dos
  frases están en «Cómo trabajamos» y en «Fuera de este alcance». «Cómo cuidamos sus datos»: mensajes con datos de
  terceros (solo lectura) y cerebro sin contenido sin publicar ni datos de terceros.
- Retorno unificado (mensajes y piezas), un solo seguimiento 30-60-90 y una sola cuenta de Claude (un solo plan).
- Sin mencionar otras herramientas ni el parentesco bancario (contexto interno).

### Pendientes (a confirmar antes de reenviar)

- Valores de «Clon digital» y «Redes sociales» y descuento (campos vacíos para ventas; 18 h en total) y cómo se
  comunica el plan de pago (no hay slide).
- Orden de las partes (mensajes primero) y estructura de 9 sesiones en 6 semanas con servicio y la asesora.
- Prueba real de TikTok e Instagram con la cuenta de Marcelo; qué incluye su plan de Claude en diseño; si el cerebro va
  con Obsidian; que el cliente entiende que Claude no monta el video.
- La asesora es María Iribarren (supuesto) y su cargo en la última slide.
- Las dos propuestas originales ya salieron el 06/10/2026 (`fecha_entrega` se respeta): confirmar si se reenvía la
  unificada y avisar al cliente de que reemplaza a las dos.

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Marcelo Restrepo
- **Slug**: `marcelo-restrepo-cai040`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-040`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Monitoreo diario de los mensajes directos de Instagram y TikTok con Claude, desde el navegador, para que Marcelo no pierda personas clave, invitaciones a eventos ni propuestas. Claude solo lee y avisa; no responde
<!--auto:inicio-->
- **Alcance**: 9 soluciones en 6 bloques · 18 h de sesión · 6 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Enviada` (2026-10-06, por convención: terminado = enviado)
- **Asesora comercial**: María Iribarren · +58 414-0570056 · miribarren@intezia.com (datos de `fivenca-acompanamiento/`; el deck no lleva slide de cierre ni contacto). El usuario dijo solo «María»: confirmar que es la misma.
- **Ficha Comercial Intezia**: no hay. Todo sale del contexto comercial que la asesora compartió por escrito (el cliente, lo que necesita y lo que pide al equipo) y de la instrucción directa del usuario.
- **fecha_arranque_deseada**: no se preguntó; sin esta respuesta no hay Calendario de inicio con fechas (semanas relativas al arranque).
- **resultados_esperados**: no se preguntó; el retorno va en modo método, sin cifras.

## Cuenta (contexto interno, NO va en el deck)

- **Quién es:** creador de contenido de finanzas con marca personal propia y presencia fuerte en Instagram y TikTok. Es hijo del presidente de un banco: relación muy valiosa para Intezia. El deck no menciona ni el parentesco ni el banco.
- **Qué le pasa:** miles de mensajes directos sin responder en las dos redes. Le preocupa perderse oportunidades (personas clave, invitaciones a eventos, propuestas). Vio por casualidad un mensaje que le pedía reunirse con un presidente. El episodio no va en el deck.
- **Qué pidió (y qué no):** estar al tanto de sus mensajes, **no responderlos**. No quiere un chatbot que conteste. De ahí que la propuesta diga que Claude solo lee y avisa.
- **Cómo lo quiere construir:** con él, en sesiones en vivo, y que quede usándolo en su día a día.
- **Son 2 propuestas.** Esta es la **1** (monitoreo de mensajes). La **2** es un Cerebro Digital enfocado en su marca personal, para editar videos y hacer diseños para su contenido: hecha como **CAI-041** (`marcelo-restrepo-cai041/`, 6 h). Conviene que no repitan sesiones ni línea base entre sí.
- **Qué pidió la asesora al equipo:** (a) la estructura de la propuesta: sesiones, horas y entregables de cada parte; (b) opinión sobre la viabilidad del monitoreo en TikTok; (c) opinión sobre una aplicación que un conocido le recomendó al cliente. **Por instrucción del usuario, esta propuesta usa solo Claude en el navegador y no nombra otras herramientas**, de modo que (c) no se evaluó aquí.

## Opinión sobre la viabilidad (para la asesora, no va en el deck)

- **Cómo funciona:** Claude actúa dentro del navegador de Marcelo, con las sesiones de Instagram y TikTok que él ya tiene abiertas. Lee la bandeja como lo haría una persona y arma el aviso. No necesita conectores ni acceso a datos por otra vía.
- **Instagram:** viable en principio desde la versión web de la bandeja de mensajes.
- **TikTok:** la incógnita es de la red, no de Claude. Hay que confirmar con su cuenta real que la bandeja de mensajes esté disponible en la versión web y que no pida verificaciones de seguridad al recorrerla. Recomendación: probarlo con él 15 minutos antes de enviar; si no, queda como primer punto de la sesión 1 (prueba de acceso) y la sesión 4 se ajusta según el resultado.
- **Diario y solo:** hay ejecución programada en el navegador, pero corre solo con el computador encendido y el navegador abierto a esa hora. Es una condición del cliente, no una función a prometer sin condiciones: está en las notas de la inversión.
- **Costo de uso:** el trabajo en el navegador consume más del plan que un chat normal, y recorrer miles de mensajes más. Por eso el rescate de la bandeja va por lotes y el plan adecuado se define en la sesión 1.
- **Riesgo de seguridad:** un mensaje de un tercero es contenido no confiable y puede traer instrucciones ocultas. La defensa de diseño es que Claude solo lee y avisa: no responde, no envía, no abre enlaces ni archivos. Conviene decírselo al cliente así.
- **Datos de terceros:** la bandeja contiene datos de personas ajenas. Qué se conserva del aviso diario y dónde se acuerda en la sesión 1.
- **Cuentas:** el uso automatizado de las redes puede chocar con sus condiciones de uso. Es un riesgo menor porque Claude solo lee desde la sesión de Marcelo, pero la asesora debe tenerlo presente al venderlo.

## Plan de sesiones (6 de 2 h, en vivo con Marcelo)

| Sesión | Semana | Contenido | Entrega |
|---|---|---|---|
| 1 · 2 h | 1 | Qué es importante (personas clave, eventos, propuestas), qué es ruido, urgencia y formato del aviso. Línea base del tiempo y de los mensajes por semana. Prueba de acceso a Instagram y TikTok | Guía de prioridad (CA-1) |
| 2 · 2 h | 1 | Instrucción de revisión diaria de Instagram sobre su bandeja real; solo lee y avisa | Revisión diaria de Instagram (IG-1) |
| 3 · 2 h | 2 | Rescate por lotes de la bandeja acumulada de Instagram; el primer lote en la sesión | Primera lista de oportunidades rescatadas (IG-2) |
| 4 · 2 h | 2 | Revisión diaria de TikTok; aquí se ajusta el alcance si la red limita la lectura | Revisión diaria de TikTok (TT-1) |
| 5 · 2 h | 3 | Rescate por lotes de la bandeja acumulada de TikTok | Primera lista de oportunidades de TikTok (TT-2) |
| 6 · 2 h | 3 | Aviso único con ambas redes, hora y ejecución programada, ajuste de la guía, qué hacer si un día no corre | Aviso diario funcionando (CA-2) |

Total: 6 × 2 h = 12 h, más 1 h de kick-off aparte (dejar listo el navegador y acordar la agenda). Máximo 4 h por semana, muy por debajo del tope de 20.

## Qué ve el equipo comercial (puntos para la conversación con el cliente)

- **Se paga por sesiones de construcción en vivo, no por una herramienta:** Marcelo termina usándolo solo. Eso es lo que pidió.
- **Claude solo lee y avisa:** responde de frente a «no quiero un chatbot que conteste».
- **12 h de sesión** (propuesta del sistema, la asesora no dio horas): es el techo del rango de 8 a 12 h por área. Ventas lo cotiza y servicio lo confirma.
- **Licencia de Claude aparte:** necesita su cuenta con un plan de pago. El deck no afirma plan ni precio porque no hay un precio de lista verificado.
- **Sin certificado:** es un proyecto con una persona (§4.21).
- **Cuando se venda esta, la 2.ª propuesta** (CAI-041, Cerebro Digital de marca personal) encaja como siguiente paso natural. Comparten la cuenta de Claude: coordinar agenda.

## Origen y fuente

- **Origen**: Contexto comercial compartido por el usuario el 06/10/2026 (conversación de la asesora con el cliente). Propuesta 1 de 2; la segunda (Cerebro Digital de marca personal) va aparte. Sin Ficha Comercial
- **Fuente del insumo**: Contexto comercial de la asesora; instrucción directa del usuario
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Código CAI-040 dado por el usuario (no aparece en el repositorio). División Educación y alianza «no» inferidas: cliente profesional individual (creador de contenido de finanzas) sin vínculo con Fundación ni alianza. Asesora María (María Iribarren, la de Fivenca): confirmar que es ella. Sin Ficha Comercial: todo sale del contexto comercial que pasó el usuario.
- Esta es la propuesta 1 de 2 que pidió la asesora. La segunda (Cerebro Digital enfocado en su marca personal, para editar videos y hacer diseños) va en otra propuesta y no se menciona aquí. Por instrucción del usuario, la propuesta nombra solo a Claude, trabajando en el navegador de Marcelo, para Instagram y TikTok; no menciona otras herramientas.
- Estructura de sesiones, horas y entregables propuesta por el sistema (la asesora la pidió y no vino definida): 6 sesiones de 2 h = 12 h, una solución por sesión, 2 por semana en 3 semanas, más kick-off de 1 h aparte sin horas (convención del sistema, como CAI-039). 12 h está en el techo del rango de la regla general (8 a 12 h por área) para un proyecto de 3 bloques; confirmar con servicio y ventas.
- Qué pidió el cliente: estar al tanto de sus mensajes, no responderlos; no quiere un chatbot que conteste. Por eso el deck lo dice dos veces (alcance y notas): Claude solo lee y avisa. También es la defensa contra mensajes maliciosos: el contenido de un mensaje ajeno no es una instrucción, y Claude no abre enlaces ni archivos.
- Viabilidad (confirmar antes de enviar): Instagram parece viable desde la versión web. TikTok depende de que su cuenta tenga la bandeja de mensajes en la versión web y de que no pida verificaciones; se prueba en la sesión 1 (prueba de acceso) y se ajusta en la sesión 4. El deck dice «solo lee y avisa» y no promete más de lo que se confirme.
- La revisión diaria programada corre solo con el computador encendido y el navegador abierto. El deck lo dice en las notas de la inversión. Hay que definir con Marcelo el computador y la hora de la revisión.
- Recorrer miles de mensajes consume uso del plan de Claude: el rescate va por lotes y el plan adecuado se define en la primera sesión. El deck no afirma un plan ni un precio (no hay precio de lista verificado).
- Hecho «Miles de mensajes sin responder» (portada): lo declaró el cliente en la conversación comercial, según el contexto de la asesora. No hay cifra exacta ni ficha; el deck cita la fuente como dato declarado. Confirmar con la asesora que el cliente está de acuerdo con que figure.
- Contexto interno que NO va en el deck: parentesco del cliente con el presidente de un banco y la importancia de la relación para Intezia. Tampoco el episodio del mensaje que pedía una reunión con un presidente.
- Retorno en modo método: sin datos del cliente no hay cifras. La meta mide tiempo recuperado y oportunidades atendidas. «Hacia la semana N» es aritmética (3 semanas de trabajo + 13): confirmar con servicio.
- Sin certificado de participación (§4.21): es un proyecto con un solo participante.
- Privacidad: los mensajes contienen datos de terceros. El deck no da a Claude ningún permiso de acción; el tratamiento de esos datos (qué se guarda del aviso, dónde) se acuerda en la sesión 1.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas). 12 h de sesión.
- Prueba real de TikTok y de Instagram con la cuenta de Marcelo antes de enviar o, a más tardar, en la sesión 1: confirmar que la bandeja se puede leer desde el navegador.
- Confirmar con servicio la estructura de 6 sesiones de 2 h y que la línea base y la prueba de acceso caben en la sesión 1.
- Fechas, modalidad (en vivo, remota o presencial) y disponibilidad semanal de Marcelo; computador y hora de la revisión diaria; confirmar el kick-off.
- Cuenta de Claude de Marcelo: si ya tiene plan de pago y cuál. Quién paga la licencia.
- Confirmar que la asesora María es María Iribarren.
- Segunda propuesta (Cerebro Digital de marca personal): hecha como CAI-041; coordinar agenda con esta.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py marcelo-restrepo-cai040      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh marcelo-restrepo-cai040             # verifica, genera el PDF y ajusta los campos
```
