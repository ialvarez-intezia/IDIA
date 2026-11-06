# Brief · Zoom · Servicio de Innovación (INN-006)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Zoom
- **Slug**: `zoom-inn006`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `innovacion`
- **Alianza**: `no`
- **Tipo de documento**: Plan de Innovación · bootcamps de Gems a Skills para 510 personas de todas las áreas de Zoom: 21 encuentros de 2 h (42 h de encuentro), hasta 25 personas por encuentro · calendario con fechas · formato compacto v3 (`INN-006`); formato compacto de 10 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Migrar a Skills los Gems de las 510 personas de Zoom, de todas sus áreas, en bootcamps de 2 horas de hasta 25 personas, antes de que Google retire los Gems
<!--auto:inicio-->
- **Alcance**: 3 encuentros en 1 área · 52 h de trabajo · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Qué está cambiando · 3 Alcance · 4 Ruta · 5 Calendario · 6 Cómo trabajamos · 7 Retorno · 8 Inversión · 9 Facilidad de pago · 10 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana del 27/10/2026: una sola propuesta INN-006, bootcamp para las 510 personas y mencionando las áreas del servicio, tras los mensajes del equipo (las opciones B y C solo cubrían 121 personas y Emma pidió los 510; si Zoom arma los grupos el número de encuentros puede crecer). Parte de la opción A de las tres propuestas INN-006-A/B/C del 26/10/2026. Sin Ficha de Levantamiento ni transcripción
- **Fuente del insumo**: Texto de la dirección y respuestas de Ivana (26/10/2026); documentación de Google para administradores (26/10/2026); dashboards y casos de éxito de Zoom
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Decisión de Ivana (27/10/2026): una sola propuesta INN-006, bootcamp con las 510 personas, mencionando las áreas del servicio. No hay total de personas por área (no se tiene), así que no se ofrecen las opciones por área (B y C). INN-006-A, -B, -C y la unión A-B-C siguen en sus carpetas, sin archivar.
- Control del número de encuentros (mensaje del equipo): como Zoom arma los grupos, el deck dice que se cotizan 21 encuentros de hasta 25 personas y que los adicionales por grupos más chicos se cotizan aparte. Es redacción del sistema, no dicha por María: confirmar.
- Áreas mencionadas: Operaciones, Comercial, Legal, Zoom Miami, Gestión Humana y Tecnología (las ya trabajadas, según la memoria y los casos de éxito) y «el resto de las áreas»; sin números por área.
- Qué reemplaza: INN-003 e INN-004 (Zoom, 19/10/2026, Borrador) llevaban Claude Fundamentals; estas tres solo migran Gems a Skills con Gemini. Confirmar con Ivana que INN-003 e INN-004 se archivan.
- Encuentros de 2 horas, hasta 25 personas. Calendario: arranque la semana del 2 de noviembre (Ivana), hasta 3 por semana (lunes, miércoles y viernes: días propuestos por el sistema), grueso antes de diciembre (temporada alta de Zoom) y margen de enero y febrero para rezagados, antes del 1 de marzo de 2027. Horario: por acordar (no lo dio nadie). Que las sesiones arranquen antes del 17 de noviembre.
- Excepción a CLAUDE.md §4.23 (Keiber, 8/10/2026: sin semanas, sesiones ni fechas): el calendario con fechas va en la propuesta por pedido expreso de Ivana («coloca todo en la propuesta»). Solo la slide de calendario usa «sesiones» y «semana»; el resto del deck dice «encuentros».
- Fechas de Google (documentación oficial, consultada el 26/10/2026): skills en Workspace desde el 5/10/2026 (Rapid Release hasta el 12/10; Scheduled Release del 19/10 a mediados de noviembre); skills en la app de Gemini desde el 13/10/2026 (hasta mediados de noviembre); 17/11/2026 los Gems pasan a Configuración; no antes del 1/3/2027 Business y Enterprise no podrán crear, editar ni usar Gems (Education, no antes del 1/6/2027). Google publicará más información al menos 30 días antes de la migración automática. Ivana pidió planificar el 1/3/2027 como fecha fija aunque Google diga «no antes de»: el deck lo dice con «no antes de».
- Dos puntos de la prensa, confirmados en la documentación oficial de Google para administradores (22/10/2026): los flujos de Workspace Studio con el paso «Ask a Gem» dejan de funcionar desde el 1/3/2027 (no se pueden añadir a flujos nuevos), y una Skill de la app de Gemini no se sincroniza con las apps de Workspace (se recrea en Workspace Studio). Los Gems que se usan en Workspace tampoco se transfieren solos.
- Requisito previo de TI (de la documentación de Google; PENDIENTE de confirmar con David): activar el ajuste «Allow people to use skills in Studio and Gemini in Workspace»; edición con skills en Workspace (Business Starter, Standard o Plus; Enterprise Standard o Plus; Google AI Pro for Education o AI Expanded Access); personas de 18 años o más; canal de lanzamiento (Rapid o Scheduled Release: el despliegue en Scheduled llega a mediados de noviembre, y el primer encuentro es el 2 de noviembre); lista de flujos de Workspace Studio con «Ask a Gem»; permisos de uso compartido de Drive de los Gems (se transfieren a las Skills).
- «Por qué con nosotros»: resultados propios de Zoom del informe de casos de éxito (clientes/casos-de-exito-zoom, 19/10/2026) y de los dashboards de impacto (Encuesta Edu-Trace de cierre, 83 respuestas de seis áreas): índice de impacto promedio 87/100, 89 % de aciertos en la evaluación técnica (222 de 249, medido), 88 % usa Gemini como herramienta principal (73 de 83, autopercibido) y el seguimiento a 30 días de Tecnología (16/10/2026, la herramienta ya adoptada). Son datos de cierre y percepción: el deck no los presenta como ahorro medido (§4.17). Sin nombres de personas.
- Agenda de 2 horas: no cabe todo a la vez; propuesta del sistema: el inventario va antes con un formulario (fuera de las 2 horas), la actualización del ecosistema se reduce a 15 minutos con lo que le sirve a Zoom, y la medición del caso se inicia en el encuentro (tiempo de hoy) y se completa con la Skill ya en uso. Reparto: priorización 15 min, migración en vivo 55, reglas 15, actualización 15 y medición 20.
- Marca: Brand Kit Intezia v2.1 (13/10/2026, adjunto de Ivana): amarillo #FFD300, negro #0A0A0A, naranja #E58423 y Poppins (OFL, descargada de fontsource). Los archivos del logo v2 («Brand Kit v2 2026-10 / archivos») no están en el repositorio: el deck usa los logos actuales de `logos/` (el amarillo del arte es el #F4BA1A anterior). El CSS compacto, las cajas de la hoja de cotización y los campos del PDF conservan tintes del amarillo anterior. Falta canonizar la marca v2.1 en `empresa/marca-visual.md` y en las plantillas.
- Horas para cotizar (el deck no lleva precios): 21 encuentros de 2 h = 42 h; con 2 facilitadores, 84 h de trabajo de encuentro; preparación 8 h, coordinación con TI 4 h y seguimiento 14 h: total 110 horas de trabajo. Estimación del sistema, por confirmar.
- Pago: tres cuotas ligadas a hitos (40/30/30, propuesta del sistema, por confirmar con María), montos vacíos. Sin garantía ni seguimiento 30-60-90.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Confirmar con María la cláusula de los encuentros adicionales por grupos más chicos y la cifra de cotización (el deck no lleva precios).
- Confirmar con David la lista de requisitos de TI y que TI pueda activar las Skills antes del 2 de noviembre.
- Confirmar horario y días (se propusieron lunes, miércoles y viernes), las horas internas y los 2 facilitadores por encuentro.
- Confirmar los porcentajes de las cuotas, la moneda y los impuestos de facturación.
- Las fechas de Google pueden cambiar: reconsultar la página oficial antes de enviar.
- Si Ivana consigue el total por área, se puede volver a ofrecer la opción por áreas (B) con control exacto de encuentros.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py zoom-inn006      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh zoom-inn006             # verifica, genera el PDF y ajusta los campos
```
