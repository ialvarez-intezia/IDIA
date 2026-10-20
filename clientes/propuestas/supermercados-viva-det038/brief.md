# Brief · Supermercados Viva · Servicio de Detección (DET-038)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Supermercados Viva
- **Slug**: `supermercados-viva-det038`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-038`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Mapear los procesos de los 9 gerentes de Supermercados Viva, dejar logros inmediatos y una ruta de IA con agentes, skills, licencias y políticas de uso, para que cada gerente lleve la IA a su equipo
<!--auto:inicio-->
- **Alcance**: 1 área (Los 9 gerentes) · 9 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Supermercados Viva, versión de la Propuesta 2 (Flavia Martínez, registrada el 13/10/2026; PDF del 15/10/2026), usada solo como referencia porque no hay ficha propia de esta propuesta, e instrucciones de Ivana del 16/10/2026: tercera propuesta de Viva, solo para los 9 gerentes (sin nombres ni áreas), 2 h de fundamentos y 9 h de levantamiento, sin facilidad de pago. Sin transcripción de la reunión
- **Fuente del insumo**: Ficha de Levantamiento de Supermercados Viva (Flavia Martínez, 13/10/2026, versión de la Propuesta 2) como referencia, e instrucciones de Ivana; sin ficha propia ni transcripción
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (16/10/2026): tercera propuesta para Supermercados Viva, solo para los gerentes: 9 personas. Es independiente de las otras dos (DET-036, solo Tecnología con 12 personas; DET-037, siete áreas con 25 personas) y sus números no se mezclan con los de ellas. Asesora: Flavia Martínez.
- Código DET-038 confirmado por Ivana. Servicio Detección, división Educación y alianza «no», como en las otras dos propuestas de Viva; no se preguntó de nuevo, por confirmar.
- Sin ficha propia: Ivana indicó usar la ficha de la Propuesta 2 como referencia. De ella sale el contexto (sistemas, falta de licencias, uso suelto de la IA, regla de datos de Tecnología) y la lectura de esta propuesta: la ficha dice que la adopción empieza «por líderes de área que luego repliquen al resto», por eso el deck dice que cada gerente lleve la IA a su equipo. No hay transcripción ni resumen propio de la reunión.
- Los 9 gerentes: Ivana no tiene sus nombres, cargos ni áreas y pidió escribir solo «9 gerentes». El deck no lista áreas ni departamentos: el alcance es una sola tarjeta («Los 9 gerentes»). Por eso no se citan procesos de un área concreta (el cruce de facturas de cuentas por pagar, el filtro de currículos): no se sabe si esos gerentes están entre los 9. Si Ivana consigue la lista de cargos, el alcance puede pasar a áreas.
- Horas (Ivana): 2 h de Fundamentos de IA en un solo bloque para los 9 gerentes (bajo el máximo de 25 por grupo) y 9 h de levantamiento, mostradas en global. Ivana dijo «quizás 9 h» y luego confirmó. El arranque no suma horas. Las 2 h de nivelación se muestran en el deck (etapa, entregable y hoja de inversión), como en Cinex y en las otras dos propuestas de Viva, aunque la spec de Detección no las muestra (plantillas/deteccion-compacto.md §2).
- Temario de la nivelación (Ivana: el mismo de la Propuesta 2 para el resto de las áreas): qué es y qué no es la IA, cómo pedirle bien y qué información cuidar, con ejemplos de cada gerencia. Sin bloque técnico y sin historia (la gerencia de Tecnología lo pidió). Si Tecnología está entre los 9, también recibe solo fundamentos. Los temas se ajustan tras medir la madurez del equipo.
- Licencias: igual que en las otras dos propuestas. Se menciona Claude Team como punto de partida, se evalúa durante el servicio y la recomendación final llega en el Informe Final. Sin puestos ni valores. Valores de lista de Claude Team verificados el 16/10/2026 en support.claude.com.
- SAP: integraciones no se prometen; va explícito en el fuera de alcance. La regla de datos de Tecnología (la información sale de SAP Business One y Profit, no de Excel) va en el Informe Final como algo cuya viabilidad se evalúa. Se menciona sin atribuirla a una persona.
- Agentes: el mapa indica dónde hace falta un agente y dónde basta una skill; el canal de atención por WhatsApp que el cliente prepara va como ejemplo, sin decir para qué lo usa.
- Valor por gerencia: va en la tarjeta «Mapa de Calor por gerencia», en el Informe Final («diagnóstico por gerencia») y en el objetivo «El valor de cada gerencia». No se cita que hay gerentes que hoy dicen que no hay nada que automatizar: son justamente los lectores de esta propuesta.
- Logros inmediatos: se mantiene el mínimo de 3 en todo el proyecto, no uno por gerente. No se nombran ejemplos concretos porque no se sabe de qué áreas son los 9 gerentes; se identifican con cada gerente en su levantamiento.
- Habilidades como fase siguiente (según la ficha: «Habilidades la quiere estimar para el año que viene»): que cada gerente lleve skills a su equipo. Intezia no desarrolla las skills: acompaña al equipo a realizarlas (corrección de Ivana, 16/10/2026).
- Sin sucursales: no se menciona la cantidad de sucursales (instrucción de Ivana). La ficha dice que Viva está instalando la 7ª.
- Un espacio por gerente: cada gerente se levanta por separado, nunca varios en la misma mesa (regla de Detección). 9 h para 9 gerentes: el deck dice que las horas se reparten según lo que necesite cada gerencia.
- Contexto interno que no va en el deck: el dueño decide y quiere avanzar muy rápido; la gerencia de Tecnología anticipa que le costará venderla adentro y compara con otros dos proveedores; patrocinio ejecutivo aún no asegurado; presupuesto en evaluación; hay gerentes que hoy dicen que no hay nada que automatizar; los nombres de las personas.
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
- Conseguir la lista de cargos o áreas de los 9 gerentes (sin nombres) y decidir si el alcance pasa a áreas.
- Conseguir ficha propia y transcripción de la reunión: solo hay la ficha de la Propuesta 2 como referencia (CLAUDE.md §4.23).
- Validar el temario de Fundamentos con quien imparta la nivelación.
- Cómo se mide la madurez en IA antes de nivelar y quién la aplica.
- Valor, descuento y total: campos vacíos para ventas (presupuesto «en evaluación»).
- Confirmar con la gerencia de Tecnología que esta propuesta no se solapa con la DET-037 (los gerentes ya están entre sus 25 personas).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py supermercados-viva-det038      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh supermercados-viva-det038             # verifica, genera el PDF y ajusta los campos
```
