# Documento de Diseño del Servicio — Detección + Habilidades

**[LOGO INTEZIA — `logos/educacion/NEGRO.png`]**

# Servicio de Detección + Habilidades
## Mantenimiento e Infraestructura de DHL

**Código**: DET-004
**Servicio (Modelo Intezia)**: Detección + Habilidades, combo · `empresa/tipos-de-documento.md §0`
(combo parcial de 2 servicios cotizados juntos = `servicio: deteccion`, §4.1a punto 1)
**Elaborado por**: Coordinación INTEZIA · Dirección de Productos y Servicios
**Fecha de elaboración**: 2026-09-04 (ajuste de la versión anterior, 2026-09-03)
**Fuente**: Ficha de Levantamiento Intezia — DHL (2026-09-20, Verónica Rubio), con el Bloque
específico de Habilidades ya lleno + precisiones directas del usuario

> Nota: al combinar Detección y Habilidades, este documento no sigue la plantilla cerrada de
> curso/taller (perfil de ingreso, sistema de evaluación) — documenta alcance, etapas y
> entregables de ambas fases para uso interno.

---

## 1. Información general

- **Servicio**: Detección (marco propio IADD · Iniciación · Auditoría · Diagnóstico · Diseño)
  + Habilidades (dividida en 2 fases), las 3 cotizadas en el mismo documento
- **Cliente**: DHL, división Express (Logística y envíos · Mediana, 50-250 empleados)
- **Área foco**: Mantenimiento e Infraestructura
- **Modalidad**: Virtual, con equipo distribuido a nivel nacional en México
- **Entorno tecnológico del cliente**: Microsoft 365, con Copilot ya en uso de forma básica
  (insuficiente para automatización avanzada: agentes, análisis de datos). Ajuste 2026-09-04:
  se suaviza el foco exclusivo en Copilot y se nombra a Claude como herramienta a evaluar
  también, según el proceso — la Detección decide cuál conviene en cada caso.
- **Estructura comercial**: Fase 1 (Detección + Nivelación, un solo bloque) + Fase 2
  (Habilidades I: automatización y datos, 2 sesiones de 2h) + Fase 3 (Habilidades II:
  dashboards y más procesos, 2 sesiones de 2h) — las 3 cotizadas ya en el mismo documento

---

## 2. Planteamiento de la necesidad

El proceso de tickets de mantenimiento de DHL nace en un sistema de gestión (SaaS) que
levanta el ticket; la mesa de Infraestructura lo procesa, analiza costos, gestiona
proveedores y genera la compra. El análisis y seguimiento de todo ese flujo se lleva hoy en
**Excel manual**, lo que genera errores, pérdida de tiempo y un proceso poco profesional
para una función crítica (incluida la generación de órdenes de compra). El equipo (25-35
años) tiene conocimientos básicos de IA y ya usa Copilot, pero de forma básica, sin
capacidad de automatizar procesos ni de análisis de datos. Antes de invertir en
automatización, la Detección define qué cuello de botella pesa más y si conviene
resolverlo con Copilot, con Claude, o con ambos, según el proceso.

---

## 3. Objetivos

### 3.1 Objetivo general

Diagnosticar los procesos de Mantenimiento e Infraestructura de DHL para identificar y
priorizar sus cuellos de botella, y entregar una hoja de ruta clara de qué resolver con IA y
con qué herramienta: Copilot, dentro del entorno Microsoft 365 que la empresa ya usa, o
Claude, según convenga a cada proceso.

### 3.2 Objetivos específicos

1. Auditar el proceso de tickets de mantenimiento (desde su generación hasta la orden de
   compra) con un guion estructurado, e identificar logros inmediatos (quick wins)
   aplicables desde la primera sesión.
2. Medir el punto de partida con la Matriz de Madurez Digital y priorizar las oportunidades
   por impacto y esfuerzo.
3. Nivelar al equipo en el uso de Copilot dentro de su entorno Microsoft 365, en paralelo al
   diagnóstico.
4. Entregar un Reporte Final con la hoja de ruta priorizada y capacitar al equipo, en Fase 2
   y Fase 3, para que aplique esas prioridades con la herramienta más adecuada para cada
   proceso, pasando de la ejecución técnica pura a roles más estratégicos y tácticos.

---

## 4. Etapas del servicio (3 fases)

**Fase 1 · Detección + Nivelación, en un solo bloque**

| Etapa | Qué se hace | Qué se entrega |
|---|---|---|
| **Kick-off** | Sesión de 30-60 min: se presenta la ruta y se agendan fechas y logística virtual. | Ruta confirmada. |
| **Auditoría del proceso** | Sesiones virtuales con el equipo de Mantenimiento e Infraestructura siguiendo un guion estructurado; identificación de quick wins. | Levantamiento validado del proceso de tickets y compras. |
| **Diagnóstico y clasificación** | Matriz de Madurez Digital + priorización de oportunidades por impacto y esfuerzo, incluida qué herramienta (Copilot o Claude) conviene por proceso. | Índice de madurez, mapa de oportunidades priorizado. |
| **Nivelación de Copilot** (en paralelo) | Formación en Copilot dentro del entorno Microsoft: prompts efectivos, cómo instruir a la IA, resultados rápidos. | Equipo con base más sólida en Copilot; manual de prompts y workbooks. |
| **Reporte Final y roadmap** | Consolidación del diagnóstico y hoja de ruta priorizada, con el camino hacia Fase 2 y Fase 3. | Reporte Final; alcance de Fase 2 y Fase 3 confirmado. |

**Fase 2 · Habilidades I — Automatización y datos (2 sesiones de 2h, 4h)** — contenido ya
definido en la Ficha de Levantamiento:

| Sesión | Tema | Qué se entrega |
|---|---|---|
| 1 | Automatización de órdenes de compra por gasto/estación | Flujo de generación de órdenes de compra automatizado, partiendo de Copilot. |
| 2 | Análisis de datos del sistema de gestión de mantenimiento | Patrones y prioridades identificados sobre datos reales. |

**Fase 3 · Habilidades II — Dashboards y más procesos (2 sesiones de 2h, 4h)** — ajuste
2026-09-04, agrega alcance abierto a los 2 temas ya conocidos:

| Sesión | Tema | Qué se entrega |
|---|---|---|
| 1 | Dashboards de mantenimiento | Dashboard construido y esquema de actualización. |
| 2 | Seguimiento y KPIs + procesos adicionales a definir | Esquema de seguimiento con Indicadores Clave de Desempeño (KPIs) propio del equipo, y ruta para capacitar otros procesos de Mantenimiento e Infraestructura que la Fase 1 identifique (con Copilot o Claude, según el proceso) — sin inventar esos procesos, quedan a definir tras la auditoría. |

---

## 5. Entregables al cliente

**Entregables (las 3 fases):**
- Reporte Final del diagnóstico (hoja de ruta priorizada, herramienta por proceso).
- Matriz de Madurez Digital del área y mapa de oportunidades.
- Automatización de compras y dashboards de mantenimiento, con Copilot o Claude.
- Certificado de participación INTEZIA.

**Valor inmediato (quick wins):**
- Manual de prompts para Copilot y Claude.
- Workbooks aplicables por el equipo.
- Esquema de seguimiento con KPIs, definido con el equipo.
- Logros inmediatos aplicados desde las primeras sesiones de diagnóstico.

---

## 6. Restricciones (bloqueantes)

- Copilot es la herramienta que el equipo ya usa dentro de su entorno M365. Ajuste
  2026-09-04: se nombra a Claude como herramienta a evaluar también, según el proceso —
  decisión explícita del usuario tras conversar con el cliente, no inferida por el sistema.
- §4.11: no se afirma que DHL migra o adopta un nuevo stack; ni Copilot ni Claude se
  presentan como reemplazo del entorno actual, sino como opciones evaluadas por proceso.
- No se expone el nombre del interlocutor (Miguel) ni el nombre del sistema de gestión de
  mantenimiento (SaaS) en el deck de cara al cliente.
- Sin nombrar un quick win específico de Fase 1 (la ficha no registró uno) — se mantiene
  genérico. Los 4 temas de Habilidades (repartidos en Fase 2 y Fase 3) sí son concretos
  (ficha 2026-09-20); los procesos adicionales de Fase 3 quedan explícitamente sin inventar.
