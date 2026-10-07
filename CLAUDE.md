# Sistema de Propuestas — Intezia

Router del sistema. Léelo siempre. Carga archivos hijos **solo cuando la tarea lo pida**.

---

## 1. Identidad

Intezia capacita bajo dos divisiones: **Fundación** (social/comunitario) y **Educación** (corporativo/profesional). Toda propuesta se adscribe además a uno de **4 servicios** del Modelo Intezia — **Detección**, **Habilidades**, **Políticas**, **Innovación** — eje ortogonal a la división (§4.1a). Dentro de Habilidades, tres categorías curriculares: **Charla**, **Curso/Diplomado**, **Taller/Capacitación In-Company**; el servicio se entrega **por defecto en el formato compacto de 9 slides** (§4.21). Modalidad (Presencial / Online Síncrono / Asíncrono / Híbrido) = atributo transversal. **Alianza** es una bandera aparte (`alianza: sí|no`), no un 5to servicio.

> `empresa/identidad.md` · `empresa/divisiones.md` · `empresa/tipos-de-documento.md` · `empresa/catalogo.md`

---

## 2. Catálogo

| Categoría | Subtipos | Detalle |
|---|---|---|
| Charla | — | `empresa/catalogo.md#charlas` |
| Taller / In-Company | `TA-`, `CAI-` (desde 2026-08-30; antes `CAP-`, ver `empresa/catalogo.md`) | `empresa/catalogo.md#talleres-y-capacitaciones` |
| Curso / Diplomado | `CU-`, `DIP-` | `empresa/catalogo.md#cursos-y-diplomados` |

---

## 3. Políticas comerciales

Cotizaciones válidas **30 días** · Anticipo **50%** · Cancelación <7 días = no reembolsable.

> Tabla completa: `empresa/politicas-comerciales.md`

---

## 4. Reglas críticas

### 4.1 Marca visual — bloqueante

Antes de generar cualquier salida visual:

1. **División**: verifica `brief.md → division`. Sin división, preguntar y guardar. Sin respuesta, no generar.
2. **Logo**: `logos/{fundacion|educacion}/{BLANCO|NEGRO}.png`. BLANCO en fondo oscuro, NEGRO en fondo claro. Logo en portada Y en cada slide.
3. **Paleta**: solo `#000000` / `#F4BA1A` / `#E58423` / `#FFFFFF`. No inventar colores.
4. **Tipografía**: Graphit Bold (títulos) + Graphit Regular (cuerpo). Fallback: Inter/Poppins, nunca serif.

> Tokens CSS: `empresa/marca-visual.md`

### 4.1a Servicio — bloqueante

Antes de generar cualquier salida (visual o de texto), además de la división:

1. **Servicio**: verifica `brief.md → servicio`. Sin servicio, preguntar *"¿Detección,
   Habilidades, Políticas o Innovación?"* y guardar. Sin respuesta, no generar. Si el cliente
   pide un **plan que combine los 4 servicios como una sola hoja de ruta secuencial** (no un
   combo parcial de 2 servicios como Detección+Habilidades, que sigue siendo `deteccion`),
   usa `integral` (§4.1b) — pregunta y confirma con el usuario antes de asumirlo, igual que
   con los otros 4 valores.
2. **Alianza** (si aplica): pregunta aparte, `brief.md → alianza: sí | no` — no sustituye la
   pregunta de servicio, se suma a ella.
3. División y servicio son **ejes ortogonales** — no se infiere uno del otro. Un cliente de
   Fundación puede adquirir cualquiera de los 5 servicios, igual que uno de Educación.
4. **Portada visible — bloqueante (2026-09-01)**: el eyebrow de la Portada (`.s-cover
   .eyebrow`) debe nombrar el/los servicio(s) reales de `brief.md → servicio`, no solo el
   tipo de documento genérico. "Propuesta formativa · Capacitación in-company" no dice nada
   del servicio — corrige a "Propuesta formativa · Servicio de Habilidades" (en los decks
   canónicos) o a **"Propuesta de proyecto · Servicio de Habilidades"** (plantilla compacta
   §4.21: la propuesta se presenta como proyecto, no como capacitación; dirección 2026-10-05). Si el servicio
   es un combo (ej. Detección + Habilidades cotizadas juntas, como DET-xxx), menciona ambos:
   "Servicio de Detección y Habilidades". Aplica a toda propuesta nueva o regenerada de aquí
   en adelante — no retroactivo a decks ya entregados salvo que se pida. Detalle y ejemplos
   por servicio: `plantillas/propuesta-comercial.md` → *Reglas de copy*.

**Tabla servicio → patrón de estructura** (equivalente a la de §4.2 para tipo de documento):

| Servicio | Patrón de estructura | Estado |
|---|---|---|
| Detección | Clonar y adaptar `clientes/propuestas/pilotes-perforados/` (roadmap origen→bifurcación→rutas→convergencia→resultado + mapa de calor 6 columnas) | Sin piloto canónico propio — construir caso por caso hasta que exista |
| Habilidades | **Plantilla compacta** `plantillas/habilidades-compacto.md` (§4.21): 9 slides (7 en Fundación) en el orden de las preguntas del cliente, dirigida por `datos.json`. **Todas las categorías** (charla, taller, capacitación, curso, diplomado) y **cualquier cliente**, sin preguntar el formato: un programa de módulos se reexpresa con las recetas de la spec §1b | **Único formato de Habilidades** (estándar desde 2026-10-05; v2.0 desde 2026-10-07; sin excepciones desde 2026-10-07) — caso base DUSA CAI-035 (`datos.ejemplo-dusa.json`). Los decks canónicos y los compactos v1.x ya entregados no se tocan salvo que se pida modificarlos o rehacerlos (spec §13) |
| Políticas | **Pendiente de decisión de formato** (Ivana + David: ¿deck o informe de consultoría?) | No construir hasta que se resuelva — ver `empresa/tipos-de-documento.md §0` |
| Innovación | Clonar `clientes/propuestas/zoom-innovacion/` (roadmap `.rmx-linear` adaptado a ciclo recurrente: Kick-off→Ejecución→Medición→se repite + cotización "Inversión por Permanencia" de 3 columnas 3/6/12 meses) | Piloto: `clientes/propuestas/zoom-innovacion/` (INN-001, 2026-08-30) |
| Integral (§4.1b) | Clonar `clientes/propuestas/aerocentro/` (multi-fase, roadmap `.rmx-linear`) y extender de 3 a 4 fases — el grid ya es flexible por número de columnas, no requiere cambios de CSS | Piloto: `clientes/propuestas/simple-tv-all001/` (ALL-001, 2026-08-28) |

> Detalle completo y razones: `empresa/tipos-de-documento.md §0`.

### 4.1b Servicio "integral" (los 4 servicios como un plan secuencial)

Introducido 2026-08-28 (caso base: Simple TV ALL-001). Es un **5to valor** de `servicio`,
para cuando el cliente pide explícitamente **un plan estratégico que combine Detección,
Habilidades, Políticas e Innovación como fases de una misma hoja de ruta** — no un combo
parcial de 2 servicios (eso se sigue registrando bajo el servicio de entrada, ej. `deteccion`
para un combo Detección+Habilidades, como DET-002).

1. **No resuelve las plantillas pendientes de Políticas ni Innovación** (siguen "sin piloto
   canónico propio" en la tabla de arriba). Un deck `integral` representa esas dos fases al
   **nivel de resumen de un roadmap** (una tarjeta de etapa + una tarjeta de resultado, igual
   que Detección/Habilidades), usando el contenido que el sistema ya tiene escrito para cada
   servicio (`empresa/tipos-de-documento.md §0`, `empresa/catalogo.md`) — no inventa
   estructura nueva para esos dos servicios ni construye su plantilla dedicada.
2. **Estructura de referencia**: clonar `clientes/propuestas/simple-tv-all001/` (ALL-001) —
   roadmap de 4 fases / N etapas numeradas de forma corrida, 1 sola hoja de cotización para
   la primera fase con el resto progresivas (mismo patrón de `aerocentro/`), Beneficios v3,
   cierre escalera.
3. **Nomenclatura de código**: no hereda el prefijo de ningún servicio individual (no es
   `DET-`, `CAI-`, etc.) — el usuario asigna un código propio para estos planes (ALL-001 fue
   el primero).
4. `clientes/INDEX.py` agrupará estas propuestas bajo `servicio: integral` una vez se
   implemente el agrupamiento por servicio (§4.20, todavía pendiente para los 5 valores).

### 4.2 Tipo de documento → plantilla

| Solicitud | Plantilla | Subtipo |
|---|---|---|
| charla | `plantillas/diseno-charla.md` | — |
| taller | `plantillas/diseno-taller-capacitacion.md` | Taller (con perfil de ingreso) |
| capacitación / in-company | `plantillas/diseno-taller-capacitacion.md` | Capacitación (sin perfil ingreso) |
| curso | `plantillas/diseno-curso-diplomado.md` | Curso (≥4 módulos, ≥5 temas) |
| diplomado | `plantillas/diseno-curso-diplomado.md` | Diplomado (≥8 módulos, ≥6 temas) |

En duda entre subtipos → preguntar antes de generar.

> **Habilidades:** esta tabla ya **no decide el formato del deck**: toda charla, taller, capacitación, curso o diplomado de Habilidades se entrega en la plantilla compacta (§4.21; recetas por categoría en `plantillas/habilidades-compacto.md` §1b). Las plantillas `diseno-*.md` quedan solo como guía para diseñar el programa y los entregables, y para los decks canónicos que ya existen.

### 4.3 Eje temático

`[Eje temático]` es parametrizable. No asumir IA por defecto. Cada propuesta inserta su área concreta.

### 4.4 Idioma — sin Spanglish

Todo texto producido por el sistema va en **español**. Excepción: términos nativos de herramientas (Artifacts, Code, Cowork, AcroForm, etc.) se mantienen como los usa la herramienta original.

**Prohibido «cohort/cohorts»** (anglicismo): para grupos de participantes se dice **«grupos»** («por grupos», «~25-30 por grupo», «número de grupos a confirmar»). El verificador (`verificar-propuesta.sh`) lo bloquea en HTML y `acroforms*.json`. Caso base: 2026-06-10 Laboratorios Farma.

### 4.5–4.7 PDF, AcroForms y plantilla canónica

> Ver `plantillas/generar-pdf.md` — formato A4 landscape, 13 campos editables, plantilla canónica `cumbre-andina/`.

### 4.8 Resaltado de palabras clave — negrita

Al redactar el contenido estático del deck, marca con `<strong>` las palabras clave
para que el equipo de ventas detecte el foco de un vistazo.

- **Qué:** nombres propios (herramientas, productos, plataformas), términos técnicos
  y metodologías del eje temático, y frases clave del documento (concepto o resultado
  central de la slide).
- **Cómo:** solo negrita (`<strong>`). Nunca fondo amarillo — reservado a títulos/cierre.
- **Dónde:** cuerpo de texto — `<p>`, `<li>`, descripciones. NO en títulos, eyebrows ni
  labels (ya pesan por CSS) ni en campos AcroForm editables (los rellena ventas).
- **Frecuencia:** solo la primera aparición de cada palabra/frase por slide.
- **Mesura:** ~2–3 resaltados por slide máximo. Resalta la palabra/frase, no la oración
  entera — si todo está en negrita, nada destaca.
- **Bloqueante — nunca en `.s-goals .general p`:** ese párrafo (Objetivo general) ya es
  `font-weight:700` por CSS. Un `<strong>` ahí es redundante *y* dispara un glitch de
  renderizado en Chrome headless (línea tipo tachado sobre el texto envuelto) — confirmado
  2026-08-28 en 4 decks del mismo linaje (aerocentro/ioed). Redacta ese párrafo sin `<strong>`.

> Detalle y ejemplos: `plantillas/propuesta-comercial.md` → *Reglas de copy*.

### 4.9 Datos de impacto — solo de estudios reales — bloqueante

La slide de Impacto (`.s-impact`, eyebrow `07 · Impacto`) respalda la propuesta con
cifras de impacto de la IA — o del eje temático — en empresas. **Ninguna cifra se inventa.**

1. Toda métrica sale de un **estudio real y verificable** (busca con WebSearch si hace falta).
2. La **fuente se cita verbatim** en la slide: estudio · institución · año.
3. Sin fuente sólida para una métrica, no la incluyas — nunca rellenes con estimaciones.
4. El contenido se adapta al **eje temático** de cada propuesta.

> Detalle: `plantillas/propuesta-comercial.md` → *Slide 9 · Impacto / estudios*.
>
> **No aplica a la plantilla compacta de Habilidades (§4.21):** no lleva slide de Impacto, y su slide de retorno **no cita estudios ni la web** (decisión 2026-10-05); usa método o cifras del propio cliente.

### 4.10 Sin overflow visual — bloqueante

El deck se imprime a tamaño fijo (A4 landscape, 842×595 pt). Cualquier contenido que se
salga de la slide, se recorte por `overflow: hidden`, o se trunque con `text-overflow:
ellipsis` es un **defecto bloqueante** — no se entrega.

> **Automatizado (ya no se revisa a ojo):** `node scripts/verificar-overflow.js <slug>`
> (integrado en `verificar-propuesta.sh`) renderiza el deck y reporta qué slide y qué caja
> desborda. Capacidades legibles por caja en `plantillas/capacidad-cajas.md` — úsalas para
> **acotar las preguntas de contenido** y prevenir el desborde en la fuente. Ante un
> desborde, ajusta el **contenido** (resume o reparte), no el diseño.

1. **Antes de declarar un PDF entregable, abre y revisa visualmente cada slide.** No basta
   con que el script termine sin error.
2. **Síntomas de overflow a buscar:**
   - Cards de Programa que muestran solo 2 de 5 temas → contenido recortado por la altura
     fija de la card (`overflow: hidden`).
   - Chips/tags con `...` al final → `text-overflow: ellipsis` truncando texto que no cabe
     en una línea con `white-space: nowrap`.
   - Texto de un `<p>` o `<li>` cortado a media palabra en la parte inferior de un bloque.
   - Footer, contador o logo solapado con contenido del cuerpo.
   - **Listas o cuadrículas con items de longitud muy distinta** → las filas se
     desalinean visualmente (ej. en el Diagnóstico de la slide 02, un punto de 8
     líneas junto a otros de 3–4 rompe el grid: la fila de abajo arranca
     desfasada). Mantener todos los items en un rango parecido de líneas.
3. **Si hay overflow, NO entregar — primero arreglar:**
   - Acortar copy (chips ≤ ~28 caracteres en cards de Programa de 5-6 módulos).
   - Aplicar modo compacto del CSS (`:has(> .module:nth-child(N))` ya soportado).
   - Reducir font-size / padding / gap del bloque afectado.
   - Reducir cantidad de items si la información se puede sintetizar sin perder valor.
4. **Cards de Programa con 5-6 módulos** ya tienen modo compacto en `styles.css` — no
   reintroducir tamaños grandes para 5+ módulos.
5. **Truncado con «…» (text-overflow: ellipsis) = el peor desborde — bloqueante propio.**
   El «…» *parece intencional* y pasa la revisión a ojo, pero oculta texto perdido y el
   directivo lo rechaza. Reglas:
   - **Prohibido reintroducir `white-space: nowrap` + `text-overflow: ellipsis`** en
     cualquier caja de texto del deck (chips, títulos, celdas). El CSS de chips de Programa
     ya envuelve (`white-space: normal`): un tema que no cabe desborda visible y el detector
     lo caza.
   - **El detector tiene chequeo dedicado de ellipsis con tolerancia ~0**: no se entrega
     con un solo «…» en el deck.
   - **La cura es el contenido, nunca el «…»**: si un tema/chip no cabe, **acórtalo** (chip
     ≤ ~28 chars) o repártelo en dos temas.

> Casos base: 2026-05-19 TA-023 (chips largos rompían la card) · 2026-06-03 BDV (entrega
> con «…» rechazada por dirección). Detalle: `aprendizajes-historico.md`.

### 4.10a Sin Metodología ni Equipo facilitador expuestos al cliente — bloqueante

Decisión 2026-08-26: la metodología de Intezia (Aprendizaje Basado en Retos) **no se
muestra al cliente** en el deck. Ventas ya la cubre en la sesión de Levantamiento de
Información, y la slide tenía un enfoque demasiado educativo/académico para una propuesta
de negocio.

1. **Slide de Metodología ABR (`.s-orange`, eyebrow "Metodología")**: no se incluye en
   ninguna propuesta nueva, de ningún servicio. El enfoque ABR se sigue documentando en
   `programa.md` (documento interno, §2.2 y §3 de `empresa/tipos-de-documento.md`), solo
   deja de ser una slide del deck visual.
2. **Bloque "Equipo facilitador" en Beneficios (`.team` dentro de `.s-benefits`)**: se
   retira también. La slide de Beneficios queda con Perfil de egreso, Beneficio del
   programa, Entregables y Acreditación (o su versión recortada por servicio, ver
   `plantillas/propuesta-comercial.md` → *Beneficios por servicio*).
3. **No retroactivo**: las propuestas ya entregadas (canónicos incluidos: `cumbre-andina/`,
   `pilotes-perforados/`, `aerocentro/`, `ioed/`, `pago-tronic/` y el resto) **no se tocan**.
   El cambio aplica a partir de propuestas nuevas o regeneradas a partir de esta fecha. Los
   canónicos existentes se actualizan más adelante cuando se formalicen los pilotos por
   servicio (§4.1a) — mientras tanto, al clonar cualquiera de ellos, retira estos dos
   bloques manualmente en el clon.

> Caso base: 2026-08-26 Go Pharma CAP-030 (primera aplicación).

**Actualización 2026-08-27 (Beneficios v2 + correo de cierre)** — dos ajustes más, ya
estándar en toda propuesta nueva:

4. **Beneficios — formato único v2**: el bloque "Perfil de egreso / Beneficio del programa /
   Entregables / Acreditación" (viejo, de cualquier servicio incluida Habilidades) se
   reemplaza por **Resultados · Por qué [Servicio] · Entregables · Valor inmediato**, con
   rediseño visual (slide oscura con tarjetas, no cuadros blancos). Detalle completo:
   `plantillas/propuesta-comercial.md` → *Beneficios — formato v2*.
5. **Correo de cierre**: `servicio@intezia.com` reemplaza `info@intezia.com` en el bloque
   "Empresa" de `.end-contact` (el correo de la asesora de ventas no cambia).

> Caso base de ambos: 2026-08-27 Cavedatos CAI-001.

### 4.11 No afirmar que el cliente migra de stack tecnológico — bloqueante

Intezia **se ajusta al stack del cliente, no lo cambia**. Ninguna propuesta puede afirmar
literalmente que una empresa migra, migrará o está migrando a otro stack, suite o
plataforma — da igual cuál sea (Google Workspace, Microsoft 365, Slack, etc.).

1. **Prohibido:** «la migración a [stack] está en curso», «el banco migrará a [suite]»,
   «cuando adopten [plataforma]» y cualquier variante que presente el cambio de stack del
   cliente como un hecho o un plan que nosotros afirmamos.
2. **Permitido:** referirse al **entorno que el cliente ya usa** y enmarcar nuestras
   herramientas como algo que **se integra** a ese entorno («el plan se apoya en el entorno
   Google del banco», «las herramientas operan dentro de su suite actual»).
3. El stack del cliente es **dato de contexto interno** (puede estar en `brief.md` para
   diseñar), nunca una afirmación de cara al cliente en el deck.

> Caso base: 2026-05-20 BDV CAP-024. Detalle: `plantillas/propuesta-comercial.md` → *Reglas de copy*.

### 4.12 Acrónimos y siglas — explicar en el primer uso — bloqueante

El equipo de ventas no puede vender lo que no entiende. Ningún acrónimo o sigla de jerga
(técnica, metodológica o interna de Intezia) puede aparecer en el deck sin estar explicado.
**No asumas que el lector sabe qué significa.**

1. **Expande en el primer uso:** la primera vez que aparece, escribe el término completo y
   la sigla entre paréntesis — «Política de Uso Aceptable (AUP)», «marco RCTF (Rol, Contexto,
   Tarea, Formato)». Después puedes usar la sigla sola.
2. **Por slide, no por deck:** cada slide se imprime y se lee aislada (§4.10). Define el
   acrónimo en **cada slide** donde aparece — al menos una vez, en el elemento con más espacio
   (un `<p>` o `<li>`, no un chip ni un segmento de barra).
3. **Si no cabe la expansión, no uses la sigla:** en chips o timebars sin espacio, escribe el
   término en lenguaje natural («Política de Uso Aceptable», «Prompting estructurado») en vez
   de la sigla cruda.
4. **Qué cuenta como jerga a explicar:** AUP, RCTF, GenAI y similares. **Excepciones** (no
   hace falta expandir): la sigla del propio cliente conocida por él (BDV, BCV), siglas de uso
   general en su sector (VPN, API en un módulo técnico) y los códigos internos de catálogo
   (CAI-, CAP- legacy, TA-, CU-…). En duda, expande.

> Caso base: 2026-05-20 BDV CAP-024. Detalle: `plantillas/propuesta-comercial.md` → *Reglas de copy*.

### 4.13 Sin guion largo como separador — bloqueante

El sistema **nunca** usa guion largo (`—`, em-dash) ni guion mediano (`–`, en-dash) como
separador en texto de cara al cliente. La redacción debe sonar humana y natural; el guion
largo es una marca de "voz de IA" que ventas detecta y rechaza.

1. **Prohibido** en todo output cara al cliente: `index.html` de cada deck, placeholders y
   tooltips de AcroForms (`scripts/agregar-campo-precio.py` y derivados), valores
   pre-llenados por `customize-<slug>.py`, copy de catálogo y briefs entregables.
2. **Reemplazo natural** según función gramatical del guion:
   - **Aposición o aclaración** → coma o paréntesis. ✓ «100 por mes, 600 al cierre» ·
     «Política de Uso Aceptable (AUP) firmable».
   - **Contraste o desarrollo** después de afirmación → dos puntos. ✓ «no es dar un
     taller por semana: es construir una arquitectura» · «el plan se construye sobre
     Gemini: vive dentro del entorno Google».
   - **Final de oración + idea relacionada** → punto + nueva oración. ✓ «sin método ni
     criterio común. Los resultados dependen de quién escriba el prompt».
   - **Separador de listas o metadatos** → middle dot `·` (ya convención de la marca).
3. **Excepción**: cuando una fuente verbatim (cita, título de estudio en `panel-source`)
   contiene `—` en el original, se respeta dentro de las comillas de la cita.

> Caso base: 2026-05-20 BDV CAP-024 (18 guiones largos reescritos). Detalle: `plantillas/propuesta-comercial.md` → *Reglas de copy*.

### 4.14 Leer antes de modificar — bloqueante

**Antes de modificar o regenerar cualquier propuesta** (HTML, CSS, PDF o scripts) se deben leer todos los archivos necesarios. Sin estas lecturas, no se toca nada.

**Lectura mínima obligatoria:**

1. `clientes/propuestas/<slug>/brief.md` — programa, módulos, códigos, audiencia.
2. `clientes/propuestas/<slug>/index.html` — estado actual exacto del deck.
3. `plantillas/diseno-{tipo}.md` — estructura curricular y §5.2 desglose instructivo.
4. `plantillas/propuesta-comercial.md` — reglas de copy y resumen de 13 campos AcroForm.
5. `plantillas/generar-pdf.md` — si hay cambios en AcroForms o generación de PDF.
6. `plantillas/estructura-canonica.md` — referencia estructural de los clones canónicos
   (slides, clases, AcroForms). Leer el `index.html` del clon canónico completo **solo**
   si queda una duda estructural que la referencia no resuelve.

**Decks compactos de Habilidades (§4.21):** la lectura mínima es `clientes/propuestas/<slug>/datos.json` (la fuente), `brief.md`, `programa.md` y `plantillas/habilidades-compacto.md`; el `index.html` es generado (no se edita). Los puntos 3, 4 y 6 de arriba no aplican (la estructura y las reglas de copy ya están en la spec compacta). Excepción: `dusa-cai035/` no tiene `datos.json` (se construyó a mano): leer su `index.html`.

**Campos AcroForm mínimos — bloqueante antes de entregar:**

| Campo | Contenido requerido |
|---|---|
| `Entregables` | 2–4 destacados del desglose instructivo + 3 institucionales (`ENTREGABLES_DEFAULT`) |
| `Acreditacion` | 3 líneas fijas con `[CÓDIGO]` sustituido por el código real del programa |
| `Paso01–03 Titulo` | Título corto del paso, sin placeholder entre corchetes |
| `Paso01–03 Body` | Descripción ≤ 130 chars. Más larga se corta en el PDF sin clic |
| Campos de precio | **Vacío intencional.** Ventas los llena en Adobe Reader |

Si el programa elimina la slide `s-price` (instrucción de no-precios del director), los 5 campos de precio no aplican. Los otros 8 campos siguen siendo obligatorios y deben pre-llenarse. (La plantilla compacta de Habilidades tiene 7 campos más uno por cuota del plan de pago: ver §4.21 punto 4.)

El `programa.md` debe existir en `clientes/propuestas/<slug>/` antes de construir el deck. La sección §5.2 del `programa.md` (desglose instructivo) es la fuente de verdad para derivar los `Entregables`.

> Caso base: 2026-05-21 Cashea CAP-005/CAP-006 (campos vacíos, sin `programa.md`). Detalle: `aprendizajes-historico.md`.

### 4.15 Sin acuerdos económicos en «Cómo arrancamos» — bloqueante

La slide de Próximos pasos (`.s-steps`, «Cómo arrancamos») describe la **logística** del
arranque, no la transacción comercial. El cierre económico es parte del proceso de venta y
**no se menciona en el deck**.

1. **Prohibido** en los tres pasos (título y body): «firmar acuerdo/contrato», «factura»,
   «anticipo», «50 %», «pago», «adelanto» y cualquier variante de compromiso económico.
2. **Permitido**: pasos de logística reales — confirmar fechas y zona horaria, coordinar
   acceso/participantes/agenda, reunión de arranque (kick-off), curaduría de casos.
3. El paso intermedio (Paso 02) por defecto cubre **acceso, participantes y agenda de
   sesiones** (título «Acceso y logística», ≤~20 chars), no la firma ni el anticipo.

> Caso base: 2026-05-25 BNC CAP-001/CAP-002 (paso 02 «Firmamos acuerdo»). Detalle: `aprendizajes-historico.md`.

### 4.16 Privacidad en Dashboards Edu-Trace — bloqueante

El `encuesta.csv` de Edu-Trace trae datos personales (nombre, **cédula**, correo). En el
Dashboard de Impacto (§11):

1. **Cédula**: se descarta en `scripts/edutrace-procesar.py` antes de serializar. **Nunca**
   aparece en `resultados.json` ni en ningún HTML/PDF de salida.
2. **Correo**: solo clave interna de deduplicación; jamás se imprime.
3. **Lista de participación**: nombre + departamento, **sin puntaje individual**.
4. **`encuesta.csv`** (PII cruda) va a `.gitignore` (`clientes/dashboards/*/encuesta.csv`). El
   `resultados.json` (ya sin PII) sí se versiona.

> Detalle: `plantillas/dashboard-edutrace.md §6`.

### 4.17 Honestidad de medición en Dashboards — bloqueante

La Encuesta Edu-Trace es **solo de cierre**: los Bloques B (impacto autopercibido) y D
(calidad) son **autopercepción**, y el «salto» (Competencia − Brecha) es **retrospectivo** (el
«antes» se pregunta al final). Solo el **Bloque C** (retención objetiva, % de aciertos) es una
**medición real**.

1. **Prohibido** afirmar mejora medida sobre datos autopercibidos/retrospectivos: «mejoró un
   X%», «la competencia subió a N» como si hubiera baseline.
2. **Permitido**: «competencia **percibida**», «salto **percibido**». Solo el Bloque C usa
   lenguaje de medición: «respondió bien el **97%**».
3. Usa los tags `.tag-medido` / `.tag-percibido` para que el lector distinga de un vistazo.
4. Muestra pequeña: si un departamento tiene n=1, márcalo **referencial**, no lo rankees.

> Hermana de §4.9. Detalle: `plantillas/dashboard-edutrace.md §4`.

### 4.18 Clave del Bloque C con confirmación — bloqueante

Las 3 preguntas técnicas del Bloque C cambian en cada capacitación y **no tienen hoja de
respuestas formal**. El consultor las define conociendo la respuesta.

1. Al procesar, **deduce la respuesta correcta por razonamiento** desde el contenido y el
   enunciado, y tradúcela en `keywords_correctas` dentro de `mapeo.json`.
2. **Si una pregunta queda ambigua, pregunta al usuario antes de calificar.** No inventes un %.
3. No infieras «correcto» por la respuesta más repetida (un error colectivo se marcaría como
   acierto).

> Detalle: `plantillas/dashboard-edutrace.md §2`.

### 4.19 Registro de entrega (`meta.json`) — fuente fechada determinista

Cada carpeta de propuesta lleva un `meta.json` que registra **qué se entregó y cuándo**.
Es la única fuente exacta para responder «qué propuestas se entregaron en tal semana» (no
inferir por fechas de archivo ni por git).

1. **Toda propuesta nueva nace con su `meta.json`** junto al `brief.md`, con este esquema:
   ```json
   {
     "codigo": "CAP-055",
     "cliente": "Corporación Bel",
     "tipo": "Capacitación In-Company · 3 mód / 6h",
     "eje": "Liderazgo Aumentado con IA, multi-herramienta",
     "servicio": "habilidades",
     "alianza": false,
     "estado": "Borrador",
     "fecha_entrega": null
   }
   ```
   `servicio` (§4.1a): `deteccion | habilidades | politicas | innovacion`. `alianza`:
   booleano aparte, no reemplaza a `servicio`. **Propuestas anteriores a 2026-08-26 no
   llevan estos dos campos** — quedan "sin servicio / legacy" en `clientes/INDEX.md`, sin
   backfill retroactivo (mismo criterio que ya aplica a las ~46 propuestas sin `meta.json`,
   §4.19 final).
   Estados válidos: **Borrador → Enviada → Aprobada / Perdida**, con **En corrección** como
   desvío lateral. Nace en `Borrador` con `fecha_entrega: null`. (Sin código —p.ej. express—
   `codigo: ""`.) **Flujo real:** terminado = enviado (el usuario envía al cliente en cuanto
   la propuesta queda lista; no hay limbo «generada pero sin enviar», por eso no existe estado
   «Entregada» de reposo). El único hueco lo abre una corrección: el usuario marca
   `En corrección` cuando la propuesta vuelve a revisión, y al regenerar (cerrada) regresa a
   `Enviada`. («Entregada» queda solo como valor legacy tolerado ≈ `Enviada`.)
2. **La fecha y el avance Borrador→Enviada los gestiona `generar-pdf.sh`** automáticamente
   (llama a `scripts/estampar-entrega.py`): al generar el PDF estampa `fecha_entrega` (= fecha
   de envío) si está vacía y sube `Borrador` —o `En corrección`— a `Enviada`. No hay que
   actualizarlo a mano. Acto seguido `generar-pdf.sh` corre `scripts/indexar.py` y regenera la
   columna vertebral relacional `clientes/INDEX.{json,md}` (§4.20).
3. **El resultado de venta no se sobrescribe** (append-only): `Aprobada`, `Perdida` y una
   `fecha_entrega` ya puesta se respetan; el hook nunca los pisa. `Aprobada/Perdida` se editan
   a mano cuando avanza la venta; `En corrección` lo pone el usuario cuando una propuesta vuelve.
4. **Sin `meta.json`, `generar-pdf.sh` imprime una advertencia visible** (no falla en silencio):
   créalo para que la entrega quede registrada.
5. **Al clonar** (`cp -r`) el `meta.json` del origen viaja con la copia: **sobrescríbelo** con
   los datos del nuevo cliente y resetéalo a `estado: "Borrador"`, `fecha_entrega: null`.
6. **Consulta semanal:** lee `clientes/INDEX.md` (vista relacional ya construida, §4.20) o
   filtra `clientes/INDEX.json`; como respaldo crudo, `find clientes/propuestas -name meta.json`
   + filtrar por `fecha_entrega`.

> Las ~46 propuestas legacy (sin `meta.json`) quedan **listadas** en `clientes/INDEX.md` bajo
> «a oscuras / pendiente backfill»: visibles pero no registradas. No se backfillean salvo
> instrucción explícita.

### 4.20 Columna vertebral relacional (`clientes/INDEX.{json,md}`) — derivada, no se edita a mano

La base de conocimiento es **relacional**: `scripts/indexar.py` recorre los `meta.json`
(§4.19, fuente fechada) y los enlaza en un modelo **Propuestas ↔ Clientes ↔ Dashboards**.
Backend **en archivos, versionado en git** (sin nube).

1. **Salidas:** `clientes/INDEX.json` (legible por máquina, para scripts/consultas) +
   `clientes/INDEX.md` (vista del equipo: pipeline por estado/división/**servicio** §4.1a,
   cotizaciones en su ventana de 30 días §3, clientes recurrentes, propuestas en corrección,
   y las legacy a oscuras).
2. **Se regenera, no se edita:** corre solo en cada entrega (lo llama `generar-pdf.sh` tras
   estampar). A mano: `python3 scripts/indexar.py` (o `--check` para no escribir).
3. **No inventa:** la división sale de `brief.md` (respaldo: ruta del logo en `index.html`);
   sin señal, `?`. El **servicio** sale de `meta.json → servicio`; sin campo (propuestas
   anteriores a 2026-08-26), queda `sin servicio / legacy`, igual que las legacy sin
   `meta.json` — nunca se fuerza al grafo. **Pendiente**: `scripts/indexar.py` todavía no
   lee ni agrupa por `servicio` — el campo ya se declara en `meta.json` (§4.19) pero falta
   el cambio de código en el script para reflejarlo en `clientes/INDEX.{json,md}`.

### 4.21 Servicio de Habilidades — plantilla compacta por defecto — bloqueante

Decisión 2026-10-05 (caso base: DUSA CAI-035, tras las correcciones de dirección);
**versión 2.0 desde 2026-10-07** (reunión de DUSA del 2026-10-06 y feedback de Ventas,
`correcciones.pdf`). **Toda propuesta nueva del servicio de Habilidades se hace con la
plantilla compacta**: 9 slides (7 en Fundación), dirigida por un `datos.json`
(`"version": 2`) que alimenta un generador. **Es el único formato del servicio y aplica a
todas sus categorías y a cualquier cliente** (instrucción del usuario, 2026-10-07): no se
clona un deck canónico de ~13 slides y no se pregunta el formato. **Disparador:** cualquier
pedido de propuesta, cotización, charla, taller, capacitación, curso, diplomado o programa de
Habilidades (incluido el que llega como «ajusta la propuesta de X al formato nuevo»).

1. **Entrada (§4.1a):** división, servicio = `habilidades` y `alianza` confirmados con el
   usuario, como siempre. Sin ellos no se genera. Se pide además la **asesora comercial** que
   atiende al cliente (la ve en la última slide) y la Ficha Comercial (requerimiento y dolor).
2. **Formato y flujo:** el orden es el de las preguntas del cliente (Ventas, 2026-10-07):
   Portada · Alcance (qué y para qué) · Ruta · Cómo trabajamos · Entregables · Retorno ·
   **Inversión (antepenúltima)** · Facilidad de pago · Próximos pasos (Fundación omite
   inversión y pago). Spec completa, esquema de `datos.json`, límites, diagnóstico y migración
   desde la v1: `plantillas/habilidades-compacto.md`. Flujo: `datos.json` →
   `python3 scripts/generar-habilidades-compacto.py <slug>` →
   `node scripts/verificar-habilidades-compacto.js <slug>` →
   `bash scripts/pdf-habilidades-compacto.sh <slug>`. El `datos.json` es la fuente: se edita
   ahí y se regenera, nunca el `index.html` generado. Sin docx de insumo, se arma el
   `datos.json` con el usuario pidiéndole soluciones, horas y fases: **no se inventan**.
3. **Reglas propias (bloqueantes), además de las de marca y copy del sistema:**
   - **Nombre del proyecto = frase-objetivo estilo título de tesis** («Optimización de
     procesos y datos con inteligencia artificial en 10 áreas de DUSA»), no un titular de
     dolor. El eyebrow dice «Propuesta de proyecto · Servicio de Habilidades».
   - **Lenguaje del cliente** (lo verifica el generador): sin «proceso base», «Frente A»,
     «S1-S3», «carril», «8 de 15 h» ni «inversión por horas»; «valor» o «inversión», nunca
     «precio» ni «costo»; cada cifra dice de qué es; no repetir información entre slides.
   - **Retorno antes de la inversión y sin estudios ni web.** Método (`metodo`) o cifras del
     propio cliente (`cifras`, con tipo de dato por fila y origen documentado). Nunca se
     inventan volúmenes, tiempos, valor de la hora, escalas salariales ni dotación: sin datos
     del cliente, modo `metodo`.
   - **Casos de éxito ya logrados con el cliente** solo con fuente documentada; la
     **contratación evitada** se plantea como probabilidad, nunca como compromiso.
   - **Posiciones y nómina** solo con `aval_posiciones` registrado (quién del cliente,
     cuándo, por qué medio) y reconfirmado antes de enviar. Sin aval, capacidad y tiempo.
   - **Facilidad de pago**: cuotas ligadas a hitos de la ruta; los montos son campos
     editables y vacíos (los llena ventas; nunca se escriben en el repositorio).
   - Semanas, no fechas calendario. Las horas se calculan, no se escriben, y van en pequeño
     detrás de las soluciones. «Hacia la semana N» es aritmética que servicio confirma.
   - Sin Metodología ABR ni Equipo facilitador (§4.10a): «Cómo trabajamos» explica cómo se
     trabaja (pasos, límites, datos), no la pedagogía. Sin Cierre. Próximos pasos = logística
     y la asesora, sin términos económicos (§4.15).
4. **Qué cambia del resto del sistema:** 7 campos de AcroForm más uno por cuota del plan de
   pago (no 13; Fundación: 2) y no aplican `Paso01–03` ni la hoja de «Cómo arrancamos»;
   `Entregables` y `Acreditacion` son las dos cajas editables de la slide de entregables, no
   los institucionales del §4.14; sin slide de Impacto (§4.9), sin Calendario de inicio ni
   ROI de la hoja de cotización. Siguen vigentes §4.1, 4.4, 4.8, 4.10, 4.10a, 4.11, 4.12,
   4.13, 4.19 y el checklist §10.
5. **Sin guardia (2026-10-07):** una **charla, curso, diplomado o taller/capacitación cuyo
   contenido es un programa de módulos y sesiones** también va en la plantilla compacta, **sin
   preguntar**: el programa se reexpresa como entregables por módulo o bloque con las recetas de
   `plantillas/habilidades-compacto.md` §1b (vocabulario propio, `omitir`, `sin_hoja_cotizacion`…,
   con un ejemplo por categoría) y la adaptación se anota en `supuestos`. El deck canónico de
   ~13 slides solo se hace si el usuario lo pide **expresamente** y se anota en `brief.md`.
   Antes de armar el `datos.json` se hace la entrevista mínima de la spec §4a (una sola vez,
   todas las preguntas juntas).
6. **Decks anteriores:** los de Habilidades ya entregados (formato canónico o compacto
   v1.x) no se tocan ni se convierten por iniciativa propia (mismo criterio que §4.10a). Si el
   usuario pide **ajustar, corregir o rehacer** una propuesta de Habilidades previa (p. ej.
   «ajusta la CAI-034 al formato nuevo»), se rehace en la v2 **sin volver a preguntar el
   formato**: un deck compacto v1.x se migra (`plantillas/habilidades-compacto.md` §13) y se
   regenera con `--actualizar-css`; uno canónico se reexpresa desde su `programa.md`. Un cambio
   puntual de texto en un deck ya entregado puede hacerse sobre ese deck, avisando al usuario
   de que sigue en el formato anterior. `dusa-cai035/` se construyó a mano (sin `datos.json`)
   en 7 slides y no cumple todas las reglas de la v2: sus cambios se hacen sobre su
   `index.html`; `datos.ejemplo-dusa.json` reproduce la propuesta con la plantilla v2.
7. **Pruebas y control:** tras tocar el generador, correr la prueba de aceptación
   (`plantillas/habilidades-compacto.md` §12) con los cinco `datos.ejemplo-*.json` (dusa,
   fundacion, charla, curso y diplomado). `verificar-propuesta.sh` avisa (⚠) de toda propuesta con
   `servicio: habilidades` en `meta.json` que no use la plantilla compacta.
8. **Otros servicios:** el mismo generador sirve a Detección y a combos con claves
   opcionales (`servicio_rotulo`, `meta_servicio`, `vocabulario`, `seguimiento.tipo`,
   `sin_hoja_cotizacion`, `omitir`; ver la spec §5). El criterio de Ventas del 2026-10-07
   (orden por las preguntas del cliente, lenguaje del cliente, próximos pasos con la
   asesora) aplica a **toda** propuesta, pero hoy solo está implementado en esta plantilla:
   al tocar propuestas de otros servicios, aplicarlo donde se pueda y avisar al usuario.

> Caso base: 2026-10-04/05 DUSA CAI-035; v2.0: 2026-10-07. Detalle y trazabilidad de decisiones:
> `plantillas/habilidades-compacto.md` y `aprendizajes.md`.

---

## 5. Delegación — qué cargar según la tarea

| Tarea | Archivos a cargar | Skill / MCP |
|---|---|---|
| **Determinar servicio** (Detección/Habilidades/Políticas/Innovación) antes de cualquier propuesta nueva | `empresa/tipos-de-documento.md §0` | — |
| **Propuesta de Detección** | `empresa/tipos-de-documento.md §0` + `clientes/propuestas/pilotes-perforados/` (semilla) | — |
| **Propuesta de Políticas** | `empresa/tipos-de-documento.md §0` (formato pendiente — confirmar con el usuario antes de generar) | — |
| **Propuesta de Innovación** | Clonar `clientes/propuestas/zoom-innovacion/` (piloto INN-001) — mismo criterio de reutilización que cualquier otro servicio (§6 Paso 0) | — |
| **Propuesta de Habilidades** (cualquier categoría; formato por defecto desde 2026-10-05, §4.21) | `plantillas/habilidades-compacto.md` (spec + flujo) · `plantillas/habilidades-compacto-canonico/` (CSS, `datos.plantilla.json`, ejemplos) · insumo: docx de Productos y Servicios o informe de Detección. `empresa/tipos-de-documento.md §0` solo si hay duda de servicio. **No se clona un deck** | — |
| **Propuesta clon** (mismo servicio + mismo tipo ya existe en `clientes/propuestas/`) | ninguno — pero §4.14 lectura mínima sigue siendo obligatoria + §10 checklist antes de entregar | — |
| **Propuesta nueva** (tipo sin precedente o primer deck del sistema; **no** Habilidades, que usa la plantilla compacta) | `plantillas/propuesta-comercial.md` + `empresa/marca-visual.md` + `plantillas/diseno-{tipo}.md` + `empresa/politicas-comerciales.md` | `ckm-slides` |
| Slide con duda puntual o edge case | `plantillas/propuesta-comercial-ref.md` (sección puntual) | — |
| Diseño pedagógico (decks canónicos y `programa.md`) | `plantillas/diseno-{tipo}.md` + `empresa/tipos-de-documento.md` | — |
| Retorno esperado con cifras del cliente (hoja de captura xlsx) | `plantillas/habilidades-compacto.md` §4 paso 3b + `scripts/habilidades-retorno-xlsx.py` | — |
| Calendario | `plantillas/calendario.md` | MCP `claude_ai_Google_Calendar` |
| Generar / entender PDF y AcroForms | `plantillas/generar-pdf.md` | — |
| **Dashboard de Impacto Edu-Trace** (cliente cerrado, hay `encuesta.csv`) | `plantillas/dashboard-edutrace.md` + `plantillas/generar-dashboard.md` + `empresa/marca-visual.md` | — |
| **Brief de Kickoff** (propuesta aprobada, arranque del servicio) | `plantillas/brief-kickoff.md` + `empresa/marca-artefactos.md` (+ canónico `plantillas/kickoff-canonico/`) | — |
| Verificar desborde / acotar contenido | `plantillas/capacidad-cajas.md` (+ `scripts/verificar-overflow.js`) | — |
| Comparar / validar estructura de un deck | `plantillas/estructura-canonica.md` (no leer el clon completo) | — |
| Agregar slide a la medida / componer deck | `plantillas/slides/README.md` | — |
| Editar identidad / tono | `empresa/identidad.md` | — |
| Editar marca visual (decks de propuesta) | `empresa/marca-visual.md` | — |
| Editar marca de artefactos comerciales (Brief de Kickoff y familia) | `empresa/marca-artefactos.md` | — |
| Editar catálogo | `empresa/catalogo.md` | — |
| Editar políticas / precios | `empresa/politicas-comerciales.md` | — |
| Editar divisiones | `empresa/divisiones.md` | — |
| Estructura curricular | `empresa/tipos-de-documento.md` | — |

Regla de oro: carga el mínimo necesario. La mayoría de propuestas son clones — no cargar archivos de instrucciones si la estructura ya existe en un deck anterior del mismo tipo.

**Lecturas masivas → subagentes haiku.** Toda tarea de lectura/extracción a gran escala (auditar el repo, comparar varios decks, inventariar archivos, resumir documentos largos que no se van a editar) se delega a subagentes con modelo **haiku** que devuelven solo el hallazgo estructurado; el agente principal orquesta y conserva su contexto para editar. No delegar la lectura §4.14 de la propuesta que SÍ se va a modificar — esa se lee directo porque se edita sobre ella.

---

## 6. Flujo propuesta nueva

### Paso 0 — Reutilización (hacer siempre primero)

Antes de cargar cualquier archivo de instrucciones:

0. **Habilidades → no se clona** (§4.21): se usa la plantilla compacta (`plantillas/habilidades-compacto.md §4`). Lo que sigue aplica solo a los demás servicios.
1. Busca en `clientes/propuestas/` si ya existe un deck del **mismo servicio** (§4.1a — Detección, Habilidades, Políticas, Innovación) **y** del **mismo tipo de documento** (taller, capacitación, curso, diplomado) con la misma división. No clonar un deck de Habilidades cuando lo que hace falta es uno de Detección, aunque los dos sean nominalmente "capacitación in-company".
2. **Si existe** → clonar con `cp -r clientes/propuestas/<slug-origen>/ clientes/propuestas/<slug-nuevo>/` y editar con `Edit` solo las secciones que cambian (contenido de cada slide, código, cliente, módulos, impacto). **No cargar `propuesta-comercial.md` ni `marca-visual.md`** — la estructura ya es correcta.
3. **Si no existe** (primer deck de ese tipo) → continuar desde el paso 1 cargando los archivos indicados en §5.

> El deck de referencia para clonar (por tipo):
> - **Habilidades (servicio): no se clona.** Plantilla compacta dirigida por datos, `plantillas/habilidades-compacto.md` (§4.21). Lo que sigue es solo para los demás servicios (y para un deck canónico de Habilidades que el usuario pida expresamente).
> - Taller / Capacitación mono-fase → `cumbre-andina/`
> - Taller / Capacitación multi-fase **con roadmap de 3 etapas** (Diagnóstico → Construcción por Intezia → Implementación — default desde 2026-07-23, ver `plantillas/propuesta-comercial.md` → *Roadmap*) → `aerocentro/` (CAP-082, declarado estándar 2026-08-07: 3 fases / 5 etapas numeradas de forma corrida, 1 sola hoja de cotización para la Fase 1 con Fase 2-3 cotizadas de forma progresiva, roadmap en 3 páginas independientes). `pago-tronic/` queda como origen histórico del patrón de 3 etapas (2026-07-23), útil si el caso es más simple (una sola fase de diagnóstico+construcción+implementación, sin subdividir en 5 etapas).
> - Taller / Capacitación multi-fase con roadmap de 2 etapas (caso puntual sin fase de construcción propia) → `pilotes-perforados/`
> - Curso / Diplomado → el más reciente del mismo subtipo en `clientes/propuestas/`
>
> **Nunca clonar un deck legacy** (anterior al formato canónico: `styles.css` local copiado,
> cronograma en tabla vieja, sin `.ruta`/`.timebar`/`.ses-cols`). Esos decks entregados se
> conservan como están y **no se modifican ni se usan como origen** — clonar siempre desde
> los canónicos de arriba para no arrastrar diseños del pasado. Estructura esperada:
> `plantillas/estructura-canonica.md`.

> **Tras aprobar la propuesta**, el arranque del servicio se documenta con el **Brief de
> Kickoff** (archivo HTML local que se llena en vivo durante el kickoff — no un PDF de
> propuesta ni un Artifact publicado). Flujo completo en §12.

---

### Pasos 1–7 (solo cuando no hay clon disponible)

> Habilidades tiene su propio flujo (§4.21): `plantillas/habilidades-compacto.md §4`. Los pasos 1–3 (división, carpeta, brief con `servicio`/`alianza` y `meta.json`) aplican igual; del 4 en adelante lo hace el generador.

1. **División**: pregunta si no se infiere del contexto.
2. **Carpeta**: `clientes/propuestas/<slug>/` (todo plano, sin sub-subcarpetas).
3. **Brief**: `brief.md` — empresa, contacto, división, **servicio** (§4.1a), tipo, eje temático, audiencia, fechas, presupuesto, **`fecha_arranque_deseada`**, **`resultados_esperados`** (los últimos dos alimentan el Calendario de inicio y el ROI de la hoja de cotización, ver `plantillas/propuesta-comercial.md`). **Ficha Comercial Intezia**: de ahora en adelante (2026-09-23) es el flujo **esperado** para la mayoría de propuestas nuevas, no la excepción — cuando existe, es la fuente primaria de todos estos datos (servicio adquirido, honorarios aplicables, hallazgos del Levantamiento, qué resultados espera el cliente) y `brief.md` referencia explícitamente qué se tomó de la Ficha. Sin Ficha Comercial todavía (transición), se arma a partir de instrucción directa del usuario — para `fecha_arranque_deseada`/`resultados_esperados` puntualmente, **preguntar directo al usuario**; sin esa respuesta, se omiten el Calendario de inicio y el ROI en esa propuesta en vez de inventarlos. Crea también el `meta.json` (estado `Borrador`, `fecha_entrega: null`, `servicio`, `alianza`) — §4.19.
4. **Programa**: mapea tipo → plantilla (§4.2) → genera `programa.md`.
5. **Deck visual**: clona el deck de referencia del tipo → edita contenido estático → `./scripts/generar-pdf.sh <slug>`.
   - **CSS compartido**: los clones mono-fase de cumbre-andina ya enlazan `../_base/styles.css` (no se copia el CSS). Lo propio del deck va en un `overrides.css` local. Detalle: `plantillas/slides/README.md`.
   - **Contenido acotado**: pide el contenido dentro de los límites de `plantillas/capacidad-cajas.md` para prevenir desborde. Certifica con `node scripts/verificar-overflow.js <slug>`.
   - **Slide a la medida** (cliente especial): inserta un bloque de `plantillas/slides/` (+ su CSS en `overrides.css`) y renumera contadores.
   - **Slide de Impacto** (`.s-impact`): reescribe barras, gauge, chips, hook y fuente con datos de **estudios reales** del eje temático, citando la fuente verbatim (§4.9).
6. **Pre-llenado de campos editables** (declara los valores en `clientes/propuestas/<slug>/acroforms.json` y aplícalos tras generar el PDF con `python3 scripts/customize-acroforms.py <slug>`; los campos siguen editables. **No se clona un `customize-<slug>.py`** salvo caso especial — resize de `/Rect`, lógica condicional):
   - **Entregables**: deduce 2–4 entregables destacados del desglose instructivo de `programa.md` + los 3 institucionales.
   - **Acreditación**: sustituye `[CÓDIGO]` por el código del programa. Las otras dos líneas son fijas.
   - **Próximos pasos**: redacta los 3 pasos «Cómo arrancamos» listos-para-entregar — título corto + descripción (1–2 frases): 1) confirmar fechas y zona horaria · 2) coordinar acceso, participantes y agenda de sesiones · 3) reunión de arranque ~30 min para alinear casos reales. **Nunca** menciones acuerdo económico, contrato, factura ni anticipo en estos pasos (§4.15).
   Ver `plantillas/generar-pdf.md`.
7. **Calendario** (preguntar primero): MCP GCal → `calendario.md`.

Slug: minúsculas, sin tildes, espacios → guiones. Ej: "Banco del Pacífico" → `banco-del-pacifico`.

---

## 6.A Flujo de modificación (propuesta existente)

> Para ajustes a un deck ya existente. No para propuestas desde cero (ver §6).

> **Deck compacto de Habilidades (§4.21):** leer `datos.json` + `brief.md` (+ `programa.md`), editar **`datos.json`** (no el `index.html`), regenerar con `python3 scripts/generar-habilidades-compacto.py <slug>`, medir con `node scripts/verificar-habilidades-compacto.js <slug>` y generar el PDF con `bash scripts/pdf-habilidades-compacto.sh <slug>` (incluye el par de campos). Detalle en `plantillas/habilidades-compacto.md §4`. Excepción: `dusa-cai035/` (hecho a mano) se edita en su `index.html` y se regenera con `generar-pdf.sh` + `customize-acroforms.py` + `customize-dusa-cai035.py`.

1. **Leer primero (§4.14 — bloqueante):**
   - `clientes/propuestas/<slug>/brief.md`
   - `clientes/propuestas/<slug>/index.html` (estado actual exacto)
   - `clientes/propuestas/<slug>/programa.md` (si existe)
   - Si hay duda estructural: `plantillas/diseno-{tipo}.md`

2. **Editar solo lo necesario** — usar `Edit` con `old_string`/`new_string` precisos. No regenerar todo el HTML si el cambio es puntual.
   - **Agregar una slide o paso a la medida**: usa un bloque de `plantillas/slides/` (HTML + su `.css` en `overrides.css`) y renumera los contadores. Ver `plantillas/slides/README.md`.

3. **Antes de generar o entregar — correr el verificador:**
   ```bash
   ./scripts/verificar-propuesta.sh <slug>
   ```

4. **Si hay que regenerar el PDF — par obligatorio:**
   ```bash
   ./scripts/generar-pdf.sh <slug>
   python3 scripts/customize-acroforms.py <slug>   # SIEMPRE inmediatamente después
   # (propuestas con script propio: python3 scripts/customize-<slug>.py "<pdf>")
   ```
   `generar-pdf.sh` resetea todos los AcroForms. Sin el customize, los campos quedan vacíos en el PDF final.

5. **Revisar visualmente cada slide del PDF** antes de declarar el trabajo entregado (§4.10). El script terminando sin error no equivale a PDF correcto.

6. **Actualizar `brief.md`** si el cambio afecta el programa, módulos, fechas o audiencia.

---

## 7. Estructura del repositorio

```
.
├── CLAUDE.md                         ← router (este archivo)
├── empresa/                          ← identidad, divisiones, marca (propuesta + artefactos), catálogo, políticas
├── logos/
│   ├── fundacion/{BLANCO,NEGRO}.png
│   ├── educacion/{BLANCO,NEGRO}.png
│   └── intezia/{BLANCO,NEGRO}.png    ← genérico sin división, para artefactos comerciales (Brief de Kickoff)
├── plantillas/                       ← propuesta-comercial, calendario, diseños, generar-pdf, dashboard-edutrace, brief-kickoff, kickoff-canonico/, habilidades-compacto.md + habilidades-compacto-canonico/ (§4.21)
├── fuentes/formatos-oficiales/       ← PDFs oficiales (referencia inmutable)
├── scripts/                          ← generar-pdf.sh, agregar-campo-precio.py, edutrace-procesar.py, generar-dashboard.sh, generar-habilidades-compacto.py + verificar-habilidades-compacto.js + pdf-habilidades-compacto.sh + habilidades-importar-insumo.py + habilidades-retorno-xlsx.py (§4.21)
├── clientes/propuestas/<slug>/       ← brief.md, programa.md, index.html, overrides.css?, kickoff.html?, "<CÓDIGO> <Título>.pdf"; en Habilidades compacto además datos.json (fuente), retorno-captura.xlsx? (interna), _pdf-anteriores/
└── clientes/dashboards/<slug>/       ← encuesta.csv (gitignored), mapeo.json, resultados.json, index-cliente.html, overrides.css
```

---

## 8. Confirmaciones requeridas

- **Google Calendar**: confirmar fechas, horarios y calendario destino antes de crear eventos.
- **Archivos estructurales** (`empresa/`, `plantillas/`, `CLAUDE.md`): confirmar antes de modificar.
- **Propuesta sin división**: bloqueado hasta obtener respuesta.
- **`clientes/<slug>/`**: sin confirmación si el usuario inició la propuesta.

---

## 9. Auto-actualización del sistema

Este sistema es **vivo**: mejora con cada conversación.

**Dónde guardar cada tipo de aprendizaje:**

| Aprendizaje | Archivo destino |
|---|---|
| Identidad / tono | `empresa/identidad.md` |
| Marca / logos / colores | `empresa/marca-visual.md` |
| Catálogo / programas | `empresa/catalogo.md` |
| Políticas / tarifas | `empresa/politicas-comerciales.md` |
| Plantillas / flujos | `plantillas/*.md` correspondiente |
| PDF / AcroForms | `plantillas/generar-pdf.md` |
| Cliente específico | `clientes/<slug>/brief.md` |
| Preferencia del usuario | `aprendizajes.md` + memoria persistente |
| Mejora del router | este `CLAUDE.md` |

**Cómo:** proponer antes de escribir cambios en `empresa/`, `plantillas/` o `CLAUDE.md`. Registrar siempre en `aprendizajes.md` con fecha. Si aplica a futuras conversaciones → memoria persistente del tipo correspondiente.

**Changelog (`aprendizajes.md`) — registrar sin leer todo el archivo:**
- Para anotar un aprendizaje nuevo, **antepónlo arriba con `Edit`** (el `old_string` es solo el encabezado + primera entrada existente). No hace falta leer el archivo completo.
- `aprendizajes.md` = changelog **activo** (últimas ~2-3 semanas). `aprendizajes-historico.md` = entradas viejas ya codificadas en plantillas; **no se carga** salvo que se pida trazabilidad histórica explícita.
- Cuando el activo pase de ~20 entradas, mover las más viejas (>~3 semanas) al histórico — son referencia, no fuente de verdad operativa (esa vive en `CLAUDE.md`, plantillas y scripts).

**Regla de adaptabilidad:** si haces algo igual dos veces sin que esté escrito → escríbelo. La plantilla sirve al caso, no al revés.

---

## 10. Checklist pre-entrega — aplicar en TODO trabajo

**Aplica a propuestas nuevas, modificaciones y regeneraciones. Sin estos pasos, no se declara el trabajo entregado.**

### Paso 1 — Verificación automática (script)

```bash
./scripts/verificar-propuesta.sh <slug>
```

Detecta: §4.13 guión largo · comillas tipográficas en atributos HTML · placeholders `[CÓDIGO]` sin llenar · **§4.15 términos económicos en «Cómo arrancamos»** (en el HTML y en `acroforms*.json`) · ausencia de fuente de pre-llenado (`acroforms*.json` o `customize-<slug>.py`) · **§4.10 desborde visual** (corre `verificar-overflow.js` y reporta slide + caja que se sale, recorta o **trunca con «…»**).

**Deck compacto de Habilidades (§4.21):** `verificar-propuesta.sh` detecta el deck por `habilidades-compacto.css` y corre además `verificar-habilidades-compacto.js` (holguras exactas en Chrome). Antes: `generar-habilidades-compacto.py <slug>` sin ✗ y con **todos los ⚠ leídos uno por uno** (el aval de posiciones, «Hacia la semana N», el plan de pago y la asesora piden confirmación humana antes de enviar). El PDF sale de `pdf-habilidades-compacto.sh`, que ya hace el par PDF-customize.

### Paso 2 — Verificación manual (no automatizable)

| # | Regla | Qué verificar |
|---|---|---|
| 1 | §4.10 Logos / alineación | Overflow ya lo cubre el script; ojea logos solapados o filas desalineadas |
| 2 | §4.11 Sin migración/adopción | Ninguna slide afirma que el cliente migra de stack ni que ya adoptó la herramienta enseñada |
| 3 | §4.12 Acrónimos glosados | Todo acrónimo de jerga (AUP, RCTF, GenAI…) expandido en la primera aparición de CADA slide donde aparece |
| 4 | §4.14 AcroForms pre-llenados | `Entregables`, `Acreditacion`, `Paso01–03 Titulo` y `Paso01–03 Body` tienen contenido real, no placeholders vacíos |
| 5 | Par PDF-customize | Si se corrió `generar-pdf.sh`, se corrió `customize-acroforms.py <slug>` (o el `customize-<slug>.py` propio) inmediatamente después |
| 6 | §4.21 Compacto de Habilidades | Titular-objetivo y eyebrow «Propuesta de proyecto»; retorno sin estudios ni web; cifras y posiciones solo con datos y aval del cliente registrados; 7 campos más uno por cuota en el PDF (Fundación: 2) y revisión visual de cada página, incluido el texto horneado de las cajas de la slide 5 |

### Regla del par PDF-customize

```
generar-pdf.sh <slug>   →   customize-acroforms.py <slug>   (siempre juntos, en ese orden)
```

> Propuestas con script propio (`customize-<slug>.py`) lo conservan como segunda mitad del par.

`generar-pdf.sh` reinyecta los AcroForms vacíos. El `/V` (valor pre-llenado) lo escribe el customize. Si se omite el customize después de regenerar, el cliente recibe un PDF con todos los campos en blanco.

---

## 11. Flujo Dashboard de Impacto Edu-Trace (post-cierre)

> Segundo flujo del sistema, **paralelo** al de propuestas (§6). Se dispara cuando termina el
> proceso de un cliente: ya impartió la capacitación y los participantes respondieron la
> **Encuesta Edu-Trace** de cierre. Convierte ese feedback en un resultado medible que se
> **entrega** al cliente. **Salida única: un solo deck de cara al cliente.** No se emite deck
> interno (regla retirada 2026-06-10 por costo/eficiencia). Reglas: §4.16 (PII), §4.17 (honestidad
> de medición), §4.18 (clave Bloque C). Diseño: `plantillas/dashboard-edutrace.md`. Mecánica:
> `plantillas/generar-dashboard.md`.

**Disparador (v1):** el usuario sube `encuesta.csv` a `clientes/dashboards/<slug>/`. (v2: web.)

**Pasos:**

1. **Leer (bloqueante):** `clientes/dashboards/<slug>/encuesta.csv` (las preguntas reales) +
   `plantillas/dashboard-edutrace.md`. Si el cliente ya tiene propuesta, también
   `clientes/propuestas/<slug>/programa.md` (ayuda a deducir la clave del Bloque C).
2. **`mapeo.json`:** declara qué columna es de qué bloque + la **clave del Bloque C** como
   `keywords_correctas` (deducida por lógica; §4.18 — preguntar si hay ambigüedad).
3. **Procesar:** `python3 scripts/edutrace-procesar.py clientes/dashboards/<slug>/` →
   `resultados.json` (descarta cédula/correo, calcula el Índice 0-100 y sus 4 ejes).
4. **Construir el deck:** clona el piloto `apb-group/` (10 slides) → `index-cliente.html`
   (Bloque E como recomendaciones de expansión de valor). Copy honesto (§4.17), sin overflow (§4.10).
5. **Generar PDF:** `./scripts/generar-dashboard.sh <slug>` (sin AcroForms; no hay customize).
6. **Verificar:** `verificar-overflow.js` en el HTML del cliente · grep PII = 0 · revisión visual
   slide por slide del PDF.

> Piloto de referencia: `clientes/dashboards/apb-group/` (Tecnología · n8n/IA · N=11 · Índice
> 86/100). Clónalo para cada cliente nuevo.

---

## 12. Flujo Brief de Kickoff (hoja de ruta del servicio)

> Tercer flujo del sistema, **posterior a la venta**. Se dispara cuando la propuesta ya está
> **aprobada** y arranca el servicio: el brief se usa en vivo en el **kickoff** (primer
> encuentro del equipo de servicio con el cliente). Acompaña al deck de propuesta, no lo
> reemplaza. No confundir con el `brief.md` interno de la carpeta (ficha de trabajo del
> sistema). Origen: reunión con Keiber (CPO), 2026-08-26; formato definido con ejemplo de
> referencia por Ivana, 2026-08-30 (ver historial de rechazos en `plantillas/brief-kickoff.md
> §0` — no repetir versiones anteriores).
>
> **Formato: archivo HTML local autocontenido** (no PDF de propuesta, no Artifact publicado
> en claude.ai). Vive en `clientes/propuestas/<slug>/kickoff.html`, se abre directamente en
> el navegador. Mecánica: ruta completa de etapas (sin sección de objetivos) → sesiones con
> fecha/hora editables por etapa → botón "Agendar todo" genera un `.ics` para importar a
> `servicio@intezia.com` → botón "Generar PDF" arma un `#print-view` y usa `window.print()`.
> Toggle "Modo interno / Modo cliente" oculta las instrucciones del consultor antes de
> compartir pantalla. Paleta y tipografía propias, **distintas** de la oficial de propuesta:
> `empresa/marca-artefactos.md`. Spec completo: `plantillas/brief-kickoff.md`. Canónico:
> `plantillas/kickoff-canonico/kickoff.html` (servicio Habilidades, cliente demo "Gato").

**Bloqueante:** antes de generar, **pregunta al usuario si la propuesta está aprobada** (y,
si tenía varios caminos de cotización, cuál se aprobó). Sin confirmación, no generes el brief.

**Qué muestra (fijo, sin objetivos):** la ruta **completa** de etapas del servicio contratado
(Detección / Habilidades / Políticas / Innovación, tabla en `plantillas/brief-kickoff.md §5`),
cada una con nombre + una frase de qué implica. Las etapas sin sesión con el cliente se marcan
como automáticas, no con casillas vacías. Los entregables se muestran en línea de tiempo,
asociados a la etapa que los produce — nunca inventados, se toman del manual del consultor o
se preguntan al usuario.

**Único contenido editable:** fecha y hora de cada sesión real (`<input type="date"/"time">`
dentro de cada `.scard`). Nunca se re-pregunta contenido/herramientas/contexto del cliente (ya
vino del levantamiento de ventas) ni se mencionan acuerdos económicos (§4.15). Sin
persistencia entre sesiones — el `.ics` y el PDF son la forma de conservar lo acordado.

**Pasos:**

1. **Confirmar la aprobación** de la propuesta con el usuario (bloqueante), y el camino si
   la propuesta era multi-camino.
2. **Leer (§4.14):** `clientes/propuestas/<slug>/{index.html, programa.md, brief.md}` +
   `plantillas/brief-kickoff.md`.
3. **Clonar el canónico:** copia `plantillas/kickoff-canonico/kickoff.html` a
   `clientes/propuestas/<slug>/kickoff.html`. Ajusta la profundidad de los logos a
   `../../../logos/intezia/...` (3 niveles; el canónico usa `../../`, 2 niveles).
4. **Editar** cliente, servicio, eje temático, la ruta completa de etapas (tabla §5 del
   spec), las sesiones de cada etapa (título + descripción + casillas de fecha/hora
   **vacías**) y los entregables en línea de tiempo. No inventar fechas ni entregables.
5. **Revisar visualmente** en el navegador: sin overflow, el toggle "Modo cliente" oculta
   correctamente todo lo interno.
6. **Durante el kickoff real:** el consultor llena fecha/hora en vivo, usa "Agendar todo" y
   "Generar PDF" al cerrar.

> Detalle completo (mecánica técnica, tabla de las 4 rutas por servicio, checklist):
> `plantillas/brief-kickoff.md`.
