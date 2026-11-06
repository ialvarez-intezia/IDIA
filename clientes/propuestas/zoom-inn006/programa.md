# Programa interno · Zoom · Servicio de Innovación (INN-006)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Texto de la dirección y respuestas de Ivana (26/10/2026); documentación de Google para administradores (26/10/2026); dashboards y casos de éxito de Zoom.

## 1. Resumen

- **3 encuentros en 1 área**, **52 h** de trabajo.
- Herramienta **Gemini y Google Workspace**: 3 encuentros, 52 h.
- Horas por fase: F1 24 h (1 sol.) · F2 28 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Bootcamps de Gems a Skills | Gemini y Google Workspace | Todas las áreas de Zoom | 52 | 3 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Noviembre (12 encuentros antes de diciembre) | Enero y febrero (9 de margen y 5 de respaldo) |
|---|---|---|
| Bootcamps de Gems a Skills | 24 h · 1 sol. | 28 h · 2 sol. |

- **TI activa las Skills**: Antes del primer encuentro, en la consola de administración.
- **Primer encuentro**: Arranca antes del 17 de noviembre, cuando los Gems pasan a Configuración.
- **Cierre de noviembre**: Los primeros 12 encuentros terminan antes de diciembre.
- **Grupos de respaldo**: Los últimos 14 encuentros: 9 de margen y 5 de respaldo.
- **Cierre**: Casos medidos y Skills compartidas, antes del 1 de marzo.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Todas las áreas de Zoom · 3 encuentros · 52 h · Gemini y Google Workspace · línea A

Para qué (lo que ve el cliente): Las 510 personas de Zoom, en grupos de hasta 25, pasan sus Gems a Skills en vivo.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| BOO-1 | Bootcamps de noviembre | Referencia interna: 12 encuentros de 2 horas en noviembre, hasta 25 personas por encuentro. | - | - | - | 24 | F1 |
| BOO-2 | Bootcamps de enero y febrero | Referencia interna: 9 encuentros de 2 horas en enero y febrero, de margen para rezagados. | - | - | - | 18 | F2 |
| BOO-3 | Grupos de respaldo | Referencia interna: 5 grupos de respaldo de hasta 25 personas, un encuentro de 2 horas cada uno (rango extra). | - | - | - | 10 | F2 |

## 4. Fuera de alcance

- Licencias de Google y activación de las Skills: las gestiona el equipo de TI de Zoom antes del primer encuentro.
- Construir Skills nuevas: se migran los Gems que ya existen y se acuerdan las reglas; lo nuevo es otra etapa.
- Rehacer los flujos de Workspace Studio con «Ask a Gem»: se señalan, y los rehace TI con la guía de Google.

## 5. Supuestos a confirmar (antes del método)

- Decisión de Ivana (27/10/2026): una sola propuesta INN-006, bootcamp con las 510 personas, mencionando las áreas del servicio. No hay total de personas por área (no se tiene), así que no se ofrecen las opciones por área (B y C). INN-006-A, -B, -C y la unión A-B-C siguen en sus carpetas, sin archivar.
- Control del número de encuentros (mensaje del equipo): como Zoom arma los grupos, el deck dice que se cotizan 26 grupos de hasta 25 personas y que los adicionales se cotizan aparte (en las Notas de la inversión). Es redacción del sistema, no dicha por María: confirmar.
- 26 grupos (indicación del equipo, 27/10/2026: «cotizar 26 grupos de hasta 25 personas: los 21 que hacen falta para los 510, más 5 grupos extra por si acaso; 52 horas de sesión»): 21 para las 510 personas (510 / 25, redondeado hacia arriba) más 5 grupos extra. Cada grupo es un encuentro de 2 h. Calendario del sistema: 12 antes de diciembre, 9 en enero y febrero y los 5 grupos extra al final, antes del 1 de marzo de 2027. Horas: 26 × 2 = 52 h de encuentro.
- Áreas mencionadas: Operaciones, Comercial, Legal, Zoom Miami, Gestión Humana y Tecnología (las ya trabajadas, según la memoria y los casos de éxito) y «el resto de las áreas»; sin números por área.
- Qué reemplaza: INN-003 e INN-004 (Zoom, 19/10/2026, Borrador) llevaban Claude Fundamentals; estas tres solo migran Gems a Skills con Gemini. Confirmar con Ivana que INN-003 e INN-004 se archivan.
- Encuentros de 2 horas, hasta 25 personas. Calendario: arranque la semana del 2 de noviembre (Ivana), hasta 3 por semana (lunes, miércoles y viernes: días propuestos por el sistema), grueso antes de diciembre (temporada alta de Zoom) y margen de enero y febrero para rezagados, antes del 1 de marzo de 2027. Horario: por acordar (no lo dio nadie). Que las sesiones arranquen antes del 17 de noviembre.
- Excepción a CLAUDE.md §4.23 (Keiber, 8/10/2026: sin semanas, sesiones ni fechas): el calendario con fechas va en la propuesta por pedido expreso de Ivana («coloca todo en la propuesta»). Solo la slide de calendario usa «sesiones» y «semana»; el resto del deck dice «encuentros».
- Fechas de Google (documentación oficial, consultada el 26/10/2026): skills en Workspace desde el 5/10/2026 (Rapid Release hasta el 12/10; Scheduled Release del 19/10 a mediados de noviembre); skills en la app de Gemini desde el 13/10/2026 (hasta mediados de noviembre); 17/11/2026 los Gems pasan a Configuración; no antes del 1/3/2027 Business y Enterprise no podrán crear, editar ni usar Gems (Education, no antes del 1/6/2027). Google publicará más información al menos 30 días antes de la migración automática. Ivana pidió planificar el 1/3/2027 como fecha fija aunque Google diga «no antes de»: el deck lo dice con «no antes de».
- Dos puntos de la prensa, confirmados en la documentación oficial de Google para administradores (22/10/2026): los flujos de Workspace Studio con el paso «Ask a Gem» dejan de funcionar desde el 1/3/2027 (no se pueden añadir a flujos nuevos), y una Skill de la app de Gemini no se sincroniza con las apps de Workspace (se recrea en Workspace Studio). Los Gems que se usan en Workspace tampoco se transfieren solos.
- Requisito previo de TI (de la documentación de Google; PENDIENTE de confirmar con David): activar el ajuste «Allow people to use skills in Studio and Gemini in Workspace»; edición con skills en Workspace (Business Starter, Standard o Plus; Enterprise Standard o Plus; Google AI Pro for Education o AI Expanded Access); personas de 18 años o más; canal de lanzamiento (Rapid o Scheduled Release: el despliegue en Scheduled llega a mediados de noviembre, y el primer encuentro es el 2 de noviembre); lista de flujos de Workspace Studio con «Ask a Gem»; permisos de uso compartido de Drive de los Gems (se transfieren a las Skills).
- «Por qué con nosotros»: resultados propios de Zoom del informe de casos de éxito (clientes/casos-de-exito-zoom, 19/10/2026) y de los dashboards de impacto (Encuesta Edu-Trace de cierre, 83 respuestas de seis áreas): índice de impacto promedio 87/100, 89 % de aciertos en la evaluación técnica (222 de 249, medido), 88 % usa Gemini como herramienta principal (73 de 83, autopercibido) y el seguimiento a 30 días de Tecnología (16/10/2026, la herramienta ya adoptada). Son datos de cierre y percepción: el deck no los presenta como ahorro medido (§4.17). Sin nombres de personas.
- Agenda de 2 horas: no cabe todo a la vez; propuesta del sistema: el inventario va antes con un formulario (fuera de las 2 horas), la actualización del ecosistema se reduce a 15 minutos con lo que le sirve a Zoom, y la medición del caso se inicia en el encuentro (tiempo de hoy) y se completa con la Skill ya en uso. Reparto: priorización 15 min, migración en vivo 55, reglas 15, actualización 15 y medición 20.
- Marca: Brand Kit Intezia v2.1 (13/10/2026, adjunto de Ivana): amarillo #FFD300, negro #0A0A0A, naranja #E58423 y Poppins (OFL, descargada de fontsource). Los archivos del logo v2 («Brand Kit v2 2026-10 / archivos») no están en el repositorio: el deck usa los logos actuales de `logos/` (el amarillo del arte es el #F4BA1A anterior). El CSS compacto, las cajas de la hoja de cotización y los campos del PDF conservan tintes del amarillo anterior. Falta canonizar la marca v2.1 en `empresa/marca-visual.md` y en las plantillas.
- Horas para cotizar (el deck no lleva precios): 26 encuentros de 2 h = 52 h; con 2 facilitadores, 104 h de trabajo de encuentro; preparación 8 h, coordinación con TI 4 h y seguimiento 16 h: total 132 horas de trabajo. Estimación del sistema, por confirmar.
- Pago: tres cuotas ligadas a hitos (40/30/30, propuesta del sistema, por confirmar con María), montos vacíos. Sin garantía ni seguimiento 30-60-90.

## 6. Cómo trabajamos (slide 6)

**Por qué en este orden:** Primero se llega con el inventario hecho; después se prioriza y se migra en vivo; al final se acuerdan las reglas y se mide un caso.

- **Antes**: Cada persona anota sus Gems en un formulario breve y llega con su inventario listo.
- **Priorizamos**: Se eligen los Gems que de verdad se usan. 15 minutos.
- **Migramos**: Esos Gems pasan a Skills, en vivo, con Intezia al lado. 55 minutos.
- **Medimos**: Un caso: el tiempo de hoy contra el tiempo con la Skill. 20 minutos.

- En la práctica, **Reglas comunes**: Se acuerda cómo nombrar y compartir las Skills. 15 minutos.
- En la práctica, **Al día con Google**: Qué cambió en Gemini y Workspace estos meses y qué le sirve a Zoom. 15 minutos.
- En la práctica, **Cabe en 2 horas**: El inventario va antes y la medición se completa con la Skill ya en uso: así las 2 horas son práctica.
- Datos: Se migran solo los Gems que cada persona comparte y se respetan los permisos de Drive: nada confidencial se carga sin permiso.
- Quién construye: Intezia guía cada encuentro en vivo y las personas de Zoom trabajan con sus propios Gems: se construye en conjunto.

**Logística:** modalidad: A acordar con el equipo de TI de Zoom: en línea o presencial. · participantes: Hasta 25 personas por encuentro; 510 personas de todas las áreas de Zoom. · ritmo: Encuentros de 2 horas, con hasta tres en cada ciclo de cinco días hábiles. · arranque: TI activa las Skills antes del primer encuentro; Zoom confirma asistentes y horarios..

## 7. Retorno esperado (slide 7)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Caso real; Tiempo de hoy; Con la Skill; Diferencia.

## 8. Facilidad de pago (slide 9)

| Cuota | Cuándo | Hito | %% |
|---|---|---|---|
| 1 | Al aprobar | Reserva del calendario. | 40 |
| 2 | Fin de noviembre | Los 12 encuentros de noviembre realizados. | 30 |
| 3 | Cierre | Todos los encuentros realizados y los casos medidos. | 30 |

Los montos van vacíos en el PDF (campos `PagoCuota1..3`): los escribe ventas y deben sumar el total de la slide de inversión. No se anotan en este repositorio.

## 9. Próximos pasos (slide 10)

Asesora comercial que ve el cliente: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056.

