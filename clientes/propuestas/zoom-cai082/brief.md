# Brief · Zoom · Servicio de Habilidades (CAI-082)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Zoom
- **Slug**: `zoom-cai082`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-082`), presentada al cliente como **propuesta de proyecto**; formato compacto de 7 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Servicios de Zoom (tarifas, tracking, estatus de envío y creación de guías) disponibles para agentes de IA mediante un servidor MCP construido junto al equipo de TI, en ambiente de pruebas
<!--auto:inicio-->
- **Alcance**: 6 entregables en 5 bloques · 40 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Plan piloto de monitoreo proactivo v2 (25/10/2026), sección 07 (frente paralelo de servicios vía MCP), y correos de María Iribarren y de Zoom (26/10 al 03/11/2026), más instrucción de Ivana del 03/11/2026: CAI-082, contacto María, solo la parte del MCP
- **Fuente del insumo**: Plan piloto de monitoreo v2 (25/10/2026) y correos entre María Iribarren y Zoom (26/10 al 03/11/2026); sin Ficha de Levantamiento ni transcripción
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (03/11/2026): propuesta CAI-082 para Zoom, contacto María Iribarren (directora comercial), con la instrucción «solo coloca la parte del MCP». Educación y sin alianza (según la cuenta de Zoom), 40 h y sin facilidad de pago: **defaults míos** (la pregunta de confirmación se canceló); por confirmar. Insumos: plan piloto de monitoreo v2 (25/10/2026, sección 07) y los correos del 26/10 al 03/11; sin Ficha ni transcripción.
- Alcance: solo la construcción del MCP, como la plantea María («construirlo nosotros junto a tu equipo en las mismas sesiones de consultoría, de modo que el trabajo quede hecho mientras ellos aprenden»). El piloto de monitoreo, Collectio, legitimación de capitales, la proyección de recursos y la hoja de ruta 2027 quedan fuera: no se nombran en el deck. El monitoreo depende del levantamiento con el equipo (la semana próxima) y no se cotiza todavía.
- Horas: 40 h de la prueba de concepto del plan (con las llaves de API actuales; un OAuth completo suma 15 h o más, fuera). El plan las llama «esfuerzo estimado» (horas internas); aquí se tratan como horas junto al equipo de TI, como dice María (se construye en las mismas sesiones). Si son horas internas de Intezia, hay que quitarlas del deck (regla de Ivana). **Reparto mío:** diseño 6 h, consultas 14 h, creación de guías 8 h, bot de prueba 4 h, documentación 5 h y traspaso 3 h.
- Del plan (sección 07): servidor MCP en pruebas con tres herramientas de consulta (tarifas, tracking y estatus) y una de creación (guía); el bot de prueba simula a un comercio externo; documentación y guía para agregar servicios (por ejemplo el cambio de dirección por webhook que ya arman). Tres condiciones: API con documentación OpenAPI y ambiente de pruebas, autenticación con las llaves de API actuales y creación solo en pruebas con confirmación previa y protección contra duplicados.
- Sin semanas, sesiones ni fechas (§4.23): el plan dice 3 a 4 semanas y en paralelo al monitoreo; el deck no lo muestra. Sin retorno (`omitir: retorno`): una prueba de concepto no tiene datos para medir horas recuperadas; el valor es la capacidad de ofrecer servicios por MCP. Seguimiento 30-60-90 estándar, con ítems míos.
- Herramientas: Cursor es la que TI ya adoptó (CAP-077) y el bot de prueba es el Grok Bot del plan, que el deck llama «bot de prueba» (producto en beta, solo con datos de prueba). Zoom usa solo Gemini como herramienta de IA (Operaciones): el deck no nombra Claude, Gemini ni Vertex AI y no promete que un modelo concreto consuma el MCP. Sin precios de licencias (no verificados).
- Marca: Brand Kit v2.1 (amarillo #FFD300, Poppins), como en INN-006, porque Ivana lo dio para las propuestas de Zoom; el logo sigue siendo el del repo (falta el logo v2). No van los nombres de personas de Zoom (Ricardo, Carlos) ni el feedback textual. NDA obligatorio (Zoom lo pidió): se menciona en «Cómo cuidamos tus datos», no en los pasos de arranque.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Sin slide de retorno (`omitir`): confirmar con ventas que aquí no aplica (charla, sesión única); si el cliente es directivo, el retorno estimado es lo que decide.
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Confirmar con Ivana: Educación y sin alianza, 40 h, sin facilidad de pago, y que se aplica el Brand Kit v2.1.
- Confirmar si las 40 h son horas junto al equipo de TI o horas internas de Intezia (en ese caso se quitan del deck).
- Confirmar con Zoom las tres condiciones: API con OpenAPI y ambiente de pruebas, llaves de API actuales y creación solo en pruebas.
- Confirmar con Ivana si el bot de prueba se nombra como Grok Bot y si Cursor va en la tarjeta de licencias.
- Valor, descuento y total: campos vacíos para María (el plan dice que el valor final lo define la CCO).
- Decidir si el deck menciona el piloto de monitoreo como siguiente paso (hoy solo «más servicios por MCP»).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py zoom-cai082      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh zoom-cai082             # verifica, genera el PDF y ajusta los campos
```
