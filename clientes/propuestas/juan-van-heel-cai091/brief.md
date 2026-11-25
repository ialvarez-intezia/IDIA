# Brief · Juan Van Heel · Servicio de Habilidades (CAI-091)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Juan Van Heel
- **Slug**: `juan-van-heel-cai091`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-091`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Nivelar en Gemini, que ya tienen en su dominio de Google, a unas 21 personas de varias áreas de Juan Van Heel, con una base común para todos y después el trabajo por función, en vivo (presencial en Caracas y en línea para el resto), para que cada área lo use en su día a día y salga con algo propio construido
<!--auto:inicio-->
- **Alcance**: 5 entregables en 2 pasos · 12 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Juan Van Heel (Flavia Martínez, 05/11/2026) y las notas de la reunión de Flavia pasadas por Ivana el 09/11/2026: primer proyecto de dos que el cliente pide por separado (nivelación en Gemini; el agente de atención por WhatsApp es otro proyecto, otra propuesta). Sin transcripción en el repositorio
- **Fuente del insumo**: Ficha de Levantamiento (05/11/2026) y notas de la reunión de la asesora (09/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (09/11/2026): propuesta CAI-091 para Juan Van Heel, asesora Flavia Martínez, con la ficha (05/11/2026) y las notas de la reunión. Educación y sin alianza: confirmados con Ivana. La ficha dice que es el primer contacto y que hay competencia (están evaluando otras empresas): no va al deck.
- El cliente pide dos proyectos por separado, de áreas distintas. Esta propuesta es solo el primero: la nivelación en Gemini. El agente de atención por WhatsApp (10 vendedores, números propios, respuestas humanizadas, demo previa) es otra propuesta; el deck lo deja fuera del alcance sin dar detalles. Mantener el número de cada vendedor debe validarlo Servicio antes de prometerlo.
- Horas (propuesta mía; la ficha no las fija; Ivana eligió la opción de 12 h): módulo 1, base común, 4 h para todo el equipo (fundamentos 2 h y Gemini aplicado a cada función 2 h); módulo 2, segundo nivel por función, 8 h (casos 2 h, una Skill propia por función 4 h y protocolo común 2 h). Modular, para ajustar en vivo según personas y funciones.
- Personas y funciones: ~21 según Flavia («unas 21»), aproximado y por confirmar por escrito con Luis Calatayud; no se sabe de qué áreas, qué funciones tienen ni su nivel con Gemini. Se escribe «unas 21» y el segundo nivel «por función». La versión de Google Workspace tampoco se sabe: Flavia se la pregunta a Luis en la reunión y se ajusta la Skill a lo que incluya la licencia (el deck lo dice).
- Modalidad (Flavia, notas): sin videos grabados; presencial en Caracas y en línea en vivo para el resto (híbrido), con sesiones de máximo 2 horas, una o dos por semana. El deck no lleva sesiones, duración ni frecuencia (§4.23): dice «en vivo» y «bloques cortos» y el calendario se acuerda en el arranque. La ficha dice «sesiones de 2 horas» y que no todos están en Caracas.
- Cotización por módulos (decisión de Ivana, 09/11/2026): `inversion.partes` con una caja de valor por módulo (base común y segundo nivel) que suman el total, para que Ventas ajuste en la reunión como se hizo con otro cliente (no se nombra: regla de no nombrar clientes). Valor, descuento y total quedan vacíos para ventas; moneda en REF con la leyenda de pago.
- Impacto (cuadro de «Lo que se llevan»): enfoque «operación», elegido por Ivana el 09/11/2026: tiempo, calidad y criterio común, sin hablar de personas ni de nómina.
- Herramienta: Gemini, que el cliente ya tiene en su dominio de Google y quiere aprovechar; es lo que pide el cliente, no una recomendación. «Skill de Gemini» viene de las notas de Flavia; si la licencia no la incluye, se construye otra solución equivalente. Sin licencias nuevas.
- Sin facilidad de pago (omitida): decisión mía por ser lo que se ha pedido en las últimas propuestas; confirmar con Ivana. Sin horas de trabajo internas ni cantidad de consultores (§4.23). Seguimiento y garantía 30-60-90 por defecto. Sin certificado.
- Personas del cliente (solo internas): Freddy Rojas, gerente general, firma y decide y estará en la presentación (confirmado); Luis Calatayud, segundo contacto y responsable de logística. No se nombran en el deck.
- Ajuste del 11/11/2026 (Ivana): un solo valor del proyecto, sin tarjetas de «Parte 1» y «Parte 2» ni desglose. La hoja de inversión dice «Valor del proyecto» (opción nueva `inversion.etiqueta_valor` del generador) y la nota aclara que el número de personas y funciones se confirma en el arranque y que el proyecto se cotiza completo. El deck ya no habla de «dos módulos»: es un programa de 12 horas en vivo con un orden (base común y después trabajo por función); «Segundo nivel» pasó a «Trabajo por función» para que no suene opcional. Las 12 horas son el proyecto y se distribuyen entre las funciones cuando se confirmen. Garantía 30-60-90 asociada al proyecto completo, sin cambio.

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

- Confirmar por escrito con Luis Calatayud el número de personas (~21), sus áreas y funciones, y su nivel actual con Gemini.
- Preguntar a Luis qué versión de Google Workspace tienen y qué incluye su licencia de Gemini, para ajustar la Skill.
- Confirmar con Ivana el reparto de las 12 h (4 de base común y 8 de segundo nivel) y que se omite la facilidad de pago.
- Valor por módulo, descuento y total: campos vacíos para ventas; moneda en REF.
- La propuesta del agente de atención por WhatsApp (otro código): pendiente de pedir; validar con Servicio que se pueda mantener el número de cada vendedor antes de prometerlo, y preparar la demo que piden.
- Fecha y formato de la reunión de presentación con Freddy Rojas (ya confirmado que asiste).
- El paso 1 de los próximos pasos (confirmar personas y funciones) ahora es para organizar el calendario y los grupos, no para decidir si hay segunda parte. El valor es uno solo, campo vacío para ventas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py juan-van-heel-cai091      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh juan-van-heel-cai091             # verifica, genera el PDF y ajusta los campos
```
