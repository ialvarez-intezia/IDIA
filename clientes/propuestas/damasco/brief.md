# Brief · DAMASCO — CAP-037

> Capacitación in-company · Fase 1 · IA aplicada a la operación retail
> Fuente: Minuta de levantamiento de requerimientos, 26 de mayo de 2026 (Isabella Palazzone).

## Datos generales

- **Cliente:** DAMASCO (retail · 54 sucursales)
- **División Intezia:** Educación
- **Código:** CAP-037
- **Tipo de documento:** Capacitación in-company (multi-ruta, sin perfil de ingreso)
- **Eje temático:** IA aplicada a la operación retail (desarrollo, soporte)
- **Modalidad:** Presencial
- **Duración Fase 1:** 12 horas (Desarrollo 8 h · Soporte 4 h)
- **Asesora de proyecto:** María Iribarren · +58 414 0570056 · miribarren@intezia.com (reasignada 2026-09-28, ver ajuste al final del brief; antes Isabella Palazzone)
- **Consultor asignado:** Rafael Carreño (facilitador, refuerzo técnico)
- **Contactos cliente:** Charlie, Benjamín, Yan (directiva y líderes de área)

## Contexto del negocio (datos duros de la minuta)

DAMASCO mueve un catálogo grande y rápido: entran entre **60 y 100 productos nuevos los
viernes por la tarde**, los **precios cambian a diario** por estrategia comercial, y la
operación procesa del orden de **100.000 facturas diarias** sobre **16.000 artículos** en
**54 sucursales**. El cliente ya pasó la etapa de curiosidad: quiere implementación y
automatización con método, no una charla genérica.

**Stack actual (híbrido, no casado con un solo proveedor):**
- IA / desarrollo: Anthropic (Claude, Claude Code, Claude Cowork, Vertex AI) sigue como eje
  del equipo de Desarrollo. **Actualización 2026-09-15**: el equipo de Desarrollo ya no usa
  Gemini como herramienta principal; sus herramientas top actuales son Claude y ChatGPT/Codex
  (OpenAI, con extensión de IDE tipo Antigravity) — revierte la postura de la minuta original,
  que descartaba Codex. DeepSeek sigue en el radar por costo/rendimiento de tokens.
- Diseño y multimedia: Canva, Figma.
- Gestión y datos: Excel / Google Sheets, **SAP Business One**, **Power BI** (equipo de BI
  propio), plataformas de pago / Banco de Venezuela.

> **Regla de stack (CLAUDE.md §4.11):** Intezia se integra al entorno híbrido del cliente,
> no propone migrarlo. El equipo de BI centraliza en Power BI: **no construimos dashboards
> en otra herramienta**, la ruta de datos alimenta los tableros que ya tienen.

## Departamentos y nivel real (la base del diseño)

| Departamento | Personas | Nivel | Necesidad clave |
|---|---|---|---|
| Tecnología / Desarrollo | 9 (4 programadores · 2 consultores SAP · 2 BI · 1 director) | Avanzado, parejo | Dominio fino de Claude Code / Cowork y ChatGPT/Codex, prompting estructurado y de lógica compleja, agentes eficientes con balance de carga, control de costos de tokens, bases de datos con IA que alimentan Power BI |
| Soporte / Infraestructura | 6 | Intermedio (ajustado 2026-09-15, antes básico) | Infraestructura, resolución de incidencias y aplicación práctica al área de trabajo, más un bloque administrativo (resumen de reuniones, correo conectado a IA, sugerencias) |

### Decisión de diseño sobre Desarrollo (clave del proyecto)

El equipo de Tecnología es **avanzado y parejo**: no hay un subgrupo rezagado que nivelar.
Por eso **se eliminó el split "intermedio + avanzado" con 2 h de nivelación remedial** que
confundía las horas (rechazado por ventas y por Douglas).

El split sí tiene sentido, pero **por función, no por nivel**, y la nivelación que pide la
minuta es **avanzada** (dominio fino de herramientas, no remedial):

- **Fundamento común (los 9 juntos):** dominio de Claude Code y Claude Cowork, con
  ChatGPT/Codex como herramienta complementaria (ya no Gemini, actualización 2026-09-15) +
  prompting estructurado y de lógica compleja. Es la "nivelación y trucos avanzados" de la
  minuta.
- **Mesa A · Integraciones (4 programadores):** agentes con Claude Code + OpenCode, con foco
  en balance de carga entre agentes y en programarlos de forma eficiente, para automatizar
  auditorías y flujos repetitivos · control de costos de tokens.
  *(Pasarelas de pago quedan fuera por ser tema delicado; entran en una fase posterior.)*
- **Mesa B · Datos y operación (2 SAP + 2 BI):** bases de datos con IA (consultar en
  lenguaje natural, sin escribir SQL a mano) cuyos resultados **alimentan los tableros de
  Power BI** del equipo de BI.

Los 9 están las **8 horas completas, en un solo grupo**. Las dos mesas son dos frentes de
práctica en la misma sala, no dos horarios distintos: por eso las horas dejan de confundir.

## Roadmap por fases (corregido contra la minuta)

- **Fase 1 (cotizada ahora):** los 2 equipos, talleres in-company por departamento.
- **Fase 2 (plus diferenciador):** dos pasos. (a) **Agentes departamentales**: un agente por
  área que carga con su trabajo repetitivo. (b) **Agentes integrados a la medida**: conectados
  a las herramientas internas (SAP, Power BI, CRM), con **auditoría de uso de IA** y
  **acompañamiento para estandarizar** esos agentes. Alcance y cotización aparte, sobre lo
  aprendido en Fase 1.

> El deck original inventaba una "Fase 2: sumamos Administración, Tesorería y Ventas". Eso
> **no está en la minuta** y se eliminó.

## Ajuste posterior (2026-09-15) — stack de Desarrollo y nivel de Soporte

Instrucción directa del usuario, acordada con el cliente:

1. **Desarrollo ya no usa Gemini como herramienta principal.** Herramientas top actuales:
   Claude (Code + Cowork, confirmado con el usuario que "Cloud" en su instrucción era un typo
   de "Claude"), ChatGPT/Codex (OpenAI, con extensión de IDE tipo Antigravity) y Kimi. Se
   actualizó todo el contenido de Desarrollo (`programa.md`, `index.html`) reemplazando Gemini
   por este stack. **Marketing mantiene Gemini** — el cambio es específico del equipo de
   Desarrollo, no cascada al resto del programa.
2. **Enfoque avanzado de Desarrollo, reforzado** con 3 temas explícitos que antes solo estaban
   implícitos en "agentes" y "prompting de lógica compleja": **balance de carga de agentes**,
   **prompting estructurado** y **cómo programar agentes de forma eficiente**. Se integraron en
   el "Fundamento común" (prompting estructurado) y en la Mesa A de programadores (balance de
   carga + eficiencia de agentes), sin tocar las 8 horas totales de la ruta.
3. **Soporte sube de básico a intermedio**, orientado a infraestructura, resolución de
   incidencias y aplicación práctica al área de trabajo, y suma un **tema administrativo**
   (resumen de reuniones, correo conectado a IA, sugerencias). **Se mantienen las 4 horas** de
   la ruta (confirmado con el usuario): se recortó el bloque de fundamentos "desde cero" (ya no
   aplica en nivel intermedio) para hacerle espacio al tema administrativo, sin extender la
   duración total del programa (sigue en 18h).

## Ajuste posterior (2026-09-15, segunda pasada) — se retira Kimi, Marketing y la cotización

Instrucción directa del usuario. **Supera los puntos 1 y 3 de la sección anterior** en lo que
toca a Kimi y a Marketing:

1. **Se retira la mención a Kimi** del stack de Desarrollo. Queda: Claude Code + Claude Cowork
   (eje) + ChatGPT/Codex. Kimi había entrado en la primera pasada del ajuste como parte de las
   "herramientas top actuales" del equipo, pero el usuario pidió quitarlo.
2. **Se retira la ruta de Marketing por completo.** El usuario aclaró que Marketing nunca
   formó parte del pedido de ajuste original ("nada más eran ellos, marketing no tenía nada
   que ver") — la mención a "Marketing mantiene Gemini" de la sección anterior queda sin
   efecto porque Marketing ya no está en el documento. Cambios:
   - Duración total: de 18h (Desarrollo 8h + Marketing 6h + Soporte 4h) a **12h** (Desarrollo
     8h + Soporte 4h).
   - Se eliminó el módulo/ruta de Marketing de `index.html` (Programa, Cronograma) y
     `programa.md` (§4.2, §5.1, §5.2, §6), y toda mención a Marketing en Diagnóstico,
     Objetivos y Roadmap.
   - En la slide de Impacto se retiró la barra "Marketing y contenidos +40%" (McKinsey/BCG),
     ya no aplica a lo que se está cotizando.
   - `scripts/customize-damasco.py`: se quitó "Lote de catálogo (Marketing)" de Entregables y
     se corrigió "las 3 rutas" → "las 2 rutas" en Paso01Body.
3. **Se retira la slide de Propuesta Económica (cotización) por completo.** Deck sin hoja de
   precio; `agregar-campo-precio.py` omite los 5 campos de precio automáticamente al no
   encontrar el marcador "Propuesta Económica" en el deck (mismo comportamiento que otros
   decks sin `.s-price`, no requiere cambios en scripts).
4. Deck pasó de 14 a 12 slides, todos los contadores renumerados.

## Ajuste posterior (2026-09-15, tercera pasada) — se retira Equipo facilitador de la página 8

Instrucción directa del usuario: quitar el bloque "Equipo facilitador" (Rafael Carreño) y la
asesora de proyecto (Isabella Palazzone) de la slide de Beneficios (página 8/12). Se eliminó
el `<div class="team">` completo de `index.html` — coincide con el estándar §4.10a ya vigente
para propuestas nuevas ("Bloque Equipo facilitador en Beneficios: se retira también"), aplicado
aquí a este deck legacy por pedido explícito.

Al retirar `.team`, la grilla de 4 tarjetas (`.grid`, `height:280px` en `_base/styles.css`)
dejaba cerca de 260px en blanco antes del pie de página. Se agrandó la grilla a `height:480px`
en `overrides.css` (regla local, no se tocó el CSS compartido) para que las 4 tarjetas ocupen
el espacio liberado sin overflow.

Rafael Carreño e Isabella Palazzone **siguen siendo** el facilitador asignado y la asesora de
proyecto del programa (ver "Datos generales" arriba y `programa.md` §7) — solo se retiró su
presentación visual de esa slide del deck, no su asignación real al proyecto. Isabella sigue
apareciendo en el cierre (página 12) como contacto de la asesora, sin cambios ahí.

## Ajuste posterior (2026-09-28) — cambio de asesora de proyecto

Instrucción directa del usuario: **María Iribarren reemplaza a Isabella Palazzone** como
asesora de proyecto de Damasco. Isabella seguía apareciendo como contacto de la asesora en
el cierre del Dashboard de Impacto Edu-Trace de la Ruta Soporte (`clientes/dashboards/
damasco-soporte/index-cliente.html`, página 10/10) — se actualizó a María Iribarren
(+58 414 0570056 · miribarren@intezia.com). Esto **supera** la nota de la "tercera pasada"
(2026-09-15) que decía que Isabella seguía apareciendo en ese cierre sin cambios. Rafael
Carreño sigue como facilitador asignado (sin cambios); esto es solo reasignación de la
asesora comercial/de proyecto. Si existe una propuesta o kickoff de Damasco con el contacto
de Isabella, actualizarlo también al regenerar.

## Notas de entrega

- Sin slide de Propuesta Económica (ver ajuste 2026-09-15 arriba) — no aplica el punto
  original de "campos comerciales vacíos".
- Datos de impacto: solo estudios reales con fuente citada (§4.9).
- Sin guion largo, sin Spanglish, redacción humana y concreta con los datos del cliente.
