# Brief · Acua-e · Servicio de Detección (DET-025)

## Actualización 2026-10-08 · migrada a la plantilla v2 (8 slides) · VIGENTE

Instrucción directa del usuario: «mejorar la DET-025 con el nuevo formato». «Formato nuevo» = **plantilla compacta
v2.0** (commit `93e0b67`, 2026-10-07): el `datos.json` v1.4 se migró según la spec §13 y se regeneró con
`--actualizar-css --forzar-overrides`. Orden del deck: Portada · Alcance · Ruta · Cómo trabajamos · Entregables ·
Retorno · Inversión · Próximos pasos. El PDF de 6 slides (v1.4) queda en `_pdf-anteriores/`. Sin cambios de contenido
de fondo: 14 h, 4 entregables, 3 áreas más Fundamentals, 3 semanas, presencial, kick-off aparte.

### Decisiones

- **Datos** (respuesta del usuario al preguntar, 2026-10-08): «solo procesos, sin datos sensibles». Las sesiones
  levantan procesos y no cargan a ninguna herramienta de IA información confidencial de Acua-e (fórmulas, datos de
  clientes); los logros se prueban con ejemplos armados para la sesión. La ficha no habla de datos: mismo criterio que
  G-MAX, Conserval y la clínica. El deck no cita ninguna norma de publicidad farmacéutica.
- **Sin «Facilidad de pago»**: no se preguntó; el usuario la omitió en las últimas propuestas migradas, así que se
  aplicó el mismo criterio (`omitir: ["pago"]`). Si Ventas la quiere, se agrega con cuotas ligadas a los hitos.

### Qué cambió respecto de la v1.4 (en el lenguaje de la v2)

| v1.4 | v2 |
|---|---|
| `alcance.pasos` y `quien_construye` | `metodo` (4 pasos propios de Detección) y `metodo.quien_construye` |
| (sin método, logística ni asesora) | `metodo.practica` (sesiones presenciales, sin sistema nuevo, dos áreas un registro), `metodo.datos`, `por_que_orden`, `logistica` y `proximos_pasos.asesora` |
| (sin «para qué» por área) | `areas[].para_que` en Fundamentals y en las 3 áreas |
| `frentes[].etiqueta`, `areas_html`, «S1-S3», «S = semana» | `frentes[].nombre` = «Auditoría presencial», «1 a 3» y nota sin códigos |
| Fases «Nivelación», «Prioritarias», «Cierre del mapa» | «Nivel», «Pedidos», «Mapa» (cabeceras de ≤ 7 caracteres: con «2 entregables» al lado no cabían más largas) |
| Inversión «por horas de sesión»; Duración con las horas al frente | «Inversión del proyecto»; «Proyecto de 4 sesiones presenciales en 3 semanas. 14 horas de trabajo.» |
| Notas con la modalidad | Notas con licencias, Habilidades y Políticas, y términos y condiciones (la modalidad ya está en «Cómo trabajamos») |
| Sin asesora ni contacto | Slide 8 con Flavia Martínez (teléfono y correo tomados de su propuesta de Fibraspol; el cargo «Asesora comercial» es supuesto) |

La slide 3 conserva la 5.ª columna «Cierre» (Priorizar · Reportar · Proyectar), sin garantía 30-60-90. El agente de
marketing sigue solo como horizonte («Después · Habilidades» y fuera de alcance). `overrides.css` nuevo, el mismo
escalado de las slides 2, 3, 4 y 5 que la DET-026 (4 filas y una sola línea de trabajo).

### Pendientes (a confirmar antes de reenviar)

- Inversión, descuento y total (campos vacíos para ventas; pyme de 12 personas, el valor debe calzar con su escala) y
  cómo se comunica el plan de pago (no hay slide).
- Con Flavia: su teléfono, su correo y su cargo en la última slide; fechas, horarios y orden de las áreas; si
  el Reporte Final es en la semana 3 o la 4.
- La propuesta ya salió el 2026-10-06: confirmar si se reenvía el PDF nuevo y avisar que reemplaza al anterior. Estado:
  `Enviada` → `En corrección` → `Enviada` al regenerar (la `fecha_entrega` 2026-10-06 se respeta).

> Lo que sigue es el brief original del 2026-10-06 (formato v1.4); las decisiones de arriba prevalecen.

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Acua-e
- **Slug**: `acua-e`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección · Fundamentals (2h grupal, 12 personas) + auditoría de 3 áreas (Administración, Operaciones y Planta, Mercadeo), 4h por área (12h), 14h totales, modalidad presencial · formato compacto (`DET-025`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Auditar Administración, Operaciones y Planta, y Mercadeo de Acua-e, con un logro inmediato en cada área (empezando por el registro compartido de pedidos e inventario), para llegar a un mapa de oportunidades de IA y una ruta hacia la capacidad propia del equipo
<!--auto:inicio-->
- **Alcance**: 4 entregables en 3 áreas · 14 h de sesión · 3 semanas de trabajo desde el arranque · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Enviada` (meta.json; fecha_entrega 2026-10-06)
- **Asesora comercial**: Flavia Martínez (la ficha la registra como «Martinez»; en Fibraspol figura con tilde). Desde la v2 (2026-10-08) la slide 8 de próximos pasos la muestra.
- **Contacto / decisora**: la fundadora de Acua-e (Carolina Garcés), decisora única; la ficha dice que tiene una socia en administración. No aparece su nombre en el deck.
- **Ficha Comercial Intezia**: `Levantamiento_Acua_e_2026-10-02.pdf` (Ficha de Levantamiento, registrada 2026-10-02, elaborada por Flavia Martínez). Es la fuente primaria; qué se tomó y qué no está en la sección siguiente.
- **fecha_arranque_deseada**: no declarada. La ficha solo dice horizonte de incorporación de IA a corto plazo (0 a 3 meses). El formato compacto no lleva Calendario de inicio.
- **resultados_esperados**: objetivo del Reporte Final según la ficha: «mapa de oportunidades por área y capacidad instalada para que el equipo cree sus propias skills y agentes». Sin cifras: el retorno va en modo método.

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Acua-e (registrada el 02/10/2026, asesora Flavia Martínez) e instrucción directa del usuario del 06/10/2026
- **Fuente del insumo**: Ficha de Levantamiento de Acua-e
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- División Educación inferida: pyme farmacéutica, cliente corporativo privado. Alianza: no (el lead vino del evento GoFarma; confirmar con Flavia que no es una alianza).
- Horas por el lineamiento de Detección: Fundamentals de 2 h (un solo grupo, 12 personas, bajo el máximo de 25) y 4 h por área en 3 áreas = 14 h. El kick-off de arranque va aparte y no suma horas (convención general; en G-MAX se incluyó por instrucción explícita, aquí no hay instrucción).
- Calendario propuesto por el sistema, no dictado por la ficha: 3 semanas (S1 kick-off y Fundamentals, S2 Administración y Operaciones y Planta, S3 Mercadeo y Reporte Final). Las dos áreas ligadas al logro de pedidos e inventario van juntas en la semana 2. El Reporte Final en la semana 3 y el orden de las áreas hay que confirmarlos con servicio y con Flavia.
- Cada sesión se presenta como un entregable (4 en total: Fundamentals y las 3 áreas). El Mapa de Calor, el Índice de Madurez y el Reporte Final son trabajo del equipo consultor, sin sesión con el cliente ni horas propias: van como entregables transversales.
- Sesiones de área con 3 a 4 personas (dato de la ficha: «de 3 a 4 personas por área a entrevistar»), no solo con el líder del área.
- Retorno en modo método: la ficha no trae volúmenes ni tiempos por proceso; el Reporte Final los estima con lo que cada área entregue en su sesión (estimación referencial, sin compromiso de resultado).
- El agente de marketing farmacéutico y los agentes a medida se presentan solo como horizonte (Habilidades), no como alcance, por la nota explícita de la ficha (Bloque F: mantener Detección como primer paso). No se promete construirlos dentro de esta propuesta.
- Reglas de Detección que se conservan: sin certificado, sin garantía 30-60-90, sin pre-recomendar herramienta de IA (el cliente espera la recomendación del Reporte Final), sin dolor dramatizado ni citas textuales, sin datos personales de la fundadora (edad, sucesión, valoración de la empresa, uso personal de herramientas) ni nombres de personas.
- La ficha menciona restricciones sobre lo que se puede afirmar en publicidad de productos farmacéuticos, sin nombrar una norma. El deck no cita ninguna regulación.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Reporte Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas). Disponibilidad presupuestaria no definida en la ficha y riesgo explícito de la asesora: el valor debe calzar con la escala de una pyme de 12 personas.
- Confirmar con Flavia las fechas, los horarios y el orden de las áreas; el deck solo lleva semanas y no muestra asesora ni contacto.
- Confirmar si el Reporte Final se entrega en la semana 3 (misma semana de la última sesión) o en la 4.
- Confirmar con Flavia si el Reporte Final debe incluir de forma explícita la identificación de un líder interno de IA (la ficha lo menciona como candidato natural dentro del equipo familiar); no se incluyó en el deck.
- Confirmar si el kick-off se cuenta aparte (criterio por defecto) o dentro de las horas.

## Qué se tomó de la ficha y qué no

**Se tomó (con el deck como destino):**

| Dato de la ficha | Dónde quedó |
|---|---|
| Servicio de interés: Detección; áreas Administración, Operaciones/Planta y Mercadeo | Slides 1 a 5 (3 áreas, 4 h cada una) |
| 12 personas para AI Fundamentals | Fundamentals de 2 h en un solo grupo (máximo 25 por sesión) |
| 3 a 4 personas por área a entrevistar | Cada sesión de área, y el paso 1 de la slide 2 |
| Modalidad presencial en sus oficinas, sin sedes distintas | Slides 3 y 4 |
| Logro inmediato ya identificado: registro compartido de pedidos e inventario entre administración y planta | Hito y celda de la semana 2 (Administración y Planta juntas) |
| Proceso 1 (pedidos e inventario con papelitos y faltantes tardíos) y proceso 2 (contenido de marketing que las agencias no entienden) | Hechos 2 y 3 de la portada |
| La información vive en papel o en la cabeza de las personas | Hecho 1 de la portada |
| El equipo no usa IA ni tiene formación | Hecho 4 de la portada |
| Quiere recomendación de herramienta (aún no saben cuál) | El Reporte Final recomienda; el deck no pre-recomienda |
| Objetivo del Reporte Final: mapa por área y capacidad instalada | Titular «Mapa de oportunidades de IA y ruta de capacidad propia» y la hoja de ruta |
| Horizonte: agente de marketing farmacéutico | Solo como horizonte (fuera de alcance en slide 2, «Después · Habilidades» en slide 6) |

**No se llevó al deck (decisión deliberada):**

- Edad de la fundadora, sucesión, valoración de la empresa, venta de acciones o crédito, y su cita textual de despedida: es motivación personal. El deck habla de capacidad propia y de documentar cómo se hace cada proceso, sin dramatizar.
- Su uso personal de un GPT propio y el diplomado de IA: el deck dice «ninguna herramienta de IA usa hoy el equipo», que es lo que la ficha dice del equipo.
- El sobrino candidato a líder interno de IA: dato familiar. Se deja como pendiente (¿el Reporte Final identifica un líder interno de IA?).
- Las citas textuales de la ficha («pidió 50 potes…», «esto no lo podemos decir»): no se usan (regla de copy: nada textual que no esté verbatim y contextualizado; aquí se parafrasea el hecho).
- La regulación publicitaria farmacéutica: la ficha no nombra una norma, así que el deck no cita ninguna.

## Riesgos que marca la ficha (Bloque F) y cómo los atiende el deck

1. **Pyme de 12 personas: el valor tiene que calzar con su escala.** Dimensionamiento mínimo del lineamiento (14 h, 3 áreas, 1 grupo). Ventas define el precio con esto en mente (campos vacíos).
2. **Dispersión hacia marketing y agentes: mantener Detección como primer paso.** El agente de marketing aparece como horizonte, no como alcance (slide 2, fuera de alcance; slide 6, destino).
3. **Sin ecosistema ni uso previo de IA.** Fundamentals nivela primero; la herramienta la recomienda el Reporte Final (no se pre-recomienda).

## Plan de sesiones (referencia interna; el deck solo lleva semanas)

| Semana | Sesión | Horas |
|---|---|---|
| 1 | Kick-off (aparte, sin horas) y Fundamentals presencial, un solo grupo de 12 personas | 2 |
| 2 | Administración (3 a 4 personas) y Operaciones y Planta (3 a 4 personas), con el registro compartido de pedidos e inventario como logro candidato | 4 + 4 |
| 3 | Mercadeo (3 a 4 personas) y Reporte Final (Mapa de Calor, Índice de Madurez, hoja de ruta, recomendación de ecosistema y licencias) | 4 |

Total 14 h. El calendario en 3 semanas y el Reporte Final en la semana 3 son propuestos por el sistema (ver Decisiones y supuestos); confirmar con servicio y con Flavia.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py acua-e      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh acua-e             # verifica, genera el PDF y ajusta los campos
```
