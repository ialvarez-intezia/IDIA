# Brief · Maenca · Servicio de Habilidades (CAI-052)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Maenca
- **Slug**: `maenca-cai052`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-052`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construcción guiada de 2 Cerebros Digitales (asistentes personales) con Claude y Obsidian para presupuestar con criterio propio: solución, estructura de trabajo, precios unitarios e informe, para los dos socios de Maenca
<!--auto:inicio-->
- **Alcance**: 8 entregables en 2 Cerebros Digitales · 16 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Enviada` el 14/10/2026 (`meta.json`; convención «terminado = enviado», lo estampa el wrapper del PDF)
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento (Verónica Rubio, 13/10/2026; de ella salen el contexto, los roles, los procesos y el uso esperado) + transcripción de la reunión por Google Meet del 13/10/2026 (de ella, lo que el cliente pidió entender antes de decidir y cómo arma hoy sus presupuestos). No hubo contradicciones entre ambas.
- **fecha_arranque_deseada**: no se preguntó (se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: la ficha dice que el cerebro opere «como una persona adicional» que cubra tareas que hoy no pueden atender por falta de personal; no hay volúmenes ni tiempos, así que el retorno va en modo método y no se agrega ROI.

## Contexto del cliente (interno, no va al deck)

- **Quién es:** constructora pequeña de remodelaciones y mantenimiento general, solo dos socios y sin empleados (micro/pyme). Primer contacto con Intezia: conocieron a la empresa en una charla en la Expo Construcción, no por prospección. Quien atendió la reunión es el socio fundador; su socio no participó, así que falta su validación.
- **Cómo trabajan (Contexto del equipo y Proceso 1 de la ficha):** uno visita al cliente, investiga la solución, arma la estructura desglosada de trabajo (las partidas con que se mide y se cobra) y el informe y presupuesto; el otro analiza precios unitarios (materiales, equipos, mano de obra), cómputos y costos. El proceso no está estandarizado y depende del criterio de cada uno; frecuencia puntual, por demanda.
- **Precios:** parte tiene una base propia, parte se saca de páginas web (Mercado Libre y otras) y los muy específicos se consultan por WhatsApp a los proveedores. No existe una base de precios armada («estamos en cero en esa parte»).
- **Stack:** mixto, hojas de cálculo en Sheets, Drive, Gemini «por practicidad» y Word (Excel quedó atrás). Se comunican por WhatsApp (una comunidad con tres grupos) y correo. La IA se usa solo como chat, sin criterio ni proceso definido; sin formación previa. En una ocasión se les acabaron los tokens de Claude.
- **Qué pidió:** entender antes de decidir (qué es Claude, Skills y Artifacts) y, a futuro, centralizar precios, proveedores y criterio de cotización para automatizar estructura de trabajo, presupuesto e informe. Receptivo pero confundido con los conceptos básicos; no cerró en caliente. Apertura al cambio media, patrocinio presente pero tibio, presupuesto no definido.
- **Qué recomendó la asesora:** un Cerebro Digital por socio (no los servicios para equipos). Prometió enviar la propuesta el 14/10/2026 con el video Loom del CEO mostrando su cerebro y agendar una llamada de cierre de dudas antes del fin de semana.

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Maenca (Verónica Rubio, 13/10/2026), transcripción de la reunión por Google Meet del 13/10/2026 e instrucción de Ivana del 14/10/2026: CAI-052, 2 Cerebros Digitales de 8 h cada uno, asesora Verónica Rubio
- **Fuente del insumo**: Ficha de Levantamiento y transcripción de la reunión (13/10/2026) e instrucción del usuario
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Instrucción de Ivana (14/10/2026): propuesta CAI-052 para Maenca, 2 Cerebros Digitales con 8 h cada uno, asesora Verónica Rubio, con la Ficha de Levantamiento (13/10/2026) y la transcripción de la reunión por Google Meet (13/10/2026). Cuando se contradicen manda la transcripción (§4.23); no hubo contradicciones.
- Horas: 8 h por Cerebro Digital, por instrucción de Ivana «en este caso» (la referencia de «Excepción — Cerebros Digitales» de empresa/politicas-comerciales.md es 6 h; mismo criterio de CAI-039 y CAI-048): 2 × 8 h = 16 h. La reunión de arranque (1 h) va aparte y no suma horas.
- Estructura: 4 entregables de 2 h por cerebro (Base, Grafo y dos de Uso). Frente a CAI-027 (3 entregables de 2 h), las 2 h adicionales se usan en una segunda Skill por socio, ligada a los procesos que describe la ficha. Cada entregable lleva sus viñetas de «incluye» (la slide 5 queda con poca carga sin ellas) y la letra de esa slide se subió en `overrides.css`: si se regenera con `--forzar-overrides`, se pierde ese ajuste.
- Reparto de los dos cerebros (Contexto del equipo de la Ficha): el Cerebro Digital 1 es para quien visita al cliente, investiga la solución, arma la estructura desglosada de trabajo y el informe y presupuesto; el Cerebro Digital 2, para quien analiza precios unitarios, cómputos de materiales y equipos y costos. Los nombres de las dos personas no van al deck.
- El cliente pidió entender Claude antes de decidir («qué es Claude, skills y artifacts»): el primer entregable de cada cerebro lo explica desde lo básico y cuándo conviene automatizar. La confusión del cliente con esos conceptos es contexto interno y no va al deck.
- Herramienta: Claude, que la asesora recomendó en la reunión. El cliente usa Gemini «por practicidad» y en una ocasión agotó los tokens de Claude; no se nombran Gemini ni Word en el deck ni se afirma que cambie de herramientas (CLAUDE.md §4.11): el cerebro se conecta a sus hojas de cálculo y archivos. La licencia de Claude (plan de pago por persona) va aparte, sin valor de lista ni quién la contrata.
- Claude Code: la asesora mostró el Cerebro Digital corriendo en Claude Code y la Ficha dice «Claude/Claude Code». El deck nombra Claude, Projects, Skills y Obsidian (como CAI-027 y CAI-039) y no promete la terminal; dónde corre cada cerebro se define en el kickoff. Por confirmar con Ivana.
- Claude sobre un cliente que opera desde Venezuela: no se menciona el acceso ni el riesgo de bloqueo ni se promete VPN (criterio de Ivana en Simple TV, Go Pharma y Banco Activo).
- Portada: tres hechos de la Ficha y la reunión (dos socios llevan todo el ciclo, información de precios dispersa, IA solo como chat). No van: nombres de las personas, cómo conocieron a Intezia, la cita del cliente, el nivel de patrocinio ni la disponibilidad presupuestaria.
- Alcance honesto: la conversación con los proveedores por WhatsApp sigue siendo manual (el cerebro incorpora lo que responden); un software de cotización o desarrollos a medida quedan fuera.
- Retorno en modo método: el cliente no declaró volúmenes ni tiempos (la frecuencia de sus presupuestos es «puntual / por demanda»). Sin casos de éxito con el cliente (primer contacto), sin contratación evitada y sin certificado.
- Sin facilidad de pago (`omitir: ["pago"]`, criterio de Ivana en las propuestas recientes): la disponibilidad presupuestaria del cliente no está definida; para agregarla, cuotas ligadas a los hitos de la ruta.
- División Educación y sin alianza (supuesto: empresa privada, no se preguntó). Modalidad mixta (supuesto del sistema). Sin semanas, sesiones ni fechas (§4.23).

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

- Definir inversión, descuento y total: ventas llena las tres cajas, que van vacías (16 h en total). Decidir si lleva facilidad de pago.
- Confirmar con el cliente quién de los dos socios es el Cerebro Digital 1 y cuál el 2. El segundo socio no participó en la reunión: falta su validación.
- Confirmar si cada cerebro corre en Claude Code (como en la demostración) o en Claude con Projects, y cómo se explica al cliente.
- Confirmar quién contrata la cuenta de Claude (plan de pago por persona) y el valor de lista con su fecha.
- Verónica prometió enviar la propuesta con el video del CEO mostrando su Cerebro Digital y agendar una llamada de cierre de dudas antes del fin de semana.
- Confirmar modalidad (remota o presencial) y el calendario de las dos personas en el kickoff.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py maenca-cai052      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh maenca-cai052             # verifica, genera el PDF y ajusta los campos
```
