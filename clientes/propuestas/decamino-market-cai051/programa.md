# Programa interno · Decamino Market · Servicio de Habilidades (CAI-051)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento y resumen de la reunión (sin transcripción) e instrucción del usuario.

## 1. Resumen

- **6 entregables en 3 áreas**, **36 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Habilidades**: 6 entregables, 36 h.
- Horas por fase: F1 12 h (3 sol.) · F2 24 h (3 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Compras, costos e inventario | Habilidades | Precios de proveedores, Costos por orden, Inventario diario | 36 | 6 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Levantamiento (levantar las 3 áreas y priorizar) | Uso (3 soluciones construidas y en uso) |
|---|---|---|
| Compras, costos e inventario | 12 h · 3 sol. | 24 h · 3 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario y quién coordina el proyecto por Decamino Market.
- **Levantamiento**: 3 áreas, 4 h cada una: cómo se trabaja hoy cada proceso.
- **Prioridades**: La solución de cada área y la recomendación de la herramienta de IA.
- **Soluciones**: 3 áreas, 8 h cada una: la solución de cada área, en uso.
- **30 · 60 · 90 días**: Seguimiento: uso de las soluciones, ajustes y tiempo recuperado.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Precios de proveedores · 2 entregables · 12 h · Habilidades · línea A

Para qué (lo que ve el cliente): Comparar los precios de los 4 o 5 proveedores y saber dónde comprar cada producto

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PRE-1 | Levantamiento de Precios de proveedores (incluye: Cómo se decide hoy dónde comprar y con qué datos; Qué se escapa hoy en esa decisión) | Trabajo de 4 h con el equipo de compras. Proceso a levantar: el mapeo de precios de los 4 o 5 proveedores cercanos al almacén para la compra diaria de víveres (el corte de órdenes es a medianoche; un proveedor, Polar, publica su lista en Excel o por WhatsApp y los demás tienen página web). Se mapea cómo se decide hoy dónde comprar, con qué datos y qué se escapa. Entrega el diagnóstico del proceso. | - | - | - | 4 | F1 |
| PRE-2 | Solución de Precios de proveedores, construida y en uso (incluye: Apoya la decisión de dónde comprar cada producto; Parte de los listados de los 4 o 5 proveedores) | Trabajo de 8 h con el equipo de compras. Se construye la solución que el levantamiento priorizó para decidir dónde comprar cada producto al mejor precio, con base en las páginas de los proveedores y en la lista que el equipo sube a medianoche. Referencia del cliente: saber desde las 6 am dónde comprar cada producto y en qué cantidad. Entrega la solución funcionando y en uso por el equipo. La conexión técnica con los sistemas de los proveedores queda fuera de alcance. | - | - | - | 8 | F2 |

### Costos por orden · 2 entregables · 12 h · Habilidades · línea A

Para qué (lo que ve el cliente): Costo real y ganancia bruta de cada orden, separando lo que corresponde a cada supermercado

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| COS-1 | Levantamiento de Costos por orden (incluye: Cómo se concilian hoy las facturas con el inventario; Cómo se separa lo que corresponde a cada supermercado; Cuánto tarda hoy y dónde se pierde el dato) | Trabajo de 4 h con el equipo de compras y las personas que reportan el inventario. Proceso a levantar: la conciliación diaria de costos de compra por orden (facturas en JPG frente a inventario) y la separación de lo que corresponde a cada supermercado cuando un mismo proveedor surte a los dos. Se mide cuánto tarda hoy y dónde se pierde el dato (lectura visual de montos, fórmulas de Excel). Entrega el diagnóstico del proceso. | - | - | - | 4 | F1 |
| COS-2 | Solución de Costos por orden, construida y en uso (incluye: Apoya la lectura de las facturas en foto; Costo real de cada orden frente al valor publicado; Ganancia bruta de la orden y su porcentaje) | Trabajo de 8 h con las mismas personas. Se construye la solución que el levantamiento priorizó para leer las facturas de compra (JPG), obtener el costo real de cada orden, compararlo con el valor publicado en la página y mostrar la ganancia bruta y su porcentaje. Referencia del cliente: valor de venta en la página, costo según la factura de cada proveedor y ganancia por orden con la tasa del día. Entrega la solución en uso. La conexión técnica con la página web requiere permisos de quien la administra y queda fuera de alcance. | - | - | - | 8 | F2 |

### Inventario diario · 2 entregables · 12 h · Habilidades · línea A

Para qué (lo que ve el cliente): Tener el inventario diario por subárea en un solo lugar, no en mensajes de WhatsApp

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| INV-1 | Levantamiento de Inventario diario (incluye: Cómo se registra y consulta hoy el inventario por subárea; Cómo se reporta hoy por WhatsApp el inventario del día) | Trabajo de 4 h con las personas que reportan el inventario por subárea (cárnicos, charcutería y pollo; víveres; vegetales). Proceso a levantar: cómo se registra y se consulta hoy el inventario del día, que se reporta por WhatsApp. Entrega el diagnóstico del proceso. | - | - | - | 4 | F1 |
| INV-2 | Solución de Inventario diario, construida y en uso (incluye: Inventario diario por subárea en un solo lugar; Alimenta el cálculo del costo por orden) | Trabajo de 8 h con las mismas personas. Se construye la solución que el levantamiento priorizó para registrar y consultar el inventario diario por subárea en un solo lugar, de modo que alimente el cálculo del costo por orden. Entrega la solución en uso. | - | - | - | 8 | F2 |

## 4. Fuera de alcance

- La conexión técnica con la página web y con los sistemas de los proveedores: requiere permisos de quienes los administran.
- Más de una solución por área: cada una recibe 8 h de construcción, lo demás va en otra etapa.
- Otras áreas, la réplica en otros estados y el marketing con IA: van en otra etapa, según el resultado.
- Licencias de IA: la herramienta se define con el levantamiento y su licencia va aparte.

## 5. Supuestos a confirmar (antes del método)

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

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se levanta la información de cada área y se prioriza con ella; después se construye en cada una la solución que el levantamiento respalda.

- **Levantamos**: Los procesos reales de cada área y su cuello de botella.
- **Construimos**: Con lo levantado, la solución de cada área, hasta dejarla en uso.
- **Adoptamos**: El equipo usa la solución en su trabajo diario, con acompañamiento.
- **Medimos**: El tiempo recuperado contra la línea base, a 30, 60 y 90 días.

- En la práctica, **Horas por área**: 4 h de levantamiento y 8 h de construcción por área, con las personas que hacen el trabajo.
- En la práctica, **Con sus datos reales**: El levantamiento y las soluciones se trabajan sobre sus facturas, listas de precios y reportes de inventario.
- En la práctica, **Lo prioriza el levantamiento**: La herramienta de IA y la solución de cada área nacen de lo que se encuentra al levantar la información.
- Datos: En el trabajo con el equipo no se carga a ninguna herramienta de IA información personal de los clientes de la tienda (nombres, direcciones, teléfonos): solo productos, cantidades y montos. Los criterios de uso seguro se acuerdan al empezar.
- Quién construye: Intezia levanta y construye con las personas de cada área, sobre sus facturas, listas y reportes reales.

**Logística:** modalidad: Mixta: virtual o presencial en el almacén, según se acuerde en la reunión de arranque. · participantes: 7 personas del equipo operativo: compras, armado, despacho e inventario. · ritmo: Dudas por escrito antes que en llamadas; el trabajo se agenda en el horario del equipo. · arranque: La fecha la fija Decamino Market; una reunión de arranque de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperadas; Valor en dinero.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

