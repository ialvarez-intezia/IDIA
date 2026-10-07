# Brief · N58 Banco Digital · Servicio de Habilidades (CAI-037)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: N58 Banco Digital
- **Slug**: `n58-banco-digital-ti`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-037`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión (campos de precio vacíos para ventas))
- **Eje temático**: Uso profesional de Claude Code y Codex en el equipo de TI de N58: fundamentos y uso seguro, construcción con código, revisión y pruebas, e implementación de un estándar de equipo
<!--auto:inicio-->
- **Alcance**: 6 entregables en 3 módulos · 12 h de sesión · 6 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
<!--auto:fin-->
- **Estado**: `Enviada` (meta.json; fecha_entrega 2026-10-06, por convención «terminado = enviado»)
- **Asesora comercial**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com (la misma de CAI-034). El deck compacto no lleva slide de cierre ni contacto.
- **Contacto del cliente**: sin definir para esta propuesta. En CAI-034 el interesado de Tecnología era Jonathan (no se nombra en el deck).
- **Ficha Comercial Intezia**: no existe una Ficha propia de Tecnología. El deck no usa datos de la ficha de CAI-034 (Mercadeo, 2026-10-01); esa ficha solo sirvió de contexto interno (Microsoft 365, modalidad presencial pedida por Mercadeo).
- **fecha_arranque_deseada**: no declarada. El formato compacto no lleva Calendario de inicio.
- **resultados_esperados**: no declarados; el retorno va en modo método, sin cifras.

## Origen y fuente

- **Origen**: Instrucción directa del usuario (06/10/2026) y antecedentes de N58 en la propuesta CAI-034 (Mercadeo con Claude) y su documento de soberanía de datos para Tecnología
- **Fuente del insumo**: Ficha de Levantamiento de N58 (01/10/2026) y documento de soberanía de datos para Tecnología (CAI-034)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Código CAI-037: el usuario pidió CAI-035, que ya es de DUSA (enviada el 04/10/2026), y CAI-036 es de Alfonzo Rivas; el usuario eligió CAI-037, el siguiente libre (06/10/2026).
- Guardia §4.21 punto 5: el usuario eligió el formato compacto. El programa se reexpresó como 6 entregables en 3 módulos (Fundamentals, Construcción, Implementación), con la misma estructura de CAI-034: 12 h de propuesta y kick-off de 1 h aparte.
- Enfoque elegido por el usuario: escribir y refactorizar código, revisión de código y pruebas, y gobierno y uso seguro. Los 6 entregables y sus nombres los propuso el sistema a partir de ese enfoque: confirmar con servicio. El usuario no dio más contexto del equipo de TI.
- Reparto de horas (propuesta del sistema): Fundamentals 2 h, Construcción 3 sesiones de 2 h y Implementación 2 sesiones de 2 h, una sesión por semana en 6 semanas. Es una proyección de Intezia: confirmar con servicio y con Tecnología.
- Las sesiones usan un repositorio de práctica, sin código de producción ni datos de clientes. Es una decisión de diseño por la restricción de soberanía de datos de N58 (circular de Sudeban del 29/12/2023, reportada por prensa y aún no confirmada contra la Gaceta Oficial); confirmar con Tecnología.
- Portada: los 3 datos describen el contenido del proyecto (2 h de Fundamentals, 6 h de Construcción, 4 h de Implementación), no al cliente. No hay una Ficha propia de Tecnología, así que no se afirma nada sobre cómo usa hoy la IA el equipo de TI. La primera versión traía «cada uno paga su herramienta» y «regulado por Sudeban» (de la ficha de Mercadeo de CAI-034); el usuario los retiró el 2026-10-06 porque no se saben para TI.
- Licenciamiento: no se afirma quién contrata ni qué plan. La propuesta no lleva precios de lista; el banco los confirma con cada proveedor. Si se quieren cifras, hay que verificarlas con fecha.
- La línea base del tiempo de revisar y probar código se levanta dentro de la sesión de Fundamentals (2 h): confirmar con servicio que cabe.
- Retorno en modo método: no hay volúmenes, tiempos ni costo hora del equipo de TI. «Hacia la semana N» es aritmética (semanas de ejecución + 13): confirmar con servicio.
- Sin certificado de participación por defecto (§4.21). Modalidad omitida: en CAI-034 Mercadeo pidió presencial, pero no se sabe para TI.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Precios de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas).
- Confirmar con Flavia: cuántas personas de TI participan, quién es el contacto de Tecnología, modalidad, fecha y horario.
- Confirmar con Tecnología qué cuenta de Claude Code y de Codex se usará y quién la contrata, y que el repositorio de práctica no contiene datos de clientes.
- Confirmar los 6 entregables y el reparto de las 12 h con servicio.
- Confirmar cómo se relaciona con CAI-034 (Mercadeo) y con el documento de soberanía de datos: paralelo, o condicionado a que Tecnología resuelva la arquitectura.

## Qué se pidió y qué se decidió

Instrucción del usuario (2026-10-06): «una propuesta para el banco N58 bajo el CAI-035, la asesora comercial es Flavia, sobre el uso de Claude Code y Codex como profesionales para el equipo de TI; no tengo más contexto, pero conoces lo que hacen por CAI-034 (no es del mismo tipo)».

Respuestas del usuario a las 4 preguntas (misma fecha):

| Pregunta | Respuesta |
|---|---|
| Código | **CAI-037**. CAI-035 ya es de DUSA (enviada 2026-10-04) y CAI-036 de Alfonzo Rivas (2026-10-06). |
| Formato (guardia §4.21 punto 5) | Compacto, ~5 slides (salió de 6 con la de retorno). |
| Enfoque | Escribir y refactorizar código · revisión de código y pruebas · gobierno y uso seguro. |
| Duración | 12 h, como CAI-034: Fundamentals 2 h + Construcción 6 h + Implementación 4 h, con kick-off de 1 h aparte. |

- **Herramientas con nombre propio.** A diferencia de CAI-036 (sin herramienta), aquí el pedido nombra Claude Code y Codex y el deck las nombra. Se agregan como un solo carril («Claude Code y Codex»), porque el contenido no se parte por herramienta.
- **Soberanía de datos.** El documento aparte para Tecnología (`n58-banco-digital/soberania-datos.html`) deja abierta una decisión de arquitectura: Sudeban exige que las bases de datos principales no salgan del país y ninguna herramienta de IA de uso general tiene infraestructura en Venezuela. Claude Code y Codex envían código a servidores externos, así que el diseño trabaja solo con un repositorio de práctica, sin código de producción ni datos de clientes. El deck lo dice en «Fuera de este alcance» y en las notas de inversión. No resuelve la arquitectura: eso se trata aparte con Tecnología.
- **Sin precios de lista de licencias.** Las licencias de ambas herramientas van aparte y el deck no cita planes ni precios (no se verificaron). No se afirma quién contrata.
- **Sin nombres de personas del cliente** (Mari, Sandokan, Jonathan) en el deck.
- **Con seguimiento 30-60-90, garantía, hoja de inversión y slide de retorno (modo método).** Es el estándar de Habilidades y lo que llevó CAI-034. El usuario no pidió quitarlos.

## Antecedentes de la cuenta

| Código | Qué es | Estado |
|---|---|---|
| CAI-034 | Mercadeo con Claude: más de 50 creativos, 4 artículos SEO, Skill propia y 1 persona formada · 12 h, presencial | Enviada 2026-10-01 |
| Documento de soberanía de datos | Para Tecnología: qué exige Sudeban, qué garantiza una suscripción de Claude y qué sigue abierto | Documento de trabajo, octubre 2026 |
| CAI-037 | Esta propuesta: equipo de TI con Claude Code y Codex · 12 h | Enviada 2026-10-06 |

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py n58-banco-digital-ti      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh n58-banco-digital-ti             # verifica, genera el PDF y ajusta los campos
```
