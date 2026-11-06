# Programa interno · Hospital de Clínicas Caracas · Servicio de Habilidades (CAI-067)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (27/10/2026) y contexto de la reunión redactado por Flavia Martínez; sin transcripción.

## 1. Resumen

- **7 entregables en 4 líneas de trabajo**, **18 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Herramientas de IA del hospital**: 7 entregables, 18 h.
- Horas por fase: F1 6 h (3 sol.) · F2 12 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Equipo comercial | Herramientas de IA del hospital | Fundamentos de IA, Atención y seguimiento de leads, Campañas por correo, Página web de reservas | 18 | 7 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Nivelación y levantamiento (equipo nivelado y punto de partida medido) | Construcción (herramientas construidas con el equipo y en uso) |
|---|---|---|
| Equipo comercial | 6 h · 3 sol. | 12 h · 4 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario y quién coordina por Clínicas Caracas.
- **Nivelación y levantamiento**: Fundamentos de IA y el punto de partida de cada proceso del área.
- **Herramientas en uso**: Atención y seguimiento de leads, campañas segmentadas y mejoras de la web.
- **30 · 60 · 90 días**: Seguimiento: uso de las herramientas, ajustes y avances medidos.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Fundamentos de IA · 2 entregables · 4 h · Herramientas de IA del hospital · línea A

Para qué (lo que ve el cliente): Nivelar al equipo para que participe en la construcción y luego la mantenga

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NV-1 | Fundamentos de IA: qué es y cómo pedirle bien (incluye: Qué es y qué no es la IA; Cómo pedirle bien, con ejemplos del área comercial) | Módulo de 2 h con las 9 personas del equipo comercial, en un solo grupo. Se nivela al equipo, que hoy parte de cero, con ejemplos de captación, atención y seguimiento de leads. Las herramientas concretas se definen en el levantamiento, según el ecosistema del hospital. Entrega al equipo con una noción común. | - | - | - | 2 | F1 |
| NV-2 | Fundamentos de IA: cuidar los datos de pacientes (incluye: Qué datos de pacientes no se comparten con la IA; Pautas básicas de manejo de datos) | Módulo de 2 h con el mismo grupo. Se acuerdan las pautas básicas para usar la IA sin exponer datos de pacientes, que son información de salud sensible. El hospital no tiene hoy una política de datos: estas pautas no la reemplazan (Políticas queda como complemento opcional). Entrega las pautas básicas. | - | - | - | 2 | F1 |

### Atención y seguimiento de leads · 3 entregables · 8 h · Herramientas de IA del hospital · línea A

Para qué (lo que ve el cliente): Atender los leads más rápido, también en campaña, y no perder el seguimiento

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AT-1 | Levantamiento del equipo comercial (incluye: Volumen de leads por canal, en un mes normal y en campaña; Dónde está la base de pacientes y en qué estado; Cómo funciona hoy la web de reservas; Línea base del retraso en la atención) | Trabajo de 2 h con el equipo comercial. Se recorre cómo llega y se atiende cada lead por WhatsApp, Instagram y la web, se mide el punto de partida (volumen y retraso), se revisa dónde vive la base de pacientes y cómo funciona la web de reservas, y se confirman el ecosistema y las licencias, que hoy no están definidos. Cubre las tres líneas de trabajo del proyecto. Entrega la línea base y el alcance de cada herramienta. | - | - | - | 2 | F1 |
| AT-2 | Atención y filtrado de leads con IA (incluye: Respuesta propuesta para cada tipo de consulta; Leads ordenados por prioridad; Una persona revisa y responde) | Trabajo de 4 h con el equipo comercial. Se construye con él una herramienta que propone la respuesta a cada tipo de consulta y ordena los leads por prioridad, para atender primero los más urgentes en campaña; una persona revisa y responde. La respuesta automática directa por WhatsApp o Instagram depende de los canales oficiales y las herramientas que el hospital contrate: se evalúa en el levantamiento, sin compromiso previo. Entrega la herramienta en uso. | - | - | - | 4 | F2 |
| AT-3 | Seguimiento de leads (incluye: Lista ordenada de leads por contactar; Mensajes de seguimiento listos para enviar) | Trabajo de 2 h con el equipo comercial. Se arma con él una lista de seguimiento de los leads por contactar y los mensajes que la IA redacta para cada caso; la persona los revisa y los envía. No incluye un CRM. Entrega el seguimiento funcionando. | - | - | - | 2 | F2 |

### Campañas por correo · 1 entregable · 4 h · Herramientas de IA del hospital · línea A

Para qué (lo que ve el cliente): Segmentar la base de pacientes y armar cada campaña sin trabajo manual

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CA-1 | Segmentación y campañas por correo con IA (incluye: Segmentos por servicio de ingreso, género y edad; Textos de la campaña por segmento; Pautas de manejo de datos de pacientes) | Trabajo de 4 h con el equipo comercial. Se construye con él la segmentación de la base por servicio de ingreso, género y edad, y los textos de cada campaña, trabajando con datos de muestra o sin identificar: los datos reales de pacientes no se cargan a ninguna herramienta sin autorización. Depende de que la base tenga esos campos, que se confirma en el levantamiento. El envío masivo requiere una herramienta de correo que el hospital ya tenga o contrate. Entrega el proceso de segmentación en uso. | - | - | - | 4 | F2 |

### Página web de reservas · 1 entregable · 2 h · Herramientas de IA del hospital · línea A

Para qué (lo que ve el cliente): Proponer cómo mejorarla como canal de captación y de reserva de citas

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| WE-1 | Propuesta de mejoras para la web de reservas (incluye: Revisión de cómo se reserva hoy una cita; Mejoras propuestas, ordenadas por prioridad) | Trabajo de 2 h con el equipo comercial. Se revisa cómo funciona hoy la web de reservas como canal de captación y se propone, con el equipo, cómo mejorarla. Los cambios en la web los aplica quien la administra; Intezia propone y acompaña. Entrega la propuesta de mejoras. | - | - | - | 2 | F2 |

## 4. Fuera de alcance

- Entregar o instalar un sistema de gestión de clientes (CRM): es software aparte, y luego es más fácil elegir uno.
- Respuesta automática por WhatsApp o Instagram y envío masivo de correos: dependen de las herramientas que el hospital contrate.
- Licencias y herramientas de envío: las contrata Clínicas Caracas, según su ecosistema, y van aparte de esta inversión.
- Cambios en la web: los aplica quien la administra; Intezia propone y acompaña.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (27/10/2026): propuesta de Habilidades para Hospital de Clínicas Caracas con Flavia Martínez como asesora, a partir de la Ficha de Levantamiento y del contexto que redactó la asesora. Sin transcripción de la reunión (CLAUDE.md §4.23): el contexto de Flavia manda la estructura. Código CAI-067 (siguiente libre tras CAI-066), división Educación y sin alianza: los tres por confirmar con Ivana.
- Cliente: hospital o clínica privada mediana (50 a 250 empleados), institución tradicional y conservadora, primer contacto, sin IA ni formación previa (la ficha dice a la vez «no usan IA» y «la usan suelta y sin criterio»: el deck dice «parte de cero»). Contacto: Samuel Jiménez (área comercial, responsable interno de logística); quién firma y quién decide aún no se sabe. El deck no nombra personas del hospital.
- Qué NO se promete: un CRM (lo pidieron al inicio; Flavia aclaró que Intezia acompaña a construir y automatizar el proceso, no entrega un sistema, y que esto facilita elegir un CRM después): fuera de alcance explícito; respuesta automática directa por WhatsApp o Instagram y envío masivo de correos: dependen de canales oficiales y herramientas que el hospital contrate, se evalúan en el levantamiento sin compromiso previo (la IA propone y una persona responde o envía); reducir el retraso de ~1 día en campañas y enviar campañas sin trabajo manual: son el uso esperado a medir en el 30-60-90, no una garantía; cambios en la web: los aplica quien la administra, Intezia propone y acompaña; segmentar por servicio de ingreso, género y edad: depende de que la base tenga esos campos (se confirma en el levantamiento).
- Datos de pacientes (información de salud sensible, sin política de datos): pautas básicas de manejo de datos dentro de Habilidades (módulo de Fundamentos y campañas), trabajo con datos de muestra o sin identificar y ningún dato real a la IA sin autorización. Políticas queda como complemento opcional, no como requisito, y solo se nombra como siguiente paso (Flavia). No hay regulación sectorial identificada además de la sensibilidad de los datos de salud.
- Líneas de trabajo: Fundamentos de IA, atención y seguimiento de leads (WhatsApp, Instagram y web), campañas por correo con segmentación de la base de pacientes y mejora de la web de reservas. «Octubre Rosa» no se nombra en el deck (el generador avisa de los meses); se dice «campañas grandes».
- Horas (Ivana, 27/10/2026: «súbela a 18 h»): 4 h de Fundamentos de IA (2 módulos de 2 h, un solo grupo de 9 personas, que la asesora pidió como «módulos iniciales» sin fijar horas) + 14 h del área comercial: levantamiento 2 h, atención y filtrado de leads 4 h, seguimiento de leads 2 h, campañas por correo 4 h y web 2 h = 18 h. La regla general de Habilidades (8 a 12 h por área hasta 5 procesos) daría 12 h al área comercial; las 2 h adicionales son pedido de Ivana y las puse en atención de leads y en campañas, que son los dos dolores principales. El reparto es mío, por confirmar. Habilidades no contempla Fundamentos y aquí se suman por pedido de Flavia, nombrados «Fundamentos de IA» (nunca «curso»).
- Horas visibles (criterio de Ivana del 27/10/2026): el deck dice «horas con el equipo» en la ruta y en la hoja de inversión, nunca «horas de trabajo» ni cuántos consultores. Sin pago (facilidad de pago omitida, como en las últimas Habilidades): hoja de inversión única con campos vacíos para ventas; hoy el hospital reúne cotizaciones y el presupuesto está en evaluación.
- Herramientas de IA: sin nombrar ninguna; el ecosistema (Google, Microsoft u otro) y las licencias no se conocen y se definen en el levantamiento. Nunca se promete VPN ni se menciona Claude. «Sistemas tradicionales» y hojas de cálculo: no se afirma migración de stack (§4.11).
- Implementación en 2027, tras aprobaciones internas (hoy reúnen cotizaciones): el deck dice que el arranque lo fija el hospital tras sus aprobaciones, sin fechas (§4.23). Detección queda como siguiente paso cuando quieran escalar a otras áreas (Samuel: lo comercial sería la puerta de entrada); no se vende ahora porque tienen claro qué quieren y en qué área.
- Sin casos de éxito, sin «curso», sin semanas, sesiones ni fechas, sin fuente en la portada ni kickoff o agenda.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se nivela al equipo, que hoy parte de cero, y se mide el punto de partida; después se construye con él, que así participa de verdad y puede mantener lo construido.

- **Nivelamos**: Fundamentos de IA para que el equipo llegue con una noción común.
- **Medimos**: Cómo se atiende hoy cada lead y se arma cada campaña.
- **Construimos**: Con el equipo, cada herramienta, sobre casos reales.
- **Seguimos**: Uso, ajustes y resultados, a 30, 60 y 90 días.

- En la práctica, **Una persona en el circuito**: La IA propone respuestas, mensajes y textos; una persona los revisa antes de enviarlos.
- En la práctica, **Datos de pacientes protegidos**: Se trabaja con datos de muestra o sin identificar; los datos reales no se cargan sin autorización.
- En la práctica, **Sin prometer cifras**: Se mide el punto de partida y cada avance; las metas son de Clínicas Caracas y no se garantizan.
- Datos: Los datos de pacientes son información de salud sensible: no se cargan a ninguna herramienta de IA sin la autorización de Clínicas Caracas; las pautas básicas se acuerdan en los Fundamentos.
- Quién construye: Intezia construye junto al equipo comercial, sobre sus casos reales, para que luego lo mantenga sin depender de un proveedor externo.

**Logística:** modalidad: Presencial, en las oficinas de Clínicas Caracas. · participantes: Las 9 personas del equipo comercial y quien coordina el proyecto por el hospital. · ritmo: Dudas por escrito antes que en llamadas; el trabajo se agenda en el horario del equipo. · arranque: La fija Clínicas Caracas, tras sus aprobaciones; una reunión de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Punto de partida; Con la herramienta; Horas recuperadas; Gasto de operar.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

