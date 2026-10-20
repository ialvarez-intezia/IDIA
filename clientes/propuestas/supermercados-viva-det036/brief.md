# Brief · Supermercados Viva · Servicio de Detección (DET-036)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Supermercados Viva
- **Slug**: `supermercados-viva-det036`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-036`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Mapear los procesos del departamento de Tecnología de Supermercados Viva, dejar logros inmediatos y una ruta de IA con agentes, skills, licencias y políticas de uso, para que Tecnología lidere la adopción en la empresa
<!--auto:inicio-->
- **Alcance**: 1 área (Tecnología) · 8 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Supermercados Viva (Flavia Martínez, registrada el 13/10/2026; PDF del 15/10/2026), resumen de la reunión con la gerencia de Tecnología aportado por la asesora e instrucciones de Ivana del 16/10/2026: Propuesta 1 de las dos que pidió la gerencia (solo Tecnología, 12 personas), 8 h de levantamiento y 2 h de nivelación con el temario visible, sin facilidad de pago. Sin transcripción de la reunión. Código DET-036: Ivana indicó DET-035, que ya es de Cinex
- **Fuente del insumo**: Ficha de Levantamiento de Supermercados Viva (Flavia Martínez, 13/10/2026) y resumen de la reunión de la asesora; sin transcripción de la reunión
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (16/10/2026): Propuesta 1 de las dos que pidió la gerencia de Tecnología de Supermercados Viva. Esta cubre solo el departamento de Tecnología (12 personas). La Propuesta 2 (varias áreas con Tecnología, 25 personas) es otra propuesta independiente, con su propia ficha y su propio código. Asesora: Flavia Martínez.
- Código DET-036: Ivana pidió DET-035, que ya es de Cinex (enviada el 15/10/2026). Se le preguntó y no respondió; se usó el siguiente libre. Si prefiere otro código, se cambia en `cliente.codigo` y se regenera.
- Servicio Detección, división Educación y alianza «no»: la ficha dice «Servicios de interés: Detección, Habilidades» y no menciona división ni alianza. Se infieren de un cliente corporativo nuevo y de las demás propuestas de Flavia; por confirmar. Habilidades va solo como la fase que sigue, sin cotizarla.
- Horas (Ivana, 16/10/2026): 8 h de levantamiento y 2 h de nivelación para las mismas doce personas; el arranque no suma horas. Las 2 h de nivelación se muestran en el deck (etapa, entregable y hoja de inversión) porque la gerencia pidió ver el contenido. Es la misma desviación de la spec de Detección que ya se aplicó en Cinex (plantillas/deteccion-compacto.md §2).
- Temario de la nivelación (Ivana: visible, a nivel técnico y no básico, y «se evalúa durante el servicio»): agentes y skills, Claude Code, uso seguro de la información e instrucciones para tareas de Tecnología. La gerencia hizo antes un programa largo de IA que no le sirvió: sin introducción histórica ni conceptos básicos. El deck dice que los temas se confirman tras medir la madurez del equipo. Los temas los redactó el sistema a partir de la ficha (Claude Code como palanca para un equipo sin área de desarrollo); no hay temario base de Intezia.
- Licencias (Ivana): se menciona Claude Team como punto de partida, porque es lo que el cliente quiere incorporar y lo que ya se le sugirió, pero se dice que se evalúa durante el servicio y que la recomendación final llega en el Informe Final. No se dice cuántos puestos ni se dan precios. Verificado (support.claude.com, 16/10/2026): desde enero de 2026 el puesto estándar de Claude Team incluye Claude Code, con menos límite de uso que el premium; por eso el deck habla de «tipo de puesto» a evaluar.
- SAP (Ivana: «ok con SAP»): integraciones no se prometen. Va explícito en el fuera de alcance: primero se analizan los procesos y su uso, y de ahí se define la implementación. SAP Business One, Profit (nómina) y Power BI aparecen como el contexto que el cliente ya usa, sin afirmar ninguna migración (CLAUDE.md §4.11).
- Regla de datos de Tecnología: toda la información debe salir de SAP Business One y Profit, no de Excel, y la gerencia pregunta si es viable. Va en el Informe Final: las políticas de uso la recogen y se evalúa si es viable. No se afirma que lo sea ni que no.
- Agentes: es lo que más interesa a la gerencia. El deck dice explícitamente que el mapa indica dónde hace falta un agente y dónde basta una skill, con un glosario corto de cada término. Se menciona el canal de atención por WhatsApp que el cliente prepara, como ejemplo; no se dice para qué lo usa porque la ficha no lo aclara.
- Logros inmediatos: se mantiene el mínimo de 3. De la ficha, la gerencia mencionó revisar qué IP y equipos están activos (va como ejemplo de logro) y la depuración de las hojas de Excel informales para pasarlas a SAP (va como proceso a mirar en el levantamiento, no como logro: es un proceso de más esfuerzo y, si lo es, pasa al Mapa de Calor).
- Un solo departamento: Tecnología, 12 personas (gerentes y coordinadores de TI) a entrevistar y a nivelar, presencial en las oficinas, una sola sede. No hay lista de personal ni organigrama, así que las píldoras de la slide 2 dicen qué se mira en cada proceso y no son subáreas. La gerencia aparece por su cargo, sin nombre.
- Contexto interno que no va en el deck: el dueño es quien decide y quiere avanzar muy rápido; la gerencia compara con otros dos proveedores; patrocinio ejecutivo aún no asegurado; presupuesto en evaluación; la propuesta debe poder leerse sin que la gerencia esté presente para explicarla.
- Los dolores de la portada salen de la ficha: IA usada de forma suelta y sin licencias corporativas, falta de un orden claro para implementarla, un departamento sin área de desarrollo que soporta 7 sucursales, y hojas de Excel informales que se cargan a mano a SAP. Son hechos de la ficha, sin cifras ni citas.
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

- Confirmar con Ivana o Flavia el código (DET-036), la división (Educación), la alianza (no) y el servicio.
- Conseguir la transcripción de la reunión: solo hay Ficha y el resumen de la asesora (CLAUDE.md §4.23). Si contradice la ficha, manda la transcripción.
- Departamentos y personas que la gerencia de Tecnología ya envió: no llegaron al repositorio. Con la lista se decide si el deck lleva departamentos reales.
- Validar el temario de la nivelación con quien la imparte: lo redactó el sistema desde la ficha.
- Cómo se mide la madurez en IA antes de nivelar y quién la aplica.
- Valor, descuento y total: campos vacíos para ventas (presupuesto «en evaluación»).
- Propuesta 2 (varias áreas con Tecnología, 25 personas): otra propuesta con su propia ficha y su propio código.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py supermercados-viva-det036      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh supermercados-viva-det036             # verifica, genera el PDF y ajusta los campos
```
