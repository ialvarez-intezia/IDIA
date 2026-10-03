# Brief — Good Latam · Administración + Digital (CAI-010)

> **Fusión de dos propuestas (2026-09-09)** — instrucción explícita del usuario. Este
> documento reemplaza el brief anterior de CAI-010 ("Automatización de Creación, Fase 1 de
> 3"). Ver historial de decisiones abajo.

## Instrucción del usuario y decisiones resueltas (2026-09-09)

1. **Origen**: el usuario pidió juntar en una sola propuesta lo que hasta ahora eran dos
   documentos separados del mismo cliente: `good-latam/` (CAP-109, Administración) y esta
   misma CAI-010 (entonces "Automatización de Creación"). Adjuntó de nuevo el documento "GOOD
   _ PROCESO DE GRILLAS.pdf" — el mismo ya usado para construir CAI-010 — llamándolo ahora
   "procesos de digital".
2. **¿"Digital" es "Creación"?** Confirmado con el usuario: **sí, es la misma área**, solo
   cambia el nombre. Se reutilizó el contenido ya diseñado (4 sesiones/8h, auditoría +
   automatización del proceso de grillas con Gemini/AI Studio/Apps Script) tal cual, solo
   renombrando "Creación" → "Digital" en todo el deck, `programa.md` y `acroforms.json`.
3. **Código destino**: el usuario eligió reemplazar una de las dos propuestas existentes en
   vez de crear una tercera. Entre las dos, confirmó **CAI-010** como la que sobrevive
   (serie de código más reciente, título de PDF ya genérico "Escalar Good Latam"). `CAP-109`
   (`clientes/propuestas/good-latam/`) **queda intacta como historial**, sin tocarse ni
   enlazarse desde aquí.
4. **Compras**: confirmado **fuera por completo** de esta propuesta (no se menciona en ningún
   lugar del deck) — mismo criterio ya aplicado al acotar CAP-109 a un solo departamento el
   2026-09-01. Sigue como posible propuesta futura si el equipo comparte su documentación de
   proceso, pero no en este documento.
5. **Precio**: confirmado **columna única estándar** ("Propuesta Económica", el mismo patrón
   que ya usaba CAP-109 para Administración) — se retira el patrón "Inversión por fases"
   (amcor) que tenía CAI-010 para Creación/Compras/Digital como fases diferidas. Un solo
   monto para Administración + Digital juntas.
6. **Administración**: contenido reutilizado **tal cual** de CAP-109 (Fundamentals 4h +
   Auditoría y Desarrollo 6h, 5 sesiones/10h) — sin cambios de fondo, solo renumeración de
   slides al fusionar.
7. **Lineamientos de horas** (mensaje del usuario a mitad de esta misma sesión, aplica en
   general, no solo aquí): Habilidades = 8-12h mientras el alcance sea de hasta 5 procesos, +4h
   por proceso adicional. Administración (1 proceso central, 10h) y Digital (1 proceso —el de
   grillas—, 8h) ya cumplen este lineamiento sin necesidad de ajuste. Ver memoria
   `lineamientos-horas-deteccion-habilidades.md`.

## Datos administrativos

- **Cliente**: Good Latam · agencia de marketing de 12 personas
- **Naturaleza**: Capacitación in-company · **2 áreas en un solo documento y un solo monto**:
  Administración (Fundamentals + Auditoría y Desarrollo) y Digital (auditoría + automatización
  del proceso de grillas)
- **Slug**: `good-latam-cai010`
- **División Intezia**: `educacion`
- **Servicio**: `habilidades` — ambas áreas siguen el patrón ABR (auditoría antes de
  construir), no Detección independiente con Reporte Final como producto propio.
- **Eje temático**: fundamentos de IA + auditoría y automatización de procesos reales, con
  Gemini y el ecosistema Google Workspace (Google AI Studio, Google Apps Script), para
  Administración y Digital de una agencia de marketing
- **Fecha del brief**: 2026-09-09 (fusión; brief original de CAI-010: 2026-09-04)
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422-3355505 · vrubio01@intezia.com
- **Contacto de referencia en Good Latam**: por confirmar

## Estructura del proyecto — un solo programa, cotizado completo

### Administración (idéntico a CAP-109, sin cambios)

- **Fundamentals**: 2 sesiones de 2h · 4h — qué es la IA, cómo funciona y cómo mejora el
  trabajo diario (Excel, Profit, procesos administrativos).
- **Auditoría + Desarrollo**: 3 sesiones de 2h · 6h — se audita el proceso contable/
  administrativo y se construye la automatización priorizada.
- **Total Administración**: 5 sesiones de 2h · 10 horas académicas.

### Digital (idéntico al contenido de "Creación" en la CAI-010 original, solo renombrado)

12 pasos documentados del proceso de grillas, plataformas Basecamp + Google Sheets, periodo
estimado 15 días (fuente: "GOOD _ PROCESO DE GRILLAS.pdf"):

1. Configuración del To-Do y cronograma (Social Media Manager)
2. Redacción de contenido (Community/Content Manager)
3. Revisión de contenido y aprobación para diseñar (Social Media Manager)
4. Diseño y paso de artes al equipo (Diseñador Gráfico)
5. Revisión final interna (Social Media Manager)
6. Carga del contenido en Basecamp (Asistente de Cuentas)
7. Envío al cliente (Asistente de Cuentas)
8. Revisión y feedback del cliente (Cliente)
9. Cambios solicitados por el cliente (Ejecutiva de Cuentas)
10. Ejecución de ajustes (Community/Content Manager y Diseñador)
11. Actualización de contenido en Basecamp (Ejecutiva de Cuentas)
12. Aprobación final (Ejecutiva de Cuentas)

**Clasificación usada para diseñar el programa** (sin cambios respecto al brief original):
- Automatizables de punta a punta: 1, 6, 7, 9, 11, 12
- Asistibles con IA, no reemplazables (criterio creativo humano): 2, 4, 10
- Puntos de aprobación, 100% humanos (no se automatizan): 3, 5, 8

- **4 sesiones de 2h · 8 horas académicas** (Diagnóstico y Fundamentals aplicados → Arranque
  automatizado + redacción con Gemini → Automatización de Basecamp → Feedback estructurado +
  integración final).

### Total del programa combinado

**9 sesiones de 2h · 18 horas académicas** (Administración 10h + Digital 8h), cotizadas en un
solo monto.

## Restricciones de copy (heredadas de ambos briefs originales, sin cambios)

1. **Sin inventar procesos de Compras** — no se menciona en este documento.
2. **Gemini, no Claude; AI Studio, no n8n** — todo asistente de IA (Digital) se construye en
   Google AI Studio sobre Gemini. Nunca se menciona Claude, "Cerebro Digital", n8n ni "Gema
   (Gem)". Nunca se sugiere que Good Latam cambie de herramienta (§4.11).
3. **No prometer automatizar los puntos de aprobación humano** del proceso de Digital (pasos
   3, 5, 8).
4. **Basecamp condicionado**: toda mención a su automatización (Sesión 3 de Digital,
   Objetivo específico 4, Entregables, Notas) incluye "sujeto a la disponibilidad de su API".
5. **Sin presupuesto** ni condiciones de pago en el deck (§4.15) — cotización vacía, la llena
   ventas.
6. **§4.12**: "Google AI Studio" y "Google Apps Script" son nombres de producto, no siglas —
   no requieren expansión. "API" tampoco (excepción de catálogo técnico, §4.12 punto 4).

## Notas de diseño

- **Estructura fusionada (17 slides)**: Portada → Diagnóstico → Objetivos → Programa·
  Administración → Cronograma·Administración (×2) → Programa·Digital → Cronograma·Digital
  (×4) → Roadmap (2 etapas: Administración | Digital + resultado) → Beneficios v3 → Impacto →
  Precio (columna única) → Próximos pasos → Cierre escalera.
- **Roadmap**: pasa de 3 nodos (Creación activa / Compras a definir / Digital a definir) a 2
  nodos (Administración | Digital), ambos ya con contenido real y cotizados juntos — mismo
  patrón `.rmx-linear` de 2 etapas que ya usaba CAP-109 internamente para sus propias 2
  etapas (Fundamentals → Auditoría/Desarrollo).
- **Impacto**: se combinan las barras de ambos decks originales — Administración/finanzas
  (-20-30%), Marketing y contenidos (+50%, aplica a Digital) y Operaciones con IA agéntica
  (+5-15%, compartida por ambos, una sola vez). Gauge 57%/44% + chip 25% (los 3 ya estaban
  verificados en ambos decks originales, mismas fuentes McKinsey/Stanford/Anthropic).
- **styles.css**: se mantiene el archivo local completo (heredado de `good-latam/styles.css`
  al clonar CAI-010 originalmente). Se retiró el bloque final "Inversión por fases (CAI-010)"
  (~240 líneas) que sobrescribía el `.s-price` estándar ya presente en el mismo archivo —
  con eso retirado, el `.s-price` genérico vuelve a aplicar limpio, igual que en `good-latam/`.
- **scripts/customize-good-latam-cai010.py**: se quitó toda la lógica de `PrecioFaseN`
  (eliminar Fase2/3 huérfanas + JS de subtotal) — el marcador nuevo nunca crea esos campos.
  Se mantiene Cierre escalera + Beneficios v3 (textos actualizados para reflejar ambas áreas).

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh good-latam-cai010
python3 scripts/customize-acroforms.py good-latam-cai010
python3 scripts/customize-good-latam-cai010.py "clientes/propuestas/good-latam-cai010/<PDF generado>.pdf"
```

## Bug encontrado y corregido durante la fusión (2026-09-09)

El texto del Paso 1 del Cierre escalera ("Fundamentos y proceso de grillas auditados", 43
caracteres) se cortaba en la caja más pequeña de la escalera (`.stair-1`, 50px de alto) — al
combinar los dos "Paso 1" originales (CAP-109: "Fundamentos de IA aprendidos" · CAI-010:
"Proceso auditado y priorizado", ambos ~30 caracteres) el texto combinado quedó demasiado
largo. `verificar-overflow.js` no lo detecta (mismo caso que
`bug-programa-acroform-cobertura-larga`: el contenido de las cajas AcroForm se hornea después
del render HTML que audita el script). Se acortó a "Fundamentos y proceso auditados" (32
caracteres) en `index.html` y en `CIERRE_FIELDS` de `scripts/customize-good-latam-cai010.py`,
y se regeneró el PDF completo (no basta con re-correr el customize: el campo ya existía y el
script tiene guarda "si ya existe, no se reagrega").

## Pendientes

- Recibir el documento de proceso de Compras si se retoma como propuesta futura (fuera de
  este documento).
- Confirmar si Good Latam tiene o puede conseguir acceso a la API de Basecamp (Digital).
- Resolver la discrepancia de nombre/logo "goodman" vs. "Good Latam" (heredado, sin resolver).
- Confirmar contacto/cargo de referencia en Good Latam para este proyecto combinado.
- Confirmar fechas tentativas de las 9 sesiones (5 Administración + 4 Digital).
- Confirmar presupuesto indicativo del programa combinado (18h).
- `clientes/propuestas/good-latam/` (CAP-109) queda como historial — no editar ni enlazar
  desde ningún flujo activo salvo instrucción explícita del usuario.
