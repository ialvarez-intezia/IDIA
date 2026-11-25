# Brief · Instituto Médico Valera · Servicio de Habilidades y Políticas (CAI-115)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Instituto Médico Valera
- **Slug**: `instituto-medico-valera-cai115`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-115`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Transferir al equipo de IT del Instituto Médico Valera la capacidad de construir y operar un agente de atención a pacientes propio y de automatizar procesos internos, con una gobernanza de IA en paralelo: política, matriz de datos, stack y licencias, responsable y control del gasto
<!--auto:inicio-->
- **Alcance**: 11 entregables en 3 áreas · 40 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento del Instituto Médico Valera (Verónica Rubio, registrada el 20/11/2026; contacto Max Arismendi, presidente ejecutivo, que decide y escala a junta directiva), transcripción de la reunión de Google Meet del 20/11/2026 (42 min) y resumen de Ventas, más instrucciones de Ivana (22/11/2026): propuesta CAI-115 de Habilidades con Políticas en paralelo, Verónica Rubio como asesora
- **Fuente del insumo**: Ficha de Levantamiento (20/11/2026) y transcripción de la reunión de Verónica Rubio con el Instituto Médico Valera (20/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (22/11/2026): propuesta CAI-115 de Habilidades para el Instituto Médico Valera, con Políticas de IA en paralelo, y Verónica Rubio como asesora. Insumos: Ficha (20/11/2026), transcripción de Meet (42 min) y resumen de Ventas. Primer contacto.
- Ajuste de Ivana (24/11/2026): «dejando solo el desarrollo del agente», sin la migración a un lenguaje moderno ni la conexión con el sistema hecho en RPG. Respuestas: se quita toda el área de Modernización del código RPG, se quita completa el área de Datos al alcance de los gerentes (consulta segura de los datos del sistema, interfaces y guía) y quedan Procesos internos, Agente de pacientes y Políticas. El deck no nombra RPG, AS400, modernización ni migración, ni el sistema de gestión. Horas confirmadas por Ivana: 20 h por área de Habilidades, total 40 h (antes 80 h).
- Decisiones previas de Ivana (22/11/2026): Educación y sin alianza; combo de Habilidades y Políticas en un deck, con Políticas en paralelo y SIN horas (se cotiza por entregable); impacto «operación». Combo parcial: se registra bajo `habilidades` (CLAUDE.md §4.1a) y el rótulo dice «Servicio de Habilidades y Políticas».
- Reparto de horas mío (Ivana fijó 20 h por área): Procesos internos 20 h (procesos elegidos 4, flujos 10, reglas de autorización 6); Agente de pacientes 20 h (mapa 4, agente de WhatsApp 10, guía 6). Fases de Habilidades de 8, 20 y 12 h = 40 h. Los cinco entregables de Gobernanza de IA llevan 0 h (política, matriz de datos, stack y licencias, responsable y comité, control del gasto).
- Sin nombres de personas (el gerente de IT, la gerente médica) ni del proveedor externo que hoy opera el agente. Sin marcas de IA: no se nombra Claude ni Meta ni N8N («herramientas de flujo»); sí WhatsApp. No se menciona VPN (Claude no está soportado en Venezuela). El stack oficial lo define la política.
- Viáticos y logística de traslado: el presidente pidió que la propuesta no los incluya. Modalidad mixta (ficha y reunión): presencial en Valera y encuentros en línea.
- Cerebros Digitales de los gerentes: quedan fuera, en «Fuera de este alcance» (propuesta aparte).
- Retorno en modo método: no hay horas ni volúmenes medidos. Seguimiento 30-60-90 incluido por ser estándar de Habilidades. Sin facilidad de pago (regla permanente). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23). Cotización de Políticas: la hoja de inversión usa `inversion.partes` (Habilidades en IT y Políticas de IA) para que ventas ponga cada valor; la regla de memoria dice que las partes solo van si Ivana las pide: confirmar o quitarlas.

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

- Valor, descuento y total: campos vacíos para ventas; con 40 h el valor cambia frente al borrador de 80 h. Moneda y forma de pago sin definir.
- Confirmar con Ivana el reparto de las 40 h entre los 6 entregables de Habilidades, y cómo se cotiza Políticas (por entregable, sin horas).
- Confirmar con Keiber que el alcance de Políticas (política, matriz, stack, responsable y control del gasto) es el que se vende.
- Confirmar cuánto del agente actual es de la clínica (el cliente no sabe si el proveedor es dueño del agente que paga) y qué permite el canal telefónico.
- Si el cliente pregunta por el sistema de gestión o los datos para gerentes, quedaron fuera por decisión de Ivana: confirmar si se ofrecen más adelante como otra propuesta.
- Confirmar el teléfono y el correo de Verónica Rubio (tomados de propuestas anteriores).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py instituto-medico-valera-cai115      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh instituto-medico-valera-cai115             # verifica, genera el PDF y ajusta los campos
```
