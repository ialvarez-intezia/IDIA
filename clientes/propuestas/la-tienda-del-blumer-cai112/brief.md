# Brief · La Tienda del Blúmer · Servicio de Habilidades (CAI-112)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: La Tienda del Blúmer
- **Slug**: `la-tienda-del-blumer-cai112`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-112`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Fortalecer al equipo de Sistemas de La Tienda del Blúmer para desarrollar con IA, conectar sus bases de datos y construir con cada área (Bodega y Compras, RRHH, Contabilidad, Tesorería y auditorías) las soluciones que reúnen la información en un solo lugar
<!--auto:inicio-->
- **Alcance**: 33 entregables en 7 áreas · 120 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana (22/11/2026): propuesta de Habilidades para La Tienda del Blúmer a partir del Informe Final de Auditoría y el Resumen Ejecutivo de la DET-020 (21/11/2026) y del plan de Habilidades que propone el consultor que atendió la Detección. Asesora: Verónica Rubio
- **Fuente del insumo**: Informe Final de Auditoría DET-020 (21/11/2026), Resumen Ejecutivo DET-020 y planteamiento del consultor para Habilidades (22/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (22/11/2026): propuesta de Habilidades CAI-112 para La Tienda del Blúmer, que ya pasó por la Detección DET-020 (Informe Final y Resumen Ejecutivo del 21/11/2026), más el planteamiento del consultor que la atendió. Asesora: Verónica Rubio. Sin Ficha nueva ni transcripción de la reunión de presentación del informe.
- Decisiones de Ivana: Educación y sin alianza; impacto «operación»; sin nombrar herramienta de IA ni tarjeta de licencias.
- **Ajuste del 23/11/2026 (Ivana)**: la clienta quiere ver reflejados los procesos de cada área y sus horas, para que la propuesta sea verificable contra el informe, con Habilidades para **todas** las áreas auditadas, tomando como referencia la propuesta de DUSA. Ivana pidió **quitar los Cerebros Digitales** y dejar las horas solo para desarrollar las habilidades. Se pasó de 5 a 7 áreas (Auditoría Interna y Cashea y Auditoría Externa son áreas propias; Tesorería se separó de las auditorías) y de 14 a 23 entregables.
- **Horas: 90 h en total, todas de Habilidades** (interpretación mía de «deja las horas solo para las habilidades»: se conserva el total de 90 h, antes repartido 60 h de áreas y 30 h de Cerebros). Reparto mío, a confirmar: Sistemas 24 h (7, 7, 4, 6); Bodega y Compras 12 h (5, 4, 3); Recursos Humanos 12 h (4, 3, 2, 3); Contabilidad 12 h (4, 6, 2); Tesorería 10 h (4, 3, 3); Auditoría Interna y Cashea 10 h (4, 4, 2); Auditoría Externa 10 h (4, 3, 3). Fases en el orden de la hoja de ruta del informe: Fase 1 Sistemas 24 h, Fase 2 Bodega, Compras y RRHH 24 h, Fase 3 Contabilidad, Tesorería y auditorías 42 h.
- **Retorno = horas que ganan, no horas de trabajo (Ivana, 23/11/2026)**: la clienta quiere ver lo que ahorra al optimizar cada proceso, como en DUSA, no cuánto se demora Intezia en cada uno. Se quitaron las horas por proceso, por fase y por área; solo queda el total de 90 h «con el equipo» en la hoja de inversión. La slide de retorno (modo `metodo`, sin costo hora) muestra por área las horas que se liberan según la Detección (Informe Final, logros e impacto del escenario): Tesorería 5 h a 1 h por día (80 h al mes); Auditoría Interna y Cashea 3 h por día en cada proceso (120 h al mes); RRHH 20 h a 5 h por analista y quincena (60 h al mes); Contabilidad 30 min por día en el libro de ventas y 12 h al mes en la conciliación (22 h al mes); Auditoría Externa 20 h a 7 h por ciclo (13 h al mes); Bodega y Compras 1 a 1,5 jornadas a 20 min más 2 o 3 h de revisión por factura (4,7 a 9,7 h al mes); Sistemas sin cifra. Total del informe: ≈300 a 305 h al mes, ≈3.600 a 3.660 al año, **escenario no medido**: el deck lo rotula «estimadas» y «sin medir». Son los logros de la Detección que esta propuesta consolida y lleva a uso sostenido; se medirán a 30, 60 y 90 días. No se usó `modo: cifras` porque exige costo hora validado y horas actuales por área que el informe no trae para todas.
- `por_fases: true` (alcance, ruta y entregables por fase, una columna por fase) porque la hoja de ruta del informe es secuencial. El generador avisa (⚠) de que ningún área es paso previo: es esperado.
- Los entregables salen del plan del consultor (desarrollo con IA, réplicas, requerimientos breves, solución centralizada, prueba de la venta al asiento) y de las fichas del informe: mapa de oportunidades (reporte de inventario contra ventas, base de importaciones, política de evidencia compartida), hoja de ruta (reglas de reposición, nómina, datos del SRH, contratos, criterios de asiento, soportes digitales, herramientas existentes, Interna/Cashea) y los «top 3 dolores» de cada área (Cashea sin número de orden, papel de Oriente, planillas de Interna tardías, dólares y bolívares en relaciones distintas, cola de transferencias). No se agregaron entregables fuera de esas fuentes; los de Auditoría Externa y de Interna y Cashea son más míos porque el informe solo dice «acompañamiento puntual».
- Sin nombrar herramienta (Ivana): no se menciona Claude ni Claude Code ni conectores MCP, aunque el plan del consultor los usa. Se dice «una herramienta de IA» (en el detalle de programa.md) y «conectores». No se menciona VPN (Venezuela no es país soportado).
- Las réplicas de bases de datos («mirrors») aún están en desarrollo por Sistemas: el deck no afirma que existan; el entregable es evaluar e implementar la conexión. La prueba de la venta al asiento contable se plantea como investigación («investigar si»), sin prometer que el punto de venta alimente automáticamente al sistema contable; no se nombra el sistema contable (§4.11).
- Sin nombres de personas del cliente (el informe nombra a líderes y analistas) ni de proveedores de servicios de pago. Las áreas se nombran como el informe (Auditoría Interna y Cashea, Auditoría Externa).
- Cerebros Digitales: quedan **fuera de esta propuesta** («se cotizan aparte»). El informe los recomienda para cinco responsables (líder de Sistemas, soporte y desarrollo, Recursos Humanos, Compras y Dirección). La versión anterior los incluía (30 h, 6 h cada uno) y quedó archivada en `_pdf-anteriores/`.
- Sin casos ya logrados (`metodo.ejemplos`): los logros de la Detección son del cliente pero el informe los rotula como escenario y varios están por contrastar; el deck no lleva fuentes. Se pueden agregar si Ivana lo pide.
- Retorno en modo método: la capacidad liberable de la Detección (≈300 a 305 h/mes) es un escenario no medido y no se carga como cifra.
- Hechos de la portada, del Informe Final: dos personas atienden Sistemas para áreas y tiendas; copias de la misma información; sistemas sin conexión acreditada con IA; el papel de Oriente puede tardar 20 días. No se cita la fuente en el deck.
- Fuera de alcance: Cerebros Digitales, marketing, gestión de clientes y comercio electrónico (sin levantamiento propio), la aplicación móvil para administradores de tienda (el informe la deja como candidato por levantar) y reemplazar los sistemas actuales.
- Modalidad «presencial en Valencia o en línea»: supuesto mío; se confirma en el arranque. Seguimiento 30-60-90 incluido por ser estándar de Habilidades. Sin facilidad de pago (omitir: pago). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23).

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

- Valor, descuento y total: campos vacíos para ventas.
- Confirmar con Ivana el reparto de las 90 h entre los 23 entregables y si se mantienen visibles las horas de cada entregable (y la excepción a §4.23).
- Confirmar con el consultor que el estado de las réplicas permite empezar la conexión en la fase 1 y que el plan de conectores aplica a todos los sistemas (el informe dice que no se presupone el mismo mecanismo).
- Confirmar con el consultor los entregables de Auditoría Interna y Cashea y de Auditoría Externa (el informe solo dice «acompañamiento puntual» para Interna y Cashea).
- Cerebros Digitales: propuesta aparte para los cinco responsables que recomienda el informe (30 h con el estándar de 6 h, si Ivana lo pide).
- Aplicación móvil para administradores de tienda: levantar con Sistemas y los usuarios de tienda; hoy fuera de alcance.
- Qué herramienta de IA se usa y quién contrata las licencias (se define en el arranque).
- Quién de cada área participa y si el trabajo es presencial en Valencia o en línea.
- Confirmar el teléfono y el correo de Verónica Rubio (tomados de propuestas anteriores).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py la-tienda-del-blumer-cai112      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh la-tienda-del-blumer-cai112             # verifica, genera el PDF y ajusta los campos
```
