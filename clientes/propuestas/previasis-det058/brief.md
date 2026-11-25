# Brief · Previasis · Servicio de Detección (DET-058)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Previasis
- **Slug**: `previasis-det058`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección · 3 áreas (Suscripción, Administración y Siniestros) con nivelación de 30 a 35 personas y agente de soporte al afiliado construido en conjunto · 65 h (16 h de levantamiento, 4 h de nivelación, 45 h del agente: construcción, testeo y adopción) · Habilidades como siguiente paso, sin valor · formato compacto de Detección v3 (`DET-058`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Detección de oportunidades de IA en Suscripción, Administración y Siniestros de una empresa de medicina prepagada, con nivelación del equipo y un agente de soporte al afiliado construido en conjunto con las áreas
<!--auto:inicio-->
- **Alcance**: 3 áreas (Suscripción, Administración, Siniestros) · 16 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 4 h) · logros inmediatos cuando el proceso lo permite, sin cifra
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Previasis (Flavia Martínez, 11/11/2026) y resumen de Flavia con la ruta única: Detección con el agente de soporte dentro, Habilidades como siguiente paso. Instrucción de Ivana: sin precios ni fechas en la propuesta
- **Fuente del insumo**: Ficha de Levantamiento de Previasis y resumen de la asesora; sin transcripción de la reunión
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Cuenta (Ivana, 12/11/2026): Detección compacta (§4.22), Educación, sin alianza, código DET-058 (libre en el registro), asesora Flavia Martínez. Insumo: la Ficha de Levantamiento del 11/11/2026 y el resumen de Flavia; sin transcripción (si la hay y contradice, manda ella, §4.23).
- **Sin precios ni fechas (Ivana, 12/11/2026):** el deck no pone valores ni fechas. Quedan fuera el rango de Habilidades (4.500 a 8.000 REF), la fecha de la presentación en vivo y la de la migración de sistema del cliente. Habilidades va solo como siguiente paso, en la ruta completa, sin valor y sin horas. Los campos de inversión y de las cuotas quedan vacíos para ventas.
- **Una sola ruta (Flavia):** Detección primero; Habilidades se arma después con lo que se mapee, con las personas más pertinentes (no las 35). El agente de soporte va **dentro de la Detección**, como entrega final, construido en conjunto con las áreas en vivo.
- Horas (propuesta mía, aceptada por Ivana): **65 h** = levantamiento 16 h en global (Suscripción 4, Siniestros 4 y Administración 8 por sus cuatro departamentos: cobranzas, cuentas por pagar, cuentas por cobrar y tesorería), nivelación 4 h (30 a 35 personas: las tres áreas y los coordinadores de ventas, en dos grupos de hasta 25; sin grupos en el deck) y agente de soporte 45 h que incluyen construcción, testeo y adopción, en conjunto con las áreas (Ivana, 13/11/2026: antes eran 20 h de construcción). Las 45 h son un estimado a cerrar con Servicio.
- Sin dolor dramatizado ni citas (§4.22): el deck no cita «construir otro piso». Los dolores son hechos de la ficha: 9 personas de soporte para unos 15.000 afiliados, chatbot que solo enruta por botones, listas de unos 500 siniestros revisadas una por una, y uso de IA por cuenta propia sin criterio común. El resumen de Flavia dice que probaron el agente interno del CRM y falló: no va al deck (no se critica una herramienta del cliente).
- **Migración de sistema (§4.11):** el cliente migra su sistema administrativo, pero Intezia no lo afirma. El deck dice que la conexión del agente se define en el levantamiento según los sistemas disponibles; no promete integraciones ni nombra el sistema de destino. Pendiente interno de Servicio: decidir sobre qué sistema se conecta el agente antes de prometerlo.
- Herramienta del agente: el deck dice «una herramienta de automatización, como n8n, según la robustez que se detecte» (palabras de la ficha y de Flavia); no recomienda una herramienta de IA (la recomienda el Informe Final). Conectado a su WhatsApp, su CRM y su sistema.
- Qué hace solo el agente y qué escala: es soporte, no ventas (consultas, citas, pagos, enrutamiento y escalamiento a una persona); el cliente quiere capacidad agéntica y el deck lo dice: responde, orienta, enruta y consulta datos del sistema, y pasa a una persona lo que no resuelve. La lista fina de acciones se define en el levantamiento.
- Datos de salud y regulación: información de afiliados y siniestros de una empresa regulada por la Superintendencia de Seguros; pesa en el diseño del agente (accesos restringidos, escalamiento) y se dice en «Cómo cuidamos los datos».
- Lo que Miguel pidió y el deck no responde con cifras (son del equipo de Servicio y no van sin precios): total de Detección + Habilidades + implementación, costo de licencias por usuario para 30 a 35 personas y estimado mensual de tokens según el volumen de mensajes. El Informe Final lo incluye como «inversión inteligente en licencias»; la cifra se da en vivo.
- Impacto (Ivana, 12/11/2026): enfoque **operación**, sin cifras ni personas. Plan de pago estándar de Detección (50 % al aprobar, 50 % con el Informe Final y el agente); sin montos.
- El resumen dice que la propuesta pasa primero por María antes de la presentación en vivo: `meta.json` queda en Borrador.

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

- Servicio: decidir sobre qué sistema se conecta el agente (el cliente usa dos sistemas y migra), antes de prometer integraciones.
- Servicio: confirmar las 45 h del agente (construcción, testeo y adopción; antes 20 h), un estimado de licencias por usuario para 30 a 35 personas (qué plan recomendar) y un rango de tokens mensuales según el volumen. Flavia pide el volumen diario de mensajes de soporte a Miguel.
- Confirmar con Ivana o María si el deck debe mencionar n8n por su nombre (se dejó «como n8n») y si Habilidades lleva en la ruta alguna descripción más.
- Confirmar la modalidad (se puso presencial en Barquisimeto o remota) y qué sedes participan (gestión comercial en varias ciudades).
- Confirmar con el cliente quién entra a cada área (1 a 2 personas por área) y quiénes son los coordinadores de ventas de la nivelación.
- Ventas llena inversión, descuento, total y los montos de las 2 cuotas antes de enviar. La hoja sale con REF y la leyenda a tasa BCV (automático).
- La propuesta pasa por María antes de la presentación en vivo con Miguel.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py previasis-det058      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh previasis-det058             # verifica, genera el PDF y ajusta los campos
```
