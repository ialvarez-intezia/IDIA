# Brief · Alfonzo Rivas & Cia. · Servicio de Habilidades (CH-015)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Alfonzo Rivas & Cia.
- **Slug**: `alfonso-rivas-ch015`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: Charla (`CH-015`) de 2 h, presentada en el formato compacto de 4 slides (portada, alcance, ruta y entregables); sin hoja de cotización, sin seguimiento y sin slide de retorno
- **Eje temático**: Charla de 2 h de inteligencia artificial para líderes: qué es y qué no es la IA, cómo decidir con ella y por dónde dar el primer paso, sin tecnicismos y sin herramienta de IA en particular
<!--auto:inicio-->
- **Alcance**: 2 entregables en 2 partes · 2 h de sesión · 1 semana de trabajo desde el arranque · sin seguimiento
<!--auto:fin-->
- **Estado**: `Enviada` (meta.json; fecha_entrega 2026-10-06)
- **Asesora comercial**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com (la misma de CAP-020, CAP-027, TA-036 y CAI-036). El deck compacto no lleva slide de cierre ni contacto.
- **Cliente**: Alfonzo Rivas & Cia. Ver `alfonso-rivas/`, `alfonso-rivas-ta036/` y `alfonso-rivas-cai036/`.
- **Ficha Comercial Intezia**: no se usa. Por instrucción del usuario el deck no lleva ningún dato del cliente (departamentos, cantidades, áreas, sector), solo su nombre.
- **fecha_arranque_deseada**: no declarada. El formato compacto no lleva Calendario de inicio.
- **resultados_esperados**: no aplica: una charla no mide retorno, el deck no lleva slide de retorno.

## Origen y fuente

- **Origen**: Transformación de la propuesta CAI-036 (sesión de 3 h para líderes de Alfonzo Rivas & Cia.) e instrucción directa del usuario del 06/10/2026: charla de 2 h, sencilla, sin datos de departamentos, cantidades ni áreas
- **Fuente del insumo**: Propuesta CAI-036 y antecedentes de la cuenta (CAP-020, CAP-027, TA-036)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Transformación de CAI-036 (sesión de 3 h) en una charla de 2 h, por instrucción del usuario (06/10/2026). Es una propuesta nueva con código de Charla (CH-015, el siguiente libre tras CH-014); CAI-036 queda intacta como registro de lo enviado.
- Guardia §4.21 punto 5: el usuario ya eligió el formato compacto para esta cuenta el mismo día y pidió la charla «sencilla». Se mantiene el compacto, en 4 slides: portada, alcance, ruta y entregables. Sin slide de retorno (una charla no mide retorno), sin hoja de cotización y sin seguimiento 30-60-90 (instrucciones previas del usuario), por tanto sin garantía.
- Instrucción del usuario: no ofrecer datos de departamentos, cantidades de personas, áreas ni nada de eso. El deck solo lleva el nombre del cliente: no hay 800 colaboradores, edades, sector, áreas ni «departamento». Los 3 datos de la portada describen el contenido de la charla, no al cliente.
- Sin herramienta de IA en particular (instrucción previa del usuario). El stack de CAP-020 (100% Google) no se menciona.
- El compacto exige horas enteras por entregable, así que las 2 h se reparten en 2 partes de 1 h. Los minutos internos de cada parte los define el facilitador.
- Entregables propuestos por el sistema (guía rápida, preguntas clave y material en digital): son los típicos de una charla (ver CH-013, INCRET) y hay que confirmarlos con servicio.
- «Sin preparación previa» y «espacio para preguntas» son decisiones de diseño por la consigna «sencilla»; confirmar con servicio.
- Sin certificado por defecto (§4.21). Modalidad, fecha y horario se omiten: no existen todavía.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md)

- Sin Metodología ABR ni Equipo facilitador (§4.10a). Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (slide opcional, módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). «Hacia la semana N» (construcción + 90 días) por confirmar con servicio. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Sin hoja de cotización (sin_hoja_cotizacion): el deck no lleva precios ni campos de cotización; el precio se comunica por otro medio.

## Pendientes

- Precio: el deck no lleva hoja de cotización ni campos de precio. Ventas lo comunica por otro medio.
- Confirmar modalidad (en TA-036 el contacto pidió online síncrono), fecha y horario.
- Confirmar el código CH-015 y si esta charla reemplaza a CAI-036, la acompaña o va en paralelo con TA-036 (cortesía de 4 h, sin respuesta registrada).
- Confirmar con servicio los entregables de la charla y el reparto de las 2 h.

## Qué se pidió y qué se decidió

Instrucción del usuario (2026-10-06): «transforma esto en una charla de 2h de IA para líderes, no ofrezcas datos de departamentos ni cuántos son ni áreas ni nada de eso, hazla sencilla». «Esto» es la propuesta CAI-036 (sesión de 3 h, compacto, sin seguimiento ni cotización).

- **Propuesta nueva, no una edición de CAI-036.** CAI-036 ya salió (Enviada) y es otro producto (capacitación de 3 h por departamento). Esta es una Charla con código propio **CH-015** (el siguiente libre tras CH-014). CAI-036 queda intacta.
- **Formato: compacto de 4 slides.** El usuario ya había elegido el compacto para esta cuenta (guardia §4.21 punto 5) y ahora pidió «sencilla». Se quitó el retorno (una charla no mide retorno) y se mantiene sin hoja de cotización ni seguimiento (instrucciones previas).
- **Sin datos del cliente.** El deck no tiene departamentos, áreas, cantidades de personas, colaboradores, edades ni sector. Solo el nombre. Los 3 datos de la portada describen el contenido de la charla, no al cliente.
- **Sin herramienta de IA en particular** (instrucción previa).
- **2 h en 2 partes de 1 h** (el compacto exige horas enteras por entregable). Parte 1 «Entender la IA» (módulo I de CAP-020, sin el stack) y parte 2 «Decidir y empezar» (módulo II, Liderazgo ejecutivo con IA, más un primer paso por líder).

## Antecedentes de la cuenta

| Código | Qué fue | Estado |
|---|---|---|
| CAP-020 | Proyecto IA en 3 fases (su Fase 2: capacitación de líderes de 8 h en 4 módulos). Stack 100% Google | Enviada, sin aprobar |
| CAP-027 | Plan de adopción trimestral para toda la empresa | Enviada, sin aprobar |
| TA-036 | Taller de cortesía de 4 h con los 4 servicios (30/09/2026) | Enviada, sin respuesta registrada |
| CAI-036 | Capacitación de líderes, sesión de 3 h, 5 slides (06/10/2026) | Enviada (convención) |

Contexto interno que **no** se expone en el deck: el contacto respondió que la empresa valida internamente antes de llegar a la directiva y que necesita ver el impacto en el negocio. Una charla de 2 h es el paso más pequeño posible y no obliga a nada más.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py alfonso-rivas-ch015      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh alfonso-rivas-ch015             # verifica, genera el PDF y ajusta los campos
```
