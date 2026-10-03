# Brief — Pago Tronic · Cerebro Digital de IA por Áreas (CAP-081)

## Datos administrativos

- **Cliente**: Pago Tronic · empresa de envío de remesas, compite directamente con Western Union · oficinas en Miami
- **Naturaleza**: Capacitación in-company · **plan de negocio + "cerebro digital" de IA que ordena y potencia 4 áreas de prioridad alta**. No es una capacitación técnica por skills: es una hoja de ruta de negocio, área por área, de dónde está el cliente hoy a dónde lo lleva el cerebro digital.
- **Slug**: `pago-tronic`
- **División Intezia**: `educacion` (cliente corporativo)
- **Tipo de documento**: Capacitación (`CAP-081`)
- **Programa**: Cerebro Digital de IA — Pago Tronic
- **Eje temático**: sistema central de IA aplicado a la operación de una empresa de remesas, ordenando las 4 áreas de prioridad alta: Marketing, Ventas, Compliance y Documentación. El equipo queda con habilidades instaladas para sumar por su cuenta nuevos pilares (Desarrollo, Auditorías, etc.) cuando la empresa lo decida.
- **Modalidad**: Online síncrono
- **Duración**: a confirmar (ver Pendientes)
- **Fecha del brief**: 2026-07-22 · reencuadrado a 4 áreas el 2026-07-28
- **Estado**: `En corrección`

## Contacto

- **Asesor comercial Intezia**: **Flavia Martínez** · +58 414 575 6615 · fmartinez@intezia.com · llevó la reunión presencial en Miami
- **Cliente referente**: pendiente de confirmar (persona/cargo que recibió a Flavia)

## Por qué este proyecto

La reunión arrancó a la defensiva: el cliente no terminaba de entender bien la propuesta ni el logo. A medida que avanzó la conversación, el enfoque le fue convenciendo, y terminó pidiendo él mismo un **plan de negocio junto con un "cerebro digital"** para su operación: un sistema central de IA que ordene y potencie sus áreas clave. Ese giro (de defensivo a pedir el proyecto él mismo) es la evidencia de que el enfoque de negocio, no técnico, es lo que vende aquí.

## Diagnóstico (4 puntos)

1. Marketing corre campañas genéricas, sin distinción por corredor de remesas ni comunidad.
2. Ventas hace seguimiento manual de leads, sin datos consolidados de cada cliente.
3. La revisión de transacciones y la validación de clientes en Compliance dependen de tiempo manual de personas clave, en una industria donde los reguladores exigen rapidez y trazabilidad.
4. Las políticas y procedimientos de Documentación viven repartidos entre archivos y personas, difíciles de mantener al día frente a cambios regulatorios.

> Desarrollo y Auditorías quedaron fuera de la priorización actual (ver Notas de diseño, reencuadre 2026-07-28): el equipo queda capacitado para sumarlas como pilares propios más adelante.

## Estructura del proyecto

### Cerebro digital · 4 áreas de prioridad alta

Sistema central de IA que ordena y potencia:

1. **Marketing** — de campañas genéricas a mensajes segmentados por corredor de remesas y comunidad.
2. **Ventas** — de seguimiento manual de leads a respuesta más rápida y datos de cada cliente.
3. **Compliance** — de horas de revisión manual a alertas que priorizan qué mirar primero.
4. **Documentación** — de políticas dispersas a un solo lugar siempre actualizado.

### Ritmo por área: diagnóstico + construcción + adopción

Cada una de las 4 áreas recorre el mismo camino:

- **Diagnóstico** — 2 sesiones de 2h por área (4h total), para entender sus necesidades reales.
- **Construcción del cerebro** — 1 semana, a cargo de Intezia, sin sesiones con el equipo: arma el cerebro digital con los hallazgos del diagnóstico.
- **Adopción** — 4h por área, para activar el cerebro digital y enseñar a usarlo en el día a día de esa área.

Total por área: 8h (4h diagnóstico + 4h adopción) × 4 áreas = 32h de sesiones en todo el proyecto, más 1 semana de construcción intermedia, repartidas en el tiempo.

## Especificaciones del programa

- **Duración**: por área, diagnóstico 2 sesiones de 2h + adopción 4h; entre ambas, 1 semana de construcción del cerebro digital a cargo de Intezia (fechas exactas a confirmar).
- **Modalidad**: Online síncrono.
- **Audiencia**: líderes de las 4 áreas de prioridad alta; número de participantes a confirmar.
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.

## Propuesta económica

- **Cotización única consolidada**: el cerebro digital se cotiza como un sistema completo de 4 áreas, no como servicios independientes. 1 sola hoja de precio (`.s-price`), sin desglose por área.

## Entregables consolidados

- Cerebro digital de IA operando en las 4 áreas de prioridad alta.
- Informe de diagnóstico por área (punto de partida real).
- Hoja de ruta de implementación priorizada.
- Equipo capacitado para sumar nuevos pilares (Desarrollo, Auditorías, etc.) por su cuenta.
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-081** en INTEZIA Education al cerrar el acuerdo.

## Notas de diseño

- **Reencuadre 2026-07-28 · 6 → 4 áreas de prioridad alta.** El cliente definió que las áreas de prioridad alta son Marketing, Ventas, Compliance y Documentación; Desarrollo y Auditorías salen del alcance de esta propuesta (no se eliminan del diagnóstico como posibilidad futura, se reencuadran como pilares que el equipo podrá construir por su cuenta una vez capacitado). Deck reducido de 18 a **16 slides**: se eliminaron las 2 slides `.s-schedule` de Desarrollo y Auditorías; `.s-program` pasó de 6 a 4 module cards (grid 2×2, ya soportado en `styles.css`); `.s-heatmap` pasó de 6 a 4 filas y Documentación subió de prioridad Media a Alta (impacto Medio → Alto, para mantener consistencia con Marketing/Ventas en el cuadrante favorable); roadmap, ABR y beneficios reescritos a 4 áreas; slide de Impacto perdió la barra y el chip de Desarrollo (ya no es área cubierta) y sumó un dato real de McKinsey Global Institute (2012) sobre tiempo del equipo buscando información dispersa, relevante para Documentación. La aclaración de "habilidades instaladas para sumar nuevos pilares" se incorporó como objetivo específico #3, como bullet del entregable insignia del roadmap y en el beneficio del programa formativo.
- Formato canónico A4 landscape, clon multi-fase de `pilotes-perforados/` (roadmap + mapa de calor), reencuadrado para presentar áreas de negocio en vez de fases técnicas.
- `.s-program`: module cards (una por área), objetivo redactado como movimiento A → B en lenguaje de negocio, sin describir skills ni herramientas de IA por nombre.
- **`.s-schedule`, una por área** (no agrupadas): cada una describe el ritmo de esa área con 3 columnas — "Diagnóstico · hasta 2 sesiones" / "Implementación · 2 sesiones" / "Recursos y entornos" — en vez de las etiquetas genéricas "Estrategias de enseñanza/aprendizaje" del template original. La `.ruta` de cada slide usa el índice del área (1 de 4 … 4 de 4), no un número de sesión.
- `.s-heatmap`: rediseñado a **1 fila por área** (sin sub-filas de tareas) — el mapa de calor de pilotes-perforados con sub-filas por tarea ya tiene un desborde conocido a partir de ~12 filas (ver `plantillas/capacidad-cajas.md`); con pocas áreas x 1 fila se evita ese riesgo y se mantiene el nivel de negocio pedido por el cliente.
- Slide Roadmap: origen (recorrido común por área) → **Etapa 1 Diagnóstico** (hasta 2 sesiones) → **Etapa 2 Construcción** (Intezia arma el cerebro digital con los hallazgos del diagnóstico, sin sesiones con el cliente) → **Etapa 3 Implementación** (2 sesiones, activa el cerebro digital y enseña a usarlo) → resultado (cerebro digital integrado en las áreas de prioridad alta). Reencuadrado el 2026-07-23 (tres rondas de feedback): primero se pasó de 2 sesiones agrupadas a diagnóstico+implementación por área; luego se insertó la etapa de Construcción entre ambas; después se fijaron las horas exactas de cada etapa (diagnóstico 2 sesiones de 2h, construcción 1 semana, adopción 4h por área). El componente `.rmx-*` se extendió de 2 a 3 rutas en el `styles.css` **local** de este deck (nodo/card negro-blanco para la etapa del medio, dentro de la paleta oficial) — ver memoria `roadmap-3-etapas-flex-minheight`.
- Slide de Impacto con datos reales: McKinsey — *The economic potential of generative AI* (2023), McKinsey — *How agentic AI in banking drives KYC/AML transformation* (2025), McKinsey Global Institute — *The social economy: Unlocking value and productivity through social technologies* (2012).
- `[CÓDIGO]` sustituido por CAP-081 en Acreditación.

## Notas internas (NO van al deck ni al cliente)

- **Capacidad de entrega**: validar si el equipo de servicio puede sostener este nivel de entrega antes de comprometer alcance y fechas. David Prato es el perfil técnico más confiable, pero está sobrecargado hoy — mapear su disponibilidad antes de firmar compromisos de fecha con Pago Tronic. El reencuadre a 4 áreas (32h vs 48h de sesiones) reduce parte de esta presión, pero no la elimina.
- **Riesgo a vigilar**: el cliente tiene un tecnólogo nuevo que podría intentar construir esto internamente. Probabilidad baja, pero es razón adicional para que la propuesta muestre valor claro y rápido (ver diseño de la slide de Impacto y del roadmap). El mensaje de "habilidades instaladas para sumar pilares" juega a favor de este riesgo: convierte la construcción interna futura en algo que Intezia habilita, no en algo que compite con la propuesta.

## Pendientes

- Confirmar contacto/cargo de referencia en Pago Tronic.
- Confirmar número de participantes por área.
- Confirmar duración y fechas tentativas.
- Confirmar presupuesto indicativo (no se discutió en la reunión).
- Mapear disponibilidad de David Prato antes de comprometer fechas de entrega (ver Notas internas).
