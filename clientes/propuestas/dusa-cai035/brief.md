# Brief · DUSA · Servicio de Habilidades, 44 soluciones en 10 áreas (CAI-035)

## Datos administrativos

- **Cliente**: DUSA · industria licorera (producción, envasado y distribución de bebidas alcohólicas) · https://dusa.com.ve
- **Naturaleza**: Capacitación in-company · **servicio de Habilidades como siguiente paso del servicio de Detección ya entregado** (Informe Final de Auditoría IA, 04/09/2026, y Informe Final DUSA, 02/10/2026). No repite diagnóstico: construye, prueba y deja adoptadas las soluciones definidas en el informe.
- **Slug**: `dusa-cai035`
- **División Intezia**: `educacion` (cliente corporativo; mismo criterio que `dusa-cai012`, `dusa-cap087`, `dusa-cap088`)
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: Capacitación In-Company (`CAI-035`, siguiente número libre de la serie; el último era CAI-034, N58 Banco Digital)
- **Eje temático**: construcción, pruebas y adopción de 44 soluciones con Microsoft Copilot (Finanzas y Comercial Centro-Sur) y Claude Team (Recursos Humanos)
- **Fecha del brief**: 2026-10-04
- **Estado**: `Enviada` el 2026-10-04 (versión de 5 slides, ver `meta.json`). La versión vigente es de **7 slides** (retorno del 2026-10-05 más las correcciones de la reunión del 2026-10-06: reorden, plan de pago y ejemplos ya construidos) y queda pendiente de reenvío
- **`fecha_arranque_deseada`**: no hay. El insumo vigente (`_6`) quitó las fechas calendario: la ruta es relativa al arranque (11 semanas de trabajo; seguimiento hasta 90 días después del cierre). El deck no muestra fechas de inicio ni de cierre.
- **`resultados_esperados`**: no hay Ficha Comercial ni respuesta explícita del cliente, y las fichas de Recursos Humanos casi no declararon horas por proceso: **DUSA no tiene hoy una línea base de horas** (se mide en la semana 1). Por eso la hoja de cotización no lleva ROI propio. El 2026-10-05 el usuario pidió una lámina final de retorno (ver «Slide 6»): usa rangos de estudios reales, rotulados como estimación externa, y NO cifras propias de DUSA.

## Fuente primaria

`DUSA_Habilidades_Procesos_Ruta_y_Horas_6.docx` (Intezia C.A., Dirección de Productos y Servicios, 02/10/2026, Keiber Quintana), aportado por el usuario el 2026-10-04 como corrección de la versión anterior (`DUSA_Habilidades_Procesos_Ruta_y_Horas.docx`). Fuentes que cita el propio documento: Informe Final de Auditoría IA (04/09/2026), Informe Final DUSA (02/10/2026), fichas de las cinco áreas de Recursos Humanos (01 y 02/10/2026), mesa con Sistemas del 02/10/2026 y nota de la reunión con Finanzas. Las tablas completas (44 soluciones con C/T/A, fase y horas) están en `programa.md`, extraídas programáticamente y validadas: **44 soluciones, 500 h** (208 + 119 + 173; F0 12 h, F1 224 h, F2 148 h, F3 116 h).

## Cambios del insumo: versión anterior → `_6` (identificados 2026-10-04)

Las 44 soluciones, sus horas C/T/A, las horas por área (35, 22, 15, 80, 21, 19, 82, 63, 44, 87, 32), por frente (208, 119, 173) y por fase (12, 224, 148, 116) **no cambiaron**. Lo que cambió:

1. **Fechas calendario eliminadas** (texto e imagen). Antes: «si el servicio arranca el 19/10/2026, la construcción cierra el 15/01/2027… seguimiento hasta abril de 2027»; fases con fechas (19/10-23/10, 19/10-20/11, 16/11-11/12, 30/11-15/01); hito «tope 11/12»; hito «cierre 15/01/2027»; seguimiento «dic 2026 a abr 2027»; pausa de fin de año 21/12-01/01; título de la imagen «si arranca el 19/10/2026». Ahora: «desde el arranque del servicio, 11 semanas de trabajo; el seguimiento corre hasta 90 días después del cierre»; fases con «N h en total»; hito de cierre «S11»; seguimiento «desde el cierre de cada área»; «S = semana de trabajo desde el arranque».
2. **Resumen de horas**: se quitan las columnas Semanas, Horas por semana y Horas por día y la frase «tres frentes en paralelo durante 11 semanas de trabajo» (las semanas y h/semana siguen en la imagen de la ruta).
3. **Claude Team**: antes «arranque en el mínimo de asientos y crecimiento por uso; más allá de cinco, solo crece por uso medido»; ahora «una licencia Standard por área, cinco en total», «se licencia igual que Microsoft 365 Copilot».
4. **Condición de contratación** (política de regiones de Anthropic): eliminada.
5. Imagen: el pie ahora dice «NM-1 se prueba dentro de una ventana parafiscal real de cinco días hábiles» antes de «las fases se traslapan», y ya no menciona la pausa de fin de año.

Efecto en el deck: se retiraron todas las fechas calendario (slides 3, 4 y 5), el campo `Notas` ya no menciona a Anthropic ni la contingencia a Copilot, la tarjeta de licenciamiento de Claude Team dice «una licencia Standard por área: 5 en total», y el «Valor inmediato» usa semanas (S4, S5) en lugar de fechas.

## Estructura pedida por el usuario (5 slides el 2026-10-04 + slide 6 el 2026-10-05)

Los títulos que dio el usuario (¿Qué voy a hacer?, etc.) eran una guía de contenido, no títulos literales. El nombre del proyecto es una frase-objetivo estilo tesis; los titulares internos son afirmativos: «44 soluciones en 10 áreas de DUSA», «Tres frentes en paralelo, 11 semanas», «Inversión por horas de sesión», «Todo lo que DUSA recibe».

**Numeración vigente desde el 2026-10-06** (las menciones anteriores a esa fecha en este brief usan el orden previo: 4 Inversión, 5 Entregables, 6 Retorno).

| # | Contenido | Slide |
|---|---|---|
| 1 | Portada con punto de dolor | `.s-cover`: «Optimización de procesos y datos con inteligencia artificial en 10 áreas de DUSA» + 3 datos de la auditoría + «≈10 posiciones» con la probabilidad de no contratarlas (2026-10-06) |
| 2 | ¿Qué voy a hacer? | `.s-scope`: alcance (44 soluciones, 10 áreas, 2 herramientas), **cuatro pasos por solución** (el 4.º mide el retorno), franja **«Ya lo hicimos con los equipos de DUSA»** (3 agentes del informe final de Detección) y qué queda fuera. «Quién construye» se fundió en los pasos 1 y 2 para dar lugar a la franja |
| 3 | ¿Cómo lo voy a hacer? | `.s-route`: 3 frentes × 3 fases, **soluciones primero y horas en pequeño**, «seguimiento y garantía» 30-60-90, hitos |
| 4 | ¿Qué tendrás a cambio? | `.s-deliv`: catálogo de los **44 entregables** + entregables transversales + valor inmediato. Subió antes del precio (reunión del 2026-10-06) |
| 5 | ¿Cuánto te va a costar? | `.s-price` estándar (por horas) + licenciamiento aparte + descuento urgente + garantía 30-60-90. Duración reordenada: soluciones, semanas y, al final, las horas |
| 6 | Facilidad de pago (nueva 2026-10-06) | `.s-pay`: 5 cuotas ligadas a hitos (30, 25, 25, 10 y 10 %; semanas 1, 5, 8, 11 y 30 días después del cierre). Montos **vacíos y editables** (campos `PagoCuota1..5`) |
| 7 | Retorno | `.s-roi`: método de cálculo, **calendario de garantía** y «hacia dónde va el proyecto». Sin estudios ni citas externas y sin cifras propias hasta tener los datos. Sin campos AcroForm |


El usuario pidió **5 slides** el 2026-10-04 y **una lámina final de retorno** el 2026-10-05: no hay Impacto genérico, Próximos pasos ni Cierre. Tampoco hay contacto de la asesora comercial en el deck.

## Correcciones de dirección del 2026-10-05 (estado)

Mensaje de revisión sobre informe, ruta de procesos y propuesta ("el cliente quedó muy satisfecho"). Estado en la **propuesta** (la ruta es el docx `_6` y el informe es otro documento; no están en este repositorio):

| Pedido | Estado |
|---|---|
| Nombre del proyecto (2026-10-05) | **Hecho.** Frase-objetivo estilo título de tesis: «Optimización de procesos y datos con inteligencia artificial en 10 áreas de DUSA» (80 caracteres: con el código cabe en los 90 del nombre del PDF, que `generar-pdf.sh` toma de la portada y corta). Sustituye al titular de dolor «Los equipos digitan, concilian y persiguen lo que ya existe» |
| 3. Quitar «propuesta formativa» | **Hecho.** Portada: «Propuesta de proyecto · Servicio de Habilidades»; lead: «Este proyecto ordena los procesos y los datos, construye y deja adoptadas las soluciones ... y mide su efecto»; slide 2: «Ordenamos procesos y datos, y construimos ...»; slide 3: «capacitación» aclarado como control de capacitación **del personal de DUSA**. Quedan, a propósito: el «Certificado de participación INTEZIA» (entregable institucional estándar) y `meta.json → tipo: Capacitación In-Company` (taxonomía interna CAI-). La plantilla genérica ya usa «Propuesta de proyecto» por defecto |
| 2. Tono sobrio, sin contrastes ni sentencias | **Parcial.** Se aplicó a la slide 6 y a los textos tocados. El informe (que es donde está el problema) no está aquí |
| 2. Tabla de Sistemas con hechos | **Preparada**, no en el deck: hoja `Sistemas` de `retorno-captura.xlsx` (20 desarrollos con lo que dice el insumo; volumen y horas manuales sin dato). Las frases «exposición», «único constructor y filtro» y «sin capacidad declarada» no aparecen en la propuesta: están en el informe |
| 2. Cuadro de hallazgos por área | **Pendiente.** Hay fichas de Nómina y Servicio Médico (sirven para dos áreas); faltan las fichas de las otras |
| 1. Retorno con datos duros (volumen, tiempo, horas recuperadas, dinero) | **Bloqueado por datos.** Las fichas disponibles dicen «No declarado» en volumen mensual y horas por ejecución. Hoja de captura: `retorno-captura.xlsx` (fórmulas listas, datos reales precargados con fuente, lista de lo que falta) |
| 1. Reducción de puestos y nómina | **Bloqueado por datos** (dotación equivalente por área, escalas salariales, costo hora). Mientras tanto la slide 6 ya no dice «no de reducirlo» |

La slide 6 actual es el **método** del retorno, sin cifras: debe completarse con los datos de DUSA cuando existan. No enviarla a los directores como versión final si ellos esperan números.

## Correcciones de la reunión del 2026-10-06 (estado)

Reunión de Keiber Quintana con María Iribarren sobre esta propuesta (transcripción de la reunión). Cada pedido, su estado y las decisiones tomadas donde la reunión daba cifras sin respaldo:

| Pedido | Estado |
|---|---|
| Portada: poner la contratación como **probabilidad**, no como compromiso | **Hecho.** «≈10 posiciones a tiempo completo harían falta para sostener a mano este mismo volumen de trabajo. Con los procesos optimizados, es alta la probabilidad de no tener que contratarlas.» Fuente de las ≈10: Informe Final de Auditoría IA (04/09/2026), tabla «Contra qué se compara esta inversión» (5 a 6 en Cuentas por Cobrar, 3 de brecha en Tesorería, 1,5 en Contabilidad, 1 de diseño en Comercial). Las «6 personas» de la reunión son las 5 a 6 de Cuentas por Cobrar. **No se usó el «10 %»** que se dijo en voz alta («no sé, 10%, algo así»): no tiene base. Si dirección quiere una cifra de probabilidad, definirla con datos |
| Slide 2: **cuarto paso** «medimos el retorno y el impacto» | **Hecho.** «Medimos el retorno en tiempo y las oportunidades de optimización para la empresa» (sin la sigla ROI, §4.12). «Quién construye» se fundió en los pasos 1 y 2 |
| Slide 2: **ejemplos de éxito** de los kickoffs (cuadro visual) | **Hecho** con lo documentado en el Informe Final (04/09/2026, sección «Logros inmediatos construidos durante las sesiones de fundamentos y auditoría») y el deck «Cierre de Detección»: (1) Contabilidad y Cuentas por Pagar, agente de estados financieros: armar a mano 2 a 3 h y analizar 30 a 40 min; con el agente, el análisis se resolvió en 3 a 4 min. (2) Cuentas por Cobrar, validador de cobros contra la base corporativa: la líder estimó unas 8 personas para hacerlo a mano. (3) Comercial Región Centro-Sur, generador de creativos: antes no existía. **No se usó «casi 2 semanas de trabajo»** (conciliación de pagos, dicho en la reunión): en las fuentes, «dos semanas» es la demora actual de validar un pago entre Comercial y Cobranza (ficha de Comercial Centro-Sur e informe), no un ahorro medido del validador. Tampoco «9 soluciones instaladas»: el informe habla de «agentes adicionales» sin número. Confirmar con Keiber si quiere alguna de las dos |
| Slide 3: «seguimiento **y garantía**» | **Hecho** en el subtítulo y en la 5.ª columna (tarjeta «Garantía · 30, 60 y 90 días · Seguimiento desde el cierre de cada área») |
| Slide 3: **soluciones primero**, horas más pequeñas | **Hecho.** Frentes: nombre de la herramienta grande («Claude Team», «Copilot») y «16 soluciones · 208 h · S1-S11» con las horas en pequeño. Celdas: «6 soluciones» grande y «87 h» chico. Fases: conteo de soluciones (19, 13 y 11); las horas por fase quedan en la nota al pie, que además explica que el mapeo de Finanzas (1 solución, 12 h) abre el Frente C: por eso el Frente C dice 17 y sus celdas suman 16 |
| **Orden**: «Todo lo que DUSA recibe» antes del precio | **Hecho.** Portada, Alcance, Ruta, Entregables, Inversión, Facilidad de pago, Retorno |
| Inversión: **Duración** con las 500 h al final | **Hecho.** «Proyecto de 44 soluciones a realizar en un total de 11 semanas, con seguimiento y garantía a 30, 60 y 90 días. 500 horas de trabajo.» El título «Inversión por horas de sesión» se dejó igual (no se pidió cambiarlo) |
| Inversión: quitar las notas de licenciamiento, poner «términos y condiciones, garantía» | **Hecho en el campo `Notas`** (pre-llenado editable): garantía 30-60-90 y términos y condiciones. María dijo que ajustaría el texto ella en Adobe. `Programa` ahora dice «soluciones» antes que horas (16, 11 y 17 por frente). **El precio sigue vacío** para ventas |
| **Plan de pago** en hoja aparte tras la inversión, **montos como placeholder** | **Hecho** (slide 6). Cuadro enviado por Keiber el 2026-10-06 (imagen): «Facilidad de pago · 5 cuotas ligadas a hitos del proyecto». Montos vacíos y editables (`PagoCuota1..5`). En la reunión se habló antes de 4 cuotas (30, 25, 25, 20); vale el cuadro enviado (5). La última frase del cuadro venía mal puntuada («Cada factura se emite en divisas o BS a BCV Euro se liquida a la tasa del día de pago») y se escribió «Cada factura se emite en divisas o en bolívares (Bs) a la tasa BCV Euro, y se liquida a la tasa del día de pago»: **confirmar** que ese es el sentido |
| Retorno: «**Calendario de garantía** y cálculo del ROI» | **Hecho** como «Calendario de garantía y cálculo del retorno», con «Desde el cierre de cada área» debajo (se evitó la sigla, §4.12) |
| Retorno: «**Hacia dónde va el proyecto**» (global) | **Hecho.** «Trabajo reenfocado» ya no nombra Nómina ni Finanzas: habla de las personas de cada área y de reenfocar sus posiciones hacia trabajo más estratégico |
| Retorno: tono **aspiracional** en «Otras áreas y líneas de negocio» | **Hecho:** «…avanza hacia una empresa inteligente, con la inteligencia artificial en el centro de su operación» (en vez de «AI first», §4.4) |
| Comité interno de DUSA para medir el retorno real (costo hora, etc.) | **No va en el deck.** Se contó como contexto: DUSA formaría un comité con un líder por área, a pedido de tecnología, para medir el retorno junto con Intezia. Es la razón por la que la slide 7 no trae costo hora |

## Slide 7 · Retorno (creada el 2026-10-05 como slide 6; la 7 desde el 2026-10-06)

**Origen del pedido.** Criterio comercial (David, vía el usuario): a la directiva hay que mostrarle el retorno de inversión real o aproximado, en ahorro de tiempo y en dinero, el reenfoque del trabajo, crecer sin sumar gente a la nómina, la oportunidad de reducción de puestos y de nómina (planteada de frente, con el aval del cliente), y una proyección de la organización, incluida la extensión a otras áreas y líneas de negocio.

**Versión vigente (sin estudios).** El usuario pidió el 2026-10-05 que la slide **no cite estudios ni nada relacionado con la web**. La slide quedó como método y metas, con datos y vocabulario de DUSA únicamente:
- Panel «Cómo se calcula, por área y por proceso»: 6 pasos (volumen mensual → tiempo actual por ejecución, que es la línea base de la semana 1 → tiempo con la solución → horas recuperadas al mes → valor en dinero con el costo hora de referencia, más retrabajo, errores y pagos o cobros tardíos cuando haya dato → posiciones y costo anual según las escalas salariales de DUSA).
- Calendario de garantía y cálculo del retorno, desde el cierre de cada área (antes «Metas»): 30 días (soluciones en uso real y línea base validada), 60 días (horas recuperadas medidas), 90 días (retorno en dinero y en posiciones).
- «Hacia dónde va el proyecto» (antes «…el tiempo recuperado»): mismo equipo con más volumen sin ampliar la nómina (condicional), trabajo reenfocado en global (personas y posiciones hacia trabajo más estratégico) y ampliación a otras áreas y líneas de negocio, con tono aspiracional (empresa inteligente).
- Gancho: «Hacia la semana 24, DUSA conoce el tiempo recuperado, su valor en dinero y las posiciones equivalentes en cada área».

**Sin cifras de retorno.** Las fichas de levantamiento disponibles (Nómina, Servicio Médico, Agente de Parafiscales) dicen «No declarado» en volumen mensual y horas por ejecución; no hay costo hora, escalas salariales ni dotación equivalente salvo Cuentas por Cobrar (≈8 personas, según el mensaje de revisión). La hoja `retorno-captura.xlsx` precarga lo que sí existe (con fuente) y calcula todo con fórmulas cuando se completen los datos. **Cuando estén, esta slide pasa de método a cifras por área** (y se agrega la página equivalente al informe).

**Decisiones.**
1. «Sin sumar plazas / sin ampliar la nómina» va en condicional («puede», «si el tiempo se libera»): es una proyección, no un resultado. La garantía 30-60-90 es de acompañamiento, no de retorno.
2. «Hacia la semana 24» es aritmética de la propia propuesta: la construcción cierra en la semana 11 y el último seguimiento llega a 90 días (~13 semanas) desde el cierre. **Confirmar con servicio** antes de reenviar.
3. La slide no usa siglas (se evita ROI) ni repite los marcadores de detección de AcroForms de las slides 4 y 5. Se usa «slide» en todo el brief.
4. Los estudios que se verificaron para la versión anterior (Bick et al., Brynjolfsson et al., Noy y Zhang, y otros cuatro) quedan **solo como respaldo oral interno** en `programa.md` §6, con sus límites; no están en el deck.
5. Revisión independiente de la versión con estudios (6 revisores, 49 hallazgos, ninguno alto): los hallazgos de tono, gancho y «el método» sin antecedente se trasladaron a esta versión; los del eje del gráfico y de las fuentes dejaron de aplicar al retirarse los estudios.

## Decisiones y supuestos (confirmar con el usuario)

1. **Código CAI-035**: siguiente número libre. Si el usuario ya asignó otro, renombrar carpeta, `meta.json`, `index.html` (`.codigo`, footers, comentarios), `acroforms.json` y `scripts/customize-dusa-cai035.py`.
2. **Precio vacío**: los campos de inversión, descuento y total quedan vacíos para ventas (regla del sistema); no hay tarifa por hora en `empresa/politicas-comerciales.md`.
3. **Licenciamiento**: el deck dice que se «contrata aparte de esta inversión». La fuente no indica quién contrata (DUSA o Intezia); por precedente (CAI-012) se asumió que no lo factura Intezia. Precios: Claude Team USD 20 por asiento al mes con pago anual (lista del 02/10/2026), una licencia Standard por área, 5 en total; Microsoft 365 Copilot USD 30 por usuario al mes con compromiso anual (informe del 04/09/2026).
4. **Condición de contratación de Claude Team**: la versión anterior del insumo la advertía (política de regiones de Anthropic); la versión `_6` la eliminó, por lo que el deck no la menciona.
5. **Entregables institucionales**: el campo `Entregables` solo lleva los transversales (línea base, seguimiento 30-60-90, certificado). No se agregaron «manual digital por participante» ni «panel de progreso», que no aplican a una construcción de soluciones (mismo criterio que CAI-012).
6. **Vocabulario**: «testeo» de la fuente se muestra como «pruebas» (§4.4, español). Se muestran los nombres de sistemas de DUSA tal como los usa el cliente (JD Edwards, Tesote, Bitácora, autopago, HCM, Seguro Humanitas). No se muestran nombres de personas de DUSA.
7. **Datos de la portada**: «10 a 15 empresas» con pagos de parafiscales sale de NM-1 del docx (`_6`), «5 fuentes» de RH-0 y «+20 archivos de Excel encadenados» del Informe Final de Auditoría IA (04/09/2026), tal como lo recoge `dusa-cai012/brief.md` (no figura en el docx). Se retiró «+300 facturas» porque ese frente lo asume Sistemas de DUSA y queda fuera del alcance.

## Antecedente

DUSA ya tiene 5 propuestas en `clientes/propuestas/`: `CH-007`, `CH-010` (charlas), `CAP-087` (políticas), `CAP-088` (auditoría de automatización, 2 áreas) y `CAI-012` (Habilidades, 5 áreas, 2026-09-07). **CAI-035 amplía el alcance de CAI-012** (de 5 áreas financieras y comerciales a 10 áreas, sumando Recursos Humanos con Claude Team). No se tocó ninguna carpeta anterior; queda pendiente decidir si CAI-012 se marca como superada.

## Notas de diseño

- Base: `_base/styles.css` + `overrides.css` local. Portada, hoja de cotización (descuento urgente, garantía 30-60-90, términos) heredadas de `_base`; slides 2, 3, 4, 6 y 7 son componentes propios de este deck.
- Slide 5 reemplaza Beneficios v3 por un catálogo de entregables (pedido del usuario). Las cajas AcroForm `Entregables` y `Acreditacion` (usada como «Valor inmediato») se reubican en una franja inferior con `scripts/customize-dusa-cai035.py`.
- Marcadores de detección de AcroForms (no repetir en otras slides): «Lo que se llevan» y «Entregables» solo en la slide 4; «Propuesta Económica» solo en la slide 5; «Facilidad de pago» (título) solo en la slide 6. Las páginas se ubican por texto, no por posición.
- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin afirmar migración de stack (§4.11): Claude Team se suma, Copilot es el Microsoft 365 que DUSA ya opera. Sin guion largo (§4.13).

## Flujo de generación

```bash
./scripts/generar-pdf.sh dusa-cai035
python3 scripts/customize-acroforms.py dusa-cai035
python3 scripts/customize-dusa-cai035.py "clientes/propuestas/dusa-cai035/<PDF>"
```

PDF de 7 páginas (las versiones de 5 y de 6 slides quedaron en `_pdf-anteriores/`). Los campos `PagoCuota1..5` los agrega `agregar-campo-precio.py` (grupo `PLAN_PAGO_FIELDS`, creado para esta propuesta; sus coordenadas están sincronizadas con `.s-pay .pay-frame` de `overrides.css`). `generar-pdf.sh` no es ejecutable directo: correr con `bash scripts/generar-pdf.sh dusa-cai035`.

Nota de entorno: los scripts usan `pypdf`, que no estaba instalado en el Python del sistema; se instaló en un entorno virtual aparte para generar y revisar el PDF.

## Pendientes

- **Confirmar con Keiber** (reunión del 2026-10-06): (a) el sentido de la última frase del plan de pago (divisas o bolívares a la tasa BCV Euro y liquidación a la tasa del día); (b) si quiere usar «casi 2 semanas de trabajo» o «9 soluciones instaladas», que hoy no tienen respaldo en las fuentes; (c) si quiere una cifra de probabilidad de no contratar (el «10 %» dicho en voz alta no se usó).
- **Montos del plan de pago**: los escribe ventas en Adobe Reader (`PagoCuota1..5`); deben sumar el total de la slide 5. No se anotan en este repositorio.
- **Plantilla compacta**: los cambios de esta reunión (orden, soluciones primero, plan de pago, franja de ejemplos, cuarto paso) no están en `plantillas/habilidades-compacto*`; queda propuesto llevarlos (ver `aprendizajes.md`).

- Regla de crecimiento de asientos de Claude Team: la `_6` la conserva (si un asiento toca su límite semanal dos semanas seguidas en un proceso de F1 o F2, se suma uno o pasa a Premium), pero la tarjeta de la slide 4 dice «5 en total, USD 100 al mes». Confirmar si «cinco en total» sustituye esa regla o si debe mencionarse.

- Confirmar el código CAI-035 y la asesora comercial (no hay contacto en el deck por no haber slide de cierre).
- Confirmar quién contrata los licenciamientos.
- Definir monto de inversión, descuento y total (campos vacíos para ventas).
- Cuando exista la línea base de la semana 1, **reemplazar las barras de estudios ajenos por las cifras propias de DUSA** (horas por proceso, horas recuperadas) en un reenvío de la lámina 6; hasta entonces el retorno es una proyección externa.
- Confirmar con Keiber/servicio que «hacia la semana 24» (cierre en la S11 + 90 días) es el plazo que se puede sostener ante la directiva.
- Si la directiva pregunta «¿cuánto en dinero?»: la respuesta honesta es que se calcula con la línea base (horas por proceso × costo de la hora de DUSA) y el monto de la inversión que fije ventas; no hay cifra hoy.
- El estudio de la Reserva Federal (Bick et al.) es un documento de trabajo, no un artículo con revisión por pares; el de Noy y Zhang se verificó en el resumen oficial (science.org devolvió 403 al agente).
