# Aprendizajes — histórico archivado

> Archivo histórico del changelog. Entradas de **2026-05-29 y anteriores** (+ algún entregable puntual recolocado).
> Todas describen decisiones **ya codificadas** en `CLAUDE.md`, las plantillas o los scripts; varias describen
> estados ya **superados** (formato vertical, 16 campos AcroForm, deck de 11 slides, defaults como placeholders).
> Se consulta solo para trazabilidad histórica puntual. El changelog activo está en `aprendizajes.md`.

---

## 2026-05-29 — [cliente:go-pharma] Mismo programa para 2 cohorts secuenciales: encuadre «misma capacitación, momentos distintos», sin fechas

**Ajuste del cliente** a go-pharma (CAP-030): pasar de sesión única (30 personas) a **dos grupos de 15** «manteniendo el formato original pero optimizando la logística». **Confirmado con el usuario que es secuencial** (un grupo y luego el otro, **un solo facilitador**), no simultáneo → **cambio superficial: el contenido, los 3 módulos y la carga cognitiva por sesión NO se tocan** (la malla 3×4 h ya está bien balanceada; bajar a 15 personas incluso refuerza el argumento de «tutoría activa» del ABR). Solo se reencuadra el mensaje. **Lo que pidió el usuario explícitamente:** (1) **no mencionar fechas** («no sé las fechas») → se quitó el «inicio 2 de julio» de portada y Paso 01, y el `brief.md` pasó a «Fecha de inicio: por confirmar»; (2) decir **claramente que es para ambos grupos y que reciben la misma capacitación en momentos distintos**. **3 edits:** portada lead («El equipo se divide en dos grupos de 15 personas; cada grupo recibe la misma capacitación completa, en momentos distintos»), Duración de la Económica («**12 horas por grupo**» en vez de «en total» — resuelve la ambigüedad: son horas por colaborador, no facilitación total de 24 h; ver [[feedback_horas_por_persona_multicohort]]), y Paso 01 body (≤130 chars). **Regla general:** cuando una capacitación se parte en cohorts que cursan el MISMO programa, el deck lo expresa como «misma capacitación, momentos distintos», las horas se dan **por grupo** (no totales), y si las fechas no están definidas no se comprometen en el deck. Par PDF-customize corrido, verificador OK, PDF revisado slide por slide.

## 2026-05-28 — [cliente:fivenca] Giro de ventas: primera entrega = capacitación 4 h mono-fase (no las 3 fases)

**Ventas corrigió** la propuesta multi-fase: la primera entrega acordada con el cliente es **solo la capacitación de Fundamentals con enfoque en productividad y efectividad, de 4 h** («no hablamos de las 3 fases de una vez sino iniciar con la capacitación de 4 horas»). **Reconversión:** el deck multi-fase (14 slides, clon BDV) → **mono-fase de 11 slides** (clon estructura cumbre-andina sobre el mismo `styles.css` local): Portada, Pain, Objetivos, Programa (3 bloques en 4 h), Cronograma (1 sesión de 4 h, **sin `.ruta`** de multi-fase), Metodología, Beneficios+Equipo, Impacto, Económica, Pasos, Cierre. Las 3 fases quedan en `brief.md` como **visión futura, NO en el deck**. **Aprendizaje de proceso:** cuando la ficha y la minuta dan señales mixtas (ficha decía «4 h» pero la minuta describía 3 fases), el «4 h» era literal → conviene confirmar con ventas el ALCANCE de la PRIMERA entrega antes de construir el deck completo. **Dos defectos que el detector automático NO ve y solo salieron en revisión visual del PDF:** (1) la Duración de la slide Económica con 3 líneas **se solapaba** con la etiqueta «Programa» (absolutamente posicionada) → acortar a ≤2 líneas; (2) título de Paso «Aprueban la capacitación CAP-039» (32 chars) **se recortó** en el campo single-line (~30 char máx) → «Aprueban la capacitación». Confirmado lo de [[feedback_overflow_visual]]: revisar el PDF slide por slide aunque el script pase.

## 2026-05-28 — [cliente:fivenca] Plan Integral IA 3 fases (CAP-039) · Microsoft sin Copilot · eje multi-herramienta

**Fivenca** (grupo financiero, casa de bolsa) creado de la ficha «Preguntas Clave» (solicitante **María Iribarren**) + minuta de reunión. Consultor **Andres Fornerino**, asesora **María Iribarren**. La ficha pedía «Capacitación In-Company» + «4 h» + 40 personas (2 grupos de 20), pero la minuta de Intezia describía explícitamente la **propuesta de valor en 3 fases** (Fundamentos → Especialización por áreas → Gobernanza). Decisión: **plan integral multi-fase lineal** clonando **bdv/CAP-024** (multi-fase financiero), interpretando «4 h» como la duración de la **Fase 1 por cohort**. **Eje delicado — Microsoft sin Copilot:** marcaron Microsoft como ecosistema pero aclararon «no hay nada oficial y **no les gusta Copilot**» → eje **multi-herramienta ecosistema-agnóstico** (Claude, ChatGPT, Gemini) **integrado a su entorno Microsoft 365**, sin empujar Copilot y sin afirmar migración (§4.11). El diagnóstico cita el uso factual de herramientas (de la minuta) y los 5 dolores reales (uso sin método, nivel desigual, correos manuales, falta de AUP, costos por créditos). Deck de **14 slides**: se **omitió la slide roadmap bespoke de BDV** (fork F2/F3 áreas-vs-tecnología) por ser un plan **lineal**; la visión de 3 fases vive en el Mapa del Plan (slide 4). **Bug 5-6 módulos otra vez:** la slide 7 (5 áreas en `s-program`) desbordó porque el `styles.css` local clonado de BDV **tampoco compacta 5-6 módulos** (solo `min-height`, mismo bug que `_base`); fix: añadida compactación 5-6 (padding 64px, roman 54px, h3 22px, obj 13px, topics 15px) directamente en el `styles.css` local del deck. Pasos de arranque solo-logística (§4.15), Entregables/Acreditación pre-llenados, apartado comercial vacío. Verificado sin desbordes.

## 2026-05-27 — [regla] Cronograma SIEMPRE en formato canónico (_base + .ruta/.timebar/.ses-cols), nunca el desglose viejo de tabla

**Defecto detectado por el usuario** en `sfic` (DIP-006): la slide de Cronograma salió con el **desglose instructivo viejo** (tabla `Módulos/Tiempo/Estrategias/Recursos` en grid). **Causa raíz:** se clonó de **DIP-002 PDVSA**, que tiene `styles.css` local antiguo y el formato de tabla viejo. El **formato canónico vigente** es el de **cumbre-andina**: una slide por sesión/fase con `.ruta` (nodo + track + `.ruta-fill` width% + `.ruta-step` «Fase N de M»), `.ses-head` (`.ses-mod` + h2 + `.ses-dur`), `.ses-body` con `.ses-block`→`.chips`, `.ses-block`→`.timebar` (`.seg` con `flex:`), y `.ses-cols` (3 `.ses-block`: enseñanza, aprendizaje, recursos con `.block-rec`). **Estas clases viven solo en `clientes/propuestas/_base/styles.css`**, no en los `styles.css` locales viejos. **Regla dura para Curso/Diplomado y cualquier deck nuevo:** (1) enlazar `../_base/styles.css` + `overrides.css` local, **nunca** copiar el `styles.css` de DIP-002/decks viejos; (2) el cronograma se arma con el bloque `.ruta`/`.ses-head`/`.timebar`/`.ses-cols`, una slide por fase (diplomado multi-fase = N slides de cronograma); (3) referencia de clonado correcta: **cumbre-andina** (mono-fase) / **pilotes-perforados** (multi-fase), no PDVSA. **Fix aplicado a sfic:** reescritas las 2 slides de tabla → 6 slides canónicas (1 por fase), deck 13→17 slides, CSS local borrado y enlazado `_base`. Como `_base` no compacta `s-program` de 5-6 módulos ni `s-goals` de 6 específicos, se añadió compactación en `overrides.css` (patrón de corpoez-cu009 para Programa + reducción de h2/general/gap para Objetivos).

## 2026-05-27 — [cliente:corpoez-cu009] Curso CU-009 que fusiona dos talleres de catálogo (IESA In Company)

**Corpoez · Inteligencia Artificial para Líderes (CU-009)** creado de la ficha «Preguntas Clave» (Flavia Martínez). La ficha marcó «Taller In-Company» pero seleccionó **dos** productos de catálogo (TA-003 Fundamentals + TA-004 Executive Masterclass), 18 h / 3 sesiones, y el archivo se llamaba CU-009 → **pregunté y el usuario confirmó Curso CU-009**, con **arco nivelación → productividad → estrategia** (1 sesión de 6 h = 2 módulos). Relación «IESA in company - Corpoez»: **Corpoez es el cliente, IESA acredita** (doble cert INTEZIA + IESA), Intezia ejecuta. Consultor **Juan Figuera**, asesora **Flavia Martínez**. **Decisión de clon:** en vez de clonar el CU más reciente (PDVSA CU-006, CSS viejo, sin slide de Impacto, pasos pre-§4.15), cloné el **canónico cumbre-andina** (`_base/styles.css`) y le **añadí el slide de Evaluación (`s-eval`)** porque `_base` ya soporta sus estilos (15 reglas) además de `s-impact`. Resultado: deck de 14 slides con Impacto + Evaluación, todo sobre `_base`. **§4.11:** cliente sin licencias previas; el deck enmarca Claude + Gemini como herramientas del curso, nunca dice que Corpoez migra/ya usa. **§4.12:** RCTF glosado en Objetivos (slide 3); en chips/títulos sin espacio (Programa, sesiones, Entregables) se escribió natural («Estructura del prompt», «Prompting estructurado», «Uso aceptable de IA») en vez de la sigla cruda; AUP queda glosado en la sesión 3 vía la chip «Política de Uso Aceptable»; FODA se deja (sigla de uso general del sector). **AcroForm Entregables desbordaba** al render (líneas destacadas de 2 renglones recortaban la última institucional) → acortadas a un renglón cada una; el detector automático NO ve este desborde de campo, solo la revisión visual del PDF. Deck verificado sin desbordes.

> Detalle bug `_base` 5-6 módulos: ver entrada `[bug]` de esta misma fecha.

## 2026-05-27 — [bug] `_base` no compacta el grid de Programa para 5-6 módulos

La slide `s-program` de `_base/styles.css` tiene modo compacto completo (padding + fuentes reducidas) para **4 módulos** y para **7-9 módulos**, pero la regla de **5-6 módulos** (línea ~481) **solo fija `min-height`** y deja el padding base de 80px y las fuentes grandes → 6 módulos con 5 temas desbordan +130/+180px. Como `_base` es CSS compartido y ningún deck previo usaba 5-6 módulos sobre `_base`, lo resolví con un **`overrides.css` local** en `corpoez-cu009/` que completa el modo compacto 5-6 (padding 48px, roman 42px, h3 17px, obj 11.5px, topics 12.5px). Si vuelve a aparecer un deck de 5-6 módulos sobre `_base`, conviene **portar este bloque a `_base`** como fix central. Patrón general: lo propio del deck va en `overrides.css`, no se toca `_base` sin necesidad (§6).

## 2026-05-27 — [cliente:sfic-comunicacion-marketing] Segundo diplomado SFIC (DIP-007 Comunicación, IA y Marketing)

**SFIC + Intezia · Diplomado en Comunicación, IA y Marketing Exponencial** creado de un PDF que el cliente entregó (alianza académica SFIC, **18 módulos en 7 fases**, 40 h, online, 800 USD/participante, reparto 50/50). Clonado de **DIP-005 UNE** (alianza académica universidad + Intezia, doble certificación, multi-fase). **Colisión de slug atrapada:** ya existía `clientes/propuestas/sfic/` (otra propuesta SFIC, «Productividad del Negocio», **DIP-006**) que un proceso paralelo estaba construyendo en simultáneo. Para no chocar usé slug propio **`sfic-comunicacion-marketing`** y código **DIP-007** (la de Productividad se quedó con `sfic`/DIP-006). Pendiente: confirmar con el usuario la convención de códigos/slugs cuando un mismo cliente tiene varios programas. **Decisiones del usuario:** (1) branding solo Intezia, SFIC textual (precedente UNE); (2) slide a la medida `.s-responsibilities` «Cuadro de Responsabilidades INTEZIA/SFIC» (tabla 3 col modelada sobre `.s-eval`, CSS local en `styles.css`); (3) **cambió de opinión a mitad:** primero pidió pre-llenar 800 USD/50-50, luego **dejar el apartado comercial vacío** para ventas (convención estándar) → el customize NO toca precio, solo Entregables/Acreditación/Pasos; asesora **Isabella Palazzone** al cierre. **Programa de 18 módulos representado como 7 fases-card** en una sola `.s-program` (modo compacto 7-9 del grid, `:has(nth-child(7))`); las 3 filas desbordaban +57px → override local que comprime padding/gap/fuentes solo de este deck (styles.css es local al clon). **§4.12:** RTF/SEO/ROI glosados; en chips de `.s-program` (sin espacio) se escribió natural («Ingeniería de Prompts I» en vez de «marco RTF») porque la sigla no cabe glosada. **§4.13:** los headers de `.s-schedule` salieron con guion largo («Fase I — …») → cambiados a dos puntos. **Cronograma rehecho al formato canónico (cumbre-andina)** tras feedback del usuario: salió primero con el desglose viejo del clon DIP-005 (`.sessions/.session/.grid`, 2 slides) → reescrito a **1 slide por fase (7 slides)** con `.ruta` (nodo + cinta de progreso) + `.ses-head` + `.chips` + `.timebar` (segmentos `flex:`, colores 3n) + `.ses-cols` (enseñanza/aprendizaje/recursos `.block-rec`). Ver la [regla] de esta misma fecha. **Diferencia con el fix de `sfic`:** ese deck se reenlazó a `../_base/styles.css`; este deck conserva su `styles.css` local (cloné DIP-005, que trae overrides propios de s-goals/s-program/s-responsibilities que no están en `_base`) y **porté el bloque `.s-schedule` de `_base` al local**, borrando el viejo. Mismo resultado visual. Deck final **18 slides**, sin desbordes, verificado. Pendiente opcional: migrar este deck a `_base` para alinearlo 100% con la regla.

## 2026-05-27 — [cliente:sfic] Conversión de PDF de alianza al formato canónico (Diplomado DIP-006)

**SFIC × Intezia · Diplomado para Aumentar la Productividad del Negocio** creado a partir de un PDF que el cliente entregó (alianza académica SFIC, 18 módulos en 6 fases, 800 USD/participante, reparto 50/50). Clonado de **DIP-002 PDVSA** (mismo eje: IA y productividad, doble certificación). Decisiones del usuario: (1) **propuesta de alianza completa** → slide a la medida `.s-resp` «Cuadro de Responsabilidades Intezia/SFIC» (tabla 3 columnas modelada sobre `.s-eval`, en `overrides.css`); (2) **branding solo Intezia** (logos Intezia, SFIC textual como aliado, glosado «South Florida International College (SFIC)»); (3) **precio pre-llenado** 800 USD + nota de reparto 50/50 en el customize (excepción a la convención de dejar precio vacío). **Programa de 6 fases** → 6 `.module` caen en el modo grid 3×2 del CSS (`:has(nth-child(5)):not(nth-child(7))`), chips ≤~28 chars, sin desborde. **Dos gotchas atrapados en revisión visual:** (a) en `overrides.css` **NO** poner `position: relative` sobre `.s-<slide> .counter` — el `.counter` base ya es `position:absolute; z-index:10`; al volverlo relative cae al flujo (top-left) y solapa el eyebrow. Solo darle z-index si hace falta, sin tocar position. (b) **título de Próximos pasos** (campo AcroForm de una línea) se recorta a ~20 chars: «Confirmas fechas y cohorte» y «Coordinamos acceso y logística» se cortaban → «Fechas y cohorte» y «Acceso y logística». Fuentes Graphit no están en el repo (todo deck cae a Inter, normal). Carpeta plana `sfic/` (paths 3 `../`); ojo: al copiar `styles.css` de un deck 4-deep hay que corregir el path de `@font-face` de `../../../../fonts/` a `../../../fonts/`.

## 2026-05-26 — [cliente:hca-venezuela-cap015] Migración al formato canónico + aplanado de carpeta

**HCA Venezuela CAP-015** (Claude Cowork · Dominio Corporativo) llevada del formato viejo (10 slides, CSS local de 37KB, cronograma en una sola slide apretada, sin Impacto) al **formato canónico cumbre-andina** (13 slides). Cambios: (1) **CSS** → `../_base/styles.css` + `overrides.css` local (solo el agrandado de cajas Programa/Notas). (2) **Cronograma** → 3 slides de desglose instructivo (1 por día) con `.ruta` + `.ses-head` + `.chips` + `.timebar` + `.ses-cols`; el Día 2 (4 áreas × 1h) quedó en una sola slide con 4 segmentos de timebar. (3) **Slide de Impacto nueva** (§4.9) con datos reales citados verbatim: McKinsey State of AI 2025 (+45% satisfacción, 78% adopción), Harvard/BCG Dell'Acqua et al. 2023 (+40% calidad, 25% más rápido), NBER Brynjolfsson/Li/Raymond 2023 (+34% noveles, +14% soporte). (4) **CTA** → botón-hipervínculo Calendly (antes `<span>` plano). (5) **§4.15** Paso 02 «Firmamos acuerdo/factura 50%» → «Acceso y logística». (6) **§4.12** «(ABR)» glosado a «Aprendizaje Basado en Retos (ABR)» en Acreditación. **Aplanado de carpeta** (decisión del usuario): de la sub-subcarpeta `hca-venezuela/CAP-015 Claude Cowork - Dominio Corporativo/` (que generaba falsos positivos del verificador y nombres raros) a `hca-venezuela-cap015/` plano; arregla rutas (logos `../../../`, CSS `../_base`) y los scripts. **Overflow atrapado por el detector:** los `topics` del Programa (chips nowrap) desbordaban +26 a +60px con texto largo («1.1 Panorama IA 2026 · Por qué Claude») → acortados a ≤~26 chars («1.1 Por qué Claude en 2026», «2.1 Ventas»). Los chips del cronograma (s-schedule, flex-wrap) sí admiten texto largo. Nota técnica: `bar-fill--out` no existe en `_base` → para barras de impacto usar valores ≥~30% (evita la barra angosta) en vez de portar esa clase.

## 2026-05-26 — [preferencia] Ventas pide agrandar cajas Programa/Notas de la slide económica (HCA Executive + HCA Venezuela)

Ventas solicitó **más espacio para escribir** en las cajas editables `Programa` y `Notas` de la slide `s-price`, sin scrollear dentro del campo. La caja visible **es el widget AcroForm** (el `.multi-box` del HTML es transparente), así que agrandar requiere cambiar **dos cosas en sincronía**: (1) el alto/posición de `.programa-box` / `.notas-box` + el `top` de `.block-notes-container` en el `styles.css` local (para que el rótulo estático "NOTAS" baje con la caja), y (2) el `/Rect` del widget en pt (conversión px→pt factor 0.75, `y_pt = 595 - y_css·0.75`). Para que el cambio sea **solo de esa propuesta** y no tocar el canónico `agregar-campo-precio.py`, el reposicionamiento del `/Rect` (+ borrar `/AP`, con `NeedAppearances=True`) se hace en el **customize-`<slug>`.py** que corre después de `generar-pdf.sh`. Hay espacio libre en la columna izquierda hasta el pie (~742px); cajas de ~185px alto (≈11 líneas) caben con ~90px de margen. **Clave:** mover solo el `/Rect` del PDF existente deja el rótulo estático desincronizado → hay que **regenerar el PDF base** desde el HTML actualizado y reaplicar todos los AcroForms en el customize. **Caveat de HCA Venezuela:** el slug tiene subcarpeta con espacios (`hca-venezuela/CAP-015 Claude Cowork - Dominio Corporativo`); `generar-pdf.sh` renombró el PDF al estándar `<CÓDIGO> <Título>.pdf` (eliminé el viejo sin prefijo) y el verificador da un **falso positivo** buscando `customize-<slug>*.py` (el script real es `customize-hca-venezuela-cap015.py`, sí corre). De paso, esta propuesta tenía Pasos en placeholder (§4.14) y 10 guiones largos §4.13 en el copy del deck → corregidos.

## 2026-05-26 — [cliente:simple-tv] CAP-035 · propuesta nueva Fase 1 (nivelación 210 personas) + 2 fixes de plantilla

Propuesta **Simple TV CAP-035** (Capacitación In-Company · Educación · Fase 1 de un plan de 3 fases): nivelación en IA de ~210 colaboradores, 8h en 4 sesiones de 2h, cohortes mixtas presencial + online. Clon de `pilotes-perforados` (multi-fase) **sin la slide de Mapa de Calor** (no aplica a una nivelación) → 15 slides; `s-roadmap` re-mapeado a **3 fases** (F1 cotizada → F2 talleres por depto → F3 consultoría → ★ capacidad interna de IA). Impacto con datos reales (McKinsey Superagency 2025; St. Louis Fed 2025; barras 88/47/36% para que el valor quede dentro del fill, gauge 33%). Dos fixes de plantilla descubiertos: (1) **`.s-program` con 4 módulos recortaba +92px**: la regla `:has(.module:nth-child(4))` del CSS solo fijaba grid 2×2 y `min-height`, **sin reducir tipografía** (la compactación solo existía para 7+ módulos). Fix: añadir compactación (padding 54px, roman 52, h3 22, obj 13, topics 15px) al breakpoint de 4 módulos + acortar `obj` a 1 línea. (2) El **título de los Próximos pasos (`Paso0NTitulo`) se recorta a ~20 chars** (campo angosto junto al ghost number): «Confirmamos fechas y cohortes» (29) se cortaba en «…y co»; bajado a «Fechas y cohortes». Pendiente de ventas: confirmar apellido del consultor Juan y datos de contacto de Isabella Palazzone.

## 2026-05-25 — [cliente:empresas-polar] CAP-011 · ajuste visual slides Programa + migración cronograma al nuevo desglose

Segunda pasada sobre **Empresas Polar CAP-011** por feedback visual: (1) las **slides de Programa (04/05) con 3 módulos** tenían demasiado espacio en blanco porque la regla `1-3 módulos → min-height: 490px` + `.topics { margin-top: auto }` deja un hueco enorme con poco contenido. **Fix:** para el caso de 3 módulos bajé `min-height` a 360px, escalé tipografía (h3 19px, obj 14px, chips 12px) y centré el grid verticalmente (`.s-program { display:flex; flex-direction:column }` + `margin:auto` en `.modules`), además de añadir un 5º subtema por módulo para llenar las cards. (2) El **cronograma (slide 06)** usaba el formato viejo `.s-schedule .session .grid` (2 sesiones apretadas en una slide con bloques de texto inline); se **migró al formato canónico de desglose instructivo: 1 slide por sesión** (`.ruta` progreso + `.ses-head` + `.chips` de temas + `.timebar` proporcional + `.ses-cols` de 3 columnas), portando ese CSS desde `_base/styles.css` a la hoja local de Polar. Esto subió el deck de **11 a 12 slides** → renumerar todos los contadores a `/12`. Recordatorio: cumbre-andina (canónico) ya trae este formato; los clones viejos con `.grid` deben migrarse cuando se retomen.

## 2026-05-25 — [cliente:empresas-polar] CAP-011 · pivote de 8h fundamentos → 6h 100% agéntico (audiencia avanzada)

Reestructuración de **Empresas Polar CAP-011** por feedback de ventas: el área de Control tiene **madurez alta en IA**, así que se **cortó el Día 1 de fundamentos** (prompting básico, Sheets supercharged, NotebookLM repositorio, diagramación) y el programa pasó de **8h/8 módulos** a **6h/6 módulos · 2 sesiones × 3h**, 100% inteligencia agéntica avanzada: arquitectura → construcción → conocimiento/confiabilidad → orquestación con Antigravity → operatividad/control → **proyecto final = automatización de un flujo real con Antigravity** (antes "Mi Gem de Polar"). **Decisión de copy del usuario:** **no nombrar productos cuyo acceso no está confirmado** (el cliente valida internamente "Gemini Sparks", Google Labs); el deck nombra solo Gemini, NotebookLM y Antigravity. De paso se subió el customize al estándar: **se arregló la violación §4.15** del Paso 02 (decía "Firmamos acuerdo / factura / 50% anticipo" → "Acceso y logística") y la **Acreditación pasó de 1 línea a las 3 estándar** + se añadió `rebake_bold_fields` y los 6 campos de Pasos. **Dos defectos atrapados en revisión visual (no por el verificador):** el título del Paso 03 "Kick-off técnico con Andres Fornerino" se **truncaba** en el campo AcroForm → "Kick-off técnico"; y "(ABR)" sin glosar en la slide 8 (§4.12) → "Aprendizaje Basado en Retos" completo. Se eliminó el PDF viejo de 8h (nombre sin prefijo de código).

## 2026-05-25 — [cliente:apb-group] APB Group CAP-033 · Capacitación RRHH con IA (Google), regalo sin slide de precio + facilitador nombrado

Nueva propuesta para RRHH de **APB Group** (Educación, in-company, `CAP-033`), clonada de `cumbre-andina` (12 slides: 1 slide de cronograma por sesión, ruta de 3 nodos). Reencuadre del catálogo TA-006 a **6 h · 3 sesiones de 2 h · 100% práctica** sobre el **ecosistema Google** (Gemini + Gemas, NotebookLM, Gamma/Canva): S1 Reclutamiento (Gema de cargo+vacante, screening de CVs con % de ajuste, entrevistas, roleplay), S2 Onboarding (kit de bienvenida, manuales visuales, buddy), S3 Operaciones (chatbot de servicio, automatización de cartas/constancias/cumpleaños). **Es un regalo:** se eliminó la slide `s-price` y `agregar-campo-precio.py` **omitió el grupo de precio solo** (mismo mecanismo que Fundación, sirve también para cortesías en Educación). **Facilitador nombrado** Douglas Vásquez (no el equipo genérico) + coordinación INTEZIA. Impacto con datos reales (SHRM 2024 89%/36% · LinkedIn The Future of Recruiting 2025 74%/37%/1 día por semana). **Bug recurrente atrapado en revisión visual (no por el verificador):** las líneas de la caja AcroForm `Entregables` envolvían a 2 renglones y se cortaban → acortadas a un renglón cada una (≤~26 chars). El verificador automático no detecta overflow dentro de campos AcroForm: revisar la slide 9 a ojo siempre.

## 2026-05-25 — [regla][scripts] §4.15 Sin acuerdos económicos en «Cómo arrancamos»

El paso 02 de la slide de Próximos pasos venía con «Firmamos acuerdo» + «factura / anticipo» en CAP-001 (`bnc-bootcamp`) y CAP-002 (`bnc`). El cierre económico es parte del proceso de venta y **no se menciona en el deck**. Fix: reencuadre a **«Acceso y logística»** (título ≤~20 chars) + body de participantes/accesos/agenda, en `index.html` y customize de ambas. **Causa raíz para futuras propuestas:** la instrucción §6 paso 6 decía literalmente «firmar acuerdo + factura 50 % anticipo» → corregida a «coordinar acceso, participantes y agenda». Nueva regla bloqueante §4.15 + guard en `verificar-propuesta.sh` (marca factura/anticipo/acuerdo/contrato/pago/50 % dentro de bloques `acro-paso-*`). No se auditaron las propuestas ya generadas (decisión del usuario): solo CAP-001, CAP-002 y prevención de futuras.

## 2026-05-24 — [cliente:bnc-bootcamp][bug] BNC CAP-001 Fase 2 (Bootcamp) + modo compacto Programa 5 módulos incompleto en _base

Creada la 2ª propuesta BNC: **CAP-001 IA Bootcamp · Fase 2** (`bnc-bootcamp/`), capacitación de 5 h · 5 módulos · 2 sesiones, clonada de `bnc/` (Fase 1). Copilot como eje (reescritos los Gemini/ChatGPT/NotebookLM/Gems del borrador original → Copilot, Copilot en Word/Excel, Copilot Agents). **Equipo definido:** Andrés Fornerino (Facilitador), Isaac Rodriguez (Product Leader), María Iribarren (Asesora). Corregidos también los `brief.md`/`programa.md` de Fase 1 que aún ponían a Isaac como facilitador. **Bug en `_base/styles.css`:** la regla de Programa para 5-6 módulos (`:has(.module:nth-child(5)):not(...7)`) solo fija `min-height:235px` pero **no** baja fuentes ni oculta `.obj` como sí hace el modo de 4 módulos → la card desborda ~140px. Fix local en `overrides.css` (replicar modo compacto: `.obj` 12px, h3 18px, topics 12.5px, min-height 0). Pendiente: portar el modo compacto al `_base` para 5-6 módulos (requiere confirmar cambio estructural).

## 2026-05-24 — [cliente:bnc][regla] Propuesta BNC CAP-002 · herramienta del cliente como eje central

Capacitación mono-fase de 90 min para BNC (banca, Educación), clonada de `cumbre-andina` (14 slides: 1 slide de cronograma por módulo, ruta de 4 nodos). **Directriz del cliente:** Microsoft Copilot es la herramienta de IA del banco; la propuesta lo posiciona como **eje central** integrado a la suite Microsoft (Outlook, Excel, PowerPoint, Teams), con carga práctica fuerte; las demás herramientas (ChatGPT, Gemini, Claude) solo se mencionan en general. **Aplica también a la 2ª propuesta BNC.** Encaja con §4.11: el deck enmarca Copilot operando *dentro* del entorno Microsoft que el banco ya usa, nunca como cambio de stack. Impacto con datos reales (Microsoft WorkLab 70/68/64 %, Forrester 116 % ROI, McKinsey banca 52 %).

## 2026-05-24 — [bug][plantilla] El campo de título de Próximos pasos (PasoNNTitulo) es de UNA línea: se trunca

En BNC, `Paso01Titulo = "Confirmamos grupo y fecha"` (25 chars) se cortó a «Confirmamos grupo y fec» en el PDF. El campo `PasoNNTitulo` no envuelve: **máx ~20-21 chars visibles**. Los que renderizan completos en la canónica son ≤20 («Kick-off y curaduría» = 20). **Regla:** títulos de paso ≤~20 chars; la explicación va en el body (≤~130 chars). Fix BNC: «Grupo y fecha». Complementa [[project_pasos_body_max_chars]] (que cubría solo el body).

## 2026-05-24 — [scripts][preferencia] PDF nombrado por código + título (no más propuesta.pdf)

El usuario perdía el control de los PDFs porque todos se generaban como `propuesta.pdf`. **Fix:** `generar-pdf.sh` ahora deriva el nombre de la portada (`span.codigo` + `<h1>`) y genera `<CÓDIGO> <Título>.pdf` (ej. `TA-001 Inteligencia Artificial aplicada con Claude.pdf`); imprime al final el path real + el comando `customize` con ese path. Los `customize-<slug>.py` ya tomaban el path por `sys.argv[1]`, así que no se rompió nada (las menciones a `propuesta.pdf` eran solo ejemplos de docstring). `verificar-propuesta.sh` ahora busca cualquier `*.pdf` en la carpeta (no solo `propuesta.pdf`) para el chequeo del par PDF-customize. Docs actualizadas: `generar-pdf.md`, CLAUDE.md §7.

## 2026-05-24 — [arquitectura][scripts][preferencia] Sistema anti-desborde + CSS compartido + biblioteca de bloques

El usuario reportó que generar propuestas gastaba demasiados tokens y, sobre todo, que no quería **revisar diseño nunca**: cada cliente trae distinto volumen de contenido y las cajas de tamaño fijo se desbordaban (§4.10), obligando a revisar el PDF a ojo slide por slide. Filosofía elegida: **prevenir, no absorber** (acotar el contenido a la capacidad de cada caja, en vez de hacer CSS auto-fit que estire las cajas) y **componer, no parchear** (bloques reutilizables). **4 entregables:** (1) `scripts/verificar-overflow.js` — detector Node+CDP (sin dependencias, usa Chrome headless + WebSocket nativo) que renderiza el deck y reporta qué slide/caja se sale o recorta; calibrado contra cumbre-andina (limpio), valida desborde forzado y detectó un desborde real latente en pilotes (Mapa de Calor, última fila recortada ~44px). Integrado en `verificar-propuesta.sh` como chequeo §4.10 automático. (2) `clientes/propuestas/_base/styles.css` — CSS canónico compartido; cumbre-andina lo enlaza por ruta relativa y los clones lo heredan (≈1.840 líneas que ya no se copian). pilotes-perforados quedó standalone (su CSS multi-fase interleaved cambia el render al reorganizarse; migrarlo es tarea futura cuidadosa). (3) `plantillas/capacidad-cajas.md` — cuánto cabe legible por caja, para acotar las preguntas de contenido; el detector es la autoridad final. (4) `plantillas/slides/` — biblioteca de bloques (README + roadmap y mapa-de-calor con su HTML y CSS) para agregar slides a la medida; validado insertando el bloque en un clon base. Pendiente conocido: el desborde real de pilotes Mapa de Calor.

## 2026-05-21 — [arquitectura][regla] §6.A + §10 + verificar-propuesta.sh · flujo de modificación unificado

El usuario detectó un patrón recurrente: al modificar propuestas existentes, las reglas acumuladas (§4.10–§4.14) no siempre se aplicaban y los campos AcroForm quedaban vacíos tras regenerar el PDF. Causa raíz: la ruta "propuesta clon" en §5 decía "ninguno" y no tenía checklist propio; el par `generar-pdf.sh` + `customize-<slug>.py` se desacoplaba. **Fix en 3 partes:** (1) Creado `scripts/verificar-propuesta.sh` que comprueba automáticamente §4.13 guiones largos, comillas tipográficas, placeholders sin llenar y presencia del customize script. (2) Añadido `§6.A Flujo de modificación` a CLAUDE.md con pasos explícitos y el par PDF-customize como obligatorio. (3) Añadido `§10 Checklist pre-entrega` con verificación automática (script) + manual (tabla de 5 ítems) que aplica a TODO trabajo: nueva propuesta, modificación y regeneración. La ruta "propuesta clon" en §5 ahora referencia §4.14 y §10 explícitamente.

---

## 2026-05-21 — [regla][cliente:cashea] §4.14 Leer antes de modificar · gaps detectados en CAP-005 y CAP-006

Al retomar CAP-005 y CAP-006 para ajustar formato se detectaron 3 campos vacíos en ambas propuestas: `Entregables`, `Acreditacion` y los 6 campos de Próximos Pasos. Causa raíz: no se leyeron `brief.md`, `programa.md` ni el `index.html` actual antes de intervenir. Fix: creada regla bloqueante §4.14 en `CLAUDE.md` que exige lectura mínima obligatoria antes de tocar cualquier propuesta. También creados `scripts/customize-cashea.py` y `scripts/customize-cashea-cap006.py` para pre-llenar AcroForms de ambas propuestas. **Operativa**: si no existe `programa.md` en la carpeta, crearlo antes de construir el deck.

---

## 2026-05-21 — [regla][scripts] Pre-llenado de AcroForms es obligatorio al crear cualquier propuesta nueva

Al crear una propuesta desde cero (flujo §6), el paso 6 de pre-llenado con `customize-<slug>.py` es **siempre** obligatorio. No dejarlo para después. El script se crea en `/scripts/customize-<slug>.py` y se ejecuta contra el PDF recién generado. Campos mínimos a llenar: `Entregables`, `Acreditacion`, `Paso01–03 Titulo` y `Paso01–03 Body`. Sin este paso, el slide "Cómo arrancamos" queda en blanco en el PDF que recibe el cliente.

**Fix aplicado**: TA-005 Marketing Estratégico — creado `customize-ta005-marketing.py` y ejecutado sobre `propuesta.pdf`.

---

## 2026-05-21 — [bug][arquitectura] Slide Programa con 4 módulos: overflow de topics — fix modo compacto en CSS

Deck TA-005 con 4 módulos en grid 2×2. El CSS original solo ajustaba el grid (`repeat(2,1fr)`) pero no reducía el `padding: 80px` ni fuentes, haciendo que los módulos mostraran solo 2 de 5 temas. Fix: añadidas reglas compactas al bloque `:has(> .module:nth-child(4)):not(...)` en `styles.css`: `padding: 56px 14px 14px`, roman 50px, h3 18px, obj 11px, topics `font-size: 13px` con `gap: 4px`. Esto permite mostrar los 5 temas por card sin overflow. El fix se aplicó al CSS canónico (`cumbre-andina/styles.css`) para que todos los decks futuros de 4 módulos lo hereden.

## 2026-05-21 — [cliente:cashea][regla] CAP-005 y CAP-006 adaptados al nuevo formato cumbre-andina · instrucción de director: sin precios

El director educativo instruyó eliminar toda referencia de precios en CAP-005 y CAP-006. Se eliminó la slide `s-price` de ambos decks y se limpiaron menciones de anticipo, cotización y divisas en Próximos Pasos. Simultáneamente se aplicó el formato nuevo: cronograma tipo "ruta de aprendizaje" (1 sesión/slide con `.ruta`, `.ses-head`, `.ses-body`, timebar y ses-cols), slide de Impacto añadida y CTA convertido de `<span>` a `<a>` con link Calendly. CAP-005 pasó de 12 a 16 slides; CAP-006 de 12 a 15. Ambos CSS reemplazados con el de cumbre-andina. **Regla operativa**: cuando el director dice "sin precios", aplica a toda slide y a todo copy visible (Próximos Pasos incluido) — no solo a la slide `s-price`.

---

## 2026-05-21 — [bug][cliente:grupo-sambil] CAP-018 reformateado a Sprint Ágil (3h · 3 sesiones) · 4 defectos de mi primera entrega

El usuario pidió reajustar CAP-018 de 8h/4 mods a **formato ágil: 3h · 3 sesiones de 1 hora · 100% práctico** (Artifacts y Skills · Estructuración de Estrategias · Contenido y Diseño). Reescribí las 10 slides (de 11: fusioné las 2 slides de cronograma en 1) pero **entregué un PDF roto sin revisarlo visualmente** (§4.10). 4 defectos:
**(1) Comillas tipográficas en atributos HTML**: la slide 02 quedó con `class=”slide s-pain”` (comillas curvas `”` en vez de rectas `"`) en TODOS sus tags → el navegador no reconoció `.s-pain`/`.slide` y la slide perdió todo el CSS (sin fondo amarillo, texto desbordado). Fix: reescribir con comillas rectas. **Regla**: tras editar/pegar bloques HTML, `grep -n 'class=[”“]'` antes de generar — las comillas curvas son invisibles a simple vista pero rompen el render entero.
**(2) `<strong>` dentro de `<li>` con `display:flex`** (diagnóstico slide 02 + objetivos específicos slide 03): fragmentó el texto («Crear y gestionar» separado de «Artifacts»). Ya documentado en memoria `project_spain_no_strong.md` — lo violé. Fix: quitar `<strong>` de esos `<li>`; el resaltado va solo en `<p>` (contexto, objetivo general).
**(3) Texto de Duración (slide 08) demasiado largo** → 3 líneas que se solapaban con el bloque «Programa» absoluto de abajo. Causa: añadí «· formato ágil ·». Fix: quitarlo, volver a 2 líneas (mismo largo que el original de 8h).
**(4) Próximos pasos + Acreditación sin pre-llenar**: regenerar reseteó los AcroForms a placeholders genéricos. Creé `customize-grupo-sambil-cap018.py` (entregables del nuevo formato + Acreditación CAP-018 + 3 pasos del Sprint, bodies ≤130 chars). Mismo par flujo que CH-004: `generar-pdf.sh` → `customize-<slug>.py` siempre juntos.

---

## 2026-05-20 — [bug][scripts] CH-004 · regenerar PDF borra los AcroForms pre-llenados + grid de 5 módulos tapaba el logo

Dos defectos detectados por el usuario tras la corrección de copy: **(1)** al regenerar el PDF con `generar-pdf.sh` se perdió el pre-llenado de «Cómo arrancamos» (los 6 campos quedaron con solo placeholder). Causa: `generar-pdf.sh` reinyecta los AcroForms vacíos; el `/V` lo escribe **después** `customize-bdv-ch004.py`. **Regla de flujo**: cada vez que se regenera el PDF de una propuesta con campos pre-llenados hay que **volver a correr su `customize-<slug>.py`** justo después; ejecutarlos siempre como par. **(2)** En la slide 04 (Programa, 5 módulos) la tarjeta IV se desbordaba ~40px hacia la zona del footer y **tapaba el logo Intezia Education** (abajo-izq). Causa: el grid `flex:1` con el contenido de la tarjeta de 2 líneas de título + 5 temas excedía la altura de fila. Fix en `styles.css` (caso 5-6 módulos): `grid-template-rows: repeat(2, minmax(0,1fr))`, `.s-program` padding-bottom 96→72px (más aire vertical para el grid), y compactado de tarjeta (padding-top 52→44, roman 46→42, obj margin 7→5 + line-height 1.35, topics li padding 3→2). Verificado renderizando slide 04 y 08 con `pdftoppm -png` antes de entregar (§4.10).
**(3) Diagnóstico (slide 02) · número desalineado del texto**: el `.s-pain ol li` usaba `align-items: center` mientras el número (`::before`) está fijado en `top: 0`. En un grid de 2 columnas, el item más corto de cada fila (ej. 02 vs 01) se estira a la altura de la fila y su texto se centra verticalmente, dejando el número arriba → desalineado respecto a la primera línea. Fix: `align-items: flex-start` en el `<li>` → texto y número se alinean por arriba en todos los items, sin importar cuál sea más alto. Patrón a vigilar en cualquier lista con numerador absoluto en `top:0` dentro de un grid con celdas que se estiran.

---

## 2026-05-20 — [cliente:bdv] CH-004 · corregido «el banco ya utiliza Gemini» (BDV no ha adoptado Gemini)

Feedback del usuario sobre **CH-004 BDV**: el deck afirmaba que el banco «ya utiliza» el ecosistema Google / Gemini cuando en realidad **BDV no ha adoptado Gemini** — Intezia es justamente quien va a enseñárselo (CAP-023 será el primer cohort). 6 afirmaciones corregidas en `index.html` **sin regenerar el deck**: (1) h2 de slide 02 «La adopción de IA en BDV avanza más rápido…» → «La banca avanza hacia la IA más rápido que su gobernanza…»; (2) párrafo de contexto «Gemini, dentro del ecosistema Google que el banco ya utiliza, lidera ese uso» → «entre las opciones de IA empresarial, las que operan sin VPN (como Gemini dentro del entorno Google) son las viables para el banco»; (3) punto 1 del diagnóstico igual reencuadre; (4) punto 2 «Ecosistema Google ya en uso» → «Ventana previa a la adopción»; (5) hook del bloque I «¿Sabe qué Gemini hizo ayer su mejor analista?» → «¿Qué podría hacer Gemini con su mejor analista?»; (6) tema 1.1 «qué hizo tu equipo con Gemini» → «qué podría hacer Gemini en tu equipo». `brief.md` alineado (incl. título del Bloque I y sección Stack 2026). PDF regenerado con `./scripts/generar-pdf.sh`.
**Por qué + regla nueva**: §4.11 prohíbe afirmar que el cliente migra a otro stack; el corolario es **no afirmar que el cliente ya adoptó una herramienta cuando no es así**. Gemini se presenta como la **opción recomendada** para el contexto operativo del banco (sin VPN), no como stack en uso. Memoria persistente en `feedback_no_afirmar_adopcion_cliente.md`. Patrón a aplicar a todo deck nuevo: si la herramienta es objeto de la capacitación, el copy no puede dar por hecha su adopción previa.

---

## 2026-05-20 — [regla] [cliente:bdv] Sin guion largo como separador (§4.13) · CAP-024

Feedback del usuario: el deck **BDV CAP-024** estaba lleno de guiones largos (`—`) usados como separador y «se ve horrible, es marca de voz de IA, ventas lo detecta». Inventario: **13 ocurrencias en `index.html`** (portada, h2 y diagnóstico de la slide 02, contexto de objetivos, hook de Impacto, fuente McKinsey, duración de Propuesta Económica, título del Roadmap, caja de ética) **más 5 ocurrencias en el script canónico `agregar-campo-precio.py`** (placeholder de Notas visible en la slide 12, placeholders de Paso01/02/03 Titulo, tooltip de cajas multilínea y tooltip de Total). Fix completo a puntuación natural según el rol gramatical del guion: **coma o paréntesis** para aposición, **dos puntos** para contraste y desarrollo, **punto y nueva oración** para idea relacionada, **`·` middle dot** para separador de listas. Ejemplos clave: «no es un taller por semana**:** es construir una arquitectura» (era «—»); «sin método ni criterio común. **Los resultados** dependen…» (era «—»); «**BDV, organización** con implementación exitosa de IA» (era «BDV —»); «**Transversal a las 3 fases:** Política de Uso Aceptable (AUP) del BDV…» (era «—»). PDF regenerado y verificado slide por slide: `grep -nE "—|–"` en `index.html` y en placeholders de scripts devuelve cero.
**Por qué y regla nueva**: el guion largo es marca de redacción de IA que rompe la sensación de copy humano y profesional. Se añade **CLAUDE.md §4.13 "Sin guion largo como separador, bloqueante"** más entrada en *Reglas de copy* e ítem de *Checklist final* en `plantillas/propuesta-comercial.md` (incluye comando de verificación `grep -nE "—|–"`). Memoria persistente en `feedback_sin_guion_largo.md`. La regla aplica a `index.html`, placeholders y tooltips de AcroForms, valores de `customize-<slug>.py`, copy de catálogo y briefs entregables; excepción: citas verbatim donde el `—` está en el original.

---

## 2026-05-20 — [regla] [cliente:bdv] Acrónimos explicados en el primer uso (§4.12) + reencuadre Gemini en positivo · CAP-024

Feedback de ventas sobre **BDV CAP-024**: el deck usaba acrónimos de jerga sin explicarlos nunca — los objetivos específicos mencionaban «**AUP** corporativo» sin decir qué es, y aparecían «**RCTF**» y «**GenAI**» sueltos. Esto complica al equipo de ventas vender lo que ofrece la propuesta. Fix en `bdv/CAP-024 .../index.html`: «**Política de Uso Aceptable (AUP)**» y «**RCTF (Rol, Contexto, Tarea, Formato)**» expandidos en el primer uso de **cada slide** donde aparecen (objetivos, mapa, Fase 1, perfil de egreso, roadmap); chips/timebars sin espacio usan el término natural en vez de la sigla cruda; «GenAI» → «**IA generativa**» en la slide de Impacto. Segundo ajuste pedido: **reencuadre del enfoque de Gemini** — el punto 02 del diagnóstico pasa de constatación de acceso/VPN a justificación **en positivo** («el plan se construye sobre Gemini porque ofrece facilidades que otras herramientas no: vive dentro del entorno Google que el banco ya usa y opera sin VPN»), neutral y sin afirmar migración de stack (§4.11); reforzado también en el «Saber» del perfil de egreso.
**Por qué + regla nueva**: no se puede asumir que el lector sabe qué significa una sigla. Se añade **CLAUDE.md §4.12 "Acrónimos y siglas — explicar en el primer uso — bloqueante"** + entrada en *Reglas de copy* (incl. «elección de herramienta en positivo») e ítem de *Checklist final* en `plantillas/propuesta-comercial.md`. Excepciones que no se expanden: sigla del propio cliente (BDV, BCV), siglas generales del sector (VPN, API en módulo técnico), códigos de catálogo (CAP-, TA-…). La regla ya existía en memoria (`feedback_acronimos_glosar.md`, detectada en CH-004) pero **reincidió** en CAP-024 sin estar codificada como bloqueante → ahora elevada a §4.12; memoria actualizada.

---

## 2026-05-20 — [cliente:bdv] CH-004 charla · aplicada §4.11 + migrada al formato canónico (8 → 9 slides)

Se aplicó la misma corrección del paquete BDV a la **charla de cortesía CH-004** (`bdv/CH-004 IA Ejecutiva con Gemini para Banca/`): **(1) §4.11** — se eliminó toda afirmación de que el banco «migra a Google Workspace» y el encuadre «la VPN bloquea ChatGPT/Claude · Gemini única opción»; reescrito a «el banco opera con restricciones de VPN · la adopción se concentra en las herramientas de IA que operan sin VPN, como Gemini dentro del **ecosistema Google que el banco ya utiliza**» (slide 2 Dolor+Diagnóstico, slide 4 Programa tema 1.2, slide 5 Metodología subtítulo, sección Stack del `brief.md`) — cubre también la petición «incluir herramientas sin VPN». **(2) Migración al formato canónico cumbre-andina**: se añadió la slide **`07 · Impacto`** (`.s-impact`) con datos de estudios reales del sector banca citados verbatim (McKinsey *The economic potential of generative AI* 2023 · *Capturing the full value of generative AI in banking* 2024 · EY-Parthenon *GenAI Banking Survey* 2025): barras +40/+30/+20 % por función bancaria, gauge 77 % de adopción, chips 9–15 % utilidades y 2,8–4,7 % ingresos, hook US$340 mil millones/año. CTA del cierre pasado a `<a href="…calendly…">`. Renumerado 8 → 9 slides. **Sigue sin slide de Propuesta Económica** (charla gratuita). **(3) §4.12 (acrónimos)** — segundo feedback del usuario: «AUP» se usaba desde la portada sin glosar. Aplicada §4.12 per-slide: `<strong>Política de Uso Aceptable (AUP)</strong>` expandida en cada slide donde aparece (portada, dolor, fundamentación, programa-bloque II, metodología-pilar 02; slide 6 sin `<strong>` extra por chocar con la negrita de etiqueta del `<li>`); «ROI» → «**Retorno de la Inversión (ROI)**» en slide 4 bloque IV; «Q&A» → «preguntas y respuestas» y «CTA» → «siguiente paso» (escritos completos en español, sin sigla); Paso 03 reescrito a «política de uso aceptable de IA» en lenguaje natural — sincronizado también en `scripts/customize-bdv-ch004.py` (el `/V` del AcroForm es lo que se ve en el PDF, no el HTML default). Recortado el párrafo de contexto de slide 2 (~60 chars) para compensar la línea extra que añadía la expansión de AUP y evitar que la tarjeta 05 del diagnóstico se cortara (§4.10). PDF regenerado (`generar-pdf.sh` + `customize-bdv-ch004.py`, 6 AcroForms de Próximos pasos) y revisado slide por slide (§4.10): sin overflow.
**Por qué**: continuación del feedback de ventas BDV (ver entradas §4.11 y §4.12 / CAP-024 de esta misma fecha) + petición del usuario de «migrar al nuevo formato como cumbre-andina» + corrección sobre AUP. Patrones confirmados: (a) al migrar una **charla de cortesía** al canónico se añade Impacto con datos citados pero **no** se añade slide de precio; como el inyector de AcroForms localiza páginas por marker de texto, insertar la slide de Impacto antes de «Cómo arrancamos» no descoloca los 6 campos de Próximos pasos. (b) Una expansión de acrónimo en un párrafo apretado puede empujar contenido fuera de slide — al aplicar §4.12 conviene presupuestar línea(s) en el copy y trimear lo redundante en la misma slide.

---

## 2026-05-20 — [regla] [cliente:bdv] No afirmar migración de stack del cliente (§4.11) + ajuste CAP-024

Feedback de ventas sobre la propuesta **BDV CAP-024**: la slide de Diagnóstico decía «la **migración a Workspace** está en curso», lo que afirma de cara al cliente que el banco cambia de stack tecnológico. Se reescribió ese punto del diagnóstico a «**El plan se apoya en el entorno Google del banco y en herramientas que operan sin VPN** — adopción sin fricción de acceso ni dependencia de plataformas externas», cubriendo además la segunda petición del cliente (incluir herramientas sin VPN). PDF regenerado (15 slides, 13 AcroForms vía `customize-bdv-cap024.py`) y revisado slide por slide (§4.10): el punto 02 del diagnóstico entra sin overflow.
**Por qué + regla nueva**: Intezia **se ajusta al stack del cliente, no lo cambia** — afirmar que una empresa migra a otra suite/plataforma es incorrecto en cualquier propuesta, sea cual sea el stack. Se añade **CLAUDE.md §4.11 "No afirmar que el cliente migra de stack tecnológico — bloqueante"** + regla en *Reglas de copy* e ítem de *Checklist final* en `plantillas/propuesta-comercial.md`. El stack del cliente es contexto interno del `brief.md` para diseñar, no una afirmación de cara al cliente. Memoria persistente en `feedback_no_afirmar_migracion_stack.md`.

---

## 2026-05-19 — [regla] [catálogo] TA-023 IA para Emprendedores + regla anti-overflow visual (§4.10)

Se publicó el nuevo taller de catálogo **TA-023 · IA para Emprendedores · De la Idea al MVP** (División Fundación · 16 h en 4 sesiones × 4 h · audiencia emprendedores tempranos idea → MVP · stack abierto Claude+ChatGPT+Gemini+Perplexity+Canva+v0/Lovable+HeyGen+ElevenLabs+Custom GPTs/Gems). Estructura: 5 módulos `0 → 1` (Idea+Validación · Marca · MVP · Marketing · Operación) · entregable hero = landing page funcional publicada · slide de Impacto con datos reales (Gusto SMB 2025 · McKinsey/Antler 2025 · OECD 2025). Deck 13 slides en HUD canónico, sin slide de Propuesta Económica (regla Fundación), 8 AcroForms pre-llenados vía `scripts/customize-ta-023.py`. Entrada añadida a `empresa/catalogo.md` después de TA-021. **Defecto recurrente detectado**: la slide Programa con 5 módulos cortaba topics (2-3 de 5 visibles) por `overflow: hidden` + chips con `text-overflow: ellipsis`. Fix: modo compacto CSS para 5-6 módulos (padding 58px, h3 21px, obj 12px, chip 14px, gap 4px) + chips ≤28 chars y obj ≤80 chars.
**Por qué + regla nueva**: el usuario reportó esto como patrón recurrente ("nuevamente empezaste a cortar elementos") → se añade **CLAUDE.md §4.10 "Sin overflow visual — bloqueante"** + sección *Presupuesto de copy por card* en `plantillas/propuesta-comercial.md` (tabla con límites de chip/h3/obj según volumen de módulos) + ítem nuevo en *Checklist final*: "abrir el PDF y revisar slide por slide antes de declarar entregable". Memoria persistente en `feedback_overflow_visual.md`. A partir de ahora: el script terminando sin error **no** equivale a PDF entregable — el sanity check visual es obligatorio.

---

## 2026-05-19 — [cliente:alfonso-rivas] CAP-027 · migrada al diseño canónico (12 → 14 slides)

Tras incorporar el feedback de ventas, la CAP-027 también se migró al **diseño canónico** (cumbre-andina / pilotes-perforados): `styles.css` reemplazado por el canónico (1822 líneas · idéntico al de pilotes); los overrides per-propuesta (4 objetivos en 2-col, 5 módulos centrados 6-col + `span 2`, 8 áreas 4×2) quedan en el `<style>` inline del `index.html`. Estructura: **14 slides** — se añadió la slide canónica **`09 · Impacto`** con datos de estudios reales (Dell'Acqua et al. HBS/BCG WP 24-013 · Brynjolfsson, Li & Raymond NBER WP 31161 · McKinsey *State of AI* nov. 2025), y el cronograma se partió en **2 slides `.s-schedule`** estilo pilotes (Fase 1 · Nivelación + Fase 2 · Especialización · barra `.ruta`, chips, timebar, ses-cols). CTA del cierre pasado a `<a href="https://calendly.com/intezia/30min?month=2026-05">`. Equipo del slide 10 reescrito con 2 personas + avatares (DV + Coordinación Intezia Education), eliminada la variante `.team-single`. `block-value` de la slide económica acortado a una línea (el detalle largo desbordaba sobre la caja Programa). PDF regenerado: 14 páginas, 13 AcroForms (markers detectados en págs. 10/12/13).
**Por qué**: el usuario pidió «usar siempre como referencia el de cumbre-andina» — las propuestas en el formato viejo (12 slides, sin Impacto, sin `.ruta`, CTA texto plano) hay que migrarlas explícitamente. Patrón aplicable: al actualizar una propuesta vieja al diseño actual, clonar el `styles.css` del canónico, preservar los overrides per-propuesta en el `<style>` inline, añadir Impacto y dividir cronograma según patrón pilotes para multi-fase.

---

## 2026-05-19 — [cliente:go-pharma] Capacitación CAP-030 · Productividad con IA (Claude + Gemini)

Generada la propuesta **CAP-030 · Productividad con IA — Dominando Claude y Gemini** para
**Go Pharma** (`clientes/propuestas/go-pharma/`): `brief.md`, `programa.md`, deck de **13
slides** (clon de `cumbre-andina`) y `propuesta.pdf`. Capacitación In-Company de división
**Educación**, **12 h presenciales en 3 sesiones de 4 h**, 30 participantes, 3 módulos
(Fundamentos de IA · Gemini en Workspace · Claude profundo y adopción). Consultor/facilitador
**Isaac Rodriguez** (una sola tarjeta de equipo). Slide de Impacto con datos verificados
(Stanford HAI 2026 AI Index · McKinsey State of AI 2025). Customización de AcroForms con
`scripts/customize-go-pharma-cap030.py`.
**Por qué — la caja AcroForm de Entregables rinde ~8-9 líneas visuales**: con 6 entradas de
texto largo (que envuelven a 2-3 líneas cada una) el contenido se desbordó fuera de la
tarjeta de la slide 9. La caja `(438, 338, 596, 455)` pt a 10 pt sólo admite ~8-9 líneas
renderizadas. Regla para futuras propuestas: los **destacados de Entregables deben ser
líneas cortas de un solo renglón** (~≤24 caracteres); las 3 institucionales ya envuelven a
2 líneas cada una.

---

## 2026-05-19 — [cliente:alfonso-rivas] CAP-027 · feedback de ventas: cohorts reducidos y horas por persona

Revisión de la CAP-027 (Plan de Adopción IA Trimestral) tras reunión de ventas con María: (1) los cohorts de Nivelación bajan de **50 → 25-30 personas** — un grupo acotado valida que la formación llegue de forma más efectiva; (2) el desglose de horas se expresa **por colaborador** (4h en cada trimestre de Nivelación · 2 sesiones de 2h · 8h en el Bootcamp T4), no en horas-cohort acumuladas; (3) la slide económica cotiza **solo el Trimestre 1** (300 personas) — los trimestres siguientes se renuevan y cotizan aparte. Editados `index.html` (slides 4, 5, 6, 7, 8, 10) y `brief.md`.
**Por qué**: «128h totales» confunde a ventas y al cliente en propuestas multi-cohort; la cifra que importa es la carga formativa por persona y el alcance de lo realmente cotizado. Patrón reutilizable: en capacitaciones multi-cohort, expresar horas por colaborador y cotizar por fase, no en totales acumulados.

---

## 2026-05-18 — [cliente:intezia-fundacion] Taller TA-021 · IA para el Sector Cafetero (BdV × Foundation)

Generada propuesta del taller **TA-021 · IA para el Sector Cafetero** para el Banco de
Venezuela a través de Intezia Foundation (`clientes/propuestas/intezia-fundacion/TA-021 IA
para el Sector Cafetero/`): `brief.md`, `programa.md`, deck de **11 slides** y `propuesta.pdf`.
Eje temático anclado en **Gemini** (vender más + medir mejor la producción). Taller de 8 h
en 2 sesiones de 4 h, 4 módulos. Registrado TA-021 en `empresa/catalogo.md`.
**Por qué — propuesta de división Fundación sin slide de Propuesta Económica**: por ser
un documento de Fundación, el deck omite la slide `.s-price`; el script
`agregar-campo-precio.py` detecta los grupos por marcador de texto y omite solo el grupo
"Propuesta Económica" cuando no está presente (líneas 425-428: lista vacía → `continue`).
Resultado: **8 campos AcroForm** en vez de 13, sin tocar el script. La negociación
financiera se maneja fuera del documento. El canónico `s-program` no tenía afinado el
caso de 4 módulos: se añadió una regla CSS de compactación (como la de 7-9 módulos) en el
`styles.css` clonado para que las 4 cards entren con sus 4 tags de tema sin recorte.

---

## 2026-05-18 — [cliente:pilotes-perforados] Propuesta regenerada al formato canónico + reencuadre de alcance

Regenerada la propuesta **CAP-021** al formato canónico de 13 slides (clon de
`cumbre-andina`, incluye `07 · Impacto`). Migrada de subcarpeta a estructura **plana**
en `clientes/propuestas/pilotes-perforados/`. Reencuadre tras feedback ventas+cliente:
deja de ser una capacitación técnica de 8h (Excel/Copilot/Claude) y pasa a un **proyecto
de digitalización operativa centrado en un diagnóstico** — Fase 1 (2 sesiones de
levantamiento con líderes de Procura, CxP, Finanzas y Licitaciones · única cotizada) +
Fase 2 (aplicación de IA · plan abierto, no cotizada, herramientas a definir tras el
Mapa de Calor). La 3.ª `.s-schedule` se reutilizó como slide de **estructura / plan de
acción**. Script `customize-pilotes-perforados.py` añadido.
**Por qué**: el cliente redujo personal, los procesos son abrumadores y no sabe qué
herramienta de IA le sirve — pidió diagnosticar antes de invertir.

---

## 2026-05-18 — [bug] `.s-pain ol li` es `display:flex` — no admite `<strong>` inline

En la slide de dolor, cada `<li>` del `<ol>` de diagnóstico es un **contenedor flex**
(`display:flex; align-items:center`). Si el texto lleva `<strong>`, cada `<strong>` y
cada fragmento de texto se vuelve un flex item independiente → el texto se solapa y los
espacios colapsan. Los `<li>` del diagnóstico van en **texto plano, sin `<strong>`** (el
canónico `cumbre-andina` no resalta ahí). El resaltado de la slide vive en `.context`
(un `<p>`, sí admite `<strong>`). Excepción a `CLAUDE.md §4.8` para esta slide.
**Por qué**: §4.8 pide resaltar palabras clave en `<li>`, pero el layout flex de
`.s-pain` lo rompe — conviene saberlo antes de la próxima propuesta.

---

## 2026-05-17 — [plantilla] Slide canónica «07 · Impacto» añadida al deck (12 → 13 slides)

Nueva slide `.s-impact` entre Beneficios y Propuesta Económica: respalda la propuesta con
**evidencia de impacto de la IA** antes de hablar de precio. Diseño de alto contraste —
slide en **negro**, gráfica de barras + **gauge radial** (`conic-gradient`) + **hook de
ventas** a todo el ancho abajo. Gráficas en **CSS puro** (sin Chart.js); verificado que
`conic-gradient`, máscaras y gradientes imprimen bien en Chrome headless. Eyebrow
`07 · Impacto` (el hueco 07 estaba libre — no se renumeran eyebrows). Renumerados los 13
`.counter` a `NN / 13`. Contenido **estático, sin AcroForms** — la detección por marcador
de texto absorbe la inserción sin tocar los 13 campos (verificado: markers en págs. 9/11/12).
Cifras de **estudios reales** con fuente citada verbatim: Stanford HAI — AI Index 2026,
McKinsey — The State of AI 2025, Anthropic Economic Index 2025. Diseño **flexible**:
barras 3–5, chips 1–3, gauge y copy parametrizables (cada cifra vive en su `--w`/`--pct`
+ texto, con comentarios `← EDITAR` en el HTML). Aplicado en `cumbre-andina/{index.html,
styles.css}` (PDF regenerado a 13 páginas); documentado en `propuesta-comercial.md`
(slide 9), `generar-pdf.md` y `CLAUDE.md` (nueva regla **§4.9**: datos de impacto solo de
estudios reales con fuente citada).
**Por qué**: el equipo de ventas pidió una diapositiva con gráficas/métricas de estudios
que respalden el impacto de la IA, para reforzar el cierre comercial con evidencia. Las
propuestas de cliente ya generadas (clones del deck de 12 slides) no se modifican
retroactivamente.

---

## 2026-05-17 — [plantilla] CTA de cierre: botón con hipervínculo a Calendly

El CTA "Esperamos tu respuesta" de la slide de Cierre (`.s-end .cta`) deja de ser texto
estático (`<span>`) y pasa a ser un **botón-hipervínculo**: `<a class="cta"
href="https://calendly.com/intezia/30min?month=YYYY-MM" target="_blank" rel="noopener">`.
Chrome headless conserva el `<a href>` como anotación Link clicable en el PDF — verificado
en la última página del PDF canónico. El diseño no cambia: la clase `.cta` aplica igual a
un `<a>`; solo se añadió `text-decoration: none;` a `.s-end .cta` para quitar el subrayado
de enlace del navegador. **URL canónica: `https://calendly.com/intezia/30min?month=YYYY-MM`
— siempre incluir `?month=` con el mes actual al generar la propuesta** (ej. `2026-05`);
sin el parámetro Calendly puede mostrar un mes sin disponibilidad y el enlace parece roto.
Aplicado en `cumbre-andina/{index.html,styles.css}` (PDF regenerado) y documentado en
`propuesta-comercial.md` §11 y `generar-pdf.md` — toda propuesta nueva debe llevar el CTA
como `<a>` con `?month=`, nunca `<span>`.
**Por qué**: el usuario confirmó que la URL sin `?month=` no funciona (Calendly mostraba
un mes sin disponibilidad). URL verificada: `https://calendly.com/intezia/30min?month=2026-05`.

---

## 2026-05-21 — [proyecto] Robin Agency (CAP-032) · clon multi-fase + fix barra angosta en Impacto

Propuesta nueva **CAP-032 Diagnóstico de IA en el Flujo Creativo** (Capacitación In-Company,
agencia creativa de marketing). Clonada de `pilotes-perforados` (canónico multi-fase): misma
estructura Fase 1 Diagnóstico cotizada + Fase 2 abierta, mismo entregable insignia (Mapa de
Calor), misma asesora (Flavia Martínez). Adaptaciones: 5 áreas (Arte, Contenido, Cuentas,
Planning, Finanzas) en 2 semanas de levantamiento; herramientas enmarcadas §4.11 (Claude
recomendado para agentes + Google AI complementario, decisión final del diagnóstico, sin
afirmar que ya usan Claude más allá de lo básico); Impacto con McKinsey 2023/2024 + Adobe 2024.

**Fix reutilizable — barra angosta en slide Impacto:** un `bar-val` con rango (ej. `+5-15%`)
sobre un `bar-fill` de `--w` pequeño (≤~20%) **desborda**: el texto no cabe dentro del fill,
se parte en dos líneas y se sale. Solución añadida a `styles.css`: `white-space: nowrap` en
`.s-impact .bar-val` + clase `.bar-fill--out` que reposiciona el valor **fuera** del fill
(`left: calc(100% + 10px)`, color blanco sobre el track oscuro). Marcar con `bar-fill--out`
toda barra cuyo valor sea más ancho que su fill. Pendiente: propagar a decks canónicos si se
confirma (cumbre-andina no tiene barras angostas; pilotes usa anchos ≥30%).

**Fix reutilizable — slide El proyecto (`.s-program`) con solo 2 módulos (proyecto en 2
fases):** el grid default es `repeat(3, 1fr)`, así que con 2 módulos quedaba una **tercera
columna vacía** a la derecha y la slide se veía vacía. Regla añadida a `styles.css` con
`:has(> .module:nth-child(2)):not(:has(> .module:nth-child(3)))` → `grid-template-columns:
repeat(2, 1fr)`, `gap: 40px`, `padding: 0 40px` (cards anchas y separadas) + en la card
`.topics { flex: 1; justify-content: space-between }` para repartir los chips en vertical y
llenar la altura sin huecos. Aplicado en `robin-agency`. Pendiente: propagar al canónico
`pilotes-perforados` (mismo caso 2 fases) si el usuario lo confirma.

---

> **Entradas anteriores a 2026-05-17 archivadas** en `aprendizajes-historico.md` (trazabilidad histórica).
> Todas ya codificadas en `CLAUDE.md`, plantillas y scripts. No se cargan en el flujo normal.


## 2026-05-16 — [plantilla] Entregables y Acreditación: texto siempre en negrita

Los campos AcroForm `Entregables` y `Acreditacion` (slide Beneficios) renderizan ahora
en **negrita**. Causa raíz: el `/DA` referenciaba `/HeBo`, una fuente sin definir; añadir
un `/DR` con `/HeBO`=Helvetica-Bold no bastó porque Preview y PDF.js (visor de VS Code)
no regeneran la apariencia desde `/DA`+`/DR` — pintan un fallback regular. Solución
definitiva: nuevo módulo `scripts/acroform_appearance.py` que **hornea el `/AP`** (Form
XObject) de esos dos campos con el texto dibujado en Helvetica-Bold y partido por
palabras (usa las métricas AFM `CORE_FONT_METRICS` de pypdf). `agregar-campo-precio.py`,
`customize-acroforms.py` y `customize-cumbre-andina.py` llaman a `rebake_bold_fields()`
antes de escribir. El campo sigue editable. PDF canónico `cumbre-andina/` regenerado.
**Por qué**: el usuario pidió que esos dos cuadros vayan siempre en negrita; el primer
intento (solo `/DR`) no se veía en su visor porque depende de que el lector regenere la
apariencia — hornear el `/AP` lo hace independiente del lector.

---

## 2026-05-16 — [plantilla] Acreditación: contenido estandarizado y código pre-llenado

El campo AcroForm `Acreditacion` (slide Beneficios) lleva siempre 3 líneas fijas para
toda propuesta con código: `Programa registrado en INTEZIA Education como [CÓDIGO].` ·
`Cumple con el modelo pedagógico oficial (ABR).` · `Material curado y revisado por el
equipo académico.` El único token variable es `[CÓDIGO]`, que ahora se pre-llena al
generar la propuesta (paso 6 de §6, `customize-acroforms.py`) con el código real del
programa — antes se dejaba como placeholder para que ventas lo editara a mano.
Actualizado: `customize-cumbre-andina.py` (Acreditacion → TA-001), comentario de
`agregar-campo-precio.py`, `generar-pdf.md`, `CLAUDE.md` §6, `propuesta-comercial.md`.
PDF canónico `cumbre-andina/` regenerado.
**Por qué**: el usuario fijó este contenido como estándar y pidió que el código se
inserte en generación, no manualmente en Adobe Reader.

---

## 2026-05-16 — [regla] Cronograma: el `<h2>` de cada slide dice «Módulo N», no «Tema N»

En las slides del desglose instructivo (`.s-schedule`) el `<h2>` pasa de «Tema N: nombre»
a **«Módulo N: nombre»** (números romanos: I, II, III…).

**Por qué**: el slide del cronograma es 1 por sesión y su unidad es un **módulo**; llamarlo
«Tema N» chocaba con el bloque «Temas» del propio slide (chips 1.1, 1.2…) — un tema no
contiene temas. La numeración `1.1 / 2.1` ya usa el primer dígito como nº de módulo.

Aplicado en `cumbre-andina/index.html` (slides 5–7), regla en `propuesta-comercial.md` §5
(«nunca Tema N») y fila de ejemplo de `diseno-curso-diplomado.md` §5.2. Estándar para
toda propuesta nueva.

---

## 2026-05-16 — [plantilla] Próximos pasos: letra de los campos editables más grande

Los campos AcroForm de la slide «Próximos pasos» se veían pequeños y dejaban mucho
blanco en las cards. Se sube el `font_size` en `agregar-campo-precio.py`:

- `_paso_title` (`PasoNNTitulo`): 14 → **18 pt**.
- `_paso_body` (`PasoNNBody`): 10 → **15 pt**.

El `font_size` vive en el `/DA` del campo, así que aplica tanto al texto que pre-llena
Claude como al que escribe ventas en Adobe Reader. La preview HTML se sincroniza en
`cumbre-andina/styles.css` (`.s-steps .acro-title/.acro-body .acro-default-text` → 24 px /
20 px). Cambio canónico — las propuestas nuevas lo heredan.

---

## 2026-05-16 — [plantilla] Próximos pasos: campos pre-llenados listos-para-entregar

Los 6 campos AcroForm de la slide «Próximos pasos» (`PasoNNTitulo` + `PasoNNBody`)
dejan de entregarse como placeholders entre corchetes. Ahora, igual que `Entregables`:

- Claude **redacta los 3 pasos listos-para-entregar** y los aplica tras generar el PDF
  con `customize-acroforms.py` (o un `customize-<slug>.py`). Los campos **siguen
  editables** — ventas ajusta en Adobe Reader.
- Pauta estándar: 1) confirmar fechas/zona horaria · 2) firmar acuerdo + factura del
  50 % de anticipo · 3) reunión de arranque (~30 min) para alinear los casos reales.
- `PASOS_DEFAULTS` en `agregar-campo-precio.py` se mantiene como brackets (estado
  sin customizar). El demo canónico se reproduce con `scripts/customize-cumbre-andina.py`.

**Por qué**: el equipo de ventas necesita una referencia ya redactada para arrancar,
no un placeholder genérico. Documentado en `CLAUDE.md` §6, `propuesta-comercial.md` §10
y `generar-pdf.md`. Archivos: `scripts/customize-cumbre-andina.py` (nuevo),
`agregar-campo-precio.py` (comentario).

---

## 2026-05-16 — [bug] Footer solapado en slides de Programa

En las slides `.s-program` las tarjetas de módulo crecen casi hasta el borde inferior y el footer (`bottom: 24px`) quedaba bisecado por el borde inferior del rectángulo: "CASHEA · PROPUESTA" parecía dentro de la tarjeta. Override `.s-program .foot { bottom: 8px; }` baja el footer a la banda blanca. Aplicado en `cashea/styles.css` y en la plantilla canónica `cumbre-andina/styles.css`.
**Por qué**: el layout `s-program` no reservaba banda inferior para el footer; se veía descuidado.

---

## 2026-05-16 — [plantilla] Desglose instructivo: columnas ajustadas al contenido + ítems con divisor

Refinamiento visual del desglose (ver el rediseño a 1 slide por sesión más abajo) para que
ninguna caja se vea vacía — **estándar para toda propuesta**:

- `.ses-cols` pasa de `flex: 1 1 auto` a `flex: 0 1 auto`: las 3 columnas dejan de estirarse
  hasta el fondo del slide y se igualan entre sí a la más alta. `.ses-body` reparte el aire
  sobrante con `justify-content: space-between` entre Temas, Tiempo y las columnas.
- Cada `<li>` es una fila `flex: 1 1 auto` con `border-bottom` rgba sutil; la lista llena la
  caja igualada con 2 o con 8 ítems. Tipografía de las listas a 15.5px, labels a 12px.

**Por qué**: tras el rediseño, las columnas con pocos ítems dejaban un hueco grande dentro
del rectángulo negro. Archivos: `cumbre-andina/styles.css`, `propuesta-comercial.md` §5.

---

## 2026-05-16 — [plantilla] Demo canónico cumbre-andina re-tematizado a «IA aplicada con Claude»

El demo de referencia `cumbre-andina/` pasa de «Comunicación Efectiva para Equipos
Comerciales» a un **Taller de IA aplicada con Claude** (TA-001 · 3 módulos · 8 h). Solo cambió
el contenido textual de las 12 slides; estructura, CSS y AcroForms intactos. Al clonar para
una propuesta nueva se reemplaza todo el contenido por el eje temático real del cliente
(`CLAUDE.md` §4.3 — no asumir IA por defecto).

**Por qué**: el usuario pidió un demo de referencia más realista y alineado con la oferta
principal de Intezia.

---

## 2026-05-16 — [plantilla] Slide Programa: la `.meta` pasa de métrica a descripción general

En la lámina **Programa** (`.s-program`, slide 4) la línea `.meta` debajo del título deja
de ser un volcado de métricas («3 módulos · 8 horas académicas», y en decks reales una
ristra larga de sesiones/modalidad). Ahora:

- El **título (`<h2>`)** absorbe las cifras: `N módulos · X horas.` — único lugar con números.
- La **`.meta`** se convierte en una **descripción general** de una línea: la síntesis más
  destacable de lo que cubren todos los módulos. Presupuesto ≈ 60 caracteres para caber
  siempre dentro de la franja negra (no la agranda). Cumbre Andina: *"Fundamentos, uso
  diario y adopción responsable de Claude"*.

**Por qué**: la métrica era un volcado mecánico que el usuario no controlaba y repetía el
conteo de módulos; aprovechar ese espacio para vender lo que se lleva el participante es
más útil comercialmente. Diseño/CSS intactos — solo cambia el contenido textual.

Archivos: `cumbre-andina/index.html`, `propuesta-comercial.md` (§4 + checklist).

---

## 2026-05-16 — [plantilla] Desglose instructivo: rediseño a 1 slide por sesión, layout flexible

El «desglose instructivo» (`.s-schedule`) deja de ser **un slide único** con cajas apiladas
y un grid de 5 columnas en tipografía de 9-11px. Ahora es **una sesión por slide**:

- Cada sesión = un `<section class="slide s-schedule">`. 3 sesiones → 3 slides; un
  diplomado de 9 módulos → 9 slides.
- Cada slide: encabezado «ruta de aprendizaje» (nodo numerado + cinta de progreso
  amarillo→naranja + «Sesión X de N»), identidad de la sesión, y los 5 elementos en
  flexbox **sin alturas fijas** — Temas (chips `flex-wrap`), Tiempo (barra proporcional
  con segmentos `flex:<minutos>`), y Estrategias enseñanza/aprendizaje/Recursos en 3 columnas.
- El deck **deja de tener un número fijo de slides**; el `.counter` global se recalcula
  a mano. Los AcroForms se ubican por marcador de texto, así que el desplazamiento de
  numeración no los afecta. `cumbre-andina` pasa de 10 a 12 slides.

**Por qué**: el formato anterior era poco visual y engorroso de presentar, y su estructura
única recortaba o apretaba el contenido al crecer (más subtemas, listas largas, más
módulos). El usuario pidió un layout que se adapte al contenido sin obligar a corregir
propuestas a mano por elementos cortados o diseño deforme. Diseño elegido con el companion
visual de superpowers («Dirección C flexible — una sesión por slide»).

Archivos: `cumbre-andina/{index.html,styles.css}`, `propuesta-comercial.md`, `generar-pdf.md`,
`diseno-taller-capacitacion.md`, `diseno-curso-diplomado.md`.

---

## 2026-05-16 — [plantilla] Campo Entregables pre-llenado desde el desglose instructivo

El campo editable `Entregables` (slide 7) deja de pre-llenarse solo con los 3
entregables institucionales fijos. Ahora, por propuesta, se **combina**:

- **2–4 destacados deducidos** del desglose instructivo de `programa.md` — Claude
  analiza temas, estrategias de aprendizaje y recursos de cada módulo y deduce los
  entregables más relevantes de esa formación.
- **+ los 3 institucionales fijos** (`ENTREGABLES_DEFAULT`, decisión 2026-05-05).

Mecanismo: tras `generar-pdf.sh`, se aplica con `scripts/customize-acroforms.py`
(reescribe `/V` y `/DV` sin tocar el flag readonly → la caja sigue editable). Sin
cambios en scripts canónicos. Documentado en `CLAUDE.md` §6, `propuesta-comercial.md`
y `generar-pdf.md`. Alcance: solo propuestas nuevas.

**Por qué**: el usuario quiere que el campo refleje los entregables reales de cada
propuesta, no solo los genéricos institucionales — conectando el desglose educativo
con lo que el participante "se lleva".

---

## 2026-05-16 — [regla] Cards de módulos: tamaño fijo + tags siempre en 1 línea

**Regla estructural — card inamovible:** `.s-program .modules` lleva `flex: 1; min-height: 0;` y `.s-program .module` lleva `overflow: hidden;`. El grid queda height-constrained al slide y el borde negro de la card nunca se mueve.

**Regla estructural — tags de 1 sola línea:** `.s-program .module .topics li` lleva `white-space: nowrap; overflow: hidden; text-overflow: ellipsis;` y la lista `.topics` usa `flex-direction: column` (no `flex-wrap: wrap`). El tag amarillo **nunca puede wrapear a 2 líneas** — su altura es siempre fija. Sin `letter-spacing` en topics (el valor anterior `0.04em` a 17px sumaba ~19px extra en textos de 28 chars y empujaba el wrap).

**Por qué:** a 17px Inter Bold, el letter-spacing de 0.04em = 0.68px/char. En un texto de 28 chars eso es +19px sobre el ancho disponible (~256px), causando wrap. El wrap duplicaba la altura del tag y la suma de varios tags desbordaba el área disponible de la card (~450px), que era recortada por `overflow: hidden`. El fix estructural (`white-space: nowrap`) garantiza que agregar contenido futuro no pueda tumbar el layout.

---

## 2026-05-16 — [regla] Footer: alineación vertical logo + meta text

**Regla:** `.foot .meta` lleva `line-height: 1`. Sin esto, el span hereda `line-height: 1.45` del body (caja de ~16px a 11px de fuente), y aunque `.foot` tiene `align-items: center`, el texto visualmente queda más arriba que el logo de 28px porque el espacio del interlineado desplaza su caja. Con `line-height: 1` la caja del span colapsa a 11px y el centro visual se alinea exactamente con el centro del logo.

**Aplica a:** `cumbre-andina/styles.css` (plantilla canónica) y toda propuesta que clone esa plantilla.

---

## 2026-05-16 — [regla] Resaltado automático de palabras clave en el deck

Nueva regla `CLAUDE.md` §4.8 + *Regla de copy* en `plantillas/propuesta-comercial.md`:
al redactar el deck, Claude marca con `<strong>` las palabras clave del documento
(nombres propios, herramientas, términos técnicos del eje temático y frases clave).

- **Estilo**: solo negrita — nunca fondo amarillo (reservado a títulos/cierre).
- **Frecuencia**: primera aparición por slide; ~2–3 resaltados por slide máximo.
- **Dónde**: cuerpo (`<p>`, `<li>`); no en títulos/labels ni campos AcroForm.
- **Alcance**: solo propuestas nuevas — las ya generadas no se retocan.

**Por qué**: el equipo de ventas necesita un golpe visual para captar el foco de cada
propuesta de un vistazo. Antes el uso de negritas era esporádico y sin criterio escrito.

---

## 2026-05-05 — [scripts] Defaults institucionales fijos para Entregables y Acreditación

Cambio canónico en `scripts/agregar-campo-precio.py` — `ENTREGABLES_DEFAULT` y `ACREDITACIONES_DEFAULT` pasan de placeholders entre corchetes a **contenido institucional fijo** que aplica a toda propuesta Intezia.

- **Entregables (3 bullets fijos · siempre iguales)**: `Workbook digital por participante.` · `Dashboard de progreso individual.` · `Certificado de participación INTEZIA.`
- **Acreditación (3 bullets fijos · 1 token sustituible)**: `Programa registrado en INTEZIA Education como [CÓDIGO].` · `Cumple con el modelo pedagógico oficial (ABR).` · `Material curado y revisado por el equipo académico.`
- **Único token per-propuesta**: `[CÓDIGO]` se sustituye por el código real del programa (TA-NNN, CU-NNN, CAP-NNN, DIP-NNN) post-script (pypdf abre el PDF y reemplaza en el `/V` del campo `Acreditacion`). Ventas/CAO también puede editarlo en Adobe Reader si hace falta.
- **Resto de defaults sin cambios**: `Programa`, `Notas` y `Pasos` siguen siendo placeholders entre corchetes — esos sí los redacta ventas por cliente.

PDFs regenerados con los nuevos defaults: `hca-venezuela/CAP-015 Claude Cowork - Dominio Corporativo` (CAP-015), `catalogo/TA-003 Intezia Fundamentals · IA + Productividad` (TA-003), `catalogo/` (TA-004).

**Por qué**: el usuario consolidó que estos tres entregables y tres acreditaciones se entregan **siempre** sin variar por cliente — no son placeholders sino el contenido institucional fijo de toda formación Intezia. Solo el código del programa cambia. Esto reduce trabajo per-propuesta y garantiza coherencia institucional.

> **Pendiente de sincronizar**: `CLAUDE.md` Regla 4.4 todavía describe estos campos como "placeholders entre corchetes" — actualizar la tabla cuando el usuario lo confirme.

---

## 2026-05-01 — [regla] Regla 4.6 — Plantilla canónica congelada + defaults Python como placeholders

Estandarización formal de la plantilla. Lo que se codificó:

- **Regla 4.6 nueva en `CLAUDE.md`**: "diseño fijo, contenido editable". Especifica qué está estandarizado (formato, marca, estructura de slides, posiciones absolutas, 13 AcroForms, placeholders, cuadritos visuales, sin texto fantasma) y qué cambia entre propuestas (contenido estático del HTML que edita Claude + contenido editable del PDF que rellena ventas/CAO en Reader). Bloqueante: cualquier cambio estructural exige aprobación explícita y sincronización en cascada (`cumbre-andina/`, plantilla, script, CLAUDE.md, changelog, memoria).
- **Defaults del script Python = placeholders**, no texto de cliente ficticio. `ENTREGABLES_DEFAULT`, `ACREDITACIONES_DEFAULT`, `PROGRAMA_DEFAULT`, `NOTAS_DEFAULT`, `PASOS_DEFAULTS` reescritos como placeholders entre corchetes (ej. `[Entregable 1 — describe qué reciben los participantes]`, `[Acreditación 1 — código del programa, ej. TA-NNN o CU-NNN]`, `[Paso 01 — título corto]`). El equipo comercial entiende inmediatamente qué tipo de contenido va en cada caja.
- **Workflow blindado**: clonar `cumbre-andina/` → editar HTML estático (título, audiencia, módulos) → generar PDF → CAO/ventas rellena los 13 AcroForms en Adobe Reader. Sin tocar CSS, script Python, ni posiciones.

**Por qué**: el usuario consolidó la plantilla y pidió una regla formal que estandarice el resultado. Aclaró que la estandarización debe ser sobre **estructura, colores, placeholders y campos editables** — no sobre el contenido del cliente ficticio (Cumbre Andina). Por eso los defaults Python pasan a placeholders neutros, mientras que el HTML estático de cumbre-andina se mantiene como muestra visual de la estructura (lo edita Claude para cada nuevo cliente).

---

## 2026-05-01 — [plantilla] Multiline AcroForms en slides 7-8 (16 → 13 campos) — base canónica nueva

Reemplazo el modelo de bullets fijos por cajas multiline tipo `<textarea>`. La estructura visual de la propuesta se congela en este estado para todas las propuestas futuras (clonar `cumbre-andina/`).

- **Slide 7 — Entregables y Acreditación**: de 4+3 AcroForms individuales (1 por viñeta, con cuadrito amarillo decorativo) a **2 cajas multiline libres** (`Entregables`, `Acreditacion`). El equipo de ventas escribe la cantidad de líneas que quiera, separadas con Enter; sin coordenadas fijas por bullet, sin límite. Cuadritos amarillos eliminados también de Perfil de Egreso (`<ul><li>` flush left, sin `::before`).
- **Slide 8 — Programa y Notas ahora editables**: pasan de texto estático (`<ul class="bullets">` con 2 `<li>` hardcoded) a 2 AcroForms multiline (`Programa`, `Notas`). Cada bloque conserva un solo cuadrito de acento al inicio del label (■ amarillo en Programa, ■ naranja en Notas) pintado como `::before` del `.block-eyebrow` — decoración fija, no por línea. Gap entre los dos bloques aumentado a ~40 px.
- **Bug visual resuelto — sin texto fantasma**: el HTML detrás de cada caja multiline queda **vacío** (`<div class="multi-box ..."></div>` sin `<span class="acro-default-text">` adentro). El contenido demo vive únicamente en el AcroForm /V (defaults Python: `ENTREGABLES_DEFAULT`, `ACREDITACIONES_DEFAULT`, `PROGRAMA_DEFAULT`, `NOTAS_DEFAULT` con `\r` como separador). Antes, dejar el demo en HTML producía letras asomando a la izquierda donde el AcroForm /BG blanco no llegaba a tapar (especialmente con el offset legacy de 14 px del cuadrito amarillo).
- **Helper Python `_multibox`**: nuevo en `scripts/agregar-campo-precio.py` (reemplaza `_bullet`). Multiline=True, font_size paramétrico (10pt slide 7, 11pt slide 8), `/BG` blanco implícito (tapa cualquier texto bajo el campo). Definido antes de `PRECIO_FIELDS` para que pueda usarse en sus 2 entradas nuevas (Programa, Notas).
- **Total campos**: 16 → **13** (slide 7: 7→2, slide 8: 3→5, slide 9: 6 sin cambios). Distribución verificada con `./scripts/generar-pdf.sh cumbre-andina`.

**Filosofía nueva**: ventas/CAO **no toca diseño**. Modifica solo contenido, abriendo el PDF ya generado en Adobe Reader y editando los AcroForms (clic → seleccionar todo → escribir). Las cajas multiline llegan pre-cargadas con el contenido demo de Cumbre Andina; sales lo reemplaza por lo que aplica al cliente.

**Por qué**: el equipo de ventas/educación pidió control total sobre el copy (entregables, acreditación, programa, notas) sin pedirnos cambios cada vez. El modelo anterior era rígido (cantidad fija de viñetas) y forzaba a editar HTML por cada propuesta. Las cajas multiline AcroForm dan libertad sin permitir romper la marca.

Documentación sincronizada: `plantillas/propuesta-comercial.md` reescrito (header + slide 8 + slide 9 + checklist), `CLAUDE.md` Regla 4.4 con tabla nueva (13 campos, filosofía multiline), memoria persistente actualizada.

---

## 2026-04-30 — [plantilla] Slide 7 con bullets editables estilo Perfil de Egreso + PrecioTotal editable

Refinamientos finales sobre los AcroForm (regla persistente):

- **Slide 7 — bullets editables 1 por línea, estilo Perfil de Egreso.** Eliminado el campo único multiline `Entregables` y `Acreditacion`. Cada bullet es ahora un AcroForm individual (`Entregable1..4` + `Acreditacion1..3` = 7 campos). Visualmente replican el estilo de "Perfil de Egreso": cuadradito amarillo 6×6 px (CSS `::before`) + texto editable a la derecha (sin fondo amarillo lleno). Multiline activado por si las frases son largas y necesitan wrap a 2 líneas. Slot height 36 px, gap 4 px. Coordenadas pt PDF documentadas inline en CSS y script.
- **PrecioTotal ahora es editable** (antes era readonly). Mantiene la acción JS `/AA/C` que calcula `base − |descuento|` automáticamente, **pero también acepta overrides manuales** — útil para redondeos, comisiones, ajustes finos. En lectores que sí ejecutan JS (Adobe Reader) se rellena solo; en lectores sin JS (Preview macOS, navegadores), ventas escribe el total a mano.
- **Bug `NumberObject` vs `FloatObject`**: pypdf `NumberObject(0.957)` → 0 (trunca a int), por eso los `/MK /BG` salieron negros la primera vez. Fix: usar `FloatObject` para colores RGB. Documentado inline en `agregar-campo-precio.py` para no recaer.
- **Total de campos AcroForm**: pasó de 11 a **16** repartidos en 3 páginas (7 + 3 + 6).
- Documentación sincronizada: `plantillas/propuesta-comercial.md`, `CLAUDE.md` Regla 4.4 actualizada con tabla nueva, memoria persistente.

**Por qué**: el usuario pidió que (a) los bullets de Entregables/Acreditación tengan el mismo lenguaje visual que Perfil de Egreso (cuadradito amarillo + texto), no tags llenos; (b) el rectángulo amarillo de TOTAL sea modificable manualmente porque hay casos donde el cálculo automático no aplica (redondeos, comisiones, overrides) y porque Preview macOS no ejecuta el JS de cálculo, dejándolo siempre vacío hasta hoy.

---

## 2026-04-30 — [plantilla] Refinamientos slides 2/3/4/7/9 + AcroForms multi-página

Tras la migración a horizontal, refinamientos por feedback del usuario sobre el deck Cumbre Andina:

- **Slide 2 (Pain)**: tipografía más grande para landscape — h2 36→44, context 15→17, diag-title 11→13, list 12.5→14.5, counter 22→28, padding-left list 50→58.
- **Slide 3 (Goals)**: layout vertical (general arriba a ancho completo, específicos debajo). El general gana protagonismo con `font-size: 22 px`, padding 28 36; los específicos tienen lista en 1 col con tipografía 16 px.
- **Slide 4 (Programa)**: grid adaptable por cantidad de módulos vía CSS `:has()`. 1-3 → 3 cols con `min-height: 490 px` (cards grandes que llenan vertical); 4 → 2×2; 5-6 → 3×2; 7-9 → 3×3 con tipografía y padding reducidos; 10+ → 4 cols. El número romano y los topics se reescalan automáticamente.
- **Slide 7 (Beneficios)**: bloques `Entregables` y `Acreditación` ahora son **AcroForm multiline editables**. El contenido demo se renderiza como texto estático en el PDF (legible sin Reader); el AcroForm con `/MK /BG` blanco se sobrepone en Reader y enmascara al editar. Pre-fill con el contenido de Cumbre Andina.
- **Slide 9 (Próximos pasos)**: eliminado el bloque negro de contacto (Lucía Pino · Project Manager) — no aplica todavía. Las 3 step-cards crecen (`min-height: 260 → 400`, padding `90 → 110/28/32`, ghost `130 → 160`) y cada card tiene **2 AcroForm** (título single-line + body multiline). 6 campos en total para esta slide.
- **Refactor `scripts/agregar-campo-precio.py`**: de un único `FIELDS` + `PAGE_MARKER` a `PAGE_GROUPS` (3 grupos × marker). Soporta multiline (`/Ff` bit 13 = 4096) y default value (`/V` y `/DV`). Total: **11 campos AcroForm** en 3 páginas.

**Por qué**: el usuario revisó el primer pase landscape e identificó que (a) la slide 2 había quedado con tipografía calibrada para vertical, (b) la slide 3 lee mejor apilada que en columnas, (c) el grid de slide 4 estaba locked a 3 cols y un programa con 6/7/8 módulos lo rompería, (d) Entregables y Acreditación cambian por cliente y deben editarse en el PDF, (e) el bloque de contacto en slide 9 todavía no aplica y dejaba la página con 3 cards pequeñas y un footer comercial que no toca llenar.

---

## 2026-04-30 — [regla] Formato horizontal obligatorio para toda propuesta

Cambio permanente: **todas las propuestas Intezia se generan en A4 landscape** (1123×794 px @ 96dpi → 842×595 pt PDF). No revertir a vertical sin instrucción explícita del usuario. Implementado:
- `clientes/propuestas/cumbre-andina/styles.css` rediseñado completo: `--slide-w: 1123px`, `--slide-h: 794px`, `@page { size: A4 landscape }`. Cada slide adaptada a layouts horizontales — Goals/Price en 2 columnas (wrapper `.columns` añadido en HTML para s-goals), Programa/ABR/Próximos pasos en grid de 3 cards en fila, Beneficios en grid de 4 bloques, lista de diagnóstico en 2 columnas. Cards con número decorativo en la parte superior (no lateral) para aprovechar el ancho.
- `scripts/agregar-campo-precio.py`: coordenadas pt PDF de los 3 AcroForm recalculadas para el nuevo layout (base `(540, 379, 780, 415)`, descuento `(615, 327, 780, 355)`, total `(540, 220, 780, 280)`). Comentario actualizado: A4 landscape = 842×595 pt.
- `plantillas/propuesta-comercial.md`: añadida regla permanente al header + nota de "Layout horizontal" + checklist incluye verificación de formato.
- `CLAUDE.md`: sección "Generar el PDF" actualizada y añadida **Regla 4.5 — Formato horizontal obligatorio**.
- Memoria `feedback_estructura_deck_final.md` sincronizada.

**Por qué**: el usuario pidió un cambio permanente del formato porque considera el horizontal más adecuado para el tipo de propuesta que Intezia entrega (lectura tipo deck en pantalla, mayor recorrido visual, layouts en columnas). La regla anterior de "deck congelado" se mantiene en cuanto a paleta/tipografía/bloques, pero el orientation queda redefinido.

---

## 2026-04-28 — [hito] Estructura final del deck APROBADA — congelada como referencia

Tras múltiples iteraciones (v1 → v4 + ajustes), el usuario aprobó la **estructura final** del deck: bloques, paleta, layout, elementos, CTAs, footers. Lo único que cambia entre propuestas futuras es **el contenido** (nombre del programa, módulos, datos del cliente, montos, asesora comercial). El demo `clientes/propuestas/cumbre-andina/` queda como **implementación de referencia canónica**: clonar la carpeta y reemplazar solo el contenido al crear nuevas propuestas.

Detalles finales:
- **Portada**: logo BLANCO 220 px con `margin-left: -28px` (alinea "Education" con padding de los textos), eyebrow "Propuesta formativa" sin fecha, h1 con `.hl` amarillo, lead descriptivo, id-line `Código: XX-NNN` + cliente en bottom 56 px, sin footer. Decoración: rectángulo en gradiente cálido en esquina superior derecha solamente.
- **Slide 9 — Propuesta Económica**: 3 campos AcroForm centrados en Helvetica Bold (`/HeBo`, `/Q 1`), sin bordes (`/BS /W 0`), sin placeholders de guiones; frames con fondo amarillo translúcido (rgba 0.18) — TOTAL en amarillo sólido. Cálculo automático del total via JavaScript del PDF (Adobe Reader; Preview macOS no ejecuta JS).
- **Cierre**: logo BLANCO 220 px **centrado**, mensaje "Danos la oportunidad de llevarte al [siguiente nivel] con [IA]" (siguiente nivel en naranja, IA en chip amarillo), CTA "Esperamos tu Respuesta" (amarillo + sombra dura naranja desplazada 10 px estilo neo-brutalista), bloque de contacto centrado al pie con datos de la asesora y razón social Intezia C.A.

**Por qué**: el usuario quiso terminar la fase de iteración visual y consolidar la plantilla maestra. Las próximas conversaciones sobre propuestas usan esta estructura sin modificarla.

---

## 2026-04-28 — [plantilla] v4: slide Inversión → Propuesta Económica con 3 campos AcroForm

Reescrita la slide de Inversión como **"Propuesta Económica"** con estructura de 4 bloques (Duración / Propuesta + Inversión / Descuento + Total / Notas) separados por líneas divisoras. Tres campos AcroForm: `PrecioBase` y `Descuento` editables manuales, `PrecioTotal` solo-lectura calculado automáticamente vía JavaScript del PDF (regex que filtra dígitos/punto/menos antes de operar, soporta sufijos como "REF" o "USD"). Cálculo automático funciona en Adobe Reader; en Preview macOS los editables funcionan pero el total queda vacío (limitación del lector — usar Adobe Reader para enviar al cliente). Marker de detección cambió de "Tu inversión total" a "Propuesta Económica" con match case-insensitive (necesario porque `text-transform: uppercase` del CSS hace que pypdf extraiga el título en mayúsculas). Notas legales fijas: "Pago en Bolívares a tasa EURO BCV" + "Intezia C.A. se reserva el derecho...". Regla 4.4 de CLAUDE.md actualizada.
**Por qué**: el formato anterior era un único campo monolítico de precio; el nuevo refleja cómo Intezia presenta económicamente sus propuestas (precio base + descuento explícito + total destacado), con cálculo automático para evitar errores aritméticos del equipo comercial.

---

## 2026-04-28 — [plantilla] v3 deck según feedback CAO + consolidación 5→3

Rediseño del deck según observaciones del CAO de Educación: portada con logo grande (200px), eyebrow "Propuesta formativa" sin fecha, "Código:" + cliente como línea media, footer texto sin imagen. Nuevas slides: 2) Punto de dolor + 5 ítems de diagnóstico unificados con frase poderosa, 3) Objetivos estratégicos (general + específicos), 4) Programa con métrica "X módulos · Y horas" + título + objetivo instructivo + temas como tags, 5) Desglose instructivo completo (un cuadro por sesión, 5 columnas), 6) Evaluación 30/50/20 SOLO si curso/diplomado, 7) Metodología ABR fija, 8) Beneficios consolidados (perfil egreso + beneficio + entregables + acreditación + equipo con avatares preparados para foto via `data-photo`). Slides 9-11 (Inversión, Próximos pasos, Cierre) sin cambios. Total: 10 slides para taller (vs 11 antes), 11 para curso/diplomado.

Consolidación de archivos: `plantillas/diseno-{taller,capacitacion,curso,diplomado}.md` → reducidas a `plantillas/diseno-taller-capacitacion.md` y `plantillas/diseno-curso-diplomado.md` con bloques condicionales por subtipo. `empresa/tipos-de-documento.md` reducido de 138 → 73 líneas (eliminada redundancia con plantillas). `scripts/agregar-campo-precio.py` ahora detecta la página de Inversión por texto ("Tu inversión total") en lugar de índice fijo, robusto frente a variaciones de orden de slides.
**Por qué**: el CAO pidió narrativa más pedagógica antes que comercial; el usuario pidió eficiencia de tokens en archivos `.md`.

---

## 2026-04-28 — [git] Repositorio en GitHub: github.com/Isaac150305/intezia-propuestas (privado)

Inicializado git, creado `.gitignore` (excluye PDFs generados de propuestas, mantiene PDFs oficiales en `fuentes/`, ignora `.DS_Store`, secretos, caches de Python/Node y archivos de editor) y subido a GitHub como repositorio **privado** vía `gh repo create --private --source=. --push`. Branch principal: `main`. Primer commit: `e5cb537`.
**Por qué**: el usuario quiere control de versiones antes de seguir iterando. Privado porque el repo contiene logos de marca, plantillas comerciales y referencias internas que no son para distribución pública.

---

## 2026-04-28 — [regla] Campo editable de precio en el PDF (AcroForm)

Toda propuesta debe llevar el precio como **campo AcroForm editable** dentro del PDF, no como texto fijo. El equipo comercial abre el PDF en Adobe Reader o Preview y escribe el valor directamente al hacer clic en el frame. Implementado vía pipeline en dos pasos: Chrome headless renderiza el HTML, luego `scripts/agregar-campo-precio.py` (pypdf) inserta el campo `PrecioTotal` sobre el `.amount-frame` con `position:absolute` en la slide 9 (coordenadas pt: `42, 556, 553, 691`). Wrapper único: `scripts/generar-pdf.sh <slug>`. Inscrito como Regla 4.4 en `CLAUDE.md` y documentado en `plantillas/propuesta-comercial.md`.
**Por qué**: el equipo de ventas analiza cada propuesta y define el precio final caso por caso; un valor fijo en el PDF generaría re-trabajo y errores. El campo editable permite que ventas guarde el PDF con el valor correcto sin tocar el código.

---

## 2026-04-28 — [plantilla] Rediseño visual del deck: vertical A4, logos grandes, identidad por slide

Rediseñado completamente `clientes/propuestas/cumbre-andina/{styles.css, index.html}`:
- Formato cambiado de horizontal 16:9 a **vertical A4** (794×1123 px) — más distintivo y clásico para propuestas comerciales.
- **Logos más grandes**: 108 px en portada, 96 px en cierre, 36 px en footer (vs. 22-32 px antes).
- **Cada slide tiene identidad propia** y aprovecha la paleta entera: portada negra con cintas geométricas, slide 2 fondo amarillo con comilla gigante, slide 6 fondo naranja completo, slide 9 mitad amarillo + bloque negro de detalle, etc.
- Elementos visuales: cintas diagonales, números fantasma, contadores 01/11, ribbons, geometría con `clip-path`, timeline vertical con dots.
- 11 estilos de slide CSS independientes (`.s-cover`, `.s-yellow`, `.s-list`, `.s-stack`, `.s-program`, `.s-orange`, `.s-team`, `.s-time`, `.s-price`, `.s-steps`, `.s-end`).
**Por qué**: el usuario pidió formato vertical, logos más grandes, mayor uso de los colores de marca, "estructura muy distintiva" con cuadros y elementos visuales llamativos, y aprovechar la flexibilidad del código.

---

## 2026-04-28 — [arquitectura] Estructura de cliente aplanada + PDF como entregable

`clientes/<slug>/` con sub-subcarpeta `propuesta/` era anidamiento innecesario. Nueva estructura: `clientes/propuestas/<slug>/` con todo plano dentro (brief.md, programa.md, calendario.md, index.html, styles.css, propuesta.pdf). Las rutas relativas a logos siguen siendo `../../../logos/...` (mismo número de niveles). El PDF se genera con Chrome headless (`--headless=new --print-to-pdf`) usando reglas `@page { size: 1280px 720px }` + `@media print` que convierten cada `.slide` en una página landscape 16:9. Comando documentado en `CLAUDE.md`.
**Por qué**: el usuario pidió aplanar la estructura ("no crees una carpeta por cliente, eso es demasiado") y exigió que el PDF sea visible junto al HTML como entregable estándar.

---

## 2026-04-28 — [cliente:cumbre-andina] Primera propuesta demo generada

Generada propuesta demo completa (cliente ficticio Cumbre Andina S.A.) para iterar el sistema: `brief.md`, `programa.md` (Taller TA-001 según `diseno-taller.md`), `calendario.md` (sin agendar en GCal) y `propuesta/{index.html, styles.css}` con 11 slides aplicando paleta oficial y tipografía Graphit con fallback Inter. Auditoría: 0 menciones de IA (eje temático parametrizado correctamente como "comunicación efectiva en ventas"), solo los 4 colores de marca en CSS, logo presente en cada slide (variante por contraste). Detectado y corregido en revisión: 3 grises derivados (`#1a1a1a`, `#e5e5e5`, `#fafafa`) reemplazados por opacidades del negro oficial.
**Por qué**: la carpeta `clientes/` estaba vacía y el sistema necesita una referencia visual concreta antes de meter clientes reales; sirve para ejercitar todas las reglas (división, marca, plantilla, ABR, parametrización del eje).

---

## 2026-04-28 — [marca] Marca oficial Intezia: paleta y tipografía Graphit

Inscritos los activos oficiales en `empresa/marca-visual.md`: paleta de tres colores (`#000000` Deep Black, `#F4BA1A` Bright Golden Yellow, `#E58423` Vibrant Ochre Orange) y tipografía **Graphit Bold + Graphit Regular** (sans-serif). Estética: minimalista, geométrica, premium tech-focused. Regla 4.1 de `CLAUDE.md` ampliada: ahora la marca completa (logos + paleta + tipografía) es bloqueante para toda salida visual, no solo los logos.
**Por qué**: el usuario suministró el manual de marca y exigió que **TODOS los documentos sin excepción** apliquen estos colores y tipografía.

---

## 2026-04-28 — [arquitectura] v2: 3 categorías reales, 5 plantillas, divisiones y logos

Refactor mayor tras analizar los PDFs oficiales: 3 categorías de documento (Charla / Taller-Capacitación / Curso-Diplomado) en lugar de 4 modalidades. 5 plantillas separadas en `plantillas/diseno-{tipo}.md`. Dos divisiones (Fundación / Educación) con logos obligatorios — regla bloqueante. Modelo pedagógico ABR. Eje temático parametrizable (no asumir IA). PDFs movidos a `fuentes/formatos-oficiales/`.
**Por qué**: la arquitectura v1 asumía modalidades incorrectas y desconocía las divisiones y los logos obligatorios.

---

## 2026-05-19 — [cliente:catalogo] Rediseño HUD del Catálogo de Talleres 2026

Rediseño visual completo del deck `clientes/propuestas/catalogo/Catalogo Talleres 2026/`: lenguaje "HUD Tecnológico" (fondo negro, rejilla amarilla, brackets de esquina, eyebrows monoespaciados) en `hud.css` con unidades `cqw`. 28 → 33 slides (se insertan 5 separadoras de sección). Cada taller suma 1 botón "Más información" (video, `href="#"` placeholder hasta tener URL por taller) + banda "Aplica aquí" → **`https://calendly.com/intezia/30min?month=2026-05`** (los 20 talleres + el CTA de cierre = **21 hipervínculos Calendly** verificados en el PDF). 41 enlaces totales preservados por Chrome headless `--print-to-pdf` como anotaciones Link. 3 slides imagen (`s-img-page`) quedan intactas. Logo institucional discreto al pie de las 28 slides interiores (§4.1).
**Por qué**: el usuario pidió un catálogo más novedoso, tecnológico y legible en TV, con video y aplicación clicables por taller. Toda solicitud de "aplicar" abre Calendly directo — patrón ya establecido en `cumbre-andina` (CTA de cierre) y aquí extendido a cada taller. Spec en `docs/superpowers/specs/2026-05-17-rediseno-catalogo-talleres-design.md`.

---

## 2026-04-27 — [scripts] Utilidades de terminal para PDFs

Añadidos `scripts/listar-pdfs.sh` y `scripts/ver-pdf.sh` para listar y abrir PDFs desde la terminal (Preview / Quick Look).
**Por qué**: el usuario sube documentación en PDF y necesita verla rápido sin pasar por Finder.

---

## 2026-04-27 — [regla] Auto-aprendizaje y actualización continua

El sistema detecta información nueva en cada conversación y la persiste en el archivo correspondiente. Confirmación previa para tocar `empresa/`, `plantillas/` y `CLAUDE.md`; escritura directa en `clientes/<slug>/` y este archivo. Documentado en `CLAUDE.md` sección 9.
**Por qué**: el usuario pidió un sistema "completamente adaptable" que se renueve solo.

---

## 2026-04-27 — [arquitectura] Creación inicial del sistema

Estructura base del repositorio: `CLAUDE.md` como router, carpetas `empresa/`, `plantillas/`, `clientes/`, sistema de delegación por intención.
**Por qué**: Intezia necesitaba una forma estructurada de producir propuestas (slides HTML vía `ckm-slides`), diseñar programas y agendar capacitaciones (Google Calendar MCP) minimizando consumo de tokens.
