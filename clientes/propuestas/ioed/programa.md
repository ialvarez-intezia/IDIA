# Programa interno · IOED · Servicio de Detección (CAP-098)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: CAP-098 enviada el 10/08/2026 e indicaciones de la asesora del 08/10/2026.

## 1. Resumen

- **5 entregables en 2 áreas (más 1 etapa previa)**, **10 h** de sesión.
- Herramienta **Detección**: 5 entregables, 10 h.
- Horas por fase: F1 2 h (1 sol.) · F2 4 h (2 sol.) · F3 4 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Semanas | Horas | Soluciones |
|---|---|---|---|---|---|
| Diagnóstico online | Detección | Fundamentals, Servicios Navales, Operaciones de Buques | 1 a 4 | 10 | 5 |

| Línea de trabajo | Nivel (Semana 1) | Mapeo (Semana 2) | Acceso (Semanas 3 y 4) |
|---|---|---|---|
| Diagnóstico online | 2 h · 1 sol. | 4 h · 2 sol. | 4 h · 2 sol. |

- **Semana 1 · Nivelación**: Kick-off y Fundamentals de 2 h para los responsables de ambas áreas.
- **Semana 2 · Procesos**: Una mesa de 2 h en Servicios Navales y otra en Operaciones de Buques.
- **Semana 3 · Accesos y datos**: Una mesa de 2 h por área sobre quién accede a qué información.
- **Semana 4 · Informe**: Informe de diagnóstico priorizado y ruta de las fases siguientes.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Fundamentals · 1 entregable · 2 h · Detección · línea A · etapa previa

Para qué (lo que ve el cliente): Que el equipo hable un lenguaje común de IA, sobre las herramientas que IOED ya tiene

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FUN-1 | Equipo nivelado en IA y uso seguro de datos | Fundamentals online de 2 h para los responsables de Servicios Navales y de Operaciones de Buques, en un solo grupo (bajo el máximo de 25 por sesión). Temas: qué es y qué no es la IA, uso seguro de la información en herramientas de IA, ejemplos aplicados a su operación, la ruta del diagnóstico, preguntas y expectativas. Se dicta sobre las herramientas que IOED ya tiene en su entorno Microsoft 365 E3; si IOED decide incorporar Claude, se dicta sobre esa herramienta. El kick-off de arranque se hace aparte y no suma horas. | - | - | - | 2 | F1 |

### Servicios Navales · 2 entregables · 4 h · Detección · línea A

Para qué (lo que ve el cliente): Ordenar cómo se documentan, aprueban y pagan sus procesos, y qué información debe protegerse

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SNA-1 | Mapa de procesos y trazabilidad de Servicios Navales | Mesa de trabajo online de 2 h con los responsables del área: procesos documentales, estados, aprobaciones y pagos, y los puntos donde se pierde la trazabilidad. Cubre los temas de mapeo de procesos y de trazabilidad y pagos de la Fase 1 de la CAP-098. | - | - | - | 2 | F2 |
| SNA-2 | Mapa de accesos y datos de Servicios Navales | Mesa de trabajo online de 2 h: quién accede a qué información, qué datos son sensibles y qué controles existen hoy. Es el insumo para evaluar el control de acceso y la protección de datos en el informe de diagnóstico. | - | - | - | 2 | F3 |

### Operaciones de Buques · 2 entregables · 4 h · Detección · línea A

Para qué (lo que ve el cliente): Ordenar cómo se generan sus informes y registros, y con qué otras plataformas se conectan

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| BUQ-1 | Mapa de procesos e informes de Operaciones de Buques | Mesa de trabajo online de 2 h con los responsables del área: procesos operativos, informes y registros, y cómo se generan hoy por separado. | - | - | - | 2 | F2 |
| BUQ-2 | Mapa de accesos y datos de Operaciones de Buques | Mesa de trabajo online de 2 h: quién accede a qué información, qué datos son sensibles y con qué otras plataformas del cliente se conectaría la operación. Es el insumo para evaluar la viabilidad de esas integraciones en el informe. | - | - | - | 2 | F3 |

## 4. Fuera de alcance

- Construcción e implementación (fases 2 y 3): se definen con el informe y no forman parte de esta propuesta.
- Conexión técnica con otras plataformas de IOED: el informe evalúa su viabilidad, no la construye.
- Licencias de IA: no hace falta comprar ninguna. Si IOED decide incorporar Claude, la nivelación se hace con esa herramienta.

## 5. Supuestos a confirmar (antes del método)

- Servicio Detección (la Fase 1 de la CAP-098) y división Educación (la del brief de agosto). Alianza: no. Código CAP-098 conservado porque la instrucción fue «ajustar la CAP-098»; si se prefiere un código DET-, es un solo cambio en cliente.codigo.
- Horas por el lineamiento de Detección: Fundamentals de 2 h en un solo grupo (bajo el máximo de 25) y 4 h por área en 2 áreas (Servicios Navales y Operaciones de Buques, los agrupadores de la CAP-098) = 10 h. La consigna dice «sesiones de 2 horas»: 4 h por área se reparten en 2 mesas de 2 h. La CAP-098 no fijaba cantidad de sesiones. El kick-off de arranque va aparte y no suma horas.
- Cada área tiene dos mesas por tema, tomados de la Fase 1 de la CAP-098: procesos y trazabilidad (mapeo de procesos, trazabilidad y pagos) y accesos y datos (control de acceso y datos, viabilidad de integraciones). El informe de diagnóstico, la evaluación del control de acceso y la viabilidad de integraciones son trabajo del equipo consultor, sin sesión con el cliente ni horas propias: van como entregables transversales.
- Calendario propuesto por el sistema, no dictado por la CAP-098 ni por la consigna: 4 semanas, para que el informe llegue en los primeros 30 días (semana 1 kick-off y Fundamentals, semana 2 mesas de procesos de ambas áreas, semana 3 mesas de accesos y datos, semana 4 informe). Hay que confirmarlo con servicio.
- Nombres de área como agrupadores, igual que en la CAP-098: a pedido del cliente (14/08/2026) no se expone la flota, el detalle de contratos o procesos internos ni el nombre de la plataforma con la que se evaluaría una integración (se habla de «otras plataformas»).
- Herramienta: IOED cuenta con Microsoft 365 E3 y una licencia de Copilot Studio (dato de la asesora en la reunión), así que no necesita comprar nada de entrada. La nivelación se dicta sobre lo que ya tiene. La asesora indicó que, si IOED decide adquirir e integrar Claude, la nivelación se hace sobre esa herramienta: se presenta como una condición que decide IOED (CLAUDE.md §4.11), sin afirmar que migra ni que adoptará. Los casos de Pago Tronic y Claude de la reunión no se citan: no hay fuente documentada para el deck.
- Confidencialidad (slide 4 y hoja resumen): redactada con lo que dijo la asesora (acuerdo firmado antes de iniciar, trabajo dentro de lo que IOED ya tiene) y con respaldo público de las licencias empresariales (Microsoft 365 Copilot: protección de datos empresariales; Claude Team y Enterprise: términos comerciales, sin entrenar con contenido del cliente). Si IOED incorpora Claude, el procesamiento de esa herramienta ya no queda dentro de Microsoft 365: por eso el texto dice que cualquier otra herramienta se valida antes con IOED. El criterio de que las mesas no cargan información real de IOED a herramientas de IA es el mismo de G-MAX, Conserval, la clínica y Acua-e. Falta la validación de Tecnología.
- Las fases siguientes (construcción e implementación) aparecen como camino en la ruta, el retorno y los límites del alcance, sin horas ni valor: en la CAP-098 no tenían horas impuestas y esta propuesta no las cotiza.
- Se retiran del formato anterior (17 slides): Quiénes somos con los clientes de referencia, los estudios de Impacto y la Metodología de retos. El compacto no lleva estudios ni cierre (CLAUDE.md §4.9, §4.10a y §4.21).
- Retorno en modo método: no hay volúmenes ni tiempos por proceso; el informe los estima con lo que cada área entregue en su mesa (estimación referencial, sin compromiso de resultado).
- Reglas de Detección que se conservan: sin certificado, sin garantía 30-60-90, sin recomendar una herramienta en esta propuesta, sin nombres de personas del cliente (la persona de contacto no aparece en el deck).
- Sin facilidad de pago: no se preguntó. El usuario la omitió en las últimas propuestas migradas, así que se aplicó omitir: ["pago"]. Si Ventas la quiere, se agrega con cuotas ligadas a los hitos de la ruta.
- Asesora (última slide): Flavia Martínez, la de la CAP-098, con el teléfono y el correo de su brief; el cargo «Asesora comercial» es supuesto.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se nivela al equipo; después se mapean los procesos y, con ellos claros, los accesos y datos; el informe cierra el diagnóstico.

- **Nivelamos**: Al equipo, con un lenguaje común de IA y de uso seguro de datos.
- **Mapeamos**: Los procesos de cada área y dónde falta trazabilidad.
- **Evaluamos**: Quién accede a qué información y qué controles hacen falta.
- **Informamos**: Con un informe priorizado por área y la ruta siguiente.

- En la práctica, **Dentro de su entorno**: Trabajamos con Microsoft 365 E3 y la licencia de Copilot Studio que IOED ya tiene: no hace falta comprar nada.
- En la práctica, **Mesas online de 2 h**: Una mesa de procesos y otra de accesos y datos por área, con los responsables de cada proceso.
- En la práctica, **Su herramienta**: Fundamentals se dicta sobre lo que IOED ya usa. Si decide incorporar Claude, se dicta sobre esa herramienta.
- Datos: El acuerdo de confidencialidad se firma antes de iniciar. En las mesas no se carga información real de IOED a herramientas de IA. Lo que se use queda en su entorno Microsoft 365, sin entrenar modelos; otra herramienta se valida antes con IOED.
- Quién construye: Intezia conduce las mesas y redacta el informe; los responsables de cada área aportan cómo se trabaja hoy.

**Logística:** modalidad: Online síncrono, por videollamada, a coordinar con IOED. · participantes: Responsables de Servicios Navales y de Operaciones de Buques; Fundamentals, hasta 25 por grupo. · arranque: El kick-off, aparte, abre el proyecto; su fecha se confirma con IOED..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Riesgo de la información; Prioridad.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

