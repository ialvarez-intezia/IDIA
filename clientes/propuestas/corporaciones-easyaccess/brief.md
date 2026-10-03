# Brief — Corporaciones EasyAccess · Detección y Habilidades: cotización (CAP-107)

## Datos administrativos

- **Cliente**: Corporaciones EasyAccess · empresa de soluciones de seguridad tecnológica personalizadas (ej. sistemas de control de acceso). No vende productos de stock: cada proyecto se cotiza a la medida, componente por componente, con proveedores nacionales e importados.
- **Naturaleza**: Capacitación in-company · **Detección + Habilidades** (actualizado
  2026-09-01, ver "Actualización 2026-09-01" abajo). Fase 1 (Detección): Intezia audita el
  proceso comercial completo de EasyAccess —desde que el bot entrega el lead hasta el cierre
  del proyecto— y entrega una hoja de ruta priorizada, con evaluación de alternativas de CRM
  **sin desarrollarlo**. Fase 2 (Habilidades, nueva): Intezia **construye junto al equipo de
  tecnología** de EasyAccess un motor de cotización multi-proveedor con las reglas de cada
  modalidad de pago — alcance acotado solo a la cotización, no al CRM. Esto no contradice la
  corrección de 2026-08-28 ("Intezia no desarrolla software"): la Fase 2 es Habilidades
  (capacitación + co-construcción con el equipo real del cliente, usando su propio entorno
  Google), no un desarrollo de software entregado como producto cerrado.
- **Slug**: `corporaciones-easyaccess`
- **División Intezia**: `educacion` (cliente corporativo)
- **Tipo de documento**: Capacitación (`CAP-107`) — **nomenclatura sin cambios** (instrucción
  explícita del usuario: "usando su misma nomenclatura").
- **Servicio** (Modelo Intezia, `empresa/tipos-de-documento.md §0`): `deteccion` — combo
  Detección + Habilidades cotizadas en el mismo documento, mismo criterio que DET-002
  (CLAUDE.md §4.1a punto 1: "combo parcial de 2 servicios como Detección+Habilidades, que
  sigue siendo `deteccion`"). El código sigue siendo `CAP-107` (nomenclatura vieja, ya
  contratada así con el cliente) — caso ya documentado desde 2026-08-28 como excepción
  deliberada (código `CAP-` con servicio `deteccion`, no un error de nomenclatura).
- **Programa**: Detección y Habilidades — cotización, Corporaciones EasyAccess
- **Eje temático**: auditoría del proceso completo —desde que el bot entrega el lead hasta el
  cierre del proyecto—, evaluación de alternativas de CRM sin desarrollarlo, y construcción
  colaborativa de un motor de cotización multi-proveedor con reglas por modalidad de pago,
  para un modelo de negocio sin productos de stock.
- **Modalidad**: a definir en próxima reunión
- **Duración**: 2 fases, sin horas impuestas — Fase 1 · Detección (Iniciación, Auditoría,
  Diagnóstico, Diseño) + Fase 2 · Habilidades (Motor de Cotización, Del Lead a la
  Cotización), a definir según el alcance de cada una.
- **Fecha del brief**: 2026-08-16 · **actualizado**: 2026-08-28 (detalles de la reunión de
  seguimiento), 2026-08-28 (corrección: se retira la promesa de construcción de CRM) y
  2026-09-01 (se agrega Fase 2 · Habilidades, ver abajo)
- **Estado**: `En corrección` (propuesta ya "Enviada" el 2026-08-16, vuelve a revisión por
  este cambio de alcance — al regenerar el PDF vuelve a "Enviada")

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Cliente referente**: Reynaldo (impulsor del proyecto del lado de EasyAccess) · cargo por confirmar

## Por qué este proyecto

EasyAccess vende seguridad tecnológica a la medida, no productos de catálogo: cada proyecto es distinto, con proveedores nacionales e importados, disponibilidad y fechas de entrega propias — no es un proceso simple de inventario, requiere manejar varias variables a la vez. Un bot (construido por VirtualScape, dato interno — no se nombra en el deck) responde por redes sociales y redirige el lead a un agente humano: ahí termina la automatización de hoy. Todo lo posterior es manual: la cotización se arma en Google Sheets y el seguimiento depende de las personas, sin alertas de campos incompletos y con métricas inconsistentes — y el proceso se satura cuando llegan varias solicitudes al mismo tiempo. Ya buscaron una solución de cotización/facturación en el mercado y no la encontraron: ese software está diseñado para productos de stock con precio fijo, no para lo que EasyAccess vende. A eso se suma que no tienen CRM (los leads se asignan a mano en un grupo de WhatsApp, sin poder medir el desempeño de ventas ni auditar dónde se pierden los negocios) y que los valores cambian según la modalidad de pago del cliente, obligando a recalcular cada cotización a mano.

## Diagnóstico (5 puntos)

1. El modelo de negocio de EasyAccess es vender seguridad personalizada, no productos de stock: cada proyecto exige cotizar con proveedores nacionales e importados, disponibilidad y fechas de entrega propias — no es un proceso simple de inventario.
2. El bot actual responde por redes sociales y redirige el lead a un agente humano: ahí termina la automatización de hoy. Todo lo posterior depende de personas, sin alertas de campos incompletos ni métricas consistentes.
3. La cotización se arma 100% a mano en Google Sheets: se satura cuando llegan varias solicitudes al mismo tiempo, y ya están perdiendo clientes por el retraso.
4. Sin CRM, los leads se asignan a mano en un grupo de WhatsApp: no pueden medir el desempeño de su fuerza de ventas ni auditar el proceso — solo saben que se pierden negocios, no dónde.
5. Los valores varían según la modalidad de pago del cliente, obligando a recalcular manualmente cada cotización: otra capa de trabajo manual sobre un proceso que ya es lento.

> Nota aparte (no cotizada en esta propuesta): EasyAccess tiene un bot de Instagram y TikTok captando leads, subutilizado — solo recoge datos básicos y redirige a un agente humano. Sin CRM ni cotización rápida detrás, la demanda que genera no se atiende a tiempo y el cliente pierde interés en el camino. Evaluar qué consultoría ofrecer sobre el bot requiere una **reunión de alcance aparte**; no se compromete alcance ni precio sobre eso en este documento. El nombre del proveedor del bot (VirtualScape) es dato interno — no se menciona en el deck.

## Necesidades identificadas (actualización 2026-08-28, reunión de seguimiento)

- **Automatizar desde que el bot entrega el lead hasta el cierre del proyecto**: seguimiento de
  tiempos de respuesta y estado de cada propuesta, una calculadora/motor de cotizaciones
  integrado, y métricas de efectividad de campañas y atención personalizada.
- **CRM a medida o implementación de uno existente con procesos automatizados** — el cliente
  prefiere avanzar por fases, empezando por las etapas más críticas del proceso.

> Estas necesidades son lo que el diagnóstico va a **priorizar y evaluar**, no lo que esta
> propuesta desarrolla. El motor de cotizaciones y el CRM son alternativas que se evalúan en
> la Etapa 3 (Diagnóstico) y se plasman como recomendación en la Etapa 4 (Diseño) — Intezia no
> los construye en este servicio (corrección 2026-08-28).

## Estructura del proyecto

Servicio de Detección de fase única, 4 etapas (numeración fija en todo el deck: programa,
cronograma, roadmap, hoja de precio):

### Etapa 1 · Iniciación

Alcance confirmado y calendario de sesiones con **ventas, tecnología y Reynaldo**.

### Etapa 2 · Auditoría

Sesiones junto a ventas, tecnología y Reynaldo para mapear el proceso completo —desde que el
bot entrega el lead hasta el cierre del proyecto— con más detalle del que se puede cubrir en
una sola reunión: cotización multi-proveedor, asignación de leads, alertas y métricas
faltantes. Incluye una primera revisión del bot de Instagram/TikTok, para acotar (no resolver)
qué conviene evaluar después en la reunión de alcance aparte.

### Etapa 3 · Diagnóstico

Priorización de los cuellos de botella identificados por impacto y esfuerzo, y evaluación de
alternativas de CRM y motor de cotizaciones para el modelo de negocio de EasyAccess —**sin
desarrollarlas**: Intezia no construye software en este servicio.

### Etapa 4 · Diseño

Reporte Final con la hoja de ruta priorizada y recomendaciones concretas de por dónde empezar.

> **Renombrado 2026-08-28 (corrección)**: la versión anterior tenía 3 etapas (Detección →
> Construcción guiada → Implementación), con solo la primera cotizada y las otras dos
> "progresivas" — implicando que Intezia construía el CRM con el equipo de tecnología del
> cliente en una fase futura. Se retiró esa promesa por completo: ahora es un servicio de
> Detección de **fase única** con 4 etapas internas, todas cotizadas en esta misma hoja.

## Especificaciones del programa

- **Duración**: servicio de fase única, sin horas impuestas; se define según el alcance.
- **Modalidad**: a definir en próxima reunión con el cliente (Presencial / Online Síncrono / Híbrido).
- **Audiencia**: equipo de ventas de EasyAccess (4-5 personas) + equipo de tecnología (2 personas) + Reynaldo.
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.

## Recomendación de herramienta — retirada del deck (corrección 2026-08-28)

- Esta sección documentaba una recomendación de **Claude** para la fase de Construcción
  guiada (Gemini/ChatGPT como punto de partida, Claude para sostener el proceso reglado de
  cotización). Esa fase ya no existe: Intezia no construye software en este servicio, así que
  la recomendación de herramienta específica se retiró del deck junto con ella.
- Si el diagnóstico evalúa alternativas de IA para el CRM o el motor de cotizaciones, esa
  evaluación se documenta como parte del Reporte Final (Etapa 4 · Diseño) — no como un
  compromiso de Intezia de construir o de una herramienta puntual pre-decidida.
- **El bot de Instagram/TikTok sigue fuera de todo esto**: su diagnóstico y cualquier
  sugerencia de herramienta se define en la reunión de alcance aparte.

## Propuesta económica

- **Hoja "Inversión por fases"** (`.s-price`, actualizada 2026-09-01 — antes era la hoja
  estándar de 1 sola fase): Fase 1 (Detección) y Fase 2 (Habilidades) **ambas con caja de
  precio editable** (`PrecioFase1`, `PrecioFase2`), sumadas en un solo "Inversión total del
  proyecto" — mismo patrón que Go Pharma CAP-030 / Simple TV DET-002 (ambas fases cotizadas
  ya, ninguna diferida), decisión explícita del usuario porque esta corrección reemplaza la
  propuesta ya "Enviada" del 2026-08-16.
- Bloque destacado **"Importante"** con la implicación comercial: el servicio se presta bajo los **términos y condiciones**, aceptados por ambas partes al avanzar con la propuesta.

## Entregables consolidados

- Informe de diagnóstico del proceso completo —desde el handoff del bot hasta el cierre del proyecto—, con los puntos de mayor apalancamiento identificados.
- Motor de cotización multi-proveedor, construido junto al equipo de tecnología (Fase 2).
- Evaluación de alternativas de CRM, sin desarrollarlo (sigue siendo solo evaluación en Fase 1).
- Certificado de participación INTEZIA.

> La caja AcroForm de Entregables (`.entregables-box`) es angosta —158×117pt, ≈27
> caracteres/línea— y solo tiene capacidad legible para ~4 destacados cortos antes de
> desbordar (bug conocido, ver memoria `bug-entregables-acroform-box-narrow`). La primera
> lectura del bot de Instagram/TikTok **no entra en la caja visible del deck**, pero sigue
> siendo un entregable real de la Etapa 2 · Auditoría (documentado en `programa.md` §5.1-5.2
> y en la "Nota aparte" del Diagnóstico, arriba).

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-107** en INTEZIA Education al cerrar el acuerdo.
- **Objetivo de fondo del cliente**: dejar de perder clientes por retrasos en la cotización, y poder medir y auditar su proceso comercial — el diagnóstico prioriza qué automatizar primero; su desarrollo o adquisición queda fuera del alcance de este servicio.

## Notas de diseño

- Clonado de `fasto/` (CAP-104, mismo patrón de roadmap/cronograma de 1 sola página con 3 etapas en línea, y misma asesora comercial Verónica Rubio). El deck original (2026-08-16) diferenciaba este proyecto de Fasto agregando una Fase 2/3 de "construcción guiada" cotizada de forma progresiva — esa diferenciación se retiró por completo el 2026-08-28 (ver subsección de corrección abajo): ahora es un servicio de Detección de fase única, más simple que Fasto en alcance (Fasto sí construye software, este servicio no).
- **12 slides**, 1 sola instancia de `.s-schedule`, `.s-roadmap` (rmx-linear, 3 nodos en línea + resultado) y `.s-program` (4 módulos, grid 2×2), ya que es un solo proyecto (no fork multi-área) con equipo pequeño (ventas 4-5 + tecnología 2 + Reynaldo).
- **Slide de Impacto**: datos reales sobre gestión de leads y CRM (no cadena de suministro, no aplica al eje de EasyAccess) — Harvard Business Review, *The Short Life of Online Sales Leads* (Oldroyd, McElheran y Elkington, 2011): sobre 2.241 empresas auditadas en EE. UU., 37% respondió a un lead web dentro de la primera hora y 23% nunca respondió; contactar dentro de la primera hora hace a una empresa casi 7 veces más probable de calificar el lead que contactarlo una hora después. Salesforce, *State of Sales* (2023): los representantes de ventas dedican menos del 30% de su tiempo a vender; el resto se va en tareas administrativas y de registro manual de datos. Nucleus Research, *CRM Pays Back $8.71 for Every Dollar Spent* (2014): retorno promedio de $8.71 por cada dólar invertido en CRM. Las tres fuentes se citan verbatim en la slide.
- Reglas §4.11 y §4.13 respetadas: no se afirma que EasyAccess migra de ningún stack tecnológico (Claude se suma al entorno Google/ChatGPT que ya usan); sin guion largo en el copy de cara al cliente. §4.12: sin siglas de jerga sin explicar (CRM se usa tal cual, es término de uso general en el sector comercial, no se expande).
- **Asesora comercial**: Verónica Rubio (contacto en slide de cierre y aquí), mismos datos que en `fasto/`.

### Actualización 2026-08-28 (reunión de seguimiento) — solo contenido, sin tocar la estructura

- **Servicio**: se agrega `servicio: "deteccion"` a `meta.json` (campo que no existía cuando se
  creó el deck, 2026-08-16, antes del Modelo Maestro de Servicio). **Código sin cambios**
  (`CAP-107`) — instrucción explícita del usuario. Ver nota en "Datos administrativos" sobre
  por qué es una excepción (código viejo + servicio nuevo).
- **Etapa 1 renombrada**: "Descubrimiento" → "Detección", en todo el deck (programa, cronograma,
  roadmap, hoja de precio) y en este brief — instrucción explícita del usuario ("aquí vamos a
  usar detección").
- **Terminología "Excel" → genérica**: el titular del deck ("Del Excel manual al CRM que
  cotiza solo", repetido en portada/objetivos/programa/cronograma/beneficios/cierre) pasa a
  "hojas de cálculo manuales" — el cliente confirmó que el proceso vive específicamente en
  **Google Sheets**, no Excel. Se generaliza el titular (evita nombrar una herramienta
  específica que podría volver a cambiar) y se usa **Google Sheets** en el contenido factual
  del Diagnóstico, donde sí aplica ser específico.
- **Contenido nuevo incorporado**: bot construido por VirtualScape (dato interno, no
  nombrado en el deck) que responde por redes y redirige a un agente humano — ahí termina la
  automatización hoy; falta de alertas de campos incompletos y métricas inconsistentes;
  saturación con solicitudes simultáneas; complejidad de cotizar productos nacionales vs.
  importados con disponibilidad y fechas de entrega propias (no es inventario simple); Fase 2
  ahora incluye explícitamente un motor/calculadora de cotizaciones y métricas de campañas y
  atención personalizada; Fase 3 enfatiza implementación por etapas (empezando por lo más
  crítico) y adopción real del equipo, no solo activación de la herramienta.
- **No se tocó en esta actualización de contenido** (fuera de alcance en ese momento): la
  slide de Metodología ABR (salvo la línea del pilar 03 que afirmaba que el CRM "se
  construye" — corregida por ser factualmente incorrecta, no por retrofit visual). El
  retrofit de Beneficios y Cierre sí se aplicó poco después, mismo día — ver subsección
  siguiente.

### Actualización 2026-08-28 (corrección) — Intezia no desarrolla software

Corrección posterior a la actualización de contenido de arriba, mismo día: la propuesta
(deck original de 2026-08-16, y la primera reescritura de esta misma fecha) prometía que
Intezia **construía** un CRM y un motor de cotizaciones junto al equipo de tecnología de
EasyAccess (Etapa 2 · Construcción guiada, Etapa 3 · Implementación), cotizadas de forma
progresiva. Instrucción explícita del usuario: *"no vas a mencionar que vamos a construir el
crm ni nada por el estilo... el objetivo principal no puede ser desarrollo porque nosotros
para este momento no desarrollamos."*

- **Se retiró por completo** la promesa de construcción: ya no hay Etapa 2 (Construcción
  guiada) ni Etapa 3 (Implementación), ni fases progresivas cotizadas a futuro.
- **El bot y la cotización manual se mencionan solo como cuellos de botella reportados por el
  cliente** (Diagnóstico, slide 2) — nunca como algo que Intezia va a construir o automatizar
  directamente.
- **Nueva estructura**: servicio de Detección de fase única, 4 etapas (Iniciación → Auditoría
  → Diagnóstico → Diseño), entregable insignia = Reporte Final con hoja de ruta priorizada
  (no un CRM construido). Mismo patrón que `embutidos-zeus/` (DET-003), el otro piloto de
  Detección pura del sistema — sin la parte de auditoría por departamento porque EasyAccess
  es un solo equipo, no varias áreas con sesiones separadas.
- **Slides reescritas**: Portada, Objetivos, Programa (4 módulos IADD), Ruta del proyecto
  (columnas por dimensión — qué se hace/qué se logra/recursos — en vez de por etapa),
  Roadmap (3 nodos: Auditoría, Diagnóstico, Diseño + resultado), pilar 03 de Metodología ABR,
  Beneficios (perfil de egreso, beneficio del programa, 2 líneas de Equipo facilitador),
  Propuesta Económica (se retiró el bloque `.cot-progressive` y el "· Fase 1" del footer),
  Cierre (end-message).
- **Impacto (slide 9) no se tocó**: las estadísticas sobre gestión manual de leads y ROI de
  CRM siguen siendo motivación válida para el diagnóstico, sin comprometer a Intezia a
  construir nada.

### Actualización 2026-08-28 (retrofit visual) — Beneficios v2/v3 y Cierre escalera

Tercera pasada del mismo día, pedido explícito del usuario ("la hoja de beneficios me la
dejaste igual que las anteriores hay que usar el formato de las nuevas que hemos construido
hoy" + "el slide de cierre también está en formato antiguo, usa el nuevo"). A diferencia de
Cavedatos/Go Pharma/Amcor (que ya estaban en formato v2 y solo subieron a v3 ampliado), CAP-107
partía del formato **más viejo del sistema** (anterior incluso a v2, 2026-08-16): Perfil de
egreso/Beneficio del programa formativo/Entregables/Acreditación + Equipo facilitador, y Cierre
con CTA a Calendly + `info@intezia.com`. Se saltó directo a v3 ampliado sin pasar por v2 como
paso intermedio (el resultado final es el mismo).

- **Beneficios**: reemplazado por completo por el formato v2/v3 (`s-benefits-v2`) —
  Resultados · Por qué Detección · Entregables · Valor inmediato, tarjetas oscuras, grid de
  570px. El bloque "Equipo facilitador" se retiró (§4.10a). El campo AcroForm `Acreditacion`
  se reutiliza tal cual para "Valor inmediato" (mismo patrón que el resto del sistema, el
  nombre interno del campo no cambia).
- **Cierre**: reemplazado por el formato escalera (`.end-summit` + `.end-stairs`, 4 cajas
  AcroForm `CierreResultado`/`CierrePaso1-3`) en vez del CTA fijo a Calendly. Correo de
  Empresa actualizado a `servicio@intezia.com` (estándar 2026-08-27, §4.10a punto 5).
- **CSS**: se agregó el bloque `.s-benefits-v2` (copiado de `go-pharma/styles.css`, layout
  ampliado ya corregido) y se reemplazó el bloque `.end-message` por la escalera (copiado de
  `go-pharma/styles.css` también, mismo `.s-end` base ya idéntico entre ambos decks).
- **Bug encontrado y corregido**: la regla `@media print` que oculta el texto demo
  (`.acro-default-text`) antes de hornear el AcroForm solo cubría `.acro-area`/`.acro-bullet`
  — no las clases nuevas `.end-summit`/`.stair-field`. Sin ese ocultamiento, Chrome horneaba
  el texto demo como contenido normal de página, y el widget AcroForm (agregado después por
  `customize-corporaciones-easyaccess.py`) se dibujaba encima en una posición ligeramente
  distinta, produciendo un efecto de texto fantasma/doblado en toda la slide de Cierre.
  Corregido agregando esas dos clases a la regla `@media print` existente.
- **Script nuevo**: `scripts/customize-corporaciones-easyaccess.py` (no existía) — agrega las
  4 cajas de Cierre escalera y re-hornea Entregables/Acreditacion con fondo oscuro y layout
  ampliado, mismo patrón que `customize-cavedatos.py`/`customize-go-pharma-cap030.py`. **Orden
  del par crítico**: corre `customize-acroforms.py` primero, este script SIEMPRE al final —
  invertirlo pisa el fondo oscuro de Beneficios con el blanco por defecto (ver
  `aprendizajes.md`, entrada "Orden del par customize con script propio").
- **No tocado**: la slide de Metodología ABR (existencia y estructura) sigue sin retrofit —
  no fue parte de lo pedido; solo se corrigió antes la línea factual del pilar 03 sobre el CRM.

### Actualización 2026-09-01 — se agrega Fase 2 · Habilidades (motor de cotización)

Instrucción explícita del usuario, a partir de una reunión de seguimiento con el cliente.
Minuta pegada por el usuario (resumen): el modelo de negocio de EasyAccess es vender
seguridad personalizada, no productos de stock — eso es la raíz de todo lo demás. El cuello
de botella principal es la cotización manual (Google Sheets, multi-proveedor, componente por
componente); ya buscaron software de cotización/facturación en el mercado y no sirve, porque
está diseñado para productos de stock con precio fijo. Segunda brecha: no tienen CRM, los
leads se asignan a mano en un grupo de WhatsApp, no pueden medir desempeño ni auditar dónde
se pierden negocios. Tercer problema: los valores varían según la modalidad de pago del
cliente, obligando a recalcular cada cotización a mano. El bot de Instagram/TikTok capta
leads pero está subutilizado — la brecha entre el primer contacto y la cotización final es
demasiado larga y el cliente pierde interés en el camino. Recursos: ventas (4-5), tecnología
(2), ecosistema Google (Gemini, NotebookLM) + ChatGPT.

**Decisión de alcance (instrucción explícita del usuario) — acotado solo a cotización:**

- **Se agrega una Fase 2 de Habilidades** para construir junto al equipo de tecnología el
  motor de cotización — **NO el CRM**, que sigue siendo solo evaluación en la Fase 1
  (Detección), sin desarrollarse. El usuario fue explícito: *"solo toma en cuenta la parte
  de cotizacion y construirla junto a ellos en la parte de habilidades"*.
- **Por qué esto no contradice la corrección de 2026-08-28** ("Intezia no desarrolla
  software"): la Fase 2 es un servicio de **Habilidades** — Intezia capacita y co-construye
  con el equipo real del cliente (tecnología, 2 personas), usando el entorno Google que ya
  tienen (Gemini, NotebookLM), no un desarrollo de software entregado como producto cerrado
  por un proveedor externo. Mismo patrón que "construir un skill/agente propio en Copilot
  Studio" en otras propuestas de Habilidades (DET-002, CAI-002) — transferencia de
  capacidad, no entrega de producto.
- **El "intermedio" entre que el bot genera el lead y llega la cotización** (mencionado en
  la reunión) se deja **abierto, sin comprometer una solución específica todavía**:
  instrucción explícita del usuario, *"no plantees una solución intermedia como escrita en
  piedra sino mencionar que podemos solucionar con eso"*. En el deck esto vive como el
  Módulo II de la Fase 2 ("Del Lead a la Cotización"), redactado como una exploración
  conjunta, no como un entregable cerrado.
- **Ambas fases se cotizan ya, en el mismo documento** (instrucción explícita del usuario,
  recomendación aceptada): la hoja de precio pasa de la variante estándar (1 fase) a
  "Inversión por fases" (2 fases, `PrecioFase1` + `PrecioFase2`, patrón go-pharma/DET-002) —
  ver "Propuesta económica" arriba.
- **Estructura del deck**: 12 → 14 slides. Se agregan 1 slide de Programa (Fase 2, 2 módulos:
  Motor de Cotización + Del Lead a la Cotización) y 1 slide de Cronograma (`.s-schedule`,
  Fase 2). El Roadmap se restructura de "3 etapas internas de Detección" (Auditoría/
  Diagnóstico/Diseño) a "2 fases del combo" (Fase 1 · Detección → Fase 2 · Habilidades →
  Resultado) — mismo criterio que DET-002: el roadmap muestra el panorama del combo, el
  detalle por etapa ya vive en Programa/Cronograma de Fase 1 (sin cambios de contenido).
- **CSS**: `styles.css` local (este deck no usa `../_base/styles.css`) no tenía las reglas
  `.fase-price-row`/`.fase-price-copy`/`.fase-price-desc`/`.fase-price-frame` — se copiaron
  de `go-pharma/styles.css`. Los frames de cotización (`base-frame`/`discount-frame`/
  `total-frame`) y sus labels se reposicionaron (antes alineados a la hoja estándar de 1
  fase, ahora a los rects reales de `FASE_PRICE_FIELDS` en `agregar-campo-precio.py`) — sin
  este ajuste, la caja visible en el HTML y el campo AcroForm real del PDF quedan
  desalineados.
- **Script**: `customize-corporaciones-easyaccess.py` gana la lógica de eliminar el campo
  huérfano `PrecioFase3` (el marcador "Inversión por fases" siempre crea 3 slots) y
  recalcular el subtotal como Fase1+Fase2 — mismo patrón que
  `customize-go-pharma-cap030.py`/`customize-simple-tv-det002.py`. También se agregó
  `/NeedAppearances=False` al final (ver memoria `bug-needappearances-cliente-regenera-
  campos`) y se corrigieron los defaults de `CierreResultado`/`CierrePaso3` (que viven
  hardcodeados en el script, no en el HTML).
- **No se tocó**: Diagnóstico (slide 2), Metodología ABR (estructura), Impacto — siguen
  siendo válidos sin cambios. El bot de Instagram/TikTok sigue fuera de alcance (reunión
  aparte, sin cambios).
- **Bugs técnicos encontrados y corregidos de paso** (no pedidos, pero bloqueantes):
  1. **Grid de Programa con 2 módulos**: la slide de Programa · Fase 2 (2 módulos) usaba el
     grid de 3 columnas por defecto, dejando un tercio de la slide vacío. Se agregó una
     regla `:has()` en `styles.css` para que exactamente 2 módulos usen 2 columnas.
  2. **Campos de Cierre fuera de `/AcroForm/Fields`**: `customize-corporaciones-
     easyaccess.py` reconstruía el array de campos (`kept_fields`) para quitar
     `PrecioFase3`, pero el paso de Cierre seguía usando la variable vieja (`fields`) para
     agregar sus 4 cajas — nunca quedaban registradas en el catálogo real del formulario
     (solo como anotaciones de página). Corregido reapuntando `fields = kept_fields`
     después de la reasignación. Mismo defecto probablemente presente (sin corregir, fuera
     de alcance) en `customize-amcor.py`, `customize-dhl.py` y
     `customize-simple-tv-det002.py` — ver memoria `bug-fields-kept-fields-divorcio`.

## Pendientes

- Confirmar modalidad (Presencial / Online Síncrono / Híbrido) en la próxima reunión.
- Confirmar cargo y datos de contacto directo de Reynaldo.
- Confirmar fechas tentativas de inicio de cada fase.
- Confirmar presupuesto indicativo de la Fase 1 (Detección) y la Fase 2 (Habilidades).
- Agendar la reunión de alcance aparte para el bot de Instagram/TikTok (no incluida en el alcance de esta propuesta).
- Si el cliente pide comprometerse a una solución específica para el "intermedio" lead→cotización, evaluar si eso pasa a ser un módulo propio con alcance cerrado (hoy queda abierto, ver Actualización 2026-09-01).
