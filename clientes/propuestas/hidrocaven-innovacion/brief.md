# Brief · Equipos y Sistemas Hidrocaven · Servicio de Innovación (INN-005)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Equipos y Sistemas Hidrocaven
- **Slug**: `hidrocaven-innovacion`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `innovacion`
- **Alianza**: `no`
- **Tipo de documento**: Plan de Innovación · Proyecto compartido y herramientas con datos persistentes sobre Claude (14 h) · hoja de inversión sin facilidad de pago · formato compacto v3 (`INN-005`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Proyecto compartido y herramientas con datos persistentes sobre Claude para el equipo de Compras, Logística y Administración de Hidrocaven
<!--auto:inicio-->
- **Alcance**: 4 soluciones en 4 bloques · 14 h de trabajo · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Retorno · 6 Inversión · 7 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Instrucciones de Ivana del 20/10/2026: propuesta de Innovación para profundizar en Claude con los 4 participantes ya formados en el CAP-074, 14 h en total, con dos temas de los próximos pasos de la ficha de post-servicio: proyecto compartido para la fase 2 del hospital y herramientas con datos persistentes
- **Fuente del insumo**: OnePager_PostServicio_Hidrocaven.pdf (post-servicio de 30 días del CAP-074, seguimiento presencial del 17/10/2026, consultor Ricardo Díaz); instrucciones de Ivana (sin Ficha Comercial ni transcripción de una reunión de esta propuesta)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Servicio y formato (Ivana, 20/10/2026): Innovación, plantilla compacta v3 con horas, como INN-003 e INN-004 de Zoom. Código INN-005 (el último registrado era INN-004); por confirmar.
- Alcance (Ivana): los 4 participantes que ya hicieron el CAP-074 (Compras, Logística y Administración). Temas (Ivana, de los cinco próximos pasos de la ficha de post-servicio): 1) proyecto compartido para la fase 2 del hospital psiquiátrico y 2) publicar las herramientas con datos persistentes. **Quedan fuera** los otros tres pasos de la ficha: cuenta empresarial, automatizar facturas y retenciones, y retomar el Maestro de Productos y las Skills.
- Horas (Ivana): 14 h en total. **El reparto es mío**: 5 h para el proyecto compartido (3 h el proyecto con la data de la fase 1 y 2 h el análisis de comprar o alquilar andamios) y 9 h para las tres herramientas (3 h cada una). Por confirmar.
- Todos los hechos del cliente salen de la ficha de post-servicio de 30 días: 3 herramientas propias creadas tras el programa; análisis de compras del proyecto del hospital de unos 15 días a 3 o 4 días; cuadro de análisis de cotizaciones de medio día a 10 minutos; la plantilla de seguimiento está solo en un computador; la app de viáticos necesita servidor y datos persistentes para salir a producción; los artefactos compartidos no guardaron los datos del portal de solicitudes. El deck no nombra personas del cliente ni al consultor.
- División Educación y sin alianza: tomadas del brief del CAP-074 (cliente de Educación, sin alianza); Ivana no las repitió. Confirmar.
- Sin Ficha ni transcripción: la estructura sale de la ficha de post-servicio y de las instrucciones de Ivana (§4.23). El retorno va en modo método; los resultados del CAP-074 se muestran como casos ya logrados, con su fuente.
- Sin seguimiento 30-60-90 ni garantía (como INN-003 e INN-004 de Zoom): `seguimiento.tipo: ninguno` e `inversion.sin_garantia`. Con hoja de inversión (campos de valor vacíos para ventas) y **sin facilidad de pago**, como en las propuestas anteriores en las que Ivana la omitió. Si prefiere cuotas, se quita `omitir: ["pago"]`.
- §4.11: Hidrocaven ya usa Claude (lo documenta la ficha); el deck habla de lo que se construye sobre eso, no de un cambio de herramienta. La ficha menciona la migración de su sistema de gestión a un nuevo ERP: es dato de contexto interno y no va en el deck.
- Licencias, cuenta de Claude y servidor u hospedaje de las herramientas quedan fuera de la propuesta (la ficha dice que hoy trabajan con cuentas individuales y que las herramientas necesitan servidor). Compartir un Proyecto de Claude con el equipo requiere un plan de equipo: verificar con la asesora antes de enviar; el deck no afirma planes ni funciones.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Confirmar el código INN-005, la división (Educación) y que no es alianza.
- Confirmar el reparto de las 14 h entre el proyecto compartido (5 h) y las tres herramientas (9 h).
- Confirmar con la asesora quién contrata y paga las licencias o el plan de equipo de Claude y el servidor u hospedaje de las herramientas; ambos quedan fuera de la propuesta.
- Confirmar si lleva facilidad de pago (se omitió) y que los valores los llena ventas: la hoja de inversión sale con los campos vacíos.
- Confirmar con el equipo de Hidrocaven que la plantilla, el portal de solicitudes y la app de viáticos son las tres herramientas a publicar, y qué área de tecnología participa en la revisión de seguridad.
- Confirmar la asesora que ve el cliente (se usó Isabella Palazzone, como en el CAP-074) y su teléfono, que no está en la ficha.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py hidrocaven-innovacion      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh hidrocaven-innovacion             # verifica, genera el PDF y ajusta los campos
```
