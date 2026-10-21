# Programa interno · DUSA · Servicio de Habilidades (CAI-059)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: DUSA_Habilidades_Procesos_Ruta_y_Horas_6.docx (Intezia C.A., Dirección de Productos y Servicios, 02/10/2026), vía datos.ejemplo-dusa.json (CAI-035 en la plantilla v3); instrucciones de Ivana del 20/10/2026.

## 1. Resumen

- **45 soluciones en 11 áreas (más 1 paso previo)**, **572 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Microsoft 365 Copilot**: 17 soluciones, 173 h.
- Herramienta **Claude Team**: 28 soluciones, 399 h.
- Horas por fase: F0 12 h (1 sol.) · F1 224 h (19 sol.) · F2 148 h (13 sol.) · F3 188 h (12 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Eje de Finanzas y Comercial | Microsoft 365 Copilot | Contabilidad y Cuentas por Pagar, Tesorería, Cuentas por Cobrar, Finanzas, Comercial Región Centro-Sur | 173 | 17 |
| Eje de RRHH | Claude Team | Base de datos de empleados, Nómina, Servicio Médico, Gestión Contable RRHH, Gestión de Gente, Beneficios y Recepción | 327 | 27 |
| Cerebros de los 12 directores | Claude Team | Cerebros de los directores | 72 | 1 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Fase 1 (prioridad de cada área, sin dependencias) | Fase 2 (necesita un acuerdo, un dato o una solución previa) | Fase 3 (extensiones, cruces y tableros) |
|---|---|---|---|
| Eje de Finanzas y Comercial | 72 h · 7 sol. | 49 h · 5 sol. | 40 h · 4 sol. |
| Eje de RRHH | 152 h · 12 sol. | 99 h · 8 sol. | 76 h · 7 sol. |
| Cerebros de los 12 directores | 0 h · 0 sol. | 0 h · 0 sol. | 72 h · 1 sol. |

- **Arranque**: Línea base de horas por proceso y mapeo de microprocesos de Finanzas (12 h).
- **Primeros accesos**: Primeros asientos y licencias activos.
- **Evidencia de capacitación**: Control de capacitación del personal de DUSA, con evidencia lista para la certificación.
- **Antes de la fase 2**: Sistemas y Nómina acuerdan el criterio de correlativo de la base de empleados.
- **Cierre**: Cierre de la construcción.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Contabilidad y Cuentas por Pagar · 3 soluciones · 35 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Pagos asignados con criterio, reportes limpios y cierres más rápidos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CP-1 | Asistente de asignación y aprobación de pagos | Asistente de asignación y aprobación de pagos: con el proveedor y el monto que asigna Tesorería, propone las facturas a pagar por antigüedad y vencimiento, con banda de tolerancia; el analista ajusta y aprueba | 7 | 4 | 3 | 14 | F1 |
| CP-2 | Depurador de reportes de JD Edwards | Depurador de reportes exportados de JD Edwards: quita columnas y filas vacías, espacios y dispersión; una plantilla por formato. Sirve también a Finanzas, Tesorería y Procura | 4 | 2 | 3 | 9 | F1 |
| CP-3 | Agente de estados financieros y cierre multimoneda | Agente de estados financieros pulido y estandarizado para todo el equipo y extendido al ciclo de cierre: 10 estados por ciclo, desviaciones contra plan, multimoneda | 6 | 3 | 3 | 12 | F2 |

### Tesorería · 2 soluciones · 22 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Solicitudes de pago ordenadas y tareas con seguimiento automático

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TS-1 | Clasificador de la bandeja de correo del tesorero | Clasificador de la bandeja del tesorero: reglas y carpetas de Outlook más un agente que separa las solicitudes de pago (nómina, procura, impuestos) y entrega un resumen diario con solicitante, área, monto y fecha | 7 | 4 | 3 | 14 | F1 |
| TS-2 | Asistente de seguimiento de tareas con recordatorios | Seguimiento de tareas del equipo y de las áreas que entregan insumos, sobre la herramienta de Microsoft que el tesorero ya usa, con recordatorios automáticos en lugar de WhatsApp | 4 | 2 | 2 | 8 | F1 |

### Cuentas por Cobrar · 1 solución · 15 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Descuentos conciliados y notas de crédito propuestas, sin cruzar a mano

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CC-1 | Cuadro de descuentos comerciales y propuesta de notas de crédito | Cuadro nacional de descuentos comerciales normalizado por marca y conciliado contra pedido, factura, línea e ítem, con la propuesta de notas de crédito. Es la solución puente hasta la fase 2 del autopago | 8 | 4 | 3 | 15 | F1 |

### Finanzas · 8 soluciones · 80 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Plan financiero consolidado, sin depender de más de 20 archivos encadenados

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FN-0 | Mapeo de microprocesos y entrega de datos por área | Mapeo de microprocesos con las cinco áreas proveedoras y contrato de datos por área: plantilla, fecha de entrega y responsable | - | - | - | 12 | F0 |
| FN-1 | Agente de premisas al comité | Agente de presentación de premisas al comité, sin dependencia de terceros | 3 | 2 | 2 | 7 | F1 |
| FN-2 | Validación del plan de ventas por producto | Plan de ventas (plan de licores) mensualizado por producto: validación y normalización del archivo del área proveedora | 4 | 3 | 2 | 9 | F2 |
| FN-3 | Costos de materiales y tablas de precios | Costos de materiales y precios: costos de reposición, cotizaciones y tablas de precios de JD Edwards | 5 | 3 | 2 | 10 | F2 |
| FN-4 | Plan administrativo | Plan administrativo | 3 | 2 | 2 | 7 | F2 |
| FN-5 | Costeo de manufactura por línea y cuadrilla | Costeo de manufactura: factores de alcohol, envejecimiento (2,7 años promedio) y envasado por línea y cuadrilla | 7 | 4 | 3 | 14 | F3 |
| FN-6 | Integración del plan de nómina | Integración del plan de nómina, construido por Nómina en NM-6, al modelo financiero | 3 | 2 | 2 | 7 | F3 |
| FN-7 | Consolidación: costo por producto, ingresos, gastos y balances | Consolidación: costo por producto terminado, ingresos y gastos (impuestos, descuentos, mercadeo al 3 %, regalías) y balances | 8 | 4 | 2 | 14 | F3 |

### Comercial Región Centro-Sur · 3 soluciones · 21 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Activaciones, descuentos y exhibición listos desde el teléfono

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CM-1 | Generador de creativos de activación y degustación | Generador de creativos extendido al ciclo completo de activación y degustación | 2 | 1 | 2 | 5 | F1 |
| CM-2 | Gestor de descuentos por cliente, desde el celular | Gestor de descuentos por cliente con la tasa del día, operable desde el teléfono | 6 | 3 | 2 | 11 | F2 |
| CM-3 | Diseñador de cabezal y exhibición en punto de venta | Diseñador de cabezal y exhibición en punto de venta; requiere el inventario de material POP digitalizado | 2 | 1 | 2 | 5 | F3 |

### Base de datos de empleados · 1 solución · 19 h · Claude Team · línea B · paso previo

Para qué (lo que ve el cliente): Una sola base por trabajador, con la cédula como llave

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| RH-0 | Archivo maestro por cédula, con diccionario y rutina mensual | Orden de la base de datos de empleados y su carga familiar, con la cédula como llave única para las 18 compañías: diccionario de datos y reglas de calidad; archivo maestro conciliado de las cinco fuentes, con duplicados, fichas repetidas, correlativos y estatus contradictorios señalados; casos dudosos validados con cada área; archivo listo para la carga masiva que defina Sistemas; rutina mensual de altas, bajas y nuevos ingresos | 10 | 6 | 3 | 19 | F1 |

### Nómina · 6 soluciones · 82 h · Claude Team · línea B

Para qué (lo que ve el cliente): Parafiscales, vacaciones y préstamos validados sin revisar a mano

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NM-1 | Solicitudes de pago de parafiscales y Humanitas | Solicitudes de pago parafiscales (Seguro Social, FAOV, INCES, sindicato y pensiones) para 10 a 15 empresas, y Seguro Humanitas con el mismo patrón. Se prueba dentro de una ventana real de cinco días hábiles | 9 | 5 | 3 | 17 | F1 |
| NM-2 | Validador de vacaciones | Validador de vacaciones sobre la exportación semanal del control de SPI, primer contacto del equipo con la IA | 5 | 3 | 2 | 10 | F1 |
| NM-3 | Notificaciones y archivo de pago | Notificaciones: resultado del retiro de fideicomiso a cada trabajador, y archivo de pago desde el reporte 337 con cuadro resumen y correos a Tesorería | 8 | 4 | 3 | 15 | F2 |
| NM-4 | Expediente mensual de parafiscales | Flujo completo de parafiscales con Registro y Tesorería: expediente mensual por empresa con solicitud, factura y soporte, listo para inspección | 7 | 3 | 3 | 13 | F2 |
| NM-5 | Validador de préstamos | Validador de préstamos: préstamo activo, disponibilidad del fondo y cierre semanal de la nómina diaria | 6 | 4 | 2 | 12 | F3 |
| NM-6 | Plan y presupuesto de nómina | Plan y presupuesto de nómina sobre la base de conocimiento laboral del líder (ley, convención, retroactividad); alimenta a Finanzas en FN-6 | 8 | 4 | 3 | 15 | F3 |

### Servicio Médico · 5 soluciones · 63 h · Claude Team · línea B

Para qué (lo que ve el cliente): Crónicos, órdenes y coberturas con seguimiento y validación previa

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SM-1 | Agentes de morbilidad y certificados de salud, trasladados a Claude | Adopción por el equipo de los agentes de morbilidad (con familiares) y certificados de salud, trasladados a Claude | 6 | 3 | 2 | 11 | F1 |
| SM-2 | Informe y pedido de tratamiento crónico | Tratamiento crónico: informe para Wilmer, pedido contra existencias con faltantes y archivo estructurado del pedido para el descuento masivo cuando Sistemas lo habilite | 8 | 4 | 3 | 15 | F1 |
| SM-3 | Trazabilidad de órdenes de referencia | Trazabilidad de órdenes de referencia: alerta a 30 días sin resultado, efectividad por proveedor y consultas de familiares | 6 | 4 | 2 | 12 | F2 |
| SM-4 | Prevalidación documental | Prevalidación documental: afiliación contra la contratación colectiva, completitud de expedientes HCM y facturas, e imputación de cada orden a su centro de costo | 8 | 4 | 2 | 14 | F2 |
| SM-5 | Coberturas y costo por beneficiario | Coberturas y costo consolidado por beneficiario (servicio médico y HCM), con alerta de cobertura disponible | 6 | 3 | 2 | 11 | F3 |

### Gestión Contable RRHH · 4 soluciones · 44 h · Claude Team · línea B

Para qué (lo que ve el cliente): Facturas de salud y gastos registrados y controlados por muestreo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| GC-1 | Registro de facturas de salud y cuadro Humanitas | Registro completo de facturas de salud: lectura de facturas en PDF, cuenta y centro de costo por regla, cuadro para Humanitas sin doble copia, alerta de diferencias contra la factura y relación mensual de consultas | 8 | 4 | 3 | 15 | F1 |
| GC-2 | Revisión por muestreo de gastos | Revisión por muestreo de gastos de representación y de vehículos, con conciliación de saldos; requiere acuerdo con Cuentas por Pagar | 5 | 3 | 2 | 10 | F2 |
| GC-3 | Distribución de la factura HCM | Distribución de la factura HCM por beneficiario, plan y centro de costo, sobre la base única | 5 | 3 | 2 | 10 | F3 |
| GC-4 | Tablero presupuestario | Tablero de ejecución presupuestaria de Recursos Humanos: indicadores, premisas y análisis de pólizas | 5 | 2 | 2 | 9 | F3 |

### Gestión de Gente · 7 soluciones · 87 h · Claude Team · línea B

Para qué (lo que ve el cliente): Ingreso, contratos y capacitación en un solo flujo, con alertas

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| GG-1 | Formulario único de ingreso | Formulario único de ingreso que llena los formatos de cada empresa, arma el expediente y entrega a Nómina los datos para SPI; requiere el nuevo formato con su código ISO | 7 | 4 | 3 | 14 | F1 |
| GG-2 | Contratos con alertas | Contratos desde la ficha y base de seguimiento con alertas: período de prueba, contratos, pasantes, becarios, cédula y pólizas del personal internacional | 7 | 4 | 2 | 13 | F2 |
| GG-3 | Filtrado de CV y orden de candidatos | Filtrado de CV por vacante, resumen frente al perfil, ranking y acuse; borrador de perfil de cargo cuando no existe | 6 | 3 | 3 | 12 | F1 |
| GG-4 | Ficha de entrevista y ejecutiva | Ficha de entrevista llenada desde la transcripción y ficha ejecutiva para el líder; con consentimiento del candidato | 5 | 3 | 2 | 10 | F1 |
| GG-5 | Control de capacitación y evidencia | Capacitación: convocados, asistencia, base, indicadores por área, certificados y repositorio, con evidencia lista para la certificación de enero | 8 | 4 | 3 | 15 | F1 |
| GG-6 | CV del talento interno | CV del talento interno, consultable por competencias para el plan de sucesión | 5 | 2 | 2 | 9 | F3 |
| GG-7 | Inducción y avisos de ingreso | Onboarding y comunicación del ingreso: plantilla y cronograma llenados, asistente de preguntas, video de bienvenida y avisos a cada involucrado | 7 | 3 | 4 | 14 | F2 |

### Beneficios y Recepción · 4 soluciones · 32 h · Claude Team · línea B

Para qué (lo que ve el cliente): Consumo telefónico, comunicados y beneficios sin cruzar a mano

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| BR-1 | Cruce del consumo telefónico | Consumo telefónico: cruce de la factura del operador con el Excel de números, por número, responsable y área | 4 | 3 | 2 | 9 | F1 |
| BR-2 | Asistente de correo y comunicados | Asistente de correo y comunicados: borradores, resúmenes y respuestas repetitivas con los parámetros de Comunicaciones | 2 | 1 | 2 | 5 | F1 |
| BR-3 | Pedido sugerido de obsequios de cumpleaños | Obsequios de cumpleaños: cajas y pedido sugerido a partir del reporte mensual del intranet | 4 | 2 | 2 | 8 | F2 |
| BR-4 | Lectura de constancias de útiles y becas | Útiles y becas: lectura de constancias (año, sello, nombre, cédula) y confirmación por cortes contra la base, lista antes de la campaña 2027 | 5 | 3 | 2 | 10 | F3 |

### Cerebros de los directores · 1 solución · 72 h · Claude Team · línea C

Para qué (lo que ve el cliente): Un Cerebro Digital para cada uno de los 12 directores, como cortesía.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CD-1 | Cerebros Digitales de los 12 directores (incluye: Un cerebro por director, con su contexto y su criterio; 6 h de trabajo guiado con cada director) | Referencia interna: 12 Cerebros Digitales, uno por director, de 6 h de trabajo guiado cada uno (72 h en total, la referencia de Intezia para un cerebro sin horas). Cortesía de Intezia, sin valor en la cotización; los asientos de Claude de los directores los paga DUSA. Cuáles son los 12 directores y cuándo trabaja cada uno se acuerda en el arranque. | - | - | - | 72 | F3 |

## 4. Fuera de alcance

- Lo que Sistemas de DUSA asume con sus propios desarrollos: autopago, Tesote, Bitácora, reporte de gasto e intranet.
- Todo proceso que requiera un aplicativo, como el portal de peticiones o el de proveedores.
- Todo Comercial Región Caracas, que Sistemas cubre con autopago, Bitácora y pago directo.
- La banca en línea, que la IA no opera, y las historias clínicas, que no entran a la plataforma.

## 5. Supuestos a confirmar (antes del método)

- Propuesta nueva (CAI-059, Ivana, 20/10/2026) con base en la CAI-035: mismas 11 áreas y 44 soluciones del informe de Detección (500 h), sin cambios de contenido. La CAI-035 queda como estaba (Enviada, 04/10/2026).
- **Presupuesto por área, en dos bloques aprobables (Ivana):** Eje de Finanzas y Comercial (Contabilidad y CxP, Tesorería, Cuentas por Cobrar, Finanzas, Comercial Centro-Sur) y Eje de RRHH (Base de empleados, Nómina, Servicio Médico, Gestión Contable RRHH, Gestión de Gente, Beneficios). Dos hojas de inversión (`inversion.etapas`), una por eje, que muestran las horas de cada área; cada hoja tiene su valor, descuento y total para que ventas los llene. No hay una caja de valor por cada una de las 11 áreas.
- **Cerebros de los 12 directores (Ivana):** 72 h (6 h por director, la referencia de Intezia; Ivana eligió esa opción). **Son cortesía de Intezia, sin valor en las hojas, y los asientos de Claude de los directores los paga DUSA.** Van como un solo entregable (12 cerebros) en una tercera línea de trabajo, en la fase 3 (mi decisión; la fuente no dice cuándo). Quiénes son los 12 directores y cuándo trabaja cada uno se acuerda en el arranque.
- **Vigencia:** el arranque del 19/10 ya no es posible (Ivana). El deck no lleva fechas (§4.23); el servicio arranca cuando DUSA confirme y la cotización vale 30 días desde el envío. La cotización anterior (CAI-035) tenía esa fecha en versiones previas.
- **Pago (propuesta mía, por confirmar):** Ivana pidió un plan de pago por eje. Se dejaron 2 cuotas por eje (la mitad al aprobar el eje y la otra al cerrarlo, la política de 50 % de anticipo) en vez de las 5 cuotas de la CAI-035 (30, 25, 25, 10 y 10 %). Los porcentajes de las tarjetas no se muestran (cada eje se paga por separado): quedan en 25 internos y los montos son campos vacíos para ventas.
- El licenciamiento va aparte y en las notas de cada hoja (con `inversion.etapas` no convive la tarjeta de licencias): Microsoft 365 Copilot USD 30 por usuario al mes (referencia del informe de Detección del 04/09/2026) y Claude Team USD 20 por asiento al mes con pago anual o USD 25 mensual (valor de lista del 02/10/2026, mínimo de 2 puestos). Los asientos de los 12 directores los paga DUSA.
- El certificado de participación INTEZIA es el institucional estándar (no figura en el insumo).
- Retorno en modo método y con posiciones: las fichas dicen «No declarado» en volumen y horas por ejecución. **El aval de posiciones** (Wilmer, de DUSA, según la dirección de Intezia, 05/10/2026, mensaje interno) **debe reconfirmarse por escrito con DUSA antes de enviar y antes de circular el documento entre líderes.**
- Calendario: la v3 no muestra semanas ni sesiones (se acuerdan en la reunión de arranque); el insumo hablaba de 11 semanas de construcción.
- Modalidad del trabajo: el insumo no dice si son presenciales o virtuales; confirmar con servicio. Asesora: María Iribarren, directora comercial (Ivana, 20/10/2026).
- Facilidad de pago en dos páginas (Ivana, 20/10/2026, sustituye las 4 cuotas de 25 % por eje): página 1, cada eje por separado en tres cuotas (30 % al aprobar, 40 % con las soluciones prioritarias del eje adoptadas, 30 % al cierre); página 2, los dos ejes juntos en las cinco cuotas de la CAI-035 (30, 25, 25, 10 y 10 %). Los hitos y porcentajes son los dados por Ivana; los montos no se escriben (campos vacíos para ventas; en el PDF PagoCuota1..6 y PagoCuota1_2..5_2). El texto «19 soluciones prioritarias adoptadas» es literal de la CAI-035 y no se calcula.
- Hojas de inversión en tres opciones (Ivana, 20/10/2026): opción 1 eje de Finanzas y Comercial, opción 2 eje de RRHH y opción 3 los dos ejes juntos, cada una con sus campos de valor, descuento y total vacíos (PrecioBase, PrecioBase_2, PrecioBase_3…). Las páginas de pago corresponden así: la 1.ª a las opciones 1 y 2, la 2.ª a la opción 3.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero la fase 1 (prioridad de cada área, sin dependencias); después la fase 2 (necesita un acuerdo, un dato o una solución previa); al final la fase 3 (extensiones, cruces y tableros).

- **Construimos**: Junto a quien ejecuta el proceso, con sus casos reales.
- **Probamos**: Con ese equipo y con el equipo de tecnología de DUSA.
- **Adoptamos**: El equipo la usa en su trabajo diario.
- **Medimos**: El retorno en tiempo y las oportunidades de optimización para la empresa.

- En la práctica, **Herramientas**: Recursos Humanos trabaja en Claude Team; las demás áreas, en Microsoft 365 Copilot y Power Automate, que DUSA ya opera.
- En la práctica, **Dónde corre cada cosa**: Lo repetitivo, como limpiar un reporte o enviar un aviso, va a Power Automate; Copilot queda para lo que exige leer y razonar.
- En la práctica, **Un asiento por persona**: En Claude Team cada persona trabaja en su propio asiento. Los asientos de los 12 directores los paga DUSA, y Sistemas revisa el uso cada mes.
- Datos: Los archivos que se suben quedan en la cuenta de DUSA, y Sistemas evalúa y autoriza cada acceso a un sistema, como el de SPI. Con los datos de Nómina se trabaja con el líder del área.
- Quién construye: Intezia construye con quien ejecuta cada proceso. Sistemas de DUSA gobierna los accesos, la seguridad y las licencias, y participa en las pruebas.

Casos reales mostrados (cada uno con su fuente; nunca se inventan casos de éxito):

- **Contabilidad y Cuentas por Pagar** · Agente de estados financieros (antes: 30 a 40 min; después: 3 a 4 min). Fuente: Informe Final de Auditoría IA de DUSA (04/09/2026).
- **Cuentas por Cobrar** · Validador de cobros. Fuente: Informe Final de Auditoría IA de DUSA (04/09/2026).
- **Comercial Región Centro-Sur** · Generador de creativos. Fuente: Informe Final de Auditoría IA de DUSA (04/09/2026).

**Logística:** modalidad: Trabajo del consultor con cada ejecutor, en su propia cuenta y con sus casos reales. · participantes: Quien ejecuta cada proceso en las 10 áreas, con su líder, y los 12 directores. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: La fecha la fija DUSA al confirmar la propuesta..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

**Posiciones y nómina (planteadas de frente).** Aval registrado: Wilmer (DUSA), según la dirección de Intezia · 2026-10-05 · mensaje de revisión interno. Confirmar que sigue vigente antes de enviar y antes de circular el documento entre líderes de área.

Pasos del método: Volumen mensual; Tiempo actual por ejecución; Tiempo con la solución; Horas recuperadas al mes; Valor en dinero; Posiciones y valor anual.

## 8. Facilidad de pago (slide 10)

| Cuota | Cuándo | Hito | %% |
|---|---|---|---|
| 1 | Al aprobar | Aprobar el eje | 30 |
| 2 | Fase 1 | Soluciones prioritarias del eje adoptadas (fase 1) | 40 |
| 3 | Cierre | Cierre del eje | 30 |
| 4 | Al aprobar | Aprobar el eje | 30 |
| 5 | Fase 1 | Soluciones prioritarias del eje adoptadas (fase 1) | 40 |
| 6 | Cierre | Cierre del eje | 30 |

Los montos van vacíos en el PDF (campos `PagoCuota1..6`): los escribe ventas y deben sumar el total de la slide de inversión. No se anotan en este repositorio.

## 9. Facilidad de pago, 2.ª página (slide 11)

| Cuota | Cuándo | Hito | %% |
|---|---|---|---|
| 1 | Arranque | Arranque | 30 |
| 2 | Fase 1 | 19 soluciones prioritarias adoptadas | 25 |
| 3 | Cierre fase 2 | Cierre de la fase 2 | 25 |
| 4 | Cierre | Cierre de la construcción | 10 |
| 5 | +30 días | 30 días después del cierre, con las soluciones ya en uso y dentro de la garantía 30-60-90 | 10 |

Los montos van vacíos en el PDF (campos `PagoCuota1_2..5_2`): los escribe ventas. No se anotan en este repositorio.

## 10. Próximos pasos (slide 12)

Asesora comercial que ve el cliente: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056.

