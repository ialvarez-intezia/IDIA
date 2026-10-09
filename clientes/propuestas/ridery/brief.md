# Brief · Ridery · Servicio de Habilidades (CAI-043)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Ridery
- **Slug**: `ridery`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-043`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construcción guiada de 5 Cerebros Digitales (asistentes personales) con Claude (Projects y Skills) y el conocimiento de cada persona organizado como grafo en Obsidian, para 5 personas que Ridery designe
<!--auto:inicio-->
- **Alcance**: 15 entregables en 5 Cerebros Digitales · 30 h de sesión · 3 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Carolain Fernandez, Directora de PR & Partnerships · COO de Intezia Foundation · +58 424 2536174
<!--auto:fin-->
- **Estado**: `Enviada` (2026-10-08; terminado = enviado, §4.19)
- **Ficha Comercial Intezia**: no hay. Todo sale de la instrucción directa del usuario del 2026-10-08 (código, 5 Cerebros Digitales de 6 h, contacto). Por eso la portada no afirma ningún dolor de Ridery.
- **fecha_arranque_deseada**: no indicada; sin Calendario de inicio (no se inventa)
- **resultados_esperados**: no indicados; sin ROI (no se inventa)

## Origen y fuente

- **Origen**: Instrucciones directas del usuario, 08/10/2026 (código CAI-043; 5 Cerebros Digitales de 6 h cada uno; contacto: Carolain Fernandez, de Intezia). Base de contenido: CAI-040, CAI-042 y CAI-039. Sin Ficha Comercial
- **Fuente del insumo**: Instrucción directa del usuario (sin Ficha Comercial)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Alcance (instrucción del usuario, 2026-10-08): 5 Cerebros Digitales de 6 h cada uno, 30 h en total. 6 h es la tarifa de referencia del Cerebro Digital (política de «Excepción — Cerebros Digitales»), así que no hay diferencia que avisar a ventas. Sin Ficha Comercial ni Levantamiento: no hay datos de Ridery.
- Quiénes son los 5: se supone un cerebro por persona, con 5 personas que Ridery designa (patrón de Fivenca CAI-039; los cerebros se llaman «Cerebro Digital 1» a «5»). Si en cambio son 5 cerebros por función o por equipo, el diseño cambia (sistema por funciones, no asistente personal) y hay que rehacer los entregables.
- Contenido de las 3 sesiones: propuesta del sistema a partir de CAP-060, CAI-039 y CAI-042 (Fundamentos y Project, grafo en Obsidian, Skill y plan de uso). Con 6 h no caben las 4 sesiones de Fivenca ni la automatización de un proceso: la tercera sesión cierra con una Skill de una tarea real y su plan de uso.
- Calendario propuesto por el sistema: 3 semanas, una sesión de 2 h por persona y por semana (10 h por semana de trabajo de Intezia), más 1 h de kick-off aparte. Servicio debe confirmarlo; modalidad, fecha de arranque y horarios quedan por acordar.
- Acceso a Claude: Ridery es una empresa venezolana (según su presencia pública, con operación también en Panamá y República Dominicana) y Venezuela no figura entre los países soportados de Anthropic. El deck no promete usar Claude con VPN ni dice que sea seguro; dice que el acceso depende del país y que se confirma en el kick-off, dentro de las condiciones del proveedor. No se nombra un respaldo (como Gemini en la DET-028) porque no se sabe qué herramientas usa Ridery. Ver la memoria «claude-no-soportado-en-venezuela-no-prometer-vpn».
- Obsidian entra por ser el estándar del patrón Cerebro Digital (gratuito, se instala en la segunda sesión). Las licencias de Claude van aparte y las confirma Ridery con el proveedor; no se afirma quién las contrata ni se escribe un valor de lista.
- Hoja de inversión estándar (sin «Valor por parte»: preferencia del usuario del 2026-10-08), con montos vacíos para ventas; sin facilidad de pago (por defecto en las propuestas v2; no se preguntó). Garantía 30-60-90; sin certificado.
- Los 3 datos de la portada son de contenido del proyecto (5 cerebros, 6 h, grafo), no hechos de Ridery: no se afirma ningún dolor ni proceso de la empresa.
- División Educación y sin alianza (supuesto, igual que la DET-030: no se preguntó).
- Contacto de la última slide (instrucción del usuario: «igual colocas a carol como contacto»): Carolain Fernandez, de Intezia, que no es asesora comercial; etiqueta «Escribe a tu contacto en Intezia». Se tomó que «Carol» es Carolain Fernandez de la DET-030. Sin correo (no se tiene): la slide muestra su teléfono y servicio@intezia.com.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md y CLAUDE.md §4.21)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo y en qué plazo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos. Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso.
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Confirmar que «Carol» es Carolain Fernandez y su correo, para la última slide.
- Confirmar si los 5 cerebros son uno por persona (5 personas a designar) o por función, y quiénes son.
- Definir cómo se trata el acceso a Claude desde Venezuela (verificación en el kick-off, respaldo con otra herramienta) y qué herramientas usa Ridery hoy.
- Definir inversión, descuento y total: ventas llena las tres cajas, que van vacías (30 h en total). Decidir si lleva facilidad de pago.
- Confirmar con servicio el calendario de 3 semanas, la modalidad y la fecha de arranque.
- Confirmar con Ridery qué información de sus personas puede cargarse en un cerebro y si ya tienen cuenta de Claude.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py ridery      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh ridery             # verifica, genera el PDF y ajusta los campos
```
