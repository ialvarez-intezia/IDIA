# Brief · Somos Corpos · Servicio de Habilidades (CAI-048)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Somos Corpos
- **Slug**: `somos-corpos-cai048`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-048`), presentada al cliente como **propuesta de proyecto**; formato compacto de 7 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Fundamentos de inteligencia artificial con Claude, de cero a experto, para dos personas de Somos Corpos: partir de lo básico y llegar a usar Claude con criterio propio en su trabajo de cada día, con el mismo lenguaje que ya recibieron los 16 líderes en la Fase 1
<!--auto:inicio-->
- **Alcance**: 8 módulos en 4 niveles · 16 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Retorno · 6 Inversión · 7 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Conversación comercial de la asesora con la Gerencia de Tecnología (09/10/2026) e instrucciones de Ivana del 09/10/2026; ajuste del mismo día: sin mencionar el cargo de las dos personas, enfocado en fundamentos de IA con Claude «de 0 a experto», sin slide de entregables y con un título menos literal. No hay Ficha de Levantamiento ni grabación de la reunión. Base de contenido: CAP-045 Fase 1 (Fundamentos con Claude para 16 líderes)
- **Fuente del insumo**: Contexto comercial de la asesora (sin Ficha ni grabación) y CAP-045 como base
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Nombre del cliente: el pedido dice «Somos Corpos» y la base (CAP-045, dashboards) dice «Grupo Corpos». Se usó «Somos Corpos». Confirmar con la asesora. División Educación y sin alianza (inferidas, como en las propuestas anteriores). Asesora Flavia Martínez, con su contacto de la CAP-045.
- Sin Ficha de Levantamiento ni grabación: todo sale del contexto que dio la asesora tras la llamada de la Gerencia de Tecnología, más las instrucciones de Ivana. Por eso la portada no cita dolores dichos por el cliente: los 3 datos son puntos de partida (16 líderes que ya trabajan con Claude, trabajo uno a uno y 4 niveles que cierran con algo propio funcionando).
- Versión del 2026-10-09 (Ivana): el documento ya no menciona el cargo de las dos personas (se dice «dos personas» y «cada persona»), se enfoca en fundamentos de inteligencia artificial con Claude «de 0 a experto», quita la slide de entregables y cambia el título por uno menos literal. «De cero a experto» es la promesa del proyecto: se sostiene con 4 niveles y con lo que cada persona debe poder hacer al cerrar (usar Claude de forma autónoma, con un pedido bien armado, su proyecto, un artefacto, una skill y criterios de uso seguro). No se mide un nivel de «experto» con una prueba: se mide con el uso real y el seguimiento a 30, 60 y 90 días.
- Lenguaje delicado (Ivana): no se nombra a nadie (ni a la Gerencia de Tecnología ni a las dos personas), no se menciona su edad ni su perfil tecnológico, y no se habla de no quedarse atrás ni de que ellas lo hayan pedido (lección de la CAI-045). El documento lo pueden leer las propias personas: sin jerga y con cada término nuevo explicado (proyecto, skill, artefacto).
- Horas (Ivana, 2026-10-09): 8 h por persona, 16 h en total (la Fase 1 de los 16 líderes fue de 6 h por grupo). 4 niveles de 4 h (2 h con cada persona), con 2 módulos cada uno (1 h con cada persona): fundamentos de Claude, pedirle bien las cosas, crear (proyecto y artefacto) y uso experto y seguro (skill y guía). Las horas por fase salen de ahí: Fundamentos 8 h, Crear 4 h, Experto 4 h. La reunión de arranque (1 h) va aparte y no suma horas.
- Sin slide de entregables (omitir: ["entregables"], Ivana): lo que se logra en cada nivel va en el «Alcance» (columna de la derecha, con un «Al cerrar: …») y la ruta; el detalle de cada módulo queda en este programa.md para la reunión de arranque. El deck pasa a 7 slides y a 5 campos editables (inversión), sin las cajas Entregables ni Acreditacion.
- Individual: la asesora recomienda sesiones individuales «o al menos la primera». Se asumió individual en todo el proyecto, a su ritmo. Si la mayor parte fuera conjunta, cambian la modalidad, los textos de «uno a uno» y las horas. Confirmar con la asesora. Cómo se reparten las 8 h en encuentros se acuerda en la reunión de arranque (§4.23): ni sesiones ni semanas en el deck.
- Apoyo en la Fase 1 (CAP-045): los 4 niveles recorren sus mismos módulos (fundamentos y tres formas de uso, prompting con rol, contexto, tarea y formato, Projects y análisis de documentos, Artifacts, Skills y ética y uso seguro) para que hablen el mismo lenguaje. Los resultados de esa fase (dashboard de impacto) NO se citan: Ivana lo decidió para no comparar. El clon digital queda fuera y se plantea como siguiente paso (`ruta.siguiente_etapa` y `fuera_alcance`), apoyado en la Fase 2 de la CAP-045.
- Licencias y cuentas de Claude: Ivana pidió no mencionarlas, así que el deck no habla de cuentas, planes ni licencias. Antes de arrancar hay que confirmar quién tramita y paga las de las dos personas. Tampoco se agrega nota de acceso: el resto de los líderes ya trabaja con Claude.
- Sin facilidad de pago (criterio de Ivana en las últimas propuestas): ventas comunica el plan por otro medio. Sin certificado de participación (dos personas, programa a la medida).
- Retorno en modo método, sin cifras ni posiciones: no hay datos del cliente.

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

- Confirmar el nombre del cliente («Somos Corpos» o «Grupo Corpos») y el código CAI-048.
- Definir inversión, descuento y total (campos vacíos para ventas); línea de facturación (moneda y tasa) por confirmar con ventas.
- Confirmar con la asesora que el trabajo es individual de principio a fin y las 8 h por persona.
- Confirmar quién tramita y paga las cuentas de Claude de las dos personas (el deck no las menciona).
- Confirmar la modalidad (remota o presencial) y el calendario en la reunión de arranque.
- Confirmar con Ivana que «quitar lo de entregables» era quitar la slide completa (así se hizo) y no solo la palabra.
- Revisar con la asesora el lenguaje del documento antes de enviarlo: lo pueden leer las propias personas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py somos-corpos-cai048      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh somos-corpos-cai048             # verifica, genera el PDF y ajusta los campos
```
