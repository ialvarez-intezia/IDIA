# Mecánica — Generar un Dashboard de Impacto Edu-Trace

> Cómo producir el dashboard de un cliente desde su `encuesta.csv`. Diseño y lógica:
> `plantillas/dashboard-edutrace.md`. Análogo a `generar-pdf.md` pero **sin AcroForms**
> (el dashboard no es editable por ventas).

---

## 0. Estructura de la carpeta

Cada cliente vive en su subcarpeta bajo `clientes/dashboards/<slug>/`:

```
clientes/dashboards/<slug>/
├── encuesta.csv          ← export del Google Form (CON PII · gitignored)
├── mapeo.json            ← declara qué columna es qué bloque + clave del Bloque C
├── resultados.json       ← SALIDA del procesador (SIN PII · versionable)
├── overrides.css         ← estilos locales (sobre ../../propuestas/_base/styles.css)
├── index-cliente.html    ← deck entregable (salida única)
└── Dashboard de Impacto · <Cliente>.pdf
```

> **Sin deck interno (desde 2026-06-10).** El dashboard tiene una sola salida: la de cara al
> cliente. No se generan `index-interno.html`, `_INTERNO · <Cliente>.pdf` ni `siguiente-venta.md`.

`<slug>`: minúsculas, sin tildes, espacios→guiones (igual que propuestas).

---

## 1. Preparar entradas

1. **`encuesta.csv`**: el export crudo del Google Form, una fila por participante. No se
   reordenan columnas; se usa tal cual lo da Forms.
2. **`mapeo.json`**: declara, por su **header exacto de columna**, qué columna es de qué bloque,
   y la **clave del Bloque C** como `keywords_correctas` (deducidas por razonamiento; §4.18).
   Plantilla en el piloto `clientes/dashboards/apb-group/mapeo.json`. Campos:
   - `capacitacion`: cliente, slug, titulo, codigo, eje, division, facilitador, fecha_cierre.
   - `identidad`: headers de timestamp, nombre, cedula, correo, departamento.
   - `bloque_b` / `bloque_d`: `{col, alias}` por ítem Likert.
   - `bloque_c`: lista de `{col, alias, keywords_correctas, modo}` (`modo`: `todas`|`alguna`).
   - `bloque_e`: lista de `{col, alias}`.

   > Antes de fijar la clave del Bloque C: lee las preguntas. Deduce la respuesta correcta por
   > lógica (ej. «4 elementos de un prompt» → rol, contexto, tarea, formato). **Si dudas,
   > pregunta al usuario** antes de calificar.

---

## 2. Procesar (CSV → resultados.json)

```bash
python3 scripts/edutrace-procesar.py clientes/dashboards/<slug>/
```

Descarta cédula/correo, normaliza Likert, califica el Bloque C contra la clave, calcula el
Índice y sus ejes, segmenta por departamento, arma la lista de participación (sin puntajes) y
agrupa los textos del Bloque E. Imprime un resumen (N, Índice, ejes, % por pregunta C). Valida
ahí mismo que el N y el Índice sean plausibles.

---

## 3. Construir / actualizar el HTML

Claude inyecta los valores de `resultados.json` en `index-cliente.html` (clonando el piloto
APB Group). 10 slides (ver `dashboard-edutrace.md §5`). Reglas de copy honesto (§4.17) y sin
overflow (§4.10). El Bloque E se presenta como «recomendaciones de expansión» de valor.

---

## 4. Generar el PDF (par procesar→render)

```bash
./scripts/generar-dashboard.sh <slug>
```

Re-procesa el CSV (regenera `resultados.json`) y renderiza el PDF con Chrome headless, **sin
AcroForms**. Nombra el entregable `Dashboard de Impacto · <Cliente>.pdf`. No hay paso
`customize` (a diferencia de las propuestas).

---

## 5. Verificar (antes de entregar)

```bash
# Overflow (§4.10)
node scripts/verificar-overflow.js clientes/dashboards/<slug>/index-cliente.html

# PII (§4.16) — debe dar 0 en JSON y HTML de salida
grep -cE "[0-9]{7,9}|@" clientes/dashboards/<slug>/resultados.json
grep -rcE "cédula|c[0-9]{6,9}" clientes/dashboards/<slug>/index-cliente.html
```

Y **revisar visualmente cada slide del PDF** (§4.10): el script terminando sin error no
equivale a PDF correcto. Comprobar: tags medido/percibido correctos, sin afirmaciones de mejora
medida sobre B/D, departamentos con disclaimer de muestra, participación sin puntajes.
