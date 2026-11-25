# Programa interno · Instituto Médico Valera · Servicio de Habilidades y Políticas (CAI-115)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (20/11/2026) y transcripción de la reunión de Verónica Rubio con el Instituto Médico Valera (20/11/2026).

## 1. Resumen

- **11 entregables en 3 áreas**, **40 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Habilidades en IT**: 6 entregables, 40 h.
- Herramienta **Políticas de IA**: 5 entregables, 0 h.
- Horas por fase: F1 8 h (4 sol.) · F2 20 h (3 sol.) · F3 12 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Procesos internos de IT | Habilidades en IT | Procesos internos automatizados | 20 | 3 |
| Agente de pacientes | Habilidades en IT | Agente de atención a pacientes | 20 | 3 |
| Gobernanza de IA en paralelo | Políticas de IA | Gobernanza de IA | 0 | 5 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Base (mapa del agente y política) | Obra (construcción con el equipo) | Traspaso (autonomía y gobernanza) |
|---|---|---|---|
| Procesos internos de IT | 4 h · 1 sol. | 10 h · 1 sol. | 6 h · 1 sol. |
| Agente de pacientes | 4 h · 1 sol. | 10 h · 1 sol. | 6 h · 1 sol. |
| Gobernanza de IA en paralelo | 0 h · 2 sol. | 0 h · 1 sol. | 0 h · 2 sol. |

- **Arranque**: Accesos, participantes y orden de las piezas confirmados con IT y la dirección.
- **Base**: Mapa del agente, procesos elegidos y política lista para aprobar.
- **Obra**: El agente propio y los flujos en marcha.
- **Cierre**: Guías y comité en uso; empieza la garantía.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Procesos internos automatizados · 3 entregables · 20 h · Habilidades en IT · línea A

Para qué (lo que ve el cliente): Automatizar lo que hoy debe revisar o autorizar una sola persona

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PA-1 | Procesos a automatizar, elegidos | Lista de los procesos internos que hoy pasan por la revisión o autorización de una persona, ordenados por impacto y esfuerzo con el equipo de IT. | - | - | - | 4 | F1 |
| PA-2 | Flujos con herramientas de flujo | Flujos de trabajo automáticos construidos por el equipo con herramientas de flujo para los procesos elegidos. | - | - | - | 10 | F2 |
| PA-3 | Reglas de autorización compartidas | Reglas escritas de quién aprueba qué y qué se autoriza solo, para que la autorización no dependa de una sola persona. | - | - | - | 6 | F3 |

### Agente de atención a pacientes · 3 entregables · 20 h · Habilidades en IT · línea B

Para qué (lo que ve el cliente): Que la clínica opere y actualice su propio agente de atención

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AP-1 | Mapa del agente y de lo que es propio | Revisión del agente actual: cómo está construido, qué canales atiende y qué es de la clínica y qué del proveedor. | - | - | - | 4 | F1 |
| AP-2 | Agente de WhatsApp construido por IT | El equipo de IT construye con Intezia el agente de atención por WhatsApp, con propiedad de la clínica. El canal telefónico se evalúa según lo que permita la telefonía. | - | - | - | 10 | F2 |
| AP-3 | Guía para operar y actualizar el agente | Guía escrita con el equipo para operar, actualizar y probar el agente sin depender del proveedor. | - | - | - | 6 | F3 |

### Gobernanza de IA · 5 entregables · 0 h · Políticas de IA · línea C

Para qué (lo que ve el cliente): Reglas claras de qué se carga a la IA, con qué herramienta y quién responde

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| GI-1 | Política de uso de IA para aprobar | Política de IA escrita, lista para que la apruebe la junta directiva. | - | - | - | 0 | F1 |
| GI-2 | Matriz de datos por herramienta | Clasificación de la información (sensible, interna y pública) y qué puede ir a cada herramienta, con los datos de pacientes, operativos y financieros. | - | - | - | 0 | F1 |
| GI-3 | Stack oficial y licencias consolidadas | Las herramientas de IA oficiales de la clínica y las licencias que hoy están dispersas, reunidas y repartidas por área o por gerente. | - | - | - | 0 | F2 |
| GI-4 | Responsable de IA y comité | Definición del responsable de IA, con sus funciones, y de un comité de gobernanza. | - | - | - | 0 | F3 |
| GI-5 | Control del gasto en IA por área | Cómo se reparte y se controla el gasto en licencias y en uso de IA por área y por gerente. | - | - | - | 0 | F3 |

## 4. Fuera de alcance

- Cerebros Digitales de los gerentes: se evalúan en una propuesta aparte.
- Licencias de IA: no están en la inversión; el stack oficial lo define la política.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (22/11/2026): propuesta CAI-115 de Habilidades para el Instituto Médico Valera, con Políticas de IA en paralelo, y Verónica Rubio como asesora. Insumos: Ficha (20/11/2026), transcripción de Meet (42 min) y resumen de Ventas. Primer contacto.
- Ajuste de Ivana (24/11/2026): «dejando solo el desarrollo del agente», sin la migración a un lenguaje moderno ni la conexión con el sistema hecho en RPG. Respuestas: se quita toda el área de Modernización del código RPG, se quita completa el área de Datos al alcance de los gerentes (consulta segura de los datos del sistema, interfaces y guía) y quedan Procesos internos, Agente de pacientes y Políticas. El deck no nombra RPG, AS400, modernización ni migración, ni el sistema de gestión. Horas confirmadas por Ivana: 20 h por área de Habilidades, total 40 h (antes 80 h).
- Decisiones previas de Ivana (22/11/2026): Educación y sin alianza; combo de Habilidades y Políticas en un deck, con Políticas en paralelo y SIN horas (se cotiza por entregable); impacto «operación». Combo parcial: se registra bajo `habilidades` (CLAUDE.md §4.1a) y el rótulo dice «Servicio de Habilidades y Políticas».
- Reparto de horas mío (Ivana fijó 20 h por área): Procesos internos 20 h (procesos elegidos 4, flujos 10, reglas de autorización 6); Agente de pacientes 20 h (mapa 4, agente de WhatsApp 10, guía 6). Fases de Habilidades de 8, 20 y 12 h = 40 h. Los cinco entregables de Gobernanza de IA llevan 0 h (política, matriz de datos, stack y licencias, responsable y comité, control del gasto).
- Sin nombres de personas (el gerente de IT, la gerente médica) ni del proveedor externo que hoy opera el agente. Sin marcas de IA: no se nombra Claude ni Meta ni N8N («herramientas de flujo»); sí WhatsApp. No se menciona VPN (Claude no está soportado en Venezuela). El stack oficial lo define la política.
- Viáticos y logística de traslado: el presidente pidió que la propuesta no los incluya. Modalidad mixta (ficha y reunión): presencial en Valera y encuentros en línea.
- Cerebros Digitales de los gerentes: quedan fuera, en «Fuera de este alcance» (propuesta aparte).
- Retorno en modo método: no hay horas ni volúmenes medidos. Seguimiento 30-60-90 incluido por ser estándar de Habilidades. Sin facilidad de pago (regla permanente). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Sin semanas, sesiones ni fechas (§4.23). Cotización de Políticas: la hoja de inversión usa `inversion.partes` (Habilidades en IT y Políticas de IA) para que ventas ponga cada valor; la regla de memoria dice que las partes solo van si Ivana las pide: confirmar o quitarlas.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se mapea el agente actual, se eligen los procesos y se escribe la política, que ordenan lo demás. Después se construye con el equipo. Al final se traspasa a la clínica para que opere y mantenga cada pieza.

- **Construimos**: Junto a quien ejecuta el proceso, con sus casos reales.
- **Probamos**: Con ese equipo y con el equipo de tecnología de Instituto Médico Valera.
- **Adoptamos**: El equipo la usa en su trabajo diario.
- **Medimos**: El retorno en tiempo y las oportunidades de optimización para la empresa.

- En la práctica, **Un agente que es de la clínica**: El equipo aprende a construir, probar y actualizar el agente de atención con IA, sin depender del proveedor.
- En la práctica, **Con datos autorizados**: El agente y los flujos trabajan solo con la información que la clínica autoriza compartir.
- En la práctica, **Depende del canal**: WhatsApp es el primer canal; el telefónico depende de lo que permita la telefonía y se verifica en el arranque.
- Datos: Los datos de pacientes, historiales y finanzas no se cargan a la IA sin autorización: la matriz de datos de la política define qué puede ir a cada herramienta.
- Quién construye: Intezia guía y el equipo de IT construye con IA el agente y los flujos; lo que se construye queda en propiedad de la clínica.

**Logística:** modalidad: Mixta: presencial en Valera y encuentros en línea, según se acuerde en la reunión de arranque. · participantes: El equipo de IT y la alta dirección en la política. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: Las fechas se acuerdan en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas del área; Tiempo actual por tarea; Tiempo con la pieza; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> La clínica deja de depender de un proveedor para su agente y de una sola persona para autorizar, y el uso de IA tiene reglas claras.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

