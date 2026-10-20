# Brief · Hidrocarburos · Servicio de Habilidades (TA-038)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Hidrocarburos (antes «Ministerio de Inteligencia Artificial y Eficiencia Productiva», nombre del documento de trabajo)
- **Slug**: `ministerio-ia-ta038`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Taller (`TA-038`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (sin hoja de inversión ni de pago (sin_hoja_cotizacion / omitir))
- **Eje temático**: Guía de gobierno de IA y datos para el sector hidrocarburos, como documento de lineamientos de referencia
<!--auto:inicio-->
- **Alcance**: 12 apartados en 4 bloques · 12 h de trabajo · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Retorno
- **Asesora comercial que ve el cliente (última slide)**: (esta propuesta omite la slide de próximos pasos)
<!--auto:fin-->
- **Estado**: `Enviada` el 14/10/2026 (`meta.json`; convención «terminado = enviado», lo estampa el wrapper del PDF). Sin asesora por indicación de Ivana.
- **Insumos (CLAUDE.md §4.23)**: documento de trabajo de Intezia «Propuestas de IA responsable para el sector público» (14/10/2026), Propuesta 2 de 2 (guía de gobierno). No hubo Ficha de Levantamiento ni transcripción de reunión con el ministerio: lo que no está en el documento no se inventó.
- **fecha_arranque_deseada**: no hay dato (el documento no la trae). Se define en el kickoff; la propuesta no lleva fechas, semanas ni sesiones.
- **resultados_esperados**: los indicadores de éxito del documento (ver el retorno en `datos.json`). Sin cifras del ministerio, así que el retorno va en modo método y no se agrega ROI.

## Contexto del cliente (interno, no va al deck)

- **Quién es:** Hidrocarburos (desde la versión 2 del 15/10/2026; el documento de trabajo lo llamaba Ministerio de Inteligencia Artificial y Eficiencia Productiva; si el destinatario es otro ministerio o empresa de hidrocarburos, cambiarlo). El documento es una propuesta de Intezia «para revisión con el ministerio»; las referencias normativas deben verificarse con el área legal antes de su uso formal.
- **Para qué sector:** hidrocarburos (instrucción de Ivana, 14/10/2026), dicho en el título, el alcance y los indicadores. El documento original era para el sector público en general.
- **Qué se propone:** una guía de gobierno de IA y datos como documento de lineamientos de referencia (no una ley ni un reglamento), para que el ministerio pueda adoptarlo dentro de sus competencias y sirva de insumo al proyecto de ley en la Asamblea Nacional. Aplica a los organismos del ministerio y, por adopción voluntaria, a entes adscritos y empresas públicas de hidrocarburos.
- **Tiempo:** el deck dice solo «sesiones de 2 h», sin cantidad de sesiones (excepción pedida por Ivana a §4.23, declarada en `frases_ok`). Se omitió el proceso de elaboración con duraciones (2, 2, 3, 2 y 1 semanas; 10 en total), que queda como ruta en tres fases sin duraciones.
- **Economía:** se omitió la parte económica.
- **Asesora:** no hay; se omite ese campo y, con él, la slide de próximos pasos.
- **Orden recomendado por el documento:** presentar primero esta guía, porque responde al vacío legal y es el punto de mayor interés del ministerio; después el programa universitario (TA-037).
- **Riesgos del documento:** ambigüedad legal (redactar como referencia y validar con el área legal), resistencia a la regulación (presentar la guía como protección para los funcionarios) y desfase tecnológico (revisiones periódicas del catálogo).
- **Es un taller por decisión de Ivana:** por contenido sería Políticas (formato de propuesta pendiente); se hizo en la plantilla compacta de Habilidades porque Ivana indicó que las dos son talleres.
- **Deck con aire:** las slides 2, 3 y 5 quedan con espacio libre al pie; no se rellenó con texto de más.

## Origen y fuente

- **Origen**: Documento de trabajo «Propuestas de IA responsable para el sector público» (Intezia, 14/10/2026), Propuesta 2 de 2, adaptado al sector hidrocarburos; instrucciones de Ivana del 14/10/2026: TA-038, sin tiempo (solo «sesiones de 2 h») ni parte económica, sin asesora
- **Fuente del insumo**: Documento de trabajo de Intezia del 14/10/2026 (sin Ficha de Levantamiento ni transcripción de reunión)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- **Versión 2 (15/10/2026, Ivana):** (1) cliente **«Hidrocarburos»** (antes «Ministerio de Inteligencia Artificial y Eficiencia Productiva»): en el pie de página y donde decía «el ministerio»; la carpeta conserva el slug `ministerio-ia-ta038`. (2) Se quitó lo que habla de **ley o de política**: el hecho «Sin marco legal específico» (ahora «Base: normativa y ética de referencia»), el «no una ley ni un reglamento» del subtítulo, el punto «Una ley o un reglamento… proyecto de ley» del fuera de alcance, el «Insumo para la ley en la Asamblea Nacional» del retorno (ahora «Referencia: lineamientos que las instituciones del sector consultan y actualizan») y «Vacío normativo» del apartado 1. (3) **Sin entregables:** se omite la slide «Qué recibe el ministerio» (`omitir: ["proximos","entregables"]`) y la palabra pasa a «apartado(s)» («una guía con doce apartados»); queda fuera, solo como referencia para el kickoff, el documento editable y en PDF, las plantillas y anexos, el resumen ejecutivo para autoridades y los insumos para el proyecto de ley. El deck pasa de 6 a 5 slides y el PDF no tiene campos editables. (4) **Sin networking:** esta propuesta no lo mencionaba. **Las viñetas siguientes son de la versión 1 (14/10/2026): lo que hablan del ministerio, de la ley, de entregables o del networking está superado.**

- Insumo único: el documento de trabajo de Intezia del 14/10/2026 (Propuesta 2 de 2). No hubo Ficha de Levantamiento ni transcripción de la reunión: los datos de la portada son de contenido de la guía y de contexto normativo que el propio documento declara, no mediciones del ministerio.
- Ivana indicó que las dos propuestas son talleres (TA-037 y TA-038), por eso esta va en la plantilla compacta de Habilidades y no como Políticas (cuyo formato de propuesta sigue pendiente). El contenido es un documento de lineamientos: se reexpresa como una guía de 12 apartados (cada uno es un entregable) en 4 bloques (spec §1b, receta de curso), y el proceso de elaboración del documento pasa a ser la ruta en tres fases.
- Instrucciones de Ivana (14/10/2026): (a) omitir la parte del tiempo y la económica; (b) poner que son «sesiones de 2 h» y solamente eso, sin cantidad de sesiones; (c) adaptar el contenido al sector hidrocarburos y decirlo en el título; (d) no hay asesora: se omite ese campo. Por (a), el deck no lleva el cuadro de duración por fase ni el total aproximado de semanas del documento, ni la hoja de inversión ni la de pago (`sin_hoja_cotizacion`). Las duraciones del documento (2, 2, 3, 2 y 1 semanas; 10 en total) quedan solo como referencia interna para el kickoff.
- «Sesiones de 2 h» es una excepción pedida por Ivana a CLAUDE.md §4.23 (que bloquea la palabra «sesiones»): se dice solo la duración de cada sesión, nunca la cantidad, la agenda ni las fechas. El generador la acepta por `frases_ok` y `verificar-propuesta.sh` ahora respeta `frases_ok`. El calendario y el número de sesiones se acuerdan en el kickoff.
- Las horas de `datos.json` (1 por entregable) son marcadores técnicos que exige el generador: no representan duración y no se muestran en el deck (`overrides.css`). La duración que sí se dice es la de las sesiones, 2 h.
- Adaptación a hidrocarburos: el documento es para el sector público en general. Se dirige al sector hidrocarburos en el título, el alcance (organismos del ministerio y, por adopción voluntaria, entes adscritos y empresas públicas de hidrocarburos), el contexto de la introducción y los indicadores. Los 12 apartados no cambian. El cliente sigue siendo el Ministerio de Inteligencia Artificial y Eficiencia Productiva; si el destinatario es otro ministerio o empresa del sector, cambiar el nombre.
- Educación y sin alianza (Ivana lo confirmó para las dos propuestas).
- El documento define el proceso por fases (revisión normativa, diagnóstico con áreas usuarias, borrador técnico y legal, validación con el ministerio y consulta con la universidad, versión final y presentación) pero no dice qué apartado de la guía se trabaja en cada fase. El reparto (apartados 1 a 3 en la fase base, 4 a 10 en el borrador y 11 y 12 en el cierre) es una propuesta de Intezia, a confirmar.
- Los cinco pasos del proceso del documento se muestran en la ruta como cinco hitos: revisión normativa, diagnóstico, borrador, validación y presentación formal.
- Sin seguimiento a 30, 60 y 90 días (el documento no lo trae): los indicadores de éxito del documento (adopción formal, proyectos evaluados con la guía, modelos en el catálogo) son el retorno.
- El texto de «cómo se cuidan los datos» (el diagnóstico se apoya en lo que cada área decide compartir) es una propuesta de redacción de Intezia: el documento solo habla de la clasificación de datos dentro de la guía. Confirmar con el ministerio.
- Los riesgos del documento se traducen en lo que el deck sí puede decir: la guía se presenta como protección para los funcionarios, se prevén revisiones periódicas del catálogo y se redacta como referencia con verificación del área legal.
- Sin asesora (Ivana): la slide de próximos pasos se omite (`omitir: ["proximos"]`), porque el generador exige la asesora para esa slide. Si más adelante hay una, se agrega `proximos_pasos.asesora`, se quita el omitir y se regenera.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Sin hoja de inversión ni de pago (sin_hoja_cotizacion / omitir): el deck no lleva montos ni campos de cotización.

## Pendientes

- ¿Quién en el ministerio validaría la guía y qué instancia la adoptaría? ¿Existe una mesa de trabajo sobre el proyecto de ley? ¿Qué referencias normativas usa hoy el ministerio para datos y nube? (preguntas del documento para la siguiente reunión).
- Referencias normativas: el documento advierte que deben verificarse con el área legal antes de su uso formal.
- Orden de presentación: el documento recomienda presentar primero esta guía, porque responde al vacío legal y es el punto de mayor interés del ministerio, y después el programa universitario (TA-037) para socializarla y sumar aliados en la universidad.
- Valor, descuento, total y plan de pago no se arman: Ivana pidió omitir la parte económica.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py ministerio-ia-ta038      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh ministerio-ia-ta038             # verifica, genera el PDF y ajusta los campos
```
