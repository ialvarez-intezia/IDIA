# Brief — Zoom Operaciones

---

## Datos administrativos

- **Empresa**: Zoom (equipo de Operaciones)
- **Sector**: Servicios / corporativo
- **Slug**: `zoom-operaciones`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-059`, Fase 2 Zoom)
- **Eje temático**: Inteligencia Operativa — criterio IA, prompting estratégico, KPIs y
  Asistentes Operativos (Gems), con Gemini y uso responsable de datos
- **Fecha del brief**: 2026-07-28
- **Estado**: propuesta en formato canónico (deck HUD, clonada de `zoom-comercial/`), sin
  slide de precio

## Contacto

- **Asesora de ventas**: María Iribarren — +58 414 0570056 — miribarren@intezia.com

## Necesidad detectada

El equipo de Operaciones de Zoom ejecuta a diario un alto volumen de tareas repetibles:
seguimiento de servicios, reportes operativos, coordinación con clientes y manejo de
incidencias, sin un criterio común para decidir qué automatizar ni protocolos de uso
responsable sobre los datos que maneja. Esta Fase 2 transforma ese flujo en procesos
asistidos por IA: desde el cálculo de KPIs hasta un Asistente Operativo (Gem) entrenado con
los procesos de Zoom.

## Especificaciones del programa

- **Duración**: 4 horas (2 sesiones × 2 horas)
- **Modalidad**: In-Company (sin afirmar presencial/online)
- **Audiencia**: equipo de Operaciones de Zoom.
- **Stack**: Google Workspace + Gemini + Gems. **Una sola herramienta de IA** (ver Notas
  internas — corrección de fondo respecto a la versión anterior de esta propuesta).

## Equipo asignado

- **Facilitación**: Equipo Education (genérico, sin nombres — consistente con el resto de
  la ruta Zoom cuando no hay facilitador nombrado en la ficha).

## Notas internas

- **Corrección 2026-07-28 — de dos herramientas a una sola**: la versión previa de esta
  propuesta configuraba "Asistentes Operativos (Gems o GPTs)" y listaba "Gemini Gems ·
  ChatGPT GPTs" en Recursos y entornos. El estándar de Intezia con Zoom (y de toda la ruta
  Zoom) es **Google/Gemini únicamente**; mezclar ChatGPT confunde al equipo y puede implicar
  una licencia adicional no contemplada. Se eliminó **toda** referencia a GPT/ChatGPT del
  deck: objetivos, programa, cronograma, perfil de egreso y recursos. El programa configura
  **Gems (Gemini) exclusivamente**.
- **Corrección 2026-07-28 — menos temas para las 4 horas disponibles**: la versión previa
  cubría 16 subtemas en 4 módulos (misma señal de sobrecarga que RRHH, aquí más leve). Se
  priorizó lo esencial: **12 subtemas** (3 por módulo), fusionando ítems redundantes
  ("Detección de brechas" y "Mapeo de energy drainers" se absorben en el Semáforo de
  Decisión IA y su estrategia de enseñanza) y recortando el módulo IV a un catálogo de
  **hasta 2** asistentes complementarios por subárea (antes 4), más realista para el tiempo
  disponible.
- **Uso responsable de la IA — mismo criterio que `zoom-miami/`**: se incorporó un tema
  dedicado (1.3 Uso responsable y protección de datos) dentro del Módulo I, más un refuerzo
  explícito al cargar el contexto de Zoom en el Gem (Módulo III): qué información de
  clientes e incidencias es sensible y no debe cargarse sin anonimizar. Reflejado también en
  el diagnóstico (punto 02) y en Perfil de egreso · Saber ser.
- **"energy drainers" (anglicismo) eliminado** (§4.4): el concepto se absorbe en el mapeo por
  impacto sin nombrarlo en inglés.
- **Uno de los cursos de la ruta de capacitación Zoom** (junto a `zoom-miami/` CAP-046
  bootcamp base, `zoom/` CAP-029 Legal y `zoom-comercial/` CAP-058 Mercadeo). **Puntos
  transversales acordados 2026-07-28, documentados en `zoom-miami/brief.md` y ya aplicados
  en `zoom-comercial/`, replicados aquí:**
  1. **Reto IA ZOOM**: nombre único del concurso interno de Zoom en los cursos de la ruta.
     Este curso llamaba a su reto final **"Demo Day"**; renombrado a **Reto IA ZOOM** en el
     módulo IV, la sesión 2 (cierre) y el chip de cronograma.
  2. **Método de prompting unificado**: la versión previa llamaba a su método **"Prompting
     ROACF (Rol, Objetivo, Audiencia, Contexto, Formato)"** — el mismo acuerdo del
     2026-07-28 identificó esto como uno de los dos nombres a unificar. Renombrado a
     **"Prompt ejecutivo (5 partes)"** (nombre oficial ya adoptado en `zoom-miami/` y
     `zoom-comercial/`), mismo contenido de fondo.
  3. **Expectativas realistas sobre los Gems**: la versión previa describía el Asistente
     Operativo como **"un empleado digital"** en el Objetivo general — lenguaje de autonomía
     prohibido por el acuerdo. Corregido a "un Gem entrenado con los procesos de Zoom que
     asiste sin sustituir el criterio del equipo", reforzado en Perfil de egreso (Saber ser)
     y en la estrategia de enseñanza del Módulo III.
  4. **Medición de tiempo ahorrado (antes/después, 30 días)**: línea base al inicio (Paso 03
     de "Cómo arrancamos") + medición a los 30 días de la misma tarea con Gemini. Alimenta
     el reporte a dirección y el Reto IA ZOOM. Mencionado en Beneficios e incluido como
     entregable en `acroforms.json`.
- **Sin slide de Propuesta Económica**: esta Fase 2 se cotiza dentro del acuerdo marco ya en
  curso con Zoom (mismo criterio que `zoom-comercial/`). Los 8 campos AcroForm no económicos
  siguen siendo obligatorios; los 5 campos de precio no aplican (§4.14).
- Slug `zoom-operaciones` distinto de `zoom-miami/`, `zoom-comercial/` y `zoom/` (Legal,
  CAP-029): mismo cliente, cursos independientes.
- **Bug de plantilla compartida descubierto (no introducido por este deck)**: en
  `.s-benefits .grid` (slide 8, `_base/styles.css`), la fila de 4 bloques tiene
  `height: 280px` fijo y cada `.block` no tiene `overflow: hidden`. Si el contenido de
  cualquier bloque (Perfil de egreso, Beneficio, Entregables o Acreditación) excede esa
  altura, el texto se derrama **fuera de su propio borde** y se solapa con la etiqueta
  "EQUIPO FACILITADOR" de la sección negra de abajo — sin que `verificar-overflow.js` lo
  detecte (el bloque en sí no excede los límites de la slide, solo su propio contenedor
  interno). **Confirmado que el mismo defecto ya está en el PDF entregado de
  `zoom-comercial/` CAP-058** (enviado 2026-07-28), así que es un problema de plantilla, no
  de este curso. Aquí se resolvió acortando "Beneficio del programa formativo" y "Perfil de
  egreso" (Saber ser en particular) hasta caber en 280px. **Pendiente**: decidir si se ajusta
  `_base/styles.css` (subir el `height` del `.grid` o poner `overflow:hidden` +
  `font-size` ligeramente menor) y si se re-emite el PDF de `zoom-comercial/` ya enviado.
