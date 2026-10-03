# Brief — Andrómeda

---

## Actualización 2026-09-30 — 6 áreas transversales, acotadas a 2 líneas de negocio

Instrucción directa del usuario: *"Las áreas transversales que debemos cubrir son: Legal,
Talento Humano, Finanzas, Tecnología, Publicidad Digital (Mercadeo), Transformación Digital.
En relación con las líneas de negocio, consideraría para este primer alcance a Conectium/
Spinmovil y Ekiipago/Neoplata."* Antes de aplicar, se confirmaron 3 puntos con el usuario
(preguntas directas, dada la magnitud del cambio):

1. **Las 6 áreas REEMPLAZAN a las 3 anteriores** (Finanzas, Legal, Mercadeo), no se suman.
   Esto revierte la exclusión previa de Tecnología y Transformación Digital: la ficha original
   las dejaba fuera de la Detección por ser "ya las más avanzadas" a nivel corporativo, pero
   esa exclusión aplicaba a Andrómeda Tech/Transformación Digital como equipo central — no a
   cómo operan esas mismas funciones dentro de cada línea de negocio, que es lo que ahora se
   audita.
2. **Las 2 líneas de negocio (Conectium/Spinmovil, Ekiipago/Neoplata) acotan el universo de
   cada área, no multiplican sesiones.** Sigue siendo 1 sesión de 4h por área (no 1 por línea
   de negocio) — el diagnóstico de cada una de las 6 áreas se limita a procesos y personas de
   estas 2 líneas de negocio en esta primera fase, no a todo el holding.
3. **Políticas también amplía su alcance** a estas 6 áreas / 2 líneas de negocio — antes
   limitado a "Andrómeda Tech, Transformación Digital y Finanzas" (ver sección original más
   abajo, no actualizada retroactivamente en su redacción pero superada por este alcance).

**Nuevo dimensionamiento**: 6 áreas × 4h = 24h + 2h Fundamentals = **26h de Detección** (antes
14h). Políticas sigue por entregable, no por horas (sin cambio de criterio).

**Publicidad Digital vs. Mercadeo**: el usuario escribió "Publicidad Digital (Mercadeo)" — se
usa "Publicidad Digital" como nombre del área en el deck (el término que el usuario dio
primero), entendiendo que es la función que antes se nombraba genéricamente "Mercadeo".

**Aplicado a**: portada, diagnóstico, objetivos, programa, roadmap, ambos cronogramas,
beneficios, impacto, propuesta económica (Duración), próximos pasos y cierre — todas las
menciones a "Finanzas, Legal y Mercadeo" o "3 áreas" se actualizaron a "6 áreas transversales"
(genérico) o a la lista completa donde correspondía. Verificado sin desbordes tras el cambio
(3 slides tuvieron que acortarse: Objetivos, Roadmap y Beneficios, todas por exceso de texto al
nombrar las 2 líneas de negocio repetidas veces — se dejó esa mención una sola vez por slide en
vez de repetirla en cada bloque).

## Actualización 2026-09-30 (continuación) — vuelta a mostrar cotización, "Inversión por fases"

Instrucción directa del usuario: agregar de nuevo la hoja de cotización y separar por servicio,
"así como lo hicimos en banco activo" (referencia a `banco-activo-deteccion-negocios/DET-021`).
Se aplica el mismo patrón "Inversión por fases" (marker propio de `agregar-campo-precio.py`,
grupo `FASE_PRICE_FIELDS`, origen CAP-098 IOED): 2 recuadros de precio del lado izquierdo, uno
por servicio del combo — **Fase 1 · Detección** y **Fase 2 · Políticas** — con una Inversión
total combinada a la derecha, Descuento urgente y ROI. Esto **supera** el ajuste 2026-09-21 de
abajo (sin cotización), que se conserva solo por trazabilidad.

- **Sin Garantía 30-60-90**: ese sello es exclusivo de servicio Habilidades
  (`seguimiento-30-60-90-habilidades.md`) — este combo es Detección + Políticas, sin
  Habilidades, así que no aplica.
- **Sin campo Programa**: el patrón `FASE_PRICE_FIELDS` no lo incluye (mismo criterio que
  DET-021). La cobertura de las 6 áreas y las 2 líneas de negocio queda resumida en `Notas`
  (antes vivía en `Programa`) — el detalle completo ya está en la slide de Programa (04/12) y en
  el Roadmap, no hace falta repetirlo en la hoja de precio.
- **Solo 2 fases (no 3)**: `PrecioFase3` queda huérfano del marker genérico y se elimina en
  `scripts/customize-andromeda.py`, que también reescribe el JS de `PrecioBase` para sumar solo
  Fase 1 + Fase 2 — mismo ajuste que `customize-banco-activo-deteccion-negocios.py` /
  `customize-go-pharma-cap030.py`.
- **CSS** (`overrides.css`): se reemplazó el bloque "sin cotización" (Programa/Notas a columna
  completa) por las coordenadas exactas de `.fase-price-row`/`.fase-price-frame`/columna de
  Cotización, portadas de `banco-activo-deteccion-negocios/overrides.css` — estas coordenadas
  matchean los `/Rect` fijos de Python, no se pueden ajustar a ojo sin romper la superposición
  campo-visible / campo-real.
- **Notas** se acorta a 2 bullets cortos (antes 3, con la lista completa de áreas) porque la
  caja de Notas en este patrón es más chica (110px de alto, no los 420px del layout "sin
  cotización") — capacidad confirmada contra el caso de Laboratorios Farma CAI-032
  (`bug-programa-acroform-cobertura-larga.md`: toda caja AcroForm multilínea se revisa siempre
  a ojo en el PDF renderizado, nunca solo con el detector de overflow del HTML).

## Ajuste 2026-09-21 — Propuesta Económica sin cotización (SUPERADO 2026-09-30, ver arriba)

A pedido explícito del usuario: se quitaron las 3 celdas de cotización (Propuesta + Inversión,
Descuento, TOTAL) y la línea "Cotización válida por 30 días" de la slide `s-price`. Programa y
Notas se agrandaron para ocupar el espacio liberado — cada una pasa a ocupar una columna
completa de la slide (Programa a la izquierda, Notas a la derecha, donde antes vivía la
Cotización), en vez de las dos cajas angostas apiladas del layout estándar.

- **HTML**: se quitó `.block-cotizacion`, los 3 `cot-label`/`cot-frame` y `.cot-validity`. Se
  conservó `.cot-terms-box` (aviso de términos y condiciones), con la vigencia de 30 días
  fusionada en su texto para no perder ese dato estándar (§3 políticas comerciales).
- **CSS** (`overrides.css`): `.block-programa`/`.programa-box` y
  `.block-notes-container`/`.notas-box` reposicionados a 2 columnas simétricas de altura 420px;
  `.cot-terms-box` bajado como banda de ancho completo al pie.
- **PDF** (`scripts/customize-andromeda.py`): los campos `PrecioBase`/`Descuento`/`PrecioTotal`
  se eliminan por completo (no solo se ocultan) con el patrón "kept_fields" — `generar-pdf.sh`
  los vuelve a crear cada vez que se regenera el PDF, porque `agregar-campo-precio.py` los
  agrega automáticamente al encontrar el marcador "Propuesta Económica" en el HTML (no hay forma
  de que el script compartido omita esos 3 campos sin tocarlo, y no se toca código compartido
  por un solo cliente). Los campos `Programa`/`Notas` se re-dimensionan a su `/Rect` nuevo — no
  usan apariencia horneada (`/AP`), así que no hace falta re-hornear texto, solo el rect.

## Datos administrativos

- **Empresa**: Andrómeda (holding multisectorial: fábrica/manufactura, tecnología con software
  factory propia, varias líneas de negocio)
- **Sector**: Holding multisectorial
- **Tamaño**: Mediana (50-250 empleados) — organización completa ~140 personas (incluye fábrica)
- **Slug**: `andromeda`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — combo Detección + Políticas cotizadas juntas bajo el código
  de entrada DET-016 (no `integral`: no son los 4 servicios como una sola hoja de ruta, es un
  combo parcial de 2, mismo criterio que DET-002 y otros combos de esta sesión).
- **Tipo de documento**: Detección (`DET-016`) · Fundamentals (2h grupal) + auditoría de 3 áreas
  (Finanzas, Legal, Mercadeo), 4 horas por área (14h totales de Detección) + Políticas como eje
  transversal (por entregable, no por horas).
- **Eje temático**: Diagnosticar el estado real de madurez de IA en Finanzas, Legal y Mercadeo
  sin caer en automatizaciones triviales, y avanzar por fin en el marco de gobernanza de IA que
  Andrómeda lleva más de un año y medio sin poder completar internamente.
- **Fecha del brief**: 2026-09-20
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Andrómeda**
(`Levantamiento_Andromeda_2026-09-18.pdf`, registrada 2026-09-17), elaborada por la asesora
**Verónica Rubio**, más una segunda ronda de contexto de reunión que la asesora aportó
directamente sobre stack técnico, dimensionamiento de horas y estructura de fases acordada con
el cliente.

## Contacto

- **Asesora comercial**: Verónica Rubio.
- **Contacto operativo / sponsor / firma**: Carlos Alonso · Liderazgo Andrómeda Tech /
  Transformación Digital — sponsor fuerte y decisor visible, firma y decide la contratación.
- **Patrocinio ejecutivo**: CEO Alfonso — mandato top-down explícito que baja hasta cada línea
  de negocio.
- **Servicio previo con Intezia**: ninguno — primer contacto.

## Decisión de alcance — bloqueante, confirmada por el usuario

**Esta propuesta cubre exclusivamente Detección (Finanzas, Legal, Mercadeo) y Políticas
(transversal).** El usuario lo confirmó de forma explícita tras compartir la ficha y las notas
de reunión: *"toma en cuenta lo que te di en la ficha comercial mas lo que te escribi de apoyo,
solo es para deteccion y piliticas"*.

**Habilidades queda fuera por completo de este documento** — ni cotizada ni con roadmap propio
— aunque tanto la ficha (Bloque F) como las notas de reunión la mencionan como fase 2 potencial
para Andrómeda Tech y Transformación Digital, a partir del diagnóstico. Se omite del deck salvo
una mención breve de contexto en Próximos pasos, sin comprometer alcance ni precio (mismo
criterio "no cotizado en este documento" que Toyocentro y Pilotes Perforados con su fase 2).

**Por qué no `integral`**: el cliente combina 2 de los 4 servicios (Detección + Políticas), no
los 4 como una hoja de ruta secuencial — el código DET- de entrada así lo confirma (§4.1a).

## Áreas de Detección (6 — actualizado 2026-09-30, ver "Actualización 2026-09-30" arriba)

1. **Legal**
2. **Talento Humano**
3. **Finanzas**
4. **Tecnología**
5. **Publicidad Digital** (antes nombrada genéricamente "Mercadeo")
6. **Transformación Digital**

Acotadas, en esta primera fase, a 2 líneas de negocio: **Conectium/Spinmovil** y
**Ekiipago/Neoplata**. (Sección histórica: la ficha original de 2026-09-18 solo cubría Finanzas,
Legal y Mercadeo, y excluía Andrómeda Tech/Transformación Digital a nivel corporativo por ser
"ya las más avanzadas" — esa exclusión no aplica a cómo operan esas funciones dentro de cada
línea de negocio, que es lo que se audita ahora.)

## Dimensionamiento (lineamiento por defecto — `empresa/politicas-comerciales.md`)

- **4 horas por área** × 6 áreas transversales = **24 horas**.
- **+ 2 horas de Fundamentals grupal**, antes de auditar por área (lineamiento por defecto de
  Detección, sin instrucción del cliente de omitirla).
- **Total: 26 horas** de Detección.
- **Atención**: el máximo de Fundamentals es 25 personas por sesión. Con ~15-20 en Finanzas y
  ~15-20 en Mercadeo (Legal sin headcount confirmado), el universo combinado podría superar el
  máximo si asisten todos los perfiles operativos de las 3 áreas juntos. **Pendiente de
  confirmar con Verónica antes de enviar**: si Fundamentals se dirige a líderes/representantes
  de cada área o si hace falta desdoblarla en más de una sesión de 2h (§ lineamiento). El deck
  queda redactado en términos genéricos ("dentro del máximo de 25 personas por sesión, con más
  sesiones si el universo lo supera") para no inventar una cifra de asistentes que la ficha no
  confirma.
- **Calendario**: la ficha registra disponibilidad de "una mañana (~3 horas) por área"; se
  interpreta como la ventana lograda para las sesiones de 45-60 min que suman esa mañana, y se
  concilia con las 4h/área acordadas en la reunión posterior (más específica y más reciente) —
  a coordinar el detalle exacto en Próximos pasos, sin inventar horario.
- **Modalidad**: no especificada de forma explícita en la ficha ni en las notas de reunión — se
  omite del deck (§ "Omitir, no inventar"), a diferencia de Toyocentro (presencial, dato
  explícito). Pendiente de confirmar con Verónica.
- **Sin logro inmediato forzado por sesión**: a diferencia de Toyocentro/Velas 3N (patrón
  "Fundamentals con logros inmediatos"), el cliente pidió explícitamente evitar quedarse en
  "automatizar procesos triviales que no valen la pena" (Bloque G). Las sesiones de área se
  redactan como **auditoría y diagnóstico real**, sin prometer una construcción/logro tangible
  dentro de la misma sesión — más cerca del patrón `pilotes-perforados/` (diagnóstico puro) que
  del patrón `toyocentro/` (diagnóstico + construcción de quick win).

## Políticas — eje transversal (por entregable, no por horas)

Contenido tomado de la especificación real del servicio (`empresa/tipos-de-documento.md §0.1`),
sin inventar estructura nueva — el combo Detección+Políticas representa a Políticas a nivel de
roadmap (una etapa + su entregable), no con una plantilla dedicada propia (esa sigue pendiente
de la decisión de formato Ivana+David, §0 de ese mismo archivo — no aplica aquí porque no es una
propuesta de Políticas *sola*).

- **Necesidad real, cita textual (Bloque D)**: *"Nuestra gobernanza está un poco escueta o
  deficiente. ¿Ustedes podrían ayudarnos en este servicio de política? es algo en el sentido de
  que hemos querido hacer y, dada la operatividad, no hemos culminado."* (Carlos / Francis).
- **Antigüedad de la brecha**: más de un año y medio (~1.5 años) sin poder cerrarla por cuenta
  propia, por falta de tiempo, no de interés (Bloque F).
- **Alcance (actualizado 2026-09-30)**: transversal a las mismas 6 áreas y 2 líneas de negocio
  de la Detección (Legal, Talento Humano, Finanzas, Tecnología, Publicidad Digital,
  Transformación Digital, en Conectium/Spinmovil y Ekiipago/Neoplata) — ya no limitado solo a
  Andrómeda Tech, Transformación Digital y Finanzas (alcance original de la ficha de
  2026-09-18, con foco en accesos sensibles como el ERP Odoo).
- **Framing normativo**: basado en el estándar **ISO/IEC 42001** (Sistema de Gestión de
  Inteligencia Artificial) y en el marco regulatorio europeo de IA y datos (**AI Act**,
  Reglamento Europeo de Inteligencia Artificial, y **RGPD**, Reglamento General de Protección
  de Datos) — mencionado por el cliente de forma imprecisa como referencia europea/normativa;
  se usan estos dos marcos reales y verificables en vez de la sigla ambigua que mencionó el
  cliente (§4.12, citabilidad).
- **Qué dispara la necesidad ahora**: riesgo de fuga de información al usar herramientas fuera
  del ecosistema autorizado (fuera de Claude/Anthropic), y necesidad de reglas claras de cuándo
  cada línea de negocio autónoma debe escalar al equipo transversal de tecnología, por
  gobernanza y seguridad, no solo por capacidad técnica.
- **Entregables reales del servicio** (§0.1): Informe de diagnóstico de madurez, Manual de
  políticas de uso responsable de IA, Matriz de riesgos y plan de acción, Marco de gobernanza
  (roles, permisos, responsables de aprobación), «Brújula IA» (recomendación de herramientas
  por área con su nivel de gobernanza requerido), sesión de socialización del manual.
- **Precio**: por entregable, no por horas (§0.1) — se combina con la cotización de Detección en
  una sola Propuesta Económica estándar (sin desglose "Inversión por fases": el cliente no pidió
  visibilidad modular, a diferencia de Maurel & Prom).

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: Google Workspace.
- **Uso de IA hoy — avanzado y disperso**: licencia corporativa de **Claude** (Anthropic) como
  estándar mínimo obligatorio, en proceso de dejar ChatGPT atrás; Gemini vía Google Workspace
  para tareas puntuales; en Tecnología, LangChain/LangGraph para agentes, Open Router para
  modelos open source, Claude Code para programación, "cerebros digitales" (Claude + Obsidian)
  que centralizan el conocimiento de cada líder/área; un colaborador corre un modelo local
  (Qwen 3.7) para datos clasificados que no deben salir a servidores externos; Figma con
  funciones agénticas en Transformación Digital; un piloto interno ambicioso ("secreto") para
  automatizar con agentes buena parte de su software factory.
- **Información del negocio**: varios sistemas separados por área; ERP **Odoo** con accesos
  restringidos para conectores externos (dato de contexto interno, no se nombra en el deck de
  cara al cliente salvo como "sus sistemas internos", mismo criterio que Toyocentro con Airtable/
  Azure Table).
- **Comunicación**: WhatsApp, Google Chat, correo corporativo.
- **Política de datos/seguridad**: existe una política básica con un gerente de ciberseguridad
  dedicado, pero cuesta mantenerla actualizada y vigilar que se aplique. Cuidan con especial
  atención datos financieros y legales.
- **Apetito de riesgo**: Moderado. **Apertura al cambio**: Alta. **Patrocinio ejecutivo**: fuerte
  y visible (Carlos Alonso, con mandato del CEO Alfonso).
- **Nivel de partida con IA**: muy desigual entre áreas — sin formación externa formal, cita
  textual: *"hemos trabajado muy empíricamente, hemos sido muy experimentales."*
- **Sin diagnóstico o auditoría previa de IA** — el conocimiento que tiene hoy el liderazgo de
  tecnología sobre Finanzas/Legal/Mercadeo es indirecto ("kinestésico").

## Objetivo final esperado del Reporte Final (cita/paráfrasis directa de la ficha)

Que el reporte identifique dónde la IA puede aportar valor real en cada área (más allá de
automatizaciones triviales) para priorizar con criterio la siguiente fase, y que el manual de
gobernanza permita consolidar la autonomía que ya tiene cada línea de negocio con reglas claras
de cuándo escalar al equipo transversal de tecnología — formalizando "IA champions" por
departamento y balanceando autonomía con protección de datos sensibles.

## Decisiones confirmadas / sin ambigüedad

1. **3 áreas de Detección** (Finanzas, Legal, Mercadeo) — la ficha lo declara directo, y excluye
   expresamente a Andrómeda Tech/Transformación Digital de esta fase por ser ya las más maduras.
2. **Políticas transversal, combo bajo DET-016** — confirmado dos veces por el usuario (mensaje
   inicial + aclaración explícita de alcance).
3. **Sin Habilidades en este documento** — confirmación explícita del usuario, aunque la ficha y
   las notas de reunión la mencionen como fase 2 potencial.
4. **Sin certificado de participación INTEZIA** en Entregables — Detección + Políticas es
   auditoría y gobernanza, no un curso (`deteccion-sin-certificado.md`).
5. **Sin nombre de herramientas de base de datos ni "Odoo" de cara al cliente** — se habla de
   "sus sistemas internos" (mismo criterio que Toyocentro).
6. **Sin slide de Mapa de Calor** ni Metodología ABR ni Equipo facilitador expuestos (§4.10a).
7. **Framing normativo de Políticas**: ISO/IEC 42001 + AI Act + RGPD (marcos reales,
   verificables), no la sigla ambigua que mencionó el cliente en la reunión.

## Pendientes (a confirmar con Verónica antes de enviar)

- **Modalidad** de las sesiones (presencial / online / híbrida) — no está en la ficha.
- **Fecha y hora** exactas de las 4 sesiones (Fundamentals + 3 áreas) — se coordinan en "Cómo
  arrancamos", no se inventan.
- **Universo exacto de Fundamentals**: si asisten los ~15-20 de cada área o solo líderes/
  representantes — definir antes de cerrar si hace falta más de 1 sesión de 2h (máximo 25/sesión).
- **Headcount de Legal**: no especificado en la ficha — no se usa ninguna cifra para esa área
  en el deck.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education (Detección) + Consultor líder de Políticas.
- **Asesora comercial**: Verónica Rubio.

## Notas internas

- Caso base estructural: `toyocentro/` (DET-014) — mismo patrón de Fundamentals + N áreas a 4h,
  roadmap `.rmx-linear` de 3 etapas, Beneficios v3, Cierre escalera, precio estándar. Adaptado a
  3 áreas (no 2) y a un combo con Políticas: la Etapa 2 del roadmap pasa de "Priorización" a
  "Políticas" (construcción del marco de gobernanza), y la Etapa 3 "Reporte Final" integra tanto
  el Mapa de Calor de Detección como el Manual de políticas + Brújula IA.
- **Sin "logro inmediato" forzado por sesión** (a diferencia de Toyocentro) — instrucción
  explícita del cliente de evitar automatizaciones triviales; la cronograma de "Estructura de
  las 4 horas por área" se redactó como auditoría/diagnóstico real, no diagnóstico+construcción.
- Impacto (§4.9, ambos verificados por WebSearch 2026-09-20): McKinsey — The State of AI 2025
  (noviembre 2025): 88% de empresas ya usa IA en al menos una función, pero solo un tercio ha
  escalado sus programas a nivel empresarial (dos tercios siguen en prueba/prueba de concepto);
  68% usa IA en más de una función; el reporte de abril 2025 de McKinsey encontró que 70% de los
  equipos de Finanzas y Estrategia reportó aumento de ingresos por IA generativa en la segunda
  mitad de 2024, el impacto de ingresos más alto entre funciones de la encuesta. + Pacific AI —
  2025 AI Governance Survey: 75% de las organizaciones ya tiene políticas de uso de IA, pero
  solo 36% cuenta con un marco de gobernanza formal, y solo 59% tiene roles de gobernanza
  dedicados — brecha que responde directo al "gobernanza escueta o deficiente" que el propio
  cliente reconoce.

## Pendiente futuro (no cotizado en este documento)

Habilidades para Andrómeda Tech y Transformación Digital, a partir de los hallazgos del
diagnóstico — mencionada solo como nota interna/contexto de venta, mismo criterio "no cotizado"
que el resto de las Detecciones de esta sesión.
