# Documento de Diseño del Servicio — Detección + Habilidades

**[LOGO INTEZIA — `logos/educacion/NEGRO.png`]**

# Detección + Nivelación en Claude para Bidzi
## Auditoría de 12 áreas + Capacitación in-company (Fase 2)

**Código**: CAI-011
**Servicio (Modelo Intezia)**: Detección + Habilidades (combo) · `empresa/tipos-de-documento.md §0`
**Elaborado por**: Coordinación INTEZIA · Dirección de Productos y Servicios
**Fecha de elaboración**: 2026-09-04 (revisado 2026-09-04)
**Fuente**: Ficha de Levantamiento Intezia — Bidzi (2026-09-04, Verónica Rubio) + precisiones
directas del usuario (alcance de Detección, estructura de Habilidades por pistas)

---

## 1. Información general

- **Servicio**: Detección (Fase 1) + Habilidades (Fase 2) — combo, servicio de entrada
  Detección. Ver `brief.md` para la nota sobre código (`CAI-011`, mantenido) vs. servicio
  (`deteccion`).
- **Cliente**: Bidzi — institución financiera pequeña, 12 áreas en total (Operaciones,
  Tecnología, Finanzas, Legal, Recursos Humanos, Contabilidad, Marketing, Ventas, y 4 más
  no nombradas todavía).
- **Perfil de ingreso**: sin perfil de ingreso (Capacitación, no Taller) en la Fase 2 — todo
  el conocimiento actual del equipo es empírico, sin formación previa en IA.
- **Modalidad**: Virtual en ambas fases (confirmada por el cliente).
- **Duración**: Fase 1 (Detección) — Kick-off + 3 etapas. Fase 2 (Habilidades) — 3 módulos ×
  2h = 6h en total.
- **Contexto regulatorio**: institución financiera con política de datos/seguridad existente y
  regulación sectorial aplicable — el manejo seguro de datos confidenciales es un tema propio
  del programa, no una mención genérica.

---

## 2. Planteamiento de la necesidad

Bidzi ya tiene personas usando Claude por su cuenta, pero de forma suelta y sin criterio
compartido entre sus 12 áreas. Hoy solo se conoce en detalle un proceso: administrativo, de
onboarding y de facturación (manual, diario, dato confidencial). Las otras 11 áreas de la
empresa no se han auditado todavía — asumir que el problema termina en el proceso ya
mencionado sería construir la propuesta sobre un techo artificial, no sobre datos reales. La
Fase 1 (Detección) resuelve ese vacío con entrevistas cortas por área y un Mapa de Calor de
oportunidades; la Fase 2 (Habilidades) nivela al equipo en Claude con un tronco común y una
pista ya identificada, dejando trazada la ruta para sumar más pistas según lo que arroje la
Detección.

---

## 3. Objetivos

### 3.1 Objetivo general

Auditar las 12 áreas de Bidzi para identificar dónde Claude genera más valor, y nivelar al
equipo con un programa de Habilidades que combine fundamentos comunes con pistas
especializadas por área, empezando por la ya identificada en procesos administrativos,
onboarding y facturación.

### 3.2 Objetivos específicos

1. Diagnosticar los procesos reales de las 12 áreas de Bidzi, no solo los mencionados de
   pasada, con entrevistas cortas por área.
2. Priorizar las áreas con mayor oportunidad de automatización con Claude, en un Mapa de
   Calor.
3. Dominar los fundamentos de Claude y el manejo seguro de datos confidenciales, requisito
   real de una institución financiera regulada.
4. Construir una pista de Habilidades especializada para administrativo, onboarding y
   facturación, y dejar trazada la ruta para las demás áreas según los hallazgos de la
   Detección.

---

## 4. Fase 1 · Detección — estructura (Kick-off + 3 etapas)

| Etapa | Título | Qué pasa | Entrega |
|---|---|---|---|
| Kick-off | Alineación de alcance | Reunión de arranque para confirmar el orden de las 12 entrevistas por área | Plan de entrevistas |
| 1 | Kick-off y entrevistas | Entrevistas cortas (45–60 min) con un referente de cada una de las 12 áreas | Inventario real de procesos y cuellos de botella por área |
| 2 | Priorización | Se prioriza cada proceso real por impacto, esfuerzo y riesgo, área por área | Mapa de Calor de las 12 áreas |
| 3 | Reporte Final | Se entrega el diagnóstico completo y se recomiendan las pistas de Habilidades por área prioritaria | Reporte Final + recomendación de pistas para la Fase 2 |

> **Sin datos inventados**: el Mapa de Calor se presenta como el entregable que la Detección
> va a producir, no como una tabla ya llena — no hay información real de 11 de las 12 áreas
> todavía. Distinto del patrón de `pilotes-perforados/`, donde sí existía información real de
> 4 áreas antes de la propuesta.

---

## 5. Fase 2 · Habilidades — estructura modular (3 módulos / 6h)

| Módulo | Título | Temas | Duración |
|---|---|---|---|
| I | Fundamentos de Claude y uso seguro (tronco común) | Qué es Claude y cómo funciona · Anatomía de un buen prompt · Manejo seguro de datos confidenciales · Primeros resultados con casos reales | 2h |
| II | Pista: Administración, Onboarding y Facturación | Qué es un Project · Contexto real de onboarding y facturación · Consultas con contexto propio · Reportes y análisis asistidos | 2h |
| III | Skills, Artifacts y pistas adicionales | Qué son Skills y Artifacts · Automatiza una tarea real · Criterio de uso responsable · Plan de pistas adicionales por área | 2h |

> El Módulo II es la única pista con contenido real hoy. Pistas adicionales para otras áreas
> (contenido, cantidad de sesiones) se definen tras el Reporte Final de la Fase 1 — no se
> inventan procesos de áreas no auditadas.

---

## 6. Desglose instructivo (Fase 2, una sesión por módulo)

- **Sesión 1 (Módulo I)**: 30' conceptos clave, 30' demostración guiada, 45' práctica con
  casos reales de Bidzi, 15' cierre y dudas.
- **Sesión 2 (Módulo II)**: 30' demostración, 60' construcción guiada sobre el proceso de
  administración/onboarding/facturación, 30' prueba e iteración.
- **Sesión 3 (Módulo III)**: 40' automatización guiada de una tarea real, 50' Skills y
  Artifacts, 30' cierre y plan de pistas adicionales.

---

## 7. Entregables

**Entregables de la Detección:**
- Mapa de Calor de las 12 áreas de Bidzi.
- Reporte Final + recomendación de pistas para Habilidades.

**Entregables de la capacitación (Fase 2):**
- Workbook digital.
- Casos reales de Bidzi resueltos en sesión.
- Certificado de participación INTEZIA.

**Valor inmediato:**
- Inventario de procesos de las 12 áreas, priorizado por impacto, esfuerzo y riesgo.
- Al menos un Project armado con información real de Administración/Onboarding/Facturación.
- Una herramienta propia (Skill o Artifact) lista para usar en el día a día.

---

## 8. Restricciones y notas

- **No se inventan procesos de las 11 áreas no auditadas** — quedan explícitas como "a
  definir" en el roadmap de Detección y en el Módulo III de Habilidades.
- No se menciona el entorno Microsoft 365 del cliente en el deck: Claude ya es la herramienta
  que usan informalmente y el pedido explícito del usuario fue mantenerla como eje (§4.11 no
  aplica: no se afirma ningún cambio de stack).
- No se menciona presupuesto ni condiciones de pago (§4.15) — vigencia 30 días + T&C. Fase 1
  y Fase 2 se cotizan ambas ahora (pedido explícito del cliente de algo concreto); solo las
  pistas adicionales de Habilidades quedan diferidas.
- Sin nombres propios de personas (Alejandro no está en el contenido) — el documento se refiere
  a "Bidzi" o "las 12 áreas de Bidzi".
- La ventana de diciembre (preferencia del cliente por bajo volumen operativo) queda como nota
  interna de logística (`Notas`), no como fecha comprometida en el cuerpo del deck.
- "Skill", "Project" y "Artifact" se mantienen en inglés (términos nativos de Claude),
  explicados en su primera aparición en cada slide donde aparecen (§4.12).
