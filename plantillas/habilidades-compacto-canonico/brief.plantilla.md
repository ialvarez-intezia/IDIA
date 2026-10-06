# Brief · {{CLIENTE}} · Servicio de Habilidades ({{CODIGO}})

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: {{CLIENTE}}
- **Slug**: `{{SLUG}}`
- **División Intezia**: `{{DIVISION}}`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `{{ALIANZA}}`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`{{CODIGO}}`), presentada al cliente como **propuesta de proyecto**; formato compacto de {{SLIDES}} slides ({{PRECIO}})
- **Eje temático**: {{EJE}}
<!--auto:inicio-->
- **Alcance**: {{N_TOTAL_TXT}} en {{N_AREAS_TXT}} · {{H_TOTAL}} h de sesión · {{SEMANAS}} semanas de trabajo desde el arranque · seguimiento a {{SEGUIMIENTO}}
<!--auto:fin-->
- **Estado**: `Borrador`
- **Asesora comercial**: (completar; el deck no lleva slide de cierre ni contacto)
- **Ficha Comercial Intezia**: (indicar si existe y qué datos se tomaron de ella: servicio adquirido, honorarios, hallazgos del Levantamiento)
- **fecha_arranque_deseada**: (preguntar al cliente; sin esta respuesta no se agrega Calendario de inicio, no se inventa)
- **resultados_esperados**: (preguntar al cliente; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: {{ORIGEN}}
- **Fuente del insumo**: {{FUENTE_INSUMO}}
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

{{SUPUESTOS}}

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- {{NOTA_PRECIO}}

## Pendientes

{{PENDIENTES}}

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py {{SLUG}}      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh {{SLUG}}             # verifica, genera el PDF y ajusta los campos
```
