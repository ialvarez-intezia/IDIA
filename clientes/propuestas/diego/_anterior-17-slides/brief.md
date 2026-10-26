# Brief — Diego

## Datos administrativos

- **Cliente**: Diego (capacitación personal, 1 participante)
- **Sector**: personal (particular, no corporativo)
- **Slug**: `diego`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company personalizada (1 participante) (`CAP-109`)
- **Eje temático**: **Claude**, de cero a experto — ecosistema completo: Projects, Artifacts, Cowork, Skills y Claude Code
- **Fecha del brief**: 2026-08-19
- **Estado**: borrador / propuesta inicial
- **Fuentes**: instrucción directa del usuario (2026-08-19). Asesora comercial: Flavia Martínez

## Contacto

- **Persona contacto (cliente)**: Diego
- **Asesora de ventas Intezia**: Flavia Martínez (+58 414-5756615 · fmartinez@intezia.com)
- **Facilitador asignado**: por confirmar — Equipo INTEZIA Educación designa al facilitador antes del arranque

## Perfil del participante

- 1 persona: Diego.
- Instrucción explícita del usuario: programa **"de cero a experto"** — las bases se mencionan sin detenerse en ellas; el grueso del programa se enfoca en el uso avanzado del ecosistema Claude: **Cowork, Skills, Projects, Artifacts y Claude Code**.

## Necesidad detectada

Dominar el ecosistema completo de Claude, más allá de una conversación suelta: pasar de los fundamentos (repasados rápido) al uso experto de Projects, Artifacts, Cowork, Skills y Claude Code, cerrando con un proyecto propio aplicado a su día a día.

## Especificaciones del programa

- **Duración**: 12 horas académicas (6 sesiones de 2 horas, 6 módulos — 1 módulo por sesión).
- **Modalidad**: **Presencial**.
- **Fechas**: por confirmar — se omiten del deck hasta que se agenden (sin placeholder).
- **Ecosistema**: **Claude** (Projects, Artifacts, Cowork, Skills, Claude Code). Programa 100% Claude.
- **Entregables esperados**: Workbook digital, Certificado de participación.
- **Aliado institucional**: no.
- **Precio**: la propuesta lleva slide de Propuesta Económica; ventas llena la cotización en Adobe Reader.

## Decisiones de diseño

- Clonada de `ailyn-gruszka/` (CAP-070, canónica personal mono-fase, Educación). Ampliada de "Claude Fundamentals" (4 mód/8h) a todo el ecosistema (6 mód/12h).
- 17 slides (vs. 15 de la canónica): Programa se reparte en 2 slides de 3 módulos cada una (patrón `cashea/`, cards a tamaño completo, no el modo compacto de 5-6 módulos en una sola grilla) + 6 slides de cronograma (1 por sesión, patrón `cashea/`). Sin slide de Alcance: a diferencia de Ailyn, no hay expectativas explícitas del cliente que delimitar.
- Arco pedagógico: **I** Claude desde cero (fundamentos + prompting estructurado, mencionados sin profundizar) · **II** Projects · **III** Artifacts · **IV** Claude Cowork · **V** Claude Skills · **VI** Claude Code + proyecto final integrador.
- Copy en **singular** («tú / tu») por ser 1 participante.
- Listas de Diagnóstico, Objetivos específicos y columnas de Cronograma van **sin `<strong>`** (bug conocido: `<li>` con `display:flex` rompe el texto — `bug-strong-flex-specifics`). Resaltados solo en párrafos (`.context`, `.general`, `.obj`).
- Propuesta Económica actualizada al estándar vigente (30 días + `.cot-terms-box` con link a T&C) — la canónica de origen (Ailyn, 2026-07-03) todavía tenía el texto antiguo de "7 días en divisas".
- Slide de Impacto con datos heredados de la canónica (Stanford HAI AI Index 2026, McKinsey State of AI 2025, Anthropic Economic Index 2025) — mismos estudios ya citados y verificados en el deck de origen (§4.9).
- Facilitador: por confirmar (Equipo INTEZIA Educación). Asesora en cierre: **Flavia Martínez**.
