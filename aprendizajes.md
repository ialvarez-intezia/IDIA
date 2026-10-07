# Aprendizajes y evolución del sistema

> Changelog del sistema. Orden cronológico inverso. Cada entrada en 2–4 líneas.

**Formato**: `## YYYY-MM-DD — [tipo] título` + qué cambió + por qué.
**Tipos**: `[arquitectura]` `[regla]` `[catálogo]` `[precio]` `[plantilla]` `[scripts]` `[cliente:<slug>]` `[preferencia]` `[bug]`.

---

## 2026-10-07 — [regla] Habilidades: la plantilla compacta v2 es el único formato, para toda categoría y cualquier cliente (sin guardia)
Instrucción del usuario: «a partir de ahora aplicarás este modelo/plantilla de propuesta para todos los servicios de habilidades de cualquier cliente; realiza los cambios internos que consideres necesarios». Hasta hoy `CLAUDE.md` §4.21 punto 5 pedía **preguntar una vez** si una charla, curso, diplomado o taller con programa de módulos iba en el compacto o en el deck canónico; ese paso desaparece.
**Qué cambió:** (1) `CLAUDE.md` §4.21: el compacto es el único formato del servicio; disparador por palabras (propuesta, cotización, charla, taller, capacitación, curso, diplomado); un programa de módulos se **reexpresa** sin preguntar y el deck canónico solo si el usuario lo pide expresamente; si pide «ajustar al formato nuevo» una propuesta previa, se rehace en v2 sin volver a preguntar. Se alinearon §1, §4.1a, §4.2, §6, `empresa/tipos-de-documento.md`, `plantillas/propuesta-comercial.md` y los tres `diseno-*.md` (quedan como guía para diseñar el programa, no como formato del deck). (2) `plantillas/habilidades-compacto.md`: nueva §1b con **recetas por categoría** (soluciones por área, capacitación por sesiones, Cerebros Digitales, charla, sesión única, curso, diplomado) y §4a con la **entrevista mínima** (una sola vez, todas las preguntas juntas). (3) Tres ejemplos nuevos probados (`datos.ejemplo-charla.json`, `-curso.json`, `-diplomado.json`, ficticios): los cinco ejemplos generan sin errores y con holguras y desborde en verde; el PDF completo de las variantes sin cotización deja solo los 2 campos de entregables. (4) Generador: con otro `vocabulario` el título de «Cómo trabajamos» y el subtítulo de entregables ya no hablan de «soluciones construidas, probadas y adoptadas»; el texto por defecto del destino del retorno se acortó para no marcar aviso con nombres de cliente largos. (5) `verificar-propuesta.sh` avisa (⚠, no bloquea) de toda propuesta con `servicio: habilidades` cuyo deck no sea el compacto.
**Para no olvidar:** en cursos, diplomados y charlas los textos por defecto (pasos del método, pasos del retorno) están escritos para soluciones por área: sustituirlos por los de la categoría, como hacen los ejemplos. Sin Ficha ni informe del cliente, los datos de portada son de contenido, no hechos del cliente.

## 2026-10-07 — [plantilla] Habilidades compacto v2.0: correcciones de la reunión de DUSA y feedback de Ventas (`correcciones.pdf`)
Pedido: «actualiza la plantilla genérica del servicio de Habilidades con las correcciones de este chat y todo lo que se mencionó en `correcciones.pdf`». Dos fuentes: la reunión de Keiber con María Iribarren sobre DUSA CAI-035 (2026-10-06, ya aplicada a mano en `dusa-cai035/`) y el documento de feedback de Ventas de María Iribarren, CCO (2026-10-07), que **aplica a todas las propuestas**. Keiber: «lo importante es estandarizar».
**Qué cambió (generador, CSS, verificador, spec y router §4.21):** (1) el orden es el de las preguntas del cliente: Portada · Alcance · Ruta · **Cómo trabajamos** · Entregables · **Retorno** · **Inversión (antepenúltima)** · **Facilidad de pago** · **Próximos pasos** (9 slides; 7 en Fundación o sin cotización). (2) **Lenguaje del cliente verificado por el generador**: bloquea «proceso base», «Frente A», «S1-S3», «F1», «carril», «8 de 15 h», «inversión por horas» y «precio»; avisa «costo»; «valor» o «inversión» siempre; compara los textos y avisa de frases repetidas entre slides. (3) El alcance dice qué resolvemos y para qué (`areas[].para_que`); las líneas de trabajo tienen nombre propio (`frentes[].nombre`). (4) «Cómo trabajamos»: pasos (el cuarto, medir), por qué en ese orden, **casos ya logrados con fuente documentada del cliente**, cómo funciona en la práctica con sus límites, cómo se cuidan los datos y 4 fichas de logística. (5) Retorno obligatorio y antes de la inversión, «Calendario de garantía y cálculo del retorno», «Hacia dónde va el proyecto» con tono aspiracional; la **contratación evitada** se plantea como probabilidad, nunca como compromiso. (6) **Facilidad de pago** en hoja aparte: cuotas ligadas a hitos, montos como campos editables y vacíos; los campos `PagoCuota1..N` se ajustan al número de cuotas que lee `agregar-campo-precio.py` en la página (`plan_pago_fields()`, misma geometría que `geometria_pago()`). (7) Próximos pasos con la **asesora comercial**. (8) Inversión del proyecto: duración con las soluciones primero y las horas al final; `Programa` con soluciones primero; `Notas` = garantía + términos. (9) Estimadores calibrados con medidas reales (alcance ±3 px, método ±1, retorno ±3) y modos de aire (`roomy`) para pocas filas.
**Conflicto resuelto con §4.10a:** Ventas pide explicar la metodología («cómo trabajamos y por qué en ese orden») y §4.10a retiró la slide ABR. Se resolvió con una slide que explica cómo se trabaja (pasos, límites, datos) y no la pedagogía; **decisión a confirmar con dirección**. También: el retorno pasó **antes** de la inversión (la reunión de DUSA lo dejaba al final) y, sin plan de pago propio, el generador usa el estándar 50/50 de `empresa/politicas-comerciales.md` con un aviso.
**Integración con GitHub (misma fecha):** el commit `369e87e` de Ivana trajo 13 propuestas compactas v1.x (G-MAX, Acua-e, Conserval, Clínica Santiago de León, CAI-034 a CAI-041, CH-015…) y cambios al generador: `vocabulario`, `composicion`, `servicio_rotulo`, `meta_servicio`, `meta_tipo`, `sin_hoja_cotizacion`, `seguimiento.tipo` y `inversion.sin_garantia`. La v2 los **absorbe** (se probaron con los 13 `datos.json` migrados de forma mínima) y agrega `omitir` para quitar método, retorno, próximos pasos, inversión o pago (charla). La ruta «las soluciones son las protagonistas» que pidió el usuario con la captura ya estaba en la v2 con otros nombres de clases. Las 13 propuestas v1.x **no se tocaron**: para modificar una, migrar su `datos.json` (spec §13) y regenerar con `--actualizar-css`; el generador v1.4 sigue en git (`369e87e`).
**Pruebas:** DUSA (9 slides) y Fundación (7) sin errores, holguras y desborde en verde; flujo completo de PDF con un slug temporal (12 campos con 5 cuotas, cada `PagoCuotaN` sobre su tarjeta); fuzz de 4.234 mutaciones sin un solo error interno; importador y hoja de captura del retorno con datos v2.
**Pendiente / para el usuario:** (a) `dusa-cai035/` (entregado, 7 slides hechas a mano) **no cumple** las reglas nuevas (sin «Cómo trabajamos» ni próximos pasos, retorno al final, «Frente A», «Inversión por horas de sesión»): se puede regenerar desde `datos.ejemplo-dusa.json` si se quiere enviar la versión nueva. (b) Las reglas de Ventas aplican a todos los servicios pero solo están implementadas aquí: los canónicos de Detección, Innovación y Políticas siguen como estaban. (c) Confirmar con servicio los datos de ejemplo (modalidad, asesora). (d) No se tocó nada operativo del correo de Ventas (fechas, rehacer propuestas, banco de casos).

## 2026-10-06 — [cliente:dusa-cai035] Correcciones de la reunión: soluciones antes que horas, entregables antes que precio, plan de pago y ejemplos ya construidos
Reunión de Keiber Quintana con María Iribarren sobre CAI-035 (deck de 7 slides; detalle en `clientes/propuestas/dusa-cai035/brief.md`). Lo que enseñó, en orden de utilidad
para futuras propuestas de Habilidades: (1) **Las horas generan rechazo**: poner la solución en grande y la hora en pequeño (frentes, celdas y fases de la ruta: «6 soluciones»
grande, «87 h» chico) y dejar «500 horas» al final de la frase de Duración. (2) **Orden de la lectura del cliente**: problema, qué se hace, cómo, **qué recibe**, cuánto cuesta,
cómo se paga, qué retorno. «Todo lo que recibe» va antes del precio. (3) **Plan de pago en hoja aparte** tras la cotización, para que esta no abrume: 5 cuotas ligadas a hitos
de la ruta (30, 25, 25, 10, 10 %), con **montos vacíos y editables** para que no se filtren. Grupo nuevo `PLAN_PAGO_FIELDS` (`PagoCuota1..5`, marker «Facilidad de pago» en el h2)
en `scripts/agregar-campo-precio.py`. (4) **Ejemplos ya logrados con el propio cliente** (los agentes construidos en las sesiones de Detección) en la slide de alcance, con las
cifras tal como las dice el informe de Detección: es el gancho más fuerte porque ya es real. Antes de usar una cifra dicha en voz alta, verificarla contra el informe: «casi 2 semanas»
era la demora actual de validar un pago, no un ahorro medido, y «9 soluciones instaladas» no figura. (5) **La contratación se plantea como probabilidad**, no como compromiso («alta
probabilidad de no tener que contratar las ≈10 posiciones»); no se pone un porcentaje sin base. (6) El cuarto paso por solución es **medir el retorno** («en tiempo y en
oportunidades de optimización»), y el calendario 30-60-90 se llama «Calendario de garantía». **Aplicado el 2026-10-07 en la plantilla v2** (ver la entrada de esa fecha; el grupo de campos pasó a `plan_pago_fields()`). Lo que se proponía: llevar estos cambios a la
plantilla compacta (`plantillas/habilidades-compacto.md`, generador y CSS: orden, módulo de plan de pago, franja de ejemplos, soluciones primero, cuarto paso) y documentar el grupo
nuevo en `plantillas/generar-pdf.md`. Mientras tanto la spec §12 deja de reproducir `dusa-cai035/` (el deck ya difiere en orden y en slides).


## 2026-10-06 — [cliente:n58-banco-digital] CAI-034: Mercadeo con Claude pasa del deck de 15 slides al compacto de 6
Pedido: «ajustar la CAI-034 hacia el nuevo formato». Se aplicó la misma estructura que su hermana CAI-037 (12 h = Fundamentals 2 + Construcción 3 sesiones de 2 + Implementación 2 sesiones de 2, kick-off de 1 h aparte), sin volver a preguntar el formato (destino ya fijado en [[ajustar-propuesta-previa-aplicar-reglas-de-fondo]]). **Mapeo:** carril «Claude», áreas = las 3 etapas (vocabulario «etapa»), cada sesión de 2 h = 1 entregable (6). Las 3 revisiones de la Construcción se leen como primer avance revisado, segundo ajustado y entrega final (más de 50 creativos y 4 artículos publicados): los nombres los propuso el sistema. La producción de Intezia entre sesiones no suma horas de sesión. Fases F1-F3 con títulos de 5-6 letras (Bases, Piezas, Skill) por la cabecera con conteo (ver DET-027).
**Cambios de fondo que el usuario debe conocer:** se retiran el certificado INTEZIA y el workbook del deck anterior (§4.21: no van por defecto), la slide de Impacto con estudios, Próximos pasos y Cierre; el retorno va en modo método. Se conserva el encuadre «parte del calendario de lanzamiento del banco, no un gasto aparte» y la modalidad presencial. Archivado en `_anterior-15-slides/`; `scripts/customize-n58-banco-digital.py` retirado.
**Gotcha del wrapper:** `pdf-habilidades-compacto.sh` aparta (y ante un fallo borra) TODOS los `*.pdf` de la carpeta y `customize-acroforms.py` exige uno solo: la carpeta de N58 guarda además `Soberanía de Datos - N58 (Tecnología).pdf`. Hubo que sacarlo antes de correr el flujo y devolverlo después. Lo mismo vale para cualquier carpeta con un PDF complementario. Hitos de la ruta: con 5 columnas, los títulos de más de ~28 caracteres se parten; «S5-S6 · Implementación» (notación ya usada en la misma slide) los resolvió.

## 2026-10-06 — [cliente:clinica-santiago-de-leon] DET-027: ruta al formato nuevo y entregables de Fundamentals sin «Grupo N»
Pedido: modificar la hoja de ruta «como debe ser ahora» y quitar «Grupo 1, 2, 3» de la slide 5. **Ruta:** el deck tenía el CSS viejo congelado (se hizo antes del cambio de la slide 3 «protagonistas = entregables, horas pequeñas»); se regeneró con `--actualizar-css` y se reescribieron los ajustes de ruta de `overrides.css` sobre las clases nuevas (patrón de Fivenca: `.rg-front-name`, `.rg-front-h b` a 16 px, no 24 px). **Gotcha:** la cabecera de fase suma el conteo («3 entregables») al rótulo y con 1 frente y 3 fases las columnas son angostas: los títulos de fase tienen que ser de **~6 caracteres o menos** (Inicio, Seguro, Logros; «Nivelación», «Seguros», «Pacientes» y hasta «Insumos» desbordaban). Los decks de Detección anteriores (Acua-e, Conserval, G-MAX) tienen títulos largos y lo van a necesitar al regenerarse. **Slide 5:** se preguntó entre 3 sesiones por áreas, 4 sesiones (24 h) o solo quitar «Grupo»; el usuario eligió **solo quitar «Grupo», sin repartir áreas**: «Primera/Segunda/Tercera sesión de nivelación en IA», subtítulo «uno por sesión y por área». Estructura y horas (22 h) sin cambios; «3 grupos» se conserva donde describe a los participantes.

## 2026-10-06 — [cliente:marcelo-restrepo-cai041] CAI-041: Cerebro Digital de marca personal con Claude para Marcelo Restrepo (compacto, 6 slides, 6 h)
Segunda de las 2 propuestas del mismo cliente (la 1 es CAI-040). Pedido: «haz la de cerebro bajo el CAI-041 para el mismo», con el contexto de la asesora: Cerebro Digital enfocado en su marca personal, que sirva para **editar videos y hacer diseños**. **Corrección del usuario:** sin horas en el pedido, la primera versión salió de 8 h en 4 sesiones (tomando como base el último precedente, CAI-039, que fue una excepción puntual) y el usuario respondió «este es de 6 h como los demás». Versión final: **1 cerebro de 6 h = tarifa de referencia** (CAI-025/027), 3 sesiones de 2 h una por semana (forma de CAP-060), reexpresado al compacto como 3 bloques y 3 entregables de 2 h: Marca (propósito, voz y audiencia + Project de Claude, todo en la sesión 1), Video y Diseño (una instrucción reutilizable cada uno). **Lección:** sin horas explícitas, un Cerebro Digital es de 6 h; el 8 h de Fivenca no es el precedente a copiar. La sesión 1 queda densa (fundamentos, documento de marca, Project y línea base) y depende de que el cliente traiga su material desde el kick-off.
**Alcance honesto de «editar videos»:** Claude no monta el archivo de video; prepara guion, plan de edición (cortes, ritmo, textos en pantalla), subtítulos, título y descripción por red, y el montaje lo hace el cliente en su herramienta (no nombrada). Automatizar el montaje exige terminal y queda como ampliación aparte. El deck lo dice en «fuera de alcance» y en las notas; el brief pide dejarle claro este alcance al cliente. Para diseño se verificó que Claude tiene funciones propias (vista previa, planes de pago a octubre de 2026): el deck dice «diseñar con Claude» sin nombrar el producto y la sesión 3 confirma qué incluye su plan.
**Decisión por confirmar:** versión **solo Claude, sin Obsidian** (los Cerebros Digitales anteriores CAI-005, 025, 027 y 039 llevan grafo de notas), por coherencia con CAI-040 y porque la memoria de una marca personal cabe en un Project. Si se quiere el estándar, se agrega y cambian las horas.
**Reglas del cliente repetidas:** el parentesco con el presidente de un banco sigue siendo contexto interno; el deck no menciona CAI-040, otras herramientas ni Obsidian. Misma cuenta de Claude para ambas propuestas: coordinar agenda y no repetir línea base ni fundamentos. Slides 2, 3 y 5 con el mismo `overrides.css` de CAI-040 (3 bloques apilados), con la escala de la ruta de Fivenca porque son 2 fases. En la ruta, títulos de hito de más de ~28 caracteres pasan a 2 líneas y descuadran la fila.

## 2026-10-06 — [cliente:marcelo-restrepo-cai040] CAI-040: monitoreo diario de mensajes directos de Instagram y TikTok con Claude (compacto, 6 slides, 12 h)
Pedido: «propuesta para Marcelo Restrepo bajo el CAI-040, asesora María» con el contexto de la asesora pegado. Eran **2 propuestas** (monitoreo de mensajes + Cerebro Digital de marca personal); el usuario pidió elaborar solo la 1.ª, con Claude en el navegador para ambas redes, **sin mencionar otras herramientas** (el contexto traía dos más, que no se nombran ni en el deck ni en el brief). La asesora pedía «sesiones, horas y entregables de cada parte» y no venía definido: el sistema propuso 6 sesiones de 2 h = 12 h (una solución por sesión, 3 bloques: criterio y aviso, Instagram, TikTok), 3 semanas, kick-off de 1 h aparte.
**Lo que cambia el diseño:** el cliente quiere **estar al tanto, no responder** (no quiere un chatbot que conteste), así que «Claude solo lee y avisa» va en alcance, fuera de alcance y notas. Es además la defensa de diseño contra instrucciones ocultas en mensajes de terceros. La viabilidad de TikTok es una incógnita de la red (bandeja en la versión web, verificaciones): se prueba en la sesión 1 y se ajusta en la 4; la ejecución diaria programada solo corre con el computador encendido y el navegador abierto, y el rescate de miles de mensajes consume uso del plan (va por lotes). Todo en `brief.md`, solo lo necesario en el deck.
**Sin salir del compacto:** 6 entregables dejaban 2/3 de la slide 2 y la 5 vacías (la plantilla está pensada para 40+). Se resolvió con `composicion` bajo cada bloque, `vocabulario.area` = «bloque» y `overrides.css` (slide 5: los 3 bloques apilados como filas anchas, nombre a la izquierda). Con 3 fases en columna, «4 h» se partía en dos líneas en la celda: `white-space: nowrap` y escala menor que con 2 fases. **El verificador no vio que la pila de la slide 5 tocaba las cajas inferiores** (mide contra otro elemento): solo la revisión visual lo detectó. Cuidado con apilar bloques por override: bajar la altura hasta que haya ≥ 20 px visibles.
**Privacidad del cliente:** el parentesco con el presidente de un banco y el episodio del mensaje que pedía una reunión son contexto interno (`brief.md`), no van en el deck. El hecho de portada «Miles de mensajes sin responder» se cita como dato declarado por el cliente y queda por confirmar con la asesora. Sin certificado (un solo participante). Asesora María Iribarren (confirmar). Código, división (Educación) y alianza (no) dados o inferidos, anotados en `supuestos`.

## 2026-10-06 — [plantilla] Slide 3 · Ruta del compacto: los protagonistas son las soluciones (procesos), no las horas
Pedido del usuario con una captura de la ruta de DUSA: «los protagonistas son los procesos y no las horas; sigue esta estructura a partir de ahora para todas las propuestas». El adjunto no coincidía con ningún deck del repositorio (ni el generador ni `dusa-cai035/` lo producían: ambos ponían las horas en grande), así que se implementó desde la imagen.
**Qué cambió:** (1) cabecera de fase = etiqueta + **«N soluciones»** a la derecha, rango de semanas y descripción (con la primera letra en mayúscula), sin horas; (2) tarjeta de frente = nombre del carril en grande + etiqueta («Frente A»), línea **«N soluciones · H h · S1-S11»** y áreas; (3) celda = **número grande + «soluciones»** y las horas pequeñas a la derecha; (4) la columna final se llama **«Garantía»** por defecto en Habilidades con garantía (con `inversion.sin_garantia` o `seguimiento.tipo` cierre/ninguno sigue «Seguimiento» o lo que diga el dato) y el subtítulo por defecto dice «seguimiento y garantía a 30, 60 y 90 días». El total de horas queda en la nota.
**Dónde:** `scripts/generar-habilidades-compacto.py` (`s3_ruta`, helper `mayus1`), `plantillas/habilidades-compacto-canonico/habilidades-compacto.css` y `scripts/verificar-habilidades-compacto.js` (comprueba que etiqueta y conteo de cada fase caben en una línea y que el nombre del frente no sobresale). Prueba de aceptación: DUSA (3 frentes) y Fundación sin errores y con todas las holguras en verde; verificado a ojo contra la captura.
**Cuidado:** las propuestas ya generadas llevan una copia congelada del CSS. Regenerar una de ellas sin `--actualizar-css` mezcla el HTML nuevo con el CSS viejo; con `--actualizar-css`, sus `overrides.css` de la ruta (escala tipográfica de `.rg-h`, `.rg-front-h`) hay que revisarlos. No se regeneró ninguna propuesta anterior. Sin actualizar todavía: `plantillas/habilidades-compacto.md` (§2 fila 3, glosario «Celda» y «Fase», §12 diferencias esperadas) y `CLAUDE.md`, pendientes de confirmación (§8).

## 2026-10-06 — [cliente:fivenca-cerebros-digitales] CAI-039: 5 Cerebros Digitales de 8 h para Fivenca (compacto, 6 slides, 40 h)
Pedido: «propuesta para Fivenca sobre cerebros digitales, son 5, 8 h cada uno, asesora María», sin ficha. Código CAI-039 (siguiente libre), Educación y sin alianza por las 5 propuestas previas de Fivenca (CAP-039, 061, 062, 105 y el express). Respuestas del usuario: un cerebro por persona, personas a designar; 4 sesiones de 2 h por persona; Claude + Projects + Skills + Obsidian, sin Claude Code. **Corrección a mitad de camino:** «la base es CAP-060, pero fíjate en otras como CAI-027» → contenido de CAP-060 (3 sesiones) con su 3.ª sesión dividida en dos para llegar a 4 sesiones, y estructura de grupo ×N de CAI-027 (tracks individuales, «Cerebro Digital 1 a 5» anónimos).
**Guardia §4.21 punto 5:** CAP-060 y CAI-027 son decks canónicos de 14 slides, así que se preguntó una vez compacto o canónico; el usuario eligió compacto. Primera propuesta de Cerebros Digitales en el formato compacto, sin tocar el generador: `vocabulario.area` = «Cerebro Digital», 5 áreas de 8 h con 2 entregables de 4 h (Project y grafo; Skill y automatización) = 10 entregables, 2 fases (semanas 1-2 y 3-4), una sesión por persona y por semana (10 h a la semana). Los hechos de portada son de contenido (5 cerebros, 8 h, grafo), no del cliente (lección de N58: sin ficha propia no se afirman hechos del cliente).
**Diseño:** la plantilla está pensada para 40+ entregables; con 10 la slide 5 quedaba con 2/3 de vacío. Se resolvió con `columnas_por_carril: [2]` y escala tipográfica mayor en `overrides.css` (slides 2, 3 y 5, base de DET-027). En la slide 2 la `composicion` va bajo el nombre del área, no pegada («Cerebro Digital 1 8 h» se leía mal).
**8 h contra la tarifa de 6 h por cerebro** (CAI-025/CAI-027): 40 h en vez de 30 h; decisión del usuario, queda en `brief.md` para ventas. Sin certificado por defecto (CAP-060 y CAI-027 sí lo tenían). Sin tocar `Obsequio de Intezia` ni el calendario con fechas de CAI-027: eran de ese caso.

## 2026-10-06 — [cliente:clinica-santiago-de-leon] DET-027: Detección en compacto para la Clínica Santiago de León, 6 slides, 22 h
Propuesta nueva con ficha (asesora Verónica Rubio). Misma lógica de DET-025/DET-026 sin tocar el generador. Con ~60 a 70 personas y máximo 25 por sesión salen **3 grupos de Fundamentals (6 h, un entregable por grupo como en G-MAX)** + 4 áreas de 4 h = 22 h, kick-off aparte. 4 semanas: Admisión y Finanzas juntas (flujo seguro-presupuesto), Atención al Paciente y Almacén después, Reporte Final en la semana 4.
**Pedido del usuario:** comentar lo que esté fuera del alcance de la IA o complicado, sin anexarlo a la propuesta. El análisis vive en `brief.md` (sección «Qué veo fuera del alcance de la IA o complicado») y en la respuesta. Lo central: el «logro inmediato» de la ficha (conectar triaje, seguro y presupuesto) es una integración de tres piezas con terceros, y mucho de lo pedido es automatización o proceso, no IA.
En el deck, solo una frase neutra de alcance («desarrollos e integraciones a medida: la etapa que sigue»), el logro como «foco» y no como promesa, el subtítulo «separando lo que necesita IA de lo que solo se automatiza» y la nota «sin datos que identifiquen a pacientes». Sin nombre ni cargo del contacto, sin su uso personal de IA, sin citas, sin HIPAA, sin el proceso 4 (Notion) ni el proyecto de investigación médica. «Caso para la Junta, con retorno e inversión» como entregable del Reporte Final: confirmar con servicio. Titular con «de Santiago de León» para no pasar de 82 caracteres.

## 2026-10-06 — [cliente:steam-solutions] CAI-038: desarrollo guiado por especificaciones con agentes de IA para el equipo de desarrollo de Steam Solutions (compacto, 6 slides, 12 h)
Propuesta nueva con ficha (asesora Verónica Rubio), código CAI-038 indicado por el usuario (libre). Habilidades en compacto sin preguntar la guardia §4.21: el contenido son soluciones concretas (método + 3 agentes), no un programa de módulos. Sin tocar el generador: misma receta que CAI-037 (`vocabulario` módulo/entregable, `composicion`, etiquetas propias y `overrides.css`).
**Instrucción del usuario:** el IDE con IA se define en el kick-off. El deck no nombra ninguna herramienta (ni las 4 que usa el equipo ni la de prototipado); el kick-off (1 h, aparte) es un hito y la licencia va aparte, con «pago y renovación estables desde Venezuela» como criterio de elección (la ficha pidió anticipar el problema de pago de una membresía).
12 h = tope del lineamiento (8 a 12 h por área, hasta 5 procesos): Fundamentals + método + 3 agentes + flujo común, 6 sesiones de 2 h en 6 semanas. Cada agente es una primera versión probada; «autónomo y robusto» se trata como horizonte del seguimiento, no se promete.
**Segunda ronda (misma fecha):** el usuario pidió quitar de «Fuera de este alcance» el punto «agentes terminados para producción» y destacar que Intezia guía la construcción para que los agentes funcionen, pero es el equipo quien los construye. Se cambió «construimos» por «guiamos» (subtítulo, pasos, lead, celda y hito de las semanas 3 a 5) y «Quién construye» pasó a «el equipo es quien lo construye». Con esto «autónomo y robusto» ya no se presenta como horizonte aparte: pesa más el seguimiento 30-60-90.
**Tercera ronda:** el usuario preguntó si 2 h por agente era muy poco. Respuesta honesta: sí, con la promesa de «funcione» (el número había salido de repartir el tope de 12 h, no de estimar el esfuerzo; CAI-032 tiene 4 h por asistente). Decisión del usuario: **4 h por agente «y quedamos con holgura»** = 18 h (2 + 2 + 3×4 + 2), una sesión de 4 h por agente en las semanas 3 a 5; excede el tope del lineamiento (12 h) por decisión suya. Lección: cuando el tope del lineamiento y la promesa del alcance chocan, estimar el esfuerzo por entregable antes de repartir el tope y decir de dónde sale cada cifra.
Datos de salud: ambiente de desarrollo con datos sintéticos (política del cliente), sin citar la norma. Sin nombres ni cargo de Juan, sin citas textuales, sin el juicio «no es riguroso». Sede y viáticos sin resolver (comercial). Una slide quedó con el aviso de «skills» glosado una sola vez (§4.12).

## 2026-10-06 — [cliente:conserval] DET-026: Detección en formato compacto para Conserval (marca Balance), 6 slides, 14 h
Propuesta nueva con ficha (asesora Verónica Rubio): Fundamentals 2 h + 4 h por cada una de las 3 áreas (Atención al cliente, Conciliación de pagos, Cuentas por pagar), kick-off aparte. Misma lógica de DET-025 (Acua-e), sin tocar el generador.
**Novedad:** la ficha dice que lo que les funciona son sesiones de 2 h, así que cada área de 4 h se parte en 2 sesiones de 2 h y el calendario sube a 4 semanas. Las 3 áreas comparten las mismas 2 o 3 personas.
**Pedido del usuario:** avisarle qué queda fuera de alcance con Gemini (el cliente no quiere salir de ahí) sin ponerlo en la propuesta. El deck no nombra Gemini ni sus límites; el análisis vive en `brief.md` (sección «Alcance con Gemini») y en la respuesta al usuario. Watiker no tiene información pública verificable: su API es la gran incógnita.
Sin datos personales ni nombres del cliente (dueño autodidacta, apego a Gemini, recursos escasos, miedo del equipo, urgencia de Instagram).

## 2026-10-06 — [cliente:n58-banco-digital-ti] CAI-037: Claude Code y Codex para el equipo de TI de N58 (compacto, 6 slides, 12 h)
Pedido: «propuesta para N58 bajo el CAI-035, asesora Flavia, uso de Claude Code y Codex como profesionales para el equipo de TI, sin más contexto». **CAI-035 ya era de DUSA** y CAI-036 de Alfonzo Rivas:
se preguntó y el usuario eligió **CAI-037**. Otras 3 respuestas: compacto (guardia §4.21 punto 5), enfoque (código, revisión y pruebas, uso seguro) y 12 h como CAI-034 (Fundamentals 2 + Construcción 6 + Implementación 4, kick-off de 1 h aparte).
Sin tocar el generador: `vocabulario` (módulo/entregable), `area.composicion`, `etiqueta_pasos`, `ruta.subtitulo`, `entregables.subtitulo` y las etiquetas del retorno (`etiqueta_pasos/metas`, `gancho`) quitan los «área» y «solución» por defecto; `overrides.css` escala las slides 2, 3 y 5 (3 módulos, un solo frente).
**Cuidado de diseño:** Claude Code y Codex envían código a servidores externos y N58 tiene la restricción de Sudeban sobre datos (documento de soberanía de CAI-034): las sesiones usan un repositorio de práctica, sin código de producción ni datos de clientes, y el deck no resuelve la arquitectura. Licencias aparte, sin precios de lista ni afirmar quién contrata.
Entregables y reparto de horas propuestos por el sistema (no había insumo del equipo de TI): confirmar con servicio. Pendiente: cantidad de personas, contacto de Tecnología, modalidad y fechas. Documentar en `plantillas/habilidades-compacto.md` las claves opcionales sigue pendiente de confirmación (§8).

## 2026-10-06 — [cliente:alfonso-rivas-ch015] CH-015: charla de 2 h de IA para líderes, sencilla y sin datos del cliente (compacto, 4 slides)
Pedido: "transforma esto en una charla de 2h de IA para líderes, no ofrezcas datos de departamentos ni cuántos son ni áreas ni nada de eso, hazla sencilla". «Esto» = CAI-036, que ya salió:
se creó una **propuesta nueva con código de Charla (CH-015, siguiente libre tras CH-014)** y CAI-036 quedó intacta. Sin tocar el generador: se combinó `sin_hoja_cotizacion`, `seguimiento.tipo: "ninguno"`
y se omitió `retorno` (una charla no mide retorno): 4 slides (portada, alcance, ruta, entregables) con solo 2 campos editables. **Qué se quitó por la consigna «sin datos del cliente»:** 800 colaboradores, edades,
sector, «departamento», «líderes de área» y cualquier cantidad; el deck solo lleva el nombre. Como `portada.hechos` exige 2-4 datos, se usaron 3 sobre el **contenido de la charla** (Qué / Cómo / Primer paso),
no sobre el cliente. Con horas enteras obligatorias, las 2 h se reparten en 2 partes de 1 h (módulos I y II de CAP-020, sin el stack). Se usó `portada.eyebrow` propio («Propuesta de charla · Servicio de Habilidades»)
en vez de «proyecto» y `vocabulario.area` = «parte». Guardia §4.21 punto 5: no se volvió a preguntar (el usuario ya había elegido el compacto para la cuenta y pidió «sencilla»); se declara en `supuestos`.
Entregables (guía rápida, preguntas clave, material en digital) son propuesta del sistema: confirmar con servicio.

## 2026-10-06 — [cliente:alfonso-rivas-cai036] CAI-036: propuesta rápida de IA para líderes (compacto, sesión de 3 h)
Pedido: "propuesta rápida de IA para líderes basada en lo que hemos realizado para Alfonzo Rivas". Antecedentes en la cuenta: CAP-020 (su Fase 2 ya era capacitación de líderes, 8 h en 4 módulos),
CAP-027 (plan masivo) y TA-036 (cortesía de 4 h, 30/09/2026). Guardia §4.21 punto 5 aplicada: se preguntó una vez (formato, duración, stack) y el usuario eligió compacto,
**sesión de 3 h** y **sin herramienta en particular**. Los 4 módulos de CAP-020 se condensaron en 3 bloques de 1 h, un entregable por bloque (criterio, mapa de oportunidades, hoja de ruta de 90 días),
con seguimiento 30-60-90 y garantía como en el estándar de Habilidades (CAI-032 hizo lo mismo). **Sin tocar el generador**: vocabulario `bloque`, `columnas_por_carril: [1]` para 3 entregables
y `overrides.css` para escalar las slides 2, 3, 5 y 6. Cosas que se evitaron a propósito: nombrar al contacto y a su coach, la dinámica interna de venta, TA-036/CAP-020/CAP-027, Empresas Polar y cualquier herramienta.
Los datos de la portada son de la ficha de mayo de 2026: reconfirmar vigencia. Cantidad de líderes, modalidad y horario no existen: se omiten.
**Segunda ronda (mismo día): «quítale los 90 días de seguimiento y la hoja de cotización».** El compacto de Educación exigía la hoja de inversión y la 5.ª columna de seguimiento, así que se agregaron
dos claves opcionales al generador: `sin_hoja_cotizacion: true` (raíz, el deck pasa a 5 slides con solo los 2 campos de la slide de entregables, igual que Fundación pero con logo de Educación) y
`seguimiento.tipo: "ninguno"` (la ruta termina en la última fase y no se exigen rango, texto ni check-ins). Sin seguimiento tampoco hay garantía 30-60-90 (vivía en la hoja de inversión). El retorno
dejó de hablar de metas a 30/60/90 y muestra qué queda definido al cerrar la sesión. El «plan de 90 días» se conservó como horizonte del entregable (no es seguimiento): se declara en `supuestos`
para que el usuario lo quite si lo entendía distinto. Regresión: DUSA, Fundación, G-MAX, CAI-032 y Acua-e salen idénticos con el generador nuevo. También se corrigió el plural «1 semana» en el brief generado.
**Pendiente de proponer (§8, archivos estructurales):** documentar `sin_hoja_cotizacion` y `seguimiento.tipo` en `plantillas/habilidades-compacto.md` §5, junto con `vocabulario`, `composicion` y `sin_garantia`.

## 2026-10-06 — [cliente:acua-e] DET-025: primera Detección NUEVA nacida en el formato compacto (6 slides)
Pedido: propuesta nueva para Acua-e (pyme farmacéutica, 12 personas, asesora Flavia Martínez) "siguiendo el formato nuevo", con la ficha adjunta. Se aplicó de entrada
el patrón de G-MAX (carril «Detección», sesiones como entregables, `vocabulario`, sin certificado, sin garantía, sin pre-recomendar herramienta, retorno en modo método).
**Dimensionamiento** por el lineamiento: Fundamentals 2 h (un solo grupo, 12 < 25) + 3 áreas × 4 h = 14 h; el kick-off va aparte y no suma horas (en G-MAX se incluyó solo por
instrucción explícita). Calendario de 3 semanas **propuesto por el sistema** (la ficha no dicta fechas): confirmar con servicio y con Flavia.
**Qué se dejó fuera del deck a propósito** (está en `brief.md`): edad, sucesión y valoración de la fundadora, su uso personal de un GPT, el sobrino candidato a líder de IA y las
citas textuales; el agente de marketing aparece solo como horizonte (Bloque F de la ficha pide Detección como primer paso).
**Generador:** el `brief.md` que crea por primera vez ya respeta `meta_servicio` (antes decía «Servicio de Habilidades» y «Capacitación In-Company» aun en una Detección).
Cambio opcional: DUSA, Fundación, G-MAX y CAI-032 salen idénticos (comparación archivo por archivo con la ruta de logos normalizada).
**Escala con pocas entregas** (4): `overrides.css` del deck amplía las slides 2, 3 y 5 (con una sola fila en la ruta y 4 entregables la plantilla quedaba medio vacía);
`columnas_por_carril: [2]` llena mejor el catálogo que 4 columnas con un entregable cada una; se usa espacio duro (`\\u00a0`) para que «12 h» no se parta en `inversion.duracion`.

## 2026-10-06 — [cliente:g-max] DET-024: primera propuesta de Detección en el formato compacto (13 → 6 slides)
Pedido: "mejorar la DET-024 con el formato nuevo aunque el definido es de Habilidades, adaptándolo con las reglas fijas de la propuesta".
**El código DET-024 está repetido** (`g-max/` del 2026-10-01 y `fibraspol/` del 2026-09-29, sin relación): se preguntó y el usuario eligió G-MAX.
Lo aprendido de CAI-032 se aplicó de entrada (sin esperar otra corrección): auditar el deck a fondo, compactar a qué/cómo/qué entrega/cuándo,
semanas en vez de fechas, sin Impacto con estudio, retorno en modo método. **Qué no cabía de Habilidades en Detección** y cómo se resolvió:
sesiones y frentes son «entregables» y «frentes» (no «soluciones» y «áreas»; clave opcional `vocabulario`), no hay seguimiento 30-60-90 (la 5.ª
columna de la ruta pasa a «Cierre»: Priorizar · Reportar · Proyectar; `seguimiento.tipo = "cierre"`), no hay garantía (`inversion.sin_garantia`),
y la composición de los 22 departamentos y de los 2 grupos de Fundamentals, que el usuario había pedido ver en el deck, va bajo cada frente
(`area.composicion`). Mapeo: kick-off = F0; Fundamentals y los 4 frentes = entregables por sesión (7, 25 h); Mapa de Calor, Índice de Madurez y
Reporte Final = entregables transversales (trabajo del consultor, sin horas de sesión). Hallazgo: el brief decía «3 semanas», pero en semanas
relativas son 4 (la sesión Asistencial cae el lunes de la semana 4). Generador comprobado idéntico para DUSA, Fundación y CAI-032. **Pendiente de
proponer** (archivos estructurales, §8): documentar en `plantillas/habilidades-compacto.md` §1 y `CLAUDE.md` §4.1a que Detección (y combos)
usan el compacto con estas claves. Fibraspol (el otro DET-024) sigue con el formato anterior.

## 2026-10-05 — [cliente:laboratorios-farma-gestion-humana] CAI-032: combo Detección+Habilidades ya enviado, reexpresado en el formato compacto (15 → 6 slides)
Pedido "ajusta la CAI-032 al formato nuevo". **Tres rondas, en orden**: (1) la plantilla compacta no cubre combos con Detección ni programas de
sesiones (§1 de la spec, guardia §4.21 punto 5): se preguntó y el usuario eligió mantener el deck canónico. (2) Error mío: tras esa elección
respondí "ya cumple" porque el verificador estaba en verde; el usuario lo rechazó ("era de antes, no puede estar perfecta") y apliqué las
reglas de fondo al deck de 15 (titular-objetivo, eyebrow «Propuesta de proyecto», línea base, sin certificado, sin nombres, sin cita no
verbatim). (3) El usuario dio el criterio de producto: **una propuesta responde qué, cómo, qué me entrega y cuándo; 15 slides es demasiado**;
pidió compactar con el formato nuevo "sin omitir lo importante" y aplicar lo que yo había dejado sin aplicar (slide de retorno, sin Impacto con
estudio, semanas en vez de fechas), con Detección 4 h, módulo conjunto 3 h y prácticas 4 h. Resultado: compacto de 6 slides (portada · alcance ·
ruta · inversión · entregables · retorno). **Cómo se mapeó un combo al esquema**: Detección y módulo conjunto como `proceso_base` (condicionan lo
demás), Nómina y Selección como las dos áreas; 1 carril (Copilot), 1 frente, 3 fases = 3 semanas; el mapa de licencias y la línea base como
entregables. **Cambio al generador** (opcional, sin efecto si no se usa): `servicio_rotulo`, `meta_servicio`, `meta_tipo`; comprobado idéntico
para DUSA y Fundación. Con solo 4 soluciones las slides 2 y 5 quedaban medio vacías: se escalaron con `overrides.css` del deck. **Pendiente de
proponer** (archivos estructurales, §8): actualizar `plantillas/habilidades-compacto.md` §1 y `CLAUDE.md` §4.1a para que un combo Detección+
Habilidades use el compacto con `servicio_rotulo`. **Hallazgo de sistema**: el campo `Acreditacion` de Beneficios v3 ya no es una acreditación
(es «Valor inmediato»), pero `good-latam`, `grupo-nena-cai033` y `unimet` aún traen las 3 líneas institucionales viejas (modelo ABR expuesto,
§4.10a); no se tocaron. Interpretación a confirmar: «4h para prácticas» = 4 h cada una (15 h en total). Detalle y mapa slide a slide: `brief.md`.
El deck de 15 slides y su PDF quedan en `_anterior-15-slides/` y `_pdf-anteriores/`.

## 2026-10-05 — [arquitectura] Habilidades pasa a plantilla compacta por defecto (`CLAUDE.md` §4.21)
Decisión del usuario: de ahora en adelante IDIA hace **todas** las propuestas del servicio de Habilidades con el esquema compacto de DUSA CAI-035 (5 slides, 4 en
Fundación, + retorno opcional, dirigido por `datos.json`). Cambios: nueva §4.21 en el router (reglas propias: titular-objetivo, eyebrow «Propuesta de proyecto ·
Servicio de Habilidades», retorno sin estudios ni web, cifras y posiciones solo con datos y aval del cliente, 7 campos de PDF, guardia para charla/curso/diplomado/programa
de módulos: preguntar antes de forzar); ajustes en §1, §4.1a (punto 4 y tabla servicio→patrón), §4.2, §4.9, §4.14, §5, §6 (Paso 0 y pasos), §6.A, §7 y §10;
`empresa/tipos-de-documento.md` (fila y nota de Habilidades), `plantillas/propuesta-comercial.md` (aviso y ejemplo de eyebrow), spec `habilidades-compacto.md` (§1 por defecto
y guardia, origen/aval/defaults por división, certificado fuera por defecto, validaciones nuevas). Los decks de Habilidades ya entregados no se tocan. `dusa-cai035` se
regeneró (PDF con la slide 6 sincronizada, par PDF-customize aplicado, verificador sin hallazgos); el PDF previo quedó en `_pdf-anteriores/`. Pendientes de datos del
cliente (no bloquean): costo hora, escalas, dotación, volúmenes, moneda de los parafiscales, informe de Detección en docx.

## 2026-10-05 — [plantilla] Habilidades compacto v1.3: titular-objetivo y slide de retorno sin citas (modelo: DUSA CAI-035)
Nueva plantilla genérica `plantillas/habilidades-compacto.md` (+ `habilidades-compacto-canonico/`, `scripts/generar-habilidades-compacto.py`,
`verificar-habilidades-compacto.js`, `customize-habilidades-compacto.py`, `pdf-habilidades-compacto.sh`, `habilidades-importar-insumo.py`,
`habilidades-retorno-xlsx.py`). Dirigida por datos (`datos.json` → deck + campos del PDF + `programa.md`); las cifras se calculan. La v1.3 toma como
modelo las dos últimas correcciones de dirección sobre DUSA: (1) el nombre del proyecto es una **frase-objetivo estilo título de tesis** (campo
`portada.titulo_lineas` + franja; el h1 baja de tamaño solo; aviso si el nombre del PDF `<CÓDIGO> <titular>` pasa de 90 caracteres) y el eyebrow dice
«Propuesta de proyecto»; (2) módulo opcional `retorno` (slide final, sin campos de PDF): modo `metodo` (cómo se calcula, metas 30-60-90, destino del
tiempo) o modo `cifras` (tabla por área con tipo de dato rotulado), **sin estudios ni referencias de la web** (el generador lo bloquea). Circuito de datos:
`habilidades-retorno-xlsx.py crear` → hoja azul/gris → `leer` → `datos.json`; se niega a inventar (una solución sin los tres datos no cuenta; cobertura
parcial se rotula «(n de m procesos)». Pruebas: 282 casos negativos + 55 del módulo + 45 de la hoja, sin errores internos; ejemplos `datos.ejemplo-dusa.json` (6 slides)
y `datos.ejemplo-fundacion.json` (5 slides). Endurecida tras revisión independiente (origen de datos, aval de posiciones, horas por posición, tipos de dato,
defaults de Fundación sin dinero, ids internos y línea base duplicada avisados). **Integrada al router el mismo día**: ver la primera entrada de arriba.

## 2026-10-05 — [regla] Portada: nombre del proyecto como frase-objetivo (estilo título de tesis) y slide de retorno sin citas externas (caso DUSA CAI-035)
Dos correcciones de dirección. (1) El nombre de la propuesta es una frase que responde al objetivo del servicio, estilo
título de tesis («Optimización de procesos y datos con inteligencia artificial en 10 áreas de DUSA»), no un titular de
dolor. Límite práctico: `generar-pdf.sh` arma el nombre del PDF con «<CÓDIGO> <h1>» y lo corta a 90 caracteres, así
que el título debe tener ≤ 82 caracteres (con código de 7) o el archivo queda cortado a media palabra; el h1 baja a
46 px en `overrides.css`. (2) La slide de retorno no cita estudios ni nada de la web: presenta el método de cálculo por
área y proceso, las metas 30-60-90 y el destino del tiempo recuperado, y recibirá cifras propias cuando se completen
los datos (`retorno-captura.xlsx`). La literatura verificada queda solo como respaldo oral en `programa.md` §6.
(Resuelto en la plantilla v1.3: `portada.titulo_lineas` de 1 a 3 líneas más franja, con tamaño de h1 según el largo.)

## 2026-10-05 — [regla] «Propuesta de proyecto» en vez de «Propuesta formativa» cuando el servicio ordena procesos y construye (caso DUSA CAI-035)
Revisión de dirección: la portada decía «Propuesta formativa», pero el proyecto ordena procesos y datos, construye
soluciones y mide su efecto; presentarlo como capacitación lo reduce. Cambio: eyebrow «Propuesta de proyecto · Servicio
de Habilidades» (sigue nombrando el servicio, §4.1a punto 4) y lead con verbos de proyecto. Ya aplicado en `dusa-cai035`
y en el default de la plantilla compacta; reflejado el mismo día en el ejemplo de §4.1a punto 4 de `CLAUDE.md` y en
`plantillas/propuesta-comercial.md → Reglas de copy`. Misma revisión: la cuenta de
dotación y nómina se plantea de frente a los dueños cuando el cliente lo avala, **con datos** (no se estima sin marcarlo):
ver la entrada siguiente y `clientes/propuestas/dusa-cai035/retorno-captura.xlsx`.

## 2026-10-05 — [regla] Propuestas a directivos llevan lámina final de retorno estimado (caso DUSA CAI-035)
Criterio comercial (David, vía el usuario): la directiva decide con dinero y tiempo, así que la propuesta
necesita el **retorno de inversión real o aproximado** (ahorro de tiempo, reenfoque del trabajo, crecer sin
sumar gente a la nómina, nunca "sacar gente") y una proyección de la organización, incluida la extensión a
otras áreas y líneas de negocio. Se agregó la slide 6 `.s-roi` a `dusa-cai035` (6 páginas). **Cómo se hace
sin inventar (§4.9)**: sin horas por proceso/tarifa/nómina del cliente no hay cifra propia; se usan 3 estudios
verificados con fuente primaria, cada barra con su base (producción por hora ≠ tiempo liberado ≠ autorreporte),
rotulados como estudios ajenos, y la medición real queda atada a la línea base de la semana 1 + seguimiento
30-60-90. La verificación corrigió datos de memoria (Brynjolfsson publicado = 15%, no 14%/34%; Bick 5,4% =
2,2 h/semana, no 1,1). Detalle y estudios descartados: `clientes/propuestas/dusa-cai035/{brief,programa}.md`.
Pendiente de decidir: llevarla como slide opcional al canon de Habilidades. **Actualización mismo día**: la dirección pidió además plantear de frente la reducción de puestos y de nómina (con el aval del cliente) y mostrar el retorno con datos duros por área y proceso; las fichas disponibles dicen «No declarado» en volumen y horas, así que la slide 6 con estudios ajenos queda provisional hasta tener esos datos.

## 2026-10-01 — [cliente:hjb-quimica] CAI-031 — reconstrucción total: de Habilidades pura a combo Detección+Habilidades
Tras mesa de trabajo real con Vianey Reyes, la propuesta cambió de estructura completa:
de "2 poblaciones de Habilidades" (gerencial + especializada) a Detección de 15 áreas +
Habilidades directiva con efecto cascada (modelo Venemergencia) y cierre con Cerebro
Digital. **Servicio reclasificado** de `habilidades` a `deteccion` (regla del combo, §4.1a
+ precedente `banco-activo-deteccion-negocios/` DET-021) — el código se mantuvo CAI-031
(código y servicio son decisiones independientes). Clonado estructuralmente de DET-021 (que
ya resolvía el patrón "Detección multi-área + Habilidades cotizada": roadmap `.rmx-linear`,
`.s-vision` reusada 2 veces, `.s-followup` reusado 2 veces, "Inversión por fases" con
`FASE_PRICE_FIELDS`). Agregado nuevo a la familia de componentes: `.s-org` (organigrama
recreado en estilo de marca, no el screenshot crudo del cliente), `.s-deliverables`
(entregables en tarjetas, familia visual `.rmx-card`) y `.hours-table` (tiempos detallados
por etapa en tabla simple) — los 3 reutilizables para el próximo combo similar.

**2 bugs/límites confirmados (ya documentados, se repiten):**
1. `<strong>` dentro de un `<li>` con `display:flex` (aquí `.s-pain ol li`) rompe el layout
   — mismo bug de `bug-strong-flex-specifics.md`, ahora confirmado también en `.s-pain`, no
   solo en `.s-goals .specifics`/`.s-schedule .ses-block`. Quitar `<strong>` de esos `<li>`
   siempre, sin excepción.
2. **Límite real de ancho del label `.rmx-facets li > span`**: el componente reserva 58px
   fijos. Labels de ~9 caracteres o menos ("Medimos", "Aportamos", "Resultado", "Detección")
   caben; labels más largos ("Metodología", "Levantamiento", "Compromiso", "Habilidades")
   desbordan el ancho y se montan sobre el párrafo adyacente — **el detector automático no
   lo ve** (no es overflow de página, es colisión interna). Revisar siempre a ojo cualquier
   `.rmx-facets` con labels nuevos, acortar a ≤9 caracteres.

Pendientes explícitos de usuario (no bloquean el resto del deck, se actualizan al llegar):
CV del consultor (slide "Por qué Intezia" se quedó institucional, sin nombre propio) y el
archivo del informe de DUSA como modelo visual (la slide de "Métricas de otros clientes"
usa a DUSA solo cualitativamente, sin cifras — no tiene Edu-Trace de cierre).

## 2026-10-01 — [cliente:grupo-nena] CAI-033 — clon dejado a medio editar entre sesiones
Grupo Nena, combo 2ª cohorte Habilidades (4 sesiones/11h) + Innovación (ciclo mensual, 3
meses), asesora Verónica Rubio. **Hallazgo de proceso**: al retomar la tarea en una sesión
nueva, la carpeta `grupo-nena-cai033/` ya existía con `brief.md`/`programa.md`/`meta.json`
completos (decisiones de dimensionamiento, diagnóstico, servicio, todo bien razonado), pero
`index.html`, `overrides.css` y `acroforms.json` eran aún el clon sin editar de `fastmed/`
(CAI-030) — contenido íntegro de otro cliente (agente de WhatsApp, Anabella, doble
autenticación), con un único cambio: el eyebrow de portada. Si una sesión se corta a mitad
del flujo de clonado, el riesgo no es "no avanzar" sino dejar documentos de planificación
(brief/programa) completos junto a un deck visual que sigue siendo el origen sin tocar —
hay que verificar el `index.html` real (no solo que el archivo exista) antes de dar un clon
por editado. Reescrito el deck completo con el contenido ya decidido en brief.md/programa.md,
creado `scripts/customize-grupo-nena-cai033.py` (clon de `customize-fastmed.py`). Bugs de
overflow encontrados: 2 por copy largo (portada, diagnóstico — acortado) y 1 estructural
(`.s-benefits-v2 .grid` fijo en 570px, heredado de fastmed/, excede el alto de slide por 8px
independiente del contenido — bajado a 557px en el `overrides.css` local). Recurrencia del
glitch de `<strong>` en `.impact-hook .hook-text` (mismo bug que `.s-goals .general p`, §4.8)
y defecto nuevo: el punto final fuera de `<span class="hl">` queda separado visualmente por
el padding del resaltado — mover el punto dentro del span, no solo en end-message (ver
`bug-punto-final-fuera-de-span-flota`, hasta ahora documentado solo para ese caso).

## 2026-09-30 — [cliente:unimet] TA-035 Unimet — primer Taller universitario sin hoja de cotización
Taller de 4h (sesión única, 2 bloques de 2h) para estudiantes de la Universidad Metropolitana,
en alianza con su Gerencia de Atención Socioeconómica Estudiantil. Eje: ecosistema Gemini
(Gmail/Docs/Slides/Drive/Gems) + Perplexity y Elicit para investigación académica + módulo de
ética y uso responsable (pedido explícito del usuario: revisión, iteración, análisis crítico,
verificación humana siempre). Clonado de `simple-tv-cai002/` (no del canónico `cumbre-andina/`)
para heredar directo el formato vigente — Beneficios v3 ampliado, Cierre escalera, eyebrow con
servicio — sin tener que retrofitear ABR/Equipo facilitador manualmente. **Slide `.s-price`
eliminada por completo** (instrucción directa del usuario, no solo precio vacío): confirma que
`agregar-campo-precio.py` omite con gracia los 3 grupos de marcador cuando no existen en el
HTML (mismo patrón que `urbe/` CU-012), sin tocar el script. Impacto con datos reales de
Digital Education Council (*Global AI Student Survey 2024* + *AI in Higher Education Global
Survey 2026*). Bug encontrado: `<strong>` en 2 puntos de `.s-pain ol li` (Gemini / Perplexity +
Elicit) rompió el layout — recurrencia número 8+ del bug ya documentado en
`bug-strong-flex-specifics` (memoria persistente), corregido quitando las negritas.

## 2026-09-30 — [bug] "Inversión por fases" sobre `_base/styles.css` compartido: campo AcroForm no coincide con el CSS
FastMed CAI-030 (retomada tras envío del 27/09, se le agregó Fase 2 · Innovación) es el
primer deck que usa el marcador "Inversión por fases" (2 filas) con `_base/styles.css`
compartido + `overrides.css` propio — los otros dos decks con esta variante
(`corporaciones-easyaccess/`, `simple-tv-det002/`) tienen un `styles.css` completo propio.
El supuesto "las filas de fase terminan muy por encima del bloque de Notas, no hace falta
mover nada más" es falso: `scripts/agregar-campo-precio.py` (`FASE_PRICE_FIELDS`) fija el
`/Rect` real de los campos (Notas, PrecioBase, Descuento, PrecioTotal) en coordenadas
absolutas **independientes del CSS del HTML** — calibradas para que el deck reposicione
manualmente `.block-notes-container`/`.notas-box`/`.cot-label-*`/`.*-frame`/`.cot-roi-box`/
`.cot-garantia-badge`/`.cot-terms-box`. Sin ese override, el campo Notas cae encima de donde
`.cot-roi-box` (heredado de `_base/styles.css`, pensado para el patrón sin fases) dibuja su
texto — el ROI sale tachado por el borde del campo, invisible para `verificar-overflow.js`
(no es overflow, es solapamiento entre elementos con posición absoluta). Fix: adoptar las
mismas coordenadas de `corporaciones-easyaccess/styles.css` (único otro deck de 2 fases) vía
overrides en el `overrides.css` del deck. Al usar "Inversión por fases" sobre `_base/`
compartido, revisar visualmente esa slide específica SIEMPRE, no solo correr el detector.
Ver `clientes/propuestas/fastmed/overrides.css` (comentario "CORRECCIÓN 2026-09-30") para
las coordenadas exactas a reutilizar.

---

## 2026-09-28 — [plantilla] Brief de Kickoff: numeración de sesiones corrida ("Sesión 1, 2, 3...") como estándar
El usuario pidió que todas las sesiones de todos los briefs de kickoff se numeren de forma
corrida ("sesión 1 2 3 y así"), sin reiniciar el contador por etapa. Ya existía este patrón
como excepción puntual (`puro-lomo-bajo-mercadeo/kickoff.html`, CAP-101, al rehacer un brief
en marcha) — ahora se generaliza como estándar desde el primer brief, no solo al rehacer.
Cambio: `.sc-no` pasa de etiqueta pequeña ("Sesión 1 · 2h") a número grande (30px, dorado) sin
`<h4>` de título temático dentro de `.scard` (el tema va como primera frase en negrita de
`.sc-desc`, o se omite). Excepción: los check-ins de Seguimiento 30-60-90 mantienen `.sc-no`
= "Check-in" (no son sesiones de trabajo secuencial); `filaSesiones()` en JS distingue ambos
casos por regex. Actualizado en `plantillas/kickoff-canonico/kickoff.html`,
`plantillas/brief-kickoff.md` §3/§8, y en `clientes/propuestas/fasto/kickoff.html` (CAP-104,
recién creado) y `aerocentro-clon-salomon/kickoff.html` (sin fechas llenas todavía, seguro de
retocar). `puro-lomo-bajo-mercadeo/kickoff.html` ya seguía el patrón, no se tocó.

---

## 2026-09-25 — [plantilla] Nuevo tipo de documento: Reporte de post-servicio (one-pager, "mapa de activos")
El usuario pidió replicar para Zoom un reporte que Grupo Nena ya recibió (CAP-016, "Lo que
quedó instalado"): un one-pager ejecutivo con franja de KPIs, mapa de activos (Gems/asistentes
construidos por área con estado de adopción), casos destacados y "lo que viene". No existía
plantilla ni archivo fuente de ese reporte en el repo (solo el PDF de ejemplo) — es un tipo de
documento nuevo, no documentado hasta ahora en `CLAUDE.md` ni en `plantillas/`.

1. **Diferencia clave con Grupo Nena**: el original declara que los activos y su estado fueron
   **presentados por el cliente en una sesión de revisión real** (frase textual en el footer).
   Para Zoom no hubo tal sesión — el usuario confirmó explícitamente usar como fuente los 6
   Dashboards de Impacto Edu-Trace ya entregados (Legal, Sistemas, Miami, Mercadeo, Ventas,
   Operaciones). **Nunca simular una sesión con el cliente que no ocurrió** (mismo principio de
   honestidad que §4.9/§4.17): el copy y el footer dicen "según Dashboard de Impacto de cierre",
   nunca "declarado en sesión". Nombres de Gems salen de `programa.md` de cada propuesta
   (planificado, no confirmado operativo); el **estado de adopción** (En uso / Adopción inicial
   / En consolidación) se infiere honestamente del % de participantes que reportan horas
   ahorradas "aún no medible" en el Bloque E de cada `resultados.json` — no se inventan cifras
   operativas (consultas/día, etc.) que no están en la fuente.
2. **Sin testimonios inventados**: el original citaba a una persona entre comillas. Sin una cita
   real y completa en los datos disponibles, esa sección se reemplaza por datos agregados reales
   sin atribución individual, con fuente explícita (`ÁREA X · CÓDIGO` vs. `RECOMENDACIÓN
   INTEZIA` cuando el punto lo aporta Intezia, no el cliente).
3. **Formato**: no es un deck de `.slide` A4 landscape (patrón de propuestas/dashboards). Es un
   documento de una sola pieza continua, fluye a varias páginas A4 verticales al imprimir sin
   forzarlo a 1 página — evitar `break-inside:auto` en tarjetas/secciones para no cortar
   contenido a la mitad entre páginas.
4. **Gotcha de generación de PDF**: el `@media (max-width: 860px)` de responsive-para-pantalla-
   angosta se activaba también al imprimir si el `--window-size` de Chrome headless usado para
   generar el PDF era angosto (794px, el ancho "natural" de A4), colapsando el grid de 3
   columnas a 1 y disparando páginas de sobra con mucho blanco. Fix: `@media screen and
   (max-width: 860px)` (nunca en print) + generar con `--window-size` ancho (≥1100px).
5. Vive en `clientes/dashboards/zoom-post-servicio/` (no en `clientes/propuestas/`, porque
   consolida 6 propuestas/áreas distintas y deriva de dashboards ya entregados, no es un deck de
   venta). Sin plantilla formal todavía en `plantillas/` — construir la próxima vez que se pida
   este tipo de reporte para otro cliente, si el patrón se repite (regla de adaptabilidad §9).

## 2026-09-24 — [cliente:grupo-corpos] DET-009 reescrita: "Detección con logros inmediatos", Matriz de Impacto vs. Esfuerzo, 24h (antes 6h)
Reescritura mayor de DET-009 (Grupo Corpos), a partir de una instrucción extensa del usuario
respondiendo dudas del cliente por correo. Cambios de fondo:

1. **Nuevo planteamiento**: "la Detección no es solo averiguar, es diagnosticar y construir al
   mismo tiempo" — Grupo Corpos no parte de cero (viene de una Fase 1 real, `CAP-045`, que NO
   se nombra en el deck, mismo criterio de independencia ya vigente, pero el concepto de "ya
   construyeron algo" sí se refleja).
2. **Horas: 6h → 24h**. 5 áreas del holding **ahora sí nombradas explícitamente**
   (Vicepresidencia, Automotriz, DENSA, Dirección Industrial, Servicios Corporativos) × 4h
   (20h) + 4h de reserva con líderes/tomadores de decisión = 24h. Esto **reversa** una
   instrucción anterior del mismo cliente (2026-09-07: "no nombrar las áreas") — instrucciones
   de un mismo cliente pueden cambiar de una conversación a otra; la más reciente manda,
   documentado explícitamente en brief.md para no confundir con la versión vieja.
3. **Nueva slide "Matriz de Impacto vs. Esfuerzo"** (`.s-matrix`, pedida explícitamente por el
   cliente) — 4 cuadrantes con respuesta distinta cada uno: alto impacto/bajo esfuerzo = quick
   win que Intezia construye en la propia Detección; bajo impacto/bajo esfuerzo = lo construye
   el propio equipo; alto impacto/alto esfuerzo = se mapea para Habilidades futuro (cotizado
   aparte); bajo impacto/alto esfuerzo = a decisión del cliente. CSS nuevo reutilizando el
   banner negro de `.s-program` (no `.modules`, que trae reglas de compactación por cantidad
   de módulos no aplicables a un grid 2x2 fijo).
4. **Nueva slide "La ruta completa"** (`.s-vision`) — mismo patrón conceptual que
   [[patron-vision-de-ruta-en-deteccion]] (`la-tienda-del-blumer/`), pero esta vez **completa-
   mente autocontenida** (fondo oscuro propio) en vez de heredar `.s-roadmap`, porque este
   deck nunca tuvo ese componente — prueba de que el patrón "visión de ruta" no depende de
   tener ya un roadmap: se puede montar como slide aislada en cualquier deck. Muestra
   Detección (ahora) → Habilidades (después, Cerebros Digitales de alto esfuerzo) → **Políticas
   de IA** (complemento, no secuencial: manual de uso + matriz de riesgo de fuga de
   información) — primer caso de 3 pasos donde el 3ro es "complemento" en paralelo, no un paso
   siguiente en la secuencia.
5. **Argumentario de venta NO trasladado literal al deck**: el usuario respondió varias
   preguntas específicas por correo (costo-beneficio, si acortar expectativas, cuánto costará
   la próxima fase). La sustancia se destiló en Beneficios/ROI ("evitar construir Cerebros
   Digitales de más — no necesariamente 17 para 17 líderes, sino 1 general o 1-3 por área");
   el formato pregunta-respuesta se quedó en `brief.md` como contexto interno. **Regla**: un
   PDF de propuesta no debe leerse como un documento de objeciones respondidas — la sustancia sí
   entra al deck, el formato FAQ no.
6. **Hoja de cotización actualizada al estándar vigente** (descuento urgente + ROI, sin
   garantía por ser Detección pura) — el deck original (2026-09-07) predataba ese estándar.

**Bug de overflow atrapado**: 6 módulos en `.s-program .modules` (5 áreas + reserva) con una
frase `.obj` repetida de 58 caracteres desbordó +20px — el modo compacto de 5-6 módulos solo
fija `min-height`, no reduce padding/fuente como sí hace el modo de 7+ módulos. Fix: acortar
`.obj` a ~37 caracteres. Confirma [[bug-program-modules-5-6-no-compact]] con un caso nuevo:
"solo min-height baja" sigue vigente, incluso con contenido idéntico repetido N veces.

PDF verificado end-to-end: `verificar-propuesta.sh` OK, 13 slides revisadas visualmente sin
overflow, `/AP` confirmado por pypdf en Programa/Notas. Deck pasa de 10 a 13 slides.

## 2026-09-24 — [regla][redacción] Títulos de portada: describir mecánica no es propuesta de valor; y nunca inventar una cita atribuida al cliente
El usuario corrigió los títulos de portada de las 3 propuestas de Banco Plaza (CAI-024,
CAI-025, CAI-026): "5 Cerebros Digitales, para quienes usted designe" y equivalentes "no son
atractivos a simple vista y no causan el impacto que queremos lograr" — son descripciones de
**mecánica** (quién decide, para quién es, cómo se llama el producto), no una **propuesta de
valor**. Se reescribieron los 3 para cerrar con el beneficio/transformación central en vez de
un dato administrativo:
- CAI-024: "El contenido del mes, y la skill para repetirlo." → "Contenido que atrae, solo y
  sin sumar más personas."
- CAI-025: "5 Cerebros Digitales, para quienes usted designe." → "5 Cerebros Digitales, y el
  fin de empezar de cero."
- CAI-026: "Copilot, a la medida del día a día de Producto." → "De usar Copilot, a que
  Copilot te entienda."

**Patrón de redacción reutilizable**: un buen título de portada no describe QUIÉN decide, A
QUIÉN es para, o CÓMO se llama el mecanismo — cierra con LA TRANSFORMACIÓN o el BENEFICIO que
el mecanismo ya produce en otra parte del deck (ej. "el fin de empezar de cero" reusa
literalmente el diagnóstico "cada conversación empieza de cero" ya escrito en la propia
slide 2). El patrón "De [estado actual], a [estado deseado]." (ya usado con éxito en AMV
"Del criterio manual a la decisión con datos.") es un molde seguro y reutilizable.

**Bug de layout atrapado al aplicar esto**: el primer intento de CAI-024 ("Contenido que
atrae solo,<br>...") generó un h1 de 4 líneas porque la primera línea (25 caracteres) no
cabía completa en el ancho de portada a ese tamaño de fuente y se partió sola, dejando "solo,"
huérfano en su propia línea antes de llegar al `<br>` explícito — mismo tipo de "línea
huérfana" que el bug del punto fuera de span, pero por longitud de línea, no puntuación. Fix:
acortar la primera línea (sin resaltar) a ~20 caracteres o menos, dejando que la segunda línea
(resaltada) absorba el resto y envuelva libremente — el envolvido DENTRO del `<span
class="hl">` se ve bien a 2 líneas, el problema es solo cuando la línea SIN resaltar se ve
forzada a partirse.

**Segunda corrección, más pequeña, en el mismo lote**: la cita de la slide 2 de CAI-024
("Necesitamos más contenido, no más personas.") **no era algo que el cliente dijo** — el
usuario lo marcó como riesgo real (atribuir palabras textuales inventadas). Se reescribió
como síntesis del enfoque estratégico ("ahorro de tiempo, el departamento atrae solo"), sin
usarla como cita literal atribuida. **Regla**: el h2 entre comillas de `.s-pain` debe ser o
(a) una cita textual real de la ficha/reunión, o (b) una síntesis que no se presenta como
palabras literales del cliente — nunca una frase inventada que suene a cita directa.

## 2026-09-24 — [cliente:amv-tecnologia-cerebro-digital][regla] CAI-023, 3ra corrección: el deck ENTERO debía pivotar al patrón "asistente personal" de Banco Plaza, no solo 1 slide
Tras 2 correcciones que solo tocaban la slide explicativa, el usuario aclaró la instrucción
de fondo: *"no menciones los departamentos ni menciones personas deja claro que hace un
cerebro digital que son 6h por persona y ya esta."* Esto no pedía ajustar una slide — pedía
**reescribir el deck completo**: el patrón "sistema por funciones" original (Compras
Inteligentes + Memoria de Servicio Técnico, 24h, roadmap de 4 etapas, nombres Juan/Yamil) se
reemplazó por el patrón **"asistente personal" genérico** de
`banco-plaza-cerebros-digitales/` (CAI-025) — 2 Cerebros Digitales (interpretación: mismo
número de necesidades ya identificadas, sin nombrarlas) × 6h cada uno = 12h de propuesta
(antes 24h), clonando casi literalmente Programa, slide "Su segundo cerebro" (`.s-graph`,
ahora SÍ correctamente genérica desde el HTML), 3 sesiones, Beneficios e Impacto de CAI-025.

**Lección central, más contundente que en las 2 correcciones previas**: cuando 2 correcciones
sucesivas sobre el mismo elemento no resuelven la queja del usuario, el problema casi seguro
NO es ese elemento — es el ENCUADRE de toda la tarea. Las 2 primeras correcciones asumieron
que "hazlo como Banco Plaza" se limitaba a una slide explicativa; la 3ra dejó claro que se
refería a la ESTRUCTURA COMERCIAL COMPLETA (patrón de servicio, unidad de cobro, alcance). Ante
la 2da corrección sobre el mismo punto, vale la pena preguntar explícitamente qué tan amplio
es el cambio pedido, en vez de asumir que el alcance de la 1ra corrección seguía siendo
válido. Número de personas (2) quedó como interpretación no confirmada — documentado en
brief.md para que el usuario lo corrija si no es el correcto. Verificado end-to-end:
`verificar-propuesta.sh` OK, 14 slides revisadas visualmente, `/AP` confirmado en
Programa/Notas.

## 2026-09-24 — [cliente:amv-tecnologia-cerebro-digital][regla] CAI-023, 2da corrección el mismo día: la explicación del mecanismo debe ser GENÉRICA, no por función
Tras la primera corrección (slide "Así funciona el cerebro digital" con 2 tarjetas, una por
función), el usuario corrigió de nuevo: *"no, en este caso tiene que ser generico porque lo
que quieren saber es que hace el cerebro no apliques temas al cerebro hazlo como la propuesta
de banco plaza."* La slide se rehizo de cero: en vez de 2 tarjetas atadas a Compras
Inteligentes/Servicio Técnico, ahora es **una sola explicación genérica** (texto + 3 bullets +
un flujo visual de 3 pasos: Datos reales → Cerebro digital → Respuesta con contexto) que no
menciona ninguna función — el mismo nivel de generalidad que "Su segundo cerebro" de
`banco-plaza-cerebros-digitales/`, pero sin su mecanismo específico (grafo de Obsidian, que no
aplica al patrón "sistema conectado" de AMV). **Lección**: cuando el usuario pide "que sea
como X", verificar si pide el NIVEL DE GENERALIDAD/CLARIDAD de X (lo más probable, como aquí)
o el mecanismo literal de X — la primera corrección asumió que "explicar mejor" significaba
"por función", cuando el usuario quería una sola explicación aplicable a cualquier función.

**Bug atrapado en el camino** (reconfirma [[bug-punto-final-fuera-de-span-flota]]): el h2 de
la nueva slide tenía el punto final fuera del `<span class="hl">` resaltado
(`...digital</span>.`) — al envolver a 2 líneas, el punto quedó huérfano en su propia línea,
visible como un punto suelto flotando entre el título y el párrafo. Fix: mover el punto
DENTRO del span (`...digital.</span>`). Mismo bug ya corregido esta semana en la portada de
CAI-025 (Banco Plaza) — confirma que es un patrón recurrente a revisar en CADA `<span
class="hl">` nuevo que envuelva a 2+ líneas, no solo en portadas.

## 2026-09-24 — [cliente:amv-tecnologia-cerebro-digital][regla] CAI-023 corregida: falta explicar el MECANISMO del Cerebro Digital, no solo el resultado
El usuario pidió corregir CAI-023 (AMV, Cerebro Digital "sistema por funciones": Compras
Inteligentes + Memoria de Servicio Técnico) "como la acabamos de hacer con banco plaza dejando
en claro que hace el cerebro y como los puede ayuda en su caso". Diagnóstico: el deck ya
explicaba el RESULTADO de cada función ("sugiere la orden de compra", "centraliza el
conocimiento") pero nunca el MECANISMO — qué hace el cerebro digital concretamente, con qué
datos, paso a paso. `banco-plaza-cerebros-digitales/` (CAI-025) sí tenía esa claridad, vía su
slide dedicada "Su segundo cerebro" (grafo relacional de Obsidian).

**Importante — se copió el ESTÁNDAR DE CLARIDAD, no el mecanismo literal**: el patrón
"asistente personal" de Banco Plaza (Claude + Projects + grafo Obsidian) no aplica al patrón
"sistema por funciones" de AMV (conectado a su sistema de gestión real, ya documentado así en
brief.md desde la construcción original). Se construyó una slide nueva y propia (`.s-explain`,
"Así funciona el cerebro digital", nueva slide 05) con 2 tarjetas en paralelo — una por
función — cada una con 3 facetas: **Datos que usa / Qué hace / Cómo te ayuda**, con las cifras
reales de AMV (7 modelos × 50-65 variantes; manuales/boletines/casos de ingenieros). Reutiliza
`.rmx-card`/`.rmx-facets` ya cargadas (mismo patrón que `.s-followup .followup-cards`: 2
tarjetas en paralelo sin nodos ni flechas, no es un roadmap secuencial). Deck pasa de 16 a 17
slides. **Lección generalizable**: una slide de Beneficios/Roadmap que describe el resultado
de un Cerebro Digital (o cualquier entregable técnico) sin explicar su mecanismo deja al
lector sin criterio para evaluar si aplica a su caso — el mecanismo + datos reales del cliente
es lo que hace tangible la promesa. Verificado end-to-end: `verificar-propuesta.sh` OK, slides
revisadas visualmente sin overflow, `/AP` confirmado por pypdf en Programa/Notas.

## 2026-09-23 — [cliente:la-tienda-del-blumer] DET-020: Detección de 7 áreas con slide nueva de "visión de ruta" hacia Habilidades y autonomía tecnológica
Primera propuesta para La Tienda del Blumer (retail familiar), a partir de Ficha de
Levantamiento de la asesora Verónica Rubio. Mismo patrón que `amv-tecnologia/` (DET-019,
Fundamentals + N áreas a 4h con logro inmediato, roadmap `.rmx-linear` de 3 etapas), escalado
de 3 a 7 áreas y de 2h a 4h de Fundamentals (pedido explícito del usuario) → **32h totales**
(4h Fundamentals + 7×4h Detección). Mismo dolor ancla que AMV (revisión manual de facturas en
Contabilidad) — se reutilizó el mismo estudio de Impacto ya verificado (Ardent Partners,
Accounts Payable Metrics 2025), sin volver a buscar fuentes.

**Novedad de esta propuesta**: instrucción explícita del usuario de dar "visión de ruta" —
la Detección no debía presentarse como servicio aislado, sino dejar visible que la clienta
(Mariana Duque) ya proyecta un camino más largo (Habilidades después, luego autonomía del
propio equipo de Sistemas en IA). Se resolvió con una **slide nueva** ("La ruta completa",
`.s-vision`) con 3 pasos horizontales: Detección (sólido, "cotizado en este documento") →
Habilidades (borde punteado, "a futuro, no cotizado") → Autonomía en IA (borde punteado,
"visión de Mariana") — separada del roadmap operativo interno de la Detección (que sigue
mostrando solo sus propios 3 pasos: Fundamentals+Áreas → Priorización → Reporte Final). Se
descartó mezclar las 2 fases futuras dentro del roadmap operativo (habría quedado en 5-6
nodos en una sola fila, con riesgo real de desborde) — mismo principio de fondo que `amcor/`
(Fase 1 cotizada + Fase 2 "a la medida del diagnóstico"), pero con slide propia en vez de vivir
dentro de un roadmap ya ocupado. El ROI de la hoja de cotización menciona explícitamente
ambos elementos por pedido directo del usuario: el logro inmediato por área Y la hoja de ruta
trazada — no alcanza con mencionar solo el diagnóstico.

**Bug de overflow atrapado y corregido**: el facet "Con quién" de la Etapa 1 del roadmap
(que lista las 7 áreas por nombre) desbordó la slide +29px al escribir los 7 nombres completos
("RRHH, Tesorería, Contabilidad, Sistemas, Administrativo, Logística/Compras e Inventario.")
— con solo 3 áreas (AMV) ese mismo patrón cabía sin problema. Fix: para N alto de items
enumerados en un facet de card compacta, resumir ("Las 7 áreas de la empresa.") en vez de
enumerar todos los nombres — el detalle completo ya vive en el Programa/Diagnóstico.

Sin garantía 30-60-90 (Detección pura, ese marco es solo de Habilidades) ni certificado
(mismo criterio que toda Detección). Hora de kick-off no especificada por el usuario para
este cliente — se usó 10-11 por consistencia con el resto de propuestas del día, marcado
"confirmar con Verónica" en `brief.md`. Calendario resumido por bloque de área (9 filas) en
vez de las 16 sesiones individuales de 2h, para no desbordar `.steps-calendar-grid`. PDF
verificado end-to-end: `verificar-propuesta.sh` OK (tras el fix de overflow), 13 slides
revisadas visualmente, `/AP` confirmado por pypdf en Programa/Notas.

## 2026-09-23 — [cliente:banco-plaza-copilot-producto] CAI-026: tercera propuesta de Banco Plaza, combo Detección+Habilidades para 1 persona con temario pendiente de la Detección
Tercera propuesta de Banco Plaza el mismo día. 1 solo participante (Alexis, área de
Producto), Copilot (licencias ya adquiridas por toda la organización). El usuario pidió
explícitamente combinar **Detección (4h, levantamiento) + Habilidades (8h, sesiones
prácticas) = 12h**, con el temario de Habilidades como **hipótesis preliminar** (instrucción
de Jean: investigar qué hace un área de Producto en un banco) que puede ajustarse tras la
Detección. **Servicio en `meta.json`**: `deteccion`, siguiendo el criterio ya documentado en
CLAUDE.md §4.1a para combos Detección+Habilidades (mismo patrón que `simple-tv-det002/`
DET-002) — pero el **código de carpeta/documento es CAI-026**, por instrucción explícita del
usuario (continúa la numeración de las 2 propuestas anteriores de la cuenta), no DET-. Esto
confirma que el código de catálogo (prefijo DET-/CAI-) y el campo `servicio` de `meta.json`
son dos decisiones independientes: el primero lo puede fijar el usuario libremente, el
segundo sigue la taxonomía del sistema para que `clientes/INDEX.md` agrupe bien el combo.

Clonado de `banco-plaza-mercadeo/` (CAI-024, mismo shell que las 2 propuestas anteriores de
la cuenta) en vez del patrón "Inversión por fases" de `simple-tv-det002/`/`amcor/` (2 cajas
de precio separadas) — con un alcance chico (12h, 1 persona) y sin una segunda propuesta
competidora, una sola hoja de cotización con el total es más clara. El roadmap de 2 etapas
(Detección + Habilidades) + estrella se resolvió reutilizando literal la plantilla de
roadmap de 1 página de 2 etapas ya usada en CAI-024/CAI-025 (`rmx-node-f2`/`rmx-node-f3`/
`rmx-node-r`), solo cambiando el contenido de las tarjetas.

**Dos bugs de mecánica atrapados y corregidos en este deck:**
1. **Marcador de Beneficios roto por copy personalizado**: al escribir el h2 de la slide de
   Beneficios como "Lo que **se lleva**." (singular, por ser 1 solo participante),
   `scripts/agregar-campo-precio.py` dejó de encontrar el marcador exacto "Lo que se llevan"
   que busca para inyectar los campos `Entregables`/`Acreditacion` — el primer
   `generar-pdf.sh` reportó "(omitido) 'Lo que se llevan' — no presente en este deck" en vez
   de agregar esos 2 campos. Fix: el h2 de esa slide es un **marcador fijo del sistema**, no
   texto de venta editable por audiencia — siempre "Lo que se llevan.", sin importar si el
   deck es para 1 persona o un equipo.
2. **Frase viajera evitada a propósito**: el hook de Impacto de `maurel-prom-copilot/` ("la
   diferencia no es la herramienta, es saber usarla") ya está marcado como frase viajera
   vendida a 3 clientes (`plantillas/redaccion.md`) — se redactó un hook nuevo, anclado al
   caso real de Alexis/Producto, en vez de reusarlo.

PDF verificado end-to-end: `verificar-propuesta.sh` OK (tras corregir 1 guion largo en un
h3 de Programa), 13 slides revisadas visualmente sin overflow, `/AP` confirmado por pypdf en
Programa/Notas.

## 2026-09-23 — [cliente:banco-plaza-cerebros-digitales] CAI-025: segunda propuesta para Banco Plaza, primera que aplica la tarifa "Cerebros Digitales" de extremo a extremo
Segunda propuesta para Banco Plaza el mismo día (la primera fue CAI-024, Mercadeo). El
usuario la describió como "básicamente lo que hicimos con Venemergencia, solo que en vez de
15, únicamente 5" — pero al preguntar por AskUserQuestion qué profundidad de "Cerebro
Digital" replicar (la ligera de catálogo/DHL, 6h/persona sin Claude Code, vs. la profunda de
la Fase 2 de `venemergencia/`, 12h/persona con Claude Code), el usuario confirmó la **ligera**
y **sin fase colectiva previa** — es decir, el nombre "Venemergencia" fue la referencia
mental del usuario, pero el contenido real coincide con el modelo ya vigente en el sistema
(`dhl-cerebro-digital/`), no con el deck de Venemergencia en sí. **Lección**: cuando un
usuario invoca un cliente pasado como referencia de un producto ("lo que hicimos con X"),
confirmar la profundidad/versión exacta antes de clonar — puede haber más de una versión del
mismo concepto en el sistema con horas muy distintas (aquí: 6h vs 12h por persona, ×2 el
costo total). Horas finales confirmadas explícitamente por el usuario en el mismo mensaje:
"esta propuesta debería ser de 30h en total, 5 personas 3 sesiones de 2h por c/u" → 5
participantes × 6h cada uno (3 sesiones de 2h) = 30h, coincidiendo con la tarifa "Excepción —
Cerebros Digitales" (6h/Cerebro) ya documentada en `empresa/politicas-comerciales.md` desde
el caso `grupo-corpos/DET-009` — **esta es la primera propuesta que construye esa tarifa de
punta a punta** (Grupo Corpos solo tiene la Detección que la originó). Clonado de
`dhl-cerebro-digital/` (CAI-005, mono-fase, sin roadmap, `.ruta` de progreso lineal),
generalizando el copy de "Miguel" (1 participante nombrado) a "cada líder"/"cada
participante" (5 personas, cargos aún sin definir — el propósito explícito de la propuesta es
que el presidente decida a quién asignar). Se le agregaron los estándares de Habilidades
vigentes desde hoy que DHL no tenía por ser anterior (descuento urgente, ROI, garantía
30-60-90 + slide `.s-followup`): como ese componente vive en `overrides.css` por deck (no en
`_base/styles.css`), hubo que copiar el bloque completo de CSS `.rmx-card`/`.s-roadmap` desde
`banco-plaza-mercadeo/overrides.css` aunque el resto del deck no usa ningún otro roadmap —
las reglas de nodos/flechas quedan sin uso, inofensivas. **Sin calendario de inicio**: a
diferencia de CAI-024, el usuario no dio fecha de arranque para esta propuesta — se omitió
`.steps-calendar` en vez de inventar fechas (regla ya establecida
[[omitir-no-inventar-placeholder]]). **Bug de nombre de archivo evitado**: el H1 de portada
tenía el punto final fuera del `<span class="hl">` (mismo patrón que
[[bug-punto-final-fuera-de-span-flota]], pero manifestado aquí como un espacio huérfano antes
de ".pdf" en el nombre del archivo generado, no solo como flotación visual) — se detectó en
el primer `generar-pdf.sh` y se corrigió moviendo el punto dentro del span antes de continuar
el trío. PDF verificado end-to-end: `verificar-propuesta.sh` OK, 14 slides revisadas
visualmente sin overflow, `/AP` confirmado por pypdf en Programa/Notas.

## 2026-09-23 — [cliente:banco-plaza-mercadeo] CAI-024 sube a 4 etapas / 10h tras 7 ajustes de alcance en vivo, mismo día
Mismo día, después de construida la v1 (3 etapas, 5h): el usuario pidió incluir al cliente en
las sesiones de Construcción ("debería ser una propuesta de 10h"), y ajustó el desglose de
horas en 6 mensajes seguidos (historial completo en `brief.md` de este cliente) hasta fijar
el orden y las horas **definitivos**: **Kick-off (1h, aparte — no cuenta en el total) →
Fundamentals (2h) → Construcción (4h, 2 sesiones de revisión con Mercadeo) → Implementación
(4h, 2 sesiones) = 10h de propuesta**. Dos correcciones intermedias vale la pena registrar
porque Claude las infirió mal: (1) al pedir "10h" y reordenar Construcción al medio, Claude
subió Kick-off de 1h a 2h para cuadrar la suma — el usuario corrigió tajante ("el kick off es
máximo 1h... y no se cuenta dentro de las horas de propuesta"); (2) con Kick-off de vuelta en
1h aparte, la suma quedaba en 8h (2+4+2) en vez de 10h — ahí sí correspondía señalar el
desfase en vez de inferir, y el usuario lo cerró subiendo Implementación a 4h (2 sesiones).
**Lección**: ante una instrucción de horas que no cuadra con un total ya dado, señalar el
desfase explícitamente en vez de adivinar qué etapa absorbe la diferencia.

Esto subió el roadmap de 3 a 4 etapas — se aplicó el mismo split en 2 páginas de
`amv-tecnologia-cerebro-digital/`, y esta vez el roadmap **no** empujó `.rmx-ethics` contra
el `.foot` (facets escritas cortas desde el principio, aplicando la lección de
[[gotchas-clonar-rmx-card-y-cierre-escalera]]). Sí volvió a aparecer el bug de Duración en
`.s-price` (texto con los 4 nombres de etapa desbordó a 3 líneas) — mismo fix de siempre:
acortar a "N etapas · Xh totales", el detalle completo ya vive en el bloque Programa de al
lado. Confirma que estos 2 gotchas (roadmap card / Duración) son los primeros que hay que
revisar cada vez que se le agrega una etapa a un roadmap ya cotizado, en cualquier deck.
Además, Construcción pasó a tener su propia schedule slide (Temas/Timebar/3 columnas), igual
tratamiento que Fundamentals/Implementación — pedido explícito del usuario ("hazle una lámina
como se lo hiciste a las demás"), no solo vivir en roadmap + calendario. PDF final verificado
end-to-end: `verificar-propuesta.sh` OK, 15 slides revisadas visualmente sin overflow, `/AP`
confirmado por pypdf en Programa/Notas.

## 2026-09-23 — [cliente:banco-plaza-mercadeo] Primera propuesta nueva con todos los estándares del día (CAI-024, sin Ficha Comercial)
Habilidades, Banco Plaza, Mercadeo — servicio de producción de creativos (50/mes, a cargo de
Intezia) en paralelo a Fundamentals de Claude + construcción de una Skill, dado directo por
el usuario sin Ficha Comercial. Reutilizó `amv-tecnologia-cerebro-digital/` (CAI-023) como
base estructural (mismo shell, todos los estándares de hoy: descuento urgente, calendario
completo, ROI, garantía + slide de Seguimiento 30-60-90, `.timebar`), simplificado a 1 solo
track de 3 etapas (sin los 2 "funciones" de CAI-023). Precedentes de contenido:
`puro-lomo-bajo-mercadeo/` (CAP-101, patrón "Skill por proceso" + contacto de Flavia
Martínez) y `venezolano-de-credito/` (CAI-018, banco + Mercadeo).

**2 bugs de overflow interno encontrados y corregidos** (ninguno lo vio el detector
automático — mismo blindspot de siempre, cajas que se hornean después del render):
1. **Roadmap `.rmx-card` con texto más largo que CAI-023 empujó `.rmx-ethics` hasta
   solaparse con el `.foot`** — las facets de "Qué pasa" tenían frases más largas que el
   original (ej. "Alineamos objetivos y contexto de marca antes de producir nada." en vez de
   algo más corto), lo que hizo crecer las 4 tarjetas lo suficiente para empujar la barra de
   metodología casi hasta el pie de página. Fix: acortar las 3 facets de cada tarjeta del
   roadmap a frases de una línea donde sea posible — **al reutilizar el patrón `.rmx-card` en
   un deck nuevo, no asumir que el mismo largo de texto del original cabe igual**, cada
   contenido nuevo puede ser más verboso y estas tarjetas no tienen altura fija.
2. **Cierre escalera, Paso 1 — la caja más chica de las 3 (37.5pt de alto) no tolera más de
   ~24 caracteres**: "Kick-off y parámetros de marca" (30 caracteres) se cortó visualmente
   contra el borde de la caja. Los pasos 2 y 3 tienen cajas más altas (75pt y 112.5pt) por el
   efecto escalera y toleran más texto — **Paso 1 siempre necesita el texto más corto de los
   3**, no simétrico con los otros dos.
Ambos corregidos antes de declarar el PDF entregable — confirma que la revisión visual
slide-por-slide (§4.10) sigue siendo obligatoria incluso clonando de un deck ya verificado
el mismo día.

## 2026-09-23 — [cliente:amv-tecnologia-cerebro-digital] Timebar faltante, slide 30-60-90 nueva, y calendario agrandado (4ta ronda del mismo día)
Tras el fix de `.ses-body` (entrada de abajo), el usuario aclaró que el vacío en las páginas
7-10 de CAI-023 no era (solo) un problema de CSS: **faltaba contenido real**. `.s-schedule`
tiene 5 elementos siempre presentes (Temas, **Tiempo/`.timebar`**, 3 columnas) — documentado
en `propuesta-comercial-ref.md` desde antes, pero CAI-023 se construyó sin el `.timebar` en
sus 4 slides de sesión. Se agregó el bloque real (mismo patrón que `amv-tecnologia/`: barras
`.seg` proporcionales a los minutos, ej. "2h Entrevista sobre criterio de compra"). Ahora sí
es contenido, no relleno visual — y de paso confirma que mi fix anterior de `.ses-body` (CSS)
seguía siendo válido, solo que no era la corrección completa por sí sola.
Además, 3 pedidos más el mismo día:
1. **Nueva slide "Seguimiento 30-60-90"** (solo Habilidades, después de Propuesta Económica):
   explica los 3 check-ins con el texto que el usuario dio al principio de la conversación
   (ya vivía en `empresa/tipos-de-documento.md §0.2`) + ROI expandido conectado a esa curva
   de tiempo. Reutiliza `.rmx-card`/`.rmx-facets` del roadmap en 3 columnas sin nodos. CAI-023
   pasa de 15 a 16 slides.
2. **Calendario agrandado**: se veía "muy pequeño" — subió `font-size` y padding en
   `.steps-calendar`/`.cal-row` (ambas propuestas). Esto **rompió el detector de overflow**
   en el caso de 7 filas por columna (CAI-023, +34px) — se corrigió bajando el padding
   vertical de `.cal-row` a 5px, quedando dentro de la slide con margen. Queda documentado
   como el límite probado: ~7 filas por columna a esta tipografía es el máximo seguro.
3. **ROI de DET-019**: se pidió sumar mención de los logros inmediatos que se construyen en
   cada sesión de área (ya establecidos en el propio Cronograma del deck), no solo el
   hallazgo de auditoría — refuerza que Detección entrega algo funcionando, no solo un
   informe.
Se encontraron y corrigieron 2 errores reales del verificador automático en el camino
(guion largo en `.followup-intro`, overflow del calendario agrandado) — ambos antes de
declarar el trabajo terminado, como corresponde según §10.
Detalle: `plantillas/propuesta-comercial.md` (Reglas de layout, Calendario de inicio, nueva
sección "Seguimiento 30-60-90").

## 2026-09-23 — [regla] `.s-schedule .ses-body` — mismo bug de "espacio vacío feo" que Programa, ahora en el desglose instructivo
Tercer caso del mismo patrón (ver entradas de arriba: `.s-program .modules`). El usuario
reportó las páginas 7-10 de CAI-023 (Diagnóstico/Adopción/Implementación por función) con un
vacío grande y feo entre los chips de "Temas" y las 3 columnas de abajo. Causa: `.ses-body`
usaba `justify-content: space-between`, que reparte TODO el aire sobrante entre los 2 hijos
— con pocos ítems (3 bullets por columna) el vacío queda enorme y partido justo en el medio
de la slide. Fix: `justify-content: flex-start` + `gap: 32px` fijo — las columnas quedan
pegadas debajo de Temas, el sobrante de alto queda como aire al final de la slide (antes del
footer), no en el medio del contenido. Afecta a **toda** propuesta con `.s-schedule`, no solo
CAI-023 — mismo principio que ya se aplicó a `.s-program .modules`: no estirar
espaciado/cajas a llenar el resto de la slide cuando el contenido es sparse. Sin riesgo de
overflow nuevo para decks con contenido denso (4-5 ítems): el cambio no agrega ni quita
límites de altura, solo redistribuye dónde cae el aire sobrante.

## 2026-09-23 — [bug][scripts] Programa y Notas invisibles en Adobe/Preview desde el 2026-08-31 — bug de sistema, no de estas 2 propuestas
Al revisar DET-019 y CAI-023 tras la ronda de correcciones de arriba, el usuario reportó que
"Programa" y "Notas" no aparecían en la hoja de cotización. Investigado con pypdf directo
sobre el PDF (no con el extractor de Claude, que SÍ los mostraba bien y por eso el bug pasó
desapercibido antes):

- **Causa raíz**: `Programa` y `Notas` tenían `/V` correcto (el texto SÍ estaba en el campo)
  pero **sin `/AP` horneado** (sin apariencia). Con `/NeedAppearances: False` — fix de
  2026-08-31 para el bug `bug-needappearances-cliente-regenera-campos.md` — Adobe Reader y
  Preview **no regeneran** la apariencia de un campo que no la tiene: lo muestran en blanco
  aunque el valor esté ahí. El extractor de PDF que usa Claude (poppler) sí regenera
  apariencias sin importar la bandera, por eso el problema no se veía en las revisiones
  visuales previas de este sistema — **es un punto ciego real del proceso de QA actual**.
- **Alcance real del bug**: no es exclusivo de estas 2 propuestas. `rebake_bold_fields()`
  (`scripts/acroform_appearance.py`) solo horneaba `BOLD_FIELDS` (Entregables, Acreditacion)
  y `REGULAR_BAKED_FIELDS` (Paso01-03 Titulo/Body) — nunca cubrió `Programa` ni `Notas`.
  **Cualquier propuesta regenerada con `customize-acroforms.py` desde el 2026-08-31** (fecha
  del fix de NeedAppearances) probablemente tiene el mismo problema en Adobe/Preview, aunque
  el HTML y el extractor de Claude la muestren bien. No se auditaron retroactivamente todas
  las ~130 propuestas del índice — pendiente si el usuario lo pide.
- **Fix**: se agregó `"Programa"` y `"Notas"` a `REGULAR_BAKED_FIELDS` en
  `acroform_appearance.py` — ahora se hornean igual que los Pasos, sin cambiar nada más del
  flujo (`rebake_bold_fields()` ya se llama en el punto correcto). Campos de precio
  (`PrecioBase`/`Descuento`/`PrecioTotal` y variantes Fase/Ciclo) quedaron **fuera** a
  propósito: nacen vacíos por diseño, no hay texto pre-llenado que pueda quedar invisible.
- **Cómo verificar de ahora en adelante**: el extractor de PDF de Claude NO sirve para
  detectar este tipo de bug (regenera apariencias igual). Verificar con pypdf directo:
  `campo.get('/AP')` debe existir para todo campo con `/V` no vacío que el sistema pre-llena.
- Aplicado y verificado en `amv-tecnologia/` y `amv-tecnologia-cerebro-digital/`
  (2026-09-23) — ambas regeneradas con el fix, `/AP` confirmado presente en Programa y Notas.

## 2026-09-23 — [regla] 4 correcciones generales aplicadas a DET-019/CAI-023 y a todo el sistema
El usuario pidió correcciones "en general para las propuestas" al revisar DET-019/CAI-023 ya
regeneradas. Las 4 aplican como estándar de aquí en adelante, no solo a estas 2:
1. **Tarjetas de Programa sin espacio en blanco excesivo**: `.s-program .modules` tenía
   `flex:1` (estiraba la grilla a llenar TODO el alto restante de la slide, y con
   `align-items:stretch` cada `.module` se inflaba con pocos temas). Fix: se quitó `flex:1`,
   se fijó `min-height:320px` en la tarjeta base (1-3 módulos). El resto de anchos por
   volumen (4/5-6/7-9/10+) ya tenían su propio min-height menor, sin tocar. Afecta a **toda**
   propuesta con `.s-program`, no solo estas 2.
2. **Descuento urgente — texto más corto y letra más grande**: "Descuento válido por
   aprobación en 15 días" (9px) → **"Descuento válido por 15 días"** (13px). Mismo criterio
   para la variante Innovación ("Beneficio válido por...").
3. **Calendario de inicio completo** (`.steps-calendar`, nueva variante junto a
   `.steps-projection`): el usuario pidió listar TODAS las sesiones de la propuesta,
   kick-off incluido, no solo una fecha resumen. Requirió compactar `.step-card` (400px →
   200px de min-height) para dejarle espacio — cascada obligatoria en
   `scripts/agregar-campo-precio.py` (rects de `Paso01-03` recalculados) y `_base/
   styles.css`. Sesiones de más de 2h en una cadencia de slots fijos (ej. "4h por área" con
   slots de 2h) se parten en `(1/2)`/`(2/2)`; etapas sin sesión (Construcción) quedan como
   fila marcadora `cal-marker`, sin hora. Fechas de este caso: kick-off martes 29 sep,
   sesiones regulares martes/jueves 10-12 desde la semana del 5 de octubre.
4. **Sin ejemplo anecdótico centrando el deck**: el título, hook de Impacto, ROI y varios
   bullets de DET-019/CAI-023 centraban la venta en "Juan consolidó 80 facturas, de 8h a 10
   min" — un ejemplo que el cliente dio en vivo de algo que ya hizo solo. El usuario pidió
   retirarlo de títulos y menciones (riesgo de disonancia si se sobre-enfoca ahí en vez de
   vender el proyecto completo). Se conserva una mención genérica ("ya probó que la IA
   funciona"), sin nombrar el proceso ni las cifras. Nuevo título DET-019: "Del criterio
   manual a la decisión con datos." (antes: "De 8 horas a 10 minutos.") — el PDF viejo se
   borró (el nombre del archivo se deriva del H1).
Detalle completo: `plantillas/propuesta-comercial.md` (Slide 4, Reglas de copy, Calendario de
inicio, Checklist), `plantillas/generar-pdf.md`, `empresa/marca-visual.md`.

## 2026-09-23 — [plantilla] Calendario de inicio implementado: `.steps-projection` dentro de paleta oficial
Tercer y último elemento pendiente de la hoja de cotización nueva (§ver entrada de abajo).
El usuario dio la fecha directo ("martes y jueves a partir de la semana del 5 al 9" → martes
6 y jueves 8 de octubre de 2026) para DET-019 y CAI-023, pidiendo que "denote urgencia".
1. **Visual**: a diferencia del descuento urgente, este bloque **no** usa la excepción
   roja/rosada (esa queda acotada solo a ese badge) — la urgencia se logra con contraste
   negro/amarillo de marca: franja negra ancho completo, borde amarillo 8px, tag en
   mayúsculas amarillas + fechas en blanco bold grande + proyección de resultado atenuada
   con separador. Clases: `.steps-projection`/`-tag`/`-dates`/`-result`.
2. **Ubicación**: dentro de `.s-steps`, debajo de las 3 `.step-card` — no toca los campos
   AcroForm `Paso01-03`. Cabe con margen antes del `.foot` (que es `position:absolute
   bottom:24px`) sin necesidad de slide nueva.
3. **Dato sin Ficha Comercial**: como no había `resultados_esperados` explícito de ningún
   cliente, la proyección de resultado se redactó desde el alcance/logro ya establecido en
   cada brief (facturas para DET-019, adopción a 30 días para CAI-023) — no se re-preguntó
   al usuario por ese dato puntual, solo por la fecha que sí pidió dar directamente.
Detalle: `plantillas/propuesta-comercial.md` → *Próximos pasos — calendario de inicio*.

## 2026-09-23 — [cliente:amv-tecnologia-cerebro-digital] CAI-023 pasa a 4 etapas (24h) + primer uso real del formato nuevo de cotización
Al repetir DET-019 y CAI-023 (AMV Tecnología) con el formato nuevo de hoja de cotización, el
usuario pidió agregar una 4ta etapa a CAI-023: **Implementación** (2 sesiones de 2h por
función × 2 funciones = 8h), además de Diagnóstico/Construcción/Adopción ya existentes.
Total de sesiones con el cliente sube de 16h a **24h**.
1. **Roadmap de 4 etapas en un servicio único (no Integral)**: se replicó el patrón de
   `simple-tv-all001/` (dividir en 2 slides `.rmx-linear` de 2 etapas + resultado cada una,
   en vez de comprimir 4 cards + resultado en una sola fila de 5 columnas) — primera vez que
   ese patrón se usa fuera de una propuesta `integral`. Evita el riesgo de overflow interno
   que `verificar-overflow.js` no detecta (mismo problema ya documentado en
   `roadmap-3-etapas-flex-minheight.md` para ir de 2 a 3 rutas).
2. **Bug real encontrado (no lo cachó el detector)**: el `.block-value` de Duración en
   `.s-price` es flujo normal (no absolute) y `.block-programa` está fijo en `top:195px` —
   agregar "+ Implementación (8h)" empujó el texto a 3 líneas y la 3ra se solapó con el label
   "PROGRAMA". Fix: acortar a solo nombres de etapa sin repetir horas individuales
   ("Diagnóstico + Construcción + Adopción + Implementación · 24h totales"), ya que el
   bloque Programa de al lado repite el desglose completo.
3. **Primer uso real de los 3 elementos nuevos de cotización** (§ver entrada de abajo,
   2026-09-23): descuento urgente + ROI + garantía (CAI-023, Habilidades) y descuento
   urgente + ROI sin garantía (DET-019, Detección — sin marco 30-60-90 propio todavía).
   Ambas cupieron sin desborde una vez resuelto el bug de Duración.
4. **Orden del trío en decks con `customize-<slug>.py` propio**: quedó reconfirmado el orden
   correcto — `generar-pdf.sh` → `customize-acroforms.py` (con paths explícitos si la carpeta
   tiene 2+ PDFs, como `amv-tecnologia/` con la nota de licencias aparte) → script propio AL
   FINAL. Invertir el orden re-hornea Beneficios v3 en blanco/negro y dobla el trabajo.
Detalle: `clientes/propuestas/amv-tecnologia-cerebro-digital/brief.md` y `programa.md`.

## 2026-09-23 — [regla] Descuento urgente: excepción de color rojo/rosado (rechaza la alternativa en naranja)
Al implementar el punto 1 de la entrada de abajo, Claude propuso primero una variante
tintada del naranja de marca (dentro de paleta, siguiendo la regla de `marca-visual.md` de
proponer alternativa antes de aceptar un color fuera de marca). El usuario la rechazó
explícitamente: "tiene que ser a juro rojo... sino no es visualmente atractivo". Queda
como **excepción de color permanente pero acotada a un único elemento** — el badge de
descuento urgente (`.cot-urgent-note`/`.cot-sign-minus`), tokens `--discount-urgent-red:
#D32F2F` / `--discount-urgent-pink-bg: #FCE4EC`. El resto del deck (fondos, textos, otros
acentos) sigue exclusivamente en la paleta oficial — esta excepción no se extiende a nada
más. Detalle: `empresa/marca-visual.md` → *Descuento con urgencia — excepción de color
explícita*, `plantillas/propuesta-comercial.md` → checklist de paleta.

## 2026-09-23 — [plantilla] Hoja de cotización como cierre de venta (descuento urgente, calendario, ROI, garantía) + lenguaje "construimos, no solo enseñamos"
El usuario pidió convertir la hoja de cotización en palanca de cierre y reposicionar el
lenguaje de venta. Cambios, todos para propuestas nuevas de aquí en adelante (no
retroactivo):
1. **Descuento con urgencia**: prefijo estático `−$` + etiqueta "Descuento válido por
   aprobación en 15 días" (fijo, convive con "Cotización válida por 30 días"). Visual:
   rojo `#D32F2F` + fondo rosado `#FCE4EC` — excepción explícita a la paleta oficial, ver
   entrada de arriba (2026-09-23, "Descuento urgente: excepción de color rojo/rosado").
2. **Calendario de inicio**: dentro de "Cómo arrancamos" (no slide nueva), fechas sugeridas
   + proyección de resultados, sourced de `brief.md → fecha_arranque_deseada /
   resultados_esperados` (Ficha Comercial o pregunta directa; sin dato, se omite).
3. **ROI estimado**: bloque narrativo en la Cotización, redactado por Claude desde lo que el
   cliente dice que quiere lograr (Ficha Comercial) — proyección, nunca cifra garantizada.
4. **Garantía 30-60-90**: solo servicio Habilidades por ahora (único con marco de
   seguimiento definido, §0.2 de tipos-de-documento.md). Copy tipo sello, sin mecanismo
   financiero específico (ni reembolso ni repetición prometida) — mensaje de acompañamiento,
   confirmado con el usuario tras aclarar que "retrocedemos sin costo" era una forma de
   hablar, no un compromiso literal.
5. **Ficha Comercial pasa a ser el flujo esperado** (ya no "modalidad vieja, la mayoría no
   la tiene") — habilita 2 y 3. Ver `CLAUDE.md §6 Paso 3`.
6. **Lenguaje**: "capacitación" convive con "construimos, probamos y dejamos instalado" en
   Objetivos/Beneficios — responde "¿ustedes lo hacen o lo hacemos nosotros?". No toca
   nombres de categoría del catálogo (Capacitación In-Company, códigos CAI-/TA-/CU-/DIP-
   siguen igual).
Detalle completo: `plantillas/propuesta-comercial.md`, `plantillas/generar-pdf.md`,
`empresa/marca-visual.md`, `empresa/politicas-comerciales.md`, `CLAUDE.md §6`.

## 2026-09-23 — [plantilla] Especificación completa del Seguimiento 30-60-90 (servicio Habilidades)
El usuario explicó qué mide cada uno de los 3 check-ins post-servicio y reemplaza la lógica
anterior ("uso vs. esperado → refuerzo → escala o cierra Habilidades/pasa a Innovación"). El
objetivo pasa a ser verificar que las habilidades instaladas se usen, se multipliquen y
generen impacto real: **30 días** = uso real de lo entregado (nivelación y recomendaciones);
**60 días** = ya no se revisa el skill entregado, se mapean skills/soluciones **nuevas**
construidas por el equipo; **90 días** = no se cuentan skills, se mide **tiempo** ahorrado, en
qué se reinvierte y productividad actual del área. Especificación completa en
`empresa/tipos-de-documento.md §0.2`. Aplicado a `plantillas/kickoff-canonico/kickoff.html`
(las 3 `.scard` de Etapa 4 + resumen de ruta) y `plantillas/brief-kickoff.md §5`. No
retroactivo a briefs de kickoff ya generados para clientes (mismo criterio `CLAUDE.md §4.10a`).

## 2026-09-14 — [regla] Sin link de Calendly en el cierre (Dashboards + Propuestas)
El cierre (`.s-end`) de Dashboards de Impacto y propuestas comerciales deja de enlazar a
`calendly.com/intezia/30min` de aquí en adelante. Caso base: Cavedatos (dashboard CAI-001),
donde el usuario pidió quitarlo y confirmó que aplica a ambos flujos, no solo al dashboard en
curso. Para propuestas, esto formaliza algo que el cierre "escalera" ya hacía desde
2026-08-26 (`<span class="cta">` sin link) pero que el checklist de
`propuesta-comercial.md` no reflejaba (seguía pidiendo `<a href="calendly...">`). El
contacto de cierre pasa a ser solo la asesora comercial en `.end-contact`. No retroactivo:
decks y dashboards ya entregados (incluido el piloto `apb-group/`) conservan su CTA.
Detalle: `plantillas/dashboard-edutrace.md` y `plantillas/propuesta-comercial.md` → checklist.

## 2026-09-09 — [regla] Especificación completa del servicio Políticas
El usuario compartió el documento maestro interno de Políticas (Dirección de Productos y
Servicios): metodología (cuestionario Genérico + Específico por área, 9 dimensiones de
gobernanza AI Verify/IMDA, 3-5 semanas), las 4 etapas (Kick-off → Diagnóstico de madurez por
área → Cuestionario dirigido por hallazgos → Redacción y validación, con la «Brújula IA» en
paralelo en la etapa 4), roles y los 7 entregables tangibles (Informe de diagnóstico, Manual
de políticas, Matriz de riesgos, Marco de gobernanza, Brújula IA, sesión de socialización,
ruta confirmada en Kick-off). Documentado en `empresa/tipos-de-documento.md §0.1` (nuevo) y
referenciado desde `empresa/politicas-comerciales.md`. **No resuelve** la decisión pendiente
de formato de la propuesta comercial (deck vs. informe de consultoría, Ivana + David) — eso
sigue bloqueante para construir cualquier propuesta real de Políticas.

## 2026-09-09 — [regla] Dimensionamiento de horas/entregables por servicio (los 4 del Modelo Intezia)
El usuario formalizó cómo calcular cuánto cotizar en toda propuesta nueva, por servicio
(§4.1a): **Detección** = 4h por área + 2h de Fundamentals grupal (máx. 25 personas por
sesión; más gente → varias sesiones de Fundamentals). **Habilidades** = 8-12h por área
(hasta 5 procesos) + 4h por proceso extra sobre el quinto — **excepción**: si el entregable
se enmarca explícitamente como construir Cerebros Digitales (no automatización de procesos
regular), la tarifa es 6h por Cerebro Digital en su lugar, nunca combinando ambas reglas.
**Políticas** = por entregable (una sola entrega: borrador + demás componentes, sin tema de
horas) — specs completas del entregable (incluye un componente tipo "brújula") aún
pendientes de que el usuario las envíe, no inventar mientras tanto. **Innovación** = sin
cambios, sigue el patrón de INN-001 (Zoom). Documentado en
`empresa/politicas-comerciales.md` → "Dimensionamiento por servicio".

## 2026-09-04 — [cliente:dhl] DET-004: 3 fases, menos foco en Copilot, Claude nombrado como opción
El usuario pidió 3 ajustes tras conversar con Miguel (DHL): (1) suavizar el foco exclusivo
en Copilot en toda la redacción, sin que la propuesta se lea como "todo es Copilot"; (2)
fusionar visualmente Fase 1 (Detección) y la nivelación de Copilot en un solo bloque —ya
lo eran en el cronograma real, el problema era solo la slide "El camino" mostrándolas como
3 tarjetas separadas—; (3) partir Habilidades en Fase 2 y Fase 3, con Fase 3 dejando espacio
abierto para procesos adicionales que la auditoría identifique (mismo principio de "no
inventar" ya aplicado en `good-latam-cai010/` y `bidzi/`). Confirmado con AskUserQuestion:
agrupación por bloque operativo/estratégico, las 3 fases cotizadas ya.
**Corrección mid-turn del usuario**: pidió explícitamente nombrar a **Claude** como la
herramienta alternativa a evaluar (no dejarla genérica) — a diferencia del patrón "no
inventar" de otros casos, aquí el usuario SÍ tenía la información directa de la conversación
con el cliente y pidió nombrarla. Lección: "no inventar" aplica a lo que el sistema infiere
sin respaldo; cuando el usuario da la instrucción directa con conocimiento de primera mano,
se ejecuta tal cual, incluso si contradice una restricción `§4.11` anterior de una ficha más
vieja (se documentó el reemplazo en brief.md, sin borrar el registro histórico).
**Patrón técnico**: 3ra variante de `make_fase_subtotal_js(N)` en la sesión (N=1 good-latam,
N=2 bidzi, y aquí N=3 — que resultó ser el default nativo de `agregar-campo-precio.py`, sin
necesitar ninguna limpieza de campos).
**Error propio cometido y corregido**: al simplificar `customize-dhl.py` edité el docstring
para decir "ya no elimina PrecioFase3" pero olvidé borrar el código real que sí lo hacía —
el script siguió comportándose igual hasta que el `grep`/pypdf post-generación lo expuso.
Recordatorio: un docstring actualizado no es evidencia de que el código cambió — verificar
el código ejecutable, no el comentario que lo describe.
**Mismo bug de Cierre repetido una 4ta vez** (`bug-cierre-default-vive-en-script-no-html`):
edité los defaults de `CierrePaso2`/`CierrePaso3` en `index.html` pero no en
`customize-dhl.py`; solo se detectó en la revisión visual del PDF. Memoria reforzada con
regla más prescriptiva (grep del texto viejo en el customize script como parte del mismo
paso de edición, no como verificación posterior).

## 2026-09-04 — [cliente:bidzi] CAI-011 corregida: de Habilidades sola a combo Detección + Habilidades
La 1ra versión de CAI-011 (Bidzi, institución financiera) se construyó como Habilidades pura,
razonando que el Bloque de Detección de la Ficha venía casi vacío. El usuario corrigió: la
Ficha SÍ pedía ambos servicios ("la propuesta tenía detección y no la coloqué"), y un bloque
vacío en la ficha significa "auditar con lo que hay", no "omitir el servicio". Contexto
adicional: la reunión con el cliente fue limitada (fue directo a pedir cotización) — los 12
departamentos y el único proceso mencionado de pasada NO deben ser el techo de la propuesta,
sino el punto de partida de una auditoría real.
**3 decisiones resueltas con AskUserQuestion**: (1) código CAI-011 se mantiene pese a que el
servicio de entrada pasa a ser Detección — inconsistencia código/servicio documentada en
brief.md, sin precedente exacto en el sistema; (2) Detección audita las 12 áreas de forma
amplia, no solo el proceso ya conocido; (3) Habilidades queda como programa único con
tronco común + 1 pista ya identificada + pistas adicionales "a definir" (nunca inventadas)
según lo que arroje la Detección.
**Patrón técnico nuevo**: "Inversión por fases" con **2 fases cotizadas** (no 1+diferidas
como amcor, ni 1 cotizada+2 notas como good-latam-cai010) — se generalizó
`make_fase_subtotal_js(N)` a N=2, eliminando solo `PrecioFase3` huérfana. Mismo mecanismo,
tercera variante de N en la misma sesión.
**Mismo bug de truncado de AcroForm, 2da vez en el mismo día**: el layout "ampliado" de
Beneficios v3 (355-474pt, no el rect chico de 158×117pt) también se desbordó — ver memoria
`bug-entregables-acroform-box-narrow` actualizada con este caso. Ninguno de los dos tamaños
de caja es inmune; solo la revisión visual a resolución alta lo detecta.

## 2026-09-04 — [cliente:good-latam-cai010] Automatización de Creación — 1er caso de "N departamentos = N fases diferidas"
Nueva propuesta CAI-010, independiente de `good-latam/` (CAP-109), retomando la nota interna
de "Creación/Compras/Digital como propuesta separada" dejada al acotar CAP-109 a
Administración. El usuario compartió el proceso real de Creación ("Proceso de grillas", 12
pasos) pero **no** los de Compras/Digital ("no me darán documentos hasta que estén seguros
de cómo trabajamos"). Al preguntarle si convenía inventar procesos similares para Compras/
Digital "de entrada", se recomendó explícitamente **no hacerlo** (riesgo: un proceso
inventado que no coincide con la realidad del área comunica lo contrario de lo que se busca)
— el usuario aceptó cotizar solo Creación y dejar las otras 2 "a definir".
**Patrón nuevo**: roadmap de 3 fases = 3 **departamentos** (no 3 etapas de un mismo
departamento) + hoja de precio "Inversión por fases" Patrón A diferido (memoria
`patron-fases-cotizadas-vs-diferidas`, mecánica de `amcor/customize-amcor.py` reutilizada
tal cual: solo se quitan PrecioFase2/3 y se recalcula el subtotal a 1 fase). Reutilizable
para cualquier cliente que pida escalar un servicio a varias áreas/departamentos sin tener
todavía la documentación de todas.
**Corrección a mitad de sesión (1/3)**: el usuario aclaró que Good Latam usa **Gemini, no
Claude**, y no quiere cambiar de herramienta — dato que no estaba en ningún brief anterior.
Sirve de recordatorio: preguntar explícitamente qué herramienta de IA ya usa el cliente antes
de asumir Claude por defecto del sistema.
**Corrección 2/3**: *"no haremos un cerebro digital, no usamos n8n solo usamos herramientas
del ecosistema google workspace"* — se retiró el naming "Cerebro Digital" (sin reemplazo por
otro nombre de producto) y n8n como capa de automatización, sustituido por **Google Apps
Script** (nativo de Workspace, incluye llamadas a APIs externas como Basecamp vía
`UrlFetchApp`).
**Corrección 3/3**: *"ellos usan google ai studio y podemos incluir otras que de verdad los
ayuden"* — los asistentes de IA (redacción, estructuración de feedback) pasaron de "Gemas
(Gems)" de Gemini a construirse en **Google AI Studio**. Patrón para clientes con stack de IA
ya definido: no asumir de una sola vez todo el stack (modelo + producto + capa de
automatización) — preguntar cada pieza por separado si no viene en el brief inicial, en vez
de inferir el paquete completo de una sola corrección.
**Bug re-encontrado durante los ajustes**: al alargar el copy de `Entregables` (mencionando
las 3 herramientas nuevas), el texto se truncó de verdad dentro de la caja AcroForm (193×355pt
— ver memoria `bug-entregables-acroform-box-narrow`), cortando el último ítem a media
palabra. El detector automático no lo vio (la caja está vacía en el HTML, el texto solo vive
en el `/V` del PDF). Se resolvió acortando el copy, no agrandando la caja.
**Bug encontrado**: `bug-impact-bar-val-narrow-overflow` — el valor de una barra angosta de
Impacto (`.s-impact .bar-val`, ej. "+5–15%" en una barra de 15%) se parte en 2 líneas o se
vuelve ilegible; el detector automático no lo agarra (no es un clip por overflow:hidden).
Fix aplicado localmente en este deck (valor reposicionado fuera del fill).

## 2026-09-03 — [cliente:grupo-ferrara] DET-005 gana etapa Fundamentals, CAI-007 gana Cerebro Digital compartido
Dos ajustes de contenido pedidos por el usuario sobre las 2 propuestas ya enviadas de Grupo
Ferrara. **DET-005**: el marco IADD (4 etapas) no tenía ningún paso de nivelación pese a que
la definición oficial de Detección (`empresa/tipos-de-documento.md §0`) exige "nivelar al
equipo... antes del informe final" — se agregó una etapa **Fundamentals** entre Iniciación y
Auditoría (1 sesión grupal de 2h, marco pasa a 5 etapas, 8h→10h total), con precedente en
Good Latam CAP-109. Decisión de alcance puntual, no se tocó el marco IADD de catálogo.
**CAI-007**: se reincorporó el concepto "Cerebro Digital" (Claude + grafo Obsidian) que se
había descartado al construir el deck original — aquí **compartido para la Dirección** (el
dueño y su hijo usan 1 sola IA con el contexto de la empresa), no individual como en
`dhl-cerebro-digital/`. Slide `.s-graph` reincorporada (12→13 slides).
**Bug re-confirmado**: `bug-cierre-default-vive-en-script-no-html` — al reincorporar el
Cerebro Digital, el HTML del Cierre se editó correctamente pero el PDF siguió mostrando el
texto viejo hasta regenerar el PDF base completo (`generar-pdf.sh`) antes de correr el
customize propio — el script solo agrega las 4 cajas de Cierre si no existen todavía, no
las actualiza si ya están presentes en el PDF.

---

## 2026-09-01 — [regla] Portada: el eyebrow debe nombrar el servicio, no solo el tipo de documento
Instrucción explícita del usuario: en la Portada, donde antes solo decía el tipo de documento
genérico ("Propuesta formativa · Capacitación in-company"), ahora debe mencionar el/los
servicio(s) reales de `brief.md → servicio` — "Servicio de Habilidades", o "Servicio de
Detección y Habilidades" si son 2 cotizados juntos. Nueva regla bloqueante: `CLAUDE.md §4.1a`
punto 4 + detalle y ejemplos por servicio en `plantillas/propuesta-comercial.md` → *Reglas de
copy*. Aplica a toda propuesta nueva o regenerada de aquí en adelante, no retroactivo. Caso
base aplicado ya: Simple TV CAI-002 ("Capacitación in-company" → "Servicio de Habilidades").

---

## 2026-08-30 — [plantilla] Brief de Kickoff: 2do rediseño — archivo HTML local, no Artifact
Segundo rechazo del formato del Brief de Kickoff (1er rechazo: 2026-08-26, deck PDF → Artifact
interactivo). El usuario aportó un ejemplo completo propio ("Ejemplo Gato") y aclaró que ya
existe una familia de **artefactos comerciales** (Ficha Comercial, Resumen modelo, Ruta del
servicio — no viven en este repo) con un patrón resuelto: **archivo HTML local** abierto con
`file://` (no un Artifact publicado en claude.ai), con casillas de fecha/hora reales por
sesión, botón "Agendar todo" que genera un `.ics` (JS puro, sin backend) para importar a
`servicio@intezia.com`, botón "Generar PDF" que arma un `#print-view` oculto y dispara
`window.print()`, y un toggle "Modo interno/cliente" que oculta las instrucciones del
consultor antes de compartir pantalla. Paleta y tipografía propias, distintas de la oficial
de propuesta (nueva: `empresa/marca-artefactos.md` — fondo `#0A0A0A`, dorado `#F4BA1A`,
naranja `#E58423`, crema `#F5EFE0`, dim `#9a948a`, Poppins + Space Grotesk vía Google Fonts,
válido porque es local y no tiene el CSP de un Artifact). Se descartó por completo el enfoque
anterior: `scripts/kickoff-embed-logos.py`, el Artifact ya publicado de Puro Lomo CAP-101, y
la sección de objetivos (se omite del todo, no solo se abrevia). Nuevo activo:
`logos/intezia/{BLANCO,NEGRO}.png` (logo genérico sin división, renombrado desde archivos que
el usuario ya había preparado). Spec reescrita: `plantillas/brief-kickoff.md`, con tabla de
las 4 rutas reales por servicio (Detección/Habilidades/Políticas/Innovación) dictada por el
usuario — solo Habilidades tiene piloto construido (canónico en
`plantillas/kickoff-canonico/kickoff.html`, cliente demo "Gato"); los otros 3 quedan "sin
piloto, construir caso por caso" (mismo criterio que sus decks de propuesta). Se mantiene la
regla bloqueante de confirmar aprobación de la propuesta antes de generar (no se genera junto
con la propuesta por defecto, a pesar de que el usuario lo insinuó al inicio — confirmado
explícitamente que sigue siendo un paso aparte). Caso base regenerado: CAP-101 Puro Lomo,
respetando que su propuesta específica (2026-08-11) no incluye EduTrace/dashboard/seguimiento
30-60-90 aunque el modelo Habilidades estándar sí los tenga — se muestran solo los
entregables realmente vendidos.
**Lección para el futuro**: "herramienta que se llena en vivo" no implica automáticamente
"Artifact de claude.ai" — antes de elegir la plataforma de publicación, preguntar si ya existe
un patrón local establecido. Ver `[[artifact-vs-pdf-para-vivo]]` en memoria.

## 2026-08-30 — [regla] Capacitación In-Company cambia de código: CAP- → CAI-
Instrucción directa del usuario: "ya no se harán CAP in company para servicios nuevos...
sigue con CAI... de ahora en adelante será así a menos que yo te indique lo contrario".
`CAI-001..003` ya existían como código ad-hoc (Cavedatos, Simple TV x2); desde `CAI-004`
(Yoyokids) es la serie oficial de Capacitación In-Company, reemplazando `CAP-`. Taller
sigue siendo `TA-` (sin cambios). No retroactivo: las ~114 propuestas `CAP-###` existentes
se quedan como están. Actualizado en `empresa/catalogo.md`, `empresa/tipos-de-documento.md
§1`, `plantillas/diseno-taller-capacitacion.md`, `CLAUDE.md §2/§4.12`.

---

## 2026-08-30 — [cliente:zoom-innovacion] INN-001 primer piloto del servicio Innovación
Zoom pidió un plan de acompañamiento continuo (sesiones mensuales que se definen mes a mes
según objetivos reales, no un programa cerrado) con cotización a 3/6/12 meses y beneficio
creciente por permanencia. Servicio Innovación estaba "Pendiente" desde
`empresa/tipos-de-documento.md §0` (2026-08-26): sin piloto, sin estructura de deck, sin
mecánica de precio. Resuelto con `clientes/propuestas/zoom-innovacion/`:
- **Roadmap del ciclo mensual**: se portó el componente `.rmx-linear` (single-track, de
  `grupo-osorio/`) a un clon con `_base` + `overrides.css`, adaptando el 4º nodo de "★
  resultado final" a "↻ se repite" — 3 etapas (Kick-off/Ejecución/Medición) + tarjeta de
  cierre que explica la lógica cíclica, más `.rmx-ethics` para la metodología ("planificación
  viva, no temario cerrado"). Primer overflow (+105px) vino de un h2 forzado a 2 líneas y un
  párrafo de metodología casi el doble de largo que el original portado; se resolvió
  acortando contenido, no el CSS.
- **Cotización nueva "Inversión por Permanencia"**: variante de `agregar-campo-precio.py`
  (`CICLO_PRICE_FIELDS`) con 3 columnas de duración (3/6/12 meses), cada una con
  `Cuota{N}m` + `Descuento{N}m` editables, sin auto-cálculo entre columnas. La 12m se
  resalta como "mayor beneficio". Todo el layout de esta variante usa `position:absolute`
  explícito por elemento (no flujo de documento) — un primer intento con `position:relative`
  habría desalineado el `/Rect` real del PDF respecto a la caja visible en CSS, además de
  colisionar el badge con el texto explicativo de arriba.
- Beneficios v3 y Cierre escalera reusados sin cambios de diseño (solo copy) desde el
  patrón `simple-tv-cai002/`.
- Documentación actualizada en cascada: `CLAUDE.md §4.1a`, `empresa/tipos-de-documento.md
  §0`, `plantillas/propuesta-comercial.md` (tabla Propuesta Económica por servicio),
  `plantillas/generar-pdf.md` (nueva variante documentada).

---

## 2026-08-28 — [cliente:dusa] CH-007 reconvertida de Claude/autonomía a Copilot/optimización de procesos
Nueva ficha de requerimientos de DUSA (`Ficha de requerimientos DUSA.csv`) + precisiones
directas: 30 participantes, 90 min, Copilot cuenta gratuita, práctica, en Word/Excel/
PowerPoint, eje = optimizar procesos interdepartamentales (no autonomía de líderes de
Comercial/Finanzas como la versión original). Se conservó el código `CH-007`, el título de
marca "La Próxima Destilación" (la metáfora de destilar un proceso sigue aplicando) y la
estructura de 9 slides ya establecida (sin `.s-orange`, sin `.s-price`, con `.s-impact`).
Se reescribió contenido completo: Portada, Diagnóstico (de la ficha), Objetivos, Programa (4
módulos: Proceso/Word/Excel/PowerPoint, 15+25+30+20=90 min), Cronograma, Beneficios,
hook de Impacto (ya no menciona Comercial/Finanzas), Próximos pasos, Cierre. Confirmado con
`dusa-cap088` que el ecosistema real de DUSA es Copilot (Claude solo como apoyo puntual) — el
cambio de herramienta encaja mejor con el resto de propuestas de este cliente, no es un
capricho aislado. Overflow de +15px en el Cronograma por texto nuevo demasiado largo,
resuelto acortando copy en 2 rondas hasta 0px.

## 2026-08-28 — [bug][cliente:corporaciones-easyaccess] Cierre escalera: texto fantasma si falta la regla @media print
Al retrofitear CAP-107 con el Cierre escalera (`.end-summit`/`.stair-field`, primer deck que
pasa de Cierre viejo→escalera dentro de esta sesión, a diferencia de Cavedatos/Go Pharma que
ya nacieron con escalera), apareció texto doblado/fantasma en toda la slide: el texto demo de
`.acro-default-text` se veía duplicado, ligeramente desplazado. Causa: la regla `@media print`
que oculta `.acro-default-text` antes de que Chrome hornee el HTML a PDF (para que solo quede
visible el texto que el AcroForm hornea después) solo cubría `.acro-area`/`.acro-bullet` — las
clases nuevas `.end-summit`/`.stair-field` no estaban en esa lista, así que Chrome baked el
texto demo como contenido normal de página, y el widget agregado después por el
customize-<slug>.py se dibujó encima. **Fix**: agregar toda clase contenedora nueva de un
campo AcroForm horneado a la regla `@media print { ... .acro-default-text { display:none } }`
existente — no asumir que el nombre de clase no importa. Aplica a cualquier deck que agregue
Cierre escalera por primera vez (los que ya nacieron con ella, como Cavedatos/Go Pharma, la
tienen bien desde el HTML original).

## 2026-08-28 — [cliente:corporaciones-easyaccess] CAP-107 corregido: Intezia no desarrolla software
Corrección sobre la actualización de contenido del mismo día (ver entrada siguiente): esa
primera pasada mantenía Etapa 2 "Construcción guiada" y Etapa 3 "Implementación" prometiendo
que Intezia construía el CRM y el motor de cotizaciones junto al equipo de tecnología del
cliente, cotizadas de forma progresiva. Instrucción del usuario: *"no vas a mencionar que
vamos a construir el crm ni nada por el estilo... el objetivo principal no puede ser
desarrollo porque nosotros para este momento no desarrollamos."* Se reescribió el deck entero
a un servicio de Detección de **fase única**, 4 etapas IADD (Iniciación, Auditoría,
Diagnóstico, Diseño) — mismo framework que `embutidos-zeus/` (DET-003), sin la parte de
sesiones por departamento porque aquí es un solo equipo. El bot y la cotización manual quedan
solo como cuellos de botella diagnosticados, nunca como algo que Intezia construye; el
entregable insignia pasa de "CRM construido" a "Reporte Final con hoja de ruta priorizada".
**Bug encontrado de nuevo**: la caja AcroForm de Entregables (angosta, ≈27 chars/línea) se
desbordó con 5 destacados largos — el detector automático no la cacha (es un campo AcroForm
horneado, no HTML), hay que revisar visualmente. Se resolvió acortando a 4 ítems concisos
(mismo patrón que Zeus). Ver memoria `bug-entregables-acroform-box-narrow`.

## 2026-08-28 — [bug][scripts] Orden del par customize con script propio: rebake_dark SIEMPRE al final
Al regenerar embutidos-zeus/DET-003, corrí `customize-<slug>.py` (rebake oscuro v3 de
Beneficios) ANTES de `customize-acroforms.py`. `customize-acroforms.py` llama a
`rebake_bold_fields()` (`acroform_appearance.py`), que re-hornea Entregables/Acreditación con
fondo blanco/texto negro por defecto (no tiene entrada en `FIELD_COLORS` para esos dos campos)
— pisó el fondo oscuro y el layout ampliado que el script propio acababa de hornear. Fix:
volví a correr `customize-<slug>.py` al final y quedó correcto (lee `/Rect` y `/DA` ya
existentes en el PDF, no valores por defecto). **Regla:** el orden documentado en §10 CLAUDE.md
(`generar-pdf.sh → customize-acroforms.py → customize-<slug>.py`) no es solo convención — invertirlo
rompe visualmente cualquier campo que el script propio pinte con colores no-default (Beneficios
v3 oscuro, Cierre escalera). Los campos con entrada en `FIELD_COLORS` (Cierre) sobreviven el
orden invertido porque `acroform_appearance.py` los conoce; los que NO tienen entrada ahí
(Entregables/Acreditación en su variante oscura) no.

## 2026-08-28 — [cliente:corporaciones-easyaccess] CAP-107 actualizado a Detección (contenido, sin retrofit visual)
Reunión de seguimiento trajo detalle nuevo (bot VirtualScape → handoff manual, cotización en
Google Sheets, complejidad multi-proveedor nacional/importado, necesidades de CRM+motor de
cotizaciones). Se mantuvo el código `CAP-107` (nomenclatura vieja) pero se fijó
`servicio: "deteccion"` en `meta.json` — primer caso de código `CAP-` con servicio Detección,
documentado como excepción deliberada. Contenido reescrito en brief.md/programa.md/index.html
(Descubrimiento → Detección en las 12 slides, título-eco "Excel manual" → "cotizar a mano");
overflow de +19px (Diagnóstico) y +37px (Roadmap) por texto nuevo demasiado largo, resuelto
acortando copy, no tocando CSS. **A propósito NO se tocó**: Metodología ABR, Equipo facilitador,
Beneficios formato viejo, Cierre con Calendly — ese retrofit visual no se pidió para este deck
(a diferencia de Cavedatos/Go Pharma/Amcor, donde sí se pidió explícitamente).

## 2026-08-28 — [cliente:go-pharma,amcor] Retrofit Beneficios v3 (layout ampliado) completado en los 3 pendientes
Mismo pedido que Cavedatos (ver entrada anterior), esta vez para Go Pharma CAP-030 y Amcor
DET-001 — **con esto se cierran los 3 decks que quedaban en v2** desde que se creó v3
(2026-08-28). Ambos usan hoja de estilos local completa (no `_base`+`overrides.css`), así que
el bloque `.s-benefits-v2` se reemplazó directo en `styles.css` de cada uno (mismo bloque
exacto que Cavedatos/CAI-002/etc., verificado que ambos comparten los mismos valores base de
`.s-benefits` — padding 56/56/80, h2 32px/1.05/22margin — antes de aplicar el cálculo de
posición de las cajas AcroForm). `customize-go-pharma-cap030.py` y `customize-amcor.py` ya
tenían lógica propia (recorte de fases de precio a 2/1) — se les agregó `rebake_dark()` +
`BENEFICIOS_LAYOUT` como un paso más del mismo script, sin tocarles la lógica existente.
Sin cambios de contenido ni horas en ninguno de los 2, solo el bullet `•` en
Entregables/Acreditacion (parte del look v3) y el aspecto visual de la slide.

## 2026-08-28 — [cliente:cavedatos] Retrofit Beneficios v3 (layout ampliado) — solo aspecto, sin tocar contenido
El usuario pidió actualizar Cavedatos CAI-001 al estándar visual vigente (mismo que
CAI-002/CAI-003/DET-002/DET-003/ALL-001), explícito en que **no se toca contenido ni horas**,
solo el aspecto. Cavedatos era el único deck de los "3 pendientes" (Cavedatos/Go Pharma/Amcor)
que se retroaplicó hasta ahora — Go Pharma CAP-030 y Amcor DET-001 siguen en v2, sin pedido
todavía. Cambios aplicados: `overrides.css` (grid v2 de 240px → v3 ampliado de 570px, 2
tarjetas blancas → 4 oscuras), `customize-cavedatos.py` (nuevo `rebake_dark()` +
`BENEFICIOS_LAYOUT`, mismo patrón que los demás decks), `acroforms.json` (bullet `•` agregado
al inicio de cada línea de Entregables/Acreditacion — es parte del look de checklist v3, no
un cambio de redacción, la única edición de texto permitida bajo "solo aspecto"). HTML sin
tocar: la estructura de bloques (`.grid` con 4 `.block`, labels) ya era idéntica entre v2 y
v3, el cambio vive enteramente en CSS + AcroForm.

## 2026-08-28 — [regla] Beneficios v3 "layout ampliado" — ahora estándar, corrección de una imprecisión documental
El usuario pidió en CAI-002 que la slide de Beneficios usara letra más grande y todo el
espacio disponible (el v3 original, grid de 250px, dejaba ~300px de negro vacío debajo de
las 4 tarjetas). Fix aplicado: grid a 570px, padding/tipografía ampliados, cajas AcroForm
(Entregables/Acreditacion) agrandadas de 158×117pt a 145×355pt con fuente de 10 a 13pt (vía
un nuevo parámetro `layout` en `rebake_dark()` que también reescribe el `/Rect` real del
campo, no solo la apariencia horneada — si no, el visor escala el `/AP` al rect chico
original y el texto sale distorsionado). **Primer intento centraba verticalmente el
contenido de las 2 tarjetas de texto (Resultados / Por qué [Servicio]) y eso produjo un
desnivel visible: cada tarjeta tiene distinto largo de texto, así que cada una centraba a una
altura distinta.** Fix final: sin centrado, los 4 bloques arrancan en el mismo `padding-top`.
El usuario declaró esto **estándar para toda propuesta de aquí en adelante** y pidió
retroaplicarlo a DET-002 de inmediato — documentado en `plantillas/propuesta-comercial.md`
(sección "Layout ampliado") con los valores exactos, para que cualquier deck nuevo nazca así.
**Retrofit pendiente** (no se ha pedido aún): Cavedatos CAI-001, Go Pharma CAP-030, Amcor
DET-001 — los 3 siguen en v2 (ni siquiera v3), ver nota de abajo.
**Corrección de una imprecisión encontrada de paso**: `propuesta-comercial.md` afirmaba que
v3 se había "propagado el mismo día [2026-08-28] a Cavedatos CAI-001, Go Pharma CAP-030 y
Amcor DET-001" — **eso nunca pasó** (verificado por grep: los 3 siguen con el CSS de v2, 2
tarjetas blancas). La confusión probablemente viene de que **v2 sí** se había propagado a
esos 3 decks el día anterior (2026-08-27) — quedó anotado y corregido en el archivo.

## 2026-08-28 — [cliente:simple-tv-det002] DET-002 · horas confirmadas (8h Detección + 16h Habilidades = 24h)
Ajuste post-entrega: el usuario definió las horas exactas de las 2 fases. **Fase 1 ·
Detección = 8h**: 4 sesiones individuales de 2h, una por cada IA Champion (no una auditoría
grupal). **Fase 2 · Habilidades = 16h**: 2 módulos (Copilot Avanzado + Prompting Ampliado) ×
4 sesiones de 2h cada uno — mismo total y misma unidad de sesión (2h) que CAI-002, aplicado a
2 módulos en vez de 4 porque DET-002 no necesita el módulo de Fundamentos (ya lo cubre la
Detección) ni el Marco de Estrategia (exclusivo de CAI-002). La Fase 2 pasó de 1 slide de
cronograma a 2 (una por módulo) para no cramear 8 sesiones en un solo timebar — mismo
criterio de densidad visual que ya se usó en CAI-002 al mostrar 4 sesiones por slide. El
deck pasó de 12 a 13 slides. Reemplaza el lenguaje vago anterior ("sesiones con cada
Champion", "contenido a definir tras el diagnóstico") en el deck, `brief.md` y `programa.md`.

## 2026-08-28 — [arquitectura] Servicio "integral" (5to valor) — plan de los 4 servicios en uno
Primer caso de un cliente pidiendo **los 4 servicios del Modelo Intezia como un solo plan
estratégico secuencial** (Simple TV ALL-001: Detección → Habilidades → Políticas →
Innovación). Ninguno de los 4 valores existentes de `servicio` encajaba (no es un combo
parcial de 2 como DET-002), así que **se confirmó con el usuario** (no se asumió) agregar
`integral` como 5to valor — documentado en `CLAUDE.md §4.1b` y `empresa/tipos-de-documento.md
§0`. Código `ALL-001`, asignado por el usuario (nomenclatura nueva, sin heredar prefijo de
ningún servicio individual).
**Decisión de alcance clave**: un deck `integral` **no resuelve** las plantillas pendientes de
Políticas ni Innovación (siguen "sin piloto canónico propio") — representa esas 2 fases al
nivel de **resumen de roadmap** (1 tarjeta de etapa + 1 de resultado, con el contenido que el
sistema ya tiene escrito en `tipos-de-documento.md §0`/`catalogo.md`: Manual de políticas /
Brújula IA / Matriz de riesgos para Políticas; cadencia mensual + evaluación continua para
Innovación), no con una plantilla dedicada nueva. Eso sigue pendiente si algún cliente
contrata Políticas o Innovación por separado.
**Hallazgo técnico útil**: extender el roadmap `.rmx-linear` (`clientes/propuestas/aerocentro/`,
declarado estándar 2026-08-07) de 3 a 4 fases **no requirió ningún cambio de CSS** — el grid
ya es flexible por número de columnas (`.rmx-lcol { flex: 1 }`), así que agregar una 4ta
página de roadmap fue solo agregar HTML siguiendo el mismo patrón (nodos E-numerados de forma
corrida, tarjeta de etapa + tarjeta de resultado). Fases de una sola etapa (Políticas,
Innovación) usan el layout de 2 columnas que aerocentro ya usaba para su propia Fase 3, en vez
del de 3 columnas de las fases con 2 etapas.
**Retrofit aplicado al clonar aerocentro** (más nuevo que aerocentro pero anterior a este
deck): Beneficios v3, cierre escalera, sin Metodología ABR — incluyendo la barra `.rmx-ethics`
("Metodología de retos...") que vive DENTRO de cada slide de roadmap, no solo la slide
dedicada `.s-orange` (§4.10a aplica igual a ambos lugares, aunque el texto oficial de la regla
solo mencionaba la slide completa).

## 2026-08-28 — [bug] Overflow dentro del /AP horneado del Cierre, invisible al detector HTML
`node scripts/verificar-overflow.js` renderiza el **HTML/CSS** del deck — nunca ve el texto
final que vive dentro del **/AP horneado** de un AcroForm (`acroform_appearance._make_appearance`
usa sus propias tablas de ancho de fuente, un layout distinto al de Chrome). En CAI-003
(Simple TV), el texto de `CierrePaso1` ("Diagnóstico y fundamentos por área", 35 caracteres)
pasó el detector limpio, pero en el PDF final la caja más chica de la escalera (`.stair-1`,
altura 50px) lo envolvió en **3 líneas** en vez de 2 y la última se cortó — visible solo en
la revisión manual página por página (§4.10, "el script terminando sin error no equivale a
PDF correcto"). Fix: acortar a "Diagnóstico por área" (21 caracteres). **Regla práctica**:
`CierrePaso1` (la caja más chica de las 3) se mantiene ≤ ~25 caracteres; `CierrePaso2`/`3`
toleran más (cajas de 100px/150px) pero igual se revisan a ojo tras cada regeneración — este
tipo de desborde solo aparece en el PDF horneado, nunca en el HTML.

## 2026-08-28 — [cliente:simple-tv-cai003] CAI-003 · Rollout organizacional (14 áreas, Habilidades con Detección integrada)
Tercera propuesta de la cuenta Simple TV (después de DET-002 y CAI-002, ambas para el piloto
"IA Champions" de 4 personas): esta escala a **las 14 áreas de la organización (~260
personas)**. Diseño validado por el cliente en la llamada: **un bloque integrado por área**
(2h de Detección fija + 8-12h de Habilidades, fundamentos comunes + quick wins propios en el
mismo bloque) — **sin separar en fases** como hacía la vieja CAP-035. La comparación contra
CAP-035 es la razón de diseño, pero **no se menciona en el deck de cara al cliente** (mismo
criterio que ya aplicó en DET-002 con "no comparar contra el alcance de CAP-035").
**Código `CAI-` y no `DET-`** pese a incluir Detección: la Detección aquí es una sesión fija
subordinada dentro de un bloque de Habilidades, no una fase separada cotizable — decisión
explícita del usuario al asignar el código, documentada en `brief.md` para que quede el
razonamiento por escrito.
**Slide nueva, no existe en los decks hermanos**: "Cobertura organizacional" —
componente `.s-coverage` (grid CSS, no flexbox, de las 14 áreas + cifra de personas),
reusando gratis el header negro/eyebrow/h2/meta de `.s-program` vía clases combinadas
(`class="slide s-program s-coverage"`). CSS Grid en vez de flex-wrap es lo que evita que
nombres de área de longitud muy distinta ("IT" vs "Riesgo, Auditoría Interna, Cumplimiento y
Seguridad") desalineen filas — la fila entera se empareja a la altura del ítem más alto.
Ver [[roadmap-fork-reusado-como-punto-de-entrada]] para el patrón hermano de reusar CSS de
una sección para un propósito nuevo.

---

## 2026-08-28 — [cliente:simple-tv-det002] DET-002 · IA Champions (Detección + Habilidades combo)
Segunda propuesta de Detección del sistema, primera que combina Detección + Habilidades para
un **grupo piloto pequeño** (4 "IA Champions": RR.HH. + Calidad y Procesos), no toda la
empresa. Sin Ficha Comercial (instrucción directa + minuta de llamada). Vive en carpeta propia
`simple-tv-det002/` — el cliente ya tenía `simple-tv/` con CAP-035 (mayo 2026, alcance
distinto: fundamentos para toda la empresa); **nunca se usa una propuesta vieja del mismo
cliente como guía de contenido**, solo como referencia de identidad/sector, y si el alcance es
otro, va en carpeta nueva. Argumento de valor explícito: productividad **por persona en equipo
chico**, no volumen — criterio real que usó el cliente para elegir a los Champions, no
jerarquía. La slide de Fase 1 y Beneficios dejan explícito **qué aporta la auditoría de
Intezia que el diagnóstico interno del cliente no cubre** (tabla comparativa en `programa.md`)
— importante cuando el cliente evalúa "hacerlo con su propio diagnóstico" en vez de contratar
Detección. **Fuera de alcance por ahora**: variante "solo Habilidades, con diagnóstico propio
del cliente" — mencionada por el cliente pero no solicitada explícitamente; documentada como
pendiente en el brief, no construida (habría ido bajo código `CAI-00X`, servicio
`habilidades`, no como parte de este DET-002).

**Beneficios v3** (reemplaza v2 del día anterior): el usuario señaló que v2 "solo le cambió el
color" y pidió algo más impactante, mostrando como referencia una slide de roadmap
(`.rmx-card`/`.rmx-result-card`: pill-tag, borde superior de acento, glow, checklist). v3
reusa esa misma DNA visual para Beneficios: las 4 tarjetas quedan oscuras con pill-tag y borde
de acento (antes 2 de las 4 eran blancas). Las cajas AcroForm de Entregables/Valor inmediato
se re-hornean con fondo oscuro y texto blanco **en el `customize-<slug>.py` del deck**,
importando `_make_appearance`/`_WIDTHS_BOLD` directo de `acroform_appearance.py` (no se toca
`FIELD_COLORS` global — eso rompería el fondo blanco por defecto de esos mismos nombres de
campo en las ~80 propuestas restantes). El "checklist" de las cajas horneadas es texto real
con bullet `•` tipeado en el `/V` (carácter válido en WinAnsiEncoding) — un `::before` de CSS
no existe dentro de un campo de formulario horneado.

**Bug nuevo, sistémico, corregido en las 4 propuestas activas**: `<strong>` dentro de
`.s-goals .general p` (el párrafo de Objetivo general) genera una línea tipo tachado sobre el
texto envuelto, en Chrome headless — el `.general p` ya es `font-weight:700` de por sí, así
que el `<strong>` es semánticamente redundante *y* dispara el glitch visual. Fix: quitar el
`<strong>` en ese párrafo específico (sin pérdida de énfasis, ya que todo el párrafo es bold).
Corregido en simple-tv-det002, go-pharma, amcor y cavedatos. **No corregido** en los canónicos
ni en las ~80 propuestas legacy (no se tocan retroactivamente) — el patrón viene de
`aerocentro`/`ioed`, así que cualquier deck de ese linaje puede tenerlo latente; revisar si se
vuelve a tocar esa slide.

## 2026-08-27 — [regla] Beneficios v2 (estándar único, todos los servicios) + correo de cierre
Dos ajustes de pulido, aplicados a **todas las propuestas de aquí en adelante** (y
retroactivamente a las 3 vigentes bajo el esquema nuevo: Cavedatos, Go Pharma, Amcor):

1. **Hoja de Beneficios unificada**: reemplaza el viejo "Perfil de egreso / Beneficio del
   programa / Entregables / Acreditación" (incluso para Habilidades, que antes lo conservaba)
   por **Resultados · Por qué [Servicio] · Entregables · Valor inmediato**. El campo AcroForm
   `Acreditacion` se repurpone como "Valor inmediato" en todos los servicios (nombre de campo
   conservado por compatibilidad con `agregar-campo-precio.py`).
2. **Rediseño visual obligatorio**: la slide pasa de cuadros blancos serios a **fondo negro
   con tarjetas** — 2 tarjetas oscuras con acento amarillo (Resultados, Por qué [Servicio],
   con `border-radius` y sombra, estilo roadmap/impacto) + 2 tarjetas blancas (Entregables,
   Valor inmediato, donde vive el AcroForm horneado). Clase `.s-benefits-v2` en el
   `<section>`; CSS en `overrides.css` (clones mono-fase con `_base`) o directo en el
   `styles.css` local (decks con hoja completa propia, tipo aerocentro/ioed/go-pharma/amcor).
   Logo del `.foot` pasa a BLANCO (fondo oscuro).
3. **Correo de cierre**: `servicio@intezia.com` reemplaza `info@intezia.com` en el bloque
   "Empresa" de `.end-contact`, en toda propuesta nueva.

Documentado en `plantillas/propuesta-comercial.md` (nueva sección "Beneficios — formato v2")
y `CLAUDE.md §4.10a`. Caso base: Cavedatos CAI-001; propagado el mismo día a Go Pharma
CAP-030 y Amcor DET-001 (sin tocar canónicos ni las ~80 propuestas legacy).

## 2026-08-27 — [regla] Sin foco legal en propuestas de Habilidades salvo pedido explícito
Cavedatos CAI-001 traía en su propuesta vieja un módulo entero de "Legalidad" (derechos de
autor, propiedad intelectual). El usuario pidió no mencionar la palabra "legalidad" ni
profundizar en el tema: es una propuesta de **Habilidades**, no de Políticas/gobierno — ese
enfoque le compete al servicio de Políticas del Modelo Intezia (Brújula IA, marco de 9
dimensiones), no a una capacitación práctica. Se retiró de diagnóstico, objetivos, programa
(módulo I renombrado "Prompting Técnico Avanzado"), cronograma y cierre. Aplica como criterio
general: no forzar contenido de otro servicio dentro de un deck de Habilidades salvo que el
cliente lo pida explícitamente.

## 2026-08-27 — [cliente:cavedatos] CAI-001 · primera propuesta de Habilidades (modelo nuevo, sin Ficha Comercial)
Primera propuesta con la nomenclatura nueva de Habilidades (**CAI-001**), re-emitiendo una
propuesta vieja de Cavedatos (CAP-002, «IA Generativa Avanzada para Equipos de Prensa») bajo
el modelo nuevo, **sin Ficha Comercial** (modalidad vieja: contenido del PDF viejo + input
del usuario). Servicio `habilidades`, división educacion, asesora Flavia. Base: clon de
**cumbre-andina/** (mono-fase canónico, enlaza `../_base/styles.css`) + **overrides.css**
local con el cierre escalera (que _base aún no trae; se carga después de _base). Cambios del
esquema nuevo aplicados sobre la propuesta vieja: se retiró la slide de Metodología ABR y el
bloque de Equipo facilitador (§4.10a); próximos pasos sin «firmamos acuerdo/factura 50%»
(§4.15); cierre escalera; 30 días + T&C (sin «7 días / pago en Bs / anticipo»). Habilidades
**sí conserva** Perfil de egreso + Acreditación en Beneficios (a diferencia de Detección).
Contenido: 4 módulos del viejo reagrupados en **2 sesiones de 5h**; quick wins nuevos (Avatar
interno, presentaciones Canva ágiles, flyers/audiovisuales ágiles) en Entregables; Gemini +
stack (Canva, CapCut, Luma Labs, Freepik, Envato). Impacto §4.9: MIT (Noy & Zhang, Science
2023, −40% tiempo de redacción), Canva Visual Economy Report 2024 (−70% diseño), McKinsey
State of AI 2024 (65% adopción). `customize-cavedatos.py` solo agrega el cierre (precio
estándar, sin fases). **Nota infra**: el detector `verificar-overflow.js` falló por el Chrome
abierto del usuario (puerto de depuración); la verificación §4.10 se hizo por revisión visual
del PDF. Bug corregido en revisión: el `lead` de portada a 4 líneas se solapaba con la línea
de código; se acortó a 3.

## 2026-08-26 — [cliente:amcor] DET-001 · primera propuesta de Detección (modelo nuevo, desde Ficha Comercial)
Primera propuesta del sistema bajo el eje Servicio y primera nacida de una **Ficha Comercial
Intezia** (Amcor Rigid Packaging, área de Compras, asesora Flavia Martínez). Servicio
`deteccion`, código nuevo `DET-001`. Estructura: Fase 1 · Detección + nivelación básica de
Copilot en paralelo (ÚNICO cotizado) → Fase 2 · Habilidades (contemplada, cotizada tras el
diagnóstico, patrón aerocentro). Clonada de `go-pharma/` (esquema nuevo). Decisiones clave:
solo Copilot dentro del entorno Microsoft 365 (§4.11, no se afirma migración; no se menciona
Claude porque el cliente debe validarlo; no se expone SAAP ni ODOO). Beneficios por servicio
Detección: sin Perfil de egreso ni Acreditación; las 2 cajas AcroForm se repurposan como
"Entregables del diagnóstico" (`Entregables`) y "Valor inmediato" (`Acreditacion`, nombre de
campo conservado por compatibilidad). Hoja "Inversión por fases" con **solo Fase 1** cotizable
(`customize-amcor.py` quita PrecioFase2/3 y recalcula PrecioBase a 1 fase, + agrega cierre
escalera). Impacto §4.9: McKinsey *Transforming procurement for an AI-driven world* (compras
+25-40%, selección de proveedores +30%) y Microsoft *Work Trend Index 2024* (77% más
productivos, 29% más rápidos). **Bug evitado**: el h2 de Beneficios DEBE contener el marcador
"Lo que se llevan" (plural) o `agregar-campo-precio.py` no inyecta Entregables/Acreditacion
(un "Lo que se lleva" singular rompió la primera pasada).

## 2026-08-26 — [arquitectura] Servicio como eje primario (Modelo Intezia de 4 servicios)
Se sumó el eje **Servicio** (Detección · Habilidades · Políticas · Innovación) como campo
bloqueante paralelo a División, más la bandera `alianza` aparte. Origen: `MODELO MAESTRO DE
SERVICIO` + `Manual de la Ficha Comercial Intezia` (Dirección de Productos y Servicios, ago
2026). Cambios: `CLAUDE.md` (identidad, §4.1a nueva con tabla servicio→patrón, Paso 0 clona
por "mismo servicio+tipo+división", tabla de delegación, brief referencia la Ficha Comercial,
§4.19/4.20 trackean `servicio`/`alianza`), `empresa/tipos-de-documento.md` (§0 Servicio, las
3 categorías curriculares quedan anidadas dentro de Habilidades), `empresa/catalogo.md`
(reorganizado por servicio). Habilidades = estructura de siempre; Detección clona de
`pilotes-perforados/`; Políticas e Innovación **pendientes de decisión de formato** (Ivana +
David). Convivencia intacta: la modalidad vieja (charla/taller/curso/diplomado sin Ficha
Comercial) sigue igual. Pendiente de código: `scripts/indexar.py` todavía no agrupa por
`servicio`. Backfill retroactivo: no (legacy queda sin servicio, mismo criterio §4.19).

## 2026-08-26 — [regla] §4.10a Sin Metodología ABR ni Equipo facilitador en el deck
La slide de Metodología ABR (`.s-orange`) y el bloque de Equipo facilitador (`.team` en
`.s-benefits`) **no se muestran al cliente** en propuestas nuevas/regeneradas. Razón: ventas
ya cubre la metodología en el Levantamiento y tenía un enfoque demasiado académico para una
propuesta de negocio. No retroactivo (canónicos y entregadas no se tocan; al clonar, retirar
a mano). Beneficios por servicio: Habilidades conserva Perfil de egreso + Acreditación; los
demás servicios los omiten y refuerzan el paquete de entregables. Caso base: Go Pharma CAP-030.

## 2026-08-26 — [plantilla+scripts] Cierre tipo ruta/escalera editable + logo Intezia nuevo
Nuevo cierre (`.s-end`): cinta de Resultado + 3 escalones ascendentes, 4 cajas AcroForm
editables (`CierreResultado`, `CierrePaso1..3`), CTA sin link. Metáfora genérica de "pasos al
éxito", sin mencionar los 4 servicios. Las 4 cajas se agregan en el `customize-<slug>.py`
(no en `agregar-campo-precio.py`) y se hornean con color de fondo por escalón vía
`acroform_appearance.FIELD_COLORS` (nuevo: soporte de `bg_rgb`/`text_rgb` en el /AP). Logo:
`logos/educacion/{BLANCO,NEGRO}.png` reemplazados por el wordmark "INTEZIA" (sin "EDUCATION");
respaldo en `logos/educacion/_anterior/`. Fundación sin tocar. Caso base: Go Pharma CAP-030.
Pendiente: propagar el cierre a los canónicos y mover su AcroForm a `agregar-campo-precio.py`.

## 2026-08-26 — [preferencia] Brief de Kickoff: Artifact interactivo, no PDF/deck de propuesta
La primera versión del Brief de Kickoff (mismo día, ver entrada siguiente) se generó como un
deck A4 landscape con el mismo lenguaje visual que una propuesta comercial (11 slides, PDF vía
Chrome headless). El usuario la rechazó explícitamente: *"no me gustó generarla como propuesta,
la idea es que se pueda ir rellenando de forma interactiva."* Rediseño completo: el brief ahora
es una página web (Artifact) de scroll único. Reglas fijadas tras 3 preguntas de alcance:
(1) **solo Logística y Cómo arrancamos son campos en vivo** — objetivos y etapas los sigue
redactando IDIA de antemano y quedan fijos; (2) **el Artifact reemplaza al PDF por completo**,
no se genera un PDF de este documento; (3) **sin persistencia entre sesiones** — se llena
durante la llamada y un resumen de texto autogenerado se copia a mano al `brief.md` al cerrar.
Se descartaron `scripts/generar-brief.sh` y el PDF/CSS de la versión anterior. Nuevo activo:
`scripts/kickoff-embed-logos.py` (los Artifacts no acceden al filesystem del repo — los logos
se embeben como data URI antes de publicar). Canónico reescrito en
`plantillas/kickoff-canonico/kickoff.html` (autocontenido, sin CSS/PDF aparte). Caso base:
CAP-101 Puro Lomo, primer brief real generado con este formato.
**Por qué importa para el futuro**: cuando un documento se usa EN VIVO frente al cliente para
acordar algo (no solo para presentar algo ya decidido), el formato correcto es una herramienta
que se llena, no un PDF que se lee.

## 2026-08-26 — [plantilla] Nuevo tipo de documento: Brief de Kickoff (hoja de ruta del servicio)
Segundo tipo de deck de cara al cliente, post-venta (paralelo a propuestas y dashboards).
Se presenta en el **kickoff** (primer encuentro del equipo de servicio con el cliente) y
muestra la **hoja de ruta por etapas**: qué se hace, con quién, cuántas sesiones y qué se
entrega en cada etapa (cada etapa responde a un objetivo específico de la propuesta). Origen:
reunión con Keiber (CPO) 2026-08-26. **Bloqueante**: IDIA debe confirmar con el usuario que la
propuesta está **aprobada** antes de generar el brief. En el kickoff **solo se cierra logística**
(fechas/ZH, grabación, acceso/participantes, agenda); nunca contenido/herramientas (ya vino del
levantamiento de ventas) ni economía (§4.15). Entregables nuevos: spec `plantillas/brief-kickoff.md`,
canónico autocontenido `plantillas/kickoff-canonico/` (11 slides, sin AcroForms, componente
roadmap lineal `.hr-*` con variante `.hr-build` para etapas Intezia-only), script
`scripts/generar-brief.sh` (render limpio, no toca `meta.json` ni el índice). Registrado en el
router `CLAUDE.md`: fila en §5, cruce en §6, mapa en §7 y flujo completo en el nuevo §12.

## 2026-08-25 — [bug] Placeholder visible también en AcroForm "Programa" (no solo "Notas")
`agregar-campo-precio.py` pre-carga **ambos** `Programa` y `Notas` con `/V` de placeholder
entre corchetes (`PROGRAMA_DEFAULT` / `NOTAS_DEFAULT`). El bug documentado en
`bug-notas-acroform-placeholder-visible` (2026-08-13) solo mencionaba `Notas`, pero
`Programa` tiene el mismo problema: si se omite la clave en `acroforms.json` pensando que
"queda vacío", el placeholder `[Nombre del programa formativo]` queda visible en el PDF.
**Cuando el apartado comercial (Programa/Notas) no aplica** (ej. propuestas sin fases,
como CAP-113 Daniela Chiesa), declarar `"Programa": ""` y `"Notas": ""` explícitos en
`acroforms.json` — omitir ambas claves, no solo una.

## 2026-08-19 — [cliente:good-latam] CAP-109 auditoría con 4 sesiones individuales (no pares)
Clon de `pilotes-perforados/` (Fase 1 auditoría cotizada + Fase 2 abierta), pero con **4
sesiones individuales de 2h** (una por departamento: Creación, Compras, Administración,
Digital) en vez de 2 sesiones combinadas — el cliente pidió explícitamente "una sesión con
cada área". El roadmap (`rmx-fork`/`rmx-routes`) sigue soportando solo 2 rutas visuales: se
agruparon las 4 sesiones en 2 bloques (A: Creación+Compras, B: Administración+Digital) solo
para el diagrama, mientras las 4 slides de cronograma detallan cada sesión por separado — no
forzar el componente a 4 rutas (arriesga desborde, no está diseñado para eso).
También: Mapa de Calor con **7 filas** (no 8) para evitar el desborde conocido de
pilotes-perforados (`capacidad-cajas.md`); y se agregó `.cot-progressive` + `.cot-terms-box`
a `styles.css` porque el pilotes-perforados original no los tenía (clon anterior al estándar
2026-08-13).

## 2026-08-17 — [cliente:zoom-comercial] CAP-058 ampliado a multi-track Ventas + Mercadeo
El deck original solo cubría Mercadeo. El cliente aclaró que el área Comercial de Zoom
también incluye Ventas (Cuentas Corporativas, Cuentas al Detal, Inteligencia Comercial), cada
equipo ve su formación por separado. Se aplicó el patrón multi-track de
`robin-agency-cap080/` duplicando Objetivos/Programa/Cronograma (2 slides c/u) por track,
mantendiendo Diagnóstico, Metodología, Beneficios, Impacto y Próximos pasos compartidos.
11→15 slides. Impacto sumó cifras reales de Salesforce State of Sales Report (7ª ed. 2026 y
6ª ed. 2024) junto a las de CoSchedule ya existentes (§4.9). `meta.json` pasó por
`En corrección` (el hook de `generar-pdf.sh` lo subió a `Enviada` de nuevo, sin tocar
`fecha_entrega` ya puesta — comportamiento esperado de §4.19).

## 2026-08-16 — [bug] `.cot-progressive` reintroducido en un clon de `fasto/` colisiona con `.cot-terms-box`
Caso: `corporaciones-easyaccess/` (CAP-107). `fasto/` es fase única cerrada (sin cotización
progresiva): su clon retiró el párrafo `.cot-progressive` del HTML, pero el `styles.css`
heredado subió `.cot-terms-box` a `top: 556px` a `top: 526px` para llenar el hueco, dejando
la regla `.cot-progressive` (top: 528px) como CSS muerto sin romper nada. Al clonar `fasto/`
para un proyecto que sí necesita cotización progresiva (patrón `aerocentro/`, Fase 1 cotizada
+ Fase 2-3 progresivas) y volver a escribir `<p class="cot-progressive">` en el HTML, el
párrafo reaparece exactamente encima de la caja "Importante", tapándola — colisión interna
que `verificar-overflow.js` no detecta (no es overflow de página). **Fix**: si se reintroduce
`.cot-progressive` en un clon derivado de `fasto/`, devolver `.cot-terms-box` a `top: 556px`
(el valor de `aerocentro/`, que sí lleva ambos elementos). Revisar visualmente la slide de
precio siempre que se mezcle contenido entre un clon "fase única" y uno "fase progresiva".

---

## 2026-08-13 — [bug] Caja `Notas` de `.s-price`: omitirla en `acroforms.json` deja el placeholder `[Condiciones de pago...]` visible en el PDF entregable
Caso: `luppro/` (CAP-103). `agregar-campo-precio.py` pre-carga el campo AcroForm `Notas`
con un `/V` real (no solo un hint visual): `"[Condiciones de pago: moneda, tasa, anticipo]" /
"[Cláusula legal de garantía / devolución]"` (`NOTAS_DEFAULT`). A diferencia de los campos
de precio (vacío intencional, sin texto) o de `Entregables`/`Acreditacion` (bloqueantes en
el checklist §10), `Notas` **no está en la tabla de campos mínimos de §4.14 ni en el
checklist §10**, así que el verificador automático no lo revisa — pero si la propuesta no
tiene un caso especial de Notas (como sí lo tenía `puro-lomo-bajo-auditoria/` con el
traslado del facilitador), omitir la clave del `acroforms.json` dejó ese placeholder entre
corchetes como texto real y visible en el PDF final, detectado solo al revisar visualmente
(§4.10 punto 1). **Fix**: cuando no hay caso especial, declarar explícitamente
`"Notas": ""` en `acroforms.json` para que `customize-acroforms.py` limpie el `/V` — no
basta con no incluir la clave. Relacionado con memoria `verificador-acroforms-economicos`
("Notas sigue vacío, NO se pre-llena con T&C") — el "vacío" ahí significa string vacío
explícito, no ausencia de la clave.

## 2026-08-13 — [cliente:fasto] CAP-104: roadmap de 3 etapas en 1 sola página (piloto de un solo equipo) + bug de fondo negro en `.s-program` heredado del canónico
Fasto (cadena de supermercados) pidió la solución directamente sobre un solo equipo
(Compras, 3 personas): a diferencia de `canguro/`/`aerocentro/` (varias fases, varios
departamentos, roadmap en 2-3 páginas), aquí las 3 etapas (Diagnóstico → Construcción →
Implementación) son un solo track sin fork. Se extendió `rmx-linear` con un **tercer nodo en
la misma página** (antes solo soportaba 2 nodos + resultado por página): `.rmx-node-f4` /
`.rmx-card-f4` en **blanco sobre negro** (Diagnóstico=amarillo f2, Construcción=blanco f4,
Implementación=naranja f3) — el fondo de `.s-roadmap` es negro, así que el 3er acento no
puede ser negro como en el patrón fork de `pago-tronic/` (ver `roadmap-3-etapas-flex-minheight`
en memoria); acá tocó blanco. `rmx-linear` es flex-column de alto automático (no el
`.rmx-journey` fijo del componente fork), así que agregar un 4to `.rmx-lcol` + arrow no
generó el bug de `min-height:0` — sin incidentes de overflow.

**Bug heredado encontrado**: la slide `.s-program` (Programa / "El camino") tiene el
`.meta` (línea bajo el h2) matemáticamente destinado a caer ~6px por debajo del banner
negro de 160px cuando el h2 ocupa 2 líneas (56 padding + eyebrow + h2 2L + meta ≈ 166px) —
**esto ya pasa en `canguro/` (CAP-100), ya "Enviada"**, no es exclusivo de este clon.
Corregido solo en `fasto/styles.css` (banner 160px → 178px, local, no toca `_base` ni otros
clientes). No se corrigió retroactivamente en `canguro/`/`aerocentro/` — si se retoma
alguno de esos decks, aplicar el mismo ajuste local.

**Recomendación Gemini+Claude, una sola vez**: el cliente ya tiene Workspace + Gemini Pro;
el deck menciona una sola vez (Etapa 2 · Construcción, en `.s-schedule`) que Gemini es buen
punto de partida pero se sugiere sumar Claude para el proceso reglado de punta a punta —
sin volver a comparar herramientas en el resto del deck, por instrucción explícita del
usuario ("no centres la propuesta en Gemini/Claude, enfócate en resolver el problema").
Al redactar esa línea se reprodujo el bug de `bug-strong-flex-specifics` (`<strong>` en un
`<li>` de `.s-schedule .ses-block` reordena el texto visualmente) — quitado el `<strong>`,
confirma que la memoria sigue vigente y aplica también fuera de `.s-goals .specifics`.

## 2026-08-13 — [bug][plantilla] Vigencia de cotización 7→30 días + bloque de términos y condiciones (estándar aerocentro, NO Notas)
El clon canónico mono-fase (`cumbre-andina/`) decía "Válido únicamente por 7 días en
divisas", contradiciendo `empresa/politicas-comerciales.md` (vigencia oficial = 30 días).
Corregido a "Cotización válida por 30 días." + agregado el bloque `.cot-terms-box` con link
a los términos y condiciones institucionales — el patrón que `aerocentro/`, `pago-tronic/`,
`pilotes-perforados/` (y 5+ decks más) ya usaban correctamente; el mono-fase era el único
linaje sin el bloque. CSS agregado a `_base/styles.css` para que todo clon de
`cumbre-andina/` lo herede. **Corrección sobre un primer intento equivocado en esta misma
sesión**: había pre-llenado `Notas` con anticipo 50%/cancelación — el usuario corrigió:
`Notas` sigue vacío para ventas (como siempre), los términos y condiciones van con link, no
como texto de condiciones de pago. Revertido en Servicom CAP-102 y documentado bien en
`plantillas/generar-pdf.md`. Los ~40 decks ya entregados con "7 días" (linaje mono-fase) no
se tocan retroactivamente.

## 2026-08-13 — [cliente:servicom] CAP-102: sin cifra de horas total, cronograma sin minutos
A pedido del usuario, la propuesta no compromete una cantidad total de horas (modalidad y
alcance quedan "a confirmar"): se quitó de portada, Programa, Propuesta Económica y también
de los badges/labels de los 3 slides de cronograma (el timebar conserva las proporciones
`flex` pero ya no imprime minutos). El diagnóstico cierra con una nota breve: los cuellos de
botella detectados son "hasta el momento" (se pueden mapear otros casos de uso) + por qué
Claude es la herramienta ideal para esas tareas — en 1 párrafo corto sobre `.s-pain`, no una
slide nueva.

## 2026-08-12 — [cliente:catalogo/TA-033] Rediseño de currículo: de "3 sistemas GerenSer" a "4 capacidades avanzadas de Claude"
A pedido del usuario, TA-033 pasó de mapear 1:1 los 3 sistemas del brochure GerenSer
(ManyChat/Make/N8N traducidos a Claude) a un eje de 4 capacidades avanzadas de Claude que
generan automatizaciones: prompting + RCTF, Proyectos y Conectores, API y agentes autónomos,
MCP y herramientas. Nuevo título: "Claude Avanzado para Automatizaciones". Se mantuvo la
alianza GerenSer (casos reales transversales, ya no 1 sistema por módulo). Aprendizajes:
1. **MCP se suma al set de siglas a explicar (§4.12)**: "Protocolo de Contexto de Modelo
   (MCP)" — igual regla que RCTF, expandir por slide en un `<p>`/`<li>`, nunca crudo en un chip.
2. **Reemplazo global de texto repetido**: un `replace_all` sobre una etiqueta de pie de
   página idéntica (13 apariciones) puede coincidir parcialmente con el mismo texto dentro de
   un `<title>` más largo si comparte el mismo prefijo — revisar el resultado del `<title>`
   después de un `replace_all` amplio, no asumir que solo tocó los pies de página.

## 2026-08-12 — [cliente:rush-academy] TA-034: primera alianza co-facilitada con cliente real (no catálogo)
Primera propuesta de alianza donde el aliado (RUSH Academy) co-facilita módulos completos con
un cliente real como destinatario (`clientes/propuestas/rush-academy/`), a diferencia de
TA-032/TA-033 (alianzas GerenSer, pero como producto de catálogo sin cliente asignado). Se
reutilizó el patrón de co-marca de TA-033 (único precedente: `.logo-big-dual`, `.ally-logo`,
`.foot-logos`, `.end-logo-dual`) copiado a un `overrides.css` local. Aprendizajes:
1. **Clonar desde un producto de catálogo pierde la slide de Impacto.** TA-016 (base curricular
   de TA-034) es "producto de catálogo, no propuesta a cliente final" y por eso no trae
   `.s-impact` (§4.9 no aplicaba). Al convertirlo en propuesta real hubo que trasplantar el
   bloque CSS completo de `.s-impact` desde `_base/styles.css` al `styles.css` local. Antes de
   clonar cualquier catálogo como base de una propuesta real, verificar que las 11-14 slides
   canónicas estén completas (`plantillas/estructura-canonica.md`), no asumir que un catálogo
   ya es canon completo.
2. **Logo de aliado sin versión NEGRO**: cuando el aliado solo entrega una versión (blanca,
   para fondo oscuro), se usa `filter: invert(1)` en el pie de slide (fondo claro) y
   `filter: none` sobre `.s-impact` (fondo negro) en vez de pedir/fabricar una segunda versión.
3. El checklist §10 no distingue slide: `verificar-propuesta.sh` marca como error económico
   (§4.15) cualquier término prohibido en **todo** `acroforms*.json`, incluida la caja `Notas`
   de la slide de precio (donde "cotización" es lenguaje normal, no una falla real). Confirma
   [[verificador-acroforms-economicos]]: evitar la palabra en cualquier campo, no solo en Pasos.

## 2026-08-11 — [scripts] Nuevo patrón "Inversión por fases" (cotización por fase + total) en CAP-098 IOED
El usuario pidió cambiar la hoja de precio de CAP-098 (IOED) del patrón "solo Fase 1
cotizada, Fase 2-3 progresivas" (default aerocentro) a **cotizar las 3 fases por separado +
un total**, siguiendo el modelo de la propuesta económica de Cinex (CAP-072, deck externo no
presente en el repo, adjuntado por el usuario como PDF de referencia). Se añadió un grupo
nuevo `FASE_PRICE_FIELDS` a `scripts/agregar-campo-precio.py`, activado por un marker propio
("Inversión por fases", el H2 de la slide) que no colisiona con "Propuesta Económica" — cada
PDF se procesa por separado, así que **no afecta a ningún otro deck existente**. Campos:
`PrecioFase1/2/3` (editables) + `PrecioBase` (subtotal auto-calculado vía nuevo
`make_fase_subtotal_js()`, sumando las N fases) + `Descuento` + `PrecioTotal` (Base −
Descuento, sin cambios) + `Notas`. Se generalizó `add_calculation_action` para aceptar un
`calc_js` custom por spec (antes solo usaba `make_calc_js` a secas). Decisión explícita del
usuario: Fase 2 y 3 (alcance aún no definido, depende del diagnóstico) llevan la **misma**
caja vacía que Fase 1, **sin distinción visual ni nota de advertencia** — ventas decide qué
escribir. Se quitó el bloque `.block-cotizacion` ("Cotización" como header genérico): se
solapaba visualmente con el label "Inversión total del plan" al reducir el layout a 2
columnas sin el bloque `Programa` (removido — redundante con las 3 filas de fase, que ya
comunican el alcance). Referencia si se repite el patrón: `clientes/propuestas/ioed/` +
`scripts/agregar-campo-precio.py` (grupo `FASE_PRICE_FIELDS`).

## 2026-08-11 — [catálogo] TA-032 y TA-033: hoja de cotización sin caja de T&C + fix validez
Se quitó `.cot-terms-box` (caja "Importante" con enlace a términos y condiciones) de la
slide `.s-price` en ambos decks de catálogo, a pedido explícito. CSS muerto (`cot-terms-*`)
removido de sus `overrides.css`. Sin overflow: el resto del bloque usa posicionamiento
absoluto, no depende de la caja. Además se corrigió `cot-validity`: decía "Válido
únicamente por 7 días en divisas" (preexistente, no introducido en esta sesión) — la
política real es **30 días** (§3 CLAUDE.md, `empresa/politicas-comerciales.md`). Texto
final homologado al usado en aerocentro/pago-tronic/beeper: "Cotización válida por 30 días."
**Hallazgo sin resolver:** ese mismo "7 días" aparece en ~90 decks más de
`clientes/propuestas/` (legacy) — no se tocaron, solo se corrigieron TA-032/TA-033 por ser
el alcance pedido. Backfill masivo pendiente de instrucción explícita.

## 2026-08-07 — [cliente:calzados-discovery] CAP-097 revisado: sin bloque de Claude, cotización única para las 3 etapas

Segunda pasada sobre CAP-097 (ver entrada anterior) a pedido explícito del usuario: (1) se
quitó por completo el bloque de nivelación en Claude (Skill/Project/Artifact) — el proyecto
arranca directo en Auditoría/Diagnóstico; (2) se eliminó el patrón de cotización por fase
heredado de CAP-082 Aerocentro (Fase 1 sola + Fase 2-3 progresivas) — para Calzados Discovery
**una sola hoja cubre las 3 etapas** (Auditoría/Diagnóstico + Desarrollo + Implementación).
La Fase 3 "Manual de políticas" de Aerocentro dejó de ser una etapa con cronograma propio y
pasó a ser un entregable dentro de Implementación. El roadmap bajó de 3 páginas a 2
(`.rmx-linear`: página 1 = Etapa 1+2 con checkpoint intermedio, página 2 = Etapa 3 + entregable
final), reutilizando el mismo componente sin tocar CSS — el deck bajó de 16 a 15 slides.

**Bug confirmado (extiende [[verificador-acroforms-economicos]])**: la palabra suelta
«Cotización» (sustantivo, no solo el verbo «cotizar») en el campo `Notas` de `acroforms.json`
("Cotización única para las 3 etapas del proyecto.") disparó el check §4.15 vía `cotiza\w*`.
El label estático "Cotización" en el HTML de `.s-price` (`block-eyebrow`) no lo dispara — el
grep de §4.15 solo escanea la sección "Cómo arrancamos" del HTML, pero escanea **todo**
`acroforms.json` sin excepción. Corregido reformulando a "Alcance único: las 3 etapas del
proyecto van juntas."

Esto significa que el esquema de CAP-082 (fases separadas + cotización progresiva) **no es
universal** incluso siendo el estándar declarado: aplica cuando el proyecto tiene fases que
el cliente quiere cotizar por separado; cuando el cliente pide "todo junto" (como Calzados
Discovery), se cotiza en una sola hoja aunque el roadmap conserve varias etapas.

---

## 2026-08-07 — [cliente:calzados-discovery] CAP-097 clonado directo de aerocentro (CAP-082) · usuario lo declara estándar de propuestas multi-fase

Nueva capacitación CAP-097 (agente de IA que califica y atiende leads de Meta Ads hasta el
punto de venta, entregando al equipo comercial para el cierre) clonada **directamente de
`aerocentro/` (CAP-082)**, no de `pago-tronic/`. El usuario declaró explícitamente que el
esquema de CAP-082 (3 fases / 5 etapas numeradas de forma corrida, 1 sola hoja de cotización
para Fase 1 con Fase 2-3 cotizadas de forma progresiva, roadmap en 3 páginas independientes)
es **el estándar de propuestas multi-fase de ahora en adelante** — no una decisión puntual de
Aerocentro. Pendiente: confirmar con el usuario si esto implica actualizar la tabla de decks
de referencia en `CLAUDE.md` §6 (hoy apunta a `pago-tronic/` para el patrón de 3 etapas) para
que apunte a `aerocentro/`/`calzados-discovery/` en su lugar, o si conviven ambos según el
caso (ver nota en `clientes/propuestas/calzados-discovery/brief.md`).

Dos aprendizajes de contenido: (1) **Posicionamiento competitivo explícito en el roadmap**:
cuando el cliente está comparando proveedores que ofrecerían una solución "llave en mano", el
contraste (factura nueva por cada ajuste de un tercero vs. el propio equipo ajustando lo que
construyó) se insertó en el `rmx-ethics` de la página 2 del roadmap (la fase de
Desarrollo/Adopción), no en la slide de dolor — es el lugar natural porque ahí se describe
cómo se construye. (2) **Slide de Impacto con métrica no-porcentual (HBR "7x más probable de
calificar un lead en la primera hora")**: no encaja en el gauge circular (diseñado para
rangos 0-100%), así que se llevó al `impact-hook` (texto libre) y el gauge se reservó para una
métrica en % (Salesforce, 83% de equipos con IA generativa vio crecer ingresos).

---

## 2026-08-06 — [cliente:agromundial] Piloto CAP-096 clonado de pago-tronic · 2 módulos · caja de términos y condiciones (patrón CAP-082)

Nueva capacitación CAP-096 (piloto Compras y Comercial, 7 personas, escalamiento a Finanzas no
cotizado) clonada de `pago-tronic/` en vez de `aerocentro/` porque el patrón de negocio (varias
áreas como un solo sistema, roadmap por defecto Diagnóstico→Construcción→Implementación) encajaba
mejor que el de 3 fases secuenciales de Aerocentro. Tres aprendizajes: (1) **Grid de 2 módulos**
ya tiene precedente reutilizable en `robin-agency/styles.css` (`:has(> .module:nth-child(2))`) —
se copió tal cual a `agromundial/styles.css`, no hubo que inventar el patrón. (2) **Caja de
términos y condiciones** (`.cot-terms-box` + `.cot-progressive`) solo existía en `aerocentro/`
(CAP-082) hasta ahora — se portó su CSS completo (bloque "Importante" con borde naranja + enlace
real a Drive) a un deck de una sola fase; queda como bloque reutilizable para cualquier propuesta
que necesite este candado comercial, no solo multi-fase. (3) Dos bugs confirmados solo al revisar
el PDF renderizado (§4.10, invisibles al detector automático): `<strong>` dentro de `.s-pain ol
li` rompe el flex igual que en `.s-goals .specifics`/`.s-schedule .ses-block` (ver
`bug-strong-flex-specifics` en memoria) — y la caja AcroForm `Entregables` desborda si se listan
7 destacados largos en vez de 2 propios + los 3 institucionales fijos de `ENTREGABLES_DEFAULT`
(ver `bug-entregables-acroform-box-narrow`).

---

## 2026-08-06 — [cliente:beeper] Auditoría por área añadida a Fase 1 · roadmap a 3 rutas · bug de colisión en slide de precio

Se restructuró CAP-079 (ya enviada) para agregar un componente protagonista a la Fase 1:
**Auditoría y diagnóstico por área** (Sesiones 5-6, Módulos V-VI), levantamiento directo con
Comercial y con Finanzas/Administración, distinto del ejercicio grupal de la Sesión 4. Tres
aprendizajes reutilizables: (1) **Extender `.s-roadmap` de 2 a 3 rutas funcionó en el primer
intento** aplicando la memoria `roadmap-3-etapas-flex-minheight` al pie de la letra
(`min-height:0` en `.rmx-route`, fork/merge recalculado a tercios con conector recto para la
fila del medio, 3er acento negro+blanco, cards compactadas ~12%) — confirma que la receta es
generalizable, no solo para el patrón Diagnóstico/Construcción/Implementación. (2) **`.s-price
.block-programa` es `position:absolute; top:195px` fijo**, asumiendo que el bloque `Duración`
de arriba (flujo normal) cabe en ≤2 líneas: alargar ese texto a 3 líneas monta "PROGRAMA"
encima de la última línea, y el detector automático **no lo ve** (colisión interna entre un
bloque en flujo normal y uno absoluto, mismo patrón que `bug-benefits-grid-280px` /
`bug-entregables-acroform-box-narrow`). Se corrigió acortando el texto de Duración a la
longitud original (~96 chars), nunca tocando el CSS compartido. (3) Al ampliar de 4 a 6
sesiones, los 4 items de `.s-goals .specifics ol` (capacidad "3 a 4") llegaron al límite:
+1 item nuevo + texto más largo en el objetivo general desbordó +12px; se resolvió acortando
ambos, no quitando el ítem.

---

## 2026-08-06 — [cliente:aerocentro] Segunda pasada: de 4 fases/4 cotizaciones a 3 fases/1 cotización progresiva

Misma tarde, corrección sobre la revisión anterior (ver entrada siguiente). Tres aprendizajes
reutilizables: (1) **Enlace real en slide de precio**: un T&C que debe ser clicable no puede vivir
en un campo AcroForm (los form fields no soportan hipervínculos) — va como `<p><a href="...">`
estático en el HTML, fuera de las cajas `multi-box` editables. (2) **Patrón "1 hoja + cotización
progresiva"**: cuando solo la primera fase tiene alcance cerrado, se cotiza solo esa (`.s-price`
única) y se agrega una nota estática (no en AcroForm) del tipo «las fases N y N+1 se cotizarán de
forma progresiva according a lo que arroje el diagnóstico» — evita inventar precio para trabajo
sin alcance definido. (3) **El roadmap de 4 rutas es reversible a 3**: como el CSS de 4 rutas se
construyó *extendiendo* el patrón original de 3 (mismo archivo, mismas clases base `.rmx-node-f2/
f3/f4`), revertir fue restaurar `.rmx-up/.rmx-mid/.rmx-dn` (arriba/centro recto/abajo) y borrar
`.rmx-b1-4`/`.rmx-node-f5`/`.rmx-card-f5` — sin rehacer el componente. **Deliverable nuevo sin specs
del cliente** (Fase 3 "Manual de políticas y uso de IA"): se redactó por inferencia razonable
(lineamientos de uso responsable + roles/permisos + manejo de datos, análogo al AUP mencionado en
CLAUDE.md §4.12) y se dejó marcado en `brief.md → Pendientes` para confirmar con el cliente, en vez
de preguntar y frenar la iteración.

## 2026-08-06 — [cliente:aerocentro] Roadmap extendido a 4 etapas: de "6 áreas × 3 etapas" a "4 fases en equipo"

CAP-082 Aerocentro se reestructuró de una entrega por área (6 áreas × diagnóstico/construcción/
implementación) a **4 fases para toda la empresa en conjunto**: Fase 1 · Conociendo la IA con Claude
(nivelación en Skills/Projects/Artifacts, horas fijas) → Fase 2 · Diagnóstico (horas fijas) → Fase 3 ·
Desarrollo (cliente participa, sin horas fijas) → Fase 4 · Implementación (en equipo, ya no por área,
sin horas fijas). Patrón nuevo, reutilizable: **4 hojas `.s-price`** (una por fase, campos
`Programa`/`Notas` + sufijo `_2`/`_3`/`_4`, mismo mecanismo de `robin-agency-cap080`) para fases sin
horas fijas — el precio queda abierto en Adobe Reader hasta cerrar alcance. El componente `.rmx-*`
del roadmap (pensado para 2, extendido a 3 en Pago Tronic) se **extendió a 4 rutas**: fork/merge pasan
de 3 ramas (up/mid/dn) a 4 (`.rmx-b1`–`.rmx-b4`, centros en 12.5/37.5/62.5/87.5%, sin rama recta
central porque con n par no hay fila en el 50% exacto) + 5º acento de color (`.rmx-node-f5`/
`.rmx-card-f5`, gradiente de marca) para la 4ª ruta. `capacidad-cajas.md` ya permitía "3 a 5 fases" en
el roadmap, así que 4 no requirió tocar esa ficha. Al quitar la segmentación por área también se
retiró la slide de Mapa de Calor (la priorización impacto×esfuerzo×riesgo por área dejó de aplicar);
el conteo total de slides se mantuvo en 18 porque -1 (heatmap) +3 (precio 1→4) se compensan.

## 2026-08-05 — [cliente:alianza-team] Nivelación en IA en 2 fases: clonar pilotes con Fase 2 = capacitación a la medida

Alianza Team CAP-094 (I+D · 12 equipos · 17 líderes / 95 colaboradores · online síncrono). Clon de
`pilotes-perforados` (roadmap de 2 etapas) con dos adaptaciones que sirven de patrón para casos de
**nivelación/diagnóstico previo a capacitar**: (1) el pivot del roadmap entrega Mapa de Calor **+
temario a la medida** y la Fase 2 es la **capacitación** (no «aplicación de soluciones» como en
Pilotes); (2) el fork del roadmap y las 2 `.s-schedule` mapean **frentes organizativos** del cliente
(Conocimiento / Desarrollo), no dos sesiones de una misma ruta. Slide `s-heatmap` marcada «ejemplo
ilustrativo» cuando aún no hubo diagnóstico, para no fabricar hallazgos. Ángulo de copy: cliente que
ya tiene un área de IA adentro → posicionar como **nivelar al resto a esa altura**, no evangelizar.

## 2026-08-05 — [regla] §4.15: «cotiza/cotización» en `acroforms.json` (incluso en Notas) bloquea el verificador

El grep §4.15 de `verificar-propuesta.sh` sobre `acroforms*.json` incluye `cotiza\w*` y aplica a
**todo** el JSON, no solo a los pasos. Poner «se cotiza la Fase 2» en el campo `Notas` disparó el
error bloqueante. Reescribir sin el verbo: «Esta propuesta económica cubre solo la Fase 1» / «la
Fase 2 se define a partir del Mapa de Calor». Hermano de [[verificador-acroforms-economicos]].

## 2026-08-04 — [scripts] Los h2 de slide son marcador de texto para `agregar-campo-precio.py` — no renombrar sin saberlo

Al condensar CAP-060 (14 slides, 3 módulos/6h) en CAP-093 (11 slides, 1 sesión/2h, regalo para
David Nibia · Doral), personalicé el h2 de `.s-benefits` de "Lo que se llevan." a "Lo que se
lleva David." `generar-pdf.sh` corrió sin error, pero el log mostró `(omitido) 'Lo que se
llevan' — no presente en este deck`: el script ubica la página de cada bloque de campos
AcroForm (Beneficios, Próximos pasos, Propuesta Económica) buscando el texto **literal** del
h2/marker en el PDF renderizado, no por posición ni por clase CSS. Al no matchear, los campos
`Entregables`/`Acreditacion` simplemente no se insertaron — sin error visible, solo un aviso
fácil de pasar por alto en el log. Revertir el h2 a "Lo que se llevan." (idéntico al marker en
`agregar-campo-precio.py`) lo arregló: 8/8 campos añadidos. **Regla**: los h2 "Lo que se
llevan.", "Cómo arrancamos." y "Propuesta Económica" son texto de sistema, no copy libre —
personalizar alrededor (subtítulo, body) pero no el h2 mismo, o si se cambia, actualizar
también el marker en `agregar-campo-precio.py` (cambio estructural, confirmar antes). También
confirmé el patrón ya conocido [[verificador-acroforms-economicos]]: el campo `_comentario` de
`acroforms.json` mencionaba "no se cotiza" y disparó el bloqueo §4.15 (`cotiza\w*`) aunque es
metadata interna, no copy de cliente — evitar esas palabras hasta en comentarios internos del JSON.

## 2026-08-03 — [cliente:puro-lomo-bajo] Colisión de código CAP-089 + patrón para "espacio para cotizar" algo aparte (traslado)

Al crear CAP-090 Puro Lomo Bajo (el usuario pidió CAP-089, pero ya estaba asignado hoy mismo a
Laboratorios Conspat — confirmado con el usuario, se usó el siguiente libre en `INDEX.json`).
El cliente pidió "un espacio para cotizar el traslado del facilitador" (sesión presencial en
Villa de Cura). Se resolvió con el campo `Notas` ya existente de `.s-price` (logística +
línea en blanco `Traslado: _____________` para que ventas escriba el monto), sin agregar un
AcroForm nuevo (cambio estructural que exige confirmación explícita, `generar-pdf.md` §4.6).
Al redactar esa nota, el primer intento ("se cotiza aparte") disparó el chequeo §4.15 de
`verificar-propuesta.sh` — el regex bloquea `cotiza\w*` en cualquier campo de `acroforms.json`,
no solo en los pasos de arranque (confirma [[verificador-acroforms-economicos]]). Reemplazo:
"monto aparte" en vez de "se cotiza aparte".

## 2026-08-03 — [cliente:dusa-cap087] Dos colisiones internas invisibles al detector: caja Entregables angosta y chips de Impacto

Al construir DUSA CAP-087 (Manual de Políticas y Gobernanza Ética de IA, clonado desde
`pago-tronic/` para reusar el roadmap `.rmx-*` de 3 etapas ya extendido), `verificar-overflow.js`
dio limpio pero el PDF renderizado mostraba dos recortes/solapamientos que el script no cubre:

1. **Caja AcroForm `Entregables`** (158×117pt, Helvetica-Bold 10pt ≈ 27 chars/línea, ~9 líneas):
   destacados largos (ej. una frase de 90 chars con departamentos entre paréntesis) envuelven a
   3 líneas y el conjunto se corta al fondo de la caja en el PDF — el detector mide desborde de
   la slide HTML, no de un campo AcroForm horneado. Fix: destacados de una sola línea corta
   (~≤27 chars). Detalle: memoria `bug-entregables-acroform-box-narrow`.
2. **`.s-impact .gauge-panel .chips`** con 2 chips de labels largos (60-70 chars) envuelve cada
   uno a 2-3 líneas y el conjunto crece hasta solaparse con la banda `.impact-hook` de abajo
   (dos hermanos en flujo normal, no un contenedor que recorta). Fix: 1 solo chip con label
   corto. Detalle: memoria `bug-impact-gauge-chips-collision`.

- **Regla derivada**: además de `verificar-overflow.js`, renderizar SIEMPRE el PDF a imagen
  (`pdftoppm -r 110 -png <pdf> <prefix>`) y mirar slide por slide antes de entregar — en
  particular las slides de Programa (cards con `:has()` compacto), Beneficios (cajas AcroForm
  angostas), Roadmap (colisión de 3 rutas) e Impacto (chips vs. hook): son los 4 puntos donde
  ya se han visto colisiones internas invisibles al detector automático.
- También se corrigió un falso positivo de §4.15 en `verificar-propuesta.sh`: el regex
  `cotiza\w*` capea legítimamente la palabra "Cotización" dentro de la caja `Notas` de
  Propuesta Económica (no es un acuerdo económico en "Cómo arrancamos", es la slide de precio
  hablando de sí misma). Se evitó reescribiendo a "Precio único y consolidado..." en vez de
  tocar el script compartido sin confirmación.

---

## 2026-08-03 — [cliente:dusa] Clonar una charla vieja (CH-001/CH-002) a CSS canónico exige portar su `.session`/`.grid` propio

Las charlas CH-001 (`smartkeep`) y CH-002 (`ia-mundo-real`) son anteriores al `../_base/styles.css`
compartido: viven con una copia local de `styles.css` que incluye un componente `.sessions >
.session > .header + .grid` (tabla ligera de 5 columnas para el cronograma) que **no existe en
`_base`**. Al clonar CH-002 para `dusa` (CH-007) y migrar el link de CSS a `../_base/styles.css`
+ `overrides.css` (para dejar de arrastrar la copia desactualizada), la slide de cronograma quedó
sin ningún estilo (`.session`/`.grid` sin reglas) y desbordó **+734px** — el contenedor crecía sin
límite porque nada lo acotaba. Solución: portar el bloque CSS completo (`.s-schedule`,
`.session`, `.header`, `.grid`, `.grid .label`) de la copia local del clon de origen al
`overrides.css` del nuevo deck antes de correr `verificar-overflow.js`.

- **Regla derivada**: al modernizar el CSS de un clon legacy (local → `_base` + overrides),
  diffear el `styles.css` de origen contra `_base` (`diff _base/styles.css <origen>/styles.css`)
  **antes** de borrar el archivo local, y portar a `overrides.css` cualquier bloque que solo
  exista en el origen (marcado `>` en el diff).
- **Además**: CH-001/CH-002 también son anteriores a dos reglas hoy vigentes de
  `plantillas/propuesta-comercial.md` — charlas **no** llevan slide `.s-orange` (ABR), y sí
  llevan `.s-impact` (Impacto). Un clon nuevo de charla debe aplicar la estructura vigente
  (sin ABR, con Impacto), no copiar literal la de CH-001/CH-002.

---

## 2026-07-28 — [bug] `.s-benefits .grid` (slide 8) se solapa con "EQUIPO FACILITADOR" cuando un bloque excede 280px

El grid de 4 bloques de la slide de Beneficios (`.s-benefits .grid`, `_base/styles.css`)
tiene `height: 280px` fijo y cada `.block` no tiene `overflow: hidden`. Si el contenido de
cualquiera de los 4 bloques (Perfil de egreso, Beneficio del programa, Entregables o
Acreditación) excede esa altura, el texto se derrama por debajo de su propio borde y se
solapa visualmente con la etiqueta "EQUIPO FACILITADOR" de la franja negra de abajo.
**`verificar-overflow.js` no lo detecta** — el bloque no excede los límites de la *slide*,
solo su propio contenedor interno, y el script solo mide desborde a nivel de slide.

- **Confirmado en dos decks**: el PDF ya **entregado** de `zoom-comercial/` CAP-058
  (enviado 2026-07-28) tiene el defecto en su columna "Beneficio del programa formativo".
  Se detectó al clonar el mismo template para `zoom-operaciones/` CAP-059 (misma fila
  overflowing, esta vez en "Perfil de egreso").
- **Cura aplicada en CAP-059**: acortar el texto de los bloques más largos (Beneficio del
  programa formativo y, sobre todo, el ítem "Saber ser" de Perfil de egreso) hasta caber en
  ~280px sin tocar el CSS compartido — ver `zoom-operaciones/brief.md` para el detalle y los
  textos antes/después.
- **Pendiente de decisión**: (a) si se sube el `height` de `.s-benefits .grid` en
  `_base/styles.css` o se añade `overflow:hidden` + reducción de `font-size`, lo que
  arreglaría el defecto de raíz para todos los decks que usan esta plantilla; (b) si se
  re-emite el PDF ya enviado de `zoom-comercial/` CAP-058. Ninguna de las dos se ejecutó
  (archivo estructural — requiere confirmación, CLAUDE.md §8).
- **Regla operativa mientras no se arregle el CSS**: al escribir Beneficios (slide 8) de
  cualquier deck canónico, mantener cada bloque de la fila de 4 en ≤ ~9-10 líneas visuales a
  11.5px (revisar visualmente el PDF, no confiar solo en el detector automático).

---

## 2026-07-28 — [cliente:zoom-comercial] Zoom Mercadeo CAP-058 (Fase 2) · 3er curso de la ruta Zoom, sin fondo por corregir

Capacitación In-Company de Mercadeo/Estrategia Digital para Zoom (4 mód / 4h / 2 sesiones), tercer curso construido de la ruta Zoom junto a `zoom-miami` (CAP-046, bootcamp base) y `zoom` (CAP-029, Legal). El usuario confirmó explícitamente **"sin observaciones de fondo"**: solo aplicar los 4 **puntos transversales** ya acordados 2026-07-28 y documentados en `zoom-miami/brief.md`.

- **Los 4 puntos transversales replicados** (ver `zoom-miami/brief.md` → Notas internas para el acuerdo original): (1) **Reto IA ZOOM** como nombre único del concurso — este curso llamaba a su reto final "Laboratorio de Proyectos · MVP" (uno de los 4 nombres distintos que el acuerdo prohíbe); renombrado en el módulo IV, chip de cronograma y sesión 2 (lanzamiento en sesión 1, cierre en sesión 2, adaptado a que este curso solo tiene 2 sesiones en vez de 3). (2) **Prompt ejecutivo (5 partes)** referenciado como el método de prompting ya adoptado en la ruta Zoom, mencionado en la estrategia de enseñanza de sesión 1 (no en Objetivos: ver bug de overflow abajo). (3) **Expectativas realistas sobre Gems**: encuadre honesto añadido en Perfil de egreso y en estrategia de enseñanza de la sesión de Gems ("qué automatiza y qué sigue dependiendo del criterio humano"). (4) **Medición de tiempo ahorrado** (línea base + 30 días): añadida a Beneficios, Entregables (`acroforms.json`) y Paso03 de "Cómo arrancamos" (renombrado "Kick-off y línea base").
- **Sin slide de Propuesta Económica** (se cotiza dentro de la ruta Zoom ya en curso, mismo patrón que `empleate/`): los 5 campos de precio no aplican, los 8 no-económicos (Entregables/Acreditación/Pasos) siguen obligatorios. Confirmado que sin el marcador "Propuesta Económica", `agregar-campo-precio.py` simplemente omite esos 5 campos sin error.
- **3 defectos propios cazados en la primera pasada del verificador** (útil para no repetirlos): (a) un guión largo (§4.13) que yo mismo escribí al renombrar el reto ("Reto IA ZOOM — Laboratorio MVP") — corregido a `·`; (b) **falso positivo §4.15 nuevo**: la palabra **"acuerdo"** en el comentario `_comentario` de `acroforms.json` ("acuerdo marco con Zoom") disparó el grep de términos económicos — mismo patrón que "Pago Tronic" con "pago" ([[nombre-cliente-falso-positivo-4-15]]), pero esta vez el disparador es una palabra de redacción interna, no el nombre del cliente; regla ampliada: evitar también "acuerdo" en comentarios internos de acroforms.json; (c) **overflow +15px en Objetivos** al añadir "aplicando el método Prompt ejecutivo (5 partes)" al objetivo específico 1 (ya cargado): la cura fue mover la mención del método a un lugar con más aire (estrategia de enseñanza de la sesión, que ya lo tenía) en vez de forzarlo en la caja `.s-goals .specifics` (capacidad 3-4 ítems, ya al límite).

Cliente pidió, en reunión presencial, un **plan de negocio + "cerebro digital"** (sistema central de IA) para 6 áreas (Marketing, Ventas, Compliance, Documentación, Desarrollo, Auditorías y certificaciones), con la condición explícita de **lenguaje de negocio, no técnico**: nada de describir skills o herramientas de IA por nombre, solo el movimiento de punto A a punto B por área.

- **Clon de `pilotes-perforados`** (no de cumbre-andina): el patrón diagnóstico → roadmap (`.s-roadmap`) → mapa de calor (`.s-heatmap`) encaja mejor con un "plan de negocio" que con un temario de sesiones. `.s-program` se usó para las **6 áreas como module cards** (no como 2 fases): h3 = área, `obj` = frase A→B en ≤80 chars, 2 chips de outcome por card (sin nombrar herramientas de IA).
- **Revisión 2026-07-23 (feedback del usuario):** el diagnóstico y la implementación son **por área**, no agrupados. Estructura final: cada una de las 6 áreas recorre, de forma independiente, hasta **2 sesiones de diagnóstico** (entender necesidades) + **2 sesiones de implementación** (activar el cerebro digital y enseñar a usarlo) — hasta 24 sesiones en total. Esto pasó las 2 slides `.s-schedule` agrupadas (3+3 áreas) a **6 slides, una por área**, cada una con 3 columnas propias — "Diagnóstico · hasta 2 sesiones" / "Implementación · 2 sesiones" / "Recursos y entornos" — en vez de las etiquetas genéricas "Estrategias de enseñanza/aprendizaje" del template. El `.s-roadmap` pasó de "2 grupos de áreas" a **2 etapas secuenciales que aplican a las 6 áreas por igual** (Etapa 1 Diagnóstico / Etapa 2 Implementación). Deck final: **18 slides** (antes 14).
- **`.s-heatmap` rediseñado a 1 fila por área** (6 filas, columna "Área" en vez de colspan por grupo + sub-filas de tareas). El heatmap original de pilotes-perforados con sub-filas de tareas (12 filas: 4 áreas × 3) **ya tiene un desborde conocido** (`plantillas/capacidad-cajas.md`); a nivel de negocio (1 fila = 1 área) no hace falta ese detalle y se evita el riesgo. Columna "Herramienta" se reemplazó por "Qué construye el cerebro digital" con tags de outcome, no de producto/vendor — más alineado al pedido de no-técnico.
- **Cotización única consolidada** (no multi-track como Robin Agency CAP-080): el cliente pidió el cerebro digital como un sistema, no 6 servicios sueltos. 1 sola `.s-price`.
- **Bug de plantilla descubierto**: `<strong>` dentro de `.s-goals .specifics ol li` rompe el layout en columnas — el `li` tiene `display:flex` (para el número circular) y el texto con `<strong>` se fragmenta en anonymous flex items en vez de fluir como texto normal. Ningún deck anterior había puesto negrita ahí. Mitigación aplicada: sin negrita en esa lista. Pendiente si se quiere negrita ahí: cambiar `.s-goals .specifics ol li` a `display:block` + `padding-left` en vez de flex (fuera de alcance de esta propuesta puntual).
- **Nombre del cliente colisiona con el filtro §4.15**: "Pago Tronic" contiene la palabra "pago", que el regex de `verificar-propuesta.sh` (términos económicos en `acroforms*.json`) cachea como falso positivo. Solución: evitar escribir el nombre del cliente dentro de los campos `Paso*`/`Notas` del AcroForm (usar "la empresa" o simplemente omitir el nombre); no se tocó el script compartido.
- Datos de Impacto (McKinsey — *economic potential of generative AI* 2023, *Unleashing developer productivity with generative AI* 2023, *How agentic AI in banking drives KYC/AML transformation* 2025) vía WebSearch — eje temático nuevo (fintech/remesas/compliance), no había estudios ya citados en otro deck para reusar.
- **Revisión 2026-07-23 (2ª ronda):** se insertó una **Etapa 2 · Construcción (Intezia)** entre Diagnóstico e Implementación en el roadmap (slide 11) — Intezia arma el cerebro digital con los hallazgos del diagnóstico, sin sesiones con el cliente, antes de activarlo con el equipo. El componente `.rmx-*` (fork/merge) estaba hecho para exactamente 2 rutas; extenderlo a 3 requirió (a) `min-height:0` en `.rmx-route` — sin eso el contenido no se encoge y desborda la altura fija de `.rmx-journey` **sin que el detector automático lo note** (colisión interna, no desborde de página); (b) compactar padding/tipografía de las cards ~15%; (c) un 3er acento de color negro/blanco (sin salir de la paleta); (d) recalcular los conectores del fork de 25/75% a 16.667/50/83.333%, con conector recto (sin curva) para la fila central. Detalle en memoria `roadmap-3-etapas-flex-minheight`.
- **Instrucción del usuario (2026-07-23): este patrón de 3 etapas pasa a ser el default** para el roadmap de toda propuesta multi-fase / capacitación de ahora en adelante (no exclusivo de Pago Tronic). Documentado en `plantillas/propuesta-comercial.md` → *Roadmap — patrón de 3 etapas* y en `CLAUDE.md` §6 (tabla de decks de referencia para clonar: `pago-tronic/` para roadmap de 3 etapas, `pilotes-perforados/` solo si un proyecto puntual no separa una fase de construcción propia).

---

## 2026-07-20 — [cliente:robin-agency-cap080] Robin Agency CAP-080 · 3 formaciones por departamento en una sola propuesta

Capacitación in-company que capacita a **3 departamentos distintos** (Medios Digitales 6 · Cuentas 30 en 2 grupos de 15 · Talento Humano 4 = 40 part.) con foco propio cada uno, en **una sola propuesta** (no fases: pueden ir en simultáneo o escalonadas). Slug nuevo `robin-agency-cap080` porque `robin-agency` ya tenía CAP-032. Eje: IA aplicada a la productividad de una agencia (Gemini + Claude).

- **Clon multi-track de `pilotes-perforados`.** El componente `.s-schedule` (ruta 1/2/3) se reusa como **una slide de detalle por departamento** (ruta = «formación N de 3», fill 33/66/100%), no como sesiones de una misma ruta. El `.s-program` de 3 módulos (grid `repeat(3,1fr)` por defecto) = las 3 formaciones. El `.s-orange` de 3 pilares presenta el **arranque común por departamento** que el cliente enfatizó: Nivelación → Kick-off con el líder (levantamiento) → Profundización práctica.
- **3 hojas de cotización, una por formación — multi-página NATIVO.** `agregar-campo-precio.py` ya soporta **varias slides `.s-price` con el marker «Propuesta Económica»**: la 1ª mantiene los nombres canónicos (`PrecioBase`, `Programa`, `Notas`…), la 2ª y 3ª reciben sufijo `_2` / `_3`, y el JS de `PrecioTotal_N` autocalcula su propio par por instancia. Para pre-llenar los `Programa_2/_3` y `Notas_2/_3` basta declararlos como claves en `acroforms.json` (`customize-acroforms.py` itera todas las claves genéricamente). Sin `customize-<slug>.py`, sin tocar scripts. (16 slides tras añadir el Kick-off conjunto como Sesión 01 en la ruta `.s-schedule` de 4 nodos.)
- **Ojo:** el verificador grepa **todo** `acroforms*.json` por términos económicos §4.15 (no solo los Paso). Poner «Cotización/Pago/BCV» en `Notas` lo bloquea. Notas debe ser logística pura; el pago va en `brief.md` (interno) y lo maneja ventas.

## 2026-07-18 — [cliente:empleate] Empléate TA-030 · taller de fundamentos con audiencia mixta, alianza sin precio

Taller único de **4 h** (alianza, **sin slide de precio**, sin asesor de ventas) para los **cinco equipos de Empléate juntos** (Administración, Comunicaciones, Servicios, Tecnología, Estrategos). Clon de `dr-care/` (taller 4h / 2 bloques / sin precio ya resuelto). Eje: **fundamentos de IA con criterio y buenas prácticas**, multi-herramienta (Gemini, Copilot, Qwen, DeepSeek).

- **Encuadre del cliente = diseño del deck.** El cliente pidió explícitamente **bases + expectativas realistas** (la IA "no es panacea"), no soluciones por equipo, para luego desarrollar cada área por su cuenta. Se honró: 6 módulos de fundamentos (qué es y qué no, ecosistema de herramientas, prompting con método, criterio/buenas prácticas, IA aplicada, cómo seguir solos). Las **necesidades de cada equipo entran como ejemplos y casos**, nunca como módulos separados.
- **Audiencia mixta → herramientas del cliente, no stack impuesto.** Los ejercicios usan lo que ya usan (Gemini/Copilot/Qwen/DeepSeek) en vez de imponer Claude. Impacto reusó las cifras verificadas de dr-care (Stanford HAI · McKinsey · Anthropic) porque son cross-funcionales y encajan con los 5 equipos; hook reorientado a "la diferencia no es la herramienta, es el criterio".

## 2026-07-16 — [cliente:beeper] Beeper CAP-079 · multi-fase invertido (formación primero) y la objeción de costos como slide

Capacitación In-Company para **Beeper** (delivery B2C desde 2020, **5 personas sostienen toda la operatividad**, sin departamento de tecnología, procesos 100% manuales). Clon de `diram/` (multi-fase canónico más reciente), **16 slides** (Diram tiene 14: +2 por tener 4 sesiones en vez de 2).

- **El multi-fase se puede invertir.** En Diram/Pilotes la Fase 1 es un *diagnóstico* y la Fase 2 la formación. En Beeper es al revés: **Fase 1 = formación** (Intezia Fundamentals con casos ajustados), **Fase 2 = agentes**. El `rmx-journey` y el Mapa de calor **aguantan la inversión sin tocar CSS**: el Mapa de automatización pasa a ser el entregable *de dentro* de la Fase 1, y las 2 rutas del fork agrupan las 4 sesiones en bloques (nodos `1·2` / `3·4`). La estructura canónica es más reusable de lo que sugiere su narrativa de origen.
- **La objeción comercial se responde en una fila del Mapa de calor, no se esquiva.** El cliente usa Claude Pro ($20/mes) personal y teme quemar créditos en un canal 24/7. **Tiene razón**, así que la fila lo declara con badge **«Fuera de alcance»** («Sostener ese canal sobre el plan personal de 20 $ al mes» · Riesgo Alto · «la preocupación de Beeper es correcta»). Mismo movimiento que el caso #4 de Diram: **darle la razón primero es lo que compra autoridad** para vender la arquitectura correcta (integración de pago por uso) en la fila de arriba.
- **§4.9 · la heterogeneidad del estudio ES el argumento de venta.** Brynjolfsson, Li y Raymond (NBER 31161, 2023) miden **5.179 agentes de atención al cliente**: +14% promedio, **+34% en novatos**, «impacto mínimo» en expertos. Beeper declara nivel *principiantes* en su ficha y su dolor #4 es atención 24/7: el estudio mide **literalmente su población y su tarea**. Gauge con Noy y Zhang (Science, 2023, 453 profesionales): −40% tiempo, +18% calidad. **La barra de «expertos» no lleva cifra** (el paper dice «minimal impact» sin darla): `bar-val` = «Efecto mínimo», ancho 4% cualitativo, declarado en un comentario del HTML. Nueva clase `.bar-min` en `overrides.css` (saca el texto al track, hermana de `.bar-neg` de Diram).
- **§4.12 cazado en revisión manual, no por script**: `rmx-ethics-tag` decía «Metodología ABR» y ABR solo se expande en la slide 10. Cura §4.12.3: **quitar la sigla** («Aprendizaje Basado en Retos · Nivelar antes de automatizar»), no forzar la glosa en un tag sin espacio. Diram arrastra el mismo defecto sin corregir.
- **El gap vertical de `.s-schedule` sin `.timebar` es canónico**, no un defecto: Diram entregado lo tiene idéntico. Verificado comparando PDFs antes de «arreglarlo». Útil para no romper el canónico persiguiendo un falso positivo visual.

## 2026-07-16 — [bug] `<strong>` suelto dentro de un `<li>` flex rompe el párrafo

`.s-pain ol li` y `.s-goals .specifics ol li` son `display: flex`. Un `<strong>` puesto directo en el `li` **se vuelve un ítem flex hermano del texto**: las palabras se separan en columnas y el punto sale destrozado (se vio en Ailyn Gruszka CAP-070, «Unificar los **Excel de nóminas** de varias organizaciones» renderizó como texto partido y desalineado).

- **Regla**: en esos `li`, el contenido con negrita va **envuelto en un `<span>`** — `<li><span>…<strong>…</strong>…</span></li>`. La canónica ya lo hacía en el objetivo 2 de `.s-goals`; era un patrón sin escribir.
- **Trampa**: §4.8 pide resaltar palabras clave en `<li>`, así que el choque aparece cada vez que se añade negrita a un diagnóstico u objetivo nuevo.
- **El detector de overflow NO lo caza** (nada se sale de la caja, solo se ve mal). Lo caza la revisión visual del PDF (§4.10.1).

## 2026-07-16 — [bug] El detector de overflow NO ve el texto de los AcroForms

`verificar-overflow.js` renderiza el **HTML**, pero los campos `Entregables` / `Acreditacion` van **vacíos en el HTML** (§4.14): su texto vive en el `/V` + `/AP` horneado del PDF. Resultado: **el detector da 0 desbordes y aun así el PDF entregable sale con el texto recortado a media palabra.** Caso base: Diram CAP-078, `Entregables` con 7 ítems largos se cortó en «Workbook digital…» y el verificador dijo OK.

- **Capacidad real de la caja `Entregables`**: `/Rect (438, 338, 596, 455)` = 158×117 pt → **~11 líneas visuales a 10 pt**, ~27–31 chars por línea. Un ítem de 70 chars ocupa 3 líneas, no 1.
- **Regla**: al escribir `acroforms.json`, contar **líneas envueltas**, no ítems. 4 destacados de una línea + los 3 de `ENTREGABLES_DEFAULT` ≈ 8–9 líneas = seguro.
- **Único control que lo caza**: la revisión visual del PDF (§4.10.1). Es la prueba de que ese paso no es opcional aunque el script termine en verde.

## 2026-07-16 — [bug] `.bar-val` se desborda cuando la barra de Impacto es corta

En `.s-impact`, `.bar-val` es `position:absolute; right:10px` **dentro de `.bar-fill`**: si el texto es más ancho que la barra, se sale y **colisiona con la fila de abajo**. Con `--w:19%` un valor como «19% más lentos» rompe el panel. `.bar-track` no tiene `overflow:hidden`, así que no se recorta: se solapa.

- **Regla**: el `bar-val` lleva **solo la cifra** («+55,8%», «−19%»); el qualifier va en el `.bar-label`.
- Para barras muy cortas, sacar el valor al track con `left: calc(100% + 10px)` (el track es oscuro, el naranja de marca se lee). Ver `clientes/propuestas/diram/overrides.css`.

## 2026-07-16 — [cliente:diram] Diram CAP-078 · reencuadre «IA que dibuja» → «IA que programa», y honestidad como estrategia

Capacitación In-Company para **7 ingenieros eléctricos (no programadores)** de Diram (México, calidad de energía, proyectos EPC). El cliente pidió «una herramienta que dibuje» y **ya se quemó**: probó claude.ai en el navegador y falló, porque un LLM no genera DWG (binario, propietario, cerrado). **Tiene razón en el hecho y se equivoca en la conclusión**: la vía es que la IA escriba el **código** (Python/ezdxf, AutoLISP) y que AutoCAD produzca el archivo.

- **Estructura multi-fase** (clon de `pilotes-perforados`): Fase 1 auditoría técnica cotizada (auditar DWG reales + sesión con TI) · Fase 2 formación abierta. El levantamiento lo exigía: sin abrir un archivo, la viabilidad de 2 de los 4 casos es especulación.
- **El Mapa de calor se usó como slide de honestidad**: las filas declaran `DWG Compare` y `DATAEXTRACTION` («Ya lo pagan») como solución **sin IA**, y el caso #4 va con badge **«Fuera de alcance»** dándole la razón al cliente. Decirlo nosotros primero es lo que recupera la autoridad técnica.
- **Impacto (§4.9) sin extrapolar**: no existe estudio que mida IA en unifilares o CAD. Se citaron estudios de **generación de código**, que es lo que el programa enseña, **incluido el resultado negativo de METR** (expertos 19% más lentos creyendo ir 20% más rápido) como argumento de por qué se capacita con método. Un dato en contra, bien usado, vende más que tres a favor.
- §4.11 aplicado: Diram es Microsoft-first y TI es «medio paranoico»; el deck **nunca** dice que migran, solo que la arquitectura se apoya en «el entorno Azure que ya usan».

## 2026-06-18 — [cliente:petroval] Petroval CAP-064 · Fundamentals Claude-forward para área administrativa desde cero

Capacitación In-Company «Fundamentos de IA» para 7 personas del área administrativa de Petroval que **parten de cero** (sin licencias ni formación) pero **usan Excel intensivamente**. Decisión del usuario: **centrar el programa en Claude** (no multi-herramienta balanceado como Fivenca) por ser lo que más transforma el trabajo administrativo sin curva técnica. **Excel = puerta de entrada concreta.** 4 mód / 8h / 2 ses. de 4h (subido de las 6h de Fivenca para dar aire a la práctica). Estructura: I Fundamentos+cultura · II Claude copiloto (Proyectos, análisis de documentos) · III Datos de Excel con IA (análisis, gráficos, dashboards) · IV Informes, presentaciones y diseño. **Clon de `fivenca-fundamentos-ia` (CAP-061)** = el analog Fundamentals canónico; re-anclado Claude-forward. Equipo Education, asesora María Iribarren, modalidad sin afirmar. Impacto sin recifrar (§4.9). [[project_petroval_cap064]]

## 2026-06-18 — [arquitectura] Estado de reposo = «Enviada» (terminado = enviado); «En corrección» para reenvíos

El usuario aclaró su flujo real: **en cuanto una propuesta queda lista, la envía al cliente ese mismo instante** — no existe limbo «generada pero sin enviar». El único hueco lo abre una corrección: vuelve a revisión y se reenvía apenas se cierra. **Cambio al modelo de estados (§4.19):** el escalón «Entregada» se elimina del flujo de reposo → `estampar-entrega.py` ahora pasa **Borrador (o En corrección) → Enviada** al generar (antes Borrador→Entregada); append-only protege solo el **resultado de venta** (Aprobada/Perdida) + la `fecha_entrega` ya puesta. Nuevo modelo: **Borrador → Enviada → Aprobada/Perdida**, con **En corrección** como desvío lateral que el usuario marca a mano cuando una propuesta vuelve. **«Entregada» queda como valor legacy tolerado** (≈ Enviada). **Migrados los 18 `meta.json`** «Entregada»→«Enviada» (todas fueron enviadas; el outcome lo marca el usuario). `indexar.py` surfacea «En corrección» en su propia sección (cotización en pausa, fuera de la ventana de 30 días). Verificado: estampador correcto en los 3 casos + append-only intacto; índice → «Pipeline: Enviada: 18». [[project_idia_columna_vertebral_relacional]]

## 2026-06-17 — [arquitectura] Columna vertebral relacional `clientes/INDEX.{json,md}` (sync) + IDIA en conversación

El usuario pidió que el sistema funcione **como un OS** con **base de conocimientos relacional**, eligiendo backend **en archivos (sin nube)**, primer paso **columna vertebral + sync**, y nombre **IDIA** (cambio del depto. de Educación) **solo en conversación, sin tocar archivos de identidad aún**. **Construido:** `scripts/indexar.py` recorre los `meta.json` (§4.19, fuente fechada) y los enlaza en un modelo relacional Propuestas↔Clientes↔Dashboards → escribe `clientes/INDEX.json` (máquina) + `clientes/INDEX.md` (vista legible: pipeline por estado/división, **cotizaciones en su ventana de 30 días** §3 como señal de OS, clientes recurrentes, y las 46 carpetas **a oscuras** listadas como *pendiente backfill*, no escondidas). División = best-effort desde `brief.md` (respaldo: ruta del logo), «?» si no hay señal — **no inventa** (§4.9). **Sync** enganchado en `generar-pdf.sh` tras `estampar-entrega.py`: cada entrega reindexa sola (no bloquea si falla). Estado real revelado: **18/64 registradas, las 18 en «Entregada»** (pipeline de ventas Enviada/Aprobada/Perdida **sin rastrear**), 46 sin `meta.json`. **Decisiones del usuario pendientes** (ofrecidas, no ejecutadas): backfill de las 46 · pipeline de ventas vivo · automatizaciones n8n/hooks · alcance del rename IDIA. [[project_idia_columna_vertebral_relacional]]

## 2026-06-17 — [preferencia] Crear slides/componentes nuevos brandeados a la medida = valor (sin romper lo canónico)

El usuario elogió explícitamente el patrón de **diseñar componentes nuevos a la medida** (`.rmx-band` timeline secuencial en el re-enfoque de Laboratorios Farma; antes `s-graph` grafo Obsidian en CAP-060, `s-demo` stepper mes a mes en fivenca-acompanamiento) en vez de recombinar mecánicamente o forzar el contenido en un molde que no le queda: *«no rompes el diseño estandarizado, sino que aportas valor creando algo nuevo y sumándolo a lo ya conocido»*. **Regla:** cuando el caso lo justifique, crea el componente nuevo **respetando** estructura canónica, paleta §4.1 y tokens de marca (`--gradient-warm`/`--yellow`/`--orange`/`--black`/fonts), con su CSS en `overrides.css` (selectores propios, sin pisar el base) y certificado con `verificar-overflow.js` + revisión visual. Suma, no reemplaces; si el contenido entra bien en una slide canónica, úsala. [[feedback_slides_a_medida_brandeadas]]

## 2026-06-17 — [cliente:laboratorios-farma] Re-enfoque de las 3 fases por feedback de ventas + mapa de proyecto secuencial (`rmx-band`)

Ventas devolvió la propuesta CAP-049 por **no ser fiel al requerimiento conversado**: la estructura de 3 fases se reordenó. **Antes** (Formación por competencias → Gobernanza/AUP → Medición de ROI). **Ahora**: **Fase 1 Fundamentos** (productividad y efectividad, = lo que ya estaba) → **Fase 2 Especialización por áreas** (capacidades transversales: datos/análisis · contenido/comunicación · procesos/documentación, cada una con **proyecto por área**) → **Fase 3 Capacidad propia** (automatización y agentes con el equipo de TI · **Centro de Excelencia de IA** · gobernanza y políticas). Decisión clave: la **medición de ROI no se elimina** (era el pilar #1 de la cuenta), se **absorbe dentro del Centro de Excelencia** (F3, módulo II). Stack de agentes/automatización **multi-herramienta** (Copilot Studio + Power Automate dentro del entorno Microsoft, n8n/Claude donde aporten más valor; §4.11: «dentro de su entorno», no migración). **Aprendizaje reusable de diseño:** cuando un deck multi-fase pasa de **paralelo** (F1 origen → bifurcación → F2‖F3 → convergencia → ★, el `rmx-journey` de Damasco) a **secuencial** (F1→F2→F3→★), el diagrama de fases debe **rehacerse como timeline vertical** (nuevas clases `.rmx-band` en `overrides.css`: 3 bandas con riel de gradiente + nodo F#, head tag/name/meta y 3 facetas horizontales, + ribbon ★ con tag «cotización única»); el fork/merge ya no representa la realidad. **Dos defectos §4.10 cazados solo en revisión visual** (el detector no los caza): (1) **Entregables AcroForm clipaba** con 8 ítems que envolvían a ~13 líneas → cura a **8 líneas de un renglón** (≤ ~30 chars; refuerza [[project_entregables_lineas_cortas]] y el caso fivenca-acompanamiento); (2) el `block-value` de **Duración** a 3 líneas **solapaba** el label «Programa» de la slide económica → acortar a ≤ 2 líneas. Detalle en `clientes/propuestas/laboratorios-farma/brief.md` (sección Re-enfoque). [[project_laboratorios_farma_cap049]]

## 2026-06-17 — [cliente:fivenca-acompanamiento] Nuevo formato «acompañamiento continuo» (CAP-062) · 3 meses, 4 h/semana, sobre los proyectos del cliente

Primer deck de **acompañamiento continuo** (no una capacitación de currículo cerrado): Intezia **guía** a un grupo selecto de Fivenca durante **3 meses, 4 h/semana (2 sesiones de 2 h, ~24 sesiones)** para que **ellos** construyan, automaticen y optimicen sus **proyectos reales** hasta dar resultados; se reevalúa al cierre. **4ª carpeta Fivenca**, clon de `fivenca-fundamentos-ia` (linaje cumbre→anabella, ya anclado a Fivenca: sector, estudios de impacto, marco sin-Copilot). **Modelado sobre la canónica mono-fase**, sin pilotes (memoria multifase-currículo): la slide de **Programa (`s-program`) se reusa como las 3 fases mensuales** (3 cards I/II/III «Diagnóstico y nivelación · Construcción guiada · Optimización y resultados»; cada `.obj` cierra con «Resultado: …»; cifras en el título, no en la `.meta`). La slide de **cronograma (`s-schedule`) se reconvierte en «una semana tipo»**: `timebar` de **2 segmentos 50/50** (Sesión 1 Taller aplicado · Sesión 2 Revisión y optimización), `ruta-node` con glifo **↻** + step «Ciclo semanal · se repite durante los 3 meses». **Metodología ABR re-acuñada al diferenciador**: «Acompañamiento, no entrega» (el resultado y la capacidad quedan en el cliente, no en Intezia) · «Sobre proyectos reales» · «Revisión y optimización continua». Eje **Claude protagonista + automatización (n8n)**, ecosistema-agnóstico (§4.11: el grupo selecto **ya maneja Claude** y lo profundiza; no es adopción org-wide ni migración de stack). Grupo **sin nº ni áreas definidas** → copy genérico «tu proyecto / el grupo selecto». Dupla **Andrés Fornerino + Isaac** en Beneficios (como el express), **María Iribarren** en el cierre. Precio: slide estándar `s-price`, Duración «3 meses · 4 h por semana», comercial vacío para ventas; reevaluación trimestral va en el copy (Fase 3/metodología), no en campos. **Slides «demo mes a mes» (`s-demo`, slides 5-7, a pedido del usuario):** 3 slides que demuestran la dinámica concreta de cada mes (como ritmo semanal pero por mes) para que el cliente la visualice; maqueta propia en `overrides.css` (stepper de meses `is-active`/`is-done` + flujo «Qué traes → Qué hacemos juntos → Con qué sales», 3ª tarjeta = resultado en amarillo + franja «Al cierre del mes»). **Dinámica genérica, sin proyecto-ejemplo** (aún no se conocen sus proyectos). Estáticas, sin AcroForms; el `agregar-campo-precio.py` ubica los campos **por contenido**, así que insertar slides NO rompe los AcroForms (Beneficios/Económica/Pasos se re-detectan en su nueva página). 14 slides. **Frases viajeras re-acuñadas** (Objetivos «A dónde llevamos…» → «Autonomía real, en 3 meses.»; Impacto «La evidencia no deja lugar a dudas» → «Usar IA no es lo mismo que dar resultados.»; metodología «se aplica al día siguiente» fuera). **Trampa §4.10 cazada en revisión visual:** la caja AcroForm de **Entregables clipa el contenido** y `verificar-overflow.js` **no lo caza** (el texto vive en el `/V` del PDF, no en el HTML) → 7 entregables largos = ~14 líneas visuales > ~10 que caben; cura = entregables a **líneas de un renglón** (≤ ~28 chars). Deriva [[project_fivenca_acompanamiento_cap062]].

## 2026-06-16 — [cliente:clon-digital-claude] Deck genérico de catálogo «Crea tu Clon Digital con Claude» (CAP-060) + slide a la medida `s-graph` (grafo de Obsidian)

Primer deck **genérico de catálogo** (sin cliente, sin facilitador con nombre, sin asesora): se vende el mismo a varios públicos de perfil no definido. Clonado de `skalto` (mismo eje), genericizado: portada con descriptor neutro («Capacitación · 6 horas») en vez de nombre de cliente, footers `Intezia · Propuesta`, **cierre sin línea de asesora** (solo datos institucionales). Código **CAP-060** y rótulo «Capacitación» (el usuario la llama capacitación; CAP- = Capacitación In-Company). **Nueva slide a la medida `s-graph`** (slide 05, eje «04 · Tu segundo cerebro»): grafo relacional de **Obsidian** en `overrides.css` — slide oscura, nodo central «Tu clon» con resplandor + 6 categorías + notas-hoja, **dibujado con SVG `<line>` (aristas) + `<span>` absolutos posicionados por su centro** (left/top px = unidades del viewBox 520×540, `translate(-50%,-50%)`); el detector de overflow lo cubre igual que a cualquier slide. Obsidian además tejido en el currículo (Mód II «conocimiento y grafo»; Mód III «Conecta Obsidian al clon» vía MCP). Aprendizaje de overflow: alargar el `.obj` de un módulo de `s-program` con 6 temas desborda +19px → mantener `.obj` ≤ ~95 chars (la cura es el contenido, §4.10). `.hl` de marca = **caja amarilla + texto negro con padding** (igual que s-impact/s-cover), NO texto con degradado (`background-clip:text` quedó a medias en el render). Deriva [[project_clon_digital_claude_cap060]].

## 2026-06-16 — [cliente:apb-group-rh] Segundo Dashboard Edu-Trace del mismo cliente · departamento RRHH (N=8, Índice 95)

**APB Group** ya tenía un dashboard (`apb-group`, Tecnología/n8n, N=11). Ahora cerró su capacitación de **«IA para la Eficiencia en RRHH»** (Gemini aplicado a tareas administrativas y de talento) y subió su `encuesta.csv` de cierre. **Un mismo cliente puede tener varios dashboards Edu-Trace, uno por capacitación/departamento**: slug con sufijo (`apb-group-rh`) para no colisionar con la carpeta existente. Clonado del piloto **chart-forward** (`tu-herraje`: radar de ejes + donut rings de retención + donut de composición), **solo salida cliente** (sin interno, §11 desde 2026-06-10). N=8 (Gestión Humana 5 · Tecnología 2 · ITS 1). Resultados: **Índice 95/100, retención medida 100%, 5/5 estrellas**, salto percibido +1.3. **Bloque C de selección con los 8 idénticos y correctos** en las 3 preguntas → 100%. Clave deducida **por lógica pedagógica, no por repetición** (§4.18): objetivo = automatizar lo administrativo para liberar tiempo estratégico · prompt = rol/contexto/formato · principio = supervisión humana + ética; las tres son la respuesta textualmente correcta de una formación RRHH, así que el 100% es legítimo (no un acierto colectivo falso). **Honestidad de muestra (§4.17):** solo Gestión Humana (n=5) se destaca con su índice (94); Tecnología (n=2) e ITS (n=1) se marcan **referenciales**, no se rankean. Donut de composición de 3 segmentos (clases `seg-gh`/`seg-tec`/`seg-its`, circunferencia 490.09: 306.3/122.5/61.3 con offsets acumulados). Verificador OK: overflow 0, PII 0 (cédula/correo nunca en JSON ni HTML), em-dash 0, cohort 0; 10 slides revisadas a ojo. Deriva [[project_apb_group_rh_dashboard]] · piloto [[project_tu_herraje_dashboard]].

## 2026-06-12 — [bug] El badge `.rmx-badge` (slide de fases) tiene ancho acotado y el detector NO lo caza

En Bit Honor CAP-054 puse `<span class="rmx-badge">Cotizado ahora · 18 h · 15 personas</span>` y «PERSONAS» se salía del pill: el `.rmx-badge` del journey (`s-roadmap`, clon cumbre/damasco) está dimensionado para un texto corto tipo «Cotizado ahora · 18 h». **`verificar-overflow.js` dio OK** (el texto desborda el borde visual del pill pero queda dentro de los límites de la slide), así que el corte solo se ve a ojo en el PDF. **Reglas:** (1) el `rmx-badge` se mantiene ultra-corto (≤ ~22 chars); el total de participantes va en las tarjetas de ruta (5 + 10 personas), no en el badge. (2) Revisar SIEMPRE a ojo la slide de fases aunque el detector pase: pills, nodos y chips de ese diagrama pueden desbordar su caja sin salirse de la slide. Caso base: 2026-06-12 Bit Honor (slide 03).

## 2026-06-12 — [arquitectura] Registro fechado de entregas (`meta.json` por carpeta + hook en `generar-pdf.sh`)

Antes no había fuente determinista para «qué propuestas se entregaron en tal semana»: 60 carpetas en `clientes/propuestas/` sin fecha de entrega ni estado (solo 8 tenían `acroforms.json`, que guarda contenido, no metadata). Adivinarlo por mtime o git omite entregas reales e incluye ruido. **Solución de 3 piezas:** (1) un **`meta.json` por carpeta** con `{codigo, cliente, tipo, eje, estado, fecha_entrega}`; estados `Borrador → Entregada → Enviada → Aprobada / Perdida`; nace en `Borrador`/`null`. (2) **Hook en `generar-pdf.sh`** → llama a `scripts/estampar-entrega.py`: como toda entrega pasa por ese script, al generar el PDF estampa `fecha_entrega` (si vacía) y sube `Borrador→Entregada`; **append-only**, nunca pisa estado manual (`Enviada/Aprobada/Perdida`) ni fecha ya puesta; sin `meta.json` imprime **advertencia visible** (no falla en silencio). (3) Regla **§4.19** en CLAUDE.md + puntero en §6 Paso 3 + nota de **resetear `meta.json` al clonar** (`cp -r` arrastra el del origen). **Backfill:** creados 13 `meta.json` (`estado: Entregada`) para las entregas del 5–11 jun (crediya, intezia-ventas-claude, colchones-regal, ninja-park, venemergencia, anabella, laboratorios-farma, corporacion-bel, joalca, patricia, skalto) + meru/bit-honor (12 jun, hoy); las ~52 legacy no se backfillean. Probado end-to-end con Chrome: Borrador→Entregada+fecha en run nuevo, Aprobada sin cambios al regenerar. Consulta: `find clientes/propuestas -name meta.json` + filtrar `fecha_entrega`.

## 2026-06-12 — [cliente:meru] Capacitación In-Company CAP-056 «Claude de la A a la Z» · 6 módulos/12h, setup técnico Venezuela

**Meru** (contacto Loredana): alianza de **4 mujeres profesionales independientes** (distintas empresas/áreas, admin, 30-45, principiantes pragmáticas) que **ya pagan Claude Pro** y lo subutilizan. Clon de **crediya** (mismo eje Claude productividad/automatización, misma asesora María). Decisión del usuario: **6 sesiones/12h (6 módulos)** en vez de 5/10h, con un **módulo I dedicado al setup técnico de Venezuela** (acceso con VPN, app de escritorio, gestión de tokens/«barra de consumo») porque la fricción técnica es parte explícita del dolor. Ruta de 6 nodos (16.6/33.3/50/66.6/83.3/100%), 16 slides. **El override de programa de crediya ya cubre 6 módulos**: la regla `:has(.module:nth-child(5)):not(:has(:nth-child(7)))` aplica a 5 **y** 6 (grid 3×2), sin tocar CSS. Facilitador = **Equipo Education** genérico (avatar ED). Entregables a líneas cortas (7): repositorio de prompts maestros + plantillas por área + entorno Claude resuelto (VPN/app) + plan 30 días + workbook + encuesta + certificado. Modalidad **sin afirmar** («sesión en vivo»). **Trampa §4.9 cazada en revisión visual**: al adaptar la slide de Impacto cambié la barra central a «Tareas de redacción +40%» (cifra inventada, sin respaldo de las fuentes citadas) → **revertida** a la original vetada «Desarrollo de software +26%». Lección: las barras de Impacto son un set coherente con su fuente; no relabelar/recifrar una sola sin fuente nueva. Verificador OK + revisión visual slide por slide (cero overflow). **Ajuste posterior (mismo día, instrucción del usuario):** toda capacitación de Claude debe incluir **capacidades nativas como fundamento**, no solo prompting: (1) **qué modelo usar y cuándo** (Opus/Sonnet/Haiku) + **optimizar tokens** → reconvertí el Módulo II en «Fundamentos y modelos de Claude» (2.2 Opus/Sonnet/Haiku · 2.3 Optimizar tus tokens), y moví la privacidad a 3.3 y la interfaz a 1.3; (2) **Skills, plugins y conectores (MCP)** → el Módulo V pasó de «Projects: tu asistente adoctrinado» a «Projects, Skills y conectores» (5.2 Skills y plugins · 5.3 Conectores/MCP). MCP glosado en la slide de sesión (chip «Conectores (MCP)» + recurso «Conectores (Model Context Protocol, MCP)»); en la slide de Programa se evita la sigla cruda (5.3 «Conectores a tu suite») porque el chip compacto no admite glosa (§4.12.3). Refuerza [[feedback_claude_training_capacidades_actuales]]: los 6 módulos caben sin agregar uno (redistribución de temas).

## 2026-06-11 — [cliente:patricia] Capacitación express «Claude de principio a fin» · sesión única 2 h, SIN código

**Patricia** (trabaja en marketing pero quiere **Claude general**, no marketing): capacitación 1 a 1 **presencial de 2 horas** para recorrer la mayor cantidad de temas con **ejemplos en vivo** y que crezca por su cuenta. Marketing solo como guiño, no foco. Clon de **anabella** (capacitación 1-a-1 moderna con `acroforms.json`), reducido a **11 slides** (1 sola sesión = 1 slide de cronograma vs. 4): los 4 bloques (I Claude desde cero · II Crea en vivo · III Claude conectado · IV Lleva Claude más lejos) se recorren en la misma sesión; el cronograma usa 1 nodo de ruta al 100% y timebar de 4 segmentos (35/30/30/25). Tres decisiones del usuario: (1) **sin código** → quité el `span.codigo` de la portada (el PDF toma solo el título, "Claude, de principio a fin.pdf") y la Acreditación va **sin `[CÓDIGO]`** («Programa registrado en INTEZIA Education.»); (2) **facilitador = Isaac**, equipo de 1 persona; (3) **sin asesora de ventas** → fuera el segundo `.person` y la línea de asesora del cierre (queda Facilitador + Empresa). **Trampa cazada**: cambié el h2 de Beneficios a «Lo que te llevas» y `agregar-campo-precio.py` **no creó** Entregables/Acreditación porque busca el marker literal **«Lo que se llevan»** (con `requires:["Entregables"]`). Ese h2 debe quedar **literal** o los campos no nacen. MCP glosado en objetivos («conectores (MCP, Model Context Protocol)») y en lenguaje natural en el chip apretado del programa (§4.12.3). Impacto reusa fuentes reales del canónico (Stanford HAI 2026 · McKinsey 2025 · Anthropic Economic Index 2025), hook sin ancla de cliente. Verificador OK + 11 slides revisadas a ojo (cero overflow). Precio: slide presente, campos vacíos para ventas.

## 2026-06-11 — [cliente:corporacion-bel] Capacitación «Liderazgo Aumentado con IA» (CAP-055) · multi-herramienta sobre stack del cliente

**Corporación Bel**: 30 líderes y gerencia de primera línea, IA dispersa, quieren algo **práctico** (ya conocen lo básico). Eje resuelto contra la ficha, no contra la pregunta inicial: la ficha marca stack **Google + Microsoft** (Claude NO marcado en «ecosistema preferido»), así que el eje quedó **multi-herramienta sobre lo que ya tienen** (Gemini + Copilot) con **Claude como sparring estratégico** (complemento recomendado, nunca migración §4.11). Cuando la ficha contradice una respuesta previa del usuario sobre el eje, **prevalece la ficha y se confirma**. Clon **cumbre-andina** (13 slides, mono-fase), 3 módulos / 6 h (3 sesiones de 2 h): I Productividad en tu día a día · II Decidir mejor con IA · III **Efecto cascada** (diagnóstico de oportunidades por área → mapa de priorización → a quién capacitar después). Dos pedidos explícitos del cliente codificados en el deck: (1) **diagnóstico previo de nivel** = Paso 01 de «Cómo arrancamos» (formulario + kick-off entrevista, personaliza), y (2) **efecto cascada** = objetivo específico 3 + Módulo III + entregables (mapa de priorización + informe de desempeño). Modalidad **híbrida confirmada en ficha** → sí se afirma. Facilitación **Equipo Education**, asesora **Flavia Martínez** (`+58 414 5756615 · fmartinez@intezia.com`). Impacto con fuentes reales nuevas (Copilot 7.000 empleados 2025 · Generative AI at Work/NBER 2025 · McKinsey 2025 · EY); barra angosta +14% con `bar-fill--out`. Verificador OK + 13 slides revisadas a ojo.

## 2026-06-11 — [cliente:skalto] Taller «Crea tu Clon Digital con Claude» (TA-026) · producto de alianza

Alianza estratégica **Intezia + Skalto** (canal de referidos en Miami; referente: Gabriela, CEO de Skalto). Taller mono-fase **productizado**: Gabriela lo prueba sin costo y luego lo ofrece a sus referidos, incluso a grupos grandes (ej. 30 personas), por eso debe quedar **autónomo y replicable**, no hiper-personalizado. Clon de **cumbre-andina** (13 slides, mono-fase), 3 módulos / 6 h (3 sesiones de 2 h): I Fundamentos del clon (Claude + prompting) · II El cerebro (Projects + conocimiento + Skills + Claude Design) · III En acción (Conectores/Plugins/MCP + Cowork + automatización + uso seguro). Eje = **clon digital** (segundo cerebro/agente) construido con herramientas accesibles de Claude (no Claude Code terminal, que es lo técnico de la Fase 2 de Venemergencia; aquí se reencuadra a Projects/Skills para audiencia de negocio). Facilitación **Equipo INTEZIA Education** (sin nombre, replicable), asesora **Isabella Palazzone**, modalidad **sin afirmar** («sesión en vivo», se cierra en arranque). Deck a nombre de Skalto pero con copy genérico que cualquier empresa referida puede recibir. `acroforms.json` estándar; impacto reusa fuentes reales del canónico (Stanford HAI 2026 · McKinsey 2025 · Anthropic Economic Index 2025). Overflow s-program: 7 topics + h3/obj largos desbordaban +14px → bajar a **6 topics** por módulo + acortar títulos/obj (mismo patrón que cumbre). Verificador OK + 8 slides revisadas a ojo.

## 2026-06-10 — [cliente:joalca] Capacitación Gemini avanzado + Google Antigravity (CAP-053)

Representaciones Joalca (ficha Google Forms + correo de Flavia Martínez): gerentes y asistentes de Junta Directiva (15-20), manejan **Gemini básico**, quieren **dominar Google Antigravity** y salir con un proyecto. Enfoque acordado: profundizar lo que no conocen de Gemini (Gems, Deep Research, NotebookLM, Workspace) + grueso en **Antigravity con prototipo departamental**. Clon de **cumbre** (Capacitación mono-fase), 6 módulos / 6 sesiones × 2h presencial = 16 slides, modo compacto s-program 5-6 vía `overrides.css` (patrón sfic/corpoez). Facilitación = **Equipo Education** (sin nombre individual), asesora Flavia Martínez. **Encuadre honesto de Antigravity** (es plataforma agéntica de *desarrollo* sobre Gemini 3 Pro, pero audiencia no técnica): se vende como «dirigir agentes en lenguaje natural para prototipar herramientas internas SIN código; de la idea al prototipo, a producción con tu equipo técnico» — no se promete software en producción ni se afirma adopción previa. Impacto con datos reales citados (BCG/Harvard n=758 +25%/+40% · Forrester TEI Workspace +30% · Google Cloud ROI of AI 2025: 52% usa agentes / 74% ROI año 1). Verificador + 8 páginas revisadas a ojo: cero overflow. Pendiente: correo/teléfono directos de Flavia para el cierre (hoy `info@intezia.com`).

## 2026-06-10 — [cliente:laboratorios-farma][arquitectura] Plan integral 3 fases (formar/gobernar/medir)

Capacitación masiva sin ficha ni minuta, solo contexto de ventas (pilares: ROI post-capacitación + refuerzo, gobernanza estilo Eurobuilding, personalización metódica con proyecto final por módulo). **Arquitectura reutilizable de «plan integral»**: clon de cumbre (multi-fase tipo currículo de formación, NO pilotes) con 3 slides `s-program` de 3 cards para las fases (F1 Formación por competencias + 3 `s-schedule` con «Proyecto: …» por sesión · F2 Gobernanza: AUP/comité-roles/zona-no-uso · F3 ROI: línea base-KPIs/30-60-90 días/refuerzo). 16 slides, cero CSS custom, cero overflow. Eje **Copilot + multi-herramienta** (M365): Copilot columna vertebral, las demás como «apoyo cuando aportan más valor». **Bug de slide económica**: el `block-value` de Duración solo admite ~2 líneas (~85 chars); más largo se solapa con el eyebrow «Programa» y el detector de overflow NO lo caza (posición absoluta) → revisar slide 14 a ojo. **Código CAP-049** (se había usado CAP-053 por error; corregido a mitad de proyecto en todo el material y renombrado el PDF).

**Iteración con feedback del usuario (mismo día):** (1) **«cohorts» prohibido** → «grupos» (anglicismo, §4.4) — ver [[feedback_no_usar_cohorts_anglicismo]]. (2) Copilot sigue siendo la IA generativa **principal** (el usuario dijo «Claude» por error y corrigió); en Fase 1 se abre el repertorio con **creación visual con IA + notas de reunión (Fathom/Fireflies)** como apoyo. (3) **Slide de esferas obligatoria en toda propuesta por fases**: se agregó la slide `s-roadmap` (rmx, esferas de Damasco) como overview de fases — proyecta el WOW (F1 → F2/F3 → ★ organización transformada), reemplaza al mapa de tarjetas s-program. F2/F3 con «duración a coordinar». **BUG corregido** en `plantillas/slides/roadmap.css` (2 errores de sintaxis: `}` suelto + falta cierre de `.rmx-origin-bot`; ahora 64 llaves balanceadas). (4) **«cohort/cohorts» bloqueado** en `verificar-propuesta.sh` (check §4.4, revisa HTML + acroforms*.json) + documentado en CLAUDE.md §4.4. (5) **Desglose por proceso en TODAS las fases**: a petición del usuario, F2 y F3 reciben su propio desglose como la Fase 1 (deck 16→22 slides). Patrón reutilizable para fases sin tiempos: `s-schedule` SIN timebar + `ses-dur`=«A coordinar» + bloque `Procesos` (chips) + línea `En qué consiste` (clase `.ses-desc`, rellena el hueco del timebar y explica el proceso) + 3 columnas «Cómo lo construimos · Qué hace el equipo · Entregable». Convence al cliente de que no compra solo la Fase 1.

## 2026-06-10 — [plantilla][regla] Guía de redacción `plantillas/redaccion.md` (v1.1) — oficio positivo del copy

Auditoría de redacción de las 5 propuestas cerradas (venemergencia, damasco, tu-herraje, crediya, cashea) con subagentes haiku. Hallazgo central: las **frases viajeras** (hooks reciclados entre clientes, ej. «La diferencia no es la herramienta, es saber usarla» vendida a 3 clientes) no vienen de plantillas sino de la clonación — principal fuente del "suena robótico". Nace `plantillas/redaccion.md`: 5 reglas de oro con ejemplos verbatim del corpus ganador (dato operativo observado, cliente tejido en todo el deck, honestidad comercial, ritmo, resultado tangible), tabla viva de frases viajeras prohibidas, y checklist de redacción. **Validada con Isaac vía A/B sobre 3 slides reales**: metodología y módulos aprobados; hook calibrado a "punto medio" — re-acuñar como aforismo corto (≤~15 palabras) con UNA ancla del cliente, nunca estirar a narrativa larga. Decks entregados intactos; aplica a futuro. Pendiente: cablear a CLAUDE.md §5 y chequeo de frases viajeras en verificador.

## 2026-06-10 — [bug][plantilla] Diagnóstico (.s-pain): items centrados se veían caídos → flex-start en _base

El usuario rechazó la alineación del punto 01 del Diagnóstico en Anabella CAP-052: `.s-pain ol li` usaba `align-items: center` y la celda del grid se estira a la fila más alta, así que un item de 2 líneas junto a uno de 3 quedaba centrado (texto caído respecto a su número). **Fix de raíz en `_base/styles.css`**: `align-items: flex-start` + `padding-top: 3px` (compensación óptica con el dígito). Misma familia que `feedback_grid_alineacion_tope` (alinear al tope, nunca centrar, en grids multi-columna). Aplica a todos los clones futuros sin tocar decks entregados.

## 2026-06-10 — [cliente:anabella][scripts] CAP-052 con flujo acroforms.json + título ancla de Beneficios

Primera propuesta nacida con el flujo nuevo (`acroforms.json` + `customize-acroforms.py anabella`, sin script propio). Hallazgo: `generar-pdf.sh` ancla los campos `Entregables`/`Acreditacion` al **h2 literal «Lo que se llevan.»** de la slide de Beneficios; al personalizarlo a «Lo que te llevas.» el generador los omitió en silencio (solo 11 de 13 campos, con un «(omitido)» en el log). El h2 de Beneficios NO se personaliza. Deck: capacitación 1 a 1 híbrida, 4 módulos / 8 h, eje liderazgo + marketing (Google + Claude), sin creación visual.

## 2026-06-10 — [arquitectura][scripts][regla] Flujo acroforms.json + regla de subagentes haiku + fix §4.15 en generar-pdf.md

**Segunda ronda de optimización (mismo día).** (1) **Customize unificado:** `scripts/customize-acroforms.py` potenciado — modo carpeta (`customize-acroforms.py <slug>` localiza el PDF único y lee `acroforms.json` de la propuesta), valores como listas (se unen con `\r`), títulos de pasos a 14 pt + borrado de `/AP` (el estándar de los 14 customize recientes) y aviso de campo no encontrado. **Las propuestas nuevas ya no clonan un `customize-<slug>.py`** (~1k tokens y riesgo de heredar textos de otro cliente): declaran `acroforms.json` (ejemplo en `_base/acroforms.ejemplo.json`); un script propio solo para casos especiales (resize `/Rect`, lógica condicional). Los 41 existentes se conservan y funcionan. `verificar-propuesta.sh` acepta `acroforms*.json` como par válido y aplica el chequeo §4.15 también al JSON; `generar-pdf.sh` sugiere el comando correcto según exista script propio o JSON. Probado en copia (/tmp): 3 modos OK, 8 campos, negrita re-horneada. (2) **Regla en §5:** lecturas masivas (auditorías, comparaciones, inventarios) se delegan a subagentes haiku que devuelven solo el hallazgo; la lectura §4.14 de lo que se va a editar sigue siendo directa. (3) **Bug §4.15 cazado en `plantillas/generar-pdf.md`:** la «pauta estándar de los 3 pasos» aún decía «firmar acuerdo + factura del 50 % de anticipo» — contradicción directa con la regla bloqueante; reescrita a logística (fechas · acceso y logística · arranque). (4) Tabla de 13 campos AcroForm deduplicada: vive solo en `generar-pdf.md` (propuesta-comercial.md apunta). (5) Extracción de bloques del workbook **descartada** a propósito: el `index.html` canónico es fuente de clonado; partirlo en dos archivos añade riesgo estructural por ~1.5k tokens únicos.

## 2026-06-10 — [arquitectura][regla] Optimización de tokens del sistema + propuestas entregadas = inmutables

**Disparador:** auditoría de consumo de tokens (subagentes haiku sobre todo el repo). Hallazgos: la lectura §4.14 costaba 25–28k tokens por modificación (releer el clon canónico completo cada vez), `aprendizajes.md` tenía 60 entradas (3× el límite de ~20) con 27k tokens, CLAUDE.md cargaba ~2k tokens de narrativa histórica por sesión, y 10 fichas de memoria duplicaban reglas §4 ya codificadas. **Cambios:** (1) rotadas 42 entradas de mayo al `aprendizajes-historico.md` (104 KB → 41 KB); (2) **nuevo `plantillas/estructura-canonica.md`**: referencia compacta de cumbre-andina (13 slides) y pilotes-perforados (14 slides) — §4.14.6 ahora apunta ahí y el `index.html` del clon canónico solo se lee ante duda no resuelta; (3) párrafos «Aprendizaje base» de §4.10–§4.15 comprimidos a una línea con puntero al histórico; (4) depuradas 10 memorias redundantes con §4/§6/§10 (índice anotado); (5) eliminado `catalogo-viejo.pdf.pdf` (899 KB de basura en la raíz). **Regla nueva (§6 Paso 0): nunca clonar un deck legacy** (styles.css local copiado, cronograma `.sessions` viejo sin `.ruta`): por ahí se colaban los diseños del pasado (desglose en tabla) a propuestas nuevas. **Directiva del usuario (bloqueante): las propuestas ya producidas NO se modifican** — la optimización aplica solo a futuro; tocar un deck existente (aunque sea para deduplicar CSS o limpiar formato viejo) requiere consultarle antes y solo si genera conflicto activo de diseño. Memoria `feedback_no_tocar_propuestas_entregadas`.

## 2026-06-10 — [arquitectura][regla][scripts] Dashboard Edu-Trace = salida única de cara al cliente (se retira el deck interno)

**Disparador:** el usuario indica que ya no se debe emitir nunca más un dashboard interno además del de cara al cliente: el doble deck encarece y hace menos eficiente el proceso. **Decisión (AskUserQuestion):** se elimina **todo lo interno**, no solo el deck — fuera `index-interno.html`, `_INTERNO · <Cliente>.pdf` y la nota `siguiente-venta.md` (cierre de ciclo). El Bloque E vive solo como «recomendaciones de expansión» de valor en el deck cliente. **Cambios:** (1) `CLAUDE.md §11` (paso 4 un solo deck, paso 6 un solo HTML, paso 7 «cierre de ciclo» eliminado), nota de §11 + §4.16.3 sin «cliente e interno», estructura §7 a `index-cliente.html`; (2) `plantillas/dashboard-edutrace.md` §1 salida única + nota de retiro, §5 tabla sin columna «Cliente vs Interno», §6 «Cierre de ciclo» eliminada (privacidad renumerada §7→§6, referencia cruzada actualizada en §4.16); (3) `plantillas/generar-dashboard.md` §0 estructura, §3/§4/§5 un solo HTML/PDF, §6 eliminada; (4) `scripts/generar-dashboard.sh` sin `HTML_INT`/`PDF_INT` ni render interno. **Retroactividad:** los dashboards internos ya generados se conservan donde estén; la regla aplica solo a futuras generaciones. Memoria `feedback_dashboard_solo_cliente`.

## 2026-06-09 — [cliente:tu-herraje][preferencia] Dashboard Edu-Trace «Tu Herraje» (Marketing/Gemini, N=2) · variante CHART-FORWARD (más gráficos, menos métricas)

**Disparador:** el usuario pide el dashboard de cierre del taller de Tu Herraje y aclara que «el diseño a nivel de información está genial pero queremos **más gráficos y menos métricas**». **Datos:** N=2 (Sandra Esquivel · Marketing, Emily Silva · Diseño gráfico); taller de **marketing de contenidos con IA** (Gemini, buyer persona, ventana de contexto, consistencia de tono). Índice **85/100**, retención objetiva (Bloque C medido) **67%** (4/6: buyer persona 50%, ventana de contexto 50%, tono entre piezas 100%), salto percibido +1.5, Bloque D **todo 5.0**. **Decisiones (AskUserQuestion):** N=2 confirmado (muestra referencial, **sin ranking entre áreas**) · título «Marketing Estratégico y Generativo» (TA-005) · facilitador **Juan Figuera** (metadato) · **sin asesora** en la slide de cierre (se elimina la línea de asesora, queda solo Empresa). **Rediseño chart-forward (clave):** se clona el piloto `apb-group` pero se sustituyen las cajas de número grande por **gráficos SVG/CSS puro** (cero dependencias → render fiable en Chrome headless + pasa `verificar-overflow.js`): slide 03 «Desglose por eje» → **radar de 4 ejes** (en vez de 4 cards de métrica) con leyenda compacta a la derecha; slide 05 «Retención» → **3 donut rings** (50/50/100) en vez de filas de %; slide 06 «Por departamento» → **donut de composición** del grupo (Marketing/Diseño 50/50) en vez de hbars con ranking (n=1 por área no se rankea). Gradiente `url(#warm)` definido una vez en un `<svg>` oculto al abrir `<main>`. **Inteligencia comercial (interno):** Bloque E → Ventas objetivo #1 (TA-008 IA para Ventas) + imagen/video con IA (TA-009 Producción Audiovisual) + sesión de refuerzo de estrategia para subir la retención. **Verificación:** overflow 0 en ambos decks · PII 0 (cédula/correo fuera de JSON y HTML; solo la palabra «cédula» en comentarios §4.16) · sin guion largo en HTML (los `—` viven solo en comentarios CSS) · revisión visual de las 10 slides por imagen (charts renderizan perfecto). **Patrón nuevo:** los dashboards Edu-Trace pasan a **chart-forward** por preferencia del cliente — priorizar radar/donut/barras sobre números grandes; el piloto canónico sigue siendo `apb-group` (metric-heavy) hasta confirmar si se migra el estándar. Memoria `feedback_dashboard_chart_forward` + `project_tu_herraje_dashboard`.

## 2026-06-09 — [cliente:venemergencia][arquitectura][scripts] CAP-047 reenfocado: DOS decks en una carpeta (Fase 1 práctica + Fases 1+2 con clon digital) · multi-deck en scripts

**Disparador:** el usuario pide subir el valor de Venemergencia: (1) Fase 1 más **práctica** (que el directivo salga con **procesos automatizados** desde la F1) sumando **Cowork, Conectores, Plugins, Claude Design** y un toque de Claude Code dentro de la app; (2) **dos propuestas en la misma carpeta** — Deck A solo Fase 1, Deck B Fases 1+2 con la Fase 2 reescrita como **inmersión técnica en Claude Code (terminal/IDE)** donde cada gerente construye su **clon digital** («segundo cerebro» que apoya decisiones y automatiza trabajo). **Decisiones (AskUserQuestion):** cascada como *porqué* pero **F3 retirada** del relato · Fase 1 = **5 módulos/10 h** (mismo tamaño, contenido nuevo: I Fundamentos · II Ecosistema+Claude Design · III Cowork+Skills · IV Conectores/Plugins/MCP/automatización · V Seguridad+cierre cascada) · Fase 2 = **6 sesiones/12 h** (Claude Code a fondo → diseño/construcción del clon → conexión MCP → automatización de decisiones → seguridad/producción) · **mismo CAP-047, dos alcances** (Deck A `CAP-047`, Deck B `CAP-047 · Fases 1+2`). **Arquitectura (clave):** dos HTML en la misma carpeta — `index.html` (Deck A, 16 slides) + `index-completo.html` (Deck B, 22 slides) — con `generar-pdf.sh` y `verificar-propuesta.sh` **generalizados** para aceptar un **2º arg opcional con el nombre del HTML** (`HTML="$DIR/${2:-index.html}"`, aditivo, cero regresión; `verificar-overflow.js` ya aceptaba ruta `.html`). Cada deck su `customize-venemergencia[-completo].py`; los PDFs no colisionan porque el nombre sale de `span.codigo`+`h1`. **Roadmap linealizado:** se quitó la bifurcación F1→F2/F3 del clon BDV; ahora F1 → F2 → ★ con conector `.rmx-link` (barra horizontal) en `overrides.css`; las rutas/fork/merge viejas quedan sin uso. **Bug visual (NO lo caza el detector):** la caja **Entregables del Deck B desbordó** — líneas de Fase 2 largas («Un clon digital funcional en Claude Code.») envolvían a 2 renglones. Fix: acortar cada entregable a **un renglón** en el customize («Clon digital en Claude Code.», «Agente conectado a tus apps.»…). Reconfirma `project_entregables_lineas_cortas`. **Reglas:** §4.12 MCP glosado en cada slide donde aparece · §4.11 el clon **se integra sin cambiar su stack** · §4.15 pasos logísticos. Ambos decks: verificar-propuesta + overflow OK, par PDF-customize corrido, revisión visual por imagen (A: 4/5/9/10/12; B: 4/5/11/14/18). Memoria `project_venemergencia_claude_cascada` actualizada. **Patrón nuevo:** **varios decks por carpeta** = `index.html` canónico + `index-<variante>.html`, scripts con 2º arg HTML, un customize por deck.

## 2026-06-09 — [cliente:ninja-park] TA-025 Ninja Park · Intezia Fundamentals re-enfocado a reportes y datos (clon cumbre, online síncrono, 4 gerentes)

**Disparador:** ficha «Preguntas Clave» (solicitante Flavia Martínez) + contexto de ventas. Ninja Park Barquisimeto (parque de trampolines), gerencia (Gerente General, Sub Gerente, Administradora) que parte de **cero en IA** y arma a mano los reportes mensuales (estadísticas, gráficas, comparación de resultados, métricas, costos y gastos). Ventas pidió tomar **Intezia Fundamentals · IA + Productividad (TA-003)** como base y re-enfocarlo a esos cuellos de botella. **Decisiones del usuario (AskUserQuestion):** facilitador = **Equipo Education sin nombrar** (como la plantilla de catálogo), asesora = **Flavia Martínez** (`fmartinez@intezia.com`, +58 414 5756615, tomado de ubii-pagos), código = **TA-025** (siguiente Taller de la serie TA-, no CAP), **con** slide de precio (campos vacíos). **Construcción:** clon de `cumbre-andina/` (canónico mono-fase, `_base/styles.css`, 13 slides con Impacto). 6 h = 3 sesiones × 2 h → **3 módulos** (uno por sesión), no 5 (evita el problema de compactación 5-6 módulos del `_base`). Eje re-pesado a **Gemini + Google Workspace/Sheets** (ecosistema Google = preferencia explícita de la ficha; Microsoft/Copilot fuera). Módulos: I Fundamentos + primer reporte (RCTF) · II Datos, métricas y gráficas en Sheets (costos/gastos) · III Reportes automatizados (plantilla + Gem) + uso responsable. **§4.9 Impacto** con estudios reales citados verbatim: Noy & Zhang (*Science* 2023: −40% tiempo / +18% calidad en redacción), McKinsey (*The State of AI* 2025: 78% usa IA, 71% IA generativa), St. Louis Fed/RTPS 2025 (2.2 h/sem ahorradas, 1 de 3 usuarios diarios ahorra 4+ h) — verificadas con WebSearch. **§4.11:** el deck se apoya en «el entorno Google que ya conoce» sin afirmar que adoptó Gemini ni que migra. **§4.12:** RCTF glosado (Rol, Contexto, Tarea, Formato) en Objetivos y Programa; en chips se escribe natural. **§4.15:** pasos = logística pura (fechas · acceso de los 4 participantes y agenda · kick-off). **Facilitador sin nombrar:** bloque de equipo usa «Equipo INTEZIA Education» + «Coordinación Intezia» (avatares IE/PM). **Bug visual (revisión slide-por-slide, NO lo caza el detector automático):** la caja **Entregables desbordó** en la 1ª pasada — 7 entregables con frases largas («Asistente de IA para reportes (Gem)», «Workbook digital por participante») envolvían a 2 renglones y la última línea («Certificado de participación INTEZIA») se recortaba abajo. **Fix:** acortar cada entregable a **un renglón** (≤~28 chars) en el customize («Asistente de reportes (Gem)», «Workbook digital», «Certificado INTEZIA»…). Reconfirma `project_entregables_lineas_cortas`: el detector de overflow NO ve el desborde de campos AcroForm rellenados por el customize; solo la revisión visual del PDF. Par PDF-customize corrido, verificar-propuesta OK, 13 slides revisadas a imagen. Memoria nueva: `project_ninja_park_ta025`.

## 2026-06-08 — [cliente:colchones-regal][preferencia] CAP-043 ajustado: COTIZACIÓN ÚNICA de ambas fases + slide de fases estilo s-program (mapa BDV) + Isaac retirado del equipo

**Disparador:** tres correcciones del usuario sobre el deck ya entregado. **(1) Slide de fases (03):** no le gusta el track de flechas `.rm-*` viejo («ya lo he mencionado antes»); quiere el **DIAGRAMA tipo journey de la slide 11 de DAMASCO CAP-037** (`.s-roadmap` con `.rmx-*`: nodo origen circular → bifurcación con ramas curvas → una ruta/tarjeta por fase con nodos F1/F2 → convergencia → nodo destino ★ con resultados + franja de alcance). **Iteración:** primero probé tarjetas `s-program` (estilo «Mapa del Plan» de BDV) y el usuario aclaró que NO, que era el diagrama de Damasco. Fix final: slide 03 = `s-roadmap`, CSS `.rmx-*` clonado de Damasco al `overrides.css`, contenido adaptado (origen «Capacitación in-company 18 h» → Fase 1 Marketing / Fase 2 Desarrollo → destino «operación con IA de punta a punta»; franja «una sola propuesta, cotización única»). **Regla en memoria (corregida):** `feedback_slide_fases_estilo_program_no_roadmap` = el diagrama de Damasco, NO s-program ni rm-*. **(2) Cotización única:** el usuario decide UNA sola cotización para ambas fases (revierte el patrón de 2 cotizaciones del cambio anterior). Fix: slide 20 migrada de la `s-invest` a medida a la **canónica `s-price`** (título «Propuesta Económica» → el script compartido `agregar-campo-precio.py` crea los 5 campos estándar PrecioBase/Descuento/PrecioTotal/Programa/Notas). Se eliminó el bloque `.s-invest` de `overrides.css` y la inyección de 7 campos del `customize-colchones-regal.py` (ahora el customize solo pre-llena Entregables/Acreditación/Pasos). Duración = «18 horas en total». **(3) Barra de equipo:** Isaac (Fase 2) retirado por instrucción del usuario → quedan 2 personas (Equipo Education + Isabella). Con el override de 3 col, Isabella quedaba descentrada y con hueco a la derecha; fix: **eliminado el override de 3 col** → vuelve al canónico de 2 col del `_base` (`1fr 1fr`, como cumbre), Isabella llena la mitad derecha. Rol del Equipo Education generalizado de «Facilitación · Fase 1» a «Facilitación» (cubre ambas fases). verificar-propuesta + overflow OK, par PDF-customize corrido, revisión visual p.3/18/20. Memorias `project_colchones_regal_manychat` y `MEMORY.md` actualizadas. **Patrón:** la económica de **cotización única** es la canónica `s-price` (la maneja el script compartido); el patrón de N-cotizaciones-en-una-slide a medida solo aplica cuando hay varias cotizaciones reales.

## 2026-06-08 — [cliente:colchones-regal] CAP-043 reestructurado a DOS fases separadas y AMBAS cotizadas (Marketing 8h + Desarrollo 10h 1-a-1) · 22 slides · Económica única de dos cotizaciones

**Disparador:** el usuario deja de unir ambos departamentos. Ahora son **dos formaciones independientes, ambas cotizadas en el mismo deck**: **Fase 1 · Marketing** (8h, 4 sesiones de 2h, Equipo Education) con IA generativa (**Gemini** copy, **Higgsfield** imágenes y video) + primer bot de Instagram con **ManyChat**; **Fase 2 · Desarrollo** (10h, 5 sesiones de 2h, **1 a 1 con Isaac**) IA agéntica con **n8n** para agente conversacional **omnicanal** (Instagram + WhatsApp vía Kommo o conexión directa) que centraliza el seguimiento. **Cada fase con su propio desglose instructivo y horas.** **Parámetros fijados con el usuario (4+2 preguntas):** sesiones de 2h en ambas; **modalidad SIN afirmar** («sesión en vivo», recursos neutros, modalidad al paso de arranque); Fase 1 = Equipo Education, Fase 2 = Isaac; asesora Isabella; **CAP-043 para ambas fases**; desglose **1 slide por sesión** (4+5=9 slides); Económica **una sola slide** de dos cotizaciones (corrección en vivo del usuario, antes había pedido 2 slides). **Estructura 14→22 slides:** portada + diagnóstico + mapa «Las dos formaciones» (reusa `s-roadmap`, ambas «Cotizada») + [Fase 1: objetivos/programa 4 mód/4 desglose] + [Fase 2: objetivos/programa 5 mód/5 desglose] + ABR + Beneficios (2 perfiles de egreso + Entregables + Acreditación, equipo de 3) + Impacto + **Económica de dos fases** + pasos + cierre. **Decisión técnica clave (Económica única de 2 cotizaciones):** el script compartido `agregar-campo-precio.py` solo coloca UN juego de campos por página (multi-instancia es por-página, no sirve para 2 cotizaciones en 1 slide) → la slide se titula **«Propuesta de inversión»** (sin la cadena «Propuesta Económica» que busca el marker) para que el compartido la **omita limpiamente**, y los 7 campos (PrecioBase/Descuento/PrecioTotal ×2 fases + Notas compartida) se **inyectan a medida en `customize-colchones-regal.py`** con coordenadas pt PDF que matchean los frames CSS de `overrides.css` (factor 0.75) + JS de autocálculo por fase. Cero cambios al script compartido. **Otros:** Programa Fase 2 (5 módulos) necesita compactado en `overrides.css` local (`_base` solo fija min-height para 5-6, memoria `feedback_base_program_5_6_modulos`); Beneficios con equipo de **3 personas** → grid 3 col + color del 3er avatar en overrides. verificar-propuesta + overflow OK (22 slides), par PDF-customize corrido, revisión visual p.1/3/4/5/9/11/16/18/20. PDF viejo de 1 fase eliminado. Memoria `project_colchones_regal_manychat` actualizada. **Patrones:** (a) **dos formaciones cotizadas en un solo deck** = bloques Objetivos+Programa+Desglose por fase entre secciones compartidas (diagnóstico/ABR/impacto/pasos/cierre); (b) **Económica con N cotizaciones en una slide** = titular distinto de «Propuesta Económica» para que el compartido la omita + inyectar campos a medida en el customize del slug (no tocar el script compartido).

## 2026-06-07 — [cliente:intezia-ventas-claude] CAP-INT-01 · capacitación INTERNA «Claude para Ventas» (2 h, mono-sesión) para el equipo comercial propio · clon dr-care (sin precio) · 10 slides

**Disparador:** Isaac (facilitador) pidió un temario tipo deck-propuesta **pero interno** y **sin slide económica** para capacitar a su equipo de ventas en Claude. Nivel del equipo = **básico** (lo usan tipo ChatGPT, sin método). Foco hands-on = **su propio trabajo de ventas** (la opción «demostrar lo que vendemos» se pospone a una Capacitación 2). **Decisiones:** clon de `dr-care/` (taller sin precio, basado en facilitador) → 10 slides (1 sola slide de Programa con 3 módulos + 1 sola slide de Cronograma de sesión única, vs. las 2+2 de dr-care). Estructura curricular: **M-I Qué es Claude de verdad** (términos clave: Claude/Anthropic, contexto, Proyectos, Artifacts, conectores) · **M-II Cómo hablarle bien** (método RCTF + límites/alucinaciones) · **M-III Claude en tu día de ventas** (4 hands-on: investigar prospecto, redactar/seguimiento, resumir reuniones, responder objeciones, + montar Proyecto de ventas con ADN de Intezia). Cronograma = **agenda 2 h en una timebar de 5 segmentos** (10/25/20/50/15), ruta 100% «Sesión única · 2 horas». **Impacto (§4.9):** cifras nuevas verificadas por WebSearch — Brynjolfsson, Li & Raymond *Generative AI at Work* (NBER 2023): **+14%** soporte, **+34%** agentes noveles; Noy & Zhang *Science* 2023: **40% menos tiempo** redacción. Gancho de ventas «quien menos sabe, más gana» (el +34% novato), ideal para audiencia básica. **Barra angosta +14%:** `dr-care/styles.css` NO traía la clase `bar-fill--out` (solo robin-agency) → se copió la regla `.s-impact .bar-fill--out .bar-val{left:calc(100%+10px);color:var(--white)}` al styles.css local para sacar el valor del fill. customize-intezia-ventas-claude.py pre-llena Entregables (RCTF + biblioteca prompts + Proyecto configurado + 3 institucionales) + Acreditación (CAP-INT-01) + 3 pasos logísticos. verificar-propuesta OK, par PDF-customize corrido, revisión visual p.1-10. **Patrones:** (a) **capacitación interna sin precio** = clon de `dr-care/` (no cumbre, que sí trae s-price), facilitador propio (Isaac), cierre sin asesora de ventas; (b) **mono-sesión de pocas horas** = 1 slide Programa + 1 slide Cronograma con la agenda como timebar de N segmentos; (c) si la barra de Impacto es <~25% el valor no cabe dentro → clase `bar-fill--out` (puede no existir en el styles del clon, copiarla).

## 2026-06-07 — [cliente:crediya] CAP-048 · capacitación 1 a 1 sobre Claude (fundamentos→automatización) · clon cumbre · 5 módulos/5 sesiones · modalidad SIN afirmar · sin consultor nombrado

**Disparador:** propuesta para CrediYA (crédito/fintech), capacitación **1 a 1** donde el participante quiere aprender Claude de cero a avanzado y automatizar tareas repetitivas; objetivo comercial = que vea la utilidad **personal Y organizacional**. **Decisiones:** 10 horas, narrativa **personal → organizacional**, con slide de precio, **sin consultor asignado**, asesora María. Nombre del participante irrelevante para el deck; casos **realistas y posibles dentro de Claude** (nada de integraciones imposibles). **Correcciones del usuario en 2ª vuelta (clave):** (1) **NO había confirmado modalidad** → prohibido afirmar «online». Solución: neutralizar TODA mención de modalidad en el deck — ses-mod «Módulo X · **Sesión en vivo**» (síncrono sin comprometer presencial/online), recursos sin «Google Meet» («Sesión en vivo con el facilitador»), portada sin «formato online», paso 01 «fechas, **la modalidad** y zona horaria». brief/programa: modalidad «sin definir, a confirmar». (2) **5 módulos, sesiones de 2 h** (antes 3 módulos/3 sesiones 4+3+3): deck pasó de 13 → **15 slides** (5 schedule slides), ruta-fill en quintos (20/40/60/80/100), «Sesión N de 5», contadores /15. **Cómo se resolvió:** clon de `cumbre-andina/`. Programa 5 módulos arco personal→organizacional: I Fundamentos · II Prompting y verificación · III Claude en tu día a día · IV Automatiza con Projects y conectores · V De lo personal a lo organizacional. Estrategias adaptadas a **1 a 1** (acompañamiento/coaching 1 a 1, práctica individual; NO parejas/breakouts/plenaria). **Sin consultor nombrado** → equipo facilitador genérico en Beneficios («Facilitador Intezia»/«Gestión del proyecto», avatares IN/PM). **Slide Programa con 5 módulos:** el `_base` solo fija `min-height` para 5-6 módulos (no compacta) → se creó **`overrides.css` local** replicando el modo compacto del caso de 4 módulos pero en 3 columnas (3×2), con el mismo selector `:has(> .module:nth-child(5)):not(:has(> .module:nth-child(7)))`; enlazado tras `../_base/styles.css`. customize-crediya.py pre-llena Entregables + Acreditación (CAP-048) + 3 pasos logísticos (paso 01 = «5 sesiones»). verificar-propuesta OK, par PDF-customize corrido, revisión visual p.4/5/8/9. **Patrones:** (a) capacitación 1 a 1 = clon + estrategias individuales + equipo genérico si piden no nombrar consultor; (b) si la modalidad NO está confirmada, no afirmarla en el deck → «sesión en vivo» + recursos sin plataforma + modalidad en el paso de arranque; (c) Programa 5-6 módulos sobre `_base` exige overrides.css local (memoria `feedback_base_program_5_6_modulos`).

## 2026-06-05 — [cliente:colchones-regal] Replanteo CAP-043: WhatsApp sale de la Fase 1 (ManyChat falla con WhatsApp) → omnicanal a Fase 2 con n8n + Kommo/API directa · slide Hoja de ruta de 2 fases

**Disparador:** el usuario pide reenfocar el deck para que cada departamento (desarrollo incl.) tenga su «apartado funcional» y avisa que **ManyChat no se puede usar para WhatsApp** (da errores). Investigación de contexto: el deck/brief/programa de CAP-043 **prometían WhatsApp** en todo el Módulo III (perfil egreso, objetivo específico 3, chips de Sesión 3, recurso «WhatsApp Business») → choque real entre la decisión ManyChat y un requisito que el propio deck ofrecía. **Decisión final (tras 4 preguntas):** ManyChat **se queda solo para Instagram** en la Fase 1 (marketing, 6h/3 sesiones, sin cambios de duración); **WhatsApp y lo omnicanal se difieren a la Fase 2** (equipo de desarrollo) con **n8n** como hub + mensajería vía **Kommo o la API directa de WhatsApp** (las dos opciones, presentadas al cliente al llegar a esa fase). **Cambios:** (1) Módulo III reescrito de «Omnicanal y puesta en marcha» → **«Puesta en marcha y medición»** (bandeja/Live Chat de ManyChat, escalamiento a humano, buenas prácticas 24h, publicación, medición, mantenimiento) en index.html + programa.md; objetivo específico 3 «Unificar IG y WhatsApp» → «Centralizar las conversaciones de Instagram»; portada encuadra «primera fase»; quitado todo WhatsApp de Fase 1 (grep = solo aparece en la slide nueva). (2) **Slide add-on Hoja de ruta** (`s-roadmap`, custom con `.rm-*` en `overrides.css` local — NO la plantilla `roadmap.html`, que es metro-line de diagnóstico y tiene el CSS roto): dos tarjetas Fase 1 (Instagram/ManyChat/marketing) ↔ Fase 2 (omnicanal/n8n/WhatsApp/Kommo-API/desarrollo) + nota «por qué en fases». Insertada tras Impacto → deck **13→14 slides**, contadores y comentarios renumerados, eyebrow «08 · Hoja de ruta», Próximos pasos a «09». (3) brief.md actualizado (Fase 1 Instagram-only + Fase 2 n8n/Kommo/API). **Ajuste visual:** primera versión de la slide quedó top-heavy (mucho vacío abajo) → `.rm-phase min-height 372px` + listas `justify-content space-between` + fuentes +1-2px. verificar-propuesta + overflow OK (14 slides), par PDF-customize corrido (customize sin cambios, ya era Instagram-only), revisión visual de p.4/7/11. Memoria: `project_colchones_regal_manychat` actualizada. **Patrón:** ManyChat NO sirve para WhatsApp → en bots no-code, WhatsApp/omnicanal va a una Fase 2 con n8n (+ Kommo o API directa), no a ManyChat.

## 2026-06-05 — [cliente:venemergencia] Capacitación nueva CAP-047: adopción de Claude en cascada (train-the-trainer) · 3 fases, multi-fase clonada de cumbre (no pilotes)

**Disparador:** alianza Intezia + Venemergencia (servicios de emergencia). El cliente quiere adoptar Claude con modelo **cascada**: empezar por la capa gerencial (perfil multiplicador) y bajar por la pirámide. Grill-me previo resolvió todas las ramas. **Estructura de 3 fases (solo F1 cotizada):** F1 = adopción de Claude · 5 módulos · **10h en 5 sesiones de 2h** (1 módulo/sesión); F2 = Claude Code (roadmap); F3 = acompañamiento en réplicas masivas (roadmap, ya solicitado). Modelo **híbrido train-the-trainer** (formamos líderes para que repliquen). **Decisión de base (importante):** aunque el canónico multi-fase es `pilotes-perforados`, ese deck está modelado para un *diagnóstico* (Mapa de Calor, 2 sesiones de auditoría) y NO encaja con un currículo de formación. La F1 es una capacitación-currículo idéntica en forma a **`cumbre-andina`** (mismo eje Claude, usa `_base`, asesora María Iribarren ya correcta) → se clonó cumbre y la **narrativa multi-fase se llevó en la slide de programa** (s-program con 3 cards: F1 con sus 5 módulos como chips, F2, F3). 15 slides. **Ciberseguridad** (interés del cliente) = NO foco; se trató como Módulo IV «Seguridad e información sensible» con **protocolos reales y verificables de Anthropic** (datos de API no entrenan los modelos, retención 7 días, SOC 2 Tipo II / ISO 27001 / ISO 42001, HIPAA con BAA, Zero Data Retention) citando Centro de Privacidad + Trust Center (§4.9). Impacto con fuentes primarias: Noy & Zhang (Science 2023, +40% redacción), Brynjolfsson/Li/Raymond (NBER w31161 · QJE 2025, +14% atención / +34% novatos), McKinsey State of AI 2025 (88% usa IA, 72% gen-AI, solo 7% escalado → gancho cascada). Audiencia general/transversal (n y áreas a confirmar en kick-off, sin inventar). Slide económica incluida, precio vacío. **Sin consultor asignado** → «Equipo INTEZIA Education». Asesora María Iribarren. customize-venemergencia.py (Entregables del desglose + Acreditacion CAP-047 + 3 pasos logísticos §4.15). Par PDF-customize, verificar-propuesta + overflow OK, revisión visual 15/15. Memoria: `project_venemergencia_claude_cascada`.

## 2026-06-04 — [cliente:colchones-regal] Capacitación nueva CAP-043: bot de atención al cliente en Instagram con ManyChat (no-code, mono-fase)

**Disparador:** minuta + ficha de Colchones Regal (fábrica de colchones, venta detal/mayor). Dolor: alto volumen de DMs de Instagram desde anuncios pagados que la directora responde a mano y pierde clientes. El equipo de desarrollo de Intezia está copado → en vez de construirles el bot, **se les capacita para construirlo y mantenerlo solos** (autosuficiencia, sin retainer). **Decisión de herramienta (analizada con el usuario):** descartados Claude (ingeniería de software, inviable para el equipo/plazo) y n8n (sobra y complica para este perfil) → **ManyChat 100% no-code + IA nativa de ManyChat** (Intention Recognition + AI Step); el usuario decidió no integrar Gemini («no requieren algo tan escalable»). **Matices verificados con WebSearch que van al deck/brief (§4.9):** API de Instagram solo responde a quien escribió en últimas 24h (no DM en frío) + tope 200 llamadas/hora (2026); no afecta el caso. **Construcción:** clon mono-fase `cumbre-andina/` → 13 slides, 3 módulos = 3 sesiones × 2h (6h presencial, formato elegido por el usuario tras evaluar 6 vs 8h: sin la pieza técnica de Gemini, 6h es el tamaño correcto). Facilitador **Isaac Rodríguez** (el propio usuario), asesora María Iribarren (default institucional, a confirmar). Impacto con estudios reales: McKinsey gen-AI customer care (+45% productividad, ~30% menos volumen, ~25% menos tiempo de gestión), Gartner (deflection hasta 80%), HBR 2011 (7× contacto en 1ª hora), Lead Response Management Study/MIT 2011 (21× leads en 5 min). **Fix visual:** 3ª barra de Impacto «+20 pts» en barra angosta (20%) partía el valor en 2 líneas → cambiada a «25% menos tiempo de gestión» (McKinsey, valor corto que entra). customize-colchones-regal.py (Entregables del desglose + Acreditacion CAP-043 + 3 pasos logísticos §4.15). Par PDF-customize corrido, verificar-propuesta + overflow OK, revisión visual slide por slide. **Fase 2 (n8n + estudio de mercado + asistentes) mencionada en brief como evolución, no cotizada.** Memoria persistente: `project_colchones_regal_manychat`.

## 2026-06-04 — [cliente:ubii-pagos][bug] Propuesta nueva CAP-042 (auditoría de adopción de IA) + heatmap del clon multi-fase desborda +44px

**Disparador:** ficha de requerimientos + mensaje de ventas de Ubii Pagos (fintech de pagos): quieren un esquema de adopción de IA en dos fases (Fase 1 = auditoría/levantamiento del uso de IA por departamento, cotizada; Fase 2 = guía modular a la medida con niveles de prioridad). Caso casi idéntico a `pilotes-perforados` (misma asesora Flavia Martínez, mismo patrón diagnóstico→plan abierto). **Cómo se construyó:** clon de `pilotes-perforados/` (multi-fase canónico) → reescritura de copy a eje «adopción ordenada de IA», ecosistema **Google + Claude** (no Microsoft/Copilot), 4 áreas ilustrativas de la ficha (Marketing, Talento Humano, Desarrollo, Dirección General), consultor **Andrés Fornerino** (decisión final del usuario; CAP-040 quedó para Protex → Ubii es CAP-042). Impacto con estudios reales (Noy & Zhang 2023, Brynjolfsson et al. 2023, McKinsey 2023/2025). **Bug encontrado:** la slide 10 `s-heatmap` del clon multi-fase **desborda +44px de fábrica** (el propio `pilotes-perforados` lo reporta) cuando lleva 8 filas `proc-row` × `height:49px` + 4 `area-row`. **Fix (en styles.css local del deck):** `proc-row td height 49→41px` + `score-pills gap 3→2px` + `.pill padding 2px→1px` → ahorra ~64px, las pills (3 apiladas) siguen entrando. **Recordatorio §4.16-titulo:** el título de Próximos pasos se recorta a ~20 chars; «Mapa de Calor y Roadmap» (23) se cortó → «Roadmap de adopción» (19). Verificado slide por slide. Memoria persistente: `project_ubii_pagos_auditoria` + `feedback_heatmap_multifase_desborda`.

## 2026-06-03 — [regla][scripts][bug] Truncado con «…» en chips de Programa = bloqueante propio (§4.10.5)

**Disparador:** correo del directivo de Educación (Keiber Quintana) rechazando propuestas entregadas con chips de Programa cortados con puntos suspensivos: «2.1 Cómo comunicarse con I…», «5.1 Guiones con estructura vi…». «Esos detalles no pueden estar» → o se acorta el subtítulo o se extiende la casilla. **Causa raíz:** `.s-program .module .topics li` traía `white-space: nowrap` + `overflow: hidden` + `text-overflow: ellipsis` en `_base/styles.css` y `pilotes-perforados/styles.css`. El «…» es el peor desborde porque *parece intencional*: oculta el texto perdido sin romper el diseño, así que pasa la revisión a ojo. **Fix triple:** (1) **CSS deja de truncar**: el chip envuelve (`white-space: normal; overflow-wrap: anywhere`) en ambos CSS → un tema que no cabe ahora desborda visiblemente y el detector lo caza; prohibido reintroducir nowrap+ellipsis. (2) **`verificar-overflow.js` gana chequeo dedicado de ellipsis** (tolerancia ~0, distinto del recorte genérico de 12px): cualquier «…» real sale como `TEXTO TRUNCADO con «…»`. (3) **Regla §4.10.5** + ficha `capacidad-cajas.md` + resumen §10. La cura siempre es acortar el contenido (chip ≤ ~28 chars) o repartir el tema, nunca el «…». Memoria persistente: `feedback_sin_ellipsis_truncado`.

**Addendum (mismo día) · dr-care TA-024:** los decks con `styles.css` **local** (clonados antes del fix, no enlazados a `_base`) arrastran su propia copia del patrón prohibido. `dr-care/styles.css` aún traía `nowrap`+`overflow:hidden`+`ellipsis` en `.s-program .module .topics li` → varios temas se cortaban («1.5 IA tradicional vs gener…», «3.1 Optimizar tareas repetiti…»). Fix doble: (1) reemplazado por `white-space: normal; overflow-wrap: anywhere` (idéntico a `_base`); (2) temas acortados a ≤ ~28 chars («1.5 Tradicional vs generativa», «3.1 Tareas repetitivas», «5.1 Guiones virales», «6.5 Palabras clave»…). Al revisar un deck con CSS local, grep `ellipsis` en su `styles.css`, no solo en `_base`.

## 2026-06-03 — [cliente:grupo-nena] CAP-016: cliente aprobó y pidió reenviar SIN el módulo de Ética y Gobernanza (Módulo V eliminado)

**Cambio del cliente (Droguería Nena)**: revisó la propuesta CAP-016, la aprobó y pidió reenviarla sin el módulo de Ética y Gobernanza de IA. Se eliminó el **Módulo V en su totalidad** y todos sus efectos en cadena. **Recálculos:** 5 módulos→**4**; 6 cards Programa→**5**; 6 sesiones calendario→**5**; **14h→11h por participante** (3 comunes de 3h + 1 IV de 2h); **16h→13h facilitación** (Douglas 14h→11h, Rafael 2h); 6 semanas→**5**; cotización por 5 sesiones. **Tema gobernanza arrancado de todo el copy** (portada, diagnóstico, objetivos, metodología, beneficios, equipo, pasos, cierre): se retiraron sus entregables (Política de Uso Aceptable/AUP, Desafío de IA, plan 90 días). Diagnóstico 5→4 puntos (quitado el de gobernanza), objetivos específicos 4→3, cierre «con gobernanza»→«con Google AI». **Contadores 15→14** (renumerados todos), rutas cronograma «de 6»→«de 5» y % fill (20/40/60/80/100). Tocados index.html, styles.css, brief.md, programa.md, customize-grupo-nena-cap016.py (Entregables sin AUP/Desafío, Paso01Body 4 sesiones/5 semanas, Paso03Body sin Desafío/AUP). Par PDF-customize corrido, verificar-propuesta + overflow OK, revisión visual slide por slide. **Anula parcialmente** la entrada 2026-06-01 (el Módulo V reenfocado a Ética/Gobernanza ya no existe; el resto de esa minuta —solo IV se divide A/B— sigue vigente).

**[bug CSS heredable]**: la slide `.s-program` tiene banda negra de header con **altura fija 160px**; la `.meta` larga solo se compacta vía reglas `:has(nth-child(6))` (6 mód) y `:has(nth-child(7))` (7+). Con **exactamente 5 módulos** no había compactación → la 3ª línea de `.meta` (amarilla) desbordaba la banda y caía sobre fondo blanco (invisible). Mismo patrón que el bug de 4 módulos ([[feedback_program4_y_paso_titulo_recortes]]). Fix: regla `:has(.modules > .module:nth-child(5)):not(:has(.modules > .module:nth-child(6)))` con meta 11.5px + h2 margin 4px + padding 48px (espejo de la de 6). **Nota:** el verificar-overflow.js NO detecta este caso (la banda `::before` es decorativa, no es caja de contenido) → revisar a ojo el header de Programa al cambiar el número de módulos.

## 2026-06-01 — [cliente:damasco] CAP-037 reconstruido: split de Desarrollo por función (no por nivel) y nivelación avanzada ≠ remedial

**Contexto:** el deck DAMASCO (3 rutas departamentales, 17 slides) existía solo como PDF; la carpeta fuente nunca se guardó. Se reconstruyó clonando `inversiones-romitec` (canónico 17→14 slides, _base). **Feedback de ventas + Douglas:** la "nivelación de 2h a un grupo medio para que siga con el avanzado" en Desarrollo no era práctica y las horas confundían; láminas 5/7/9 ("Contenido detallado") con letra ilegible. **Causa raíz (minuta 26-may):** Desarrollo (9) es **avanzado y parejo**, no mixto; el deck inventó un split por nivel. La nivelación real de la minuta es **Soporte** (6, nivel básico). **Fix de estructura:** (1) Desarrollo = un solo grupo 8h, sin pistas; el "split" se reencuadra **por función** (Mesa A programadores: agentes + tokens · Mesa B SAP/BI: bases de datos con IA que **alimentan Power BI**, sin construir dashboards nuevos, [[feedback_no_competir_con_bi_cliente]]); los 9 están las 8h completas, dos mesas en la práctica → horas dejan de confundir. (2) **Pasarelas de pago fuera** (tema delicado, va a fase posterior). (3) Soporte 4h básico, Marketing 6h intermedio. Total 18h. **Fix de legibilidad (opción A aprobada):** se eliminaron las 3 láminas "Contenido detallado" a la medida (no canónicas, causaban la letra chica) y su contenido se fundió en el **cronograma canónico** (`.s-schedule`) por ruta. El detalle por tema vive en `programa.md §5.2`. **Roadmap:** reusa el layout de `s-program` (3 cards, blanco, cero CSS nuevo); corregido a Fase 1 (3 equipos) / Fase 2-plus (asistentes virtuales + agentes, CRM con Claude) — se eliminó la "Fase 2: Admin/Tesorería/Ventas" que el deck inventó (no está en la minuta). Consultor = Rafael Carreño, asesora = Isabella Palazzone.

## 2026-06-01 — [preferencia] Redacción humana y concreta, nunca genérica ("voz de IA")

Directriz general del usuario: todo output de cara al cliente debe sonar **humano y concreto** (datos duros del cliente: 60-100 SKUs los viernes, 100.000 facturas/día, 54 sucursales; herramientas que ya usa: SAP Business One, Power BI, Claude Code), nunca abstracto ni de molde. Refuerza [[feedback_sin_guion_largo]] y §4.8. Guardado en memoria persistente como `feedback_redaccion_humana_no_generica`.

## 2026-06-01 — [arquitectura] Nuevo flujo: Dashboard de Impacto Edu-Trace (post-cierre de cliente)

**Segundo flujo del sistema**, paralelo al de propuestas: cuando termina el proceso de un cliente y los participantes responden la **Encuesta Edu-Trace** (Google Form de cierre), se genera un Dashboard de Impacto que se archiva interno y se entrega al cliente. **Fuente única:** un `encuesta.csv` por capacitación cerrada. **Estructura de la encuesta = 4 bloques con lógica distinta:** A identidad · B impacto autopercibido (Likert) · C conocimiento objetivo (3 preguntas técnicas a la medida, se CALIFICAN) · D calidad/facilitador (Likert) · E inteligencia comercial (textos abiertos → próxima venta). **Resultado medible = Índice de Impacto Edu-Trace 0-100** ponderando 4 ejes priorizando lo medido (Retención objetiva 35% · Competencia 30% · Aplicabilidad 20% · Calidad 15%); el salto Competencia−Brecha se reporta aparte como *percibido/retrospectivo*. **Vive en `clientes/dashboards/<slug>/`** (hermano de propuestas, subcarpeta por cliente). **Dos salidas de un mismo motor:** `index-cliente.html` (Bloque E como recomendaciones de valor) e `index-interno.html` (Bloque E como prospección). **Reutiliza el stack visual:** enlaza `../../propuestas/_base/styles.css` + `overrides.css`, reusa `.s-cover`/`.s-impact` (gauge + barras)/`.s-end`. **Sin AcroForms** (el dashboard no es editable → no hay customize). **Archivos creados:** `scripts/edutrace-procesar.py` (CSV→Índice→`resultados.json`, descarta PII), `scripts/generar-dashboard.sh`, `plantillas/dashboard-edutrace.md`, `plantillas/generar-dashboard.md`. **CLAUDE.md:** nuevas reglas bloqueantes §4.16 (PII: cédula nunca en salida; `encuesta.csv` gitignored), §4.17 (honestidad de medición: solo Bloque C es «medido», B/D «percibido»; tags `.tag-medido`/`.tag-percibido`), §4.18 (clave Bloque C deducida por lógica, preguntar si ambigua), §11 (flujo) y fila en §5. **Piloto:** APB Group · Tecnología (n8n/IA) · N=11 · **Índice 86/100**, retención objetiva 97%. El Bloque E señaló **RRHH como #1 a formar**, respaldando la propuesta CAP-033 RRHH ya en curso (cierre de ciclo real). v1 = núcleo (pipeline + PDF cliente + vista interna estática); filtros interactivos y web → v2. Overflow OK en ambos decks, PDF revisado slide por slide, grep PII = 0.

## 2026-06-01 — [cliente:grupo-nena] Minuta del líder educativo: solo Módulo IV se divide A/B, V unificado y reenfocado a Ética y Gobernanza (no Looker)

**Cambio del lider educativo (CAP-016)**: la propuesta inicial duplicaba IV y V por grupo (IV-A/IV-B y V-A/V-B → 7 cards Programa, 7 sesiones calendario). Minuta corrige: **solo el Módulo IV se diferencia por perfil** (IV-A sin código con Douglas para Grupo A, IV-B Apps Script con Rafael Carreño para Grupo B). **El Módulo V se unifica y se reenfoca a Ética y Gobernanza de IA**: razón explícita en la minuta — el equipo de BI de Nena centraliza dashboards en Power BI para mantener gobernanza de datos, por lo que el módulo de Looker Studio no aplica; se reemplaza por co-creación de la Política de Uso Aceptable (AUP), Desafío de IA y plan de implementación a 90 días (Douglas, los 40). Resultado: **5 módulos, 6 sesiones calendario, 6 cards en Programa**. Se ajustaron index.html (6 cards Programa, 4 cronograma + S6 V común reescrito de cero), brief.md, programa.md, customize-grupo-nena-cap016.py (Entregables: AUP + Desafío + plan 90 días; quitado «Dashboard»; Paso01Body actualizado a 6 semanas). **Regla heredable**: cuando el cliente tiene un equipo BI centralizado en otra plataforma (Power BI, Tableau, etc.), el cierre de la propuesta NO entra a competir con esa herramienta — se reenfoca al marco de gobernanza/política/plan firmable que sí cae en el alcance de Intezia. **CSS Programa**: agregada regla `:has(> .module:nth-child(6)):not(:has(> .module:nth-child(7)))` con cards compactas (min-height 0, padding 38px 13px 12px, font-size 13.5/10.5/9.5) — antes solo había modo 5 y 7+ módulos, y 6 cards en 3×2 con min-height 235 desbordaba +139px. Par PDF-customize corrido, verificador OK.

