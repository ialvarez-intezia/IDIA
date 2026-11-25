# Programa interno · Palmarini&Asociados · Servicio de Habilidades (CAI-114)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (18/11/2026) y transcripción de la reunión de Verónica Rubio con Palmarini&Asociados (18/11/2026).

## 1. Resumen

- **10 entregables en 4 áreas**, **80 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **IA para la operación de RRHH**: 10 entregables, 80 h.
- Horas por fase: F1 20 h (3 sol.) · F2 40 h (5 sol.) · F3 20 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Reclutamiento y banco de vacantes | IA para la operación de RRHH | Reclutamiento y banco de vacantes | 20 | 3 |
| Contratos y cobros | IA para la operación de RRHH | Contratos y firmas, Cobros a clientes nuevos | 40 | 5 |
| Seguimiento de asesoras | IA para la operación de RRHH | Seguimiento de asesoras | 20 | 2 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Banco (reclutamiento y banco de reclutados) | Alertas (contratos, firmas y cobros) | Reporte (seguimiento de asesoras) |
|---|---|---|---|
| Reclutamiento y banco de vacantes | 20 h · 3 sol. | 0 h · 0 sol. | 0 h · 0 sol. |
| Contratos y cobros | 0 h · 0 sol. | 40 h · 5 sol. | 0 h · 0 sol. |
| Seguimiento de asesoras | 0 h · 0 sol. | 0 h · 0 sol. | 20 h · 2 sol. |

- **Arranque**: Se eligen las cinco empresas del piloto y se confirman accesos y participantes.
- **Banco y agente**: El agente filtra CVs y el banco de reclutados está en uso.
- **Alertas en marcha**: Contratos, firmas y cobros con sus avisos, probados con las empresas del piloto.
- **Cierre**: Reporte de asesoras en uso; empieza la garantía.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Reclutamiento y banco de vacantes · 3 entregables · 20 h · IA para la operación de RRHH · línea A

Para qué (lo que ve el cliente): Filtrar CVs y no perder a los candidatos que ya se entrevistaron

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| RC-1 | Agente que filtra los CVs | Un agente de IA que revisa los CVs que llegan para cada vacante y deja solo los candidatos que cumplen lo que pide el cargo; la persona agenda y entrevista. | - | - | - | 8 | F1 |
| RC-2 | Banco de reclutados por cliente | Base de datos centralizada de los candidatos entrevistados, por cliente y por tipo de cargo (meseros, cajeros), con búsqueda y filtrado, que reemplaza el Excel y las carpetas. | - | - | - | 8 | F1 |
| RC-3 | Lista corta por vacante | Para cada vacante nueva, la lista de candidatos del banco que encajan, para llamarlos antes de buscar otros. | - | - | - | 4 | F1 |

### Contratos y firmas · 3 entregables · 20 h · IA para la operación de RRHH · línea B

Para qué (lo que ve el cliente): Que ningún vencimiento ni firma se olvide, turno por turno

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CT-1 | Base de contratos por empresa y turno | Una base de datos por empresa con cada contrato, su turno y su fecha de vencimiento, en lugar de revisar a mano cada archivo. | - | - | - | 8 | F2 |
| CT-2 | Alertas de vencimiento por correo | Aviso por correo cuando se acerca el vencimiento de un contrato, con el nombre de la persona y de la empresa. | - | - | - | 6 | F2 |
| CT-3 | Firmas pendientes por turno | Por empresa y por turno, quién firmó y quién falta, con un recordatorio de las firmas pendientes. | - | - | - | 6 | F2 |

### Cobros a clientes nuevos · 2 entregables · 20 h · IA para la operación de RRHH · línea B

Para qué (lo que ve el cliente): Que ningún cliente nuevo pase días sin facturarse

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CB-1 | Alerta de cobro a cliente nuevo | Cuando entra un cliente nuevo, un recordatorio para facturar sus honorarios, que llega a la dirección y al área administrativa. | - | - | - | 10 | F2 |
| CB-2 | Honorarios por cobrar, a la vista | Un listado de los honorarios facturados y pendientes de cobro por cliente, con aviso cuando pasan los días. | - | - | - | 10 | F2 |

### Seguimiento de asesoras · 2 entregables · 20 h · IA para la operación de RRHH · línea C

Para qué (lo que ve el cliente): Ver qué hace cada asesora en cada cliente y qué falta firmar

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SA-1 | Registro de la actividad por cliente | Cada asesora registra de forma sencilla a dónde va, qué hizo y qué documentos se firmaron en cada cliente. | - | - | - | 10 | F3 |
| SA-2 | Reporte centralizado por asesora | Un reporte para la dirección con lo que hizo cada asesora por cliente y por turno, y lo que falta. | - | - | - | 10 | F3 |

## 4. Fuera de alcance

- Las nóminas y los cálculos: se siguen haciendo como hoy; la IA no los reemplaza.
- Información de clientes con contrato de confidencialidad: solo entra lo que cada cliente autorice.
- Las demás empresas clientes: el piloto empieza con cinco y el resto se suma después.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (22/11/2026): propuesta de Habilidades CAI-114 para Palmarini&Asociados con Verónica Rubio como asesora, a partir de la Ficha (18/11/2026) y la transcripción de la reunión (25 min). Primer contacto con Intezia. La clienta rechazó una Detección («no quiero algo que me lleve mucho tiempo»): el deck no nombra la Detección.
- Decisiones de Ivana (22/11/2026): Educación y sin alianza; impacto «reenfoque»; se nombran solo sus plataformas (Excel, Profit, WhatsApp Business), sin marcas de IA ni licencias de IA. Horas: primero 60 h; luego Ivana pidió subirlas a 80 h y precisó que son 20 h por cada proceso (cuatro áreas).
- Reparto de horas: Ivana fijó 20 h por área (4 × 20 = 80 h). El reparto dentro de cada área es mío: Reclutamiento y banco 20 h (agente que filtra CVs 8, banco de reclutados por cliente 8, lista corta por vacante 4); Contratos y firmas 20 h (base de contratos 8, alertas por correo 6, firmas pendientes 6); Cobros a clientes nuevos 20 h (alerta de cobro 10, honorarios por cobrar 10); Seguimiento de asesoras 20 h (registro 10, reporte centralizado 10). Fases de 20, 40 y 20 h (contratos y cobros comparten la fase 2). Cobros tiene solo dos entregables, así que cada uno pesa 10 h: si Ivana prefiere más entregables en esa área, se agregan. Las versiones de 60 h y de 80 h con otro reparto quedaron en `_pdf-anteriores/`.
- Orden de las fases según lo que dijo la clienta: lo más importante ahora es el reclutamiento y, luego, las bases de datos («por lo menos la parte de reclutamiento este año, luego bases de datos, resto en enero»). Por eso reclutamiento va en la fase 1; contratos y cobros (que usan la base de datos) en la 2; el seguimiento de asesoras en la 3. El deck no dice este año ni enero (§4.23, sin fechas); la propuesta se puede dividir en dos partes en la reunión, como habló Verónica.
- Los entregables salen de los cinco resultados que pidió Ingrid: agente que filtre CVs, base de datos de reclutados por cliente con alertas, notificaciones de vencimiento de contratos, reporte centralizado de lo que hace cada asesora y alertas de cobros. «Lista corta por vacante», «firmas pendientes por turno» y «honorarios por cobrar» salen de lo que ella describió (candidatos del banco para una vacante, quién firmó y quién falta, cobrar honorarios a clientes nuevos).
- Verónica dijo que el agente le dejaría «30, 40, 50 opciones»: es un ejemplo de su charla, no un compromiso; el deck no lo cita. Tampoco cita el piloto como «cinco empresas» con nombres: se dice «cinco empresas clientes» sin nombrarlas (son clientes de la clienta y están bajo contratos de confidencialidad).
- Piloto con cinco empresas: lo propuso la clienta, que dijo que «con estas cinco empresas vamos a digitalizar primero, quizás la más sencilla». No se sabe cuáles; se eligen en el arranque (hito 1).
- No se menciona el WhatsApp como conexión prometida: Ingrid quiere conectar Claude con WhatsApp Business y no lo ha logrado. El deck dice que lo que se conecta (correo, WhatsApp Business, Profit) depende de cada plataforma y se verifica en el arranque. No se nombra Claude ni ninguna marca de IA ni VPN (Claude no está soportado en Venezuela).
- Sin nombres de personas ni de los clientes de la clienta (los de la ficha y la transcripción). Se llaman «las asesoras», «la gerente» y «la dirección». «Cobros»: el deck habla de recordar la facturación de honorarios a clientes nuevos; no promete cobranza.
- Fuera de alcance: nóminas y cálculos (la clienta dijo que los seguirá sacando en su cálculo tradicional), información bajo contrato de confidencialidad y las demás empresas clientes. La ficha menciona también el área Legal, que no tiene proceso propio en la ficha ni en la reunión; no se incluyó como área.
- Retorno en modo método: no hay horas, volúmenes ni dotación medidos. La frase de Ingrid «crecer sin sumar más personas a la nómina» no se usa: enfoque de reenfoque, sin posiciones ni nómina (no hay aval).
- Seguimiento 30-60-90 incluido por ser estándar de Habilidades. Sin facilidad de pago (regla permanente; además moneda y forma de pago siguen sin definirse en la ficha). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Modalidad presencial en las oficinas de Maracay (la matriz, según la ficha).

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero el reclutamiento y el banco de reclutados, que es lo más urgente. Después contratos y cobros, que usan la misma base. Al final el seguimiento de asesoras, que reúne lo anterior.

- **Construimos**: Junto a quien ejecuta el proceso, con sus casos reales.
- **Probamos**: Con ese equipo y con el equipo de tecnología de Palmarini&Asociados.
- **Adoptamos**: El equipo la usa en su trabajo diario.
- **Medimos**: El retorno en tiempo y las oportunidades de optimización para la empresa.

- En la práctica, **Con quien hace el trabajo**: Cada herramienta se construye con la asesora o la gerente que hace la tarea, para que la use desde el primer día.
- En la práctica, **Empezamos con cinco empresas**: El piloto se hace con cinco empresas clientes; con lo aprendido, el resto se suma después.
- En la práctica, **Depende de cada conexión**: Lo que se conecta (correo, WhatsApp Business, Profit) depende de lo que permita cada plataforma: se verifica en el arranque.
- Datos: Los datos de clientes con contrato de confidencialidad no se cargan a la IA sin su autorización: se trabaja con los ejemplos y accesos que cada cliente permita.
- Quién construye: Intezia guía y el equipo de Palmarini&Asociados construye con IA sus propias herramientas, sobre lo que ya usa.

**Logística:** modalidad: Presencial en las oficinas de Maracay, según se acuerde en la reunión de arranque. · participantes: Las asesoras y líderes de Maracay que hacen cada tarea. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas del área; Tiempo actual por tarea; Tiempo con la herramienta; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **reenfoque**. Las personas pasan a trabajo de más valor; no se habla de menos personas ni de nómina.

> El equipo deja de revisar a mano CVs, vencimientos y cobros y se concentra en atender clientes y decidir, con la información reunida y al día.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

