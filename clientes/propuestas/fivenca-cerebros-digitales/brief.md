# Brief · Fivenca · Servicio de Habilidades (CAI-039)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Fivenca
- **Slug**: `fivenca-cerebros-digitales`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-039`), presentada al cliente como **propuesta de proyecto**; formato compacto de 10 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construcción guiada de Cerebros Digitales (asistentes personales) con Claude (Projects, Skills y conectores) y el conocimiento de cada persona organizado como grafo en Obsidian, para 1, 3 o 5 personas que Fivenca designe
<!--auto:inicio-->
- **Alcance**: 10 entregables en 5 Cerebros Digitales · 40 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Inversión (etapa 2) · 9 Inversión (etapa 3) · 10 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Instrucción directa del usuario del 06/10/2026 (5 Cerebros Digitales de 8 h cada uno, asesora María); base de contenido CAP-060 (Crea tu Clon Digital con Claude) y referencias de estructura CAI-027 y CAI-025. Versión 2 del 15/10/2026 (Ivana): tres hojas de cotización, para 1, 3 y los 5 cerebros (clones); pasada del formato compacto v1 al v3. Sin Ficha Comercial
- **Fuente del insumo**: Instrucción directa del usuario; contenido de CAP-060
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Versión 2 (Ivana, 15/10/2026): «ajustar la CAI-039 colocando 3 hojas de cotización para hacerlo para 1 clon, 3 clones y los 5». Son tres opciones alternativas, una hoja de inversión por opción (valor, descuento y total propios, campos vacíos para ventas), con `inversion.etapas`. «Clon» se leyó como Cerebro Digital (el nombre que usa el deck). El alcance, la ruta y los entregables muestran los cinco cerebros, que es el máximo; con 1 o 3 cada uno conserva sus 8 h.
- El deck enviado el 06/10/2026 era un compacto v1 (6 slides, con semanas y sesiones), formato que el generador ya no produce. Se rehízo en la plantilla v3 (CLAUDE.md §4.21 punto 6) y los archivos de la v1 quedaron en `_anterior-6-slides/`. Cambios por la v3: sin semanas ni sesiones (el calendario de 4 semanas y las 4 sesiones de 2 h por persona pasan al kickoff, CLAUDE.md §4.23); slides nuevas «Cómo trabajamos» y «Próximos pasos» con la asesora; «Facilidad de pago» omitida (`omitir: ["pago"]`); el retorno cambia «Hacia la semana N» por «a los 90 días del cierre». Se conserva todo lo demás: 8 h por cerebro, dos entregables de 4 h, seguimiento a 30, 60 y 90 días, retorno en modo método y la reunión de arranque de 1 h aparte.
- Horas por opción: 8 h con 1 cerebro, 24 h con 3 y 40 h con los 5, siempre 8 h por cerebro (excede en 2 h por cerebro la tarifa de referencia de 6 h, `empresa/politicas-comerciales.md`, caso CAI-025 y CAI-027; decisión del usuario del 06/10/2026). Las horas de cada hoja se escriben en su programa; cada una lleva su descuento y su total.
- Contenido (base CAP-060): cada Cerebro Digital es un «área» de 8 h con 2 entregables de 4 h: (1) Project de Claude y grafo en Obsidian (fundamentos, propósito, Project y grafo) y (2) Skill y automatización conectada. El reparto de las 8 h en los dos entregables es propuesta del sistema, por confirmar con servicio. Los antiguos «4 sesiones de 2 h» solo quedan como referencia interna para el kickoff.
- Tracks individuales (como CAI-025 y CAI-027): cada persona trabaja su cerebro por separado, no en grupo. Si Fivenca prefiere trabajo en conjunto, cambian las horas y el reparto.
- Sin facilidad de pago: el deck enviado no la llevaba y el usuario la omite por defecto. Con tres hojas, si se quiere, hay que definir cuotas por opción.
- Se quitó el certificado de participación (no va por defecto). CAP-060 y CAI-027 lo incluían: confirmar si Fivenca lo quiere.
- Sin Ficha Comercial: los hechos de portada son de contenido (cuántos cerebros, las 8 h, el grafo), no del cliente. Fivenca opera sobre Microsoft 365 y no usa Copilot: es contexto interno (CLAUDE.md §4.11) y el deck no afirma que adopte Claude ni que cambie de stack. Tampoco se menciona el acceso a Claude ni se promete VPN.
- Licenciamiento: cada persona necesita su cuenta de Claude con un plan que permita construir su cerebro. El deck no afirma un plan ni un valor de lista (no hay uno verificado) ni quién paga; va en las notas de cada hoja. Las hojas no llevan la tarjeta de licenciamiento porque `inversion.etapas` no convive con ella.
- Asesora: María Iribarren, la misma de CAP-062 y CAP-105 y de las otras propuestas de Fivenca; confirmar que es ella.
- Fivenca es un grupo financiero (servicios financieros y mercado de capitales): el deck pide autorización antes de cargar datos confidenciales o de clientes en un cerebro; la regla concreta la fija Fivenca.

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

- Definir inversión, descuento y total de cada una de las tres hojas (campos vacíos para ventas). La opción de 5 son 40 h, 10 h sobre la referencia de 6 h por cerebro (30 h).
- Confirmar la lectura de «clones» como Cerebros Digitales y que las tres opciones son alternativas (se elige una).
- Quiénes son las personas (1, 3 o 5) y si ya tienen cuenta de Claude. Si algunas vienen del grupo selecto de CAP-062 o de la directiva de CAP-105, ajustar los fundamentos.
- Fechas, modalidad y disponibilidad de cada persona: se acuerdan en la reunión de arranque (no van en el deck).
- Confirmar con servicio el reparto de las 8 h en los dos entregables y que la línea base del tiempo cabe en las primeras 4 h.
- Confirmar con Fivenca qué información de su trabajo puede cargarse en un cerebro, y si quieren certificado de participación.
- Si se quiere facilidad de pago, definir las cuotas por opción.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py fivenca-cerebros-digitales      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh fivenca-cerebros-digitales             # verifica, genera el PDF y ajusta los campos
```
