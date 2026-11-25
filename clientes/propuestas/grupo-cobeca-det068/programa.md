# Programa interno · Grupo Cobeca · Servicio de Detección (DET-068)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json` (formato de Detección, `plantillas/deteccion-compacto.md`): no editar a mano.
> Fuente del insumo: Resumen de Ventas de la reunión con Grupo Cobeca (24/11/2026); sin ficha ni transcripción.

## 1. Horas (internas: el deck solo dice las de levantamiento, en global)

| Etapa | Horas | En el deck |
|---|---|---|
| Arranque | 0 | sin horas |
| Nivelación | 2 | sin horas ni grupos |
| Levantamiento | 20 | «20 horas», sin reparto por área |
| **Total de referencia para cotizar** | **22** | no se muestra |

Sin semanas ni sesiones en la propuesta (Keiber, 2026-10-08): el número de sesiones, su duración, los grupos de la nivelación y el calendario se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). Las horas de levantamiento se reparten según lo que necesite cada departamento.

## 2. Qué se audita

- **Áreas (como las nombra el cliente)**: Centro de soporte, Capital humano · Selección, Capital humano · Nómina, Capital humano · Desarrollo, Capital humano · Administración.
- **Departamentos** (4): Pasos del proceso, Información que usa, Quién lo hace, Dónde se hace a mano.
- **Foco**: Dos áreas que no se han tocado: se recorre el Centro de soporte y cada subárea de Capital humano por separado.
- **Para qué**: Ver cómo se trabaja hoy (Cómo funciona cada área, quién hace qué y dónde se hace a mano.); Mejorar desde ya (Logros inmediatos que cada equipo usa mientras avanza el levantamiento.); Automatizar con criterio (Qué puede resolver la IA sin quitarle lo humano a la atención.); Saber por dónde empezar (Qué conviene hacer primero para el mayor impacto, sin ir a ciegas.).
- **Logros inmediatos**: se realizan cuando el proceso o el área lo permite; la propuesta no dice cuántos (Ivana, 2026-11-13). Un proceso de mucho esfuerzo pasa al mapa.

## 3. Ruta por etapas (slide 3)

1. **Arranque**: Reunión de arranque: alcance, responsables de cada área y calendario.
2. **Nivelación**: 2 horas de Fundamentos de IA para el personal de las dos áreas, antes de levantar.
3. **Levantamiento**: Una conversación por departamento, con quien hace el trabajo. · 20 horas de levantamiento, según lo que necesite cada departamento.
4. **Priorización**: Intezia cruza lo levantado y ordena las oportunidades por impacto y esfuerzo.
5. **Informe Final**: Diagnóstico por área, mapa de oportunidades y hoja de ruta, presentados a la dirección.

Ruta completa: Ahora, Detección: Esta propuesta. · Después, Habilidades: Formación práctica por área sobre lo que encontró la Detección. · Más adelante, Políticas: Manual de uso de IA de Grupo Cobeca, con reglas claras para todo el equipo.

## 4. Entregables (slide 5)

- Al arrancar · **Alcance y calendario**: Acordados en el arranque: el orden de las áreas y quién acompaña a cada una.
- Al arrancar · **Equipo nivelado en IA**: 2 horas de fundamentos: qué es y qué no es la IA, cómo pedirle bien y qué información cuidar.
- En el levantamiento · **Logros inmediatos**: Cuando el proceso lo permite, en cada área, con las herramientas que el grupo ya tiene y sobre tareas reales.
- Al cierre · **Mapa de Calor**: Las oportunidades de IA de Soporte y Capital humano en un solo mapa, por impacto y esfuerzo.
- Al cierre · **Informe Final y hoja de ruta**: Cómo está cada área hoy, sus cuellos de botella, las oportunidades de IA y la ruta para construirlas.
- Al cierre · **Uso de lo que ya tienen**: Qué se logra con Copilot y N8N tal como están hoy, y qué haría falta.
- Caja editable «Para todo el proyecto»: Ficha de levantamiento de cada área; Presentación del Informe Final a la gerencia.
- Caja editable «Valor inmediato»: Logros inmediatos en uso antes de cerrar; Datos para decidir por dónde empezar.

## 5. Fuera de alcance

- Construir el agente de soporte y las automatizaciones: es la fase que sigue (Habilidades).
- Cambiar sus licencias o su ecosistema: el trabajo se apoya en lo que el grupo ya tiene.
- Las áreas que ya trabajan con IA dentro del grupo: no se tocan.

## 6. Supuestos a confirmar

- Pedido de Ivana (24/11/2026): dos propuestas para Grupo Cobeca, CAI-120 (Habilidades) y DET-068 (Detección), con María Iribarren como directora comercial. Insumo: resumen de Ventas de la reunión del mismo día; sin ficha ni transcripción. Contacto: el gerente corporativo de tecnología, que conoció a Keiber en el IA TechDay (no se nombra en el deck).
- Decisiones de Ivana (24/11/2026): 20 h de levantamiento (5 departamentos × 4 h: Soporte y las cuatro subáreas de Capital humano, cada una por separado); impacto «reenfoque»; viáticos y modalidad en texto (presencial en Maracaibo con viáticos aparte, o virtual). Educación y sin alianza son supuestos míos. Sin facilidad de pago (regla permanente).
- Áreas como las nombra el cliente: Centro de soporte (unas 8 personas, soporte a 81 farmacias, 4 centros de distribución y el centro corporativo; usan Jira) y Capital humano (15 a 20 personas en 4 o 5 subáreas: selección y captación, nómina, desarrollo y gestión administrativa; se tomaron 4). Lo que el cliente quiere (agente o chatbot de primer nivel con predictibilidad y analítica, y buen uso de Copilot y N8N en Capital humano) guía la conversación pero no es estructura ni se promete.
- El cliente ya trabaja con otra consultora de IA en otras áreas y pidió no desvirtuar ese trabajo: la propuesta entra solo por Soporte y Capital humano y lo dice como «las áreas que ya trabajan con IA no se tocan», sin nombrar a nadie. Se nombran Microsoft 365 con Copilot y N8N porque el cliente pidió apoyarse en esas licencias y en su consola; no se pre-recomienda otra herramienta ni se nombran Claude ni Google.
- Ecosistema declarado (no va completo en el deck): Microsoft 365 con Copilot como IA corporativa, Google Cloud para modelos avanzados, una consola corporativa de N8N y Jira/Atlassian. Estructura de datos con Data Stewards, Data Owner y Product Owner.
- Nivelación de 2 h (interna, un solo grupo): el personal de las dos áreas suma 23 a 28 personas, así que si pasa de 25 serían dos grupos (4 h); confirmar la lista. Sin semanas ni fechas (§4.23): el cliente prefiere arrancar en enero o febrero de 2027 (no antes de las vacaciones; los laboratorios que los surten cierran del 15 de diciembre al 15 de enero), y eso se acuerda en el arranque.
- Caso de nómina contado en la reunión (pagos de más por cálculo manual; 2 días a 15 minutos) es de otro cliente de Intezia y no va en el deck (no se nombran otros clientes). El cerebro digital que se le mostró queda como posible paso para 2027 y no va en estas propuestas.

## 7. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se nivela al equipo, para que todos sepan qué es la IA. Después se levanta área por área. Al final se prioriza con la foto completa de Grupo Cobeca.

- **Entrevistamos**: A quien hace cada tarea, también donde no hay un proceso escrito.
- **Mapeamos**: Sus tareas, la información, las herramientas y los cuellos de botella.
- **Construimos**: Un logro inmediato en el momento, cuando la tarea lo permite.
- **Priorizamos**: Cada oportunidad en el Mapa de Calor, con su impacto y esfuerzo.

- En la práctica, **Humano primero**: En soporte, la IA atiende lo repetitivo y la persona lo que necesita intervención humana, sin generar rechazo.
- En la práctica, **Sin tarea previa**: Nadie prepara nada antes de su turno: todo se levanta en la conversación.
- En la práctica, **Sin forzar soluciones**: Si una tarea exige mucho esfuerzo, no se resuelve en el momento: pasa al Mapa de Calor con su prioridad.
- Datos: Los datos de empleados, nómina y equipos no se cargan a la IA sin el visto bueno de Grupo Cobeca; se trabaja con los ejemplos que autoriza.
- Quién construye: Intezia levanta y construye junto a quien hace cada tarea, sobre las licencias de Microsoft 365 con Copilot y la consola de N8N que el grupo ya tiene.

**Logística:** modalidad: Presencial en Maracaibo (viáticos aparte) o virtual; se acuerda al confirmar. · participantes: El personal del Centro de soporte y de Capital humano; en cada área, quien hace el trabajo. · ritmo: Jornadas en el horario que acuerde cada responsable. · arranque: La fecha se fija al confirmar la propuesta..

## 8. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Prioridad.

## 9. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **reenfoque**. Las personas pasan a trabajo de más valor; no se habla de menos personas ni de nómina.

> Soporte y Capital humano saben dónde automatizar y el equipo pasa a dedicarse a lo que necesita intervención humana, con atención humanizada.

## 10. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056.

