# Brief — Zoom (Innovación · Opción A + Opción B fusionadas)

---

> **Fusión 2026-08-31** (decisión del usuario): este deck combina lo que antes eran 2
> propuestas completas e independientes — INN-001 (Opción A, esta carpeta) e INN-002
> (Opción B, `zoom-innovacion-b/`, que queda intacta, sin uso a partir de esta fusión).
> Zoom ahora evalúa un solo documento con ambas opciones dentro. Ver §"Qué cambió con la
> fusión" más abajo.

## Datos administrativos

- **Empresa**: Zoom
- **Sector**: Servicios / corporativo
- **Slug**: `zoom-innovacion`
- **División Intezia**: `educacion`
- **Servicio (Modelo Intezia)**: `innovacion` — primer piloto de este servicio en el sistema (INN-001). Estructura de deck resuelta con esta propuesta (ver `empresa/tipos-de-documento.md §0` y `CLAUDE.md §4.1a`).
- **Código**: INN-001 (conserva el código original; INN-002 no se reutiliza ni se retira, solo queda sin uso comercial a partir de esta fusión)
- **Eje temático**: Cultura continua de innovación con IA en el ecosistema Google — radar mensual de novedades (Gemini, Google Workspace) + foco variable por área según los objetivos reales del mes.
- **Fecha del brief**: 2026-08-30 (fusionado 2026-08-31)
- **Estado**: Enviada (respetado — ver meta.json)

## Contacto

- **Asesora de ventas**: María Iribarren — +58 414 0570056 — miribarren@intezia.com
- **Contacto cliente**: sin nombre individual asignado aún — el deck se dirige al equipo de Zoom de forma genérica.

## Necesidad detectada

Zoom ya trabaja con Intezia en capacitaciones puntuales por departamento (Legal, RRHH, Comercial, IT, Operaciones). La necesidad ahora es distinta: sostener la adopción de IA en el tiempo, no con un programa cerrado de una sola vez, sino con una cadencia mensual que se ajuste a lo que Google lanza y a las prioridades reales del negocio mes a mes.

## Especificaciones del plan

- **Modelo**: sesiones al mes que se definen y planifican según los objetivos reales de ese mes (no un temario fijo de 3, 6 o 12 meses cerrado de antemano).
- **Opción A**: 3 sesiones al mes. Distribución flexible: mes a mes se decide si es 1 masterclass general + 2 sesiones enfocadas por área, o 3 sesiones enfocadas, según lo que convenga. No se fija de antemano cuántas ni cuáles áreas — eso se define en el kick-off de cada mes.
- **Opción B**: hasta 5 sesiones al mes. Más margen que la Opción A: cubre hasta 5 áreas en el mes, o reemplaza alguna sesión por una mesa de trabajo o espacio de consultoría a demanda.
- La narrativa general del deck (Diagnóstico, Objetivos, Roadmap, Beneficios, Impacto) **no menciona horas** — solo cantidad de sesiones y qué se obtiene en cada etapa. La cifra de horas (6h para A, 10h para B) queda **solo** en las 2 hojas de cotización, donde sí es una cifra comercial concreta.
- **Duración del ciclo**: 3, 6 o 12 meses, a elegir, para cualquiera de las 2 opciones. A mayor permanencia, mayor beneficio en la cuota mensual (2 hojas de cotización, una por opción, cada una con 3 columnas: 3 / 6 / 12 meses, cuota mensual y beneficio por permanencia editables).
- **Modalidad**: online síncrono o presencial, se define en el kick-off de cada mes según el tema y el área convocada.
- **Stack**: ecosistema Google (Gemini, Google Workspace) — Intezia se integra al entorno que Zoom ya usa, no propone migrar de plataforma (CLAUDE.md §4.11).

## Lógica del ciclo mensual (Roadmap del deck)

1. **Kick-off mensual**: se revisan las novedades de Gemini/Workspace del mes y las prioridades reales de Zoom; se define la agenda (masterclass y/o áreas del mes).
2. **Ejecución**: se dictan las sesiones definidas ese mes (3 en Opción A, hasta 5 en Opción B — el roadmap no distingue por opción, queda genérico: "Sesiones del mes").
3. **Medición**: se mide la adopción real de lo visto ese mes y se identifican los focos del siguiente ciclo.
4. El ciclo se repite cada mes durante la duración contratada (3, 6 o 12 meses) — la medición de un mes alimenta la agenda del siguiente.

## Qué cambió con la fusión (2026-08-31)

Antes de esta fecha existían 2 documentos completos: INN-001 (Opción A) en esta carpeta e
INN-002 (Opción B) en `zoom-innovacion-b/`. Por decisión del usuario, se fusionan en un
solo deck de 12 slides (antes 10) que Zoom evalúa de una vez:

1. **Diagnóstico, Objetivos, Beneficios, Impacto, Pasos y Cierre**: sin cambios, ya eran
   idénticos entre A y B.
2. **Programa**: pasa de 1 slide a 2 (una por opción, slides 4 y 5) — cada una en lenguaje
   general, sin cifra de horas fija, con la cantidad de sesiones y qué se obtiene en cada
   una (mismos módulos que ya tenía cada opción por separado).
3. **Roadmap**: sigue siendo 1 sola slide compartida (antes cada documento tenía su propia
   copia idéntica salvo el nombre de la Etapa 2) — la Etapa 2 ya no dice "3 sesiones · 6
   horas" ni "5 sesiones · 10 horas", queda genérica: "Sesiones del mes".
4. **Propuesta Económica**: pasa de 1 slide a 2 (una por opción, slides 9 y 10) — cada una
   tal cual estaba en su documento original (sí mencionan horas, es la sección donde la
   intensidad se cotiza). `agregar-campo-precio.py` ya soportaba nativamente esta
   duplicación (`find_pages_by_marker` detecta ambas páginas con el marcador "Inversión por
   Permanencia" y sufija automáticamente la 2ª instancia con "_2": `Cuota3m_2`,
   `Descuento3m_2`, `Cuota6m_2`, `Descuento6m_2`, `Cuota12m_2`, `Descuento12m_2`,
   `Notas_2`) — no requirió tocar el script para la detección/creación de campos.
5. **INN-002 / `zoom-innovacion-b/` NO se toca**: queda intacta, sin uso comercial a partir
   de esta fusión (no se borra ni se marca "Perdida" — eso es decisión de venta, no
   automática).
6. `scripts/customize-zoom-innovacion.py` (paso 3 del trío, siempre después de
   `customize-acroforms.py`): se actualizó el default de `CierrePaso2` (quitó "6 horas de
   ejecución" → "Ejecución del mes, foco distinto cada vez") y se agregó
   `/NeedAppearances = False` al final (mismo fix aplicado 2026-08-31 en DUSA CH-007/CH-010,
   ver memoria `bug-needappearances-cliente-regenera-campos` — este script propio no
   heredaba el fix de `customize-acroforms.py` porque corre después y lo pisaba).

## Notas internas

- Primera propuesta de servicio Innovación (§4.1a) del sistema — antes marcado "Pendiente" (sin piloto canónico, estructura de deck sin resolver). Este deck se convierte en la referencia a clonar para futuras propuestas de Innovación — incluido el patrón de 2 hojas de cotización en un mismo PDF (ver §"Qué cambió con la fusión").
- Variante de AcroForm de precio: "Inversión por Permanencia" (`CICLO_PRICE_FIELDS` en `scripts/agregar-campo-precio.py`) — 3 columnas de duración de ciclo, cada una con cuota mensual y beneficio por permanencia editables, vacíos para que ventas los complete. Ya soporta múltiples instancias en el mismo PDF (sufijo automático `_N`).
- Base clonada de `cavedatos/` (mono-fase, `../_base/styles.css` + `overrides.css` local, Beneficios v3, Cierre escalera, sin Metodología ABR ni Equipo facilitador expuestos — §4.10a).
- Roadmap (`.s-roadmap`, componente `.rmx-linear`) adaptado de `grupo-osorio/` (single-track, 3 etapas + resultado) para representar el ciclo recurrente Kick-off → Ejecución → Medición → se repite, en vez de fases con fin.
