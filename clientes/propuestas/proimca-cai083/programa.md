# Programa interno · Proimca · Servicio de Habilidades (CAI-083)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (02/11/2026) y transcripción de la reunión de Verónica Rubio con Proimca (02/11/2026).

## 1. Resumen

- **10 soluciones en 4 áreas**, **36 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Gemini en Google Workspace**: 10 soluciones, 36 h.
- Horas por fase: F1 18 h (5 sol.) · F2 18 h (5 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Las cuatro áreas de {cliente_corto} | Gemini en Google Workspace | Administración y contabilidad, CDC (Centro de Contacto), Mercadeo y redes sociales, Planificación técnica | 36 | 10 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Inicio (procesos con los datos que ya tienen) | Enlace (procesos que dependen de sus sistemas) |
|---|---|---|
| Las cuatro áreas de {cliente_corto} | 18 h · 5 sol. | 18 h · 5 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario, quién lidera cada área y el acceso a los datos.
- **Punto de partida**: Se mide cuánto toma hoy cada proceso: el «antes» del retorno.
- **Primeras herramientas**: Conciliación, libros, redes y visitas funcionando.
- **Procesos conectados**: Carga contable, talento humano, CDC y tiempos en calle.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Administración y contabilidad · 4 soluciones · 12 h · Gemini en Google Workspace · línea A

Para qué (lo que ve el cliente): Conciliar pagos, cargar la venta a Odoo y revisar libros con menos retrabajo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AD-1 | Conciliación de pagos con el banco | Tres horas con el equipo de Administración. Cada mes se concilian miles de pagos de clientes contra el estado de cuenta y, cuando la referencia viene errada, hay que revisar el banco uno por uno. Se construye con ellos una herramienta que cruza los pagos con el estado de cuenta y propone con quién coincide cada ingreso, y una persona valida. Entrega la conciliación en uso. | - | - | - | 3 | F1 |
| AD-2 | Carga de la venta diaria a Odoo | Tres horas con las contadoras. Hoy SAE Plus y Odoo no se conectan, y cada día se procesa a mano la venta total para montar la contabilidad. Se construye con ellas la preparación del archivo de la venta diaria para cargarlo en Odoo, con una persona que valida antes de cargar. Depende de los datos que entregue SAE Plus. Entrega la carga diaria en uso. | - | - | - | 3 | F2 |
| AD-3 | Revisión de libros de venta y compra | Tres horas con las contadoras. Antes del libro mayor y del diario se revisa a mano que cada registro tenga cédula, dirección y número de factura. Se construye una revisión asistida que señala lo que falta o no cuadra, y una persona corrige. Entrega la revisión de libros en uso. | - | - | - | 3 | F1 |
| AD-4 | Recibos, vacaciones y liquidaciones | Tres horas con talento humano. Hoy estos procesos son manuales mientras se implementa el módulo de nómina de Odoo. Se construye con el equipo la preparación de recibos, vacaciones y liquidaciones, ajustada a lo que Odoo vaya cubriendo. Entrega los procesos de talento humano en uso. | - | - | - | 3 | F2 |

### CDC (Centro de Contacto) · 2 soluciones · 8 h · Gemini en Google Workspace · línea A

Para qué (lo que ve el cliente): Que ningún cliente quede sin respuesta, de la venta a la postventa

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CD-1 | Control de clientes sin respuesta | Cuatro horas con el equipo del CDC. Todo lo que entra por los canales del cliente, en venta, cobranza y soporte, debe tener respuesta y solución a tiempo. Se construye con el equipo un control que muestra qué contactos siguen sin atender, y una persona decide cómo responder. Depende de los datos que entreguen sus sistemas. Entrega el control en uso. | - | - | - | 4 | F2 |
| CD-2 | Seguimiento de PQR y postventa | Cuatro horas con el equipo del CDC. El ciclo del cliente, de la conexión a la postventa, pasa por dos sistemas que no están integrados. Se construye con el equipo el seguimiento de cada PQR (petición, queja o reclamo) y de la postventa, para que ninguno quede abierto sin responsable. Entrega el seguimiento en uso. | - | - | - | 4 | F2 |

### Mercadeo y redes sociales · 2 soluciones · 8 h · Gemini en Google Workspace · línea A

Para qué (lo que ve el cliente): Ver en un solo resumen qué entra y qué llega por cada red

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| MK-1 | Resumen de métricas de redes sociales | Cuatro horas con los analistas de Mercadeo. Las métricas existen en las herramientas de cada red, pero están dispersas. Se construye con ellos un resumen consolidado que muestra qué entra, qué sale y si el contenido llega a donde se quiere. Entrega el resumen en uso. | - | - | - | 4 | F1 |
| MK-2 | Requerimientos de redes en un solo lugar | Cuatro horas con los analistas de Mercadeo. Los requerimientos entran dispersos por Instagram, Facebook y Telegram, sin comunicación entre canales. Se construye con ellos el orden de esos requerimientos en un solo lugar, con su estado. Entrega el seguimiento de requerimientos en uso. | - | - | - | 4 | F1 |

### Planificación técnica · 2 soluciones · 8 h · Gemini en Google Workspace · línea A

Para qué (lo que ve el cliente): Cerrar las visitas sin retrabajo y medir si se cumplen los tiempos acordados

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PT-1 | Carga y cierre de visitas técnicas | Cuatro horas con la gerencia y los supervisores de cada sucursal. Hoy el técnico trae la visita en papel y cada supervisor la vacía a mano y la cierra en el sistema que la generó. Se construye con ellos una forma de pasar cada visita a datos y cerrarla con menos pasos manuales. Entrega la carga y el cierre en uso. | - | - | - | 4 | F1 |
| PT-2 | Cumplimiento de tiempos en calle | Cuatro horas con la gerencia de planificación. No hay una estadística confiable de si se cumplen los tiempos acordados de instalación y atención de fallas. Se construye con ellos el tablero de cumplimiento a partir de las visitas ya cargadas. Depende de PT-1. Entrega el tablero en uso. | - | - | - | 4 | F2 |

## 4. Fuera de alcance

- Licencias de IA y su consumo: las contrata Proimca, aparte de esta inversión.
- Conectar SAE Plus con Odoo: los proveedores no han permitido una API; se usa lo que cada sistema exporta.
- Los ajustes al bot de WhatsApp del CRM: es un proyecto aparte, del área de Tecnología.
- El manual de uso y gobernanza de la IA: es el servicio de Políticas, el paso que sigue.
- Traslado del equipo de Intezia a Barquisimeto: los viáticos los asume Proimca o se cotizan aparte.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (03/11/2026): propuesta de Habilidades CAI-083 para Proimca con Verónica Rubio como asesora, a partir de la Ficha de Levantamiento y la transcripción del 02/11/2026. División Educación y sin alianza: por confirmar con Ivana. Sin facilidad de pago: criterio de Ivana en las últimas propuestas (OCAATVE, Suri Import); no lo dijo para esta, confirmar.
- Insumos: ficha y transcripción coinciden. Primer contacto. Telecomunicaciones (internet y televisión) en Lara; ISO 9001 reciente. Damaris Pérez García es directora y parte del grupo de 2 o 3 directores que aprueba caso por caso, por costo-beneficio; sin partida fija. Descartó Detección («ya hemos avanzado mucho»): va directo a Habilidades y la secuencia Habilidades, Políticas e Innovación («va por paso»).
- Áreas: las cuatro que ella eligió, en una sola fase («primero cuatro áreas»): Administración y contabilidad (con talento humano, una sola gerencia), CDC, Mercadeo y Planificación técnica (unas 23 personas). Ella dijo que quizá no todas al mismo tiempo; la fase 1 y la fase 2 reparten el orden, no los equipos.
- Herramienta (supuesto mío, por confirmar con Verónica o Ivana): Gemini en Google Workspace, que ya usan y la empresa tiene incluido, con NotebookLM. Damaris preguntó en qué áreas hacen falta licencias corporativas (también ha considerado Claude): la «Recomendación de licencias por área» responde esa pregunta y no pre-decide una herramienta. No se menciona Claude ni VPN (Venezuela no es país soportado).
- Horas (lineamiento de empresa/politicas-comerciales.md, 8 a 12 h por área hasta 5 procesos): Administración 12 h (4 procesos × 3 h, la gerencia que más retrabajo tiene), CDC 8 h, Mercadeo 8 h y Planificación técnica 8 h = 36 h con el equipo, mi reparto por solución. Las 10 soluciones salen de las tareas reales de la ficha. Sin Fundamentos ni nivelación aparte: sus cursos internos no prendieron, el método es aprender haciendo sobre sus procesos.
- Fases (mi criterio, por confirmar): fase 1 «Inicio» (18 h) = procesos con datos que ya tienen (conciliación, libros, redes, carga de visitas); fase 2 «Enlace» (18 h) = procesos que dependen de datos de sus sistemas (SAE Plus a Odoo, talento humano mientras llega la nómina de Odoo, CDC entre HiBot y SAE Plus, tiempos en calle sobre las visitas cargadas).
- Fuera de alcance, dicho por Verónica en la reunión: los ajustes al bot de HiBot (proyecto aparte, de Tecnología) y el traslado a Barquisimeto (viáticos de Proimca o cotizados aparte, como con DUSA). La gobernanza que pide Damaris es el servicio de Políticas, siguiente paso; la «política de uso de IA» que ellos mismos redactan queda fuera.
- Retorno en modo método, sin cifras (el volumen de conciliaciones es «miles» y no hay horas). Su indicador duro es la retención (perder como máximo 1 % de la base): en el deck solo aparece como «meta de retención» sin la cifra, porque no está validada con el área.
- Calendario (no va en el deck, §4.23): días de corte del 6 al 10 de cada mes se evitan (dato del cliente en «ritmo»); horario de 8:00 a. m. a 5:00 p. m. de lunes a sábado; Intezia recomendó encuentros de 2 horas y no se fijó la frecuencia. Revisión de la propuesta el jueves 05/11/2026 a las 10:30 a. m.; Verónica prometió enviarla el 03/11 al final de la tarde o el 04/11 por la mañana.
- Del texto de Verónica no se toman los 10 roles delegables de DUSA ni la reubicación de personal. Las citas de la ficha no se usan. Sin semanas, sesiones ni fechas; sin horas de trabajo ni cantidad de consultores (CLAUDE.md §4.23).
- 04/11/2026 (Ivana): se quitó el IVA de la hoja de inversión, porque Intezia no lo ofrece; los totales quedan en subtotal, descuento y total (`sin_iva` en `inversion.desglose`).

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se mide el punto de partida; después se construye en dos fases: los procesos que parten de datos que ya tienen y luego los que dependen de sus sistemas.

- **Medimos**: Cuánto toma hoy cada proceso y quién lo hace.
- **Construimos**: Cada herramienta con el equipo, sobre sus casos reales.
- **Adoptamos**: Cada persona la usa en su trabajo hasta sostenerla.
- **Seguimos**: Uso, ajustes y resultados, a 30, 60 y 90 días.

- En la práctica, **Una persona revisa**: La IA propone conciliaciones, asientos y respuestas; una persona las revisa antes de cargarlas o enviarlas.
- En la práctica, **Un criterio común**: Mismas reglas de uso en todas las áreas, dentro de las cuentas de la empresa.
- En la práctica, **Sin tocar sus sistemas**: SAE Plus, Odoo y el CRM no se modifican: se trabaja con los datos que cada uno entrega.
- Datos: Los datos de clientes, pagos y nómina no se cargan a la IA sin la autorización de Proimca; se trabaja con cuentas de la empresa y los accesos que autoriza su área de Tecnología.
- Quién construye: Se construye con el equipo: Intezia guía y cada persona prueba la herramienta sobre sus propios casos, dentro del entorno Google que ya usan.

**Logística:** modalidad: Virtual; si conviene, algún encuentro presencial en Barquisimeto, con viáticos aparte. · participantes: Unas 23 personas de las cuatro áreas, con sus líderes y los supervisores por sucursal. · ritmo: Se agenda sin frenar la operación y fuera de los días de corte de cada mes (del 6 al 10). · arranque: Apenas se apruebe la propuesta; una reunión de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Punto de partida; Con la herramienta; Horas recuperadas; Gasto de operar.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

