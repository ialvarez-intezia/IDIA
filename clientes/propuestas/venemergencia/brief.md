# Brief — Venemergencia · Adopción de Claude en cascada (CAP-047)

## Datos administrativos

- **Cliente**: Venemergencia · empresa venezolana de servicios de emergencia y atención
- **Naturaleza**: Capacitación in-company · **adopción de Claude** · DOS propuestas en la misma carpeta: Deck A = Fase 1 (10 h, capa gerencial, temario práctico); Deck B = Fases 1+2 (Fase 2 = clon digital con Claude Code, 12 h, cotizada). Fase 3 (réplica masiva) retirada del relato.
- **Slug**: `venemergencia`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación (`CAP-047`)
- **Programa**: Adopción de Claude · Fase 1 (Deck A) y Fases 1+2 con clon digital (Deck B)
- **Eje temático**: adopción de **Claude** (la plataforma de IA de Anthropic) con método, criterio y manejo seguro de la información, partiendo de la capa gerencial como multiplicadora
- **Marco de la relación**: **alianza** entre Intezia y Venemergencia
- **Fecha del brief**: 2026-06-05
- **Estado**: DOS decks en la carpeta. **Deck A `index.html` (15 slides, solo Fase 1, código `CAP-047`)** — slide 04 = los **5 módulos con su resultado** («Te llevas…»), **SIN roadmap** (una propuesta de una sola fase no muestra la Fase 2; modo compacto de 5 módulos en `overrides.css`). **Deck B `index-completo.html` (24 slides, Fases 1+2, código `CAP-047 · Fases 1+2`)** — plan de 2 fases + roadmap **lineal** F1 → F2 → ★ (`.rmx-link`) + slide **«Fase 1 · El programa»** (5 módulos con resultado, igual que Deck A) + **slide divisor notorio «Fase 2 · Clon digital»** (`.s-fase-divider`, pantalla completa) entre el cierre de Fase 1 y el arranque de Fase 2. Customizes: `customize-venemergencia.py` (A) y `customize-venemergencia-completo.py` (B). `generar-pdf.sh` y `verificar-propuesta.sh` aceptan 2º arg HTML (multi-deck)

> **Nota de diseño**: aunque la referencia canónica multi-fase es `pilotes-perforados`, ese deck está modelado para un *diagnóstico* (Mapa de Calor) que no aplica a un currículo de formación. La Fase 1 de Venemergencia es una capacitación-currículo con la misma forma que `cumbre-andina` (mismo eje Claude, usa `_base`, asesora María Iribarren ya correcta). Se clona de `cumbre-andina` y la narrativa de 3 fases se lleva en la slide de programa.

## Contacto

- **Asesora comercial Intezia**: **María Iribarren** · +58 414 0570056 · miribarren@intezia.com
- **Consultor / Facilitador**: **sin consultor asignado** → "Equipo INTEZIA Education" (no inventar nombre)
- **Cliente referente**: a confirmar en kick-off

## Por qué este proyecto

Venemergencia, en el marco de una **alianza** con Intezia, quiere impulsar la adopción de IA en su
organización. El interés es claro pero la adopción debe hacerse **con método y en cascada**: empezar por
la **capa gerencial** (personas con disponibilidad y rol para transmitir lo aprendido) y luego ir bajando
por la pirámide. Por eso la Fase 1 forma a esos líderes como **multiplicadores**: dominan Claude, salen con
entregables propios y quedan listos para replicar la formación a sus equipos.

Venemergencia mostró además interés en **ciberseguridad**. No es el foco de la Fase 1, pero sí se aborda como
pilar de **uso seguro**: qué protocolos de seguridad y privacidad ofrece Claude/Anthropic, cómo se maneja la
información y qué pueden hacer ellos con información sensible.

## Diagnóstico (5 puntos)

1. La alianza abre la puerta a adoptar IA en Venemergencia, pero hace falta convertir el interés en una capacidad real, no en entusiasmo disperso.
2. Para que la adopción escale, debe empezar por la **capa gerencial**: líderes con disponibilidad y rol para transmitir lo aprendido.
3. Hoy el uso de herramientas de IA, donde existe, es informal: sin método común, los resultados dependen de quién y cómo lo use.
4. Hay dudas legítimas sobre **privacidad y manejo de información sensible** al usar IA.
5. Venemergencia quiere una adopción que baje en **cascada** y deje entregables útiles desde la primera fase.

## Estructura del proyecto

### Fase 1 · Adopción de Claude (capa gerencial) — única cotizada

- **Modalidad**: a decisión del cliente (Presencial / Online síncrono / Híbrido) · cronograma a consideración del cliente
- **Audiencia**: cohorte gerencial cerrada · **general y transversal** (número y áreas a confirmar en kick-off) · perfil multiplicador
- **Duración**: **10 horas en 5 sesiones de 2 h** (1 módulo por sesión)
- **Modelo**: **train-the-trainer híbrido** — formamos a los líderes para que la información baje en cascada
- **Módulos (5) — temario práctico**:
  1. Fundamentos de Claude · prompting efectivo
  2. Ecosistema de trabajo + Claude Design (Projects, Artifacts, análisis de documentos)
  3. Cowork y Skills (crear una Skill reutilizable y automatizar una tarea)
  4. Conectores, Plugins e integraciones (MCP; toque de Claude Code dentro de la app) · automatización
  5. Seguridad y manejo de información sensible (protocolos de Claude/Anthropic) · cierre de cascada
- **Entregables rápidos**: cada participante sale con ≥1 **Skill funcional** + ≥1 **proceso automatizado** (conector/plugin) + un caso de uso real de su área.
- **Cascada**: se mantiene como narrativa (porqué empezar por gerencia), ya no como módulo dedicado.

### Fase 2 · Clon digital con Claude Code — cotizada en el Deck B

- **Inmersión técnica en Claude Code** (incluye terminal/IDE). Cada directivo construye su **clon digital**: un agente «segundo cerebro» que apoya decisiones y le automatiza trabajo en varias áreas.
- **6 sesiones / 12 h.** Sesiones: 1) Claude Code a fondo · 2) Diseño del clon · 3) Construcción del agente · 4) Conexión a herramientas (MCP/conectores) · 5) Automatización de decisiones · 6) Seguridad y puesta en producción.
- Cotizada dentro del Deck B (Fases 1+2). En el Deck A aparece solo como continuación (teaser para el upsell).

### Fase 3 · Réplica en cascada — RETIRADA

- Eliminada del relato por reenfoque (foco en F1 + F2). El multiplicador/cascada permanece solo como narrativa de la Fase 1.

## Especificaciones del programa

- **Acreditación**: constancia de participación INTEZIA Education
- **Pre-requisitos**: acceso a casos y tareas reales del equipo para personalizar la práctica
- **Slide económica**: incluida, campos de precio **vacíos** (los llena ventas)

## Reglas críticas aplicadas

- **§4.11**: el deck no afirma que Venemergencia migra de stack ni que ya adoptó Claude; Claude se presenta como herramienta recomendada que se integra a su entorno.
- **§4.9**: datos de impacto y protocolos de seguridad de Claude salen de fuentes reales verificables, citadas verbatim.
- **§4.15**: «Cómo arrancamos» = logística, sin acuerdos económicos.
