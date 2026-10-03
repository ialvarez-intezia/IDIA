# Brief — Alianza Team · Fundamentals con logros inmediatos (CAP-095)

> **REEMPLAZO COMPLETO** (2026-09-02) de la versión anterior de este documento
> (2026-08-05). La versión anterior — 2 fases (Diagnóstico + Capacitación a la medida),
> 25 personas de I+D (7 líderes + 18 colaboradores), roadmap fork, Mapa de Calor,
> Metodología ABR, Beneficios formato viejo — se descarta entera. `alianza-team/` (CAP-094,
> versión masiva del mismo cliente, 95 colaboradores) **queda intacta, sin tocar**.

## Instrucción del usuario y preguntas resueltas

El usuario pidió mejorar CAP-095 con un alcance completamente distinto: capacitación para
**solo 3 personas**, de fundamentos a resolver problemas, con **Google, Claude, n8n y
GCP** (corrigió explícitamente: no es "Gemini", es "Google"). Recomendó servicio
`habilidades`. No sabe a qué se dedican esas 3 personas — pidió referirse a ellas como
"miembros de Alianza Team". Se preguntó y se confirmó:

1. **Alcance del cambio**: reemplazar CAP-095 completo (no crear código nuevo).
2. **Área de las 3 personas**: mantener contenido genérico, sin especificar área ni casos
   reales de un departamento — se levantan en el arranque.
3. **Duración**: capacitación personalizada breve — se concretó en 4 módulos / 8h (uno por
   herramienta), siguiendo el patrón de capacitaciones personalizadas recientes del sistema
   (dhl-cerebro-digital, grupo-ferrara-cai007).
4. **Modalidad**: el usuario pidió explícitamente **no mencionarla** en el deck — queda sin
   definir, a confirmar en el arranque.
5. **Encuadre**: el usuario aclaró que esto es **"Fundamentals con logros inmediatos"** —
   nivel introductorio y práctico, no dominio experto; cada módulo cierra con un logro
   inmediato aplicable en esa herramienta, no solo teoría.

## Datos administrativos

- **Cliente**: Alianza Team (mismo cliente de CAP-094, multinacional de negocios de valor
  agregado — grasas, aceites, food services, retail).
- **Slug**: `alianza-team-cap095` (sin cambios — se reemplaza el contenido, no la carpeta).
- **División Intezia**: `educacion`
- **Servicio** (Modelo Intezia): `habilidades` — capacitación personalizada, sin fase de
  diagnóstico (a diferencia de la versión anterior de este mismo documento y de CAP-094).
- **Alianza**: no — "Alianza Team" es el nombre de la empresa cliente, no una alianza
  comercial de Intezia con un tercero.
- **Código**: `CAP-095` (se mantiene; no se renombra a CAI- pese a la convención vigente
  desde 2026-08-30, porque el usuario pidió mejorar el documento existente, no crear uno
  nuevo — mismo criterio de "no retroactivo" del resto del sistema).
- **Eje temático**: Fundamentals de Google, Claude, n8n y GCP, con un logro inmediato por
  herramienta, para 3 miembros de Alianza Team.
- **Fecha del brief**: 2026-09-02
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
  (misma asesora de cuenta que CAP-094/CAP-095 original — sin cambios).
- **Participantes**: 3 miembros de Alianza Team, sin nombres ni área específica — el deck
  no los identifica más allá de "los 3 participantes" / "miembros de Alianza Team".

## Restricciones de copy

1. **Sin modalidad**: ninguna mención a Presencial/Online/Híbrido en ningún lugar del deck
   (portada, Programa, Cronograma, Notas, Próximos pasos) — instrucción explícita del
   usuario, queda para el arranque.
2. **Sin casos reales de área específica**: el contenido de cada módulo se queda a nivel de
   fundamentos de herramienta y "logro inmediato" genérico — no se inventan procesos de
   I+D ni de ninguna otra área, porque no se sabe a cuál pertenecen los 3 participantes.
3. **Sin presupuesto** ni condiciones de pago (§4.15) — cotización vacía, la llena ventas.
4. **§4.11**: no se afirma que Alianza Team migra o adopta un nuevo stack — Google, Claude,
   n8n y GCP son las herramientas que el cliente ya pidió dominar.
5. **"Google" no "Gemini"**: corrección explícita del usuario — todo el deck dice "Google",
   nunca "Gemini" como nombre de la primera herramienta.

## Notas de diseño

- Migración estructural completa: de `styles.css` local (legacy, sin `_base`, 14 slides con
  roadmap fork + Mapa de Calor + Metodología ABR + Beneficios viejo) a
  `../_base/styles.css` + `overrides.css` (patrón vigente). El `styles.css` legacy se
  eliminó de la carpeta — ya no se usa.
- Estructura adaptada del patrón de capacitación personalizada más reciente del sistema
  (`dhl-cerebro-digital/`, `grupo-ferrara-cai007/`): 1 slide de cronograma por sesión
  (componente `.ruta`), Beneficios v3, Cierre escalera. 13 slides (4 sesiones, no 3, porque
  son 4 herramientas).
- **Impacto (§4.9)**: se reutilizan las mismas fuentes reales ya citadas en
  dhl-cerebro-digital/grupo-ferrara-cai007 (Stanford HAI — AI Index Report 2026, McKinsey —
  The State of AI 2025, Anthropic Economic Index 2025) — datos generales de productividad
  con IA, aplicables al mismo eje temático (fundamentals de herramientas de IA), no
  específicos de una audiencia que justifique una nueva búsqueda.
- **Nuevo script propio**: `scripts/customize-alianza-team-cap095.py` (Cierre escalera +
  Beneficios v3 con fondo oscuro) — el documento anterior no tenía script propio porque
  usaba el formato viejo de Beneficios y un Cierre fijo sin escalera.
- **PDF anterior eliminado** (`CAP-095 Nivelación en Inteligencia Artificial.pdf`, de la
  versión de 25 personas) — se regenera desde cero con el nuevo contenido y nombre de
  archivo.

## Ajuste 2026-09-04 — de 4 sesiones de 2h a 2 sesiones de 4h

El usuario pidió: *"vamos a mejorar la propuesta CAP-095 haciendo esto: aumentaría el
número de horas, que sean dos sesiones de 4 horas c/u"*. Se mantienen las 8h totales y las
4 herramientas (Google, Claude, n8n, GCP); cambia solo la distribución: de 4 módulos/sesiones
de 2h (uno por herramienta) a **2 módulos/sesiones de 4h** (dos herramientas por sesión).

1. **Agrupación de herramientas por sesión**: Sesión 1 = Google + Claude (fundamentos y
   prompting); Sesión 2 = n8n + GCP (automatización, conectando las 4 herramientas). Esta
   agrupación **no fue confirmada explícitamente por el usuario** — se infirió del
   agrupamiento que ya usaba el Cierre escalera del propio deck (Fundamentals de Google y
   Claude como un paso, automatizaciones como pasos posteriores). Si el usuario prefiere otra
   combinación (p. ej. Google+n8n / Claude+GCP), es un ajuste de contenido, no estructural.
2. **Slides**: 13 → 11 (2 slides de Cronograma en vez de 4; el resto de la numeración se
   recorre).
3. **Programa**: 2 módulos en vez de 4, cada uno con su propio `.obj` y 4 `.topics` (temas de
   ambas herramientas + logro inmediato combinado).
4. **Cronograma**: cada sesión usa un solo timebar de 4 segmentos (240' = 4h), no dos
   timebars separados — mismo patrón usado en DHL Fase 2 (varias herramientas en una sola
   sesión larga).
5. Duración en Propuesta Económica actualizada a "8 horas en total · 2 sesiones de 4 h · 3
   participantes."

## Pendientes

- Confirmar nombres/roles/área real de los 3 participantes (para personalizar casos reales
  en el arranque, si se desea).
- Confirmar modalidad (Presencial / Online síncrono / Híbrida).
- Confirmar fechas tentativas de las 2 sesiones.
- Confirmar presupuesto indicativo.
- Confirmar con el usuario si la agrupación Google+Claude / n8n+GCP es la deseada (ver
  Ajuste 2026-09-04, punto 1).
