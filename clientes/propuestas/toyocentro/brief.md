# Brief — Toyocentro

---

## Datos administrativos

- **Empresa**: Toyocentro (concesionario automotriz Toyota: venta de vehículos, taller y repuestos)
- **Sector**: Automotriz / concesionario
- **Tamaño**: Micro / Pyme (menos de 50 empleados)
- **Slug**: `toyocentro`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Tipo de documento**: Detección (`DET-014`) · Fundamentals (2h grupal) + auditoría de 2
  áreas (Ventas, Tecnología), 4 horas por área (10h totales), modalidad presencial.
- **Eje temático**: Llevar el uso disperso de IA de hoy a un criterio común entre Ventas y
  Tecnología, con logro inmediato por área empezando por el cruce de bases de datos comerciales
  y la atención de leads por WhatsApp fuera de horario.
- **Fecha del brief**: 2026-09-15
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Toyocentro**
(`Levantamiento_Toyocentro_2026-09-14.pdf`, reunión del 2026-09-14), elaborada por la asesora
**Flavia Martínez**.

## Contacto

- **Asesora comercial**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
- **Contacto operativo cliente**: Christopher Rodríguez · Director de Tecnología ·
  christopher.tecnologia@toyocentro.com — lleva la propuesta y el presupuesto a José A. Sol
  para su aprobación, no firma él mismo.
- **Decisor final**: José A. Sol · CEO · firma y decide la contratación.
- **Servicio previo con Intezia**: ninguno — primer contacto.
- **¿Hubo una propuesta previa sin aprobar?**: No.

## Áreas a auditar (2 — dato directo de la ficha, sin ambigüedad)

1. **Ventas** (~6 personas). Stakeholder clave: José A. Sol, CEO (visión y objetivos
   estratégicos).
2. **Tecnología** (2 personas, liderada por Christopher Rodríguez, Director de Tecnología —
   líder técnico in-house, sería quien construya los agentes/soluciones que salgan de la
   auditoría).

**Headcount del alcance**: ~8 personas totales (6 de Ventas, 2 de Tecnología), la misma
audiencia recibiría la sesión de Fundamentals (sin distinción declarada en la ficha entre
quién audita y quién se capacita).

## Decisiones confirmadas / sin ambigüedad

1. **2 áreas** (Ventas y Tecnología) — la ficha lo declara directo, sin necesidad de
   interpretación (a diferencia de otras Detecciones recientes de esta sesión con universo
   ambiguo).
2. **4 horas de Detección por área** (8h) + **Fundamentals de 2h grupal** (8 personas, una
   sola sesión, dentro del máximo de 25 del lineamiento de Detección) = **10h totales**. Sin
   instrucción del usuario de acortar horas para este cliente — se aplicó el lineamiento por
   defecto (`empresa/politicas-comerciales.md` → Dimensionamiento por servicio), a diferencia
   del ajuste puntual hecho en `hoteles-cumberland/` (DET-011, 2h/área por instrucción
   explícita del usuario, caso distinto).
3. **Modalidad presencial**, en las oficinas de Toyocentro (Quinta Crespo, Caracas) — dato
   explícito y único de la ficha, sin sedes adicionales.
4. **Sin recomendación preliminar de ninguna herramienta**: a diferencia de otras Detecciones
   de esta sesión (Gemini/Claude como contexto informal), aquí el cliente declara
   explícitamente "aún no lo saben, esperan la recomendación" (Bloque B). El Reporte Final sí
   promete una **recomendación de ecosistema de IA** como deliverable (pedido explícito del
   cliente en Bloque específico Detección), pero sin nombrar marca — 100% Metodología ABR.
5. **Nombre de la herramienta de base de datos, resuelto con el usuario (2026-09-15)**: la
   ficha nombra la herramienta de forma inconsistente — "Airtable" en el Proceso 1 (Bloque C),
   pero "Azure Table" en la expectativa del cliente (Bloque G) y en el logro inmediato (Bloque
   específico Detección). Son productos distintos. El usuario eligió **no mencionar el nombre
   específico** en el deck — se habla solo de "sus bases de datos" / "sus sistemas
   comerciales", evitando el conflicto por completo.
6. **Sin Certificado de participación INTEZIA** en Entregables ni en Programa — la Detección
   (incluida la sesión de Fundamentals) es una auditoría, no un curso. Ver memoria
   `deteccion-sin-certificado.md`.
7. **Sin slide de Mapa de Calor** (tabla ilustrativa) — mismo criterio que el resto de las
   Detecciones recientes. "Mapa de Calor" sigue como nombre del entregable de la Etapa de
   Priorización, sin slide propia.

## Necesidad detectada

Objetivo y necesidad central citado textualmente por José A. Sol, CEO: *"Quiero usar la
inteligencia artificial para buscar oportunidades dentro de mi lista de clientes existentes.
Todos los meses Toyota me asigna carros que van a llegar en seis meses; quiero que la
herramienta vaya a mis tres bases de datos y me diga: estas personas llamaron en su momento
por estos carros y no los teníamos, o son potenciales clientes porque tienen esa misma
camioneta con cuatro años de uso, para incorporarlos a la lista de contactos potenciales de
esa remesa. Básicamente lo que está buscando es potenciar a su departamento comercial, tanto
con soluciones como la operatividad del día a día hasta la creación de sus propios agentes (el
equipo de IT se encargaría de esto), tienen muchas ideas que les gustaría llevar a cabo pero
los asesoremos en la misma detección."*

**2 procesos específicos (Bloque C)**:

1. **Cruce de bases de datos comerciales** contra el inventario mensual de Toyota, para
   detectar oportunidades de venta. Frecuencia mensual. Cuello de botella: no hay forma
   automatizada de cruzar sus sistemas comerciales cuando llega inventario nuevo. Este es el
   **logro inmediato ("quick win") que el propio cliente ya trae definido**.
2. **Atención de leads por WhatsApp fuera de horario**. Frecuencia diaria. Cuello de botella:
   los leads que llegan en "horas muertas" (noche, fin de semana) se pierden o se atienden
   tarde, hasta el día siguiente o el lunes.

Ambos procesos alimentan las sesiones de Ventas y Tecnología: Ventas aporta el contexto
comercial (a quién contactar, qué oportunidad representa), Tecnología evalúa la viabilidad
técnica de construirlo puertas adentro.

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Información del negocio**: varios sistemas separados por área.
- **Comunicación y coordinación**: WhatsApp, canal principal de leads.
- **Uso de IA hoy**: ya usan IA en la operatividad diaria, aunque no todo el personal —
  solo el "más medular" lo usa de forma constante. El CEO trajo ideas concretas que ahora
  quiere materializar.
- Sin política de datos/seguridad existente. Sin regulación sectorial aplicable declarada.

## Universo y modalidad

- **~8 personas** en el alcance (6 de Ventas, 2 de Tecnología) — cifra exacta, sin ambigüedad.
- **1 sesión grupal por área** (Ventas: José A. Sol + equipo comercial; Tecnología: Christopher
  Rodríguez + 1 persona más) + Fundamentals grupal para las 8 personas juntas.
- **Modalidad**: Presencial, en las oficinas de Toyocentro (Quinta Crespo, Caracas).
- **Nivel de partida con IA**: disperso — "algunos la usan bien, otros no la usan". Sin
  formación previa en IA para nadie del equipo.
- **Presupuesto**: en evaluación. **Apertura al cambio**: Alta. **Patrocinio ejecutivo**:
  fuerte y visible (José A. Sol es el patrocinador/campeón directo).
- **Urgencia**: alta — el cliente describe que en el negocio de concesionarios "todo surge muy
  rápido" (contexto interno de venta, no se expone así de cara al cliente en el deck; se
  refleja en Diagnóstico como "el negocio de concesionarios se mueve rápido").
- **Quién decide**: José A. Sol (CEO) firma y decide; Christopher Rodríguez es el punto de
  contacto operativo que lleva la propuesta y el presupuesto para su aprobación.

## Hacia dónde va esto (contexto, no cotizado en este documento)

Bloque F (observaciones internas): *"Lo ideal es iniciar con detección aunque ya tienen
algunas ideas, debemos delimitar un poco el alcance de cada una de las soluciones y entender
bien el plan de acción para una siguiente fase de habilidades."* — una futura fase de
Habilidades queda mencionada como nota interna/pendiente, **no cotizada** en este documento,
mismo criterio que el resto de las Detecciones de esta sesión.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Flavia Martínez.

## Notas internas

- Caso base estructural: `velas-3n/` (DET-013) — mismo patrón de 4h por área, logro inmediato,
  sin recomendación preliminar de herramienta, sin certificado, sin slide de Mapa de Calor.
  Toyocentro tiene 2 áreas en vez de 4, y modalidad presencial en vez de virtual.
- Reunión muy sólida (observación de Flavia, Bloque F): el cliente llegó con casos de uso ya
  pensados y concretos (cruce de bases de datos, agente de WhatsApp), no una exploración
  genérica, y cerró diciendo explícitamente que la presentación le pareció excelente.
- Impacto (§4.9): Fullpath — The 2025 State of AI Adoption in Car Dealerships, encuesta con
  Kerrigan Advisors (43% de concesionarios ya implementa IA, 95% la cree crítica para su éxito
  futuro, 55% de quienes ya usan IA tuvo un aumento de ingresos del 10-30% en la primera mitad
  de 2025) + Strolid — Lead Response Time: Speed Matters in Automotive Lead Management (2026,
  contactar en los primeros 5 minutos da 10x más probabilidad de contacto que esperar 30 —
  dato que responde directo al dolor de los leads de WhatsApp fuera de horario). Ambos
  verificados por WebSearch.

## Pendientes (a confirmar con Flavia/el cliente antes de enviar)

- Fecha y hora exactas de las 3 sesiones (Fundamentals + 2 áreas) — no se inventan, se
  coordinan en "Cómo arrancamos".
- Presupuesto: "en evaluación" según la ficha — no afecta la estructura del programa, solo la
  cotización final que completa Ventas.
