# Brief · Médica Campestre · Servicio de Habilidades (CAI-095)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Médica Campestre
- **Slug**: `medica-campestre-cai095`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-095`), presentada al cliente como **propuesta de proyecto**; formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Clon Digital con Claude para 17 directivos y gerentes de Médica Campestre y Proquimed, construido en parejas del mismo cargo entre ambas empresas, con medición Edu-Pulse y Edu-Trace
<!--auto:inicio-->
- **Alcance**: 18 entregables en 9 cargos · 72 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Facilidad de pago · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Instrucciones de Ivana del 12/11/2026: problema (todos los directivos ya usan IA, no todos bien), mismo modelo del CAP-075, 17 personas en parejas del mismo cargo, Clon Digital y medición con Edu-Pulse y Edu-Trace, cronograma flexible, 3 cuotas
- **Fuente del insumo**: Instrucciones pegadas por Ivana (sin Ficha Comercial ni transcripción de la reunión); propuesta anterior de la cuenta, CAP-075, solo como referencia del modelo
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Servicio y cuenta (instrucciones de Ivana, 12/11/2026): Habilidades, plantilla compacta v3, código CAI-095, contacto María Iribarren (directora comercial). División Educación y sin alianza: tomados de la cuenta (CAP-075, Educación, sin aliado); por confirmar.
- Participantes: 17 personas, 8 de Médica Campestre y 9 de Proquimed, de nueve cargos (médica, administrativa, comercial, recursos humanos, IT, compras, operaciones, contabilidad y calidad). Con 8 + 9 sale **un cargo con una sola persona**, sin contraparte (la fuente no dice cuál). Se dejó como un cargo más, con las mismas 8 h; la alternativa es sumarlo como tercero a la pareja del cargo más cercano (8 grupos y 64 h).
- Horas por pareja (mía, a confirmar): **8 h por cargo** = kick-off de 2 h + construcción de 6 h en tres encuentros de 2 h (cómo funciona Claude y arquitectura del Clon, construcción del Clon, prueba y ajuste). Total 9 cargos × 8 h = 72 h (18 h de kick-off y 54 h de construcción). Referencia del CAP-075: 6 sesiones de 2 h, de las cuales 3 eran de Clon; aquí no hay fundamentos básicos ni Claude Code ni app propia. Las 6 h de construcción son compartidas por la pareja: cada persona construye su propio Clon en el mismo encuentro.
- Esquema de encuentros: Ivana pidió el esquema de sesiones en la propuesta, lo que es una excepción a la regla de Keiber (§4.23). Se escribe «encuentros», sin días, fechas ni semanas. El horario de cada pareja se acuerda en su kick-off.
- Cronograma flexible (Ivana): kick-offs de las parejas este año con una primera cuota y encuentros de construcción según la agenda de cada pareja. Intezia sale de vacaciones el 15 de diciembre y vuelve la segunda semana de enero: en el deck se dice «antes del cierre de año de Intezia» y «desde mediados de enero» (sin fechas).
- Cuotas (mías, a confirmar): 40 % al aprobar (kick-offs), 30 % cuando la mitad de las parejas tiene sus Clones listos y 30 % al cierre con todos los Clones y la medición. Los montos quedan como campos vacíos para ventas.
- Medición: Edu-Pulse (anónimo, después de cada encuentro) y Edu-Trace (de cierre, personal) con el Dashboard de Impacto, como en el CAP-075. Es autopercepción salvo el bloque de conocimientos (§4.17): la propuesta no promete «mejora medida».
- Claude se nombra como herramienta del Clon (Ivana: «entender cómo funciona Claude»). Licencias fuera de la propuesta, sin valor de lista (no verificado para esta cuenta) y sin afirmar qué plan tienen. Sin afirmar que ya usan Claude ni qué herramientas de IA usan hoy (§4.11).
- Sin Ficha ni transcripción: los hechos de portada salen de lo que dijo Ivana de la reunión (17 personas, ya usan IA, distinto nivel). «Abusan de ella» no va al deck (sin dolor dramatizado); se dice distinto nivel y criterio. Sin nombres de personas del cliente.
- Hechos de contexto de la cuenta no verificados: país y moneda de Médica Campestre y Proquimed. La hoja de inversión sale con REF y la leyenda de pago a tasa BCV (automático); si facturan en otra moneda se apaga con `inversion.sin_ref`.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Confirmar con Ivana el enfoque del cuadro «Impacto» de «Lo que se llevan» (reenfoque, posiciones u operación). No se incluyó: el generador avisa.
- Confirmar cuál de los nueve cargos queda con una sola persona y si es un cargo más (72 h) o un tercero en otra pareja (64 h).
- Confirmar las 8 h por cargo (kick-off de 2 h + 6 h de construcción) y que el kick-off cuenta dentro de las horas y de la primera cuota.
- Confirmar división (Educación), alianza (no) y modalidad (online síncrono, como el CAP-075, o presencial).
- Confirmar si Proquimed debe aparecer en el titular de la portada (hoy solo en el lead y la logística) y quién contrata y factura: una empresa o cada una por separado.
- Confirmar quién contrata las licencias de Claude para los 17 y qué plan; no se afirma ninguno.
- Ventas llena inversión, descuento, total y los montos de las 3 cuotas antes de enviar.
- Confirmar que se da el 15 de diciembre y la segunda semana de enero como datos al cliente y no solo como límite interno.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py medica-campestre-cai095      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh medica-campestre-cai095             # verifica, genera el PDF y ajusta los campos
```
