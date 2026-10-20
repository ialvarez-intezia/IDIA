# Programa interno · Go Pharma · Servicio de Detección y Habilidades (CAI-050)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Minuta de la reunión con Go Pharma e indicaciones de la asesora: charla de 2 h, levantamiento y construcción por área (Comercialización primero, con GoHighLevel) y clones digitales para los dos decisores.

## 1. Resumen

- **18 entregables en 6 bloques**, **64 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Claude y Google Workspace**: 18 entregables, 64 h.
- Horas por fase: F1 2 h (1 sol.) · F2 50 h (13 sol.) · F3 12 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Tres etapas | Claude y Google Workspace | Charla para todo el equipo, Comercialización, Operaciones y Atención al cliente, Administración y Finanzas, Clon digital 1, Clon digital 2 | 64 | 18 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Etapa 1 (charla de fundamentos para todo el equipo) | Etapa 2 (levantamiento y construcción en tres áreas) | Etapa 3 (un clon digital para cada decisor) |
|---|---|---|---|
| Tres etapas | 2 h · 1 sol. | 50 h · 13 sol. | 12 h · 4 sol. |

- **Charla**: Todo el equipo alineado y listo para los levantamientos.
- **Levantamientos**: El proceso real de cada área, con Comercialización primero.
- **Construcción en vivo**: Cada solución, construida con el equipo y documentada.
- **Clones digitales**: Un clon para cada decisor, conectado a su trabajo.
- **30 · 60 · 90 días**: Seguimiento de uso real y de tiempo recuperado.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Charla para todo el equipo · 1 entregable · 2 h · Claude y Google Workspace · línea A

Para qué (lo que ve el cliente): Alinear a todo el equipo en el uso de la IA y prepararlo para los levantamientos.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CHA-1 | Charla de fundamentos, mindset y concientización (incluye: Fundamentos de la IA y mentalidad para trabajar con ella; Tres niveles de automatización: autónoma, asistida y con supervisión; Ejercicio práctico con tareas del propio equipo) | Charla de 2 h para todo el equipo de Go Pharma, con un ejercicio práctico. Es la entrada del proyecto: alinea al equipo y lo prepara para los levantamientos por área. Go Pharma define la fecha y el lugar. Contenido propuesto desde la minuta (se afina con María): por qué el momento es distinto, los tres niveles de automatización (autónoma, asistida y con supervisión total) y qué se puede y qué no se debe automatizar. | - | - | - | 2 | F1 |

### Comercialización · 6 entregables · 24 h · Claude y Google Workspace · línea A

Para qué (lo que ve el cliente): Centralizar los leads, dar seguimiento y ordenar la entrada de las farmacias aliadas.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| COM-1 | Proceso comercial levantado, de lead a cierre | Detección de Comercialización (4 h): levantamiento del proceso real de la gerencia comercial y las vendedoras, con la participación de la gerencia general. Es la primera área en levantarse (la de mayor prioridad). Hoy los leads llegan por Instagram, WhatsApp y formularios sin centralizar y el seguimiento está en libretas y Excel enviado por correo. | - | - | - | 4 | F2 |
| COM-2 | GoHighLevel configurado con sus etapas | Acompañamiento en la configuración del CRM recomendado (GoHighLevel): entrada automática de los leads de todos los canales, etapas del pipeline, asignación a las vendedoras y condiciones de entrada (para que una reacción en Instagram no genere un lead falso). Kommo fue descartado por no haberse adoptado. La licencia de GoHighLevel no está en esta inversión. | - | - | - | 4 | F2 |
| COM-3 | Adopción del CRM en vivo con el equipo | Acompañamiento en la adopción en vivo: el equipo comercial trabaja sus leads reales en el CRM, con revisión de reuniones y toques por vendedora. La adopción es el punto crítico: la experiencia previa con Kommo no prosperó. | - | - | - | 4 | F2 |
| COM-4 | Seguimiento de oportunidades con Claude | Claude conectado al CRM propone recomendaciones de seguimiento y borradores de respuesta (nivel asistido: la IA propone y la persona aprueba). | - | - | - | 4 | F2 |
| COM-5 | Reportes automáticos de lunes y viernes | Reportes de reuniones, propuestas enviadas y métricas por vendedora, generados de forma automática desde el CRM los lunes y los viernes (skill programado de Claude). | - | - | - | 4 | F2 |
| COM-6 | Onboarding de farmacias aliadas en Claude y Drive | Flujo provisional de onboarding para las farmacias aliadas con Claude y Drive: historial, manuales y contactos asignados. El portal definitivo depende del sistema administrativo propio que Go Pharma desarrolla (unos 6 meses): no se invierte en una solución temporal que se descartaría. | - | - | - | 4 | F2 |

### Operaciones y Atención al cliente · 4 entregables · 14 h · Claude y Google Workspace · línea A

Para qué (lo que ve el cliente): Vigilar pedidos, farmacias y entregas sin tanto trabajo manual, con informes automáticos.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| OPE-1 | Procesos de operaciones levantados | Detección de Operaciones y Atención al cliente (4 h): hoy el equipo vigila pedidos, farmacias activas y entregas de forma manual, con el directorio de farmacias y motorizados en papel o Excel abierto y los informes diarios armados a mano. | - | - | - | 4 | F2 |
| OPE-2 | Informe diario de operación, automatizado | Informe diario generado de forma automática (hoy se arma a mano y se pasa por IA sin automatización real). | - | - | - | 4 | F2 |
| OPE-3 | Seguimiento de pedidos y entregas con alertas | Seguimiento de pedidos, farmacias activas y entregas, con alertas cuando algo se sale de lo esperado. No incluye la integración con el inventario de las farmacias (es desarrollo y va como oportunidad en el informe). | - | - | - | 4 | F2 |
| OPE-4 | Directorio de farmacias y motorizados centralizado | Directorio único de farmacias y motorizados, que hoy está en papel o en Excel abierto. | - | - | - | 2 | F2 |

### Administración y Finanzas · 3 entregables · 12 h · Claude y Google Workspace · línea A

Para qué (lo que ve el cliente): Conciliar y cobrar con menos trabajo manual, con una persona que aprueba cada paso.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ADM-1 | Procesos de administración levantados | Detección de Administración y Finanzas (4 h): conciliaciones bancarias y cobranzas hechas a mano (7 cuentas de correo y formatos copiados) y cobro mensual a las farmacias aliadas en los primeros 5 días del mes, sin flujo de recordatorios o incentivos. | - | - | - | 4 | F2 |
| ADM-2 | Conciliación bancaria asistida, con alertas | Conciliación mensual en nivel asistido (la IA propone y la persona aprueba), con alertas de variaciones inusuales. | - | - | - | 4 | F2 |
| ADM-3 | Recordatorios del cobro mensual a las farmacias | Flujo de recordatorios (y, si se define en el levantamiento, incentivos) para el cobro de los primeros 5 días de cada mes, en nivel autónomo para los recordatorios y asistido para lo financiero. | - | - | - | 4 | F2 |

### Clon digital 1 · 2 entregables · 6 h · Claude y Google Workspace · línea A

Para qué (lo que ve el cliente): Que el decisor consulte y automatice su trabajo con Claude, conectado a su información.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CL1-1 | Clon digital con sus procesos y clientes (incluye: Procesos, clientes y propuestas cargados y conectados; Claude conectado a Drive y a sus fuentes de información; Reglas de cotización y de respuesta definidas con el decisor) | Primer clon digital (6 h en total, tarifa de Cerebro Digital): Claude entrenado con los procesos, los clientes, las propuestas y las reglas de cotización del decisor, y conectado a su información en Drive. Sirve también para que el decisor vea el valor por sí mismo. | - | - | - | 3 | F3 |
| CL1-2 | Reuniones y primeras automatizaciones del clon (incluye: Minutas de reuniones conectadas al clon; Primeras tareas automáticas: reportes, borradores y seguimientos; La persona aprueba antes de que algo salga) | Las minutas de las reuniones se exportan al clon para dejar traza de cada cliente (se recomienda Granola; la minuta también mencionó Fathom). Primeras automatizaciones demostradas en la reunión: reporte de CRM de lunes y viernes, cotizaciones con reglas de cotización, borradores de correo y seguimiento de oportunidades sin entrar al CRM. Todo con aprobación humana antes de enviar. | - | - | - | 3 | F3 |

### Clon digital 2 · 2 entregables · 6 h · Claude y Google Workspace · línea A

Para qué (lo que ve el cliente): Que el decisor consulte y automatice su trabajo con Claude, conectado a su información.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CL2-1 | Clon digital con sus procesos y clientes | Segundo clon digital (6 h en total, tarifa de Cerebro Digital): misma estructura que el primero, con los procesos, los clientes y las propuestas propios del segundo decisor. | - | - | - | 3 | F3 |
| CL2-2 | Reuniones y primeras automatizaciones del clon | Misma estructura que el primer clon: minutas de reuniones conectadas y primeras tareas automáticas, con aprobación humana. Las automatizaciones se definen con el decisor. | - | - | - | 3 | F3 |

## 4. Fuera de alcance

- La integración con el sistema de inventario de las farmacias: es desarrollo y se deja como oportunidad en el informe.
- El portal definitivo de farmacias aliadas: depende del sistema administrativo propio en desarrollo; aquí va un flujo provisional.
- Las licencias de Claude y de GoHighLevel: no forman parte de esta inversión y se suman de forma progresiva, por perfil.

## 5. Supuestos a confirmar (antes del método)

- Fuentes: indicaciones de la asesora María Iribarren y minuta de la reunión con Go Pharma (13/10/2026). División Educación, servicio Habilidades en formato compacto, combo Detección + Habilidades en la Etapa 2 (`servicio_rotulo` y `meta_servicio: deteccion`, como CAI-032 y CAI-026), sin alianza, código CAI-050 por instrucción del usuario. La propuesta no lleva fechas (§4.23): la charla de la Etapa 1 se busca para el viernes 16/10/2026, pero eso va al kickoff, no al deck.
- Por etapas porque Go Pharma no pudo aprobar el monto global anterior por flujo de caja y Marco, quien aprueba el presupuesto, no estuvo en la reunión: cada etapa lleva su propia hoja de cotización (`inversion.etapas`: una hoja por etapa, con sus horas, sus áreas, su valor, su descuento y su total; Ivana, 13/10/2026, reemplazó el recuadro de valor por etapa en una sola hoja). El generador solo soportaba 2 hojas y se extendió a 3.
- Horas propuestas por el sistema con los lineamientos de `empresa/politicas-comerciales.md`, porque María no las dio: Etapa 1 = 2 h (charla). Etapa 2 = 4 h de levantamiento por área (Detección) más Habilidades de 8 a 12 h por área hasta 5 procesos: Comercialización 24 h (4 + 12 + 8 por el CRM GoHighLevel, configuración y adopción), Operaciones y Atención al cliente 14 h (4 + 10) y Administración y Finanzas 12 h (4 + 8), total 50 h. Etapa 3 = 6 h por Cerebro Digital × 2 = 12 h. Total 64 h y 18 entregables. María ajusta.
- Áreas de la Etapa 2 según la minuta: Comercialización (prioridad), Operaciones y Atención al cliente, y Administración y Finanzas. Quedan para una etapa posterior Tecnología, Recursos Humanos y Mercadeo, con una escucha aparte con Tecnología.
- Plataforma: Google Workspace como base (ya lo usan) y Claude donde se justifica; licencias progresivas por perfil. El riesgo de bloqueo de cuentas de Claude en Venezuela NO se menciona en el deck (indicación de Ivana, 13/10/2026: «eso no se dice»; antes se había escrito de frente por pedido de María). Interno: Anthropic no incluye a Venezuela entre los países y regiones soportados (anthropic.com/supported-countries, consultada el 13/10/2026), nunca se promete VPN y el respaldo, si hiciera falta, es Gemini en Workspace.
- Clones digitales: las áreas se llaman «Clon digital 1» y «Clon digital 2» porque no se exponen nombres de personas del cliente (como en CAI-039) y no se sabe el cargo de cada decisor. Contenido tomado de la minuta (procesos, clientes, propuestas, precios y reuniones) y de las indicaciones de María (conecta Claude con procesos, clientes, propuestas y reuniones). La minuta recomienda Granola para las reuniones (y menciona Fathom); no se nombra en el deck para no sumar otra herramienta. El rollout de la minuta (empezar con la directora comercial sola y luego un asiento compartido para las vendedoras) queda como parte de las licencias progresivas, no como entregable.
- Los tres niveles de automatización de la minuta (autónoma, asistida y con supervisión total) se usan en el contenido de la charla y en el método («la IA propone y una persona aprueba» en lo financiero). La mayoría de los procesos de Go Pharma caen en el nivel asistido.
- Retorno en modo método: la minuta no trae tiempos ni volúmenes (solo frecuencias: informe diario, cobro en los primeros 5 días del mes), así que no se calculan horas liberadas por mes. Con los tiempos del cliente se pasa a modo cifras, marcado como estimado y sin cifras externas (`retorno-captura.xlsx`).
- Sin hoja de facilidad de pago (omitir: pago): Ivana (13/10/2026) pidió quitarla («quitar la hoja de plan de pago»). Antes se incluía porque Carolina dijo que las condiciones de pago ayudan: 4 cuotas atadas a hitos de las etapas (30 % al aprobar, 25 % con Comercialización construida y el CRM en uso, 25 % con Operaciones y Administración construidas, 20 % con los dos clones digitales entregados), provisional. Las condiciones de pago las negocia ventas. En la slide «Cómo trabajamos» se retiró también el subtítulo («El equipo participa en cada construcción; en lo financiero, la IA propone y una persona aprueba»): metodo.sin_subtitulo: true.
- Contenido de la charla (fundamentos, tres niveles de automatización, ejercicio práctico) propuesto desde la minuta, sin temario de María. Las soluciones de cada área salen de los dolores de la minuta; sus nombres y horas se ajustan en cada levantamiento.
- Asesora: María Iribarren, con los datos de la CAI-045 y la CAI-049.

## 6. Cómo trabajamos (slide 3)

**Por qué en este orden:** Primero se alinea al equipo; después se levanta y se construye por área, con Comercialización primero por su impacto. Los clones digitales pueden arrancar en paralelo.

- **Levantamos**: El proceso real de cada área, con su equipo y la gerencia general.
- **Construimos**: En vivo con el equipo, la solución que ese proceso necesita.
- **Documentamos**: Todo queda por escrito, útil también para el personal nuevo.
- **Medimos**: Con la línea base del arranque, medimos el uso real y el tiempo recuperado.

- En la práctica, **Workspace como base**: Go Pharma ya usa Drive, Sheets, Meet y el correo: la información vive ahí, y Claude se suma donde se justifica.
- En la práctica, **Licencias progresivas**: Se empieza por los pocos perfiles que se definan y se amplía solo si el uso lo justifica, sin sumar licencias antes de tiempo.
- Datos: Solo se carga a la IA lo que Go Pharma decide compartir. La información queda en su Drive y lo construido, documentado.
- Quién construye: Intezia levanta y construye en vivo con el equipo de cada área; en la Etapa 2 participa la gerencia general.

**Logística:** modalidad: En vivo con el equipo; Go Pharma define el lugar de la charla. · participantes: Todo el equipo en la charla; en cada área, su equipo y, en la Etapa 2, la gerencia general. · ritmo: La Etapa 3 puede arrancar en paralelo a las otras. · arranque: La charla de la Etapa 1 abre el proyecto; Go Pharma elige cuándo y dónde..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Procesos elegidos; Tiempo actual; Tiempo con IA; Horas liberadas; Valor del tiempo.

## 8. Próximos pasos (slide 10)

Asesora comercial que ve el cliente: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056.

