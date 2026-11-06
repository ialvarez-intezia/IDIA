# Brief · Canguro · Servicio de Habilidades (CAI-086)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Canguro
- **Slug**: `canguro-cai086`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-086`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Repatriar productos entre tiendas con un proceso ágil, clasificar las tiendas por metraje y venta y surtir los productos clave donde más se venden, con IA y datos dentro del entorno Google de Canguro
<!--auto:inicio-->
- **Alcance**: 5 entregables en 3 partes del proceso · 40 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Impacto · 8 Inversión · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: transcripción de la reunión con Canguro (pasada por Ivana el 05/11/2026; de ella salen las cifras, el proceso actual, los sistemas y el caso Fasto). Sin Ficha de Levantamiento. Si se contradicen, manda la transcripción; el resumen de la asesora no define la estructura.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Transcripción de la reunión de Verónica Rubio, Keiber Quintana y David Prato con Canguro (Gonzalo y su equipo de datos), pasada por Ivana el 05/11/2026, y las especificaciones de Ivana para la propuesta CAI-086. Sin Ficha de Levantamiento en el repositorio
- **Fuente del insumo**: Transcripción de la reunión con Canguro (05/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (05/11/2026): propuesta de Habilidades CAI-086 para Canguro, asesora Verónica Rubio. Educación, sin alianza y sin facilidad de pago: confirmados con Ivana. Ajustada con la transcripción de la reunión (Gonzalo, 2 meses en la empresa, y su equipo de datos); donde se contradicen las notas y la transcripción, manda la transcripción (§4.23).
- Horas (propuesta mía; Ivana dijo «propón tú» y luego pidió subirlas un poco porque participan 5 personas y se construye el producto): 40 h = manual y flujo ideal 8 (construcción 5, testeo 1, adopción 2), repatriación sugerida 12 (6, 3, 3), clasificación de tiendas 8 (4, 2, 2), surtido de productos clave 8 (4, 2, 2) y tablero de retorno 4 (2, 1, 1); total construcción 21, testeo 9, adopción 10. Antes eran 32 h. Las cinco soluciones y su reparto son diseño mío; la transcripción no fija horas.
- El preservicio (levantamiento, manual y flujo ideal, y validación de las bases de datos) se integra como la solución LG-1 de la fase de base; el postservicio es el seguimiento 30-60-90 y el tablero de retorno (DP-2).
- Cifras de la transcripción: 230 tiendas, ~19.000 productos activos, crecimiento del 100 % que esperan mantener. Gonzalo dijo «10 de 1000 aproximadamente hacen el 80 % de la venta»: se leyó como «10 de cada 1.000» por ser coherente con ~19.000 productos (≈ 190); confirmar con él. «50 personas» se dijo de forma ambigua (¿BI y Pricing?): no se cita.
- Clasificación de tiendas: Gonzalo dice que hoy es por venta; otro participante mencionó metraje. Se escribe «por tamaño» (mini, pequeña, mediana, grande) y la solución DP-1 la lleva a metraje y venta, con la «imagen» (término de Canguro para el surtido que debe tener cada tienda o grupo de tiendas).
- Caso análogo: se cuenta como «con un cliente», sin nombrar a Fasto ni la ciudad (Ivana, 05/11/2026); es el caso que Keiber contó en la reunión (conexión de las ventas de caja con compras, almacén y recepción; hoy en uso), sin cifras.
- Herramienta de IA: no se nombra. Keiber dijo que se define en el levantamiento; Canguro ya usa varias (Claude, Gemini, Kiro, Antigravity, Lovable), todo en entorno Google, sin Python ni servidores propios; Odoo y SimplyPost no se modifican. No se afirma que migren de stack (§4.11) ni se promete acceso desde Venezuela.
- Sin IA TechDay, sin Presidencia (está de viaje), sin diciembre ni plazos de aprobación en el deck: contexto interno del seguimiento comercial. El siguiente paso que se habló (mapear las demás áreas: comercio electrónico, finanzas) queda en «fuera de alcance» sin nombrar el servicio. La gobernanza de la IA no se menciona.
- Seguimiento comercial: Verónica envía la propuesta esta semana y la reunión de revisión es presencial la semana siguiente; Gonzalo la lleva a Presidencia.
- Participantes: 5 personas de Canguro (dato de Ivana, 05/11/2026), de Logística, Compras y Datos y Pricing; no se nombra quiénes. Metodología: construir, testear y adoptar (la de Habilidades de Intezia), explicada en «Cómo trabajamos».
- Ajuste del 05/11/2026 (Ivana): no hablar de áreas sino del proceso que se construye y cómo, según la información que se levante. El deck presenta un solo proceso (repatriación y surtido) en tres partes: levantamiento y clasificación (levantamiento, manual, flujo ideal y clasificación de tiendas), surtido y repatriación, y retorno. Las partes sustituyen a Logística, Datos y Pricing y Compras; las horas y la fase de cada entregable no cambian. El levantamiento (BA-1) define el diseño final de las demás piezas; si cambia, se ajusta el reparto de las 40 h con Ivana y Verónica. Los ids pasaron de LG/DP/CO a BA/SR/RE.
- Pedido del 05/11/2026 (mensaje de Verónica, pasado por Ivana): Gonzalo pidió mostrar de forma visual el impacto del recorte de personal y cómo operar con menos personas, porque a Presidencia le atraerá el beneficio operativo y la rentabilidad. Se plantea con `retorno.posiciones: true` y aval registrado (Gonzalo, 05/11/2026, mensaje de la asesora). Sin datos de dotación, escalas ni valor de la hora, el deck no trae cifras de personas ni de dinero: es método y comparación «Hoy / Con el proceso / Crecer con menos personas» en la lámina de retorno, y el tablero RE-1 mide horas, posiciones y venta contra el punto de partida. Se dice «posiciones que se reducen o no hace falta cubrir», no «recorte» ni «despidos».
- Lámina 7, «Impacto» (Ivana, 05/11/2026: «haz algo visual, un gráfico, así sea una hoja más»): gráfico de personas y horas, hoy frente a con el proceso. Son proporciones de ejemplo (10 íconos, 4 liberados; barra 35 % manual, 25 % validar y decidir, 40 % tiempo recuperado) sin datos de Canguro: la propia lámina lo dice en su nota y los números no se muestran. Se reemplaza por cifras reales cuando Gonzalo entregue personas, horas y escalas (modo cifras del retorno).

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

- Confirmar el reparto de las 40 h (21 de construcción, 9 de testeo y 10 de adopción) y las cinco soluciones con Ivana y Verónica.
- Confirmar con Gonzalo qué significa «10 de 1000 aproximadamente» frente a ~19.000 productos.
- Valor, descuento y total: campos vacíos para ventas; moneda de facturación por confirmar.
- Gonzalo es el contacto y lleva la propuesta a Presidencia: confirmar su nombre completo y cargo para dirigirla.
- Confirmar qué 5 personas participan (de qué áreas) y si los supervisores regionales validan sin ser parte de las 5.
- Si lo que se levante cambia el diseño de los entregables, reconfirmar el reparto de las 40 h antes de arrancar.
- Aval de posiciones: reconfirmar por escrito con Gonzalo (con fecha) que quiere el planteamiento de posiciones y que Presidencia lo verá; el aval actual es un mensaje de la asesora.
- Los 5 participantes y los supervisores regionales pueden leer la propuesta: decidir con Verónica y Gonzalo si el documento circula entre ellos o va solo a Presidencia.
- Para mostrar cifras reales (posiciones hoy, a reducir, valor anual) hacen falta datos de Canguro: personas que gestionan hoy traslados y surtido, horas productivas y escalas. Sin ellos se queda en método.
- Los íconos y porcentajes de la lámina de impacto son de ejemplo: confirmar con Ivana y Verónica que se aceptan como ilustración o esperar los datos reales de Canguro.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py canguro-cai086      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh canguro-cai086             # verifica, genera el PDF y ajusta los campos
```
