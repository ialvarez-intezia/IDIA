# Spec: Slide Mapa de Calor — Pilotes Perforados CAP-021

**Fecha:** 2026-05-21
**Propuesta:** `clientes/propuestas/pilotes-perforados/`
**Inserción:** entre slide 09 (Beneficios) y slide 10 (Impacto)

---

## Qué se construye

Una slide nueva de tipo "Tabla de Calor" que convierte el entregable principal del diagnóstico en una visualización accionable. Se inserta como slide 10 (el total pasa de 13 a 14 slides). Todos los contadores de slides 10–13 suben en 1.

---

## Diseño aprobado

**Layout:** fondo blanco, borde negro de 12px a la izquierda (igual que `s-goals` y `s-benefits`).

**Header:**
- Eyebrow: `07 · Mapa de Calor`
- Título: `Dónde automatizar <span class="hl">primero</span>.` (highlight dorado)

**Tabla — 6 columnas con `table-layout: fixed`:**

| Columna | Ancho | Contenido |
|---|---|---|
| Proceso / Tarea | auto | Nombre del proceso con `<strong>` en palabra clave |
| Puntuación | 128px | 3 filas: Impacto · Esfuerzo · Riesgo, cada una con pill coloreada |
| Herramienta | 158px | 2 `tool-tag` (chips gris claro) con las herramientas recomendadas |
| Plazo | 100px | Rango de semanas + sublabel "implementación" |
| Frecuencia / Manual | 148px | Cadencia + horas manuales actuales en sublabel |
| Prioridad | 104px | Badge negro/dorado (Alta) o naranja (Media) |

**Separadores de área:** filas `tr.area-row` con `colspan="6"`, fondo negro, texto dorado, `▸` naranja como prefijo. Áreas: Procura · Cuentas por Pagar (CxP) · Finanzas · Licitaciones.

**Escala de color de pills:**
- Dorado `#F4BA1A`: Impacto Alto / Esfuerzo Bajo / Riesgo Bajo (favorable)
- Naranja claro `#F9C980`: nivel Medio
- Naranja `#E58423` + texto blanco: Esfuerzo Alto / Riesgo Alto (atención)

**Leyenda:** franja inferior con escala de colores + significado de badges de prioridad.

---

## Datos de los 8 procesos

| Área | Proceso | Impacto | Esfuerzo | Riesgo | Herramienta | Plazo | Frecuencia / Manual | Prioridad |
|---|---|---|---|---|---|---|---|---|
| Procura | Seguimiento de órdenes de compra | Alto | Bajo | Bajo | Power Automate · Sheets IA | 2–4 sem | Diario · 1–2 h | Alta |
| Procura | Solicitud de cotizaciones a proveedores | Alto | Bajo | Bajo | Gemini · ChatGPT | 1–2 sem | Semanal · 2–3 h | Alta |
| CxP | Reconciliación automática de facturas | Alto | Bajo | Medio | Power Automate · Excel IA | 3–5 sem | Mensual · 4–6 h | Alta |
| CxP | Registro y categorización de pagos | Medio | Bajo | Bajo | Gemini · Sheets IA | 1–2 sem | Diario · 30–45 min | Alta |
| Finanzas | Generación de reportes mensuales de cierre | Alto | Medio | Bajo | Gemini · Power BI | 3–6 sem | Mensual · 6–8 h | Alta |
| Finanzas | Alertas de desviación presupuestal | Medio | Medio | Bajo | Power Automate · Sheets IA | 4–8 sem | Semanal · 1–2 h | Media |
| Licitaciones | Elaboración y revisión de pliegos | Alto | Alto | Medio | Claude · ChatGPT | 6–10 sem | Por proyecto · 8–16 h | Media |
| Licitaciones | Seguimiento de contratos activos | Medio | Bajo | Bajo | Notion IA · Drive IA | 2–4 sem | Semanal · 1–2 h | Alta |

> Estos valores son estimados de referencia para el deck de venta. El diagnóstico real los reemplazará con datos de Pilotes Perforados.

---

## Cambios en `index.html`

1. Insertar la nueva `<section class="slide s-heatmap">` después del cierre de `<!-- 9 · Beneficios -->`.
2. Actualizar contadores de slides 10–13: `10/13 → 11/14`, `11/13 → 12/14`, `12/13 → 13/14`, `13/13 → 14/14`.
3. Agregar estilos `.s-heatmap` en `styles.css` (o inline en `<style>` dentro del HTML si se prefiere contenerlo).

---

## Cambios en `styles.css`

Agregar al final de `styles.css`:

- `.s-heatmap` — layout base (fondo blanco, borde negro izquierdo, padding igual a `s-goals`)
- `table.hm` + colgroup — tabla con `table-layout: fixed`
- `tr.area-row td` — separadores de área
- `tr.proc-row td` — filas de proceso
- `.score-pills`, `.pill-row`, `.pill-letter`, `.pill` — columna de puntuación
- `.tool-tag` — chips de herramienta
- `.badge-alta`, `.badge-media` — badges de prioridad
- `.hm-legend` — franja de leyenda inferior

---

## Restricciones

- Altura de fila de proceso: 49px — no aumentar para evitar overflow (§4.10).
- Textos de proceso: máx ~55 caracteres para no romper en 3 líneas.
- No agregar una novena fila sin reducir la altura de las existentes.
- Los datos de herramientas/plazos/frecuencias son placeholders — el campo no es AcroForm; el equipo los editará directamente en HTML antes de entregar.
