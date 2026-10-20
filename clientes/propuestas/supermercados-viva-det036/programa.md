# Programa interno · Supermercados Viva · Servicio de Detección (DET-036)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json` (formato de Detección, `plantillas/deteccion-compacto.md`): no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Supermercados Viva (Flavia Martínez, 13/10/2026) y resumen de la reunión de la asesora; sin transcripción de la reunión.

## 1. Horas (internas: el deck solo dice las de levantamiento, en global)

| Etapa | Horas | En el deck |
|---|---|---|
| Arranque | 0 | sin horas |
| Nivelación | 2 | sin horas ni grupos |
| Levantamiento | 8 | «8 horas», sin reparto por área |
| **Total de referencia para cotizar** | **10** | no se muestra |

Sin semanas ni sesiones en la propuesta (Keiber, 2026-10-08): el número de sesiones, su duración, los grupos de la nivelación y el calendario se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). Las horas de levantamiento se reparten según lo que necesite cada departamento.

## 2. Qué se audita

- **Áreas (como las nombra el cliente)**: Tecnología.
- **Departamentos** (6): Pasos del proceso, Datos que usa, Sistemas que usa hoy, Volumen y frecuencia, Seguridad y riesgo, Quién lo hace.
- **Foco**: Recorremos los procesos de Tecnología, persona por persona, como la depuración de las hojas de Excel informales antes de cargarlas a SAP Business One. Profit (nómina) y Power BI son el contexto.
- **Para qué**: Ver la operación real (Cómo trabaja hoy Tecnología, proceso por proceso, y qué ya resuelven SAP y Profit.); Agente o skill (Dónde va un agente (tareas de varios pasos) y dónde una skill (instrucción reutilizable).); Mejorar desde ya (Logros inmediatos que Tecnología usa mientras avanza el levantamiento.); Reglas y licencias (Qué licencias conviene tener y qué reglas de uso protegen la información.).
- **Logros inmediatos mínimos del proyecto**: 3 (no uno por área: un proceso de mucho esfuerzo pasa al mapa).

## 3. Ruta por etapas (slide 3)

1. **Arranque**: Reunión con la gerencia de Tecnología: alcance, personas a entrevistar y calendario.
2. **Nivelación**: 2 horas aplicadas a los procesos de Tecnología, a nivel técnico, tras medir la madurez del equipo.
3. **Levantamiento**: Una conversación con cada persona de Tecnología, en sus oficinas. · 8 horas de levantamiento con los gerentes y coordinadores de Tecnología.
4. **Priorización**: Intezia cruza lo levantado y ordena las oportunidades por impacto y esfuerzo.
5. **Informe Final**: Diagnóstico, hoja de ruta, políticas de uso y licencias, presentados a la gerencia y a la dirección.

Ruta completa: Ahora, Detección: Esta propuesta. · El año que viene, Habilidades: Con los resultados: formar al equipo en skills, o que Intezia lo acompañe a realizarlas.

## 4. Entregables (slide 5)

- Al arrancar · **Alcance y calendario**: Acordados con la gerencia de Tecnología: personas a entrevistar y orden del levantamiento.
- Al arrancar · **Equipo nivelado en IA**: Medición de madurez y 2 h técnicas: agentes y skills, Claude Code, uso seguro de datos. Temas a evaluar en el servicio.
- En el levantamiento · **Logros inmediatos**: Al menos tres soluciones en uso desde el primer día; por ejemplo, revisar qué IP y equipos están activos.
- Al cierre · **Mapa de Calor**: Los procesos de Tecnología en un mapa: qué requiere un agente (como el canal de WhatsApp de Viva) y qué basta con una skill.
- Al cierre · **Informe Final y hoja de ruta**: Diagnóstico, hoja de ruta y políticas de uso; se evalúa si es viable su regla de que la información salga de SAP y Profit.
- Al cierre · **Inversión inteligente en licencias**: Se evalúan durante el servicio partiendo de Claude Team y su tipo de puesto; la recomendación final llega en el Informe Final.
- Caja editable «Para todo el proyecto»: Ficha de levantamiento de cada proceso; Presentación del Informe Final a la dirección.
- Caja editable «Valor inmediato»: Logros inmediatos en uso antes de cerrar; Datos para decidir licencias y reglas de uso.

## 5. Fuera de alcance

- Licencias de IA: la recomendación va en el Informe Final y no están en la inversión.
- Integraciones con SAP Business One o Profit: no se prometen antes de analizar los procesos y su uso.
- Otras áreas de Viva: esta propuesta cubre solo Tecnología.

## 6. Supuestos a confirmar

- Pedido de Ivana (16/10/2026): Propuesta 1 de las dos que pidió la gerencia de Tecnología de Supermercados Viva. Esta cubre solo el departamento de Tecnología (12 personas). La Propuesta 2 (varias áreas con Tecnología, 25 personas) es otra propuesta independiente, con su propia ficha y su propio código. Asesora: Flavia Martínez.
- Código DET-036: Ivana pidió DET-035, que ya es de Cinex (enviada el 15/10/2026). Se le preguntó y no respondió; se usó el siguiente libre. Si prefiere otro código, se cambia en `cliente.codigo` y se regenera.
- Servicio Detección, división Educación y alianza «no»: la ficha dice «Servicios de interés: Detección, Habilidades» y no menciona división ni alianza. Se infieren de un cliente corporativo nuevo y de las demás propuestas de Flavia; por confirmar. Habilidades va solo como la fase que sigue, sin cotizarla.
- Horas (Ivana, 16/10/2026): 8 h de levantamiento y 2 h de nivelación para las mismas doce personas; el arranque no suma horas. Las 2 h de nivelación se muestran en el deck (etapa, entregable y hoja de inversión) porque la gerencia pidió ver el contenido. Es la misma desviación de la spec de Detección que ya se aplicó en Cinex (plantillas/deteccion-compacto.md §2).
- Temario de la nivelación (Ivana: visible, a nivel técnico y no básico, y «se evalúa durante el servicio»): agentes y skills, Claude Code, uso seguro de la información e instrucciones para tareas de Tecnología. La gerencia hizo antes un programa largo de IA que no le sirvió: sin introducción histórica ni conceptos básicos. El deck dice que los temas se confirman tras medir la madurez del equipo. Los temas los redactó el sistema a partir de la ficha (Claude Code como palanca para un equipo sin área de desarrollo); no hay temario base de Intezia.
- Licencias (Ivana): se menciona Claude Team como punto de partida, porque es lo que el cliente quiere incorporar y lo que ya se le sugirió, pero se dice que se evalúa durante el servicio y que la recomendación final llega en el Informe Final. No se dice cuántos puestos ni se dan precios. Verificado (support.claude.com, 16/10/2026): desde enero de 2026 el puesto estándar de Claude Team incluye Claude Code, con menos límite de uso que el premium; por eso el deck habla de «tipo de puesto» a evaluar.
- SAP (Ivana: «ok con SAP»): integraciones no se prometen. Va explícito en el fuera de alcance: primero se analizan los procesos y su uso, y de ahí se define la implementación. SAP Business One, Profit (nómina) y Power BI aparecen como el contexto que el cliente ya usa, sin afirmar ninguna migración (CLAUDE.md §4.11).
- Regla de datos de Tecnología: toda la información debe salir de SAP Business One y Profit, no de Excel, y la gerencia pregunta si es viable. Va en el Informe Final: las políticas de uso la recogen y se evalúa si es viable. No se afirma que lo sea ni que no.
- Agentes: es lo que más interesa a la gerencia. El deck dice explícitamente que el mapa indica dónde hace falta un agente y dónde basta una skill, con un glosario corto de cada término. Se menciona el canal de atención por WhatsApp que el cliente prepara, como ejemplo; no se dice para qué lo usa porque la ficha no lo aclara.
- Logros inmediatos: se mantiene el mínimo de 3. De la ficha, la gerencia mencionó revisar qué IP y equipos están activos (va como ejemplo de logro) y la depuración de las hojas de Excel informales para pasarlas a SAP (va como proceso a mirar en el levantamiento, no como logro: es un proceso de más esfuerzo y, si lo es, pasa al Mapa de Calor).
- Un solo departamento: Tecnología, 12 personas (gerentes y coordinadores de TI) a entrevistar y a nivelar, presencial en las oficinas, una sola sede. No hay lista de personal ni organigrama, así que las píldoras de la slide 2 dicen qué se mira en cada proceso y no son subáreas. La gerencia aparece por su cargo, sin nombre.
- Contexto interno que no va en el deck: el dueño es quien decide y quiere avanzar muy rápido; la gerencia compara con otros dos proveedores; patrocinio ejecutivo aún no asegurado; presupuesto en evaluación; la propuesta debe poder leerse sin que la gerencia esté presente para explicarla.
- Los dolores de la portada salen de la ficha: IA usada de forma suelta y sin licencias corporativas, falta de un orden claro para implementarla, un departamento sin área de desarrollo propia que soporta la operación de las sucursales, y hojas de Excel informales que se cargan a mano a SAP. Son hechos de la ficha, sin cifras ni citas. Corrección del 16/10/2026 (Ivana): no se menciona la cantidad de sucursales en ninguna de las dos propuestas. La ficha de la Propuesta 2 dice «instalando su 7ª sucursal», así que «7 sucursales» no era exacto.
- Sin facilidad de pago (Ivana): 8 slides. Sin semanas, sesiones ni fechas (CLAUDE.md §4.23).
- Corrección del 16/10/2026 (Ivana): Intezia no desarrolla las skills, acompaña al equipo a realizarlas. La ruta completa dice «formar al equipo en skills, o que Intezia lo acompañe a realizarlas».

## 7. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se mide la madurez del equipo y se nivela, para que todos hablen el mismo idioma técnico sobre IA. Después se levanta persona por persona. Al final se prioriza con la foto completa de Tecnología.

- **Entrevistamos**: A cada persona del departamento de Tecnología, una por una.
- **Mapeamos**: Sus procesos, los datos, los sistemas y los cuellos de botella.
- **Construimos**: Un logro inmediato en el momento, cuando el proceso lo permite.
- **Priorizamos**: Cada oportunidad en el Mapa de Calor, con su impacto y esfuerzo.

- En la práctica, **Sin tarea previa**: Nadie prepara nada antes de su turno: todo se levanta en la conversación.
- En la práctica, **Persona por persona**: Cada integrante cuenta cómo trabaja, sin esperar a los demás.
- En la práctica, **Sin forzar soluciones**: Si un proceso exige mucho esfuerzo, no se resuelve en el momento: pasa al Mapa de Calor con su prioridad.
- Datos: Trabajamos con ejemplos reales y solo con las cuentas y la información que Viva autoriza: nada confidencial entra a la IA sin su visto bueno.
- Quién construye: Intezia levanta y construye junto a cada persona. Los accesos y las herramientas con las que se trabaja los autoriza Viva; sus sistemas no se modifican.

**Logística:** modalidad: Presencial, en las oficinas de Viva. · participantes: La gerencia en el arranque; las doce personas de Tecnología en la nivelación y el levantamiento. · ritmo: Jornadas en el horario que acuerde cada responsable. · arranque: La fecha la fija Viva al confirmar la propuesta..

## 8. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Prioridad.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

