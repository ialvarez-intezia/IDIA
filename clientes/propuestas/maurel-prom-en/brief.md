# Brief — Maurel & Prom Venezuela · Plan Estratégico Integral (ALL-003) · English version

> **Nota 2026-09-17**: esta carpeta (`maurel-prom-en/`) es la **traducción al inglés** del
> deck de `clientes/propuestas/maurel-prom/` (mismo código ALL-003, mismo contenido
> comercial, mismo cliente y asesora) — instrucción directa del usuario ("puedes crear ambas
> propuestas en inglés?"). Este `brief.md` y `programa.md` se mantienen en **español**
> (documentación interna del equipo, no cara al cliente); solo el `index.html` (el deck que
> se entrega) y `acroforms.json`/el customize script están en inglés. Ver la sección
> "Mecánica AcroForm — versión en inglés" más abajo para el detalle técnico de por qué esta
> carpeta usa un `customize-maurel-prom-en.py` propio en vez del trío estándar.
>
> Para todo el resto de decisiones de negocio (por qué integral, por qué el énfasis
> regulatorio europeo, dimensionamiento, las 8 áreas, nota sobre Keiber, segunda propuesta
> pendiente), ver el `brief.md` del deck en español — es la fuente de verdad, esta carpeta
> no la duplica.

## Mecánica AcroForm — versión en inglés (bloqueante, leer antes de regenerar el PDF)

El deck en español usa marcadores de texto literal en español ("Inversión por fases", "Lo
que se llevan", "Cómo arrancamos") que `scripts/agregar-campo-precio.py` (compartido, **nunca
se modifica por deck**) busca para decidir dónde inyectar los AcroForms. Como este deck está
en inglés, esos marcadores NO aparecen — el script compartido reporta los 3 grupos como
"(omitido)" y no crea ningún campo. Por eso:

1. **No correr `customize-acroforms.py` para este deck** — no encontraría ningún campo
   (todos fueron omitidos por el paso anterior) y solo imprimiría avisos de "campo no
   encontrado".
2. **`scripts/customize-maurel-prom-en.py` es el ÚNICO paso de personalización** — construye
   TODOS los campos (PrecioFase1-3 + PrecioBase/Descuento/PrecioTotal + Notas, Entregables +
   Acreditacion, Paso01-03 Titulo/Body) directamente por índice de página fijo (no por
   marcador de texto), con el contenido en inglés ya incluido como `/V`, además de
   InnovacionEstimado y el Cierre escalera (que este deck ya requería aparte, igual que la
   versión en español).
3. **Trío correcto para este deck**:
   ```bash
   bash scripts/generar-pdf.sh maurel-prom-en
   python3 scripts/customize-maurel-prom-en.py "clientes/propuestas/maurel-prom-en/<pdf>"
   ```
   Sin el paso de `customize-acroforms.py` en medio.
4. Los nombres internos de campo (`/T`) se mantienen en español (`PrecioBase`,
   `Entregables`, `CierreResultado`, etc.) — son identificadores invisibles para el lector
   final, y mantenerlos permite reutilizar `acroform_appearance.rebake_bold_fields()` (que
   matchea por esos nombres) sin tocar ese módulo compartido.

## Datos administrativos

- **Empresa**: Maurel & Prom Venezuela
- **Sector**: Hidrocarburos / Petróleo — filial venezolana de un grupo francés con **Casa
  Matriz en París**.
- **Slug**: `maurel-prom-en` (traducción de `maurel-prom/`, verificado con `ls` antes de
  clonar — lección del incidente de sobrescritura en `robin-agency/`, 2026-09-16).
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `integral` — Detección + Habilidades + Políticas + Innovación como
  una sola hoja de ruta secuencial, por instrucción explícita del cliente (§4.1b).
- **Tipo de documento**: Plan estratégico integral · 4 fases · cotización por fase separada.
- **Eje temático**: gobierno responsable del uso de IA (dato, cumplimiento, legal), con
  énfasis regulatorio explícito por la Casa Matriz europea, más adopción práctica del
  entorno Microsoft 365 ya licenciado.
- **Fecha del brief**: 2026-09-17
- **Alianza**: no

## Fuente primaria

Ficha comercial de Maurel & Prom Venezuela adjunta por el usuario (2026-09-17), más un
segundo mensaje del usuario con contexto adicional de la reunión de levantamiento (incluye
la participación de Keiber) y los dos requisitos específicos de esta propuesta (cotización
por fase separada, énfasis regulatorio europeo). Sin Ficha de Levantamiento formal más allá
de la ficha comercial inicial.

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414 0570056 · miribarren@intezia.com
  (única "María" que aparece como asesora comercial en el resto del sistema — mismo contacto
  que ya cierra Simple TV ALL-001/ALL-002 y otras propuestas; se asume la misma persona salvo
  corrección del usuario).
- **Contacto cliente / punto de entrada**: Carmen, responsable de Legal y Cumplimiento
  (apellido no confirmado — se usa solo el nombre, "omitir, no inventar").

## Contexto del cliente

- Empresa francesa de exploración y producción de hidrocarburos. La Casa Matriz en París
  opera bajo marco europeo (RGPD, AI Act) — cualquier política de uso de IA que se construya
  para la filial venezolana debe poder sostenerse frente a esa Casa Matriz.
- **Punto de entrada: Legal y Cumplimiento, no Tecnología.** La prioridad número uno de
  Carmen es que el equipo sepa **qué información no puede subir a herramientas de IA**, más
  gobernanza de datos en general — esto ancla el énfasis de toda la propuesta, sobre todo la
  Fase 3 (Políticas).
- **~50 personas, en 8 áreas** (confirmadas por el usuario el 2026-09-17): Legal y
  Cumplimiento, Finanzas, RRHH, Administración e IT, Trading y Logística, SCM, Técnica y
  HSSE. Perfil administrativo-gerencial y operativo.
- **Sedes**: Caracas y Maracaibo.
- **Entorno tecnológico**: Microsoft 365 con licencia de **Copilot** ya activa, pero **sin
  adopción real todavía**. Claude y ChatGPT están en evaluación como "próxima apertura
  corporativa mundial" del grupo — no decidido ni disponible aún, se mencionan como contexto
  de evaluación, nunca como herramienta ya adoptada (§4.11).
- **Gemini queda explícitamente fuera del abanico de posibilidades** para este cliente
  (definición de Casa Matriz) — no se menciona como herramienta candidata en ningún punto
  del deck.

## Por qué "integral" y no un servicio individual

El cliente pidió explícitamente un plan que combine las 4 etapas del Modelo Intezia
(Detección, Habilidades, Políticas, Innovación) como una sola hoja de ruta secuencial, no un
combo parcial de 2 servicios. Esto activa `servicio: integral` (CLAUDE.md §4.1b).

**Estructura de referencia**: se clonó `simple-tv-all002/` (no `all001/`) porque su patrón
de cotización "Inversión por fases" (valor explícito por cada fase, no un combo cerrado) es
exactamente lo que el cliente pidió — ver siguiente sección.

## Cotización por fase separada (requisito explícito del cliente)

El cliente pidió que la propuesta sea modular y escalable: que se pueda ver el valor de cada
servicio de forma independiente, no solo un combo cerrado. Por eso se usa el patrón de
ALL-002 ("Inversión por fases"), no el de ALL-001 ("Fase 1 cotizada, resto progresivo"):

- **Fase 1 · Detección**: cotizada.
- **Fase 2 · Habilidades**: cotizada como paquete completo.
- **Fase 3 · Políticas**: cotizada.
- **Fase 4 · Innovación**: estimado aparte (retainer mensual, no cotización firme), igual
  criterio que ALL-002.

## Énfasis regulatorio europeo (requisito explícito del cliente)

Dado que la cuenta entró por Legal y Cumplimiento y que la Casa Matriz está en Francia, la
Fase 3 (Políticas) hace referencia explícita al marco europeo — **RGPD** (Reglamento General
de Protección de Datos) y **AI Act** (Ley de Inteligencia Artificial de la Unión Europea) —
y no solo al marco venezolano, que hoy no tiene ley de protección de datos personales. Esto
le da más peso a la política frente a la Casa Matriz. Esta capa se añade sobre el contenido
estándar del servicio de Políticas (`empresa/tipos-de-documento.md §0.1`): Manual de
políticas, Brújula IA, Matriz de riesgos, 3 a 5 semanas.

## Dimensionamiento (`empresa/politicas-comerciales.md` → Dimensionamiento por servicio)

- **Detección**: 4h por área × 8 áreas + 2 sesiones de Fundamentals grupal de 2h (máx. 25
  personas por sesión; ~50 personas total → 2 sesiones, una por sede: Caracas y Maracaibo).
- **Habilidades**: 8-12h por área, cotizado como paquete completo (no introductorio), mismo
  criterio que ALL-002.
- **Políticas**: por entregable, no por horas — paquete completo (Informe de diagnóstico,
  Manual de políticas con capa RGPD/AI Act, Matriz de riesgos, Brújula IA, sesión de
  socialización), 3 a 5 semanas.
- **Innovación**: estimado de acompañamiento, retainer mensual (no cotización firme) — mismo
  tratamiento que ALL-002 y el piloto `zoom-innovacion/`.

## Áreas — confirmadas (2026-09-17)

El usuario confirmó las 8 áreas durante la revisión de este documento:

1. Legal y Cumplimiento
2. Finanzas
3. RRHH
4. Administración e IT
5. Trading y Logística
6. SCM
7. Técnica
8. HSSE

Se incorporaron al deck en la Fase 1 · Detección (roadmap, Etapa 1 · Auditoría por Área,
facet "Con quién"). El resto de las menciones a lo largo del deck sigue usando "8 áreas" en
genérico (mismo criterio que Simple TV ALL-002 con sus 14 áreas), para no repetir la lista
completa en cada slide.

## Nota sobre Keiber (alineación recomendada, no ejecutada)

El usuario mencionó que Keiber participó en la reunión de levantamiento y ya tiene clara la
visión de por dónde debería ir la propuesta dado el tipo de empresa, recomendando alinear
con él antes de redactar. Este sistema no tiene mecanismo para contactar a Keiber
directamente — este borrador se construyó con el mejor criterio posible a partir de la ficha
y el contexto escrito por el usuario. **Se recomienda que el equipo lo revise con Keiber
antes de enviarlo al cliente.**

## Segunda propuesta pendiente (fuera de alcance de este documento)

El cliente también necesita una propuesta separada, más genérica, enfocada en Copilot
(entrenamiento práctico por área: redacción, análisis, minutas de reunión, integraciones con
Excel/Word). Esta propuesta **no se construye en este documento** — el usuario indicó
explícitamente construir primero solo la integral de 4 etapas ("esta que vamos a desarrollar
primero es la que incluye las 4 etapas").

## Impacto (§4.9) — datos reales verificados por WebSearch

- **LayerX, "Enterprise AI and SaaS Data Security Report" (2025)**: 77% de los empleados que
  usan herramientas de IA generativa han copiado y pegado datos de la empresa en sus
  consultas; 22% de esos pegados incluye información personal o de pago (PII/PCI).
- **AI Act de la Unión Europea (Reglamento (UE) 2024/1689)**: las obligaciones para sistemas
  de IA de alto riesgo entran en vigor el 2 de agosto de 2026, con sanciones de hasta 35
  millones de euros o 7% de la facturación global anual.

Ambos datos conectan directo con el eje de esta propuesta: el riesgo real de fuga de
información sin gobernanza (la preocupación explícita de Carmen) y el costo de no anticipar
el marco regulatorio europeo que ya aplica a la Casa Matriz.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: María Iribarren.

## Pendientes

- Confirmar fechas de arranque y modalidad (presencial/híbrida) por sede.
- Confirmar apellido y datos de contacto completos de Carmen (contacto cliente).
- Alinear el borrador con Keiber antes de enviarlo al cliente (recomendación del usuario, no
  ejecutada por el sistema).
- Confirmar presupuesto y monto de la cotización (campos de precio vacíos, los llena ventas).
- Construir la segunda propuesta (Copilot, entrenamiento práctico por área) una vez esta
  quede aprobada o enviada.
