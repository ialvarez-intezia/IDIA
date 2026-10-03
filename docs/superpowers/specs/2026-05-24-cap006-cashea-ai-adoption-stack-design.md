# CAP-006 Cashea · Reconversión a AI Adoption Stack (Claude-céntrico)

**Fecha:** 2026-05-24
**Slug:** `clientes/propuestas/cashea/CAP-006 Claude Power - Skills MCP y Workflows`
**División:** educacion · **Código:** CAP-006 (se conserva)
**Tipo de deck:** multi-fase (clon de `pilotes-perforados/`)

---

## 1. Problema

El deck CAP-006 actual ("Claude Power · Skills, MCP y Workflows Avanzados") es un curso
de nicho: 12.5 h, exclusivo Claude, para power users avanzados que construyen Skills, MCP
y agentes. **Dejó de responder al ask real de Cashea.** El equipo definió la estrategia en
el documento interno *Cashea · Análisis Comparativo de Propuestas* (2026-05-04): la
recomendada es la **Propuesta E — Cashea AI Adoption Stack**, arquitectura de 3 tiers para
**1.000 colaboradores + 50 directivos**, cuyos dolores centrales son **escalable** y
**persistente para nuevos ingresos**.

## 2. Objetivo

Reconvertir CAP-006 al deck del **AI Adoption Stack**, manteniendo a **Claude** como
columna vertebral (decisión del usuario: conservar el enfoque Claude según Propuesta E).
El deck se mide por cobertura (1.000 + 50) y tiers, no por horas de un curso único.

## 3. Decisiones de framing (cerradas con el usuario)

1. **Rol:** reconvertir a programa amplio (no curso de power users).
2. **Estructura:** 3 tiers escalables (Fundamentals / Ecosystem / Enterprise), multi-fase,
   Tier 2 marcado como recomendado.
3. **Precios:** NINGÚN monto en el deck. Las cifras (18K/48K/78K REF) son referencia
   interna del equipo. La propuesta no habla de dinero; el slide de precio (`s-price`)
   queda como AcroForm vacío para ventas. Los tiers se presentan por **scope**.
4. **Identidad:** se mantiene enfoque Claude, reestructurado según Propuesta E.
5. **MaratonIA:** escribir siempre así (juego "maratón" + IA). En su primer uso describirla
   como **la plataforma educativa en línea de Intezia**.

## 4. Reglas críticas aplicables (CLAUDE.md)

- **§4.11 / corolario adopción:** Claude se presenta como el stack recomendado. Prohibido
  afirmar que Cashea "ya migró" o "ya adoptó" Claude como un hecho de cara al cliente.
- **§4.13:** sin guion largo (—) ni mediano (–) como separador. Usar coma, paréntesis,
  dos puntos, punto o middle dot (·).
- **§4.9 Impacto:** toda cifra de la slide de Impacto sale de un estudio real y verificable,
  con fuente citada verbatim. Sin fuente sólida, no entra la cifra. (Buscar con WebSearch.)
- **§4.12:** glosar acrónimos de jerga en su primer uso por slide.
- **§4.10:** sin overflow visual; revisar PDF slide por slide antes de entregar.
- **§4.14 + §10:** leer brief/index/programa antes de modificar; pre-llenar AcroForms
  no-precio; correr `verificar-propuesta.sh` y el par `generar-pdf.sh` → `customize-*.py`.

## 5. Mapa slide por slide (estructura pilotes-perforados)

| # | Slide | Contenido nuevo |
|---|---|---|
| Cover | `s-cover` | Título: **Cashea AI Adoption Stack · Adopción de IA a escala con Claude**. Bajada: "Un sistema, no un taller: nivelar a 1.000, blindar cada nuevo ingreso." |
| 01 | `s-pain` (Diagnóstico) | (a) La capacitación puntual no persiste: cada nuevo ingreso entra desde cero. (b) 1.000 colaboradores en niveles dispares; el conocimiento vive en personas, no en un sistema. (c) Los 50 directivos necesitan liderar la adopción, no solo aprobarla. (d) Cashea pidió algo escalable y persistente, no un modelo tradicional que no escala. |
| 02 | `s-goals` (Objetivos) | Nivelar piso común con Claude · sistema persistente que onboarda nuevos ingresos en automático · directivos que lideran la adopción · atacar áreas críticas con datos. |
| 03 | `s-program` (Componentes, 1-2 slides) | Bloques Claude-céntricos: (1) Nivelación masiva (Claude Fundamentals, cohortes de 250, 6 facilitadores). (2) Executive Masterclass directivos (entregable Mapa de Calor). (3) **MaratonIA × Cashea**, la plataforma educativa en línea de Intezia, con branding Cashea + Asistente IA de Ruta de Aprendizaje (onboarding automático de nuevos ingresos). (4) Auditoría y consultoría de procesos con IA (deliverables). |
| 04 | `s-roadmap` (3 tiers escalables) | **Núcleo.** Tier 1 · Fundamentals: nivelación masiva + masterclass directivos. **Tier 2 · Ecosystem (RECOMENDADO):** Tier 1 + MaratonIA + asistente + onboarding nuevos ingresos + dashboard ejecutivo. Tier 3 · Enterprise: Tier 2 + auditoría + talleres por área + account manager. **Sin montos**, presentados por scope. |
| 05 | `s-orange` (Metodología) | ABR + cohortes online de 250 + MaratonIA como capa persistente. |
| 06 | `s-benefits` (Beneficios) | Escala sin perder calidad · el conocimiento queda en un sistema · cada nuevo ingreso se onboarda solo · directivos alineados. |
| 07 | `s-impact` (Impacto) | Cifras de estudios reales sobre ROI/adopción de IA a escala, fuente verbatim (§4.9). |
| 08 | `s-price` | AcroForm **vacío** (ventas). |
| 09 | `s-steps` (Próximos pasos) | AcroForm prellenado: confirmar fechas + zona horaria · firmar acuerdo + 50% anticipo · kickoff ~30 min. |
| Cierre | `s-end` | CTA (botón-hipervínculo si aplica). |

## 6. Archivos a modificar

- `clientes/propuestas/cashea/CAP-006 .../index.html` — reescritura de copy por slide.
- `clientes/propuestas/cashea/CAP-006 .../styles.css` — ajustes solo si el layout de tiers
  lo requiere (reaprovechar clases de `s-roadmap` de pilotes-perforados).
- `clientes/propuestas/cashea/CAP-006 .../brief.md` — reflejar nuevo enfoque (stack, no power-user).
- `clientes/propuestas/cashea/CAP-006 .../programa.md` — reflejar componentes y tiers.
- `customize-*.py` del slug — pre-llenado de AcroForms no-precio.

## 7. Fuera de alcance (YAGNI)

- No tocar CAP-005 ni otras propuestas.
- No introducir contenido de power-user (Skills/MCP/Computer Use) salvo como mención
  opcional dentro de Tier 3 si encaja sin desviar el foco.
- No añadir montos en ninguna parte del deck.

## 8. Criterios de aceptación

- El deck no menciona el techo del power user ni Skills/MCP como eje.
- Los 3 tiers aparecen por scope, sin precios, con Tier 2 marcado recomendado.
- MaratonIA escrito correctamente y descrito como plataforma educativa en línea de Intezia.
- Sin guion largo; acrónimos glosados; sin overflow (revisión PDF slide por slide).
- AcroForms no-precio pre-llenados; slide de precio vacío.
- `verificar-propuesta.sh` pasa; par `generar-pdf.sh` → `customize-*.py` ejecutado.
