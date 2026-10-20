# Brief · All Clean · Servicio de Detección (DET-031)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: All Clean
- **Slug**: `all-clean-det031`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-031`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Mapear los procesos de ventas, almacén y conciliación de All Clean, dejar logros inmediatos construidos con el equipo y llegar a Habilidades con claridad sobre qué automatizar
<!--auto:inicio-->
- **Alcance**: 3 áreas (Ventas, Almacén, Conciliación) · 12 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de All Clean (Verónica Rubio, 08/10/2026). No hay transcripción de la reunión: si la transcripción contradice la Ficha, manda la transcripción
- **Fuente del insumo**: Ficha de Levantamiento de All Clean (sin transcripción de la reunión)
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- División y alianza inferidas: Educación y sin alianza (empresa privada, primer contacto, la Ficha no menciona aliado). Confirmar con Ivana.
- Fuente: solo la Ficha de Levantamiento del 08/10/2026; no hay transcripción de la reunión (CLAUDE.md §4.23). Si la transcripción contradice la Ficha, manda la transcripción.
- Áreas: las 3 de la Ficha, con el nombre normalizado (ventas, almacén, «conciliacon» → Conciliación). No hay lista de personal (10 analistas), por eso no se muestran departamentos.
- Horas (lineamiento de Detección): 4 h por área x 3 = 12 h de levantamiento, que es lo único que se muestra, más 2 h de nivelación en IA para las 10 personas en un solo grupo (la Ficha dice 10). El arranque va aparte, sin horas. Total interno: 14 h.
- Logros inmediatos: al menos 3 en el proyecto, no uno por área, para cumplir el pedido de construir algunos durante el levantamiento. Lo que el cliente mencionó (conversaciones repetitivas de atención, trazabilidad entre ventas y almacén, cotizaciones en su sistema de gestión, un cerebro digital de ventas) guía la conversación del arranque, pero no se promete ni se prioriza: los focos salen del levantamiento.
- Ruta: Detección ahora y Habilidades después, como pidió Ivana; sin «Más adelante: Políticas» (si se quiere mostrar, se agrega como tercera tarjeta de ruta_completa).
- Entrevistados: la Ficha pide 1 persona por área; el estándar de Detección es el líder y su mano derecha. Ajustar si All Clean no tiene ese segundo perfil.
- Modalidad mixta y calendario a mutuo acuerdo (Ficha); sin sedes distintas. Las «sesiones de 2 h» de la Ficha son para Habilidades: se definen en el arranque y no van en el deck (§4.23).
- Plan de pago estándar de Detección: 50 % al aprobar y 50 % con el Informe Final; montos vacíos para ventas.
- Sin pre-recomendar herramienta de IA: el cliente usa ChatGPT y Gemini y le interesa Claude, pero la recomendación la hace el Informe Final. El CRM aparece solo como ejemplo de sistema nuevo fuera de alcance (no se afirma que lo adopten, §4.11).
- No va al deck: nombres de personas del cliente, que el dueño paga ChatGPT de forma personal, las automatizaciones en n8n que ya armó su equipo de tecnología, los productos de CRM que evalúan, el patrocinio «presente pero tibio» ni el presupuesto «en evaluación».

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Detección (`plantillas/deteccion-compacto.md`, Keiber 2026-10-08): sin frentes ni áreas prioritarias antes de detectar (lo que el cliente señaló como interés guía la conversación, no la estructura); cada departamento por separado, con su líder y su mano derecha, sin tarea previa; horas en global, sin reparto por área; al menos 3 logros inmediatos en el proyecto (no uno por área); entregables nombrados, sin conteos.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Pedir la transcripción de la reunión con All Clean y revisar la propuesta contra ella.
- Definir inversión, descuento, total y los montos de las 2 cuotas (campos vacíos para ventas); línea de facturación (moneda y tasa) por confirmar con ventas.
- Confirmar las 14 h (12 de levantamiento y 2 de nivelación) con ventas; la Ficha da «sesiones de 2 h» solo para Habilidades.
- Presentación al cliente: Verónica pide que Servicios participe para mostrar de forma visual cómo quedaría un proceso automatizado (el cliente necesita verlo). No es parte del PDF: definir si se prepara una pieza visual aparte.
- Levantar en el arranque qué automatizaciones en n8n ya existen, para distinguir lo que se puede crecer de lo que ya funciona.
- Confirmar el nombre del área «conciliación» y quién es su responsable.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py all-clean-det031      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh all-clean-det031             # verifica, genera el PDF y ajusta los campos
```
