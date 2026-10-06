# Plantilla: Propuesta compacta de Habilidades (5 slides, dirigida por datos)

> **Estado: estándar del servicio de Habilidades desde 2026-10-05** (`CLAUDE.md` §4.21). Toda propuesta nueva de Habilidades se hace con esta plantilla; las excepciones están en §1.
> **Servicio**: Habilidades (§4.1a) · **División**: Educación o Fundación · **Formato**: A4 horizontal, 5 slides (4 en Fundación) **+ 1 slide opcional de retorno esperado**.
> **Caso base**: `clientes/propuestas/dusa-cai035/` (CAI-035, DUSA, 2026-10-04/05): 44 soluciones en 10 áreas, 2 herramientas, 500 h; 6 slides con la de retorno.
> **Cómo se usa**: se llena un `datos.json` y `scripts/generar-habilidades-compacto.py` produce el deck, los campos del PDF y el `programa.md`. Las cifras **se calculan**, no se escriben.
> **Modelo de la versión 1.3**: las dos últimas correcciones de dirección sobre el caso base: (1) el nombre del proyecto es una **frase-objetivo estilo título de tesis**, no un titular de dolor, y la propuesta se presenta como **proyecto** (no como capacitación); (2) la slide de retorno **no cita estudios ni nada de la web**: método y datos del cliente.
> Versión de la plantilla: 1.3 (2026-10-05). Integrada al router el 2026-10-05 (ver §10).

---

## 1. Cuándo usarla (y cuándo no)

**Es el formato por defecto de toda propuesta del servicio de Habilidades** (decisión del 2026-10-05). Responde a «qué voy a construir, cómo, cuánto cuesta y qué recibe» y se apoya en una **lista concreta de soluciones por área** (idealmente del informe de Detección del cliente). IDIA no debe elegir otro formato para Habilidades por iniciativa propia.

| Situación | Usar |
|---|---|
| Habilidades con N soluciones ya identificadas por área, varias áreas, con horas por solución | **Esta plantilla**, directo (importador del insumo, §4) |
| Habilidades sin insumo todavía (solo se sabe el objetivo y las áreas) | **Esta plantilla**: armar `datos.json` con el usuario, pidiéndole las soluciones, horas y fases. No se inventan soluciones, horas ni precios |
| Capacitación o taller in-company (`CAI-`, `TA-`) cuyo contenido son **soluciones/entregables por área** | **Esta plantilla** |
| Charla, curso, diplomado, o taller/capacitación cuyo contenido es un **programa de módulos y sesiones** sin lista de soluciones | **Preguntar antes de generar** (una sola vez): «¿Lo armo en el esquema compacto de Habilidades (el programa se reexpresa como entregables por área) o en el deck canónico de ~13 slides?». Sin respuesta, no generar. Si el usuario elige compacto, se reexpresa cada módulo o sesión como una solución con su entregable y horas, y se documenta la adaptación en `supuestos` |
| Combo Detección + Habilidades cotizados juntos, plan integral de 4 servicios, Políticas, Innovación | Los canónicos de cada servicio (§4.1a/§4.1b): esta plantilla no los cubre |
| Cotización por fases o por permanencia | No soportada (solo la hoja por horas, marcador «Propuesta Económica») |
| Más de 3 frentes, más de 2 herramientas (carriles) o más de 13 filas de área | Fuera de límites (§9): diseñar a mano o dividir en dos propuestas |

El deck **no** lleva: Impacto con estudios, Próximos pasos, Cierre, Metodología ABR, Equipo facilitador. Es una decisión del caso base (el usuario pidió 5 slides y luego una de retorno sin estudios). El **retorno esperado** es un módulo opcional (§6, «Retorno esperado»). Ver §10 si el cliente exige alguna de las otras.

## 2. Las 5 slides y la pregunta que responde cada una

| # | Clase | Responde | Contenido |
|---|---|---|---|
| 1 | `.s-cover` | **El dolor** | Titular en 2 partes + lead + 3 datos de la auditoría (+ fuente) |
| 2 | `.s-scope` | **Qué voy a hacer** | N soluciones en K áreas, una barra de unidades por área (1 unidad = 1 solución), pasos, quién construye, qué queda fuera |
| 3 | `.s-route` | **Cómo lo voy a hacer** | Matriz frentes × fases con horas y nº de soluciones por celda, columna de seguimiento 30-60-90, 3 a 5 hitos, nota |
| 4 | `.s-price` | **Cuánto cuesta** | Hoja de cotización estándar por horas (campos de precio vacíos para ventas), licenciamiento de terceros aparte, descuento urgente, garantía 30-60-90 |
| 5 | `.s-deliv` | **Qué recibe** | Catálogo de **todos** los entregables (uno por solución) por área + 2 cajas editables: entregables transversales y valor inmediato |
| 6 (opcional) | `.s-roi` | **Qué retorno se espera** | Módulo `retorno`. Modo `metodo`: cómo se calcula el retorno (volumen → tiempo actual = línea base → tiempo con la solución → horas recuperadas → dinero → posiciones y costo anual), metas a 30-60-90 y destino del tiempo recuperado. Modo `cifras`: tabla por área con las cifras del cliente. **Sin campos de PDF y sin citas de estudios ni de la web** |

> Los títulos que el usuario dio al pedir el caso base («¿Qué voy a hacer?», «¿Cómo lo voy a hacer?»…) eran una **guía de contenido, no títulos literales**. Los titulares del deck son afirmativos («44 soluciones en 10 áreas de DUSA.», «Tres frentes en paralelo, 11 semanas.», «Inversión por horas de sesión.», «Todo lo que DUSA recibe.»). El eyebrow de cada slide lleva el nombre de la sección (`02 · Alcance`, `03 · Ruta`, `05 · Entregables`, `06 · Retorno`). El **nombre del proyecto** (h1 de la portada) sí es una frase-objetivo estilo título de tesis («Optimización de procesos y datos con inteligencia artificial en 10 áreas de DUSA»): dice qué se logra y dónde, no el dolor.

### Glosario (los términos de `datos.json`)

| Término | Qué es |
|---|---|
| **Carril** | Herramienta o plataforma sobre la que se construye (1 o 2; p. ej. Microsoft 365 Copilot, Claude Team). Define el color (amarillo/naranja) y el orden de los paneles |
| **Área** | Función del cliente cuyos procesos se automatizan (Contabilidad, Nómina…). Cada área pertenece a un carril y a un frente |
| **Proceso base** | Un proceso previo que condiciona a otros (p. ej. ordenar la base de datos de empleados). Cuenta sus soluciones y horas pero **no** cuenta como «área» en «N soluciones en K áreas» |
| **Solución / entregable** | Una unidad construida (asistente, validador, tablero, archivo…). Cada solución genera exactamente un entregable en la slide 5 |
| **Frente** | Equipo de trabajo que avanza en paralelo (1 a 3). Agrupa áreas del mismo carril; tiene un rango de semanas |
| **Fase (F1 a F3)** | Etapa de la ruta, en columna: F1 prioridad sin dependencias · F2 necesita un acuerdo, dato o solución previa · F3 extensiones y tableros (los textos son editables). Se **destaca** (`destacada`) la que concentra más horas |
| **F0** | Horas de arranque (semana 1), sin columna. Si se declara una solución F0 cuenta en `{n_total}`, en las horas y en el catálogo. La línea base de horas ya es un entregable transversal por defecto: no duplicarla como solución |
| **Celda** | Cruce frente × fase: horas y nº de soluciones se calculan; el texto lo escribe una persona (≤ ~90 caracteres) |
| **C / T / A** | Horas de construcción, pruebas y adopción por solución (el insumo dice «testeo»; en el deck, «pruebas») |
| **Hito** | Evento de la ruta (3 a 5): título corto + texto ≤ ~90 caracteres, sin fechas calendario |
| **Seguimiento 30-60-90** | Check-ins posteriores al cierre de cada área (`empresa/tipos-de-documento.md §0.2`) |
| **Titular-objetivo** | Frase nominal estilo título de tesis que responde al objetivo del servicio («Optimización de …  con … en …»). Va en 1 a 3 líneas más una franja amarilla; sin punto final |
| **Línea base** | Medición de la semana 1 del tiempo que toma hoy cada proceso: es el «antes» contra el que se mide el retorno |
| **Retorno esperado** | Slide opcional (§6). **No** es una garantía de retorno: la garantía 30-60-90 es de acompañamiento. «Hacia la semana N» = `semanas_total` + 13 (90 días de seguimiento), aritmética que servicio debe confirmar |

## 3. Archivos

```
plantillas/habilidades-compacto.md                       ← este documento
plantillas/habilidades-compacto-canonico/
    habilidades-compacto.css      CSS genérico (se copia congelado a cada propuesta)
    datos.plantilla.json          esquema anotado con POR_DEFINIR
    datos.ejemplo-dusa.json       instancia real completa, 6 slides (prueba de aceptación: reproduce dusa-cai035)
    datos.ejemplo-fundacion.json  ejemplo ficticio de Fundación, 5 slides (prueba de la variante sin inversión)
    brief.plantilla.md            brief interno con placeholders
scripts/
    habilidades-importar-insumo.py   docx de insumo → borrador de datos.json
    habilidades-retorno-xlsx.py      crear: datos.json → retorno-captura.xlsx · leer: hoja completada → datos.json["retorno"] (requiere openpyxl)
    generar-habilidades-compacto.py  datos.json → index.html, acroforms.json, programa.md, meta.json, brief.md
    verificar-habilidades-compacto.js  mide holguras exactas en Chrome (colisiones, desbordes de tarjeta, pie, márgenes)
    customize-habilidades-compacto.py  ajusta las 2 cajas de la slide de entregables en el PDF (genérico)
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

`verificar-propuesta.sh` detecta el deck por la presencia de `habilidades-compacto.css` y corre también el verificador de holguras.

## 4. Flujo para una propuesta nueva

**Pre-requisitos (bloqueantes, CLAUDE.md §4.1, §4.1a y §6 paso 3):** división confirmada (`educacion`/`fundacion`), servicio = `habilidades` y `alianza` (sí/no) confirmados con el usuario, código asignado (siguiente `CAI-###` libre; ver `clientes/INDEX.md`). Preguntar también por la **Ficha Comercial**, la `fecha_arranque_deseada` y los `resultados_esperados`: sin ellos el deck no muestra fechas de inicio ni ROI (y no se inventan). Sin división no se genera.

1. **Carpeta y datos.** `clientes/propuestas/<slug>/`. Con docx de insumo:
   `python3 scripts/habilidades-importar-insumo.py <insumo.docx> --nombre "Cliente" --slug <slug> --codigo CAI-0NN --salida clientes/propuestas/<slug>/datos.json`
   Sin docx: copiar `datos.plantilla.json`.
2. **Completar `datos.json`** siguiendo §5 y §6. Pedir al usuario lo que falte; no inventar. Los `POR_DEFINIR` y las marcas `_revisar` bloquean la generación.
3. **Generar y validar:** `python3 scripts/generar-habilidades-compacto.py <slug>`. Los errores (✗) impiden escribir; los avisos (⚠) hay que leerlos uno por uno.
3b. **Retorno (opcional).** Sin datos del cliente: agregar `retorno` en modo `metodo` (default; en Fundación habla de capacidad liberada, no de dinero). Con datos: `python3 scripts/habilidades-retorno-xlsx.py crear <slug>` genera `retorno-captura.xlsx` (hoja **interna**, nunca va al cliente; trae una pestaña `_control` con el código y la huella de ids para que no se cargue en el `datos.json` equivocado). Las personas completan las celdas azules (tiempos, ejecuciones, **tipo de dato** de cada fila, costo hora, dotación) y `leer retorno-captura.xlsx --datos <slug> --origen "documento o sesión; fecha; quién del cliente lo validó" --nota "..." [--posiciones --aval "quién; fecha; medio"] [--quitar-destino]` escribe el bloque en modo `cifras`. Obligatorios: `--origen` y `--nota`; con `--posiciones`, también `--aval` y las horas productivas por posición en la hoja. El lector es estricto (rechaza números ambiguos como «1.200», fórmulas sin valor guardado, valores lógicos, negativos), valida con el generador **antes de escribir** y deja un `.bak` con sello. **Nunca** completar la hoja por intuición: una solución sin los tres datos no cuenta y las áreas con cobertura parcial se rotulan «(n de m procesos)».
4. **Medir holguras:** `node scripts/verificar-habilidades-compacto.js <slug>` y `node scripts/verificar-overflow.js <slug>` (o `--medir` en el generador). Ante un ✗, **acortar contenido**, no el diseño (§4.10). Cómo leer los mensajes:

   | Mensaje del verificador | Qué hacer |
   |---|---|
   | portada: fuente/datos vs línea de código · titular vs lead | Acortar `portada.fuente`, `hechos[].texto`, `titulo_linea1/destacado` (máx. 3 líneas) o `lead` |
   | alcance: bloque principal vs pie (detalla alturas) | Acortar `alcance.subtitulo`, `pasos`, `quien_construye`, `fuera_alcance`; `alcance.compacto: true` |
   | ruta: nota vs pie · celda/frente/fase desborda | Acortar `ruta.nota`, la celda indicada o los hitos; la fila admite 4 líneas |
   | inversión: Duración vs Programa | `inversion.duracion` ≤ 2 líneas (~110 caracteres) |
   | inversión: licenciamiento vs pie / tarjeta desborda | Acortar `licencias.tarjetas[].texto` (≤ ~250) o su `nota` |
   | entregables: columna N vs franja (lista áreas y px) | Nombres a 1 línea (≤ 36 caracteres) en las áreas largas, `entregables.compacto`, `columnas_por_carril`, título/subtítulo más cortos |
   | entregables: ancho del subtítulo / marcador «Lo que se llevan» en una línea | Título demasiado largo: definir `entregables.titulo` (≤ 28) o `nombre_pie` corto |
   | retorno: bloque principal / franja de destino vs banda final | Acortar pasos, metas, destino o gancho; en modo cifras, menos filas o `etiqueta` más corta |
   | texto dentro del margen derecho | Algún texto se sale de la slide: acortarlo |

5. **PDF:** `bash scripts/pdf-habilidades-compacto.sh <slug>` (regenera, verifica, genera el PDF y corre el par de campos). Requiere `pypdf` en el Python activo; si no está, el script explica cómo crear un entorno aparte. **Dentro de este paso** `generar-pdf.sh` estampa `fecha_entrega`, pasa `meta.json` a «Enviada» (convención: terminado = enviado) y reindexa `clientes/INDEX.*`; si el flujo falla después, el wrapper restaura `meta.json`. PDF previos de la carpeta se mueven a `_pdf-anteriores/` con sello de fecha y hora (el nombre del PDF sale del titular de la portada: `<CÓDIGO> <titular>`, cortado a 90 caracteres).
6. **Revisión visual** de las páginas del PDF (§4.10 es bloqueante: el script terminando sin error no equivale a PDF correcto). Renderizar a PNG (p. ej. PyMuPDF) y mirar cada slide, incluido el texto horneado de los campos.
7. **Registro:** si aún no se envía, corregir a mano `estado`/`fecha_entrega`. Añadir la entrada en `aprendizajes.md` si el caso enseñó algo.

Para **cambios posteriores**: se edita `datos.json` y se regenera (el `index.html` se sobrescribe). `meta.json` se actualiza respetando estado y fecha; `brief.md` solo refresca su bloque «auto» (`--forzar-brief` lo reescribe); `overrides.css` no se toca (`--forzar-overrides`). Para propagar un cambio de CSS de la plantilla: `--actualizar-css` (recalcular antes los rects de `customize-habilidades-compacto.py` si se movieron cajas).

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
| carriles, áreas, proceso base, soluciones con C/T/A/fase/detalle, frentes y su alcance, semanas totales y tope h/semana si el texto los dice | cliente/división, portada, alcance, rangos de fases, celdas de la ruta, hitos, notas de inversión, entregables transversales |

Valida contra lo que declara el docx (horas por área, carril y frente; total de cada fila; cobertura de filas) y avisa si algo no cuadra. La asignación de áreas a frentes es por coincidencia de nombre completo: si es ambigua queda `POR_DEFINIR` con aviso. Los nombres de entregable son una propuesta cortada del texto largo y quedan `_revisar` (hay que reescribirlos con el matiz correcto, §6). No sobrescribe un `--salida` existente (`--forzar`): para incorporar una versión nueva del insumo, importar a otra ruta y copiar a mano lo que cambió.

## 5. Esquema de `datos.json`

Los textos de cara al cliente aceptan **tokens** `{token}` en minúsculas (el generador los reemplaza y falla si no existen o quedan sin resolver). Tokens: `{cliente} {cliente_corto} {codigo} {n_total} {n_total_txt} {n_entregables_txt} {n_areas} {n_areas_txt} {n_bases} {h_total} {semanas} {semanas_txt} {semana_medicion} {tope_h_semana} {tope_h_dia} {rango_seguimiento}`, por fase `{n_f0..n_f3} {h_f0..h_f3}`, por frente `{n_frente_<id>} {h_frente_<id>}` (id en minúsculas), por carril `{n_carril_<id>} {h_carril_<id>}`. `{n_total_txt}`, `{n_entregables_txt}` y `{n_areas_txt}` ya traen la concordancia («1 solución», «44 entregables», «10 áreas»).
**Negrita** `**x**`: se interpreta en `portada.lead`, `hechos[].texto`, `alcance.*`, `fases[].descripcion`, `frentes[].celdas`, `ruta.*`, `seguimiento.*`, `licencias.tarjetas[].texto`, `inversion.duracion` y `entregables.subtitulo`; en nombres de entregable y en los campos del PDF se ignora (§4.8: sin negrita en campos editables). Máx. ~3 resaltados por slide.

| Sección | Campos | Notas y límites |
|---|---|---|
| `cliente` | `nombre`, `slug`, `codigo`, `nombre_pie` (opc.) | `nombre_pie`: nombre corto para el pie y los **titulares por defecto** (`{cliente_corto}`); definirlo si `nombre` supera ~12 caracteres |
| raíz | `division`, `alianza` (bool, obligatorio), `eje`, `origen`, `fuente_insumo`, `siglas_ok`, `supuestos`, `pendientes` | `siglas_ok`: siglas del cliente que no requieren glosa (§4.12). Claves desconocidas se avisan con sugerencia |
| `portada` | `titulo_lineas[1-3]`, `titulo_destacado`, `lead`, `hechos[2-4]` (`num`, `texto`, **`resuelto_por`**), `fuente`, `eyebrow` (opc.) | **Titular-objetivo**: líneas + franja amarilla; largo total ≤ 82 caracteres con código de 7 (si no, el nombre del PDF se corta a media palabra), sin punto final. El h1 baja solo de tamaño: ≤ 44 car. → 64 px, ≤ 60 → 54 px, ≤ 82 → 46 px, más → 42 px; cada línea ≤ 25/30/35/38 caracteres según el tamaño. `titulo_linea1` (una sola línea) sigue aceptado como alias antiguo. `texto` del hecho ≤ ~95, `num` ≤ 9 |
| `carriles[1-2]` | `id` (minúsculas/números/_), `nombre`, `nombre_corto`, `color` (`amarillo`/`naranja`) | El orden manda en slides 2 y 5 |
| `areas[]` | `id`, `nombre`, `carril`, `frente`, `proceso_base`, `nombre_frente`, `nombre_catalogo`, `soluciones[]` | Máx. 13 filas; >11 pide `alcance.compacto`. El orden es el de aparición. Ids únicos |
| `…soluciones[]` | `id`, `entregable`, `C`,`T`,`A` (o solo `h`), `fase`, `detalle` | Horas enteras ≥ 0, ≥ 1 en total. `entregable` ≤ 36 ideal (1 línea), ≤ 72 recomendado, ≤ 99 máx. |
| `alcance` | `subtitulo`, `pasos[2-4]`, `quien_construye`, `fuera_alcance[]`, `compacto`, `titulo`, `etiqueta_pasos`, `etiqueta_quien`, `etiqueta_fuera`, `etiqueta_proceso_base` | `subtitulo` 1 línea (~110); la etiqueta de pasos se ajusta a 2/3/4 |
| `fases[]` | `id` (`F0`..`F3`), `titulo`, `rango`, `descripcion`, `destacada` | 2-3 con columna + `F0` opcional. Rangos en **semanas** |
| `frentes[1-3]` | `id`, `carril`, `semanas`, `celdas{F1,F2,F3}`, `areas_html` (opc.) | Cada celda ≤ ~90; horas y nº se calculan; `areas_html` reemplaza el rótulo automático de áreas |
| `ruta` | `semanas_total` (entero), `tope_h_semana` (entero, por defecto 20), `hitos[3-5]`, `titulo`, `subtitulo`, `nota` | Hito: `titulo` corto, `texto` ≤ ~90 |
| `seguimiento` | `rango`, `texto`, `items[2-3]` (`dias`,`texto`), `etiqueta` | Marco 30-60-90 |
| `inversion` | `notas[]`, `licencias{titulo,tarjetas[≤2],nota}`, `titulo`, `duracion`, `programa[]`, `garantia_texto` | Sin precios aquí. Sin `notas` el campo Notas del PDF queda **en blanco** para ventas. En Fundación se ignora |
| `retorno` (opc.) | `modo` (`metodo`\|`cifras`), `posiciones` (bool), `aval_posiciones{quien,fecha,medio}`, `titulo`, `subtitulo`, `pasos[4-7]`, `metas[3]`, `destino[3]`, `gancho`, `semana_medicion`, `costo_hora_usd`, `horas_por_posicion`, `areas[]`, `nota_datos`, `origen_datos{documento,fecha,validado_por}` | Activa la slide 6 (5 en Fundación). **`posiciones=true` exige `aval_posiciones`** (quién del cliente avaló plantear posiciones, cuándo y por qué medio; sin aval no se genera). Modo `cifras` exige `costo_hora_usd` > 0, `nota_datos` (≥ 30 car.: de dónde salen las cifras y cuáles son estimaciones), `origen_datos` completo, y 1 a 11 filas `areas[]` = `area` (id o nombre), `tipo_dato` (`medido`\|`declarado`\|`estimacion`), `horas_actuales`, `horas_con_solucion`, opcionales `retrabajo_usd`, `tardios_usd`, `etiqueta` y, con `posiciones=true`, `horas_por_posicion` (global) y por fila `posiciones_hoy`, `posiciones_reducibles`, `posiciones_evitables` (contratación que no será necesaria; puede superar a las de hoy), `costo_anual_usd`, `tipo_dato_posiciones`. Sin textos que citen estudios, la web, `http`, `.com`. **Por división**: los pasos, metas, destino y título por defecto de Fundación hablan de capacidad liberada y de atender a más personas, no de dinero ni de nómina |
| `entregables` | `transversales[]`, `valor_inmediato[]`, `compacto`, `columnas_por_carril`, `titulo`, `subtitulo`, `etiqueta_transversales`, `etiqueta_valor` | Viñetas ≤ ~60 caracteres (el generador mide líneas con las métricas exactas del PDF si hay pypdf), ≤ 4 líneas por caja. `columnas_por_carril`: lista con un valor ≥ 1 por carril (en orden), suma ≤ 4 (p. ej. `[2,2]`, `[3,1]`, `[2]`) |

## 6. Reglas de contenido (lo que se aprendió construyendo el caso base)

### Portada
- **El dolor es del alcance.** Cada dato de la portada debe estar **resuelto por soluciones de la propuesta** (`resuelto_por` obligatorio). Caso base, ronda 1: la portada abría con «+300 facturas al mes a mano», pero ese frente lo asumía Sistemas del cliente y estaba fuera de alcance; la slide 2 lo contradecía.
- Usar **datos de la auditoría** del cliente (citar la fuente en `fuente`); no cifras de estudios ajenos (el Impacto del §4.9 no está en este formato).
- **El nombre del proyecto es una frase-objetivo estilo título de tesis** (pedido del 2026-10-05): nominal, responde al objetivo del servicio y dice dónde («Optimización de procesos y datos con inteligencia artificial en 10 áreas de DUSA»). El dolor va en los 3 datos de la franja, no en el titular. Usar tokens (`{n_areas}`, `{cliente_corto}`) en la franja amarilla.
- El eyebrow nombra el servicio y presenta el trabajo como proyecto, no como capacitación («Propuesta de proyecto · Servicio de Habilidades», §4.1a punto 4; cambio pedido el 2026-10-05 para CAI-035). El lead usa verbos de proyecto: ordena procesos y datos, construye, deja adoptado y mide el efecto. Revisar que el resto del deck no reduzca el trabajo a una capacitación («capacitación» solo cuando es un proceso del cliente, no de Intezia).
- Lead: «identificó» (no «midió») si la fuente no tiene mediciones; «las soluciones que atienden cada uno», no «que los resuelven» (no prometer de más).

### Alcance
- Una unidad = una solución; el total sale del conteo. «N soluciones en K áreas» **excluye** el proceso base del conteo de áreas (se anota «y un proceso base»).
- Glosar qué son las soluciones en el subtítulo (p. ej. «asistentes de IA, validadores y tableros»): «agentes» sin explicar confunde.
- `fuera_alcance`: lo que el cliente ya asume con sus desarrollos (decir «asume con sus propios desarrollos», no «ya cubre»: la fuente puede decir que no tienen fecha), lo que requiere un aplicativo, y restricciones de datos sensibles. Si algo queda fuera, dar el **motivo** («que Sistemas cubre con…»), para que el líder del área no lo lea como un rechazo.

### Ruta
- **Semanas, no fechas.** El insumo vigente es relativo al arranque («S = semana de trabajo desde el arranque, cuya fecha se acuerda con el cliente»). El caso base tuvo fechas en la primera versión del insumo y se retiraron todas en la corrección. El generador avisa de cualquier fecha o mes calendario, también en los campos del PDF.
- **Las horas deben cuadrar a la vista.** Si hay fase de arranque (F0) cuyas horas no aparecen en ninguna celda, la nota debe explicarlo («12 h de arranque más 224, 148 y 116 h…»). Quien suma las celdas del frente y no llega al total cree que hay un error.
- Llamar «proyección» a las horas: la fuente las estima por ruta y factores.
- Explicar la «S» y evitar «ejecutor»/«prioridad declarada» sin contexto («quien ejecuta el proceso», «prioridad de cada área»).
- El 90 días no debe sonar a ROI garantizado: «Retorno en tiempo ahorrado y habilidades instaladas», no «ROI de X».
- Hitos con dependencias del cliente: decir quién («Sistemas y Nómina acuerdan…»).
- Evitar anglicismos: «inducción» y no «onboarding», «orden de candidatos» y no «ranking» (§4.4). «Pruebas» y no «testeo».

### Inversión
- Hoja estándar por horas: campos `PrecioBase`, `Descuento`, `PrecioTotal` **vacíos** (los llena ventas), `Programa` y `Notas` pre-llenados (o `Notas` en blanco). Sin tarifa en `empresa/politicas-comerciales.md`: no inventar precios.
- **Licenciamiento de terceros aparte**, con precio de lista y **fecha de cada fuente por separado**. Aclarar el pago anual vs mensual. No afirmar quién contrata si la fuente no lo dice: anotarlo en `supuestos` y confirmar.
- **Duración**: «Proyección de N h de sesión en M semanas de trabajo desde el arranque» (máx. 2 líneas).
- **No** incluir ROI estimado sin Ficha Comercial o resultados esperados explícitos. La garantía 30-60-90 es la del servicio Habilidades y va sin mecanismo de reembolso.
- No exponer condiciones contractuales internas o de terceros que la fuente ya retiró (en el caso base, la «condición de contratación» de un proveedor se mostró en la primera versión y la fuente la eliminó).

### Entregables
- **Un entregable por solución**, todos visibles, agrupados por área. El nombre dice **qué se entrega** y conserva el matiz del insumo: «propuesta de notas de crédito» (no «notas de crédito»), «pedido sugerido», «solicitudes de pago» (no «pagos»: la IA no opera la banca), «archivo para carga masiva» (no «carga masiva»: la carga la hace otro), «trasladados a [herramienta]» si es adopción de algo ya construido.
- Evitar nombres que parezcan un tema («Plan administrativo») cuando la fuente nombra un tipo de entregable; evitar «contrato de datos» (se lee como contrato legal): «entrega de datos por área».
- Si un entregable de la fuente es insumo del proceso (constancias, certificados), no nombrarlo como si Intezia lo emitiera («Lectura de constancias…»).
- **Capacidad real del catálogo** (4 columnas de ~200 px a 11 px): 1 línea ≈ 36 caracteres, 2 líneas ≈ 72, 3 líneas ≈ 108. Cabe en total aproximadamente **44 entregables de 2 líneas u ~80 de 1 línea** (repartidos entre columnas con el desequilibrio entre carriles). Con 1 o 2 columnas el texto es más ancho y entran más. Prioriza nombres cortos (≤ 36) en el carril más cargado.
- **Entregables transversales** (línea base, seguimiento 30-60-90) y **valor inmediato** (hitos tempranos) van en las dos cajas editables. El valor inmediato usa **semanas** y solo hitos respaldados por la fuente («Semana 5: N soluciones prioritarias adoptadas» sale de `{n_f1}`).
- El «Certificado de participación INTEZIA» **ya no va por defecto** (es un rastro de curso y estas propuestas se presentan como proyecto). Solo se incluye si el cliente lo pide; el ejemplo de DUSA lo conserva porque reproduce el deck entregado, anotado en `supuestos`.
- El subtítulo conserva «Lo que se llevan» (el generador lo mantiene en una sola línea) y la slide contiene la palabra «Entregables» (marcador de las cajas, §7).

### Retorno esperado (slide opcional)
- **Sin estudios ni referencias de la web** (decisión del 2026-10-05): ni barras de literatura, ni «fuentes» externas, ni `http`, ni «según un informe de [Firma]», ni «garantizado». El generador falla si el texto de la slide los menciona. Una nota de datos del cliente («Datos declarados por los líderes en las sesiones de levantamiento…») sí es válida, y también «estudio de tiempos» (es un método de medición, no una cita). Las cifras de estudios, si el usuario las quiere, se respaldan **de forma oral** y quedan en el `programa.md`/`brief.md`, no en la slide.
- **Sin cifras propias sin datos.** Si las fichas de levantamiento dicen «No declarado» (caso DUSA), la slide va en modo `metodo`: explica cómo se calculará y qué metas se miden a 30-60-90. Pasar a `cifras` solo con datos del cliente, con el **tipo de dato de cada fila** y el **origen de los datos** (documento o sesión, fecha y quién del cliente los validó); las estimaciones se rotulan «(estimación)» en la tabla y el pie nombra el origen.
- **Posiciones y nómina.** `posiciones: true` plantea de frente cuántas posiciones representa el trabajo manual, cuántas se reducen o no hará falta contratar y su costo anual con las escalas del cliente. Se activa **solo con aval registrado** en `aval_posiciones` (en DUSA, la gerencia lo aceptó y quedó anotado) y, en modo `cifras`, con datos y horas productivas por posición; si no, dejarlo en `false` y hablar de capacidad y tiempo. El generador avisa siempre que el aval hay que reconfirmarlo antes de enviar y antes de circular el documento entre líderes de área. **Nunca** se escribe una cifra de nómina, escala salarial o dotación que el cliente no haya entregado.
- «Sin ampliar la nómina» va en condicional («puede», «si el tiempo se libera»): es una proyección de Intezia, no un hallazgo. La garantía 30-60-90 es de acompañamiento, no de retorno: no usar «garantizado».
- «Hacia la semana N» es aritmética de la propia propuesta (`semanas_total` + 13). El generador lo avisa siempre: confirmarlo con el equipo de servicio antes de enviar.
- Tono sobrio, de consultor: sin contrastes «no es X, es Y», sin cierres sentenciosos.

### Transversales a todo el deck
- Español neutro, sin voseo; sin guion largo ni mediano (§4.13); sin «cohort» (§4.4); acrónimos de jerga glosados en cada slide (§4.12); sin afirmar migración de stack del cliente (§4.11): la herramienta nueva **se suma**, la que el cliente ya opera «se extiende».
- No exponer nombres de personas del cliente.
- Nada de lo que la fuente no diga: lo supuesto va en `supuestos` para confirmar con el usuario.

## 7. Campos AcroForm (PDF)

7 campos (13 en el canónico; aquí no hay slide de pasos; la slide de retorno no lleva campos): `PrecioBase`, `Descuento`, `PrecioTotal`, `Programa`, `Notas` (slide 4) y `Entregables`, `Acreditacion` (slide 5, «Valor inmediato»; el nombre `Acreditacion` se conserva por compatibilidad con `agregar-campo-precio.py`). Fundación: solo los 2 de la slide 5.

- `agregar-campo-precio.py` ubica cada grupo por **texto de página**: «Propuesta Económica» (solo slide 4) y «Lo que se llevan» + «Entregables» (solo slide 5). El generador falla si la frase aparece en otra slide o si falta, y el verificador comprueba que «Lo que se llevan» quede en **una** línea. No usar nunca «Cómo arrancamos», «Inversión por fases» ni «Inversión por Permanencia».
- Los rects de slide 4 son los del canónico (`_base/styles.css`); no mover `.programa-box`, `.notas-box`, `.cot-frame`.
- Los de slide 5 se reubican en `customize-habilidades-compacto.py` (px × 0.75 → pt): `.db-box-1` (60, 49.75, 397.125, 100.75) y `.db-box-2` (445.125, 49.75, 782.25, 100.75), 68 px de alto (4 líneas sin recortar descendentes), fondo oscuro y texto blanco horneados (10,5 pt, negrita). Cada viñeta cabe en una línea (~60 caracteres incluida la viñeta); el generador mide las líneas con las métricas del PDF (4 máx.).
- Caracteres: solo Latin-1/WinAnsi (sin ≥, →, ✓, emoji): el PDF los dibujaría como «?».
- Orden obligatorio: `generar-pdf.sh` → `customize-acroforms.py` → `customize-habilidades-compacto.py` (el wrapper lo hace). `generar-pdf.sh` resetea todos los campos.

### Diagnóstico del PDF

| Síntoma | Causa probable | Acción |
|---|---|---|
| Campos vacíos o con el texto de ejemplo del sistema (`[Condiciones de pago…]`) | Se corrió `generar-pdf.sh` sin `customize-acroforms.py`, o falta la clave en `acroforms.json` | Correr el par completo con el wrapper |
| Faltan los campos de la slide 5 | La frase «Lo que se llevan» o «Entregables» se partió en dos líneas (título/nombre de cliente largo) o falta | `verificar-habilidades-compacto.js` lo marca; definir `entregables.titulo` corto / `nombre_pie` |
| Campos de la slide 5 con texto cortado | Más de 4 líneas o viñetas largas | Acortar `transversales` / `valor_inmediato` (3 viñetas de una línea) |
| Texto de ejemplo del HTML visible bajo los campos | CSS de impresión alterado | No tocar `.multi-box`; regenerar |
| «?» en lugar de un símbolo | Carácter fuera de WinAnsi | Reemplazar por texto |

## 8. Qué valida y calcula el generador

**Calcula:** soluciones, áreas, horas por área/frente/fase/celda/carril, totales, conteo por fase (`{n_f1}`), tokens, concordancia singular/plural, reparto en columnas del catálogo (partición contigua que minimiza la columna más alta, con 1 a 4 columnas), alineación del primer título entre columnas del mismo carril, unidades de la slide 2, textos por defecto.

**Bloquea (✗) además de lo anterior:** titular sin líneas o con más de 3; retorno con `modo` inválido, `destino`/`metas` ≠ 3, `pasos` fuera de 4 a 7, textos que citen estudios o la web, y en modo `cifras`: sin costo hora, sin `nota_datos`, sin filas o más de 11, áreas inexistentes o repetidas, `tipo_dato` ausente o inválido, horas con la solución mayores que las actuales, números negativos, posiciones incompletas o reducibles mayores que las de hoy.

**Bloquea (✗) en general:** `datos.json` inválido; tipos incorrectos (con la ruta del campo); secciones obligatorias o campos faltantes; `POR_DEFINIR` y textos «(opcional…» sin completar; `_revisar`; ids duplicados (carriles, fases, frentes, áreas, soluciones); horas no enteras, negativas, cero o > 500; C+T+A ≠ h; fase/frente/carril inexistentes; área de un carril distinto al de su frente; `alianza` ausente o no booleana; hecho de portada sin `resuelto_por` o con id inexistente; celda con soluciones y sin texto; límites de frentes/carriles/fases/hitos/pasos/viñetas; marcadores de AcroForm mal ubicados o partidos; guion largo/mediano; «cohort»; `{token}` desconocido o sin resolver; «**» sin cerrar; cajas AcroForm con demasiadas líneas o caracteres fuera de WinAnsi; catálogo estimado > 115 % del cupo.

**Bloquea (✗) también** (v1.3 endurecida): `posiciones=true` sin `aval_posiciones` completo; modo `cifras` sin `origen_datos` completo o, con posiciones, sin `horas_por_posicion`; `tipo_dato_posiciones` inválido; números no finitos; texto de la slide de retorno con «garantiz-», firmas citadas («informe de McKinsey»), `http`, `www.`, dominios, benchmark o «según un estudio»; holgura estimada de la slide de retorno menor de −10 px.

**Avisa (⚠) además de lo anterior:** titular que cortaría el nombre del PDF o que termina en punto, líneas del titular más anchas que el tamaño admite, titular idéntico al del ejemplo de DUSA, «Hacia la semana N» por confirmar, semana de medición fijada a mano, aval de posiciones por reconfirmar, pasos genéricos (iguales para cualquier cliente), destino genérico, área que recupera el 100 % de sus horas (horas con la solución = 0), cobertura parcial en cifras (el total se rotula con la cobertura), estimaciones sin tipo de dato, línea base duplicada como solución F0, **ids internos de solución visibles** en el texto del cliente (ninguna slide los define), holgura estimada de la slide de retorno menor de 12 px.

**Avisa (⚠) en general:** fecha o mes calendario (slides y campos), siglas sin glosar, más de 3 resaltados por slide, celdas/hitos/pasos/licencias largos, nombres de entregable > 72, filas de área > 11, titulares largos, claves desconocidas, licenciamiento sin notas, catálogo cerca del cupo (el estimador varía ±10 %: manda el verificador con Chrome).

**No valida** (lo hacen las personas y los revisores): que los datos coincidan con la fuente, la calidad del español, la fidelidad de cada nombre de entregable, que el dolor sea cierto, la revisión visual del PDF.

## 9. Límites y qué hacer

| Límite | Qué pasa | Salida |
|---|---|---|
| > 3 frentes o > 3 fases en columna | No soportado | Agrupar frentes; usar la nota para el detalle |
| > 2 carriles | No soportado | Agrupar en 2 o diseñar a mano |
| Catálogo no cabe (≈ > 44 entregables de 2 líneas) | El verificador marca la columna y los px que sobran | Nombres de 1 línea (≤ 36), `entregables.compacto`, `columnas_por_carril`, título corto |
| Menos de 4 áreas por carril | Se usan menos columnas, más anchas (automático) | — |
| > 11 áreas | Slide 2 apretada | `alcance.compacto: true` (hasta 13) |
| Retorno en modo `cifras` con 11 filas y nombres largos | La tabla puede no caber (la franja de destino no se muestra en este modo) | `etiqueta` corta por área, menos filas, o modo `metodo` |
| Nombre de cliente largo (> ~12 caracteres) | Titulares por defecto a 2 líneas, quitan ~40 px al catálogo | `nombre_pie` corto o títulos propios |
| Fundación | Sin slide de inversión (4 slides) | Los campos de precio no aplican; `inversion` se ignora |
| Cliente exige Próximos pasos, Cierre o Impacto | Fuera del formato | Añadir esas slides del canónico y recalcular contadores y campos (`Paso01-03`); documentar la excepción |
| Fechas calendario del cronograma | Aviso | Solo si el usuario lo pide; poner el rango como texto en `fases[].rango` |

## 10. Desviaciones del sistema canónico (deliberadas)

Este formato **no sigue** la secuencia canónica de §6/§4.2; es una variante pedida por el usuario. Se suspende: Objetivos, Programa por módulos, cronograma por sesión, Impacto con estudios (§4.9), Próximos pasos (§4.15 aplica solo si se agrega), Cierre/escalera, Calendario de inicio. El ROI se reemplaza por el módulo opcional de retorno (método o cifras del cliente, sin estudios). Se mantiene todo lo bloqueante de marca, copy y verificación (§4.1, 4.4, 4.8, 4.10, 4.10a, 4.11, 4.12, 4.13, 4.14 en lo que aplica, §10). Los 13 campos canónicos pasan a 7. El titular de portada es una frase-objetivo (no un titular de dolor) y el eyebrow dice «Propuesta de proyecto · Servicio de Habilidades» en vez de «Propuesta formativa»: reflejado el 2026-10-05 en `CLAUDE.md` §4.1a punto 4 y §4.21 y en `plantillas/propuesta-comercial.md`. Si el usuario pide más de lo que cabe en 5 slides, no forzar: proponer el deck canónico.

## 11. Verificación recomendada antes de entregar

1. `generar-habilidades-compacto.py` sin ✗ y con todos los ⚠ leídos.
2. `verificar-propuesta.sh` (incluye las holguras del deck), `verificar-overflow.js` y `verificar-habilidades-compacto.js` en verde.
3. PDF: 7 campos (Fundación: 2), `/AP` horneado en `Programa`, `Notas`, `Entregables`, `Acreditacion`; marcadores en la página correcta; sin residuos de versiones anteriores del insumo.
4. **Revisión independiente** (en el caso base, dos rondas de 6 revisores en paralelo encontraron 71 y 48 hallazgos, varios sustanciales): cifras contra la fuente, cobertura y fidelidad de los entregables, reglas del sistema, visual, AcroForms y lectura como cliente/vendedor.
5. Pendientes para el usuario: quién contrata el licenciamiento, precios, asesora/contacto (el deck no lleva cierre), código, certificado.

## 12. Prueba de aceptación

```bash
python3 scripts/generar-habilidades-compacto.py --datos plantillas/habilidades-compacto-canonico/datos.ejemplo-dusa.json --salida /tmp/prueba-dusa
node scripts/verificar-habilidades-compacto.js /tmp/prueba-dusa/index.html          # 6 slides
python3 scripts/generar-habilidades-compacto.py --datos plantillas/habilidades-compacto-canonico/datos.ejemplo-fundacion.json --salida /tmp/prueba-fund
node scripts/verificar-habilidades-compacto.js /tmp/prueba-fund/index.html          # 5 slides, sin inversión
```
Ambos deben generar sin errores y con todas las holguras en verde. DUSA: 4 avisos esperados (nombre largo de RH-0, «Hacia la semana 24» por confirmar, aval de posiciones por reconfirmar y pasos genéricos) y reproduce `clientes/propuestas/dusa-cai035/` (titular-objetivo, slide de retorno en modo método con posiciones); diferencias deliberadas: en la 3 los rótulos de áreas de cada frente se agrupan distinto (`nowrap` por área), en la 4 el bloque de licenciamiento sube 4 px y en la 5 se alinea el primer título de la 4.ª columna. Fundación: 2 avisos (semana de medición por confirmar y pasos genéricos).

Pruebas de regresión del generador (corridas el 2026-10-05, en el scratchpad de la sesión; no están versionadas): 282 casos negativos del importador/validador sin errores internos; 55 casos del módulo de retorno y del titular (modos inválidos, destino/metas/pasos mal contados, estudios, firmas citadas, URL y «garantizado», «estudio de tiempos» permitido, cifras sin costo hora, nota u origen, áreas inexistentes o repetidas, tipo de dato inválido, aval de posiciones ausente o incompleto, horas por posición, posiciones evitables, valores no finitos, 12 filas, titular de 4 líneas o sin líneas, ids internos visibles, defaults de Fundación) y 45 de la hoja de captura (números ambiguos, fórmulas sin valor, huella de ids, `_control`, origen/nota/aval, archivos que no son xlsx). Si se vuelve a tocar el generador, rehacerlas o versionarlas antes.
