# Brief · Conserval (Balance) · Servicio de Detección (DET-026)

## Actualización 2026-10-08 · migrada a la plantilla v2 (8 slides) · VIGENTE

Instrucción directa del usuario: «ajustar la DET-026 al formato nuevo». «Formato nuevo» = **plantilla compacta v2.0**
(commit `93e0b67`, 2026-10-07): el `datos.json` v1.4 se migró según la spec §13 y se regeneró con
`--actualizar-css --forzar-overrides`. Orden del deck: Portada · Alcance · Ruta · Cómo trabajamos · Entregables ·
Retorno · Inversión · Próximos pasos. El deck de 6 slides v1.4 y su PDF quedan en `_pdf-anteriores/`. Sin cambios de
contenido de fondo: 14 h, 4 entregables, 3 áreas más Fundamentals, 4 semanas, modalidad mixta, kick-off aparte.

### Decisiones del usuario al preguntar

- **Sin «Facilidad de pago»** (igual que la CAI-032, la DET-024 y la CAI-040): `omitir: ["pago"]`; ventas comunica el
  plan de pago por otro medio.
- **Fundamentals:** «el equipo, sin cifra». El deck sigue sin decir si asisten las 2 o 3 personas de condominio o las 8
  de la empresa; sigue pendiente de confirmar con la asesora.
- **Datos:** «solo procesos, sin datos» (mismo criterio que G-MAX): las sesiones levantan procesos y no cargan a
  ninguna herramienta de IA información que identifique a condóminos, clientes o personal. Por eso el logro de
  Atención al cliente se prueba con **ejemplos armados para la sesión** y ya no con «capturas de ejemplo» a secas
  (la nota del análisis de Gemini más abajo quedó en la versión anterior; vale esta decisión).

### Qué cambió respecto de la v1.4 (en el lenguaje de la v2)

| v1.4 | v2 |
|---|---|
| `alcance.pasos` y `quien_construye` | `metodo` (4 pasos propios de Detección: entrevistamos, identificamos, construimos, dejamos listo) |
| (sin método, logística ni asesora) | `metodo.practica` (sesiones de 2 h, con lo que ya usan, una persona confirma), `metodo.datos`, `por_que_orden`, `logistica` y `proximos_pasos.asesora` |
| (sin «para qué» por área) | `areas[].para_que` en Fundamentals y en cada área, con las palabras del cliente |
| `frentes[].etiqueta`, `areas_html`, «S1-S4», «S = semana» | `frentes[].nombre` = «Auditoría de las 3 áreas», «1 a 4» y nota sin códigos |
| Fases «Nivelación», «Pagos y atención», «Cierre del mapa» | «Nivel», «Pagos», «Mapa» (cabeceras de ≤ 6 caracteres: con «2 entregables» al lado no cabían más largas) |
| Inversión «por horas de sesión», Duración con las horas al frente | «Inversión del proyecto»; «Proyecto de 7 sesiones en 4 semanas, en modalidad mixta. 14 horas de trabajo.» |
| Sin asesora ni contacto | Slide 8 con Verónica Rubio (teléfono y correo de la Ficha; el cargo «Asesora comercial» sale de este brief) |

La slide 3 conserva la 5.ª columna «Cierre» (Priorizar · Reportar · Proyectar), sin garantía 30-60-90. El retorno
(modo método, «decidir con datos») no cambió. `overrides.css` nuevo: escala de las slides 2, 3, 4 y 5.

### Pendientes (a confirmar antes de reenviar)

- Inversión, descuento y total (campos vacíos para ventas; el cliente es sensible al precio por área) y cómo se
  comunica el plan de pago (no hay slide).
- Fechas, horarios y orden de las áreas con Verónica; quién asiste a Fundamentals; si el Reporte Final es en la
  semana 4 o la 5; confirmar con el cliente que los logros se prueben con ejemplos armados.
- La propuesta ya salió el 2026-10-06: confirmar si se reenvía el PDF nuevo. Estado: `Enviada` → `En corrección` →
  `Enviada` al regenerar (la `fecha_entrega` 2026-10-06 se respeta).

> Lo que sigue es el brief original del 2026-10-06 (formato v1.4); las decisiones de arriba prevalecen.

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Conserval (Balance)
- **Slug**: `conserval`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección · Fundamentals (2h grupal) + auditoría de 3 áreas (Atención al cliente, Conciliación de pagos, Cuentas por pagar), 4h por área en 2 sesiones de 2h (12h), 14h totales, modalidad mixta · formato compacto (`DET-026`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Auditar Atención al cliente, Conciliación de pagos y Cuentas por pagar de Conserval, con un logro inmediato en cada área, para llegar a un mapa de oportunidades de IA y una ruta hacia la capacidad propia del equipo
<!--auto:inicio-->
- **Alcance**: 4 entregables en 3 áreas · 14 h de sesión · 4 semanas de trabajo desde el arranque · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Enviada` (meta.json; fecha_entrega 2026-10-06, por convención «terminado = enviado»)
- **Asesora comercial**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com. Desde la v2 (2026-10-08) la slide 8 de próximos pasos la muestra.
- **Contacto / decisor**: el dueño y líder de Conserval (Fernando Luis Vegas), que decide y pagaría el servicio. Responsable interno de logística durante el servicio: Luis. Ningún nombre aparece en el deck.
- **Ficha Comercial Intezia**: `Levantamiento_Conserval_marca_comercial_Balance_2026-10-05.pdf` (Ficha de Levantamiento, registrada 2026-09-30, elaborada por Verónica Rubio). Fuente primaria; qué se tomó y qué no está en la sección siguiente.
- **fecha_arranque_deseada**: no declarada («a mutuo acuerdo»). El formato compacto no lleva Calendario de inicio.
- **resultados_esperados**: objetivo del Reporte Final según la ficha: hoja de ruta para automatizar atención al cliente y cuentas por cobrar con IA sin desperdiciar recursos, aprovechando su sistema de condominios y Watiker. A los 3 meses quiere ver datos y métricas del impacto y el análisis del retorno. Sin cifras propias: el retorno va en modo método.

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Conserval (marca comercial Balance), registrada el 30/09/2026 por la asesora comercial, e instrucción directa del usuario del 06/10/2026
- **Fuente del insumo**: Ficha de Levantamiento de Conserval (marca comercial Balance)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- División Educación inferida: empresa privada de administración de condominios, cliente corporativo. Alianza: no (la ficha no menciona ninguna). Confirmar con la asesora.
- Servicio de Detección por el código DET-026. La ficha marca Detección y Habilidades: Habilidades queda como horizonte («Después») y no se cotiza, igual que en DET-025. Cotizar ambas juntas sería un combo y cambiaría el formato.
- Horas por el lineamiento de Detección: Fundamentals de 2 h (un solo grupo, bajo el máximo de 25) y 4 h por área en 3 áreas = 14 h. El kick-off de arranque va aparte y no suma horas (convención general).
- Sesiones de 2 h: la ficha dice que la duración que les funciona es de 2 horas, así que cada área de 4 h se parte en 2 sesiones de 2 h. Es propuesta del sistema: confirmar con servicio y con la asesora.
- Calendario propuesto por el sistema, no dictado por la ficha: 4 semanas (S1 kick-off y Fundamentals, S2 y S3 Atención al cliente y Conciliación de pagos, S4 Cuentas por pagar y Reporte Final). Atención y Conciliación van primero porque comparten el flujo de pagos; Cuentas por pagar (mensual y ya resuelta en parte) al final. El orden difiere del de la ficha (Atención, Cuentas por pagar, Conciliación): confirmar.
- Las 3 áreas comparten las mismas 2 o 3 personas del área de condominio (primera fase), así que cada sesión de área es con las mismas personas. La ficha no dice si Fundamentals es para esas personas o para las 8 del equipo: el deck dice «el equipo», sin cifra; en ambos casos es un solo grupo de 2 h.
- Modalidad mixta (dato de la ficha en Detección y Habilidades; ambas partes en Caracas). El deck no detalla qué sesiones son presenciales y cuáles virtuales.
- Herramientas: la ficha pide anclar la propuesta en lo que el cliente ya usa y no salir de su zona de confort. El deck no nombra ni pre-recomienda ninguna herramienta; dice que el Reporte Final parte de las que ya usa. El análisis de lo que se puede y no se puede lograr con esas herramientas está solo en brief.md (interno).
- Retorno en modo método: la ficha declara el volumen de reportes de pago, pero no los tiempos por proceso ni el costo hora; el Reporte Final los estima con lo que cada área entregue. «Sin compromiso de resultado».
- Reglas de Detección que se conservan: sin certificado, sin garantía 30-60-90, sin dolor dramatizado ni citas textuales, sin datos personales ni nombres de personas del cliente.
- Las capturas de pago son datos confidenciales según la ficha: el logro inmediato de Atención al cliente se prueba con capturas de ejemplo, sin datos reales de condóminos, hasta definir qué cuenta de IA se usa. Confirmar con el cliente.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Reporte Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas). El cliente es sensible al precio por área y su disponibilidad presupuestaria está «en evaluación»: el programa muestra las horas de cada área para poder cotizar por área.
- Confirmar con la asesora las fechas, los horarios y el orden de las áreas; el deck solo lleva semanas y no muestra asesora ni contacto.
- Confirmar quién asiste a Fundamentals: las 2 o 3 personas del área de condominio o las 8 del equipo.
- Confirmar si el Reporte Final se entrega en la semana 4 (misma semana de la última sesión) o en la 5.
- Confirmar la división (Educación) y que no es alianza, y si el kick-off va aparte (criterio por defecto).

## Qué se tomó de la ficha y qué no

**Se tomó (con el deck como destino):**

| Dato de la ficha | Dónde quedó |
|---|---|
| Servicios de interés: Detección y Habilidades; 3 áreas priorizadas (Atención al cliente, Cuentas por pagar, Conciliación de pagos) | Slides 1 a 5 (Detección, 3 áreas, 4 h cada una); Habilidades como «Después» en la slide 6 |
| Duración que les funciona: 2 horas; modalidad mixta; ambas partes en Caracas | Cada área = 2 sesiones de 2 h; «modalidad mixta» en slides 3 y 4 |
| 2 o 3 personas por área a entrevistar | Paso 1 de la slide 2 |
| Proceso 1: 50 a 60 reportes de pago diarios por WhatsApp, 1 persona valida cada captura | Hecho 1 de la portada |
| Proceso 3: 6 cuentas de Gmail, unos 5 condominios por cuenta | Hecho 2 de la portada |
| Proceso 4: recibos de servicios de terceros, resuelto en parte, sin estandarizar | Hecho 3 de la portada |
| El equipo no usa IA de forma estructurada; solo un chatbot por menú | Hecho 4 de la portada |
| Proceso 2: la decisión final de confirmar el pago y la tasa de cambio se queda en una persona | «Fuera de este alcance» (slide 2) |
| Objetivo del Reporte Final: hoja de ruta sin desperdiciar recursos | Lead de la portada y slide 6 |
| Quiere que el equipo pierda el miedo a la IA y no dependa solo de él | Fundamentals y «Capacidad» en la slide 6 |
| No hay política de datos formal | «Más adelante · Políticas» (slide 6) |

**No se llevó al deck (decisión deliberada):**

- Que el dueño es autodidacta, que construyó su propio sistema con IA y que se apega a Gemini «por comodidad»: es contexto interno. El deck no nombra Gemini ni ninguna herramienta; dice que el Reporte Final parte de las que el cliente ya usa.
- Que la empresa tiene recursos escasos y es sensible al precio por área, y que el equipo no ha perdido el miedo a la IA: tono comercial interno. Se atiende con el dimensionamiento mínimo de Detección (14 h) y mostrando las horas de cada área en el campo Programa.
- Frenar el crecimiento en Instagram, 18 condominios y la urbanización de 350 casas (más de 2.000 personas): la ficha lo da como urgencia. No se dramatiza; el deck habla de los procesos.
- Nombres de personas (dueño, responsable de logística) y el nombre de la integración propia del cliente.
- La cita textual del objetivo y las respuestas «exactamente lo que necesitábamos»: no se usan como citas.

## Alcance con Gemini (análisis interno, no va en la propuesta)

Pedido del usuario (2026-10-06): avisarle qué de lo que pide el cliente queda fuera de alcance con Gemini, porque no quieren salir de ahí, sin ponerlo en la propuesta. Es una evaluación mía; las partes de la web son de la búsqueda del 2026-10-06 y hay que revalidarlas antes de comprometer algo con el cliente.

| Lo que pide el cliente | Con Gemini |
|---|---|
| Que lea las capturas de pago y pre-registre los datos (monto, referencia, fecha, banco) | **Viable como logro inmediato**: Gemini lee imágenes. Con capturas de ejemplo en la sesión, y con la persona validando. |
| Que el sistema lea WhatsApp/Watiker solo, sin pasos manuales | **Depende de Watiker, no de Gemini.** Hace falta que Watiker entregue los mensajes por API, webhook o exportación. No encontré información pública de Watiker: sin eso, queda manual. Es Habilidades, no Detección. |
| Que la IA responda a los condóminos por WhatsApp (en lugar del menú) | **Misma dependencia de Watiker**, y exige conectar un modelo al canal. Fuera de la Detección. |
| Que lea los 6 Gmail y rutee por condominio | **Gemini en Gmail no lo hace**: resume y redacta dentro de un buzón. Rutear entre 6 cuentas exige Apps Script o la API de Gmail con Gemini, o centralizar con reenvío y etiquetas (parte se resuelve sin IA). Si son cuentas @gmail.com y no Workspace, las funciones de Workspace no aplican. |
| Conciliar con el banco y precargar | **El límite es el acceso al banco, no Gemini.** Se puede cruzar un extracto exportado contra los reportes. La confirmación en firme y la tasa de cambio quedan humanas (preferencia del cliente); la tasa debe venir de una fuente cargada, no consultada por la IA. |
| Estandarizar adjudicación de pagos y envío de recibos | **Viable en Gemini**: ya lo resolvió en parte con una integración propia; es documentar y estandarizar. |
| Enseñarle a él y a su equipo a conectar la IA (no la básica) a Watiker y a los correos | **Es Habilidades**, no Detección. La Detección deja el mapa y un logro inmediato por área. |
| Automatizar la mayor cantidad de procesos y ver el retorno a los 3 meses | Sin tiempos por proceso ni costo hora no hay línea base: de ahí el retorno en modo método. Expectativa alta del cliente: cuidar que no se lea como promesa. |

**Datos confidenciales.** Las capturas de pago son datos confidenciales según la ficha y no hay política de datos formal. La búsqueda indica que en la API de pago de Gemini Google no usa los datos para mejorar sus productos y en la gratuita sí (y revisores humanos pueden leerlos), y que el contenido de cuentas Workspace queda excluido del entrenamiento. Antes de cargar datos reales hay que definir qué cuenta usa el cliente; mientras tanto, ejemplos armados para la sesión (decisión del 2026-10-08: solo procesos, sin datos).

**Por qué el deck no lo dice:** la propuesta no nombra Gemini ni sus límites. Lo que sí hace es dejar fuera de alcance «integraciones a medida entre sus herramientas» (horizonte) y «licencias», y ancla el Reporte Final en las herramientas que el cliente ya usa. «Después · Habilidades» dice «aplicar la IA a los procesos priorizados y crear sus propios asistentes», sin prometer conexiones con Watiker.

## Riesgos que marca la ficha (Bloque F) y cómo los atiende el deck

1. **Empresa pequeña, presupuesto «en evaluación», sensible al precio por área.** Dimensionamiento mínimo (14 h, 3 áreas, 1 grupo) y horas por área visibles en Programa. Ventas define el precio (campos vacíos).
2. **Dueño con expectativas altas sobre qué se automatiza rápido.** El deck promete un logro inmediato por área y un mapa, no integraciones; retorno «sin compromiso de resultado».
3. **Apego a Gemini y a su zona de confort.** El Reporte Final parte de lo que ya usan; no se pre-recomienda otra herramienta.
4. **El equipo aún no pierde el miedo a la IA.** Fundamentals primero.

## Plan de sesiones (referencia interna; el deck solo lleva semanas)

| Semana | Sesión | Horas |
|---|---|---|
| 1 | Kick-off (aparte, sin horas) y Fundamentals, un solo grupo | 2 |
| 2 y 3 | Atención al cliente (2 sesiones de 2 h) y Conciliación de pagos (2 sesiones de 2 h), con las 2 o 3 personas del área de condominio | 4 + 4 |
| 4 | Cuentas por pagar (2 sesiones de 2 h) y entrega del Reporte Final (Mapa de Calor, Índice de Madurez, hoja de ruta y recomendación de herramientas) | 4 |

Total 14 h. El calendario en 4 semanas, el orden de las áreas y el Reporte Final en la semana 4 son propuestos por el sistema; confirmar con servicio y con la asesora.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py conserval      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh conserval             # verifica, genera el PDF y ajusta los campos
```
