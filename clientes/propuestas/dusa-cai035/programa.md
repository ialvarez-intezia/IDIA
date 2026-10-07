# Programa interno · DUSA · Servicio de Habilidades (CAI-035)

> Documento interno (no se muestra al cliente). Fuente única: `DUSA_Habilidades_Procesos_Ruta_y_Horas_6.docx` (versión vigente desde 2026-10-04; reemplaza a `DUSA_Habilidades_Procesos_Ruta_y_Horas.docx`; Intezia C.A., Dirección de Productos y Servicios, 02/10/2026, Keiber Quintana). Las tablas se extrajeron programáticamente del docx y se validaron: 44 soluciones, 500 h.

## 1. Resumen

- **44 soluciones en 10 áreas**: 17 en el carril Microsoft Copilot (173 h) y 27 en el carril Claude Team (327 h). 500 horas de sesión, más seguimiento a 30, 60 y 90 días.
- Cada solución se reparte en **C**onstrucción, **T**esteo (en el deck: «pruebas») y **A**dopción. Las horas son de sesión, sin habilitación ni seguimiento.
- Fases: F0 (semana 1, 12 h) · F1 prioridad declarada sin dependencias (19 soluciones, 224 h) · F2 requiere un acuerdo, un dato o una solución previa (13 soluciones, 148 h) · F3 extensiones, cruces y tableros (11 soluciones, 116 h).
- Quién construye: Intezia construye junto a quien ejecuta cada proceso. Sistemas de DUSA gobierna accesos, seguridad y licencias, y participa en el testeo.

## 2. Frentes y ruta (relativa al arranque: la versión _6 del insumo ya no fija fechas calendario)

Desde el arranque del servicio, la construcción toma 11 semanas de trabajo y el seguimiento corre hasta 90 días después del cierre. Tres frentes trabajan en paralelo. S = semana de trabajo desde el arranque.

| Frente | Carril | Alcance | Horas | Semanas | h/semana | h/día |
|---|---|---|---|---|---|---|
| A | Claude Team | Base de datos de empleados, Nómina, Servicio Médico, Gestión Contable RRHH | 208 | S1-S11 (11) | 18,9 | 3,8 |
| B | Claude Team | Gestión de Gente, Beneficios y Recepción | 119 | S2-S7 (6) | 19,8 | 4,0 |
| C | Copilot | Contabilidad y CxP, Tesorería, Cuentas por Cobrar, Finanzas, Comercial Centro-Sur | 173 | S1-S10 (10) | 17,3 | 3,5 |

(La tabla «Resumen de horas» del insumo _6 solo trae Alcance y Horas; las semanas y h/semana salen de la imagen de la ruta.)

| Frente | F0 | F1 | F2 | F3 |
|---|---|---|---|---|
| A (208 h) | Claude Team configurado, línea base | 87 h (S1-S5) | 64 h (S5-S8) | 57 h (S8-S11) |
| B (119 h) | Línea base | 65 h (S2-S5) | 35 h (S5-S6) | 19 h (S7) |
| C (173 h) | 12 h (S1, FN-0), licencias, línea base | 72 h (S2-S5) | 49 h (S5-S8) | 40 h (S8-S10) |

- Fases: F0 semana 1 (12 h) · F1 semanas 1-5 (224 h) · F2 semanas 5-8 (148 h) · F3 semanas 7-11 (116 h). Seguimiento a 30, 60 y 90 días «desde el cierre de cada área».
- Hitos: asientos y licencias activos (S1-S2) · evidencia de capacitación lista (S4) · correlativo acordado antes de la fase 2 · cierre de construcción (S11).
- Tope de 20 h de sesión por semana por frente (4 h por día); la carga indicada es el promedio. NM-1 se prueba dentro de una ventana parafiscal real de cinco días hábiles. Las fases se traslapan: cada frente entra a la siguiente cuando su ejecutor ya opera lo anterior.
- La línea base no es opcional: sin ella el seguimiento a 60 y 90 días no tiene contra qué comparar.

## 3. Soluciones y horas (C = construcción, T = testeo, A = adopción)

### Contabilidad y Cuentas por Pagar · 3 soluciones · 35 h · Copilot · Frente C

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| CP-1 | Asistente de asignación y aprobación de pagos: con el proveedor y el monto que asigna Tesorería, propone las facturas a pagar por antigüedad y vencimiento, con banda de tolerancia; el analista ajusta y aprueba | 7 | 4 | 3 | 14 | F1 |
| CP-2 | Depurador de reportes exportados de JD Edwards: quita columnas y filas vacías, espacios y dispersión; una plantilla por formato. Sirve también a Finanzas, Tesorería y Procura | 4 | 2 | 3 | 9 | F1 |
| CP-3 | Agente de estados financieros pulido y estandarizado para todo el equipo y extendido al ciclo de cierre: 10 estados por ciclo, desviaciones contra plan, multimoneda | 6 | 3 | 3 | 12 | F2 |

### Tesorería · 2 soluciones · 22 h · Copilot · Frente C

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| TS-1 | Clasificador de la bandeja del tesorero: reglas y carpetas de Outlook más un agente que separa las solicitudes de pago (nómina, procura, impuestos) y entrega un resumen diario con solicitante, área, monto y fecha | 7 | 4 | 3 | 14 | F1 |
| TS-2 | Seguimiento de tareas del equipo y de las áreas que entregan insumos, sobre la herramienta de Microsoft que el tesorero ya usa, con recordatorios automáticos en lugar de WhatsApp | 4 | 2 | 2 | 8 | F1 |

### Cuentas por Cobrar · 1 soluciones · 15 h · Copilot · Frente C

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| CC-1 | Cuadro nacional de descuentos comerciales normalizado por marca y conciliado contra pedido, factura, línea e ítem, con la propuesta de notas de crédito. Es la solución puente hasta la fase 2 del autopago | 8 | 4 | 3 | 15 | F1 |

### Finanzas · 8 soluciones · 80 h · Copilot · Frente C

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| FN-0 | Mapeo de microprocesos con las cinco áreas proveedoras y contrato de datos por área: plantilla, fecha de entrega y responsable | — | — | — | 12 | F0 |
| FN-1 | Agente de presentación de premisas al comité, sin dependencia de terceros | 3 | 2 | 2 | 7 | F1 |
| FN-2 | Plan de ventas (plan de licores) mensualizado por producto: validación y normalización del archivo del área proveedora | 4 | 3 | 2 | 9 | F2 |
| FN-3 | Costos de materiales y precios: costos de reposición, cotizaciones y tablas de precios de JD Edwards | 5 | 3 | 2 | 10 | F2 |
| FN-4 | Plan administrativo | 3 | 2 | 2 | 7 | F2 |
| FN-5 | Costeo de manufactura: factores de alcohol, envejecimiento (2,7 años promedio) y envasado por línea y cuadrilla | 7 | 4 | 3 | 14 | F3 |
| FN-6 | Integración del plan de nómina, construido por Nómina en NM-6, al modelo financiero | 3 | 2 | 2 | 7 | F3 |
| FN-7 | Consolidación: costo por producto terminado, ingresos y gastos (impuestos, descuentos, mercadeo al 3 %, regalías) y balances | 8 | 4 | 2 | 14 | F3 |

### Comercial Región Centro-Sur · 3 soluciones · 21 h · Copilot · Frente C

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| CM-1 | Generador de creativos extendido al ciclo completo de activación y degustación | 2 | 1 | 2 | 5 | F1 |
| CM-2 | Gestor de descuentos por cliente con la tasa del día, operable desde el teléfono | 6 | 3 | 2 | 11 | F2 |
| CM-3 | Diseñador de cabezal y exhibición en punto de venta; requiere el inventario de material POP digitalizado | 2 | 1 | 2 | 5 | F3 |

### Base de datos de empleados (proceso base de Recursos Humanos) · 1 soluciones · 19 h · Claude Team · Frente A

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| RH-0 | Orden de la base de datos de empleados y su carga familiar, con la cédula como llave única para las 18 compañías: diccionario de datos y reglas de calidad; archivo maestro conciliado de las cinco fuentes, con duplicados, fichas repetidas, correlativos y estatus contradictorios señalados; casos dudosos validados con cada área; archivo listo para la carga masiva que defina Sistemas; rutina mensual de altas, bajas y nuevos ingresos | 10 | 6 | 3 | 19 | F1 |

### Nómina · 6 soluciones · 82 h · Claude Team · Frente A

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| NM-1 | Solicitudes de pago parafiscales (Seguro Social, FAOV, INCES, sindicato y pensiones) para 10 a 15 empresas, y Seguro Humanitas con el mismo patrón. Se prueba dentro de una ventana real de cinco días hábiles | 9 | 5 | 3 | 17 | F1 |
| NM-2 | Validador de vacaciones sobre la exportación semanal del control de SPI, primer contacto del equipo con la IA | 5 | 3 | 2 | 10 | F1 |
| NM-3 | Notificaciones: resultado del retiro de fideicomiso a cada trabajador, y archivo de pago desde el reporte 337 con cuadro resumen y correos a Tesorería | 8 | 4 | 3 | 15 | F2 |
| NM-4 | Flujo completo de parafiscales con Registro y Tesorería: expediente mensual por empresa con solicitud, factura y soporte, listo para inspección | 7 | 3 | 3 | 13 | F2 |
| NM-5 | Validador de préstamos: préstamo activo, disponibilidad del fondo y cierre semanal de la nómina diaria | 6 | 4 | 2 | 12 | F3 |
| NM-6 | Plan y presupuesto de nómina sobre la base de conocimiento laboral del líder (ley, convención, retroactividad); alimenta a Finanzas en FN-6 | 8 | 4 | 3 | 15 | F3 |

### Servicio Médico · 5 soluciones · 63 h · Claude Team · Frente A

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| SM-1 | Adopción por el equipo de los agentes de morbilidad (con familiares) y certificados de salud, trasladados a Claude | 6 | 3 | 2 | 11 | F1 |
| SM-2 | Tratamiento crónico: informe para Wilmer, pedido contra existencias con faltantes y archivo estructurado del pedido para el descuento masivo cuando Sistemas lo habilite | 8 | 4 | 3 | 15 | F1 |
| SM-3 | Trazabilidad de órdenes de referencia: alerta a 30 días sin resultado, efectividad por proveedor y consultas de familiares | 6 | 4 | 2 | 12 | F2 |
| SM-4 | Prevalidación documental: afiliación contra la contratación colectiva, completitud de expedientes HCM y facturas, e imputación de cada orden a su centro de costo | 8 | 4 | 2 | 14 | F2 |
| SM-5 | Coberturas y costo consolidado por beneficiario (servicio médico y HCM), con alerta de cobertura disponible | 6 | 3 | 2 | 11 | F3 |

### Gestión Contable RRHH · 4 soluciones · 44 h · Claude Team · Frente A

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| GC-1 | Registro completo de facturas de salud: lectura de facturas en PDF, cuenta y centro de costo por regla, cuadro para Humanitas sin doble copia, alerta de diferencias contra la factura y relación mensual de consultas | 8 | 4 | 3 | 15 | F1 |
| GC-2 | Revisión por muestreo de gastos de representación y de vehículos, con conciliación de saldos; requiere acuerdo con Cuentas por Pagar | 5 | 3 | 2 | 10 | F2 |
| GC-3 | Distribución de la factura HCM por beneficiario, plan y centro de costo, sobre la base única | 5 | 3 | 2 | 10 | F3 |
| GC-4 | Tablero de ejecución presupuestaria de Recursos Humanos: indicadores, premisas y análisis de pólizas | 5 | 2 | 2 | 9 | F3 |

### Gestión de Gente · 7 soluciones · 87 h · Claude Team · Frente B

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| GG-1 | Formulario único de ingreso que llena los formatos de cada empresa, arma el expediente y entrega a Nómina los datos para SPI; requiere el nuevo formato con su código ISO | 7 | 4 | 3 | 14 | F1 |
| GG-3 | Filtrado de CV por vacante, resumen frente al perfil, ranking y acuse; borrador de perfil de cargo cuando no existe | 6 | 3 | 3 | 12 | F1 |
| GG-4 | Ficha de entrevista llenada desde la transcripción y ficha ejecutiva para el líder; con consentimiento del candidato | 5 | 3 | 2 | 10 | F1 |
| GG-5 | Capacitación: convocados, asistencia, base, indicadores por área, certificados y repositorio, con evidencia lista para la certificación de enero | 8 | 4 | 3 | 15 | F1 |
| GG-2 | Contratos desde la ficha y base de seguimiento con alertas: período de prueba, contratos, pasantes, becarios, cédula y pólizas del personal internacional | 7 | 4 | 2 | 13 | F2 |
| GG-7 | Onboarding y comunicación del ingreso: plantilla y cronograma llenados, asistente de preguntas, video de bienvenida y avisos a cada involucrado | 7 | 3 | 4 | 14 | F2 |
| GG-6 | CV del talento interno, consultable por competencias para el plan de sucesión | 5 | 2 | 2 | 9 | F3 |

### Beneficios y Recepción · 4 soluciones · 32 h · Claude Team · Frente B

| ID | Solución y entregable | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|
| BR-1 | Consumo telefónico: cruce de la factura del operador con el Excel de números, por número, responsable y área | 4 | 3 | 2 | 9 | F1 |
| BR-2 | Asistente de correo y comunicados: borradores, resúmenes y respuestas repetitivas con los parámetros de Comunicaciones | 2 | 1 | 2 | 5 | F1 |
| BR-3 | Obsequios de cumpleaños: cajas y pedido sugerido a partir del reporte mensual del intranet | 4 | 2 | 2 | 8 | F2 |
| BR-4 | Útiles y becas: lectura de constancias (año, sello, nombre, cédula) y confirmación por cortes contra la base, lista antes de la campaña 2027 | 5 | 3 | 2 | 10 | F3 |

## 4. Lo que asume Sistemas de DUSA (fuera del alcance de Intezia)

Eje financiero y comercial (11 frentes): lectura de facturas y preregistro en JD Edwards, validación fiscal y preregistro de proveedor (app de reporte de gasto), validación de movimientos bancarios y disponibilidad (Tesote), flujo de caja (herramienta de tesorería), sinceración de cartera, imputación de pagos y descuento financiero (autopago y Bitácora), descuentos comerciales del pedido al cobro (fase 2 del autopago, sin fecha; Intezia cubre el intervalo con CC-1), cobranza y falso estatus de mora (Comercial Centro-Sur), todos los dolores de Comercial Región Caracas.
Recursos Humanos (9 frentes que requieren aplicativo): portal único de peticiones, inventario de licores y uniformes, autogestión de carga familiar, plataforma de la base única y carga masiva, adjuntos en afiliación y despacho crónico, circuito digital de solicitud y movimiento de personal, altas de usuario, portal de carga de facturas del proveedor, recibos y constancias del trabajador.
Fuera de todo alcance: el montaje y la descarga en la banca en línea (la IA no opera la banca). Las historias clínicas no entran a la plataforma.

## 5. Licenciamiento

- **Claude Team** (RR. HH.): se licencia igual que Microsoft 365 Copilot, **una licencia Standard por área, cinco en total**. Precio de lista USD 20 por asiento Standard al mes con pago anual (USD 25 mensual), consultado el 02/10/2026. Arranca con 2 asientos (USD 40/mes, el mínimo del plan) y suma uno por área cuando arranca su construcción: S1 → 2 (USD 40), S2 → 3 (USD 60), S4 → 4 (USD 80), S4 → 5 (USD 100). Regla de crecimiento: si un asiento toca su límite semanal dos semanas seguidas en un proceso de F1 o F2, se suma un asiento Standard o esa persona pasa a Premium (USD 100/mes). Control: revisión mensual del panel de uso con Sistemas; créditos de uso extra desactivados. Un asiento, una persona.
- **Microsoft 365 Copilot** (demás áreas): DUSA eligió una licencia por área, con un superusuario que comparte los agentes; el uso de agentes por personas sin licencia se cobra por consumo, así que se mide desde el primer mes. USD 30 por usuario al mes con compromiso anual (informe del 04/09/2026). Fase 1: 5 licencias (Tesorería eleva su licencia actual al plan que habilita agentes); fases 2 y 3: hasta 4 más (una por área proveedora de Finanzas). Lo determinístico corre en Power Automate (incluido en Microsoft 365); el paquete de capacidad de Copilot Studio solo entra si una automatización desatendida lo exige.
- La «condición de contratación» (política de regiones de Anthropic) que traía la versión anterior del insumo **fue eliminada** en la versión _6.

## 6. Respaldo oral de evidencia externa (NO está en el deck)

El 2026-10-05 se pidió que la slide de retorno (hoy la 7) no cite estudios ni nada de la web; esta sección queda solo como respaldo interno para ventas, por si la directiva pregunta qué dice la literatura. Documento interno de respaldo para ventas. Verificado con fuentes primarias el 2026-10-05 (workflow multiagente, 7 estudios). Regla: las cifras de la slide son de estudios ajenos, rotuladas como tales; **DUSA no tiene hoy horas por proceso, tarifa ni nómina en el sistema**, así que no hay cifra propia. El retorno de DUSA se mide con la línea base de la semana 1 en el seguimiento 30-60-90.

### 6.1 Versión anterior de la slide (3 barras, escala 0 a 50%, cada una con su base; retirada)

| Barra | Cifra | Qué mide exactamente | Fuente completa (la slide muestra una versión abreviada: sin número de documento, DOI ni NBER) | Límites |
|---|---|---|---|---|
| 1 | -5% | Horas de trabajo que **declaran ahorrar** quienes usan IA generativa (autorreporte, EE. UU., ola de noviembre de 2024). 5,4% = 2,2 h por semana en una jornada de 40 h (versión de feb. 2025); 5,2% en la revisión de oct. 2025 | The Rapid Adoption of Generative AI · Federal Reserve Bank of St. Louis (Working Paper 2024-027) · 2025 | Base: tiempo de quienes usan IA, no de toda la plantilla (sobre todos los trabajadores el mismo estudio da 1,4%). Documento de trabajo sin revisión por pares. Encuesta en línea con panel comercial |
| 2 | +15% | **Casos resueltos por hora** (producción, no tiempo liberado) por agente de soporte por chat, 5.172 agentes de una empresa Fortune 500 de software, herramienta de sugerencias basada en GPT-3 | Generative AI at Work · MIT Sloan, Stanford y NBER (The Quarterly Journal of Economics) · 2025 (https://doi.org/10.1093/qje/qjae044) | Una empresa, una ocupación. Efecto mínimo en el personal más experimentado (hasta ~30% en el menos calificado). La versión previa NBER 31161 (2023) decía 14% y 34%: **no mezclar versiones**. No mide empleo; los autores señalan que una empresa podría incluso contratar más |
| 3 | -40% | **Tiempo por tarea** de redacción profesional de 20 a 30 minutos, con ChatGPT, 453 profesionales (calidad +18%) | Experimental evidence on the productivity effects of generative artificial intelligence · MIT (Noy y Zhang), Science · 2023 | Experimento en línea, tareas cortas y sin conocimiento del negocio (puede inflar el efecto), enero-febrero de 2023. El documento de trabajo previo decía 37%. Verificado en el resumen oficial (science.org devolvió 403) |

La escala común solo fija la longitud de las barras: **no se suman ni se convierten** (producción por hora no equivale a tiempo liberado).

### 6.2 Verificados y NO usados en la slide (respaldo oral, con límites)

| Estudio | Cifras verificadas | Por qué no va en la slide / cómo usarlo |
|---|---|---|
| Dell'Acqua et al., Navigating the Jagged Technological Frontier (HBS WP 24-013, con Boston Consulting Group, 2023) | 758 consultores: 12,2% más tareas, 25,1% más rápido (≈25% menos tiempo), calidad +40%; en una tarea **fuera** de la frontera, 19 puntos porcentuales **menos** de respuestas correctas | Título de 139 caracteres que no cabe sin truncar; experimento de laboratorio de 90 minutos. Útil para decir que la IA no sirve para todo y por eso se construye proceso por proceso con pruebas |
| Microsoft Work Trend Index 2023, What Can Copilot's Earliest Users Teach Us About Generative AI at Work? | 29% más rápidos en 3 tareas simuladas (147 personas); 14 min al día ahorrados (autorreporte, 297 adoptantes tempranos); de quienes ahorran más de 30 min al día, 53% lo dedica a trabajo de foco | **Estudio del proveedor** (conflicto de interés), laboratorio y encuestas de percepción. No citar como evidencia independiente |
| McKinsey Global Institute, The economic potential of generative AI (2023) | Potencial: marketing 5% a 15% del gasto de la función, ventas 3% a 5%; 60% a 70% del tiempo de trabajo con actividades automatizables con tecnología de 2023 | Base de **gasto por función**, potencial técnico teórico, no resultado medido; sin cifras para Finanzas ni Recursos Humanos |
| Humlum y Vestergaard, Large Language Models, Small Labor Market Effects (BFI WP 2025-56 / NBER 33777, 2025) | Ahorro de tiempo declarado ~2,8% de las horas; 80% a 85% de los usuarios reasigna el tiempo ahorrado a otras tareas del trabajo (menos de 10% a descanso u ocio); sin efectos detectables en empleo total, ingresos ni horas registradas hasta 2024; 8,4% de los trabajadores con nuevas tareas | Tres versiones con cifras distintas; Dinamarca, 11 ocupaciones administrativas y profesionales (sin planta, sin Venezuela). **Útil como respuesta a «¿esto implica sacar gente?»**: en ese estudio el tiempo ahorrado se reasigna a otras tareas y no se detectó efecto en empleo. No es una promesa para DUSA |

### 6.3 Qué NO afirmar con esta slide

- Que DUSA ahorrará un porcentaje o un número de horas concreto, ni dólares, ni un plazo de recuperación en meses (no hay línea base, nómina, tarifa ni monto de inversión).
- Que «sin sumar plazas» es un resultado: es una **proyección** (ningún estudio citado mide empleo).
- Que la garantía 30-60-90 asegura el retorno: es garantía de acompañamiento.
- Que las tres barras son comparables o aditivas.
- «Hacia la semana 24» (en la slide: «cerca de 6 meses del arranque») = construcción cerrada en la S11 + 90 días de seguimiento (~13 semanas) desde el cierre del último frente: 24 semanas son ~5,5 meses. **Confirmar con servicio antes de reenviar**; si no se sostiene, cambiar por «unos 90 días después del cierre del último frente».
- «Un 5% declarado son unas 2 horas por semana»: aritmética del propio estudio sobre una jornada de 40 h (2,2 h en la versión de feb. 2025; 2,1 h en la de oct. 2025). Sobre **todos** los trabajadores el mismo estudio da 1,4% de las horas.

## 7. Ejemplos ya construidos con los equipos de DUSA (slide 2) y plan de pago (slide 6)

Interno. Fuentes de lo que muestra el deck, para que ventas lo respalde de palabra.

**Ejemplos (Informe Final de Auditoría IA, 04/09/2026, sección «Logros inmediatos construidos durante las sesiones de fundamentos y auditoría»; también en el deck «Cierre de Detección» presentado al Comité Ejecutivo de DUSA):**
- Contabilidad y Cuentas por Pagar, agente de estructuración de estados financieros: montar un estado a mano toma de 2 a 3 h y analizarlo de 30 a 40 min; con 10 estados por ciclo. Con el estado ya estructurado, el análisis se resolvió en 3 a 4 min respetando el formato del área. (El deck de cierre resume «de 2 a 3 horas a 3 a 4 minutos»; el informe distingue armar y analizar: la slide sigue al informe.)
- Cuentas por Cobrar, validador del consolidado de cobros contra la base de datos corporativa (SQL Server): la líder estimó que procesar la data a mano requeriría alrededor de 8 personas con conocimiento avanzado; el informe dice que el agente cierra esa brecha sin ampliar la estructura.
- Comercial Región Centro-Sur, generador de creativos para puntos de activación: antes no existía por falta de tiempo, herramientas y formación en diseño.
- Límite que NO se debe afirmar: el informe aclara que ninguno de esos usos está todavía convertido en proceso (no hay automatización en producción). Por eso la slide dice «construyeron» y «punto de partida del proyecto», no «en producción».

**Posiciones de la portada (≈10):** Informe Final, «Contra qué se compara esta inversión»: 5 a 6 en Cuentas por Cobrar, 3 de brecha en Tesorería, 1 posición a tiempo completo más media en Contabilidad y Cuentas por Pagar, 1 de diseño en Comercial; Finanzas es riesgo de continuidad, no dotación adicional. El informe no tiene las escalas salariales de DUSA.

**Plan de pago (cuadro enviado el 2026-10-06):**

| Cuota | Hito | % |
|---|---|---|
| 1 | Arranque (semana 1) | 30 |
| 2 | 19 soluciones prioritarias adoptadas (semana 5) | 25 |
| 3 | Cierre de la fase 2 (semana 8) | 25 |
| 4 | Cierre de la construcción (semana 11) | 10 |
| 5 | 30 días después del cierre, con las soluciones ya en uso y dentro de la garantía 30-60-90 | 10 |

Los montos van vacíos en el deck (campos `PagoCuota1..5`) y los llena ventas; los hitos coinciden con la ruta de la slide 3 (fases 1 a 3 y semana 11) y con el valor inmediato de la slide 4 (semana 5: 19 soluciones prioritarias adoptadas).
