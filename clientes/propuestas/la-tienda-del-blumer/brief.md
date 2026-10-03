# Brief — La Tienda del Blumer (DET-020)

## Datos administrativos

- **Empresa**: La Tienda del Blumer (empresa familiar de retail, tiendas físicas a nivel
  nacional, oficina administrativa en Valencia)
- **Sector**: Retail
- **Tamaño**: no especificado en la ficha (7 áreas, ~30 personas entre líderes y equipo
  operativo, cifra aproximada de la clienta)
- **Slug**: `la-tienda-del-blumer`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — servicio de interés único declarado en la ficha. La
  Habilidades y la autonomía tecnológica futura se muestran como **visión de ruta**, no se
  cotizan en este documento.
- **Tipo de documento**: Detección (`DET-020`) · Fundamentals (4h grupal, modalidad mixta) +
  auditoría de 7 áreas, 4h por área (28h), 32h totales.
- **Eje temático**: auditar las 7 áreas de La Tienda del Blumer con un logro inmediato en
  cada una, empezando por Contabilidad (revisión de facturas 100% manual), dejando trazada la
  ruta hacia Habilidades y hacia un equipo de Sistemas autónomo en IA.
- **Fecha del brief**: 2026-09-23
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento La Tienda del Blumer**
(`Levantamiento_La_tienda_del_Blumer_2026-09-23.pdf`, registrada 2026-09-23), elaborada por
la asesora **Verónica Rubio**, más el contexto y las instrucciones directas que el usuario
aportó sobre la reunión y el enfoque deseado.

## Contacto

- **Asesora comercial**: Verónica Rubio.
- **Contacto / decisor principal en la reunión**: Mariana Duque — familia fundadora (hija del
  presidente), recién incorporada (2 meses en el cargo), impulsora del proyecto desde adentro.
  Viene de experiencia previa en un banco digital, por eso llega con buen criterio de IA.
- **Quién firma y decide la contratación**: no confirmado con certeza en la ficha — dirigida
  por el papá de Mariana (presidente/dueño), con su hermano también en el área administrativa;
  probablemente el papá apruebe la inversión final. Mariana es la champion interna, pero las
  decisiones grandes probablemente necesiten su respaldo.
- **Servicio previo con Intezia**: ninguno — primer contacto.

## Las 7 áreas de Detección (dato directo de la ficha)

1. **Recursos Humanos**
2. **Tesorería**
3. **Contabilidad** — foco especial por volumen de trabajo manual (revisión de facturas)
4. **Sistemas** — ~4 personas, hoy enfocadas en soporte técnico diario
5. **Administrativo** (gestión de tiendas)
6. **Logística / Compras** (importaciones desde China)
7. **Inventario**

**Stakeholders por área**: Mariana Duque (impulsora) + líderes de cada área (varios con 20+
años en la empresa). En Contabilidad se pidió incluir, además del líder, a alguien más
operativo/joven del equipo (el líder actual es más de supervisión que operativo). Número de
personas a entrevistar por área: no definido con precisión, referencia aproximada de 1 a 2
líderes por área.

## Dimensionamiento — confirmado explícitamente por el usuario (2026-09-23)

- **4 horas de Fundamentals** (grupal) — el usuario pidió explícitamente 4h, no las 2h que
  usa el lineamiento por defecto para grupos más chicos (ver `amv-tecnologia/`, 3 áreas,
  2h de Fundamentals) — razonable dado que aquí son 7 áreas y ~30 personas, un grupo bastante
  más grande y diverso.
- **4 horas por área** × 7 áreas = **28 horas**.
- **Total: 32 horas** (4h Fundamentals + 28h de auditoría por área). Kick-off (1h) aparte, no
  cuenta en el total — mismo criterio que el resto de propuestas de esta sesión.
- **Modalidad mixta** (dato explícito de la ficha, Bloque específico Detección: "Modalidad de
  las sesiones: Mixta").

## Por qué "visión de ruta" y no Detección aislada — instrucción explícita del usuario

> *"Lo que necesito: la cotización/propuesta de Detección como puerta de entrada, pero armada
> con visión de ruta — la clienta ya conectó con la idea de avanzar después a Habilidades, y
> eventualmente a empoderar a su propio departamento de tecnología para que sea autónomo en
> IA. La propuesta debería dejar esa ruta visible, no presentar Detección como un servicio
> aislado."*

Esto está respaldado por la propia Ficha (Bloque F, observaciones internas): *"Encaje fuerte
con Detección como puerta de entrada, con visión explícita de la clienta hacia una ruta más
larga (Habilidades primero en los equipos, luego un ingeniero de sistemas con enfoque IA que
consolide y escale lo construido, hasta llegar a un dashboard ejecutivo centralizado)."*

**Decisión de diseño**: se agregó una **slide nueva dedicada** ("La ruta completa", slide 06)
que muestra 3 pasos — Detección (ahora, cotizada en este documento) → Habilidades (después, a
futuro, no cotizada) → Autonomía en IA (más adelante, visión final de Mariana) — SEPARADA del
roadmap interno de Detección (slide 05, que muestra los pasos operativos propios de este
servicio: Fundamentals+Áreas → Priorización → Reporte Final). Se prefirió esto sobre extender
el roadmap interno a 5-6 nodos porque mezclaría pasos operativos de este documento con fases
de negocio futuras de naturaleza distinta, y un roadmap de 5+ nodos en una sola página
arriesgaba desborde (ver `capacidad-cajas.md`). Mismo patrón conceptual que `amcor/` (Fase 1
cotizada + Fase 2 "a la medida del diagnóstico", no cotizada), pero con 2 fases futuras en vez
de 1, y con su propia slide en vez de vivir dentro del roadmap operativo.

**Instrucción explícita adicional del usuario**: *"dejar en claro que se dejan logros
inmediatos y se deja una hoja de ruta trazada, mencionalo en el roi"* — el texto de ROI en la
hoja de cotización menciona explícitamente ambos elementos (logro inmediato por área + hoja
de ruta hacia Habilidades y autonomía), no solo el diagnóstico.

## Dolor principal y logro inmediato (con precedente real y ya validado)

**Contabilidad revisa todas las facturas manualmente, una por una** — motivo declarado de por
qué esa área tiene tanto personal (Bloque D, cita textual: *"Todas las facturas que llegan las
revisan manualmente"*). Este es el logro inmediato ancla, igual patrón que `amv-tecnologia/`
(DET-019, mismo tipo de dolor: revisión manual de facturas) — **mismo estudio de Impacto
reutilizado** (Ardent Partners, ver abajo), porque el quick win es esencialmente el mismo
proceso (revisión/procesamiento de facturas).

Las otras 6 áreas también prometen un logro inmediato (patrón general, sin caso pre-validado
específico) — se define en la propia sesión de 4h de cada área, igual criterio que AMV.

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: Google Workspace.
- **Información dispersa**: varios sistemas separados por área, sin visibilidad cruzada —
  Mariana lo declaró explícitamente como un problema ("no que sea como que esto lo está
  haciendo por su lado... contabilidad tiene su propio sistema y lo usan ellos, nadie más lo
  puede ver").
- **Comunicación del equipo**: WhatsApp (quieren migrar a algo más corporativo) — dato de
  contexto interno, no se menciona como parte del alcance de esta Detección.
- **Uso de IA hoy**: prácticamente nulo y no organizado. El líder de Sistemas la usa de forma
  habitual pero no como herramienta principal; Mariana la usa activamente por su experiencia
  previa en un banco digital.
- **"Paso cero" en curso**: están migrando su servidor local a la nube (apuntando a BigQuery),
  en paralelo a un proceso de consultoría empresarial general — **no existe todavía** un
  diagnóstico de IA previo.
- **Sin política de datos/seguridad formal aún** ("apenas vamos a empezar este proceso").
  Regulación sectorial no confirmada por la clienta (retail).
- **Apertura al cambio**: media. **Patrocinio ejecutivo**: presente pero tibio. **Resistencia
  esperada** en líderes veteranos (20+ años en la empresa), sobre todo en Contabilidad/
  Auditoría ("temas de números, cosas delicadas") — anticipada por la propia clienta y por
  Verónica, de ahí antepone Fundamentals antes de la auditoría, para reducir esa fricción.

## Objetivo final esperado del Reporte Final (Bloque G)

Diagnosticar organigrama, roles y procesos para identificar qué automatizar o delegar a IA;
sentar las bases de una data limpia (tras la migración a la nube) y diseñar la ruta hacia la
futura centralización tipo "intranet" con dashboard ejecutivo para la dirección.

## Decisiones confirmadas / sin ambigüedad

1. **7 áreas de Detección** (RRHH, Tesorería, Contabilidad, Sistemas, Administrativo,
   Logística/Compras, Inventario) — dato directo de la ficha.
2. **Con logro inmediato por sesión** — ancla en Contabilidad (revisión de facturas), mismo
   patrón que AMV Tecnología.
3. **Modalidad mixta** — dato explícito de la ficha.
4. **Visión de ruta visible** (Habilidades → Autonomía tecnológica), no cotizada, en slide
   propia — instrucción explícita del usuario.
5. **Sin certificado de participación** en Entregables — Detección es una auditoría, no un
   curso (`deteccion-sin-certificado.md`).
6. **Sin garantía 30-60-90** — ese marco es de Habilidades, no de Detección (mismo criterio
   que `amv-tecnologia/`).
7. **Sin pre-recomendar ninguna herramienta de IA específica** antes del diagnóstico
   (Metodología ABR) — el Reporte Final entrega la recomendación formal.

## Impacto (§4.9) — reutilizado de `amv-tecnologia/`, mismo quick win (facturas)

**Ardent Partners — Accounts Payable Metrics That Matter (2025)**: la tasa promedio de
procesamiento de facturas sin intervención manual (touchless) es 32.6% en la industria,
contra 49.2% en las organizaciones de mejor clase; el mejor de su clase procesa una factura en
3.1 días contra 17.4 días del promedio (~5.6× más rápido); el costo promedio por factura es
$9.40 contra $2.78 del mejor de su clase (~70% menos costo); la tasa de excepciones que
requieren revisión manual es 22% en el promedio, contra 9% en el mejor de su clase. Mismo
estudio ya verificado en `amv-tecnologia/` — se reutiliza porque el quick win es el mismo tipo
de proceso (revisión manual de facturas).

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Calendario (dato directo del usuario, 2026-09-23)

*"coloca el kick off para el jueves 1 y las sesiones a partir del 5 de octubre martes y jueves
de 2 a 4"* → Kick-off **jueves 1 de octubre**. Como el 5 de octubre de 2026 es lunes, la
lectura razonable de "martes y jueves a partir del 5" es la semana del 5: primera sesión
**martes 6 de octubre**, 14:00-16:00. Con Fundamentals (4h = 2 sesiones de 2h) + 7 áreas ×
4h (2 sesiones de 2h cada una) = 16 sesiones de 2h, martes y jueves consecutivos, el
calendario completo corre de martes 6 de octubre a jueves 26 de noviembre. El calendario de
"Cómo arrancamos" (`.steps-calendar`) se muestra **resumido por área** (fechas de inicio/fin
de cada bloque de 2 sesiones, no las 16 sesiones individuales) para no desbordar la caja —
9 filas: Kick-off + Fundamentals + 7 áreas.

**Hora del kick-off no especificada por el usuario** — se usó 10:00-11:00 por consistencia con
el resto de propuestas de esta sesión (mismo horario usado en CAI-024/025/026); **confirmar
con Verónica** antes de enviar si el cliente prefiere otro horario.

## Pendientes

- Confirmar la hora exacta del kick-off (se usó 10-11 por defecto, sin dato explícito del
  usuario para este cliente).
- Confirmar con Verónica el orden exacto en que se auditan las 7 áreas (aquí se usó el orden
  en que aparecen en la ficha: RRHH, Tesorería, Contabilidad, Sistemas, Administrativo,
  Logística/Compras, Inventario) — podría reordenarse para auditar Contabilidad primero, dado
  que es el área de mayor dolor y logro inmediato ya validado.
- Estimado de costos — vacío en el PDF, lo llena ventas.

## Notas internas

- Caso base estructural: `amv-tecnologia/` (DET-019) — mismo patrón de Fundamentals + N áreas
  a 4h con logro inmediato, roadmap `.rmx-linear` de 3 etapas, Beneficios v3, Cierre escalera,
  precio estándar con descuento urgente + ROI (sin garantía, Detección pura). Escalado de 3 a
  7 áreas y de 2h a 4h de Fundamentals. **Slide nueva** ("La ruta completa") que AMV no tenía,
  agregada específicamente para este cliente por la instrucción de "visión de ruta".
