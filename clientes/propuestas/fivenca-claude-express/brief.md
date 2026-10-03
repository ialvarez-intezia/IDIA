# Brief — Fivenca · Claude express (grupo de 4-5)

## Datos administrativos

- **Cliente**: Fivenca (grupo financiero · servicios financieros / mercado de capitales)
- **Sector**: Servicios financieros
- **Slug**: `fivenca-claude-express`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company express · grupo reducido (**sin código** — es un documento-acuerdo educativo, no una propuesta comercial)
- **Eje temático**: Claude (dominar la herramienta a fondo) aplicado a los **procesos actuales de cada rol** del equipo
- **Fecha del brief**: 2026-06-12
- **Estado**: borrador / propuesta inicial
- **Fuentes**: instrucción directa del usuario 2026-06-12

> **Distinto de `fivenca/` (CAP-039)**: aquella es el plan integral de 3 fases para toda
> la empresa (~40 colaboradores, multi-herramienta). Esta es una sesión corta, enfocada
> y **solo sobre Claude**, para un grupo pequeño. Carpeta y deck independientes.

## Naturaleza del documento

- **NO es una propuesta comercial con cotización.** Es un **acuerdo / documento educativo**:
  comunica qué verá el equipo en esas 2 horas. **Sin slide de Propuesta Económica**
  (instrucción del usuario 2026-06-12). Los 5 campos AcroForm de precio no aplican;
  `generar-pdf.sh` omite el grupo de precio automáticamente.

## Contacto

- **Asesora comercial Intezia**: María Iribarren · miribarren@intezia.com
- **Facilitadores asignados**: **Andrés Fornerino** (consultor que lleva la cuenta) **+ Isaac** (dupla, instrucción del usuario 2026-06-12).

## Perfil de los participantes

- **Grupo reducido de 4 o 5 personas** del equipo de Fivenca.
- Ya usan IA de forma empírica en su trabajo (correos, análisis, revisión de documentos),
  sin un método común; el resultado depende de quién escriba el prompt.
- La meta: que **usen Claude bien**, con criterio, para **mejorar los procesos actuales
  dentro de sus roles** y poder seguir creciendo por su cuenta.

## Necesidad detectada

Aprender a usar Claude de manera amplia y con método, viéndolo en acción con ejemplos en
vivo sobre los procesos reales del equipo. Abarcar la mayor cantidad de capacidades útiles
en 2 horas para dejar una base sólida y un método común aplicable desde el día siguiente.

## Especificaciones del programa

- **Duración**: 2 horas académicas (1 sesión única). Capacitación express.
- **Estructura**: 4 bloques temáticos recorridos en la misma sesión de 2 h, panorámica de
  las capacidades actuales de Claude.
- **Modalidad**: **Presencial** (confirmada por el usuario 2026-06-12).
- **Fechas**: no definidas.
- **Herramienta**: Claude (Projects, Artifacts, Claude Design, conectores, Cowork, Skills,
  plugins, MCP). No solo fundamentos/prompting (memoria: capacitaciones de Claude incluyen
  capacidades actuales).
- **Ejemplos en vivo**: eje de la sesión. Los facilitadores construyen los ejemplos con el
  equipo en tiempo real, sobre los procesos de Fivenca.
- **Infraestructura**: Claude se presenta como opción recomendada (no afirmar que ya la usa
  ni que Fivenca migra de stack — §4.11). Fivenca opera sobre Microsoft 365; el deck NO se
  ancla a ese ecosistema.
- **Aliado institucional**: no.
- **Precio**: **sin slide de Propuesta Económica** (documento-acuerdo educativo).

## Decisiones de diseño

- Clonada de `patricia/` (canónica express 2 h vía cumbre-andina, Educación), no del deck
  legacy `fivenca/` (CAP-039, styles.css local).
- **10 slides**: se elimina la slide `s-price` respecto al canónico (sin cotización).
- **Sin código** en portada, acreditación ni PDF.
- **Equipo: 2 facilitadores** (Andrés Fornerino + Isaac) en la slide de Beneficios;
  **asesora María Iribarren** en el cierre.
- Copy re-anclado a Fivenca (`plantillas/redaccion.md`): hook de Impacto y título de
  Objetivos re-acuñados para no reusar frases viajeras de Patricia.
- Programa de 4 bloques recorridos en la sesión de 2 h: I Claude desde cero · II Crea en
  vivo · III Claude conectado · IV Lleva Claude más lejos.
- Slide de Impacto con datos de estudios reales citados (Stanford HAI AI Index 2026,
  McKinsey State of AI 2025, Anthropic Economic Index 2025) — sin recifrar (§4.9).
