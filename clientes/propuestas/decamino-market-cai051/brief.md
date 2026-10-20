# Brief · Decamino Market · Servicio de Habilidades (CAI-051)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Decamino Market
- **Slug**: `decamino-market-cai051`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-051`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Soluciones de IA en compras, costos e inventario de Decamino Market (supermercado en línea): precios de proveedores, costo real y ganancia bruta por orden, e inventario diario
<!--auto:inicio-->
- **Alcance**: 6 entregables en 3 áreas · 36 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Contexto del cliente (interno, no va al deck)

- **Quién es:** supermercado en línea de la Gran Caracas, con más de 2 años de operación, micro/pyme (menos de 50 empleados). Primer contacto con Intezia. Tiene frentes en otros estados operados por otros socios (fuera de este alcance). Dueña y socia: Carens León, decide y aprueba directamente.
- **Qué pide:** automatizar con IA los precios y costos (ficha, bloque D): saber a las 6 am dónde comprar cada producto de la orden que el sistema entrega a medianoche y en qué cantidad, y obtener el costo real de cada orden (facturas del grupo de WhatsApp) frente al valor publicado en la página, con la ganancia bruta y su porcentaje. Hoy se hace a mano en Excel y no alcanza el día con 10 órdenes. En alimentos en Venezuela el valor cambia incluso en el mismo día.
- **Lo que rechazó:** el paquete completo de automatización; pidió una propuesta acotada a compras, inventario y costeo, con presupuesto ajustado (sale de las ganancias del supermercado, sin fondo de inversión).
- **Urgencia:** temporada alta (los mejores meses del año para el rubro) y la salida del único empleado que conocía a fondo el proceso y a los proveedores. No hay responsable interno designado para el proyecto. Dato sensible: no va al deck.
- **Equipo:** 7 personas, todas operativas y sin líder (compras, armado de pedidos, despacho y reporte de inventario por subárea: cárnicos y charcutería, víveres, vegetales). Apertura al cambio alta, patrocinio fuerte y visible. Nivel de IA: uso suelto y sin criterio (un empleado consulta Gemini de manera informal); la dueña hizo cursos personales. Sin política de datos ni regulación sectorial.
- **Stack:** sin ecosistema definido; la información vive en hojas de cálculo y la coordinación es por WhatsApp. No saben qué herramienta de IA quieren: esperan la recomendación (se entrega con el levantamiento).
- **Procesos de la ficha:** (1) mapeo de precios de los 4 o 5 proveedores cercanos al almacén para la compra diaria (solo Polar maneja lista de precios por Excel o WhatsApp, a medianoche; los demás tienen página web); (2) conciliación de costos por orden (facturas en foto frente a inventario) y separación entre los dos supermercados cuando un mismo proveedor les surte a ambos.
- **Material recibido (13/10/2026):** orden de compra consolidada (5 órdenes, 103 productos y 170 unidades), hoja de costos del 10/10 con la tasa de 876,80 Bs por dólar y el pedido #2459 del 09/10. Ejemplo del cliente, cálculo del sistema: el pedido #2459 suma 132,32 USD (sin envío) y su costo en la hoja es 81.065,33 Bs, o 92,46 USD, lo que da una ganancia bruta de 39,86 USD (30,1 %). Sirve para el levantamiento; no se cita en el deck. El pedido trae datos personales de un cliente final.
- **Restricciones operativas:** la dueña está de viaje y pidió evitar reuniones adicionales; prefiere resolver dudas por escrito (enviará una minuta propia del proceso). Sin responsable de logística designado.
- **Plazo comercial:** Verónica prometió la propuesta formal de dos fases (levantamiento y construcción) antes del miércoles 14/10/2026 a las 3 PM, con reunión de revisión ese día. La minuta de Meet es un resumen automático, no una transcripción.

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Decamino Market (Verónica Rubio, 12/10/2026), resumen de la reunión por Google Meet del 12/10/2026 y material del cliente (orden de compra consolidada de 5 órdenes, hoja de costos del 10/10 y pedido #2459 del 09/10), más la instrucción de Ivana del 13/10/2026: CAI-051, 2 encuentros de levantamiento por área más la construcción, 10 h por área; después, 8 h de construcción en cada área (36 h)
- **Fuente del insumo**: Ficha de Levantamiento y resumen de la reunión (sin transcripción) e instrucción del usuario
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (13/10/2026): propuesta CAI-051 para Decamino Market, asesora Verónica Rubio, «2 sesiones de levantamiento por área más las de construcción, 10 h por área». Ivana confirmó la lectura: **3 áreas y 10 h en total por área** = 4 h de levantamiento de información (los dos encuentros) + 6 h de construcción: 30 h. Después subió Costos por orden a 8 h de construcción (32 h) y, por último, pidió **estandarizar todas las áreas a 8 h de construcción**: cada área suma 12 h (4 h de levantamiento + 8 h de construcción) y el proyecto, **36 h** (12 h de levantamiento y 24 h de construcción). Las 12 h por área caen dentro de la pauta de Habilidades (8 a 12 h por área). El deck no muestra sesiones ni semanas (CLAUDE.md §4.23): solo horas.
- Servicio (instrucción de Ivana, 13/10/2026): es un servicio de **Habilidades únicamente**. Lo que antes se nombraba como otro servicio es, para el cliente y para el sistema, el **levantamiento de información**: la primera parte del proyecto, de 4 h por área. Por eso `datos.json` y `meta.json` dicen `habilidades`, el eyebrow dice «Servicio de Habilidades» y el deck no usa el nombre de ese otro servicio ni el de sus productos. Decisión del sistema por confirmar: la recomendación de la herramienta de IA que espera el cliente se entrega como resultado del levantamiento («Prioridades»), en vez de un reporte aparte.
- Las 3 áreas son una decisión de Ivana: el primer bloque de la ficha define una sola área («Compras, inventario y costeo», 7 personas). Se partió en precios de proveedores (Proceso 1 de la ficha), costos por orden (Proceso 2) e inventario diario por subárea (tercera tarea real del bloque de Habilidades). Los nombres los propuso el sistema.
- Estructura: formato de Habilidades v3. Cada área tiene un levantamiento de información (4 h) y una solución en uso (8 h). Instrucción de Ivana (14/10/2026): la hoja de inversión **no se divide por etapas** (una sola caja de valor, sin «Parte 1» ni «Parte 2» y sin fases en la duración) y **no hay logros inmediatos**: solo se abordan los procesos mencionados y descritos en la ficha y la minuta (precios de proveedores, costos por orden e inventario diario); el levantamiento no abre procesos nuevos.
- Qué se construye: la ficha y la minuta dan el objetivo (dónde comprar cada día, costo real por orden con facturas en foto, ganancia bruta por orden, inventario diario). Con 8 h por área no se promete todo: cada área recibe «la solución prioritaria que el levantamiento señale» y el alcance acota lo que queda fuera (conexión técnica con la página web y con los proveedores, otras áreas, otros estados, marketing). Riesgo comercial: la dueña espera una automatización completa y lo que se financia es un primer ciclo; conviene reforzarlo en la reunión de revisión.
- Sin nivelación grupal (Fundamentals): no se incluyó porque la instrucción no la menciona y el presupuesto es ajustado (con 2 h para los 7 serían 38 h). El equipo usa la IA «de forma suelta y sin criterio» (un empleado consulta Gemini de manera informal), de modo que una nivelación corta ayudaría.
- Herramienta de IA: no está definida («aún no lo saben, esperan la recomendación»). El deck no nombra ni pre-recomienda ninguna: el levantamiento la recomienda y la licencia va aparte (Intezia no recomienda antes de levantar). No va al deck el uso informal de Gemini.
- Datos: el pedido #2459 trae nombre, dirección y teléfono de un cliente final. La ficha declara que no hay política de datos. El deck dice que no se carga información personal de los clientes de la tienda a ninguna herramienta (solo productos, cantidades, precios y montos). Propuesta del sistema: confirmar con la dueña.
- Portada: 3 hechos de la ficha y la minuta (7 personas entre Excel y WhatsApp; 4 a 5 proveedores sin comparación automática de precios; facturas en foto que se leen a mano). No van, a propósito: la salida del líder que conocía el proceso (dato sensible, está en brief.md), la temporada alta (contexto), los montos de los ejemplos del cliente ni la cita textual de la dueña, ni nombres de personas ni de proveedores.
- Retorno en modo método: no hay horas por proceso ni valor hora. El material del cliente (orden de compra con 5 órdenes, 103 productos y 170 unidades; hoja de costos a 876,80 Bs por dólar; pedido #2459) sirve de ejemplo para el levantamiento y no se cita en el deck. Sin casos logrados con el cliente (primer contacto) ni contratación evitada.
- Sin facilidad de pago (`omitir: ["pago"]`, criterio de Ivana en las propuestas recientes). El presupuesto del cliente es ajustado y sale de las ganancias del supermercado: un plan por hitos (levantamiento y cierre) le calza, pero no se agregó sin que lo pidiera.
- División Educación y sin alianza (supuesto: empresa privada, no se preguntó). Asesora Verónica Rubio, con su contacto de otras propuestas.
- Modalidad mixta (virtual o presencial en el almacén de Caracas): supuesto del sistema. La ficha dice que la dueña viaja y prefiere resolver dudas por escrito antes que en llamadas: el deck lo recoge en la logística y el trabajo se agenda en el horario del equipo.
- Nombre del cliente: «Decamino Market» (ficha, logo y facturas); la minuta de Meet dice «De Camino Market». Contexto interno: la propuesta debe salir antes del miércoles 14/10/2026 a las 3 PM, con reunión de revisión ese día; la dueña enviará una minuta propia del proceso.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md y CLAUDE.md §4.21 y §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas): 36 h en total (una sola caja de valor, sin división por etapas). Decidir si lleva facilidad de pago dado el presupuesto del cliente.
- Confirmar con Ivana que la recomendación de la herramienta de IA va como resultado del levantamiento («Prioridades»), ya que el cliente la esperaba en un reporte final.
- Confirmar con Verónica y con la dueña los nombres de las 3 áreas y que el inventario diario va como área propia.
- Decidir si se agregan 2 h de nivelación para los 7 (38 h en total).
- Confirmar modalidad, quiénes son las 7 personas y quién coordina el proyecto (no hay responsable designado; el líder anterior ya no está).
- Cuando llegue la minuta de la dueña sobre el proceso, contrastarla con la ficha y con este deck: si se contradicen, manda la transcripción o la minuta (§4.23). Solo hay el resumen automático de la reunión, no la transcripción.
- Confirmar con la dueña que las soluciones se prueben sin datos personales de clientes y que la conexión con la página web y con los proveedores quede fuera.
- Enviar la propuesta antes del miércoles 14/10/2026 a las 3 PM y agendar la reunión de revisión.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py decamino-market-cai051      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh decamino-market-cai051             # verifica, genera el PDF y ajusta los campos
```
