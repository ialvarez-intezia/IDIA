# Brief — Luis Sosa, Consultor independiente · Cerebro Digital individual (CAI-029)

## Datos administrativos

- **Empresa/Cliente**: Luis Sosa (Consultor independiente, mentor y asesor organizacional)
- **Slug**: `luis-sosa-cerebro-digital`
- **División Intezia**: `educacion` — cliente corporativo/profesional (mentor de directivos
  de empresas privadas), sin ambigüedad de división a diferencia de casos sin fines de lucro.
- **Servicio (§4.1a)**: `habilidades` — la Ficha confirma explícitamente en el Bloque F que
  "el caso no encaja en los 4 servicios estándar... lo que se está cotizando es el producto
  Cerebro Digital individual". Cerebro Digital es formato Habilidades-adjacente (código
  `CAI-`), no un 5to servicio — mismo criterio ya aplicado en `dhl-cerebro-digital/`,
  `banco-plaza-cerebros-digitales/` y `amv-tecnologia-cerebro-digital/`.
- **Tipo de documento**: Capacitación In-Company (`CAI-029`, dado directo por el usuario).
- **Fuente**: Ficha de Levantamiento (`Levantamiento_Luis_Sosa_Consultor_independiente_2026-09-25.pdf`,
  elaborada por Verónica Rubio, fecha de registro 2026-09-24) + documento propio del
  cliente (`fydeh Programa Mentoring 27-02-26.pdf`, su deck de mercadeo del programa de
  mentoring FYDEH).
- **Base estructural**: clonado de `banco-plaza-cerebros-digitales/` (CAI-025) por ser el
  precedente más reciente y completo en estándares de Habilidades (descuento urgente, ROI,
  garantía 30-60-90 + `.s-followup`), pero **reestructurado de patrón ligero a patrón
  profundo** (ver Decisiones de diseño §1) — la mayoría del contenido de cada slide se
  reescribió desde cero para Luis.

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com.
- **Contacto cliente**: Luis Sosa Brito (Lsosa2358@gmail.com, 0424-513.91.91, según su propio
  material FYDEH). Universo: 1 persona (él mismo).

## Qué pide el cliente (mensaje directo del usuario, 2026-09-25)

- Reunión con Luis Sosa, consultor mentor independiente que trabaja de la mano con dueños y
  directivos de empresas importantes en Venezuela: programas activos con **Farmatodo, IESA,
  Río y Canguro**, entre otros. Vio en vivo el Cerebro Digital en Claude Code durante la
  reunión y quedó entusiasmado, quiere avanzar.
- Documentos adjuntos: la Ficha de Levantamiento (a partir de la transcripción de la
  reunión) + material que Luis compartió por su cuenta.
- **Restricción explícita del enfoque (verbatim, bloqueante)**: *"este caso es un consultor
  individual, no una empresa con equipo — la propuesta de cerebro digital debe estar
  orientada a automatizar sus propios procesos (cotización de propuestas, diferenciación de
  tarifas por tipo de hora, diseño instruccional), no a un despliegue corporativo."*

### Nota de discrepancia en documentos (transparencia, no bloqueante)

El mensaje del usuario describe 4 documentos propios de Luis: "su resumen profesional,
resumen de su firma/consultoría, información de su programa de mentoring y el esquema de
talleres/educación que ya tiene armado". **Solo se recibió 1**: `fydeh Programa Mentoring
27-02-26.pdf` (su deck de mercadeo del programa de mentoring). Los otros 3 no llegaron como
adjunto. Se avisó al usuario; esta propuesta se construyó con lo disponible (Ficha +
FYDEH), sin inventar contenido de los documentos faltantes.

## Contenido de la Ficha de Levantamiento (2026-09-25, Verónica Rubio)

- **Servicios de interés**: "Aun no definido / a la expectativa".
- **Universo**: 1 persona (Luis Sosa mismo).
- **Bloque F**: confirma que el caso no encaja en los 4 servicios estándar — lo cotizado es
  el producto Cerebro Digital individual. Expectativa explícita del cliente: **"un cerebro
  digital conectado a Claude Code"**.
- **Modalidad**: presencial en Caracas, sesiones de 2h.
- **Timeline**: propuesta el 25-sep-2026, feedback esperado el 29-sep-2026.

## Contenido de `fydeh Programa Mentoring 27-02-26.pdf` (material propio de Luis)

Su programa de mentoring FYDEH usa una **metodología de 3 pasos** ("lo que nos diferencia"):
1. **Diagnóstico de Precisión** (análisis integral del rol, entrevistas 360° con
   supervisores y pares).
2. **Acompañamiento en la Acción** (sesiones de mejores prácticas, gestión de riesgos,
   visibilidad estratégica).
3. **Control de Impacto** (seguimiento trimestral de KPI, plan de trabajo de 6-12 meses).

Esta propuesta **ecoa** esa estructura de 3 pasos (mismo espíritu: diagnóstico → acción →
seguimiento) como reconocimiento de cómo Luis ya empaqueta su trabajo, sin citar su material
textualmente ni construir el deck como una copia de su metodología.

## Decisiones de diseño (2026-09-25)

1. **Patrón profundo, no ligero — decisión central de esta propuesta**: la Ficha pide
   explícitamente "un cerebro digital conectado a Claude Code". El sistema tiene documentados
   2 patrones de Cerebro Digital:
   - **Ligero** (6h/persona, 3 sesiones de 2h, Claude.ai Projects + Skills + Obsidian, SIN
     Claude Code/terminal) — usado en `dhl-cerebro-digital/` y `banco-plaza-cerebros-digitales/`.
     Coincide con la tarifa documentada "Excepción — Cerebros Digitales" (6h) de
     `empresa/politicas-comerciales.md`.
   - **Profundo** (12h/persona, 6 sesiones de 2h, Claude Code/terminal, memoria persistente,
     subagentes, conectores MCP, automatización multi-paso, puesta en producción) — usado
     solo en la Fase 2 de `venemergencia/` (deck corporativo multi-fase), sin tarifa
     documentada propia (dimensionado ad hoc).

   Como Luis pidió Claude Code explícitamente, se usa el **patrón profundo**, adaptado por
   primera vez como propuesta mono-persona (nunca antes extraído de Venemergencia como deck
   independiente). Esto implica **6 slides de sesión** (una por cada sesión de 2h), no 3
   como en el patrón ligero — el deck pasa de 14 a **17 slides**.

2. **Automatización de SUS PROPIOS procesos, no despliegue corporativo (restricción
   explícita del usuario)**: todo el contenido de cada módulo/sesión se reescribió desde el
   contenido genérico de Venemergencia Fase 2 (pensado para múltiples directivos de una
   empresa) hacia los 2 dolores reales y nombrados de Luis:
   - Cotización de propuestas sin un criterio que diferencie tarifas por tipo de hora
     (mentoría 1:1, taller grupal, diseño instruccional).
   - Diseño instruccional de sus programas (mentoring, talleres) armado caso por caso, sin
     método reutilizable.

   Por eso el deck construye 2 "subagentes" concretos durante el programa (cotizador de
   propuestas + diseño instruccional) en vez de un agente genérico de "automatización
   ejecutiva". Sin fase grupal ni lenguaje de equipo/líderes/cascada — todo en singular
   ("usted"/"Luis").

3. **Personalización con su cartera real**: se nombra su cartera de clientes activa
   (Farmatodo, IESA, Río, Canguro) en el Punto de dolor como contexto de credibilidad —
   información que el propio Luis compartió como pública/propia sobre su práctica, no un
   dato confidencial de terceros. Se usa una sola vez, sin sobrecargar el resto del deck.

4. **Slide "Su Cerebro Digital" (antes grafo en Obsidian) relabeleada, no rediseñada**: el
   patrón ligero usa una slide a la medida (`.s-graph`) que visualiza el grafo relacional de
   Obsidian. El patrón profundo no usa Obsidian (usa memoria persistente de Claude Code), así
   que se reutilizó el mismo componente visual (SVG + nodos, sin cambios de CSS) pero se
   cambió el texto: el nodo central sigue siendo "Cerebro Digital", y los 6 nodos periféricos
   pasan de categorías genéricas (Conocimiento, Proyectos, Procesos...) a sus 2 dolores reales
   más contexto (Metodología, Tarifas por hora, Cotización, Diseño instruccional, Cartera de
   clientes, Seguridad y datos).

5. **Horas — sin tarifa documentada, dimensionado ad hoc por precedente**: 12h (6 sesiones de
   2h) para 1 persona, igual que el criterio usado para cada directivo en la Fase 2 de
   `venemergencia/`. No aplica la "Excepción — Cerebros Digitales" de 6h, que es
   exclusivamente para el patrón ligero (`empresa/politicas-comerciales.md`: "No se combinan
   ambas reglas en la misma propuesta").

6. **Modalidad y fechas**: presencial en Caracas, sesiones de 2h (dato de la Ficha). Sin
   fecha de inicio confirmada — se omite del deck, no se inventa (regla "Omitir, no
   inventar").

7. **Estándares Habilidades vigentes desde 2026-09-23**: descuento urgente (15 días), ROI
   explícito (redactado en torno a sus 2 dolores reales, no en cifras exactas — sin dato de
   tarifa/hora facturable de Luis en la Ficha), garantía 30-60-90 + slide de Seguimiento
   dedicada (`.s-followup`).

8. **Sin afirmar migración de stack (§4.11)**: no aplica de forma directa (Luis no tiene un
   stack corporativo previo relevante mencionado en la Ficha) — el deck no afirma nada al
   respecto.

9. **Con certificado de participación INTEZIA** — Habilidades con capacitación real.

10. **Impacto (§4.9)**: reutiliza las mismas fuentes ya verificadas de
    `dhl-cerebro-digital/`/`banco-plaza-cerebros-digitales/` (Stanford HAI AI Index Report
    2026, McKinsey The State of AI 2025, Anthropic Economic Index 2025) — datos generales de
    adopción/productividad de IA, válidos para este eje temático sin necesidad de una fuente
    distinta.

## Entregables

- Cerebro Digital propio: un agente en Claude Code configurado con su metodología.
- Subagente cotizador de propuestas con tarifas diferenciadas por tipo de hora.
- Subagente de diseño instruccional para sus programas.
- Certificado de participación INTEZIA.

## Notas internas

- **Pendiente de confirmar con Verónica antes de enviar**: fecha de inicio de las 6
  sesiones.
- Fuera de alcance de esta propuesta (mencionado por el usuario como contexto, no
  construido ni cotizado): cualquier productización futura del programa de retail o
  comisiones por referidos de Luis — no forma parte de esta Habilidades de Cerebro Digital.
- Primera propuesta del sistema que extrae y adapta el patrón profundo de Cerebro Digital
  (antes solo visto dentro de la Fase 2 corporativa de `venemergencia/`) como deck
  mono-persona independiente — precedente a citar si aparece otro caso similar (consultor
  individual que pide explícitamente Claude Code).
