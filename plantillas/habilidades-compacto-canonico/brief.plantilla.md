# Brief · {{CLIENTE}} · {{SERVICIO_ROTULO}} ({{CODIGO}})

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: {{CLIENTE}}
- **Slug**: `{{SLUG}}`
- **División Intezia**: `{{DIVISION}}`
- **Servicio (§4.1a)**: `{{SERVICIO}}`
- **Alianza**: `{{ALIANZA}}`
- **Tipo de documento**: {{TIPO_DOC}}; formato compacto de {{SLIDES}} slides ({{PRECIO}})
- **Eje temático**: {{EJE}}
<!--auto:inicio-->
- **Alcance**: {{ALCANCE_TXT}}
- **Orden de las slides**: {{ORDEN}}
- **Asesora comercial que ve el cliente (última slide)**: {{ASESORA}}
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: {{ORIGEN}}
- **Fuente del insumo**: {{FUENTE_INSUMO}}
- {{NOTA_TABLAS}}

## Decisiones y supuestos (confirmar con el usuario)

{{SUPUESTOS}}

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- {{REGLAS_FORMATO}}
- {{REGLA_RETORNO}}
- {{NOTA_PRECIO}}

## Pendientes

{{PENDIENTES}}

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py {{SLUG}}      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh {{SLUG}}             # verifica, genera el PDF y ajusta los campos
```
