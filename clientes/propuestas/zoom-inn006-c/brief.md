# Brief · Zoom · Servicio de Innovación (INN-006-C)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Zoom
- **Slug**: `zoom-inn006-c`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `innovacion`
- **Alianza**: `no`
- **Tipo de documento**: Plan de Innovación · Opción C, híbrido: 8 encuentros por área de 2 h y 1 bootcamp abierto para quienes no estuvieron (supuesto de ausencia del 15 %, 19 personas) · calendario con fechas · formato compacto v3 (`INN-006-C`); formato compacto de 10 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Migrar a Skills los Gems de las seis áreas de Zoom con un encuentro por área y un bootcamp abierto para quienes no estuvieron, antes de que Google retire los Gems
<!--auto:inicio-->
- **Alcance**: 7 encuentros en 7 áreas · 18 h de trabajo · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Qué está cambiando · 3 Alcance · 4 Ruta · 5 Calendario · 6 Cómo trabajamos · 7 Retorno · 8 Inversión · 9 Facilidad de pago · 10 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana del 26/10/2026 con el texto de la dirección de Intezia (tres opciones, A, B y C, bajo el código INN-006), la documentación oficial de Google para administradores (consultada el 26/10/2026), los dashboards de impacto y el informe de casos de éxito de Zoom, los totales por área de Ivana y el Brand Kit Intezia v2.1. Sin Ficha de Levantamiento ni transcripción
- **Fuente del insumo**: Texto de la dirección y respuestas de Ivana (26/10/2026); documentación de Google para administradores (26/10/2026); dashboards y casos de éxito de Zoom
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (26/10/2026), con el texto de la dirección (Jean y María; Emma pidió la sección «Qué está cambiando»): tres propuestas de Innovación para Zoom bajo un solo código, INN-006, con sufijo A (Bootcamp), B (Por área) y C (Híbrido), cada una en su carpeta. Educación, sin alianza, María Iribarren como directora comercial, sin mencionar Claude (solo Gems a Skills) (confirmado por Ivana).
- Qué reemplaza: INN-003 e INN-004 (Zoom, 19/10/2026, Borrador) llevaban Claude Fundamentals; estas tres solo migran Gems a Skills con Gemini. Confirmar con Ivana que INN-003 e INN-004 se archivan.
- Personas: la base de la dirección es 510 (Fase 1 de Intezia Fundamentals alcanzó a unas 500 personas, según el informe de casos de éxito). Los registros de Ivana (26/10/2026) por área suman 121: Comercial 27, Legal 8, Zoom Miami 11, Operaciones 40, Gestión Humana 17, Tecnología (sistemas o IT) 18. Ivana pidió usarlos «mientras» y corregirlos después. La opción A usa 510 y las opciones B y C usan las áreas de Ivana (121), así que las tres NO son comparables hasta cruzar los registros. Con 121 personas, la opción A serían 5 encuentros (10 h).
- Cruce con los registros de asistencia y certificados (Fase 1, Zoom Miami y Fase 2): no están en el repositorio (solo los dashboards con 83 respuestas, sin cédulas), así que no se pudo hacer el cruce.
- Encuentros de 2 horas, hasta 25 personas. Calendario: arranque la semana del 2 de noviembre (Ivana), hasta 3 por semana (lunes, miércoles y viernes: días propuestos por el sistema), grueso antes de diciembre (temporada alta de Zoom) y margen de enero y febrero para rezagados, antes del 1 de marzo de 2027. Horario: por acordar (no lo dio nadie). Que las sesiones arranquen antes del 17 de noviembre.
- Excepción a CLAUDE.md §4.23 (Keiber, 8/10/2026: sin semanas, sesiones ni fechas): el calendario con fechas va en la propuesta por pedido expreso de Ivana («coloca todo en la propuesta»). Solo la slide de calendario usa «sesiones» y «semana»; el resto del deck dice «encuentros».
- Fechas de Google (documentación oficial, consultada el 26/10/2026): skills en Workspace desde el 5/10/2026 (Rapid Release hasta el 12/10; Scheduled Release del 19/10 a mediados de noviembre); skills en la app de Gemini desde el 13/10/2026 (hasta mediados de noviembre); 17/11/2026 los Gems pasan a Configuración; no antes del 1/3/2027 Business y Enterprise no podrán crear, editar ni usar Gems (Education, no antes del 1/6/2027). Google publicará más información al menos 30 días antes de la migración automática. Ivana pidió planificar el 1/3/2027 como fecha fija aunque Google diga «no antes de»: el deck lo dice con «no antes de» y la fuente.
- Dos puntos de la prensa, confirmados en la documentación oficial de Google para administradores (22/10/2026): los flujos de Workspace Studio con el paso «Ask a Gem» dejan de funcionar desde el 1/3/2027 (no se pueden añadir a flujos nuevos), y una Skill de la app de Gemini no se sincroniza con las apps de Workspace (se recrea en Workspace Studio). Los Gems que se usan en Workspace tampoco se transfieren solos.
- Requisito previo de TI (de la documentación de Google; PENDIENTE de confirmar con David): activar el ajuste «Allow people to use skills in Studio and Gemini in Workspace»; edición con skills en Workspace (Business Starter, Standard o Plus; Enterprise Standard o Plus; Google AI Pro for Education o AI Expanded Access); personas de 18 años o más; canal de lanzamiento (Rapid o Scheduled Release: el despliegue en Scheduled llega a mediados de noviembre, y el primer encuentro es el 2 de noviembre); lista de flujos de Workspace Studio con «Ask a Gem»; permisos de uso compartido de Drive de los Gems (se transfieren a las Skills).
- «Por qué con nosotros»: resultados propios de Zoom del informe de casos de éxito (clientes/casos-de-exito-zoom, 19/10/2026) y de los dashboards de impacto (Encuesta Edu-Trace de cierre, 83 respuestas de seis áreas): índice de impacto promedio 87/100, 89 % de aciertos en la evaluación técnica (222 de 249, medido), 88 % usa Gemini como herramienta principal (73 de 83, autopercibido) y el seguimiento a 30 días de Tecnología (16/10/2026, la herramienta ya adoptada). Son datos de cierre y percepción: el deck no los presenta como ahorro medido (§4.17). Sin nombres de personas.
- Horas para cotizar (María cotiza con cuotas de pago; el deck no lleva precios): estimación del sistema, por confirmar. Encuentros: 42 h (A), 16 h (B), 18 h (C). Facilitadores: 2 en los bootcamps (varias áreas, 25 personas migrando en vivo) y 1 en los encuentros por área; con eso las horas de trabajo de encuentro son 84 (A), 16 (B) y 20 (C). Preparación (formulario de inventario 2 h, material 4 h, guía de nombres 2 h; más 1 h por área para adaptar el material en B y C): 8, 14 y 14 h. Coordinación con TI: 4, 6 y 6 h. Seguimiento (medición del caso a 0,5 h por encuentro y cierre de 3 h): 14, 7 y 8 h. Total: 110 (A), 43 (B) y 48 (C) horas de trabajo.
- Agenda de 2 horas: no cabe todo a la vez; propuesta del sistema: el inventario va antes con un formulario (fuera de las 2 horas), la actualización del ecosistema se reduce a 15 minutos con lo que le sirve a Zoom, y la medición del caso se inicia en el encuentro (tiempo de hoy) y se completa con la Skill ya en uso. Reparto: priorización 15 min, migración en vivo 55, reglas 15, actualización 15 y medición 20.
- Pago: cuotas ligadas a hitos con los montos vacíos (María cotiza); los porcentajes son propuesta del sistema (A y C: 40/30/30; B: 50/50), por confirmar con María. Sin garantía ni seguimiento 30-60-90.
- Marca: Brand Kit Intezia v2.1 (13/10/2026, adjunto de Ivana): amarillo #FFD300, negro #0A0A0A, naranja #E58423 y Poppins (OFL, descargada de fontsource). Los archivos del logo v2 («Brand Kit v2 2026-10 / archivos») no están en el repositorio: el deck usa los logos actuales de `logos/` (el amarillo del arte es el #F4BA1A anterior). El CSS compacto, las cajas de la hoja de cotización y los campos del PDF conservan tintes del amarillo anterior. Falta canonizar la marca v2.1 en `empresa/marca-visual.md` y en las plantillas.
- Opción C: los mismos 8 encuentros por área de la opción B y 1 bootcamp abierto en enero. Supuesto de ausencia: 15 % de las 121 personas de las áreas no estarán en el encuentro de su área (19 personas), que caben en 1 bootcamp de hasta 25; con hasta un 20 % de ausencia (25 personas) sigue siendo 1 bootcamp.

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

- Confirmar la base: 510 (A) frente a los totales por área de Ivana (121, para B y C). Pasar los registros reales de asistencia y certificados (Fase 1, Zoom Miami y Fase 2) para el cruce y el total por área.
- Confirmar con David la lista de requisitos de TI (activación de Skills, edición, canal de lanzamiento, flujos con «Ask a Gem», permisos de Drive).
- Confirmar el horario de los encuentros y los días (se propusieron lunes, miércoles y viernes) y que TI pueda activar las Skills antes del 2 de noviembre.
- Confirmar las horas internas (preparación, coordinación con TI, seguimiento) y los facilitadores por encuentro (1 por área, 2 en bootcamp).
- Confirmar con María los porcentajes de las cuotas y las cifras de cotización (el deck no lleva precios).
- Revisar con Ivana los logos de la marca v2.1 (archivos del Brand Kit) y la canonización de la marca nueva.
- Confirmar con Ivana que INN-003 e INN-004 se archivan y que el contacto con Zoom sigue siendo María (Anaís y Ricardo no van en el deck).
- Las fechas de Google pueden cambiar: reconsultar la página oficial antes de enviar.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py zoom-inn006-c      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh zoom-inn006-c             # verifica, genera el PDF y ajusta los campos
```
