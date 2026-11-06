# Brief · Fiat · Servicio de Habilidades (CAI-081)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Fiat
- **Slug**: `fiat-cai081`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-081`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Claude aplicado por la alta gerencia de Fiat (red automotriz de 21 concesionarios): nivelación estratégica y un entregable real por gerente, con el posicionamiento de la cuenta corporativa de LinkedIn como entregable de Mercadeo
<!--auto:inicio-->
- **Alcance**: 7 entregables en 6 líneas de trabajo · 28 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Fiat (Flavia Martínez, registro 02/11/2026; contacto de Mercadeo; decide el director general) y contexto de Flavia (03/11/2026), más respuestas de Ivana del 03/11/2026: CAI-081, Educación, sin alianza, 28 h, sin facilidad de pago
- **Fuente del insumo**: Ficha de Levantamiento (registro 02/11/2026) y contexto de Flavia Martínez (sin transcripción de la reunión)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (03/11/2026): propuesta CAI-081 para Fiat, asesora Flavia Martínez (correo y teléfono tomados de propuestas anteriores). Confirmados por Ivana: Educación, sin alianza, 28 h y sin facilidad de pago. Insumos: Ficha de Levantamiento (registro 02/11/2026) y el contexto de Flavia; no hay transcripción de la reunión. Empresa mediana con 21 concesionarios; primer contacto, referidos por su agencia de PR.
- Estructura (contexto de Flavia): la propuesta aborda a la alta gerencia completa, no un proyecto de LinkedIn (el director general no ve sentido en pagar una consultoría solo para posicionar la cuenta). Nivelación en Claude, un entregable real por gerente y LinkedIn como el entregable de Mercadeo. El deck no cita al director ni su objeción y no nombra personas.
- Horas (opción recomendada, elegida por Ivana): nivelación 6 h (la ficha sugiere 6 a 8 h) + levantamiento de la tarea de cada gerente 2 h + cinco entregables de 4 h (Administración, Comercial, Mercadeo con LinkedIn, Tecnología y Recursos Humanos) = 28 h con el equipo; reparto mío. Dirección General participa en la nivelación y no tiene entregable propio. El número de gerentes se confirma en la presentación (5 a 6 gerencias): si cambia, se ajusta 4 h por entregable. Sin horas de trabajo ni consultores.
- Licencias y acceso: Flavia pidió un bloque corto sobre licencias y acceso (plan, puestos, VPN corporativa desde Venezuela y qué información no se sube). **Por la regla de Ivana, el deck no promete ni menciona VPN** (Venezuela no figura en la lista oficial de países soportados de Claude): el bloque dice «cómo se accede según las condiciones del proveedor». La ficha anota que se recomendó VPN y cuenta centralizada; eso se trata en la sesión, no en el deck. Valor de lista de Claude Team al 02/11/2026: USD 25 al mes o USD 20 por año, mínimo 2 puestos; con seis puestos, USD 150 al mes.
- Sin Odoo ni desarrollos propios en el deck: se dejan fuera para no afirmar integraciones (Claude no se conecta a sistemas propios en esta etapa). Sin Detección. LinkedIn: Claude propone el contenido y el posicionamiento; el equipo de Mercadeo revisa y publica. El ejemplo del gerente de ventas (skill de análisis de la competencia) se dice como «posible», a confirmar con el gerente. Mercadeo queda abierto a otro contenido si lo piden.
- Hecho de la portada: de la ficha (nadie ha usado IA ni recibido formación; 6 a 7 personas en la alta gerencia). Sin cifras de la empresa ni estudios. Seguimiento 30-60-90 estándar y retorno en modo método, sin cifras inventadas. Sin pago, hoja de inversión única con campos vacíos para ventas (presupuesto en evaluación). Sin semanas, sesiones ni fechas (§4.23).

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

- Confirmar con Flavia el número de gerentes (5 a 6) y si Dirección General lleva entregable propio.
- Confirmar con Ivana el reparto de 28 h (nivelación 6, levantamiento 2, 4 por entregable).
- Confirmar que el bloque de licencias y acceso no menciona VPN (regla de Ivana) aunque Flavia la pidió.
- Confirmar la modalidad y las personas de Mercadeo para LinkedIn (se terminan de levantar en la presentación).
- Valor, descuento y total: campos vacíos para ventas.
- Confirmar el teléfono y el correo de Flavia Martínez (tomados de propuestas anteriores).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py fiat-cai081      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh fiat-cai081             # verifica, genera el PDF y ajusta los campos
```
