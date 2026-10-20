# Brief · Grupo Leti · Servicio de Detección (DET-034)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Grupo Leti
- **Slug**: `grupo-leti-det034`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-034`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Clasificar los casos de uso de IA de Grupo Leti según la solución que necesita cada uno (Copilot o automatización), con arquitectura sugerida, prioridades y logros inmediatos
<!--auto:inicio-->
- **Alcance**: 1 área (Casos de uso de Grupo Leti) · 12 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 0 h) · al menos 3 logros inmediatos
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Enviada` el 14/10/2026 (`meta.json`; convención «terminado = enviado», lo estampa el wrapper del PDF)
- **Insumos (CLAUDE.md §4.23)**: resumen de Flavia Martínez de su reunión con el responsable técnico de Grupo Leti y la ruta que ella propone (14/10/2026). No hubo Ficha de Levantamiento ni transcripción: lo que no está en ese resumen no se inventó. La estructura (Detección técnica acotada a los casos de uso, no por áreas) es la que propone Flavia y confirmó Ivana.
- **fecha_arranque_deseada**: no hay dato. Se define en el kickoff; la propuesta no lleva fechas, semanas ni sesiones.
- **resultados_esperados**: que cada caso de uso quede en su vía (Copilot o automatización) con arquitectura y prioridad, y algunos logros inmediatos en uso. Sin volúmenes ni tiempos del cliente, así que el retorno va en modo método y no se agrega ROI.

## Contexto del cliente (interno, no va al deck)

- **Quién es:** Grupo Leti. Su estrategia de IA está montada sobre Microsoft (Copilot, agentes y Azure) por seguridad de la información; el core operativo es SAP.
- **Contacto técnico (Elvis):** perfil técnico, lleva poco tiempo en la empresa y la gerencia está naciendo con él. Ya entregó unas cinco soluciones por su cuenta, su equipo no va a crecer y las áreas le piden ayuda. No necesita formación (su gente ya usa prompts y Copilot «como GPT»; quiere frenar la formación básica de Infraestructura): necesita más manos. Su visión: el funcional dibuja el proceso y su unidad, con aliados, lo construye (integraciones con APIs, procesamiento masivo de datos, orquestación de agentes y RAG, con una persona verificando el resultado). Es crítico del hype: «se fuerza un agente donde bastaba una automatización».
- **Mejor ángulo comercial:** ser el aliado que le dice con criterio qué sí y qué no hacer. De ahí las dos vías y el «sin forzar soluciones».
- **Lo acordado (Flavia):** enviar dos propuestas, una de Políticas (ya conectó: sus políticas de IA las hizo Ciberseguridad sin experto en IA y obligan a usar solo Copilot; lo discute con su director) y una ruta para la parte de construcción. Esta es la segunda: solo Detección. Agendar esta semana una sesión con él y alguien del equipo técnico de Intezia.
- **Sin otros servicios (Ivana, 14/10):** el deck es solo la Detección. No menciona Políticas, Habilidades ni Innovación, ni «la etapa que sigue». La construcción conjunta (Habilidades o Innovación, si aplica) la propuso Flavia para después y queda fuera de este deck.
- **Respuesta de Flavia tras hablar con el equipo (14/10):** el mejor ángulo es el criterio, ser el aliado que dice qué sí y qué no hacer. Lo construye Intezia: agentes en Copilot Studio, skills de Claude y, en RAG (asistentes sobre los documentos del cliente), también las integraciones que requiera, siempre con asesoría. n8n: Intezia es partner (su mejor carta) y forma y acompaña al equipo del cliente, pero no asume la construcción. Queda fuera: integraciones con SAP y orquestación compleja de agentes; se dice desde el inicio para no prometer de más, **a la espera de la lectura de David**. **Ivana (14/10): «nosotros no construimos»**, así que nada de lo que Intezia construye va al deck; esta línea es solo el contexto de Flavia.
- **Ruta que Flavia ve viable, con un ajuste:** separar la Detección de Habilidades. La Detección, acotada a su unidad, mide el alcance real, clasifica los casos (Copilot, automatización y una tercera vía de desarrollo que Ivana pidió quitar), entrega arquitectura sugerida y prioridades y, como el cliente ya tiene políticas de IA, también las mapea para alimentar la propuesta de Políticas. Este deck recoge lo de la Detección, incluido el mapeo de políticas, sin mencionar la propuesta de Políticas.

## Origen y fuente

- **Origen**: Resumen de la asesora (Flavia Martínez) de su reunión con el responsable técnico de Grupo Leti y la ruta de Detección técnica que ella propone, compartidos el 14/10/2026. Sin Ficha de Levantamiento ni transcripción
- **Fuente del insumo**: Resumen de la reunión con el responsable técnico, de la asesora (14/10/2026)
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Alcance pedido por Ivana (14/10/2026): solo una propuesta de Detección. No se incluyen la propuesta de Políticas (va aparte y esta no la menciona), ni Habilidades ni Innovación, ni la ruta completa de servicios; el deck termina en el Informe Final. Sin facilidad de pago (criterio de Ivana en las Detecciones recientes; el estándar sería 50 % al aprobar y 50 % con el Informe Final).
- Insumo: el resumen de Flavia de su reunión con el responsable técnico de Grupo Leti. No hubo Ficha de Levantamiento ni transcripción (CLAUDE.md §4.23): los tres dolores de la portada son lo que ella cuenta que dijo el cliente, sin nombres de personas.
- Estructura: Detección técnica acotada a los casos de uso de Grupo Leti, no por áreas (la ruta que propone Flavia). Por eso hay un solo «área» a auditar, «Casos de uso de Grupo Leti», sin departamentos ni nombre de la unidad (Ivana: «habla como Grupo Leti»). Las reglas de Keiber siguen: horas en global, al menos 3 logros inmediatos, entregables sin conteos, sin frentes prioritarios.
- Horas (elegidas por Ivana entre 8, 12 y 16): 12 h de levantamiento en global, sin nivelación (el equipo ya maneja prompts y usa Copilot, y la formación básica no es su prioridad) y arranque sin horas. Total interno: 12 h.
- Dos vías: lo que el usuario resuelve con Copilot y lo que se automatiza. Flavia proponía una tercera (lo que requiere desarrollo); Ivana pidió quitarla de toda la propuesta y no nombrar ninguna otra («deja Copilot o automatización», 14/10). «Copilot» se nombra porque es la plataforma del cliente (su estrategia se monta sobre Microsoft por seguridad de la información); no se nombran Copilot Studio, skills de Claude ni el caso de La Mundial, y no se pre-recomienda otra herramienta: la arquitectura sugerida sale del Informe Final. **n8n** se nombra a pedido de Ivana, solo junto a «automatización» (slide 2: «qué se automatiza con n8n»; slide 5: tarjeta «Casos clasificados»); no se dice que Intezia sea partner de n8n ni que forme o acompañe.
- Intezia no construye (Ivana, 14/10: «nosotros no construimos, nada de construir»). Se quitó del deck la tercera vía, la caja «Quién construye» de la slide 4 (`metodo.quien_construye` vacío; el generador se ajustó para permitirlo), el paso «Construimos» (ahora «Mejoramos»), «cómo construirlo» en la arquitectura y «qué construir primero» (ahora «por dónde empezar» y «qué atender primero»). Ivana permitió nombrar n8n: va junto a «automatización», no en una frase de quién construye.
- Fuera de alcance: integraciones con SAP y orquestación compleja de agentes («quedan fuera de esta propuesta»), licencias y cambios en SAP. Pendiente la lectura de David.
- Mapeo de las políticas de IA vigentes: píldora de la slide 2, tarjeta «Informe Final y hoja de ruta» y Programa de la inversión. No se menciona la propuesta de Políticas ni que el mapeo la alimente (Ivana: solo Detección).
- Logros inmediatos: son una regla de la Detección (al menos 3, CLAUDE.md §4.22) y el generador no deja ponerlos en cero. Como Intezia no construye, el deck los redacta sin construir: «mejoras en uso desde el primer día, identificadas con el equipo en el levantamiento». Decisión mía por confirmar con Ivana.
- «Revisión humana» en el método viene de lo que el cliente busca (que una persona verifique el resultado). El método sigue las prácticas de Keiber (sin tarea previa, sin forzar soluciones).
- No va al deck: el nombre del contacto, que lleva poco tiempo en la empresa, que la formación no es su prioridad, que sus políticas de IA las hizo Ciberseguridad sin experto en IA y obligan a usar solo Copilot (es el ángulo de la propuesta de Políticas), y su visión de que el funcional dibuje el proceso y su unidad lo construya (es la etapa de construcción, fuera de esta propuesta).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Detección (`plantillas/deteccion-compacto.md`, Keiber 2026-10-08): sin frentes ni áreas prioritarias antes de detectar (lo que el cliente señaló como interés guía la conversación, no la estructura); cada departamento por separado, con su líder y su mano derecha, sin tarea previa; horas en global, sin reparto por área; al menos 3 logros inmediatos en el proyecto (no uno por área); entregables nombrados, sin conteos.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Definir inversión, descuento y total (campos vacíos para ventas); línea de facturación (moneda y tasa) por confirmar con ventas. Decidir si lleva facilidad de pago (hoy se omitió).
- Confirmar la modalidad (presencial o virtual) y dónde: hoy el deck dice que se acuerda en el arranque.
- Lectura de David sobre lo que queda fuera de la propuesta: integraciones con SAP y orquestación compleja de agentes.
- Confirmar con Ivana qué son los logros inmediatos si Intezia no construye: hoy el deck dice «mejoras en uso desde el primer día, identificadas con el equipo en el levantamiento».
- Flavia pidió una sesión esta semana con el responsable técnico y alguien del equipo técnico de Intezia, antes de enviar.
- Si se quiere nombrar la unidad con su nombre oficial, hay que pedirlo: hoy el deck habla de Grupo Leti.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py grupo-leti-det034      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh grupo-leti-det034             # verifica, genera el PDF y ajusta los campos
```
