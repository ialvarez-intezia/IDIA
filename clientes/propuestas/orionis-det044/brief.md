# Brief · Orionis · Servicio de Detección (DET-044)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Orionis
- **Slug**: `orionis-det044`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-044`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Detectar oportunidades de automatización con IA en cuatro áreas de Orionis (Operaciones, Negocios, Fraudes y Productos y Proyectos), con la información cuidada, y trazar la ruta para pasar de la Detección a la implementación
<!--auto:inicio-->
- **Alcance**: 4 áreas (Operaciones, Negocios, Fraudes, Productos y Proyectos) · 16 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Contexto escrito por la asesora Flavia Martínez sobre la primera reunión con Orionis, pasado por Ivana el 27/10/2026. No hay ficha de levantamiento ni transcripción (Granola y Fathom no se conectaron). Propuesta base para presentar en vivo a los líderes y ajustar en esa misma reunión. Código DET-044, división Educación y sin alianza, por confirmar
- **Fuente del insumo**: Contexto de la asesora sobre la primera reunión con Orionis (27/10/2026); sin ficha ni transcripción
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (27/10/2026): propuesta base de Detección para Orionis con Flavia Martínez como asesora. No hay ficha ni transcripción: Granola y Fathom no se conectaron en la primera reunión y el cliente dio poco detalle (quieren entender primero cómo funcionaría el esquema). Código DET-044 (siguiente libre tras DET-043), división Educación y sin alianza: los tres por confirmar con Ivana.
- No es la propuesta oficial: la asesora la presentará en vivo, de preferencia presencial, a los líderes de cada área y hará en esa misma reunión un levantamiento más completo para ajustarla al 100 %. Por eso va por áreas y deja abierta una segunda fase para sumar otras. Al ajustarla, se cambian áreas, horas y pasos en `datos.json` y se regenera.
- Áreas: cuatro, tal como las nombra la asesora (Operaciones, Negocios, Fraudes y Productos y Proyectos), sin prioridades entre ellas (CLAUDE.md §4.22). Participarían entre 3 y 5 personas, los líderes de esas áreas. Origen: referido por Sandokan (Banco N58); según él su modelo se parece al de Credicard, lo que no está confirmado. Nada de eso va en el deck.
- Horas (lineamiento de empresa/politicas-comerciales.md): 4 h por área en 4 áreas = 16 h de levantamiento en global, sin reparto por área, y 2 h de Fundamentos de IA en un solo grupo (3 a 5 líderes, muy por debajo del máximo de 25). Arranque sin horas. Si se suman áreas, cada una agrega 4 h de levantamiento.
- Lo que falta y la asesora levantará en la presencial: los procesos concretos de cada área, cuántas personas tiene cada equipo, qué herramientas y sistemas usan hoy y quién toma la decisión final de inversión. Por eso el deck no nombra procesos, herramientas ni stack, ni dice quién recibe el Informe Final más allá de «los líderes».
- Interés declarado: automatizar procesos y proyectos con IA. El deck lo recoge en el mapa y en la ruta de la Detección a la implementación (Habilidades construye las soluciones priorizadas con el equipo). No promete automatizaciones concretas, integraciones con sus sistemas ni resultados: el retorno es una estimación de referencia.
- Confidencialidad: se asume que Fraudes maneja información sensible (aún sin confirmar). El deck lo trata como cuidado de la información en tres lugares: objetivo «Cuidar la información», un espacio por área y el párrafo de datos en «Cómo trabajamos»; se acuerdan reglas en el arranque y en los Fundamentos. No se promete certificación, acuerdo de confidencialidad ni infraestructura propia.
- Stack y herramientas: no se conocen y el deck no pre-recomienda ninguna (la recomienda el Informe Final). Nunca se promete VPN ni se menciona Claude (memoria sobre Claude y Venezuela). Sin afirmar migración de stack (§4.11).
- Modalidad sin definir: el deck dice «presencial o virtual, según lo que acuerden con Orionis». Confirmar en la reunión con los líderes.
- Pago: estándar de Detección (50 % al aprobar y 50 % con el Informe Final), montos vacíos para ventas; no se sabe si Orionis lleva facilidad de pago ni el valor. El deck no usa la palabra «curso» (las 2 h son «Fundamentos de IA»).
- Sin semanas, sesiones ni fechas; sin horas de trabajo ni cantidad de consultores (CLAUDE.md §4.23).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Detección (`plantillas/deteccion-compacto.md`, Keiber 2026-10-08): sin frentes ni áreas prioritarias antes de detectar (lo que el cliente señaló como interés guía la conversación, no la estructura); cada departamento por separado, con su líder y su mano derecha, sin tarea previa; horas en global, sin reparto por área; al menos 3 logros inmediatos en el proyecto (no uno por área); entregables nombrados, sin conteos.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Confirmar con Ivana el código DET-044, la división Educación y que no hay alianza.
- Conseguir en la reunión presencial: procesos de cada área, personas por equipo, herramientas y sistemas actuales y quién decide la inversión; después ajustar áreas, horas y pasos del deck.
- Confirmar los cargos y nombres de los líderes de las cuatro áreas y quiénes asistirán a los Fundamentos (entre 3 y 5).
- Confirmar con Flavia si Orionis lleva facilidad de pago, la moneda de facturación y el valor.
- Confirmar la modalidad (presencial o virtual) y qué datos de Fraudes tendrán restricción para las sesiones.
- Confirmar el teléfono y el correo de Flavia Martínez (tomados de la CAI-067).
- Decidir si se incluye una segunda fase con otras áreas y cuáles, una vez levantado lo que falta.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py orionis-det044      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh orionis-det044             # verifica, genera el PDF y ajusta los campos
```
