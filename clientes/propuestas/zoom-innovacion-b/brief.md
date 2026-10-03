# Brief — Zoom (Innovación · Opción B)

---

## Datos administrativos

- **Empresa**: Zoom
- **Sector**: Servicios / corporativo
- **Slug**: `zoom-innovacion-b`
- **División Intezia**: `educacion`
- **Servicio (Modelo Intezia)**: `innovacion` — segunda propuesta del servicio, clon de
  `zoom-innovacion/` (INN-001, Opción A) escalado a Opción B. No modifica la carpeta
  original: son dos propuestas independientes que Zoom evalúa en paralelo.
- **Código**: INN-002
- **Eje temático**: Cultura continua de innovación con IA en el ecosistema Google — radar
  mensual de novedades (Gemini, Google Workspace) + hasta 5 áreas o mesas de trabajo y
  consultoría, según los objetivos reales del mes.
- **Fecha del brief**: 2026-08-30
- **Estado**: Borrador

## Contacto

- **Asesora de ventas**: María Iribarren — +58 414 0570056 — miribarren@intezia.com
- **Contacto cliente**: sin nombre individual asignado aún — el deck se dirige al equipo de Zoom de forma genérica.

## Necesidad detectada

Misma que INN-001 (Opción A): Zoom ya trabaja con Intezia en capacitaciones puntuales por
departamento. La necesidad es sostener la adopción de IA en el tiempo con una cadencia
mensual. Esta propuesta ofrece una segunda configuración de intensidad para que Zoom evalúe
ambas antes de decidir.

## Especificaciones del plan

- **Modelo**: igual a INN-001 — sesiones al mes que se definen y planifican según los
  objetivos reales de ese mes (no un temario fijo cerrado de antemano).
- **Opción B**: 10 horas al mes · 5 sesiones de 2 horas. Más margen que la Opción A: cubre
  hasta 5 áreas en el mes, o reemplaza alguna sesión por una mesa de trabajo o espacio de
  consultoría a demanda, según lo que convenga. La combinación se decide en el kick-off
  mensual, no de antemano.
- **Duración del ciclo**: 3, 6 o 12 meses, a elegir. A mayor permanencia, mayor beneficio en
  la cuota mensual (misma hoja de cotización "Inversión por Permanencia" que INN-001, con 3
  columnas: 3 / 6 / 12 meses, cada una con cuota mensual y beneficio por permanencia
  editables — los montos de la Opción B son mayores que los de la A por el mismo servicio,
  ventas los define caso por caso, los campos quedan vacíos igual).
- **Modalidad**: online síncrono o presencial, se define en el kick-off de cada mes.
- **Stack**: ecosistema Google (Gemini, Google Workspace) — igual criterio que INN-001
  (Intezia se integra al entorno que Zoom ya usa, CLAUDE.md §4.11).

## Lógica del ciclo mensual (Roadmap del deck)

Igual estructura que INN-001 (Kick-off → Ejecución → Medición → se repite). Único cambio:
la Etapa 2 · Ejecución pasa de "3 sesiones · 6 horas" a "5 sesiones · 10 horas".

## Diferencias respecto a INN-001 (Opción A)

Por decisión explícita del usuario (2026-08-30): Diagnóstico, Objetivos, Beneficios,
Impacto, Próximos pasos y Cierre son **iguales** a INN-001 (mismo cliente, mismo problema de
fondo, mismo mensaje). Solo cambian:
1. Slide de Programa: 5 módulos (Masterclass + 4 sesiones/mesas de trabajo) en vez de 3.
2. Roadmap, Etapa 2: "5 sesiones · 10 horas" en vez de "3 sesiones · 6 horas".
3. Slide de Precio: `price-intro` y "Cómo se arma cada mes" mencionan Opción B (10h/5
   sesiones) en vez de Opción A.

## Notas internas

- Reusa la variante de AcroForm de precio "Inversión por Permanencia"
  (`CICLO_PRICE_FIELDS` en `scripts/agregar-campo-precio.py`) sin cambios — ya existe desde
  INN-001, no requirió tocar el script.
- Base clonada de `zoom-innovacion/` completa (`cp -r`), no de `cavedatos/` — más simple que
  reconstruir desde el canónico de Habilidades, ya que INN-001 ya resolvió todo el esquema
  de Innovación (roadmap cíclico, cotización por permanencia, Beneficios v3, Cierre
  escalera). Ver `empresa/tipos-de-documento.md §0` y memoria persistente
  `piloto-innovacion-inn001-zoom`.
