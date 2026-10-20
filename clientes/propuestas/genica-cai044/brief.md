# Brief · Génica · Servicio de Habilidades (CAI-044)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Génica
- **Slug**: `genica-cai044`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-044`), presentada al cliente como **propuesta de proyecto**; formato compacto de 10 slides (dos hojas de inversión, una por etapa, y facilidad de pago en 3 cuotas; campos de monto vacíos para ventas)
- **Eje temático**: Nivelación y clasificación de los pioneros de Génica en el uso de la IA con gobernanza, ética y seguridad de datos en Microsoft 365 Copilot (Etapa 1) y, de forma opcional, optimización de 10 casos de negocio de Tecnología, Finanzas y Talento con los pioneros (Etapa 2)
<!--auto:inicio-->
- **Alcance**: 12 entregables en 3 bloques · 76 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Cómo trabajamos · 4 Ruta · 5 Entregables · 6 Retorno · 7 Inversión · 8 Inversión (etapa 2) · 9 Facilidad de pago · 10 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Génica (Flavia Martínez, 08/10/2026), transcripción de la reunión con el cliente e instrucciones de Ivana (09/10/2026) para la primera versión; ajuste del 11/10/2026 de Ivana: la prioridad de Génica es nivelar y clasificar a sus pioneros, así que la propuesta pasa a dos etapas con valores separados (Etapa 1 nivelación y clasificación, Etapa 2 opcional de optimización de los 20 procesos); ajustes finales de María (mensaje trasladado por Ivana, 13/10/2026): Etapa 1 en 16 h (2 grupos, cada uno con 2 h de clasificación y 6 h de Fundamentos), Etapa 2 de 120 h con un máximo de 6 h por proceso, proyecto de 136 h, plan de pago en 3 cuotas atadas a resultados, los 20 procesos contados como entregables, seguimiento explicado y Fundamentos con lo que aprenden; versión 2 del 15/10/2026 (Ivana, a partir del mensaje sobre lo que explicó Mauricio): la Etapa 2 pasa de 20 procesos a 10 casos de negocio de Tecnología, Finanzas y Talento, con hasta 6 h por caso (60 h) y proyecto de 76 h
- **Fuente del insumo**: Ficha de Levantamiento, transcripción de la reunión e instrucciones de Ivana (09/10/2026 y 11/10/2026) y ajustes finales de María (13/10/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- **Versión 2 (15/10/2026, Ivana): solo cambia la Etapa 2.** En lugar de 20 procesos son **10 casos de negocio**, y en esta versión se usa la frase «casos de negocio» y no «procesos» (en el lenguaje de Intezia, áreas a abordar). Enfoque: Tecnología, Finanzas y Talento, las áreas propietarias de los 10 casos; sin reparto conocido, el deck muestra una sola lista de 10 con las tres áreas nombradas. Horas (opción recomendada, elegida por Ivana): hasta 6 h por caso, 10 x 6 = **60 h** en la Etapa 2 y **76 h** en total (antes 120 h y 136 h). Etapa 1 sin cambios (40 a 60 pioneros, 2 grupos, 16 h), salvo que ya no dice «de los 20 procesos». Cuota 3: «con 5 de los 10 casos de negocio ya optimizados». Entregables CIE-01 a CIE-10, «Caso de negocio N optimizado con Copilot» (12 entregables en total). «Proceso» solo queda en la definición del nivel 3 del propio cliente. No hay en el repositorio la explicación de Mauricio: no se nombra a nadie y no se inventó nada de ella. **Las viñetas siguientes son de la versión 1 (13/10/2026) y las cifras de 20 procesos, 120 h y 136 h están superadas.**

- Versión del 11/10/2026 (Ivana): Génica prioriza nivelar a sus colaboradores en el uso de la IA con gobernanza, ética y seguridad de datos y ubicarlos por nivel. Los 20 procesos son el paso siguiente (optimizar, automatizar y resolver cuellos de botella) y, de los más de 90 procesos mapeados, tecnología ya resolvió o está resolviendo la mayoría; con todo eso, el alcance y el valor de la primera versión quedaban por encima de lo que necesitan aprobar ahora. La propuesta pasa a dos etapas con valores separados: Etapa 1 «Nivelación y clasificación de pioneros» (el foco, con su cotización) y Etapa 2 «Optimización de los 20 procesos» (opcional, con su valor; se puede contratar junto con la Etapa 1 o más adelante). Se mantienen el esquema, el enfoque en Copilot, el cuidado de los datos y «qué viene después». Nada de este contexto (que tecnología ya resolvió la mayoría) se muestra en el deck.
- Estructura por etapa (por_fases con dos fases): Alcance, Ruta y Entregables van separados por etapa; «Cómo trabajamos» sigue antes de la ruta (metodo_antes_de_ruta). Las dos áreas de la Etapa 1 (clasificación por nivel y nivelación) ya no son «paso previo»: son entregables propios (2 en la Etapa 1 y 20 en la Etapa 2, uno por proceso). El generador avisa de que por_fases sirve cuando hay pasos previos: aquí es a propósito, para separar por etapa.
- Horas por etapa (ajuste de María, 13/10/2026): Etapa 1 = 16 h: cada uno de los 2 grupos de pioneros recibe 2 h de clasificación y 6 h de Fundamentos, (2 + 6) x 2 = 16 (es la lectura de «2 h de clasificación y 6 h de Fundamentos para cada uno de los 2 grupos» que da 16 h). Etapa 2 = 120 h, con un máximo de 6 h por proceso (20 x 6). Total 136 h (antes 128 h: 8 h + 120 h, con 60 pioneros / 25 = 3 grupos de 2 h). Con 2 grupos ya no se dice «grupos de hasta 25». La revisión de los 20 requerimientos, que antes estaba en el levantamiento de 2 h, sigue dentro de las 6 h de cada proceso (no se añaden horas): confirmar con servicio.
- Una hoja de inversión por etapa (inversion.etapas): cada una con su valor, su descuento y su total, vacíos para ventas; la 2.ª lleva los campos con sufijo _2 en el PDF (PrecioBase_2, Descuento_2, PrecioTotal_2, Programa_2 y Notas_2). Se interpretó «el descuento por separado» como un descuento propio para cada etapa, de modo que la Etapa 2 pueda contratarse más adelante con el suyo; si Ivana lo quería como una sola línea de descuento sobre la suma, se cambia a inversion.partes.
- Plan de pago en 3 cuotas atadas a resultados (María, 13/10/2026): cuota 1 al firmar, para arrancar; cuota 2 al cerrar la Etapa 1, con los pioneros ya clasificados y nivelados; cuota 3 a mitad de las «sesiones» de los 20 procesos optimizados, redactada como mitad de la Etapa 2, con 10 de los 20 procesos optimizados, porque la propuesta no lleva sesiones (CLAUDE.md §4.23). Los montos van vacíos (campos PagoCuota1..3: los llena María). Los porcentajes 50/25/25 son los del plan anterior (retirado el 11/10/2026) y están PROVISIONALES: María no los dio. Sin «facturacion» (moneda y tasa): no se indicó.
- Garantía 30-60-90 solo en la Etapa 2 (revisión pedida por Ivana, que anticipaba que sería la 2): la garantía y el seguimiento miden uso real, nuevas construcciones y tiempo recuperado contra la línea base de cada proceso, que solo existe cuando se optimizan los procesos. La Etapa 1 (clasificación y nivelación) no lleva seguimiento ni garantía; su hoja de inversión lo aclara en una nota. Si Ivana prefiere una garantía de adopción también en la Etapa 1, se agrega en esa hoja (quitar sin_garantia y definir qué se mide).
- La Etapa 2 incluye «optimizar y automatizar» (la frase de Ivana): se redactó dentro de Microsoft 365 Copilot, sin prometer agentes de IA ni desarrollos a medida, que siguen en los niveles 2 y 3 (fuera de alcance). Confirmar con servicio hasta dónde llega la automatización en Copilot.
- Titular (Ivana, 11/10/2026, «hazlo atractivo»): «IA con criterio: pioneros nivelados y listos para liderar en Génica», en lugar de la versión descriptiva «Nivelación y clasificación de pioneros en inteligencia artificial en Génica». Alternativas pensadas: «Cada pionero en su nivel, todos con un mismo criterio de IA» y «De pioneros a referentes en IA: todos con el mismo criterio».
- Estructura según la Ficha de Levantamiento (Flavia Martínez, 08/10/2026), la transcripción de la reunión (manda sobre la Ficha) y las instrucciones de Ivana (09/10/2026): propuesta única de primera fase; los niveles 2 y 3 solo como referencia, sin personalizar ni cotizar. Se agrupa por fase (por_fases) y «Cómo trabajamos» va antes de la ruta (metodo_antes_de_ruta), como en la CAI-032.
- El «kick-off» de más de 1 h de la Ficha pasa a llamarse levantamiento de información (indicación de Ivana). La reunión de arranque de unos 30 minutos se mantiene aparte, como tercer paso de logística.
- 20 procesos = 20 requerimientos priorizados, uno por proceso (la Ficha habla de 20 requerimientos de más de 90 y de 20 procesos del mapa de procesos; Ivana los trata como equivalentes). El deck no nombra los procesos porque la fuente no los lista: se identifican en el levantamiento.
- Licencia paga de Microsoft 365 Copilot (respuesta de Ivana, 09/10/2026). Falta confirmar que los 60 pioneros la tienen asignada. En la reunión el cliente ofreció una licencia de desarrollo si Intezia debe trabajar dentro de su ecosistema; no se menciona en el deck.
- «Assessment» se evita por el anglicismo (indicación de Ivana): el deck dice evaluación de nivel. «Fundamentals» se escribe Fundamentos.
- Confidencialidad: Génica compartió su plan estratégico de forma confidencial; no está en el repositorio ni se cita. El deck solo usa cifras dichas en la reunión (40 a 60 pioneros, 20 requerimientos de más de 90). No se usa «6 de 29 iniciativas accesibles a IA» (la reunión habla de 29, luego 15 y de ellas 6, y contradice la Ficha) ni la meta de unas 300 personas del plan 2026-2027 (indicación de Ivana). Sin nombres de personas ni mención a la presidencia o al comité.
- Plazo del cliente (solo interno, la propuesta no muestra fechas, semanas ni sesiones): ejecución de la última semana de octubre a la última de enero; el comité de estrategia es el 14-oct y la propuesta debía llegar el 10-oct.
- Retorno en modo método: no hay cifras del cliente. La línea base de horas por proceso y el seguimiento a 30, 60 y 90 días son el estándar de Habilidades; el levantamiento de 2 h no menciona la línea base, así que se mide al arrancar cada requerimiento (confirmar con servicio).
- Datos sensibles (Cómo trabajamos): los ejercicios usan solo casos que Génica autorice, según su clasificación de la información. Es la práctica habitual de Intezia, no un compromiso que Génica haya pedido: confirmar con servicio.
- Asesora: Flavia Martínez, con el correo, teléfono y cargo de sus otras propuestas (Acua-e, IOED, Metalblanc, N58).
- Los 20 procesos como entregables (María, 13/10/2026): CIE-01 a CIE-20, «Proceso N optimizado con Copilot», de hasta 6 h cada uno. Los procesos no se nombran porque la fuente no los lista: se identifican en el levantamiento. La Etapa 2 cuenta ahora 20 entregables (antes 1) y el alcance vuelve a mostrar el conteo por fila.
- Fundamentos, qué aprenden (María, 13/10/2026): Copilot en Outlook, Excel, Teams y Word, aplicado a sus tareas reales; se muestra en el alcance, en «Cómo trabajamos» y en los entregables.
- Seguimiento a 30, 60 y 90 días (María, 13/10/2026): se explica que mide el uso real y el tiempo recuperado, en la ruta, «Cómo trabajamos», los entregables, el retorno y la hoja de la Etapa 2. Se conservan los tres hitos (30 días uso real, 60 días nuevas construcciones, 90 días tiempo recuperado contra la línea base).
- Fuera de este deck, a cargo de María (13/10/2026): los valores y las hojas de cotización, los montos de las cuotas, la página de valor de lista del proyecto completo con el descuento especial por cierre del proyecto completo (válido 15 días) y el documento de valor para la directiva. El deck conserva las dos hojas de inversión por etapa, con los campos vacíos. Génica puede iniciar solo con la Etapa 1 o con ambas etapas.

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

- Versión 2: confirmar con servicio que 6 h bastan para un caso de negocio (puede ser más amplio que un proceso; si no, subir las horas por caso), cuántos casos tiene cada área (Tecnología, Finanzas y Talento) y si Génica ya recibió la versión anterior, porque esta la reemplaza.
- Definir el valor, el descuento y el total de cada etapa y los montos de las 3 cuotas (campos vacíos para ventas; la Etapa 2 lleva los suyos con sufijo _2; las cuotas, PagoCuota1..3).
- Confirmar con María cómo se aplica el descuento especial por cierre del proyecto completo (válido 15 días) y si va en este deck una página de valor de lista del proyecto completo (hoy no existe: el generador solo dibuja las dos hojas por etapa), y que la garantía 30-60-90 va solo en la Etapa 2.
- Plan de pago: confirmar con María los porcentajes de las 3 cuotas (provisionales: 50/25/25, los del plan anterior), la moneda y la tasa de facturación, y qué plan aplica si Génica contrata solo la Etapa 1 (las cuotas 1 y 2 cubren la Etapa 1; la 3 depende de la Etapa 2).
- Confirmar con servicio las horas por etapa (versión 2: 16 h y 60 h, 76 h en total), que la revisión de la necesidad priorizada de cada caso entra en las 6 h y hasta dónde llega la automatización en Copilot.
- Confirmar con Génica que los pioneros tienen asignada la licencia paga de Microsoft 365 Copilot.
- Línea base de horas por proceso: se mide al arrancar la Etapa 2 (confirmar con servicio).
- La propuesta pasa por el equipo de servicio antes de enviarse: dejar meta.json en Borrador hasta entonces; si Génica ya recibió la versión anterior, avisar que esta la reemplaza.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py genica-cai044      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh genica-cai044             # verifica, genera el PDF y ajusta los campos
```
