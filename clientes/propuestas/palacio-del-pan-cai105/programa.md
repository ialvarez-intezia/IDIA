# Programa interno · El Palacio del Pan · Servicio de Habilidades (CAI-105)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Informe del sistema v14 (17/11/2026), Esquema del sistema v3, Datos base del sistema v10 y Recetas de referencia v2 del cliente; DET-051 (Ficha y transcripción del 02/11/2026).

## 1. Resumen

- **16 entregables en 4 áreas**, **48 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **IA para la administración**: 16 entregables, 48 h.
- Horas por fase: F1 24 h (8 sol.) · F2 24 h (8 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Administración de la panadería | IA para la administración | Cierre de caja, Cuentas por pagar, Producción y costos, Inventario y compras | 48 | 16 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Caja y pagos (cierre de caja y cuentas por pagar) | Producción e inventario (costos, inventario y compras) |
|---|---|---|
| Administración de la panadería | 24 h · 8 sol. | 24 h · 8 sol. |

- **Arranque**: Se confirman los participantes y los accesos, y se verifica la integración con las herramientas.
- **Caja y pagos**: El cierre de caja y las cuentas por pagar, construidos y probados con ejemplos.
- **Producción e inventario**: Recetario, costos e inventario, construidos con las 13 recetas entregadas.
- **Cierre**: Las cuatro áreas en uso diario; empieza la garantía a 30, 60 y 90 días.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Cierre de caja · 4 entregables · 12 h · IA para la administración · línea A

Para qué (lo que ve el cliente): Cerrar cada turno una sola vez y cuadrar lo físico con los bancos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CC-1 | Cierre de turno en una sola captura | Efectivo en bolívares y dólares, lotes de los puntos de venta y lo facturado contra lo cobrado, registrados una sola vez al terminar el turno. | - | - | - | 3 | F1 |
| CC-2 | Arqueo del día siguiente | La administración valida que los cierres coinciden con lo físico y con el banco; los faltantes y sobrantes quedan con su motivo. | - | - | - | 3 | F1 |
| CC-3 | Cruce de lotes con los bancos | El lote de cada punto de venta contra lo que abona cada banco, para ver las diferencias a tiempo. | - | - | - | 3 | F1 |
| CC-4 | Resumen diario por medio de pago | Los ingresos del día por medio de pago, listos para entregar al contador. | - | - | - | 3 | F1 |

### Cuentas por pagar · 4 entregables · 12 h · IA para la administración · línea A

Para qué (lo que ve el cliente): Saber cuánto falta por pagar de cada factura, aunque se pague en abonos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CP-1 | Registro de facturas sin duplicados | Número, número de control, fecha, exento, base, IVA y total de cada factura de compra; una factura no se carga dos veces. | - | - | - | 3 | F1 |
| CP-2 | Saldo de cada factura con abonos | Cada pago parcial se descuenta de la factura y se ve lo que falta por pagar de cada una. | - | - | - | 3 | F1 |
| CP-3 | Programación de pagos sugerida | Según los ingresos y los compromisos fijos, indica qué facturas se pueden pagar; la programación definitiva la escoge una persona. | - | - | - | 3 | F1 |
| CP-4 | Antigüedad de saldos de proveedores | Lo que se debe a cada proveedor, ordenado por antigüedad, como auxiliar para el contador. | - | - | - | 3 | F1 |

### Producción y costos · 4 entregables · 12 h · IA para la administración · línea A

Para qué (lo que ve el cliente): Conocer el costo y el margen de cada tanda y de cada producto

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PC-1 | Recetario de las 13 recetas | Las recetas de referencia, con varios niveles (una masa o una crema pueden ser ingrediente de otro producto) y los productos que sirven para cada ingrediente. | - | - | - | 3 | F2 |
| PC-2 | Plan de producción del día | Qué tandas se hacen cada día y cuánto sale de cada una, a partir del recetario. | - | - | - | 3 | F2 |
| PC-3 | Costo de cada tanda y producto | El costo de cada tanda según los ingredientes de la última compra, repartido entre los productos que salen de ella. | - | - | - | 3 | F2 |
| PC-4 | Margen y alerta bajo el costo | El margen de cada producto y un aviso cuando el valor de venta queda por debajo del costo. | - | - | - | 3 | F2 |

### Inventario y compras · 4 entregables · 12 h · IA para la administración · línea A

Para qué (lo que ve el cliente): Contar y reponer con alertas, y recibir las compras sin teclear de más

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| IC-1 | Fichas de productos con unidades | Unidad de compra, unidad de uso y cuántas unidades trae cada una, completadas para los productos que hoy no las tienen. | - | - | - | 3 | F2 |
| IC-2 | Conteo físico guiado | Una lista guiada para contar el inventario, con las diferencias contra lo que el sistema espera. | - | - | - | 3 | F2 |
| IC-3 | Alertas de mínimo y de merma | Aviso cuando un producto baja de su cantidad mínima y registro de la merma de insumos y de producto terminado. | - | - | - | 3 | F2 |
| IC-4 | Orden de compra y recepción | La orden de compra al proveedor y la recepción de la mercancía contra la factura, que alimenta el inventario y las cuentas por pagar. | - | - | - | 3 | F2 |

## 4. Fuera de alcance

- Un sistema integral que reemplace a Profit: se construyen las herramientas de cuatro áreas, no el sistema completo.
- Facturación fiscal e impresora fiscal: siguen en el sistema que la panadería usa hoy.
- Contabilidad, nómina, impuestos, mercadeo y mantenimiento: los asientos los sigue llevando el servicio contable.
- Licencias de IA: no están en la inversión; se confirman en el arranque.

## 5. Supuestos a confirmar (antes del método)

- Ajuste de Ivana (18/11/2026): el deck dice, en «Cómo trabajamos» y en el hito de arranque, que lo que se construye depende de las herramientas y de la facilidad de integrarse a ellas, y que se verifica en el arranque (el informe del cliente dice que Profit no tiene API ni importador). No se nombra Profit en esa frase.
- Pedido de Ivana (18/11/2026): propuesta de Habilidades a partir del paquete que El Palacio del Pan envió a los proveedores del sistema (Informe v14, Esquema v3, Datos base v10, Recetas v2) y de lo que ya se sabe por DET-051. Asesora: Verónica Rubio.
- Decisiones de Ivana (18/11/2026): alcance de cuatro áreas (cierre de caja, cuentas por pagar, producción y costos, inventario y compras), 12 h por área = 48 h con el equipo, sin nombrar herramienta de IA, impacto «operación». División Educación y alianza = no: tomados por mí (misma cuenta que DET-051), no los dio Ivana.
- Reparto mío: cada área en 4 entregables de 3 h, tomados del informe (cierre por turno, arqueo, conciliación de lotes y resumen diario de cierres; registro de facturas, abonos, programación de pagos y antigüedad de saldos; recetario, plan del día, costo de cada tanda y margen; fichas con unidades, conteo guiado, alertas de mínimo y merma, orden de compra y recepción). Fase 1 = los dos cuellos de botella que marca el informe; fase 2 = producción e inventario, que parten de los datos base.
- Lo que el cliente pide es un sistema integral de 15 módulos que reemplace a Profit y lo ofrece a varios proveedores. El deck no promete un sistema completo: dice qué se construye (cuatro áreas) y deja explícito lo que queda fuera (sistema integral, facturación fiscal, contabilidad, nómina, impuestos, mercadeo y mantenimiento).
- Hechos de la portada: salen del propio informe del cliente (cierre tecleado dos veces, cuentas por pagar con abonos en Excel, Profit sin costo de lo vendido, 775 productos y 13 recetas). No se cita su fuente en el deck (regla de fuentes en presentaciones).
- Profit no se nombra en las soluciones; solo en «Fuera de este alcance» (reemplazarlo no es parte del servicio). No se afirma que la panadería migre ni que las herramientas se conecten con Profit (§4.11): el informe dice que el sistema nuevo no se conecta con él.
- Datos fiscales y de nómina: fuera de alcance. No se cargan datos de clientes ni cuentas bancarias a la IA; los 775 productos, recetas y proveedores se usan como datos de prueba, que el informe declara «de referencia».
- Herramienta (Ivana): sin nombrar. Juan Carlos ya probó Claude Code por su cuenta; no se menciona Claude ni VPN (Venezuela no es país soportado).
- Enfoque del cuadro Impacto: operación (Ivana, 18/11/2026), sin posiciones ni nómina: no hay aval del cliente. La pregunta de Juan Carlos sobre roles y cuántas personas (DET-051) no se responde en esta propuesta.
- Seguimiento 30-60-90 incluido por ser estándar de Habilidades y porque responde a la objeción de adopción de DET-051; Ivana puede quitarlo. Sin facilidad de pago (omitir: pago, regla permanente). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23): el informe habla de conteo semanal y de calendarios de avisos; no aparecen en el deck.
- Contacto de la última slide: Verónica Rubio, asesora comercial.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero la caja y los pagos, que hoy dan más trabajo; después producción e inventario, que parten de los datos base ya entregados.

- **Construimos**: Con quien hace la tarea y con sus casos reales.
- **Probamos**: Con ejemplos de cierres y facturas que la panadería autoriza.
- **Adoptamos**: Cada equipo usa su herramienta en el día a día.
- **Medimos**: El tiempo ganado en cada tarea, a 30, 60 y 90 días.

- En la práctica, **Con quien hace el trabajo**: Cada herramienta se construye con quien cierra la caja, paga las facturas o produce, para que la use desde el primer día.
- En la práctica, **Con datos ya entregados**: Se parte de los productos, recetas y proveedores que la panadería preparó, usados como datos de prueba.
- En la práctica, **Depende de las herramientas**: Lo que se construye depende de las herramientas de IA y de los sistemas que la panadería usa, y de qué tan fácil sea integrarse a ellos: se verifica en el arranque.
- Datos: Las claves, las cuentas bancarias y los datos de nómina no se cargan a la IA: se trabaja con ejemplos que la panadería autoriza.
- Quién construye: Intezia guía y el equipo de la panadería construye con la IA sus propias herramientas, sobre lo que ya usa.

**Logística:** modalidad: Presencial en la panadería o en línea, según se acuerde en la reunión de arranque. · participantes: Quienes hacen la tarea en caja, administración, compras y producción. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas del área; Tiempo actual por tarea; Tiempo con la herramienta; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> El cierre de caja se hace una sola vez, los saldos con los proveedores están al día y la panadería conoce el costo, el margen y el inventario de cada producto, con sus propios datos.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

