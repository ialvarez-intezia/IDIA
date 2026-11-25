# Brief · Clínica Santiago de León · Servicio de Habilidades (CAI-104)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Clínica Santiago de León
- **Slug**: `clinica-santiago-de-leon-cai104`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-104`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construir 10 Cerebros Digitales, uno por gerente de distintas áreas de la Clínica Santiago de León, con el contexto de cada área cargado para consultar y decidir en minutos
<!--auto:inicio-->
- **Alcance**: 20 soluciones en 10 Cerebros Digitales · 60 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Solicitud de propuesta pegada por Ivana (17/11/2026), con detalles de la reunión de Verónica Rubio con la clínica: propuesta adicional para implementar 10 cerebros digitales dirigidos a gerentes de distintas áreas. Sin Ficha Comercial ni transcripción propias de este programa
- **Fuente del insumo**: Solicitud de propuesta (instrucción directa, sin Ficha Comercial ni transcripción)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Alcance (solicitud de Ivana, 17/11/2026, con detalles de Verónica): propuesta adicional para implementar 10 cerebros digitales dirigidos a gerentes de distintas áreas. Sin más datos del cliente.
- Horas (Ivana, 17/11/2026): 6 h por cerebro, la tarifa de referencia de Cerebros Digitales, con 2 entregables de 3 h por gerente (grafo de conocimiento y Project de Claude), como la CAI-102: 60 h en total. Con sin_horas_trabajo el deck muestra el total y el reparto solo en la hoja de inversión (regla del 17/11/2026).
- División Educación y alianza = no: tomados por mí (misma clínica que DET-056), no los dio Ivana.
- Herramienta (Ivana, 17/11/2026): Claude. Por criterio de Ivana el deck no menciona el acceso desde Venezuela ni promete VPN (Venezuela no figura entre los países soportados de Anthropic). Ojo: en la DET-056 la clínica objetó justo eso; ver pendientes.
- Los 10 gerentes no están identificados: los cerebros se llaman «Gerente 1» a «Gerente 10» y todos llevan el mismo contenido. No se nombran áreas ni personas.
- Sin Ficha ni transcripción propias: los datos de la portada son de contenido, no hechos de la clínica. El contenido del cerebro (procesos, políticas, reportes y decisiones del área) es mío, por confirmar con cada gerente en el arranque.
- Los datos de pacientes quedan fuera del cerebro: límite que pongo yo, coherente con la DET-056 («Los datos de pacientes no se cargan a la IA»).
- Enfoque del cuadro Impacto: operación (Ivana, 17/11/2026), sin cifras ni estudios.
- Sin certificado (como la CAI-102) y con seguimiento 30-60-90; sin facilidad de pago (omitir: pago, regla permanente de Ivana). Hoja de inversión con valores vacíos para ventas, en REF.
- Contacto de la última slide: Verónica Rubio, asesora comercial.

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

- Valor, descuento y total: campos vacíos para ventas.
- Acceso a Claude desde Venezuela: la clínica ya objetó en la DET-056 que los proveedores conocidos no incluyen a Venezuela. Conviene tener una respuesta verificada y por escrito antes de presentar esta propuesta, y un respaldo declarado si no es viable (por ejemplo, otra herramienta que la clínica ya use).
- Quiénes son los 10 gerentes y de qué áreas: con eso cada cerebro se nombra por su área («Cerebro Digital de Finanzas») y se ajusta el contenido.
- Formato de trabajo: si cada cerebro se construye de forma individual con su gerente o en grupos (cambia la logística y lo que se cotiza).
- Modalidad (presencial o en línea) y quién contrata las licencias de Claude (plan y puestos).
- Confirmar con Ivana si el programa lleva certificado.
- Relación con DET-056 y CAI-103 (misma clínica): confirmar con Ivana y Verónica si se presentan juntas, por separado o en paquete.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py clinica-santiago-de-leon-cai104      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh clinica-santiago-de-leon-cai104             # verifica, genera el PDF y ajusta los campos
```
