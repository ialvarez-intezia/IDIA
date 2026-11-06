# Brief · Pago Directo · Servicio de Detección (DET-054)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Pago Directo
- **Slug**: `pago-directo-det054`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-054`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Auditar Finanzas y Operaciones de Pago Directo sobre lo que ya construyeron con Quorum y Claude, nivelar a quienes aún no han tomado la herramienta y dejar logros inmediatos, un plan común y prioridades con retorno medible, con Tecnología al final para conocer el informe y dejar todo documentado
<!--auto:inicio-->
- **Alcance**: 2 áreas (Finanzas, Operaciones) · 8 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Contexto de la reunión con la dirección de Pago Directo, resumido y pasado por Ivana el 06/11/2026, más sus instrucciones: propuesta de Detección DET-054 con María Iribarren como asesora, 8 h de levantamiento (Finanzas y Operaciones a 4 h; Tecnología no se audita, solo participa al final). Sin Ficha de Levantamiento ni transcripción. División Educación, sin alianza y asesora confirmadas con Ivana
- **Fuente del insumo**: Resumen de la reunión con la dirección de Pago Directo, pasado por Ivana (06/11/2026); sin ficha ni transcripción
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (06/11/2026): propuesta de Detección DET-054 para Pago Directo con María Iribarren como asesora (directora comercial, datos ya registrados), a partir de un resumen de la reunión. División Educación y sin alianza confirmadas con Ivana. Sin Ficha de Levantamiento ni transcripción (CLAUDE.md §4.23): el resumen es la única fuente, así que la estructura sigue la Detección estándar y no las «áreas propuestas» del resumen.
- Empresa de pagos y servicios alrededor de estacionamientos (también parquímetros, seguros, colegios y aliados): 70 personas, de las cuales 40 a 50 son núcleo de oficina; el resto (taquilla y calle) no usa estas herramientas y no entra.
- Áreas auditadas: Finanzas (4 personas, una quinta por entrar) y Operaciones (unas 2 personas clave; confirmar si entra el equipo completo o solo esa parte). Ajuste de Ivana (06/11/2026): Tecnología (unas 8 personas, contando a quienes participaron en el hackathon) NO se audita; no es área central del paquete y son quienes más avanzados están. Se involucra solo al final, para presentarle el informe, que tenga contexto, lo conecte con la estrategia y deje todo documentado. Por área, una persona estratégica y otra operativa que conozca el detalle. Antes (versión del 06/11 por la mañana) eran 3 áreas y 12 h; con 2 áreas a 4 h quedan 8 h de levantamiento en global.
- Quién no entra: Axel (COO, uno de los founders; sostiene Motor Quorum y lo actualiza a diario) no forma parte del equipo del proyecto; la idea de Mark y Bento es quitarle carga. El deck no lo nombra: dice «una sola persona» y «lo que hoy sostiene una persona quede documentado». Mark y Bento ven la Detección como el comienzo, porque de ahí parte todo.
- Reconocer lo construido: el deck parte de Quorum (ERP propio con finanzas, comercial y tareas), Motor Quorum, Claude conectado a Quorum (MCP, sin la sigla), Wisi, la precalificación de leads, el semáforo de postventa, el presupuesto de mercadeo, las órdenes de pago en Quorum y las cuentas de Claude del equipo de oficina. No se les ofrece lo que ya tienen y no se habla como a quien arranca de cero; no se afirma migración de stack (§4.11). Las cuentas de Claude son de ellos: no se promete acceso ni VPN.
- Dolores de la portada (dichos en la reunión): sin plan común; adopción desigual; Motor Quorum sostenido por una persona; la atención de madrugada por WhatsApp, con consultas repetitivas. Operaciones («un universo gigante de mejora») y Finanzas (orden y monitoreo diario de entradas y salidas de pago) quedan como terreno del levantamiento, sin asignarles soluciones antes de detectar (§4.22).
- Horas: 8 h de levantamiento mostradas en global (2 áreas a 4 h, por la regla de Ivana de 4 h por área) y 2 h de Fundamentos de IA en un solo grupo (lineamiento de empresa/politicas-comerciales.md), pensadas para quienes aún no han tomado la herramienta (el resumen dice que Bento apuntaría a ellos); es propuesta mía, Ivana no la pidió. Con 40 a 50 personas de oficina el grupo máximo es de 25: confirmar a quiénes alcanza. Arranque sin horas. Sin semanas, sesiones ni fechas; sin horas de trabajo ni cantidad de consultores (§4.23).
- Retorno: modo método (sin cifras del cliente). El resumen dice «horas que hoy pierden por proceso frente a las horas después»; el deck lo expresa como método y estimación de referencia, no como compromiso. Se omiten licencias de IA como entregable (ya tienen cuentas para todo el equipo de oficina) y se sustituyen por «Retorno medible por proceso».
- Ruta completa con solo dos pasos (Detección ahora, Habilidades después): Políticas no se habló en la reunión y no se ofrece. Habilidades se presenta como «construir con ustedes, en vivo, los agentes y automatizaciones de los procesos que ya tienen claros».
- Sin facilidad de pago (Ivana, 06/11/2026): la lámina de pago se omite; el deck queda en 8 láminas y la forma de pago la define ventas.
- Modalidad: el resumen no la dice; el deck propone presencial o virtual según cada área, a acordar en el arranque.

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

- Confirmar con María la moneda de facturación y el valor (campos vacíos para ventas); la facilidad de pago se quitó.
- Confirmar la modalidad (presencial o virtual) y la ciudad.
- Confirmar si en Operaciones entra el equipo completo o solo las 2 personas clave, y quiénes son la persona estratégica y la operativa de cada área.
- Confirmar si a las 8 h se suma o no la nivelación de 2 h (propuesta mía), a quiénes alcanza y si se omite dado que ya tienen cuentas de Claude para toda la oficina.
- Conseguir la transcripción de la reunión y la Ficha de Levantamiento, y ajustar el deck si algo se contradice (manda la transcripción).
- Confirmar con María cuál es el nombre completo y cargo de quien decide en Pago Directo (Mark y Bento) para dirigirle la propuesta.
- Definir inversión, descuento y total (campos vacíos para ventas).
- Confirmar con Ivana las 8 h de levantamiento (2 áreas a 4 h) ahora que Tecnología no se audita, o si se mantienen 12 h.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py pago-directo-det054      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh pago-directo-det054             # verifica, genera el PDF y ajusta los campos
```
