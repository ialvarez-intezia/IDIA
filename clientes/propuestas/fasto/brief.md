# Brief — Fasto · Calculador de Pedidos Óptimos de Inventario (CAP-104)

## Datos administrativos

- **Cliente**: Fasto · cadena de supermercados, 7 años de operación
- **Naturaleza**: Capacitación in-company · **piloto enfocado en el equipo de Compras (3 personas)** para automatizar el cálculo de pedidos de inventario. El cliente ya tiene el problema diagnosticado y pide la solución directamente — no un proceso de descubrimiento general. La propuesta se construye con el patrón de 3 etapas (Diagnóstico → Construcción (Intezia) → Implementación) en **una sola fase**, sin fase de réplica ni cotización progresiva.
- **Slug**: `fasto`
- **División Intezia**: `educacion` (cliente corporativo)
- **Tipo de documento**: Capacitación (`CAP-104`)
- **Programa**: Calculador de Pedidos Óptimos de Inventario — Fasto
- **Eje temático**: automatización del cálculo de pedidos de reposición con IA, aplicada al equipo de Compras: la IA analiza los datos ya disponibles en el sistema Estelar (stock actual, última cantidad pedida, ventas de 7 y 30 días, precio) y calcula el pedido óptimo considerando el lead time del proveedor y el tiempo de recepción, codificación y almacenamiento, generando automáticamente la orden de compra.
- **Modalidad**: a definir en próxima reunión
- **Duración**: sin horas impuestas, a definir según el diagnóstico con el equipo de Compras
- **Fecha del brief**: 2026-08-13
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Cliente referente**: Javier (impulsor del proyecto del lado de Fasto) · cargo por confirmar

## Por qué este proyecto

Fasto quiere abrir 1 a 2 tiendas nuevas por año, y ese ritmo es justo lo que hace insostenible su proceso actual de pedidos: cada quiebre de stock es una venta que no se recupera, porque el cliente de supermercado no espera y compra en otro lado. La causa raíz ya está identificada, y es lo que hace este caso resoluble: el equipo de Compras (3 personas) no está considerando el lead time del proveedor ni el tiempo de recepción, codificación y almacenamiento al calcular los pedidos — no por negligencia, sino porque ese cálculo hecho a mano, producto por producto, es inviable. El resultado son pedidos que no alcanzan a cubrir la demanda durante todo el lead time.

Javier optó explícitamente por un **piloto enfocado en el equipo de Compras** (no algo general a toda la empresa), para atacar directamente el quiebre de stock y ver resultados inmediatos en las finanzas de Fasto.

## Diagnóstico (5 puntos)

1. Fasto planea abrir 1 a 2 tiendas nuevas por año; ese ritmo de expansión hace insostenible el proceso manual de pedidos que usan hoy.
2. Cada quiebre de stock es una venta que no se recupera: el cliente de supermercado no espera, compra en otro lado.
3. El equipo de Compras (3 personas) calcula los pedidos a mano, producto por producto, sin considerar el lead time del proveedor ni el tiempo de recepción, codificación y almacenamiento.
4. Resultado: piden cantidades que no alcanzan a cubrir la demanda durante el lead time total — no es negligencia, es que ese cálculo manual es inviable a la escala de un supermercado.
5. En el otro extremo, los proveedores a veces entregan de más, generando sobrestock y capital inmovilizado, sin un documento formal para respaldar el rechazo del exceso.

> La data ya existe y está disponible: el equipo descarga de **Estelar** un reporte con stock actual, última cantidad pedida, ventas de 7 y 30 días y precio. El problema es el procesamiento, no la fuente.

## Estructura del proyecto

### Fase única · Piloto equipo de Compras (cotizada) — Etapas 1 a 3

1. **Etapa 1 · Diagnóstico**: mapear con el equipo de Compras las reglas reales de reposición por proveedor/categoría — lead time de cada proveedor y tiempo de recepción, codificación y almacenamiento.
2. **Etapa 2 · Construcción (Intezia)**: Intezia construye el calculador que lee los reportes de Estelar y calcula el pedido óptimo (stock actual + tendencia de ventas + lead time + tiempo de recepción/almacenamiento), generando automáticamente la orden de compra. **Sin sesiones con el equipo** — no consume su tiempo.
3. **Etapa 3 · Implementación**: se activa el calculador con el equipo de Compras y se entrena su uso diario, incluido el uso de la orden de compra generada como **documento formal para rechazar entregas en exceso de los proveedores**.

> Numeración fija: Etapa 1 Diagnóstico · Etapa 2 Construcción · Etapa 3 Implementación. Se usa
> igual en todo el deck (programa, cronograma, roadmap, hoja de precio) y en este brief.
> **No hay Fase 2 ni réplica**: es un piloto de alcance cerrado, sin cotización progresiva.

## Especificaciones del programa

- **Duración**: sin horas impuestas, a definir según el diagnóstico.
- **Modalidad**: a definir en próxima reunión con el cliente (Presencial / Online Síncrono / Híbrido).
- **Audiencia**: equipo de Compras de Fasto, 3 personas.
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.

## Recomendación de herramienta (sugerencia, no restricción)

- Fasto ya tiene **Google Workspace y licencias de Gemini Pro**. Gemini puede leer los reportes de Estelar y generar un análisis general — es un buen punto de partida, ya disponible para el equipo.
- Donde Gemini queda corto es en **llevar el proceso completo con un formato específico y reglas estrictas**: aplicar de forma consistente las reglas de negocio (lead time por proveedor, tiempos de recepción/almacenamiento por categoría) y mantener el formato exacto de la orden de compra, pedido tras pedido, sin desviarse.
- Por eso la propuesta sugiere **sumar Claude** para sostener ese proceso reglado de punta a punta, operando dentro del mismo entorno Google que Fasto ya usa (no se propone migrar de plataforma — ver §4.11).
- Esta mención aparece **una sola vez en el deck** (Etapa 2 · Construcción): la propuesta no gira en torno a comparar Gemini vs. Claude, gira en torno a resolver el quiebre de stock.

## Propuesta económica

- **1 sola hoja de cotización** (`.s-price`), cubre el piloto completo (Etapas 1 a 3). No hay Fase 2 que cotizar de forma progresiva.
- Bloque destacado **"Importante"** con la implicación comercial: el servicio se presta bajo los **términos y condiciones**, aceptados por ambas partes al avanzar con la propuesta.

## Entregables consolidados

- Calculador de pedidos óptimos operando sobre los datos de Estelar.
- Orden de compra generada automáticamente, lista como documento formal frente a los proveedores.
- Informe de diagnóstico con las reglas de reposición mapeadas (lead time y tiempos de recepción/almacenamiento por proveedor/categoría).
- Equipo de Compras capacitado en el uso diario del calculador.
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-104** en INTEZIA Education al cerrar el acuerdo.
- **Objetivo de fondo del cliente**: automatizar para no tener que contratar más personal de Compras a medida que abre tiendas nuevas. El proyecto no compite contra el costo de esta propuesta: compite contra el costo de dos nóminas nuevas.

## Notas de diseño

- Clonado de `canguro/` (a su vez clon de `aerocentro/`, estándar 2026-08-07 de roadmap de 3 etapas). Formato canónico A4 landscape, reducido a **12 slides** (de 16): el cliente pide la solución directamente, sin fase de auditoría extendida ni réplica a otras tiendas, así que se omiten las slides de Fase 2 / réplica progresiva y se colapsan cronograma y roadmap a **una sola instancia cada uno** (no 3 páginas), ya que solo hay 3 etapas y un único equipo (Compras).
- **`.s-schedule`**: 1 sola slide con 3 columnas (Etapa 1 Diagnóstico / Etapa 2 Construcción / Etapa 3 Implementación), en vez de 3 slides separadas — no hace falta una columna de "Recursos" aparte porque el piloto es de un solo equipo pequeño (3 personas) y los recursos (Estelar, cuentas del equipo) se mencionan dentro de cada etapa.
- **`.s-roadmap`**: 1 sola página con **3 nodos en línea** (E1 → E2 → E3 → resultado), no 2-3 páginas. Se extendió el componente `rmx-linear` con un tercer acento de color dentro de la paleta oficial: `.rmx-node-f4` / `.rmx-card-f4` en **blanco sobre negro** (Diagnóstico = amarillo `f2`, Construcción = blanco `f4`, Implementación = naranja `f3`), documentado en `styles.css` local de este deck.
- **`.s-program`**: 3 module cards, una por etapa (I Diagnóstico, II Construcción, III Implementación) — modo "1-3 módulos" del componente, sin necesidad de modo compacto.
- **Recomendación Gemini + Claude**: mencionada una sola vez, en Etapa 2 · Construcción (schedule, roadmap y programa.md), enmarcada en positivo (lo que Claude suma) y nunca como que Gemini "no sirve" (§4.11, §4.13 reglas de copy). El resto del deck no vuelve a comparar herramientas — se enfoca en el problema del cliente (quiebres de stock, sobrestock, expansión sin sumar personal).
- **Sin Fase 2 ni cotización progresiva**: se retiró el párrafo `.cot-progressive` de `.s-price` (no aplica, es un piloto de alcance cerrado) y las menciones a "réplica en la red" del deck de origen.
- **Slide de Impacto** (§4.9): mismos datos reales de cadena de suministro/retail usados en `canguro/` (aplican igual de bien al problema de quiebres de stock de Fasto) — McKinsey, *Succeeding in the AI supply-chain revolution* (2021): +35% en niveles de inventario, hasta 65% en nivel de servicio, −15% en costos logísticos en early adopters de IA en su cadena de suministro. IHL Group, *Inventory Distortion: The Good, the Bad and the Ugly* (2023): 1.77 billones de dólares de costo global anual por distorsión de inventario (fuera de stock + sobrestock). Ambas fuentes citadas verbatim.
- `[CÓDIGO]` sustituido por CAP-104 en Acreditación.
- Reglas §4.11 y §4.13 respetadas: no se afirma que Fasto migra de ningún stack tecnológico (el calculador opera dentro del entorno Google que Fasto ya usa); sin guion largo en el copy de cara al cliente.
- **Asesora comercial**: Verónica Rubio (contacto en slide de cierre y aquí, mismos datos que en `canguro/`).

## Pendientes

- Confirmar modalidad (Presencial / Online Síncrono / Híbrido) en la próxima reunión.
- Confirmar cargo/apellido de Javier y datos de contacto directo.
- Confirmar fechas tentativas de inicio y duración exacta según lo que arroje el diagnóstico.
- Confirmar presupuesto indicativo del piloto.
- Confirmar con el cliente si adquiere licencias de Claude o si Intezia las gestiona como parte del entregable (no discutido en la reunión).
