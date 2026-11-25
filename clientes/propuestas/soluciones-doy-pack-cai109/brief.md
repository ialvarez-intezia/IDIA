# Brief · Soluciones Doy Pack · Servicio de Detección y Habilidades (CAI-109)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Soluciones Doy Pack
- **Slug**: `soluciones-doy-pack-cai109`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-109`), presentada al cliente como **propuesta de proyecto**; formato compacto de 9 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Detectar con las tres gerencias los procesos de Ventas y Mercadeo y de Administración, nivelar al equipo en IA y construir con él un agente conectado a Instagram (n8n y API de Meta) que atiende y deriva clientes, y apoyo en cotizaciones, cuentas por pagar, facturas y históricos
<!--auto:inicio-->
- **Alcance**: 9 entregables en 3 áreas · 41 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Respuesta a la solicitud (1) · 6 Entregables · 7 Retorno · 8 Inversión · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Soluciones Doy Pack (Flavia Martínez, registrada el 19/11/2026) y resumen de la reunión con las gerencias pegado por Ivana el 20/11/2026. Sin transcripción: pendiente de recibir
- **Fuente del insumo**: Ficha de Levantamiento (19/11/2026) y resumen de la reunión de Flavia Martínez con las gerencias. Sin transcripción
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (20/11/2026): propuesta CAI-109 para Soluciones Doy Pack con Flavia Martínez como asesora, a partir de la Ficha (19/11/2026) y del resumen de la reunión que pegó Ivana. No hay transcripción: la Ficha y ese resumen son la fuente (§4.23).
- Decisiones de Ivana (20/11/2026): el agente de Instagram va **conectado a Instagram** y, en un segundo mensaje, **25 h de construcción para el agente** porque debe hacerse con **n8n y la API de Meta**; impacto **reenfoque**; y una **hoja extra de gobernanza de datos dentro de la propuesta** (no un PDF aparte), como lámina adicional «Gobernanza de datos». Total **41 h** = detección previa 6 h + fundamentos 2 h + construcción 33 h (agente 25 h + compras y cuentas por pagar 8 h). Ivana había elegido antes 24 h (construcción 16 h, el tope de Flavia). Si las 25 h debían cubrir toda la construcción (6 + 2 + 25 = 33 h), basta bajar las 8 h de compras. División Educación y alianza = no: tomados por mí (primer contacto), no los dio Ivana.
- Combo: la Detección previa va dentro del mismo proyecto como paso previo, con la plantilla de Habilidades y `servicio_rotulo` «Servicio de Detección y Habilidades» (como CAI-032). `meta.json` queda en habilidades (código CAI y servicio de interés de la Ficha). Una sola hoja de inversión con tres tramos descritos (no `inversion.partes`: solo si Ivana lo pide).
- Reparto de horas (decisión mía a partir de lo que dijo Flavia e Ivana): detección previa 6 h = reunión central 2 h + 2 h en Ventas y Mercadeo + 2 h en Administración y Almacén; fundamentos 2 h (el «paso cero» de Lady); construcción 33 h = agente de Instagram 25 h (atiende y califica 8 h, flujo en n8n con la API de Meta 10 h, derivación al área del grupo y pruebas 7 h) + compras y cuentas por pagar 8 h (cotizaciones y lista 4 h; facturas e históricos 4 h). El calendario (sesiones de 2 h) va al kickoff, no a la propuesta (§4.23).
- Agente de Instagram conectado con **n8n y la API de Meta** (Ivana, 20/11/2026): se nombran en «Cómo trabajamos», el entregable y la inversión. La viabilidad (cuenta de Meta para empresas, permisos y aprobación de la API, dónde se aloja n8n) no está validada: el deck dice que se confirma en la Detección previa, antes de comprometer la construcción. n8n y la cuenta de Meta quedan fuera de la inversión. Con 25 h esta parte es más desarrollo que formación: alinear con Flavia cómo se lo presentó al cliente (construcción en conjunto).
- Quedan fuera (siguiente etapa): conexión directa al banco (se les dijo que hoy no es posible), conciliación automática, informes de indicadores, flujo de caja e inventario. Flavia nombró «indicadores e inventario» como fase 2 y el pedido original incluía informes de indicadores y flujo de caja: confirmar que el flujo de caja también pasa a la fase 2. Reemplazar los sistemas administrativos y el Excel (expectativa de la Ficha) queda fuera: la IA se apoya en ellos.
- Herramienta de IA sin nombrar: la Detección previa la confirma. Hoy usan Gemini gratuito y Claude gratuito (se agotó el límite), sin licencias. No se pre-recomienda ninguna, no se habla de VPN ni se garantiza nada sobre las cuentas (Claude no está soportado en Venezuela).
- Gobernanza de datos (lámina adicional, `respuesta_solicitud`): responde lo que preguntaron las gerencias (filtración, VPN y Venezuela, separación entre cuentas) sin explicar la filtración que escucharon (no la conocemos) y sin prometer acceso ni seguridad. «Un espacio por empresa del grupo» y «sin cuentas compartidas» son reglas de diseño mías: confirmar con Ivana.
- Participantes: 3 gerencias más 2 o 3 analistas (compras y administración, y mercadeo); la Ficha dice que podrían sumarse hasta 3 personas más. El número exacto está sin cerrar. Mary insistió en que los agentes son sobre todo para los analistas. No se nombra a ninguna persona del cliente.
- Sin citas ni dolor dramatizado: los hechos de la portada son datos de la Ficha parafraseados (6 solicitudes al día, ~3 h por conversación que no califica, cotizaciones a mano, históricos en carpetas). Las 6 solicitudes y las 3 h son cifras declaradas por el cliente, sin medir.
- Sin facilidad de pago (omitir: pago, regla permanente de Ivana). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23). Modalidad presencial en sus oficinas (Ficha). Las gerencias quieren que María Prin, quien decide y firma, esté en la presentación.
- Contacto de la última slide: Flavia Martínez, asesora comercial; correo y teléfono tomados de DET-060 y DET-061, no confirmados.

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

- Valor, descuento y total: campos vacíos para ventas. Moneda REF. Total de horas: 41 h (6 + 2 + 33).
- Viabilidad técnica de la conexión del agente a Instagram con n8n y la API de Meta (cuenta de Meta para empresas, permisos, alojamiento de n8n): se confirma en la Detección previa.
- Número exacto de analistas (2 o 3, o hasta 3 más) y de personas que participan.
- Confirmar que informes de indicadores, flujo de caja e inventario pasan a la fase 2.
- Qué herramienta de IA y qué plan se usan (la Detección previa la confirma); licencias a cargo del cliente.
- Revisar con Ivana la hoja de gobernanza de datos antes de presentarla (reglas de separación entre cuentas).
- Recibir la transcripción de la reunión y contrastarla con la Ficha (si se contradicen, manda la transcripción).
- Presentación: las gerencias quieren a quien decide y firma (María Prin) presente.
- Confirmar el teléfono y el correo de Flavia Martínez.
- Confirmar con Ivana si el programa lleva certificado.
- Confirmar con Ivana si las 25 h cubren solo el agente (41 h en total, como quedó) o toda la construcción (33 h).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py soluciones-doy-pack-cai109      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh soluciones-doy-pack-cai109             # verifica, genera el PDF y ajusta los campos
```
