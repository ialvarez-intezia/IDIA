# Programa interno · Supermercados Viva · Servicio de Detección (DET-037)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json` (formato de Detección, `plantillas/deteccion-compacto.md`): no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Supermercados Viva (Flavia Martínez, 13/10/2026, versión de la Propuesta 2) y resumen de la reunión de la asesora; sin transcripción de la reunión.

## 1. Horas (internas: el deck solo dice las de levantamiento, en global)

| Etapa | Horas | En el deck |
|---|---|---|
| Arranque | 0 | sin horas |
| Nivelación | 4 | sin horas ni grupos |
| Levantamiento | 28 | «28 horas», sin reparto por área |
| **Total de referencia para cotizar** | **32** | no se muestra |

Sin semanas ni sesiones en la propuesta (Keiber, 2026-10-08): el número de sesiones, su duración, los grupos de la nivelación y el calendario se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). Las horas de levantamiento se reparten según lo que necesite cada departamento.

## 2. Qué se audita

- **Áreas (como las nombra el cliente)**: Ventas, Finanzas, Cadena de Suministro, Operaciones, Talento Humano, Consultoría Jurídica, Tecnología.
- **Foco**: Recorremos los procesos de cada área, como el cruce de facturas de cuentas por pagar y la depuración de hojas de Excel informales antes de cargarlas a SAP Business One.
- **Para qué**: El valor de cada área (Qué potencia la IA en cada área, proceso por proceso, y qué ya resuelven SAP y Profit.); Agente o skill (Dónde va un agente (tareas de varios pasos) y dónde una skill (instrucción reutilizable).); Mejorar desde ya (Logros inmediatos que las áreas usan mientras avanza el levantamiento.); Reglas y licencias (Qué licencias conviene tener y qué reglas de uso protegen la información.).
- **Logros inmediatos mínimos del proyecto**: 3 (no uno por área: un proceso de mucho esfuerzo pasa al mapa).

## 3. Ruta por etapas (slide 3)

1. **Arranque**: Reunión con la gerencia de Tecnología y los líderes de área: alcance, personas y calendario.
2. **Nivelación**: 4 horas: 2 para Tecnología y 2 para el resto de las áreas. Los temas se ajustan tras medir la madurez.
3. **Levantamiento**: Cada área por separado, con su líder y su equipo, en las oficinas de Viva. · 28 horas de levantamiento, repartidas según lo que necesite cada área.
4. **Priorización**: Intezia cruza lo levantado y ordena las oportunidades de cada área por impacto y esfuerzo.
5. **Informe Final**: Diagnóstico, hoja de ruta, políticas de uso y licencias, presentados a la gerencia y a la dirección.

Ruta completa: Ahora, Detección: Esta propuesta. · El año que viene, Habilidades: Con los resultados: formar a cada área en skills, o que Intezia la acompañe a realizarlas.

## 4. Entregables (slide 5)

- Al arrancar · **Nivelación del resto de áreas**: 2 horas de Fundamentos de IA: qué es y qué no es, cómo pedirle bien y qué información cuidar, con ejemplos de cada área.
- Al arrancar · **Nivelación de Tecnología**: 2 horas: fundamentos y, a nivel técnico, agentes y skills, Claude Code y uso seguro de datos.
- En el levantamiento · **Logros inmediatos**: Al menos tres soluciones en uso desde el primer día, como filtrar currículos por zona de residencia.
- Al cierre · **Mapa de Calor por área**: El valor de cada área en un mapa: dónde hace falta un agente (como el canal de WhatsApp de Viva) y dónde basta una skill.
- Al cierre · **Informe Final y hoja de ruta**: Diagnóstico por área y políticas de uso; se evalúa si es viable su regla de que la información salga de SAP y Profit.
- Al cierre · **Inversión inteligente en licencias**: Se evalúan durante el servicio partiendo de Claude Team y su tipo de puesto; la recomendación final llega en el Informe Final.
- Caja editable «Para todo el proyecto»: Ficha de levantamiento de cada área; Presentación del Informe Final a la dirección.
- Caja editable «Valor inmediato»: Logros inmediatos en uso antes de cerrar; Datos para decidir licencias y reglas de uso.

## 5. Fuera de alcance

- Licencias de IA: la recomendación va en el Informe Final y no están en la inversión.
- Integraciones con SAP Business One o Profit: no se prometen antes de analizar los procesos y su uso.
- Cambios en los sistemas de Viva: el levantamiento no los modifica.

## 6. Supuestos a confirmar

- Pedido de Ivana (16/10/2026): Propuesta 2 de las dos que pidió la gerencia de Tecnología de Supermercados Viva. Cubre siete áreas junto con Tecnología, 25 personas: Ventas 3, Finanzas 5, Cadena de Suministro 6, Operaciones 1, Talento Humano 3, Consultoría Jurídica 1 y Tecnología 6. La Propuesta 1 (solo Tecnología, 12 personas) es independiente y sus números no se mezclan con los de esta. Asesora: Flavia Martínez.
- Código DET-037 confirmado por Ivana (DET-036 es la Propuesta 1).
- Servicio Detección, división Educación y alianza «no»: la ficha dice «Servicios de interés: Detección, Habilidades» y no menciona división ni alianza. Se infieren como en la Propuesta 1; por confirmar. Habilidades va solo como la fase que sigue, sin cotizarla.
- Horas (Ivana, 16/10/2026): 28 h de levantamiento (4 h por cada una de las 7 áreas, la regla estándar de Detección) y 4 h de nivelación: 2 h para Tecnología y 2 h para el resto de las áreas. El arranque no suma horas. Las horas de levantamiento se muestran en global, sin reparto por área. Las de nivelación se muestran separadas por pedido de Ivana, lo que se aparta de la spec de Detección, que no muestra grupos de nivelación (plantillas/deteccion-compacto.md §2).
- Temario de la nivelación (Ivana): Fundamentos de IA para todos, que es básico, más el temario de Tecnología ya definido en la Propuesta 1. Lectura tomada: el resto de las áreas recibe 2 h de Fundamentos de IA, y Tecnología recibe 2 h con los fundamentos y, a nivel técnico, agentes y skills, Claude Code y uso seguro de datos. Si Ivana quiere que Tecnología tome además los fundamentos con el resto, las horas cambian. Temas de Fundamentos tomados de las Detecciones de Acua-e y Conserval (qué es y qué no es la IA, cómo preguntarle con criterio, ejemplos de cada área, qué información cuidar); sin historia, porque la gerencia lo pidió («no quiero la historia, quiero ir de lleno»). Los temas se ajustan tras medir la madurez del equipo.
- Entregables: se omitió la tarjeta «Alcance y calendario» para dar una tarjeta a cada nivelación (la de Tecnología y la del resto). El calendario y el alcance se acuerdan en la reunión de arranque y aparecen en los próximos pasos.
- Licencias: igual que en la Propuesta 1. Se menciona Claude Team como punto de partida, se dice que se evalúa durante el servicio y que la recomendación final llega en el Informe Final. Sin puestos ni precios.
- SAP: integraciones no se prometen; va explícito en el fuera de alcance. La regla de datos de Tecnología (la información sale de SAP Business One y Profit, no de Excel) va en el Informe Final como algo cuya viabilidad se evalúa.
- Agentes: el mapa indica dónde hace falta un agente y dónde basta una skill; el canal de atención por WhatsApp que el cliente prepara va como ejemplo, sin decir para qué lo usa.
- Valor por área (la ficha pide que la Detección lo haga visible área por área): va en la tarjeta «Mapa de Calor por área», en el Informe Final («diagnóstico por área») y en el objetivo «El valor de cada área».
- Logros inmediatos: se mantiene el mínimo de 3 en todo el proyecto, no uno por área. Ejemplos de la ficha: filtrar currículos por zona de residencia (Talento Humano) y revisar qué IP y equipos están activos (Tecnología). Procesos concretos a mirar: el cruce de facturas de cuentas por pagar y la depuración de las hojas de Excel informales antes de cargarlas a SAP Business One; no se prometen como logros porque son procesos de más esfuerzo.
- Habilidades como fase siguiente: que cada área automatice sus procesos con sus propias skills y agentes sin depender de Tecnología. Intezia no desarrolla las skills: acompaña al equipo a realizarlas (corrección de Ivana, 16/10/2026). La estimación es para el año que viene, según la ficha.
- Sin áreas prioritarias: la ficha rotula cada área como «Area priorizada», pero las siete se auditan por igual. El deck las nombra como las nombra el cliente. No lleva las píldoras de «Qué miramos en cada proceso» (opcionales): con siete áreas la tarjeta de alcance crecía y la franja «Fuera de este alcance» quedaba a 1,7 px del pie (mínimo 8). Tampoco hay departamentos con organigrama: la ficha da responsables y roles (soporte técnico, compradores, nómina), no departamentos.
- No se menciona la cantidad de sucursales (instruccion de Ivana): la ficha dice que Viva está instalando la 7ª, así que «7 sucursales» no era exacto.
- Contexto interno que no va en el deck: el dueño decide y quiere avanzar muy rápido; la gerencia anticipa que le costará venderla adentro y compara con otros dos proveedores; patrocinio ejecutivo aún no asegurado; presupuesto en evaluación; hay gerentes que hoy dicen que no hay nada que automatizar (no se cita, porque esos gerentes leerán la propuesta); los nombres de las personas de cada área; la propuesta primero la revisa la gerencia de Tecnología y luego se presenta a los directivos.
- Modalidad presencial en las oficinas, una sola sede. Horizonte de 3 a 12 meses y presupuesto «en evaluación»: no van en el deck (sin semanas ni fechas, §4.23).
- Sin facilidad de pago (Ivana): 8 slides. Sin semanas, sesiones ni fechas (CLAUDE.md §4.23).

## 7. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se mide la madurez y se nivela: fundamentos para todos y un bloque técnico para Tecnología. Después se levanta área por área. Al final se prioriza con la foto completa de la empresa.

- **Entrevistamos**: A cada persona de las siete áreas, área por área.
- **Mapeamos**: Sus procesos, los datos, los sistemas y los cuellos de botella.
- **Construimos**: Un logro inmediato en el momento, cuando el proceso lo permite.
- **Priorizamos**: Cada oportunidad en el Mapa de Calor de su área, con su impacto y esfuerzo.

- En la práctica, **Sin tarea previa**: Nadie prepara nada antes de su turno: todo se levanta en la conversación.
- En la práctica, **Un espacio por área**: Cada área se levanta por separado, con su líder y su equipo, nunca varias en la misma mesa.
- En la práctica, **Sin forzar soluciones**: Si un proceso exige mucho esfuerzo, no se resuelve en el momento: pasa al Mapa de Calor con su prioridad.
- Datos: Trabajamos con ejemplos reales y solo con las cuentas y la información que Viva autoriza: nada confidencial entra a la IA sin su visto bueno.
- Quién construye: Intezia levanta y construye junto a cada persona. Los accesos y las herramientas con las que se trabaja los autoriza Viva; sus sistemas no se modifican.

**Logística:** modalidad: Presencial, en las oficinas de Viva. · participantes: Las 25 personas de las siete áreas, en la nivelación y en el levantamiento de su área. · ritmo: Jornadas en el horario que acuerde cada responsable. · arranque: La fecha la fija Viva al confirmar la propuesta..

## 8. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Prioridad.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

