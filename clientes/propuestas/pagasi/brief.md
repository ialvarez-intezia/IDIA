# Brief — Pagasi · Auditoría de Procesos con IA (CAP-112)

## Datos administrativos

- **Cliente**: Pagasi
- **Sector**: Financiera de motos (crédito y cobranza)
- **Slug**: `pagasi`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-112`)
- **Programa**: Auditoría de Procesos y Oportunidades de Automatización con IA — Fase 1
- **Eje temático**: análisis de procesos de Ventas, Cobranzas y RR.HH. de Pagasi para identificar oportunidades de automatización con IA que sostengan el ritmo de crecimiento de la cartera.
- **Modalidad**: a definir
- **Duración**: sesiones de 2 horas por área (Ventas, Cobranzas, RR.HH.); cantidad total de sesiones por área a confirmar según alcance.
- **Fecha del brief**: 2026-08-21
- **Estado**: `Enviada` (fecha de entrega 2026-08-21, estampada por `generar-pdf.sh`)

## Contacto

- **Persona/empresa contacto en Pagasi**: sin datos por el momento (omitido, no se coloca placeholder).
- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com

## Contexto del cliente

Pagasi es una financiera de motos en crecimiento acelerado: pasó de 0 a más de 430 motos financiadas en 4 meses. Su modelo de negocio combina 45% de enganche con pagos quincenales. El equipo es de 8 a 10 personas y el riesgo de la cartera hoy es bajo (6 clientes críticos, 1 con más de 60 días de atraso).

**Tecnología actual**: CRM de ventas Kommo (3 a 4 usuarios, subutilizado por falta de capacitación) y una plataforma interna propia construida por los socios de Pagasi. Este stack es contexto interno para diseñar la propuesta, no una afirmación de cara al cliente en el deck (CLAUDE.md §4.11).

## El reto

- La cobranza se gestiona manualmente entre dos personas, lo que genera errores (por ejemplo, recordatorios enviados a números de WhatsApp desactualizados).
- **Cuello de botella principal**: cuando un cliente en mora hace un compromiso de pago, el sistema interno de Pagasi lo sigue marcando "en mora". Los recordatorios automatizados (vía Gemini) le llegan igual, así que el equipo tiene que excluirlo manualmente uno por uno, algo que ya no escala conforme crece la cartera.
- **Fricción entre departamentos**: Ventas ofrece condiciones de pago no estándar (por ejemplo mensual en vez de quincenal), lo que complica el seguimiento de Cobranzas.
- Pagasi no tiene un departamento formal de RR.HH., lo que dificulta contratar al ritmo del crecimiento actual.

## Alcance de esta propuesta

El proyecto completo que se conversó con el cliente tiene dos frentes: automatizar los recordatorios de Cobranzas y auditar los procesos de Ventas, Cobranzas y RR.HH. **Esta propuesta cubre únicamente la auditoría de procesos**, presentada como la **Fase 1** del proyecto (no como "Fase 2"): es la fase única que se ofrece por el momento, sin exponer al cliente una fase previa que no está incluida aquí.

- **Fase 1 — Auditoría de procesos**: sesiones de 2h por área (Ventas, Cobranzas, RR.HH.) para mapear cómo trabaja cada una hoy y priorizar oportunidades de automatización con IA.
- **Entregable**: un dashboard para medir el ROI del proyecto (antes, durante y después), incluido en esta fase como parte de los entregables (campo `Entregables` del AcroForm y beneficio del programa en el deck).
- La automatización de Cobranzas (integración con el sistema interno, reconocimiento de compromisos de pago activos) queda fuera del alcance de esta propuesta; es candidata natural de una fase posterior una vez cerrada la auditoría.

## Especificaciones del programa

- **Duración**: 3 áreas × sesiones de 2h c/u; cantidad total de sesiones por área a confirmar según alcance.
- **Modalidad**: a definir.
- **Audiencia**: equipo de Pagasi por área — Ventas (equipo comercial), Cobranzas (las 2 personas a cargo), RR.HH./socios (contratación y estructura del equipo).
- **Fechas tentativas**: sin definir.
- **Facilitador**: no se asigna en la propuesta inicial — INTEZIA designa un consultor senior al confirmar el kick-off.

## Propuesta económica

- Campos de precio vacíos para que ventas los complete en Adobe Reader.
- Vigencia de la cotización: 30 días (estándar `.cot-terms-box`).

## Notas internas (NO van al deck ni al cliente)

- El usuario (Verónica, vía Ivana) pidió explícitamente no exponer esta propuesta como "Fase 2" del proyecto completo, sino renumerarla como la Fase 1 (única fase ofrecida por ahora), para no mencionar una fase de cobranza que no está incluida en este documento.
- Sin datos de contacto directo en Pagasi todavía: se omite el campo en vez de usar un placeholder ("a confirmar"), según preferencia registrada del sistema (`omitir-no-inventar-placeholder`).
- Sin fechas, modalidad ni número de sesiones por área definidos: quedan explícitamente abiertos en el deck y en `Notas`/`Programa` del AcroForm para que ventas los cierre con el cliente.
- La auditoría por área (slides 5-7 y sección 5 de `programa.md`) se redactó en términos genéricos ("mapear procesos", "identificar oportunidades") sin nombrar hallazgos puntuales por departamento: en teoría no se conocen los procesos exactos hasta hacer la auditoría. Por el mismo pedido, se quitó toda mención al CRM Kommo por nombre propio en el deck y en `programa.md` (queda solo como dato interno en "Tecnología actual" de este brief); el punto 5 del diagnóstico ahora dice "las herramientas de Ventas" en vez de nombrar la herramienta.

## Pendientes

- Confirmar contacto/cargo de referencia en Pagasi.
- Confirmar modalidad (presencial / online / híbrido) y, si aplica, ciudad/país.
- Confirmar cantidad de sesiones por área y fechas tentativas.
- Confirmar número de participantes por sesión.
- Confirmar presupuesto indicativo.
