# Brief · Steam Solutions · Servicio de Habilidades (CAI-038)

## Actualización 2026-10-08 · migrada a la plantilla v2 (8 slides) · VIGENTE

Instrucción directa del usuario: «ajustar la CAI-038 al nuevo formato». «Formato nuevo» = **plantilla compacta v2.0**
(commit `93e0b67`, 2026-10-07): el `datos.json` v1.4 se migró según la spec §13 y se regeneró con
`--actualizar-css --forzar-overrides`. Orden del deck: Portada · Alcance · Ruta · Cómo trabajamos · Entregables ·
Retorno · Inversión · Próximos pasos. El deck de 6 slides v1.4 y su PDF quedan en `_pdf-anteriores/`. Sin cambios de
contenido de fondo: 18 h, 6 entregables en 3 módulos, 6 semanas, kick-off de 1 h aparte, seguimiento 30-60-90, retorno
en modo método, herramienta de IA a definir en el kick-off.

### Decisiones

- **Sin «Facilidad de pago»**: no se preguntó; el usuario la omitió en la CAI-032, la DET-024, la CAI-040 y la
  DET-026, así que se aplicó el mismo criterio (`omitir: ["pago"]`). Si Ventas la quiere, se agrega con cuotas
  ligadas a los hitos de la ruta.
- Se conservan las reglas de la ronda anterior: Intezia **guía** y el equipo **construye**; sin nombrar herramientas
  de IA; ambiente de desarrollo con datos sintéticos.

### Qué cambió respecto de la v1.4 (en el lenguaje de la v2)

| v1.4 | v2 |
|---|---|
| `alcance.pasos` y `quien_construye` (la regla «guiamos, el equipo construye») | `metodo` (4 pasos: nivelamos, instalamos, guiamos, dejamos listo) y `metodo.quien_construye` con la regla en negrita |
| (sin método, logística ni asesora) | `metodo.practica` (tareas reales, herramienta, probado de verdad), `metodo.datos`, `por_que_orden`, `logistica` y `proximos_pasos.asesora` |
| (sin «para qué» por módulo) | `areas[].para_que` en los 3 módulos |
| `frentes[].etiqueta`, `areas_html`, «S1-S6», «S = semana» | `frentes[].nombre` = «Equipo de desarrollo», «1 a 6» y nota sin códigos |
| Fase «Implementación», carril «Desarrollo con IA» en la tarjeta de la ruta | Fase «Flujo» (≤ 6 caracteres con «1 entregable» al lado) y `nombre_corto` «Desarrollo» (la tarjeta de la línea de trabajo no cabía) |
| «Precios de lista», «costo hora de referencia» | «Valores de lista», «valor hora de referencia» |
| Inversión «por horas de sesión», sin términos y condiciones en Notas | «Inversión del proyecto»; Duración con soluciones y semanas primero; Notas con los términos y condiciones |
| Sin asesora ni contacto | Slide 8 con Verónica Rubio (teléfono y correo de la Ficha; el cargo «Asesora comercial» sale de este brief) |

La slide 7 conserva la tarjeta de licenciamiento («Herramienta de IA · a definir») y la garantía 30-60-90.
`overrides.css` nuevo: escala de las slides 2, 3, 4 y 5.

### Pendientes (a confirmar antes de reenviar)

- Inversión, descuento y total (campos vacíos para ventas), cómo se comunica el plan de pago (no hay slide) y, como
  antes, sede y viáticos (tema comercial, fuera del deck).
- Sede, fechas, horarios, quién asiste a cada sesión de agentes y si cada agente va en 1 sesión de 4 h o en 2 de 2 h.
- «Hacia la semana 19» (6 semanas más 90 días) es aritmética: confirmarla con servicio.
- La propuesta ya salió el 2026-10-06: confirmar si se reenvía el PDF nuevo y avisar que reemplaza al anterior. Estado:
  `Enviada` → `En corrección` → `Enviada` al regenerar (la `fecha_entrega` 2026-10-06 se respeta).

> Lo que sigue es el brief original del 2026-10-06 (formato v1.4); las decisiones de arriba prevalecen.

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Steam Solutions
- **Slug**: `steam-solutions`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-038`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Desarrollo guiado por especificaciones con agentes de IA en el equipo de desarrollo de Steam Solutions: método común, agentes de desarrollo, pruebas y despliegue, y un flujo común adoptado por el equipo
<!--auto:inicio-->
- **Alcance**: 6 entregables en 3 módulos · 18 h de sesión · 6 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Enviada` (meta.json; fecha_entrega 2026-10-06, por convención «terminado = enviado»)
- **Asesora comercial**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com. Desde la v2 (2026-10-08) la slide 8 de próximos pasos la muestra.
- **Contacto del cliente**: Juan Cisneros, probable líder técnico del equipo de desarrollo (cargo sin confirmar); es también el responsable interno de logística durante el servicio. Su nombre no aparece en el deck.
- **Ficha Comercial Intezia**: `Levantamiento_Steam_Solutions_2026-10-05.pdf` (Ficha de Levantamiento, registrada 2026-09-30, elaborada por Verónica Rubio). Es la fuente primaria; qué se tomó y qué no está en la sección siguiente.
- **fecha_arranque_deseada**: no declarada. La disponibilidad semanal exacta se define en el kick-off. El formato compacto no lleva Calendario de inicio.
- **resultados_esperados**: que el equipo construya y mantenga agentes de desarrollo, pruebas y despliegue de forma autónoma tras la capacitación, bajo una metodología común (así lo declara la ficha para medir a 30, 60 y 90 días). Sin cifras: el retorno va en modo método.

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Steam Solutions (registrada el 30/09/2026 por la asesora comercial) e instrucción directa del usuario del 06/10/2026: la herramienta de IA para desarrollo se define en el kick-off
- **Fuente del insumo**: Ficha de Levantamiento de Steam Solutions
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Código CAI-038 indicado por el usuario (siguiente libre tras CAI-037). División Educación y alianza «no» inferidas: software house privada, cliente corporativo, sin alianza en la ficha. Confirmar con la asesora.
- Guardia §4.21 punto 5: no se preguntó. El contenido son soluciones concretas (un método y 3 agentes), no un programa de módulos de charla o curso, así que va directo al compacto, como CAI-032 y CAI-037.
- Herramienta de IA: por instrucción del usuario (06/10/2026) se define en el kick-off. El deck no nombra ninguna herramienta ni las 4 que usa hoy el equipo (ficha); dice que se elige en el kick-off. El problema de pago con tarjetas en Venezuela que tuvo el equipo con una membresía se anticipa como criterio de elección (pago y renovación estables), sin nombrar la herramienta (§4.11: no se afirma que el cliente cambie de stack).
- Horas: 18 h por instrucción del usuario (06/10/2026). Se había propuesto 12 h (el tope del lineamiento de Habilidades: 8 a 12 h por área, hasta 5 procesos, con 2 h por agente) y el usuario subió cada agente a 4 h para dar holgura. Excede el tope del lineamiento: es una excepción decidida por el usuario. Son Fundamentals 2 h, método 2 h, 3 agentes de 4 h y flujo común 2 h. El kick-off de 1 h va aparte y no suma (como CAI-034 y CAI-037).
- Reparto y calendario propuestos por el sistema: 6 sesiones, una por semana, en 6 semanas (Fundamentals y método de 2 h en las semanas 1 y 2, un agente de 4 h por semana en las 3 a 5 y el flujo común de 2 h en la 6). Se supuso una sesión de 4 h por agente; también podría ser en 2 sesiones de 2 h según la disponibilidad semipresencial (4 o 5 personas en la oficina por día, el resto remoto), que la ficha deja para el kick-off: confirmar.
- Rol del equipo y de Intezia (instrucción del usuario, 06/10/2026): Intezia guía la construcción para que cada agente funcione, pero es el equipo quien lo construye. Por eso se quitó de «Fuera de este alcance» el punto «agentes terminados para producción» y el deck dice «guiamos» donde antes decía «construimos». Cada entregable sigue acotado a «probado en una tarea real» o «en un ambiente de desarrollo». La expectativa del cliente (agentes «autónomos y robustos») se consolida en el seguimiento a 30, 60 y 90 días; con 4 h por agente (subido por el usuario para dar holgura), confirmar con servicio que alcanza para que funcionen.
- Se trabaja en ambiente de desarrollo con datos sintéticos, que es la política que el cliente ya sigue (su solución vendida a clínicas está sujeta a normativa de datos de salud). El deck no cita ninguna norma.
- Las 8 personas son los programadores del equipo de desarrollo (no incluye servidores/plataforma): un solo grupo de Fundamentals. Quién asiste a cada sesión de agentes depende de la disponibilidad semipresencial: confirmar.
- Los hechos de la portada salen de la ficha. «Cuatro distintas» cuenta las herramientas que la ficha menciona (cuatro), sin nombrarlas. Se omitió la frase de la ficha sobre falta de rigor en especificaciones: se dice neutral que falta un método común.
- «Skills» aparece solo en un entregable y glosado como «instrucciones reutilizables (skills)» (§4.12 y §4.4: término nativo de las herramientas de IA). En el resto del deck se dice «especificación».
- Línea base del tiempo actual de probar y desplegar: se levanta en la sesión de Fundamentals (2 h). Confirmar con servicio que cabe.
- Retorno en modo método: la ficha no trae volúmenes, tiempos ni costo hora. «Hacia la semana N» es aritmética (semanas de trabajo + 13): confirmar con servicio.
- Sin certificado de participación por defecto (§4.21). Sin nombres de personas del cliente ni su cargo. La sede (oficinas del cliente o sala de Intezia) y los viáticos no van en el deck: son un tema comercial pendiente.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas). Si las sesiones son en las oficinas del cliente (San Antonio de los Altos) hay que evaluar viáticos y transporte del consultor; la alternativa es la sala de Intezia (Las Mercedes). Son 18 h de sesión: 6 más que el tope del lineamiento (12 h).
- Confirmar con la asesora la sede, las fechas, los horarios y la disponibilidad semanal (kick-off), y cuántas personas asisten a cada sesión.
- Definir la herramienta de IA en el kick-off y resolver cómo se paga y se renueva su licencia desde Venezuela antes de cotizar la parte de licencias.
- Confirmar con servicio el reparto de las 18 h y si cada agente va en 1 sesión de 4 h o en 2 de 2 h, según la disponibilidad del equipo.
- La ficha dice que la propuesta se enviaba esa misma semana y que había sesión de revisión el lunes a las 3:30 pm: confirmar la fecha vigente.

## Qué se pidió y qué se decidió

Instrucción del usuario (2026-10-06): propuesta para Steam Solutions bajo el CAI-038, asesora Verónica, con la ficha adjunta. **«El IDE con IA a utilizar lo vamos a definir en el kick-off, conociendo un poco más de ellos.»** Por eso el deck no nombra ninguna herramienta de IA ni las cuatro que usa hoy el equipo; la elección es un hito del kick-off.

Segunda ronda (misma fecha): quitar de «Fuera de este alcance» el punto «agentes terminados para producción» y destacar que Intezia guía y el equipo construye (ver Riesgos, punto 2).

Tercera ronda (misma fecha): el usuario preguntó si 2 h por agente era muy poco; se le respondió que sí y se propusieron 3 opciones. **Decisión del usuario: 4 h por agente «y quedamos con holgura»**. Pasó de 12 h a 18 h (Fundamentals 2 + método 2 + 3 agentes de 4 h + flujo común 2), kick-off aparte. Excede el tope del lineamiento (12 h): excepción decidida por el usuario.

## Qué se tomó de la ficha y qué no

**Se tomó (con el deck como destino):**

| Dato de la ficha | Dónde quedó |
|---|---|
| Servicio de interés: Habilidades; área priorizada: desarrollo de software | Todo el deck (1 módulo de trabajo, 12 h) |
| 8 programadores (no incluye servidores/plataforma), de niveles distintos | Hecho 1 de la portada; Fundamentals en un solo grupo |
| Cuatro herramientas de IA en uso, ninguna homologada | Hecho 2 de la portada (sin nombrarlas); flujo común de la semana 6 |
| Proceso aislado, poco sistemático, cada quien a su manera | Hecho 3 de la portada, dicho en neutro |
| Expectativa: agentes de desarrollo, pruebas y despliegue, bajo una metodología por especificaciones y skills | Módulos «Método y criterios» y «Agentes de IA»; titular |
| Quiere una metodología común para todo el ciclo (prototipo de pantalla, experiencia de usuario, desarrollo) | Entregable del método (el prototipo se vuelve especificación) y flujo común |
| Tareas reales: prototipado de pantallas, capas de API, Odoo y Python, apps móviles, pruebas y despliegue | `detalle` de los entregables (programa.md) y «Odoo y Python» en slide 2 |
| Ambiente de desarrollo con datos sintéticos; normativa de datos de salud en su solución para clínicas | Slide 2 («Fuera de este alcance») y notas de inversión; sin citar la norma |
| Modalidad mixta, equipo semipresencial (4 o 5 personas en la oficina por día) | «Modalidad mixta» en slides 3 y 4; la disponibilidad exacta va al kick-off |
| Uso esperado para medir a 30, 60 y 90 días | Seguimiento 30-60-90 y retorno |
| Acceso a una herramienta inconsistente por problemas de pago con tarjetas en Venezuela | Tarjeta de licenciamiento: «un criterio es que su pago y renovación funcionen de forma estable desde Venezuela» |

**No se llevó al deck (decisión deliberada):**

- El nombre y el cargo de Juan Cisneros, y la cita textual de su objetivo (no se usan citas).
- El juicio de que el equipo «no es riguroso» en especificaciones y skills: el deck dice solo que falta un método común.
- Los nombres de las herramientas (GitHub Copilot, Claude, Cursor, Antigravity) y Lovable: la herramienta se define en el kick-off (§4.11: no se afirma que el cliente cambie de stack).
- La sede y los viáticos: el cliente preguntó si la capacitación puede darse en sus oficinas (San Antonio de los Altos), algo que Intezia no ha hecho antes; queda pendiente evaluar viáticos y transporte del consultor o usar la sala de Intezia (Las Mercedes). Es un tema comercial, no va en el deck.
- El compromiso de enviar la propuesta esa misma semana y la sesión de revisión del lunes a las 3:30 pm.

## Riesgos que marca la ficha (Bloque F) y cómo los atiende el deck

1. **Herramienta indefinida y problema de pago desde Venezuela.** La ficha pide anticiparlo antes de cotizar. El deck lo hace sin nombrar la herramienta (criterio de elección en el licenciamiento y hito de kick-off). Pendiente real: resolver cómo se paga y renueva la licencia antes de cotizar esa parte.
2. **Expectativa alta: agentes «autónomos y robustos».** Instrucción del usuario (2026-10-06, segunda ronda): quitar de «Fuera de este alcance» el punto «agentes terminados para producción» y destacar que Intezia **guía** la construcción para que los agentes funcionen, pero **es el equipo quien los construye**. El deck lo dice en el subtítulo y el paso 3 de la slide 2, en «Quién construye» (con negrita), en la celda y el hito de las semanas 3 a 5 y en el valor inmediato de la semana 5. Cada entregable sigue acotado («probado en una tarea real», «en un ambiente de desarrollo»). Con 2 h por agente, que «funcionen» era un compromiso más fuerte que antes, así que el usuario subió cada agente a 4 h (18 h en total) para dar holgura. Lo robusto se apoya en el seguimiento a 30, 60 y 90 días.
3. **Datos de salud.** Todo el trabajo en ambiente de desarrollo con datos sintéticos, como ya lo hace el equipo.
4. **Sede fuera de Intezia.** Sin decidir; puede afectar el precio por viáticos.
5. **Pide control y saber si le sacan el máximo provecho.** Línea base en Fundamentals y medición a 30, 60 y 90 días.

## Plan de sesiones (referencia interna; el deck solo lleva semanas)

| Semana | Sesión | Horas |
|---|---|---|
| Antes | Kick-off (aparte, sin horas): definir la herramienta de IA, la tarea real de práctica y la disponibilidad semanal | 1 |
| 1 | Fundamentals: criterios y reglas de uso (8 desarrolladores en un solo grupo) y línea base | 2 |
| 2 | Método: plantilla de especificación y skills, sobre una tarea real | 2 |
| 3 | Agente de desarrollo: lo construye el equipo, con la guía de Intezia | 4 |
| 4 | Agente de pruebas automatizadas: lo construye el equipo, con la guía de Intezia | 4 |
| 5 | Agente de despliegue (ambiente de desarrollo): lo construye el equipo, con la guía de Intezia | 4 |
| 6 | Flujo común documentado y adoptado por el equipo | 2 |

Total 18 h (2 + 2 + 4 + 4 + 4 + 2). Se supuso una sesión de 4 h por agente; también puede ser en 2 sesiones de 2 h. El reparto, el orden y el calendario en 6 semanas son propuestos por el sistema (ver Decisiones y supuestos); confirmar con servicio y con la asesora.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py steam-solutions      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh steam-solutions             # verifica, genera el PDF y ajusta los campos
```
