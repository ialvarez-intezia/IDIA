# Brief · Supermercados Viva · Servicio de Detección (DET-037)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Supermercados Viva
- **Slug**: `supermercados-viva-det037`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-037`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Mapear los procesos de las siete áreas de Supermercados Viva, dejar logros inmediatos y una ruta de IA con agentes, skills, licencias y políticas de uso, para que cada área gane capacidad propia sin depender de Tecnología
<!--auto:inicio-->
- **Alcance**: 7 áreas (Ventas, Finanzas, Cadena de Suministro, Operaciones, Talento Humano, Consultoría Jurídica, Tecnología) · 28 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 4 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Supermercados Viva, versión de la Propuesta 2 (Flavia Martínez, registrada el 13/10/2026; PDF del 15/10/2026), resumen de la reunión con la gerencia de Tecnología aportado por la asesora e instrucciones de Ivana del 16/10/2026: Propuesta 2 de las dos que pidió la gerencia (siete áreas junto con Tecnología, 25 personas), 28 h de levantamiento y 4 h de nivelación (2 h para Tecnología y 2 h para el resto), temario visible, sin facilidad de pago. Sin transcripción de la reunión. Código DET-037 confirmado por Ivana
- **Fuente del insumo**: Ficha de Levantamiento de Supermercados Viva (Flavia Martínez, 13/10/2026, versión de la Propuesta 2) y resumen de la reunión de la asesora; sin transcripción de la reunión
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (16/10/2026): Propuesta 2 de las dos que pidió la gerencia de Tecnología de Supermercados Viva. Cubre siete áreas junto con Tecnología, 25 personas: Ventas 3, Finanzas 5, Cadena de Suministro 6, Operaciones 1, Talento Humano 3, Consultoría Jurídica 1 y Tecnología 6. La Propuesta 1 (solo Tecnología, 12 personas) es independiente y sus números no se mezclan con los de esta. Asesora: Flavia Martínez.
- Código DET-037 confirmado por Ivana (DET-036 es la Propuesta 1).
- Servicio Detección, división Educación y alianza «no»: la ficha dice «Servicios de interés: Detección, Habilidades» y no menciona división ni alianza. Se infieren como en la Propuesta 1; por confirmar. Habilidades va solo como la fase que sigue, sin cotizarla.
- Horas (Ivana, 16/10/2026): 28 h de levantamiento (4 h por cada una de las 7 áreas, la regla estándar de Detección) y 4 h de nivelación: 2 h para Tecnología y 2 h para el resto de las áreas. El arranque no suma horas. Las horas de levantamiento se muestran en global, sin reparto por área. Las de nivelación se muestran separadas por pedido de Ivana, lo que se aparta de la spec de Detección, que no muestra grupos de nivelación (plantillas/deteccion-compacto.md §2).
- Temario de la nivelación (Ivana): Fundamentos de IA para todos, que es básico, más el temario de Tecnología ya definido en la Propuesta 1. Lectura tomada: el resto de las áreas recibe 2 h de Fundamentos de IA, y Tecnología recibe 2 h con los fundamentos y, a nivel técnico, agentes y skills, Claude Code y uso seguro de datos. Si Ivana quiere que Tecnología tome además los fundamentos con el resto, las horas cambian. Temas de Fundamentos tomados de las Detecciones de Acua-e y Conserval (qué es y qué no es la IA, cómo preguntarle con criterio, ejemplos de cada área, qué información cuidar); sin historia, porque la gerencia lo pidió («no quiero la historia, quiero ir de lleno»). Los temas se ajustan tras medir la madurez del equipo.
- Entregables: se omitió la tarjeta «Alcance y calendario» para dar una tarjeta a cada nivelación (la de Tecnología y la del resto). El calendario y el alcance se acuerdan en la reunión de arranque y aparecen en los próximos pasos.
- Licencias: igual que en la Propuesta 1. Se menciona Claude Team como punto de partida, se dice que se evalúa durante el servicio y que la recomendación final llega en el Informe Final. Sin puestos ni precios.
- SAP: integraciones no se prometen; va explícito en el fuera de alcance. La regla de datos de Tecnología (la información sale de SAP Business One y Profit, no de Excel) va en el Informe Final como algo cuya viabilidad se evalúa.
- Agentes: el mapa indica dónde hace falta un agente y dónde basta una skill; el canal de atención por WhatsApp que el cliente prepara va como ejemplo, sin decir para qué lo usa.
- Valor por área (la ficha pide que la Detección lo haga visible área por área): va en la tarjeta «Mapa de Calor por área», en el Informe Final («diagnóstico por área») y en el objetivo «El valor de cada área».
- Logros inmediatos: se mantiene el mínimo de 3 en todo el proyecto, no uno por área. Ejemplos de la ficha: filtrar currículos por zona de residencia (Talento Humano) y revisar qué IP y equipos están activos (Tecnología). Procesos concretos a mirar: el cruce de facturas de cuentas por pagar y la depuración de las hojas de Excel informales antes de cargarlas a SAP Business One; no se prometen como logros porque son procesos de más esfuerzo.
- Habilidades como fase siguiente: que cada área automatice sus procesos con sus propias skills y agentes sin depender de Tecnología. Intezia no desarrolla las skills: acompaña al equipo a realizarlas (corrección de Ivana, 16/10/2026). La estimación es para el año que viene, según la ficha.
- Sin áreas prioritarias: la ficha rotula cada área como «Area priorizada», pero las siete se auditan por igual. El deck las nombra como las nombra el cliente. Las píldoras de la slide 2 dicen qué se mira en cada proceso: la ficha da responsables y roles (soporte técnico, compradores, nómina), no departamentos con organigrama.
- No se menciona la cantidad de sucursales (instruccion de Ivana): la ficha dice que Viva está instalando la 7ª, así que «7 sucursales» no era exacto.
- Contexto interno que no va en el deck: el dueño decide y quiere avanzar muy rápido; la gerencia anticipa que le costará venderla adentro y compara con otros dos proveedores; patrocinio ejecutivo aún no asegurado; presupuesto en evaluación; hay gerentes que hoy dicen que no hay nada que automatizar (no se cita, porque esos gerentes leerán la propuesta); los nombres de las personas de cada área; la propuesta primero la revisa la gerencia de Tecnología y luego se presenta a los directivos.
- Modalidad presencial en las oficinas, una sola sede. Horizonte de 3 a 12 meses y presupuesto «en evaluación»: no van en el deck (sin semanas ni fechas, §4.23).
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

- Confirmar con Ivana o Flavia la división (Educación), la alianza (no) y el servicio.
- Conseguir la transcripción de la reunión: solo hay Ficha y el resumen de la asesora (CLAUDE.md §4.23). Si contradice la ficha, manda la transcripción.
- Confirmar la lectura de la nivelación de Tecnología: 2 h con los fundamentos y el bloque técnico juntos, o fundamentos con el resto más 2 h técnicas.
- Validar el temario con quien imparta la nivelación: lo redactó el sistema desde la ficha y desde Detecciones anteriores.
- Cómo se mide la madurez en IA antes de nivelar y quién la aplica.
- Tecnología aparece con 6 personas en esta ficha y con 12 en la Propuesta 1: confirmar si las 6 son parte de las 12.
- Valor, descuento y total: campos vacíos para ventas (presupuesto «en evaluación»).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py supermercados-viva-det037      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh supermercados-viva-det037             # verifica, genera el PDF y ajusta los campos
```
