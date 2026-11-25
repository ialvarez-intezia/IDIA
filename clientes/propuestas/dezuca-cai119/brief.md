# Brief · Dezuca · Servicio de Habilidades (CAI-119)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Dezuca
- **Slug**: `dezuca-cai119`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-119`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Ordenar la producción de Dezuca con ChatGPT: órdenes de pedido y pantalla simple por puesto, seguimiento y datos de cada pedido, control de inventario y compras, productividad, presupuesto contra real y un Cerebro Digital para la dirección
<!--auto:inicio-->
- **Alcance**: 6 entregables en 2 áreas · 16 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana (24/11/2026): propuesta CAI-119 de Habilidades para Dezuca a partir del resumen de Ventas de la primera reunión con el dueño (conocido en el IA TechDay) y lo que se le planteó; contacto: María Iribarren, directora comercial
- **Fuente del insumo**: Resumen de Ventas de la primera reunión con el dueño de Dezuca (23/11/2026); sin ficha ni transcripción
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (24/11/2026): propuesta CAI-119 de Habilidades para Dezuca, con María Iribarren como directora comercial. Insumo: resumen de Ventas de la primera reunión con el dueño (conocido en el IA TechDay); sin ficha ni transcripción. Propuesta prometida entre el martes 24 y el miércoles 25 de noviembre.
- Decisiones de Ivana (24/11/2026): Educación y sin alianza (confirmado); todo sobre ChatGPT, que el cliente ya tiene en plan Business, y por eso el deck lo nombra; los seis dolores en tres etapas, 80 h; impacto «operación»; una sola hoja de inversión, sin plan de pago (Ventas le anticipó al cliente pago por etapas en tres hitos: lo comunica Ventas).
- Reparto de horas mío (Ivana fijó 80 h): Órdenes y puestos 22 h (orden única 6, pantalla por puesto 10, acceso 4, prueba en planta 2); Seguimiento y datos 28 h (avance 6, línea de tiempo 8, datos por pedido 6, tablero 8); Inventario y compras 10 h (inventario 6, rendimiento y compra 4); Productividad y presupuesto 8 h (4 y 4); Cerebro Digital 12 h (contexto 6, informe semanal y alertas 6; tope del Cerebro Digital). Fases de 28, 28 y 24 h, que coinciden con los tres hitos de pago que anticipó Ventas.
- Los entregables salen de los seis dolores del dueño (órdenes por puesto, datos centralizados, inventario y compras, línea de tiempo del pedido, productividad por costurera y presupuesto contra real) y de las dos capas que le planteó Ventas (Cerebro Digital y pantalla por puesto). Productividad y presupuesto contra real van en la fase 3 porque dependen de los datos que generan los puestos.
- Aplicativo por puesto sin sonar a software a la medida: se presenta como «pantalla simple por puesto, construida en vivo con el equipo en ChatGPT», de dos toques (ver la orden y marcar el avance). No se nombra «GPT personalizado» porque OpenAI anunció que los retirará y los migrará a otro mecanismo (agentes del espacio de trabajo o plugins); el mecanismo exacto y cómo se registra cada marca (Drive, tabletas) se confirman en el arranque. El conector de Google Drive de ChatGPT Business permite acciones de escritura sobre Sheets (activas por defecto en Business), por verificar con el cliente.
- Sin nombre de personas del cliente (el deck no nombra al dueño ni al equipo). Se nombra ChatGPT por pedido de Ivana, igual que en el CAI-112 con los sistemas del cliente. No se menciona Claude. Cerebro Digital del dueño con información sensible solo para él y quien él decida (en «Cómo trabajamos»).
- Sin semanas, sesiones ni fechas (§4.23): horas de sesión en vivo, número de sesiones, fechas posibles y consultor asignado (que Ventas pidió a Servicio) viven en la reunión de arranque y en el Brief de Kickoff, que solo se hace si Ivana lo pide.
- Valor: Ventas proyectó un rango de 3.500 a 4.000 atado al retorno de inversión; no va en el deck (hoja de inversión con valores vacíos, en REF). Retorno en modo método: no hay horas ni volúmenes medidos del cliente. Sin certificado. Seguimiento 30-60-90 incluido por ser estándar de Habilidades.

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

- Valor, descuento y total: campos vacíos para Ventas (rango proyectado 3.500 a 4.000; el pago por etapas lo comunica Ventas). Ventas le dijo al cliente que la propuesta traería «el mapa de horas»: las 80 h están en la hoja de inversión y la ruta por fases, no por entregable.
- Confirmar con Ivana el reparto de las 80 h entre los 14 entregables de Habilidades.
- Consultor asignado, horas de sesión en vivo, número de sesiones y fechas posibles: se definen con el consultor y en el arranque, no van en el deck.
- Confirmar con el equipo técnico cómo se arma la pantalla por puesto en ChatGPT Business (mecanismo vigente tras el retiro de los GPT personalizados), cómo se registra cada marca y cuántos puestos y personas por puesto hay.
- Confirmar si el cliente quiere ver el plan de pago por tres hitos en el deck (Ivana lo omitió por la regla).
- Confirmar el teléfono y el correo de María Iribarren (tomados de la memoria del sistema).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py dezuca-cai119      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh dezuca-cai119             # verifica, genera el PDF y ajusta los campos
```
