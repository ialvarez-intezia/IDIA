# Brief · Corimón · Servicio de Detección y Políticas (DET-060)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Corimón
- **Slug**: `corimon-det060`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección y Políticas: Fundamentals en 2 grupos (4 h, 46 líderes sin TI) + auditoría de 12 áreas con 51 líderes estratégicos (52 h de levantamiento, más peso en TI) y marco de gobernanza de IA, en formato compacto de Detección (`DET-060`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Auditar la operación real de las 12 áreas corporativas y de planta de Corimón con sus 51 líderes estratégicos, recomendar la arquitectura y el camino tecnológico por área, y construir el marco de gobernanza de IA que necesitan antes de escalar a toda la organización
<!--auto:inicio-->
- **Alcance**: 12 áreas (TI, Finanzas, Compras, Negocios, Comercial y BI, RR. HH., Gerencia General, Logística, Normalización, Laboratorio y Desarrollo, Legal, CEO, Proyectos, Ingeniería y Mantenimiento, Producción) · 52 h de levantamiento en global, sin reparto por área (internas: arranque 2 h, nivelación 4 h) · logros inmediatos cuando el proceso lo permite, sin cifra
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Corimón (Flavia Martínez, 16/11/2026) y contexto adicional del usuario del 17/11/2026 (exclusión de TI de los Fundamentals por grupos de 25, y de omitir cualquier referencia a un modelo pre-entrenado).
- **Fuente del insumo**: Ficha de Levantamiento de Corimón. Sin transcripción de la reunión disponible; si aparece y contradice la ficha, manda la transcripción.
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Servicio: combo Detección + Políticas bajo `deteccion` (CLAUDE.md §4.1a), mismo criterio que Andrómeda DET-016: Políticas se representa como una etapa de la ruta y un entregable (Marco de gobernanza de IA), con su propio valor en `inversion.partes`. La plantilla de Detección no tiene un formato propio para Políticas.
- Fundamentals (nivelación): instrucción directa del usuario (17/11/2026) de excluir a TI (5 personas) porque ya trabaja con Claude para desarrollo y no necesita repetir lo básico (la Ficha pedía nivelar a las mismas 51 personas entrevistadas, sin excluir a TI; el usuario lo ajustó en el chat). Quedan 46 líderes, repartidos en 2 grupos de hasta 25 personas (25 y 21), 2 h cada grupo = 4 h de Fundamentals en total. La composición exacta de cada grupo se define en el kickoff.
- Horas de levantamiento: 4 h por área (lineamiento estándar, `empresa/politicas-comerciales.md`) para las 11 áreas restantes (44 h) + 8 h para TI (el doble, por el pedido explícito de más peso en sus sesiones porque ahí se define el camino tecnológico) = 52 h en total. El reparto exacto por área se decide en el kickoff (regla de la plantilla: horas en global, sin desglose por área en la propuesta).
- Sin mencionar ningún modelo pre-entrenado ni el tipo de modelo detrás de la arquitectura recomendada (instrucción directa del usuario, 17/11/2026): el deck solo habla de la recomendación de arquitectura (IA central que reparte peticiones), los criterios de separación de datos y control de tokens, y la ruta de implementación — nunca de construirla ni de qué modelo la sustenta.
- La «columna vertebral» (arquitectura central tipo router) queda explícitamente fuera de alcance como construcción: Intezia la recomienda, Corimón (su equipo de TI) la construye. Esto se escribió con claridad en `fuera_alcance` a pedido explícito del cliente (Ficha, Bloque F).
- Recomendación de herramienta objetiva: Jonathan (gerente de TI) se inclina por Copilot y pidió privacidad como criterio; Alejandro pidió expresamente que la recomendación no esté «amañada». El deck no pre-recomienda ninguna herramienta (ni Copilot, ni Gemini, ni Claude): la Brújula del Informe Final decide con datos.
- Nombres de personas (Alejandro Padra, Jonathan, Valerie) no se mencionan en el deck — quedan en brief.md para uso interno de Ventas.
- Plan de pago: se usa el estándar de la plantilla (50 % al aprobar, 50 % con el Informe Final); no se pidió otro.
- Impacto (`entregables.impacto`) con enfoque `operacion`: el diagnóstico y la gobernanza dan orden y objetividad, no implican reducir personal.
- Segunda fase (fuera de esta propuesta): profundización por filial y nivelación del resto del personal (~600 personas en el grupo), según la Ficha y el contexto del usuario. Se refleja solo en `ruta_completa` como «Después».

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Detección (`plantillas/deteccion-compacto.md`, Keiber 2026-10-08): sin frentes ni áreas prioritarias antes de detectar (lo que el cliente señaló como interés guía la conversación, no la estructura); cada departamento por separado, con su líder y su mano derecha, sin tarea previa; horas en global, sin reparto por área; logros inmediatos cuando el proceso o el área lo permite, sin decir cuántos; entregables nombrados, sin conteos.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Confirmar con Flavia si hay transcripción de la reunión (la Ficha es la única fuente disponible); si aparece, contrastarla antes de enviar.
- Definir el valor de Detección y de Políticas, el descuento y el total (campos vacíos para ventas).
- Confirmar modalidad exacta (100 % presencial u algo mixto para alguna filial) y si Alejandro o Jonathan estarán en la presentación.
- Confirmar la composición final de los 2 grupos de Fundamentals en el kickoff.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py corimon-det060      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh corimon-det060             # verifica, genera el PDF y ajusta los campos
```
