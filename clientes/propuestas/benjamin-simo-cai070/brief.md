# Brief · Benjamín Simo · Servicio de Habilidades (CAI-070)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Benjamín Simo
- **Slug**: `benjamin-simo-cai070`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-070`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construcción guiada de un Cerebro Digital (asistente personal) con Claude y Obsidian para el dueño de Alma Mia, Hostal Madrid y Motel Villa Ricardo: cierre de ventas, cuentas por pagar y por cobrar con vencimientos por plazo de proveedor, e ideas de mercadeo para el restaurante nuevo
<!--auto:inicio-->
- **Alcance**: 5 entregables en 1 Cerebro Digital · 10 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Alma Mia, Hostal Madrid y Motel Villa Ricardo (Flavia Martínez, 27/10/2026; dueño Benjamín Simo, quien decide y firma) y contexto escrito por la asesora, más instrucciones de Ivana del 28/10/2026: propuesta de Cerebro Digital con el código CAI-070 y 5 sesiones. No hay transcripción de la reunión. División Educación y sin alianza, por confirmar
- **Fuente del insumo**: Ficha de Levantamiento (27/10/2026) y contexto de la asesora; sin transcripción
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (28/10/2026): propuesta de Cerebro Digital para Benjamín Simo con el código CAI-070 y 5 sesiones, a partir de la Ficha de Levantamiento (27/10/2026) y el contexto de Flavia Martínez. No hay transcripción. División Educación y sin alianza: por confirmar con Ivana.
- Cliente: dueño de dos restaurantes (uno familiar de 40 años y uno nuevo) y de un hotel pequeño que funciona como motel (Alma Mia, Hostal Madrid y Motel Villa Ricardo); primer contacto, llega por Jimena Simó, cercana a Flavia: se trata como cliente de la casa. Él decide y firma, y confirmó que estará en la presentación. Los nombres de las tres marcas y de personas no van al deck (se asigna el cerebro al dueño).
- Su dolor, para ventas: trabaja domingos y lunes consolidando en Excel las ventas del restaurante principal y del hotel y revisando cuentas por pagar y por cobrar, con proveedores a 7, 15, 30 y 60 días; el sistema administrativo solo le sirve para lo fiscal. Segundo frente: ideas frescas de mercadeo del restaurante nuevo (lo lleva una persona externa; «la gente es más crítica»). La cita textual no va en el deck.
- 5 sesiones (pedido de Ivana, excepción a CLAUDE.md §4.23): se escribe «5 sesiones de 2 horas» y las frases están en `frases_ok`. La duración de 2 h por sesión es mía (es la forma de CAP-060 y de los cerebros anteriores), lo que da 10 h con el cliente (la referencia de Cerebro Digital sin horas es 6 h, y Decovenezia usó 10 h). Reparto mío: 1 de base y levantamiento de tareas, 1 de grafo, y 3 de uso (cierre de ventas, cuentas por pagar y por cobrar, mercadeo).
- Flavia pidió que las primeras sesiones sirvan para mapear y delimitar las tareas, porque él no conoce la IA y probablemente no ve otros usos; los ejemplos a explorar (reservas y ocupación del hotel, costo de platos y márgenes, pedidos e inventario, turnos del personal, reseñas) van como posibles, nunca como promesa. La sesión de base los explora; si salen más tareas, se ajustan las horas.
- Qué hace el cerebro solo y qué requiere integraciones aparte (preguntas del cliente: qué IA es, si necesita el computador encendido, conexión con WhatsApp, Instagram y el banco): el deck aclara que responde cuando se le pide, que no se conecta solo con WhatsApp, Instagram ni el banco y que no envía alertas por sí solo. Qué necesita el computador encendido no se afirma en el deck (depende de dónde corra Obsidian): decirlo en la presentación en vivo. La Fase 2 que propuso Flavia (integraciones con WhatsApp e Instagram para atención al cliente y tareas que corran solas) se menciona como etapa siguiente, sin cotizar.
- Acceso de gerentes y supervisores (lo pidió): va por Claude Team, que exige mínimo 2 puestos; estándar USD 25 al mes pagando mensual y USD 20 pagando por año (verificado el 28/10/2026 en support.claude.com, «What is the Team plan?»; coincide con la verificación del 16/10). La tarjeta de licencias lo dice y la nota aclara que los valores los confirma el cliente. Cuántos gerentes y supervisores: sin definir; Benjamín lo mencionará en las sesiones.
- Claude con un cliente venezolano: nunca VPN; sin mención al acceso ni al riesgo en el deck (criterio de Ivana en Simple TV y Go Pharma). Nota interna: Venezuela no figura entre los países soportados por Anthropic; si Ivana dice algo distinto, cambiarlo.
- Dato contradictorio en la ficha: «Regulación sectorial aplicable: manejo de datos de pacientes (información de salud sensible)». No tiene sentido para restaurantes y un hotel (parece un valor copiado de otra ficha): se ignora en el deck y se pregunta a Flavia. El tipo de dato del cierre es «confidencial»: el deck dice que no se suben claves del banco ni datos de clientes.
- Horizonte: implementación en 2027 tras aprobaciones internas; presupuesto «en evaluación»; apertura al cambio alta y patrocinio fuerte. Sin fechas en el deck (§4.23).
- Pago: se omite la facilidad de pago (criterio habitual); valor, descuento y total quedan como campos vacíos para ventas. Sin horas de trabajo ni cantidad de consultores (§4.23). Las licencias van en tarjetas dentro de la inversión (con valores de lista y su fecha), no como precio de Intezia.

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

- Confirmar con Ivana la división Educación y que no hay alianza (el código CAI-070 y las 5 sesiones los dio Ivana).
- Confirmar con Ivana que cada sesión es de 2 h (10 h en total) y el reparto 1 de base, 1 de grafo y 3 de uso.
- Confirmar con Flavia cuántos gerentes y supervisores tendrán acceso (cada uno suma un puesto de Claude Team) y quién contrata la cuenta.
- Preguntar a Flavia por la «regulación sectorial: datos de pacientes» de la ficha (parece un error).
- Confirmar si Benjamín quiere facilidad de pago, la moneda de facturación y el valor.
- Aclarar en la presentación qué requiere el computador encendido y qué integraciones (WhatsApp, Instagram, banco) serían de la etapa siguiente.
- Confirmar el teléfono y el correo de Flavia Martínez (tomados de la CAI-067).
- Volver a verificar el precio de Claude Team antes de enviar si pasan semanas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py benjamin-simo-cai070      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh benjamin-simo-cai070             # verifica, genera el PDF y ajusta los campos
```
