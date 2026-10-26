# Brief · C&C · Servicio de Detección (DET-041)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: C&C
- **Slug**: `cc-det041`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-041`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Auditar las 4 áreas de C&C (Ventas / Comercial, Administración y contabilidad, Producción / Planta y Dirección General), nivelar al equipo en IA y dejar logros inmediatos y un mapa de oportunidades que ordene los procesos antes de que el sistema centralizado que construyen empiece a recibir datos
<!--auto:inicio-->
- **Alcance**: 4 áreas (Ventas / Comercial, Administración y contabilidad, Producción / Planta, Dirección General) · 18 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de C&C (Verónica Rubio, registrada el 22/10/2026; contacto Karla, Gerencia de Ventas) e instrucciones de Ivana del 23/10/2026: código DET-041, asesora Verónica Rubio, división Educación, sin alianza, 18 h de levantamiento y 2 h de nivelación, modalidad mixta, sin facilidad de pago y ruta completa por defecto. Sin transcripción de la reunión
- **Fuente del insumo**: Ficha de Levantamiento de C&C (Verónica Rubio, 22/10/2026); sin transcripción de la reunión
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (23/10/2026): propuesta de Detección para C&C, código DET-041, asesora Verónica Rubio. Educación y sin alianza, 18 h de levantamiento y 2 h de nivelación, modalidad mixta, sin facilidad de pago y ruta completa por defecto, confirmados por Ivana el 23/10/2026.
- Insumo: solo la Ficha de Levantamiento (22/10/2026). No hay transcripción de la reunión (CLAUDE.md §4.23). El resumen de la ficha no define la estructura: las 4 áreas se muestran tal como las lista el cliente, sin prioridades. Ivana pidió ponerlas tal cual las nombra la ficha; «Administración (contabilidad y administración)» se acortó a «Administración y contabilidad» por el largo de la tarjeta.
- Horas (Ivana): 18 h de levantamiento en global, sin reparto por área, y 2 h de Fundamentos de IA en un solo grupo para las 10 a 12 personas (bajo el máximo de 25). El lineamiento de Detección daría 16 h (4 h por área en 4 áreas); Ivana pidió 18 h. La ficha dice «45-60 min c/u» por conversación y de 4 a 6 personas a entrevistar: las 18 h se reparten en el arranque según lo que necesite cada área; hay que confirmar la disponibilidad real. Arranque sin horas.
- Las 2 h de nivelación se muestran en el deck (etapa, entregable y hoja de inversión), como en AGN, Cinex y Supermercados Viva, aunque la spec de Detección no las muestra (plantillas/deteccion-compacto.md §2).
- Logros inmediatos (Ivana): la ficha identifica tres, que el deck nombra como posibles y sujetos a evaluación en el levantamiento: predicción de inventario y producción, carga digital de pedidos de los vendedores y control digital de gastos, cuentas por pagar y por cobrar. No se prometen ni se asocian a ninguna herramienta.
- Sistema centralizado (ERP), página web y app de condominios, con un desarrollador externo: el deck nombra solo «el sistema centralizado que construyen» y dice que se revisa en el levantamiento si es posible conectarse con esa herramienta, sin prometerlo (Ivana). No se nombra al desarrollador ni se afirma el alcance técnico, que Karla no conoce; ese alcance hay que levantarlo con el jefe o el desarrollador. El deck no afirma migración de stack (§4.11) y evita la sigla ERP.
- Áreas: Producción / Planta se levanta solo con el gerente de planta (sin personal obrero, fuera del alcance); Dirección General, con el jefe, que viaja casi siempre. No hay lista de personal ni organigrama, así que no se asignan departamentos: la tarjeta «Qué miramos en cada proceso» es genérica.
- Stack: Microsoft 365, ChatGPT y Gemini de uso individual, información en papel y WhatsApp. El deck no pre-recomienda ninguna herramienta de IA (el cliente «espera la recomendación»): la da el Informe Final. Sin Claude ni VPN.
- Modalidad mixta (Ivana), una sola sede. Reunión presencial tentativa el martes siguiente a la entrega de la propuesta (23/10/2026).
- Contexto interno que no va en el deck: el jefe o dueño decide y firma todo (nombre sin indicar; Karla y las gerencias solo sugieren) y viaja constantemente; patrocinio ejecutivo aún no asegurado; presupuesto y horizonte sin definir; apertura al cambio alta; contadora y asistente administrativo sin nombre; micro o pyme de menos de 50 empleados. Karla enviará el correo del jefe para copiarlo en el envío. Las citas textuales de la ficha no se usan.
- Sin facilidad de pago (Ivana): 8 slides. Sin semanas, sesiones ni fechas (CLAUDE.md §4.23).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Detección (`plantillas/deteccion-compacto.md`, Keiber 2026-10-08): sin frentes ni áreas prioritarias antes de detectar (lo que el cliente señaló como interés guía la conversación, no la estructura); cada departamento por separado, con su líder y su mano derecha, sin tarea previa; horas en global, sin reparto por área; al menos 3 logros inmediatos en el proyecto (no uno por área); entregables nombrados, sin conteos.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Conseguir la transcripción de la reunión del 22/10/2026 (solo hay ficha) y confirmar que no contradice nada.
- Confirmar con Verónica si el jefe estará en la presentación de la propuesta y recibir su correo (Karla lo enviará) para copiarlo en el envío.
- Levantar con el jefe o con el desarrollador externo el alcance real del sistema centralizado, la web y la app, antes de prometer cualquier conexión.
- Confirmar con Verónica la disponibilidad real: el jefe casi nunca está en sede y la ficha da 45-60 min por conversación; las 18 h van en global.
- Confirmar con Ivana si el lineamiento de 4 h por área (16 h) se sustituye definitivamente por las 18 h pedidas.
- Confirmar el teléfono y el correo de Verónica Rubio (tomados de la DET-031).
- Valor, descuento y total: campos vacíos para ventas (presupuesto sin definir, moneda sin conocer).
- Validar con quien imparta la nivelación el temario y cómo se mide el punto de partida del equipo.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py cc-det041      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh cc-det041             # verifica, genera el PDF y ajusta los campos
```
