# Brief — IMECA

---

## Datos administrativos

- **Empresa**: IMECA
- **Sector**: Venta de materiales de construcción
- **Tamaño**: Mediana (50-250 empleados)
- **Slug**: `imeca`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Tipo de documento**: Capacitación In-Company (`CAI-016`)
- **Eje temático**: Automatización con Claude de procesos 100% manuales (conciliación bancaria, atención al cliente), con una sesión de Apertura dedicada a manejo del cambio antes del contenido técnico
- **Fecha del brief**: 2026-09-08
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento IMECA** (`Levantamiento_IMECA_2026-09-07.pdf`, reunión del 2026-09-07), elaborada por la asesora **Verónica Rubio**. Es la fuente primaria de los datos de esta sección — no se armó por instrucción directa suelta, sino desde la ficha completa. Datos tomados de la ficha: sector, tamaño, contacto, stack tecnológico, universo de personas, los 2 procesos del Bloque C (conciliación bancaria y carga/revisión de documentos), restricciones (Bloque E) y observaciones internas (Bloque F).

## Contacto

- **Asesora comercial**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Contacto cliente**: María Pérez y José Escorcha (equipo de Tecnología) · jescorcha@imeca.com
- **Aliado / aval**: ninguno
- **Servicio previo con Intezia**: ninguno — primer contacto

## Necesidad detectada

Objetivo central citado textualmente por el cliente: **"Automatizar todos los procesos manuales."**

1. **Conciliación bancaria** (Administración/Contabilidad): +3.000 documentos revisados uno a uno, todos los días, ocupa una jornada completa (8h/día). Es el cuello de botella más grave de IMECA.
2. **Carga y revisión/rechequeo de documentos** (Administración/Contabilidad): necesidad de rechequear manualmente gran parte de los documentos cargados.
3. **Atención al Cliente**: automatización de respuestas. Ya intentaron un agente de automatización en n8n, pero lo cerraron por alto volumen y costo de mensajes — la solución debe evitar ese mismo problema.
4. **Tecnología**: no tiene un cuello de botella manual como las otras 2 áreas — ya usa IA de forma más adelantada (apoyo a diseño, investigaciones, análisis de datos). Fue el equipo que pidió esta propuesta.

**Uso de IA hoy**: Gemini a criterio individual, sin licencias corporativas ni criterio común (fuera de Tecnología, uso básico tipo consulta). **Herramienta deseada por el cliente: Claude.**

**Nivel de partida**: mixto — algunos colaboradores ya usan bien la IA, otros no la usan en absoluto. Sin formación previa en IA.

**Resistencia al cambio (crítico, de Bloque F de la ficha)**: los colaboradores temen ser sustituidos por la IA. La ficha es explícita: *"la capacitación debe trabajar primero esa resistencia, antes que la parte técnica."* Apertura al cambio calificada como "Media"; patrocinio ejecutivo "presente pero tibio". Por esto la propuesta abre con una sesión de manejo del cambio antes de cualquier contenido técnico (decisión confirmada con el usuario, ver sección Decisiones).

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: Google Workspace.
- **Sistema de gestión central** interno (tipo ERP) para la información del negocio.
- **Comunicación operativa**: WhatsApp (grupos) y correo. Teams casi no se usa.
- Intezia se integra a este entorno, no lo cambia.

## Universo y modalidad

- **~40 personas** entre Tecnología, Administración/Contabilidad y Atención al Cliente.
- **Roles**: mixto — operativo, analistas, supervisores, gerentes.
- **Modalidad**: Presencial (confirmado en la ficha). Sede: Valencia, preferida para arrancar.
- **Duración de sesión preferida**: 2 horas.
- **Restricciones operativas**: a mutuo acuerdo (sin bloqueo específico de horario más allá de eso).
- **Política de datos**: sin política cerrada, salvo la información bancaria (área de Finanzas) — se respeta en las prácticas de conciliación bancaria.
- **Regulación sectorial**: ninguna en particular.
- **Presupuesto**: no definido aún.
- **Medición esperada**: seguimiento a 30, 60 y 90 días (confirmado en la ficha); sin KPIs definidos todavía por el cliente — esta propuesta ayuda a construir el caso de negocio interno de IMECA, dado el patrocinio ejecutivo tibio.

## Decisiones confirmadas con el usuario (2026-09-08)

1. **Rol de Tecnología**: track propio, de nivel más avanzado que Administración/Contabilidad y Atención al Cliente (no el mismo contenido introductorio, ni solo facilitadores sin sesión propia).
2. **Manejo del cambio**: sesión de Apertura propia (2h, para las ~3 áreas juntas), antes de las sesiones técnicas por área — no un enfoque solo transversal sin sesión dedicada.
3. **Volumen del programa**: compacto — 1 sesión de Apertura + 2 sesiones de 2h por cada una de las 3 áreas = **7 sesiones, 14 horas totales**.
4. Esta propuesta es la que se presenta en la reunión de seguimiento de la ficha (fecha no mencionada en el deck, por instrucción del usuario).

## Estructura de la propuesta (4 tracks, 1 sola cotización)

- **Apertura** (~40 personas, todas las áreas) — 1 sesión de 2h: manejo del cambio, IA como herramienta complementaria, no amenaza.
- **Administración y Contabilidad** — 2 sesiones de 2h (4h): conciliación bancaria y carga/revisión de documentos con Claude.
- **Atención al Cliente** — 2 sesiones de 2h (4h): automatización de respuestas con Claude, sin repetir el costo/volumen que cerró el intento con n8n.
- **Tecnología** — 2 sesiones de 2h (4h), track avanzado: de uso ad-hoc a automatización de procesos, y rol de soporte interno al rollout de las otras 2 áreas.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Notas internas

- Primer contacto de IMECA con Intezia — sin Detección previa; la ficha de levantamiento ya cumplió ese rol de diagnóstico.
- Eje 100% Claude (herramienta ya elegida por el cliente). No introducir n8n (ya lo probaron y lo cerraron) ni otras plataformas.
- Caso base estructural: `simple-tv-cai014/` (shell compliant vigente: Beneficios v3, Cierre escalera, precio estándar) + mecánica de tracks diferenciados por área de `go-pharma/` y `bit-honor/` (grid de módulos + cronograma por track).
- Patrocinio ejecutivo tibio y presupuesto no definido: el deck debe ayudar a vender el caso de negocio internamente, sin exponer esta intel de ventas en el copy visible.
