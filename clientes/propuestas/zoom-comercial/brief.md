# Brief — Zoom · Ventas y Mercadeo

---

## Datos administrativos

- **Empresa**: Zoom (área Comercial: equipos de Ventas y de Mercadeo)
- **Sector**: Servicios / corporativo
- **Slug**: `zoom-comercial`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-058`, Fase 2 Zoom) · **2 formaciones en
  una sola propuesta** (multi-track, patrón `robin-agency-cap080`): Track Ventas + Track
  Mercadeo, cada equipo ve su formación por separado.
- **Eje temático**:
  - **Track Ventas**: Prospección y cartera, mezcla de producto y factura promedio,
    Inteligencia Comercial (tendencias/proyecciones) y Sales Gems, con Gemini, Gems y
    NotebookLM.
  - **Track Mercadeo**: Inteligencia Analítica de Mercado, Copywriting persuasivo, Curaduría
    de marca y Marketing Gems, con Gemini, Gems y NotebookLM.
- **Fecha del brief**: 2026-07-28 (ampliado a 2 tracks el 2026-08-17)
- **Estado**: propuesta en formato canónico (deck HUD, clonada de `zoom-miami/`), sin slide de
  precio

## Contacto

- **Asesora de ventas**: María Iribarren — +58 414 0570056 — miribarren@intezia.com

## Necesidad detectada

El área Comercial de Zoom agrupa dos frentes con procesos manuales distintos:

- **Ventas** — 3 equipos:
  - **Cuentas Corporativas**: negociación B2B, prospección y captación de nuevos clientes,
    mantenimiento de cartera; KPI principal = cumplir metas comerciales.
  - **Cuentas al Detal**: venta por Oficinas Propias y Agentes Autorizados; debe garantizar la
    mezcla adecuada de productos para cumplir la meta y subir la factura promedio.
  - **Inteligencia Comercial**: genera reportes y estadísticas para toda la unidad (tendencias,
    predicciones, proyecciones) que alimentan la toma de decisiones estratégicas.
  - Hoy la prospección, el seguimiento de cartera, la mezcla de producto y los reportes de
    tendencias se trabajan sin apoyo de IA.
- **Mercadeo** — saturación operativa y creativa: redacción masiva de contenido, análisis
  manual de reportes de pauta (Meta Ads, Google Ads), auditoría de competencia a mano y falta
  de asistentes que resguarden la voz de marca. (Dentro del área de Mercadeo de Zoom también
  existen Productos, Inteligencia de Mercadeo, Publicidad y Comunicaciones; esta Fase 2 cubre
  el eje de analítica de pauta y contenido — no se abrieron módulos propios para esas 4
  sub-áreas por falta de alcance/tiempo definido con el cliente.)

Esta Fase 2 transforma ambos flujos en procesos asistidos por IA: Ventas prioriza prospección,
mezcla de producto y reportes de Inteligencia Comercial con Gemini y NotebookLM; Mercadeo pasa
de producir a mano a construir Marketing Gems configurados con el manual de marca de Zoom.

## Especificaciones del programa

- **Duración**: 4 horas por formación (2 sesiones × 2 horas) · 2 formaciones: Ventas y
  Mercadeo (no son fases secuenciales — se dictan a cada equipo por separado, en simultáneo o
  escalonadas).
- **Modalidad**: In-Company (sin afirmar presencial/online)
- **Audiencia**:
  - Track Ventas: Cuentas Corporativas, Cuentas al Detal e Inteligencia Comercial.
  - Track Mercadeo: equipo de Mercadeo de Zoom.
- **Stack**: Google Workspace + Gemini + Gems + NotebookLM (ambos tracks).

## Equipo asignado

- **Facilitación**: Equipo Education (genérico, sin nombres — consistente con el resto de
  la ruta Zoom cuando no hay facilitador nombrado en la ficha).

## Notas internas

- **Sin slide de Propuesta Económica**: esta Fase 2 se cotiza dentro del acuerdo marco ya
  en curso con Zoom (mismo criterio que decks "sin precio" del sistema, p. ej. `empleate/`).
  Los 8 campos AcroForm no económicos (Entregables, Acreditación, 3 Pasos × título/body)
  siguen siendo obligatorios; los 5 campos de precio no aplican (§4.14).
- **Uno de los cursos de la ruta de capacitación Zoom** (junto a `zoom-miami/` CAP-046
  bootcamp base, Legal `zoom/` CAP-029 y Operaciones). **Puntos transversales acordados
  2026-07-28 y ya aplicados en `zoom-miami/`, replicados aquí (en ambos tracks) para
  consistencia entre los cursos Zoom:**
  1. **Reto IA ZOOM**: nombre único del concurso interno de Zoom en los cursos de la ruta
     (antes cada curso usaba un nombre distinto — Demo Day, Lab de Proyectos, Mini Proyecto,
     Quiz). Cada track cierra su Módulo IV con su propia edición del Reto IA ZOOM: Track
     Ventas con roles Guardián de Cartera / Guionista de Negociación / Analista de Tendencias
     / Generador de Mezcla (slide 6); Track Mercadeo con Guardián de la Marca / Fábrica de
     Copys / Generador de Guiones / Analista de Reportes (slide 10, ya aplicado antes de
     ampliar a 2 tracks). Lanzamiento breve en la sesión 1 de cada track, cierre en su sesión 2.
  2. **Método de prompting unificado**: nombre oficial **"Prompt ejecutivo (5 partes)"**
     (ya adoptado en el bootcamp base `zoom-miami`). Ninguno de los 2 tracks enseña un método
     de prompting desde cero (asume que el equipo ya pasó por fundamentos), pero donde se
     nombra cómo se interroga a Gemini (pauta/analítica en Mercadeo, pipeline/cartera en
     Ventas) se referencia el mismo método oficial, para que ambos hablen el mismo idioma que
     el resto de la ruta Zoom.
  3. **Expectativas realistas sobre los Gems**: evitar lenguaje que sugiera autonomía. Un
     Gem es una configuración guardada que asiste, no reemplaza al equipo (Ventas o
     Mercadeo). Reforzado en Perfil de egreso (slide 12, compartido) y en la estrategia de
     enseñanza de la sesión de Gems de cada track (slide 6 Ventas / slide 10 Mercadeo).
  4. **Medición de tiempo ahorrado (antes/después, 30 días)**: línea base al inicio (Paso 03
     de "Cómo arrancamos") + medición a los 30 días de la misma tarea con Gemini, en ambos
     tracks. Alimenta el reporte a dirección y el Reto IA ZOOM. Mencionado en Beneficios
     (slide 12) e incluido como entregable en `acroforms.json`.
- **Ampliación a 2 tracks (2026-08-17)**: el deck original solo cubría Mercadeo; se agregó el
  Track Ventas completo (objetivos, programa de 4 módulos y 2 sesiones, igual estructura que
  Mercadeo) porque el área Comercial de Zoom incluye Ventas (Cuentas Corporativas, Cuentas al
  Detal, Inteligencia Comercial) además de Mercadeo. Patrón multi-track tomado de
  `robin-agency-cap080/` — ver `programa.md` §5 para el detalle curricular de ambos tracks.
- Slug `zoom-comercial` distinto de `zoom-miami/` (bootcamp base) y de `zoom/` (Legal,
  CAP-029): mismo cliente, cursos independientes.
