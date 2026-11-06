# Brief · DUSA · Servicio de Detección (DET-042)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: DUSA
- **Slug**: `dusa-operaciones-det042`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-042`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Auditar las seis áreas de Operaciones de DUSA (Logística nacional, Planificación, Procura, Calidad, Seguridad Industrial y Manufactura), nivelar a sus líderes en IA y dejar logros inmediatos y un mapa de oportunidades para mejorar sus procesos
<!--auto:inicio-->
- **Alcance**: 3 áreas (Logística nacional, Planificación, Procura) · 24 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 4 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Facilidad de pago · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414-0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Sesión inicial del 27/10/2026 con el equipo de Operaciones de DUSA (María Iribarren y David Prato por Intezia; Marco Pisani y su equipo por DUSA), con la transcripción y el resumen de María; instrucciones de Ivana del 27/10/2026: Detección, contacto María Iribarren. Código DET-042, división Educación y sin alianza, por confirmar
- **Fuente del insumo**: Transcripción de la sesión inicial con Operaciones de DUSA (27/10/2026) y resumen de María Iribarren
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (27/10/2026): propuesta de Detección para Operaciones de DUSA; contacto María Iribarren (directora comercial, que dirigió la reunión). Código DET-042 (siguiente libre tras DET-041), división Educación (DUSA es Educación en CH-007, CAI-035 y CAI-059) y sin alianza: los tres por confirmar con Ivana.
- Insumo: transcripción de la sesión inicial (27/10/2026) y resumen de María. Coinciden. La transcripción tiene un detalle que el resumen no: Wilmer pidió hablar de «mejorar procesos» y no de automatizar, por eso el deck dice «mejorar» y nunca «automatizar».
- Áreas (María: «las 3 áreas principales y espacios para estas otras 3»): el deck muestra las seis áreas por igual, como las nombra el cliente (Logística nacional, Planificación, Procura, Calidad, Seguridad Industrial y Manufactura), porque la regla de Detección no admite áreas prioritarias (CLAUDE.md §4.22). Las tres primeras son las que DUSA priorizó por resultados más rápidos y las otras tres las pidieron Wilmer y Dexsis (Seguridad y Calidad) y salieron en la reunión. Si DUSA decide dejar fuera alguna, las horas bajan de 18 a 3 por área.
- Horas: 18 h de levantamiento en global (6 áreas por unas 3 h; DUSA y David hablaron de 2 a 4 h por área y de unas 3 h en promedio) y charlas de Fundamentos de IA de unas 3 h, 2 en paralelo (Grupo A y Grupo B). El deck no muestra el reparto por área ni el número de charlas ni de consultores (reglas de Keiber y de Ivana del 27/10/2026): solo «charlas por grupos de áreas» y las 18 horas de levantamiento.
- Grupos de las charlas: DUSA los enviará antes del viernes 30/10 (Grupo A y Grupo B, con la disponibilidad de cada líder). El deck los deja a definir y dice que el contenido se adapta a cada grupo.
- Calendario (no va en el deck, §4.23): visita presencial tentativa del 9 al 13/11 (DUSA tiene auditorías del 2 al 6/11), el equipo sale de Caracas; la charla sería la tarde del día del viaje y el levantamiento arrancaría al día siguiente a las 7:00 a. m. (jornada de planta de 7:00 a 15:30). Con dos consultores en paralelo caben 2 áreas de 3 h por consultor y por día. DUSA pide el menor número de días posible por costos: falta decidir si son 1 o 2 días y confirmar la disponibilidad de David y Keiber.
- Sistemas: JD Edwards en la nube, centralizado por Sistemas (módulos de procura, manufactura y finanzas). Intezia no tiene acceso: se trabaja a partir de los reportes (se bajan a Excel). El deck lo dice como fuera de alcance. No afirma migración de stack (§4.11).
- Interés del cliente (guía la conversación, no la estructura): en Procura, el análisis de cotizaciones, el análisis anual de precios, impacto financiero y riesgo de suministro (matriz de riesgo), los flujos de caja mensuales y los indicadores de gestión; en Planificación, el almacén de materias primas y los requerimientos de compra. No se prometen ni se asocian a una herramienta. El deck no pre-recomienda ninguna herramienta de IA (la da el Informe Final): David mencionó Copilot, Claude y Gemini solo como ejemplos.
- Departamentos: salen de lo que dijo el equipo (distribución nacional, logística internacional, planificación de alcoholes y de producción, almacén de materias primas, cadena de suministro, compras, y elaboración, producción y envasado). No hay organigrama desglosado, así que no se asignan a cada área. Logística internacional se mostró porque Marco dijo que «puede llevarse»; por confirmar.
- Personas: Procura tiene al jefe y 4 compradores; Logística, 6 personas; Planificación, el jefe y una persona más (muy buena en IA, puede apoyar). El deck no nombra personas de DUSA. Quienes asistieron: Marco Pisani (director de Operaciones), los jefes de Procura, Planificación de Alcoholes y Logística y Distribución Nacional, el jefe de Cadena de Suministro y un planificador de producción; de Talento Humano, Wilmer, Dexsis y Antonielis.
- Pago: estándar de Detección (50 % al aprobar y 50 % con el Informe Final), montos vacíos. Ivana no indicó si DUSA lleva facilidad de pago: confirmar. Viáticos del equipo: María los confirma; no constan en el deck.
- Sin Fundamentos como «curso»; sin semanas, sesiones ni fechas; sin horas de trabajo ni cantidad de consultores (CLAUDE.md §4.23).

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

- Confirmar con Ivana el código DET-042, la división Educación y que no hay alianza.
- Decidir si las seis áreas van todas en la inversión de 18 h o si Calidad, Seguridad Industrial y Manufactura van como espacios aparte (María pidió «espacios para estas otras 3»).
- Decidir cuántos días de visita (1 o 2) y confirmar la disponibilidad de David y Keiber para la semana tentativa del 9 al 13/11.
- Confirmar con María los viáticos y si se incluyen en la inversión (fuera del deck).
- Esperar los Grupos A y B de DUSA (antes del viernes 30/10) y adaptar el contenido de las charlas.
- Preparar el guion y la ficha de detección para Logística, Procura y Planificación.
- Confirmar si DUSA lleva facilidad de pago (por defecto, 2 cuotas 50/50) y la moneda de facturación.
- Valor, descuento y total: campos vacíos para ventas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py dusa-operaciones-det042      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh dusa-operaciones-det042             # verifica, genera el PDF y ajusta los campos
```
