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
- **Alcance**: {{N_TOTAL_TXT}} en {{N_AREAS_TXT}} · {{H_TOTAL}} h de sesión · {{SEMANAS_TXT}} de trabajo desde el arranque{{SEGUIMIENTO_TXT}}
- **Orden de las slides**: {{ORDEN}}
- **Asesora comercial que ve el cliente (última slide)**: {{ASESORA}}
<!--auto:fin-->
- **Estado**: `Borrador`
- **Ficha Comercial Intezia**: (indicar si existe y qué datos se tomaron de ella: servicio adquirido, honorarios, hallazgos del Levantamiento, requerimiento y dolor del cliente)
- **fecha_arranque_deseada**: (preguntar al cliente; sin esta respuesta no se agrega Calendario de inicio, no se inventa)
- **resultados_esperados**: (preguntar al cliente; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: {{ORIGEN}}
- **Fuente del insumo**: {{FUENTE_INSUMO}}
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

{{SUPUESTOS}}

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md y CLAUDE.md §4.21)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo y en qué plazo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos. Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- {{REGLA_RETORNO}}
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso.
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- {{NOTA_PRECIO}}

## Pendientes

{{PENDIENTES}}

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py {{SLUG}}      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh {{SLUG}}             # verifica, genera el PDF y ajusta los campos
```
