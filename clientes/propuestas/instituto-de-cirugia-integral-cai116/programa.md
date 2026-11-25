# Programa interno · Instituto de Cirugía Integral · Servicio de Habilidades (CAI-116)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (18/11/2026), resumen de la asesora y transcripción de la reunión del 18/11/2026.

## 1. Resumen

- **11 entregables en 3 áreas**, **40 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **IA para la clínica**: 11 entregables, 40 h.
- Horas por fase: F1 8 h (2 sol.) · F2 20 h (5 sol.) · F3 12 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Atención y administración | IA para la clínica | Levantamiento e introducción, Atención del paciente, Administración | 40 | 11 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Base (Levantamiento e introducción) | Paciente (Atención del paciente) | Cierre (Pagos, correos, material e indicadores) |
|---|---|---|---|
| Atención y administración | 8 h · 2 sol. | 20 h · 5 sol. | 12 h · 4 sol. |

- **Arranque**: Reunión para conocer al equipo y sus roles y fijar la línea base de tiempos.
- **Mapa de procesos**: Recorrido del paciente y administración mapeados, con prioridades acordadas.
- **Paciente en digital**: Del primer dato al postoperatorio, en un solo flujo.
- **Cierre**: Administración e indicadores; empieza la garantía.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Levantamiento e introducción · 2 entregables · 8 h · IA para la clínica · línea A

Para qué (lo que ve el cliente): Mapear dónde aplicar la IA y entender con criterio qué se puede lograr

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| LF-1 | Levantamiento y mapa de oportunidades | Levantamiento breve del recorrido del paciente y de la administración, con quien hace cada tarea, para mapear dónde aplicar la IA y qué se construye primero. | - | - | - | 5 | F1 |
| LF-2 | Introducción a la IA y datos del paciente | Introducción a la IA para todo el equipo, enfocada en eficiencia, y una regla de qué datos de pacientes se comparten con la IA y cuáles no. | - | - | - | 3 | F1 |

### Atención del paciente · 5 entregables · 20 h · IA para la clínica · línea A

Para qué (lo que ve el cliente): Que el paciente no pase datos a mano y reciba sus documentos a tiempo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AP-1 | Recepción y datos del paciente | Captura de los datos del paciente una sola vez, por una vía digital, para adelantar la ficha sin esperar al paciente en persona. | - | - | - | 4 | F2 |
| AP-2 | Agenda de citas y ficha médica | Flujo entre el pedido de cita, el sistema de citas y la ficha médica, sin repetir datos. Se investiga qué se puede conectar con el sistema de citas actual. | - | - | - | 4 | F2 |
| AP-3 | Propuesta quirúrgica y presupuesto | Propuesta y presupuesto armados y enviados en digital, en lugar de papel o correo suelto, con las alternativas de fecha. | - | - | - | 4 | F2 |
| AP-4 | Instructivo preoperatorio y laboratorios | Instructivo preoperatorio y lista de exámenes y laboratorios enviados al paciente según la intervención, con seguimiento de lo pendiente. | - | - | - | 4 | F2 |
| AP-5 | Postoperatorio según la intervención | Indicaciones postoperatorias personalizadas, enviadas según el tipo de intervención que se realizó. | - | - | - | 4 | F2 |

### Administración · 4 entregables · 12 h · IA para la clínica · línea A

Para qué (lo que ve el cliente): Pagos, correos y pedidos de material ordenados, con indicadores

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AD-1 | Pagos y confirmaciones | Registro y confirmación de los pagos y transferencias del paciente, con el cierre administrativo ordenado. | - | - | - | 4 | F3 |
| AD-2 | Correos separados por función | Un correo por tipo de gestión, con criterio, para saber quién envió y quién recibió cada cosa y no exponer un solo buzón. | - | - | - | 2 | F3 |
| AD-3 | Pedido de material quirúrgico | Pedido de material según el plan quirúrgico próximo y lo que falta en quirófano, con un método propio, hoy sin números. | - | - | - | 4 | F3 |
| AD-4 | Indicadores de pacientes y respuesta | Indicadores simples: pacientes que vinieron y los que se operaron, y tiempo de respuesta, para decidir con datos. | - | - | - | 2 | F3 |

## 4. Fuera de alcance

- Historias clínicas e imágenes de pacientes: no se cargan a la IA ni se mueven del sistema actual.
- Mercadeo y redes sociales: los lleva una empresa externa.
- Reemplazar el sistema de citas actual: se conecta lo que se pueda, no se cambia.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (23/11/2026): propuesta de Habilidades CAI-116 para el Instituto de Cirugía Integral (primer contacto, sin servicio previo de Intezia). Asesora: Verónica Rubio.
- Decisiones de Ivana: Educación y sin alianza; 40 h; impacto «operación»; sin nombrar herramienta de IA ni tarjeta de licencias.
- Reparto de las 40 h mío: levantamiento e introducción 8 h (5 + 3), atención del paciente 20 h (5 entregables de 4 h) y administración 12 h (4, 2, 4, 2).
- Insumos: Ficha del 18/11/2026, resumen de Verónica y transcripción de la reunión del 18/11/2026 (parte 2 truncada al final). Si se contradicen, manda la transcripción.
- El pequeño levantamiento de procesos y la introducción a la IA salen del pedido de Verónica a la clienta («un levantamiento pequeño que nos permite mapear bien los procesos» y «una primera capacitación básica»). Van como el primer bloque.
- Sin nombres de personas del cliente (ni de la administradora ni del cirujano) ni del software de citas ni de la empresa de mercadeo. El decisor conjunto aún no está en la conversación: los próximos pasos dicen «quienes toman la decisión».
- Sin nombrar herramienta de IA ni VPN (Verónica recomendó Claude, pero Venezuela no es país soportado). La preocupación por la seguridad de los datos se responde con el acuerdo de confidencialidad y una regla de qué datos se comparten con la IA.
- Sin fechas ni meses: la clienta prefiere arrancar en enero de 2027 y Verónica habló de 1 a 1,5 meses, pero el calendario se acuerda en el arranque (§4.23).
- Sin facilidad de pago (regla permanente); Verónica mencionó reservar con 30 % y cuotas ligadas a hitos, solo si Ivana lo pide.
- Retorno en modo método: la clienta no declaró tiempos ni volúmenes. Los ejemplos de Verónica (registro de 40 a 10 min) eran ilustrativos y no van como cifras del cliente.
- Inventario de material quirúrgico: Mabel contó que el pedido se hace según el plan quirúrgico y lo que falta, sin números formales; se plantea un método propio, no una promesa de predicción.
- Modalidad presencial en sus oficinas (ficha). Las historias clínicas y las imágenes de pacientes quedan fuera de alcance por confidencialidad.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero el levantamiento y la introducción, para que el equipo decida con criterio qué construir. Después el recorrido del paciente, el corazón del trabajo diario. Al final la administración, que se apoya en lo anterior.

- **Construimos**: Junto a quien hace cada tarea, con sus casos reales.
- **Probamos**: Con el equipo administrativo y de enfermería, antes de usarlo con pacientes.
- **Adoptamos**: El equipo lo usa en su trabajo diario.
- **Medimos**: El tiempo ahorrado por proceso y los pasos que ya no se hacen a mano.

- En la práctica, **Con el trabajo real de cada uno**: Cada flujo parte de una tarea de su día a día, no de ejercicios de aula.
- En la práctica, **Con los datos del paciente protegidos**: Antes de cargar datos de pacientes se acuerda qué se puede compartir con la IA y cómo protegerlo.
- En la práctica, **Sobre lo que ya usan**: Se parte de sus hojas de cálculo, su correo y su sistema de citas; lo que conviene cambiar se decide con el equipo.
- Datos: Los datos de los pacientes son confidenciales: se firma un acuerdo de confidencialidad y se trabaja solo con los datos que el Instituto autoriza.
- Quién construye: Intezia guía y construye junto al equipo, que aprende cómo se hace y cómo saber si el resultado es bueno.

**Logística:** modalidad: Presencial en sus oficinas, según se acuerde en la reunión de arranque. · participantes: Administración, enfermería e instrumentistas y, si lo desean, los doctores. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas del proceso; Tiempo actual por tarea; Tiempo con la solución; Horas recuperadas; Respuesta al paciente.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> El recorrido del paciente queda digitalizado, los documentos del antes y el después de la cirugía salen según la intervención y el equipo opera sin depender de una o dos personas.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

