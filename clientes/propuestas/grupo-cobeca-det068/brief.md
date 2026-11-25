# Brief · Grupo Cobeca · Servicio de Detección (DET-068)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Grupo Cobeca
- **Slug**: `grupo-cobeca-det068`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-068`); formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Nivelar en IA al personal del Centro de soporte y de Capital humano, auditar sus procesos con las licencias de Microsoft 365 con Copilot y la consola de N8N que Grupo Cobeca ya tiene, y dejar logros inmediatos, un mapa de oportunidades y una hoja de ruta para incorporar automatización e IA con atención humanizada
<!--auto:inicio-->
- **Alcance**: 5 áreas (Centro de soporte, Capital humano · Selección, Capital humano · Nómina, Capital humano · Desarrollo, Capital humano · Administración) · 20 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · logros inmediatos cuando el proceso lo permite, sin cifra
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Resumen de Ventas de la primera reunión con la gerencia corporativa de tecnología de Grupo Cobeca (contacto que Keiber conoció en el IA TechDay), más instrucciones de Ivana (24/11/2026): propuesta DET-068 de Detección con María Iribarren como directora comercial, junto a la CAI-120
- **Fuente del insumo**: Resumen de Ventas de la reunión con Grupo Cobeca (24/11/2026); sin ficha ni transcripción
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (24/11/2026): dos propuestas para Grupo Cobeca, CAI-120 (Habilidades) y DET-068 (Detección), con María Iribarren como directora comercial. Insumo: resumen de Ventas de la reunión del mismo día; sin ficha ni transcripción. Contacto: el gerente corporativo de tecnología, que conoció a Keiber en el IA TechDay (no se nombra en el deck).
- Decisiones de Ivana (24/11/2026): 20 h de levantamiento (5 departamentos × 4 h: Soporte y las cuatro subáreas de Capital humano, cada una por separado); impacto «reenfoque»; viáticos y modalidad en texto (presencial en Maracaibo con viáticos aparte, o virtual). Educación y sin alianza son supuestos míos. Sin facilidad de pago (regla permanente).
- Áreas como las nombra el cliente: Centro de soporte (unas 8 personas, soporte a 81 farmacias, 4 centros de distribución y el centro corporativo; usan Jira) y Capital humano (15 a 20 personas en 4 o 5 subáreas: selección y captación, nómina, desarrollo y gestión administrativa; se tomaron 4). Lo que el cliente quiere (agente o chatbot de primer nivel con predictibilidad y analítica, y buen uso de Copilot y N8N en Capital humano) guía la conversación pero no es estructura ni se promete.
- El cliente ya trabaja con otra consultora de IA en otras áreas y pidió no desvirtuar ese trabajo: la propuesta entra solo por Soporte y Capital humano y lo dice como «las áreas que ya trabajan con IA no se tocan», sin nombrar a nadie. Se nombran Microsoft 365 con Copilot y N8N porque el cliente pidió apoyarse en esas licencias y en su consola; no se pre-recomienda otra herramienta ni se nombran Claude ni Google.
- Ecosistema declarado (no va completo en el deck): Microsoft 365 con Copilot como IA corporativa, Google Cloud para modelos avanzados, una consola corporativa de N8N y Jira/Atlassian. Estructura de datos con Data Stewards, Data Owner y Product Owner.
- Nivelación de 2 h (interna, un solo grupo): el personal de las dos áreas suma 23 a 28 personas, así que si pasa de 25 serían dos grupos (4 h); confirmar la lista. Sin semanas ni fechas (§4.23): el cliente prefiere arrancar en enero o febrero de 2027 (no antes de las vacaciones; los laboratorios que los surten cierran del 15 de diciembre al 15 de enero), y eso se acuerda en el arranque.
- Caso de nómina contado en la reunión (pagos de más por cálculo manual; 2 días a 15 minutos) es de otro cliente de Intezia y no va en el deck (no se nombran otros clientes). El cerebro digital que se le mostró queda como posible paso para 2027 y no va en estas propuestas.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Detección (`plantillas/deteccion-compacto.md`, Keiber 2026-10-08): sin frentes ni áreas prioritarias antes de detectar (lo que el cliente señaló como interés guía la conversación, no la estructura); cada departamento por separado, con su líder y su mano derecha, sin tarea previa; horas en global, sin reparto por área; logros inmediatos cuando el proceso o el área lo permite, sin decir cuántos; entregables nombrados, sin conteos.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Valor, descuento y total: campos vacíos para Ventas. Viáticos a Maracaibo: se cotizan aparte; si coincide con un viaje ya previsto a Maracaibo, mejor.
- Confirmar con Ivana el reparto de las 20 h entre los 5 departamentos y si Capital humano son 4 o 5 subáreas.
- Confirmar la lista del personal y los grupos de nivelación (23 a 28 personas), y quién lleva cada departamento.
- Confirmar con María si el correo y teléfono de la última slide siguen vigentes (tomados de la memoria del sistema).
- Educación y sin alianza son supuestos míos: confirmar.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py grupo-cobeca-det068      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh grupo-cobeca-det068             # verifica, genera el PDF y ajusta los campos
```
