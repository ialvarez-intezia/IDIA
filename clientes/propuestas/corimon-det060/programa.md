# Programa interno · Corimón · Servicio de Detección y Políticas (DET-060)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json` (formato de Detección, `plantillas/deteccion-compacto.md`): no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Corimón. Sin transcripción de la reunión disponible; si aparece y contradice la ficha, manda la transcripción..

## 1. Horas (internas: el deck solo dice las de levantamiento, en global)

| Etapa | Horas | En el deck |
|---|---|---|
| Arranque | 2 | sin horas |
| Nivelación | 4 | sin horas ni grupos |
| Levantamiento | 52 | «52 horas», sin reparto por área |
| **Total de referencia para cotizar** | **58** | no se muestra |

Sin semanas ni sesiones en la propuesta (Keiber, 2026-10-08): el número de sesiones, su duración, los grupos de la nivelación y el calendario se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). Las horas de levantamiento se reparten según lo que necesite cada departamento.

## 2. Qué se audita

- **Áreas (como las nombra el cliente)**: TI, Finanzas, Compras, Negocios, Comercial y BI, RR. HH., Gerencia General, Logística, Normalización, Laboratorio y Desarrollo, Legal, CEO, Proyectos, Ingeniería y Mantenimiento, Producción.
- **Foco**: Levantamiento con los 51 líderes estratégicos de las 12 áreas, con más tiempo dedicado a TI, donde se define el camino tecnológico.
- **Para qué**: Ver la operación real (Cómo trabaja hoy cada una de las 12 áreas, con quien hace el trabajo, no solo con la dirección.); Recomendar con objetividad (La Brújula dice qué herramienta conviene en cada área, sin inclinarse por ninguna.); Mejorar desde ya (Logros inmediatos que el equipo usa mientras avanza el levantamiento.); Gobernar y proteger datos (Políticas de uso de IA y reglas para monitorear el uso indebido de la información más sensible.).
- **Logros inmediatos**: se realizan cuando el proceso o el área lo permite; la propuesta no dice cuántos (Ivana, 2026-11-13). Un proceso de mucho esfuerzo pasa al mapa.

## 3. Ruta por etapas (slide 3)

1. **Arranque**: Reunión con la dirección: alcance, responsable de cada área y calendario.
2. **Nivelación**: 4 horas de Fundamentals en 2 grupos, para 46 líderes.
3. **Auditoría**: Área por área, con el líder y su equipo; más tiempo dedicado a TI. · 52 horas de levantamiento, repartidas según lo que necesite cada departamento.
4. **Priorización**: Intezia cruza lo levantado y ordena las oportunidades de las 12 áreas.
5. **Políticas**: Diagnóstico de madurez y redacción del marco, con foco en el uso indebido.
6. **Informe**: Diagnóstico, camino tecnológico por área y hoja de ruta, presentados a la dirección.

Ruta completa: Ahora, Detección y Políticas: Esta propuesta: 51 líderes estratégicos en 12 áreas. · Después, Habilidades: Profundización por filial y nivelación del resto del personal.

## 4. Entregables (slide 5)

- Al arrancar · **Alcance y calendario**: Acordados con la dirección: responsable de cada área y orden de las auditorías.
- Al arrancar · **Equipo nivelado en IA**: Los 46 líderes sin nivelación previa, con un lenguaje común sobre IA y su uso responsable.
- En el levantamiento · **Logros inmediatos**: Soluciones construidas con el equipo, cuando el proceso o el área lo permite.
- Al cierre · **Mapa de Calor**: Las oportunidades de las 12 áreas en un solo mapa, con su Índice de Madurez en IA.
- Al cierre · **Marco de gobernanza de IA**: Manual de políticas, Matriz de riesgos y Brújula IA, con roles, permisos y reglas de escalamiento y de monitoreo del uso indebido.
- Al cierre · **Informe Final y hoja de ruta**: Diagnóstico por área, camino tecnológico recomendado y resumen ejecutivo de una página.
- Caja editable «Para todo el proyecto»: Ficha de levantamiento de cada área; Presentación del Informe Final a la dirección.
- Caja editable «Valor inmediato»: Mejoras en uso antes de cerrar el proyecto; Datos para decidir licencias con criterio; Brújula de herramienta por área, sin inclinarse de antemano.

## 5. Fuera de alcance

- Construir la arquitectura central (la columna vertebral): la recomendamos; la construye el equipo de TI.
- Las licencias de las herramientas recomendadas: van aparte.
- Desarrollos a la medida: si el Informe Final los recomienda, se cotizan aparte.

## 6. Supuestos a confirmar

- Servicio: combo Detección + Políticas bajo `deteccion` (CLAUDE.md §4.1a), mismo criterio que Andrómeda DET-016: Políticas se representa como una etapa de la ruta y un entregable (Marco de gobernanza de IA), con su propio valor en `inversion.partes`. La plantilla de Detección no tiene un formato propio para Políticas.
- Fundamentals (nivelación): instrucción directa del usuario (17/11/2026) de excluir a TI (5 personas) porque ya trabaja con Claude para desarrollo y no necesita repetir lo básico (la Ficha pedía nivelar a las mismas 51 personas entrevistadas, sin excluir a TI; el usuario lo ajustó en el chat). Quedan 46 líderes, repartidos en 2 grupos de hasta 25 personas (25 y 21), 2 h cada grupo = 4 h de Fundamentals en total. La composición exacta de cada grupo se define en el kickoff.
- Horas de levantamiento: 4 h por área (lineamiento estándar, `empresa/politicas-comerciales.md`) para las 11 áreas restantes (44 h) + 8 h para TI (el doble, por el pedido explícito de más peso en sus sesiones porque ahí se define el camino tecnológico) = 52 h en total. El reparto exacto por área se decide en el kickoff (regla de la plantilla: horas en global, sin desglose por área en la propuesta).
- Sin mencionar ningún modelo pre-entrenado ni el tipo de modelo detrás de la arquitectura recomendada (instrucción directa del usuario, 17/11/2026): el deck solo habla de la recomendación de arquitectura (IA central que reparte peticiones), los criterios de separación de datos y control de tokens, y la ruta de implementación — nunca de construirla ni de qué modelo la sustenta.
- La «columna vertebral» (arquitectura central tipo router) queda explícitamente fuera de alcance como construcción: Intezia la recomienda, Corimón (su equipo de TI) la construye. Esto se escribió con claridad en `fuera_alcance` a pedido explícito del cliente (Ficha, Bloque F).
- Recomendación de herramienta objetiva: Jonathan (gerente de TI) se inclina por Copilot y pidió privacidad como criterio; Alejandro pidió expresamente que la recomendación no esté «amañada». El deck no pre-recomienda ninguna herramienta (ni Copilot, ni Gemini, ni Claude): la Brújula del Informe Final decide con datos.
- Nombres de personas (Alejandro Padra, Jonathan, Valerie) no se mencionan en el deck — quedan en brief.md para uso interno de Ventas.
- Plan de pago: se usa el estándar de la plantilla (50 % al aprobar, 50 % con el Informe Final); no se pidió otro.
- Impacto (`entregables.impacto`) con enfoque `operacion`: el diagnóstico y la gobernanza dan orden y objetividad, no implican reducir personal.
- Segunda fase (fuera de esta propuesta): profundización por filial y nivelación del resto del personal (~600 personas en el grupo), según la Ficha y el contexto del usuario. Se refleja solo en `ruta_completa` como «Después».

## 7. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero nivelamos al equipo, para que todos hablen el mismo idioma sobre IA. Después levantamos cada departamento por separado, para que cada líder hable de sus procesos sin esperar a otros. Al final priorizamos con la foto completa de Corimón.

- **Entrevistamos**: Al líder de cada departamento y a su mano derecha.
- **Mapeamos**: Procesos, tiempos, herramientas y cuellos de botella del día a día.
- **Construimos**: Un logro inmediato en el momento, cuando el proceso lo permite.
- **Priorizamos**: Cada oportunidad por impacto, esfuerzo y riesgo.

- En la práctica, **Un espacio por área**: Nunca varias áreas juntas en la misma mesa, salvo las que ya comparten subdepartamento.
- En la práctica, **Sin tarea previa**: Los líderes no preparan nada antes de su turno: llegan con su día a día real.
- En la práctica, **Herramienta sin favoritismos**: El Informe Final recomienda con datos, no con lo que ya usa cada área.
- Datos: Legal maneja millones de documentos y RR. HH. datos de personal: trabajamos con ejemplos reales sin sacarlos de la organización, y las políticas definen cómo monitorear el uso indebido de la información confidencial.
- Quién construye: Intezia recomienda la arquitectura central, los criterios de separación de datos y control de tokens, y la ruta. La construcción queda del lado del equipo de TI de Corimón.

**Logística:** modalidad: Presencial, coordinada por área en la reunión de arranque. · participantes: Todo el equipo en la nivelación; cada líder y su mano derecha en el levantamiento. · ritmo: Jornadas en el horario que acuerde cada responsable. · arranque: La fecha la fija Corimón al confirmar la propuesta..

## 8. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen por área; Nivel de madurez; Oportunidades priorizadas; Camino tecnológico.

## 9. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> Corimón sale con un diagnóstico objetivo de sus 12 áreas, una Brújula que dice qué herramienta conviene en cada una sin favoritismos, y un marco de políticas que protege su información más sensible.

## 10. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

