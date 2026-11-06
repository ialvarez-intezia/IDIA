# Programa interno · Canguro · Servicio de Habilidades (CAI-086)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Transcripción de la reunión con Canguro (05/11/2026).

## 1. Resumen

- **5 entregables en 3 partes del proceso**, **40 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **BigQuery y Apps Script**: 5 entregables, 40 h.
- Horas por fase: F1 16 h (2 sol.) · F2 24 h (3 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Repatriación y surtido | BigQuery y Apps Script | Levantamiento y clasificación, Surtido y repatriación, Retorno del proceso | 40 | 5 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Base (levantar el proceso y clasificar las tiendas) | Uso (surtido, repatriación y tablero de retorno) |
|---|---|---|
| Repatriación y surtido | 16 h · 2 sol. | 24 h · 3 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario, quiénes participan y el acceso a los datos.
- **Proceso levantado**: Cómo funciona hoy, el flujo ideal y las tiendas clasificadas; define el diseño.
- **Surtido y repatriación**: Los productos clave y los traslados sugeridos, en uso.
- **Retorno a la vista**: El tablero muestra el tiempo, las posiciones y la venta recuperados.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Levantamiento y clasificación · 2 entregables · 16 h · BigQuery y Apps Script · línea A

Para qué (lo que ve el cliente): Levantar cómo se mueve hoy un producto, documentar el proceso ideal y clasificar las tiendas

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| BA-1 | Manual del proceso y flujo ideal | Ocho horas de construcción, testeo y adopción con el equipo. Es el levantamiento: no existe un manual del proceso, así que se registra cómo se mueve hoy un producto, desde la compra y la recepción en el centro de distribución hasta la tienda, quién decide en cada paso y con qué datos, y se validan las bases de datos. Lo que se encuentre define el diseño de las demás piezas. Se construye el flujo ideal, se prueba con casos reales y el equipo lo adopta. Entrega el manual y el flujo. | 5 | 1 | 2 | 8 | F1 |
| BA-2 | Clasificación de tiendas por metraje y venta | Ocho horas de construcción, testeo y adopción con el área de datos. Las tiendas se agrupan por tamaño y las de una misma clase se tratan igual, aunque una tienda grande del interior no venda como una de Valencia. Con lo levantado se define el criterio y se construye una clasificación por metraje y venta, con la imagen de cada grupo: lo que debe tener en surtido. Entrega la clasificación en uso. | 4 | 2 | 2 | 8 | F1 |

### Surtido y repatriación · 2 entregables · 20 h · BigQuery y Apps Script · línea A

Para qué (lo que ve el cliente): Que los productos clave no falten donde más se venden y trasladarlos sin hacerlo a mano

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SR-1 | Surtido de los productos clave por tienda | Ocho horas de construcción, testeo y adopción con Compras. Unos 10 de cada 1.000 productos generan el 80 % de la venta y faltan en las tiendas que más venden. Con la clasificación y los datos levantados se construye el surtido de esos productos por tienda, según la imagen de su grupo, y se prueba antes de usarlo. Depende de BA-2. Entrega el surtido en uso. | 4 | 2 | 2 | 8 | F2 |
| SR-2 | Repatriación sugerida entre tiendas | Doce horas de construcción, testeo y adopción con el equipo de Logística. Hoy repatriar productos entre tiendas lo hacen los supervisores regionales de forma manual y no hay un proceso ágil. Sobre el flujo ideal y los datos de BigQuery se construye una sugerencia de qué traslados hacer y dónde; se prueba con traslados reales y una persona valida antes de ejecutar. Entrega la repatriación en uso. | 6 | 3 | 3 | 12 | F2 |

### Retorno del proceso · 1 entregable · 4 h · BigQuery y Apps Script · línea A

Para qué (lo que ve el cliente): Medir el tiempo, las posiciones y la venta recuperados frente al punto de partida

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| RE-1 | Tablero de retorno: tiempo, posiciones y venta | Cuatro horas de construcción, testeo y adopción con el área de datos. Se construye el tablero que muestra, contra el punto de partida, las horas recuperadas, las posiciones que se reducen o no hace falta cubrir y la venta recuperada, frente al gasto de operar. Usa las herramientas de reporte que ya usa el equipo y sirve para presentar el retorno a la dirección. Depende de las demás piezas. Entrega el tablero en uso. | 2 | 1 | 1 | 4 | F2 |

## 4. Fuera de alcance

- Licencias de IA y el consumo de BigQuery, si aplica: los asume Canguro, aparte de esta inversión.
- Cambiar sistemas: Odoo, SimplyPost y la base de datos no se modifican; se usan los datos que entregan.
- Mover la mercancía: la operación física sigue en manos del equipo de Canguro.
- Otros procesos de Canguro, como comercio electrónico y finanzas: se mapean en una etapa posterior.

## 5. Supuestos a confirmar (antes del método)

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

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se levanta el proceso: lo que se encuentre define qué se construye y cómo. Después se arman el surtido y la repatriación, y al final el tablero.

- **Levantamos**: Cómo se mueve hoy un producto, quién decide y con qué datos. De ahí sale el diseño.
- **Construimos**: Cada pieza del proceso, con el equipo y sobre casos reales.
- **Testeamos**: Probamos cada pieza con datos reales hasta que funciona.
- **Adoptamos**: Cada persona la usa en su trabajo; seguimos a 30, 60 y 90 días.

- En la práctica, **Una persona decide**: La herramienta sugiere traslados y surtido; el supervisor o el comprador valida antes de ejecutar.
- En la práctica, **Dentro de Google**: Se construye con BigQuery y Apps Script, sin servidores ni programas nuevos que mantener; la herramienta de IA se define en el levantamiento.
- En la práctica, **Ya se ha hecho**: Con un cliente conectamos las ventas de caja con compras, almacén y recepción para saber qué comprar; hoy está en uso.
- Datos: Se trabaja con los datos que entregan BigQuery, Odoo y SimplyPost, con cuentas de la empresa y los accesos que autoriza su equipo de datos. Se validan primero con el equipo y los sistemas no se modifican.
- Quién construye: Se construye con las 5 personas del equipo: Intezia guía y cada una prueba cada pieza sobre sus propios casos, dentro del entorno Google que ya usan.

**Logística:** modalidad: Presencial, como prefiere Canguro; un esquema mixto si hace falta. · participantes: 5 personas de Canguro que intervienen en el proceso: logística, compras y datos. · ritmo: Se agenda sin frenar la operación en temporada alta. · arranque: Apenas se apruebe la propuesta; una reunión de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

**Posiciones y nómina (planteadas de frente).** Aval registrado: Gonzalo (Canguro), según el mensaje de la asesora Verónica Rubio · 2026-11-05 · mensaje de la asesora, pasado por Ivana. Confirmar que sigue vigente antes de enviar y antes de circular el documento entre líderes de área.

Pasos del método: Punto de partida; Con el proceso nuevo; Horas recuperadas; Posiciones; Venta recuperada; Gasto de operar.

## 8. Próximos pasos (slide 9)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

