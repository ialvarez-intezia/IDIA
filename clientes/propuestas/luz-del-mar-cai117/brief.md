# Brief · Luz del Mar · Servicio de Habilidades (CAI-117)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Luz del Mar
- **Slug**: `luz-del-mar-cai117`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-117`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construir con el equipo de Luz del Mar tres agentes de IA conectados entre sí (cálculo de impuestos de valoración, gestión de tráfico con rastreo en las navieras y cotización) y dejar al equipo en capacidad de entenderlos y mantenerlos
<!--auto:inicio-->
- **Alcance**: 14 entregables en 4 áreas · 80 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana (23/11/2026): propuesta de Habilidades para Luz del Mar a partir de la Ficha de Levantamiento del 20/11/2026, el resumen de Verónica y la transcripción de su reunión con la dueña (50 min). Asesora: Verónica Rubio
- **Fuente del insumo**: Ficha de Levantamiento (20/11/2026), resumen de la asesora y transcripción de la reunión del 20/11/2026
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (23/11/2026): propuesta de Habilidades CAI-117 para Luz del Mar (agencia de aduanas en Puerto Cabello, primer contacto). Asesora: Verónica Rubio.
- Decisiones de Ivana: 80 h, impacto «operación», sin nombrar herramienta de IA ni licencias, sin facilidad de pago. División Educación y sin alianza: supuesto mío, no se preguntó (confirmar).
- Reparto de las 80 h mío: 20 h por agente (Valoración 6, 8 y 6; Tráfico 5, 9, 4 y 2; Cotización 6, 9 y 5) y 20 h de conexión y traspaso (8, 4, 4 y 4).
- Orden de las fases por dependencia (no el de la ficha): Valoración primero porque su cálculo alimenta a Tráfico y a Cotización; la conexión de los tres cierra.
- Sin nombres de personas del cliente, del valorador externo ni de empresas de mensajería. Se dice «el valorador externo», «las 10 navieras» y «la dueña».
- Sin nombrar herramienta ni plataforma de flujos (la dueña pidió n8n, Make o Zapier; Verónica habló de Claude, n8n y Gemini). Sin VPN: Venezuela no es país soportado.
- El rastreo en las 10 navieras depende de cómo permita consultar cada portal: el deck lo dice y lo prueba con cada una; no promete que todas sean automatizables.
- La meta «liberar 90 % del trabajo manual» es declarada por la dueña, no medida: el deck la rotula como meta. El 70 % de información repetida de cada carga y el 90 % manual también son declarados por ella.
- Retorno en modo método: la ficha no trae tiempos ni volúmenes ni lo que cobra el valorador externo por documento. Si llegan, pasar a cifras con su origen.
- Fuera de alcance: Cerebro Digital de la dueña (propuesta aparte, Verónica ofreció enviarla), página web de estatus con usuario y clave (la dueña lo mencionó como deseo) y crear un software propio.
- La dueña pidió ver las formas de pago y el pago inicial; se omitió la facilidad de pago por decisión de Ivana y se comentará aparte (Verónica mencionó 30 % inicial y 2 o 3 cuotas). Sin fechas ni meses (§4.23).
- Un solo valorador externo y eventual: la persona de Valoración interna revisa su cálculo. El agente reemplaza la pre-valoración del externo, no la revisión humana.

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

- Valor, descuento y total: campos vacíos para ventas.
- Confirmar División (Educación) y alianza (no).
- Confirmar el reparto de las 80 h entre los 14 entregables.
- Confirmar con el consultor si los 10 portales de navieras permiten consulta automática.
- Si la dueña quiere ver las formas de pago en la propuesta (lo pidió en la reunión).
- Herramienta de IA y de flujos, y quién contrata las licencias (arranque).
- Propuesta aparte del Cerebro Digital de la dueña.
- Confirmar el teléfono y el correo de Verónica Rubio (tomados de propuestas anteriores).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py luz-del-mar-cai117      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh luz-del-mar-cai117             # verifica, genera el PDF y ajusta los campos
```
