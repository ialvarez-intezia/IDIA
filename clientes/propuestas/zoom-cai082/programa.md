# Programa interno · Zoom · Servicio de Habilidades (CAI-082)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Plan piloto de monitoreo v2 (25/10/2026) y correos entre María Iribarren y Zoom (26/10 al 03/11/2026); sin Ficha de Levantamiento ni transcripción.

## 1. Resumen

- **6 entregables en 5 bloques**, **40 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Servidor MCP de Zoom**: 6 entregables, 40 h.
- Horas por fase: F1 6 h (1 sol.) · F2 26 h (3 sol.) · F3 8 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Servicios de {cliente_corto} vía MCP | Servidor MCP de Zoom | Diseño de las herramientas, Consultas: tarifas, tracking, estatus, Creación de guías, Prueba con un comercio simulado, Documentación y traspaso | 40 | 6 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Diseño (levantamiento técnico y diseño de las herramientas) | Construcción (consultas, creación de guías y comercio simulado) | Traspaso (documentación y traspaso al equipo de TI) |
|---|---|---|---|
| Servicios de {cliente_corto} vía MCP | 6 h · 1 sol. | 26 h · 3 sol. | 8 h · 2 sol. |

- **Arranque · aparte**: Reunión de 1 h para acordar el calendario, la persona de TI y los accesos.
- **Diseño**: APIs confirmadas y herramientas diseñadas con TI.
- **Servidor en pruebas**: Consultas, creación de guías y comercio simulado.
- **Traspaso a TI**: Documentación, guía y operación en manos de TI.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Diseño de las herramientas · 1 entregable · 6 h · Servidor MCP de Zoom · línea A

Para qué (lo que ve el cliente): Definir con TI qué consultas y qué creación expone el servidor

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DS-1 | Levantamiento técnico y diseño de las herramientas (incluye: Qué APIs existen, con qué documentación y ambiente de pruebas; Cómo se autentica hoy a los comercios; Las tres consultas y la creación que se construyen) | Trabajo de 6 h con el equipo de TI. Se confirma qué APIs existen, con qué documentación (OpenAPI) y si tienen ambiente de pruebas, cómo se autentica a los comercios y qué pasa con una guía creada por error, y se diseñan las herramientas del servidor. Entrega el diseño acordado y las condiciones confirmadas. | - | - | - | 6 | F1 |

### Consultas: tarifas, tracking, estatus · 1 entregable · 14 h · Servidor MCP de Zoom · línea A

Para qué (lo que ve el cliente): Que un agente consulte tarifas, tracking y estatus de envío

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CO-1 | Servidor MCP con tres herramientas de consulta (incluye: Consulta de tarifas; Consulta de tracking; Consulta del estatus de un envío) | Trabajo de 14 h junto al equipo de TI, sobre el repositorio de Zoom y en ambiente de pruebas. Se construye el servidor MCP con tres herramientas de consulta (tarifas, tracking y estatus de envío) que usan las llaves de API que ya usan los comercios. Las consultas no modifican nada. Entrega el servidor consultando en pruebas. | - | - | - | 14 | F2 |

### Creación de guías · 1 entregable · 8 h · Servidor MCP de Zoom · línea A

Para qué (lo que ve el cliente): Que un agente cree guías en pruebas, sin duplicados ni errores

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CR-1 | Herramienta de creación de guías, en pruebas (incluye: Creación solo en el ambiente de pruebas; Confirmación previa antes de crear; Protección contra guías duplicadas) | Trabajo de 8 h junto al equipo de TI. Se construye una herramienta que crea guías solo en el ambiente de pruebas, con confirmación previa y protección contra duplicados. Entrega la creación funcionando en pruebas. | - | - | - | 8 | F2 |

### Prueba con un comercio simulado · 1 entregable · 4 h · Servidor MCP de Zoom · línea A

Para qué (lo que ve el cliente): Verificar de punta a punta lo que haría un comercio externo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PR-1 | Bot de prueba que consulta y crea guías (incluye: Un comercio simulado consulta tarifas y tracking; Y crea una guía en el ambiente de pruebas) | Trabajo de 4 h con el equipo de TI. Un bot de prueba simula a un comercio externo que consulta y crea guías en el ambiente de pruebas. Entrega la prueba de punta a punta. | - | - | - | 4 | F2 |

### Documentación y traspaso · 2 entregables · 8 h · Servidor MCP de Zoom · línea A

Para qué (lo que ve el cliente): Que el equipo de TI agregue servicios por su cuenta

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DO-1 | Documentación y guía para agregar servicios (incluye: Cómo funciona el servidor y cómo se opera; Una guía para sumar un servicio nuevo) | Trabajo de 5 h con el equipo de TI. Se documenta el servidor y se deja una guía para que TI agregue servicios, por ejemplo el cambio de dirección por webhook que ya están armando. Entrega la documentación y la guía. | - | - | - | 5 | F3 |
| DO-2 | Traspaso al equipo de TI (incluye: Revisión conjunta del código; El equipo de TI lo opera y lo ajusta) | Trabajo de 3 h con el equipo de TI. Se revisa el código en conjunto y TI queda con la operación y los ajustes. Entrega el servidor en manos de TI. | - | - | - | 3 | F3 |

## 4. Fuera de alcance

- Llevar el servidor a producción: se decide después de la prueba, con sus resultados.
- Autenticación OAuth completa: se usan las llaves de API de los comercios; OAuth suma horas aparte.
- Crear guías reales: la creación es solo en el ambiente de pruebas.
- Licencias y consumo de las herramientas: los contrata Zoom, aparte de esta inversión.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (03/11/2026): propuesta CAI-082 para Zoom, contacto María Iribarren (directora comercial), con la instrucción «solo coloca la parte del MCP». Educación y sin alianza (según la cuenta de Zoom), 40 h y sin facilidad de pago: **defaults míos** (la pregunta de confirmación se canceló); por confirmar. Insumos: plan piloto de monitoreo v2 (25/10/2026, sección 07) y los correos del 26/10 al 03/11; sin Ficha ni transcripción.
- Alcance: solo la construcción del MCP, como la plantea María («construirlo nosotros junto a tu equipo en las mismas sesiones de consultoría, de modo que el trabajo quede hecho mientras ellos aprenden»). El piloto de monitoreo, Collectio, legitimación de capitales, la proyección de recursos y la hoja de ruta 2027 quedan fuera: no se nombran en el deck. El monitoreo depende del levantamiento con el equipo (la semana próxima) y no se cotiza todavía.
- Horas: 40 h de la prueba de concepto del plan (con las llaves de API actuales; un OAuth completo suma 15 h o más, fuera). El plan las llama «esfuerzo estimado» (horas internas); aquí se tratan como horas junto al equipo de TI, como dice María (se construye en las mismas sesiones). Si son horas internas de Intezia, hay que quitarlas del deck (regla de Ivana). **Reparto mío:** diseño 6 h, consultas 14 h, creación de guías 8 h, bot de prueba 4 h, documentación 5 h y traspaso 3 h.
- Del plan (sección 07): servidor MCP en pruebas con tres herramientas de consulta (tarifas, tracking y estatus) y una de creación (guía); el bot de prueba simula a un comercio externo; documentación y guía para agregar servicios (por ejemplo el cambio de dirección por webhook que ya arman). Tres condiciones: API con documentación OpenAPI y ambiente de pruebas, autenticación con las llaves de API actuales y creación solo en pruebas con confirmación previa y protección contra duplicados.
- Sin semanas, sesiones ni fechas (§4.23): el plan dice 3 a 4 semanas y en paralelo al monitoreo; el deck no lo muestra. Retorno en modo método, sin cifras (no hay datos del cliente: se mide la línea base en el levantamiento); lo pide el criterio de Ventas en toda propuesta. Seguimiento 30-60-90 estándar, con ítems míos.
- Herramientas: Cursor es la que TI ya adoptó (CAP-077) y el bot de prueba es el Grok Bot del plan, que el deck llama «bot de prueba» (producto en beta, solo con datos de prueba). Zoom usa solo Gemini como herramienta de IA (Operaciones): el deck no nombra Claude, Gemini ni Vertex AI y no promete que un modelo concreto consuma el MCP. Sin precios de licencias (no verificados).
- Marca: Brand Kit v2.1 (amarillo #FFD300, Poppins), como en INN-006, porque Ivana lo dio para las propuestas de Zoom; el logo sigue siendo el del repo (falta el logo v2). No van los nombres de personas de Zoom (Ricardo, Carlos) ni el feedback textual. NDA obligatorio (Zoom lo pidió): se menciona en «Cómo cuidamos tus datos», no en los pasos de arranque.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se confirman las APIs, la documentación y cómo se autentica; después las consultas, que no modifican nada; la creación de guías va al final, con confirmación previa y solo en pruebas.

- **Confirmamos**: Las APIs que existen, su documentación y cómo se autentica.
- **Construimos**: Con TI, sobre el repositorio de Zoom, en pruebas.
- **Probamos**: Un comercio simulado consulta y crea guías.
- **Traspasamos**: Documentación y guía para que TI agregue servicios.

- En la práctica, **Consultar antes que crear**: Las tres consultas no modifican nada; la creación de guías va al final y solo en el ambiente de pruebas.
- En la práctica, **Una confirmación antes de crear**: Cada guía exige confirmación previa y tiene protección contra duplicados.
- En la práctica, **Con tres condiciones**: Una API con documentación (OpenAPI) y ambiente de pruebas, y las llaves de API actuales; sin ellas se ajusta el alcance.
- Datos: Se trabaja en el ambiente de pruebas de Zoom, sin datos de clientes reales, y bajo el acuerdo de confidencialidad (NDA) que la empresa exige.
- Quién construye: Intezia construye junto al equipo de TI, sobre el repositorio de Zoom, para que el trabajo quede hecho mientras TI aprende y nada del esfuerzo se pierda.

**Logística:** modalidad: Se acuerda en el arranque, junto con el equipo de TI. · participantes: Una persona de TI con nombre y dedicación definida, y quien conozca las APIs y los servicios. · ritmo: El trabajo se agenda sin frenar las prioridades que TI ya tiene. · arranque: Apenas se apruebe la propuesta; una reunión de 1 h, aparte, acuerda el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Demanda; Punto de partida; Con el servidor; Tiempo de TI recuperado; Gasto de operar.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056.

