# Brief — Banco Plaza · Copilot para Producto, Alexis (CAI-026)

## Datos administrativos

- **Empresa**: Banco Plaza
- **Sector**: Banca
- **Slug**: `banco-plaza-copilot-producto`
- **División Intezia**: `educacion` (mismo criterio que CAI-024/CAI-025, mismo cliente).
- **Servicio (§4.1a)**: **combo Detección + Habilidades** — se registra `servicio: "deteccion"`
  en `meta.json`, mismo criterio de sistema que `simple-tv-det002/` (DET-002, "combo
  Detección+Habilidades, sigue siendo deteccion") — CLAUDE.md §4.1a. **Código**: el usuario
  pidió explícitamente `CAI-026` (continúa la numeración de las 2 propuestas anteriores de
  Banco Plaza del mismo día), no `DET-`. Se respeta la instrucción directa del usuario para
  el código/carpeta; el campo `servicio` de `meta.json` refleja igual el combo, para que
  `clientes/INDEX.md` lo agrupe correctamente.
- **Tipo de documento**: Capacitación In-Company con fase previa de Detección (`CAI-026`).
- **Fuente**: instrucción directa del usuario, **sin Ficha Comercial** (2026-09-23) — mismo
  criterio que CAI-024/CAI-025, tercera propuesta de la cuenta el mismo día.

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
  (misma asesora que CAI-024/CAI-025, mismo cliente).
- **Contacto / participante cliente**: **Alexis**, del área de **Producto** de Banco Plaza.
  **1 solo participante** — a diferencia de CAI-025 (5 personas), aquí se nombra
  explícitamente en el deck (mismo criterio que `dhl-cerebro-digital/` con Miguel): el
  producto es personalizado para él como individuo.

## Qué pide el cliente (mensaje directo del usuario, 2026-09-23)

- Tercera propuesta para Banco Plaza el mismo día. Una sola persona, **Alexis**, del área de
  **Producto**. Se le quiere enseñar **Microsoft Copilot** — las licencias que **toda la
  organización ya maneja** (mismo ecosistema Microsoft mencionado en CAI-024/CAI-025) — para
  que le saque el máximo provecho en sus procesos y tareas del día a día.
- **Esquema explícito del usuario**: combinar **Detección** con **Habilidades**, pero es "una
  propuesta netamente práctica", por lo que entra en el rango de Habilidades (mayoría de
  horas). El usuario consideró pertinente incluir horas de Detección como **levantamiento de
  información previo**, para personalizar más las prácticas.
- **Instrucción de Jean** (interno, transmitida por el usuario): investigar qué hace un
  departamento de Producto en un banco, y en base a eso construir una **idea preliminar** del
  temario y las prácticas de Habilidades — **dejando explícito que esto puede variar** después
  de las horas de Detección (el levantamiento real con Alexis manda sobre cualquier hipótesis
  previa).
- **Horas — confirmadas explícitamente por el usuario** (mensaje de seguimiento): *"esta
  propuesta serian 4h de deteccion y 8h en sesiones de habilidades para un total de 12h en la
  propuesta"* → **Detección 4h (levantamiento) + Habilidades 8h (sesiones prácticas) = 12h de
  propuesta**. Coincide con el dimensionamiento estándar de Detección por área
  (`empresa/politicas-comerciales.md` / memoria `lineamientos-horas-deteccion-habilidades`:
  4h/área) — aquí Alexis/Producto hace las veces de esa "área".
- **Calendario — confirmado explícitamente por el usuario**: *"coloca el kick off para el 1
  de cotubre de 10 a 11 y las sesiones lunes y miercoles a partir del 5 de 2 a 4"* → Kick-off
  jueves 1 de octubre, 10:00-11:00 (1h, aparte, no cuenta en las 12h). Sesiones lunes y
  miércoles, 14:00-16:00 (2h c/u), desde el 5 de octubre: las 2 primeras (5 y 7 de octubre)
  son las 2 sesiones de Detección (4h); las 4 siguientes (12, 14, 19 y 21 de octubre) son las
  4 sesiones de Habilidades (8h).

## Decisiones de diseño (2026-09-23)

1. **Detección individual, no organizacional**: a diferencia del patrón habitual de Detección
   por múltiples áreas (`pilotes-perforados/`, mapa de calor), aquí la "unidad de auditoría"
   es 1 sola persona (Alexis) representando el área de Producto — coherente con el
   dimensionamiento de 4h/área ya documentado, aplicado a este caso puntual. La Detección
   levanta las tareas reales de Alexis (qué documentos redacta, qué análisis hace, con quién
   se reúne, qué fricciones tiene hoy con Copilot) y de ahí sale el temario definitivo de la
   fase de Habilidades.
2. **Temario de Habilidades — preliminar, sujeto a ajuste**: siguiendo la instrucción de Jean,
   se investigó qué hace típicamente un área de Producto en un banco (diseño y gestión del
   ciclo de vida de productos financieros, casos de negocio, coordinación con Riesgo/
   Cumplimiento/Legal/Operaciones, análisis de rentabilidad y adopción, presentaciones a
   comités, documentación regulatoria) para proponer 4 bloques de práctica tentativos,
   mapeados 1:1 a las 4 sesiones de 2h de Habilidades:
   - Redacción de especificaciones y documentos de producto (Word + Copilot)
   - Análisis de métricas y rentabilidad de producto (Excel + Copilot)
   - Preparación de presentaciones para comités (PowerPoint + Copilot)
   - Gestión de reuniones y seguimiento con otras áreas (Teams/Outlook + Copilot)
   El deck deja explícito en la slide de Habilidades y en el campo `Notas` que este temario es
   una hipótesis de trabajo: se confirma o ajusta con los hallazgos reales de la Detección.
3. **Base estructural**: clonado de `banco-plaza-mercadeo/` (CAI-024) — mismo shell visual que
   las 2 propuestas anteriores de la cuenta el mismo día (roadmap `.rmx-linear` de 2 etapas +
   resultado en 1 sola página, `.s-schedule` con Temas/Timebar/3 columnas, Beneficios v3,
   Cierre escalera, `.s-followup` de Seguimiento 30-60-90, `.steps-calendar`). Se prefirió este
   shell sobre el patrón "Inversión por fases" de `simple-tv-det002/`/`amcor/` (2 cajas de
   precio separadas) porque el alcance es más chico (12h, 1 persona) y no hay una segunda
   propuesta competidora con la que comparar fase por fase — una sola hoja de cotización con
   el total (12h) es más clara aquí, igual que CAI-024/CAI-025.
4. **Garantía 30-60-90 y slide de Seguimiento — sí aplican**: la propuesta incluye un
   componente real de Habilidades (8h de práctica), así que sigue el mismo criterio ya
   establecido ("la garantía aplica al servicio que la ocupe, en este caso Habilidades") de
   CAI-024/CAI-025.
5. **Con certificado de participación INTEZIA** — hay capacitación práctica real (Habilidades),
   mismo criterio que CAI-024/CAI-025 (y a diferencia de una Detección pura, que no lleva
   certificado — memoria `deteccion-sin-certificado`).
6. **Sin afirmar migración de Microsoft/Copilot (§4.11)**: no aplica aquí en el sentido
   estricto (Copilot YA es la herramienta nativa de Banco Plaza, no una nueva que reemplaza
   algo) — pero se mantiene la misma cautela de no prometer que Alexis "ya adoptó" Copilot
   antes de la capacitación.
7. **Modalidad**: no especificada por el usuario para esta propuesta — se deja "a definir",
   mismo criterio que CAI-025.

## Impacto (§4.9)

Reutiliza las cifras ya verificadas de `maurel-prom-copilot/` y `doral/` (mismo eje temático:
adopción práctica de Microsoft Copilot) — Microsoft, *Work Trend Index Special Report*
(noviembre 2023): 85% redacta un primer borrador más rápido, 75% encuentra información más
rápido, 64% procesa menos tiempo el correo, usuarios de Copilot resumen una reunión perdida 4
veces más rápido.

## Entregables

- Diagnóstico de tareas y fricciones reales de Alexis con Copilot en Producto (Detección).
- Temario de Habilidades confirmado y calibrado a esos hallazgos.
- Prácticas y prompts reutilizables para documentos, análisis y presentaciones de Producto.
- Workbook digital y certificado de participación INTEZIA.

## Corrección de copy (2026-09-24) — título de portada

Instrucción directa del usuario: mismo criterio aplicado a las 3 propuestas de Banco Plaza —
el título original ("Copilot, a la medida del día a día de Producto") describía la mecánica
del servicio, no una propuesta de valor atractiva. Se cambió a: **"De usar Copilot, a que
Copilot te entienda."** — enmarca la transformación (de uso genérico a uso calibrado) en vez
de describir el proceso.

## Notas internas

- **Pendiente de confirmar con Flavia antes de enviar**: modalidad de las sesiones, y
  validación con Alexis/Producto de que el temario preliminar (basado en investigación
  general de áreas de Producto bancarias, no en un levantamiento real todavía) resuena antes
  de la Detección.
- El temario de Habilidades es una **hipótesis de trabajo**, no un compromiso cerrado — la
  Detección (4h) puede cambiarlo. El deck lo deja explícito en la slide y en `Notas`.
