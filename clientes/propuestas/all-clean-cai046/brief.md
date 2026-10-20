# Brief · All Clean · Servicio de Habilidades (CAI-046)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: All Clean
- **Slug**: `all-clean-cai046`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-046`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Cerebro Digital con Claude y Obsidian para la dirección de All Clean: un asistente con memoria propia que conoce su rol, su voz y su criterio, y la ayuda a decidir y a ahorrar tiempo
<!--auto:inicio-->
- **Alcance**: 3 entregables en 3 bloques · 6 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de All Clean (Verónica Rubio, 08/10/2026) e instrucción de Ivana del 09/10/2026: Cerebro Digital de 6 h, para la dirección de All Clean, sin mencionar los procesos ni nada de la DET-031
- **Fuente del insumo**: Ficha de Levantamiento de All Clean (sin transcripción de la reunión) e instrucción del usuario
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Código CAI-046 asumido (el siguiente libre; Ivana no lo indicó). División Educación y sin alianza, como la DET-031. Asesora Verónica Rubio, con el contacto de la DET-031.
- Pedido de Ivana (2026-10-09): Cerebro Digital de 6 h «como los demás», para el mismo jefe de All Clean, sin mencionar los procesos ni nada de la DET-031. El deck no nombra procesos, áreas, sistemas del cliente, herramientas de IA que usan hoy ni la Detección. Un solo cerebro y una sola persona: la dirección.
- Qué hace el cerebro: al no mencionar procesos, queda como el cerebro del rol de dirección con la receta estándar de 6 h de la CAI-043 (Project de Claude, grafo en Obsidian, Skill y plan de uso). La tarea de la Skill se elige en el arranque con la dirección, de su línea base.
- Horas: 6 h por Cerebro Digital (tarifa de referencia, empresa/politicas-comerciales.md), 3 entregables de 2 h; la reunión de arranque (1 h) va aparte. La Ficha dice «sesiones de 2 h»: cómo se reparten las horas se acuerda en el arranque y no va en el deck (§4.23).
- Portada: 3 datos de la Ficha que no son procesos (uso suelto de la IA sin criterio ni formación, sin política de datos, y que la dirección busca ganar tiempo para atender más).
- Claude: lo pidió el cliente en la Ficha. Se dice desde el inicio que la licencia va aparte con plan de pago (Pro, USD 20 al mes de lista, consultado el 08/10/2026 en claude.com/pricing para la CAI-040; volver a consultar antes de enviar). El acceso se confirma en la reunión de arranque, sin nombrar países ni prometer VPN (claude-no-soportado-en-venezuela-no-prometer-vpn). Obsidian entra por ser el estándar del patrón de Cerebro Digital.
- Sin facilidad de pago: criterio de Ivana en la DET-031 y en los Cerebros Digitales anteriores (`omitir: ["pago"]`); ventas comunica el plan por otro medio.
- No va al deck: nombres de personas del cliente, que la dirección paga ChatGPT de forma personal, las herramientas de IA que usan hoy, las automatizaciones en n8n, el sistema de gestión y los CRM que evalúan, el bot, el patrocinio «presente pero tibio» y el presupuesto «en evaluación».

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

- Confirmar el código CAI-046 y que el cerebro es para la dirección (el dueño) y no para otra persona.
- Definir inversión, descuento y total (campos vacíos para ventas); línea de facturación (moneda y tasa) por confirmar con ventas.
- Confirmar con el cliente el plan de Claude y quién lo paga; volver a consultar el valor de lista antes de enviar.
- Confirmar si va Obsidian (estándar del patrón) y el acceso a Claude desde donde trabaja la dirección.
- Coordinar con la DET-031: es el mismo cliente. Ninguna propuesta menciona a la otra; decidir cuál se presenta primero y cómo.
- Transcripción de la reunión con All Clean: no la hay; si contradice la Ficha, manda la transcripción.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py all-clean-cai046      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh all-clean-cai046             # verifica, genera el PDF y ajusta los campos
```
