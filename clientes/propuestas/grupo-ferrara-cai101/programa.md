# Programa interno · Grupo Ferrara · Servicio de Habilidades y Políticas (CAI-101)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento + transcripción de la reunión con el cliente. Primer contacto de Intezia con esta empresa: sin informe de Detección propio..

## 1. Resumen

- **9 soluciones en 3 áreas**, **35 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Claude**: 9 soluciones, 35 h.
- Horas por fase: F1 21 h (5 sol.) · F2 14 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Marketing: contenido que convierte | Claude | Marketing | 16 | 4 |
| Ventas: propuestas en minutos | Claude | Ventas | 16 | 2 |
| Políticas: marco y comité de IA | Claude | Políticas | 3 | 3 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Primeras soluciones (dashboard, cotizador y manual de políticas) | Escala y automatización (réplica automática, conexión y comité de IA) |
|---|---|---|
| Marketing: contenido que convierte | 9 h · 2 sol. | 7 h · 2 sol. |
| Ventas: propuestas en minutos | 10 h · 1 sol. | 6 h · 1 sol. |
| Políticas: marco y comité de IA | 2 h · 2 sol. | 1 h · 1 sol. |

- **Arranque**: Accesos listos, cuenta corporativa activa y la librería de productos cargada.
- **Primeros resultados**: Dashboard, cotizador inicial y manual de políticas operando.
- **Escala**: Réplica automática de contenido, cotizador conectado y comité de inteligencia activo.
- **Cierre**: El equipo usa las herramientas por su cuenta; empieza la garantía a 30, 60 y 90 días.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Marketing · 4 soluciones · 16 h · Claude · línea A

Para qué (lo que ve el cliente): Medir qué contenido convierte de verdad y replicarlo automáticamente en cada red

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| MKT-1 | Dashboard de rendimiento de creativos orgánicos y pagos | Dashboard conectado a Claude, Meta, la base de datos interna y Grafana. Mide creativos orgánicos y pagos por conversión, no solo por viralidad, y resume el rendimiento diario. | - | - | - | 6 | F1 |
| MKT-2 | Monitor de contenido de marcas de referencia del sector | Apify conectado a Claude para rastrear el contenido de marcas de referencia del sector (lujo), como insumo de inspiración para las piezas propias. | - | - | - | 3 | F1 |
| MKT-3 | Asistente de redacción y edición de piezas por canal | Claude redacta, ajusta colores y animaciones, y prepara la publicación y la segmentación de cada pieza para Meta, YouTube y TikTok. | - | - | - | 4 | F2 |
| MKT-4 | Sistema que replica los creativos ganadores por canal | El sistema identifica los creativos ganadores por conversión y genera automáticamente variantes para cada canal, incluidos YouTube y TikTok, hoy poco explotados. | - | - | - | 3 | F2 |

### Ventas · 2 soluciones · 16 h · Claude · línea B

Para qué (lo que ve el cliente): Generar una propuesta de diseño con cotización en minutos, en vivo con el cliente

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| VTA-1 | Cotizador de propuestas con la librería de productos cargada | Cotizador construido sobre la librería interna de 5.000 productos (códigos y medidas), para armar una propuesta estética con cotización en minutos, en la misma reunión con el cliente. | - | - | - | 10 | F1 |
| VTA-2 | Conexión del cotizador con el sistema de gestión del inventario | Conecta el cotizador con el sistema de gestión del inventario de Ferrara, vía API, para que la propuesta refleje existencias y precios reales. Suma capacidades de render tridimensional más avanzadas. | - | - | - | 6 | F2 |

### Políticas · 3 soluciones · 3 h · Claude · línea C

Para qué (lo que ve el cliente): Centralizar el uso de IA en una sola cuenta corporativa, con reglas y accesos claros

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| POL-1 | Manual de políticas de uso de IA, con roles y accesos | Manual de políticas de uso de IA: una sola cuenta corporativa en lugar de licencias sueltas, con roles, permisos y reglas de uso para los tres equipos. | - | - | - | 1 | F1 |
| POL-2 | Protocolo de protección de la librería interna de productos | Protocolo para que la librería interna de 5.000 productos y la información de clientes no se pierdan ni salgan de la empresa cuando alguien del equipo se va. | - | - | - | 1 | F1 |
| POL-3 | Comité de inteligencia: criterios de aprobación de contenido | Comité de inteligencia que valida el contenido antes de publicarse, con criterios de estética, información, comunicación y conexión con el público. | - | - | - | 1 | F2 |

## 4. Fuera de alcance

- El sistema de gestión del inventario de Ferrara: se integra lo que ya tengan listo, sin intervenir en ese proceso.
- Publicar en redes o cerrar ventas en nombre del equipo: las herramientas preparan, las personas deciden.
- Render tridimensional avanzado de los diseños: queda para una fase posterior, fuera de este alcance.
- Las licencias de las herramientas de IA: van aparte (detalle en la inversión).

## 5. Supuestos a confirmar (antes del método)

- Combo Habilidades + Políticas registrado en meta.json como servicio: habilidades (servicio_rotulo: «Servicio de Habilidades y Políticas»), siguiendo el mismo criterio que Andrómeda DET-016 (combo Detección + Políticas bajo deteccion, confirmado con Ivana el 2026-11-17): no hay un formato propio para Políticas, así que se representa como una línea de trabajo más, con sus propios entregables y su propia parte en la inversión (inversion.partes).
- No se nombra el sistema de gestión (Odoo) ni su migración en el deck (§4.11): Ferrara ya está migrando de Profit a Odoo por su cuenta; el cotizador se conecta a «su sistema de gestión» en el texto de cara al cliente, y el detalle interno (Odoo) vive en las soluciones[].detalle, que es interno (programa.md).
- Sin informe de Detección previo (primer contacto de Intezia con esta empresa, según la Ficha): los «para_que» y las soluciones salen de la Ficha de Levantamiento y de la transcripción de la reunión, no de un informe propio de Ferrara.
- No se muestra en el deck la cantidad de consultores de Intezia que cubren las tres líneas de trabajo (la Ficha menciona «hasta 3 consultores» para el arranque): dato interno para la coordinación del kickoff, no para la propuesta (regla permanente de Ivana del 2026-10-27, sin_horas_trabajo: true).
- Sin datos propios del cliente para el retorno (horas-hombre, valor de la hora, volumen exacto de ventas): modo metodo.
- entregables.impacto con enfoque «operacion»: el equipo de marketing y ventas mantiene su tamaño (12 personas) y gana velocidad y alcance; no se plantea operar con menos personas ni se habla de nómina.
- Facilidad de pago omitida (omitir: ["pago"]): la Ficha no trae un plan de cuotas propio; se puede agregar si se confirma con Ventas.
- Herramienta de IA sin elegir todavía por el cliente (la Ficha dice «aún no lo saben, esperan la recomendación»): el carril del deck es Claude, consistente con lo recomendado en la transcripción para Marketing, Dirección/Tecnología y el marco de gobernanza; el cotizador de Ventas se describe sin nombrar una herramienta de diseño de terceros (iHouse, Cojum) porque esas no son una recomendación de Intezia, sino lo que el cliente ya exploró por su cuenta.
- Horas visibles (Ivana, 2026-11-17): 16 h con el equipo en Habilidades Marketing y 16 h en Habilidades Ventas (suman exactamente las soluciones MKT y VTA); Políticas no muestra horas (sus 3 h de soluciones son internas, solo viven en programa.md). Son horas con el equipo del cliente, no de trabajo interno de Intezia (sin_horas_trabajo).

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se ordena el criterio y los datos de cada equipo; después se automatiza, y al final se mide el resultado.

- **Construimos**: Con los tres equipos, sobre sus datos y su librería reales.
- **Probamos**: Sobre sus piezas, sus propuestas y su librería reales, hasta que funcione.
- **Adoptamos**: Cada equipo lo usa en su día a día, bajo el mismo criterio.
- **Medimos**: El alcance y la velocidad ganados, a 30, 60 y 90 días.

- En la práctica, **Una sola cuenta corporativa**: No licencias sueltas por persona: todo el equipo trabaja bajo el mismo criterio y la información no se pierde cuando alguien se va.
- En la práctica, **Claude se integra a su operación**: Se suma a Google Workspace y al sistema de gestión que ya usan; no reemplaza nada de lo que ya funciona.
- En la práctica, **La librería de productos queda protegida**: Los 5.000 productos con sus códigos y medidas son información confidencial: se trabaja con accesos controlados, no con copias sueltas.
- Datos: La librería interna de 5.000 productos y la información de clientes son datos sensibles: se definen accesos por rol y la cuenta corporativa evita que la información se pierda si alguien del equipo se va.
- Quién construye: Se construye en vivo con los equipos de Marketing, Ventas y Dirección/Tecnología, sobre sus casos y su librería reales.

**Logística:** modalidad: Presencial, en las oficinas de Grupo Ferrara. · participantes: Equipo de Marketing, Ventas y Dirección/Tecnología: 12 personas en total. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: En cuanto se aprueba, Grupo Ferrara está abierto a arrancar de inmediato con las tres líneas a la vez..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tiempo por propuesta; Volumen de contenido; Qué convierte; Adopción del criterio; Propuestas cerradas en vivo.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> El equipo de marketing pasa a medir qué convierte de verdad; Ventas cierra en minutos lo que hoy toma más de un día; y la empresa trabaja con la IA bajo un mismo criterio, con su librería protegida.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

