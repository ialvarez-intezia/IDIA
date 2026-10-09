# Plantilla: Propuesta compacta de Detección (9 slides, dirigida por datos)

> **Estado: estándar del servicio de Detección** (`CLAUDE.md` §4.22) desde el 2026-10-08. Toda propuesta nueva de Detección se hace con esta plantilla, sin clonar un deck.
> **Origen**: correcciones de Keiber Quintana (CPO) a G-MAX DET-024 en la reunión del 2026-10-08 con David Prato y María Iribarren. Caso base: `clientes/propuestas/g-max/` (`datos.ejemplo-deteccion.json` es su `datos.json` en la versión estándar; la propuesta enviada a G-MAX además omite la facilidad de pago y regala los fundamentos de IA, decisiones solo de ese cliente).
> **Cómo se usa**: un `datos.json` con `"version": 3` y `"formato": "deteccion"`, y el mismo generador de Habilidades (`scripts/generar-habilidades-compacto.py`). Las slides 1, 4 y 6 a 9 son las de Habilidades; las 2, 3 y 5 son propias de Detección. Lo que no es del cliente sale de los valores por defecto del servicio (§5).
> **Reglas comunes** con Habilidades (orden por las preguntas del cliente, lenguaje del cliente, sin semanas ni sesiones, retorno sin estudios, próximos pasos con la asesora): `plantillas/habilidades-compacto.md` §2 y §6, y `CLAUDE.md` §4.23.

---

## 1. Cuándo usarla

| Situación | Usar |
|---|---|
| Propuesta nueva del servicio de Detección (cualquier cliente y división) | **Esta plantilla**, sin preguntar el formato |
| Ajustar, corregir o rehacer una Detección ya entregada (canónica o compacta v1/v2) | Esta plantilla: se arma su `datos.json` desde la transcripción y la ficha (no desde el deck anterior) y el deck previo se archiva en `_anterior-N-slides/` |
| Combo Detección + Habilidades cotizado junto (p. ej. DET-002) | Formato de Habilidades con `servicio_rotulo` (como hasta ahora), sin semanas ni sesiones. **Pendiente de decisión**: si la parte de Habilidades aún no tiene soluciones conocidas, preguntar al usuario si va en este formato |
| Plan integral de 4 servicios, Políticas, Innovación | Los de su servicio (`CLAUDE.md` §4.1a/§4.1b) |

## 2. Reglas de Keiber (bloqueantes)

En una Detección **no se sabe todavía qué se hará en cada área**: los números que en Habilidades salen del informe de Detección (soluciones, horas por área, semanas) aquí no existen y, si se inventan, confunden al cliente y a Ventas. Keiber: «que lo entienda alguien que no seamos tú ni yo ni Ivana».

| Regla | Qué hace la plantilla |
|---|---|
| **No hay frentes ni áreas prioritarias** antes de detectar, ni un «resto corporativo» que agrupe el grueso de las áreas | El alcance muestra las áreas **como las nombra el cliente** y sus departamentos. Lo que el cliente señaló como interés guía la conversación del arranque (va en `supuestos`), no la estructura. El generador bloquea «frente/área prioritaria» y «resto corporativo» |
| **Cada departamento por separado** (líder y su mano derecha), nunca varios en la misma mesa | «Un espacio por departamento» en «Cómo trabajamos» |
| **Horas en global**, sin reparto por área: logística las reparte según lo que necesite cada departamento | Solo se muestran las horas de levantamiento (`deteccion.horas.levantamiento`), en la etapa de levantamiento y en la inversión. Arranque y nivelación son horas internas (`programa.md`) |
| **Ni semanas ni sesiones**: se cuadran en el kickoff | Ruta por etapas, sin semanas; sin grupos de nivelación ni número de sesiones. El generador bloquea «semana» y «sesión» (`CLAUDE.md` §4.23) |
| **Logro inmediato: al menos N en el proyecto**, no uno por área (un proceso de mucho esfuerzo pasa al mapa) | `deteccion.logros_minimos` (por defecto 3) en la tarjeta de logros, la inversión y «Cómo trabajamos» |
| **Entregables sin conteos** («7 entregables») y sin volver a nombrar las áreas: una página de lo que recibe | Slide 5 con tarjetas nombradas: alcance y calendario, equipo nivelado, logros inmediatos, Mapa de Calor, Informe Final y hoja de ruta, inversión inteligente en licencias. El generador bloquea «N entregables» |
| **Alcance = auditar y dejar logros** (lo global) y ahí van las áreas | Slide 2: «Auditamos cada área y dejamos logros inmediatos.», qué auditamos y para qué |
| **Sin tarea previa** para los líderes antes de su turno | «Sin tarea previa» en «Cómo trabajamos» |
| **Fuente: transcripción de la reunión con el cliente** (y la ficha), no el resumen de la asesora | `origen` y `fuente_insumo` dicen de dónde sale; si la ficha y la transcripción se contradicen, manda la transcripción (`CLAUDE.md` §4.23) |

Se mantienen las reglas de Detección anteriores: sin certificado, sin garantía 30-60-90 (es de Habilidades), sin pre-recomendar una herramienta de IA (la recomienda el Informe Final), sin dolor dramatizado ni citas, y sin Metodología ABR ni Equipo facilitador (§4.10a).

## 3. Las 9 slides

| # | Clase | El cliente se pregunta | Contenido |
|---|---|---|---|
| 1 | `.s-cover` | ¿Cuál es mi problema? | Titular-objetivo + lead + 2 a 4 dolores reales de la reunión (sin `resuelto_por`) + fuente |
| 2 | `.s-scope.s-det-scope` | ¿Qué van a hacer y para qué? | «Qué auditamos»: áreas del cliente + departamentos (píldoras) + foco; «Para qué» (4 objetivos); fuera de alcance |
| 3 | `.s-route.s-det-route` | ¿Cómo? | 4 a 6 etapas en línea (por defecto Arranque, Nivelación, Levantamiento con las horas, Priorización, Informe Final); la ruta completa (Ahora Detección, Después Habilidades, Más adelante Políticas) |
| 4 | `.s-method` | ¿Cómo funciona en la práctica? | Entrevistamos, Mapeamos, Construimos, Priorizamos; por qué en ese orden; quién construye; sin tarea previa, un espacio por departamento, sin forzar soluciones; cuidado de los datos; logística |
| 5 | `.s-deliv.s-det-deliv` | ¿Con qué me quedo? | 3 a 6 tarjetas nombradas con su momento («Al arrancar», «En el levantamiento», «Al cierre») + las 2 cajas editables (Entregables y Acreditacion) |
| 6 | `.s-roi` | ¿Qué gano? | Modo método: cómo se estima el retorno de cada oportunidad; qué decide el cliente con el Informe Final (licencias, prioridades, control); hacia dónde va; sin estudios ni web |
| 7 | `.s-price` | ¿Cuánto cuesta? | «Inversión del proyecto», sin garantía 30-60-90; campos vacíos para ventas |
| 8 | `.s-pay` | ¿Cómo se paga? | Por defecto 2 cuotas: 50 % al aprobar y 50 % con el Informe Final (montos vacíos) |
| 9 | `.s-next` | ¿Qué sigue y a quién escribo? | Fecha de arranque, lista de responsables, reunión de arranque; la asesora comercial |

Fundación omite las slides 7 y 8 (7 slides).

## 4. Flujo

**Pre-requisitos (bloqueantes, `CLAUDE.md` §4.1, §4.1a, §4.23):** división, servicio = `deteccion` y alianza confirmados con el usuario; código `DET-0NN` libre; **transcripción de la reunión con el cliente** y Ficha de Levantamiento (si existe); lista de personal si la hay; la asesora comercial.

1. **Entrevista mínima** (una sola vez, todas las preguntas juntas; lo que no se responda va a `supuestos`): áreas como las nombra el cliente y sus departamentos; horas de levantamiento en global (y las internas de arranque y nivelación); logros inmediatos mínimos (por defecto 3); modalidad; asesora; si el pago sigue el estándar 50/50.
2. **`datos.json`**: copiar `plantillas/habilidades-compacto-canonico/datos.plantilla-deteccion.json` (o partir de `datos.ejemplo-deteccion.json`) a `clientes/propuestas/<slug>/datos.json` y completar los `POR_DEFINIR`. Solo se escribe lo del cliente; para cambiar un valor por defecto se define la clave completa (las listas no se mezclan).
3. **Generar:** `python3 scripts/generar-habilidades-compacto.py <slug>`. Leer los ⚠ uno por uno (plan de pago estándar, pasos del retorno o datos por defecto, facturación).
4. **Medir:** `node scripts/verificar-habilidades-compacto.js <slug>` (incluye las medidas de las slides de Detección) y `node scripts/verificar-overflow.js <slug>`.
5. **PDF:** `bash scripts/pdf-habilidades-compacto.sh <slug>` (genera, verifica, PDF y el par de campos). Requiere `pypdf`.
6. **Revisión visual** de cada página del PDF (§4.10), incluido el texto horneado de las cajas de la slide 5.
7. **Estado:** el wrapper deja `meta.json` en «Enviada». Si la propuesta todavía pasa por revisión (p. ej. Keiber pidió verla antes de enviarla), corregirlo a mano a «En corrección» y correr `python3 scripts/indexar.py`.

## 5. Esquema de `datos.json`

Raíz: `"version": 3`, `"formato": "deteccion"`, `cliente`, `division`, `alianza`, `eje`, `origen`, `fuente_insumo`, `portada`, `deteccion`, `logistica.modalidad`, `proximos_pasos.asesora`, `siglas_ok`, `frases_ok`, `supuestos`, `pendientes`. No lleva `carriles`, `areas`, `fases` ni `frentes` (se ignoran con un aviso).

| Clave | Qué es | Por defecto |
|---|---|---|
| `deteccion.areas[]` | 1 a 8 áreas, con el nombre que les da el cliente (≤ ~30 caracteres) | Obligatorio |
| `deteccion.departamentos[]` | Departamentos de la lista de personal, en píldoras (≤ 24; ≤ ~30 caracteres cada uno). No se asignan a cada área si no hay organigrama desglosado | Opcional |
| `deteccion.foco` | Dónde se concentra el levantamiento (≤ ~190 caracteres) | Opcional |
| `deteccion.horas` | `{levantamiento, arranque, nivelacion}` en horas enteras. Solo `levantamiento` se muestra (en global) | `levantamiento` obligatorio; los otros, 0 |
| `deteccion.texto_horas` | Frase de las horas en la etapa de levantamiento | «**{h_levantamiento} horas** de levantamiento, repartidas según lo que necesite cada departamento.» |
| `deteccion.logros_minimos` | Logros inmediatos que asegura el proyecto | 3 |
| `deteccion.para_que[]` | 3 o 4 objetivos `{titulo, texto}` | Ver la operación real · Mejorar desde ya · Invertir con criterio · Cuidar la información |
| `deteccion.etapas[]` | 4 a 6 `{titulo, texto, horas}`; exactamente una con `"horas": true` | Arranque · Nivelación · Levantamiento (horas) · Priorización · Informe Final |
| `deteccion.ruta_completa[]` | 0 a 3 `{cuando, servicio, texto}` | Ahora Detección · Después Habilidades · Más adelante Políticas |
| `deteccion.entregables[]` | 3 a 6 `{cuando, titulo, texto, color?}` (`color`: amarillo, naranja o blanco; por defecto según el momento) | Alcance y calendario · Equipo nivelado en IA · Logros inmediatos · Mapa de Calor · Informe Final y hoja de ruta · Inversión inteligente en licencias |
| `deteccion.etiqueta_*` | `etiqueta_que`, `etiqueta_para_que`, `etiqueta_departamentos`, `etiqueta_ruta_completa` | «Qué auditamos», «Para qué», «Con sus departamentos», «La ruta completa de {cliente_corto}» |
| `alcance` | `titulo`, `subtitulo`, `fuera_alcance[]`, `etiqueta_fuera` | «Auditamos cada área y dejamos logros inmediatos.» y 3 puntos fuera de alcance (licencias, cambios en sistemas, desarrollos a la medida) |
| `ruta` | `titulo`, `subtitulo` | «Del arranque al Informe Final, en {n_etapas_palabra} etapas.» |
| `metodo` | Igual que en Habilidades | Pasos, por qué en ese orden, quién construye, las 3 prácticas de Keiber y el cuidado de los datos |
| `logistica` | `modalidad` (obligatoria), `participantes`, `ritmo`, `arranque` | Participantes, ritmo y arranque genéricos |
| `entregables` | `titulo`, `subtitulo` (con «Lo que se llevan»), `transversales[]`, `valor_inmediato[]` (cajas editables) | Ficha de levantamiento de cada departamento; presentación del Informe Final · mejoras en uso antes del cierre; datos para decidir licencias |
| `retorno` | Igual que en Habilidades (modo método o cifras con `deteccion.areas` como nombres) | Pasos, metas (Licencias, Prioridades, Control), destino y gancho de Detección |
| `inversion` | `duracion`, `programa[]`, `notas[]` (sin garantía) | Arranque, nivelación y {h_levantamiento} horas de levantamiento |
| `pago.cuotas[]` | Igual que en Habilidades | 50 % al aprobar · 50 % con el Informe Final |
| `proximos_pasos` | `asesora` (obligatoria) y `pasos[3]` | Fecha de arranque · Lista de responsables · Reunión de arranque |

**Tokens** de Detección: `{cliente} {cliente_corto} {codigo} {h_levantamiento} {h_arranque} {h_nivelacion} {h_total} {logros_minimos} {logros_minimos_palabra} {n_areas} {n_areas_palabra} {n_areas_txt} {areas_las} {n_etapas} {n_etapas_palabra} {n_cuotas} {n_cuotas_palabra}`. No existen `{n_total}`, `{h_f1}` ni los de semanas.

## 6. Qué valida el generador (además de lo común de Habilidades)

**Bloquea (✗):** `deteccion` ausente; áreas fuera de 1 a 8 o repetidas; horas de levantamiento ausentes o fuera de 1 a 400; logros mínimos fuera de 1 a 10; etapas fuera de 4 a 6 o sin exactamente una con `horas`; entregables fuera de 3 a 6; más de 24 departamentos o que ocupen más de 6 filas; «frente/área prioritaria», «resto corporativo» y «N entregables» en cualquier slide; «semana» y «sesión» (`CLAUDE.md` §4.23).
**Avisa (⚠):** valores por defecto que conviene personalizar (pasos del retorno, cuidado de los datos, plan de pago); textos largos por caja; ningún entregable que nombre los logros inmediatos; `resuelto_por`, `carriles`, `areas`, `fases`, `frentes`, `hitos` o `siguiente_etapa` presentes (se ignoran).

## 7. Campos del PDF

Los mismos 7 + N de Habilidades (`plantillas/habilidades-compacto.md` §7): `PrecioBase`, `Descuento`, `PrecioTotal`, `Programa`, `Notas`, `PagoCuota1..N` y las dos cajas de la slide 5 (`Entregables`, `Acreditacion`). La franja inferior de la slide 5 y sus cajas están en la misma posición que en Habilidades, así que `customize-habilidades-compacto.py` sirve igual. Fundación: solo las 2 cajas.

## 8. Límites

| Límite | Salida |
|---|---|
| Más de 8 áreas o más de 24 departamentos | Agrupar sububicaciones bajo su departamento; si el cliente tiene más áreas, nombrar las grandes |
| Una sola área | Una tarjeta ancha |
| Más de 6 etapas | Fusionar (p. ej. Priorización e Informe Final) |
| Cotización por fases o por permanencia | No soportada |

## 9. Historial

- **v3.0 (2026-10-08)**: primera versión, desde G-MAX DET-024 (armado a mano ese mismo día con las correcciones de Keiber y luego reproducido por el generador con el mismo texto en las 9 slides).
