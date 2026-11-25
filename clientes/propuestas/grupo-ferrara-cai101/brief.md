# Brief · Grupo Ferrara · Servicio de Habilidades y Políticas (CAI-101)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Grupo Ferrara
- **Slug**: `grupo-ferrara-cai101`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-101`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Clonar el criterio del equipo de marketing para medir qué convierte, llevar el cotizador de propuestas de Ventas a minutos, y dejar un marco de políticas de IA y un comité de inteligencia para todo el equipo, en Grupo Ferrara
<!--auto:inicio-->
- **Alcance**: 9 soluciones en 3 áreas · 35 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Grupo Ferrara (Verónica Rubio, 17/11/2026) y transcripción de la reunión con el cliente.
- **Fuente del insumo**: Ficha de Levantamiento + transcripción de la reunión con el cliente. Primer contacto de Intezia con esta empresa: sin informe de Detección propio.
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Combo Habilidades + Políticas registrado en meta.json como servicio: habilidades (servicio_rotulo: «Servicio de Habilidades y Políticas»), siguiendo el mismo criterio que Andrómeda DET-016 (combo Detección + Políticas bajo deteccion, confirmado con Ivana el 2026-11-17): no hay un formato propio para Políticas, así que se representa como una línea de trabajo más, con sus propios entregables y su propia parte en la inversión (inversion.partes).
- No se nombra el sistema de gestión (Odoo) ni su migración en el deck (§4.11): Ferrara ya está migrando de Profit a Odoo por su cuenta; el cotizador se conecta a «su sistema de gestión» en el texto de cara al cliente, y el detalle interno (Odoo) vive en las soluciones[].detalle, que es interno (programa.md).
- Sin informe de Detección previo (primer contacto de Intezia con esta empresa, según la Ficha): los «para_que» y las soluciones salen de la Ficha de Levantamiento y de la transcripción de la reunión, no de un informe propio de Ferrara.
- No se muestra en el deck la cantidad de consultores de Intezia que cubren las tres líneas de trabajo (la Ficha menciona «hasta 3 consultores» para el arranque): dato interno para la coordinación del kickoff, no para la propuesta (regla permanente de Ivana del 2026-10-27, sin_horas_trabajo: true).
- Sin datos propios del cliente para el retorno (horas-hombre, valor de la hora, volumen exacto de ventas): modo metodo.
- entregables.impacto con enfoque «operacion»: el equipo de marketing y ventas mantiene su tamaño (12 personas) y gana velocidad y alcance; no se plantea operar con menos personas ni se habla de nómina.
- Facilidad de pago omitida (omitir: ["pago"]): la Ficha no trae un plan de cuotas propio; se puede agregar si se confirma con Ventas.
- Herramienta de IA sin elegir todavía por el cliente (la Ficha dice «aún no lo saben, esperan la recomendación»): el carril del deck es Claude, consistente con lo recomendado en la transcripción para Marketing, Dirección/Tecnología y el marco de gobernanza; el cotizador de Ventas se describe sin nombrar una herramienta de diseño de terceros (iHouse, Cojum) porque esas no son una recomendación de Intezia, sino lo que el cliente ya exploró por su cuenta.

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

- Confirmar responsable de Marketing y de Ventas/Diseño (la Ficha los deja «por confirmar»).
- Confirmar si Nacho (propietario, quien decide) estará en la presentación de la propuesta (la Ficha lo deja «por confirmar»).
- Definir el valor de cada línea de trabajo (Habilidades Marketing, Habilidades Ventas, Políticas), el descuento y el total: campos vacíos para ventas; la suma se calcula sola en Adobe Reader.
- Confirmar con Grupo Ferrara qué herramienta de IA licencian para cada equipo y quién la paga.
- Si se quiere facilidad de pago, definir las cuotas y a qué hito de la ruta se ligan.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py grupo-ferrara-cai101      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh grupo-ferrara-cai101             # verifica, genera el PDF y ajusta los campos
```
