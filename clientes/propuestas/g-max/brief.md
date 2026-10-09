# Brief — G-MAX (DET-024)

## Ajuste 2026-10-08 (noche): sin facilidad de pago y fundamentos de IA de regalo · SOLO G-MAX

Instrucción del usuario: «quitarle la lámina del 50 50 y [...] poner que los fundamentos de IA serán un regalo de parte
de Intezia. Solo a esta propuesta de G-MAX, no estandarices esto.»

- `datos.json` → `"omitir": ["pago"]`: el deck queda en **8 slides** (sin «Facilidad de pago») y el PDF con **7 campos**
  (sin `PagoCuota1..2`).
- **Fundamentos de IA = regalo de Intezia**: en la etapa «Nivelación» de la ruta («Un regalo de Intezia», resaltado) y
  como primera línea del campo `Notas` de la inversión. Internamente la nivelación sigue siendo de 4 h: en
  `programa.md` el total de referencia de 25 h la incluye; lo que se cotiza son el arranque y el levantamiento (21 h),
  a confirmar con ventas.
- **No es un cambio de la plantilla**: el formato de Detección sigue llevando la facilidad de pago y no regala la
  nivelación. `plantillas/habilidades-compacto-canonico/datos.ejemplo-deteccion.json` conserva la versión estándar.

## Actualización 2026-10-08 — rehecha (9 slides) con las correcciones de Keiber · VIGENTE (con el ajuste de arriba)

**Pedido:** David (2026-10-08): «genera la propuesta para el servicio de detección de GMAX basándote en la reunión
que tuvimos con el cliente», con la transcripción de la reunión de levantamiento. Se preguntó qué hacer con la
DET-024 existente y el usuario eligió **rehacerla en el formato nuevo con el mismo código**, aplicando las correcciones de la
reunión de **Keiber Quintana con David y María (2026-10-08)**. Keiber pidió armarla **desde la transcripción del
cliente** («no uses ese mensaje de María», el correo con las «áreas prioritarias») y **enviársela a ella primero,
antes que a María**. Por eso `meta.json` queda en **«En corrección»** hasta que Keiber la apruebe.

### Correcciones de Keiber (2026-10-08) y cómo se aplicaron

| Corrección | Aplicación |
|---|---|
| En una Detección no se dice qué frentes son prioritarios antes de detectar; «Resto corporativo» con el grueso de las áreas está mal; Atención al Paciente no salió como prioridad | Sin frentes ni prioridades. El alcance muestra las **4 áreas que nombró la Gerente General** (Gerencia de Operaciones, Gerencia de Tecnología, Dirección Médica, Recursos Humanos) y sus departamentos de la lista de personal |
| No juntar departamentos en la misma sesión («gallinero»): cada líder habla de lo suyo | «Un espacio por departamento» en Cómo trabajamos; levantamiento con el líder y su mano derecha |
| **20 horas**, sin decir cuántas por área; logística las reparte según lo que necesite cada departamento | Ruta e inversión: «20 horas de levantamiento presencial, repartidas según lo que necesite cada departamento» |
| En la propuesta **no van semanas ni sesiones**: se cuadran en el kickoff | Ruta en 5 etapas sin semanas ni sesiones; el calendario se acuerda en la reunión de arranque. Sin grupos de Fundamentals visibles |
| El logro inmediato no está garantizado por área; sí a nivel proyecto: **al menos 3** | Entregables: «al menos tres» logros; método: si un proceso exige mucho esfuerzo, pasa al Mapa de Calor |
| Quitar los números de los entregables («7 entregables», «3 entregables»…); no volver a nombrar las áreas en entregables; una página «bella» de lo que recibe | Slide 5 con 6 tarjetas sin conteos ni áreas: alcance y calendario, equipo nivelado, logros inmediatos, Mapa de Calor, Informe Final y hoja de ruta, inversión inteligente en licencias |
| Alcance = lo global (auditar y entregar logros) y ahí van las áreas | Slide 2: «Auditamos cada área y dejamos logros inmediatos», qué auditamos y para qué |
| Orden: qué hacemos, cómo, qué se llevan, retorno | Orden v2: portada, alcance, ruta, cómo trabajamos, entregables, retorno, inversión, pago, próximos pasos |
| Que lo entienda alguien que no estuvo en la reunión | Menos cifras: solo «3» (cobranza), «20 horas», «al menos tres» y los porcentajes del pago |
| No mandar tarea a los líderes antes de la sesión | «Sin tarea previa» en Cómo trabajamos |

### Cómo se armó el deck

- **Desde 2026-10-08 (misma tarde) se genera desde `datos.json`** con el formato de Detección de la plantilla compacta
  v3 (`"formato": "deteccion"`, `plantillas/deteccion-compacto.md`, CLAUDE.md §4.22). Este deck es el caso base de ese
  formato: `plantillas/habilidades-compacto-canonico/datos.ejemplo-deteccion.json` es su `datos.json` en la versión
  estándar (sin el ajuste de pago y regalo, que es solo de G-MAX).
  El texto de las 9 slides es idéntico al de la primera versión armada a mano (comparado slide por slide).
- Para cambiar algo: editar `datos.json` y correr `python3 scripts/generar-habilidades-compacto.py g-max` y
  `bash scripts/pdf-habilidades-compacto.sh g-max` (después, devolver `meta.json` a «En corrección» si sigue en
  revisión). `index.html`, `acroforms.json` y `programa.md` son generados: no se editan a mano.
- Archivado: el compacto de 6 slides (con su `datos.json` v1 y su PDF) en `_anterior-6-slides/`; la migración a la v2
  que hizo Ivana en paralelo (8 slides, commit `a546b6b`) en `_anterior-8-slides/`; el PDF de la versión armada a mano
  (mismo texto) en `_pdf-anteriores/` (local, no se versiona).

### Datos de la reunión con el cliente que se usaron

- 3 personas en cobranza a seguros arman a mano el expediente de cobro, sin criterios unificados, y sin
  seguimiento claro de la facturación vencida («cuánto me deben a 90 días»).
- Cada gerencia entrega un informe de gestión mensual que la Gerente General lee uno por uno; quiere estructura,
  almacenamiento y trazabilidad mes a mes y por trimestre.
- El proceso contable y administrativo se lleva en Excel, con un volumen alto de operaciones (en paralelo se
  parametriza su sistema; meta: tenerlo listo para el inicio del año contable; **contexto interno**, §4.11).
- Quieren control sobre qué herramienta usa cada puesto y qué datos salen de cada área (seguridad de la
  información de la clínica); hoy cada quien usa la IA que quiere.
- 48 personas en la reunión (≈28 corporativas, ≈20 asistenciales); la lista de personal confirmó 51.
- Objetivo: crecer en automatización y no en personal; encontrar dónde reducir costos.
- Modalidad presencial, jornadas de mañana; Recursos Humanos confirmará los participantes por departamento.

### Supuestos y pendientes (confirmar con Keiber antes de enviar a María)

1. **Horas**: el deck dice 20 h de levantamiento; el arranque (1 h) y la nivelación (4 h) van sin horas. Total
   interno 25 h (`programa.md`). ¿Las 20 h eran el levantamiento o el total?
2. **Logros inmediatos**: «al menos tres» para todo el proyecto.
3. **Áreas y departamentos**: sin asignar cada departamento a su área (no hay organigrama desglosado).
4. **Plan de pago**: 50 % al aprobar y 50 % con el Informe Final (estándar de `empresa/politicas-comerciales.md`);
   montos vacíos para ventas. Sin línea de facturación (moneda y tasa): confirmar con ventas.
5. **Asesora**: María Iribarren, con su teléfono y correo de las propuestas anteriores (sin cargo).
6. Nombre del entregable: «Informe Final» (como la skill de cierre de Detección), no «Reporte Final».
7. Inversión, descuento y total: vacíos para ventas (María anticipó un descuento de arranque).

## Actualización 2026-10-08 — migrada a la plantilla v2 (8 slides) · SUPERADA por la plantilla de Detección v3 del 2026-10-08 (de Ivana, commit `a546b6b`; archivada en `_anterior-8-slides/`)

Instrucción directa del usuario: «ajustar la DET-024 con el formato nuevo». El código **DET-024 sigue repetido**
(`fibraspol/` también lo usa, sin relación): se preguntó y el usuario eligió G-MAX otra vez. «Formato nuevo» =
**plantilla compacta v2.0** (commit `93e0b67`, 2026-10-07): el `datos.json` v1.4 se migró según la spec §13 y se
regeneró con `--actualizar-css --forzar-overrides`. Orden del deck: Portada · Alcance · Ruta · Cómo trabajamos ·
Entregables · Retorno · Inversión · Próximos pasos. El deck de 6 slides v1.4 y su PDF quedan en `_pdf-anteriores/`.
Sin cambios de contenido de fondo: 25 h, 7 entregables, 4 frentes, 2 grupos de Fundamentals, presencial.

### Decisiones del usuario al preguntar

- **Sin «Facilidad de pago»** (igual que la CAI-032): `omitir: ["pago"]`; ventas comunica el plan de pago por otro
  medio. El generador avisa que Ventas la pide en toda propuesta.
- **Datos:** «Se levantan procesos, sin datos personales»: las sesiones no cargan a ninguna herramienta de IA
  información que identifique a pacientes, personal o clientes (mismo criterio que la DET-027 de la clínica).
- **Grupo 1 de Fundamentals (~29 personas):** se deja como está, por encima del máximo de 25 por sesión del
  lineamiento de Detección (decisión del usuario del 01/10, reconfirmada).

### Qué cambió respecto de la v1.4 (en el lenguaje de la v2)

| v1.4 | v2 |
|---|---|
| `alcance.pasos` y `quien_construye` | `metodo` (4 pasos propios de Detección: entrevistamos, identificamos, construimos, dejamos listo) |
| (sin método, logística ni asesora) | `metodo.practica` (3 puntos), `metodo.datos`, `logistica` (presencial, 51 personas, arranque, ritmo) y `proximos_pasos.asesora` |
| (sin «para qué» por frente) | `areas[].para_que` en cada frente, con las palabras del cliente |
| `frentes[].etiqueta`, `areas_html`, «S1-S4», «S = semana» | `frentes[].nombre` = «Auditoría presencial», «1 a 4» y nota sin códigos |
| Fases «Nivelación», «Prioritarios», «Resto del mapa» | «Nivel», «Clave», «Resto» (cabeceras de ≤ 6 caracteres: con «2 entregables» al lado no cabían más largas) |
| Inversión «por horas», Duración con las horas al frente | «Inversión del proyecto»; «7 sesiones presenciales en 4 semanas. 25 horas de trabajo.» |
| Sin asesora ni contacto | Slide 8 con María Iribarren (teléfono y correo de sus otras propuestas; el cargo «Asesora comercial» es supuesto) |

La slide 3 conserva la 5.ª columna «Cierre» (Priorizar · Reportar · Proyectar), sin garantía 30-60-90. El retorno
(modo método, «decidir con datos») no cambió. `overrides.css` nuevo: escala de las slides 3, 4 y 5.

### Pendientes (a confirmar antes de reenviar)

- Inversión, descuento y total (campos vacíos para ventas; María anticipó un descuento de arranque) y cómo se
  comunica el plan de pago (no hay slide).
- Fechas y horas de las sesiones, orden de los frentes y cargo de la asesora en la última slide (con María). El
  deck dice «la fecha se acuerda con G-MAX»; el brief fija el kick-off para la semana del 12 de octubre de 2026,
  que ya está encima.
- La propuesta ya salió el 2026-10-01: confirmar si se reenvía el PDF nuevo. Estado: `Enviada` → `En corrección` →
  `Enviada` al regenerar (la `fecha_entrega` 2026-10-01 se respeta).
- Fibraspol, el otro DET-024, sigue en el deck canónico de 13 slides.

## Actualización 2026-10-06 — reexpresada en el formato compacto adaptado a Detección (6 slides) · REEMPLAZADA (archivada en `_anterior-6-slides/`)

Instrucción directa del usuario: "mejorar la DET-024 usando este nuevo formato, a pesar de que el
definido es de Habilidades, con una adaptación usando las reglas fijas de esta propuesta". El
código **DET-024 está repetido** (también lo usa `fibraspol/`, sin relación): se preguntó y el
usuario eligió G-MAX. El deck de 13 slides, su PDF y su `customize-g-max.py` están archivados en
`_anterior-13-slides/` y `_pdf-anteriores/`; `scripts/customize-g-max.py` se retiró (el compacto usa
el par genérico `customize-acroforms.py` + `customize-habilidades-compacto.py`).

**Hoy el deck es compacto de 6 slides, dirigido por `datos.json`** (fuente única; `index.html`,
`acroforms.json` y `programa.md` se generan). Flujo: `python3 scripts/generar-habilidades-compacto.py
g-max` → `node scripts/verificar-habilidades-compacto.js g-max` → `generar-pdf.sh g-max` →
`customize-acroforms.py g-max` → `customize-habilidades-compacto.py <pdf>`.

### Reglas fijas de esta propuesta que se conservan (todas de este brief)

Sin certificado (Detección pura) · sin garantía 30-60-90 (es de Habilidades) · sin pre-recomendar
herramienta de IA (el Reporte Final la recomienda) · sin dolor dramatizado ni citas · sin mencionar
el producto propio de cobranza ni la relación entre contactos · sin nombrar a Venemergencia · kick-off
de 1 h **dentro** de las 25 h (excepción explícita del usuario) · 4 frentes y 2 grupos de Fundamentals
con su composición visible (cuarta ronda) · 4 h por frente, 8 h en Resto corporativo · modalidad
presencial · visión de ruta Detección → Habilidades → Políticas con nombres reales.

### Cómo se mapeó Detección al esquema compacto

| En el compacto | En G-MAX |
|---|---|
| Carril | «Detección» (no hay herramienta) |
| Área | Cada **frente** (4) y «Arranque y Fundamentals» como etapa previa |
| Solución / entregable | Cada **sesión**: kick-off (F0), Grupo 1, Grupo 2 y los 4 frentes = 7 entregables, 25 h |
| Fases (3 columnas) | Nivelación (S1, 4 h) · Prioritarios (S2, 8 h) · Resto del mapa (S3-S4, 12 h) |
| 5.ª columna de la ruta | «Cierre»: Priorizar · Reportar · Proyectar (en vez del seguimiento 30-60-90) |
| Slide 5 transversales | Mapa de Calor e Índice de Madurez · Reporte Final · recomendación de ecosistema y licencias |
| Slide 6 retorno (modo método) | «Decidir con datos»: cómo se estima el retorno de cada oportunidad y qué decide G-MAX (licencias, prioridades, control) |

### Dónde quedó lo del deck de 13

| Antes | Ahora |
|---|---|
| Diagnóstico (5 puntos) | 4 hechos de la portada, cada uno atendido por un entregable |
| Objetivos, Programa, composición de los 4 frentes y de los 2 grupos | Slide 2 (cada frente muestra sus departamentos y los grupos) |
| Roadmap de 3 etapas, 3 cronogramas, calendario con fechas | Slide 3 (en semanas; los tiempos de cada sesión viven en `programa.md`) |
| Visión de ruta | Hito de cierre (slide 3) y tarjetas «Ahora / Después / Más adelante» (slide 6) |
| Beneficios | Slide 5 |
| ROI | Slide 6 |
| Propuesta Económica | Slide 4, sin garantía |
| Impacto (caso del sector salud, Venemergencia sin nombrar) | **Retirado**: el compacto no lleva Impacto (§4.9). Los datos reales siguen más abajo en este brief |
| Próximos pasos, Cierre con el contacto de María | **Retirados** por el formato compacto |

### Calendario: 4 semanas, no 3

El brief fijaba «~3 semanas» (12 oct a 2 nov). En semanas relativas al arranque son **4**: la sesión
Asistencial cae el lunes 2 de noviembre (semana 4) y el Reporte Final en la primera semana de
noviembre (también semana 4). Fechas y horas (8-10 y 8-12) siguen en la sección de calendario de más
abajo; el deck solo lleva semanas. Confirmar con servicio y con cada responsable.

### Cambios al generador (opcionales, sin efecto si no se usan)

`scripts/generar-habilidades-compacto.py` ahora acepta: `vocabulario` (entregable/frente/etapa previa
en vez de solución/área/proceso base), `area.composicion` (texto bajo el nombre del frente en la
slide 2), `frentes[].etiqueta`, `inversion.sin_garantia` y `seguimiento.tipo = "cierre"`. Comprobado:
DUSA, Fundación y CAI-032 salen idénticos (HTML, acroforms, programa y meta). Falta formalizarlo en
`plantillas/habilidades-compacto.md` §1 y `CLAUDE.md` §4.1a (proponer al usuario antes de editar esos
archivos estructurales). El estilo de `.comp`, y la escala de las slides 2 y 5 para pocos entregables,
viven en el `overrides.css` de este deck.

### Pendientes (a confirmar antes de reenviar)

- Calendario de 4 semanas, fechas y horas de cada sesión, y orden de los frentes (con María).
- Inversión, descuento y total: campos vacíos para ventas. El deck ya no muestra asesora ni contacto.
- El Grupo 1 de Fundamentals (~29) supera el máximo de 25 por sesión del lineamiento de Detección
  (composición definida por el usuario, no se modificó). ¿Se divide?
- La propuesta ya salió el 2026-10-01: confirmar si se reenvía el PDF nuevo.
- Otro DET-024 (Fibraspol) sigue con el formato anterior.

## Datos administrativos

- **Empresa**: G-MAX (clínica privada, salud, 1,5 años operativa)
- **Sector**: Salud clínica privada
- **Tamaño**: Mediana (50-250 empleados según la ficha) — universo confirmado por Patricia:
  51 personas en 22 departamentos (lista de personal enviada 2026-10-01; la ficha de
  levantamiento, registrada dos días antes, estimaba "48 personas... 24 departamentos" como
  cifra preliminar de la reunión — se usa la lista de personal como fuente final por ser la
  más reciente y confirmada).
- **Slug**: `g-max`
- **División Intezia**: `educacion` (cliente corporativo pagante)
- **Servicio (§4.1a)**: `deteccion` — único servicio de interés declarado en la ficha. El
  Fundamentals para las 51 personas es parte del propio lineamiento de Detección (2h
  grupales), no un combo con Habilidades.
- **Alianza**: no
- **Tipo de documento**: Detección (`DET-024`)
- **Eje temático**: auditar los departamentos de G-MAX, con foco en Seguros y Cobranzas y
  Atención al Paciente, para construir un mapa de oportunidades con control sobre el uso de
  la información, antes de invertir en licencias.
- **Fecha del brief**: 2026-10-01 (reajustado 2026-10-01, mismo día, a partir de feedback del
  usuario sobre la primera versión)
- **Estado**: `Enviada`
- **Origen**: Ficha de Levantamiento G-MAX (`Levantamiento_G_MAX_2026-10-01.pdf`, registrada
  2026-09-29, elaborada por María Iribarren) + lista de personal (`gmax.pdf`, 51 personas,
  enviada 2026-10-01) + instrucciones directas del usuario sobre el enfoque y la
  organización de sesiones (chat, 2026-10-01) + ronda de ajustes del usuario tras la primera
  entrega (chat, 2026-10-01, mismo día).

## Contacto

- **Asesora comercial**: María Iribarren.
- **Contacto / decisora principal**: Patricia Ortega Coneo — Gerente General.
- **Servicio previo con Intezia**: ninguno — primer contacto.
- **Propuesta previa sin aprobar**: no.

## Decisiones confirmadas con el usuario (2026-10-01, primera ronda)

1. **División**: Educación.
2. **Alcance de la auditoría**: los departamentos completos de G-MAX, organizados en frentes
   de sesión. Coincide con el dato del Bloque específico de Detección de la ficha ("líder +
   mano derecha por área").
3. **Alianza**: no.
4. **Calendario**: kick-off semana del 12 de octubre de 2026, sesiones a partir de esa
   semana (instrucción directa del usuario).
5. **Producto propio de cobranza**: la ficha anota como nota interna de venta que G-MAX es
   "candidato ideal" para un futuro producto propio de cobranza de Intezia. **No se menciona
   en el deck** — queda solo como nota interna aquí, para seguimiento comercial de María.
6. **Sin mención de relación familiar** entre contactos de G-MAX y de otros clientes de
   Intezia — dato interno que no aplica a ningún documento de esta propuesta.

## Reajuste confirmado con el usuario (2026-10-01, segunda ronda — reemplaza la primera versión)

El usuario revisó la primera versión (12 frentes, 3 grupos de Fundamentals, 52h) y pidió
compactarla significativamente, con instrucciones explícitas y cálculo de horas propio:

1. **Kick-off (1h)**: ahora se **incluye** en el total mostrado en Objetivo, Propuesta
   Económica y Cronograma (instrucción explícita) — excepción puntual a la convención general
   del sistema de dejarlo aparte, solo para esta propuesta.
2. **AI Fundamentals**: de 3 grupos de ~17 a **2 grupos de 2h**, con composición explícita del
   usuario:
   - **Grupo 1, corporativo y operativo (~29 personas)**: Gerencia General, Administración,
     Seguros, Atención al Paciente, Logística, Almacén, Farmacia, Servicios Generales,
     Tecnología, Procesos y Recursos Humanos.
   - **Grupo 2, asistencial (~22 personas)**: Dirección Médica, Enfermería y Laboratorio.
   Headcount verificado contra la lista de personal: Grupo 1 = 29 exacto (incluye Auditoría y
   Procesos + Procesos como "Procesos"), Grupo 2 = 22 exacto. Suman 51.
3. **4 frentes agrupados de auditoría** (no 12): el usuario pidió "cuatro frentes agrupados de
   4 horas" y dio la cuenta total "25 horas (1+4+12+8)" — matemáticamente eso exige que 3
   frentes sean de 4h (12h) y 1 sea de 8h (doble sesión), no los 4 iguales. Reconstruido y
   **confirmado con el usuario** a partir de los 2 grupos de Fundamentals (ver tabla abajo).
4. **Página 10 (Impacto)**: retirar Experian Health (datos de EE.UU., instrucción explícita de
   no apoyarse en cifras externas) y usar un caso propio del sector salud, **sin nombrar al
   cliente** — el usuario sugirió explícitamente Venemergencia como candidato.
5. **Página 6 (La ruta completa)**: usar nombres reales de servicio — después de Detección
   viene Habilidades, y luego Políticas (responde directo a la preocupación de Patricia por
   el control de los datos).
6. **Consistencia de horas**: Objetivo, Propuesta Económica y Cronograma deben mostrar el
   mismo conteo total (25h, incluyendo Kick-off).

## Los 4 frentes de auditoría (confirmado con el usuario, segunda ronda)

| # | Frente (sesión) | Departamentos agrupados | Duración | Prioridad |
|---|---|---|---|---|
| 1 | Seguros y Cobranzas | Seguros | 4h | ★ Prioritario |
| 2 | Atención al Paciente | Atención al Paciente | 4h | ★ Prioritario |
| 3 | Resto corporativo | Gerencia General, Administración y Tesorería, Informes de gestión gerencial (transversal, vía Gerencia General), Logística, Almacén (+Almacén Quirófano), Farmacia (3 sub-ubicaciones), Servicios Generales, Tecnología, Procesos (Auditoría y Procesos + Procesos), Recursos Humanos — 9 departamentos | 8h (2 jornadas de 4h, por volumen) | — |
| 4 | Asistencial | Dirección Médica (+Hemodiálisis), Enfermería (4 sub-áreas), Laboratorio — 3 departamentos | 4h | — |

**Total auditoría por frente**: 4h + 4h + 8h + 4h = **20h**.

Nota: Administración/Tesorería e Informes de gestión gerencial ya no tienen sesión dedicada
propia (sí la tenían en la versión de 12 frentes) — quedan dentro del frente 3 "Resto
corporativo", consistente con la instrucción de compactar a 4 frentes.

## AI Fundamentals — 51 personas, 2 grupos

- **Grupo 1 · Corporativo y operativo** (~29 personas): mismos departamentos del frente 3 +
  los 2 frentes prioritarios (Seguros, Atención al Paciente).
- **Grupo 2 · Asistencial** (~22 personas): mismos departamentos del frente 4.
- 2 sesiones × 2h = **4h totales**. Se enfocan los ejemplos de cada grupo en su propio día a
  día (corporativo/administrativo vs. clínico-asistencial), instrucción explícita del
  usuario.

## Dimensionamiento total (reajustado)

- Kick-off: **1h** (incluido en el total, instrucción explícita del usuario)
- Fundamentals: 2 grupos × 2h = **4h**
- Auditoría por frente: **20h**
- **Total: 25h** — debe aparecer igual en Objetivo, Propuesta Económica y Cronograma.

## Calendario (kick-off lunes 12 de octubre de 2026, ~3 semanas de ejecución)

| Fecha | Hora | Sesión |
|---|---|---|
| Lun 12 oct | 10-11 | Kick-off |
| Mar 13 oct | 8-10 | Fundamentals · Grupo 1 Corporativo |
| Jue 15 oct | 8-10 | Fundamentals · Grupo 2 Asistencial |
| Mar 20 oct | 8-12 | Seguros y Cobranzas |
| Jue 22 oct | 8-12 | Atención al Paciente |
| Mar 27 oct | 8-12 | Resto corporativo · día 1 |
| Jue 29 oct | 8-12 | Resto corporativo · día 2 |
| Lun 2 nov | 8-12 | Asistencial |

8 sesiones, 12 oct a 2 nov = 3 semanas exactas, consistente con la instrucción del usuario
("en unas 3 semanas de ejecución"). Priorización y Reporte Final: primera semana de
noviembre (trabajo de equipo consultor + reunión de entrega con Patricia). Calendario
propuesto por Intezia — sujeto a ajuste real según disponibilidad de cada responsable.

## Diagnóstico (hechos documentados en la ficha — sin dramatizar, sin citas textuales en el deck)

1. Cobranza a seguros: 3 personas arman a mano el expediente de cobro de cada seguro
   bajando información de varios lados, sin criterios unificados, trabajando con Excel y
   llamadas. No hay seguimiento sistemático a la facturación vencida por antigüedad (30, 60,
   90 días) y la información no se comparte con otras áreas.
2. Informes de gestión: cada gerencia entrega un informe mensual a Patricia; ella los lee
   uno por uno, sin estructura común, almacenamiento ni trazabilidad mes a mes o trimestral.
3. Proceso contable y administrativo: se lleva en Excel con volumen importante de
   operaciones, en paralelo a la parametrización de Odoo (módulo de inventario casi listo;
   el módulo administrativo/contable arrancó esta semana con asesores externos).
4. Sin política de uso de IA. Preocupación explícita por el control de qué herramienta usa
   cada puesto y qué datos salen de cada área (confidencialidad de datos de la clínica).
5. Ecosistema tecnológico mixto, sin definir (Microsoft 365 + Google Drive). La propia
   directiva fue receptiva a la recomendación de definir un solo ecosistema + Claude.
6. Nivel de partida con IA: uso suelto y sin criterio, sin formación previa.

## Por qué "visión de ruta" con nombres reales de servicio

El objetivo final que Patricia espera del Reporte Final es un "mapa de oportunidades por
área para no invertir a ciegas, con datos para justificar qué licencias adquirir", y su
criterio de éxito es "ver de manera inmediata cuáles procesos podemos mejorar y optimizar" y,
a partir de ahí, "crecer de forma gradual y consciente" (ambos del Bloque G/F de la ficha).
El usuario pidió explícitamente nombrar los servicios reales que siguen: **Habilidades**
(capacitación práctica sobre los hallazgos) y **Políticas** (responde directo a la
preocupación de Patricia por el control de qué herramienta usa cada puesto y qué datos
salen de cada área). Sin mencionar el producto propio de cobranza ni ningún otro producto
específico no confirmado.

## Logro inmediato / quick win

Candidato fuerte identificado en la ficha: **estructura del informe de gestión mensual**
(Bloque G). Se construye dentro del frente 3 "Resto corporativo" (que ahora incluye
Informes de gestión gerencial).

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: mixto, sin definir (Microsoft 365 + Google Drive). Se recomendó definir
  uno solo + Claude Teams; la recomendación fue bien recibida, pero no se afirma en el deck
  que G-MAX ya migró o migrará — solo que el plan se apoya en el entorno que ya usan.
- **Datos del negocio**: mezcla de sistemas y hojas de cálculo; se está parametrizando Odoo
  (inventario casi listo, administrativo/contable arrancó esta semana).
- **Comunicación del equipo**: WhatsApp y correo.
- **Herramientas de IA hoy**: ninguna corporativa definida. Herramienta deseada: Claude
  (Anthropic).
- **Apertura al cambio**: alta. **Patrocinio ejecutivo**: fuerte y visible.
- **Sin política de datos/seguridad de IA** — preocupación explícita por filtración de datos
  de la clínica.

## Objetivo final esperado del Reporte Final (Bloque G de la ficha)

Mapa de oportunidades por área para no invertir a ciegas, con datos que justifiquen qué
licencias adquirir, y una herramienta de IA organizativa por puesto con control de la
información. Acelerar el levantamiento de procesos que ya están haciendo para parametrizar
el ERP (Odoo).

## Impacto (§4.9) — caso propio de Intezia en el sector salud, sin nombrar al cliente

Instrucción explícita del usuario (segunda ronda): retirar Experian Health (datos externos de
EE.UU.) y usar un caso propio del sector, sugiriendo Venemergencia (empresa venezolana de
servicios de emergencia y atención médica) como candidato, **sin mencionarla por nombre** en
el deck — se refiere genéricamente como "empresa del sector salud".

**Fuente real usada**: `clientes/dashboards/venemergencia/resultados.json` — Dashboard de
Impacto del programa "Adopción de Claude en Cascada · Fase 1" (CAP-047, cierre 2026-08-07,
n=22 respuestas):
- **97% de retención real** del contenido al cierre (Bloque C · % de aciertos — única cifra
  **medida**, no percibida, según el criterio de honestidad de medición de
  `dashboard-edutrace.md §4.17`).
- **Índice de Impacto general: 90/100**.
- **4.5 estrellas** de satisfacción ("Excelente").
- Aplicabilidad percibida 4.77/5 (95%) y productividad percibida 4.68/5 (94%) — Bloque B,
  **autopercepción**, etiquetadas como "percibida" en el copy del deck, no como medición.

Fuente citada en el deck como "programa de capacitación en IA de Intezia, empresa del sector
salud (2026)" — real, verificable internamente, sin nombrar al cliente.

## Decisiones confirmadas / sin ambigüedad

1. **22 departamentos agrupados en 4 frentes** (tabla arriba) — confirmado con el usuario en
   la segunda ronda, reemplaza la agrupación de 12 frentes de la primera versión.
2. **Sin logro inmediato ancla único**: el candidato de quick win (informes de gestión) se
   construye dentro del frente 3, igual que el resto.
3. **Modalidad presencial** en las oficinas de G-MAX — dato explícito de la ficha.
4. **Visión de ruta con nombres reales**: Detección (ahora) → Habilidades (después) →
   Políticas (más adelante), sin mencionar productos específicos no confirmados.
5. **Sin certificado de participación** en Entregables — Detección es una auditoría, no un
   curso (`deteccion-sin-certificado.md`).
6. **Sin garantía 30-60-90** — ese marco es de Habilidades, no de Detección.
7. **Sin pre-recomendar ninguna herramienta de IA específica** antes del diagnóstico
   (Metodología ABR) — el Reporte Final entrega la recomendación formal, aunque Claude ya es
   la herramienta de interés expresada por el cliente.
8. **Sin puntos de dolor dramatizados ni citas textuales en el deck** — instrucción explícita
   del usuario (2026-10-01): el diagnóstico se redacta en lenguaje propio de Intezia, sin
   comillas de cita, basado estrictamente en los hechos documentados en la ficha.
9. **Kick-off incluido en el total de horas mostrado** — excepción puntual para esta
   propuesta, instrucción explícita del usuario; no es un cambio al criterio general del
   sistema (que sigue dejando Kick-off aparte salvo instrucción en contrario).

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: María Iribarren.

## Pendientes

- Confirmar con María el orden exacto en que se auditan los 4 frentes (aquí se usó el orden
  de prioridad declarado por Patricia: Seguros/Cobranzas → Atención al Paciente → Resto
  corporativo → Asistencial).
- Confirmar hora exacta de cada sesión con cada responsable (se usó 8:00-12:00 para las
  jornadas de 4h y 8:00-10:00 para Fundamentals, dato de la ficha: "en la mañana").
- Estimado de costos — vacío en el PDF, lo llena ventas (María ya anticipó un descuento de
  arranque, a su criterio).

## Tercera ronda de ajustes (2026-10-01, mismo día)

1. **Página 6 (La ruta completa)**: se retiró el lenguaje "cotizado en este documento / a
   futuro, no cotizado / visión de [cliente]" de los 3 `vision-tag` — instrucción explícita
   del usuario: "eso no debe salir en ninguna propuesta" (regla general del sistema, no solo
   de G-MAX). Los tags quedan solo "Ahora" / "Después" / "Más adelante"; el estilo visual
   (borde sólido vs. punteado, ya existente) comunica qué está cotizado sin decirlo en texto.
2. **Página 9 (Beneficios)**: Entregables y "Valor inmediato" salían con fondo blanco — el
   flujo genérico (`agregar-campo-precio.py` → `customize-acroforms.py`) hornea esas 2 cajas
   con /MK /BG blanco por defecto (pensado para decks claros), pero este deck usa Beneficios
   v3 oscuro (`.s-benefits-v2`). Mismo patrón ya resuelto en `la-tienda-del-blumer/` (de donde
   se clonó este deck) vía un script propio `customize-<slug>.py` con función `rebake_dark()`
   — **se creó `scripts/customize-g-max.py`** replicando ese mecanismo (mismo /Rect ampliado,
   mismo fondo oscuro `(0.06,0.06,0.06)` + texto blanco). **No se replicó** la parte de
   `CIERRE_FIELDS` de blumer (crear CierreResultado/CierrePaso1-3 como AcroForm real): en
   G-MAX esos campos no son AcroForm, son texto estático horneado por Chrome al imprimir el
   HTML (ver `bug-cierre-escalera-texto-vacio-sin-script-propio.md`), y ya funcionan bien así
   — no hacía falta tocarlos.

**Regeneración del PDF a partir de ahora — trío obligatorio, en este orden exacto**:
```
./scripts/generar-pdf.sh g-max
python3 scripts/customize-acroforms.py "<pdf>" "clientes/propuestas/g-max/acroforms.json"
python3 scripts/customize-g-max.py "<pdf>"
```
`generar-pdf.sh` detecta `customize-g-max.py` y lo sugiere como único siguiente paso, pero
**omitir `customize-acroforms.py` dejaría Entregables/Acreditación con el texto DEFAULT
genérico** (no el de G-MAX) — `customize-g-max.py` solo re-pinta la apariencia (fondo oscuro)
sobre el valor `/V` que ya esté puesto, no fija contenido propio. Siempre los 3 pasos, en ese
orden (mismo criterio ya documentado para `la-tienda-del-blumer/`).

## Cuarta ronda de ajustes (2026-10-01, mismo día)

El usuario pidió que la composición de los 4 frentes y de los 2 grupos de Fundamentals
quedara visible en el deck mismo (antes solo estaba documentada aquí en brief.md, no en el
PDF de cara al cliente):

- **Slide 4 ("El proyecto")**: se agregó un bloque `.detail-panel` ("Los 4 frentes, en
  detalle") debajo de la grilla de módulos, nombrando cada frente con su composición exacta.
- **Slide 7 (Fundamentals)**: se agregó el mismo componente `.detail-panel` ("Cómo dividimos
  los grupos") debajo de las 3 columnas, con la composición exacta de Grupo 1 y Grupo 2 tal
  como el usuario los definió originalmente.

Componente nuevo (`.detail-panel`/`.detail-grid`/`.detail-item`/`.detail-num`/`.detail-name`/
`.detail-list`), propio de este deck en `overrides.css` — no existe en `_base/styles.css`.
Ajustado de tamaño una vez (font-size, line-height, margin-top) tras un desborde de +26px en
slide 4 detectado por `verificar-overflow.js`.

## Notas internas

- Caso base estructural: `la-tienda-del-blumer/` (DET-020) — mismo patrón de Fundamentals +
  N frentes a 4h, roadmap `.rmx-linear` de 3 etapas, slide de visión de ruta, Beneficios v3,
  Cierre escalera.
- **Reajuste 2026-10-01**: de 12 frentes/46h/3 grupos de Fundamentals (primera versión) a 4
  frentes/20h/2 grupos de Fundamentals, por instrucción directa del usuario — ver sección
  "Reajuste confirmado" arriba para el detalle completo y el porqué de cada número.
- **No mencionar** en ningún documento de cara al cliente la posible relación entre contactos
  de G-MAX y de otros clientes de Intezia (instrucción explícita del usuario).
- **No mencionar** en el deck el producto propio de cobranza — queda como nota de venta
  futura para María.
- **No mencionar** por nombre a Venemergencia en el deck — solo "empresa del sector salud".
