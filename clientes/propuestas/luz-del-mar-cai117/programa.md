# Programa interno · Luz del Mar · Servicio de Habilidades (CAI-117)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (20/11/2026), resumen de la asesora y transcripción de la reunión del 20/11/2026.

## 1. Resumen

- **14 entregables en 4 áreas**, **80 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Agentes de IA**: 14 entregables, 80 h.
- Horas por fase: F1 20 h (3 sol.) · F2 20 h (4 sol.) · F3 40 h (7 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Tres agentes conectados | Agentes de IA | Valoración, Tráfico, Cotización, Conexión y traspaso | 80 | 14 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Base (Valoración y gacetas) | Estatus (Tráfico y rastreo) | Cierre (Cotización y conexión) |
|---|---|---|---|
| Tres agentes conectados | 20 h · 3 sol. | 20 h · 4 sol. | 40 h · 7 sol. |

- **Arranque**: Reunión para conocer al equipo, ver el recorrido de una carga y fijar la línea base de tiempos.
- **Valoración**: El agente calcula la pre-valoración de una carga real.
- **Estatus**: El estatus de una carga sale armado, con lo que falta.
- **Cierre**: Los tres agentes conectados; empieza la garantía.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Valoración · 3 entregables · 20 h · Agentes de IA · línea A

Para qué (lo que ve el cliente): Calcular los impuestos de cada carga con la base propia, sin esperar al valorador externo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| VA-1 | Base de gacetas y reglas | Ordenar las gacetas de arancel y el historial de cargas anteriores que la agencia ya tiene archivados, con las reglas de valoración, para que el agente los consulte y se actualicen con cada gaceta nueva. | - | - | - | 6 | F1 |
| VA-2 | Agente de cálculo de impuestos | Agente que recibe el documento de la carga, consulta las gacetas y las referencias de importaciones anteriores y genera la pre-valoración; la persona de Valoración la revisa. | - | - | - | 8 | F1 |
| VA-3 | Pruebas del equipo con cargas reales | El equipo de Valoración prueba el agente con cargas reales de la agencia, comparadas con valoraciones ya hechas, y Intezia ajusta hasta que confíe en el resultado. | - | - | - | 6 | F1 |

### Tráfico · 4 entregables · 20 h · Agentes de IA · línea A

Para qué (lo que ve el cliente): Saber dónde está cada carga y qué falta, sin perseguir información portal por portal

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TR-1 | Lectura del correo y de la carga | Agente que revisa el correo de entrada, identifica la carga y lo que falta de cada cliente. | - | - | - | 5 | F2 |
| TR-2 | Rastreo en las 10 navieras | Consulta automática del estado de cada carga en el portal de cada naviera con su número de guía. Depende de cómo permita consultar cada portal; se prueba con cada una. | - | - | - | 9 | F2 |
| TR-3 | Estatus consolidado para enviar | Estatus armado con el rastreo, lo que falta y la valoración recibida, listo para que la persona de Tráfico lo revise y lo envíe al cliente. | - | - | - | 4 | F2 |
| TR-4 | Cartas y documentos de cada carga | Las cartas y solicitudes que cada carga necesita, generadas de una vez cuando llega. | - | - | - | 2 | F2 |

### Cotización · 3 entregables · 20 h · Agentes de IA · línea A

Para qué (lo que ve el cliente): Cotizar cada carga a partir de su valoración, con lo que se pagó antes

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CO-1 | Historial de pagos y permisos | Ordenar el historial de lo que se pagó en cargas anteriores y los permisos con su valor, hoy en hojas de cálculo, para que el agente lo consulte. | - | - | - | 6 | F3 |
| CO-2 | Agente de cotización | Agente que, a partir de la valoración del agente anterior, arma la cotización para el cliente; la persona la revisa. | - | - | - | 9 | F3 |
| CO-3 | Cotización revisada para el cliente | Formato de cotización de la agencia y revisión de la persona antes de enviarla. | - | - | - | 5 | F3 |

### Conexión y traspaso · 4 entregables · 20 h · Agentes de IA · línea A

Para qué (lo que ve el cliente): Que los tres agentes funcionen como un solo flujo y el equipo sepa usarlos y probarlos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CX-1 | Tres agentes en un solo flujo | Conexión de los tres agentes: la valoración alimenta el estatus y la cotización, sin pasar datos a mano. | - | - | - | 8 | F3 |
| CX-2 | Alertas y revisión de fallas | Avisos cuando un agente falla o le falta información, para que el equipo sepa cuándo revisar y a quién reportarlo. | - | - | - | 4 | F3 |
| CX-3 | Guía de uso de cada agente | Guía de qué hace cada agente, cuándo revisar su resultado y cómo avisar de una falla. | - | - | - | 4 | F3 |
| CX-4 | Capacitación de uso de los agentes | Capacitación breve para que el equipo use y pruebe los agentes: qué hace cada uno, cuándo revisar y cómo reportar lo que falla. | - | - | - | 4 | F3 |

## 4. Fuera de alcance

- Cerebro Digital de la dueña: propuesta aparte.
- Página web con usuario y clave para que cada cliente vea su estatus: queda para una etapa posterior.
- Crear un software o un sistema administrativo propio: se construyen agentes, no un sistema.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (23/11/2026): propuesta de Habilidades CAI-117 para Luz del Mar (agencia de aduanas en Puerto Cabello, primer contacto). Asesora: Verónica Rubio.
- Decisiones de Ivana: 80 h, impacto «operación», sin nombrar herramienta de IA ni licencias, sin facilidad de pago. División Educación y sin alianza: supuesto mío, no se preguntó (confirmar).
- Reparto de las 80 h mío: 20 h por agente (Valoración 6, 8 y 6; Tráfico 5, 9, 4 y 2; Cotización 6, 9 y 5) y 20 h de conexión y traspaso (8, 4, 4 y 4).
- Orden de las fases por dependencia (no el de la ficha): Valoración primero porque su cálculo alimenta a Tráfico y a Cotización; la conexión de los tres cierra.
- Sin nombres de personas del cliente, del valorador externo ni de empresas de mensajería. Se dice «el valorador externo», «las 10 navieras» y «la dueña».
- Sin nombrar herramienta ni plataforma de flujos (la dueña pidió n8n, Make o Zapier; Verónica habló de Claude, n8n y Gemini). Sin VPN: Venezuela no es país soportado.
- El rastreo en las 10 navieras depende de cómo permita consultar cada portal: el deck lo dice y lo prueba con cada una; no promete que todas sean automatizables.
- La meta «liberar 90 % del trabajo manual» es declarada por la dueña, no medida: el deck la rotula como meta. El 70 % de información repetida de cada carga y el 90 % manual también son declarados por ella.
- Retorno en modo método: la ficha no trae tiempos ni volúmenes ni lo que cobra el valorador externo por documento. Si llegan, pasar a cifras con su origen.
- Fuera de alcance: Cerebro Digital de la dueña (propuesta aparte, Verónica ofreció enviarla), página web de estatus con usuario y clave (la dueña lo mencionó como deseo) y crear un software propio.
- La dueña pidió ver las formas de pago y el pago inicial; se omitió la facilidad de pago por decisión de Ivana y se comentará aparte (Verónica mencionó 30 % inicial y 2 o 3 cuotas). Sin fechas ni meses (§4.23).
- Un solo valorador externo y eventual: la persona de Valoración interna revisa su cálculo. El agente reemplaza la pre-valoración del externo, no la revisión humana.
- Ajuste del 23/11/2026 (Ivana): Intezia construye los agentes y la agencia los prueba y adopta; el equipo no participa en la construcción ni queda a cargo de mantenerlos (los ajustes los cubre la garantía 30-60-90). Se reescribieron la portada, el alcance, el método, el retorno, los entregables y los próximos pasos; «Pruebas con cargas reales» pasa a «Pruebas del equipo», «Guía de mantenimiento» a «Guía de uso» e «Introducción a los agentes» a «Capacitación de uso». Las horas no cambian (80 h).

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero Valoración, porque su cálculo alimenta a los otros dos. Después Tráfico, que usa esa valoración en el estatus. Al final Cotización y la conexión de los tres, que dependen de lo anterior.

- **Construimos**: Intezia construye cada agente con cargas y correos reales de la agencia.
- **Probamos**: El equipo los prueba con cargas reales y dice qué ajustar, antes de usarlos solos.
- **Adoptamos**: El equipo los usa en su trabajo diario y sabe cuándo revisar.
- **Medimos**: El tiempo recuperado por flujo y el gasto en cada valoración.

- En la práctica, **Con el trabajo real de cada uno**: Cada agente parte de una tarea de su día a día: cargas, correos y cálculos reales, no ejercicios de aula.
- En la práctica, **Sobre la base propia**: Se parte de lo que la agencia ya tiene archivado; no hace falta el software de un proveedor del sector.
- En la práctica, **Depende de cada portal**: El rastreo depende de cómo permita consultar cada naviera: se prueba con cada una antes de fijar el flujo.
- Datos: Los datos de las cargas y de los clientes se usan solo con la autorización de la agencia, y una persona revisa cada estatus y cotización antes de enviarlos.
- Quién construye: Intezia construye los agentes con la información de la agencia; el equipo los prueba y adopta, sin tener que construir nada.

**Logística:** modalidad: Presencial en su sede de Puerto Cabello, según se acuerde en la reunión de arranque. · participantes: Tráfico, Valoración y la dueña, para probar y adoptar los agentes. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas de cada flujo; Tiempo actual por tarea; Tiempo con el agente; Horas recuperadas; Gasto en cada valoración.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> Los tres flujos quedan conectados: de la carga que llega al correo a la valoración, el estatus y la cotización, con el equipo usando y revisando cada agente.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

