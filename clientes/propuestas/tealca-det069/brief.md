# Brief · Tealca · Servicio de Detección (DET-069)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Tealca
- **Slug**: `tealca-det069`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Servicio de Detección (`DET-069`); formato compacto de 9 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Nivelar en IA al personal de Servicio al Cliente y Mercadeo, auditar sus departamentos, y dejar logros inmediatos, un mapa de oportunidades y una hoja de ruta, con dos opciones de alcance para que Tealca decida cuánto abarcar
<!--auto:inicio-->
- **Alcance**: 2 áreas (Servicio al Cliente, Mercadeo) · 28 h de levantamiento en global, sin reparto por área (internas: arranque 0 h, nivelación 2 h) · logros inmediatos cuando el proceso lo permite, sin cifra
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Inversión (etapa 2) · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Resumen de Ventas de las conversaciones con la gerencia de Tealca (24/11/2026) y mensaje de la gerencia con los departamentos y su orden de prioridad, más instrucciones de Ivana (24/11/2026): propuesta DET-069 de Detección en dos opciones (A: las 7 subáreas por fases; B: los 4 departamentos), con María Iribarren como directora comercial
- **Fuente del insumo**: Resumen de Ventas y mensaje de la gerencia de Tealca (24/11/2026); sin ficha ni transcripción
- Las horas internas (arranque, nivelación y levantamiento) y el detalle de áreas, departamentos y etapas están en `programa.md`, generado desde `datos.json`.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (24/11/2026): propuesta DET-069 de Detección para Tealca, con María Iribarren como directora comercial. Insumo: resumen de Ventas, un primer mensaje (tres áreas) y un segundo mensaje de la gerencia que lo corrige: **dos áreas con siete subáreas** (Servicio al Cliente: Formación, Post Venta, Servicio a Tiendas y Centro de Contacto; Mercadeo: Mercadeo, Comunicaciones e Inteligencia de Negocio). Ventas y Operaciones quedan fuera por ahora; Recursos Humanos y Finanzas también (migran a Odoo, no va en el deck). Sin ficha ni transcripción.
- Decisiones de Ivana (24/11/2026): **modular en dos opciones, cada una con un valor único sin desglose**: Opción A, las siete subáreas «por fases por departamento» (28 h de levantamiento, 4 h por departamento) y Opción B, solo los cuatro departamentos prioritarios (16 h). Impacto «operación». Una sola opción se elige. Educación y sin alianza son supuestos míos. Sin facilidad de pago (regla permanente).
- Orden de prioridad que dio la gerencia (va aquí y no en el deck, porque la plantilla de Detección no lleva áreas prioritarias): 1 Formación (equipo que forma a los taquilleros a nivel nacional), 2 Inteligencia de Negocio, 3 Post Venta, 4 Mercadeo; luego Servicio a Tiendas, Centro de Contacto y Comunicaciones. La Opción B toma los cuatro primeros; la Opción A los hace en fases en el orden que se acuerde en el arranque.
- Datos de la reunión usados en la portada: comparar las tarifas con la competencia toma unos 2 días en Excel y lo hacen 2 personas (el resumen lo ubica en Mercadeo e inteligencia de mercado); muchos reportes de calidad de servicio para clientes corporativos (Servicio al Cliente); Formación forma de manera constante a los taquilleros a nivel nacional. «Skills para segmentar la presentación de ventas y responder consultas» (Ventas) queda fuera junto con el área.
- Ecosistema declarado (no va en el deck): Google Workspace con Gemini, y el equipo de tecnología ya usa Claude. La gerencia quiere conversar el tema de las licencias: se explicó que la decisión puede apoyarse en los datos de la detección, y el deck lo recoge en «Inversión inteligente en licencias». No se pre-recomienda herramienta.
- No se nombran personas del cliente (la gerente que pide la propuesta ni el director de tecnología). Sin semanas, sesiones ni fechas (§4.23): el resumen hablaba de auditoría de 5 a 15 días y de cronómetro; no van en el deck. Nivelación de 2 h (interna, un grupo): confirmar la cantidad de personas, si pasa de 25 serían dos grupos.

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

- Valor de cada opción (campos de la hoja de inversión vacíos para Ventas; un valor único por opción, sin desglose).
- Confirmar con Ivana si la Opción A lleva el orden de los departamentos en el deck (hoy no: «por fases» y el orden se acuerda en el arranque).
- Confirmar el personal de las dos áreas (para los grupos de nivelación) y quién lleva cada departamento.
- Educación y sin alianza son supuestos míos: confirmar.
- Confirmar con María si el correo y teléfono de la última slide siguen vigentes (tomados de la memoria del sistema).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py tealca-det069      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh tealca-det069             # verifica, genera el PDF y ajusta los campos
```
