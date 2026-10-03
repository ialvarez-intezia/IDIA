# Brief — Grupo Ferrara · Dominio de IA para la Dirección (CAI-007)

> **Propuesta adicional e independiente** a la Detección de Grupo Ferrara
> (`clientes/propuestas/grupo-ferrara/`, DET-005) — mismo cliente, sin referencias cruzadas
> entre ambos documentos. Fuente primaria: Ficha de Levantamiento Intezia — Grupo Ferrara
> (2026-08-28, Verónica Rubio), Bloque específico · Habilidades.

## Referencia "Luis Vicente" — no encontrada, decisión tomada

El usuario pidió replicar "un esquema similar al que implementamos con Luis Vicente (visita
a domicilio y capacitación altamente personalizada)". Se buscó exhaustivamente en el
sistema (slugs de `clientes/propuestas/`, todos los `meta.json`, `brief.md`, HTML,
`clientes/INDEX.json/md`, `aprendizajes.md`, `aprendizajes-historico.md` y memoria
persistente) y **no existe ningún cliente "Luis Vicente" ni un caso documentado con ese
patrón exacto**. Se le preguntó al usuario cómo continuar; su respuesta ("es Grupo Ferrara
igual que la anterior DET-005") confirmó el cliente pero no resolvió la referencia
puntual — se avanzó con la opción recomendada:

- **Base estructural**: `dhl-cerebro-digital/` (CAI-005), el clon personalizado-ejecutivo
  más reciente del sistema (2026-08-30) — ya trae Beneficios v3, Cierre escalera y el
  campo `servicio` correctos.
- **Se descartó el concepto de producto "Cerebro Digital"** (Claude + grafo Obsidian) de
  ese clon: Ferrara no pidió ese producto específico, solo dominio general de IA aplicado
  al rol ejecutivo. Se quitó la slide a la medida `.s-graph`.
- **Único dato concreto de "Luis Vicente"** que el usuario dio (visita a domicilio +
  capacitación altamente personalizada) sí se aplicó: modalidad presencial con visita a
  domicilio en cada una de las 3 sesiones, mencionada en portada, Programa, Cronograma,
  Beneficios y Próximos pasos.
- **Si el usuario confirma después que "Luis Vicente" sí existe** (con otro nombre de
  carpeta, o en un sistema externo), revisar ese caso y ajustar este deck para alinearlo si
  hace falta.

## Datos administrativos

- **Empresa**: Grupo Ferrara (mismo cliente que DET-005)
- **Slug**: `grupo-ferrara-cai007` (carpeta separada de `grupo-ferrara/`, a pedido del
  usuario — "crea otra carpeta para esta propuesta")
- **División Intezia**: `educacion`
- **Servicio** (Modelo Intezia): `habilidades` — capacitación personalizada, no un servicio
  de Detección ni un combo con ella.
- **Alianza**: no
- **Código**: `CAI-007` (dado por el usuario; verificado libre: CAI-001 Cavedatos, CAI-002/
  CAI-003 Simple TV, CAI-004 Yoyokids, CAI-005 DHL, CAI-006 Miosoty).
- **Eje temático**: dominio ejecutivo de IA (Gemini y Claude) aplicado al rol directivo,
  para el dueño de Grupo Ferrara y su hijo.
- **Fecha del brief**: 2026-09-01
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
  (misma asesora que DET-005).
- **Participantes**: el dueño de Grupo Ferrara y su hijo — **sus nombres reales no están en
  la ficha** (solo se registró a Gabriela Arocena, Gerente de Marketing, como la persona que
  solicitó la propuesta en su nombre; ella no es una de las 2 participantes). El deck se
  refiere a "la Dirección" / "el dueño y su hijo" en todo el contenido, sin nombres propios.
  **Pendiente**: confirmar sus nombres reales antes de personalizar más el trato (portada,
  cierre) si el usuario lo pide.

## Contexto (Ficha, Bloque específico · Habilidades)

- **Qué debe poder hacer el equipo al terminar**: "dominar la IA para su rol de directores"
  y que los ayude "en su rol de gestión de toda la empresa" (cita de la ficha).
- **Quién solicitó la propuesta**: la gerente de Marketing (Gabriela Arocena), en nombre del
  dueño y su hijo — la ficha registra que ellos no tienen esta información con exactitud y
  quieren la propuesta en mano para poder hablar con Intezia directamente.
- **Modalidad preferida**: Presencial (ficha) → interpretada como visita a domicilio, según
  instrucción del usuario.
- **Duración y frecuencia**: sesiones de 2 horas (ficha) → 3 sesiones de 2h, 6h en total
  (mismo patrón que el clon de referencia dhl-cerebro-digital, ajustado a 2 participantes).
- **Uso esperado post-formación**: medir a 30 y 60 días (ficha) — no hay actualmente un
  flujo de Dashboard de Impacto para capacitaciones personalizadas de 1-2 participantes;
  queda como nota, no se construyó nada al respecto en esta pasada.
- **Cómo sabrán que valió la pena**: "si logran integrar la guía en su día a día como rol de
  directores ejecutivos" (cita de la ficha) — reflejado en el objetivo general del deck.
- **Contexto ya usado en DET-005** (mismo Ficha, reutilizado aquí sin duplicar investigación):
  ecosistema no definido, información en varios sistemas separados por área, uso de Gemini
  y Claude sin coordinación, ~10 personas involucradas (gerentes y directores) en general —
  aquí el foco se acota a 2 de esas personas: el dueño y su hijo.

## Restricciones de copy

1. **Sin nombres propios** del dueño ni de su hijo (no están en la ficha).
2. **Sin presupuesto** ni condiciones de pago en el deck (§4.15) — cotización vacía, la
   llena ventas.
3. **§4.11**: no se afirma que Grupo Ferrara migra o adopta un nuevo stack — Gemini y Claude
   son su entorno actual.
4. **Sin combo ni mención de Detección**: este deck es Habilidades puro, independiente de
   DET-005 (mismo criterio que dhl-cerebro-digital/dhl).

## Notas de diseño

- Base estructural: `dhl-cerebro-digital/` (CAI-005) — 3 módulos/6h, 1 slide de cronograma
  por sesión con componente `.ruta` (en vez del cronograma de una sola slide que usa
  DET-005/embutidos-zeus), Beneficios v3, Cierre escalera. Se quitó la slide a la medida
  `.s-graph` y el concepto "Cerebro Digital" — no aplican aquí. 12 slides (13 del clon menos
  `.s-graph`).
- **Impacto (§4.9)**: se reutilizan las mismas fuentes reales y ya citadas de
  dhl-cerebro-digital (Stanford HAI — AI Index Report 2026, McKinsey — The State of AI 2025,
  Anthropic Economic Index 2025) — son datos generales de productividad con IA, aplicables
  al mismo eje temático (dominio ejecutivo de IA), no específicos de una audiencia que
  justifique una nueva búsqueda.
- **"Visita a domicilio"**: interpretado como que el consultor de Intezia se traslada a las
  instalaciones/domicilio del cliente para cada una de las 3 sesiones (en vez de sesiones
  virtuales o en oficinas de Intezia). No se especifica la dirección exacta — queda para
  confirmar en el arranque (Paso 02 de "Cómo arrancamos").
- **Correo de cierre**: `servicio@intezia.com` (estándar del sistema).

## Actualización 2026-09-03 — se incorpora el concepto "Cerebro Digital"

Instrucción del usuario: reconsiderar si el producto **Cerebro Digital** (Claude + grafo
relacional en Obsidian, el mismo concepto retirado en la construcción original de este
deck — ver sección inicial de este brief) tiene sentido aquí, dado que esta propuesta es
exactamente el vehículo separado para contenido ejecutivo personalizado de Grupo Ferrara.

**Decisión: sí se incorpora, como Cerebro Digital *compartido* para la Dirección** — no un
Cerebro Digital por persona (opción descartada: el dueño y su hijo comparten una sola IA con
el contexto de la empresa, no 2 instancias personalizadas cada uno). Esto es una diferencia
deliberada frente a `dhl-cerebro-digital/` (CAI-005), donde Miguel es 1 participante con su
propio Cerebro Digital individual.

- **Slide a la medida `.s-graph`** ("Su segundo cerebro", grafo relacional en Obsidian) se
  reincorpora, adaptada a "la Dirección" en plural (sin nombrar a ninguno de los dos
  individualmente) — copiada de `dhl-cerebro-digital/index.html` + su CSS en
  `overrides.css`. Insertada como slide 5, entre Programa y Cronograma (mismo lugar que en
  el clon de origen). El deck pasa de 12 a **13 slides**.
- **Módulo II** renombrado de "IA aplicada a la gestión diaria" a **"El Cerebro Digital de la
  Dirección"** (construcción del grafo de conocimiento con Projects + Obsidian). **Módulo
  III** renombrado de "Un método propio y sostenible" a **"El Cerebro Digital en acción"**
  (mismo contenido: automatización, conectores, privacidad, plan de continuidad — solo
  cambia el nombre para reflejar que es la puesta en marcha del Cerebro Digital, no un
  concepto aparte).
- **Objetivos, Beneficios, Entregables, Cierre**: se ajustó el copy para nombrar el Cerebro
  Digital como el entregable central de la propuesta (antes era "un método propio" sin
  nombre de producto).
- **Duración sin cambios**: sigue siendo 3 módulos / 6h / 2 participantes — el Cerebro
  Digital se construye dentro de las mismas 3 sesiones ya cotizadas, no agrega sesiones.
- Estado del `meta.json` vuelve a `En corrección` (la propuesta ya estaba `Enviada`); al
  regenerar el PDF regresa a `Enviada` automáticamente (§4.19).

## Pendientes

- Confirmar los nombres reales del dueño y su hijo.
- Confirmar la dirección exacta de las visitas a domicilio.
- Confirmar fechas tentativas de las 3 sesiones.
- Confirmar presupuesto (ficha: "en evaluación").
- Aclarar si "Luis Vicente" existe en algún otro sistema o con otro nombre de cliente —
  si aparece, revisar este deck para alinearlo con ese precedente real.
