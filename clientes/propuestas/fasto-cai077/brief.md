# Brief · Fasto · Servicio de Habilidades (CAI-077)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Fasto
- **Slug**: `fasto-cai077`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-077`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Recepción asistida de facturas, alertas de stock, distribución por sede, cobertura y vencimientos, y conteos y mermas con Claude conectado a Estelar, construidos con los equipos de Inventario y Costos de Fasto, cadena de supermercados
<!--auto:inicio-->
- **Alcance**: 12 entregables en 4 líneas de trabajo · 64 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Respuesta a la solicitud (1) · 4 Ruta · 5 Cómo trabajamos · 6 Entregables · 7 Retorno · 8 Inversión · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Resumen interno «FASTO: lo que quedó funcionando y lo que sigue» (David Prato, 25/10/2026), transcripciones de las sesiones del servicio de Habilidades para Compras (5 al 23 de octubre), texto de Verónica Rubio con la ruta propuesta y respuestas de Ivana del 30/10/2026: CAI-077, Educación, sin alianza, 40 h, hoja de inversión por partes
- **Fuente del insumo**: Resumen interno de David Prato (25/10/2026), transcripciones de las sesiones de Compras y texto de Verónica Rubio (sin Ficha de Levantamiento propia ni transcripción de la reunión de esta propuesta)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (30/10/2026): propuesta CAI-077 para Fasto, asesora Verónica Rubio. Educación y sin alianza (confirmados); 40 h con el equipo y hoja de inversión por partes: confirmados. Continuación del servicio de Habilidades para Compras (CAP-104 y su implementación del 5 al 23 de octubre).
- Insumos: resumen interno de David Prato (25/10/2026), transcripciones de las sesiones de Compras y texto de Verónica; no hay Ficha ni transcripción propias de esta propuesta. El levantamiento de Inventario ya está hecho (22/10, enviado el 23/10), por eso no hay levantamiento ni Fundamentos de Inventario: va directo a construcción.
- Alcance: los cinco subproyectos de Inventario (recepción asistida, proyecto nuevo, y cuatro sobre la conexión actual) y el levantamiento de la oficina de costo. La lectura asistida de facturas de Costos se trata como la misma pieza que la recepción asistida (Verónica: «la misma puerta») para no contarla dos veces. Los demás subproyectos de Costos (Verónica habló de ocho; el PDF no los lista), la carga de mínimos y máximos, la Detección de las demás áreas y el acompañamiento quincenal o mensual van como siguiente paso, sin cotizar.
- Horas (propuestas por mí, Ivana: «40 h, sí»): levantamiento de Costos 4 h + recepción asistida 12 h (proyecto nuevo, dos equipos) + cuatro herramientas de 6 h sobre la conexión actual (24 h) = 40 h. Reunión de arranque de 1 h aparte. Partes de la hoja (pedido de Ivana, «columnas por partes»; reparto mío): «Costos y recepción» = 16 h; «Inventario» = 24 h.
- Cifras de la portada: del propio cliente y de sus datos de Estelar, con el origen dicho en el texto (80 a 90 proveedores, licor de 167 unidades que vende 0,33 al mes, 1 % a 8 % de recepciones ligadas a su orden). Sin línea «Fuente» (Ivana, 30/10/2026: ninguna presentación lleva fuentes). No se citan las satisfacciones, los 10.000 productos bajo mínimo ni el número de tiendas, ni personas de Fasto.
- Herramienta: se nombra Claude (ya en uso por el servicio anterior), sin precios de licencias, sin VPN y sin «cuesta menos» (frase del argumento interno de David). Estelar es el nombre del sistema; el texto de Verónica dice «Stellar» y el PDF usa «Estelar» para el sistema y «Stellar» para el proveedor: no se nombra al proveedor.
- Requisito: la recepción asistida necesita que Fasto habilite la carga de datos en Estelar (la conexión actual es de solo lectura): va en fuera de alcance, notas y próximos pasos. Sin facilidad de pago, con seguimiento 30-60-90.

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

- Confirmar con Ivana el reparto de las partes (16 h y 24 h) y las horas de cada pieza.
- Confirmar con Verónica los demás subproyectos de Costos (¿ocho?) y si alguno entra en esta propuesta.
- Confirmar quiénes participan de Inventario y de Costos y la modalidad.
- Valor, descuento y total: campos vacíos para ventas; si se elige una sola parte, ventas escribe el total a mano.
- Confirmar el teléfono y el correo de Verónica Rubio (tomados de propuestas anteriores).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py fasto-cai077      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh fasto-cai077             # verifica, genera el PDF y ajusta los campos
```
