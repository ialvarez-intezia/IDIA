# Brief · Metalurgia Metalblanc · Servicio de Detección (DET-028)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Metalurgia Metalblanc
- **Slug**: `metalblanc`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Alianza**: `no`
- **Tipo de documento**: Detección · Fundamentals (2h grupal, 11 personas) + auditoría de 5 áreas (Estructura de costos, Producción, Administración, Ventas y Marketing), 4h por área (20h), 22h totales, modalidad a coordinar · formato compacto v2 (`DET-028`); formato compacto de 9 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Auditar Estructura de costos, Producción, Administración, Ventas y Marketing de Metalblanc, con un logro inmediato en cada área (empezando por agilizar los presupuestos), para llegar a un mapa de oportunidades de IA priorizado y a las bases para ordenar sus procesos
<!--auto:inicio-->
- **Alcance**: 6 entregables en 5 áreas · 22 h de sesión · 4 semanas de trabajo desde el arranque · sin seguimiento
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Facilidad de pago · 9 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Enviada` (fecha_entrega 2026-10-08; PDF de 9 páginas, 9 campos editables)
- **Ficha Comercial Intezia**: Ficha de Levantamiento de Metalblanc (08/10/2026, Flavia Martínez), más el resumen de la reunión pegado por el usuario. Se tomó: servicio de interés (Detección), las 5 áreas a auditar (Estructura de costos, Producción, Administración, Ventas y Marketing), 11 personas (también para Fundamentals), el dolor de los presupuestos a mano, el stack (Google Workspace, hojas de cálculo, Gemini de 20), el quick win (agilizar presupuestos a partir de una estructura de costos), el horizonte (corto plazo, 0 a 3 meses) y que firma la CEO (Grisel Toubia, no aparece en el deck)
- **fecha_arranque_deseada**: no indicada (horizonte de corto plazo, 0 a 3 meses). Sin Calendario de inicio
- **resultados_esperados**: saber qué se puede automatizar y en qué orden, empezando por algo pequeño, y ordenar los procesos como base para luego implementar un ERP (Odoo). Sin cifras: no se agrega ROI, el retorno es en modo método

## Origen y fuente

- **Origen**: Ficha de Levantamiento de Metalblanc (registrada el 08/10/2026, asesora Flavia Martínez), resumen de la reunión pegado por el usuario e instrucción directa del usuario del 08/10/2026: código DET-028
- **Fuente del insumo**: Ficha de Levantamiento de Metalblanc (08/10/2026) y resumen de la reunión de la asesora
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- División Educación inferida: pyme manufacturera, cliente corporativo privado. Alianza: no (primer contacto, sin servicio ni propuesta previos). Código DET-028 por instrucción del usuario. Servicio Detección (el de la Ficha y el que recomendó la asesora). Asesora: Flavia Martínez.
- Horas por el lineamiento de Detección: Fundamentals de 2 h (un solo grupo, 11 personas, bajo el máximo de 25) y 4 h por área en 5 áreas (Estructura de costos, Producción, Administración, Ventas y Marketing, las 5 que lista la Ficha) = 22 h. El kick-off de arranque va aparte y no suma horas (convención general). La Ficha dice 11 personas por área a entrevistar: en una empresa de 11 personas son las mismas personas repartidas en las áreas, así que cada sesión es con quienes conocen el área.
- Calendario propuesto por el sistema, no dictado por la Ficha: 4 semanas (semana 1 kick-off y Fundamentals, semana 2 Estructura de costos y Producción, semana 3 Administración y Ventas, semana 4 Marketing y Reporte Final). La Estructura de costos va en la primera semana de auditoría porque es la prioridad y la urgencia de la cliente. El orden y el Reporte Final en la semana 4 hay que confirmarlos con servicio y con Flavia.
- Anclaje en la prioridad (pedido del resumen de la asesora): la estructura de costos y los presupuestos son el eje visible (titular, lead, hechos, primera sesión, fase destacada y metas), y su sesión de 4 h es el logro inmediato que identifica la Ficha. Las otras 4 áreas se mantienen: la asesora pidió no quedarse solo con los procesos que la cliente nombró, y el Reporte Final debe dar una ruta de prioridades.
- Alcance honesto del logro de presupuestos: en 4 h se arma una primera versión de la estructura de costos y un presupuesto de prueba más rápido, sobre los costos que Metalblanc decide compartir. No es una app terminada, ni un ERP, ni la estructura completa de todos sus productos. La cliente imagina una app de presupuestos y luego un ERP: el deck deja ambos como posteriores (fuera de alcance y «Más adelante»).
- ERP (CLAUDE.md §4.11): la cliente quiere a largo plazo implementar un ERP (Odoo) y ve la IA como paso previo. El deck no afirma que migra ni nombra el producto: dice que, con los procesos ordenados, decide cómo seguir «por ejemplo con un sistema de gestión (ERP)». La asesora sugirió presentar la Detección como el paso que deja la empresa lista para Odoo; se mantiene la idea sin afirmarlo como plan.
- Acceso a Claude desde Venezuela (la objeción principal de la cliente): Anthropic no incluye a Venezuela en su lista oficial de países soportados (anthropic.com/supported-countries, consultada el 08/10/2026) y su política prohíbe el uso estando físicamente en una región no soportada; usar una VPN para saltarla puede llevar al bloqueo de la cuenta, que es justo el miedo de la cliente. Por eso el deck NO promete «usar Claude con seguridad con VPN». Dice que el acceso depende del país, que se define antes de arrancar cómo usarlo dentro de las condiciones del proveedor y que, si no es viable, la nivelación y los logros se hacen con Gemini (que ya usan). El Reporte Final recomienda la herramienta con ese criterio. Pendiente de decisión de la dirección y de servicio.
- Herramienta: no se pre-recomienda. La Ficha dice que la cliente prefiere Claude y combinarlo con Gemini (marketing y gráfico, plan de 20); el deck nombra Claude y Gemini solo por esa razón y por la verificación de acceso. La asesora prometió a la cliente un comparativo de licencias de Claude con una recomendación: va aparte de la propuesta y debe tratar el mismo punto de acceso.
- Reglas de Detección que se conservan: sin certificado, sin garantía 30-60-90, sin dolor dramatizado ni citas textuales (se omiten «manual, pero manual mal» y «desesperada») y sin nombres de personas del cliente (la CEO no aparece en el deck).
- Facilidad de pago INCLUIDA: a diferencia de las últimas propuestas, la cliente preguntó expresamente si hay formas de pago o cuotas. Sin plan propio de Ventas se usa el estándar (50 % al aprobar, 50 % al cierre) con aviso del generador; los montos son campos editables y vacíos. Ventas debe decidir si ofrece más cuotas, dada la sensibilidad al valor de una pyme de 11 personas.
- Sensibilidad al valor: la asesora pidió un alcance acotado y fácil de decidir. Se respetaron las 5 áreas de la Ficha (22 h). Si se quiere acotar, la opción natural es quitar Marketing (usan Gemini y no es el dolor) para 18 h, pero eso lo decide Ventas con la cliente.
- Retorno en modo método: la Ficha no trae volúmenes ni tiempos por proceso; el Reporte Final los estima con lo que cada área entregue en su sesión (estimación referencial, sin compromiso de resultado).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md y CLAUDE.md §4.21)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo y en qué plazo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos. Sin fechas calendario del cronograma: la ruta es relativa al arranque (semanas).
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Retorno esperado (módulo `retorno` de `datos.json`): sin estudios ni citas de la web. En modo método explica cómo se estima el retorno de cada oportunidad y qué decide el cliente con el Reporte Final, sin compromiso de resultado; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación).
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso.
- El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por` en `datos.json`).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Decidir cómo se trata el acceso a Claude desde Venezuela: el deck propone verificarlo antes de arrancar y usar Gemini como respaldo. Confirmar con la dirección de Intezia y con servicio antes de enviar, y que el comparativo de licencias prometido a la cliente diga lo mismo.
- Definir inversión, descuento y total (campos vacíos para Ventas) y confirmar el plan de pago: se usó el estándar 50/50 porque la cliente preguntó por cuotas, con un valor que calce con una pyme de 11 personas.
- Confirmar con Flavia las fechas, los horarios y el orden de las áreas; el deck solo lleva semanas. La Ficha pide corto plazo (0 a 3 meses).
- Confirmar con la asesora la modalidad (presencial, remota o mixta), que la Ficha no indica, y dónde está la empresa.
- Confirmar si el Reporte Final se entrega en la semana 4 (misma semana de la última sesión) o en la 5.
- Confirmar con Flavia que las 5 áreas se mantienen (22 h) o si se acota (por ejemplo sin Marketing, 18 h).
- Confirmar con Flavia su teléfono, su correo y su cargo en la última slide. Confirmar si el kick-off se cuenta aparte (criterio por defecto) o dentro de las horas.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py metalblanc      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh metalblanc             # verifica, genera el PDF y ajusta los campos
```

## Actualización 2026-10-08 (tarde): documento de licencias y decisión sobre el acceso a Claude

- **Pedido del usuario:** (1) decir en la propuesta que Claude se usa con VPN en Venezuela, que es seguro y que los datos están protegidos; (2) un PDF aparte con el valor de la licencia Team, pago mensual y anual.
- **(1) Lo que NO se escribió:** que usar Claude con VPN en Venezuela es seguro o está permitido. La página oficial de Anthropic (anthropic.com/supported-countries, 08/10/2026) no lista a Venezuela y su política prohíbe el uso estando físicamente en una región no soportada; la VPN puede llevar al bloqueo de la cuenta, que es el miedo de la cliente. Afirmarlo sería inexacto y la expondría a perder la cuenta. **Lo que sí se escribió:** con Claude Team el contenido de la empresa no se usa para entrenar los modelos por defecto (claude.com/pricing y términos comerciales), en la slide 4; el acceso se define antes de arrancar y Gemini queda de respaldo. Si Intezia tiene una confirmación escrita del proveedor que contradiga lo anterior, se actualiza el deck.
- **(2) Documento aparte:** `DET-028 Licencias de Claude Team.pdf` (A4 horizontal, 1 página, fuente `licencias-claude-team.html`). Valores de lista de claude.com/pricing al 08/10/2026, en US$ y sin impuestos: asiento estándar $25 mensual y $20 al mes con pago anual ($240 al año); asiento premium $125 mensual y $100 al mes con pago anual ($1.200 al año). Para 11 asientos estándar: $275 al mes ($3.300 en 12 meses) o $2.640 al año (20 % menos). Referencia: Claude Pro $20 mensual o $17 al mes con pago anual ($200). Incluye una nota de disponibilidad por país. **Volver a consultar claude.com/pricing antes de reenviar:** los valores cambian y una fuente de terceros mostraba $30/$25 y un mínimo de 5 asientos (la página oficial dice «equipos de 2 a 150»).
- **PDF complementario en la carpeta:** el wrapper `pdf-habilidades-compacto.sh` aparta todo `*.pdf`; sacar el de licencias antes de regenerar el deck y devolverlo después.
- El deck ya no dice que el comparativo de licencias «se envía aparte» como recomendación: dice que «el valor de lista de Claude Team va en un documento aparte». La recomendación de licencias sigue en el Reporte Final.

