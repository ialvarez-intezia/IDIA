# Brief · Diego · Servicio de Habilidades (CAP-109)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Diego
- **Slug**: `diego`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAP-109`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Claude como tutor universitario por materia, para estudiar, reforzar y hacer seguimiento al rendimiento, desde un test de nivel
<!--auto:inicio-->
- **Alcance**: 5 entregables en 4 módulos · 8 h de trabajo · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Reunión del 21/10/2026 con la madre del participante (instrucción de Ivana): propuesta reajustada, antes «De cero a experto en Claude» de 12 h y 17 slides. Un encuentro de 1 h por semana, test de nivel al inicio y Claude como tutor por materia (estudia Comunicación Social). Sin Ficha Comercial ni transcripción
- **Fuente del insumo**: Resumen de la reunión del 21/10/2026 con la madre del participante (instrucción directa, sin Ficha Comercial)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Reajuste pedido en la reunión del 21/10/2026 con la madre del participante: un encuentro de 1 h por semana (sin cargar los fines de semana), test de nivel al inicio (ya hizo un introductorio de Claude y lo usa) y Claude como tutor universitario por materia (estudia Comunicación Social, ejemplo: tomar el feedback de una práctica de convertir un artículo en noticia y armar un plan de refuerzo). Reemplaza la CAP-109 anterior de 12 h («De cero a experto en Claude», 17 slides, archivada en _anterior-17-slides/).
- Horas (elegidas por Ivana, 21/10/2026): 8 h en encuentros de 1 h. El reparto por módulo es mío: test de nivel 1 h, tutor por materia 3 h, refuerzo con el feedback 2 h y seguimiento 2 h. El deck dice «un encuentro de 1 h por semana» como tasa (§4.23) y no lleva semanas, sesiones ni fechas: el calendario se acuerda antes de empezar.
- El grado académico y la nota de la práctica (12) no van en el deck; el ejemplo solo aparece como caso en el detalle del plan de refuerzo. No se nombra ni a la madre ni a la profesora.
- Código CAP-109 conservado (es el de la propuesta anterior de Diego). Existe otra CAP-109, la de Good Latam, sin relación: la colisión de códigos sigue sin resolverse.
- Cliente normal sin alianza. Hoja de inversión con valor vacío para ventas (campos para Adobe Reader) y sin facilidad de pago, como la versión anterior. Sin garantía ni seguimiento 30-60-90.
- Todavía no se define si arranca ya o al terminar el proyecto de Mercadeo de la madre (dato interno): el deck no pone fecha y solo dice «ya o más adelante».
- Modalidad: la versión anterior era presencial; con un encuentro de 1 h por semana se deja «presencial o virtual» a elegir. Facilitador sin asignar.
- Contacto de la última slide: Flavia Martínez, asesora de la CAP-109 anterior y de Puro Lomo (elegida por Ivana, 21/10/2026).
- Sin cantidad de entregables en las láminas (regla de Ivana, 20/10/2026). Certificado de participación y cuaderno de trabajo digital se mantienen de la versión anterior.

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

- Valor de la hoja de inversión: ventas lo llena.
- Fecha de arranque (ya o al terminar el proyecto de Mercadeo) y día y hora del encuentro semanal.
- Modalidad (presencial o virtual) y facilitador.
- Confirmar con Ivana el reparto de horas por módulo (propuesto por el sistema).
- Nombre completo del participante (el deck usa «Diego»).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py diego      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh diego             # verifica, genera el PDF y ajusta los campos
```
