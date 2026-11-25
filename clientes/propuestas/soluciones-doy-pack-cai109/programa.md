# Programa interno · Soluciones Doy Pack · Servicio de Detección y Habilidades (CAI-109)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (19/11/2026) y resumen de la reunión de Flavia Martínez con las gerencias. Sin transcripción.

## 1. Resumen

- **9 entregables en 3 áreas (más 1 paso previo)**, **41 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Asistentes de IA**: 9 entregables, 41 h.
- Horas por fase: F1 6 h (3 sol.) · F2 2 h (1 sol.) · F3 33 h (5 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Las tres empresas del grupo | Asistentes de IA | Detección previa con las gerencias, Fundamentos de IA, Ventas y Mercadeo, Administración y Almacén | 41 | 9 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Detección (con las 3 gerencias, antes de construir) | Fundamentos (el «paso cero» de todo el equipo) | Construcción (en conjunto, sobre procesos reales) |
|---|---|---|---|
| Las tres empresas del grupo | 6 h · 3 sol. | 2 h · 1 sol. | 33 h · 5 sol. |

- **Detección previa**: Procesos cerrados y herramienta confirmada con las gerencias.
- **Fundamentos**: El equipo sabe instruir a la IA y qué información no se sube.
- **Atención por Instagram**: El agente califica y deriva cada solicitud al área correcta.
- **Compras y pagos**: Cotizaciones, lista semanal y facturas con apoyo de la IA.
- **30 · 60 · 90 días**: Seguimiento: uso, ajustes y tiempo recuperado.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Detección previa con las gerencias · 3 entregables · 6 h · Asistentes de IA · línea A · paso previo

Para qué (lo que ve el cliente): Cerrar los procesos y confirmar la herramienta antes de construir

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DET-1 | Reunión central con las 3 gerencias | Reunión con las tres gerencias del grupo para alinear procesos, prioridades y la herramienta de IA. | - | - | - | 2 | F1 |
| DET-2 | Levantamiento de Ventas y Mercadeo | Levantamiento de la atención por Instagram y WhatsApp: cómo llegan las solicitudes, cómo se filtran y a qué empresa del grupo se derivan. | - | - | - | 2 | F1 |
| DET-3 | Levantamiento de Administración y Almacén | Levantamiento de compras, cuentas por pagar, facturas y históricos, con almacén. | - | - | - | 2 | F1 |

### Fundamentos de IA · 1 entregable · 2 h · Asistentes de IA · línea A

Para qué (lo que ve el cliente): El «paso cero»: que todo el equipo use la IA con criterio y cuide la información

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FUN-1 | Fundamentos: instrucciones, documentos y proyectos (incluye: Cómo darle instrucciones a la IA; Cargar documentos y armar proyectos; Qué información no se debe subir) | Cómo darle instrucciones a la IA, cargar documentos y contexto, armar proyectos y qué información no se debe subir. | - | - | - | 2 | F2 |

### Ventas y Mercadeo · 3 entregables · 25 h · Asistentes de IA · línea A

Para qué (lo que ve el cliente): Un agente que atiende Instagram, filtra al cliente y lo deriva al área correcta

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| VEN-1 | Agente que atiende y califica al cliente | Con el equipo, el agente que atiende lo que entra por Instagram y distingue al emprendedor pequeño del cliente industrial según volumen y producto, con las preguntas técnicas resueltas desde información cargada. | - | - | - | 8 | F3 |
| VEN-2 | Flujo en n8n conectado a la API de Meta | Construcción en n8n del flujo que recibe los mensajes de Instagram por la API de Meta y se los entrega al agente, y devuelve su respuesta. | - | - | - | 10 | F3 |
| VEN-3 | Derivación al área del grupo y pruebas | Derivación de cada cliente a la empresa del grupo que corresponde y pruebas con solicitudes reales, hasta que el flujo funcione. | - | - | - | 7 | F3 |

### Administración y Almacén · 2 entregables · 8 h · Asistentes de IA · línea A

Para qué (lo que ve el cliente): Compras, cuentas por pagar y facturas con menos búsqueda manual

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ADM-1 | Comparativo de cotizaciones y cuentas por pagar | Comparación de las cotizaciones de cada compra y armado de la lista semanal de cuentas por pagar. | - | - | - | 4 | F3 |
| ADM-2 | Facturas y consulta de históricos | Apoyo para cargar facturas y consultar históricos de compras y pagos sin buscar en carpetas. | - | - | - | 4 | F3 |

## 4. Fuera de alcance

- Conexión directa al banco: hoy no es posible; la descarga de pagos sigue como está.
- Conciliación automática: depende de la conexión al banco; se evalúa en la siguiente etapa.
- Informes de indicadores, flujo de caja e inventario: se planifican en la siguiente etapa.
- Licencias de IA y de n8n, y la cuenta de Meta: se confirman en la Detección previa y no están en la inversión.
- Reemplazar el sistema administrativo actual: la IA se apoya en él, no lo sustituye.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (20/11/2026): propuesta CAI-109 para Soluciones Doy Pack con Flavia Martínez como asesora, a partir de la Ficha (19/11/2026) y del resumen de la reunión que pegó Ivana. No hay transcripción: la Ficha y ese resumen son la fuente (§4.23).
- Decisiones de Ivana (20/11/2026): el agente de Instagram va **conectado a Instagram** y, en un segundo mensaje, **25 h de construcción para el agente** porque debe hacerse con **n8n y la API de Meta**; impacto **reenfoque**; y una **hoja extra de gobernanza de datos dentro de la propuesta** (no un PDF aparte), como lámina adicional «Gobernanza de datos». Total **41 h** = detección previa 6 h + fundamentos 2 h + construcción 33 h (agente 25 h + compras y cuentas por pagar 8 h). Ivana había elegido antes 24 h (construcción 16 h, el tope de Flavia). Si las 25 h debían cubrir toda la construcción (6 + 2 + 25 = 33 h), basta bajar las 8 h de compras. División Educación y alianza = no: tomados por mí (primer contacto), no los dio Ivana.
- Combo: la Detección previa va dentro del mismo proyecto como paso previo, con la plantilla de Habilidades y `servicio_rotulo` «Servicio de Detección y Habilidades» (como CAI-032). `meta.json` queda en habilidades (código CAI y servicio de interés de la Ficha). Una sola hoja de inversión con tres tramos descritos (no `inversion.partes`: solo si Ivana lo pide).
- Reparto de horas (decisión mía a partir de lo que dijo Flavia e Ivana): detección previa 6 h = reunión central 2 h + 2 h en Ventas y Mercadeo + 2 h en Administración y Almacén; fundamentos 2 h (el «paso cero» de Lady); construcción 33 h = agente de Instagram 25 h (atiende y califica 8 h, flujo en n8n con la API de Meta 10 h, derivación al área del grupo y pruebas 7 h) + compras y cuentas por pagar 8 h (cotizaciones y lista 4 h; facturas e históricos 4 h). El calendario (sesiones de 2 h) va al kickoff, no a la propuesta (§4.23).
- Agente de Instagram conectado con **n8n y la API de Meta** (Ivana, 20/11/2026): se nombran en «Cómo trabajamos», el entregable y la inversión. La viabilidad (cuenta de Meta para empresas, permisos y aprobación de la API, dónde se aloja n8n) no está validada: el deck dice que se confirma en la Detección previa, antes de comprometer la construcción. n8n y la cuenta de Meta quedan fuera de la inversión. Con 25 h esta parte es más desarrollo que formación: alinear con Flavia cómo se lo presentó al cliente (construcción en conjunto).
- Quedan fuera (siguiente etapa): conexión directa al banco (se les dijo que hoy no es posible), conciliación automática, informes de indicadores, flujo de caja e inventario. Flavia nombró «indicadores e inventario» como fase 2 y el pedido original incluía informes de indicadores y flujo de caja: confirmar que el flujo de caja también pasa a la fase 2. Reemplazar los sistemas administrativos y el Excel (expectativa de la Ficha) queda fuera: la IA se apoya en ellos.
- Herramienta de IA sin nombrar: la Detección previa la confirma. Hoy usan Gemini gratuito y Claude gratuito (se agotó el límite), sin licencias. No se pre-recomienda ninguna, no se habla de VPN ni se garantiza nada sobre las cuentas (Claude no está soportado en Venezuela).
- Gobernanza de datos (lámina adicional, `respuesta_solicitud`): responde lo que preguntaron las gerencias (filtración, VPN y Venezuela, separación entre cuentas) sin explicar la filtración que escucharon (no la conocemos) y sin prometer acceso ni seguridad. «Un espacio por empresa del grupo» y «sin cuentas compartidas» son reglas de diseño mías: confirmar con Ivana.
- Participantes: 3 gerencias más 2 o 3 analistas (compras y administración, y mercadeo); la Ficha dice que podrían sumarse hasta 3 personas más. El número exacto está sin cerrar. Mary insistió en que los agentes son sobre todo para los analistas. No se nombra a ninguna persona del cliente.
- Sin citas ni dolor dramatizado: los hechos de la portada son datos de la Ficha parafraseados (6 solicitudes al día, ~3 h por conversación que no califica, cotizaciones a mano, históricos en carpetas). Las 6 solicitudes y las 3 h son cifras declaradas por el cliente, sin medir.
- Sin facilidad de pago (omitir: pago, regla permanente de Ivana). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23). Modalidad presencial en sus oficinas (Ficha). Las gerencias quieren que María Prin, quien decide y firma, esté en la presentación.
- Contacto de la última slide: Flavia Martínez, asesora comercial; correo y teléfono tomados de DET-060 y DET-061, no confirmados.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se cierran los procesos y la herramienta; luego se aprende lo básico; solo entonces se construye sobre procesos reales.

- **Construimos**: Con el equipo, sobre sus procesos reales.
- **Probamos**: Con solicitudes y compras reales, hasta que funcione.
- **Adoptamos**: El equipo usa los agentes en su día a día.
- **Medimos**: El tiempo recuperado, a 30, 60 y 90 días.

- En la práctica, **Herramienta a confirmar**: La Detección previa confirma qué herramienta y qué plan conviene, con sus condiciones de privacidad y de acceso.
- En la práctica, **Conexión a Instagram**: Se construye en n8n con la API de Meta; su viabilidad (cuenta de Meta para empresas y permisos) se confirma en la Detección previa.
- En la práctica, **Los analistas, protagonistas**: Los agentes son sobre todo para los analistas, que los usan a diario; las gerencias los consultan.
- Datos: Los datos del banco, de clientes y de pagos no se cargan a la IA sin el visto bueno de las gerencias: se trabaja con los ejemplos que autoricen. Ver la hoja de gobernanza de datos.
- Quién construye: Intezia guía y el equipo construye con IA sus propios agentes y skills, sobre sus procesos reales, para mantenerlos solo.

**Logística:** modalidad: Presencial, en las oficinas de Soluciones Doy Pack. · participantes: Las 3 gerencias y de 2 a 3 analistas; el número exacto se confirma al arrancar. · ritmo: Según la agenda del equipo, sin frenar la operación diaria. · arranque: En cuanto se aprueba, se coordina el arranque con las gerencias..

## 7. Retorno esperado (slide 7)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con el agente; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 6)

Enfoque decidido con Ivana: **reenfoque**. Las personas pasan a trabajo de más valor; no se habla de menos personas ni de nómina.

> Gerentes y analistas recuperan tiempo del trabajo repetitivo y de la búsqueda de documentos, para dedicarlo a decidir y a atender mejor a los clientes que sí califican.

## 9. Próximos pasos (slide 9)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

