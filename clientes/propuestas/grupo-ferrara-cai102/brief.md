# Brief · Grupo Ferrara · Servicio de Habilidades (CAI-102)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Grupo Ferrara
- **Slug**: `grupo-ferrara-cai102`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-102`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construir dos Clon Digital personalizados para la dirección de Grupo Ferrara, con el contexto de la empresa cargado para consultar decisiones complejas en minutos
<!--auto:inicio-->
- **Alcance**: 4 soluciones en 2 áreas · 12 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Transcripción de la reunión con Grupo Ferrara (clon digital para la dirección) y la relación comercial vigente de CAI-101.
- **Fuente del insumo**: Transcripción de la reunión con el cliente. Continuación comercial de CAI-101 (mismo cliente); sin Ficha de Levantamiento propia para este programa personalizado.
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- No se mencionan nombres ni el parentesco de los dos integrantes de la dirección (instrucción explícita del usuario, 2026-11-17): el deck se refiere a ellos como «Clon Digital 1» y «Clon Digital 2», dos integrantes de la dirección de Grupo Ferrara.
- Mismo cliente que CAI-101 (Grupo Ferrara): se reutiliza la asesora comercial (Verónica Rubio) y el carril Claude, consistente con lo recomendado en la transcripción para Dirección y Tecnología.
- 6 horas por clon (12 h en total), indicadas por el usuario. Con sin_horas_trabajo: true no se muestran en el deck; quedan en el detalle interno (programa.md) para cotizar.
- Sin datos propios del cliente para el retorno: modo metodo.
- Sin facilidad de pago (omitir: ["pago"]): no se especificó un plan de cuotas.
- Contenido de ambos clones construido desde la sección de la transcripción de Grupo Ferrara sobre «Clon Digital y Ecosistema de IA Corporativo» (grafo de nodos, consulta de decisiones en minutos), no desde una Ficha propia de este programa personalizado.

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

- Definir el valor del proyecto, el descuento y el total: campos vacíos para ventas.
- Confirmar con Grupo Ferrara qué plan de Claude usará cada integrante (Pro o superior) y quién lo paga.
- Si se quiere facilidad de pago, definir las cuotas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py grupo-ferrara-cai102      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh grupo-ferrara-cai102             # verifica, genera el PDF y ajusta los campos
```
