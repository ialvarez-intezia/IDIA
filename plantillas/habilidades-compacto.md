# Plantilla: Propuesta compacta de Habilidades (9 slides, dirigida por datos)

> **Estado: estándar del servicio de Habilidades** (`CLAUDE.md` §4.21). Toda propuesta nueva de Habilidades se hace con esta plantilla; las excepciones están en §1.
> **Versión 3.0 (2026-10-08)**: correcciones de Keiber Quintana (CPO) a la Detección de G-MAX que valen para todo el sistema: **ninguna propuesta lleva semanas, sesiones ni fechas** (el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque; la ruta va por fases nombradas e hitos por evento y la duración, en horas), la propuesta se arma desde la **transcripción de la reunión con el cliente** y la ficha (`CLAUDE.md` §4.23), y la **Detección tiene su propio formato** en el mismo generador (`"formato": "deteccion"`, `plantillas/deteccion-compacto.md`). Migración desde la v2: §13 y `scripts/migrar-datos-v3.py`.
> **v2.0 (2026-10-07)**: incorpora las correcciones de la reunión de Ventas sobre DUSA CAI-035 (2026-10-06) y el documento de feedback de Ventas de María Iribarren, CCO (`correcciones.pdf`, 2026-10-07), que aplica a todas las propuestas. Cambios de fondo respecto de la v1.x: otro orden de slides, dos slides nuevas («Cómo trabajamos» y «Facilidad de pago»), una última slide de próximos pasos con la asesora, el retorno obligatorio y antes de la inversión, y un lenguaje del cliente que se verifica de forma automática (§2, §6).
> **Servicio**: Habilidades (§4.1a) · **División**: Educación o Fundación · **Formato**: A4 horizontal, 9 slides (7 en Fundación o sin cotización).
> **Caso base**: DUSA CAI-035 (`datos.ejemplo-dusa.json` reproduce la propuesta con esta plantilla). El deck entregado `clientes/propuestas/dusa-cai035/` se hizo a mano en 7 slides y **no** cumple todas las reglas nuevas (§10).
> **Cómo se usa**: se llena un `datos.json` (`"version": 3`) y `scripts/generar-habilidades-compacto.py` produce el deck, los campos del PDF y el `programa.md`. Las cifras **se calculan**, no se escriben.
> **Alcance universal (2026-10-07):** es el **único formato** del servicio de Habilidades, para todas sus categorías (charla, taller, capacitación in-company, curso, diplomado) y para cualquier cliente, **sin preguntar el formato**. El deck canónico de ~13 slides solo se hace si el usuario lo pide expresamente.
> **Detección**: desde la v3 tiene su propio formato (`plantillas/deteccion-compacto.md`; caso base G-MAX DET-024). **Combos y categorías sin cotización**: claves opcionales (§5, «Claves opcionales»; precedentes CAI-032, CH-015). Los decks de Detección v1 hechos con esta plantilla (Acua-e, Conserval, Clínica Santiago de León) no se tocan salvo que se pida rehacerlos.

---

## 1. Cuándo usarla (y cuándo no)

**Es el formato por defecto de toda propuesta del servicio de Habilidades** (decisión del 2026-10-05). Responde a las preguntas del cliente en su orden y se apoya en una **lista concreta de soluciones por área** (idealmente del informe de Detección del cliente). IDIA no debe elegir otro formato para Habilidades por iniciativa propia.

| Situación | Usar |
|---|---|
| Habilidades con N soluciones ya identificadas por área, varias áreas, con horas por solución | **Esta plantilla**, directo (importador del insumo, §4) |
| Habilidades sin insumo todavía (solo se sabe el objetivo y las áreas) | **Esta plantilla**: armar `datos.json` con el usuario, pidiéndole las soluciones, horas y fases. No se inventan soluciones, horas, valores ni casos de éxito |
| Capacitación o taller in-company (`CAI-`, `TA-`) cuyo contenido son **soluciones/entregables por área** | **Esta plantilla** |
| Charla, curso, diplomado, o taller/capacitación cuyo contenido es un **programa de módulos y sesiones** sin lista de soluciones | **Esta plantilla, sin preguntar** (2026-10-07). El programa se reexpresa como entregables por módulo o bloque con las recetas del §1b y la adaptación se anota en `supuestos`. El deck canónico de ~13 slides solo si el usuario lo pide expresamente |
| Detección (cualquier cliente) | **`plantillas/deteccion-compacto.md`**: mismo generador con `"formato": "deteccion"` (sin conteos de entregables, horas por área ni prioridades). Combo Detección + Habilidades cotizado junto: esta plantilla con `servicio_rotulo` y las claves opcionales de §5 |
| Plan integral de 4 servicios, Políticas, Innovación | Los canónicos de cada servicio (§4.1a/§4.1b): esta plantilla no los cubre |
| Cotización por fases o por permanencia | No soportada (solo la hoja de inversión del proyecto, marcador «Propuesta Económica», más la facilidad de pago en cuotas) |
| Más de 3 líneas de trabajo, más de 2 herramientas o más de 13 filas de área | Fuera de límites (§9): diseñar a mano o dividir en dos propuestas |

El deck **no** lleva: Impacto con estudios, Cierre, Metodología ABR ni Equipo facilitador (§4.10a). La slide «Cómo trabajamos» explica cómo se trabaja sin exponer la pedagogía. Las slides de método, retorno y próximos pasos se pueden quitar con `omitir` (charla, encuentro único), pero el criterio de Ventas es que van en toda propuesta y el generador lo avisa.

### 1b. Recetas por categoría (cómo reexpresar cualquier servicio de Habilidades)

Regla común: cada módulo, encuentro o bloque se vuelve una **unidad con nombre de entregable** (qué se lleva el cliente), con **horas enteras** y una fase. Las palabras del deck se ajustan con `vocabulario` (módulo, bloque, parte, Cerebro Digital…). Lo que el insumo no diga va en `supuestos` y los reparos en `pendientes`; nunca se inventan horas, valores ni hechos del cliente. La propuesta **no muestra semanas ni sesiones** (§6 «Ruta»): si el insumo las trae, quedan en `supuestos` como referencia interna para el kickoff. Sin Ficha ni informe propio, los datos de la portada son **de contenido** (qué, cómo, primer paso), no hechos del cliente.

| Categoría | Cómo se reexpresa | Claves típicas del `datos.json` | Precedente |
|---|---|---|---|
| **Soluciones por área** (`CAI-`, `TA-`) | Directo: áreas, soluciones, C/T/A, fases | Sin claves especiales | DUSA CAI-035 |
| **Capacitación por etapas** (p. ej. Fundamentals, Construcción, Implementación) | Una línea de trabajo; cada etapa es un **módulo** (área) y cada entrega, un **entregable**; fases = las etapas, con títulos cortos; el kick-off va aparte y no suma horas de trabajo | `vocabulario`: área «módulo», solución «entregable»; 1 carril | CAI-037 (N58 TI), CAI-038, CAI-034 |
| **Cerebros Digitales y programas por persona** | Un área por cerebro (o por bloque); 2 entregables por área; la `composicion` dice qué incluye (sin número de sesiones) | `vocabulario.area` «Cerebro Digital» o «bloque»; `columnas_por_carril: [2]` si hay pocas áreas | CAI-039, CAI-041 |
| **Charla** (`CH-`) | 2 h = 2 partes de 1 h (horas enteras); sin datos del cliente si así se pide | `vocabulario.area` «parte»; `sin_hoja_cotizacion: true` y `seguimiento.tipo: "ninguno"` si no lleva cotización ni seguimiento; `omitir: ["retorno"]` (una charla no mide retorno) | CH-015, `datos.ejemplo-charla.json` |
| **Encuentro único de capacitación** | Un bloque por hora o por tema, con un entregable cada uno | `vocabulario.area` «bloque»; `sin_hoja_cotizacion`, `seguimiento.tipo: "ninguno"` y `retorno.metas` propios (qué queda definido al cerrar) | CAI-036 |
| **Curso** (`CU-`, ≥ 4 módulos) | Cada módulo es un área; cada tema relevante, un entregable con sus horas (agrupar si pasan de ~44 entregables) | `vocabulario.area` «módulo»; `metodo.pasos` y `retorno.pasos` propios; certificado solo si el curso lo acredita (entregable transversal) | `datos.ejemplo-curso.json` |
| **Diplomado** (`DIP-`, ≥ 8 módulos) | Igual que el curso; hasta 13 módulos como áreas, y si hay más, se agrupan en bloques | `alcance.compacto: true`, `entregables.compacto: true`, nombres de ≤ 36 caracteres; certificado como entregable transversal si acredita | `datos.ejemplo-diplomado.json` |

**Textos por defecto y otro vocabulario.** Los textos por defecto del deck están escritos para soluciones por área. Con otro `vocabulario` el generador ajusta el título de «Cómo trabajamos» y el subtítulo de entregables, pero en cursos, diplomados y charlas conviene sustituir también `metodo.pasos` (p. ej. aprendemos, practicamos, aplicamos, medimos), `metodo.subtitulo` y `retorno.pasos` (tareas de cada participante en lugar de procesos), como hacen los ejemplos.

Qué se conserva de la categoría: el **código** del catálogo (`CH-`, `TA-`, `CAI-`, `CU-`, `DIP-`), las horas y la modalidad. Qué cambia: el deck deja de ser un programa de módulos con cronograma por sesión y pasa a responder las preguntas del cliente (§2). El detalle curricular (módulos, temas, desglose instructivo) vive en `programa.md`; si hace falta diseñarlo, guiarse por `plantillas/diseno-{charla|taller-capacitacion|curso-diplomado}.md`.

## 2. Las 9 slides, en el orden de las preguntas del cliente

Criterio de Ventas (2026-10-07): la propuesta se ordena por lo que el cliente se pregunta, y **la inversión es la antepenúltima** para que llegue sabiendo qué recibe y qué retorno espera.

| # | Clase | El cliente se pregunta | Contenido |
|---|---|---|---|
| 1 | `.s-cover` | ¿Cuál es mi problema? | Titular-objetivo + lead + 3 datos de dolor real (+ fuente) + franja opcional de contratación evitada (como probabilidad, con fuente) |
| 2 | `.s-scope` | ¿Qué voy a hacer y para qué? | Un panel por herramienta; cada área dice **qué resuelve** (`para_que`) y cuántas soluciones tiene; qué queda fuera de alcance |
| 3 | `.s-route` | ¿Cómo? | Líneas de trabajo × fases nombradas, **sin semanas** (**soluciones en grande, horas en pequeño**), columna de garantía 30-60-90, 3 a 5 hitos por evento (una sola línea de tiempo), nota, y la ruta completa si existe |
| 4 | `.s-method` | ¿Cómo funciona en la práctica? | Los 4 pasos por solución (construimos, probamos, adoptamos, medimos) y por qué en ese orden; quién construye; casos ya logrados con el cliente (con fuente); cómo funciona en la práctica (límites incluidos); cómo se cuidan los datos; 4 datos de logística |
| 5 | `.s-deliv` | ¿Con qué me quedo? | Catálogo de **todos** los entregables (uno por solución) por área + 2 cajas editables: entregables transversales («Para todas las áreas») y valor inmediato |
| 6 | `.s-roi` | ¿Qué retorno espero? | Cómo se calcula el retorno (método) o cifras del cliente; calendario de garantía y cálculo del retorno; «Hacia dónde va el proyecto» (tono aspiracional); sin estudios ni web |
| 7 | `.s-price` | ¿Cuánto cuesta? | «Inversión del proyecto»: Duración (soluciones y fases; las horas, al final), Programa, hoja de cotización (campos vacíos para ventas), licenciamiento de terceros aparte, garantía, términos |
| 8 | `.s-pay` | ¿Cómo se paga? | **Facilidad de pago**: 2 a 6 cuotas ligadas a hitos de la ruta, con el monto de cada una como campo editable y vacío |
| 9 | `.s-next` | ¿Qué sigue y a quién escribo? | 3 pasos de logística, tarjeta de la asesora comercial y datos de Intezia |

Fundación y las propuestas «sin cotización» omiten las slides 7 y 8 (7 slides). Los títulos que el usuario dio como guía («¿Qué voy a hacer?»…) no son literales: los titulares son afirmativos («44 soluciones en 10 áreas de DUSA.», «Tres líneas de trabajo en paralelo, en tres fases.», «Inversión del proyecto.») y el eyebrow lleva el nombre de la sección. El **nombre del proyecto** (h1 de la portada) es una frase-objetivo estilo título de tesis.

### Lenguaje del cliente (se verifica solo)

El deck usa las palabras del cliente. El generador **bloquea** (✗) estas expresiones y avisa (⚠) de las dudosas:

| No decir | Decir |
|---|---|
| «proceso base» | «paso previo» (o la etiqueta propia en `alcance.etiqueta_proceso_base` / `vocabulario.proceso_base`) |
| «Frente A», «Frente B» | El nombre de la línea de trabajo: «Nómina, Servicio Médico y Contabilidad RRHH» (`frentes[].nombre`) |
| «S1-S3», «F1» | «fase 1», o el nombre del hito («Arranque», «Cierre») |
| Semanas, sesiones o fechas del cronograma («Semana 4», «11 semanas», «6 sesiones de 2 h») | Fases nombradas, hitos por evento y la duración en horas; el calendario se acuerda en el kickoff (§6 «Ruta»). Las tasas del cliente («12 h por semana») sí van |
| «carril» | La herramienta: «Claude Team», «Copilot» |
| «8 de 15 h» (sin contexto), columnas con un número sin explicar | Decir de qué es cada cifra («8 de las 15 horas del programa son…») |
| «Inversión por horas de sesión» | «Inversión del proyecto» (se cobra por proyecto) |
| «precio» (✗) y «costo» (⚠) | «valor» o «inversión». «Costo» solo para el costo interno del propio cliente (la hora de su equipo) |

Además: **no repetir información entre slides** (el generador compara los textos y avisa de frases de 9 o más palabras repetidas), menos texto y más jerarquía, y toda cifra con su fuente. Si un nombre de solución del cliente lleva «costo» o «precio» (p. ej. «tablas de precios»), se declara en `frases_ok`.

### Glosario (los términos de `datos.json`)

| Término | Qué es |
|---|---|
| **Carril** | Herramienta o plataforma sobre la que se construye (1 o 2; p. ej. Microsoft 365 Copilot, Claude Team). Define el color (amarillo/naranja) y el orden de los paneles. **Término interno**: el cliente ve la herramienta |
| **Área** | Función del cliente cuyos procesos se automatizan (Contabilidad, Nómina…). Pertenece a un carril y a una línea de trabajo. `para_que` dice qué resolvemos en ella |
| **Paso previo** (`proceso_base`) | Un proceso previo que condiciona a otros (p. ej. ordenar la base de datos de empleados). Cuenta sus soluciones y horas pero **no** cuenta como «área» en «N soluciones en K áreas» |
| **Solución / entregable** | Una unidad construida (asistente, validador, tablero, archivo…). Cada solución genera exactamente un entregable en la slide 5 |
| **Línea de trabajo** (`frentes[]`) | Equipo de trabajo que avanza en paralelo (1 a 3). Agrupa áreas del mismo carril, tiene un **nombre** que ve el cliente y sus horas (sin semanas). El id (A, B, C) es interno |
| **Fase (F1 a F3)** | Etapa de la ruta, en columna: F1 prioridad sin dependencias · F2 necesita un acuerdo, dato o solución previa · F3 extensiones y tableros (textos editables). Se **destaca** la que concentra más horas. Se nombra por lo que agrupa (`descripcion`), nunca por semanas |
| **F0** | Horas de arranque (al arrancar), sin columna. Si se declara una solución F0 cuenta en `{n_total}`, en las horas y en el catálogo. La línea base de horas ya es un entregable transversal por defecto |
| **Celda** | Cruce línea de trabajo × fase: nº de soluciones y horas se calculan; el texto lo escribe una persona (≤ ~90 caracteres) |
| **C / T / A** | Horas de construcción, pruebas y adopción por solución (el insumo dice «testeo»; en el deck, «pruebas») |
| **Hito** | Evento de la ruta (3 a 5): título = el evento («Arranque», «Primeros accesos», «Cierre») + texto ≤ ~90 caracteres, sin semanas ni fechas |
| **Garantía 30-60-90** | Seguimiento posterior al cierre de cada área (`empresa/tipos-de-documento.md §0.2`); en la ruta es la columna «Garantía». No es garantía de retorno: es de acompañamiento |
| **Titular-objetivo** | Frase nominal estilo título de tesis que responde al objetivo del servicio. Va en 1 a 3 líneas más una franja amarilla; sin punto final |
| **Línea base** | Medición, al arrancar, del tiempo que toma hoy cada proceso: el «antes» contra el que se mide el retorno |
| **Retorno esperado** | Slide 6. **No** es una garantía de retorno. El gancho se ata al seguimiento («a los 90 días del cierre de cada área»), sin semanas |
| **Facilidad de pago** | Plan de cuotas ligadas a hitos de la ruta (slide 8). Los porcentajes están en el deck; **los montos no** (campos editables vacíos) |

## 3. Archivos

```
plantillas/habilidades-compacto.md                       ← este documento
plantillas/habilidades-compacto-canonico/
    habilidades-compacto.css      CSS genérico v2 (se copia congelado a cada propuesta)
    datos.plantilla.json          esquema anotado con POR_DEFINIR
    datos.ejemplo-dusa.json       instancia real completa, 9 slides (prueba de aceptación: DUSA CAI-035 con la plantilla v2)
    datos.ejemplo-fundacion.json  ejemplo ficticio de Fundación, 7 slides (prueba de la variante sin inversión ni pago)
    datos.ejemplo-charla.json     ejemplo ficticio de charla de 2 h, 6 slides (sin cotización, seguimiento ni retorno)
    datos.ejemplo-curso.json      ejemplo ficticio de curso de 6 módulos y 24 h, 9 slides (método y retorno adaptados a un curso)
    datos.ejemplo-diplomado.json  ejemplo ficticio de diplomado de 10 módulos y 120 h, 9 slides (modo compacto, certificado transversal)
    datos.ejemplo-deteccion.json  Detección real (G-MAX DET-024), "formato": "deteccion", 9 slides (plantillas/deteccion-compacto.md)
    datos.plantilla-deteccion.json  esquema anotado de Detección con POR_DEFINIR (solo lo del cliente; el resto tiene valor por defecto)
    brief.plantilla.md            brief interno con placeholders
scripts/
    habilidades-importar-insumo.py   docx de insumo → borrador de datos.json (v2)
    habilidades-retorno-xlsx.py      crear: datos.json → retorno-captura.xlsx · leer: hoja completada → datos.json["retorno"] (requiere openpyxl)
    generar-habilidades-compacto.py  datos.json → index.html, acroforms.json, programa.md, meta.json, brief.md (Habilidades y Detección)
    migrar-datos-v3.py               datos.json v2 → v3: quita las semanas y lista lo que hay que reescribir a mano
    verificar-habilidades-compacto.js  mide holguras exactas en Chrome (colisiones, desbordes de tarjeta, pie, márgenes)
    customize-habilidades-compacto.py  ajusta las 2 cajas de la slide de entregables en el PDF (genérico)
    agregar-campo-precio.py          (compartido) agrega los campos del PDF; los de pago se ajustan a las cuotas que lea en la página
    pdf-habilidades-compacto.sh      flujo completo: generar → verificar → PDF → campos
clientes/propuestas/<slug>/
    datos.json                    ← LA FUENTE (lo único que se edita a mano)
    index.html, acroforms.json, programa.md   ← generados (no editar)
    habilidades-compacto.css      copia congelada de la plantilla
    overrides.css                 ajustes propios del deck (vacío por defecto; nunca se sobrescribe sin --forzar-overrides)
    meta.json, brief.md           se crean una vez; meta.json se actualiza sin tocar estado/fecha; brief.md refresca solo su bloque «auto»
    retorno-captura.xlsx          (opcional, INTERNA, no se entrega) hoja de captura de las cifras del retorno (§4 paso 3b)
    _pdf-anteriores/              PDF previos con sello de fecha y hora (los mueve el wrapper)
```

`verificar-propuesta.sh` detecta el deck por la presencia de `habilidades-compacto.css` y corre también el verificador de holguras. Si la carpeta tiene un PDF complementario (p. ej. un documento de soberanía de datos), sacarlo antes de correr el wrapper: mueve todos los PDF a `_pdf-anteriores/` y `customize-acroforms.py` exige uno solo.

## 4. Flujo para una propuesta nueva

**Pre-requisitos (bloqueantes, CLAUDE.md §4.1, §4.1a y §6 paso 3):** división confirmada (`educacion`/`fundacion`), servicio = `habilidades` y `alianza` (sí/no) confirmados con el usuario, código asignado (siguiente `CAI-###` libre; ver `clientes/INDEX.md`). Pedir también: **Ficha Comercial** (de ella sale el requerimiento y el dolor del cliente) y la **transcripción de la reunión con el cliente** (`CLAUDE.md` §4.23: si contradice a la ficha, manda la transcripción; el resumen o correo de la asesora no define la estructura), `fecha_arranque_deseada`, `resultados_esperados` y **la asesora comercial** que ve el cliente en la última slide. Sin división no se genera; sin asesora el deck queda con un pendiente que bloquea el envío.

1. **Carpeta y datos.** `clientes/propuestas/<slug>/`. Con docx de insumo:
   `python3 scripts/habilidades-importar-insumo.py <insumo.docx> --nombre "Cliente" --slug <slug> --codigo CAI-0NN --salida clientes/propuestas/<slug>/datos.json`
   Sin docx: copiar `datos.plantilla.json`.
2. **Completar `datos.json`** siguiendo §5 y §6. Pedir al usuario lo que falte; no inventar. Los `POR_DEFINIR` y las marcas `_revisar` bloquean la generación.
3. **Generar y validar:** `python3 scripts/generar-habilidades-compacto.py <slug>`. Los errores (✗) impiden escribir; los avisos (⚠) hay que leerlos uno por uno. Con `HAB_DEBUG=1` imprime las holguras estimadas de alcance, método y retorno.
3b. **Retorno con datos del cliente (opcional).** Sin datos del cliente: se deja el modo `metodo` (por defecto; en Fundación habla de capacidad liberada, no de dinero). Con datos: `python3 scripts/habilidades-retorno-xlsx.py crear <slug>` genera `retorno-captura.xlsx` (hoja **interna**, nunca va al cliente; trae una pestaña `_control` con el código y la huella de ids para que no se cargue en el `datos.json` equivocado). Las personas completan las celdas azules (tiempos, ejecuciones, **tipo de dato** de cada fila, valor de la hora, dotación) y `leer retorno-captura.xlsx --datos <slug> --origen "documento o sesión; fecha; quién del cliente lo validó" --nota "..." [--posiciones --aval "quién; fecha; medio"] [--quitar-destino]` escribe el bloque en modo `cifras`. Obligatorios: `--origen` y `--nota`; con `--posiciones`, también `--aval` y las horas productivas por posición. El lector es estricto (rechaza números ambiguos como «1.200», fórmulas sin valor guardado, valores lógicos, negativos), valida con el generador **antes de escribir** y deja un `.bak` con sello. **Nunca** completar la hoja por intuición.
4. **Medir holguras:** `node scripts/verificar-habilidades-compacto.js <slug>` y `node scripts/verificar-overflow.js <slug>`. Ante un ✗, **acortar contenido**, no el diseño (§4.10). Cómo leer los mensajes:

   | Mensaje del verificador | Qué hacer |
   |---|---|
   | portada: datos de dolor vs franja de contratación / fuente vs línea de código / titular vs lead | Acortar `portada.fuente`, `hechos[].texto`, `contratacion.texto`, el titular (máx. 3 líneas) o `lead` |
   | alcance: franja «Fuera de este alcance» vs pie / fila pisa la píldora | Acortar `alcance.subtitulo`, `para_que`, `fuera_alcance`, nombres de área; `alcance.compacto: true` |
   | ruta: línea de trabajo dentro de su tarjeta / nombre en 2 líneas | `frentes[].nombre` más corto (≈ 36 caracteres con 3 líneas de trabajo) o `carriles[].nombre_corto` |
   | ruta: rótulo y conteo de la fase en una línea | `fases[].titulo` más corto (≤ 6 caracteres con una sola línea de trabajo y 3 fases) |
   | ruta: nota / siguiente etapa / hitos vs pie | Acortar `ruta.nota`, la celda o los hitos; la fila admite 4 líneas |
   | método: logística vs pie / bloque vs bloque | Acortar `practica`, `datos`, los casos ya logrados o las 4 fichas de logística; bajar a 2 casos |
   | entregables: columna N vs franja (lista áreas y px) | Nombres a 1 línea (≤ 36 caracteres), `entregables.compacto`, `columnas_por_carril`, título/subtítulo más cortos |
   | entregables: ancho del subtítulo / marcador «Lo que se llevan» en una línea | Título demasiado largo: definir `entregables.titulo` (≤ 28) o `nombre_pie` corto |
   | retorno: bloque principal / franja de destino vs banda final | Acortar pasos, metas, destino o gancho; en modo cifras, menos filas o `etiqueta` más corta |
   | inversión: Duración vs Programa / licenciamiento vs pie | `inversion.duracion` ≤ 3 líneas; `licencias.tarjetas[].texto` ≤ ~250 |
   | pago: hito vs porcentaje / caja de monto dentro de su tarjeta | Acortar `pago.cuotas[].hito` (≈ 4 líneas) o usar menos cuotas |
   | próximos pasos: contacto vs pie | Acortar los 3 pasos |
   | texto dentro del margen derecho | Algún texto se sale de la slide: acortarlo |

5. **PDF:** `bash scripts/pdf-habilidades-compacto.sh <slug>` (regenera, verifica, genera el PDF y corre el par de campos). Requiere `pypdf` en el Python activo; si no está, el script explica cómo crear un entorno aparte. **Dentro de este paso** `generar-pdf.sh` estampa `fecha_entrega`, pasa `meta.json` a «Enviada» (convención: terminado = enviado) y reindexa `clientes/INDEX.*`; si el flujo falla después, el wrapper restaura `meta.json`. El nombre del PDF sale del titular de la portada: `<CÓDIGO> <titular>`, cortado a 90 caracteres.
6. **Revisión visual** de las páginas del PDF (§4.10 es bloqueante). Renderizar a PNG (p. ej. PyMuPDF) y mirar cada slide, incluido el texto horneado de los campos y la caja de monto de cada cuota.
7. **Antes de enviar**, confirmar con humanos: el aval de posiciones (si aplica), el plan de pago y la asesora. **Registro:** si aún no se envía, corregir a mano `estado`/`fecha_entrega`; añadir la entrada en `aprendizajes.md` si el caso enseñó algo.

Para **cambios posteriores**: se edita `datos.json` y se regenera (el `index.html` se sobrescribe). `meta.json` se actualiza respetando estado y fecha; `brief.md` solo refresca su bloque «auto» (`--forzar-brief` lo reescribe); `overrides.css` no se toca (`--forzar-overrides`). Para propagar un cambio de CSS de la plantilla: `--actualizar-css`.

### 4a. Entrevista mínima (se hace una sola vez, con todas las preguntas juntas)

Antes de armar el `datos.json`, pedir al usuario lo que no esté ya en el insumo o en la Ficha Comercial. Lo que no responda va a `supuestos` o `pendientes`, nunca se inventa.

1. **Cuenta:** división (Educación o Fundación), alianza (sí o no), cliente y nombre corto, código, **asesora comercial** (nombre, correo, cargo).
2. **Qué se vende:** categoría (charla, taller, capacitación, curso, diplomado o proyecto de soluciones), horas, personas o grupos, modalidad. El número de sesiones y su duración no van en la propuesta: se acuerdan en el kickoff.
3. **Contenido:** áreas o módulos y qué entrega cada uno (informe de Detección, docx de Productos y Servicios o Ficha). Sin insumo, pedir las soluciones, las horas y las fases.
4. **Herramientas y licencias:** 1 o 2 herramientas y quién contrata el licenciamiento (con el valor de lista y su fecha).
5. **Ruta:** fases (qué agrupa cada una), hitos por evento y cómo se fija el arranque. Sin semanas ni fechas.
6. **Cotización:** si lleva hoja de inversión, el plan de pago (cuotas, hitos y porcentajes), y si lleva seguimiento a 30, 60 y 90 días y garantía (si no, `sin_hoja_cotizacion`, `seguimiento.tipo` y `sin_garantia`).
7. **Retorno:** si hay datos del cliente (volúmenes, tiempos, valor de la hora). Sin datos, modo método. Posiciones y nómina solo si el cliente lo avaló (aval registrado).
8. **Portada y método:** los dolores reales del cliente con su fuente, los casos ya logrados con su fuente (si los hay), y los límites y datos sensibles (para «Cómo trabajamos»).
9. **Ficha Comercial y transcripción** de la reunión, `fecha_arranque_deseada` (para el kickoff, no para el deck) y `resultados_esperados`: sin ellos no se agrega ROI.

### Importador del insumo

`habilidades-importar-insumo.py` lee el docx estándar de Productos y Servicios por **párrafos y filas de tabla**.

| Formato esperado | Ejemplo |
|---|---|
| Encabezado de carril | `Carril Microsoft Copilot — 17 soluciones, 173 horas` |
| Encabezado de área | `Contabilidad y CxP — 35 h` (o `Proceso base — orden de la base de datos — 19 h`) |
| Tabla de soluciones | filas `ID · Solución y entregable · C · T · A · Total · Fase` (la fila F0 puede traer `—` en C/T/A) |
| Tabla de frentes | filas `Frente A · Claude` · alcance · horas |

| Extrae | No extrae (queda `POR_DEFINIR`) |
|---|---|
| carriles, áreas, paso previo, soluciones con C/T/A/fase/detalle, líneas de trabajo y su alcance (si el docx dice semanas o un tope de horas por semana, van a `supuestos`, nunca al deck) | cliente/división, portada, `para_que` de cada área, nombre de cada línea de trabajo, alcance, método, logística, rangos de fases, celdas de la ruta, hitos, entregables transversales, asesora |

Valida contra lo que declara el docx (horas por área, carril y línea de trabajo; total de cada fila; cobertura de filas) y avisa si algo no cuadra. La asignación de áreas es por coincidencia de nombre completo: si es ambigua queda `POR_DEFINIR` con aviso. Los nombres de entregable son una propuesta cortada del texto largo y quedan `_revisar`. No sobrescribe un `--salida` existente (`--forzar`).

## 5. Esquema de `datos.json`

Los textos de cara al cliente aceptan **tokens** `{token}` en minúsculas (el generador los reemplaza y falla si no existen o quedan sin resolver). Tokens: `{cliente} {cliente_corto} {codigo} {n_total} {n_total_txt} {n_entregables_txt} {n_areas} {n_areas_txt} {n_frentes_txt} {n_bases} {h_total} {n_fases} {n_fases_txt} {n_fases_palabra} {rango_seguimiento} {n_cuotas} {n_cuotas_palabra}`, por fase `{n_f0..n_f3} {h_f0..h_f3}`, por línea de trabajo `{n_frente_<id>} {h_frente_<id>}` (id en minúsculas), por carril `{n_carril_<id>} {h_carril_<id>}`. `{n_total_txt}`, `{n_entregables_txt}`, `{n_areas_txt}` y `{n_frentes_txt}` ya traen la concordancia («1 solución», «44 entregables», «10 áreas», «3 líneas de trabajo»); `{n_fases_txt}` da «tres fases». **Retirados en la v3** (error si se usan): `{semanas}`, `{semanas_txt}`, `{semana_medicion}`, `{tope_h_semana}`, `{tope_h_dia}`. Los tokens de Detección están en `plantillas/deteccion-compacto.md` §5.
**Negrita** `**x**`: se interpreta en `portada.lead`, `hechos[].texto`, `contratacion.texto`, `alcance.*`, `metodo.*`, `fases[].descripcion`, `frentes[].celdas`, `ruta.*`, `seguimiento.*`, `licencias.tarjetas[].texto`, `inversion.duracion`, `pago.*`, `retorno.*` y `entregables.subtitulo`; en nombres de entregable y en los campos del PDF se ignora (§4.8). Máx. ~3 resaltados por slide (el conteo de la ruta no incluye el número de soluciones de cada línea).

| Sección | Campos | Notas y límites |
|---|---|---|
| `cliente` | `nombre`, `slug`, `codigo`, `nombre_pie` (opc.) | `nombre_pie`: nombre corto para el pie y los **titulares por defecto** (`{cliente_corto}`); definirlo si `nombre` supera ~12 caracteres |
| raíz | `version` (= 3), `formato` (`habilidades` por defecto; `deteccion`: otra spec), `division`, `alianza` (bool, obligatorio), `eje`, `origen`, `fuente_insumo`, `siglas_ok`, `frases_ok`, `supuestos`, `pendientes` | `siglas_ok`: siglas del cliente que no requieren glosa (§4.12). `frases_ok`: nombres del cliente que llevan «costo» o «precio». Claves desconocidas se avisan con sugerencia |
| `portada` | `titulo_lineas[1-3]`, `titulo_destacado`, `lead`, `hechos[2-4]` (`num`, `texto`, **`resuelto_por`**), `fuente`, `contratacion` (opc.: `num`, `texto`, `fuente`), `eyebrow` (opc.) | **Titular-objetivo**: líneas + franja amarilla; largo total ≤ 82 caracteres con código de 7, sin punto final. El h1 baja solo de tamaño (64/54/46/42 px). `texto` del hecho ≤ ~95, `num` ≤ 9. `contratacion`: la contratación evitada es **probabilidad, nunca compromiso** (exige lenguaje como «alta probabilidad» o «podría», bloquea «garantiza», «se reducirán», «siempre»…), con fuente documentada |
| `carriles[1-2]` | `id` (minúsculas/números/_), `nombre`, `nombre_corto`, `color` (`amarillo`/`naranja`) | El orden manda en slides 2 y 5. `nombre_corto` ≤ ~22 caracteres |
| `areas[]` | `id`, `nombre`, **`para_que`**, `carril`, `frente`, `proceso_base`, `nombre_catalogo`, `composicion`, `soluciones[]` | `para_que` **obligatorio**: qué resolvemos y para qué, ≤ 78 caracteres con dos herramientas, ≤ 95 con una (máx. 150). Máx. 13 filas; >11 pide `alcance.compacto`. Ids únicos. `composicion`: texto pequeño bajo el nombre del área |
| `…soluciones[]` | `id`, `entregable`, `C`,`T`,`A` (o solo `h`), `fase`, `detalle` | Horas enteras ≥ 0, ≥ 1 en total. `entregable` ≤ 36 ideal (1 línea), ≤ 72 recomendado, ≤ 99 máx. |
| `alcance` | `subtitulo`, `fuera_alcance[]`, `compacto`, `titulo`, `etiqueta_fuera`, `etiqueta_proceso_base` | `subtitulo` 1 línea (~110). `fuera_alcance` máx. 5 puntos de ≤ ~130 caracteres, con el motivo. Los pasos y «quién construye» ya no van aquí (`metodo`) |
| `metodo` | `quien_construye` (opc.), **`practica[1-3]`** (`titulo`, `texto`), **`datos`**, `ejemplos[1-3]` (opc.), `etiqueta_ejemplos`, `nota_ejemplos`, `pasos[3-4]`, `por_que_orden`, `titulo`, `subtitulo` | `practica` y `datos` **obligatorios** (TI y los directivos lo preguntan). `ejemplos[]` = `area`, `titulo`, `texto`, **`fuente`** (documento y fecha del propio cliente, obligatoria) y, juntos, `antes`/`despues`. Pasos por defecto: construimos, probamos, adoptamos, medimos. `por_que_orden` por defecto se arma con las fases |
| `fases[]` | `id` (`F0`..`F3`), `titulo`, `descripcion`, `destacada` | 2-3 con columna + `F0` opcional. Sin semanas: la `descripcion` nombra la fase en su cabecera, en negrita (≤ ~55 caracteres). Título ≤ ~6 caracteres si hay una sola línea de trabajo y 3 fases |
| `frentes[1-3]` | `id`, `carril`, **`nombre`**, `celdas{F1,F2,F3}` | `nombre` ≤ 44 caracteres y máx. 2 líneas en la tarjeta. Cada celda ≤ ~90; horas y nº se calculan. Sin semanas (v3) |
| `ruta` | `hitos[3-5]`, `titulo`, `subtitulo`, `nota`, `siguiente_etapa{titulo,texto}` | Hito: `titulo` = el evento (≤ ~28), `texto` ≤ ~90, sin semanas. `nota` ≤ ~340. `siguiente_etapa`: la ruta completa o etapa 2, solo si existe y está documentada |
| `logistica` | **`modalidad`**, **`participantes`**, **`arranque`**, `ritmo` | Cuatro fichas al pie de «Cómo trabajamos» (≤ ~100 caracteres). `ritmo` por defecto: «Según la disponibilidad de cada área, sin frenar su operación diaria.» |
| `seguimiento` | `rango`, `texto`, `items[2-3]` (`dias`,`texto`), `etiqueta`, `tipo` | Marco 30-60-90. `tipo`: `seguimiento` (por defecto, columna «Garantía») · `cierre` (la última columna muestra el cierre) · `ninguno` (sin columna ni rango/items) |
| `entregables` | `transversales[]`, `valor_inmediato[]`, `compacto`, `columnas_por_carril`, `titulo`, `subtitulo`, `etiqueta_transversales`, `etiqueta_valor` | Viñetas ≤ ~60 caracteres (el generador mide con las métricas exactas del PDF si hay pypdf), ≤ 4 líneas por caja. `columnas_por_carril`: un valor ≥ 1 por carril, suma ≤ 4 |
| `retorno` | `modo` (`metodo`\|`cifras`), `posiciones` (bool), `aval_posiciones{quien,fecha,medio}`, `titulo`, `subtitulo`, `pasos[4-7]`, `metas[3]`, `destino[3]`, `gancho`, `costo_hora_usd`, `horas_por_posicion`, `areas[]`, `nota_datos`, `origen_datos{documento,fecha,validado_por}`, `etiqueta_pasos`, `etiqueta_metas`, `etiqueta_destino` | **Va por defecto** (modo método) y **antes de la inversión**; se quita con `omitir: ["retorno"]`. **`posiciones=true` exige `aval_posiciones`**. Modo `cifras` exige `costo_hora_usd` > 0, `nota_datos` (≥ 30 car.), `origen_datos` completo, `tipo_dato` por fila (`medido`\|`declarado`\|`estimacion`) y, con posiciones, `horas_por_posicion`. Sin textos que citen estudios, la web, `http`, `.com`. Con `seguimiento.tipo` ≠ `seguimiento` hay que definir `metas` propias. En Fundación los textos por defecto hablan de capacidad liberada, no de dinero |
| `inversion` | `licencias{titulo,tarjetas[≤2],nota}`, `notas[]`, `titulo`, `duracion`, `programa[]`, `garantia_texto`, `sin_garantia`, `partes[2-4]` (`rotulo`, `nombre`, `texto`), `etiqueta_partes`, `etiqueta_base` | Sin montos aquí. `notas` por defecto: la garantía 30-60-90 y los términos y condiciones (si no hay `sin_garantia`). `duracion` por defecto: «Proyecto de N soluciones en K fases, con seguimiento y garantía a… X horas de trabajo.» `programa` por defecto: soluciones primero y horas en pequeño, en la versión que quepa en las 6 líneas de la caja. Se ignora en Fundación |
| `pago` | `cuotas[2-6]` (`cuando`, `hito`, `pct`), `mensaje`, `facturacion`, `titulo`, `subtitulo` | Los `pct` suman 100. Sin `cuotas` se usa el plan estándar de `empresa/politicas-comerciales.md` (50 % al aprobar, 50 % al cierre) y se avisa. `cuando` ≤ 16 caracteres, un hito («Al aprobar», «Fase 1», «Cierre», «+30 días»; nunca «Semana 5»); `hito` ≈ 4 líneas. **Los montos no se escriben**: salen como campos `PagoCuota1..N`. Se ignora en Fundación |
| `proximos_pasos` | **`asesora{nombre, correo}`** (+ `cargo`, `telefono`), `pasos[3]`, `titulo`, `subtitulo` | La asesora comercial que atiende al cliente. Pasos por defecto: fecha de arranque, accesos y agenda, reunión de arranque. **Sin términos económicos** (`CLAUDE.md` §4.15) |

### Claves opcionales (otros servicios, y categorías sin cotización ni seguimiento)

Opcionales, sin efecto si no se usan. Origen: propuestas de Detección y charlas hechas con esta plantilla el 2026-10-06.

| Clave | Para qué |
|---|---|
| `formato` | `deteccion` cambia el esquema y las slides 2, 3 y 5 (`plantillas/deteccion-compacto.md`); por defecto `habilidades` |
| `servicio_rotulo` | Servicio que se nombra en la portada, la inversión y el brief (por defecto «Servicio de Habilidades»; combo: «Servicio de Detección y Habilidades») |
| `meta_servicio`, `meta_tipo` | `servicio` y `tipo` de `meta.json` (`habilidades` por defecto) y el texto del tipo de documento en el brief |
| `vocabulario` | `{solucion, area, proceso_base}`: `[singular, plural]` para cambiar las palabras del deck («entregable/entregables», «frente/frentes», «etapa previa/etapas previas») |
| `areas[].composicion` | Qué componen los departamentos o grupos de un frente, bajo el nombre del área |
| `seguimiento.tipo` | `cierre` o `ninguno` (ver arriba); con `cierre` o `ninguno` tampoco hay garantía |
| `inversion.sin_garantia` | Quita la garantía 30-60-90 de la inversión y de los textos por defecto |
| `sin_hoja_cotizacion: true` | Sin inversión ni facilidad de pago (igual que Fundación) |
| `inversion.partes` | «Valor por parte»: 2 a 4 tarjetas bajo las Notas, cada una con su caja de monto (`PrecioParte1..N`, vacías para ventas); la caja base pasa a «Suma de ambas partes» (o `etiqueta_base`) y se autocalcula como la suma. No convive con `licencias.tarjetas` (mismo espacio). Origen: CAI-040 Marcelo Restrepo (2026-10-08) |
| `omitir: [...]` | Quita slides de entre `metodo`, `retorno`, `proximos`, `inversion`, `pago` (se avisa: Ventas las pide en toda propuesta) |
| `por_fases: true` | Agrupa alcance, ruta y entregables por fase, para el combo «paso previo + entrenamiento compartido + proyectos finales». El alcance numera cada fase (`fases[].titulo` y `descripcion`) con sus áreas debajo y resalta la fase destacada; solo cuentan como soluciones las de las áreas que no son paso previo (`proceso_base`): una fase sin soluciones muestra sus horas, y con una sola línea de trabajo la cabecera de la ruta no repite el conteo; los entregables van en una columna por fase. Exige una sola herramienta y cada área en una sola fase en columna. Origen: CAI-032 Laboratorios Farma (Keiber, 2026-10-08: «se tiene que entender visualmente» que primero va la Detección, después el entrenamiento y al final los proyectos) |
| `metodo_antes_de_ruta: true` | «Cómo trabajamos» pasa a la tercera página, antes de la ruta (Keiber, CAI-032, 2026-10-08) |
| `areas[].soluciones[].incluye` | Hasta 4 puntos (≤ ~75 caracteres) con lo que incluye un entregable, en viñetas menores bajo su nombre (slide 5 y `programa.md`), sin conteo ni horas propias. Sirve para los temas de un entrenamiento o el detalle de un diagnóstico sin partir sus horas (CAI-032) |

## 6. Reglas de contenido

### Portada
- **El dolor es del alcance.** Cada dato de la portada debe estar **resuelto por soluciones de la propuesta** (`resuelto_por` obligatorio). Se mantienen los dolores reales del cliente (Ventas lo pidió expresamente).
- Datos de la **auditoría** del cliente con su fuente en `fuente`; no cifras de estudios ajenos. Sin Ficha o informe propio no se afirman hechos del cliente: se usan hechos de contenido y se dice en `supuestos`.
- **El nombre del proyecto es una frase-objetivo estilo título de tesis**, nominal, que dice qué se logra y dónde. El dolor va en los 3 datos, no en el titular. Eyebrow «Propuesta de proyecto · Servicio de Habilidades» (§4.1a punto 4); el lead usa verbos de proyecto y «identificó», no «midió», si no hay mediciones.
- **Contratación como probabilidad**: «alta probabilidad de no tener que contratar las ≈10 posiciones», nunca un compromiso ni un porcentaje sin base. La cifra exige fuente documentada.

### Alcance
- Una unidad = una solución; «N soluciones en K áreas» **excluye** el paso previo del conteo de áreas.
- **Cada área dice qué resolvemos y para qué** (`para_que`) con las palabras del cliente. Glosar qué son las soluciones en el subtítulo («asistentes de IA, validadores y tableros»).
- `fuera_alcance`: lo que el cliente asume con sus desarrollos («asume con sus propios desarrollos»), lo que requiere un aplicativo y restricciones de datos sensibles, siempre con el **motivo**.

### Ruta
- **Ni semanas, ni sesiones, ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, `CLAUDE.md` §12). La ruta va por fases nombradas e hitos por evento; la duración, en horas. El generador bloquea «semana» y «sesión» en las slides (no en las fuentes citadas; las tasas del cliente, como «12 h por semana», sí van). Una sola línea de tiempo en todo el deck. Las horas son una «proyección» y deben cuadrar a la vista: la nota explica las horas de arranque (F0).
- **Las soluciones son las protagonistas; las horas van en pequeño.** Cada línea de trabajo tiene nombre propio (nada de «Frente A»). Garantía y seguimiento a 30-60-90 desde el cierre de cada área.
- El 90 días no suena a ROI garantizado: «Retorno en tiempo ahorrado y habilidades instaladas».
- Hitos con dependencias del cliente: decir quién («Sistemas y Nómina acuerdan…»). Evitar anglicismos («inducción», «pruebas»).
- Si existe una etapa 2 o la ruta completa, va en `siguiente_etapa`; si no está documentada, no se inventa.

### Cómo trabajamos
- **Anticipar las preguntas**: cómo funciona en la práctica **con sus límites** (licencias, qué hace cada herramienta, ventanas de prueba, qué no hace) y cómo se cuidan los datos sensibles (casos reales, anonimización, accesos que autoriza el área de tecnología). Si no está escrito, el cliente asume que no funciona.
- **Casos ya logrados con el cliente** (los agentes que sus equipos construyeron en la Detección o el kickoff): solo con fuente documentada y las cifras tal como las dice el informe. Se verifica cada cifra contra la fuente antes de usarla (caso DUSA: «casi 2 semanas» era una demora actual, no un ahorro medido). Nunca se inventan casos de éxito.
- La explicación de la metodología es cómo se trabaja y por qué en ese orden; **no** se expone la pedagogía ABR (§4.10a).
- No afirmar migración de stack del cliente (§4.11): la herramienta nueva se suma, la que ya opera se extiende.

### Inversión y facilidad de pago
- Se llama **«Inversión del proyecto»** (cobramos por proyecto). Siempre «valor» o «inversión», nunca «precio»; para el licenciamiento de terceros, «valor de lista» con la fecha de cada fuente. No afirmar quién contrata el licenciamiento si la fuente no lo dice.
- Hoja estándar: `PrecioBase`, `Descuento`, `PrecioTotal` **vacíos** (los llena ventas), `Programa` y `Notas` pre-llenados. **Duración**: soluciones y fases primero; las horas, al final. Sin ROI estimado sin Ficha o resultados esperados explícitos.
- **Facilidad de pago** en hoja aparte: cuotas ligadas a hitos de la ruta, **montos vacíos y editables**. Ventas confirma el plan antes de enviar; sin plan propio se usa el estándar (50/50) con un aviso.

### Entregables
- **Un entregable por solución**, todos visibles, agrupados por área. El nombre dice qué se entrega y conserva el matiz del insumo («propuesta de notas de crédito», «pedido sugerido», «archivo para carga masiva», «trasladados a [herramienta]»).
- **Capacidad real del catálogo**: 1 línea ≈ 36 caracteres, 2 líneas ≈ 72, 3 líneas ≈ 108; caben ≈ 44 entregables de 2 líneas. Con pocas áreas el generador sube el tamaño de letra solo (`roomy`).
- Las dos cajas editables: **Para todas las áreas** (línea base, seguimiento) y **Valor inmediato** (hitos tempranos por fase o evento, sin semanas, respaldados por la fuente).
- El «Certificado de participación» no va por defecto: solo si el cliente lo pide.

### Retorno esperado
- **Sin estudios ni referencias de la web**: ni barras de literatura, ni «fuentes» externas, ni `http`, ni «según un informe de [Firma]», ni «garantizado». El generador falla si el texto los menciona. «Estudio de tiempos» es un método de medición y sí se admite.
- **Sin cifras propias sin datos.** Si las fichas dicen «No declarado», va el modo `metodo`. `cifras` solo con datos del cliente: tipo de dato por fila y origen (documento o sesión, fecha y quién del cliente validó); las estimaciones se rotulan.
- **Posiciones y nómina** solo con aval registrado (`aval_posiciones`) y reconfirmado antes de enviar. Nunca se escribe una cifra de nómina, escala salarial o dotación que el cliente no haya entregado.
- «Hacia dónde va el proyecto» con **tono aspiracional** y global (sin nombrar áreas concretas): mismo equipo con más volumen (condicional), trabajo reenfocado y ampliación a otras áreas, hacia una empresa inteligente.
- «Calendario de garantía y cálculo del retorno», no «metas».

### Próximos pasos
- Tres pasos de logística (fecha y zona horaria, accesos y agenda, reunión de arranque) y la **asesora comercial** a quien escribir. Sin acuerdos económicos (§4.15).

### Transversales a todo el deck
- Sin semanas, sesiones ni fechas en ninguna slide (§6 «Ruta»). Español neutro, sin voseo; sin guion largo ni mediano (§4.13); sin «cohort» (§4.4); acrónimos de jerga glosados en cada slide (§4.12). No exponer nombres de personas del cliente. Nada de lo que la fuente no diga: lo supuesto va en `supuestos`.

## 7. Campos AcroForm (PDF)

**7 + N campos** en Educación (N = cuotas; con `inversion.partes`, además `PrecioParte1..P`, y `PrecioBase` suma las partes): `PrecioBase`, `Descuento`, `PrecioTotal`, `Programa`, `Notas` (slide 7), `PagoCuota1..N` (slide 8) y `Entregables`, `Acreditacion` (slide 5, «Valor inmediato»; el nombre `Acreditacion` se conserva por compatibilidad con `agregar-campo-precio.py`). Fundación y «sin cotización»: solo los 2 de la slide 5. No hay `Paso01–03` ni hoja de pasos.

- `agregar-campo-precio.py` ubica cada grupo por **texto de página**: «Propuesta Económica» (solo la inversión), «Facilidad de pago» (solo el pago, en su título; la cantidad de campos sale de los «Cuota 1…N» de la página) y «Lo que se llevan» + «Entregables» (solo la de entregables). El generador falla si la frase aparece en otra slide o si falta. No usar «Cómo arrancamos», «Inversión por fases» ni «Inversión por Permanencia».
- La geometría de las cajas de monto la fija `geometria_pago(n)` en el generador y la reproduce `plan_pago_fields()` en `agregar-campo-precio.py` (tarjetas de 1011 px con 14 px de separación; la caja va 16 px adentro de cada tarjeta). Si se cambia una, cambiar la otra.
- Los de la slide de entregables se reubican en `customize-habilidades-compacto.py` (px × 0.75 → pt): `.db-box-1` (60, 49.75, 397.125, 100.75) y `.db-box-2` (445.125, 49.75, 782.25, 100.75), fondo oscuro y texto blanco horneados (10,5 pt, negrita; ≤ 4 líneas).
- Caracteres: solo Latin-1/WinAnsi (sin ≥, →, ✓, emoji). Orden obligatorio: `generar-pdf.sh` → `customize-acroforms.py` → `customize-habilidades-compacto.py` (el wrapper lo hace); `generar-pdf.sh` resetea todos los campos.

### Diagnóstico del PDF

| Síntoma | Causa probable | Acción |
|---|---|---|
| Campos vacíos o con el texto de ejemplo del sistema | Se corrió `generar-pdf.sh` sin `customize-acroforms.py`, o falta la clave en `acroforms.json` | Correr el par completo con el wrapper |
| Faltan los campos de la slide de entregables | «Lo que se llevan» o «Entregables» se partió en dos líneas o falta | `verificar-habilidades-compacto.js` lo marca; definir `entregables.titulo` corto / `nombre_pie` |
| Faltan los campos de pago o hay menos que cuotas | «Facilidad de pago» fuera del título, o «Cuota N» no se extrae de la página | Revisar `pago.titulo` y que cada tarjeta diga «Cuota N» |
| Campos con texto cortado | Más de 4 líneas o viñetas largas | Acortar `transversales` / `valor_inmediato` (3 viñetas de una línea) |
| «?» en lugar de un símbolo | Carácter fuera de WinAnsi | Reemplazar por texto |

## 8. Qué valida y calcula el generador

**Calcula:** soluciones, áreas, horas por área/línea de trabajo/fase/celda/carril, totales, conteo por fase (`{n_f1}`), tokens, concordancia singular/plural (con el `vocabulario`), reparto en columnas del catálogo (partición contigua con 1 a 4 columnas), las 9 slides en su orden, plan de pago estándar, `Programa` y `Notas` por defecto, y los modos de aire (`roomy`) de alcance, método y entregables cuando hay pocas filas.

**Bloquea (✗):** `datos.json` inválido o sin `"version": 3` (con la guía de migración: §13); tipos incorrectos con la ruta del campo; secciones o campos obligatorios faltantes (`para_que`, `frentes[].nombre`, `metodo.practica`, `metodo.datos`, `logistica`, `proximos_pasos.asesora`); `POR_DEFINIR` y «(opcional…» sin completar; `_revisar`; ids duplicados; horas no enteras, negativas, cero o > 500; C+T+A ≠ h; referencias inexistentes; hecho de portada sin `resuelto_por`; celda con soluciones sin texto; límites de líneas, carriles, fases, hitos, pasos y viñetas; marcadores de AcroForm mal ubicados o partidos; guion largo/mediano; «cohort»; `{token}` desconocido; «**» sin cerrar; cajas del PDF con demasiadas líneas o caracteres fuera de WinAnsi; catálogo estimado > 115 % del cupo; **jerga del cliente** (proceso base, Frente X, S1, F1, carril, «8 de 15 h», «inversión por horas», «precio»); **semanas y sesiones** en cualquier slide (salvo fuentes citadas y tasas del cliente) y los tokens retirados de la v3; **contratación** con lenguaje de compromiso; **próximos pasos con términos económicos**; **casos de éxito sin fuente**; plan de pago que no suma 100 %; retorno con estudios o la web, `posiciones=true` sin aval, modo `cifras` incompleto; `seguimiento.tipo` ≠ `seguimiento` sin `retorno.metas`; holguras estimadas de alcance, método o retorno menores que −10 px.

**Avisa (⚠):** fecha o mes calendario (slides y campos; la fuente de un caso ya logrado no cuenta), siglas sin glosar, «costo», más de 3 resaltados por slide, frases repetidas entre slides, celdas/hitos/pasos/tarjetas largos, nombres de línea de trabajo de más de 2 líneas, `hito` de cuota de más de 4 líneas, nombres de entregable > 72, filas de área > 11, claves de la v2 que se ignoran (`semanas_total`, `tope_h_semana`, `frentes[].semanas`, `fases[].rango`, `semana_medicion`), aval de posiciones por reconfirmar, pasos del retorno genéricos, slides omitidas, plan de pago estándar sin confirmar, `facturacion` ausente, licenciamiento sin notas, ids internos de solución visibles, claves desconocidas, holguras estimadas bajas (el estimador varía ±10 %: manda el verificador con Chrome).

**No valida** (lo hacen las personas y los revisores): que los datos coincidan con la fuente, la calidad del español, la fidelidad de cada nombre de entregable, que el dolor sea cierto, que un caso de éxito sea real, la revisión visual del PDF.

## 9. Límites y qué hacer

| Límite | Qué pasa | Salida |
|---|---|---|
| > 3 líneas de trabajo o > 3 fases en columna | No soportado | Agrupar líneas; usar la nota para el detalle |
| > 2 carriles | No soportado | Agrupar en 2 o diseñar a mano |
| Catálogo no cabe (≈ > 44 entregables de 2 líneas) | El verificador marca la columna y los px que sobran | Nombres de 1 línea (≤ 36), `entregables.compacto`, `columnas_por_carril`, título corto |
| Pocas áreas o pocas soluciones | La slide queda con aire | El generador agranda la letra de alcance, método y entregables; no se rellena con texto de más |
| > 11 áreas | Slide 2 apretada | `alcance.compacto: true` (hasta 13) |
| Alcance con > 7 filas por panel (dos herramientas) | No cabe | `alcance.compacto`, `para_que` de una línea o repartir áreas |
| Método con 3 casos, 3 prácticas largas y logística larga | Choca con el pie | Dejar 2 casos o acortar (el estimador avisa) |
| Retorno en modo `cifras` con 11 filas y nombres largos | La tabla puede no caber (la franja de destino no se muestra en este modo) | `etiqueta` corta por área, menos filas, o modo `metodo` |
| Más de 6 cuotas | No soportado | Agrupar cuotas |
| Nombre de cliente largo (> ~12 caracteres) | Titulares por defecto a 2 líneas, quitan ~40 px al catálogo | `nombre_pie` corto o títulos propios |
| Fundación | Sin inversión ni facilidad de pago (7 slides) | Los campos de monto no aplican; `inversion` y `pago` se ignoran |
| Cliente exige Impacto con estudios o Cierre | Fuera del formato | Añadir esas slides del canónico y documentar la excepción |
| Semanas, sesiones o fechas del cronograma | Bloqueo (semanas, sesiones) o aviso (fechas) | Van en el kickoff (Brief de Kickoff, `CLAUDE.md` §12), no en la propuesta |

## 10. Desviaciones del sistema canónico (deliberadas)

Este formato **no sigue** la secuencia canónica de §6/§4.2; es una variante pedida por el usuario. Se suspende: Objetivos, Programa por módulos, cronograma por sesión, Impacto con estudios (§4.9), Cierre/escalera, Calendario de inicio, la hoja de 3 pasos «Cómo arrancamos» (reemplazada por los próximos pasos con la asesora; §4.15 aplica a su redacción). El ROI se reemplaza por el retorno (método o cifras del cliente, sin estudios). La slide «Cómo trabajamos» explica el método sin exponer la metodología ABR (§4.10a). Se mantiene lo bloqueante de marca, copy y verificación (§4.1, 4.4, 4.8, 4.10, 4.10a, 4.11, 4.12, 4.13, 4.14 en lo que aplica, §10). Los 13 campos canónicos pasan a 7 + N. El titular es una frase-objetivo y el eyebrow dice «Propuesta de proyecto · Servicio de Habilidades».

**Decks anteriores:** los ya entregados no se convierten por iniciativa propia; si el usuario pide **ajustarlos, corregirlos o rehacerlos** (por ejemplo «al formato nuevo»), se rehacen en esta plantilla sin volver a preguntar el formato (un compacto v1.x se migra, §13; un canónico se reexpresa desde su `programa.md`). `dusa-cai035/` se hizo a mano en 7 slides y conserva el orden y las palabras de la reunión del 2026-10-06; **no** tiene Próximos pasos ni «Cómo trabajamos», lleva el retorno al final y todavía usa «Frente A», «S1-S11» e «Inversión por horas de sesión». Las propuestas compactas v1.x (Acua-e, Conserval, Fivenca, N58, Steam…) llevan su propio CSS congelado y `datos.json` en versión 1. Si hay que modificar una de ellas, se migra a la v3 (§13: v1 → v2 a mano y v2 → v3 con `scripts/migrar-datos-v3.py`) y se regenera con `--actualizar-css`.

## 11. Verificación recomendada antes de entregar

1. `generar-habilidades-compacto.py` sin ✗ y con todos los ⚠ leídos uno por uno.
2. `verificar-propuesta.sh` (incluye las holguras del deck), `verificar-overflow.js` y `verificar-habilidades-compacto.js` en verde.
3. PDF: 7 + N campos (Fundación: 2), `/AP` horneado en `Programa`, `Notas`, `Entregables`, `Acreditacion`; marcadores en la página correcta; cada caja de monto sobre su cuota.
4. **Revisión independiente**: cifras contra la fuente, cobertura y fidelidad de los entregables, casos de éxito contra su fuente, reglas del sistema, visual, AcroForms y lectura como cliente y como vendedor.
5. Pendientes para el usuario: quién contrata el licenciamiento, valores y plan de pago, asesora, código, certificado, aval de posiciones.

## 12. Prueba de aceptación

```bash
python3 scripts/generar-habilidades-compacto.py --datos plantillas/habilidades-compacto-canonico/datos.ejemplo-dusa.json --salida /tmp/prueba-dusa
node scripts/verificar-habilidades-compacto.js /tmp/prueba-dusa/index.html          # 9 slides
python3 scripts/generar-habilidades-compacto.py --datos plantillas/habilidades-compacto-canonico/datos.ejemplo-fundacion.json --salida /tmp/prueba-fund
node scripts/verificar-habilidades-compacto.js /tmp/prueba-fund/index.html          # 7 slides, sin inversión ni pago
```
Ambos deben generar sin errores y con todas las holguras en verde (y `verificar-overflow.js` sin desbordes). Lo mismo con `datos.ejemplo-charla.json` (6 slides), `datos.ejemplo-curso.json` y `datos.ejemplo-diplomado.json` (9 slides), que prueban las recetas del §1b, y con `datos.ejemplo-deteccion.json` (G-MAX, formato de Detección, 9 slides; 2 avisos: facturación y plan de pago estándar). DUSA: 3 avisos esperados («inversion.notas» por el licenciamiento, aval de posiciones por reconfirmar y pasos genéricos del retorno); reproduce la propuesta de DUSA con la plantilla v2, con diferencias deliberadas respecto del deck entregado (§10). Fundación (ejemplo ficticio de 19 soluciones en 5 áreas y un paso previo): 1 aviso (pasos genéricos).

Flujo completo de PDF (con un slug temporal; borrarlo y correr `python3 scripts/indexar.py` después): `bash scripts/pdf-habilidades-compacto.sh <slug>` debe dejar 12 campos con 5 cuotas (`PrecioBase`, `Descuento`, `PrecioTotal`, `Programa`, `Notas`, `PagoCuota1..5`, `Entregables`, `Acreditacion`), cada `PagoCuotaN` sobre la caja de su tarjeta.

Pruebas de regresión del generador v3 (2026-10-08, en el scratchpad de la sesión; no versionadas): **23.160 mutaciones** de los seis ejemplos (incluida la Detección) sin un solo error interno; flujo completo de PDF con un slug temporal (12 campos con 5 cuotas en Habilidades; 9 campos con 2 cuotas en Detección). Pruebas de la v2 (2026-10-07): fuzz de **4.234 mutaciones** de ambos ejemplos (borrar, null, tipos erróneos, textos vacíos o larguísimos, números negativos o cero en cada hoja) sin un solo traceback ni «Error interno»; los 13 `datos.json` v1 del repositorio migrados de forma mínima se generan o se rechazan con mensajes claros (vocabulario de Detección, composición, cierre y ninguno, sin cotización, retorno omitido); circuito de la hoja de captura (`crear` + `leer`) con datos v2. Si se vuelve a tocar el generador, rehacerlas o versionarlas antes.

## 13. Migración

### De la v2 a la v3 (2026-10-08): sin semanas ni sesiones

Un `datos.json` con `"version": 2` no se genera: el generador indica el comando. `python3 scripts/migrar-datos-v3.py <slug>` hace lo mecánico (deja una copia `.v2.<sello>.bak`; `--solo-revisar` no escribe) y lista lo que hay que reescribir a mano:

| En la v2 | En la v3 |
|---|---|
| `"version": 2` | `"version": 3` (el script) |
| `ruta.semanas_total`, `ruta.tope_h_semana`, `frentes[].semanas`, `fases[].rango`, `retorno.semana_medicion` | Se quitan (el script). Si se dejan, el generador los ignora con un aviso |
| Hitos «Semana 1 · Arranque» | «Arranque» (el script quita el prefijo); un hito que era solo «Semana 11» se renombra a mano por su evento («Cierre») |
| Cuotas «Semana 5» | Por hito: «Fase 1», «Cierre», «+30 días» (a mano) |
| «Sesiones de 2 h», «en cada sesión», «semana 1» en textos | «Encuentros de 2 h», «en cada módulo», «al arrancar» (a mano; el generador los bloquea) |
| Tokens `{semanas_txt}`, `{semana_medicion}`, `{tope_h_semana}` | Se retiran; `{n_fases_txt}` («tres fases») si hace falta |
| CSS congelado v2.0 | Regenerar con `--actualizar-css` (la cabecera de fase ya no lleva rango) |

Una Detección hecha con esta plantilla (claves opcionales) no se migra así: se rehace en el formato de Detección (`plantillas/deteccion-compacto.md`).

### De la v1.x a la v2

Un `datos.json` con `"version": 1` no se genera: el generador explica qué falta. Para migrarlo (y después pasarlo a la v3):

| En la v1 | En la v2 |
|---|---|
| `"version": 1` | `"version": 2` |
| `areas[].nombre_frente` | Se quita (la línea de trabajo tiene su propio nombre) |
| (sin `para_que`) | `areas[].para_que`: qué resuelve cada área, con palabras del cliente |
| `frentes[].areas_html`, `frentes[].etiqueta` | Se quitan; agregar `frentes[].nombre` |
| `frentes[].semanas`: «S1-S11» | «1 a 11» (y en la v3 se quita) |
| `alcance.pasos`, `alcance.quien_construye`, `etiqueta_pasos`, `etiqueta_quien` | Pasaron a `metodo` (los 4 pasos son fijos; `metodo.quien_construye`) |
| (sin método, logística ni asesora) | Agregar `metodo.practica`, `metodo.datos`, `logistica` y `proximos_pasos.asesora` |
| `retorno` opcional | Va por defecto; para quitarlo: `"omitir": ["retorno"]` |
| `inversion.titulo` «Inversión por horas de sesión» | Por defecto «Inversión del proyecto.»; «precio» y «costo» pasan a «valor» |
| (sin plan de pago) | Agregar `pago` (o aceptar el estándar 50/50 con su aviso) |
| `ruta.nota` con «S = semana…» o «Frente C» | Reescribir sin códigos internos |
| `proceso base` en textos | «paso previo» (o `vocabulario.proceso_base`) |

Después: regenerar con `--actualizar-css` (el generador se niega a regenerar un deck cuyo CSS congelado es de otra versión y lo explica) y **rehacer el `overrides.css`** del deck, porque las clases de la ruta y del alcance cambiaron (`.rg-front-name`, `.rg-front-tag`, `.rg-front-areas`, `.scope-left/.scope-right`). El generador de la v1.4 sigue en la historia de git (commit `369e87e`: `git show 369e87e:scripts/generar-habilidades-compacto.py`) por si hay que tocar un deck v1 sin migrarlo.

## 14. Historial

- **v1.3 (2026-10-05)**: titular-objetivo y retorno sin citas (caso DUSA).
- **v1.4 (2026-10-06, GitHub)**: ruta con las soluciones como protagonistas; claves opcionales para otros servicios (`vocabulario`, `composicion`, `servicio_rotulo`, `meta_servicio`, `meta_tipo`, `sin_hoja_cotizacion`, `seguimiento.tipo`, `inversion.sin_garantia`).
- **v2.0 (2026-10-07)**: reunión de DUSA del 2026-10-06 (orden, soluciones antes que horas, plan de pago, casos ya logrados, contratación como probabilidad, calendario de garantía, tono aspiracional) y `correcciones.pdf` de Ventas (preguntas del cliente en su orden, inversión antepenúltima, próximos pasos con la asesora, lenguaje del cliente, no repetir, anticipar preguntas). Absorbe las claves de la v1.4.
- **v3.0, opciones del 2026-10-08 (CAI-040 y CAI-032)**: `inversion.partes` (valor por parte), `por_fases`, `metodo_antes_de_ruta` e `incluye`; todas opt-in, sin cambio en la salida de los seis ejemplos.
- **v3.0 (2026-10-08)**: correcciones de Keiber Quintana a la Detección de G-MAX: sin semanas, sesiones ni fechas en ninguna propuesta (bloqueo en el generador y en `verificar-propuesta.sh`), fases nombradas en la ruta, hitos y cuotas por evento, retorno «a los 90 días del cierre», insumos = ficha + transcripción; formato de Detección en el mismo generador (`plantillas/deteccion-compacto.md`); `scripts/migrar-datos-v3.py`; importador del docx y ejemplos en v3.
