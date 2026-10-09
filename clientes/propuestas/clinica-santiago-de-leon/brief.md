# Brief · Clínica Santiago de León · Servicio de Detección (DET-027)

## Actualización 2026-10-08 · migrada a la plantilla v2 (8 slides) · VIGENTE

Instrucción directa del usuario: «ajustar la DET-027 al nuevo formato». «Formato nuevo» = **plantilla compacta v2.0**
(commit `93e0b67`, 2026-10-07): el `datos.json` v1.4 se migró según la spec §13 y se regeneró con
`--actualizar-css --forzar-overrides`. Orden del deck: Portada · Alcance · Ruta · Cómo trabajamos · Entregables ·
Retorno · Inversión · Próximos pasos. Los dos PDF de 6 slides (v1.4) quedan en `_pdf-anteriores/`. Sin cambios de
contenido de fondo: 22 h, 7 entregables (3 sesiones de Fundamentals y 4 áreas), 4 semanas, kick-off aparte y caso
para la Junta Directiva en el Reporte Final. El análisis interno de más abajo («Qué veo fuera del alcance de la IA»)
sigue vigente y no va en el deck.

### Decisiones

- **Sin «Facilidad de pago»**: no se preguntó; el usuario la omitió en la CAI-032, la DET-024, la CAI-040, la DET-026 y
  la CAI-038, así que se aplicó el mismo criterio (`omitir: ["pago"]`). Si Ventas la quiere, se agrega con cuotas
  ligadas a los hitos de la ruta. Importa más aquí: la propuesta la presenta el campeón interno ante la Junta.
- **Datos:** se mantiene «sin datos que identifiquen a pacientes» (decisión de la versión anterior; mismo criterio que
  G-MAX y Conserval). Los logros se prueban con ejemplos armados para la sesión. No se cita HIPAA ni ninguna norma.
- **Modalidad:** la ficha no la trae y la v2 exige una ficha de logística: dice «a acordar con la clínica» y que las
  sesiones se agendan según los turnos de cada área.

### Qué cambió respecto de la v1.4 (en el lenguaje de la v2)

| v1.4 | v2 |
|---|---|
| `alcance.pasos` y `quien_construye` | `metodo` (4 pasos propios de Detección) y `metodo.quien_construye` |
| (sin método, logística ni asesora) | `metodo.practica` (sesiones, con lo que ya tienen, IA o automatización), `metodo.datos`, `por_que_orden`, `logistica` y `proximos_pasos.asesora` |
| (sin «para qué» por área) | `areas[].para_que` en Fundamentals y en las 4 áreas |
| `frentes[].etiqueta`, `areas_html`, «S1-S4», «S = semana» | `frentes[].nombre` = «Auditoría de las 4 áreas», «1 a 4» y nota sin códigos |
| «Precios distintos» en la portada y en Atención al Paciente | «Montos distintos» (la v2 bloquea «precio»; son los montos que cobra la clínica, no los de esta propuesta) |
| Inversión «por horas de sesión»; Duración con las horas al frente | «Inversión del proyecto»; «Proyecto de 7 sesiones en 4 semanas: 3 de Fundamentals y 4 de área. 22 horas de trabajo.» |
| Notas con datos y modalidad | Notas con licencias, Habilidades y Políticas, y términos y condiciones (datos y modalidad ya están en «Cómo trabajamos») |
| Sin asesora ni contacto | Slide 8 con Verónica Rubio (teléfono y correo de la Ficha; el cargo «Asesora comercial» sale de este brief) |

La slide 3 conserva la 5.ª columna «Cierre» (Priorizar · Reportar · Proyectar), sin garantía 30-60-90. «Inicio · Seguro ·
Logros» y «Primera/Segunda/Tercera sesión de nivelación en IA» no cambiaron. `overrides.css` nuevo: escala de las
slides 2, 3, 4 y 5 (la columna de la slide 5 no pasa de ~450 px o se mete debajo de las cajas del PDF).

### Pendientes (a confirmar antes de reenviar)

- Inversión, descuento y total (campos vacíos para ventas; la Junta decide y la disponibilidad presupuestaria no está
  definida) y cómo se comunica el plan de pago (no hay slide).
- Fechas, horarios, modalidad y orden de las áreas con Verónica; cuántas personas hay por área y cómo son los turnos
  (de eso depende que sean 3 grupos de Fundamentals).
- Si el Reporte Final incluye una estimación de inversión de la ruta que sigue (el deck promete «caso para la Junta,
  con retorno e inversión»).
- La propuesta ya salió el 2026-10-06: confirmar si se reenvía el PDF nuevo y avisar que reemplaza al anterior. Estado:
  `Enviada` → `En corrección` → `Enviada` al regenerar (la `fecha_entrega` 2026-10-06 se respeta).

> Lo que sigue es el brief original del 2026-10-06 (formato v1.4); las decisiones de arriba prevalecen.

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Clínica Santiago de León
- **Slug**: `clinica-santiago-de-leon`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección · Fundamentals (3 grupos de 2h, hasta 25 personas cada uno) + auditoría de 4 áreas (Admisión, Finanzas y Facturación, Almacén, Atención al Paciente), 4h por área (16h), 22h totales · formato compacto (`DET-027`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Auditar Admisión, Finanzas y Facturación, Almacén y Atención al Paciente de la Clínica Santiago de León, con un logro inmediato en cada área, para llegar a un mapa de oportunidades de IA y un caso que la Dirección pueda llevar a su Junta Directiva
<!--auto:inicio-->
- **Alcance**: 7 entregables en 4 áreas · 22 h de sesión · 4 semanas de trabajo desde el arranque · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Enviada` (meta.json; fecha_entrega 2026-10-06, por convención «terminado = enviado»)
- **Asesora comercial**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com. Desde la v2 (2026-10-08) la slide 8 de próximos pasos la muestra.
- **Contacto del cliente**: Jacobo Idbeis, Coordinador de Innovación y Proyectos Médicos: campeón interno y quien presentará la propuesta, pero **no decide**. Decide la Junta Directiva. Su nombre y cargo no aparecen en el deck.
- **Ficha Comercial Intezia**: `Levantamiento_Clinica_Santiago_de_Leon_2026-10-05.pdf` (Ficha de Levantamiento, registrada 2026-10-05, elaborada por Verónica Rubio). Fuente primaria; qué se tomó y qué no está en la sección siguiente.
- **fecha_arranque_deseada**: no declarada. El formato compacto no lleva Calendario de inicio.
- **resultados_esperados**: según la ficha, un mapa claro de qué automatizar primero en las 4 áreas y un caso con presupuesto que el contacto pueda defender ante la Junta Directiva. Sin cifras propias: el retorno va en modo método.

## Origen y fuente

- **Origen**: Ficha de Levantamiento de la Clínica Santiago de León (registrada el 05/10/2026 por la asesora comercial) e instrucción directa del usuario del 06/10/2026
- **Fuente del insumo**: Ficha de Levantamiento de la Clínica Santiago de León
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- División Educación inferida: clínica privada, cliente corporativo. Alianza: no (la ficha no menciona ninguna). Confirmar con la asesora.
- Horas por el lineamiento de Detección: Fundamentals de 2 h con un máximo de 25 personas por sesión y 4 h por área en 4 áreas. Con un universo declarado de unas 60 a 70 personas (con turnos de guardia) salen 3 grupos de Fundamentals (6 h) y 16 h de áreas: 22 h en total. El kick-off de arranque va aparte y no suma horas (convención general).
- Los 3 grupos de Fundamentals se arman con la clínica por áreas y turnos, que la ficha no detalla (cuántas personas hay por área ni cómo se reparten las guardias de mañana, tarde y noche). Si los turnos obligan a más grupos, suben las horas: confirmar.
- Calendario propuesto por el sistema, no dictado por la ficha: 4 semanas (S1 kick-off y Fundamentals en 3 grupos, S2 Admisión y Finanzas, S3 Atención al Paciente y Almacén, S4 Reporte Final). Admisión y Finanzas van juntas porque comparten el flujo del seguro y el presupuesto. El Reporte Final va una semana después de la última sesión para dar tiempo al caso para la Junta. Orden y calendario por confirmar con servicio y con la asesora.
- Cada sesión de área es de 4 h con 1 o 2 personas (la ficha dice «1 o 2 por área»: jefes y gerentes de cada unidad, sin nombres). Cada sesión de área se presenta como un entregable; el Mapa de Calor, el Índice de Madurez y el Reporte Final son trabajo del equipo consultor, sin sesión con el cliente ni horas propias: van como entregables transversales.
- Caso para la Junta Directiva: la ficha pide «un caso con presupuesto que se pueda defender ante la Junta». El deck lo lleva como entregable del Reporte Final («con retorno e inversión»). Confirmar con servicio que el Reporte Final estándar incluye una estimación de inversión de la ruta que sigue.
- El deck no cita el modelo HIPAA ni ninguna norma: la ficha dice que la clínica lo usa solo como referencia. Las sesiones se trabajan sin datos que identifican a pacientes (decisión de diseño por la sensibilidad de los datos médicos); confirmar con la clínica.
- Logro inmediato: la ficha identifica conectar el triaje con la aprobación del seguro y el presupuesto. El deck lo presenta como el foco de la semana 2, no como un logro prometido; el primer paso aplicable se define en la sesión.
- Modalidad, fechas y horarios se omiten: la ficha no los trae.
- Retorno en modo método: la ficha trae tiempos declarados (aprobación del seguro cerca de 1 hora, presupuesto cerca de 15 minutos, triaje unos 5 minutos) y un volumen (unos 2.000 pacientes al mes), pero no costo hora ni tiempos con la solución; el Reporte Final los estima. Sin compromiso de resultado.
- Reglas de Detección que se conservan: sin certificado, sin garantía 30-60-90, sin pre-recomendar herramienta de IA (el Reporte Final recomienda), sin dolor dramatizado ni citas textuales, sin nombres de personas del cliente ni su cargo, sin el uso personal de IA del contacto.
- Fuera del deck y del alcance: el proceso 4 de la ficha (seguimiento de proyectos internos en Notion) no pertenece a ninguna de las 4 áreas priorizadas; el área de Tecnología (la ficha la deja para después) y el proyecto paralelo de investigación médica con IA que mencionó el contacto.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Reporte Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas). La disponibilidad presupuestaria no está definida, el patrocinio ejecutivo no está asegurado y la Junta Directiva decide: el valor debe poder defenderse ante ella y calzar con 22 h de sesión.
- Confirmar con la asesora las fechas, los horarios, la modalidad y el orden de las áreas; el deck solo lleva semanas y no muestra asesora ni contacto.
- Confirmar cuántas personas hay por área y cómo son los turnos, para fijar los 3 grupos de Fundamentals.
- Confirmar si el Reporte Final se entrega en la semana 4 y si incluye una estimación de inversión de la ruta que sigue.
- Confirmar la división (Educación), que no es alianza y si el kick-off va aparte (criterio por defecto).

## Qué se tomó de la ficha y qué no

**Se tomó (con el deck como destino):**

| Dato de la ficha | Dónde quedó |
|---|---|
| Servicio de interés: Detección; 4 áreas priorizadas (Admisión, Finanzas y Facturación, Almacén, Atención al Paciente) | Slides 1 a 5 (4 áreas, 4 h cada una) |
| Universo de unas 60 a 70 personas, con guardias de mañana, tarde y noche en Admisión y Almacén | 3 grupos de Fundamentals de 2 h (máximo 25 por sesión) |
| 1 o 2 personas por área a entrevistar (jefes y gerentes de cada unidad) | Paso 1 de la slide 2; cada sesión de área |
| Aprobación de seguro cerca de 1 hora frente a unos 5 minutos del triaje con IA | Hecho 1 de la portada |
| Presupuesto manual en SAP, cerca de 15 minutos | Hecho 2 de la portada |
| Quejas de pacientes por precios distintos por teléfono y al llegar | Hecho 3 de la portada |
| Unos 2.000 pacientes al mes; consumo de insumos calculado a mano | Hecho 4 de la portada |
| Logro inmediato identificado: conectar el triaje con la aprobación del seguro y el presupuesto | «Foco» de la semana 2 (Admisión y Finanzas); no se promete como logro |
| Objetivo del Reporte Final: mapa de qué automatizar primero y un caso para la Junta | Entregable transversal «Caso para la Junta Directiva, con retorno e inversión»; slide 6 |
| Jacobo percibe que otros proveedores confunden IA con automatización | Subtítulo de la slide 2 («separando lo que necesita IA de lo que solo se automatiza») y contenido de Fundamentals |
| Sensibilidad por los datos médicos y legales; posible camino hacia Políticas | Nota «sin datos que identifiquen a pacientes» y «Más adelante · Políticas» |
| Tecnología queda para más adelante | «Fuera de este alcance» (slide 2) |

**No se llevó al deck (decisión deliberada):**

- El nombre y el cargo del contacto, su uso personal de Claude, Gemini y ChatGPT, y la frase textual «de qué me sirve que lo detecten en 5 minutos…» (no se usan citas).
- Que la Junta ya se reunió con varios proveedores y que el contacto cree que confunden IA con automatización: es contexto comercial interno.
- El proyecto paralelo de investigación médica con IA (línea futura) y el proceso 4 (seguimiento de proyectos internos en Notion): no pertenecen a las 4 áreas priorizadas.
- El modelo HIPAA y la normativa sanitaria venezolana: la ficha no nombra la norma venezolana y el contacto usa HIPAA solo como referencia. El deck no cita ninguna.
- Que el patrocinio ejecutivo aún no está asegurado y la disponibilidad presupuestaria no está definida.

## Qué veo fuera del alcance de la IA o complicado (análisis interno, no va en la propuesta)

Pedido del usuario (2026-10-06): comentar lo que esté fuera del alcance de la IA o se vea complicado, sin anexarlo a la propuesta. Es una evaluación mía a partir de la ficha; no está verificada con la clínica ni con sus proveedores.

**1. El «logro inmediato» que la ficha da por identificado es el punto más difícil.** Conectar el triaje con la aprobación del seguro y con el presupuesto es una integración de tres piezas, no un caso de IA:
- El triaje con IA «ya instalado» está aislado: conectarlo exige una API o exportación y la colaboración de su proveedor.
- SAP (presupuestos) pide permisos y, normalmente, un consultor de SAP.
- La aprobación depende de la aseguradora, que es un tercero. Es probable que parte de la «cerca de 1 hora» sea espera de la aseguradora y no trabajo de la clínica. La IA de la clínica no acorta la respuesta de un tercero; sí puede preparar el expediente completo y verificar requisitos antes de enviarlo. Primera pregunta para la sesión de Admisión: qué parte de esa hora es interna.
- Tecnología solo da soporte y mantenimiento, sin desarrollo: no hay capacidad interna para construir ni mantener integraciones. Todo depende de terceros y de costo fuera de la Detección. También condiciona Habilidades (que el equipo «construya»).
- Por eso el deck dice «foco» y no «logro prometido», y deja «desarrollos e integraciones a medida» como etapa que sigue.

**2. Mucho de lo que piden es automatización o proceso, no IA** (el contacto mismo hace esa distinción y valora que se respete):
- Presupuestos con ítems predeterminados por patología: configuración de SAP y reglas; la IA solo ayuda a proponer paquetes a partir del histórico.
- Precio distinto por teléfono y al llegar: es un problema de fuente única de precios y de proceso. Un asistente de IA solo sirve si existe una lista de precios única y vigente.
- Reposición automática de insumos: pronóstico estadístico con reglas de reorden. Exige consumos por patología que hoy viven en sistemas separados por área; puede resolverse con hoja de cálculo o tablero, y la IA aporta poco al inicio.
- Seguimiento de proyectos (Notion, Gantt): herramienta y hábito, no IA; además fuera de las 4 áreas.
- «Digitalizar todo»: digitalizar no es IA. Eliminar el papel exige sistemas (historia clínica electrónica, ERP), con las excepciones legales que la clínica ya acepta (historia clínica física y récipe de controlados). Riesgo: expectativa de «todo» frente a un mapa de 4 áreas.
- **Recomendación:** que el Reporte Final clasifique cada oportunidad como IA, automatización o proceso. Es lo que diferencia a Intezia de los proveedores que el contacto critica.

**3. Datos regulados de pacientes.** Los procesos 1 y 2 manejan datos «regulados» y el 3, «confidenciales». Usar herramientas de IA de uso general con datos de pacientes exige condiciones con el proveedor (acuerdos, retención, anonimización); no verifiqué qué ofrece cada proveedor para datos de salud. La clínica tiene una política de seguridad, pero la ficha no la detalla. Por eso las sesiones usan datos sin identificar y el logro inmediato se demuestra con datos ficticios, lo que limita lo «inmediato». Conviene pedir la política y ver qué norma aplica (la ficha solo nombra HIPAA como referencia).

**4. El triaje con IA es software clínico.** La Detección no evalúa su exactitud clínica y el deck solo cita el dato declarado (unos 5 minutos). Riesgo: que la clínica espere que lo auditemos o validemos.

**5. Riesgos comerciales.**
- Decide la Junta Directiva, el patrocinio ejecutivo no está asegurado y no hay presupuesto definido. La Junta ya vio a varios proveedores que «trajeron algo»; el deck lo presentará el contacto, así que tiene que sostenerse solo y hablar el idioma de la Junta (por eso lleva «caso para la Junta»).
- 22 h es la Detección más grande de las recientes (6 h de Fundamentals + 16 h de áreas). Si el presupuesto no alcanza, una alternativa es empezar solo por Admisión y Finanzas, donde está el dolor y el logro identificado. Decisión del usuario y de ventas.
- La ficha pide «un caso con presupuesto»: no sé si el Reporte Final estándar incluye una estimación de inversión de la ruta que sigue. Lo puse como entregable; confirmar con servicio.
- Fundamentals: no sabemos cuántas personas hay por área ni cómo son los turnos. Con guardias nocturnas puede hacer falta más de 3 grupos y subirían las horas.
- Sesiones de 4 h con jefes y gerentes en medio de la operación: logística difícil, sobre todo en Admisión y Almacén.
- La modalidad no viene en la ficha.

## Riesgos que marca la ficha (Bloque F) y cómo los atiende el deck

1. **La decisión depende de la Junta y «siempre lleva tiempo».** El deck termina en un caso para la Junta y no menciona la aprobación.
2. **Dolor muy concreto y ya autodiagnosticado.** Los 4 hechos de la portada son los de la ficha, con sus cifras declaradas.
3. **Sensibilidad por los datos de pacientes.** Nota de datos sin identificar y camino hacia Políticas.
4. **Otras líneas futuras** (investigación médica, Tecnología): fuera del deck.

## Plan de sesiones (referencia interna; el deck solo lleva semanas)

| Semana | Sesión | Horas |
|---|---|---|
| 1 | Kick-off (aparte, sin horas) y Fundamentals en 3 grupos, de hasta 25 personas, armados con la clínica por áreas y turnos | 2 + 2 + 2 |
| 2 | Admisión y Finanzas y Facturación (1 o 2 personas por área), con el flujo del seguro y el presupuesto como foco | 4 + 4 |
| 3 | Atención al Paciente y Almacén (1 o 2 personas por área) | 4 + 4 |
| 4 | Reporte Final (Mapa de Calor, Índice de Madurez, hoja de ruta, caso para la Junta y recomendación de herramientas y licencias) | sin sesión |

Total 22 h. El calendario en 4 semanas, el orden y el Reporte Final en la semana 4 son propuestos por el sistema; confirmar con servicio y con la asesora.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py clinica-santiago-de-leon      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh clinica-santiago-de-leon             # verifica, genera el PDF y ajusta los campos
```
