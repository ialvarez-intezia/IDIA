# Programa interno · N58 Banco Digital · Servicio de Habilidades (CAI-037)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de N58 (01/10/2026) y documento de soberanía de datos para Tecnología (CAI-034).

## 1. Resumen

- **6 entregables en 3 módulos**, **12 h** de sesión, más seguimiento a 30, 60 y 90 días.
- Herramienta **Claude Code y Codex**: 6 entregables, 12 h.
- Horas por fase: F1 2 h (1 sol.) · F2 6 h (3 sol.) · F3 4 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Semanas | Horas | Soluciones |
|---|---|---|---|---|---|
| Equipo de TI | Claude Code y Codex | Fundamentals y uso seguro, Construcción, Implementación | 1 a 6 | 12 | 6 |

| Línea de trabajo | Bases (Semana 1) | Código (Semanas 2 a 4) | Norma (Semanas 5 y 6) |
|---|---|---|---|
| Equipo de TI | 2 h · 1 sol. | 6 h · 3 sol. | 4 h · 2 sol. |

- **Kick-off · aparte**: 1 h con TI para elegir el repositorio de práctica y acordar las reglas del banco.
- **Semana 1 · Fundamentals**: 2 h con el equipo: criterio y reglas de uso seguro de Claude Code y Codex.
- **Semanas 2 a 4 · Construcción**: 3 sesiones de 2 h: código, revisión y pruebas con IA sobre el repositorio de práctica.
- **Semanas 5 y 6 · Implementación**: 2 sesiones de 2 h: quedan las instrucciones del repositorio y el estándar del equipo.
- **30 · 60 · 90 días**: Seguimiento: uso, nuevas construcciones y tiempo recuperado contra la línea base.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Fundamentals y uso seguro · 1 entregable · 2 h · Claude Code y Codex · línea A

Para qué (lo que ve el cliente): Que el equipo de TI entienda cómo trabajan las herramientas y qué código y datos pueden usar

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TI-1 | Guía de uso seguro de Claude Code y Codex | Sesión grupal de 2 h con el equipo de TI. Cómo trabaja un asistente de código (contexto, permisos y revisión de lo que propone), qué hace Claude Code y qué hace Codex, y qué código y datos del banco pueden entrar a cada herramienta y cuáles no. La guía descargable resume esas reglas. Registra la línea base del tiempo que toma hoy revisar y probar código. | - | - | - | 2 | F1 |

### Construcción · 3 entregables · 6 h · Claude Code y Codex · línea A

Para qué (lo que ve el cliente): Construir con el equipo un flujo de código, revisión y pruebas asistido por IA

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TI-2 | Flujo para escribir y refactorizar con IA | Sesión práctica de 2 h con el equipo, sobre un repositorio de práctica acordado en el kick-off (sin código de producción ni datos de clientes). Se escribe y se refactoriza código con Claude Code y con Codex, y el equipo documenta el flujo que le funciona. | - | - | - | 2 | F2 |
| TI-3 | Lista y flujo de revisión de código con IA | Sesión práctica de 2 h para revisar cambios de código con apoyo de IA: qué se le pide al asistente, qué siempre lo revisa una persona y cómo se deja registro de la revisión. Entrega la lista de revisión y el flujo del equipo. | - | - | - | 2 | F2 |
| TI-4 | Pruebas automatizadas con IA, probadas en el repositorio de práctica | Sesión práctica de 2 h para generar, ejecutar y corregir pruebas automatizadas con ayuda de IA sobre el repositorio de práctica. Entrega las pruebas construidas y el criterio del equipo para aceptarlas. | - | - | - | 2 | F2 |

### Implementación · 2 entregables · 4 h · Claude Code y Codex · línea A

Para qué (lo que ve el cliente): Dejar las instrucciones del repositorio y un estándar de uso que el equipo adopte

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TI-5 | Instrucciones del repositorio para Claude Code y Codex | Sesión de 2 h para escribir con el equipo las instrucciones que cada herramienta lee del repositorio (CLAUDE.md para Claude Code y AGENTS.md para Codex): estructura del proyecto, convenciones, comandos de prueba y límites de lo que puede tocar. | - | - | - | 2 | F3 |
| TI-6 | Estándar de uso de IA del equipo de TI | Sesión de 2 h para cerrar el estándar del equipo: qué código y datos se pueden usar, permisos de cada herramienta, qué se revisa siempre antes de aceptar y cómo se registra el uso. Deja el documento listo para que TI lo adopte. | - | - | - | 2 | F3 |

## 4. Fuera de alcance

- Código de producción y datos de clientes: las sesiones usan material de práctica.
- La decisión de soberanía de datos del banco, que se trata aparte con Tecnología.
- Contratar las licencias de Claude Code y Codex.

## 5. Supuestos a confirmar (antes del método)

- Código CAI-037: el usuario pidió CAI-035, que ya es de DUSA (enviada el 04/10/2026), y CAI-036 es de Alfonzo Rivas; el usuario eligió CAI-037, el siguiente libre (06/10/2026).
- Guardia §4.21 punto 5: el usuario eligió el formato compacto. El programa se reexpresó como 6 entregables en 3 módulos (Fundamentals, Construcción, Implementación), con la misma estructura de CAI-034: 12 h de propuesta y kick-off de 1 h aparte.
- Enfoque elegido por el usuario: escribir y refactorizar código, revisión de código y pruebas, y gobierno y uso seguro. Los 6 entregables y sus nombres los propuso el sistema a partir de ese enfoque: confirmar con servicio. El usuario no dio más contexto del equipo de TI.
- Reparto de horas (propuesta del sistema): Fundamentals 2 h, Construcción 3 sesiones de 2 h y Implementación 2 sesiones de 2 h, una sesión por semana en 6 semanas. Es una proyección de Intezia: confirmar con servicio y con Tecnología.
- Las sesiones usan un repositorio de práctica, sin código de producción ni datos de clientes. Es una decisión de diseño por la restricción de soberanía de datos de N58 (circular de Sudeban del 29/12/2023, reportada por prensa y aún no confirmada contra la Gaceta Oficial); confirmar con Tecnología.
- Licenciamiento: no se afirma quién contrata ni qué plan. La propuesta no lleva precios de lista; el banco los confirma con cada proveedor. Si se quieren cifras, hay que verificarlas con fecha.
- La línea base del tiempo de revisar y probar código se levanta dentro de la sesión de Fundamentals (2 h): confirmar con servicio que cabe.
- Retorno en modo método: no hay volúmenes, tiempos ni costo hora del equipo de TI. «Hacia la semana N» es aritmética (semanas de ejecución + 13): confirmar con servicio.
- Sin certificado de participación por defecto (§4.21). Modalidad omitida: en CAI-034 Mercadeo pidió presencial, pero no se sabe para TI.
- Portada: los 3 datos describen el contenido del proyecto (horas de Fundamentals, Construcción e Implementación), no al cliente. No hay una Ficha de Levantamiento propia de Tecnología, así que no se afirma nada sobre cómo usa hoy la IA el equipo de TI. Primera versión: «cada uno paga su herramienta» y «regulado por Sudeban» salían de la ficha de Mercadeo de CAI-034; el usuario los retiró (06/10/2026) porque no se saben para TI.
- Migración a la plantilla v2 (2026-10-08, instrucción del usuario: «ajustar las CAI-034 y CAI-037 al nuevo formato, cada una por separado»). Versión 1 a 2 según la spec §13. Contenido de fondo sin cambios: 12 h, 6 entregables en 3 módulos, 6 semanas, kick-off de 1 h aparte, seguimiento 30-60-90. Lo que se agregó por la v2: «Cómo trabajamos» (método, práctica, datos y logística), el para qué de cada módulo y la slide de próximos pasos con la asesora. Los 4 pasos pasaron de «Alcance» a «Cómo trabajamos». «Costo» pasó a «valor».
- Fases con nombre corto por límite de la v2 (cabecera de ≤ ~7 caracteres con «N entregables» al lado): «Bases», «Código» y «Norma» (antes Fundamentals, Construcción e Implementación). Los módulos de la slide 2 siguen con sus nombres.
- Modalidad: la v2 exige una ficha de logística y no se sabe la modalidad para TI (en CAI-034 Mercadeo pidió presencial): dice «a acordar con Tecnología». Participantes: «el equipo de TI», sin cifra, hasta confirmarla con Flavia.
- Sin facilidad de pago: no se preguntó. El usuario la omitió en las últimas propuestas migradas, así que se aplicó el mismo criterio con omitir: ["pago"]. Si Ventas la quiere, se agrega con cuotas ligadas a los hitos de la ruta.
- Asesora (slide de próximos pasos): Flavia Martínez, la misma de CAI-034, con su teléfono y correo del brief; el cargo «Asesora comercial» es supuesto. El deck de 6 slides no mostraba contacto: ahora la última slide sí lo hace.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se nivela al equipo y se fijan las reglas de uso seguro; después se construye el flujo de código, revisión y pruebas; al final queda el estándar.

- **Nivelamos**: Al equipo en Claude Code, Codex y su uso seguro.
- **Practicamos**: Con ambas herramientas, sobre un repositorio de práctica.
- **Construimos**: El flujo del equipo para el código, la revisión y las pruebas.
- **Dejamos listo**: El estándar del equipo y la medición a 30, 60 y 90 días.

- En la práctica, **Repositorio de práctica**: Todas las sesiones usan un repositorio acordado en el kick-off, sin código de producción.
- En la práctica, **Dos herramientas**: Se trabaja con Claude Code y con Codex sobre las mismas tareas, para ver qué hace cada una.
- En la práctica, **Una persona revisa**: Todo cambio que propone la IA lo revisa una persona antes de aceptarlo.
- Datos: Las sesiones usan material de práctica, sin código de producción ni datos de clientes. Qué código y datos puede usar cada herramienta lo fija el estándar del equipo.
- Quién construye: Intezia dicta las sesiones y construye cada flujo con el equipo de TI, sobre un repositorio de práctica.

**Logística:** modalidad: A acordar con Tecnología; la fecha y el horario, con el equipo de TI. · participantes: El equipo de TI de N58; cuántas personas participan se acuerda con Tecnología. · arranque: El kick-off de 1 h, aparte, elige el repositorio de práctica y acuerda las reglas del banco..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.
Hacia la semana 19: construcción (6 semanas) más 90 días de seguimiento; aritmética a confirmar con servicio.

Pasos del método: Volumen semanal; Tiempo actual por tarea; Tiempo con la IA; Horas recuperadas a la semana; Valor en dinero.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

