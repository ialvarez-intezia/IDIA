# Brief — Go Pharma (CAP-030 · rediseño 2 fases por área)

---

## Datos administrativos

- **Empresa**: Go Pharma
- **Sector**: Farmacéutico
- **Slug**: `go-pharma`
- **División Intezia**: `educacion`
- **Servicio** (Modelo Intezia, `empresa/tipos-de-documento.md §0`): `habilidades` — es el servicio de capacitación con la estructura de siempre (charla/taller/capacitación/curso/diplomado); la mención a "Fase 1 Detección" dentro de este mismo proyecto es el levantamiento previo a la capacitación, no el servicio de Detección del Modelo Intezia (que es un producto propio, con su propio Reporte Final de 10 secciones).
- **Alianza**: no
- **Tipo de documento**: Capacitación In-Company (`CAP-030`)
- **Eje temático**: Productividad con Claude aplicada a tareas reales, por área — Fase 1 Detección + Fase 2 Habilidades, en un mismo proyecto
- **Fecha del brief**: 2026-08-26 — **rediseño completo**, mismo código `CAP-030`, alcance nuevo
- **Estado**: `Borrador` (reinicia el ciclo de venta con el nuevo alcance)
- **Origen**: instrucciones directas del usuario (chat, 2026-08-26) reemplazando la propuesta original de mayo 2026

## Contacto

- **Solicitante**: María Iribarren (Asesora de ventas — Intezia)
- **Correo**: miribarren@intezia.com
- **Teléfono**: +58 414 0570056

## Qué cambia respecto a la propuesta original

La propuesta original (2026-05-19) era **30 personas en 2 grupos genéricos de 15**, equipo
mezclado de todas las áreas, nivel fundamentals, Claude + Gemini, formato single-fase de 12h.
Esta versión la reemplaza por completo:

- **4 grupos distintos, uno por área** — no equipo genérico.
- **Nivel intermedio** — el equipo ya usa Claude en versión gratuita, no quiere fundamentos.
- **Solo Claude** — Gemini sale del alcance.
- **2 fases en un mismo proyecto**: Fase 1 Detección (diagnóstico por área) → Fase 2
  Habilidades (capacitación con el contenido que arroje la Detección).

## Qué queda fuera de alcance

Go Pharma ya usa sus propios agentes de IA para desarrollo tecnológico — ese tema queda
explícitamente fuera. El foco es 100% capacitación por área.

## Alcance definido por el cliente — 4 grupos, 11 personas

| Área | Personas | Roles |
|---|---|---|
| Administración | 3 | Gerente + 2 especialistas |
| Marketing | 3 | Diseñador + Especialista de Marketing + Community Manager |
| Operaciones y Atención al Cliente | 3 | Alto volumen de generación de reportes — área con mayor potencial de optimización del programa |
| Recursos Humanos | 2 | — |

## Nivel: intermedio, no básico

Ya usan Claude en versión gratuita, así que no quieren "cómo usar la herramienta ni
fundamentos teóricos" — quieren la lógica de uso aplicada a su día a día: cómo cada área
puede optimizar sus procesos y tareas repetitivas con IA (textual del cliente).

## Formato: 4 entrenamientos independientes

No es un taller único — son 4 grupos con su propio programa, cada uno por separado. Es
exactamente la metodología que ya se aplica con otros clientes (ver `ioed/`, `aerocentro/`),
ejecutada en 4 grupos en paralelo, no área por área de forma secuencial forzada.

## Estructura del proyecto (roadmap 2 fases)

- **Fase 1 · Detección** (2 horas por área): Kickoff por área o levantamiento vía formulario
  (tenemos las dos modalidades) para levantar procesos y tareas reales de cada grupo, antes
  de armar el contenido de su sesión de Habilidades.
- **Fase 2 · Habilidades** (10 horas por departamento): el contenido y las prácticas se
  diseñan **a partir de los hallazgos de la Fase 1** — nada genérico. Sí es fijo: una
  introducción al ecosistema completo de Claude (Cowork, Skills, Artifacts, Code) para sentar
  bases sólidas, adaptando después cada componente a los procesos reales de esa área.

> Todo en un mismo proyecto, no propuestas separadas por fase ni por área.

## Especificaciones del programa

- **Duración**: Fase 1 · 2h por área (8h en total, repartidas en 4 sesiones) + Fase 2 · 10h
  por departamento (40h en total) — todo dentro del mismo proyecto CAP-030.
- **Modalidad**: Presencial (continuidad del brief original — confirmar con el cliente si
  cambia dado el nuevo formato por área).
- **Audiencia**: 11 personas en 4 grupos separados por área (ver tabla arriba). Cada grupo
  cursa su propio programa, no se mezclan.
- **Aliado**: ninguno (Capacitación In-Company — acreditación solo INTEZIA).
- **Fecha de inicio**: por confirmar (calendario de kickoffs por área se cierra en el Paso 01).

## Equipo asignado

- **Consultor / Facilitador**: Isaac Rodriguez (continuidad del brief original — confirmar
  disponibilidad para el formato de 4 grupos).

## Propuesta económica

- **Hoja "Inversión por fases"** (`.s-price`, variante de `agregar-campo-precio.py` /
  `FASE_PRICE_FIELDS`, ver `ioed/`): **Fase 1 y Fase 2 cotizadas en la misma hoja**, cada una
  con su propia caja de monto vacía + `PrecioBase` (subtotal auto-calculado) + `Descuento` +
  `PrecioTotal`. Ventas llena ambos montos en Adobe Reader — no hay distinción entre "ya
  definido" y "pendiente de diagnóstico", ambos quedan igual de vacíos.
- **Sin montos de dinero en ningún lado del deck.**
- **Nota de presupuesto** (campo `Notas`, sin cifras): la cotización se estructura para que
  Go Pharma pueda gestionarla dentro del ciclo presupuestario del próximo mes.
- **Referencia interna, no va en el deck**: la propuesta anterior (2 grupos, 12h) se cotizó en
  3150 REF con una tarifa especial (familia de Alejandro). Este alcance nuevo — 4 grupos en
  vez de 2, nivel intermedio en vez de fundamentals, más horas totales — debe cotizarse por
  encima de esa referencia. Decisión de ventas al llenar el AcroForm, no contenido del deck.

## Sobre la recomendación de licencias

Go Pharma pidió explícitamente una recomendación de licencias (cuántas y de qué perfil/plan
por área, ya que el uso de tokens de Marketing no es el mismo que el de Administración u
Operaciones). **Se resuelve aparte, no en este deck** — pendiente como entregable propio.

## Entregables consolidados

- Diagnóstico validado por área (Fase 1), antes de diseñar el contenido de Fase 2.
- Capacidad instalada en cada uno de los 4 grupos, sobre sus propias tareas reales.
- Workbook a la medida por grupo y certificado de participación INTEZIA.
- Introducción común al ecosistema completo de Claude (Cowork, Skills, Artifacts, Code).

## Notas de diseño

- Formato canónico A4 landscape, clonado de `ioed/` (a su vez clon de `aerocentro/`),
  **recortado de 3 a 2 fases**: Fase 1 Detección, Fase 2 Habilidades — sin Etapas
  intermedias, cada fase es una sola etapa.
- **Roadmap en 1 sola página** (no 1 por fase, como en `aerocentro/`/`ioed/`): al ser solo 2
  fases y contenido genérico compartido entre los 4 grupos, cabe todo en un `.rmx-linear` de
  2 nodos + resultado, igual que la página de cierre de fase única que ya usa `ioed/` para su
  Fase 3.
- **Programa (`.s-program`) con 4 tarjetas**, una por área (Administración, Marketing,
  Operaciones y Atención al Cliente, Recursos Humanos) — patrón multi-track (ver memoria
  `multi-track-una-propuesta`), no 4 módulos secuenciales. Cada tarjeta es genérica (Fase 1 +
  Fase 2) porque el contenido real depende del diagnóstico de cada área.
- **Sin Gemini** en ningún lugar del deck — solo Claude.
- **Sin slide ni mención de recomendación de licencias.**
- **Impacto (§4.9)** — fuentes reales:
  - McKinsey, *The economic potential of generative AI: The next productivity frontier*
    (junio 2023): operaciones de clientes +30–45% de productividad sobre el costo de la
    función; marketing +5–15% del gasto total en marketing (~$463 mil millones anuales); IA
    generativa podría automatizar actividades laborales que hoy absorben 60–70% del tiempo de
    los empleados.
  - Brynjolfsson, Li y Raymond, *Generative AI at Work* (NBER Working Paper, 2023): +14% de
    casos resueltos por hora en soporte al cliente al usar un asistente de IA generativa.
- **Nomenclatura**: se usa la nomenclatura vieja (`CAP-030`) en esta propuesta — no `DET-`/
  `CAI-` (nomenclatura nueva reservada a propuestas que parten de la Ficha Comercial Intezia).
- **Beneficios v3, layout ampliado (retrofit 2026-08-28, solo aspecto visual)**: el deck nació
  en v2 (2 tarjetas oscuras + 2 blancas, grid de 240px) y se actualizó al estándar vigente por
  pedido directo del usuario — mismo contenido, mismas horas, sin cambios de texto salvo el
  bullet `•` agregado al inicio de cada línea de Entregables/Valor inmediato (parte del look
  de checklist del formato v3, no un cambio de redacción). Las 4 tarjetas quedan oscuras, el
  grid sube a 570px, tipografía y padding ampliados, y las cajas AcroForm se agrandan de
  158×117pt a 145×355pt con fuente de 10 a 13pt vía `BENEFICIOS_LAYOUT` en
  `customize-go-pharma-cap030.py`. Ver `plantillas/propuesta-comercial.md` → *Layout ampliado*.

## Regenerar el PDF — trío obligatorio, no el par estándar

`FASE_PRICE_FIELDS` en `scripts/agregar-campo-precio.py` está fijo a 3 fases (origen
IOED/CAP-098). Este deck usa solo 2, así que **cada vez que se regenere el PDF** hace falta
un tercer paso además del par estándar, o queda un campo huérfano `PrecioFase3` flotando en
la hoja de precio y el subtotal suma 3 fases en vez de 2:

```bash
./scripts/generar-pdf.sh go-pharma
python3 scripts/customize-acroforms.py go-pharma
python3 scripts/customize-go-pharma-cap030.py "clientes/propuestas/go-pharma/CAP-030 Productividad con Claude por área, en Go Pharma.pdf"
```

El script especial no toca `agregar-campo-precio.py` (compartido con `ioed/` y otros decks de
3 fases) — vive aislado en `scripts/customize-go-pharma-cap030.py`.

## Pendientes

- Confirmar modalidad exacta (se asumió Presencial, continuidad del brief original).
- Confirmar fechas de kickoff/levantamiento por área.
- Recomendación de licencias — entregable aparte, pendiente de construir.
- Tarifa de Fase 1 y Fase 2 — vacías en el PDF, las llena ventas.
