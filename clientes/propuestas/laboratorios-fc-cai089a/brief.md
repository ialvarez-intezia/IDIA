# Brief · Laboratorios FC · Servicio de Habilidades (CAI-089A)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Laboratorios FC
- **Slug**: `laboratorios-fc-cai089a`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-089A`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Aplicar IA con método en los procesos de las 9 áreas de Laboratorios FC, clave y de apoyo: levantar cada proceso y construir una solución por área, con seguimiento a 30, 60 y 90 días
<!--auto:inicio-->
- **Alcance**: 18 entregables en 9 áreas · 90 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Laboratorios FC (Verónica Rubio, 05/11/2026) y transcripción de la reunión del 05/11/2026 con Mariana Salcedo (Gerente de Tecnología). Estructura (levantamiento de 2 h y 8 h de ejecución por área) indicada por Ivana el 05/11/2026
- **Fuente del insumo**: Ficha de Levantamiento y transcripción de la reunión (05/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (05/11/2026): propuesta de Habilidades CAI-089 para Laboratorios FC, asesora Verónica Rubio. Aunque el cliente pidió Detección, Ivana decidió Habilidades por ser más atractivo para la directiva y porque hay procesos documentados: levantamiento de 2 h por área y 8 h de ejecución por área. Educación, sin alianza y sin facilidad de pago: confirmados con Ivana. Después pidió dos propuestas: A con todas las áreas y B con las áreas priorizadas, para que Mariana decida.
- Áreas: las 9 de la ficha. Procesos clave: Compras, Producción y operaciones (vía maquiladores), Ventas y comercialización, Despacho y logística. Procesos de apoyo: Finanzas, Gestión humana, Asuntos regulatorios, Tecnología y Mercadeo. La propuesta B toma los 4 procesos clave como áreas priorizadas: es mi lectura de la reunión («en mi opinión serían esos procesos clave», Mariana); confirmar con Ivana.
- Horas: 2 h de levantamiento (F1) y 8 h de ejecución (F2: 4 de construcción, 2 de testeo y 2 de adopción) por área, según Ivana; A = 9 áreas = 90 h (18 + 72); B = 4 áreas = 40 h (8 + 32). Son horas de encuentro con los equipos (sin_horas_trabajo). La solución de cada área no se define antes del levantamiento: por eso los entregables se llaman «Levantamiento de X» y «Solución de X, construida y en uso».
- Herramienta de IA: no se nombra. La ficha dice que aún no saben y esperan la recomendación; ya tienen licencias puntuales (Claude Enterprise para un grupo, una Pro) y usan gratuitas (Gemini, Perplexity); su ecosistema de oficina es Microsoft 365 con Power Automate. Tecnología quiere conocer n8n, Claude Code y Cursor: no se nombran en el deck. El deck dice «entre las que Laboratorios FC puede usar con sus licencias».
- Restricciones de OpenAI y Anthropic en Venezuela (el «12 de noviembre»): Mariana lo preguntó y la ficha pide una respuesta por escrito. El deck NO promete acceso ni VPN (regla del sistema) y no repite lo dicho en la llamada. Falta una respuesta verificada (consulta a Rebeca).
- Transferencia de conocimiento y autonomía de Tecnología (la pregunta clave de Mariana): se responde en «Cómo trabajamos» («el equipo queda con la capacidad de sostener y ampliar lo construido, tecnología incluida») y en el área de Tecnología.
- Detección o Habilidades: Mariana, como gerente de tecnología, prefería Detección y pidió que Intezia recomiende; Ivana eligió Habilidades con levantamiento por área. No se nombra Detección en el deck. Casos del sector (Laboratorios Farmac, Go Pharma) mencionados en la llamada: no se incluyen sin fuente documentada.
- Contexto interno que no va en el deck: presupuesto 2027 en formulación (ejecución probable en 2027), Junta de Presidencia decide (Mariana no), patrocinio tibio, 60 % de la plantilla es fuerza de venta en calle (de ahí «sin frenar la venta en calle»), sistema contable Profit, cadena de distribución con aplicación web propia. Sin fechas ni semanas en el deck (§4.23).
- Participantes: ~40-45 personas del personal administrativo (de ~120 en total), por áreas (gerentes, líderes, analistas, colaboradores); los líderes por área están por identificar. Modalidad mixta; sede en Caracas.

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

- Confirmar los códigos de las dos propuestas (CAI-089A todas las áreas, CAI-089B áreas priorizadas) y que B son los 4 procesos clave.
- Confirmar con Ivana el reparto (2 h + 8 h por área) y si las 8 h cuentan como construcción, testeo y adopción de 4, 2 y 2.
- Respuesta por escrito, verificada, sobre las restricciones de Claude y OpenAI en Venezuela antes de enviar (Mariana la pidió en la reunión).
- Valor, descuento y total: campos vacíos para ventas; moneda de facturación y la forma de pago la define el cliente.
- Vigencia de la cotización: el sistema usa 30 días y el cliente decide al formular el presupuesto 2027; ver con Ivana si se extiende.
- Quién asiste a la presentación (Junta de Presidencia) y si Mariana quiere a otros líderes; si trabajan con orden de compra.
- Identificar los líderes de cada área y si el programador o tecnología participa en todas las áreas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py laboratorios-fc-cai089a      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh laboratorios-fc-cai089a             # verifica, genera el PDF y ajusta los campos
```
