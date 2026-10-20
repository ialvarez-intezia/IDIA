# Brief · Fivenca · Servicio de Habilidades (CAI-039)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Fivenca
- **Slug**: `fivenca-cerebros-digitales`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-039`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Construcción guiada de 5 Cerebros Digitales (asistentes personales) con Claude (Projects, Skills y conectores) y el conocimiento de cada persona organizado como grafo en Obsidian, para 5 personas que Fivenca designe
<!--auto:inicio-->
- **Alcance**: 10 entregables en 5 Cerebros Digitales · 40 h de sesión · 4 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
<!--auto:fin-->
- **Estado**: `Enviada` (2026-10-06, por convención: terminado = enviado)
- **Asesora comercial**: María Iribarren · +58 414-0570056 · miribarren@intezia.com (datos de `fivenca-acompanamiento/` y `fivenca-agregado/`; el deck no lleva slide de cierre ni contacto). Confirmar que es la misma María.
- **Ficha Comercial Intezia**: no hay. Todo sale de la instrucción directa del usuario (5 Cerebros Digitales, 8 h cada uno, asesora María), de CAP-060 (contenido) y de CAI-027 y CAI-025 (estructura de grupo ×N).
- **fecha_arranque_deseada**: no se preguntó; sin esta respuesta no hay Calendario de inicio con fechas (semanas relativas al arranque).
- **resultados_esperados**: no se preguntó; el retorno va en modo método, sin cifras.

## Cuenta Fivenca (contexto interno, no va en el deck)

Fivenca (grupo financiero, servicios financieros y mercado de capitales) tiene 5 propuestas previas: CAP-039 (plan integral, deck legacy), `fivenca-claude-express` (2 h, solo Claude), CAP-061 (Fundamentos de IA, 6 h), CAP-062 (acompañamiento de 3 meses para un grupo selecto) y CAP-105 (ampliación de 5 h para la directiva). Todas Educación y sin alianza. Opera sobre Microsoft 365, pidió no anclar las propuestas a ese ecosistema y no usa Copilot como su IA (§4.11: contexto interno, no se afirma ni se contradice en el deck). En CAP-062 el enfoque fue «nosotros guiamos, el equipo construye»; aquí se mantiene: cada persona construye su cerebro y Intezia lo guía.

## Plan de sesiones (por persona, tracks individuales ×5)

| Sesión | Semana | Contenido (base: CAP-060) | Entrega |
|---|---|---|---|
| 1 · 2 h | 1 | Qué es un Cerebro Digital, fundamentos de Claude, anatomía del prompt, contexto, rol y voz, iteración y verificación. Propósito del cerebro. Línea base del tiempo de sus tareas repetitivas | Propósito definido y un caso real resuelto |
| 2 · 2 h | 2 | Projects (memoria y contexto), conocimiento propio en Obsidian como grafo de notas, voz y criterio | Project de Claude con su conocimiento y su grafo |
| 3 · 2 h | 3 | Qué es una Skill y cómo se construye; conectores, plugins y Cowork; conexión de Obsidian al cerebro (MCP, Model Context Protocol) | Skill funcional y cerebro conectado |
| 4 · 2 h | 4 | Automatización de un proceso real; privacidad y uso seguro de la información; ajuste final y plan de puesta en marcha | Automatización conectada y criterio de uso seguro |

Las 2 h extra respecto de CAP-060 (3 sesiones, 6 h) salen de dividir su sesión 3, que concentraba conectores, MCP, automatización y uso seguro en 2 h. Por semana: 5 sesiones de 2 h (una por persona) = 10 h de sesión, bajo el tope de 20 h. Total: 5 × 8 h = 40 h, más 1 h de kick-off aparte.

## Qué ve el equipo comercial (puntos para la conversación con el cliente)

- **8 h por cerebro contra la tarifa de referencia de 6 h** (CAI-025 y CAI-027): son 10 h más en total (40 h contra 30 h). Es decisión del usuario; ventas lo cotiza.
- **Personas por designar:** el deck no nombra cargos ni personas; el kick-off de 1 h es donde Fivenca las define.
- **Licencias:** cada persona necesita su cuenta de Claude. El deck no afirma un plan ni un precio porque no hay un precio de lista verificado.
- **Sin certificado** por defecto (§4.21): CAP-060 y CAI-027 sí entregaban constancia de participación.

## Origen y fuente

- **Origen**: Instrucción directa del usuario del 06/10/2026 (5 Cerebros Digitales de 8 h cada uno, asesora María). Base de contenido: CAP-060 (Crea tu Clon Digital con Claude). Referencias de estructura: CAI-027 (Banco Activo) y CAI-025 (Banco Plaza). Sin Ficha Comercial
- **Fuente del insumo**: Instrucción directa del usuario; contenido de CAP-060
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Código CAI-039: siguiente libre (el usuario no dio código; se buscó en todo el repositorio y no aparece). División Educación y alianza «no» inferidas de las 5 propuestas anteriores de Fivenca (CAP-039, CAP-061, CAP-062, CAP-105 y el express: todas Educación, sin alianza). Asesora María Iribarren, la misma de CAP-062 y CAP-105: confirmar que es ella.
- Pedido del usuario (06/10/2026): 5 Cerebros Digitales de 8 h cada uno, 40 h en total. Excede en 2 h por cerebro la tarifa de «Excepción — Cerebros Digitales» (6 h por cerebro, `empresa/politicas-comerciales.md`, caso CAI-025 y CAI-027) y queda dentro del rango de la regla general (8 a 12 h por área). Decisión del usuario; no se mezclan ambas reglas.
- Respuestas del usuario (06/10/2026): un cerebro por persona, personas a designar por Fivenca; 4 sesiones de 2 h por persona; versión sin terminal (Claude con Projects, Skills y Obsidian, sin Claude Code). Base de contenido CAP-060 (Crea tu Clon Digital con Claude) y CAI-027 como referencia de grupo ×N; formato compacto elegido por el usuario al preguntarle la guardia de §4.21 punto 5.
- Reexpresión al compacto (guardia §4.21 punto 5): cada Cerebro Digital es un «área» de 8 h con 2 entregables de 4 h: (1) Project de Claude y grafo en Obsidian (sesiones 1 y 2: fundamentos, propósito, Project y grafo) y (2) Skill y automatización conectada (sesiones 3 y 4). Las 2 h extra respecto de CAP-060 reparten su 3.ª sesión (conectores, MCP, automatización y uso seguro) en dos. Es un reparto propuesto por el sistema: confirmar con servicio.
- Tracks individuales (como CAI-025 y CAI-027): cada persona tiene sus 4 sesiones, no un grupo de 5. Si Fivenca prefiere sesiones en conjunto, cambian las horas de sesión y el reparto.
- Calendario propuesto por el sistema: 4 semanas, una sesión por persona y por semana (5 sesiones y 10 h a la semana, bajo el tope de 20). Fase 1 en las semanas 1 y 2, fase 2 en las 3 y 4. CAI-027 corrió los tracks de forma secuencial en unas 9 semanas; aquí van en paralelo. Confirmar disponibilidad con Fivenca.
- Kick-off de 1 h aparte, sin horas (como CAI-034, CAI-037 y CAI-038): el usuario no lo pidió, es la convención del sistema. Sirve para acordar las 5 personas y sus casos reales.
- Sin Ficha Comercial: los 3 hechos de portada son de contenido (5 cerebros, 8 h, el grafo), no del cliente. Ningún dato de las otras propuestas de Fivenca se afirma en el deck: su entorno Microsoft 365 y que no use Copilot son contexto interno (§4.11); no se afirma que adopte Claude ni que cambie de stack.
- «Project», «Skill» y «grafo» van glosados en cada slide donde aparecen (§4.12). MCP no aparece en el deck, solo en programa.md con su expansión. Los nombres de los entregables llevan la glosa corta entre paréntesis.
- Línea base del tiempo de las tareas repetitivas: se levanta en la sesión 1 de cada persona. Confirmar con servicio que cabe en 2 h.
- Retorno en modo método: sin datos del cliente no hay cifras. «Hacia la semana N» es aritmética (4 semanas de trabajo + 13): confirmar con servicio.
- Sin certificado de participación por defecto (§4.21). CAP-060 y CAI-027 lo incluían (constancia por participante): confirmar si Fivenca lo quiere.
- Licenciamiento: cada persona necesita su cuenta de Claude, con un plan que permita construir su cerebro (el deck no afirma un plan ni un precio: no hay precio de lista verificado). Quién paga las licencias queda para ventas y Fivenca.
- Tras generar el deck se amplió la escala tipográfica de las slides 2, 3 y 5 en `overrides.css` y el catálogo de la slide 5 va en 2 columnas (`columnas_por_carril: [2]`), porque 10 entregables dejaban media slide vacía (la plantilla está pensada para 40+).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas). 40 h de sesión: 10 h por encima de la referencia de 6 h por cerebro (30 h) de CAI-025.
- Quiénes son las 5 personas y si ya tienen cuenta de Claude. Si algunas pertenecen al grupo selecto de CAP-062 o a la directiva de CAP-105, ajustar los fundamentos de la sesión 1.
- Fechas, modalidad y disponibilidad semanal de las 5 personas (no están en el deck); confirmar el kick-off.
- Confirmar con servicio el reparto de las 8 h en 4 sesiones y que la línea base cabe en la sesión 1.
- Fivenca es un grupo financiero: confirmar con ellos qué información de su trabajo puede cargarse en un cerebro (la sesión 4 trata el uso seguro, pero la regla la fija Fivenca).
- Confirmar si Fivenca quiere certificado de participación.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py fivenca-cerebros-digitales      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh fivenca-cerebros-digitales             # verifica, genera el PDF y ajusta los campos
```
