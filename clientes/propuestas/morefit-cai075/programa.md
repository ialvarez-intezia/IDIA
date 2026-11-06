# Programa interno · MoreFit · Servicio de Habilidades (CAI-075)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (28/10/2026) y transcripción de la reunión de Verónica Rubio con Corporación MoreFit (28/10/2026).

## 1. Resumen

- **5 entregables en 3 líneas de trabajo**, **18 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Herramientas de IA del equipo**: 5 entregables, 18 h.
- Horas por fase: F1 6 h (2 sol.) · F2 12 h (3 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Equipo de {cliente_corto} | Herramientas de IA del equipo | Fundamentos de IA, Levantamiento de las cinco áreas, Pedidos, facturación e inventario | 18 | 5 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Nivelación y levantamiento (equipo nivelado y punto de partida medido) | Construcción (procesos construidos con el equipo y en uso) |
|---|---|---|
| Equipo de {cliente_corto} | 6 h · 2 sol. | 12 h · 3 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario, quiénes participan y quién coordina por MoreFit.
- **Nivelación y levantamiento**: Fundamentos de IA y cómo trabaja hoy cada área.
- **Procesos en uso**: Pedidos, facturación e inventario.
- **30 · 60 · 90 días**: Seguimiento: uso de las herramientas, ajustes y avances medidos.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Fundamentos de IA · 1 entregable · 2 h · Herramientas de IA del equipo · línea A

Para qué (lo que ve el cliente): Llevar a todo el equipo al mismo punto, para que participe en la construcción y la sostenga

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NV-1 | Fundamentos de IA para todo el equipo (incluye: Qué es la IA y qué puede hacer por la operación; Cómo pedirle bien, con ejemplos del trabajo del equipo; Qué datos se cuidan y cuáles no se cargan) | Módulo de 2 h con el equipo, en un solo grupo. Nadie ha usado IA todavía, así que se parte de cero: qué es, cómo se le pide bien y qué puede hacer por los pedidos, la facturación y el inventario, con ejemplos del trabajo de cada persona. Se acuerdan las pautas básicas de qué datos se cuidan y cuáles no se cargan. Entrega al equipo con una noción común. | - | - | - | 2 | F1 |

### Levantamiento de las cinco áreas · 1 entregable · 4 h · Herramientas de IA del equipo · línea A

Para qué (lo que ve el cliente): Medir cómo trabaja hoy cada área, ver los cuellos de botella y definir qué construir

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| LV-1 | Levantamiento de las cinco áreas (incluye: Cómo trabaja hoy cada una de las cinco áreas; Dónde están los cuellos de botella de cada proceso; Qué construir primero y en qué orden) | Cuatro horas de entrevista y observación con el equipo en las cinco áreas: venta al detalle, venta al mayor, producción, administración y facturación, e inventario. Se recorre cómo trabaja cada una, se mide el punto de partida y se confirman los procesos a construir y su orden. Entrega el punto de partida y el plan de construcción. | - | - | - | 4 | F1 |

### Pedidos, facturación e inventario · 3 entregables · 12 h · Herramientas de IA del equipo · línea A

Para qué (lo que ve el cliente): Ordenar con IA los pedidos, la facturación y el inventario

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CO-1 | Pedidos del canal al detalle con IA (incluye: Del mensaje de WhatsApp al pedido listo, sin transcribir a mano; Un mismo formato para todos los pedidos que llegan; Registro claro de cada pedido y su estado) | Trabajo de 4 h con quien lleva la venta al detalle y su apoyo. Buena parte de los clientes pide por el WhatsApp de la empresa y el equipo monta cada pedido a mano en la tienda en línea. Se construye con herramientas de IA el camino de cada pedido: se lee el mensaje, se ordena el pedido y queda listo para montarlo. Una persona revisa cada pedido antes de confirmarlo. Entrega el proceso de pedidos en uso. | - | - | - | 4 | F2 |
| CO-2 | Facturación y administración ordenadas con IA (incluye: Facturas preparadas a partir del pedido, sin escribir todo de nuevo; Control de lo facturado, lo cobrado y lo pendiente; Información lista para la administradora y el contador) | Trabajo de 4 h con la administración. Hoy la facturación es manual y no hay un sistema administrativo. Se construye con herramientas de IA un orden de trabajo para preparar cada factura, controlar lo facturado y lo pendiente y dejar la información lista para quien la revisa. Esta propuesta no implementa un sistema administrativo (ERP): ordena lo que hoy se hace a mano. Entrega la facturación y el control en uso. | - | - | - | 4 | F2 |
| CO-3 | Control de inventario con IA (incluye: Inventario de producto terminado y materia prima al día; Entradas y salidas registradas con un mismo método; Alertas de lo que se acaba, para comprar a tiempo) | Trabajo de 4 h con quien lleva el inventario. Se parte de las hojas de Excel que ya existen y se construye con herramientas de IA un control único de producto terminado y materia prima: cada entrada y salida se registra con el mismo método y se ve qué se está acabando. Las recetas y los gramajes quedan fuera: no se cargan. Entrega el control de inventario en uso. | - | - | - | 4 | F2 |

## 4. Fuera de alcance

- Implementar un sistema administrativo (ERP): se ordena la facturación con IA, pero no se instala un sistema.
- Licencias y consumo de las herramientas de IA: los contrata MoreFit, aparte de esta inversión.
- Marketing y redes: los lleva un proveedor externo y no forman parte de este alcance.
- Ventas: son una meta de MoreFit; se acompañan y miden, no se garantizan.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (29/10/2026): propuesta CAI-075 para MoreFit (Corporación MoreFit / Inversiones MoreFit), asesora Verónica Rubio. Habilidades con un levantamiento previo corto (la ficha pide contemplarlo y darle mayor peso a Habilidades; Verónica lo ofreció como «un poquito de detección»), sin nombrar Detección. Educación, sin alianza, sin facilidad de pago, con seguimiento 30-60-90: confirmados por Ivana.
- Insumos: Ficha de Levantamiento y transcripción del 28/10/2026 (completa). Primer contacto. Fabricante y distribuidor de alimentos saludables, 9 a 10 personas, operación 100 % manual, nunca han usado IA, sin ecosistema tecnológico definido (Excel y un disco duro compartido). Decisión compartida: la directora de ventas al mayor (contacto) y Morela, que aprueba; la contacto presenta la propuesta. El deck no nombra personas.
- Horas (confirmadas por Ivana): 2 h de Fundamentos de IA en un grupo + 4 h de levantamiento en las cinco áreas (venta al detalle, venta al mayor, producción, administración y facturación, inventario; Marketing queda fuera por ser tercerizado) + 12 h de construcción (4 h por proceso) = 18 h con el equipo. Reunión de arranque de 1 h aparte. El reparto interno de las 4 h de levantamiento entre áreas es mío, por confirmar.
- Construcción (Ivana, 29/10/2026): se dejan **solo los tres procesos principales de la ficha**: toma y montaje de pedidos del canal al detalle (WhatsApp a la tienda en línea), facturación y administración, y control de inventario. Las órdenes de compra de los aliados y el apoyo comercial para abrir más puntos de venta no van (antes Ivana había cambiado los pedidos por las órdenes de compra; la última instrucción manda). Las cinco áreas siguen en el levantamiento: interpretación mía, por confirmar.
- Sin ERP (Ivana): la directora pidió «un sistema administrativo». La propuesta lo dice claramente en el alcance, en el método y en la hoja de inversión: ordena la facturación con IA, no implementa un ERP. Si el cliente lo quiere, es otra conversación.
- Herramientas (Ivana): no se nombra ninguna herramienta de IA; el cliente espera la recomendación y el levantamiento orienta cuáles hacen falta. Sin VPN ni mención al acceso desde Venezuela.
- Datos (de la ficha): las recetas, los gramajes y la base de datos de aliados son confidenciales y se excluyen de las herramientas de IA; está escrito en «Cómo trabajamos» y en el inventario.
- Contexto interno que no va en el deck: empresa que se achicó («hemos tenido que prescindir de personal»), año difícil y caída de ventas, presupuesto por aprobación (sin monto definido), las barras las maquila un tercero. Sin casos de éxito, sin «curso», sin semanas, sesiones ni fechas, sin kickoff ni agenda. La reunión de revisión con la cliente queda propuesta para el martes 3/11/2026, por confirmar.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se nivela al equipo y se observa cómo trabaja cada área, para construir donde más pesa; después se construye, y el equipo lo sostiene sin depender de Intezia.

- **Nivelamos**: Fundamentos de IA para que todo el equipo parta del mismo punto.
- **Medimos**: Cómo trabaja hoy cada área y dónde están los cuellos de botella.
- **Construimos**: Con el equipo, sobre sus pedidos, su facturación y su inventario.
- **Seguimos**: Uso, ajustes y resultados, a 30, 60 y 90 días.

- En la práctica, **Una persona en el circuito**: La IA prepara y ordena; una persona revisa cada pedido y cada factura antes de confirmarlos.
- En la práctica, **Sin instalar un sistema**: Se ordena lo que hoy se hace a mano con herramientas de IA; no se implementa un sistema administrativo (ERP).
- En la práctica, **Sin prometer cifras**: Se mide el punto de partida y cada avance; las metas son de MoreFit y no se garantizan.
- Datos: Las recetas, los gramajes y la base de datos de los aliados no se cargan a ninguna herramienta de IA; solo se usan los datos que MoreFit autoriza.
- Quién construye: Intezia construye junto al equipo, sobre sus casos reales: sus pedidos, su facturación y su inventario.

**Logística:** modalidad: Se acuerda en la reunión de arranque, según lo que mejor funcione para el equipo. · participantes: El equipo de MoreFit: venta al detalle, venta al mayor, producción, administración e inventario. · ritmo: El trabajo se agenda sin frenar la operación diaria de un equipo pequeño. · arranque: Apenas se apruebe la propuesta; una reunión de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Punto de partida; Con la herramienta; Horas recuperadas; Gasto de operar.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

