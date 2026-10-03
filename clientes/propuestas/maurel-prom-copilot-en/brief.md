# Brief — Maurel & Prom Venezuela · Copilot para tu equipo (CAI-021) · English version

> **Nota 2026-09-17**: esta carpeta (`maurel-prom-copilot-en/`) es la **traducción al
> inglés** del deck de `clientes/propuestas/maurel-prom-copilot/` (mismo código CAI-021,
> mismo contenido comercial, mismo cliente y asesora, incluyendo el Módulo IV "Agentes y
> flujos" agregado el mismo día) — instrucción directa del usuario ("puedes crear ambas
> propuestas en inglés?"). Este `brief.md` y `programa.md` se mantienen en **español**
> (documentación interna); solo el `index.html` (el deck que se entrega) y
> `acroforms.json`/el customize script están en inglés.
>
> Para todo el resto de decisiones de negocio (por qué habilidades, por qué genérico y no
> por área, dimensionamiento, contenido de agentes/flujos), ver el `brief.md` del deck en
> español — es la fuente de verdad, esta carpeta no la duplica.

## Mecánica AcroForm — versión en inglés (bloqueante, leer antes de regenerar el PDF)

El deck en español usa marcadores de texto literal en español ("Lo que se llevan", "Cómo
arrancamos") que `scripts/agregar-campo-precio.py` (compartido, **nunca se modifica por
deck**) busca para decidir dónde inyectar los AcroForms. Como este deck está en inglés, esos
marcadores NO aparecen — el script compartido reporta esos grupos como "(omitido)" y no crea
ningún campo (la slide de precio SÍ usa el patrón estándar "Propuesta Económica", que aquí es
"Economic Proposal" — tampoco coincide). Por eso:

1. **No correr `customize-acroforms.py` para este deck** — no encontraría ningún campo.
2. **`scripts/customize-maurel-prom-copilot-en.py` es el ÚNICO paso de personalización** —
   construye TODOS los campos (PrecioBase/Descuento/PrecioTotal + Programa/Notas,
   Entregables + Acreditacion, Paso01-03 Titulo/Body) directamente por índice de página fijo,
   con el contenido en inglés ya incluido como `/V`, además del Cierre escalera.
3. **Trío correcto para este deck**:
   ```bash
   bash scripts/generar-pdf.sh maurel-prom-copilot-en
   python3 scripts/customize-maurel-prom-copilot-en.py "clientes/propuestas/maurel-prom-copilot-en/<pdf>"
   ```
   Sin el paso de `customize-acroforms.py` en medio.
4. Los nombres internos de campo (`/T`) se mantienen en español, mismo criterio que
   `maurel-prom-en/`.

## Datos administrativos

- **Empresa**: Maurel & Prom Venezuela
- **Sector**: Hidrocarburos / Petróleo — filial venezolana de un grupo francés con Casa
  Matriz en París.
- **Slug**: `maurel-prom-copilot-en` (traducción de `maurel-prom-copilot/`, verificado con
  `ls` antes de clonar — lección del incidente de sobrescritura en `robin-agency/`,
  2026-09-16).
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades` — capacitación práctica de un solo servicio, sin
  diagnóstico previo ni fases adicionales.
- **Tipo de documento**: Capacitación In-Company (`CAI-021`) · 5 módulos / 5 sesiones de 3h /
  15h totales · Presencial, en 2 grupos (Caracas y Maracaibo).
- **Eje temático**: adopción práctica de **Microsoft Copilot** dentro del entorno Microsoft
  365 que Maurel & Prom ya tiene licenciado — redacción, análisis, minutas de reunión,
  integraciones con Excel y Word, y elaboración de agentes e introducción a flujos.
- **Fecha del brief**: 2026-09-17
- **Alianza**: no

## Ajuste 2026-09-17 — se agregó Agentes y flujos con Copilot

Instrucción directa del usuario: "a esta última propuesta agrégale elaboración de agentes y
la introducción de flujos en Copilot". Se agregó un **Módulo IV nuevo** entre "Copilot en el
día a día" y "Adopción responsable": construcción guiada de un agente propio + introducción a
flujos que automatizan tareas repetitivas. Pasa de 4 a 5 módulos, de 12 a 15 horas totales, de
4 a 5 sesiones (una nueva slide de cronograma). Contenido y longitudes calibrados sobre
`bnc-bootcamp/` (CAP-001, Módulo III "Fábrica de Agents"), precedente real ya verificado sin
desborde con 5 módulos y 4 temas por card en la slide de Programa.

## Segunda propuesta de la cuenta — independiente de ALL-003

Esta es la **segunda de las dos propuestas** que el usuario indicó para Maurel & Prom: la
primera (`clientes/propuestas/maurel-prom/`, ALL-003) es el plan estratégico integral de 4
fases (Detección + Habilidades + Políticas + Innovación), con fuerte énfasis en gobernanza y
marco regulatorio europeo (RGPD, AI Act), porque la cuenta entró por Legal y Cumplimiento.
Esta segunda propuesta es **deliberadamente más genérica y ligera**: entrenamiento práctico
de Copilot por competencias (no por área, no por diagnóstico previo), pensado como una
capacitación independiente que Maurel & Prom puede contratar sola o junto con la integral.

- Slug y código distintos (`maurel-prom-copilot/`, CAI-021 vs. `maurel-prom/`, ALL-003).
- Mismo cliente y misma asesora comercial (María Iribarren), pero el deck es autocontenido:
  no depende de ALL-003 para tener sentido.
- Sin mención al énfasis regulatorio (RGPD, AI Act) — eso vive en la propuesta integral. Esta
  propuesta es puramente de habilidades prácticas.

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414 0570056 · miribarren@intezia.com
  (mismo contacto que ALL-003 y el resto de las cuentas que cierra).
- **Contacto cliente**: sin persona específica asignada a esta propuesta en el mensaje del
  usuario — se mantiene el mismo punto de entrada de la cuenta (Legal y Cumplimiento /
  Carmen) a nivel de relación comercial, sin nombrarla en el deck (esta propuesta no es de
  su área).

## Por qué "habilidades" y no parte de la integral

El usuario pidió esta propuesta explícitamente como la **segunda, más genérica**, ya
mencionada en el levantamiento original de Maurel & Prom pero fuera de alcance de la
integral ("esta que vamos a desarrollar primero es la que incluye las 4 etapas" — la
integral). Ahora que la integral (ALL-003) está entregada, se construye esta segunda pieza:
capacitación práctica de Copilot, sin diagnóstico previo (no es Detección) ni construcción de
políticas (no es Políticas) — un servicio de Habilidades puro.

## Contenido (tomado literal del pedido original del cliente)

El usuario especificó el alcance práctico esperado: **redacción, análisis, minutas de
reunión e integraciones con Excel y Word**. Se mapeó a la estructura de 4 módulos ya validada
en `doral/` (CAP-092, mismo eje temático — Copilot corporativo dentro de Microsoft 365),
clonada como punto de partida por ser el precedente más cercano en servicio + tipo de
documento + división (§6 Paso 0):

1. **Fundamentos de Copilot** — qué es y cómo se integra en Microsoft 365, alcances y
   límites.
2. **Copilot Chat y prompting** — instrucciones efectivas, iteración y verificación de
   resultados.
3. **Copilot en el día a día** — Word (redacción), Excel (análisis), Outlook (correos) y
   Teams (minutas de reunión): cubre uno a uno los 4 puntos que pidió el cliente.
4. **Agentes y flujos con Copilot** (agregado 2026-09-17) — qué es un agente y cuándo
   construir uno, elaboración guiada de un agente propio, introducción a flujos que
   automatizan tareas repetitivas y armado de un primer flujo simple.
5. **Adopción responsable** — privacidad de datos corporativos, verificación y protocolo de
   uso, plan de adopción a 30 días.

## Decisiones de diseño (sin ficha formal para esta propuesta específica)

- **Modalidad presencial, 2 grupos (Caracas y Maracaibo)**: a diferencia de Doral (online
  síncrono, cliente en Miami), Maurel & Prom tiene 2 sedes físicas en Venezuela — se optó por
  presencial en cada sede, replicando el mismo programa, en vez de forzar una sesión virtual
  única. Decisión propia del consultor, ajustable con el cliente.
- **Genérico, no por área**: a diferencia del dimensionamiento de Habilidades por área (8 a
  12h por área, `empresa/politicas-comerciales.md`), esta propuesta es un solo programa
  aplicable a toda la organización — el propio cliente la definió como "más genérica" frente
  a la integral, que sí diagnostica y capacita por área.
- **Sin certificado tradicional**: se mantiene el entregable de Doral (Certificado de
  participación INTEZIA + Workbook + Dashboard de progreso), consistente con una
  capacitación de equipo (a diferencia de una asesoría 1:1 como CAI-020).
- **Estructura actualizada al estándar vigente** (Doral es de 2026-08-04, previo a varias
  reglas): se retiró la slide de Metodología ABR y el bloque "Equipo facilitador" de
  Beneficios (§4.10a), se subió Beneficios al formato v3 (oscuro, 4 tarjetas), se agregó
  Cierre tipo escalera, se corrigió el correo de cierre a `servicio@intezia.com` y se quitó
  el enlace a Calendly del CTA (memoria `sin-calendly-en-cierre.md`).

## Impacto (§4.9) — reutilizado de Doral, mismo eje temático (Copilot)

- **Microsoft — Work Trend Index Special Report, "What Can Copilot's Earliest Users Teach Us
  About Generative AI at Work?"** (noviembre 2023): 85% redacta un primer borrador más
  rápido, 75% encuentra información más rápido, 64% procesa menos tiempo el correo; 70% se
  reportó más productivo; usuarios de Copilot resumen una reunión perdida 4 veces más rápido.
  Mismo estudio ya usado en Doral (CAP-092) y BNC Bootcamp — el eje temático (adopción de
  Copilot) es idéntico, no se reinventa la cita.

## Equipo asignado

- **Facilitación**: consultor senior Intezia, perfil de adopción de Microsoft 365 / Copilot
  (sin nombrar en el deck, igual que Doral — se asigna al confirmar el kick-off).
- **Asesora comercial**: María Iribarren.

## Pendientes

- Confirmar fechas de arranque y si las 2 sedes corren en paralelo o de forma escalonada.
- Confirmar número exacto de participantes por sede (referencia: ~50 personas en 8 áreas,
  mismo dato que ALL-003, pero esta capacitación es de alcance general, no por área).
- Confirmar presupuesto y monto de la cotización (campos de precio vacíos, los llena ventas).
- Evaluar con el usuario si esta propuesta se presenta junto con ALL-003 o por separado.
