# Brief — HJB Química · Detección (15 áreas) + Habilidades directivas (CAI-031)

## Pase de balance visual (2026-10-02, d) — sin espacios en blanco en 5/6/7/9

El pase anterior (c) agrandó el contenido de estas 4 slides pero todavía dejaba espacio
vacío visible. Instrucción del usuario: llevarlo más grande y al centro para que no quede
espacio en blanco.

1. **Garantía (6) / Casos (7) / Por qué Intezia (9)**: `.followup-cards` pasa a `flex:1`
   (la fila de tarjetas crece para llenar todo el alto disponible) y `.rmx-facets` usa
   `justify-content: space-evenly` (antes `center`) para que las 1-2 facetas de cada
   tarjeta se repartan en todo ese alto en vez de apelotonarse en el medio. Tipografía de
   nombre (18→26px) y de facetas (12→15px) otra vez más grande. Resultado: tarjetas que
   llegan casi al pie de página, sin franja vacía debajo.
2. **Entregables (5)** — hallazgo clave: el texto horneado en los campos AcroForm **siempre
   arranca arriba del rect** (`acroform_appearance.py` no tiene lógica de centrado vertical
   propio) — agrandar la caja más allá de lo que el texto ocupa solo mueve el vacío a
   *dentro* de la caja (confirmado visualmente en el intento anterior: texto en el tercio
   superior, caja vacía abajo). La corrección real fue **la contraria**: volver la caja a un
   tamaño que coincide con el contenido (h=320) y centrar la unidad completa (etiqueta +
   caja) en el espacio entre el header y el footer — calculado explícitamente (header
   termina ~y=138, footer empieza ~y=740, unidad de 354px centrada → top=262 la etiqueta,
   top=296 la caja). Recalculado el rect AcroForm en `customize-hjb-quimica.py`
   (BENEFICIOS_LAYOUT) a juego. Si se vuelve a tocar esta caja, agrandarla NO es la
   solución — hay que igualar tamaño a contenido y centrar la posición.

Verificado sin desbordes (11 slides) y revisado visualmente cada slide tras cada ajuste.

## Pase de balance visual (2026-10-02, c) — de 12 a 11 slides

Instrucción del usuario: eliminar la slide 5 ("Habilidades" — 5 módulos como construcción)
y aprovechar los espacios vacíos del resto del deck de forma armónica; sobre la marcha,
también mejorar el diseño del Cierre para que sea más atractivo al cliente.

1. **Slide 5 eliminada** — su contenido (Construir/Probar/Adoptar mapeado a los 5 módulos)
   no se descartó: se condensó dentro de "Vista por fase · Fase 2" (ahora slide 3, layout de
   2 columnas: tabla de horas + panel "Lo que construye cada responsable"), que antes tenía
   mucho espacio vacío a la derecha de una tabla angosta. El deck pasa de 12 a 11 slides.
2. **Priorización** (slide 4): matriz más grande (340→430px alto, celdas con más padding y
   tipografía mayor) y franja de Índice de Madurez con más aire — llenaba poco menos de la
   mitad de la slide.
3. **Entregables** (slide 5): cajas de 460→380px (mejor proporción al contenido real),
   texto más grande (13→15pt) y con el doble de interlineado, y un tinte de color sutil por
   fase (amarillo Fase 1, naranja Fase 2) para diferenciarlas a simple vista. Recalculado el
   rect AcroForm en `customize-hjb-quimica.py` (BENEFICIOS_LAYOUT) para que coincida.
4. **Garantía / Casos / Por qué Intezia** (slides 6, 7, 9): tarjetas con mucho más padding y
   tipografía mayor (nombre 18→23px, facetas con más espacio entre sí) — eran las slides con
   más vacío debajo de las tarjetas. "Por qué Intezia" también recuperó una 2ª faceta por
   tarjeta (Continuidad/Alcance/Vigencia) y una intro, contenido ya implícito en el resto del
   documento (mismo equipo y mismo criterio en ambas fases), no un dato nuevo.
5. **Cierre rediseñado** (slide 11, ahora la última): se agregaron los mismos blobs
   orgánicos de la Apertura (círculo naranja-amarillo arriba a la derecha + acento amarillo
   abajo a la izquierda) para un cierre de deck a juego con la apertura, una frase cálida
   "Gracias por la confianza" sobre el logo, y más presencia visual en la escalera y el
   banner de resultado (esquinas redondeadas + sombra). **Los 4 campos AcroForm
   (CierreResultado + CierrePaso1-3) no cambiaron de posición ni tamaño** — todo lo nuevo son
   elementos puramente decorativos, para no arriesgar el desajuste entre la caja visual y el
   campo real (riesgo ya documentado en el sistema, ver memoria
   `bug-entregables-acroform-box-narrow` y afines).

Verificado sin desbordes (`verificar-overflow.js`, 11 slides) y revisado visualmente slide
por slide tras cada cambio.

## Formas orgánicas vs. geométricas (2026-10-02) — ajuste acotado a este deck

El usuario compartió el manual de identidad corporativa oficial de Intezia
(`manual-de-marca.pdf`) y pidió adaptar diseño/estilo. Comparado contra
`empresa/marca-visual.md`: **colores y tipografía ya coinciden exactamente** (paleta
`#000000`/`#F4BA1A`/`#E58423`, Graphit Bold/Regular). La diferencia real: el manual usa
**formas orgánicas redondeadas** (blobs) en sus láminas divisoras, mientras el sistema
compartido (`plantillas/_base/styles.css`) documenta y usa **formas geométricas de bordes
nítidos** (el único caso de `rotate(45deg)` en todo el CSS compartido, en `.s-cover::before`).

**Alcance confirmado con el usuario: solo este deck, solo las formas** (no colores/
tipografía — ya alineados; no logo/ícono ni contenido institucional Misión/Visión/Valores —
no pedido). No se tocó `plantillas/_base/styles.css` ni `empresa/marca-visual.md` — el
estándar compartido sigue siendo el geométrico hasta que se pida explícitamente lo
contrario para el resto del sistema.

**Qué se cambió** (`overrides.css` de este deck únicamente): el diamante/rombo rotado de
la Apertura (slide 1) se convirtió en un círculo (blob), y se agregó un acento amarillo
redondeado en la esquina inferior izquierda, replicando el patrón de 2 tonos (naranja
arriba-derecha, amarillo abajo-izquierda) de las láminas divisoras del manual. El acento
amarillo usa `bottom:0` sin offset negativo — un primer intento con `bottom:-70px` (blob
centrado exactamente en la esquina) disparó el detector de desborde (+70px): el script
`verificar-overflow.js` vigila específicamente que nada exceda el borde **inferior** de la
página (relevante para paginación de impresión), aunque `overflow:hidden` lo recorte
visualmente — a diferencia del borde superior/derecho, donde el diamante original sí
sangra sin problema. Ajustado a `height:46px` (bajo los 56px donde empieza `.id-line`) para
no superponerse con "Código: CAI-031".

## Reestructuración 2026-10-02 — de 21 a 12 slides, formato consultivo

Instrucción directa del usuario: reconstruir el deck completo trabajando **solo con su
contenido existente** (sin pedir insumos nuevos, sin WebSearch, sin placeholders
"pendiente"), con estas reglas — pensadas para que esta estructura sirva de **plantilla**
a futuras propuestas del combo Detección+Habilidades:

1. **Sin nombres de personas de HJB** (solo cargos) — afectaba el organigrama (antigua p.5)
   y el roadmap de Detección (antigua p.6, "Con quién: Vianey Reyes y Jorge Molina").
2. **Sin datos de terceros**: fuera la slide de Impacto (Microsoft & LinkedIn, antigua p.15).
3. **Solo el alcance contratado**: fuera la slide "La ruta completa" (cascada, antigua p.7) —
   0 menciones de cascada en todo el documento (la instrucción permitía hasta 1 línea en el
   cierre; se optó por omitirla por completo, más conservador con "solo alcance contratado").
4. **La Detección no es un "360"**: su entregable central es una hoja de ruta hacia
   Habilidades con secuencia **construir → probar → adoptar** (se usa "probar", no
   "testear" — mismo concepto, sin anglicismo adyacente). Aparece en la intro de la Fase 1 y
   como etiqueta de cada módulo de Habilidades.
5. **Títulos serios y consultivos**: la Apertura (fusiona antiguas p.1+2) ya no usa titular
   llamativo ni cita entre comillas atribuida al cliente.
6. **Sin cifras/fechas/promesas nuevas**: todo el contenido sale de `index.html`/`brief.md`
   previos. Promesas y vigencias idénticas en todas las páginas donde se repiten (ver
   verificación abajo).

### Estructura nueva (12 slides)

1. Apertura (fusiona 1+2: situación actual + objetivo general; los objetivos específicos
   salen del deck, quedan como material de kick-off)
2. Vista por fase · Fase 1 — Detección (participantes por cargo en 7 frentes, horas con
   kick-off, entrega)
3. Vista por fase · Fase 2 — Habilidades (horas con kick-off, arranca al validar el
   Informe Final, entrega)
4. Priorización — Matriz Impacto/Esfuerzo (4 cuadrantes) + Índice de Madurez como esquema
   (Cultura/Talento/Gobernanza, sin cifras)
5. Habilidades — 5 módulos reescritos como lo que construye cada responsable, etiquetados
   Construir/Probar/Adoptar
6. Entregables — 1 sola página, por fase, antes de la inversión (horas recuperables como
   estimación referencial, no resultado garantizado)
7. Garantía 30-60-90 — 30d uso de lo enseñado, 60d si replicó y construyó más, 90d retorno
   en tiempo e inversión con análisis de impacto
8. Casos — 2 referencias con sus datos reales + 1 línea para HJB (ya no un 3er card)
9. Inversión por fases — desglose por componente y horas dentro de cada fila de fase,
   casillas de monto vacías sin texto (sin cambios en el mecanismo AcroForm)
10. Por qué Intezia — condensado a 1 faceta por tarjeta, "sin horas extra" sin aludir a
    otro proveedor
11. Calendario — kick-off movido de lunes 12 a **martes 13 de octubre** (el 12 es feriado en
    Venezuela, Día de la Resistencia Indígena), resto de fechas igual, rotulado
    **"Calendario tentativo"** (a confirmar con HJB según sus feriados locales)
12. Cierre — sin cambios de contenido

### Terminología unificada en todo el documento

"Fase 1 / Fase 2" (no "Etapa") · "frentes" (no "clusters") · "logro inmediato" (no "quick
win") · "Habilidades directivas" · nombres de área según la nomenclatura de la antigua p.5
(Control de Gestión, Ventas, Desarrollo de Nuevos Negocios, Compras) — el Calendario (antigua
p.20) usaba nombres distintos (Contraloría, Comercial Farmer, Comercial Hunter, Compras
Materia Prima) y quedó corregido para que coincidan.

### Hallazgo técnico sin resolver — tipografías del AcroForm horneado

La instrucción pedía quitar "tipografías ajenas" de las antiguas p.14/17/20. Verificado
visualmente: el HTML/CSS del deck renderiza en Inter (vía Google Fonts, fallback de marca),
pero **todo el texto horneado en campos AcroForm** (Entregables, Acreditación, Notas,
PrecioFase, Paso01-03) se renderiza en **Helvetica** — así está construido
`scripts/acroform_appearance.py` (fuente base-14 de PDF, sin archivo de fuente para
embeber). No hay archivos de fuente (Graphit/Inter/Poppins) en el repo
(`find . -iname "*.ttf" -o -iname "*.otf" -o -iname "*.woff*"` → vacío), y la instrucción de
esta tarea prohibía buscar en internet — por lo que **no se pudo corregir** sin un archivo de
fuente real para embeber en el PDF. Esto es un problema **de sistema**, no solo de CAI-031:
afecta a todo deck con AcroForms. Pendiente de decisión: conseguir un archivo .ttf de Inter (o
Graphit) y extender `acroform_appearance.py` para embeberlo.

### Verificación antes de entregar

- **Horas y sesiones cuadran**: Fase 1 = 1+2+60+2 = 65h (18 sesiones) · Fase 2 =
  1+2+4+4+2+6+3 = 22h (13 sesiones). Total proyecto: 87h (sin cambios en las cifras, solo en
  cómo se presentan).
- **Ninguna fecha cae domingo** y cada fecha coincide con su día real (verificado con
  `date -j -f '%Y-%m-%d'` para las 19 fechas del calendario, incluida la nueva fecha de
  kick-off del 13 de octubre).
- **Cero nombres de HJB** en el documento (solo cargos).
- **Cero datos externos** (Microsoft & LinkedIn fuera).
- **Terminología única** (ver arriba).
- **Promesas idénticas**: "Si hacen falta horas adicionales para cumplir el objetivo de cada
  fase, no se cobran aparte." aparece textual en Notas (p.9) y en Por qué Intezia (p.10).
  "Cotización válida por 30 días" / "Descuento válido por 15 días" aparecen una sola vez,
  en p.9.
- **Caja rosada retirada** (antigua p.17): el badge de descuento urgente se recoloreó a
  naranja de marca, solo en `overrides.css` de este deck — la excepción roja/rosada de
  `_base/styles.css` es permanente y compartida por el resto del sistema, no se tocó.

### Tabla página original (21 slides) → acción → página nueva (12 slides)

| Original | Acción | Nueva |
|---|---|---|
| 1 · Portada | Fusionada con 2 | 1 · Apertura |
| 2 · Punto de dolor + Diagnóstico | Fusionada con 1, sin cita ni dolor inventado | 1 · Apertura |
| 3 · Objetivos estratégicos | Eliminada (objetivos específicos → material de kick-off) | — |
| 4 · Programa (resumen 5 módulos) | Fusionada en Vista por fase | 2-3 · Vista por fase |
| 5 · Las 15 áreas (organigrama, nombres) | Cargo-only, incorporada | 2 · Vista por fase · Fase 1 |
| 6 · Roadmap Detección (3 etapas + Mapa de Calor) | Horas→Vista por fase; Mapa de Calor→Priorización | 2 y 4 |
| 7 · La ruta completa (cascada) | Eliminada (fuera de alcance contratado) | — |
| 8 · Entregables Detección | Fusionada | 6 · Entregables |
| 9 · Tiempos detallados Etapa 1 | Fusionada (tabla de horas) | 2 · Vista por fase · Fase 1 |
| 10 · Punto de validación | Fusionada (nota de arranque) | 3 · Vista por fase · Fase 2 |
| 11 · Programa Habilidades | Reescrita como construcción (Construir/Probar/Adoptar) | 5 · Habilidades |
| 12 · Entregables Habilidades | Fusionada | 6 · Entregables |
| 13 · Tiempos detallados Etapa 2 | Fusionada (tabla de horas) | 3 · Vista por fase · Fase 2 |
| 14 · Beneficios (v3, 4 bloques) | Reducida a 2 tarjetas por fase | 6 · Entregables |
| 15 · Impacto (Microsoft & LinkedIn) | Eliminada (dato de terceros) | — |
| 16 · Métricas de otros clientes | 2 cards + 1 línea (antes 3 cards) | 8 · Casos |
| 17 · Inversión por fases | Desglosada por componente y horas; caja rosada→naranja | 9 · Inversión por fases |
| 18 · Seguimiento 30-60-90 | Reescrita (sin frase "Módulo I") | 7 · Garantía 30-60-90 |
| 19 · Por qué Intezia | Condensada (sin aludir a otro proveedor) | 10 · Por qué Intezia |
| 20 · Próximos pasos + Calendario | Kick-off movido, nomenclatura de áreas corregida | 11 · Calendario |
| 21 · Cierre | Sin cambios | 12 · Cierre |

## Corrección 2026-10-01 (b) — slide de dolor, texto heredado del clon sin adaptar

Al clonar `banco-activo-deteccion-negocios/` (DET-021), el `.s-pain .context` heredó la
estructura "[Empresa] ya [trabajó/invirtió] antes..." — cierta para Banco Activo (cliente
recurrente de Intezia), pero **falsa para HJB**: HJB nunca tuvo un proyecto de preparación
previo, solo activó 3 licencias sin criterio compartido ("respuesta corta: ignorancia",
Vianey Reyes). Corregido para reflejar la realidad (licencias activas sin criterio, no
inversión ya preparada) — ver memoria `[[combo-deteccion-habilidades-codigo-vs-servicio]]`.

También se retiraron 2 puntos del Diagnóstico que eran contexto de venta (comparación con
otros proveedores / Tec de Monterrey, mala experiencia con un proveedor anterior) tomados
casi textuales de la mesa de trabajo — no son hallazgos operativos de HJB, son argumentario
comercial (criterio ya documentado: una propuesta no se lee como objeciones respondidas). Se
reemplazó uno por un punto de diagnóstico real (riesgo de continuidad: el criterio de uso
vive solo en la cabeza de cada responsable), grounded en el punto 7 del contexto del cliente
(por qué les atrae el Cerebro Digital). `meta.json` pasa a `En corrección` (ya estaba
documentado como pendiente en la reconstrucción de abajo).

## Reconstrucción 2026-10-01 — cambio de estructura completo

Instrucción directa del usuario, tras una mesa de trabajo real con Vianey Reyes (Human
Capital / Desarrollo Organizacional) y el envío del organigrama de las 15 áreas. Reemplaza
por completo la versión anterior (2 poblaciones de Habilidades, Gerencial + Especializada).
**La versión anterior queda descartada** — HJB no compra 2 poblaciones de un mismo
currículo, compra Detección completa de las 15 áreas y, después, Habilidades para los 15
tomadores de decisión con efecto cascada (modelo Venemergencia).

## Datos administrativos

- **Empresa**: HJB Química — distribuidora mexicana de materias primas químicas, ~110
  personas, 15 áreas funcionales, con carga financiera fuerte (compras indirectas, compras
  de materia prima, precios, tesorería, comercio exterior).
- **Slug**: `hjb-quimica` (se mantiene, es revisión de la misma propuesta)
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — **reclasificado** desde `habilidades` (versión
  anterior). Es un combo Detección + Habilidades cotizadas en el mismo documento, y por
  regla del sistema el campo `servicio` de `meta.json` sigue la taxonomía del combo, no el
  prefijo del código (ver memoria `combo-deteccion-habilidades-codigo-vs-servicio` y el
  precedente directo `banco-activo-deteccion-negocios/` DET-021). El código se mantiene
  **CAI-031** porque así lo asignó originalmente el propio cliente/usuario — código y
  servicio son decisiones independientes.
- **Tipo de documento**: Detección multi-área (15 áreas) + Habilidades In-Company
  combinadas, estructura calcada de `banco-activo-deteccion-negocios/` (DET-021), que a su
  vez extiende `la-tienda-del-blumer/` (DET-020).
- **Estado**: `meta.json` pasa de `Enviada` a `En corrección` (propuesta ya enviada antes,
  ahora en revisión mayor por pedido del cliente).
- **Fuente**: mesa de trabajo con Vianey Reyes (contexto extenso dado por el usuario,
  2026-10-01) + organigrama de las 15 áreas (captura de correo de Vianey, confirmado) +
  brief original del cliente (`hjbqumica.pdf`, ya no vigente como estructura, solo como
  antecedente de qué herramientas tienen licenciadas).

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414-0570056 · miribarren@intezia.com.
- **Contacto cliente / patrocinadora**: Vianey Reyes · Coordinadora Desarrollo
  Organizacional · vianey.reyes@hjb.com.mx.
- **Sponsor ejecutivo**: Jorge Molina, Director General — caso insignia del cierre con
  Cerebro Digital en la Etapa 2.

## Contexto del cliente (mesa de trabajo, 2026-10-01)

1. **110 personas, 15 áreas**, carga financiera pesada (compras indirectas, compras de
   materia prima, precios, tesorería, comercio exterior).
2. **Todo aprendido solo, sin estandarización**: ni plantillas, ni seguridad, ni
   privacidad, ni criterio de uso. Cada quien usa la IA "como le parece".
3. **3 herramientas licenciadas que se solapan** (ChatGPT y Claude para gerencia este año,
   Copilot es el Microsoft 365 estándar) y **ni ellos saben bien por qué**. Cita textual de
   Vianey sobre por qué tienen ecosistemas tan parecidos: *"respuesta corta: ignorancia"*.
   Cada usuario elige la que le resulta más cómoda, sin saber cuál rinde de verdad. Les
   recomendamos evaluar consolidar y les hizo sentido — **la recomendación de licencias es
   un entregable explícito de la Detección**.
4. **Comparando 3 proveedores**, entre ellos el **Tec de Monterrey** — hay que competir en
   grande, no como "un curso más" (ver Reglas de copy abajo, posicionamiento).
5. **Compran resultados, no metodología.** Vianey se definió como "materialista": necesita
   entregables tangibles y visuales que pueda mostrar adentro, y un retorno simple en
   números. Invertir no les preocupa si ven que invierten bien.
6. **Mala experiencia previa**: un proveedor anterior prometió mucho, se trabó en la
   implementación y cobró horas extra. **Por eso la cláusula "sin horas extra" es explícita
   en la cotización de este documento** (ver Inversión por fases).
7. **El Cerebro Digital les encantó.** Vianey lo quiere para conectar las áreas en
   decisiones estratégicas y dar continuidad cuando alguien se ausenta (vacaciones,
   permisos, salida). Es el **gran cierre y principal diferenciador frente al Tec**.

## Estructura nueva — una propuesta, dos etapas (ambas cotizadas)

### Etapa 1 · Detección organizacional — 15 áreas

Auditar la operación real de las 15 áreas y entregar un plan de acción con datos para que
HJB decida dónde y cómo invertir en IA.

**Las 15 áreas (organigrama de Vianey, nombre y responsable reflejados 1:1 en el informe
final — bloqueante, pedido explícito del cliente):**

| # | Área | Responsable | Puesto |
|---|---|---|---|
| 1 | Dirección General | Jorge Molina | Director General |
| 2 | Auditoría | Guadalupe Bolaños | Gerente Auditoría |
| 3 | Contraloría (Control de Gestión) | Alberto Zuñiga | Gerente de Control de Gestión |
| 4 | Comercial Farmer (Ventas) | Cecilia Gutierrez | Gerente Ventas |
| 5 | Comercial Hunter (Desarrollo de Nuevos Negocios) | Diego Martínez Prieto | Gerente Desarrollo de Nuevos Negocios |
| 6 | Compras de Materia Prima | Francisco Maldonado | Gerente Compras |
| 7 | Almacén | Liliana Herrera | Gerente Almacén |
| 8 | Transportes | Irving Gonzalez | Gerente Transportes |
| 9 | Capital Humano | Lorena Sánchez | Gerente Capital Humano |
| 10 | Proyectos | Keren Romero | Gerente de Proyectos |
| 11 | Precios | Sandra Samperio | Gerente Precios |
| 12 | Tesorería | Nancy Cortes | Gerente de Tesorería |
| 13 | Comercio Exterior | José Martín García | Gerente Comercio Exterior |
| 14 | Planeación | Erika Clemente | Gerente Planeación |
| 15 | Desarrollo Organizacional | Vianey Reyes | Coordinador Desarrollo Organizacional |

**Agrupamiento para las sesiones de levantamiento** (decisión de Intezia, pedida
explícitamente por el cliente — "evalúen ustedes si conviene agrupar... ustedes son
quienes mejor saben cómo armarlo"): se agrupan en **7 clusters por proceso compartido**
para la narrativa y agenda del proyecto, pero **cada área mantiene su sesión íntegra de 4h**
(no se reduce profundidad por agrupar, solo se optimiza logística agendando áreas
relacionadas en días consecutivos):

| Cluster | Áreas (horas) |
|---|---|
| A · Dirección | Dirección General (4h) |
| B · Control y Cumplimiento | Auditoría (4h) + Contraloría (4h) = 8h |
| C · Comercial | Comercial Farmer (4h) + Comercial Hunter (4h) = 8h |
| D · Cadena de Suministro | Compras de Materia Prima (4h) + Almacén (4h) + Transportes (4h) = 12h |
| E · Finanzas y Comercio Exterior | Precios (4h) + Tesorería (4h) + Comercio Exterior (4h) = 12h |
| F · Capital Humano y Desarrollo Organizacional | Capital Humano (4h) + Desarrollo Organizacional (4h) = 8h |
| G · Proyectos y Planeación | Proyectos (4h) + Planeación (4h) = 8h |

**Qué incluye (requisitos explícitos del cliente):**
- Levantamiento de las 15 áreas, 1 sesión de 4h por área (política estándar de Detección,
  `empresa/politicas-comerciales.md`).
- Recomendación del ecosistema de licencias: qué herramientas conservar (de ChatGPT, Claude
  y Copilot), cuántas licencias y para quién, con criterio operativo.
- Quick wins durante las mismas sesiones de auditoría, modelo DUSA (expediente CAP-088:
  cada equipo construye su propio asistente mientras se audita, no al final).
- Fundamentals de IA para nivelar a todos desde el inicio (sesión grupal, antes de las 15
  sesiones de área, máx. 25 personas por `empresa/politicas-comerciales.md` — con 110
  personas totales en la organización, pero el grupo de levantamiento real son los 15
  responsables de área, bajo el máximo).

**Dimensionamiento (regla `empresa/politicas-comerciales.md` → Detección: 4h/área + 2h
Fundamentals grupal):** 15 áreas × 4h = 60h + 2h Fundamentals = **62h de sesiones de
servicio**. Sumando kick-off (1h) y presentación del Informe Final (2h), el total de
tiempo de la Etapa 1 es **65h** (ver tabla de Tiempos detallados en `index.html`).

### Etapa 2 · Habilidades para directivos, efecto cascada (modelo Venemergencia)

Los 15 tomadores de decisión (los mismos 15 responsables auditados en la Etapa 1) instalan
el criterio, recuperan horas y siguen definiendo la estrategia con IA, para después
llevarla en cascada al resto de la organización.

**5 módulos (dimensionado por diseño curricular estándar,
`plantillas/diseno-taller-capacitacion.md` — no es Habilidades de "área con procesos
discretos", es un programa de cohorte cruzado para el mismo grupo directivo, mismo criterio
de dimensionamiento ya documentado en la versión anterior de este deck):**

| Módulo | Contenido | Sesiones | Horas |
|---|---|---|---|
| I | Fundamentos de IA y criterio de herramientas (las que recomiende conservar la Detección) | 1 | 2h |
| II | Prompting y decisiones con criterio, riesgos y verificación humana | 2 | 4h |
| III | Reportes y tableros con IA, casos reales de cada área | 2 | 4h |
| IV | Privacidad y gobierno de datos, con manual de uso para la organización | 1 | 2h |
| V | Cierre · Cerebro Digital de Claude (cada directivo construye el suyo, Director General como caso insignia) | 3 | 6h |

Total: **9 sesiones, 18h**. El Módulo V recibe el mayor peso (6h, 3 sesiones) porque es el
diferenciador frente al Tec de Monterrey y el cliente lo pidió como "gran cierre" — no se
trata como un quick add-on.

**Efecto cascada**: se menciona como siguiente paso natural hacia los puestos
especializados de cada área, **sin cotizar y sin fechas** — se define con los resultados
de la Detección y de la Etapa 2 (mismo criterio ya usado en DET-021 para "Expansión de
Habilidades", `.vision-step-future`).

**Dimensionamiento total Etapa 2**: kick-off propio (post-validación, 1h) + 18h de sesiones
+ 3h de garantía 30-60-90 (1h por check-in) = **22h**.

**Total del proyecto completo: 65h (Etapa 1) + 22h (Etapa 2) = 87h.**

## Punto de validación entre etapas

El Informe Final de la Detección (hallazgos + Índice de Madurez + recomendación de
licencias) es la decisión natural para avanzar a la Etapa 2, con resultados medibles — no
una aprobación a ciegas. Se representa como slide propia entre el bloque de Detección y el
de Habilidades.

## Calendario (actualizado 2026-10-01 — corrido +1 semana completa)

El lunes 5 de octubre ya no es el kick-off: ese día hay mesa de trabajo interna. Instrucción
directa del usuario: correr todo el calendario +1 semana completa.

- **Kick-off**: lunes **12 de octubre**, 10:00-11:00 (1h).
- **Fundamentals grupal** (15 responsables de área): jueves 15 de octubre, 10:00-12:00 (2h).
- **15 sesiones de levantamiento** (4h cada una, 1 por área, martes y jueves 10:00-14:00),
  agendadas por cluster para optimizar logística:

  | Fecha | Área (cluster) |
  |---|---|
  | Mar 20 oct | Dirección General (A) |
  | Jue 22 oct | Auditoría (B) |
  | Mar 27 oct | Contraloría (B) |
  | Jue 29 oct | Comercial Farmer (C) |
  | Mar 3 nov | Comercial Hunter (C) |
  | Jue 5 nov | Compras de Materia Prima (D) |
  | Mar 10 nov | Almacén (D) |
  | Jue 12 nov | Transportes (D) |
  | Mar 17 nov | Precios (E) |
  | Jue 19 nov | Tesorería (E) |
  | Mar 24 nov | Comercio Exterior (E) |
  | Jue 26 nov | Capital Humano (F) |
  | Mar 1 dic | Proyectos (G) |
  | Jue 3 dic | Planeación (G) |
  | Mar 8 dic | Desarrollo Organizacional (F) |

- **Presentación del Informe Final**: jueves 10 de diciembre, 10:00-12:00 (2h).
- **Etapa 2**: sin fecha fija — arranca una vez validado el informe con HJB (kick-off propio
  + 9 sesiones + garantía 30-60-90, sin calendario todavía, mismo criterio de "omitir, no
  inventar placeholder").

**Calendario de 3 columnas** (18 filas: kick-off + Fundamentals + 15 sesiones +
presentación, por encima del máximo de 9 filas en 2 columnas — ver memoria
`calendario-inicio-comprimir-filas-muchas-sesiones` y el precedente de DET-021 con 15
filas/3 columnas).

## Modalidad

**Virtual por Teams**, con grabaciones disponibles para quien no pueda asistir a una
sesión (requisito explícito del cliente) — para ambas etapas.

## Pendiente de confirmar antes de enviar

1. **Consultor que facilita**: el cliente quiere conocerlo y ver su CV antes de decidir,
   idealmente en la mesa de trabajo del lunes 12 de octubre. El usuario confirmó
   (2026-10-01) que el CV lo adjunta aparte por correo (no en esta conversación) —
   **esta versión del deck sigue sin exponer un consultor con nombre** (slide "Por qué
   Intezia" institucional, Equipo INTEZIA, sin CV ni nombre propio, mismo criterio de
   "omitir, no inventar placeholder"). Actualizar en cuanto se confirme quién lo va a
   facilitar.

## Modelo visual del informe de DUSA — recibido 2026-10-01

El usuario compartió `Resumen_Informe_Final_Auditoria_IA_DUSA.pdf` (resumen ejecutivo de 1
página del Informe Final de Detección real de DUSA, "Framework IADD", 5 áreas auditadas).
**Usado anonimizado**, tal como pidió el usuario ("sin el nombre del cliente"):

- **Slide "Métricas de otros clientes"** (`index.html`): la tarjeta de Detección ya no dice
  "DUSA" — dice "Otro cliente de distribución", con cifras reales y citables tomadas del
  resumen: 5 áreas auditadas, 33 procesos clasificados, 3 agentes ya construidos antes del
  informe final (logros inmediatos durante la propia auditoría, no al cierre).
- **Validación de la estructura de Entregables de la Detección** (slide 8): el resumen de
  DUSA confirma que la estructura ya diseñada para HJB (mapa de procesos, Índice de
  Madurez, focos de mayor impacto, hoja de ruta por área, horas recuperables, recomendación
  de licencias) coincide con el formato real de un Informe Final de Detección de Intezia —
  no se necesitó rediseñar nada, solo se enriqueció la descripción del Índice de Madurez
  con sus 3 dimensiones reales (cultura, talento, gobernanza), confirmadas por este
  documento.
- **No usado**: cifras específicas de DUSA que identifican al cliente o revelan datos
  operativos confidenciales (headcount, USD/mes, número exacto de facturas/movimientos
  bancarios, nombre de sus áreas) — eso se queda fuera del deck de HJB por respeto a la
  confidencialidad de DUSA, más allá de lo que pidió el usuario.

## Métricas de otros clientes (citables, §4.9)

- **Venemergencia** (modelo cascada, CAP-047): Encuesta Edu-Trace de Fase 1 (22 personas):
  **91% percibió algún ahorro semanal** (20 de 22), **Índice de Impacto Edu-Trace 90/100**.
  Fuente: `clientes/banco-casos-de-exito/index.html`, caso Venemergencia. Cifras
  autopercibidas de cierre, no medición longitudinal — se citan como tal (§4.17 aplicado por
  analogía).
- **DUSA** (modelo de Detección, CAP-088): citado solo de forma cualitativa (auditoría con
  mapa de calor de oportunidades + asistentes propios construidos durante la misma sesión
  de auditoría, sin cifras — no tiene Edu-Trace de cierre). Pendiente de actualizar si el
  usuario comparte el archivo del informe real.

## Entregables

**Etapa 1 · Detección:**
- Informe final con mapa de procesos de las 15 áreas.
- Índice de madurez (por área y consolidado).
- Focos de mayor impacto (priorización).
- Hoja de ruta por área.
- Horas recuperables (estimado).
- Recomendación de licencias (qué conservar entre ChatGPT, Claude y Copilot, cuántas y
  para quién).

**Etapa 2 · Habilidades:**
- Criterio de uso documentado (de las herramientas que recomiende conservar la Detección).
- El reporte o tablero que construye cada directivo.
- Su asistente propio.
- Manual de gobierno de datos.
- Su Cerebro Digital funcionando.
- Certificado de participación INTEZIA.

## Decisiones de diseño y transparencia (judgment calls, confirmar si no aplica)

1. **Agrupamiento en 7 clusters**: decisión de Intezia pedida explícitamente por el
   cliente — ver tabla arriba. No reduce horas por área (sigue siendo 4h/área íntegras),
   solo agenda sesiones relacionadas en días consecutivos.
2. **18h / 5 módulos / 9 sesiones para la Etapa 2**: dimensionamiento razonado (no regla
   mecánica — esto no es Habilidades de área con procesos discretos, es un programa de
   cohorte directiva), con el Módulo V (Cerebro Digital) sobreponderado a propósito por ser
   el diferenciador pedido por el cliente.
3. **Sin horas extra facturadas**: cláusula explícita en Notas/ROI de la Inversión por
   fases — si hacen falta horas adicionales para cumplir el objetivo de cada etapa, no se
   cobran aparte (pedido explícito del cliente, por la mala experiencia previa).
4. **Garantía 30-60-90 solo en Etapa 2**: por regla del sistema
   (`empresa/tipos-de-documento.md §0.2`, aplica solo a Habilidades) — la Etapa 1
   (Detección pura) no lleva ese sello en su propia fila de la Inversión por fases.
5. **Referencias del sector (Empresas Polar, GoPharma, Nestlé)**: se retiran de esta
   versión — la slide "Por qué Intezia" se reduce a institucional (sin consultor con
   nombre) mientras el usuario confirma el adjunto del CV; se puede reincorporar junto con
   el consultor cuando llegue ese dato.
