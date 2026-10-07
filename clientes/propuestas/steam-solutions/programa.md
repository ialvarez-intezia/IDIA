# Programa interno · Steam Solutions · Servicio de Habilidades (CAI-038)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Steam Solutions.

## 1. Resumen

- **6 entregables en 3 módulos**, **18 h** de sesión, más seguimiento a 30, 60 y 90 días.
- Carril **Desarrollo con IA**: 6 entregables, 18 h.
- Horas por fase: F1 4 h (2 sol.) · F2 12 h (3 sol.) · F3 2 h (1 sol.).

## 2. Frentes y ruta

| Frente | Carril | Áreas | Semanas | Horas | Soluciones |
|---|---|---|---|---|---|
| A | Desarrollo con IA | Fundamentals y método, Agentes de IA, Implementación | S1-S6 | 18 | 6 |

| Frente | Método (Semanas 1 y 2) | Agentes (Semanas 3 a 5) | Implementación (Semana 6) |
|---|---|---|---|
| A | 4 h · 2 sol. | 12 h · 3 sol. | 2 h · 1 sol. |

- **Kick-off · aparte**: 1 h para definir la herramienta de IA, la tarea real de práctica y la disponibilidad.
- **Semanas 1 y 2 · Método**: 2 sesiones de 2 h: criterios de uso de la IA y especificación antes de programar.
- **Semanas 3 a 5 · Agentes**: 3 sesiones de 4 h: el equipo construye sus agentes, con nuestra guía, sobre tareas reales.
- **Semana 6 · Implementación**: Flujo común de especificación, código, pruebas y despliegue, adoptado por el equipo.
- **30 · 60 · 90 días**: Seguimiento: uso, nuevos agentes y tiempo recuperado contra la línea base.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Fundamentals y método · 2 entregables · 4 h · carril Desarrollo con IA · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FUN-1 | Guía de criterios y reglas de uso de la IA en desarrollo | Fundamentals de 2 h con los 8 desarrolladores, en un solo grupo (bajo el máximo de 25 por sesión). Temas: cómo trabaja un asistente de IA para programar y cómo trabaja un agente, qué contexto y qué permisos necesita, qué se revisa siempre antes de aceptar un cambio, y qué reglas de datos aplican (trabajo en ambiente de desarrollo con datos sintéticos, como ya lo hace el equipo). La guía descargable resume los criterios y reglas comunes. Registra la línea base del tiempo que toma hoy probar y desplegar. La herramienta de IA para desarrollo ya se definió en el kick-off, que va aparte. | - | - | - | 2 | F1 |
| MET-1 | Plantilla de especificación e instrucciones reutilizables (skills) | Sesión práctica de 2 h para instalar el método: el prototipo de pantalla (insumo para validar requerimientos con el cliente) se convierte en una especificación completa, y se definen las instrucciones reutilizables (skills) que la IA lee antes de programar. Se trabaja sobre una tarea real del equipo. Entrega la plantilla de especificación y las primeras instrucciones reutilizables. | - | - | - | 2 | F1 |

### Agentes de IA · 3 entregables · 12 h · carril Desarrollo con IA · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DEV-1 | Agente de desarrollo, probado en una tarea real | Sesión práctica de 4 h en la que el equipo construye, con la guía de Intezia, un agente de desarrollo que parte de la especificación (tareas de Odoo y Python, o de las apps móviles, según la tarea real elegida) y lo prueba en esa tarea hasta que funciona. Intezia orienta y revisa; el equipo es quien lo construye. | - | - | - | 4 | F2 |
| TES-1 | Agente de pruebas automatizadas, probado en una tarea real | Sesión práctica de 4 h en la que el equipo construye, con la guía de Intezia, un agente que escribe y ejecuta pruebas automatizadas a partir de la especificación, y lo prueba sobre el código que produce el agente de desarrollo hasta que funciona. | - | - | - | 4 | F2 |
| DEP-1 | Agente de despliegue, probado en un ambiente de desarrollo | Sesión práctica de 4 h en la que el equipo construye, con la guía de Intezia, un agente que prepara y ejecuta el despliegue, y lo prueba en un ambiente de desarrollo con datos sintéticos hasta que funciona. Las sesiones no despliegan a producción. | - | - | - | 4 | F2 |

### Implementación · 1 entregable · 2 h · carril Desarrollo con IA · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FLU-1 | Flujo común de especificación, código, pruebas y despliegue | Sesión de 2 h para unir el método y los 3 agentes en un solo flujo: de la especificación al despliegue, con responsables, criterios de revisión y reglas de uso. El equipo lo documenta, con la guía de Intezia, y lo adopta en una tarea real, para dejar de trabajar cada quien a su manera. | - | - | - | 2 | F3 |

## 4. Fuera de alcance

- Producción y datos reales de salud: las sesiones usan un ambiente de desarrollo con datos sintéticos.
- La licencia de la herramienta de IA, que va aparte.

## 5. Supuestos a confirmar

- Código CAI-038 indicado por el usuario (siguiente libre tras CAI-037). División Educación y alianza «no» inferidas: software house privada, cliente corporativo, sin alianza en la ficha. Confirmar con la asesora.
- Guardia §4.21 punto 5: no se preguntó. El contenido son soluciones concretas (un método y 3 agentes), no un programa de módulos de charla o curso, así que va directo al compacto, como CAI-032 y CAI-037.
- Herramienta de IA: por instrucción del usuario (06/10/2026) se define en el kick-off. El deck no nombra ninguna herramienta ni las 4 que usa hoy el equipo (ficha); dice que se elige en el kick-off. El problema de pago con tarjetas en Venezuela que tuvo el equipo con una membresía se anticipa como criterio de elección (pago y renovación estables), sin nombrar la herramienta (§4.11: no se afirma que el cliente cambie de stack).
- Horas: 18 h por instrucción del usuario (06/10/2026). Se había propuesto 12 h (el tope del lineamiento de Habilidades: 8 a 12 h por área, hasta 5 procesos, con 2 h por agente) y el usuario subió cada agente a 4 h para dar holgura. Excede el tope del lineamiento: es una excepción decidida por el usuario. Son Fundamentals 2 h, método 2 h, 3 agentes de 4 h y flujo común 2 h. El kick-off de 1 h va aparte y no suma (como CAI-034 y CAI-037).
- Reparto y calendario propuestos por el sistema: 6 sesiones, una por semana, en 6 semanas (Fundamentals y método de 2 h en las semanas 1 y 2, un agente de 4 h por semana en las 3 a 5 y el flujo común de 2 h en la 6). Se supuso una sesión de 4 h por agente; también podría ser en 2 sesiones de 2 h según la disponibilidad semipresencial (4 o 5 personas en la oficina por día, el resto remoto), que la ficha deja para el kick-off: confirmar.
- Rol del equipo y de Intezia (instrucción del usuario, 06/10/2026): Intezia guía la construcción para que cada agente funcione, pero es el equipo quien lo construye. Por eso se quitó de «Fuera de este alcance» el punto «agentes terminados para producción» y el deck dice «guiamos» donde antes decía «construimos». Cada entregable sigue acotado a «probado en una tarea real» o «en un ambiente de desarrollo». La expectativa del cliente (agentes «autónomos y robustos») se consolida en el seguimiento a 30, 60 y 90 días; con 4 h por agente (subido por el usuario para dar holgura), confirmar con servicio que alcanza para que funcionen.
- Se trabaja en ambiente de desarrollo con datos sintéticos, que es la política que el cliente ya sigue (su solución vendida a clínicas está sujeta a normativa de datos de salud). El deck no cita ninguna norma.
- Las 8 personas son los programadores del equipo de desarrollo (no incluye servidores/plataforma): un solo grupo de Fundamentals. Quién asiste a cada sesión de agentes depende de la disponibilidad semipresencial: confirmar.
- Los hechos de la portada salen de la ficha. «Cuatro distintas» cuenta las herramientas que la ficha menciona (cuatro), sin nombrarlas. Se omitió la frase de la ficha sobre falta de rigor en especificaciones: se dice neutral que falta un método común.
- «Skills» aparece solo en un entregable y glosado como «instrucciones reutilizables (skills)» (§4.12 y §4.4: término nativo de las herramientas de IA). En el resto del deck se dice «especificación».
- Línea base del tiempo actual de probar y desplegar: se levanta en la sesión de Fundamentals (2 h). Confirmar con servicio que cabe.
- Retorno en modo método: la ficha no trae volúmenes, tiempos ni costo hora. «Hacia la semana N» es aritmética (semanas de trabajo + 13): confirmar con servicio.
- Sin certificado de participación por defecto (§4.21). Sin nombres de personas del cliente ni su cargo. La sede (oficinas del cliente o sala de Intezia) y los viáticos no van en el deck: son un tema comercial pendiente.

## 6. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.
Hacia la semana 19: construcción (6 semanas) más 90 días de seguimiento; aritmética a confirmar con servicio.

Pasos del método: Volumen semanal; Tiempo actual por tarea; Tiempo con los agentes; Horas recuperadas a la semana; Valor en dinero.

