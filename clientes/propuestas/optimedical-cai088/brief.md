# Brief · Optimedical · Servicio de Habilidades (CAI-088)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Optimedical
- **Slug**: `optimedical-cai088`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-088`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construcción guiada de un Cerebro Digital (asistente personal) con Claude y Obsidian para la socia y responsable de la operación de Optimedical: cotización estandarizada con envío y seguimiento, catálogo de cristales de laboratorios externos, manual de procesos vivo y una interfaz interna para el equipo
<!--auto:inicio-->
- **Alcance**: 5 entregables en 1 Cerebro Digital · 8 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Verónica Rubio (03/11/2026) y transcripción de la reunión del 03/11/2026 con Marling Duc; 8 h y formato dados por Ivana (05/11/2026)
- **Fuente del insumo**: Ficha de Levantamiento (03/11/2026) y transcripción de la reunión con Marling Duc (03/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (05/11/2026): propuesta de Habilidades CAI-088 para Optimedical (Marling Duc), asesora Verónica Rubio, con la ficha del 03/11/2026 y la transcripción de la reunión. Educación, sin alianza, 8 h y sin facilidad de pago: confirmados con Ivana. Si la transcripción y la ficha se contradicen, manda la transcripción (§4.23).
- Horas: 8 h con Marling (dadas por Ivana); el reparto es mío: base 1 h, grafo 2 h, cotización con envío y seguimiento 2 h, catálogo de cristales 2 h, interfaz del equipo y mantenimiento 1 h. Las horas son de encuentro con la cliente, no horas de trabajo de Intezia (§4.23); las horas de `datos.json` son marcadores técnicos. Sin «sesiones»: el calendario se acuerda en el arranque y, por el tiempo de Marling, en bloques cortos.
- Alcance: de las siete tareas que nombró, en las 8 h entran la cotización con seguimiento y post-consulta, el catálogo y las listas de laboratorios, el manual de procesos y la práctica de atención, el orden de pasos de las obligaciones del mes y la interfaz del equipo. El ingreso administrativo y su reporte para socios, los recordatorios que se envían solos y los envíos automáticos quedan fuera (el cerebro responde cuando se le pide) y se mencionan como tareas a explorar o etapa siguiente.
- Herramientas: Claude y Obsidian se nombran porque Marling los eligió como herramienta a incorporar (ficha) y Verónica se los mostró en la reunión. Marling ya usa Gemini, NotebookLM y ChatGPT gratuito: no se nombran. No se afirma que migre de herramienta (§4.11) ni se promete acceso a Claude desde Venezuela.
- Licencia: plan individual de Claude de USD 20 al mes, dicho por Verónica en la reunión (también mencionó uno de USD 100 para compartir, que no se recomienda aquí porque cada persona necesita su propio puesto). Sin verificación posterior: confirmar el valor vigente.
- Cifras: «más de 1.000 cristales» y «equipo de 5 personas» salen de la ficha y la transcripción; no hay volúmenes, tiempos ni valor de la hora, así que el retorno es por método. El comparativo con el costo de contratar una persona que usó Verónica no va en el deck: es argumento de venta, con cifras de ella.
- Hechos de la portada: salen de la ficha (procesos 3, 4 y 6). «Un Word que nadie consulta» sintetiza la cita de Marling sin ponerla entre comillas.
- El valor, el descuento y el total van vacíos para ventas. En la reunión se habló de 2.300 REF; la ficha indica que el piso del Cerebro Digital individual es 2.500 REF y que la cotización necesita aprobación de la directora comercial antes de enviarse: nada de esto va al deck.
- Marling pidió cuotas y la ficha dice «cuotas por avance del proyecto», pero Ivana decidió no incluir facilidad de pago.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Aprobación de la CCO antes de enviar (ficha, señal 2: valor por debajo del piso).
- Confirmar con Ivana el reparto de las 8 h, sobre todo si 1 h basta para la interfaz del equipo.
- Verificar el valor vigente de la licencia de Claude de USD 20 al mes.
- Confirmar si participan los socios en la decisión y quién estará en la presentación (ficha: por confirmar).
- Valor, descuento y total: campos vacíos para ventas; moneda de facturación por confirmar.
- Verónica enviaba la propuesta el jueves por la mañana (05/11/2026): coordinar la fecha con ella.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py optimedical-cai088      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh optimedical-cai088             # verifica, genera el PDF y ajusta los campos
```
