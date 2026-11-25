# Brief · Dra. Bethania · Servicio de Habilidades (CAI-108)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Dra. Bethania
- **Slug**: `dra-bethania-cai108`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-108`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construir en ChatGPT un Cerebro Digital para la consulta de fertilidad de la Dra. Bethania, con la historia clínica digital, los documentos y el resumen de cada consulta, la grabación y transcripción, una base clínica de guías y evidencia y un componente de mercadeo, en dos opciones (en casa o en conjunto), como primera etapa de una modernización que luego se extiende a Fertilab
<!--auto:inicio-->
- **Alcance**: 11 entregables en 7 bloques · 32 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana (19/11/2026): propuesta CAI-108 para la Dra. Bethania, con Flavia Martínez como asesora, a partir del mensaje de la doctora pegado en la sesión. Ivana eligió tres de las áreas que la doctora lista (documentos y materiales al paciente, historia clínica digital y base de datos, revisión clínica asistida por IA), las agrupó en un solo Cerebro Digital y pidió mencionar para una siguiente etapa lo que no pueda hacerse. Ajuste del 20/11/2026 (Ivana, con lo que conversó la asesora con la doctora): dos opciones de modalidad como en CAI-096, ChatGPT como herramienta, levantamiento exhaustivo como primer paso, grabación y transcripción de consultas, resumen de la consulta para el paciente y componente de mercadeo
- **Fuente del insumo**: Mensaje de la Dra. Bethania con sus objetivos y ajustes del 20/11/2026 con lo conversado con ella (pegados por Ivana). Sin Ficha de Levantamiento ni transcripción de la reunión
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (19/11/2026): propuesta CAI-108 para la Dra. Bethania, con Flavia Martínez como asesora, a partir del mensaje de la doctora que Ivana pegó (sin Ficha de Levantamiento ni transcripción). Falta el apellido de la doctora: el deck dice «Dra. Bethania».
- Alcance (Ivana): de las seis áreas del mensaje entran tres (documentos y materiales al paciente, historia clínica digital y base de datos, revisión clínica asistida por IA), agrupadas en un solo Cerebro Digital. Indicación posterior de Ivana: la IA como apoyo a las decisiones médicas queda como una base dentro del cerebro, según la información que se pueda cargar (guías, consensos y evidencia); la parte avanzada (revisión y auditoría clínica) va a otra etapa más especializada. Lo demás va en «Para una siguiente etapa» a pedido de Ivana: automatización de citas y WhatsApp, estimaciones individuales de probabilidad de embarazo, integración con los sistemas actuales con control de accesos y respaldo, revisión y auditoría clínica avanzada, extensión a Fertilab, y soporte y mejoras.
- Horas (decisión mía a partir de lo que dijo Ivana): ella dijo «10-12 h, tú indícame según lo que te marque». La referencia es 6 h para un cerebro ligero y 12 h para uno profundo; este lleva datos clínicos estructurados, documentos y revisión con evidencia, así que puse 12 h: 4 h por entregable. Si Ivana prefiere 10 h, se baja la historia clínica a 2 h o un entregable a 2 h.
- El pedido de la doctora es de implementación: quiere un equipo que diseñe, programe, integre y ponga en marcha, con soporte posterior, y aclara que no busca solo capacitación. Habilidades construye con la doctora, guiada por Intezia. Lo que requiere programar e integrar queda en la siguiente etapa. Hay que alinear esa expectativa con Flavia antes de la presentación (puede ser un caso de Desarrollo).
- Enfoque del cuadro Impacto: reenfoque (Ivana, 19/11/2026), sin cifras ni nómina. El texto recoge lo que dice la doctora: más tiempo para la atención humana y cercana, con la decisión clínica en sus manos.
- Herramienta de IA sin nombrar (Ivana). La doctora no pidió ninguna; la conexión con sus herramientas se confirma en el arranque según sea posible (indicación de Ivana, 19/11/2026: se dice en «Cómo trabajamos» y en el hito de arranque) y la atención de pacientes y las citas se hacen en la etapa posterior. El deck no menciona el acceso a Claude desde Venezuela ni VPN.
- Hechos de la portada: salen del mensaje de la doctora (migrar del papel, estandarizar récipes e informes, contrastar con guías). Que los documentos hoy se preparen paciente por paciente y que roben tiempo a la atención es una inferencia mía a partir de su frase sobre perder tiempo: confirmar con Flavia.
- Datos de pacientes: no se cargan sin autorización y sin definir antes confidencialidad, accesos y respaldo (la doctora lo pide). No se afirma cumplimiento de ninguna norma. No se prometen estimaciones de probabilidad de embarazo: van a la siguiente etapa.
- Sin siglas de procedimientos (FIV, ICSI): se usa «tratamientos de fertilidad». Fertilab se nombra solo como extensión futura. Sin personas ni otros clientes nombrados. No se usa la experiencia de la doctora ni su trayectoria.
- División Educación y alianza = no: tomados por mí, no los dio Ivana. Seguimiento 30-60-90 incluido (estándar de Habilidades). Sin facilidad de pago (omitir: pago, regla permanente). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23). La doctora pide tiempos estimados, presupuesto y modalidad de acompañamiento: los tiempos se acuerdan en el arranque y el valor lo pone Ventas. La experiencia en proyectos similares y las tecnologías que se recomiendan no van en el deck (no se nombran casos ni herramientas).
- Contacto de la última slide: Flavia Martínez, asesora comercial; correo y teléfono tomados de las propuestas DET-060 y DET-061, no confirmados para esta.
- AJUSTE 20/11/2026 (Ivana, con lo que conversó la asesora con la doctora). **Dos opciones de modalidad**, como en CAI-096: **A en casa** (Intezia levanta, construye internamente y hace la implementación o enseña a adoptarlo; la doctora se conecta en línea para ver avances y recibe reportes y actualizaciones) y **B en conjunto** (la doctora construye con Intezia guiando, como estaba). Ambas con el mismo total, para que se elija por preferencia y no por valor; una sola hoja de inversión, con la nota de que el valor es el mismo (como quedó CAI-096).
- Horas (decisión mía, avisar a Ivana): suben de 12 a **16 h por opción** porque entran el levantamiento exhaustivo, el resumen de la consulta, la grabación y transcripción y el componente de mercadeo. Reparto igual en las dos: levantamiento 2 h, construcción 10 h (historia clínica 2, documentos 2, resumen 1, grabación 1, base clínica 2, mercadeo 2) y pruebas y adopción 4 h. En la A, la construcción (10 h) es asíncrona de Intezia y con la doctora van 6 h (levantamiento y adopción); en la B las 16 h son con la doctora. Se muestran las horas asíncronas por pedido de Ivana (como en CAI-096, excepción a §4.23 punto 4). Si Ivana prefiere mantener 12 h, se baja la construcción a 6-7 h.
- Calendario y viaje: la doctora viaja el 18 de diciembre y quiere arrancar lo antes posible. La propuesta no lleva fechas (§4.23): dice que las dos opciones se piensan para avanzar antes de su viaje, sin dar la fecha, y que en la A ella sigue los avances en línea. Las fechas concretas van en el kickoff si Ivana lo pide.
- Herramienta: **ChatGPT** (la doctora ya trabaja en ella y tiene su material bajado y estructurado). Se nombra en la portada, el alcance, la inversión y las licencias. El levantamiento confirma qué plan tiene y qué configuración de privacidad aplica, por los datos de pacientes; no se afirma ningún cumplimiento normativo.
- Levantamiento exhaustivo: es el primer paso de la ruta (fase Base, 2 h, igual en las dos opciones) y la página 2 dice que los puntos nuevos se terminan de definir ahí. Confirma alcance final, sistemas que usa hoy, material estructurado, plan y privacidad de ChatGPT, presencia digital.
- Grabación y transcripción de las consultas: con Granola o cualquier herramienta de transcripción que se conecte con otras (lo que Ivana dijo a la doctora). Añadí que la grabación exige el consentimiento del paciente (decisión mía, por los datos clínicos): confirmar con Ivana.
- Resumen de la consulta para el paciente: documento práctico que sale de la grabación y la transcripción y se envía con el récipe; entregable propio (CD1-4, 1 h) y aparece en la slide de entregables.
- Mercadeo y redes sociales: la doctora lleva sus redes sola. Entra contenido para redes, análisis de mercado y lo que surja en el levantamiento sobre su presencia digital (CD1-7, 2 h); no se incluye pauta ni manejo de campañas. El cuarto dato de la portada («Redes») sale de lo que contó la doctora; que le falte tiempo es inferencia mía: confirmar con Flavia.
- El mismo texto de impacto (reenfoque) se amplió con «contenido para redes». Sin nombrar personas ni otros clientes.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Apellido de la doctora y si el cliente es ella o Fertilab (hoy el deck es de la consulta particular).
- Horas: 16 h por opción (decisión mía, antes 12 h); confirmar con Ivana o volver a 12 h.
- Qué plan de ChatGPT tiene la doctora y qué configuración de privacidad aplica (se confirma en el levantamiento, por los datos de pacientes).
- Qué herramienta de transcripción se usa (Granola u otra), quién la contrata y cómo se obtiene el consentimiento del paciente para grabar.
- Sistemas que usa hoy la consulta (agenda, WhatsApp, historias) y material ya estructurado: se confirma en el levantamiento.
- Qué guías, consensos y evidencia aporta la doctora para cargar al cerebro.
- Qué incluye lo de mercadeo según su presencia digital actual (cuentas, frecuencia, qué analizar): se define en el levantamiento.
- Fechas de las dos opciones frente al viaje del 18 de diciembre: se fijan en el kickoff (no van en la propuesta).
- Alinear la expectativa con Flavia: la doctora quiere implementación y soporte; la Opción A se acerca (Intezia construye), pero programar e integrar sigue en la siguiente etapa (puede ser Desarrollo).
- Valor, descuento y total: una sola hoja, campos vacíos para Ventas (el mismo valor para A y B).
- Correo y teléfono de Flavia Martínez para esta propuesta.
- Confirmar con Ivana si el programa lleva certificado.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py dra-bethania-cai108      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh dra-bethania-cai108             # verifica, genera el PDF y ajusta los campos
```
