# Brief · Banco del Tesoro · Servicio de Habilidades (CAI-097)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Banco del Tesoro
- **Slug**: `banco-del-tesoro-cai097`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-097`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: IA para directivos del Banco del Tesoro: uso responsable y seguro, cómo sacarle provecho, estrategia y políticas de uso, con prácticas que hacen salir los problemas reales de cada área
<!--auto:inicio-->
- **Alcance**: 8 entregables en 4 módulos · 8 h de trabajo · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Solicitud de propuesta pegada por Ivana (12 a 13/11/2026) a partir de la conversación con el contacto del banco: primera fase práctica de IA para directivos, general y básica, de 6 a 8 h, presencial, con prácticas en Gemini. Sin Ficha Comercial ni transcripción
- **Fuente del insumo**: Solicitud de propuesta (instrucción directa, sin Ficha Comercial)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Alcance (solicitud de Ivana, 13/11/2026): primera fase práctica de IA para directivos, general y básica, presencial, con prácticas en Gemini. El contacto pidió de 6 a 8 h: Ivana eligió 8 h. Reparto mío en 4 módulos de 2 h con 8 entregables de 1 h: uso responsable, cómo sacarle provecho, estrategia y políticas, y prácticas por área que hacen salir los problemas reales.
- Participantes: entre 20 y 25 directivos (gerentes generales, el contacto, la vicepresidenta y el presidente), que convoca el contacto. Al principio se habló de 40 o 50 y se prefirió empezar más pequeño: no se menciona el cambio en el deck. No se citan nombres ni cargos de los participantes.
- División Educación y alianza = no: tomados por mí, no los dio Ivana.
- Gemini es la herramienta de las prácticas por acuerdo con el contacto (la más usada en el banco). El deck no afirma que el banco migre ni adopte nada (§4.11) y no habla de VPN ni de acceso.
- Datos del banco (1.600 trabajadores, 550 en la sede, 30 a 40 gerencias generales, Tecnología como cuello de botella, proyectos antes del primer semestre de 2027, Gestión financiera como área a potenciar): son contexto interno y no van al deck. De los dolores solo se usa la falta de criterio común, la sensibilidad de la información y los niveles distintos; la dependencia de Tecnología se menciona como «tareas simples sin apoyo técnico».
- El ejemplo «no digas que soy el presidente… di que es la bancaria» se reescribe en la guía como «una entidad bancaria»; no se cita al presidente ni al contacto.
- Sin pago, seguimiento ni garantía (no se pidieron). Certificado de participación INTEZIA y cuaderno digital como transversales estándar. La hoja de inversión va con los valores vacíos, que llena ventas.
- Enfoque del cuadro Impacto: operación (Ivana, 13/11/2026), sin cifras ni estudios.
- Contacto de la última slide: María Iribarren, directora comercial (cargo y etiqueta vigentes).

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

- Valores de la hoja de inversión: ventas los llena (REF).
- Quién paga las cuentas de Gemini (el banco ya lo usa) y qué versión.
- Confirmar si Gestión financiera, Tecnología y Seguridad de la información tienen casos prioritarios para las prácticas (el contacto los mencionó como dolores).
- Presentación en vivo del contacto la semana próxima: la propuesta debe explicar sola qué incluye y su valor.
- Calendario con fechas: no va en la propuesta (§4.23); se acuerda en la reunión de arranque.
- Siguiente paso comercial: Detección por área u otros programas, a proponer tras el mapa; no se cotiza ahora.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py banco-del-tesoro-cai097      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh banco-del-tesoro-cai097             # verifica, genera el PDF y ajusta los campos
```
