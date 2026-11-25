# Brief · Superfina · Servicio de Habilidades (CAI-092)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Superfina
- **Slug**: `superfina-cai092`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-092`), presentada al cliente como **propuesta de proyecto**; formato compacto de 10 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Automatizar por completo la compra de Superfina, un solo departamento trabajado a fondo: de los sugeridos con ventas reales (Vilches y Estelar) a la orden de compra generada por Claude, cargada en Estelar con validación humana y enviada por el WhatsApp de compras a los proveedores, como solución lista que el equipo opera
<!--auto:inicio-->
- **Alcance**: 6 entregables en 2 partes del proceso · 42 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Respuesta a la solicitud (1) · 8 Respuesta a la solicitud (2) · 9 Inversión · 10 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Especificación de Ivana del 09/11/2026 (qué pide el cliente, flujo, alcance, modelo de entrega, distribución de 42 horas, requisitos, riesgos, inversión y hoja de ruta) para la propuesta CAI-092 de Superfina, con Verónica Rubio como asesora. Sin ficha ni transcripción en el repositorio
- **Fuente del insumo**: Especificación de la propuesta (Ivana, 09/11/2026) y tabla de distribución de horas
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (09/11/2026): propuesta CAI-092 para Superfina, asesora Verónica Rubio, con la especificación completa (qué pide el cliente, flujo, alcance, modelo de entrega, distribución de 42 h, requisitos, riesgos, inversión y hoja de ruta) y la tabla de construcción. Educación y sin alianza: confirmados con Ivana. Sin ficha ni transcripción en el repositorio.
- Horas (de Ivana): 42 h = construcción 26 h en línea (sesiones con TI 4, conexión de Estelar 5, Vilches 7, proyecto del comprador y manual 4, tareas programadas 2, Skills 4), testeo 8 h presencial (conexiones en sitio 1, ciclo real con un proveedor 3, ciclo con otros proveedores 2, comparación contra la carga manual 1, ajustes 1) y adopción 8 h presencial (entrega de la cuenta y del manual 2, ejecución con acompañamiento 4, evaluación y acta 1, plan 30/60/90 y siguiente propuesta 1). El reparto del testeo y la adopción entre las seis piezas es mío: Ivana dio los totales por actividad, no por entregable. Las 16 h presenciales caben en 3 jornadas de 6, 6 y 4 h: dato interno, el deck no cuenta sesiones ni jornadas (§4.23).
- No se nombra a Fasto (decisión de Ivana, 09/11/2026): el deck dice «un proyecto anterior del grupo», «otras empresas del grupo» y «el equipo de TI del grupo». Tampoco se nombra a Polar (proveedor de ejemplo del ciclo real, y cliente de Intezia: «un proveedor») ni a las personas (Alejandro, socio del grupo, patrocinio: «la dirección»).
- VPN: Ivana pidió dejar «VPN estable» como requisito del cliente en el deck (09/11/2026). Va sin explicar el riesgo ni prometer acceso a Claude desde Venezuela (regla de memoria). Riesgo interno: el bloqueo de acceso a Claude no es nuevo pero puede endurecerse el día 12; mitigación: VPN a nivel de red, tareas programadas antes de la visita y sin conexiones nuevas durante ella.
- Supuestos de las 26 h de construcción (internos): Vilches se puede conectar de forma directa y el envío por WhatsApp usa una ruta sencilla. Si no, las alternativas son una exportación programada de Vilches o un archivo de importación para Estelar. Otros riesgos: escrituras erróneas (validación humana y registro de cada acción) y calidad de datos (mínimos desactualizados, códigos duplicados y productos sin proveedor); la depuración de datos está fuera de alcance.
- Licencias de Claude aparte y cuenta con el dominio de la compañía dentro de su Claude Team: requisito del cliente, en el deck. Presupuesto separado del de Fasto (el deck dice «otros proyectos del grupo»). Acompañamiento 30/60/90 como postservicio: seguimiento por defecto de Habilidades.
- Impacto (cuadro de «Lo que se llevan»): enfoque «operación», elegido por Ivana (09/11/2026): errores, tiempo y control, sin hablar de personas ni de nómina.
- Hoja de ruta posterior sin precio (Recepción y Costeo y márgenes, con la meta de bajar el lead time de 24 a 12 horas) y requisitos del cliente: dos páginas «Requisitos y hoja de ruta» después de la ruta (opción respuesta_solicitud). Sin facilidad de pago (omitida): decisión mía por ser lo que se ha pedido en las últimas propuestas; confirmar con Ivana.
- Sin sesiones ni horas de trabajo internas (§4.23): el deck dice «horas con el equipo». Herramienta: Claude (nombrada por Ivana). No se afirma que migren de stack (§4.11).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Confirmar con Ivana el reparto de testeo y adopción entre las seis piezas (los totales de 8 y 8 son de ella) y que se omite la facilidad de pago.
- Valor, descuento y total: campos vacíos para ventas; moneda en REF con la leyenda de pago.
- Confirmar con Superfina quién es el responsable dedicado al 100 %, quiénes son los 2 compradores y el contacto de TI.
- Validar con el equipo de TI del grupo y con el proveedor de Estelar la ruta de escritura y la conexión directa de Vilches (si no, exportación programada o archivo de importación).
- Vigilar el acceso a Claude desde Venezuela antes de la visita presencial (riesgo del día 12): mitigación interna, no va al deck.
- Nombre completo y cargo de quien decide en Superfina, y fechas de la visita presencial (3 jornadas).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py superfina-cai092      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh superfina-cai092             # verifica, genera el PDF y ajusta los campos
```
