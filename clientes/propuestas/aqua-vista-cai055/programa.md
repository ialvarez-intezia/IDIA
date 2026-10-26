# Programa interno · Aqua Vista · Servicio de Habilidades (CAI-055)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Aqua Vista (Flavia Martínez, 15/10/2026) y contexto de la asesora; sin transcripción de la reunión.

## 1. Resumen

- **10 entregables en 4 áreas**, **40 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Claude Team**: 10 entregables, 40 h.
- Horas por fase: F1 8 h (4 sol.) · F2 32 h (6 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Agentes y consejo de Aqua Vista | Claude Team | Atención al cliente, Mercadeo y redes sociales, Recursos Humanos, Consejo Ejecutivo | 40 | 10 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Levantamiento (delimitar el agente de cada área) | Uso (agentes y consejo construidos y en uso) |
|---|---|---|
| Agentes y consejo de Aqua Vista | 8 h · 4 sol. | 32 h · 6 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario y quién coordina el proyecto por Aqua Vista.
- **Levantamiento**: 4 áreas, 2 h cada una: cómo funciona hoy cada proceso y qué hará cada agente.
- **Agentes en uso**: Atención por WhatsApp, mercadeo, reclutamiento y el consejo, construidos con el equipo.
- **30 · 60 · 90 días**: Seguimiento: uso de los agentes, nuevas construcciones y tiempo recuperado.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Atención al cliente · 2 entregables · 10 h · Claude Team · línea A

Para qué (lo que ve el cliente): Atender por WhatsApp con tono humano y pasar a un vendedor a quien ya quiere reservar

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ATE-1 | Levantamiento de Atención al cliente (incluye: Las preguntas frecuentes y el tono de atención; Cuándo una persona pasa a un vendedor) | Trabajo de 2 h con el equipo. Se delimita el agente de atención: las preguntas frecuentes de los huéspedes, el tono cercano que se espera y el punto en que la conversación pasa a un vendedor para cerrar la reserva. Contexto del cliente: ya probó chatbots y los clientes los rechazaron, por eso el humano queda en el circuito. Entrega el alcance del agente. | - | - | - | 2 | F1 |
| ATE-2 | Agente de atención por WhatsApp con traspaso a vendedor (incluye: Responde preguntas frecuentes con tono cercano; Filtra y detecta quién ya quiere reservar; Pasa la conversación a un vendedor) | Trabajo de 8 h con el equipo. Se construye con él un agente que filtra y responde las preguntas frecuentes por WhatsApp con tono humano y, cuando detecta que la persona ya quiere reservar, la pasa a un vendedor que completa el ciclo de la reserva. El ojo crítico humano se mantiene: el cliente lo aceptó. Qué se conecta a WhatsApp Business se confirma en el levantamiento. Entrega el agente en uso. | - | - | - | 8 | F2 |

### Mercadeo y redes sociales · 4 entregables · 12 h · Claude Team · línea A

Para qué (lo que ve el cliente): Responder en Instagram, analizar el mercado y crear contenido, sin una persona dedicada

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| MER-1 | Levantamiento de Mercadeo y redes sociales (incluye: Qué hace hoy la herramienta que ya pagan; Cuáles de los tres agentes conviene construir) | Trabajo de 2 h con el equipo. Se delimitan los agentes de mercadeo (dos o tres, según lo que salga del levantamiento) y, en Instagram, se compara qué hace la herramienta que el cliente ya paga y qué haría el agente propio, que solo se construye si cuesta menos. Entrega el alcance de cada agente. | - | - | - | 2 | F1 |
| MER-2 | Agente de Instagram: comentarios y mensajes (incluye: Responde comentarios y mensajes; Redirige a los enlaces pertinentes) | Trabajo de 3 h con el equipo. Se construye un agente propio que responde comentarios y mensajes de Instagram y redirige a las plataformas o enlaces pertinentes, solo si su costo de operar es menor que el de la herramienta actual. Qué se conecta a Instagram se confirma en el levantamiento. Entrega el agente en uso. | - | - | - | 3 | F2 |
| MER-3 | Analista de mercado: tarifas, temporadas y feriados (incluye: Parte de la información que ya tienen levantada; Da recomendaciones y envía notificaciones) | Trabajo de 3 h con el equipo. Se construye un agente alimentado con la información que Aqua Vista ya tiene sobre las tarifas de la competencia, las temporadas altas y los feriados, para analizar las tarifas propias, dar recomendaciones y enviar notificaciones. Hoy ese análisis se hace a mano y toma mucho tiempo. Entrega el agente en uso. | - | - | - | 3 | F2 |
| MER-4 | Creación de contenido: imágenes y videos (incluye: Parte de la información de las posadas; Crea piezas de imagen y de video para redes) | Trabajo de 4 h con el equipo. Se construye un agente o skill con la información de las posadas que crea piezas de imagen y de video y automatiza ese proceso, porque hay posadas rentables que no alcanzan a pagar a una persona dedicada a las redes. Entrega la solución en uso. | - | - | - | 4 | F2 |

### Recursos Humanos · 2 entregables · 8 h · Claude Team · línea A

Para qué (lo que ve el cliente): Filtrar los currículos que llegan y devolver los 3 mejores perfiles para entrevistar

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| RRH-1 | Levantamiento de Recursos Humanos (incluye: Cómo se filtran hoy los currículos; Qué pide el equipo de cada perfil) | Trabajo de 2 h con el equipo. Se delimita el agente de reclutamiento: cómo se clasifican hoy los currículos y se agendan las citas con herramientas sueltas, y qué instrucción le da el equipo para cada perfil. Entrega el alcance del agente. | - | - | - | 2 | F1 |
| RRH-2 | Agente de currículos: los 3 mejores perfiles (incluye: Filtra y cualifica según la instrucción del equipo; Devuelve los 3 mejores perfiles para entrevistar) | Trabajo de 6 h con el equipo. Se construye un agente que filtra y cualifica los currículos que llegan según la instrucción del equipo y devuelve los tres mejores perfiles para entrevistar. La conexión con Gmail para contactar directamente a los candidatos se evalúa durante la construcción, de ser posible. Entrega el agente en uso. | - | - | - | 6 | F2 |

### Consejo Ejecutivo · 2 entregables · 10 h · Claude Team · línea A

Para qué (lo que ve el cliente): Un consejo de tres consejeros y un presidente con perfiles definidos por el dueño

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CON-1 | Levantamiento del Consejo Ejecutivo (incluye: Los perfiles estratégicos de cada consejero; Qué decisiones se llevan al consejo) | Trabajo de 2 h con el dueño. Se definen los perfiles estratégicos de los tres consejeros y del presidente del consejo, y qué decisiones se llevan a ese consejo, porque hoy el negocio no puede contratar asesores. Entrega los perfiles y el alcance. | - | - | - | 2 | F1 |
| CON-2 | Consejo Ejecutivo: tres consejeros y un presidente (incluye: Tres consejeros y un presidente con sus perfiles; Se trabaja por escrito, con Claude Code) | Trabajo de 8 h con el dueño y el responsable de la plataforma. Se construye, lo más robusto posible con los perfiles definidos, un consejo de tres consejeros más un presidente que asesora al negocio en sus decisiones, con Claude Code y por escrito. Entrega el consejo en uso. | - | - | - | 8 | F2 |

## 4. Fuera de alcance

- La plataforma de reservas de Aqua Vista: está en desarrollo, así que esta fase no depende de ella ni se conecta a ella.
- Conexiones con WhatsApp Business e Instagram: se confirman en el levantamiento de cada agente, sin compromiso previo.
- Control de egresos, dashboard y el consejo en vivo: van en otra etapa, según el resultado.
- Licencias y consumo de IA: van aparte de la inversión de cada proyecto, con su valor de lista en las notas de cada hoja.

## 5. Supuestos a confirmar (antes del método)

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
- Cotización por proyecto (reunión del 21/10/2026; pedido del cliente: «cotizar los proyectos por separado para entender la inversión de cada uno»): cuatro hojas de inversión, una por proyecto (Atención 10 h, Mercadeo 12 h con su analista de mercado, Recursos Humanos 8 h y Consejo Ejecutivo 10 h; 40 h en total), cada una con sus campos de valor, descuento y total vacíos (PrecioBase a PrecioBase_4). Cambia la hoja única anterior y la regla de «sin partes»: ahora lo pide el cliente. Sin facilidad de pago (Ivana, 21/10/2026).
- Licenciamiento: con cuatro hojas de inversión el bloque de tarjetas de licencias no se puede usar (comparte lugar con las etapas), así que el valor de lista de Claude Team (16/10/2026) va en las notas de cada hoja.
- Analista de mercado dentro de Mercadeo y redes (decisión del 21/10/2026, de la asesora): se descartó unirlo al Consejo Ejecutivo (propuesta del mismo día) porque habla el mismo idioma que el resto de mercadeo y deja el departamento de mercadeo completo (Instagram, analista de mercado y contenido); el Consejo Ejecutivo queda solo. Mercadeo vuelve a 12 h (2 de levantamiento, 3 de Instagram, 3 del analista y 4 de contenido) y el Consejo a 10 h (2 y 8); el total sigue en 40 h. El cliente puede ver Mercadeo como su departamento de mercadeo completo.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se levanta cada proceso para delimitar su agente; después se construye con el equipo, que aprende a ajustarlo y a mantenerlo sin depender de un proveedor externo.

- **Levantamos**: Cada proceso y lo que su agente debe hacer, con quien lo vive.
- **Construimos**: Con el equipo, cada agente, hasta dejarlo en uso.
- **Adoptamos**: El equipo opera, ajusta y mantiene los agentes por su cuenta.
- **Medimos**: El tiempo recuperado y el consumo, a 30, 60 y 90 días.

- En la práctica, **Una persona en el circuito**: Los agentes filtran y responden, y pasan a una persona cuando hace falta: un vendedor cierra cada reserva.
- En la práctica, **Gasto bajo control**: El equipo aprende a elegir el modelo y a medir el consumo de tokens, la unidad con que se factura la IA.
- En la práctica, **Solo si conviene**: En Instagram, el agente propio se construye solo si cuesta menos que la herramienta que ya pagan.
- Datos: Los datos de los huéspedes no se cargan a ninguna herramienta de IA sin la autorización de Aqua Vista; los criterios de uso seguro se acuerdan al empezar.
- Quién construye: Intezia construye junto a las dos personas del equipo, sobre los casos reales de las posadas, sin entregar un producto empaquetado.

**Logística:** modalidad: Presencial, en el lugar que se acuerde en la reunión de arranque. · participantes: Las dos personas del equipo de Aqua Vista que construyen y mantendrán los agentes. · ritmo: Dudas por escrito antes que en llamadas; el trabajo se agenda en el horario del equipo. · arranque: La fecha la fija Aqua Vista; una reunión de arranque de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con el agente; Horas recuperadas; Gasto de operar.

## 8. Próximos pasos (slide 11)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

