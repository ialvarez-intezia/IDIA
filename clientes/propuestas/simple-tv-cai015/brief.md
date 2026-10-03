# Brief — Simple TV · Taller ejecutivo de Claude para los 12 directores (CAI-015)

> **Sin Ficha Comercial** (modalidad vieja: instrucción directa del usuario — misma cuenta que
> **DET-002**, **CAI-002**, **CAI-003**, **ALL-001**, **CAI-013**, **CAI-014** y **ALL-002**,
> ver `clientes/propuestas/simple-tv-det002/brief.md` para el detalle completo de la cuenta).
> Esta es la **séptima propuesta** de la cuenta y la **primera dirigida exclusivamente a los 12
> directores** (no a las 14 áreas ni al piloto de 4 IA Champions) — un taller de regalo/valor
> agregado, no una propuesta comercial con cotización. Vive en carpeta propia
> `simple-tv-cai015/`; no reemplaza ninguna de las otras 6.

## Datos administrativos

- **Empresa**: Simple TV (empresa venezolana de telecomunicaciones y entretenimiento)
- **Slug**: `simple-tv-cai015`
- **División Intezia**: `educacion`
- **Servicio** (Modelo Intezia, `empresa/tipos-de-documento.md §0`): `habilidades` — sesión
  única, sin Detección.
- **Código**: `CAI-015` — instrucción explícita del usuario.
- **Alianza**: no
- **Eje temático**: uso estratégico de Claude para la toma de decisiones ejecutivas y
  comunicación directiva, con casos reales de cada director.
- **Fecha del brief**: 2026-09-07
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: María — **María Iribarren** (miribarren@intezia.com ·
  +58 414 0570056), misma asesora que en el resto de la cuenta.
- **Cliente referente**: Neliana (lado Simple TV).

## Por qué esta propuesta — instrucción explícita del usuario

Los **12 directores** de Simple TV son quienes tienen **licencia propia de Claude** (a
diferencia del resto de la organización, que usa mayormente Microsoft 365 / Copilot, con
Claude en uso disperso). El usuario los describió como **"los embajadores que más nos
interesa comprar"** — es decir, ganarlos como aliados internos de la adopción de IA tiene un
valor estratégico desproporcionado a su número (12 personas), porque son quienes deciden y
dan ejemplo hacia sus propias áreas.

> **Nota de diseño interna (no exponer así en el deck)**: el framing "comprar embajadores" es
> el razonamiento comercial interno, no un lenguaje apropiado para los propios directores. En
> el deck se traduce a algo respetuoso y ejecutivo: los directores ya usan Claude con licencia
> propia, y este taller profundiza esa base para que lideren la adopción de IA en sus áreas —
> sin mencionar la palabra "embajadores" en el sentido transaccional del brief interno, ni que
> la empresa busca "ganarlos" a nada.

**Formato pedido, instrucción explícita del usuario**:
- **Un solo workshop**, práctico, presencial.
- **Nivel estratégico** (no fundamentos básicos — los directores llegan con más contexto de
  negocio que un colaborador operativo).
- **Enfocado en Claude, no en Copilot** — coherente con que son quienes ya tienen licencia
  propia de esa herramienta específica.
- **Gesto de regalo / valor agregado, no un curso completo** — respeta que su tiempo es
  limitado. No se diseña como un programa de varias sesiones (a diferencia de CAI-002/CAI-003/
  CAI-013/CAI-014, todos multi-sesión).
- **Sin pricing en el deck** — instrucción explícita: "esto no lleva pricing, eso lo pongo yo".
  A diferencia de todas las propuestas anteriores de esta cuenta (que sí llevan una hoja de
  cotización con campos vacíos para que ventas los llene), **este deck no incluye ninguna
  slide de precio ni campos AcroForm de cotización** — la asesora define el tratamiento
  económico (probablemente ninguno, dado el carácter de regalo) por fuera de este documento.

## Audiencia: los 12 directores (no las 14 áreas ni los 4 IA Champions)

Grupo distinto a los de cualquier otra propuesta de la cuenta: los directores con licencia
propia de Claude. No hay indicación de que correspondan 1:1 con las 14 áreas del resto de la
cuenta (ver `simple-tv-cai003/brief.md` para esa lista) — se trata como un grupo ejecutivo
propio, sin nombrar individualmente a ningún director (mismo criterio que el resto de la
cuenta con los IA Champions: nunca se exponen nombres propios de cara al cliente salvo
Neliana, ya usada como referente en el resto de los decks).

## Formato de la sesión

- **Modalidad**: presencial.
- **Duración**: sesión única de 3 horas (no un programa de varias semanas).
- **Estructura interna** (3 segmentos dentro de la misma sesión, no 3 módulos de varias horas
  cada uno como en CAI-002):
  1. Panorama estratégico — Claude para la toma de decisiones ejecutivas (uso ya validado en
     otros clientes: síntesis de información, comparación de escenarios, apoyo a
     comunicaciones directivas).
  2. Práctica guiada — cada director trabaja un caso real propio (un informe, una
     comunicación, un análisis pendiente) directamente con Claude, en la misma sesión.
  3. Cierre y autonomía — cómo seguir aplicando Claude sin depender de una sesión siguiente,
     dado que no hay Fase 2 programada.
- **Herramienta**: exclusivamente Claude — no se menciona Copilot en ningún punto del deck
  (a diferencia del resto de la cuenta, que sí es cross-ecosistema), porque estos directores
  ya tienen licencia propia de Claude específicamente.

## Cómo tratar el alcance

- No es cotización ni propuesta con temario cerrado — el caso real de cada director se define
  el día de la sesión, no se cierra un temario ahora.
- Se incluye slide de Beneficios con Entregables/Valor inmediato (certificado, guía de
  referencia), igual que el resto de la cuenta — **no incluye ninguna hoja de precio ni campos
  de cotización**, a diferencia de todas las propuestas anteriores de Simple TV.

## Notas de diseño

- **Base**: clon de `simple-tv-cai002/` (mono-fase, `../_base/styles.css` + `overrides.css`
  local, Beneficios v3 con layout ampliado, Cierre escalera) — es la base más cercana
  estructuralmente (mono-servicio, audiencia chica, sin roadmap de fases), pero se **recorta
  significativamente**: de 12 slides a **9**, sin hoja de precio y con un solo bloque de
  cronograma (no 3 módulos de varias horas).
- **Sin slide de precio**: se elimina por completo la sección `.s-price` y sus campos AcroForm
  asociados (Programa, Notas, Cotización). `generar-pdf.sh` omite el marcador "Propuesta
  Económica" con gracia cuando no está presente (mismo comportamiento ya visto en otros
  decks al omitir "Inversión por fases" cuando no aplica) — no requiere ningún ajuste al
  script compartido.
- **Sin roadmap ni `.ruta`**: al ser una sola sesión (no varios bloques secuenciales), no
  aplica el indicador de progreso `.ruta` ("Bloque 1 de 3") que sí usa CAI-002 — el cronograma
  es una sola slide autocontenida.
- **Programa**: 3 tarjetas representan los 3 segmentos de la misma sesión (Panorama
  estratégico · Práctica guiada · Cierre y autonomía), no 3 módulos multi-hora como en CAI-002.
- **Sin mención de Copilot**: única propuesta de la cuenta enfocada exclusivamente en Claude,
  porque el grupo de entrada (12 directores) tiene licencia propia de esa herramienta
  específica — no cross-ecosistema como el resto de la cuenta.
- **Impacto (§4.9)** — mismas fuentes que el resto de la cuenta Simple TV, por consistencia:
  Microsoft, *Work Trend Index 2024*; MIT — Noy y Zhang, *Science* 2023; Anthropic —
  investigación sobre uso de Claude Code. Se ajusta el copy del *hook* para hablar de
  decisiones ejecutivas en vez de tareas operativas.
- **Tono de Cierre y Próximos pasos ajustado**: al ser un regalo (no una decisión de compra),
  el CTA cambia de "Esperamos tu respuesta" a un tono de coordinación de agenda, y "Cómo
  arrancamos" se limita a logística de la sesión única (fecha, sala, participantes) — nunca
  menciona acuerdos económicos, igual que el resto de la cuenta (§4.15), pero aquí ni siquiera
  hay una decisión de compra que esperar.
- **Correo de cierre**: `servicio@intezia.com`. **Sin Metodología ABR ni Equipo facilitador**
  (§4.10a).

## Pendientes

- Confirmar fecha y sala con Neliana para la sesión única presencial.
- Confirmar si los 12 directores asisten juntos en un solo grupo o se divide en 2 turnos de 6
  (no especificado por el usuario — se asume 1 solo grupo de 12 salvo indicación contraria).
- Tratamiento económico: fuera de este documento, lo define la asesora (instrucción explícita
  del usuario).
