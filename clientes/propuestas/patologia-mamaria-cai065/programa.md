# Programa interno · Unidad de Patología Mamaria · Servicio de Habilidades (CAI-065)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (22/10/2026) y transcripción de la reunión del 22/10/2026.

## 1. Resumen

- **5 entregables en 5 bloques**, **12 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Herramienta de IA**: 5 entregables, 12 h.
- Horas por fase: F1 2 h (1 sol.) · F2 10 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Historia, imágenes y citas | Herramienta de IA | Levantamiento y lineamientos, Historia clínica asistida, Imágenes médicas, Datos y documentos, Agendamiento de citas | 12 | 5 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Arranque (levantamiento de tareas y reglas) | Construcción (en vivo, tarea por tarea) |
|---|---|---|
| Historia, imágenes y citas | 2 h · 1 sol. | 10 h · 4 sol. |

- **Kick-off**: Hasta 1 h para alinear al equipo, aparte de las horas.
- **Levantamiento**: Tareas, reglas de uso e imágenes validadas.
- **Construcción**: Historia clínica, imágenes, datos y citas, en vivo.
- **30 · 60 · 90 días**: Seguimiento del uso y del tiempo recuperado.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Levantamiento y lineamientos · 1 entregable · 2 h · Herramienta de IA · línea A

Para qué (lo que ve el cliente): Definir con el equipo las tareas reales y las reglas de uso de la información de pacientes

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| LEV-1 | Tareas levantadas y lineamientos de uso (incluye: Qué se construye y qué se evalúa antes; Imágenes validadas antes de prometer su uso; Reglas de uso de los datos de pacientes) | Trabajo de 2 h con el equipo. Se levanta cómo trabaja cada persona hoy, se valida si las imágenes se pueden usar con IA antes de prometerlo, se evalúa cuáles de las demás ideas propuestas (historia clínica asistida, citas, hojas de cálculo y documentos) se pueden construir con la herramienta y con la información que la unidad autorice, y se acuerdan los lineamientos de uso de la información de pacientes. Entrega las tareas, la validación y los lineamientos. | - | - | - | 2 | F1 |

### Historia clínica asistida · 1 entregable · 4 h · Herramienta de IA · línea A

Para qué (lo que ve el cliente): Que el médico dedique su atención al paciente y revise un borrador en vez de escribir

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| HIS-1 | Borrador de historia clínica que el médico revisa (incluye: Borrador que el médico revisa y valida; Historias e imágenes ordenadas y buscables, a evaluar) | Trabajo de 4 h con el equipo, a evaluar en el levantamiento. Se construye con datos de ejemplo una forma de que la IA arme el borrador de la historia clínica a partir de la consulta, para que el médico solo lo revise y lo valide, y de organizar y buscar historias e imágenes. Que se pueda hacer con la herramienta y con la información autorizada se evalúa antes de construir. Entrega el flujo probado. | - | - | - | 4 | F2 |

### Imágenes médicas · 1 entregable · 2 h · Herramienta de IA · línea A

Para qué (lo que ve el cliente): Validar las imágenes y, si se puede, usar la IA con un método común y no por tanteo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| IMG-1 | Apoyo con imágenes, validado antes de prometerlo | Trabajo de 2 h con el equipo. Primero se validan las imágenes (mamografía, ecografía y fotos pre-cirugía): si la herramienta las puede leer, con qué calidad y con la autorización de la unidad. Solo si la validación resulta, se acuerda un método común de apoyo según las guías de lectura; la IA orienta y el médico valida y decide. Entrega la validación y, si procede, el método probado con ejemplos. | - | - | - | 2 | F2 |

### Datos y documentos · 1 entregable · 2 h · Herramienta de IA · línea A

Para qué (lo que ve el cliente): Resolver con IA el manejo de datos y la redacción que hoy toman tiempo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DAT-1 | Hojas de cálculo y documentos clínicos y académicos | Trabajo de 2 h con el equipo. Se resuelven con IA el manejo de hojas de cálculo (cargar y extraer datos) y la redacción de documentos clínicos y académicos, sobre tareas reales del equipo. Entrega las tareas resueltas y la forma de repetirlas. | - | - | - | 2 | F2 |

### Agendamiento de citas · 1 entregable · 2 h · Herramienta de IA · línea A

Para qué (lo que ve el cliente): Montar el agendamiento digital desde el día uno, antes de abrir la unidad

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CIT-1 | Agendamiento de citas digital desde el inicio | Trabajo de 2 h con el equipo, a evaluar en el levantamiento. Se diseña y se prueba cómo agendar y manejar las citas de forma digital desde el arranque de la unidad, con la herramienta que se defina. Es la segunda prioridad, después de la historia clínica. Entrega el agendamiento probado. | - | - | - | 2 | F2 |

## 4. Fuera de alcance

- Un sistema de resguardo (repositorio único de historias e imágenes): se evalúa en el levantamiento y no se promete antes.
- Uso de imágenes médicas con IA: no se promete hasta validar las imágenes en el levantamiento.
- Licencias de herramientas de IA: se definen con la unidad tras el levantamiento y no están en esta inversión.
- Diagnóstico médico: la IA apoya con borradores y orientación, y el médico valida y decide siempre.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (23/10/2026): propuesta de Habilidades para la Unidad de Patología Mamaria del Instituto Médico La Floresta, código CAI-065, asesora Verónica Rubio. Educación, sin alianza, Habilidades puro (sin nombrar Detección) y contacto de Verónica confirmados por Ivana.
- Insumo: Ficha de Levantamiento y transcripción de la reunión del 22/10/2026 (45 min, con la Dra. Maybell Nieves y el Dr. Andrés Calles). La observación interna de la ficha pide «un Habilidades enfocado a sus roles» porque la unidad aún no opera y una Detección clásica no tiene procesos que auditar. Sin nombres de personas en el deck.
- Horas (Ivana): levantamiento 2 h, historia clínica 4 h, imágenes 2 h, datos y documentos 2 h y citas 2 h: 12 h de trabajo. Propuse 10 h; Ivana subió la historia clínica a 4 h y las citas a 2 h y dejó el resto. El kick-off, de hasta 1 h, va aparte y no suma (criterio de Ivana del 23/10/2026).
- Herramienta sin nombrar (Ivana): hoy usan Copilot con licencias personales de Microsoft 365, Gemini de pago para imágenes y Perplexity, y esperan la recomendación; en la reunión Verónica mostró Claude. La unidad está en Caracas y Claude no tiene soporte en Venezuela (nunca se promete VPN). La herramienta se define en el levantamiento; las licencias no están en la inversión y no hay valores en el deck.
- Lo que se construye depende de la evaluación: historia clínica asistida (que una IA escuche la consulta y arme el borrador), imágenes con criterio unificado y agendamiento de citas se presentan como propuestas a evaluar en el levantamiento, no como compromisos (Ivana).
- Repositorio único por paciente (exámenes, cirugías, imágenes y fotos pre-cirugía): es una de las dos prioridades de Maybell, pero es un sistema de resguardo y no una capacitación. Va en «Fuera de este alcance» como algo que se evalúa, y Ivana lo evaluará con el resto del equipo; dentro de la historia clínica solo se prueba organizar y buscar historias e imágenes, a evaluar.
- Participantes: tal como lo dice la transcripción (25:19), «en la clínica seríamos nosotros dos nada más y en el equipo seríamos cuatro». El deck dice «Cuatro personas en el equipo; hoy, dos en la clínica» y no precisa quién va a cada bloque.
- Datos de pacientes: manejarán historias clínicas con imágenes y fotos y la reunión no tocó regulación, resguardo ni confidencialidad. El deck habla solo de lo que la unidad autorice, datos de ejemplo y lineamientos de uso desde el arranque; no afirma cumplimiento de ninguna norma ni que la IA diagnostique.
- Seguimiento 30-60-90 con garantía: Verónica lo explicó en la reunión y Ivana no lo cambió (no respondió esa pregunta); queda como en el estándar de Habilidades. Sin facilidad de pago (Ivana): 8 slides con hoja de inversión de valores vacíos, sin casillas por parte ni tarjetas de licencias. El programa de posgrado de mastología se dejó fuera, como pidió Ivana.
- Retorno en modo método: no hay datos de la unidad y aún no opera, así que la línea base se toma al empezar (levantamiento), no «hoy».
- Contexto interno que no va en el deck: presupuesto no definido y alerta de costos («nosotros no podemos costear costos tan altos»); para montos altos decide el Instituto Médico La Floresta, interlocutor no identificado; patrocinio no asegurado; apertura al cambio alta; reunión de revisión la semana del 27/10/2026 y propuesta comprometida por correo el 23/10/2026; Andrés vive lejos y prefiere lo virtual; correo y teléfono del Dr. Calles por confirmar.
- Imágenes (Ivana, 23/10/2026): el deck dice que las imágenes (mamografía, ecografía y fotos pre-cirugía) se validan en el levantamiento antes de prometer que se puede hacer cualquier uso con IA; el bloque de imágenes queda condicionado a esa validación y su entregable es la validación y, si procede, el método.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se levantan las tareas y las reglas de uso; después se construye, de la historia clínica a las citas, y al final se mide el uso.

- **Levantamos**: Las tareas reales del equipo y las reglas de uso de la información.
- **Evaluamos**: Qué se puede hacer en cada tarea, antes de prometerlo.
- **Construimos**: En vivo con el equipo, una tarea por vez.
- **Medimos**: El uso y el tiempo recuperado, a 30, 60 y 90 días.

- En la práctica, **Primero se valida**: Las imágenes se validan antes de prometer su uso; la historia asistida y las citas se evalúan antes de construirlas.
- En la práctica, **El médico decide**: La IA propone borradores y apoyos; el médico revisa, valida y decide.
- En la práctica, **Con ejemplos**: Se construye con datos de ejemplo mientras no haya autorización para usar información real.
- Datos: Se trabaja solo con lo que la unidad autoriza: nada de pacientes entra a una herramienta de IA sin su visto bueno, y los lineamientos de uso se acuerdan desde el arranque.
- Quién construye: Intezia construye junto al equipo, en vivo y sobre sus tareas reales: no se entrega nada hecho.

**Logística:** modalidad: Mixta: presencial en la unidad y virtual para quien viva lejos. · participantes: Cuatro personas en el equipo; hoy, dos en la clínica. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: La fecha la fija la unidad; el kick-off, de hasta 1 h y aparte, acuerda calendario y accesos..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo de partida; Tiempo con la herramienta; Horas recuperadas.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

