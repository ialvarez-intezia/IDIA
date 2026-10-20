# Brief · Go Pharma · Servicio de Detección y Habilidades (CAI-050)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Go Pharma
- **Slug**: `go-pharma-cai050`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Capacitación In-Company · Detección + Habilidades por etapas · Etapa 1 charla (2 h) + Etapa 2 Comercialización, Operaciones y Administración (50 h) + Etapa 3 dos clones digitales (12 h) · 64 h · Claude sobre Google Workspace · compacto v3 (`CAI-050`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Alineación del equipo de Go Pharma en IA, levantamiento y construcción en Comercialización (con el CRM GoHighLevel), Operaciones y Administración, y clones digitales con Claude para los dos decisores, sobre Google Workspace y en tres etapas con valor propio
<!--auto:inicio-->
- **Alcance**: 18 entregables en 6 bloques · 64 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Cómo trabajamos · 4 Ruta · 5 Entregables · 6 Retorno · 7 Inversión · 8 Inversión (etapa 2) · 9 Inversión (etapa 3) · 10 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: no hay Ficha de Levantamiento. Se usó la minuta de la reunión con Go Pharma (13/10/2026, sin fecha en el deck) y las indicaciones de la asesora (María): por qué por etapas, estructura de las 3 etapas, plataforma, CRM y fuera de alcance. La minuta no trae horas, tiempos ni volúmenes: las horas por etapa y por área son una propuesta del sistema con los lineamientos de `empresa/politicas-comerciales.md`.
- **fecha_arranque_deseada**: Carolina busca un lugar para la charla de la Etapa 1 el viernes 16/10/2026 y quiere arrancar pronto (se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones). La fecha y el lugar los define Go Pharma.
- **resultados_esperados**: no se dieron en cifras; la minuta solo da dolores (leads en libreta y Excel, informes diarios a mano, conciliación y cobro mensual manuales). Sin tiempos del cliente no se calculan horas liberadas por mes, no se inventan (retorno en modo método).

## Origen y fuente

- **Origen**: Indicaciones de la asesora María Iribarren y minuta de la reunión con Go Pharma (13/10/2026). Go Pharma no aprobó el monto global anterior por flujo de caja, así que la propuesta se presenta por etapas, con valor propio cada una
- **Fuente del insumo**: Minuta de la reunión con Go Pharma e indicaciones de la asesora: charla de 2 h, levantamiento y construcción por área (Comercialización primero, con GoHighLevel) y clones digitales para los dos decisores
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Fuentes: indicaciones de la asesora María Iribarren y minuta de la reunión con Go Pharma (13/10/2026). División Educación, servicio Habilidades en formato compacto, combo Detección + Habilidades en la Etapa 2 (`servicio_rotulo` y `meta_servicio: deteccion`, como CAI-032 y CAI-026), sin alianza, código CAI-050 por instrucción del usuario. La propuesta no lleva fechas (§4.23): la charla de la Etapa 1 se busca para el viernes 16/10/2026, pero eso va al kickoff, no al deck.
- Por etapas porque Go Pharma no pudo aprobar el monto global anterior por flujo de caja y Marco, quien aprueba el presupuesto, no estuvo en la reunión: cada etapa lleva su propia hoja de cotización (`inversion.etapas`: una hoja por etapa, con sus horas, sus áreas, su valor, su descuento y su total; Ivana, 13/10/2026, reemplazó el recuadro de valor por etapa en una sola hoja). El generador solo soportaba 2 hojas y se extendió a 3.
- Horas propuestas por el sistema con los lineamientos de `empresa/politicas-comerciales.md`, porque María no las dio: Etapa 1 = 2 h (charla). Etapa 2 = 4 h de levantamiento por área (Detección) más Habilidades de 8 a 12 h por área hasta 5 procesos: Comercialización 24 h (4 + 12 + 8 por el CRM GoHighLevel, configuración y adopción), Operaciones y Atención al cliente 14 h (4 + 10) y Administración y Finanzas 12 h (4 + 8), total 50 h. Etapa 3 = 6 h por Cerebro Digital × 2 = 12 h. Total 64 h y 18 entregables. María ajusta.
- Áreas de la Etapa 2 según la minuta: Comercialización (prioridad), Operaciones y Atención al cliente, y Administración y Finanzas. Quedan para una etapa posterior Tecnología, Recursos Humanos y Mercadeo, con una escucha aparte con Tecnología.
- Plataforma: Google Workspace como base (ya lo usan) y Claude donde se justifica; licencias progresivas por perfil. El riesgo de bloqueo de cuentas de Claude en Venezuela NO se menciona en el deck (indicación de Ivana, 13/10/2026: «eso no se dice»; antes se había escrito de frente por pedido de María). Interno: Anthropic no incluye a Venezuela entre los países y regiones soportados (anthropic.com/supported-countries, consultada el 13/10/2026), nunca se promete VPN y el respaldo, si hiciera falta, es Gemini en Workspace.
- Clones digitales: las áreas se llaman «Clon digital 1» y «Clon digital 2» porque no se exponen nombres de personas del cliente (como en CAI-039) y no se sabe el cargo de cada decisor. Contenido tomado de la minuta (procesos, clientes, propuestas, precios y reuniones) y de las indicaciones de María (conecta Claude con procesos, clientes, propuestas y reuniones). La minuta recomienda Granola para las reuniones (y menciona Fathom); no se nombra en el deck para no sumar otra herramienta. El rollout de la minuta (empezar con la directora comercial sola y luego un asiento compartido para las vendedoras) queda como parte de las licencias progresivas, no como entregable.
- Los tres niveles de automatización de la minuta (autónoma, asistida y con supervisión total) se usan en el contenido de la charla y en el método («la IA propone y una persona aprueba» en lo financiero). La mayoría de los procesos de Go Pharma caen en el nivel asistido.
- Retorno en modo método: la minuta no trae tiempos ni volúmenes (solo frecuencias: informe diario, cobro en los primeros 5 días del mes), así que no se calculan horas liberadas por mes. Con los tiempos del cliente se pasa a modo cifras, marcado como estimado y sin cifras externas (`retorno-captura.xlsx`).
- Facilidad de pago: **se quitó la hoja el 13/10/2026** (Ivana: «quitar la hoja de plan de pago»; `omitir: ["pago"]`). Antes se incluía porque Carolina dijo que las condiciones de pago ayudan (la CAI-049 de Mercosur no la llevaba): 4 cuotas (30/25/25/20) atadas a hitos de las etapas, provisional. Las condiciones de pago las negocia ventas.
- Contenido de la charla (fundamentos, tres niveles de automatización, ejercicio práctico) propuesto desde la minuta, sin temario de María. Las soluciones de cada área salen de los dolores de la minuta; sus nombres y horas se ajustan en cada levantamiento.
- Asesora: María Iribarren, con los datos de la CAI-045 y la CAI-049.

## Plataforma: justificación por perfil (interna, propuesta del sistema; el deck solo dice «licencias progresivas, por perfil»)

La slide de inversión no tiene espacio para una tabla de licencias (`inversion.partes` ocupa esa zona), así que el detalle vive aquí y en el correo de envío. Valores de lista de Claude y de GoHighLevel: no se escriben (cambian y María los envía en un documento aparte, como en la DET-028).

| Perfil | Claude | Por qué | Cuándo |
|---|---|---|---|
| Los dos decisores (Etapa 3) | Sí, primero | El clon digital conecta Claude con procesos, clientes, propuestas y reuniones; Marco ve el valor por sí mismo | Con la Etapa 3, que puede arrancar en paralelo |
| Dirección comercial (Comercialización) | Sí, sola durante el primer mes | Claude conectado al CRM propone seguimientos y borradores, y arma los reportes de lunes y viernes | Después de configurar GoHighLevel |
| Vendedoras | Un asiento compartido | Solo si el uso del equipo comercial lo justifica; la minuta propone este rollout | Tras el primer mes de la dirección comercial |
| Administración y Finanzas | A decidir en el levantamiento | La conciliación es de nivel asistido (la IA propone, la persona aprueba): Claude aporta si el volumen y las 7 cuentas de correo lo justifican | Después del levantamiento de esa área |
| Operaciones y Atención al cliente | Workspace primero | Informe diario, alertas y directorio pueden resolverse con Sheets y Drive; Claude solo si el levantamiento muestra que hace falta | Después del levantamiento de esa área |

**Riesgo de bloqueo de cuentas en Venezuela** (solo interno; el deck NO lo menciona desde el 13/10/2026, indicación de Ivana): Venezuela no figura entre los países con soporte oficial de Claude (anthropic.com/supported-countries, consultada el 13/10/2026) y la política prohíbe usarlo estando físicamente en una región no soportada. Nunca se promete VPN. Por qué es acotado: pocas cuentas al inicio, la información vive en el Drive de Go Pharma, lo construido queda documentado y el respaldo es Gemini en Workspace (confirmar que su plan lo incluya). La política puede cambiar: volver a consultar antes de enviar.

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Informe Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Montos de inversión, descuento y total: vacíos, los llena ventas.

## Pendientes

- Definir el valor de cada etapa, el descuento y el total (campos vacíos para ventas) .
- Confirmar las horas por etapa y por área (64 h en total) con María: son una propuesta con los lineamientos del sistema.
- Confirmar con María los datos para el retorno en horas liberadas por mes (tiempo por tarea, veces al mes y personas por área): sin ellos el retorno queda en modo método.
- Confirmar que el plan de Google Workspace de Go Pharma incluye Gemini (respaldo interno, el deck ya no lo nombra) y qué perfiles llevan Claude primero.
- Confirmar cargos de Carolina y Marco: si se pueden nombrar, «Clon digital 1» y «Clon digital 2» pasan a decir para quién son.
- Fecha y lugar de la charla (Go Pharma define; Carolina busca un lugar para el viernes 16/10/2026) y del informe de diagnóstico: van al kickoff y al correo de envío, no al deck.
- Dejar meta.json en Borrador hasta que ventas llene los valores y envíe.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py go-pharma-cai050      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh go-pharma-cai050             # verifica, genera el PDF y ajusta los campos
```
