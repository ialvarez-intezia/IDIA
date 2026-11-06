# Brief · Colegio Los Arcos · Servicio de Habilidades (CAI-087)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Colegio Los Arcos
- **Slug**: `colegio-los-arcos-cai087`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-087`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: IA en el aula para 50 docentes: recuperar el tiempo de planificar, corregir e informar, renovar la clase con material visual y dinámico, evaluar y enseñar con alumnos que ya usan IA, y una visión de la educación a 2030, con ejercicios sobre su propio material
<!--auto:inicio-->
- **Alcance**: 6 entregables en 4 módulos · 6 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Contexto de Ivana del 05/11/2026 (50 docentes; ejes del programa; seguimiento 30-60-90; visión 2030), PDF «Programa de Formación Docente 2026» de Intezia (contenido de referencia, no se concretó por el valor) y banco de casos de éxito de Intezia (formación de 50 docentes en 2024). Sin Ficha de Levantamiento ni transcripción
- **Fuente del insumo**: Contexto de Ivana (05/11/2026) y programa docente 2026 de Intezia
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (05/11/2026): propuesta de Habilidades CAI-087 para el Colegio Los Arcos, contacto María Iribarren (directora comercial). Educación, sin alianza, sin herramienta nombrada, sin facilidad de pago y con certificado de participación: confirmados con Ivana. Sin Ficha ni transcripción: el insumo es su contexto y el programa docente 2026 de Intezia.
- Duración (propuesta mía; Ivana dijo «ustedes me dicen»): 6 h por grupo en 4 módulos (tiempo 2, material visual y dinámico 1, evaluar y enseñar 2, Educación 2030 1); con dos grupos de 25, el total es de 12 h de encuentro con los docentes (Ivana pidió ver el total). El programa 2026 era de 8 h y no se concretó por su valor. Las horas son de encuentro, no horas de trabajo de Intezia (§4.23); las horas de `datos.json` son marcadores técnicos.
- 50 docentes en dos grupos de hasta 25 (Luis Prieto, director, confirmó «en principio 50»; Ivana confirmó los dos grupos el 05/11/2026). Dato del cliente, así que se dice; el calendario se acuerda en el arranque, sin número de sesiones.
- Hecho de la portada: la formación de 2024 (50 docentes) sale del banco de casos de éxito de Intezia (la fuente va en `origen`, no en la portada, por la regla del 29/10); los otros dos hechos («en casa» y «a diario») son contenido del programa y del contexto de Ivana, no mediciones de Los Arcos.
- Contenido rediseñado (Ivana: no copiar el programa 2026): cada módulo es lo que el docente construye con su propio material (asistente propio, material visual y dinámico, rúbrica y tutor, plan personal de adopción). Del PDF 2026 se tomó la intención, no el temario: quedan fuera el repaso de fundamentos, la configuración del entorno, la taxonomía de Bloom y las tarjetas de agentes.
- Herramienta de IA: no se nombra, pero las actividades están pensadas para lo que ofrece Gemini (Ivana supone que el colegio lo usa): asistente personalizado con el tono del colegio (Gems), cuaderno de estudio con fuentes propias, guía, resumen y audio (NotebookLM), presentaciones, video corto desde un guion e infografías, y tutor con preguntas guía. Si el colegio no tiene Gemini, se adaptan al arrancar. No se mencionan Gemini ni Microsoft for Startups.
- Seguimiento 30-60-90 tipo Habilidades, adaptado a docentes: uso real en clase, nuevos usos y ajustes, tiempo recuperado medido contra una encuesta breve de inicio (método, sin cifras ni valor de la hora).
- Contacto de María: miribarren@intezia.com (el PDF de 2026 traía maria@intezia.com). El director es Luis Prieto; el deck no lo nombra.
- Sin valor, descuento ni total en el repositorio: campos vacíos para ventas. El colegio está corto de presupuesto: el valor accesible lo fija ventas.

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

- Confirmar con Ivana las 12 h en total (6 por grupo) y el reparto entre los cuatro módulos.
- Confirmar la modalidad (presencial en el colegio) y si el colegio usa Gemini (y quién contrata las cuentas), para ajustar las actividades.
- Valor, descuento y total: campos vacíos para ventas; moneda de facturación por confirmar.
- Confirmar el correo de María (miribarren@ o maria@) y si el director, Luis Prieto, debe aparecer.
- Confirmar si se quiere citar la formación de 2024 como hecho de la portada.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py colegio-los-arcos-cai087      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh colegio-los-arcos-cai087             # verifica, genera el PDF y ajusta los campos
```
