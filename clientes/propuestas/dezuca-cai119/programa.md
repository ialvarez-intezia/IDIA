# Programa interno · Dezuca · Servicio de Habilidades (CAI-119)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Resumen de Ventas de la primera reunión con el dueño de Dezuca (23/11/2026); sin ficha ni transcripción.

## 1. Resumen

- **6 entregables en 2 áreas**, **16 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **IA para la producción**: 6 entregables, 16 h.
- Horas por fase: F1 10 h (4 sol.) · F2 6 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Producción de Dezuca | IA para la producción | Aplicación de producción, Cerebro Digital de la dirección | 16 | 6 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Aplicación (Pedido, puestos y dashboard) | Cerebro (Dirección) |
|---|---|---|
| Producción de Dezuca | 10 h · 4 sol. | 6 h · 2 sol. |

- **Arranque**: Reunión para conocer los puestos, ver el recorrido de un pedido y fijar la línea base.
- **Puestos**: Cada puesto usa su pantalla con órdenes reales.
- **Dashboard**: Un pedido se sigue en su línea de tiempo y en el dashboard.
- **Cierre**: La dirección usa su Cerebro Digital; empieza la garantía.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Aplicación de producción · 4 entregables · 10 h · IA para la producción · línea A

Para qué (lo que ve el cliente): Que cada puesto vea solo lo que le toca y la dirección siga cada pedido hasta la entrega

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AP-1 | Carga del pedido (orden única) | Un formato de orden que recibe cada cliente y cada prenda (diseño, tallas, tela y entrega) y alimenta a corte y a diseño desde el inicio, para que lleguen juntos a impresión y sublimación. | - | - | - | 2 | F1 |
| AP-2 | Pantalla simple por puesto | Una pantalla para cada puesto (corte, diseño, sublimación y costura), con el mismo patrón: ver la siguiente orden con lo que toca hacer y marcar el avance en dos toques, sin escribir ni buscar. Cada puesto entra solo a lo suyo. Pensada para una tableta y para personal operativo. | - | - | - | 5 | F1 |
| AP-3 | Línea de tiempo y dashboard | Cada marca de un puesto queda registrada con su hora. Con ellas, una línea de tiempo por pedido y un dashboard para la dirección, que reemplaza los tableros en Excel armados a mano. | - | - | - | 2 | F1 |
| AP-4 | Prueba en planta con cada puesto | Cada puesto prueba su pantalla con órdenes reales y dice qué ajustar, antes de usarla solo. | - | - | - | 1 | F1 |

### Cerebro Digital de la dirección · 2 entregables · 6 h · IA para la producción · línea A

Para qué (lo que ve el cliente): Un asistente con el contexto de la empresa, para decidir con datos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CD-1 | Cerebro con contexto y análisis financiero | El contexto de la empresa, sus skills (instrucciones guardadas) de órdenes, presupuesto y prioridades, y el análisis de costos y financiero, reunidos en un asistente en ChatGPT para el dueño. La información sensible queda solo para él y para quien él decida. | - | - | - | 4 | F2 |
| CD-2 | Informe semanal de ejemplo | Un informe semanal de inventario y compras que el Cerebro prepara con los datos que Dezuca entregue, como modelo para los siguientes informes. | - | - | - | 2 | F2 |

## 4. Fuera de alcance

- Licencias de IA: no están en la inversión; Dezuca ya tiene ChatGPT Business.
- Un sistema completo de gestión: se construye una aplicación base sencilla, que puede crecer en una siguiente etapa.
- Siguiente etapa: inventario y compras, productividad por costurera, presupuesto contra real, predicción y alertas.
- Cambiar las tabletas que ya usan: la aplicación se apoya en ellas.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (24/11/2026): propuesta CAI-119 de Habilidades para Dezuca, con María Iribarren como directora comercial. Insumo: resumen de Ventas de la primera reunión con el dueño (conocido en el IA TechDay); sin ficha ni transcripción. Propuesta prometida entre el martes 24 y el miércoles 25 de noviembre.
- Decisiones de Ivana (24/11/2026): Educación y sin alianza (confirmado); impacto «operación»; una sola hoja de inversión, sin plan de pago. Ajuste del mismo día tras el correo de María (había anticipado alrededor de 4.000 por un piloto parecido al de Médica Campestre, 10 h de prototipo): de 80 h a **16 h**, con una aplicación hecha con Codex (10 h) y el Cerebro Digital (6 h, el estándar).
- Reparto de horas mío (Ivana fijó 16 h): aplicación 10 h (carga del pedido 2, pantalla por puesto 5 con patrón replicado en cuatro puestos y acceso por usuario, línea de tiempo y dashboard 2, prueba en planta 1); Cerebro Digital 6 h (contexto, skills y análisis financiero 4, informe semanal de ejemplo 2). Fases de 10 y 6 h.
- El alcance sale del pedido del dueño: (1) Cerebro Digital con el contexto, skills, costos y financiero, predicción y alertas, e informe semanal; (2) aplicación simple por puesto con control de accesos que alimente un dashboard en tiempo real y la línea de tiempo del pedido, amigable. La línea de tiempo y el dashboard salen del mismo registro de marcas (pedido, puesto y hora), por eso caben en pocas horas. Quedan para una siguiente etapa, sin horas ni valor: inventario y compras, productividad por costurera, presupuesto contra real, predicción y alertas automáticas.
- La aplicación se presenta como un prototipo funcional hecho en conjunto con el equipo con Codex (como el de Médica Campestre, que no se nombra en el deck); el Cerebro Digital va en ChatGPT. Se nombran Codex y ChatGPT por pedido de Ivana (excepción a «sin nombrar herramienta»). No se nombra «GPT personalizado» porque OpenAI lo retirará.
- Sin nombre de personas del cliente (el deck no nombra al dueño ni al equipo). Se nombra ChatGPT por pedido de Ivana, igual que en el CAI-112 con los sistemas del cliente. No se menciona Claude. Cerebro Digital del dueño con información sensible solo para él y quien él decida (en «Cómo trabajamos»).
- Sin semanas, sesiones ni fechas (§4.23): horas de sesión en vivo, número de sesiones, fechas posibles y consultor asignado (que Ventas pidió a Servicio) viven en la reunión de arranque y en el Brief de Kickoff, que solo se hace si Ivana lo pide.
- Valor: Ventas anticipó alrededor de 4.000 al cliente; no va en el deck (hoja de inversión con valores vacíos, en REF). Retorno en modo método: no hay horas ni volúmenes medidos del cliente. Sin certificado. Seguimiento 30-60-90 incluido por ser estándar de Habilidades.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero el pedido y los puestos, porque de ahí salen los datos. La línea de tiempo y el dashboard se alimentan de las marcas, y al final el Cerebro Digital reúne el contexto de la dirección.

- **Mapeamos**: Cómo viaja hoy un pedido por cada puesto y qué necesita ver cada uno.
- **Construimos**: En conjunto con el equipo, con Codex y con lo que ya tiene Dezuca.
- **Probamos**: Cada puesto prueba su pantalla con órdenes reales y dice qué ajustar.
- **Medimos**: El tiempo de cada tarea, contra la línea base del arranque.

- En la práctica, **Una aplicación para todos**: Pantallas sencillas por puesto, pensadas para personas no técnicas; cada puesto entra solo a lo suyo.
- En la práctica, **Dos toques por tarea**: Cada pantalla se diseña para la planta: ver la orden y marcar el avance, sin escribir ni buscar.
- En la práctica, **Una base que puede crecer**: Es un prototipo funcional que se prueba en la planta; lo que se agregue después se acuerda en una siguiente etapa.
- Datos: Los márgenes, los gastos y los datos de la empresa quedan solo para la dirección y para quien ella decida; cada puesto ve únicamente lo suyo.
- Quién construye: Intezia guía y el equipo de Dezuca construye en conjunto, con Codex, la aplicación que cada puesto va a usar.

**Logística:** modalidad: Se acuerda en la reunión de arranque: en la planta con los puestos y en línea con la dirección. · participantes: La dirección, administración, ventas y una persona por puesto de la planta. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas de cada puesto; Tiempo actual por tarea; Tiempo con la pantalla; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> Cada puesto sabe qué le toca, el pedido deja de ser una pregunta en planta y la dirección ve la fábrica con datos, no con Excel armado a mano.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056.

