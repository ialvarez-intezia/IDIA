# Brief — Venemergencia · Domina Claude en 90 Minutos (CH-009)

## Datos administrativos

- **Cliente**: Venemergencia · empresa venezolana de servicios de emergencia y atención
- **Slug**: `venemergencia-ch009` (distinto de `venemergencia/`, que aloja el CAP-047 · Adopción de Claude en cascada, ya entregado; este es un documento nuevo e independiente para el mismo cliente)
- **División Intezia**: `educacion`
- **Tipo de documento**: Charla (`CH-009` — novena charla del catálogo)
- **Programa**: Domina Claude en 90 Minutos · Masterclass práctica para Venemergencia
- **Eje temático**: dominio práctico de **Claude** (versión gratuita) en una masterclass de 90 minutos, con dos casos de uso aplicados de forma general: elaboración de un **dashboard** y de un **reporte**
- **Naturaleza**: Charla/masterclass **sin propuesta económica** y **sin asesor comercial nombrado** — primer acercamiento práctico, no una venta
- **Fecha del brief**: 2026-08-13
- **Estado**: `Borrador`

## Contacto

- **Asesor/a comercial Intezia**: **no se nombra en el deck** (instrucción explícita del usuario: "no coloques... asesora de ventas") — cierre solo con contacto institucional (Intezia C.A / info@intezia.com), mismo patrón que `dusa` (CH-007).
- **Consultor / Facilitador**: NO se asigna en la propuesta inicial → "Equipo INTEZIA Education" (no inventar nombre).
- **Contacto Venemergencia**: pendiente de confirmar en kick-off.

## Por qué esta masterclass

Venemergencia quiere que su equipo **domine Claude** de forma práctica, no teórica: en 90 minutos, cada participante construye con sus propias manos un dashboard y un reporte usando Claude en su versión gratuita. No es una capacitación extensa ni una venta: es una masterclass de adopción, con foco en soltura real sobre la herramienta.

## Diagnóstico (5 puntos)

1. En una empresa donde los minutos cuentan, armar un reporte o un dashboard a mano sigue tomando tiempo que podría dedicarse a la operación.
2. El equipo tiene curiosidad por Claude, pero no ha tenido una introducción práctica y guiada, con casos reales, para dominarlo de verdad.
3. Sin una sesión estructurada, cada persona aprendería a su ritmo y sin un piso común de buenas prácticas.
4. Claude en su versión gratuita ya resuelve casos de uso cotidianos, como estructurar un dashboard o redactar un reporte, sin costo de licencia.
5. Una masterclass de 90 minutos, con grupo reducido y práctica guiada, es la forma más rápida de instalar ese dominio en el equipo.

## Especificaciones del programa

- **Duración**: 90 minutos (4 módulos)
- **Modalidad**: a decisión del cliente (no se menciona explícitamente en el deck, mismo patrón que `dusa`)
- **Audiencia**: grupo de **15 a 20 personas**
- **Requisito indispensable**: **laptop propia por cada participante** y **VPN activa** para acceder a Claude durante la sesión. Las **cuentas de Claude se crean en vivo, durante la masterclass** (no se piden creadas de antemano).
- **Propuesta económica**: **sin slide `.s-price`** — no se muestra cotización en el deck (instrucción explícita del usuario).
- **Asesor comercial**: **sin mención en el deck** (instrucción explícita del usuario) — cierre solo institucional.
- **Acreditación**: Certificado de participación INTEZIA Education
- **Metodología**: práctica guiada con casos de uso reales (sin slide de metodología ABR independiente — las charlas no la llevan)

## Estructura de la masterclass (4 módulos · 90 min)

1. **Domina las Bases** (20 min) — qué es y qué no es Claude, cómo crear la cuenta gratis (con VPN activa) y prompting efectivo desde el primer intento.
2. **Caso de Uso: Dashboard** (30 min) — construir en vivo, con Claude, un dashboard a partir de datos generales, iterando el diseño con la herramienta.
3. **Caso de Uso: Reporte** (30 min) — estructurar y redactar en vivo un reporte completo con Claude, listo para compartir.
4. **Cierre y Ruta de Práctica** (10 min) — repaso de lo dominado, dudas, ruta para seguir practicando y certificado de participación.

## Impacto / estudios (fuentes reales, §4.9)

Se reutilizan las cifras ya validadas en el sistema (mismas fuentes citadas en `dusa`, `cumbre-andina` y otros decks):

- **Stanford HAI — AI Index Report 2026** (cap. Economía) y **McKinsey — The State of AI 2025**: mejoras de productividad por área de trabajo con IA generativa (Marketing y ventas +50%, Desarrollo de software +26%, Atención al cliente +15%).
- **Anthropic Economic Index 2025**: adopción de IA generativa (78% ya usa IA, 2.6× adopción vs. 2023, 1 de cada 3 organizaciones escala su uso).
- **Hook de cierre**: adaptado al contexto de Venemergencia — en una empresa donde los minutos cuentan, el tiempo perdido armando reportes y dashboards a mano es tiempo que no vuelve; la diferencia no es la herramienta, es saber usarla.

## Notas comerciales

- **Sin propuesta económica en el deck**: no hay slide de cotización ni banner de cortesía/gratuidad; el cierre económico, si aplica, se maneja fuera de la presentación.
- **Sin asesor comercial nombrado**: cierre del deck solo con contacto institucional (Intezia C.A / info@intezia.com), patrón `team-single` igual que `dusa`.
- **Vigencia de la propuesta**: 30 días para coordinar fecha.
- Programa registrado como **CH-009** en INTEZIA Education.

## Notas de diseño

- **Clon técnico**: partido de `dusa` (CH-007), deck canónico de charla ya migrado al CSS compartido (`../_base/styles.css` + `overrides.css` local con el componente de cronograma propio de charlas).
- **Sin slide `.s-orange` (ABR)**: regla vigente — las charlas no llevan metodología ABR como slide independiente.
- **Sin slide `.s-price`**: instrucción explícita del usuario, mismo patrón que `dusa`. Los 5 campos de precio no aplican; `agregar-campo-precio.py` los omite al no encontrar el marker "Propuesta Económica".
- **Sin asesor nombrado**: instrucción explícita del usuario — patrón `team-single`, contacto de cierre solo institucional.
- **Requisito de laptop + VPN + creación de cuentas en vivo**: visible en tres puntos del deck para que quede claro antes de coordinar fecha — (1) el `lead` de portada, (2) la línea `.meta` de la slide de Programa, y (3) el body del Paso 02 de "Cómo arrancamos" (`Paso02Body`, ≤130 chars).
- **Grupo de 15 a 20 personas**: declarado en el eyebrow de portada y en el Paso 01 de "Cómo arrancamos".
- **Sin afirmación de migración de stack (§4.11)**: no aplica — la masterclass no depende del stack tecnológico de Venemergencia, solo del acceso a Claude vía VPN.
- **Sin guion largo (§4.13)** y sin acrónimos sin explicar (§4.12): "VPN" es excepción reconocida (sigla de uso general), no requiere expansión.
