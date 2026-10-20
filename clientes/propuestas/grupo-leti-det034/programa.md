# Programa interno · Grupo Leti · Servicio de Detección (DET-034)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json` (formato de Detección, `plantillas/deteccion-compacto.md`): no editar a mano.
> Fuente del insumo: Resumen de la reunión con el responsable técnico, de la asesora (14/10/2026).

## 1. Horas (internas: el deck solo dice las de levantamiento, en global)

| Etapa | Horas | En el deck |
|---|---|---|
| Arranque | 0 | sin horas |
| Nivelación | 0 | sin horas ni grupos |
| Levantamiento | 12 | «12 horas», sin reparto por área |
| **Total de referencia para cotizar** | **12** | no se muestra |

Sin semanas ni sesiones en la propuesta (Keiber, 2026-10-08): el número de sesiones, su duración, los grupos de la nivelación y el calendario se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). Las horas de levantamiento se reparten según lo que necesite cada departamento.

## 2. Qué se audita

- **Áreas (como las nombra el cliente)**: Casos de uso de Grupo Leti.
- **Departamentos** (7): Pasos del proceso, Datos que usa, Sistemas involucrados, Volumen y frecuencia, Seguridad y riesgo, Políticas de IA vigentes, Quién lo usa.
- **Foco**: El levantamiento parte de los casos que las áreas ya piden al equipo técnico y de las soluciones que ya se entregaron.
- **Para qué**: Ordenar los casos (Qué piden las áreas hoy y qué ya resolvió el equipo técnico.); Elegir la solución (Qué resuelve cada usuario con Copilot y qué se automatiza con n8n.); Mejorar desde ya (Logros inmediatos en uso mientras avanza el levantamiento.); Cuidar la información (Arquitecturas que respetan la seguridad de Grupo Leti y sus datos.).
- **Logros inmediatos mínimos del proyecto**: 3 (no uno por área: un proceso de mucho esfuerzo pasa al mapa).

## 3. Ruta por etapas (slide 3)

1. **Arranque**: Reunión para cerrar el alcance, la lista de casos de uso y el calendario.
2. **Levantamiento**: Un caso a la vez, con el equipo técnico y el área que lo pidió. · 12 horas de levantamiento, repartidas según lo que necesite cada caso.
3. **Clasificación**: Cada caso se asigna a la vía que necesita, según lo que se levantó.
4. **Priorización**: Intezia ordena los casos por impacto, esfuerzo y riesgo, con su arquitectura sugerida.
5. **Informe Final**: Clasificación, arquitectura y hoja de ruta, presentados a la dirección.

## 4. Entregables (slide 5)

- Al arrancar · **Alcance y calendario**: Acordados en el arranque: los casos de uso que entran y el orden del levantamiento.
- En el levantamiento · **Logros inmediatos**: Al menos tres mejoras en uso desde el primer día, identificadas con el equipo en el levantamiento.
- Al cierre · **Casos clasificados**: Cada caso en su vía: lo que resuelve el usuario con Copilot y lo que se automatiza con n8n.
- Al cierre · **Arquitectura sugerida**: Para cada caso, la solución recomendada y con qué piezas, dentro de las reglas de seguridad de Grupo Leti.
- Al cierre · **Mapa de Calor**: Todos los casos de Grupo Leti en un solo mapa, ordenados por impacto, esfuerzo y riesgo, para ver por dónde empezar.
- Al cierre · **Informe Final y hoja de ruta**: Diagnóstico de los casos con las políticas de IA vigentes mapeadas, hoja de ruta y resumen ejecutivo de una página.
- Caja editable «Para todo el proyecto»: Ficha de levantamiento de cada caso de uso; Presentación del Informe Final a la dirección.
- Caja editable «Valor inmediato»: Logros inmediatos en uso antes de cerrar el proyecto; Datos para decidir por dónde empezar.

## 5. Fuera de alcance

- Licencias y herramientas de IA: no están en la inversión de esta propuesta.
- Cambios en SAP y en los sistemas de Grupo Leti: el levantamiento no los modifica.
- Integraciones con SAP y orquestación compleja de agentes: quedan fuera de esta propuesta.

## 6. Supuestos a confirmar

- Alcance pedido por Ivana (14/10/2026): solo una propuesta de Detección. No se incluyen la propuesta de Políticas (va aparte y esta no la menciona), ni Habilidades ni Innovación, ni la ruta completa de servicios; el deck termina en el Informe Final. Sin facilidad de pago (criterio de Ivana en las Detecciones recientes; el estándar sería 50 % al aprobar y 50 % con el Informe Final).
- Insumo: el resumen de Flavia de su reunión con el responsable técnico de Grupo Leti. No hubo Ficha de Levantamiento ni transcripción (CLAUDE.md §4.23): los tres dolores de la portada son lo que ella cuenta que dijo el cliente, sin nombres de personas.
- Estructura: Detección técnica acotada a los casos de uso de Grupo Leti, no por áreas (la ruta que propone Flavia). Por eso hay un solo «área» a auditar, «Casos de uso de Grupo Leti», sin departamentos ni nombre de la unidad (Ivana: «habla como Grupo Leti»). Las reglas de Keiber siguen: horas en global, al menos 3 logros inmediatos, entregables sin conteos, sin frentes prioritarios.
- En la slide 2, las píldoras que en otras Detecciones son los departamentos se usan aquí para «Qué miramos en cada caso» (proceso, datos, sistemas, volumen, seguridad y usuarios), porque la propuesta no es por departamentos y la tarjeta quedaba vacía. En programa.md aparecen rotuladas como «Departamentos».
- Horas (elegidas por Ivana entre 8, 12 y 16): 12 h de levantamiento en global, sin nivelación (el equipo ya maneja prompts y usa Copilot, y la formación básica no es su prioridad) y arranque sin horas. Total interno: 12 h.
- Dos vías: lo que el usuario resuelve con Copilot y lo que se automatiza. Flavia proponía una tercera vía (lo que no resuelven ni Copilot ni la automatización); Ivana pidió quitarla de toda la propuesta y no nombrar ninguna otra («deja Copilot o automatización», 14/10). «Copilot» se nombra porque es la plataforma del cliente (su estrategia se monta sobre Microsoft por seguridad de la información). **n8n** se nombra a pedido de Ivana, solo junto a «automatización» (slide 2: «qué se automatiza con n8n»; slide 5: tarjeta «Casos clasificados»); no se dice que Intezia sea partner de n8n ni que forme o acompañe. No se nombran Copilot Studio, skills de Claude ni el caso de La Mundial, y no se pre-recomienda otra herramienta: la arquitectura sugerida sale del Informe Final.
- Intezia no construye (Ivana, 14/10: «nosotros no construimos, nada de construir»). Se quitó del deck todo lo que dijera lo contrario: la tercera vía, la caja «Quién construye» de la slide 4 (`metodo.quien_construye` vacío; sin ella, «Por qué en este orden» ocupa todo el ancho), el paso «Construimos» (ahora «Mejoramos»), «cómo construirlo» en la arquitectura y «qué construir primero» (ahora «por dónde empezar» y «qué atender primero»). Lo que dijo Flavia sobre lo que Intezia construye (agentes en Copilot Studio, skills de Claude, asistentes sobre documentos; n8n lo construye el cliente) queda fuera. n8n sí se nombra (ver el supuesto de las dos vías).
- Fuera de alcance: integraciones con SAP y orquestación compleja de agentes (Flavia, a la espera de la lectura de David), más licencias y cambios en SAP. El deck dice que quedan fuera de esta propuesta.
- Políticas de IA vigentes: Flavia propone que la Detección las mapee, porque el cliente ya las tiene. Entra como píldora de la slide 2 («Políticas de IA vigentes») y en el Informe Final (slide 5, sin conteos). El deck no menciona la propuesta de Políticas ni que el mapeo la alimente (instrucción de Ivana: solo Detección).
- Logros inmediatos: son una regla de la Detección (al menos 3, CLAUDE.md §4.22) y el generador no deja ponerlos en cero. Como Intezia no construye, el deck los redacta sin construir: «mejoras en uso desde el primer día, identificadas con el equipo en el levantamiento». Decisión mía por confirmar con Ivana: si los logros inmediatos tampoco van, hay que cambiar el generador o quitar esa promesa del deck.
- «Revisión humana» en el método viene de lo que el cliente busca (que una persona verifique el resultado). El método sigue las prácticas de Keiber (sin tarea previa, sin forzar soluciones).
- No va al deck: el nombre del contacto, que lleva poco tiempo en la empresa, que la formación no es su prioridad, que sus políticas de IA las hizo Ciberseguridad sin experto en IA y obligan a usar solo Copilot (es el ángulo de la propuesta de Políticas), y su visión de que el funcional dibuje el proceso y su unidad lo ejecute (es otra etapa, fuera de esta propuesta).

## 7. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero levantamos cada caso con quien lo conoce. Después lo clasificamos, para que reciba la solución que necesita y no se fuerce un agente donde basta una automatización. Al final priorizamos con la foto completa de Grupo Leti.

- **Entrevistamos**: Al equipo técnico y a quien pidió cada caso de uso.
- **Mapeamos**: El proceso, los datos, los sistemas involucrados y los cuellos de botella.
- **Mejoramos**: Un logro inmediato en el momento, cuando el caso lo permite.
- **Clasificamos**: Cada caso en su vía, con su arquitectura sugerida y su prioridad.

- En la práctica, **Sin tarea previa**: Quien pidió el caso no prepara nada antes: todo se levanta en la conversación.
- En la práctica, **Sin forzar soluciones**: Si un caso exige mucho esfuerzo, no se resuelve en el momento: pasa al Mapa de Calor con su prioridad.
- En la práctica, **Revisión humana**: Cada logro lo revisa una persona de Grupo Leti antes de usarse.
- Datos: Trabajamos con ejemplos reales y solo con las cuentas y la información que Grupo Leti autoriza. Los logros respetan sus reglas de seguridad, y sus sistemas no se modifican.

**Logística:** modalidad: Presencial o virtual: se acuerda con Grupo Leti en la reunión de arranque. · participantes: El equipo técnico y quienes pidieron cada caso de uso. · ritmo: Encuentros en el horario que acuerde cada responsable. · arranque: La fecha la fija Grupo Leti al confirmar la propuesta..

## 8. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Prioridad.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615.

