# Programa interno · Ocean Marine Service International LLC · Servicio de Habilidades (CAI-096)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Documento de requerimiento de OMS (alcance de recepción, Odoo, validación, proveedores, comparativos, catálogo y control) sin Ficha Comercial ni transcripción de la reunión.

## 1. Resumen

- **13 entregables en 4 bloques**, **100 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Agente de compras**: 13 entregables, 100 h.
- Horas por fase: F1 7 h (2 sol.) · F2 48 h (7 sol.) · F3 45 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Opción A · En casa | Agente de compras | A · Levantamiento con Stores, A · Agente construido en casa, A · Testeo y adopción con Stores | 50 | 10 |
| Opción B · En conjunto | Agente de compras | B · Construido junto a Stores | 50 | 3 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Base (levantamiento con Stores) | Agente (desarrollo en casa) | Uso (adaptación y pruebas) |
|---|---|---|---|
| Opción A · En casa | 5 h · 1 sol. | 25 h · 6 sol. | 20 h · 3 sol. |
| Opción B · En conjunto | 2 h · 1 sol. | 23 h · 1 sol. | 25 h · 1 sol. |

- **Arranque**: Se acuerdan el calendario, los accesos y los primeros requerimientos reales.
- **Levantamiento**: Stores explica cómo llegan y se aprueban hoy los requerimientos.
- **Agente construido**: En casa (A) o junto a Stores (B), listo para probar.
- **Pruebas reales**: Un requerimiento recorrido del correo a la compra lista para aprobar.
- **30 · 60 · 90 días**: Seguimiento: uso, ajustes y tiempo recuperado.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### A · Levantamiento con Stores · 1 entregable · 5 h · Agente de compras · línea A

Para qué (lo que ve el cliente): Entender cómo llegan hoy los requerimientos y qué se revisa y aprueba.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| LEV-1 | Levantamiento de requerimientos y reglas (incluye: Cómo llegan hoy los requerimientos y qué se aprueba; Reglas de aprobación y quién autoriza cada compra) | Referencia interna: levantamiento con el equipo de Stores de cómo llegan los requerimientos, qué revisa cada quien y las reglas de aprobación. | - | - | - | 5 | F1 |

### A · Agente construido en casa · 6 entregables · 25 h · Agente de compras · línea A

Para qué (lo que ve el cliente): Intezia construye el agente sin el equipo: lee, valida, cotiza y compara.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AGE-1 | Lectura de correos y adjuntos (incluye: Correo y adjuntos, en ambos idiomas; Barco, puerto, fecha, artículos, cantidades y códigos IMPA; Consultas por los datos que faltan, sin inventar especificaciones) | Referencia interna: lectura de correos y adjuntos en Excel, PDF e imágenes, en inglés y español; barco, puerto, fecha, artículos, cantidades, unidades, marcas, modelos, referencias y códigos IMPA; consultas por datos faltantes; vínculo de cada artículo al requerimiento original y control de revisiones. | - | - | - | 4 | F2 |
| AGE-2 | Conector de solo lectura a Odoo (incluye: Consulta por la API externa de Odoo, solo lectura; Productos, proveedores, existencias y reservas; Cotizaciones, órdenes, recepciones y facturas) | Referencia interna: consulta por la API externa de Odoo.sh (XML-RPC o JSON-RPC), con un usuario de solo lectura creado por OMS, de productos, proveedores, existencias, reservas, cotizaciones, órdenes de compra, recepciones y facturas; sin modificar registros ni instalar módulos dentro de Odoo. | - | - | - | 4 | F2 |
| AGE-3 | Clasificación de productos (incluye: Historial comprobable, registrado sin validar, posible equivalente o nuevo; Muestra los registros de Odoo que respaldan cada clase) | Referencia interna: búsqueda por código, marca, modelo, referencia y descripción, con revisión de la evidencia documental; cada producto queda en una de cuatro clases, con los registros que la respaldan. | - | - | - | 4 | F2 |
| AGE-4 | Solicitudes de cotización a proveedores | Referencia interna: consulta de proveedores históricos y búsqueda de nuevas opciones; solicitudes de cotización preparadas como borrador; distingue valor publicado, cotización recibida y disponibilidad confirmada, con fuente y fecha. | - | - | - | 4 | F2 |
| AGE-5 | Comparativo y compra recomendada (incluye: Ofertas lado a lado y total hasta el destino; La más económica, la más rápida y la recomendada, con su criterio; En pantalla y en Excel, con vínculos a las cotizaciones) | Referencia interna: cuadro comparativo por artículo con las ofertas lado a lado, sobre una misma base de cantidades, unidades y moneda; mejor opción por artículo y combinación recomendada del pedido completo; la más económica, entrega más rápida y recomendada; consulta en pantalla y exportación a Excel con vínculos a las cotizaciones. | - | - | - | 7 | F2 |
| AGE-6 | Fichas nuevas y base de conocimiento | Referencia interna: propuesta de ficha para productos nuevos, con búsqueda previa de duplicados y sin crear ni modificar productos en Odoo; correcciones y equivalencias aprobadas en una base de conocimiento que administra OMS. | - | - | - | 2 | F2 |

### A · Testeo y adopción con Stores · 3 entregables · 20 h · Agente de compras · línea A

Para qué (lo que ve el cliente): El agente ajustado a Stores, probado con casos reales y en uso.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ADA-1 | Adaptación del agente a Stores | Referencia interna: ajuste del agente a las reglas, formatos y criterios de Stores, con el equipo. | - | - | - | 5 | F3 |
| ADA-2 | Pruebas con requerimientos reales | Referencia interna: pruebas con requerimientos reales (productos con historial, fichas incompletas, productos nuevos y posibles equivalencias) y validación de comparativos, conversiones de unidades, totales y fechas de entrega. | - | - | - | 7 | F3 |
| ADA-3 | Adopción, documentación y accesos | Referencia interna: adopción del agente por el equipo de Stores, entrega de la documentación y de los accesos a OMS, y recorrido completo desde el correo hasta una propuesta de compra verificable lista para aprobación. | - | - | - | 8 | F3 |

### B · Construido junto a Stores · 3 entregables · 50 h · Agente de compras · línea B

Para qué (lo que ve el cliente): El mismo agente, construido en vivo con el equipo de Stores y luego testeado.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| OPB-0 | Levantamiento dentro de la construcción | Referencia interna: el levantamiento con Stores se hace dentro de los primeros encuentros de las 25 h de construcción (2 h de ellas); en el deck se muestra «Incluido». | - | - | - | 2 | F1 |
| OPB-1 | Construcción del agente con Stores (incluye: Los mismos módulos del agente, construidos en vivo con Stores; Levantamiento dentro de los primeros encuentros) | Referencia interna: construcción del agente junto al equipo de Stores, en vivo; el levantamiento se hace dentro de los primeros encuentros. Mismos módulos que la opción A: lectura de correos, conector de solo lectura a Odoo, clasificación, cotizaciones, comparativo y fichas nuevas. | - | - | - | 23 | F2 |
| OPB-2 | Testeo y adopción con Stores (incluye: Pruebas con requerimientos reales y adaptación; Adopción, documentación y accesos) | Referencia interna: 25 h más para testear con requerimientos reales, adaptar, adoptar y entregar la documentación y los accesos. | - | - | - | 25 | F3 |

## 4. Fuera de alcance

- Escribir en Odoo, crear productos, enviar correos, emitir órdenes o aceptar sustituciones: requieren autorización expresa.
- Licencias y servicios de terceros (Odoo, correo, modelo de IA): los define y contrata OMS.
- Operación y mantenimiento posteriores al proyecto: se cotizan aparte.

## 5. Supuestos a confirmar (antes del método)

- Servicio y cuenta (instrucciones de Ivana, 12/11/2026): Habilidades, plantilla compacta v3, Educación y sin alianza (confirmados con Ivana). Código **CAI-096**: Ivana lo pidió bajo CAI-095, que ya se usó para Médica Campestre; ella aceptó CAI-096 para Ocean Marine Service.
- **Dos opciones (Ivana, 12/11/2026, segunda ronda):** el requerimiento pedía presentar ambas y Ivana pidió reflejarlas. **Opción A:** desarrollo en casa (20 h asíncronas sin el equipo) y 20 h síncronas con Stores (levantamiento, adaptación, testeo y adopción). **Opción B:** se construye con Stores 20 h y 20 h más para testear y adoptar (el levantamiento va dentro de la construcción). Ambas de 40 h (luego 50 h, ver «Subida a 50 h»); se elige una. Se reflejan en alcance, ruta, método y dos hojas de inversión (`inversion.etapas`, con valor, descuento y total propios).
- Horas (Ivana, 12/11/2026): 40 h por opción (subidas a 50 h el 13/11/2026, ver «Subida a 50 h»). A = 20 h asíncronas sin el equipo + 20 h síncronas (reparto mío: levantamiento 4, adaptación 4, pruebas 6, adopción y documentación 6; las 20 h asíncronas se reparten 3 + 3 + 3 + 3 + 6 + 2 entre los módulos del agente). B = 20 h de construcción con el equipo + 20 h de testeo y adopción. Ivana pidió mostrar las horas asíncronas (excepción a ocultar las de Intezia, §4.23 punto 4). Ojo: `{h_total}` suma 80 (las dos opciones); el deck escribe las horas a mano.
- Alcance: sale del requerimiento de OMS, sin agregar nada. Recepción (correo y adjuntos Excel, PDF e imágenes, inglés y español), conector de solo lectura a Odoo v18, validación en cuatro clases, proveedores y solicitudes de cotización, comparativo por artículo y combinación recomendada con Excel, fichas de producto nuevo con base de conocimiento, y control (aprobaciones, pendientes, accesos y registro). La primera fase no escribe en Odoo, no envía correos ni emite órdenes.
- Sin herramienta de IA nombrada: el requerimiento no la define; se acuerda en el levantamiento. Odoo v18 se nombra como entorno del cliente al que el agente se integra (§4.11); no se afirma migración.
- El requerimiento pide también arquitectura, costos de desarrollo, operación y mantenimiento, seguridad y soporte: el deck cubre seguridad (solo lectura, accesos restringidos y registro) y deja la **operación y el mantenimiento posteriores como cotizados aparte** (supuesto mío). La arquitectura detallada se presentará en vivo.
- El requerimiento no dice país, moneda ni modalidad de OMS (LLC): la hoja de inversión sale con REF y la leyenda de pago a tasa BCV (automático); se apaga con `inversion.sin_ref` si facturan en otra moneda. Sin nombres de personas del cliente (solo el cargo del Director de Logística).
- Impacto (Ivana, 12/11/2026): enfoque **operación**; texto sin cifras.
- Sin facilidad de pago (Ivana, 12/11/2026): el deck no lleva la lámina de pago (`omitir: ["pago"]`); la hoja de inversión sigue con valor, descuento y total vacíos para ventas.
- Opción B: el levantamiento va dentro de las 25 h de construcción; internamente se anota como 2 h (OPB-0) + 23 h (OPB-1) porque el generador no admite 0 h. El deck muestra «Incluido» y «25 h».
- **Respuestas de OMS a las preguntas de viabilidad (13/11/2026):** su Odoo 18 está en **Odoo.sh**, que admite la API externa por XML-RPC y JSON-RPC; el usuario de integración será de solo lectura; y OMS puede habilitar una clave de API de un modelo de IA para el desarrollo. Con eso el deck dejó de condicionar el conector a «alojamiento y accesos»: lo afirma como confirmado por el cliente (método, entregable del conector, fuera de alcance y próximos pasos: «Usuario y clave»). Sin n8n ni protocolo en las láminas, solo «API externa».
- **Subida a 50 h (Ivana, 13/11/2026):** cada opción pasa de 40 a 50 h; Ivana no dijo dónde van las 10 h extra, así que las repartí a partes iguales (+5 y +5, reparto mío). A: 25 asíncronas (lectura de correos 4, conector 4, clasificación 4, cotizaciones 4, comparativo 7, fichas 2) + 25 síncronas (levantamiento 5, adaptación 5, pruebas 7, adopción y documentación 8). B: 25 de construcción (levantamiento incluido, 2 + 23 internas) + 25 de testeo y adopción. `{h_total}` suma 100.
- **Una sola hoja de cotización (Ivana, 13/11/2026):** se quitó `inversion.etapas`: las dos opciones de 50 h comparten una hoja con un solo valor, descuento y total, y la nota dice que el valor es el mismo para A y B (supuesto que sigue de pedir una sola hoja). La hoja resume ambas opciones en la duración y el programa.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se construye el agente, sin el equipo o con él; después se testea y se adopta con Stores, con sus requerimientos reales.

- **Levantamos**: Con el equipo de Stores.
- **Construimos**: En casa o en conjunto.
- **Probamos juntos**: Con requerimientos reales.
- **Adoptamos**: Stores lo usa y lo administra.

- En la práctica, **Opción A · en casa**: Intezia construye el agente de forma asíncrona (25 h) y luego Stores lo testea y lo adopta en 25 h síncronas.
- En la práctica, **Opción B · en conjunto**: Se construye junto al equipo de Stores (25 h) y se dedican 25 h más a testear y adoptar.
- En la práctica, **Casos reales**: Productos con historial, fichas incompletas, nuevos y posibles equivalencias.
- Datos: Odoo se consulta por su API externa con un usuario de solo lectura que crea OMS: nada se modifica. Enviar correos, emitir órdenes o aceptar sustituciones requiere autorización expresa, y las acciones quedan registradas.
- Quién construye: Opción A: Intezia construye sin el equipo. Opción B: se construye junto al equipo de Stores.

**Logística:** modalidad: A: construcción asíncrona y encuentros síncronos. B: todo síncrono. Remota o presencial, por acordar. · participantes: El equipo de Stores y materiales técnicos de OMS: 4 personas, con el Director de Logística. · ritmo: Según la agenda de Stores, sin frenar su operación diaria. · arranque: OMS confirma las fechas; la reunión de arranque acuerda el calendario y los accesos..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Requerimientos por mes; Tiempo actual; Tiempo con el agente; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> Cada requerimiento llega a la aprobación con sus productos validados, sus ofertas comparadas sobre una misma base y su total hasta el destino. Compras más rápidas, con trazabilidad y control, y sin que nada se compre sin aprobación.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

