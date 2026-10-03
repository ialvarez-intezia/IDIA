# Brief — Venemergencia · Agente Personal para Andrés Simón (CAI-028)

## Datos administrativos

- **Empresa**: Venemergencia (empresa venezolana de servicios de emergencia y atención)
- **Slug**: `venemergencia-agente-personal`
- **División Intezia**: `educacion` (mismo criterio que el resto de propuestas de
  Venemergencia — ver `venemergencia/brief.md`)
- **Servicio (§4.1a)**: `habilidades` — **interpretación documentada, no un encaje exacto**.
  Ver sección "Nota de clasificación" abajo.
- **Alianza**: `true` — Venemergencia ya tiene marco de alianza con Intezia (dato existente
  en `venemergencia/brief.md`), no se volvió a preguntar por ser un hecho ya establecido en
  el sistema.
- **Tipo de documento**: Desarrollo de Agente Personal (`CAI-028`, dado directo por el
  usuario).
- **Destinatario**: Andrés Simón.
- **Asesora comercial Intezia**: María Iribarren · +58 414-0570056 · miribarren@intezia.com
  (confirmado por el usuario: "la asesora comercial es maria" — coincide con la asesora ya
  registrada para Venemergencia en el sistema).

## Fuentes

1. **Instrucción directa del usuario** (2026-09-24): construir la propuesta para Andrés
   Simón / Venemergencia, código CAI-028, kick-off el 6, sesiones martes y jueves a partir
   del 12.
2. **PDF de referencia**: "Cotización Propuesta Agente Personal Gabriel Cohen" — propuesta de
   **otro cliente** (Gabriel Cohen, no relacionado con Venemergencia hasta donde se sabe),
   en un **formato viejo** (fondo oscuro con degradado, sin AcroForms, cotización en REF/Bs a
   tasa BCV Euro, distinto a la paleta y mecánica de AcroForms del sistema). El usuario pidió
   explícitamente tomar sus puntos (estructura y alcance funcional) y adaptarlos al formato
   canónico de Intezia.
3. **Informe de actividades diarias** (Ing. David Prato, 2026-03-27) — bitácora técnica de
   trabajo YA REALIZADO para un cliente distinto ("Constructora Sambil", cuenta
   gabriel.cohen2010@gmail.com). El usuario confirmó explícitamente usarlo **solo como
   contexto técnico general** de cómo funciona el producto "Agente Personal" de Intezia por
   dentro (OpenClaw + WhatsApp + integración GoG/Google Workspace + archivos de memoria
   MEMORY.md/TOOLS.md/SOUL.md/AGENTS.md) — **nada de ese informe se atribuye a Andrés Simón
   específicamente**, ya que es de otro cliente y otra fecha.

## Decisiones de diseño confirmadas por el usuario (2026-09-24, vía preguntas directas)

1. **Código**: CAI-028 (CAI-027 ya estaba tomado por `banco-activo-cerebros-digitales/`,
   construida el mismo día — se preguntó y el usuario confirmó CAI-028).
2. **Punto de partida — construcción nueva desde cero**: a diferencia de Gabriel Cohen (una
   "optimización y ampliación" de un asistente ya existente), Andrés Simón **no tiene** un
   asistente previo. Todo el copy se redactó en clave de "diseñar y construir", nunca
   "evolucionar" o "ampliar".
3. **Alcance funcional — el mismo que Gabriel Cohen**: operación en múltiples grupos de
   WhatsApp, gestión de contactos, automatización de correos, control de consumo de IA, sobre
   OpenClaw. Confirmado explícitamente por el usuario — se reutilizó el Objetivo y la
   Descripción de la Solución del PDF de referencia, adaptados a "construcción nueva" y
   personalizados a Andrés Simón/Venemergencia.
4. **Formato — canónico de Intezia**: paleta amarillo/negro/naranja, AcroForms editables
   (campos de precio vacíos para que la asesora los complete en Adobe), en vez del diseño de
   fondo oscuro degradado y precios estáticos en REF/Bs del PDF de referencia.

## Nota de clasificación (servicio, §4.1a) — pendiente de resolver a nivel de sistema

Este proyecto no encaja en ninguno de los 4 servicios del Modelo Intezia (Detección /
Habilidades / Políticas / Innovación): no hay diagnóstico previo (no es Detección), no hay
currículo ni adopción de un proceso por un equipo (no es Habilidades en su sentido estricto —
no hay certificado, no hay Seguimiento 30-60-90 de adopción), no es un paquete de gobernanza
(no es Políticas), y no es un modelo de permanencia recurrente (no es Innovación).

El propio PDF de referencia de Gabriel Cohen muestra por qué: su infografía de "Quiénes
somos" (página 2, no incluida en este deck) separa **Desarrollo** ("a la medida de
automatizaciones o agentes de IA") como una línea de negocio distinta de **Educación**, junto
a Consultoría/Fundación/Evento. El catálogo actual del sistema (`CLAUDE.md`,
`empresa/catalogo.md`, `empresa/tipos-de-documento.md`) no tiene una categoría para
"Desarrollo".

**Decisión tomada para poder completar el `meta.json` (campo obligatorio)**: `servicio:
"habilidades"`, por ser la más cercana — mismo razonamiento que ya se usa para un Cerebro
Digital (una IA personalizada construida para un individuo específico, ver
`banco-activo-cerebros-digitales/` CAI-027). Esto es una **interpretación, no una categoría
exacta** — si este tipo de proyecto se vuelve a repetir, vale la pena formalizar "Desarrollo"
como una categoría propia en el sistema (similar a como Políticas o Innovación ya están
documentadas en `empresa/tipos-de-documento.md §0`).

**Consecuencias de esta clasificación en el deck**:
- Sin certificado de participación INTEZIA (es una entrega de software, no una capacitación).
- Sin slide de Seguimiento 30-60-90 ni `.s-followup` (no hay adopción de currículo que
  verificar) — el rol de "acompañamiento después de la entrega" lo cubre la nueva slide de
  Mantenimiento y Soporte.
- Sin roadmap `.rmx-linear` ni slide de grafo relacional (`.s-graph`) — no aplican a este
  alcance.
- 8 slides en total (más corto que las propuestas de capacitación, apropiado para un
  proyecto de alcance más acotado y sin currículo).

## Slide nueva: "Mantenimiento y Soporte" (opcional)

Primera vez que se construye este tipo de slide en el sistema — contenido tomado del PDF de
referencia (`ALCANCE DEL SOPORTE`, `INCLUYE`/`NO INCLUYE`). Diferencias respecto al PDF
original:

- **Sin precio estático**: el PDF de Gabriel Cohen mostraba "520 REF (Pago en BS a tasa BCV
  Euro)" como cifra fija. Para Andrés Simón, dado que se adoptó el formato canónico (precios
  vacíos, la asesora los completa), **no se agregó un campo AcroForm nuevo para este precio**
  — habría requerido un script de personalización adicional (mecanismo similar al usado para
  la escalera de Cierre) para una sola cifra opcional. En su lugar, se dejó una nota de texto:
  "Cuota mensual, se cotiza aparte de esta propuesta con tu asesora comercial" — describe un
  proceso real (la negociación de este add-on es aparte), no inventa un dato omitido por el
  usuario.
- **CSS nuevo**: `.s-maintenance` en `overrides.css`, reutiliza el fondo/eyebrow/h2 de
  `.s-steps` (mismo `<section>` con 2 clases) y agrega solo las columnas Incluye/No incluye.

## Calendario de inicio

Instrucción directa del usuario: *"el kick off lo colocas para el 6 y las sesiones martes y
jueves a partir del 12"*.

- **Mes asumido: octubre de 2026** — el usuario no lo especificó; se asumió por continuidad
  con el resto de las propuestas construidas en esta misma sesión (todas en el rango
  septiembre-diciembre 2026). **Confirmar antes de enviar.**
- **Kick-off**: martes 6 de octubre, 10-11.
- **Sesiones**: como el 12 de octubre es lunes (no martes ni jueves), la primera sesión
  martes/jueves real cae el **martes 13 de octubre** — mismo criterio ya aplicado en
  `banco-activo-cerebros-digitales/` y `banco-activo-deteccion-negocios/` cuando la fecha de
  inicio dada no coincide con el día de la semana pedido.
- **6 sesiones** (martes y jueves, 13 oct → 29 oct), una por cada fase técnica del proyecto
  (auditoría/configuración, integración con Google Workspace, memoria y comportamiento,
  operación multigrupo, validación funcional, ajustes y entrega). **Esta división en 6 fases
  es una interpretación** para poder llenar el ritmo martes/jueves pedido — no viene de un
  desglose de alcance/horas dado explícitamente por el usuario. Confirmar antes de enviar.
- **Sin fecha de "Reporte Final" ni de inicio de Mantenimiento**: no se inventaron fechas más
  allá de lo pedido.

## Actualización — "OpenClaw" generalizado (2026-09-24)

A pedido del usuario, se retiró el nombre "OpenClaw" de todo el contenido de cara al
cliente (`index.html`, `acroforms.json`, `programa.md`, `meta.json`) y se reemplazó por
"la plataforma de automatización" / "una herramienta de automatización", para no atar la
propuesta a una plataforma nombrada específica. El nombre se conserva únicamente en el
comentario interno de documentación al inicio de `index.html` (fuentes del deck, no se
imprime) y en las notas históricas de `brief.md` que registran de dónde salió el contenido
original. Trío regenerado y verificado tras el cambio (sin overflow, sin bugs nuevos).

## Trío ejecutado y verificado (2026-09-24)

`verificar-propuesta.sh` OK (sin desbordes) → `generar-pdf.sh` → `customize-acroforms.py` →
`customize-venemergencia-agente-personal.py`. Revisión visual de las 8 slides. PDF: "CAI-028
De todo a mano, a un asistente que ya lo resolvió..pdf".

**Bugs encontrados y corregidos durante la construcción**:
- **Marcador "Lo que se llevan" en singular**: se escribió inicialmente "Lo que se lleva"
  (por tratarse de una sola persona) — `agregar-campo-precio.py` busca el texto literal en
  plural y no encontró la marca, dejando "Lo que se llevan" fuera del PDF en el primer
  render. Corregido a plural (bug ya documentado, memoria
  `bug-marcador-lo-que-se-llevan-fijo`).
- **`<strong>` dentro de un `<li>` de `.s-goals .specifics`**: rompió el layout del 4to
  objetivo específico (el texto "OpenClaw" se desplazaba fuera de la línea). Quitado el
  `<strong>` (bug ya documentado, memoria `bug-strong-flex-specifics` — nuevo caso, en
  Objetivos, no solo en Beneficios/Cronograma).
- **Colisión "Duración"/"PROGRAMA" en Propuesta Económica**: el texto de Duración
  ("...aproximadamente 4 semanas...") wrapeaba a 3 líneas por la palabra larga
  "aproximadamente", montando el rótulo "PROGRAMA" encima. Acortado a "unas 4 semanas" (bug
  ya documentado, memoria `bug-price-block-programa-absolute`).
- **Título de portada, primera línea larga**: "De responder todo uno por uno," (31
  caracteres) forzaba un wrap antes del `<br>` explícito y desbordaba la slide. Acortado a
  "De todo a mano," (bug ya documentado, memoria `bug-punto-final-fuera-de-span-flota` /
  patrón de primera línea de h1 >~20 caracteres).
