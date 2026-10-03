# Brief — Fivenca · Fundamentos de IA (CAP-061)

## Datos administrativos

- **Cliente**: Fivenca (grupo financiero · servicios financieros / mercado de capitales)
- **Sector**: Servicios financieros
- **Slug**: `fivenca-fundamentos-ia`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-061`)
- **Eje temático**: Fundamentos de IA generativa para productividad, **multi-herramienta y
  ecosistema-agnóstico**, con **Gemini y Claude como ejes de práctica**. Énfasis en elegir la
  herramienta correcta y en automatizar tareas de forma progresiva.
- **Audiencia objetivo**: ~25 personas del equipo de Fivenca · niveles de IA desiguales.
- **Modalidad**: **sin afirmar** (se confirma en el arranque). El deck usa "Sesión en vivo"
  en el cronograma y deja la modalidad para el Paso 01.
- **Fecha del brief**: 2026-06-16
- **Estado**: Borrador
- **Fuentes**: instrucción directa del usuario 2026-06-16 + contexto de cuenta Fivenca
  (CAP-039 y `fivenca-claude-express`).

> **Distinto de `fivenca/` (CAP-039)** y de `fivenca-claude-express/`: CAP-039 es el plan
> integral de 3 fases (~40 colaboradores, 4 h, mono-fase entregada, deck legacy); el express
> es una sesión de 2 h solo-Claude para 4-5 personas. **Esta (CAP-061)** es una capacitación
> de **8 h / 4 módulos** de Fundamentos de IA para ~25 personas, multi-herramienta. Carpeta y
> deck independientes.

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414-0570056 · miribarren@intezia.com
- **Facilitación**: **Equipo Education** (elección del usuario 2026-06-16). Nota de cuenta:
  Andrés Fornerino lleva la relación con Fivenca; se puede nominar en el deck si ventas lo prefiere.

## Necesidad detectada (encargo del usuario)

Una capacitación para 25 personas sobre los **fundamentos de la IA**: lo básico de la IA, el
**ecosistema de herramientas**, la importancia de **escoger la herramienta correcta** y luego
**resolver ejemplos cotidianos con Gemini o Claude**. Mostrar **mejoras e impacto** de la IA en
procesos manuales, repetitivos o complejos, y la importancia de la IA para **automatizar tareas**
(no necesariamente al 100%: reducir pasos poco a poco).

## Diagnóstico (contexto comercial · cuenta Fivenca)

1. El personal ya usa IA por su cuenta (Gemini, Claude y otras), **sin método ni criterio
   común**. Los resultados dependen de quién escriba el prompt.
2. El nivel de manejo de IA es **muy desigual** entre las personas del equipo.
3. Tareas manuales y repetitivas (correos, documentos, reportes) consumen horas cada semana.
4. Sin criterio para **elegir la herramienta**, se usa la primera a mano y no la más adecuada.
5. La dirección quiere una adopción con **método y resultados medibles**, no entusiasmo sin control.

## Ecosistema y stack del cliente (dato de contexto interno · §4.11)

- Fivenca opera sobre **Microsoft 365**, pero pidió **no anclar la propuesta a ese ecosistema**
  y aclaró que **no usa Copilot como su IA**. Por eso el eje es **multi-herramienta y
  ecosistema-agnóstico**: el deck habla del trabajo diario (correos, documentos, hojas, reportes)
  y de elegir la herramienta adecuada, con **Gemini y Claude** como ejes de práctica.
- **No afirmar migración de stack (§4.11)**: las herramientas se presentan como kit de trabajo;
  nunca decir que Fivenca migra a otra suite ni que ya adoptó una herramienta. La IA enseñada se
  presenta como **opción recomendada** (§4.11 corolario), no como algo que el equipo ya usa.

## Especificaciones del programa

- **Duración**: 6 horas académicas · 4 módulos · 2 sesiones de 3 h (2 módulos por sesión). Bajado de 8 h a 6 h el 2026-06-17 (corrección del usuario: lo acordado eran 6 h).
- **Estructura**: I Fundamentos de IA · II El ecosistema y la herramienta correcta · III Manos a
  la obra con Gemini y Claude · IV Automatiza y mide el impacto.
- **Modalidad**: sin afirmar (se confirma al arranque). Sesiones "en vivo".
- **Fechas**: no definidas.
- **Acreditación**: certificado de participación INTEZIA.
- **Precio**: la propuesta lleva slide de Propuesta Económica; los campos de precio quedan
  vacíos (ventas cotiza en Adobe Reader). El apartado comercial (Programa, Notas) también vacío.

## Decisiones de diseño

- **Clonada de `anabella/` (CAP-052)**: clon limpio y reciente de la canónica mono-fase
  (formato cumbre-andina, Educación, enlaza `_base`), ya estructurado en 4 módulos / 4 sesiones /
  14 slides con `acroforms.json`, `meta.json` y `overrides.css`; aquí condensado a 2 sesiones de 3 h / 12 slides. **No** se clonó el deck legacy
  `fivenca/` (CAP-039, `styles.css` local).
- **12 slides**: portada · dolor+diagnóstico · objetivos · programa (4 mód) · 2 sesiones de
  cronograma (2 módulos por sesión) · metodología ABR · beneficios · impacto · propuesta económica · próximos pasos · cierre.
- **Equipo en la slide de Beneficios**: Equipo Education (facilitación) + María Iribarren (asesora).
- **Slide de Impacto** con datos de estudios reales citados (Stanford HAI AI Index 2026, McKinsey
  State of AI 2025, Anthropic Economic Index 2025), sin recifrar (§4.9).
- Copy re-anclado a Fivenca (sector financiero, uso empírico previo, automatización progresiva);
  sin frases viajeras de Anabella.
