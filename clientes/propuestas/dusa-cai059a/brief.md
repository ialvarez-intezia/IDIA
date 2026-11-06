# Brief · DUSA · Servicio de Habilidades (CAI-059A)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: DUSA
- **Slug**: `dusa-cai059a`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-059A`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construir tres soluciones frecuentes de DUSA, instalar dos agentes ya construidos y medir, antes del 11 de noviembre, las horas que liberan los cinco procesos
<!--auto:inicio-->
- **Alcance**: 5 soluciones en 4 áreas · 42 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Estructura y horas enviadas a Ivana el 04/11/2026: DUSA eligió la opción 3 del piloto y sumó la instalación de los dos agentes ya construidos. Cifras de las fichas de levantamiento de septiembre de 2026 y base de la CAI-035 y la CAI-059
- **Fuente del insumo**: Estructura y horas de la etapa (04/11/2026) y fichas de levantamiento de septiembre de 2026
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Código: Ivana pidió «mismo código con sufijo A» sin decir cuál; se tomó CAI-059 (última propuesta de DUSA, con tres opciones). Si era CAI-035, cambiar `cliente.codigo` y el slug.
- El «piloto» y su opción 3 no están en el repositorio: la estructura y las horas son las enviadas a Ivana el 04/11/2026.
- Horas: 42 en total = construcción 19, testeo 10, adopción 9 e instalación 4; por etapa, preparación en línea 2 h, construcción presencial 27 h y adopción e instalación presencial 13 h. Ivana las pidió visibles en la propuesta (excepción a la regla del 27/10/2026), así que `sin_horas_trabajo` queda en false.
- Fecha: «antes del 11 de noviembre» va en la portada y en el retorno por pedido expreso (excepción a §4.23; en `frases_ok`).
- Las fichas de septiembre se citan dentro del texto de la portada, sin línea de fuente (regla del 30/10/2026).
- Todo en Copilot Premium (6 cuentas aportadas por DUSA); la CAI-059 usaba Claude Team para Nómina.
- Sin facilidad de pago: no se pidió; la propuesta económica es una hoja con 42 h y licencias aparte.

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

- Confirmar el código (CAI-059A o CAI-035A) y que el nombre de la carpeta es el correcto.
- Valor, descuento y total: campos vacíos para ventas; moneda de facturación por confirmar.
- Confirmar que «3 o 4 páginas» se cumple con el formato compacto vigente (8 láminas, sin pago): el generador no produce menos.
- Confirmar la fecha del 11 de noviembre y si la medición incluye los dos agentes instalados.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py dusa-cai059a      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh dusa-cai059a             # verifica, genera el PDF y ajusta los campos
```
