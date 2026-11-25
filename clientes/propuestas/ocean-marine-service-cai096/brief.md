# Brief · Ocean Marine Service International LLC · Servicio de Habilidades (CAI-096)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Ocean Marine Service International LLC
- **Slug**: `ocean-marine-service-cai096`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-096`), presentada al cliente como **propuesta de proyecto**; formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Agente de IA que procesa requerimientos de compra recibidos por correo, consulta el historial de Odoo v18 en solo lectura y presenta comparativos con recomendación para aprobación del equipo de Stores
<!--auto:inicio-->
- **Alcance**: 13 entregables en 4 bloques · 100 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Requerimiento escrito del cliente (pegado por Ivana el 12/11/2026) e instrucciones de Ivana: desarrollo en casa, luego adaptación y pruebas con el equipo; 40 h con la construcción sin el equipo; enfoque de Impacto: operación; asesora Flavia Martínez
- **Fuente del insumo**: Documento de requerimiento de OMS (alcance de recepción, Odoo, validación, proveedores, comparativos, catálogo y control) sin Ficha Comercial ni transcripción de la reunión
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Servicio y cuenta (instrucciones de Ivana, 12/11/2026): Habilidades, plantilla compacta v3, Educación y sin alianza (confirmados con Ivana). Código **CAI-096**: Ivana lo pidió bajo CAI-095, que ya se usó para Médica Campestre; ella aceptó CAI-096 para Ocean Marine Service.
- **Una sola opción, no dos (Ivana, 12/11/2026):** el requerimiento pedía presentar ambas formas (construir en conjunto, o levantar, desarrollar en casa y adoptar); Ivana respondió «en este caso no construimos en conjunto, hacemos el desarrollo en casa y luego junto con ellos adaptamos y testeamos». El deck presenta solo esa ruta. Si se quiere mostrar también la construcción en conjunto, se agrega como una segunda hoja de inversión (`inversion.etapas`).
- Horas (Ivana: «40 h, pero la construcción es sin ellos, lo demás lo distribuyes»): **40 h en total**, de las cuales **24 h son de desarrollo de Intezia sin el equipo** (no se muestran, §4.23 punto 4) y **16 h con el equipo de Stores**, repartidas por mí: levantamiento 4 h, adaptación 4 h, pruebas con requerimientos reales 4 h y adopción, documentación y accesos 4 h. Las 24 h se reparten internamente entre los seis módulos del agente (4, 4, 4, 4, 6 y 2 h). El deck dice «16 horas con el equipo» escrito a mano (no usa `{h_total}`, que sumaría las 40).
- Alcance: sale del requerimiento de OMS, sin agregar nada. Recepción (correo y adjuntos Excel, PDF e imágenes, inglés y español), conector de solo lectura a Odoo v18, validación en cuatro clases, proveedores y solicitudes de cotización, comparativo por artículo y combinación recomendada con Excel, fichas de producto nuevo con base de conocimiento, y control (aprobaciones, pendientes, accesos y registro). La primera fase no escribe en Odoo, no envía correos ni emite órdenes.
- Sin herramienta de IA nombrada: el requerimiento no la define; se acuerda en el levantamiento. Odoo v18 se nombra como entorno del cliente al que el agente se integra (§4.11); no se afirma migración. La viabilidad del conector depende del alojamiento y los accesos: el requerimiento pide confirmarla y el deck la deja para el levantamiento.
- El requerimiento pide también arquitectura, costos de desarrollo, operación y mantenimiento, seguridad y soporte: el deck cubre seguridad (solo lectura, accesos restringidos y registro) y deja la **operación y el mantenimiento posteriores como cotizados aparte** (supuesto mío). La arquitectura detallada se presentará en vivo.
- Pago: plan estándar de la política comercial (50 % al aprobar, 50 % al cierre) ligado a hitos; los montos quedan como campos vacíos. Seguimiento 30-60-90 por defecto.
- El requerimiento no dice país, moneda ni modalidad de OMS (LLC): la hoja de inversión sale con REF y la leyenda de pago a tasa BCV (automático); se apaga con `inversion.sin_ref` si facturan en otra moneda. Sin nombres de personas del cliente (solo el cargo del Director de Logística).
- Impacto (Ivana, 12/11/2026): enfoque **operación**; texto sin cifras.

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

- Confirmar la viabilidad del conector de solo lectura según el alojamiento de Odoo v18 (propio o alojado) y los accesos y permisos disponibles; se aclara en el levantamiento o antes, en la presentación en vivo.
- Confirmar con Ivana si la propuesta lleva también la construcción en conjunto como segunda opción (el requerimiento la pedía).
- Confirmar las 40 h (24 h de desarrollo sin el equipo y 16 h con el equipo) y el reparto de las 16 h.
- Confirmar si la operación y el mantenimiento posteriores se cotizan aparte y si hay que ponerles valor; y los servicios que OMS contrata (modelo de IA, correo, alojamiento).
- Confirmar modalidad (remota o presencial), moneda de facturación y país de OMS.
- Preparar la presentación en vivo de la arquitectura (correo → agente → Odoo en solo lectura → comparativo en pantalla y Excel → aprobación humana).
- Ventas llena inversión, descuento, total y los montos de las 2 cuotas antes de enviar.
- Reasignar el código en el registro si Médica Campestre vuelve a pedirlo.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py ocean-marine-service-cai096      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh ocean-marine-service-cai096             # verifica, genera el PDF y ajusta los campos
```
