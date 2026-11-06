# Programa interno · Fasto · Servicio de Habilidades y Detección (CAI-077)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Resumen interno de David Prato (25/10/2026), transcripciones de las sesiones de Compras y texto de Verónica Rubio (sin Ficha de Levantamiento propia ni transcripción de la reunión de esta propuesta).

## 1. Resumen

- **12 entregables en 4 líneas de trabajo**, **64 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Claude conectado a Estelar**: 12 entregables, 64 h.
- Horas por fase: F1 28 h (7 sol.) · F2 36 h (5 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Inventario y Costos de {cliente_corto} | Claude conectado a Estelar | Oficina de costo, Detección en seis áreas, Recepción de mercancía, Inventario sobre la conexión actual | 64 | 12 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Levantamiento (levantamiento de Costos y Detección en seis áreas) | Construcción (recepción asistida y herramientas de inventario, en uso) |
|---|---|---|
| Inventario y Costos de {cliente_corto} | 28 h · 7 sol. | 36 h · 5 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario, quiénes participan y la carga de datos en Estelar.
- **Levantamiento y Detección**: Costos y seis áreas, con su punto de partida y su Mapa de Calor.
- **Recepción asistida**: La factura precarga la recepción en Estelar.
- **Inventario en uso**: Alertas, distribución, cobertura, conteos y mermas.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Oficina de costo · 1 entregable · 4 h · Claude conectado a Estelar · línea A

Para qué (lo que ve el cliente): Medir cómo se registra cada factura y definir qué construir con Costos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CS-1 | Levantamiento de la oficina de costo (incluye: Tiempo de registro por factura; Facturas por día y errores más frecuentes; Qué sigue en Costos tras la recepción asistida) | Cuatro horas de trabajo con el equipo de Costos. Se mide cuánto toma registrar cada factura, cuántas facturas llegan por día y cuáles son los errores más frecuentes, porque hasta que Costos registra la factura Estelar no deja trasladar la mercancía. Es la condición de la recepción asistida. Entrega el punto de partida de Costos y qué sigue. | - | - | - | 4 | F1 |

### Detección en seis áreas · 6 entregables · 24 h · Claude conectado a Estelar · línea A

Para qué (lo que ve el cliente): Detectar cómo trabajan seis áreas y definir dónde construir después

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| LV-1 | Detección de Recepción | Cuatro horas con el equipo de Recepción. Se recorre cómo trabaja hoy el área, se mide su punto de partida y se define dónde conviene construir después, apoyándose en la conexión con Estelar cuando aplique. Entrega el punto de partida del área y su lugar en el Mapa de Calor. | - | - | - | 4 | F1 |
| LV-2 | Detección de Mercadeo | Cuatro horas con el equipo de Mercadeo. Se recorre cómo trabaja hoy el área, se mide su punto de partida y se define dónde conviene construir después, apoyándose en la conexión con Estelar cuando aplique. Entrega el punto de partida del área y su lugar en el Mapa de Calor. | - | - | - | 4 | F1 |
| LV-3 | Detección de Administración | Cuatro horas con el equipo de Administración. Se recorre cómo trabaja hoy el área, se mide su punto de partida y se define dónde conviene construir después, apoyándose en la conexión con Estelar cuando aplique. Entrega el punto de partida del área y su lugar en el Mapa de Calor. | - | - | - | 4 | F1 |
| LV-4 | Detección de Contabilidad | Cuatro horas con el equipo de Contabilidad. Se recorre cómo trabaja hoy el área, se mide su punto de partida y se define dónde conviene construir después, apoyándose en la conexión con Estelar cuando aplique. Entrega el punto de partida del área y su lugar en el Mapa de Calor. | - | - | - | 4 | F1 |
| LV-5 | Detección de Cuentas por pagar | Cuatro horas con el equipo de Cuentas por pagar. Se recorre cómo trabaja hoy el área, se mide su punto de partida y se define dónde conviene construir después, apoyándose en la conexión con Estelar cuando aplique. Entrega el punto de partida del área y su lugar en el Mapa de Calor. | - | - | - | 4 | F1 |
| LV-6 | Detección de Recursos Humanos | Cuatro horas con el equipo de Recursos Humanos. Se recorre cómo trabaja hoy el área, se mide su punto de partida y se define dónde conviene construir después, apoyándose en la conexión con Estelar cuando aplique. Entrega el punto de partida del área y su lugar en el Mapa de Calor. | - | - | - | 4 | F1 |

### Recepción de mercancía · 1 entregable · 12 h · Claude conectado a Estelar · línea A

Para qué (lo que ve el cliente): Que la factura llegue precargada a la recepción de Estelar

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| RE-1 | Recepción asistida con lectura de facturas (incluye: Foto o escaneo de la factura que precarga la recepción; Validación de una persona antes de cargar; Facturas y recepción ligadas a su orden de compra) | Trabajo de 12 h con los equipos de Inventario y Costos. Hoy un solo analista teclea cada factura y los jueves y viernes llegan de 80 a 90 proveedores, con la mercancía retenida. Se construye con ellos, con Claude, la lectura de la factura (descripción, cantidad y código) para precargar la recepción en Estelar, con validación de una persona antes de cargarla. Es un proyecto nuevo y requiere que Fasto habilite la carga de datos en Estelar. Entrega la recepción asistida en uso. | - | - | - | 12 | F2 |

### Inventario sobre la conexión actual · 4 entregables · 24 h · Claude conectado a Estelar · línea A

Para qué (lo que ve el cliente): Cuatro herramientas de inventario sobre la conexión actual

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| IV-1 | Alertas de fallas y stock mínimo (incluye: Fallas del almacén registradas sin papel; Piso y almacén cruzados sin Excel; Alerta de productos en riesgo de quiebre) | Trabajo de 6 h con el equipo de Inventario. Hoy el almacén anota las fallas en papel y solo una persona cruza piso y almacén en Excel. Se construye con Claude, sobre la conexión con Estelar ya en uso, el registro de fallas y las alertas de stock mínimo. Entrega las alertas en uso. | - | - | - | 6 | F2 |
| IV-2 | Sugerido de distribución por sede (incluye: Cuánto enviar a cada tienda según lo que vende; Existencia y venta de cada sede a la vista; Sugerido revisado por una persona) | Trabajo de 6 h con el equipo de Inventario. Hoy el almacén decide cuánto enviar a cada tienda por su existencia, sin ver lo que vende. Se construye con Claude un sugerido de distribución por sede que cruza existencia y ventas de cada tienda, y una persona lo revisa antes de enviar. Entrega el sugerido en uso. | - | - | - | 6 | F2 |
| IV-3 | Panel de cobertura y vencimientos (incluye: Días de cobertura por producto y por sede; Productos con sobreexistencia o por vencer; Panel compartido con Compras) | Trabajo de 6 h con el equipo de Inventario. Parte del Excel que ya lleva la líder de Inventario y se construye con Claude un panel de cobertura y vencimientos que se comparte con Compras, para ver la sobrecompra antes de que venza. Entrega el panel en uso. | - | - | - | 6 | F2 |
| IV-4 | Conteos priorizados y mermas (incluye: Conteos ordenados por riesgo y diferencia; Ajustes validados con menos pasos manuales; Merma calculada con el mismo método) | Trabajo de 6 h con el equipo de Inventario. Hoy cada diferencia de conteo se valida y se ajusta a mano, y la merma se calcula a mano. Se construye con Claude la priorización de los conteos y el cálculo de la merma, y una persona valida cada ajuste. Entrega los conteos y las mermas en uso. | - | - | - | 6 | F2 |

## 4. Fuera de alcance

- Desarrollar un sistema nuevo: se trabaja sobre Estelar y la conexión actual.
- Habilitar la carga de datos en Estelar: la acuerda Fasto con Sistemas y el proveedor.
- Licencias de Claude y su consumo: los contrata Fasto, aparte de esta inversión.
- Otros subproyectos de Costos y construcción en las demás áreas: siguiente etapa.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (30/10/2026): propuesta CAI-077 para Fasto, asesora Verónica Rubio. Educación y sin alianza (confirmados). **Combo Habilidades y Detección con Habilidades al frente** (Ivana: «es detección y habilidades pero tiene que reflejar que es habilidades»): portada «Servicio de Habilidades y Detección», `meta_servicio: habilidades`, título que empieza por Habilidades. Continuación del servicio de Habilidades para Compras (CAP-104 y su implementación del 5 al 23 de octubre).
- Insumos: resumen interno de David Prato (25/10/2026), transcripciones de las sesiones de Compras y texto de Verónica; no hay Ficha ni transcripción propias de esta propuesta. El levantamiento de Inventario ya está hecho (22/10, enviado el 23/10), por eso no hay levantamiento ni Fundamentos de Inventario: va directo a construcción.
- Alcance (corrección de Ivana, 30/10/2026: «ya va habilidades para inventario y costos y las demás áreas de Fasto para levantar información»): Habilidades en Inventario (cinco subproyectos del PDF de David) y el levantamiento de la oficina de costo, más el **levantamiento de información de las demás áreas de Fasto**, que ya no es siguiente paso. Ivana pidió decir «demás áreas» mientras tanto: no se nombran (en las transcripciones aparecen Mercadeo y Recursos Humanos). La lectura asistida de facturas de Costos se trata como la misma pieza que la recepción asistida. Siguiente paso, sin cotizar: otros subproyectos de Costos (Verónica habló de ocho), carga de mínimos y máximos, Habilidades en las demás áreas y acompañamiento quincenal o mensual.
- Cifras de la portada: del propio cliente y de sus datos de Estelar, con el origen dicho en el texto (80 a 90 proveedores, licor de 167 unidades que vende 0,33 al mes, 1 % a 8 % de recepciones ligadas a su orden). Sin línea «Fuente» (Ivana, 30/10/2026: ninguna presentación lleva fuentes). No se citan las satisfacciones, los 10.000 productos bajo mínimo ni el número de tiendas, ni personas de Fasto.
- Herramienta: se nombra Claude (ya en uso por el servicio anterior), sin precios de licencias, sin VPN y sin «cuesta menos» (frase del argumento interno de David). Estelar es el nombre del sistema; el texto de Verónica dice «Stellar» y el PDF usa «Estelar» para el sistema y «Stellar» para el proveedor: no se nombra al proveedor.
- Requisito: la recepción asistida necesita que Fasto habilite la carga de datos en Estelar (la conexión actual es de solo lectura): va en fuera de alcance, notas y próximos pasos. Sin facilidad de pago, con seguimiento 30-60-90.
- Horas: levantamiento de Costos 4 h + recepción asistida 12 h + cuatro herramientas de 6 h (24 h) = 40 h de Habilidades, tal como estaban (Ivana, 03/11/2026: «mantén las habilidades tal cual»). Detección: 4 h por área en seis áreas = 24 h; total con el equipo 64 h. Reunión de arranque de 1 h aparte. Partes de la hoja de cotización: «Habilidades» (40 h) y «Detección en seis áreas» (24 h), cada una con su caja de valor para Ventas, más el total del proyecto.
- Áreas de la Detección (Ivana, 03/11/2026): Recepción, Mercadeo, Administración, Contabilidad, Cuentas por pagar y RRHH (escrito Recursos Humanos). La lista traía «contabilidad» dos veces: se tomó como una sola (**supuesto mío**, por eso son seis áreas y 24 h). Beneficios de la Detección añadidos a la slide de entregables: Mapa de Calor, Informe Final y hoja de ruta, inversión inteligente en licencias y logros inmediatos (sin cifra); el Mapa de Calor y los logros se incluyen como en el estándar de Detección y están por confirmar con Ivana. La Detección conserva «4 h por área» en el deck (Detección de cada área por separado, sin reparto distinto).

## 6. Cómo trabajamos (slide 5)

**Por qué en este orden:** Primero se mide Costos, porque Estelar no deja trasladar la mercancía hasta que Costos registra la factura; después se construye la recepción y las herramientas de inventario.

- **Medimos**: La oficina de costo y las demás áreas de Fasto.
- **Recibimos**: Recepción asistida, con Inventario y Costos.
- **Sumamos**: Cuatro herramientas sobre la conexión actual.
- **Seguimos**: Uso, ajustes y resultados, a 30, 60 y 90 días.

- En la práctica, **Una persona valida**: La factura se precarga y las sugerencias se calculan; una persona las valida antes de cargarlas.
- En la práctica, **Solo lectura por defecto**: La conexión actual solo lee datos; escribir en Estelar se acuerda con Sistemas y el proveedor.
- En la práctica, **Sin prometer cifras**: Se mide el punto de partida y cada avance; las metas son de Fasto y no se garantizan.
- Datos: La conexión usa un usuario dedicado y consultas predefinidas, sin acceso libre a la base; cada persona tiene su clave y cada consulta queda registrada.
- Quién construye: Intezia construye con Inventario y Costos, sobre la conexión con Estelar ya construida, probada y en uso.

**Logística:** modalidad: Se acuerda en la reunión de arranque, según lo que mejor funcione para los equipos. · participantes: Las personas de Inventario, Costos y las demás áreas que se definan en el arranque. · ritmo: El trabajo se agenda sin frenar la recepción de mercancía, que se concentra los jueves y viernes. · arranque: Apenas se apruebe la propuesta; una reunión de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 7)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Punto de partida; Con la herramienta; Horas recuperadas; Gasto de operar.

## 8. Próximos pasos (slide 9)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

