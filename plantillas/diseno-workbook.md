# Plantilla operativa: Workbook del participante

> Documento del **participante**, entregado al **inicio** del programa y enriquecido
> sesión a sesión (documento vivo). Se genera a partir del `programa.md` del cliente y
> se rinde como PDF A4 vertical vía el pipeline `HTML → Chrome headless → PDF`.

> **Pre-requisitos**: `brief.md` con `division: educacion` y `programa.md` ya completo
> según `plantillas/diseno-taller-capacitacion.md` o `plantillas/diseno-curso-diplomado.md`.

---

## 1. Identidad del documento

- **Audiencia**: el participante (no el comprador).
- **Tono**: directo, didáctico, en segunda persona. Sin marketing comercial.
- **Marca**: la oficial — `empresa/marca-visual.md`. Logo `logos/educacion/{BLANCO|NEGRO}.png`.
- **Formato**: A4 **vertical**, ~12–20 páginas según volumen del programa.
- **Idioma**: español. Excepciones: nombres propios de herramientas (Loom, n8n,
  Mentimeter, etc.).

---

## 2. Estructura obligatoria

El workbook **siempre** lleva estas secciones en este orden:

| # | Sección | Páginas |
|---|---|---|
| 1 | Portada | 1 |
| 2 | Contenido del workbook (índice) | 1 |
| 3 | Glosario de términos clave | 2–4 |
| 4 | Una sección por **sesión** o **módulo** (alternables) | 1 por sesión/módulo |
| 5 | Proyecto final / Evaluación de cierre | 1 |

### 2.1 Portada

- Eyebrow `INTEZIA × {{CLIENTE}}` sobre fondo negro.
- Título `WORKBOOK DE CAPACITACIÓN` en Graphit Bold (blanco).
- Subtítulo en cursiva amarilla: `{{Nombre del programa}} · {{Eje temático}}`.
- Caption: sector / contexto del cliente.
- Tres tarjetas-stat: `{{H}} Horas` · `{{M}} Módulos` · `{{P}} Prueba/Proyecto Final`.
- Bloque-callout amarillo: misión del workbook adaptada al programa.
- Tabla `NIVEL · METODOLOGÍA · OBJETIVO · INSTRUCTOR · RESPALDADO POR`.
- Pie de página: `Asesor: {{nombre}} · {{email}} · {{tel}}`.

### 2.2 Contenido del workbook

Índice numerado con códigos `GL` (glosario) + `01..NN` por sección. Los números viven
en una etiqueta naranja, el texto a la derecha. Es navegacional — no índice de
contenido detallado.

### 2.3 Glosario de términos clave

- Cabecera negra ancha con badge `GL` amarillo + título + subtítulo.
- Callout amarillo: por qué este glosario (adaptado al eje temático).
- 8–14 términos, cada uno en un bloque con:
  - `Término` (negrita) + etiqueta de categoría (chip naranja, ej. `IA`,
    `ARQUITECTURA`, `CONECTIVIDAD`, `NEGOCIO`…).
  - Definición precisa, 2–3 líneas.
  - Línea `Ej. {{Cliente}}: ...` — aplicación concreta al sector del cliente.
- Los términos se eligen del **eje temático** del programa. Si el eje es IA → API,
  Webhook, Prompt, JSON, etc. Si es otro eje → términos propios.

### 2.4 Una sección por sesión o módulo

Cada sesión del cronograma (`programa.md §5.2`) → una página de tipo **sesión**.
Cada módulo (`programa.md §5.1`) → una página de tipo **módulo**.

**Página de sesión** (incluye práctica con campo editable):

- Cabecera negra ancha con badge `NN` amarillo + título + subtítulo (tipo de sesión).
- `¿De qué trata esta sesión?` — bajada breve.
- Callout amarillo: `Concepto clave de esta sesión`.
- `Contexto — ¿Cómo lo trabajamos?` — bloque amarillo de 2–4 párrafos
  (la guía narrativa para el participante).
- Bloque `PRÁCTICA N — {{título}}` (cabecera naranja) con instrucciones cortas
  + ancla `MI PROMPT:` + recuadro editable para que el participante escriba.
- `Material de la sesión` — tabla compacta con grabación · presentación · workflow.
- Pie de página: `INTEZIA × {{Cliente}} · {{Programa}} · {{Instructor}} · Pág. N`.

**Página de módulo** (sin campo editable):

- Cabecera idéntica con badge `NN`.
- Objetivo del módulo + tabla compacta con sub-items (1–3).
- `Guía de contexto` (callout amarillo).
- `Contenido visto en el módulo` — bloques con barra naranja izquierda
  describiendo lo trabajado, + filas de material con enlaces.
- Pie de página estándar.

### 2.5 Proyecto final / Evaluación de cierre

Página única que describe el cierre del programa: dinámica, herramienta (Mentimeter,
encuesta EduTrace, defensa de proyecto…), criterios y enlace al artefacto.

---

## 3. Mapeo `programa.md` → workbook

| Origen en `programa.md` | Destino en el workbook |
|---|---|
| §1 Información general (nombre, modalidad, duración) | Portada (subtítulo, stats, tabla META) |
| §4.1 Objetivo general | Portada (fila OBJETIVO) |
| §4.2 Objetivos específicos | Sección de cada módulo (objetivo del módulo) |
| §5.1 Estructura modular (módulo, objetivo instructivo, temas) | Página de módulo |
| §5.2 Desglose instructivo (sesión, temas, estrategias, recursos) | Página de sesión + tabla "Material" |
| §7 Equipo facilitador | Portada (fila INSTRUCTOR) |
| Eje temático del brief | Glosario (selección de términos) y copy contextualizado |
| Cliente / sector del brief | Línea `Ej. {{Cliente}}:` de cada término |

---

## 4. Campos editables (AcroForms)

El participante escribe sus respuestas directamente en el PDF.

- **Marcador canónico**: el texto exacto `MI PROMPT:` aparece justo arriba del recuadro
  editable en cada página de sesión con práctica. El script
  `scripts/agregar-campos-workbook.py` detecta ese marcador y coloca un campo
  multilínea en la coordenada fija que la CSS reserva (`.prompt-box`).
- **Naming**: el primer campo es `MiPrompt`; sucesivos `MiPrompt_2`, `MiPrompt_3`…
  (patrón canónico — ver `scripts/agregar-campo-precio.py`).
- **Una práctica editable por página de sesión** como máximo. Si una sesión tiene
  varias prácticas, cada una vive en su propia página.
- **Tablas de práctica** (mapeo, brainstorms) en v1 son visuales (no editables) —
  el participante imprime o anota desde un visor PDF.

---

## 5. Ciclo de vida — documento vivo

El workbook se regenera **una vez por sesión**. El consultor:

1. **Al inicio del programa**: clona la plantilla canónica, mapea `programa.md` y
   ejecuta `./scripts/generar-workbook.sh <slug>`. Entrega el PDF a los participantes.
2. **Después de cada sesión**: edita la sección correspondiente añadiendo:
   - El bloque `CONTENIDO N` con lo trabajado.
   - Los enlaces de grabación · presentación · workflow.
3. **Re-ejecuta** `./scripts/generar-workbook.sh <slug>` — el PDF se actualiza.

> **Nota**: al regenerar se produce un PDF fillable nuevo. Las respuestas escritas
> por el participante viven en su copia personal — el master del repo no las guarda.
> El workbook es una **guía de referencia permanente**, no un repositorio de
> respuestas.

---

## 6. Reglas duras (no romper)

| Regla | Aplica |
|---|:---:|
| División Educación, logo correcto | ✅ |
| A4 vertical (`@page { size: A4 }`) | ✅ |
| Paleta oficial (negro · amarillo · naranja · blanco), sin colores extra | ✅ |
| Tipografía Graphit (Inter / Poppins como fallback) | ✅ |
| Cabecera negra con badge amarillo en cada sección no-portada | ✅ |
| Pie de página con marca + paginación en cada página excepto portada | ✅ |
| Una práctica con `MI PROMPT:` por página de sesión (no más) | ✅ |
| Glosario con chip naranja de categoría + línea `Ej. {{Cliente}}:` | ✅ |
| Sin tablas con cuadrículas pesadas — usar interlineado y separadores de 1 px | ✅ |
| Sin texto fantasma detrás del `.prompt-box` | ✅ |
| Idioma español (excepciones: nombres propios de herramientas) | ✅ |

---

## 7. Checklist antes de entregar

- [ ] División confirmada (logo Educación correcto, contraste por fondo).
- [ ] Portada con stats reales (Horas / Módulos / Proyecto Final), instructor y asesor.
- [ ] Glosario adaptado al eje temático (≥ 8 términos, cada uno con `Ej. {{Cliente}}:`).
- [ ] Cada sesión del cronograma tiene su página; cada módulo tiene la suya.
- [ ] Cada página de sesión con práctica tiene exactamente un `MI PROMPT:`.
- [ ] Proyecto final / evaluación de cierre presente con su herramienta y enlace.
- [ ] Pie de página INTEZIA × {{Cliente}} · {{Programa}} · Pág. N en todas las páginas.
- [ ] PDF en A4 vertical, no horizontal.
- [ ] Sin placeholders `{{...}}` sin llenar.
- [ ] Campos editables verificados en Adobe Reader y Preview (macOS).

---

## 8. Archivos relacionados

- Plantilla canónica: `plantillas/workbook-canonico/{index.html, workbook.css}`.
- Generador: `scripts/generar-workbook.sh`.
- Inyector de AcroForms: `scripts/agregar-campos-workbook.py`.
- Marca y tokens: `empresa/marca-visual.md`.
- Fuente de contenido: `clientes/propuestas/<slug>/programa.md`.
- Salida por cliente (planos, mismo folder del cliente):
  `clientes/propuestas/<slug>/{workbook.html, workbook.css, workbook.pdf}`.
