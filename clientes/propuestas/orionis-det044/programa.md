# Programa interno · Orionis · Servicio de Detección (DET-044)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json` (formato de Detección, `plantillas/deteccion-compacto.md`): no editar a mano.
> Fuente del insumo: Contexto de la asesora sobre la primera reunión con Orionis (27/10/2026); sin ficha ni transcripción.

## 1. Horas (internas: el deck solo dice las de levantamiento, en global)

| Etapa | Horas | En el deck |
|---|---|---|
| Arranque | 0 | sin horas |
| Nivelación | 2 | sin horas ni grupos |
| Levantamiento | 16 | «16 horas», sin reparto por área |
| **Total de referencia para cotizar** | **18** | no se muestra |

Sin semanas ni sesiones en la propuesta (Keiber, 2026-10-08): el número de sesiones, su duración, los grupos de la nivelación y el calendario se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). Las horas de levantamiento se reparten según lo que necesite cada departamento.

## 2. Qué se audita

- **Áreas (como las nombra el cliente)**: Operaciones, Negocios, Fraudes, Productos y Proyectos.
- **Departamentos** (6): Pasos del proceso, Información que usa, Herramientas y sistemas, Información sensible, Dónde se hace a mano, Quién lo hace.
- **Foco**: Recorremos cómo se trabaja hoy en cada área para ver qué se puede automatizar con IA. Otras áreas pueden sumarse en una segunda fase.
- **Para qué**: Ver la operación real (Cómo trabaja hoy cada área y qué tareas se hacen a mano.); Mejorar desde ya (Logros inmediatos que cada área usa mientras avanza el levantamiento.); Elegir qué automatizar (Los procesos ordenados por impacto y esfuerzo, con la ruta para construirlos.); Cuidar la información (Qué datos no entran a la IA se define al inicio, junto con Orionis.).
- **Logros inmediatos mínimos del proyecto**: 3 (no uno por área: un proceso de mucho esfuerzo pasa al mapa).

## 3. Ruta por etapas (slide 3)

1. **Arranque**: Reunión de arranque: alcance, responsables de cada área, reglas para la información y calendario.
2. **Nivelación**: 2 horas de Fundamentos de IA para los líderes de las cuatro áreas, en un solo grupo.
3. **Levantamiento**: Una conversación con cada área, con su líder y las personas clave. · 16 horas de levantamiento, repartidas según lo que necesite cada área.
4. **Priorización**: Intezia cruza lo levantado y ordena qué automatizar primero, por impacto y esfuerzo.
5. **Informe Final**: Diagnóstico, hoja de ruta hacia la implementación y licencias, presentados a los líderes.

Ruta completa: Ahora, Detección: Mapa de oportunidades, logros inmediatos y la ruta para automatizar. · Después, Habilidades: Se construyen con el equipo las soluciones priorizadas, área por área. · Si lo desean, Más áreas: Se suman al mismo mapa, con su propio levantamiento.

## 4. Entregables (slide 5)

- Al arrancar · **Alcance y calendario**: Acordados en el arranque: el orden de las áreas, el calendario y las reglas para cuidar la información.
- Al arrancar · **Líderes nivelados en IA**: 2 horas de fundamentos: qué es y qué no es la IA, cómo pedirle bien y qué información cuidar.
- En el levantamiento · **Logros inmediatos**: Al menos tres, a evaluar en el levantamiento, con las herramientas que Orionis autorice.
- Al cierre · **Mapa de Calor**: Las oportunidades de las cuatro áreas en un solo mapa, por impacto y esfuerzo, con su camino a la implementación.
- Al cierre · **Informe Final y hoja de ruta**: Qué automatizar primero, tareas por área y los pasos para pasar a construirlo.
- Al cierre · **Inversión inteligente en licencias**: Qué herramientas de IA conviene y de qué tipo, con datos de sus propias áreas.
- Caja editable «Para todo el proyecto»: Ficha de levantamiento de cada área, que valida su líder; Presentación del Informe Final a los líderes.
- Caja editable «Valor inmediato»: Logros inmediatos en uso antes de cerrar; Mapa de qué automatizar primero y datos para decidir licencias.

## 5. Fuera de alcance

- Licencias de IA: la recomendación va en el Informe Final y no están en la inversión.
- Cambios en sus sistemas: se revisan en el levantamiento y no se modifican.
- Construir y poner en uso las automatizaciones: es la fase que sigue (Habilidades).

## 6. Supuestos a confirmar

- Pedido de Ivana (27/10/2026): propuesta base de Detección para Orionis con Flavia Martínez como asesora. No hay ficha ni transcripción: Granola y Fathom no se conectaron en la primera reunión y el cliente dio poco detalle (quieren entender primero cómo funcionaría el esquema). Código DET-044 (siguiente libre tras DET-043), división Educación y sin alianza: los tres por confirmar con Ivana.
- No es la propuesta oficial: la asesora la presentará en vivo, de preferencia presencial, a los líderes de cada área y hará en esa misma reunión un levantamiento más completo para ajustarla al 100 %. Por eso va por áreas y deja abierta una segunda fase para sumar otras. Al ajustarla, se cambian áreas, horas y pasos en `datos.json` y se regenera.
- Áreas: cuatro, tal como las nombra la asesora (Operaciones, Negocios, Fraudes y Productos y Proyectos), sin prioridades entre ellas (CLAUDE.md §4.22). Participarían entre 3 y 5 personas, los líderes de esas áreas. Origen: referido por Sandokan (Banco N58); según él su modelo se parece al de Credicard, lo que no está confirmado. Nada de eso va en el deck.
- Horas (lineamiento de empresa/politicas-comerciales.md): 4 h por área en 4 áreas = 16 h de levantamiento en global, sin reparto por área, y 2 h de Fundamentos de IA en un solo grupo (3 a 5 líderes, muy por debajo del máximo de 25). Arranque sin horas. Si se suman áreas, cada una agrega 4 h de levantamiento.
- Lo que falta y la asesora levantará en la presencial: los procesos concretos de cada área, cuántas personas tiene cada equipo, qué herramientas y sistemas usan hoy y quién toma la decisión final de inversión. Por eso el deck no nombra procesos, herramientas ni stack, ni dice quién recibe el Informe Final más allá de «los líderes».
- Interés declarado: automatizar procesos y proyectos con IA. El deck lo recoge en el mapa y en la ruta de la Detección a la implementación (Habilidades construye las soluciones priorizadas con el equipo). No promete automatizaciones concretas, integraciones con sus sistemas ni resultados: el retorno es una estimación de referencia.
- Confidencialidad: se asume que Fraudes maneja información sensible (aún sin confirmar). El deck lo trata como cuidado de la información en tres lugares: objetivo «Cuidar la información», un espacio por área y el párrafo de datos en «Cómo trabajamos»; se acuerdan reglas en el arranque y en los Fundamentos. No se promete certificación, acuerdo de confidencialidad ni infraestructura propia.
- Stack y herramientas: no se conocen y el deck no pre-recomienda ninguna (la recomienda el Informe Final). Nunca se promete VPN ni se menciona Claude (memoria sobre Claude y Venezuela). Sin afirmar migración de stack (§4.11).
- Modalidad sin definir: el deck dice «presencial o virtual, según lo que acuerden con Orionis». Confirmar en la reunión con los líderes.
- Sin facilidad de pago (Ivana, 27/10/2026): se omite la lámina de pago; el valor queda en campos vacíos para ventas. El deck no usa la palabra «curso» (las 2 h son «Fundamentos de IA»).
- Sin semanas, sesiones ni fechas; sin horas de trabajo ni cantidad de consultores (CLAUDE.md §4.23).

## 7. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se nivela a los líderes con fundamentos. Después se levanta área por área. Al final se prioriza con la foto completa.

- **Entrevistamos**: Al líder de cada área y a las personas clave.
- **Mapeamos**: Sus procesos, la información, los sistemas y los cuellos de botella.
- **Construimos**: Un logro inmediato en el momento, cuando el proceso lo permite.
- **Priorizamos**: Cada oportunidad en el Mapa de Calor, con su camino a la implementación.

- En la práctica, **Sin tarea previa**: Nadie prepara nada antes de su turno: todo se levanta en la conversación.
- En la práctica, **Un espacio por área**: Cada área se levanta por separado: lo de una no se conversa en la mesa de otra.
- En la práctica, **Sin forzar soluciones**: Si un proceso exige mucho esfuerzo, no se resuelve en el momento: pasa al Mapa de Calor con su prioridad.
- Datos: Áreas como Fraudes manejan información sensible. Trabajamos con los ejemplos que Orionis autoriza, sin datos reales de clientes ni de casos, y nada confidencial entra a la IA sin su visto bueno.
- Quién construye: Intezia levanta y construye junto a cada área, con las herramientas que Orionis autorice. Sus sistemas no se modifican.

**Logística:** modalidad: Presencial o virtual, según lo que acuerden con Orionis en la reunión con los líderes. · participantes: Entre tres y cinco líderes en la nivelación; en cada área, su líder y las personas clave. · ritmo: Jornadas en el horario que acuerde cada responsable. · arranque: La fecha la fija Orionis al confirmar la propuesta..

## 8. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Prioridad.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

