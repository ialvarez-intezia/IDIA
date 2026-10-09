# Brief · Universal de Seguros · Servicio de Detección y Habilidades (DET-030)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Universal de Seguros
- **Slug**: `universal-de-seguros`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección + Habilidades · 4 áreas priorizadas · Detección: 4 áreas de 4h = 16h · Habilidades: 4 áreas de 12h = 48h · 64h totales · equipo de 50 personas · seguimiento 30-60-90 · formato compacto v2 (`DET-030`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Auditar 4 áreas priorizadas de Universal de Seguros, con un logro inmediato en cada una, y construir con el equipo la solución prioritaria de cada área, hasta dejarla en uso, con medición del tiempo recuperado a 30, 60 y 90 días
<!--auto:inicio-->
- **Alcance**: 8 entregables en 4 áreas · 64 h de sesión · 7 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Carolain Fernandez, Directora de PR & Partnerships · COO de Intezia Foundation · +58 424 2536174
<!--auto:fin-->
- **Estado**: `Enviada` (2026-10-08; terminado = enviado, §4.19)
- **Ficha Comercial Intezia**: no hay. Todo sale de la instrucción directa del usuario del 2026-10-08 (código, equipo de 50 personas, 4 áreas priorizadas, horas y contacto). Por eso las áreas no tienen nombre y la portada no afirma ningún dolor del cliente.
- **fecha_arranque_deseada**: no indicada; sin Calendario de inicio (no se inventa)
- **resultados_esperados**: no indicados; sin ROI (no se inventa)

## Origen y fuente

- **Origen**: Instrucciones directas del usuario, 08/10/2026 (código DET-030; equipo de 50 personas; 4 áreas priorizadas sin nombrar; Detección 4 h por área y Habilidades 12 h por área; contacto: Carolain Fernandez, de Intezia). Sin Ficha Comercial ni Levantamiento
- **Fuente del insumo**: Instrucción directa del usuario (sin Ficha Comercial)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Alcance y horas (instrucción del usuario, 2026-10-08): combo Detección + Habilidades para un equipo de 50 personas. Detección: 4 áreas priorizadas × 4 h = 16 h. Habilidades: 12 h por área × 4 = 48 h. Total 64 h. Sin Fundamentals (no se pidió; el lineamiento lo trae de 2 h): si se quiere nivelar a las 50 personas, se agregan 2 h por grupo de hasta 25 (2 grupos).
- Sin Ficha Comercial ni Levantamiento: no hay datos del cliente. Las 4 áreas se llaman «Área priorizada 1» a «Área priorizada 4» (instrucción del usuario: «déjalo como área priorizada porque no tengo más información»). Los 4 datos de la portada son de contenido del proyecto (horas, personas, seguimiento), no hechos del cliente, y no se afirma ningún dolor ni proceso. Cuando se conozcan las áreas, se cambian los nombres y los `para_que` en datos.json y se regenera.
- Los 4 `para_que` son idénticos a propósito: sin información del cliente no se puede decir qué resuelve cada área. Se reemplazan por frases propias de cada área en cuanto existan.
- Equipo de 50 personas (instrucción del usuario): no se sabe cuántas están en cada área ni si son todo el equipo de las 4 áreas. El deck dice «el equipo de 50 personas; cada área define quiénes participan en sus sesiones».
- Calendario propuesto por el sistema, no dictado por el usuario: 7 semanas. Semanas 1 y 2: kick-off y Detección (dos áreas por semana, 4 h cada una). Semana 3: Reporte Final y priorización, trabajo de Intezia sin sesiones. Semanas 4 a 7: Habilidades, una área por semana, 12 h repartidas en tres sesiones de 4 h. Servicio debe confirmarlo; modalidad, fecha de arranque y horarios quedan por acordar con el cliente.
- Reporte Final, Mapa de Calor, Índice de Madurez y recomendación de ecosistema de IA: entregables estándar de las propuestas de Detección anteriores (DET-023, DET-027); no los pidió el usuario para esta.
- Hoja de inversión estándar (instrucción del usuario, 2026-10-08): sin cajas de «Valor por parte»; solo Propuesta + Inversión, Descuento y TOTAL, vacíos para ventas. Una primera versión llevaba dos cajas, «Detección» y «Habilidades», como la CAI-032; se quitaron. Facilidad de pago omitida (por defecto en las propuestas v2): no se preguntó.
- Habilidades lleva garantía 30-60-90 (por defecto del servicio). La Detección no lleva certificado.
- Herramienta de IA sin definir: ni se nombra ni se afirma el stack del cliente (§4.11). El deck dice que la define el Reporte Final y que la licencia va aparte.
- Datos sensibles (propuesta del sistema por tratarse de una aseguradora): las sesiones se hacen con procesos y ejemplos armados o anonimizados, sin información de asegurados ni de clientes. Confirmar con el área de Tecnología del cliente cuando exista un contacto.
- División Educación (el usuario escribió «educacion» al dar los datos de contacto) y sin alianza (supuesto: no se contradijo cuando se preguntó).
- Contacto de la última slide (instrucción del usuario): Carolain Fernandez, de Intezia, que no es asesora comercial. La etiqueta de la tarjeta dice «Escribe a tu contacto en Intezia». Cargo tal como lo dio el usuario: «Directora de PR & PARTNERSHIPS / COO Intezia Foundation», con el formato normalizado. Teléfono +58 424 2536174. No se dio correo: la slide muestra el teléfono y el correo general de servicio@intezia.com. Para esto se agregaron al generador dos claves opcionales: `proximos_pasos.etiqueta_contacto` y correo opcional si hay teléfono.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md y CLAUDE.md §4.21)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo y en qué plazo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos. Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Reporte Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso.
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Nombres reales de las 4 áreas, qué resuelve cada una y quién del cliente las prioriza (sin Ficha, el deck es genérico).
- Correo de Carolain Fernandez para la última slide, y confirmar su cargo tal como se imprime.
- Definir inversión, descuento y total: ventas llena las tres cajas, que van vacías (Detección 16 h y Habilidades 48 h, 64 h en total). En Adobe Reader el total se calcula solo; Preview no calcula. Decidir si lleva facilidad de pago.
- Confirmar con servicio el calendario de 7 semanas, la modalidad, la fecha de arranque y si las 50 personas participan en las sesiones.
- Decidir si se agrega nivelación (Fundamentals) para las 50 personas: no está en las 64 h.
- Confirmar con el cliente la regla de datos sensibles (ejemplos armados o anonimizados) y la herramienta de IA que usarán.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py universal-de-seguros      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh universal-de-seguros             # verifica, genera el PDF y ajusta los campos
```
