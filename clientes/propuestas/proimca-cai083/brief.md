# Brief · Proimca · Servicio de Habilidades (CAI-083)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Proimca
- **Slug**: `proimca-cai083`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-083`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Automatizar con IA los procesos manuales y repetitivos de Administración y contabilidad (con talento humano), CDC, Mercadeo y Planificación técnica de Proimca, con un criterio común de uso de IA y herramientas de la empresa
<!--auto:inicio-->
- **Alcance**: 10 soluciones en 4 áreas · 36 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Proimca (Verónica Rubio, registrada el 02/11/2026; contacto Damaris Pérez García, directora que forma parte del grupo que aprueba) y transcripción de la reunión virtual del 02/11/2026, más instrucciones de Ivana del 03/11/2026: propuesta de Habilidades CAI-083 con Verónica Rubio como asesora. División Educación y sin alianza, por confirmar
- **Fuente del insumo**: Ficha de Levantamiento (02/11/2026) y transcripción de la reunión de Verónica Rubio con Proimca (02/11/2026)
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (03/11/2026): propuesta de Habilidades CAI-083 para Proimca con Verónica Rubio como asesora, a partir de la Ficha de Levantamiento y la transcripción del 02/11/2026. División Educación y sin alianza: por confirmar con Ivana. Sin facilidad de pago: criterio de Ivana en las últimas propuestas (OCAATVE, Suri Import); no lo dijo para esta, confirmar.
- Insumos: ficha y transcripción coinciden. Primer contacto. Telecomunicaciones (internet y televisión) en Lara; ISO 9001 reciente. Damaris Pérez García es directora y parte del grupo de 2 o 3 directores que aprueba caso por caso, por costo-beneficio; sin partida fija. Descartó Detección («ya hemos avanzado mucho»): va directo a Habilidades y la secuencia Habilidades, Políticas e Innovación («va por paso»).
- Áreas: las cuatro que ella eligió, en una sola fase («primero cuatro áreas»): Administración y contabilidad (con talento humano, una sola gerencia), CDC, Mercadeo y Planificación técnica (unas 23 personas). Ella dijo que quizá no todas al mismo tiempo; la fase 1 y la fase 2 reparten el orden, no los equipos.
- Herramienta (supuesto mío, por confirmar con Verónica o Ivana): Gemini en Google Workspace, que ya usan y la empresa tiene incluido, con NotebookLM. Damaris preguntó en qué áreas hacen falta licencias corporativas (también ha considerado Claude): la «Recomendación de licencias por área» responde esa pregunta y no pre-decide una herramienta. No se menciona Claude ni VPN (Venezuela no es país soportado).
- Horas (lineamiento de empresa/politicas-comerciales.md, 8 a 12 h por área hasta 5 procesos): Administración 12 h (4 procesos × 3 h, la gerencia que más retrabajo tiene), CDC 8 h, Mercadeo 8 h y Planificación técnica 8 h = 36 h con el equipo, mi reparto por solución. Las 10 soluciones salen de las tareas reales de la ficha. Sin Fundamentos ni nivelación aparte: sus cursos internos no prendieron, el método es aprender haciendo sobre sus procesos.
- Fases (mi criterio, por confirmar): fase 1 «Inicio» (18 h) = procesos con datos que ya tienen (conciliación, libros, redes, carga de visitas); fase 2 «Enlace» (18 h) = procesos que dependen de datos de sus sistemas (SAE Plus a Odoo, talento humano mientras llega la nómina de Odoo, CDC entre HiBot y SAE Plus, tiempos en calle sobre las visitas cargadas).
- Fuera de alcance, dicho por Verónica en la reunión: los ajustes al bot de HiBot (proyecto aparte, de Tecnología) y el traslado a Barquisimeto (viáticos de Proimca o cotizados aparte, como con DUSA). La gobernanza que pide Damaris es el servicio de Políticas, siguiente paso; la «política de uso de IA» que ellos mismos redactan queda fuera.
- Retorno en modo método, sin cifras (el volumen de conciliaciones es «miles» y no hay horas). Su indicador duro es la retención (perder como máximo 1 % de la base): en el deck solo aparece como «meta de retención» sin la cifra, porque no está validada con el área.
- Calendario (no va en el deck, §4.23): días de corte del 6 al 10 de cada mes se evitan (dato del cliente en «ritmo»); horario de 8:00 a. m. a 5:00 p. m. de lunes a sábado; Intezia recomendó encuentros de 2 horas y no se fijó la frecuencia. Revisión de la propuesta el jueves 05/11/2026 a las 10:30 a. m.; Verónica prometió enviarla el 03/11 al final de la tarde o el 04/11 por la mañana.
- Del texto de Verónica no se toman los 10 roles delegables de DUSA ni la reubicación de personal. Las citas de la ficha no se usan. Sin semanas, sesiones ni fechas; sin horas de trabajo ni cantidad de consultores (CLAUDE.md §4.23).

- Ajuste del 04/11/2026 (Ivana): la hoja de inversión se desglosa por área (`inversion.desglose`, como Viva CAI-079): una fila por área con herramientas, horas (12, 8, 8 y 8 h = 36 h) y valor en USD editable, más subtotal, descuento «por contratar el programa completo», IVA y total que se calculan en el PDF. Motivo: el total queda alto y la empresa quiere evaluar si arranca con las 4 áreas o con 2. La nota dice que cada área se puede contratar por separado. Confirmar con Ivana/Verónica: si elegir 2 áreas conserva las dos fases (Inicio y Enlace) de esas áreas, y si el descuento aplica solo al proyecto completo.

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

- Confirmar con Ivana la división Educación, que no hay alianza y que va sin facilidad de pago.
- Confirmar la herramienta (Gemini en Google Workspace) y, con ella, si la recomendación de licencias nombra otras (Claude).
- Confirmar las 36 h y el reparto por solución, y las dos fases.
- Valor, descuento y total: campos vacíos para ventas; moneda de facturación por confirmar con Verónica.
- Conseguir los nombres de la gerente administrativa, el coordinador del CDC y la gerente de planificación, y el nombre del chat corporativo interno (Verónica lo debe pedir).
- Confirmar si la reunión de revisión incluirá a los otros directores (Verónica los invitó).
- Confirmar el teléfono y el correo de Verónica Rubio (tomados de propuestas anteriores).

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py proimca-cai083      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh proimca-cai083             # verifica, genera el PDF y ajusta los campos
```
