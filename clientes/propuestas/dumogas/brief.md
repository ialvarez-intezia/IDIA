# Brief — Dumogas

---

## Datos administrativos

- **Empresa**: Dumogas (venta de gas)
- **Sector**: Ventas de gas
- **Tamaño**: Micro / Pyme (menos de 50 empleados)
- **Slug**: `dumogas`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` (Detección pura — esta propuesta no incluye Habilidades, ver
  "Decisión de alcance" abajo)
- **Tipo de documento**: Detección (`DET-017`) · Fundamentals (2h grupal) + auditoría de 7 áreas
  (Tesorería, Cuentas por pagar, Cuentas por cobrar, Caja, Recursos Humanos, Tributos, Almacén),
  4 horas por área (30h totales), modalidad virtual.
- **Eje temático**: Auditar las 7 áreas operativas de Dumogas y dejar un logro inmediato en cada
  una, empezando por llevar la conciliación diaria a tiempo real, para pasar de un uso de IA
  suelto y sin criterio a un criterio común.
- **Fecha del brief**: 2026-09-21
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Dumogas**
(`Levantamiento_Dumogas_2026-09-21.pdf`, registrada 2026-09-17), elaborada por la asesora
**Verónica Rubio**.

## Contacto

- **Asesora comercial**: Verónica Rubio.
- **Contacto operativo / logística**: Daviana, Gerente — lidera de facto las 7 áreas operativas
  bajo Finanzas, pero **no es la única decisora**.
- **Quién firma y decide la contratación**: toda la gerencia (no solo Daviana) — la ficha lo
  aclara explícitamente dos veces (Bloque F y Bloque específico Detección).
- **Servicio previo con Intezia**: ninguno — primer contacto. Sin propuesta previa sin aprobar.

## Decisión de alcance — bloqueante, confirmada por el usuario

**La ficha (Bloque F) pide explícitamente construir 2 propuestas alternativas**, cita textual:

> *"Trabajemos en este esquema hagamos 2 propuestas: 1 propuesta: Detección con fundamentals
> completo. 1 propuesta: 2 horas de detección por cada área, fundamentals prácticos compartidos
> y un extra de horas enfocada en sus procesos a cada área."*

El usuario pidió construir **solo la Propuesta 1: "Detección con fundamentals completo"** — la
versión de dimensionamiento estándar (lineamiento por defecto, 4h/área + 2h Fundamentals
grupal), **sin combinar con Habilidades**.

**La Propuesta 2 queda sin construir** (2h de detección por área + Fundamentals prácticos
compartidos + horas extra enfocadas en procesos por área — una versión más liviana y con una
extensión de tipo Habilidades embebida por área). No se construye salvo que el usuario lo pida
explícitamente más adelante; el `Bloque específico · Habilidades` de la ficha (qué debe poder
hacer el equipo, tareas reales de trabajo, modalidad preferida) queda documentado abajo como
contexto para cuando se construya, pero **no se usa en este documento**.

## Áreas de Detección (7 — dato directo de la ficha, sin ambigüedad)

Tesorería, Cuentas por pagar, Cuentas por cobrar, Caja, Recursos Humanos, Tributos, Almacén.

- **1 persona por área a entrevistar** (equipo muy pequeño: cada analista cubre procesos
  completos de su área).
- **Headcount inconsistente en la ficha, sin resolver por invención**: "Universo total de
  personas involucradas" (Bloque B) = 8 personas; "Nº de personas que recibirán la capacitación
  AI Fundamentals" (Bloque específico Detección) = 9 personas. Se usa **9** para dimensionar
  Fundamentals (cifra específica para esa sesión, la más relevante para el límite de 25/sesión),
  sin forzar una reconciliación entre ambas cifras.
- **Modalidad: Virtual** (dato explícito de la ficha, Bloque específico Detección).
- **Sin sedes distintas involucradas.**

## Dimensionamiento — Propuesta 1 ("fundamentals completo" = lineamiento por defecto)

- **4 horas por área** × 7 áreas = **28 horas**.
- **+ 2 horas de Fundamentals grupal** (9 personas, dentro del máximo de 25) = **30 horas
  totales**.
- **Con logro inmediato por sesión de área** (a diferencia de Andrómeda DET-016): el propio
  cliente pide explícitamente "automatizar la mayor cantidad de tareas repetitivas" (Bloque G) y
  ya trae un candidato de quick win concreto (conciliación diaria, Bloque C) — se sigue el
  patrón `toyocentro/` (auditoría + construcción de un logro tangible en la misma sesión de 4h),
  no el patrón `pilotes-perforados/`/`andromeda/` (auditoría pura).

## Necesidad y proceso específico (Bloque C, D)

- **Cita textual (Bloque D)**: *"Automatizar procesos claves para ir de la mano de la
  tecnología avanzada."*
- **Proceso específico — Conciliación** (candidato a logro inmediato / quick win):
  frecuencia diaria, dato confidencial, volumen "todo el día", 1 persona involucrada, cuello de
  botella: "llevarlo a tiempo real y no atrasado". Se usa como hilo conductor del Diagnóstico y
  los Objetivos, igual que el cruce de bases de datos en Toyocentro.

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: no está definido.
- **Información del negocio**: varios sistemas separados por área.
- **Comunicación**: WhatsApp.
- **Uso de IA hoy**: sistema administrativo contable llamado **Galex**, y uso suelto de
  **Gemini**, sin criterio. Nombre del sistema contable no se expone en el deck de cara al
  cliente (mismo criterio que Toyocentro con Airtable/Azure Table) — se habla de "su sistema
  administrativo" cuando haga falta.
- **Sin recomendación preliminar de ninguna herramienta**: el cliente declara "aún no lo saben,
  esperan la recomendación" — 100% Metodología ABR, igual que Toyocentro.
- **Nivel de partida con IA**: "la usan de forma suelta y sin criterio". Sin formación previa.
- **Sin diagnóstico o auditoría previa de IA.**

## Restricciones y políticas (Bloque E — usar con cautela, sin inventar certeza)

- **Política de datos/seguridad**: "sí hay, no me pudo especificar cuál" — **no se afirma en el
  deck que existe una política real y operativa**; se omite del todo en vez de asumir (§ "Omitir,
  no inventar").
- **Regulación sectorial aplicable**: "no sabe" — se omite.
- **Disponibilidad presupuestaria**: en evaluación.
- **Apertura al cambio**: Media.
- **Patrocinio ejecutivo**: **aún no asegurado** — a diferencia de otras Detecciones recientes de
  esta sesión (Andrómeda, Toyocentro), el deck **no debe asumir ni afirmar un patrocinio
  ejecutivo fuerte y visible**. Daviana lidera de facto pero la aprobación depende de "toda la
  gerencia", un público más amplio que no estuvo en la reunión de levantamiento.

## Restricción de diseño — bloqueante (Bloque F)

Cita textual: *"La aprobación depende de gerencia, no de ella sola: la propuesta debe quedar
clara para un público que no estuvo en esta llamada."* El deck se redacta en lenguaje llano,
sin dar por sentado contexto de la reunión — cada slide debe explicarse sola.

## Objetivo final esperado (Bloque G)

- **Expectativa frente a la IA**: automatizar la mayor cantidad de tareas repetitivas.
- **Hacia dónde**: profesionales que integren la IA para manejar datos en tiempo real.
- **Horizonte**: corto plazo (0-3 meses) — urgencia real, impulsada por la insistencia de
  Daviana como líder (Bloque específico Detección: "¿Hay urgencia o evento disparador?:
  Insistencia por Daviana la líder" — no un evento de negocio externo).

## Decisiones confirmadas / sin ambigüedad

1. **7 áreas de Detección**, dato directo de la ficha, mismo listado en Bloque A y en el
   Bloque específico de Detección.
2. **Solo Propuesta 1 (Detección pura, fundamentals completo)** — confirmado por el usuario.
3. **Con logro inmediato por área** (a diferencia de Andrómeda) — el cliente lo pide
   explícitamente y ya trae un candidato concreto (conciliación).
4. **Modalidad virtual** — dato explícito, a diferencia de Andrómeda (sin especificar).
5. **Sin certificado de participación INTEZIA** en Entregables — Detección es una auditoría, no
   un curso (`deteccion-sin-certificado.md`).
6. **Sin nombre del sistema administrativo (Galex)** de cara al cliente.
7. **Sin slide de Mapa de Calor** ni Metodología ABR ni Equipo facilitador expuestos (§4.10a).
8. **Sin afirmar patrocinio ejecutivo fuerte** — el deck se redacta neutral en ese punto, sin
   sobreprometer compromiso que la ficha no confirma.

## Impacto (§4.9, verificado por WebSearch 2026-09-21)

- **OCDE — AI adoption by small and medium-sized enterprises (diciembre 2025)**: entre 2020 y
  2024 la proporción de empresas que usan IA en países de la OCDE más que se duplicó (5,6% →
  14%); 17% de las pequeñas empresas y 30% de las medianas reportó usar IA en 2025; entre
  quienes ya usan IA, el 76% se clasifica como "principiante", con herramientas básicas para
  funciones aisladas — coincide directamente con el "uso suelto y sin criterio" de Dumogas.
- **McKinsey — The state of AI in early 2025 (abril 2025)**: 70% de los equipos de Finanzas y
  Estrategia reportó aumento de ingresos por IA generativa en la segunda mitad de 2024 (mismo
  dato ya verificado y usado en Andrómeda DET-016) — relevante porque la mayoría de las 7 áreas
  de Dumogas son de Finanzas (Tesorería, Cuentas por pagar/cobrar, Caja, Tributos).
- Se descartaron varias estadísticas de "ahorro de horas en conciliación bancaria" atribuidas a
  AICPA/Deloitte/MIT-Stanford encontradas en blogs de proveedores (ustechautomations.com,
  stealthagents.com, digitalapplied.com) — no se pudo verificar que esos estudios existan con
  esos datos exactos citados; se prefirió usar solo fuentes primarias confirmables (OCDE,
  McKinsey), per §4.9.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Notas internas

- Caso base estructural: `toyocentro/` (DET-014) — mismo patrón de Fundamentals + N áreas a 4h
  con logro inmediato, roadmap `.rmx-linear` de 3 etapas, Beneficios v3, Cierre escalera, precio
  estándar. Adaptado de 2 a 7 áreas y de presencial a virtual.
- **Bloque específico · Habilidades (no usado en este documento, contexto para la Propuesta 2
  futura)**: qué debe poder hacer el equipo al terminar — analizar datos, manejar datos con
  precisión en tiempo real, automatizar procesos, usar el sistema administrativo con IA (no como
  una hoja de cálculo); tareas reales: conciliación, entre otras; modalidad preferida: mixta;
  responsable interno de logística: Daviana.
