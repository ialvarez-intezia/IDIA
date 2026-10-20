# Brief · COD Salud Visual · Servicio de Habilidades (CAI-057)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: COD Salud Visual
- **Slug**: `cod-salud-visual-cai057`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-057`), presentada al cliente como **propuesta de proyecto**; formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Una web nueva construida en vivo con el equipo de COD Salud Visual, herramientas sencillas para su día a día y la capacidad de mantenerlas, con Claude
<!--auto:inicio-->
- **Alcance**: 7 entregables en 5 bloques · 18 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Facilidad de pago · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Resumen de la minuta de la reunión con la dirección de COD Salud Visual (clínica de oftalmología de Barquisimeto) y contexto de la asesora María Iribarren, más instrucciones de Ivana del 16/10/2026: CAI-057, Habilidades con Claude de unas 16 h, web construida desde cero y alojada fuera del sitio actual, herramienta de citas por evaluar o por reemplazar, licencias de Claude Team incluidas. Sin Ficha de Levantamiento ni transcripción
- **Fuente del insumo**: Resumen de la minuta de la reunión con COD Salud Visual y contexto de la asesora; sin Ficha de Levantamiento ni transcripción
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (16/10/2026): CAI-057 para COD Salud Visual, asesora María Iribarren (Asesora comercial, con los datos de Simple TV; Ivana confirmó «si es esa»). Educación y alianza «no» (no se dijo; las alianzas de la minuta, OpenAI, n8n y Lovable, son de Intezia, no de COD). Habilidades puro. Sin Ficha ni transcripción: la portada usa hechos de la minuta; si contradicen a la transcripción, manda la transcripción.
- Estructura: una sola propuesta de 16 h, la de la asesora. La minuta dice «enviar propuesta con varias opciones o fases para que el cliente elija»; la plantilla compacta no soporta cotización por fases ni por opciones. Ivana no respondió si prefería dos documentos: se hizo uno y la ruta que sigue va como «siguiente etapa», sin cotizar.
- Horas (16 h exactas, horas enteras): arranque y diagnóstico 1 + fundamentos con Claude 2 + web 6 + herramientas del día a día 4 + autonomía y seguimiento 3 (cambio a la web hecho por el equipo 1 + tres revisiones de seguimiento 2). La asesora tiene el seguimiento en 1,5 h; la plantilla exige horas enteras, así que pasa a 2 h y el total queda en 16. El kick-off cuenta como trabajo (incluye el mini diagnóstico). Ivana no respondió esta confirmación; por confirmar.
- Camino técnico de la web (Ivana: «hay que subirlo a otro dominio porque se construye de 0; se puede evaluar la herramienta o bien ver otra que se adecue»): la web se construye desde cero, no sobre el Squarespace actual, y se publica en un alojamiento nuevo, en un dominio que se define en el arranque. La herramienta de citas actual se evalúa; si no se adecua, se elige otra. El deck no nombra la plataforma de alojamiento, ni Squarespace, ni el agendador. Hechos revisados el 16/10/2026 en fuentes secundarias: Squarespace funciona como sistema de gestión de contenidos y no admite subir un sitio HTML completo; un dominio puede apuntarse a otro alojamiento con registros DNS (A y CNAME), con propagación de minutos a 48 h; Acuity Scheduling (Squarespace Scheduling) puede incrustarse en casi cualquier sitio, según su ayuda oficial. Falta saber dónde está registrado el dominio y qué extensión de citas es.
- Herramientas del día a día: las tres de la asesora (cédula del paciente a una hoja compartida, recordatorios de compras e inventario, control simple de facturas y documentos recibidos) van como ejemplos de un solo entregable de 4 h, que se elige en el arranque, porque la asesora pidió evaluar con más profundidad antes de prometer. Fuera de alcance: conciliación bancaria y otras tareas complejas, e integraciones con el sistema administrativo (Valery) y la facturación digital (HKA); no se nombran los sistemas en el deck.
- Licencias (Ivana: «sí, diga las licencias»): tarjeta de Claude Team estándar a valor de lista con fecha, verificado el 16/10/2026 en support.claude.com: mínimo de dos puestos, USD 25 por puesto al mes pagando mensual o USD 20 pagando por año, con Claude Code incluido. Se muestra el ejemplo de tres puestos (la persona que lidera la clínica y hasta dos más): USD 75 al mes. La minuta dice «~USD 100/mes por 4 asientos» (4 por 25): Ivana no dijo cuántos puestos; el número lo decide COD. Segunda tarjeta: alojamiento, dominio y citas, sin valores porque no hay fuente; se informa el valor de lista antes de construir.
- CRM: la minuta pide enviar referencias de costos de licencias de CRM, pero no dice cuál ni trae valores, y no está en las 16 h de la asesora. Queda fuera de alcance y en la ruta que sigue. Pendiente: qué CRM y sus valores de lista, como entrega aparte a la dirección de COD.
- Google: el contexto dice «conectar su Google Workspace»; la minuta dice que solo tiene una licencia personal Pro y ninguna empresarial. Ivana no respondió. El deck dice «conectado a las herramientas de Google» sin nombrar Workspace.
- Facilidad de pago (la dirección necesita cuotas; la minuta menciona un inicial de unos USD 2.000 y mensualidades de USD 1.000 a 1.500, que no son de esta propuesta de 16 h): 3 cuotas ligadas a hitos, 40 % al aprobar, 40 % con la web publicada y 20 % al cierre. Los porcentajes los propuso el sistema y Ivana no los confirmó. Los montos son campos vacíos para ventas. Los montos de la minuta no se escriben en el repositorio.
- Seguimiento 30-60-90 sí (la asesora lo incluye; la minuta menciona un informe de retorno). Retorno en modo método, sin cifras: no hay datos del cliente. No se usa el caso DUSA de la minuta (no hay fuente documentada del cliente aquí).
- Participantes: la persona que lidera la clínica y hasta dos personas de su equipo que ella elija, sin nombres. La asesora recomienda incluir a su socia y a una persona de apoyo interno; eso queda solo en el brief. El hijo que ya usa Claude, los médicos socios (se suman después) y la doctora con 40 pacientes al día no se nombran.
- Modalidad remota, con presencial en Barquisimeto solo si COD cubre los viáticos (asesora y minuta).
- Posicionamiento (la asesora): se construye con ellos y la capacidad queda instalada. La historia de agencias que cobraron y no entregaron no se menciona; el deck dice que nada se entrega hecho.
- Datos sensibles: la cédula del paciente es un dato personal. El deck dice que las herramientas con datos de pacientes se construyen con datos de ejemplo y autorización de la clínica, y que no incluyen historias clínicas. Es una decisión del sistema; por confirmar.
- Acceso a Claude desde Venezuela: no se menciona (criterio de Simple TV y Go Pharma) ni se promete VPN.
- Visión a futuro (la asesora): Detección de la clínica, el resto del equipo, compras y administración. Va en `siguiente_etapa` sin cotizar, comprometer ni fechar; los médicos socios se mencionan como parte del resto del equipo.
- Contexto interno que no va en el deck: precios de Detección y del proyecto global de la minuta; el cliente compara con nada más que su propio presupuesto; la regla de plazos (meta de arrancar antes de fin de año y lo grande en enero); la dependencia del sistema contable de las normas del SENIAT; los nombres de las personas.
- Sin semanas, sesiones ni fechas (CLAUDE.md §4.23): la asesora habla de sesiones (la web son 3); eso queda para el kick-off. La duración va en horas.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Confirmar con Ivana o María la división (Educación), la alianza (no) y que una sola propuesta basta (la minuta pide varias opciones).
- Confirmar que las 16 h cuadran con seguimiento de 2 h (la asesora lo tenía en 1,5 h) y el kick-off contado como trabajo.
- Confirmar los porcentajes de las cuotas (40/40/20) y que Ventas llene los montos.
- Equipo técnico: decidir el alojamiento de la web nueva, dónde está registrado el dominio, y qué herramienta de citas conviene (la actual por evaluar, o la que se adecue).
- Confirmar cuántos puestos de Claude Team (3 o 4) y si COD tiene Google Workspace empresarial o cuentas personales.
- Elegir qué CRM citar con referencias de costo (entrega aparte) y conseguir sus valores de lista.
- Conseguir transcripción de la reunión y datos del cliente (volúmenes, tiempos) si se quiere pasar el retorno a cifras.
- Valor, descuento, total y montos de cada cuota: campos vacíos para ventas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py cod-salud-visual-cai057      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh cod-salud-visual-cai057             # verifica, genera el PDF y ajusta los campos
```
