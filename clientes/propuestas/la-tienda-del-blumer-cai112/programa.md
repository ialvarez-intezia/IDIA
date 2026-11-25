# Programa interno · La Tienda del Blúmer · Servicio de Habilidades (CAI-112)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Informe Final de Auditoría DET-020 (21/11/2026), Resumen Ejecutivo DET-020 y planteamiento del consultor para Habilidades (22/11/2026).

## 1. Resumen

- **33 entregables en 7 áreas**, **120 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **IA para la operación**: 33 entregables, 120 h.
- Horas por fase: F1 24 h (9 sol.) · F2 24 h (7 sol.) · F3 42 h (12 sol.) · F4 30 h (5 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Áreas de La Tienda del Blúmer | IA para la operación | Sistemas, Bodega y Compras, Recursos Humanos, Contabilidad, Tesorería, Auditoría Interna y Cashea, Auditoría Externa, Cerebros Digitales | 120 | 33 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Fase 1 (Sistemas) | Fase 2 (Bodega, Compras y RRHH) | Fase 3 (Contabilidad, Tesorería y las dos auditorías) | Fase 4 (Cerebros Digitales) |
|---|---|---|---|---|
| Áreas de La Tienda del Blúmer | 24 h · 9 sol. | 24 h · 7 sol. | 42 h · 12 sol. | 30 h · 5 sol. |

- **Arranque**: Accesos, participantes y orden de las áreas, según el informe de la Detección.
- **Sistemas con IA**: Conexión a SQL Server, SRH, Conetsoft y SPDV por MCP, el conector entre la IA y cada sistema.
- **Datos y nómina**: Reporte de inventario, importaciones y nómina validada.
- **Cierre de las áreas**: Contabilidad, Tesorería y las auditorías; empieza la garantía.
- **Cerebros Digitales**: Cinco asistentes con el conocimiento de los responsables clave.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Sistemas · 9 entregables · 24 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Ajustar sus sistemas con Claude Code y conectarlos por MCP, el enlace de la IA con cada sistema

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SI-1 | Mantenimiento ágil de sus sistemas y scripts con Claude Code | Claude Code, la herramienta de IA que programa junto al equipo, lee sus sistemas y scripts propios, propone los cambios y los documenta; Sistemas los revisa y los aplica. A cambio, el mantenimiento y los ajustes salen con menos esfuerzo y el conocimiento deja de concentrarse en una sola persona. | - | - | - | 3 | F1 |
| SI-2 | Tareas repetidas entre tiendas, automatizadas con scripts | Con Claude Code se construyen los scripts que reemplazan los cambios que hoy se repiten tienda por tienda. A cambio, Sistemas recupera tiempo para desarrollar, que hoy el soporte interrumpe. | - | - | - | 3 | F1 |
| SI-3 | Cambios probados antes de tocar las bases en uso | Claude Code prepara las pruebas y el control de cada cambio sobre las réplicas de datos, antes de llevarlo a las bases en uso. A cambio, Sistemas cambia con menos riesgo para la operación. | - | - | - | 2 | F1 |
| SI-4 | Conexión a SQL Server por MCP | Evaluar e implementar un conector MCP (la interfaz entre la IA y una herramienta) hacia las bases SQL Server locales de sus aplicaciones, sobre las réplicas que Sistemas está desarrollando, con el mapa de fuentes y accesos de cada sistema. | - | - | - | 3 | F1 |
| SI-5 | Prueba de conexión con SRH por MCP | Investigar y probar un conector MCP hacia el sistema de RRHH (SRH) para consultar los datos de nómina y de personal; si el sistema no lo permite, se usan exportaciones o los datos de SQL Server. | - | - | - | 3 | F1 |
| SI-6 | Pruebas de conexión: Conetsoft, SPDV, Infotex | Investigar y probar cómo conectar con IA el sistema contable (Conetsoft), el punto de venta (SPDV) y las consultas de Infotex, sin presuponer que compartan el mismo mecanismo; cada vía se decide con Sistemas. | - | - | - | 3 | F1 |
| SI-7 | Registro de solicitudes de soporte | Registro sistemático de las solicitudes de soporte, con métricas de carga, a partir de la bitácora y el cuestionario de soportes ya trabajados en la Detección. | - | - | - | 2 | F1 |
| SI-8 | Requerimientos breves de cada área | Definir brevemente lo que necesita cada área y contrastarlo entre áreas, para llegar a una solución compatible o a un punto medio útil para todas. | - | - | - | 2 | F1 |
| SI-9 | Solución centralizada con trazabilidad | Diseño conjunto de la solución que reúne la información que consultan y gestionan las áreas y la Dirección: un sistema de información centralizado, conectores para que la IA trabaje con él o con las aplicaciones actuales, o un agente autónomo para procesos concretos, con registro de cada consulta. | - | - | - | 3 | F1 |

### Bodega y Compras · 3 entregables · 12 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Saber qué se vendió contra lo que hay y seguir cada importación

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| BC-1 | Reporte de inventario contra ventas | Reporte periódico de inventario contra ventas por categoría y marca, con la mercancía en tránsito cuando exista la fuente. Puede avanzar desde las exportaciones disponibles. | - | - | - | 5 | F2 |
| BC-2 | Pedido, recepción y saldos de importación | Una base o aplicación que relaciona el pedido, la proforma, la recepción y los saldos de cada importación. | - | - | - | 4 | F2 |
| BC-3 | Reglas de reposición y reparto por tienda | Dejar escritas las reglas de reposición y reparto de cada tienda para que el reporte las aplique. Contar la mercancía sigue siendo del equipo. | - | - | - | 3 | F2 |

### Recursos Humanos · 4 entregables · 12 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Preparar y validar la nómina con datos completos y menos copias

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| RH-1 | Validación de nómina contra asistencia | Contraste del cálculo de nómina con el marcaje, las fotografías de asistencia y las novedades, con alertas de diferencias. El visto bueno sigue siendo de la persona responsable. | - | - | - | 4 | F2 |
| RH-2 | Reporte de RRHH con todos los datos | Reporte del sistema de RRHH completado con los datos que hoy faltan, para evitar consultas adicionales y copias sucesivas. | - | - | - | 3 | F2 |
| RH-3 | Formatos de pago de nómina y liquidaciones | Formatos de pago de nómina y de liquidaciones preparados desde un único cálculo, para no rehacerlos en cada copia. | - | - | - | 2 | F2 |
| RH-4 | Seguimiento de contratos y préstamos | Control de vencimientos y saldos de contratos y préstamos, hoy llevados a mano. | - | - | - | 3 | F2 |

### Contabilidad · 3 entregables · 12 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Registrar las ventas como asientos con los criterios del área

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CO-1 | Criterios de asiento por banco y tarjeta | Levantamiento de los criterios de asiento, bancos, tarjetas, comisiones y excepciones, con el equipo de Contabilidad y Sistemas. | - | - | - | 4 | F3 |
| CO-2 | Prueba: de la venta al asiento contable | Investigar si el sistema de punto de venta de cada tienda puede alimentar al sistema contable y registrar las ventas como asientos, y demostrarlo con casos completos antes de extenderlo. | - | - | - | 6 | F3 |
| CO-3 | Libro de ventas y conciliación, en uso | Consolidar las herramientas del libro de ventas y de la conciliación bancaria ya creadas en la Detección y dejarlas documentadas para el equipo. | - | - | - | 2 | F3 |

### Tesorería · 3 entregables · 10 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Guardar cada soporte una sola vez, ordenado, para que las áreas lo reutilicen

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TE-1 | Soportes digitales con archivo ordenado | Guardar los soportes digitales con impresora virtual y una regla común de ubicación, nombre, fecha e identificador, para no imprimir y volver a escanear. | - | - | - | 4 | F3 |
| TE-2 | Consolidación de las herramientas de Tesorería | Reunir y ordenar las herramientas de relación y recepción de comprobantes que Tesorería ya usa, para que trabajen con la misma información. | - | - | - | 3 | F3 |
| TE-3 | Medición de la cola de transferencias | Medir qué carga de nómina retira el servicio de pagos actual y cómo queda la cola de transferencias, para que la Dirección decida con datos. | - | - | - | 3 | F3 |

### Auditoría Interna y Cashea · 3 entregables · 10 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Revisar cada venta con un mismo criterio y conciliar los abonos de Cashea

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| IC-1 | Registro digital de la revisión de ventas | Consolidar el registro digital en marcha para que la revisión siga un mismo criterio entre tiendas, puntos de venta y soportes legibles. | - | - | - | 4 | F3 |
| IC-2 | Cruce de Cashea: órdenes y abonos | Cruce de las órdenes con los abonos de Cashea; los abonos sin número de orden o de cuentas de empresas distintas pasan a revisión de la persona responsable. | - | - | - | 4 | F3 |
| IC-3 | Soportes de Oriente en digital | Que los soportes de las tiendas de Oriente lleguen en digital en lugar de esperar el paquete de papel. | - | - | - | 2 | F3 |

### Auditoría Externa · 3 entregables · 10 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Que cada pago coincida con su aprobación, su comprobante y su banco

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| EX-1 | Conciliación de pagos con sus soportes | Contraste de la aprobación, el comprobante y el movimiento bancario de una misma operación y período. | - | - | - | 4 | F3 |
| EX-2 | Registro de dólares y bolívares | Registro de los pagos en divisas y en bolívares desde el mismo mensaje diario, sin repetirlo en relaciones distintas. | - | - | - | 3 | F3 |
| EX-3 | Planillas de Interna recibidas en digital | Que las planillas de Interna lleguen a Externa en digital apenas se revisan, para que no esperen un mes o más. | - | - | - | 3 | F3 |

### Cerebros Digitales · 5 entregables · 30 h · IA para la operación · línea A

Para qué (lo que ve el cliente): Un asistente con el conocimiento de cada responsable clave, para consultarlo y delegarlo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CE-1 | Cerebro del líder de Sistemas | Reúne en un grafo de conocimiento la bitácora, los recursos y el cuestionario de soportes ya trabajados en la Detección, con un asistente de IA que responde sobre ellos. | - | - | - | 6 | F4 |
| CE-2 | Cerebro de soporte y desarrollo | Reúne el conocimiento de soporte y desarrollo del área, hoy repartido entre pocas personas, con un asistente de IA para consultarlo. | - | - | - | 6 | F4 |
| CE-3 | Cerebro de Recursos Humanos | Reúne las reglas de revisión de nómina y el seguimiento de contratos y préstamos, con un asistente de IA que ayuda a validarlos. | - | - | - | 6 | F4 |
| CE-4 | Cerebro de Compras | Reúne las reglas de importación y sus variantes, con un asistente de IA que responde sobre cada caso. | - | - | - | 6 | F4 |
| CE-5 | Cerebro de Dirección | Reúne la información que reúnen las áreas, con un asistente de IA para consultarla y gestionarla. | - | - | - | 6 | F4 |

## 4. Fuera de alcance

- Cerebros Digitales para otras personas: se pueden sumar después, según impacto.
- Marketing, gestión de clientes y comercio electrónico: no tuvieron levantamiento propio.
- Reemplazar los sistemas actuales: se conectan y se extienden, no se cambian.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (22/11/2026): propuesta de Habilidades CAI-112 para La Tienda del Blúmer, que ya pasó por la Detección DET-020 (Informe Final y Resumen Ejecutivo del 21/11/2026), más el planteamiento del consultor que la atendió. Asesora: Verónica Rubio (datos tomados de sus propuestas anteriores). Sin Ficha nueva ni transcripción de la reunión de presentación del informe (Granola no tiene esa reunión en los últimos 30 días).
- Decisiones de Ivana (22/11/2026): Educación y sin alianza; alcance de Sistemas más los planes del informe final (Bodega y Compras, RRHH, Contabilidad, Tesorería y auditorías); impacto «operación»; sin nombrar herramienta de IA ni tarjeta de licencias. Primero pidió 60 h sin Cerebros Digitales; después pidió agregar los Cerebros Digitales, desglosados, con su importancia y cómo ayudan.
- Cerebros Digitales (pedido de Ivana, 22/11/2026): cinco, para los responsables que recomienda el informe final (líder de Sistemas, la otra persona de Sistemas, RRHH, Compras y la persona que impulsa el proyecto en la Dirección). Horas mías: 6 h por Cerebro (estándar de la empresa: grafo de conocimiento 3 h y asistente de IA 3 h), 30 h en total, que sumadas a las 60 h de Sistemas y las áreas dan 90 h. Ivana no dio horas para los Cerebros: confirmar. Fases: Sistemas y su segundo Cerebro en la fase 1; RRHH y Compras en la fase 2, junto a sus áreas; Dirección en la fase 3, cuando ya hay información reunida.
- Sin nombres de personas en los Cerebros (regla de no exponer nombres): se llaman por su función («líder de Sistemas», «soporte y desarrollo», «Recursos Humanos», «Compras» y «Dirección»). Dirección es una etiqueta mía para la persona que impulsa el proyecto (el informe no da su cargo): confirmar el nombre del Cerebro con Ivana o Verónica. El informe no describe el trabajo de la segunda persona de Sistemas: su Cerebro se adaptó a soporte y desarrollo, que es lo que el informe atribuye al área.
- Desglose: cada Cerebro tiene dos entregables de 3 h (grafo de conocimiento y asistente de IA) y, bajo cada uno, lo que incluye (sin horas propias). La importancia y cómo ayuda salen del informe final: conocimiento concentrado en una persona, soportes sin registro sistemático, revisión de nómina y seguimiento de contratos y préstamos con copias sucesivas, reglas de importación y variantes en Compras, y la Dirección que necesita consultar y gestionar la información reunida. El Cerebro del líder de Sistemas parte de la bitácora, los recursos y el cuestionario de soportes que ya se trabajaron en la Detección.
- Reparto de horas mío (Ivana pidió 60 h y yo las repartí): tres fases de 20 h. Fase 1 Sistemas 20 h (desarrollo con IA 7, conexión a las réplicas 6, requerimientos breves 3, solución centralizada 4). Fase 2 Bodega, Compras y RRHH 20 h (reporte de inventario 6, importaciones 4, nómina 4, reporte de RRHH 3, contratos y préstamos 3). Fase 3 Contabilidad, Tesorería y auditorías 20 h (criterios de asiento 4, prueba del punto de venta al asiento 6, soportes digitales 4, herramientas 3, Interna y Cashea 3). El orden de las fases sigue la hoja de ruta del informe (Sistemas primero; Bodega y RRHH en paralelo; Contabilidad y Tesorería al final).
- Los entregables salen del plan del consultor (desarrollo con IA sobre casos reales, conexión a las réplicas de las bases de datos, requerimientos breves de cada área, solución centralizada con registro, prueba de la venta al asiento contable) y del mapa de oportunidades y la hoja de ruta del informe (reporte de inventario contra ventas, base de importaciones, validación de nómina, soportes digitales). No se inventaron entregables fuera de esas dos fuentes.
- Sin nombrar herramienta (Ivana): no se menciona Claude ni Claude Code ni conectores MCP, aunque el plan del consultor los usa. Se dice «una herramienta de IA» (en el detalle de programa.md) y «conectores» entre la IA y las bases de datos. No se menciona VPN (Venezuela no es país soportado). Los entregables dicen «conexión de la IA a las réplicas de datos», sin sigla técnica.
- El consultor habla de réplicas de bases de datos «mirrors»: en el deck se dice «réplicas» (sin anglicismo). Las réplicas aún están en desarrollo por Sistemas; el deck no afirma que existan ni que estén al día en tiempo real: el entregable es evaluar e implementar la conexión.
- Prueba de la venta al asiento contable: el consultor la plantea como un caso cuya factibilidad se evalúa con Sistemas y Contabilidad. El entregable dice «Prueba» y el detalle «investigar si»: no se promete que el punto de venta alimente automáticamente a Conetsoft. No se nombra Conetsoft en el deck (§4.11).
- Sin nombres de personas del cliente (el informe nombra a líderes y analistas): el deck habla de «el equipo de Sistemas» y de cada área. Se nombran las áreas como las llama el informe, y «Interna y Cashea» (Cashea es parte de su operación).
- Sin casos ya logrados (`metodo.ejemplos`): los logros de la Detección (por ejemplo, cruce de 17 facturas con 17 órdenes de Cashea, 26 referencias cotejadas en Tesorería) son del propio cliente pero el informe los rotula como escenario y varios aún por contrastar; además el deck no lleva fuentes. Se pueden agregar si Ivana lo pide, con el Informe Final como fuente.
- Retorno en modo método: el informe estima ≈300 a 305 h/mes de capacidad liberable de la Detección, pero es un escenario no medido y no se carga como cifra del cliente en esta propuesta (las horas de Habilidades no son las de ese escenario). No se cita el informe como estudio.
- Hechos de la portada, del Informe Final: dos personas atienden Sistemas para áreas y tiendas; la misma información se reconstruye desde mensajes, papel y hojas distintas; los sistemas se usan por interfaz gráfica sin conexión para IA acreditada. No se cita la fuente en el deck (regla de fuentes en presentaciones).
- Modalidad «presencial en Valencia o en línea»: supuesto mío (la empresa está en Valencia según el informe); se confirma en el arranque.
- Seguimiento 30-60-90 incluido por ser estándar de Habilidades. Sin facilidad de pago (omitir: pago, regla permanente). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23). Las horas de la ruta y de la inversión son horas con el equipo; las internas viven en programa.md y brief.md.
- Fuera de alcance: marketing, gestión de clientes y comercio electrónico (el informe los deja como horizonte sin levantamiento) y Cerebros Digitales para otras personas (el informe dice que se pueden sumar después según impacto e interés).
- Ajuste del 23/11/2026 (Ivana): la fase 1 (Sistemas) debe decir qué procesos incluye, como las fases 2 y 3, y los Cerebros Digitales vuelven en una fase 4, sin protagonismo (una fila en el alcance, una columna en la ruta). Horas confirmadas por Ivana: +30 h (cinco Cerebros de 6 h, estándar de la empresa) sobre las 90 h de las áreas, total 120 h. Los cinco del informe de la Detección, por función y sin nombres: líder de Sistemas, soporte y desarrollo, Recursos Humanos, Compras y Dirección (esta última es etiqueta mía: confirmar el nombre).
- Ajuste del 23/11/2026 (Ivana), segunda parte: el área de Sistemas debe decir qué sistema se conecta por MCP, qué se mejora y qué proceso se mejora. Por eso se nombran en el deck los sistemas del cliente que da el Informe Final (SQL Server local, SRH, Conetsoft, SPDV e Infotex) y el conector MCP; sigue sin nombrarse Claude ni Claude Code, ni personas. Sistemas pasa de 4 a 7 entregables (24 h: 4, 4, 3, 4, 3, 3, 3; reparto mío): mejoras a sus sistemas y scripts, conexión a SQL Server, pruebas de conexión con SRH y con Conetsoft, SPDV e Infotex, registro de solicitudes de soporte (bitácora y cuestionario de la Detección) y los dos entregables previos de requerimientos y solución centralizada. Como el informe dice que la vía de acceso se determina con Sistemas y que no se presupone el mismo mecanismo, los entregables dicen «prueba» o «evaluar e implementar» y el detalle ofrece exportaciones como alternativa: no se promete que cada sistema se conecte por MCP.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero Sistemas, porque su capacidad y sus conexiones sirven a todas las áreas. Después Bodega, Compras y RRHH; luego Contabilidad, Tesorería y las auditorías, que dependen de los criterios previos. Al final, los Cerebros Digitales, con la información ya reunida.

- **Construimos**: Junto a quien ejecuta el proceso, con sus casos reales.
- **Probamos**: Con ese equipo y con el equipo de tecnología de La Tienda del Blúmer.
- **Adoptamos**: El equipo la usa en su trabajo diario.
- **Medimos**: El retorno en tiempo y las oportunidades de optimización para la empresa.

- En la práctica, **Con el trabajo real de cada uno**: Sistemas aprende con su propio trabajo y cada área construye sobre sus procesos, no con ejercicios de aula.
- En la práctica, **Sobre las réplicas de datos**: La IA se conecta a las réplicas que Sistemas desarrolla, no a las bases en uso, y cada consulta queda registrada.
- En la práctica, **Depende de cada sistema**: Lo que se conecta depende de cada sistema y de qué tan fácil sea integrarlo: se investiga y se prueba antes de fijar la solución.
- Datos: Los datos de nómina, bancos y clientes no se cargan a la IA sin la autorización de La Tienda del Blúmer: se trabaja con las réplicas y los ejemplos que Sistemas aprueba.
- Quién construye: Intezia guía y el equipo de Sistemas construye con IA, junto a quien conoce cada proceso de su área.

**Logística:** modalidad: Presencial en Valencia o en línea, según se acuerde en la reunión de arranque. · participantes: El equipo de Sistemas y, en cada fase, quienes conocen el proceso de cada área. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tesorería; Auditoría Interna y Cashea; Recursos Humanos; Contabilidad; Auditoría Externa; Bodega y Compras; Sistemas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> La información de las siete áreas queda reunida y conectada, y Sistemas desarrolla con IA las soluciones, con menos tareas repetidas y cambios probados.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

