# Brief — FastMed · Agente conversacional para atención al paciente (CAI-030)

## Datos administrativos

- **Empresa**: FastMed
- **Sector**: Salud, servicios médicos corporativos (medicina ocupacional, vigilancia
  epidemiológica, atención clínica, laboratorio, seguros).
- **Slug**: `fastmed`
- **División Intezia**: `educacion` — cliente corporativo, sin ambigüedad.
- **Servicio (§4.1a)**: `habilidades` — la Ficha lo confirma explícitamente ("Servicios de
  interés: Habilidades") y llena el "Bloque específico · Habilidades" completo (qué debe
  poder hacer el equipo al terminar, tareas reales de sesión). A diferencia de
  `venemergencia-agente-personal/` (CAI-028, ver memoria
  `producto-desarrollo-agente-personal-sin-categoria.md`), este SÍ es un currículo real de
  Habilidades con certificado y adopción medible a 30-60-90 — no un proyecto de
  "Desarrollo"/software puro. Tampoco es un Cerebro Digital individual (como Luis Sosa
  CAI-029): es UN agente de producción compartido, construido por un equipo de 8 personas
  para toda la organización, no una IA personal por individuo.
- **Tipo de documento**: Capacitación In-Company (`CAI-030`, dado directo por el usuario).
- **Fuente**: Ficha de Levantamiento completa (`Levantamiento_FastMed_2026-09-25.pdf`,
  elaborada por Verónica Rubio, fecha de registro 2026-09-25) + contexto adicional dado por
  el usuario en el mensaje de encargo.

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com.
- **Contacto cliente**: Anabella Guerrero (responsable de logística del lado cliente). Lado
  técnico: Gerente de Tecnología y su equipo de sistemas (8 personas, área priorizada).

## Qué pide el cliente (Ficha + contexto del usuario, 2026-09-25/27)

- FastMed **no llega en frío**: dos años de adopción real de IA (filtro de IA sobre
  vigilancia epidemiológica antes de que el médico revise resultados, análisis de
  quejas/fortalezas de calidad de servicio, NotebookLM para repositorios de capacitación,
  Google Classroom para formación), interoperabilidad propia entre sistemas (ERP, CRM,
  historia clínica vía FastTech/SoaInt), y en 2025 un programa formal de capacitación en IA
  para gerencia media y alta con un consultor externo (Tony Martín).
- **Necesidad central (cita textual de la Ficha, Bloque D)**: resolver con un agente la
  atención al paciente para dos cosas: (1) gestión de casos (pedir cita, a quién debe
  llamar), y (2) sobre todo, cumplir la exigencia legal de entregar informes y resultados de
  laboratorio en menos de 24-48 horas. Hoy lo resuelven vía un sistema de tickets integrado a
  WhatsApp a través de Meta, cuyo costo por iteración de un examen es muy alto. Punto crítico
  explícito: **no puede haber un agente al que solo con la cédula se le entregue toda la
  información médica** — exige doble autenticación.
- **Filosofía del servicio**: Verónica propuso construir el agente **en conjunto** con el
  equipo de tecnología de FastMed (transferencia de capacidad, no dependencia de Intezia) —
  es justamente la filosofía que Anabella busca ("que el propio departamento de tecnología
  construya y sostenga el agente in-house, acompañado por Intezia como
  consultoría/mentoring").
- **Restricciones operativas**: el equipo de tecnología está saturado con otros proyectos
  (carga del sector petrolero/energético) y están contratando un administrador de proyectos
  de tecnología — disponibilidad limitada en el corto plazo. Modalidad preferida: mixta
  (Anabella trabaja asíncrona; aceptaría alguna sesión presencial puntual para la conexión
  de bases de datos).
- **Seguridad**: sufrieron 2 hackeos grandes este año que infectaron la base de datos, con
  pérdidas económicas por temas bancarios — refuerza la exigencia de doble autenticación y
  controles serios sobre datos médicos.
- **Oportunidad secundaria identificada, fuera de alcance de esta propuesta**: automatizar
  la conciliación bancaria (35 cuentas, bancos no estandarizados en Venezuela) — mencionada
  en el Bloque F de la Ficha como observación interna, no cotizada aquí.

## Decisiones de diseño (2026-09-27)

1. **Clasificación de servicio confirmada como Habilidades genuina** (no "Desarrollo" ni
   Cerebro Digital individual): la Ficha llena el bloque curricular completo y pide
   explícitamente que el propio equipo aprenda a construir y sostener el agente. Deck con
   certificado, Seguimiento 30-60-90 y todos los estándares vigentes de Habilidades.
2. **Horas**: 12h (6 sesiones de 2h) para el área de Tecnología/Sistemas. Según
   `empresa/politicas-comerciales.md` → Dimensionamiento por servicio → Habilidades: 8-12h
   por área, hasta 5 procesos. FastMed tiene 2 procesos (gestión de citas, entrega de
   resultados) — muy por debajo del tope de 5 que sumaría horas extra. Se usó el techo del
   rango (12h, no 8h) por la profundidad técnica exigida: doble autenticación, conexión a
   sistemas reales (repositorios + citas online), y cumplimiento de un plazo legal — no por
   cantidad de procesos.
3. **Base estructural**: clonado de `luis-sosa-cerebro-digital/` (CAI-029) — precedente más
   reciente y ya verificado visualmente de un deck Habilidades mono-fase de 6 sesiones (sin
   roadmap, `.ruta` de progreso, estándares completos desde 2026-09-23). Todo el contenido de
   cada slide se reescribió desde cero para FastMed.
4. **Slide bespoke "Cómo funciona el agente"** (antes "Su Cerebro Digital"/memoria de Claude
   Code en el clon de origen): se reutilizó el mismo componente visual (SVG + nodos, sin
   cambios de CSS) para mostrar la arquitectura del agente — nodo central "Agente WhatsApp",
   6 nodos periféricos: Doble autenticación, Gestión de citas, Entrega de resultados,
   Repositorios, Sistema de citas, Seguridad y datos.
5. **Cita de la slide de Punto de dolor**: es una cita real (Bloque D de la Ficha, marcada
   explícitamente como "cita textual"), parafraseada levemente para evitar comillas
   anidadas dentro del `<h2>` — no es una cita inventada (regla de
   `titulo-portada-valor-no-mecanica.md`: nunca inventar una cita atribuida al cliente; aquí
   sí existe una real, se usa con cuidado de formato).
6. **Título de portada**: molde "De X, a Y" (transformación, no mecánica) —
   "De tickets vía Meta, a un agente propio y seguro." — capta el dolor real (costo de
   iterar por Meta) y el valor (autonomía + seguridad).
7. **Impacto (§4.9) — 2 fuentes nuevas, verificadas por WebSearch 2026-09-27** (no se
   reutilizaron las cifras genéricas de adopción de IA de otros decks, porque el eje temático
   de FastMed es más específico: chatbots de atención al paciente + seguridad de datos
   médicos):
   - **MGMA Stat** (encuesta a consultorios médicos, abril 2025): 19% de los consultorios ya
     usa un chatbot/asistente virtual para comunicación con pacientes; los médicos ven valor
     en programar citas (78%), encontrar instalaciones (76%) e información de medicamentos
     (71%).
   - **IBM — Cost of a Data Breach Report (2025)**: el sector salud tiene el costo promedio
     más alto de una filtración de datos, $7.42 millones, 15º año consecutivo como el sector
     más caro.
8. **Sin calendario de inicio**: la Ficha da una fecha de **reunión de seguimiento** para
   revisar esta propuesta (lunes 28 o miércoles 30 de septiembre, 10:00 a.m. hora de Anabella,
   6h de diferencia con Venezuela) — no una fecha de arranque del servicio. Se omite
   cualquier calendario en el deck para no confundir ambas cosas (regla "Omitir, no
   inventar").
   - `fecha_arranque_deseada`: no confirmada (solo la reunión de feedback del 28/30 de
     septiembre sobre esta propuesta).
   - `resultados_esperados` (cita de la Ficha, "Uso esperado post-formación para medir a
     30-60-90"): que el agente quede funcionando en producción atendiendo pacientes vía
     WhatsApp para gestión de citas y entrega segura de resultados con doble autenticación
     activa, y que el equipo de tecnología de FastMed pueda mantenerlo y escalarlo sin
     depender de Intezia. Usado para redactar el ROI y la slide de Seguimiento 30-60-90.
9. **Modalidad**: mixta (dato de la Ficha) — se documenta en Notas del AcroForm, sin fechas
   concretas.
10. **Sin afirmar migración de Google Workspace (§4.11)**: FastMed ya usa Google Workspace;
    el agente se integra a ese entorno y a sus sistemas propios (FastTech/SoaInt), nunca se
    afirma que la empresa migra o reemplaza su stack.
11. **Con certificado de participación INTEZIA** — Habilidades con capacitación real.
12. **Estándares Habilidades vigentes desde 2026-09-23**: descuento urgente (15 días), ROI
    explícito (redactado desde el `resultados_esperados` de la Ficha, sin inventar cifras en
    dólares ya que la Ficha no dio un monto exacto del costo de iterar por Meta), garantía
    30-60-90 + slide de Seguimiento dedicada (`.s-followup`).

## Actualización 2026-09-30 — Fase 2 · Innovación agregada (corrección post-envío)

Propuesta ya enviada el 2026-09-27 (§4.19: `fecha_entrega` no se pisa); esta sesión retomó
el trabajo en curso y lo cerró. Cambios sobre el deck original mono-fase:

1. **Combo Habilidades + Innovación** (servicio de entrada sigue `habilidades`, §4.1a — un
   combo de 2 servicios no usa `integral`, ese valor es solo para los 4 servicios como una
   sola hoja de ruta). Se agregó una Fase 2 · Innovación (ciclo mensual, 3 meses) que
   sostiene el mismo agente construido en Fase 1, sin abrir nuevos frentes ni cotizar la
   oportunidad de conciliación bancaria (sigue fuera de alcance). Alcance de Innovación
   confirmado por el usuario: solo mantenimiento/evolución del agente ya construido.
   Deck pasó de 17 a 18 slides: se insertó el roadmap `.rmx-linear` cíclico (mismo patrón de
   `zoom-innovacion/`, INN-001) y se sumó un bullet de Innovación en Objetivos y Beneficios.
   Portada actualizada a "Servicio de Habilidades e Innovación" (§4.1a Portada visible).
2. **3 desbordes bloqueantes corregidos** (detectados por `verificar-overflow.js` al retomar):
   Objetivos específicos (5→4 ítems, capacidad `.s-goals .specifics ol` es 3-4), Roadmap
   Innovación (se retiró un párrafo `.roadmap-lead` agregado fuera del patrón probado — ni
   zoom-innovacion ni banco-plaza-mercadeo lo llevan, y con 3 `.rmx-card` + 1
   `.rmx-result-card` ya llena la slide) y Beneficios (Resultados 4→3 ítems, el patrón v2/v3
   estándar es 3, no 4).
3. **Bug de layout no detectado por el script automático, encontrado en revisión visual**:
   la hoja "Inversión por fases" (2 filas) es la primera vez que ese patrón se usa sobre
   `_base/styles.css` compartido + `overrides.css` propio (los otros decks con esta variante,
   `corporaciones-easyaccess/` y `simple-tv-det002/`, tienen `styles.css` completo propio).
   El supuesto inicial de que "las 2 filas de fase terminan muy por encima de
   `block-notes-container`, no hace falta mover nada" era incorrecto: el `/Rect` real de los
   campos AcroForm (Notas, PrecioBase, Descuento, PrecioTotal) para el marcador "Inversión
   por fases" lo fija `scripts/agregar-campo-precio.py` (`FASE_PRICE_FIELDS`) en coordenadas
   absolutas fijas, independientes del CSS del HTML — el campo Notas caía en 428-538px,
   encima de donde `.cot-roi-box` (heredado de `_base/styles.css`, top:512px) dibuja su
   texto, y el ROI salía tachado por el borde del campo. Fix: overrides en `overrides.css`
   reposicionando toda la columna de precio (notas, labels, frames, ROI, garantía, términos)
   a las mismas coordenadas que `corporaciones-easyaccess/styles.css` (único otro deck de 2
   fases) + el mismo desplazamiento relativo aplicado a ROI/Garantía (ausentes ahí). Ver el
   comentario "CORRECCIÓN 2026-09-30" en `overrides.css` para las coordenadas exactas.
4. **`scripts/customize-fastmed.py` actualizado**: agrega el bloque que elimina el campo
   huérfano `PrecioFase3` (agregar-campo-precio.py siempre crea 3 slots) y recalcula
   `PrecioBase` como Fase1+Fase2, mismo patrón que `customize-corporaciones-easyaccess.py`.
5. Registro de entrega: `estado` pasó `Enviada → En corrección → Enviada` (mismo
   `fecha_entrega` original, 2026-09-27 — el hook de `generar-pdf.sh` no la pisa).

**Refinamiento el mismo día**: el usuario precisó el alcance operativo exacto de Innovación
(2 sesiones al mes, 4h en total, para ajustar nodos, mejorar o innovar el flujo ya construido)
y pidió alinear la hoja de cotización al patrón usado en `banco-activo-deteccion-negocios/`
(DET-021, mismo marcador "Inversión por fases"). Cambios:
- Roadmap (`.rmx-ethics`) y descripción de Fase 2 en la hoja de precio actualizados con la
  cadencia exacta (2 sesiones al mes, 4h en total).
- Coordenadas de la columna de precio realineadas EXACTAS a
  `banco-activo-deteccion-negocios/overrides.css` (antes eran una derivación propia, muy
  cercana pero no idéntica): `.block-notes-container` 400px, `.cot-roi-box` 552px,
  `.cot-garantia-badge` 632px, `.cot-validity` 452px, `.cot-terms-box` 476px.
- Beneficios de Innovación sumados en los 4 bloques: Resultados y "Por qué Habilidades"
  (HTML estático, ya lo mencionaban, se afinó la redacción) + Entregables y Valor inmediato
  (AcroForm `acroforms.json`, se agregó una línea de Innovación en cada uno — antes solo
  vivía en Resultados/Por qué).

## Entregables

- Agente conversacional propio (WhatsApp) para atención al paciente, con los 2 flujos
  (gestión de citas, entrega de resultados) construidos y en producción.
- Doble autenticación y controles de seguridad sobre la data médica.
- Equipo de Tecnología capacitado para sostener y escalar el agente sin depender de Intezia.
- Certificado de participación INTEZIA.

## Notas internas

- **Pendiente de confirmar con Verónica antes de enviar**: fecha real de arranque de las 6
  sesiones (distinta de la reunión de feedback del 28/30 de septiembre sobre esta
  propuesta), y el detalle de la modalidad mixta (qué sesión será presencial).
- Fuera de alcance de esta propuesta (mencionado como oportunidad secundaria en el Bloque F
  de la Ficha, no cotizado): automatizar la conciliación bancaria (35 cuentas, bancos no
  estandarizados).
- Precedente de clasificación de servicio a citar en casos similares futuros (equipo técnico
  interno que aprende a construir y sostener un agente de producción propio, con
  currículo/certificado real): este deck, `fastmed/` (CAI-030).
