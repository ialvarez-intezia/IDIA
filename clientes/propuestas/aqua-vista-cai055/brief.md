# Brief · Aqua Vista · Servicio de Habilidades (CAI-055)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Aqua Vista
- **Slug**: `aqua-vista-cai055`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-055`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Agentes de IA con Claude para atención por WhatsApp, mercadeo, reclutamiento y un Consejo Ejecutivo, construidos con el equipo de Aqua Vista para que aprenda a ajustarlos y mantenerlos
<!--auto:inicio-->
- **Alcance**: 10 entregables en 4 áreas · 40 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Inversión (etapa 2) · 9 Inversión (etapa 3) · 10 Inversión (etapa 4) · 11 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Aqua Vista (Flavia Martínez, 15/10/2026), contexto de la asesora sobre la reunión con el cliente e instrucciones de Ivana del 16/10/2026: CAI-055, Educación, asesora Flavia, horas por la regla general (40 h), hoja de cotización única sin facilidad de pago ni valor por parte, licenciamiento con Claude Team estándar, sin casos ya logrados, sin nombrar a Jean, Innovación solo como paso siguiente, presencial. Sin transcripción de la reunión
- **Fuente del insumo**: Ficha de Levantamiento de Aqua Vista (Flavia Martínez, 15/10/2026) y contexto de la asesora; sin transcripción de la reunión
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (16/10/2026): CAI-055 para Aqua Vista (posadas, turismo y hotelería, menos de 50 empleados). Educación, asesora Flavia Martínez, alianza «no» (no lo dijo; se infiere de un cliente nuevo y de las demás propuestas de Flavia; por confirmar). Servicio Habilidades puro: la ficha dice «servicio netamente de Habilidades».
- Horas por la regla general de Habilidades (8 a 12 h por área; Ivana: «me gusta la regla general»). Se tomó el reparto que se le propuso y ella no objetó: Atención 10 h, Mercadeo 12 h, Recursos Humanos 8 h y Consejo Ejecutivo 10 h, 40 h en total. Dentro de cada área, 2 h de levantamiento previo para delimitar cada agente (la ficha pide «levantamiento previo para delimitar cada agente») y el resto de construcción: Atención 8 h, Mercadeo 3 + 3 + 4 h para sus tres agentes, Recursos Humanos 6 h y Consejo 8 h. Ese reparto interno lo decidió el sistema; Ivana lo puede ajustar.
- Mercadeo: la ficha dice «dos o tres agentes, según lo que salga del levantamiento». Se cotizaron tres (Instagram, analista de mercado y creación de contenido). Si el levantamiento muestra que bastan dos, las horas se reasignan en el kickoff sin cambiar el total del área.
- Instagram: el cliente ya paga una herramienta para responder comentarios. El deck dice que el agente propio se construye solo si cuesta menos que esa herramienta, y no la nombra (la ficha dice «WeChat», por confirmar).
- Hoja de cotización única, sin facilidad de pago ni valor por parte (Ivana: «el plan total en una sola hoja, sin financiamiento ni partes del lado izquierdo»). El cliente había pedido «plan total con valor para decidir si van por partes»; se atiende con el valor total y el desglose de horas por área en el deck, sin `inversion.partes`.
- Seguimiento 30-60-90: se deja (la ficha pide medir «a 30-60-90»). Ivana solo dijo «sin financiamiento»; si no lo quiere, se quita con `seguimiento.tipo`.
- Licencias (Ivana: proponer Claude Team estándar). Valores de lista verificados el 16/10/2026 en support.claude.com: el plan exige un mínimo de dos miembros (justo las dos personas de Aqua Vista); puesto estándar USD 25 al mes pagando mensual o USD 20 pagando por año; incluye Claude Code. Cada puesto estándar trae USD 20 al mes en créditos de la Plataforma Claude (tope de USD 500 por equipo), que sirven para conectar agentes a sus aplicaciones y vencen cada mes; si se agotan, el uso se detiene hasta el mes siguiente o se compran más. Flavia había hablado de «20 a 50 USD por puesto»: no cuadra con la lista (el estándar cuesta 20 a 25 y el premium 100 a 125), y por eso el deck usa el valor de lista con su fecha.
- Costo operativo (la ficha dice que preocupa tanto como el valor del servicio): el deck muestra las licencias y cómo se estima el consumo, pero no un monto, porque no hay volumen de mensajes ni de uso. Se agregó la nota de que cualquier otra herramienta de terceros que el levantamiento requiera (por ejemplo, la conexión con WhatsApp Business) se informa con su valor de lista antes de construir. Esa nota la agregó el sistema. En el deck se escribe «gasto de operar» y no «costo» (el verificador tolera «costo» solo para el costo interno del cliente).
- WhatsApp Business e Instagram: no se pudo validar con una fuente oficial de Meta qué se puede conectar desde Venezuela (un proveedor dice que la API de WhatsApp Business sí está disponible; de Instagram no hay confirmación). Para no comprometer integraciones ni plazos, el deck dice que las conexiones se confirman en el levantamiento de cada agente. Ficha: la API de TikTok no funciona desde Venezuela y Meta no está validada; TikTok no se nombra.
- Acceso a Claude desde Venezuela: Ivana no respondió la pregunta. Se aplica el criterio de Simple TV y Go Pharma: el deck no lo menciona ni promete VPN. Sigue siendo un riesgo real para agentes en producción sobre Claude: ver la memoria claude-no-soportado-en-venezuela-no-prometer-vpn.
- Casos ya logrados: Ivana dijo «omite eso». Se omite el caso de Hotel Eurobuilding que citó Flavia para el filtro de currículos: no hay documento en el repositorio y la regla pide fuente del propio cliente. Tampoco se menciona la skill del Consejo Ejecutivo de Jean ni a Jean (Ivana: «sin nombrar a Jean»). El consejo se describe solo como tres consejeros y un presidente con perfiles definidos por el dueño, construido con Claude Code. Falta confirmar si la skill de Jean existe para reutilizarla.
- Innovación como paso siguiente (Ivana: «sin cotizar ni evaluar ni comprometer»): control de egresos, dashboard, conexión de los agentes con la plataforma de reservas y el consejo en vivo. Se menciona como siguiente paso, sin valor, sin plazo y sin decir que se evaluará. La idea del consejo en vivo por video o Meet es del cliente y la ficha dice que hay que ver si se puede gestionar.
- Plataforma de reservas: está en construcción (nube) y las posadas validan en Excel, así que la fase 1 no depende de ella ni se conecta a ella; va en el fuera de alcance. No se menciona su inestabilidad.
- Gmail en reclutamiento: la ficha dice que la conexión para contactar a los candidatos «se evalúa sobre la marcha, de ser posible». Va en el detalle del agente como algo que se evalúa al construir, no como entregable.
- Presencial (Ivana): el deck dice «en el lugar que se acuerde en la reunión de arranque» porque no se dijo la ciudad ni la sede. Las posadas están en varias ubicaciones.
- Persona o equipo: son dos personas (el dueño y el responsable de la plataforma, ambos ingenieros) que construyen; el resto del equipo entra después, con su filtro. El deck no las nombra: dice «las dos personas del equipo». El resto del equipo operativo de las posadas no participa en esta fase.
- Retorno en modo método, sin cifras: la ficha no trae volúmenes, tiempos ni valor de la hora. El objetivo del cliente es reducir la operatividad y aumentar la productividad sin contratar más gente; se plantea como posibilidad, nunca como compromiso.
- Portada sin datos de contratación evitada (no hay cifra con fuente). Los cuatro hechos son de la ficha, sin cifras ni citas.
- «Chairman» se escribe «presidente del consejo» (CLAUDE.md §4.4, sin anglicismos).
- Sin semanas, sesiones ni fechas (CLAUDE.md §4.23): la duración va en horas y el calendario se acuerda en la reunión de arranque. La ficha dice «duración y frecuencia: lo que sugiramos».

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

- Confirmar con Ivana o Flavia la división (Educación), la alianza (no) y el reparto de horas dentro de cada área.
- Conseguir la transcripción de la reunión: solo hay Ficha y el contexto de la asesora (CLAUDE.md §4.23). Si contradice la ficha, manda la transcripción.
- Valor, descuento y total: campos vacíos para ventas.
- Confirmar con Flavia o Jean si existe la skill del Consejo Ejecutivo para reutilizarla (sin nombrar a Jean en el deck).
- Validar con fuente oficial de Meta qué se puede hacer sobre WhatsApp Business e Instagram desde Venezuela antes del kickoff.
- Confirmar el nombre y el precio de la plataforma de pago que hoy responde los comentarios de Instagram: la regla del proyecto es construir el agente propio solo si cuesta menos.
- Definir la ciudad o sede de la modalidad presencial.
- Si el levantamiento requiere otra herramienta de terceros (conexión con WhatsApp Business, automatización), pedir su valor de lista para informarlo antes de construir.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py aqua-vista-cai055      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh aqua-vista-cai055             # verifica, genera el PDF y ajusta los campos
```
