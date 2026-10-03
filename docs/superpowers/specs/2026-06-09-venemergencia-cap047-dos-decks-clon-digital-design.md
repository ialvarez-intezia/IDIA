# Diseño · Venemergencia CAP-047 · Dos decks (Fase 1 práctica + Fases 1+2 con Clon Digital)

**Fecha:** 2026-06-09
**Cliente:** Venemergencia (servicios de emergencia, Venezuela) · División Educación · alianza Intezia
**Programa base:** CAP-047 · Adopción de Claude en cascada
**Tipo:** Capacitación in-company · modificación mayor de propuesta existente (§6.A)

---

## 1. Objetivo

Convertir la propuesta CAP-047 (hoy un solo deck de 16 slides, clon de `cumbre-andina`) en **dos
propuestas que conviven en la misma carpeta** `clientes/propuestas/venemergencia/`:

- **Deck A — Fase 1 práctica:** una Fase 1 reescrita para que sea "todo práctico" y el participante
  salga con **procesos automatizados desde la primera fase**.
- **Deck B — Fases 1+2:** la misma Fase 1 + una **Fase 2 nueva de inmersión técnica en Claude Code**
  donde cada gerente/director construye su **clon digital** (un agente "segundo cerebro" que le ayuda
  a decidir mejor y le automatiza trabajo en varias áreas).

El propósito comercial es **mostrar el máximo valor**: el deck A es la oferta de entrada y el deck B es
la versión ampliada que abre el upsell al proyecto estrella (el clon digital).

## 2. Decisiones lockeadas (preguntas resueltas con el usuario)

| Fork | Decisión |
|---|---|
| Narrativa | **Cascada como porqué, sin F3.** La cascada/multiplicador justifica empezar por gerencia, pero se retira la Fase 3 (réplica masiva) del relato. Foco total en F1 y F2. |
| Tamaño Fase 1 | **5 módulos / 10 h** (5 sesiones de 2 h, mismo tamaño que hoy). Se sustituye contenido por temario práctico; no se agranda. |
| Fase 2 (clon digital) | **Inmersión técnica con Claude Code completo (incluye terminal/IDE).** Tamaño: **6 sesiones / 12 h.** |
| Códigos | **Mismo CAP-047, dos alcances.** Deck A = `CAP-047`; Deck B = `CAP-047 · Fases 1+2`. |

Matices aprobados por defecto (el usuario aprobó el diseño tal cual):
- Fase 1 **pierde el módulo dedicado "Modelo cascada"**; la cascada vive solo como narrativa.
- Fase 2 = **6 sesiones / 12 h** (total deck B = 11 sesiones / 22 h).
- Deck A **incluye teaser de Fase 2** (slide de plan + roadmap) para empujar el upsell.

## 3. Arquitectura de archivos

Dos HTML independientes en la misma carpeta (sin sub-subcarpetas, §6). Se descartó el HTML único con
toggle (renumerar contadores en print es frágil) y un sistema de includes (el repo no tiene templating).

| | Deck A · Fase 1 | Deck B · Fases 1 + 2 |
|---|---|---|
| Archivo | `index.html` (canónico) | `index-completo.html` |
| Código portada (`span.codigo`) | `CAP-047` | `CAP-047 · Fases 1+2` |
| PDF resultante | `CAP-047 Adopción de Claude en cascada.pdf` | `CAP-047 · Fases 1+2 …​.pdf` (nombre distinto, sin colisión) |
| Customize | `customize-venemergencia.py` (se actualiza el existente) | `customize-venemergencia-completo.py` (nuevo) |
| Generación | `./scripts/generar-pdf.sh venemergencia` | `./scripts/generar-pdf.sh venemergencia index-completo.html` |
| CSS | `../_base/styles.css` + `overrides.css` (compartido) | igual; lo propio de Fase 2 se añade a `overrides.css` |

**Duplicación asumida:** los 5 slides de Fase 1 viven en ambos HTML. Es deliberado: la Fase 1 es estable
y la robustez de generación a tamaño-fijo pesa más que el DRY. Se construye Fase 1 en deck A y se deriva
deck B clonando esos slides + añadiendo Fase 2.

### 3.1 Cambio estructural requerido (§8 — confirmado con el usuario en el diseño)

Generalizar `scripts/generar-pdf.sh` para aceptar un 2º argumento opcional con el nombre del HTML:

```
./scripts/generar-pdf.sh <slug> [archivo.html]   # default: index.html
```

Cambio **aditivo y retrocompatible**: si se omite el 2º arg, comportamiento idéntico al actual (cero
regresión para los ~40 decks existentes). Internamente: `HTML="$DIR/${2:-index.html}"`. El nombre del
PDF se sigue derivando de `span.codigo` + `h1` de la portada, así que cada deck produce su propio PDF.

## 4. Deck A — Fase 1 práctica (5 módulos / 10 h)

Cada sesión deja un **artefacto**. La cascada/multiplicador es solo narrativa (portada, diagnóstico,
objetivos, pilar de metodología, cierre): pierde el módulo dedicado.

| # | Módulo | Capacidades (nombres nativos §4.4) | Entregable de la sesión |
|---|---|---|---|
| I | Fundamentos + prompting efectivo | Qué es/no es Claude, anatomía del prompt, contexto/roles, iteración | Caso real resuelto con prompting estructurado |
| II | Ecosistema de trabajo + Claude Design | Projects, Artifacts, análisis de documentos, Claude Design | Un entregable visual real de su área |
| III | Cowork + Skills | Crear una Skill reutilizable, automatizar una tarea en Cowork | Skill funcional propia |
| IV | Conectores, Plugins e integraciones | Conectores, Plugins, MCP (glosar §4.12), toque de Claude Code *dentro de la app* | 1 proceso automatizado conectado a una herramienta que ya usan |
| V | Seguridad e información sensible | Protocolos reales de Anthropic, qué compartir/qué no, criterio de uso seguro | Criterio de uso seguro del equipo |

**Entregable Fase 1 (reforzado):** cada participante sale con **≥1 Skill funcional + ≥1 proceso
automatizado (conector/plugin) + un caso real de su área**.

**Claude Code en Fase 1:** solo "toque" desde la app de Claude (sin terminal ni VS Code). La inmersión
técnica se reserva para la Fase 2 (deck B).

**Lista de slides deck A (16):**
1. Portada · 2. Diagnóstico · 3. Objetivos · 4. El plan (Fase 1 + teaser Fase 2) ·
5. Roadmap simplificado (F1 → F2 ★, **sin bifurcación F3**) · 6–10. Sesiones 1–5 (s-schedule) ·
11. Metodología ABR · 12. Beneficios + Entregables + Acreditación + Equipo · 13. Impacto ·
14. Precio (Fase 1, campos vacíos) · 15. Próximos pasos · 16. Cierre.

## 5. Deck B — Fases 1+2 (clon digital)

Deck B = **los 5 slides de Fase 1 idénticos** + **Fase 2 nueva**. La Fase 2 es la inmersión técnica en
Claude Code (incluye terminal/IDE) donde cada directivo construye su **clon digital**: un agente
"segundo cerebro" que conoce su área, sus documentos y su contexto de decisión, conectado a sus
herramientas, que le ayuda a decidir mejor y le automatiza trabajo en varias áreas.

**Fase 2 — 6 sesiones / 12 h** (total deck B = 11 sesiones / 22 h):

| # | Sesión Fase 2 | Foco |
|---|---|---|
| 1 | Claude Code a fondo | Entorno real (terminal + IDE), proyectos, archivos, contexto, CLAUDE.md |
| 2 | Diseño del clon digital | Qué decisiones apoya, fuentes de conocimiento del directivo, alcance del "segundo cerebro" |
| 3 | Construcción del agente | Memoria persistente, conocimiento del área, documentos, subagentes |
| 4 | Conexión a herramientas | MCP + conectores: el clon actúa **dentro de las herramientas que ya usa** (§4.11) |
| 5 | Automatización de flujos de decisión | El agente facilita el trabajo en varias áreas (multi-paso) |
| 6 | Seguridad, gobernanza y puesta en producción | Uso responsable del clon, datos sensibles, mantenimiento |

**Lista de slides deck B (~22):**
1. Portada (hero: clon digital) · 2. Diagnóstico · 3. Objetivos (ambas fases) · 4. El plan (2 fases) ·
5. Roadmap (F1 → F2 → ★ clon digital) · 6–10. Sesiones Fase 1 (idénticas a deck A) ·
11–16. Sesiones Fase 2 (1–6) · 17. Metodología · 18. Beneficios (ambas fases) · 19. Impacto ·
20. Precio (cubre F1+F2, campos vacíos) · 21. Próximos pasos · 22. Cierre.

## 6. Reglas críticas honradas

- **§4.9** Impacto con cifras de estudios reales, fuente citada verbatim. Se reusa/actualiza el panel
  de impacto actual; si la Fase 2 (automatización/agentes) pide cifras distintas, se buscan con fuente.
- **§4.11** No afirmar que Venemergencia migra de stack ni que ya adoptó Claude. El clon digital **se
  integra** a sus herramientas, no las cambia.
- **§4.12** Glosar MCP, Plugins, Conectores en su primer uso por slide.
- **§4.13** Sin guion largo/mediano como separador.
- **§4.15** "Cómo arrancamos" = logística, sin acuerdos económicos.
- **§4.10** Sin overflow: chips ≤ ~28 chars en cards de Programa; certificar con
  `node scripts/verificar-overflow.js` en **ambos** HTML antes de entregar.
- **§4.14** AcroForms pre-llenados (Entregables, Acreditación con `[CÓDIGO]` sustituido, Paso01–03
  Título/Body) en **ambos** decks; campos de precio **vacíos**.

## 7. Plan de construcción (workflow — autorizado por el usuario)

1. Generalizar `generar-pdf.sh` (§3.1).
2. Construir **Deck A**: editar `index.html` (temario práctico Fase 1, roadmap sin F3, teaser F2) →
   `verificar-overflow.js` → `generar-pdf.sh venemergencia` → actualizar `customize-venemergencia.py` →
   correr customize.
3. Construir **Deck B**: clonar deck A a `index-completo.html`, ajustar portada/código/plan/roadmap,
   **clonar los 5 slides Fase 1** + **añadir 6 slides Fase 2** + CSS de Fase 2 en `overrides.css` →
   `verificar-overflow.js` → `generar-pdf.sh venemergencia index-completo.html` → crear
   `customize-venemergencia-completo.py` → correr customize.
4. Verificación final por deck: `verificar-propuesta.sh` + revisión visual slide por slide de cada PDF.
5. Actualizar `brief.md` (dos alcances, Fase 2 costeada, sin F3) y registrar en `aprendizajes.md`.

**Fan-out aprovechable en el workflow:** los 11 slides de sesión, la investigación de impacto y los dos
customize son tareas paralelizables; la verificación de overflow es barrera por deck.

## 8. Fuera de alcance

- Fase 3 (réplica masiva): se retira del relato.
- Calendario / fechas: modalidad y cronograma siguen a decisión del cliente (no se afirman).
- Precio: lo llena ventas (campos vacíos intencionales).
