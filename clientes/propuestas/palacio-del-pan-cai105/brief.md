# Brief · El Palacio del Pan · Servicio de Habilidades (CAI-105)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: El Palacio del Pan
- **Slug**: `palacio-del-pan-cai105`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-105`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Construir con el equipo de El Palacio del Pan, con IA, las herramientas de cuatro áreas administrativas (cierre de caja, cuentas por pagar, producción y costos, inventario y compras) a partir del informe del sistema y los datos base que la panadería entregó
<!--auto:inicio-->
- **Alcance**: 16 entregables en 4 áreas · 48 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Pedido de Ivana (18/11/2026): propuesta de Habilidades para El Palacio del Pan a partir del paquete que la panadería envió a los proveedores del sistema (Informe del sistema v14, Esquema del sistema v3, Datos base v10, Recetas de referencia v2, noviembre de 2026) y de lo que ya se sabe de ellos por la DET-051. Asesora: Verónica Rubio
- **Fuente del insumo**: Informe del sistema v14 (17/11/2026), Esquema del sistema v3, Datos base del sistema v10 y Recetas de referencia v2 del cliente; DET-051 (Ficha y transcripción del 02/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (18/11/2026): propuesta de Habilidades a partir del paquete que El Palacio del Pan envió a los proveedores del sistema (Informe v14, Esquema v3, Datos base v10, Recetas v2) y de lo que ya se sabe por DET-051. Asesora: Verónica Rubio.
- Decisiones de Ivana (18/11/2026): alcance de cuatro áreas (cierre de caja, cuentas por pagar, producción y costos, inventario y compras), 12 h por área = 48 h con el equipo, sin nombrar herramienta de IA, impacto «operación». División Educación y alianza = no: tomados por mí (misma cuenta que DET-051), no los dio Ivana.
- Reparto mío: cada área en 4 entregables de 3 h, tomados del informe (cierre por turno, arqueo, conciliación de lotes y resumen diario de cierres; registro de facturas, abonos, programación de pagos y antigüedad de saldos; recetario, plan del día, costo de cada tanda y margen; fichas con unidades, conteo guiado, alertas de mínimo y merma, orden de compra y recepción). Fase 1 = los dos cuellos de botella que marca el informe; fase 2 = producción e inventario, que parten de los datos base.
- Lo que el cliente pide es un sistema integral de 15 módulos que reemplace a Profit y lo ofrece a varios proveedores. El deck no promete un sistema completo: dice qué se construye (cuatro áreas) y deja explícito lo que queda fuera (sistema integral, facturación fiscal, contabilidad, nómina, impuestos, mercadeo y mantenimiento).
- Hechos de la portada: salen del propio informe del cliente (cierre tecleado dos veces, cuentas por pagar con abonos en Excel, Profit sin costo de lo vendido, 775 productos y 13 recetas). No se cita su fuente en el deck (regla de fuentes en presentaciones).
- Profit no se nombra en las soluciones; solo en «Fuera de este alcance» (reemplazarlo no es parte del servicio). No se afirma que la panadería migre ni que las herramientas se conecten con Profit (§4.11): el informe dice que el sistema nuevo no se conecta con él.
- Datos fiscales y de nómina: fuera de alcance. No se cargan datos de clientes ni cuentas bancarias a la IA; los 775 productos, recetas y proveedores se usan como datos de prueba, que el informe declara «de referencia».
- Herramienta (Ivana): sin nombrar. Juan Carlos ya probó Claude Code por su cuenta; no se menciona Claude ni VPN (Venezuela no es país soportado).
- Enfoque del cuadro Impacto: operación (Ivana, 18/11/2026), sin posiciones ni nómina: no hay aval del cliente. La pregunta de Juan Carlos sobre roles y cuántas personas (DET-051) no se responde en esta propuesta.
- Seguimiento 30-60-90 incluido por ser estándar de Habilidades y porque responde a la objeción de adopción de DET-051; Ivana puede quitarlo. Sin facilidad de pago (omitir: pago, regla permanente). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23): el informe habla de conteo semanal y de calendarios de avisos; no aparecen en el deck.
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

- Valor, descuento y total: campos vacíos para ventas. En DET-051 Verónica dio como anclaje «de 2.300 en adelante»; con 48 h de Habilidades el valor es otro: confirmar con Verónica antes de enviar.
- Expectativa del cliente: pide un sistema completo que reemplace a Profit. Conviene que Verónica lo aclare con Juan Carlos antes o durante la presentación: Intezia construye con su equipo herramientas con IA, no entrega un sistema integral.
- Relación con DET-051 (Detección en 3 áreas, aún en Borrador): confirmar con Ivana y Verónica si se presentan juntas, por separado o si CAI-105 reemplaza a DET-051. El deck de CAI-105 no nombra la Detección.
- Qué herramienta de IA se usa y quién contrata las licencias (se define en el arranque).
- Dónde se ejecutan las herramientas construidas (los equipos de la panadería usan Windows y Excel; el servidor tiene SQL Server) y quién las sostiene después: aclarar en el arranque.
- Quién del equipo participa en cada área (el informe cuenta 18 personas) y si el trabajo es presencial en Guacara o en línea.
- Dudas del cliente que el informe pide listar («qué dudas tienen y cuáles serían los siguientes pasos»): armar la respuesta con Verónica.
- Si hace falta agregar más áreas (Ventas y clientes, Bancos y tesorería, Nómina, Impuestos): +12 h por área según el lineamiento; no incluidas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py palacio-del-pan-cai105      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh palacio-del-pan-cai105             # verifica, genera el PDF y ajusta los campos
```
