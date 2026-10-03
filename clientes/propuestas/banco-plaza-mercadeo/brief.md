# Brief — Banco Plaza · Mercadeo con Claude (CAI-024)

## Datos administrativos

- **Empresa**: Banco Plaza
- **Sector**: Banca
- **Slug**: `banco-plaza-mercadeo`
- **División Intezia**: `educacion` (confirmado con el usuario, 2026-09-23 — mismo criterio
  que el resto de clientes corporativos del sistema: AMV Tecnología, Venezolano de Crédito,
  Puro Lomo).
- **Servicio (§4.1a)**: `habilidades` — dado explícitamente por el usuario ("PROPUESTA DE
  HABILIDADES PARA MERCADEO").
- **Tipo de documento**: Capacitación In-Company (`CAI-024`).
- **Fuente**: instrucción directa del usuario, **sin Ficha Comercial** (2026-09-23) — se
  arma a partir del brief que el usuario dio en el mensaje, con datos faltantes preguntados
  directo (división, modalidad, fecha de arranque).

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
  (mismos datos que en Puro Lomo CAP-101 y Venezolano de Crédito CAI-018).
- **Contacto cliente**: Daisy González, líder del área de Mercadeo.

## Qué pide el cliente (mensaje directo del usuario, 2026-09-23)

- Banco Plaza trabaja bajo el ecosistema Microsoft (licencias de Copilot ya adquiridas), pero
  no todos los usan como deberían ni le sacan el máximo provecho.
- **Mercadeo en particular** está dispuesto e interesado en adquirir **licencia de Claude**
  para su equipo — ya entienden el potencial y la necesitan puntualmente para este
  requerimiento. Dato de contexto: es el cliente quien decide adquirir la licencia, Intezia
  no se la vende ni la gestiona.
- **Servicio propuesto**: Intezia produce **~50 creativos publicitarios al mes** para el
  banco — bocetos, bases y llamados a la acción — siguiendo los parámetros de marca y el
  contexto de campaña del cliente. Equivale a lo que un rol interno de creatividad de Intezia
  hace hoy para el propio mercadeo de Intezia (contexto interno para dimensionar el servicio
  — **no se menciona ese nombre ni esa comparación de cara al cliente**).
- **En paralelo**, Intezia capacita al equipo en Fundamentals de Claude, para que entiendan
  cómo usarla y le saquen el máximo provecho.
- **Quick win pedido explícitamente**: no solo entregar el contenido de 1 mes, sino **dejar
  construida (o enseñarles a construir) la Skill** que reproduce ese proceso, para que el
  equipo pueda seguir generando creativos por su cuenta después.
- **Audiencia**: Daisy mencionó que inicialmente serían **2 personas**, pero pidió dejar
  abierta la posibilidad de que participen **las 6 personas** que componen el departamento
  de Mercadeo, si ellos deciden hacerlo así. El deck no fija un número: dice "2 a 6 personas
  del equipo de Mercadeo".
- **Estructura pedida por el usuario**: Kick-off (alinear objetivos y contexto de marca antes
  de iniciar la creación de los creativos) → Capacitación en Fundamentals de Claude → Skill
  para que el equipo repita el proceso solo.

## Decisiones de diseño (2026-09-23)

1. **4 etapas, un solo track**: **Kick-off → Fundamentals → Construcción → Implementación**.
   Ajustado 6 veces el mismo día por instrucción directa del usuario — historial completo:
   - 1ra: "incluye al cliente en las sesiones de construcción y suma esas horas... debería
     ser una propuesta de 10h" — Construcción deja de ser "sin sesiones con el cliente".
   - 2da: "4h de fundamentals, 2h de construcción y 2h de implementación".
   - 3ra: "mejor 2h fundamentals 4h de construcción y 2h de implementación" — Construcción
     sube a 4h, Fundamentals baja a 2h.
   - 4ta: "la propuesta tiene que dar 10h, no reflejas la etapa de construcción... que debe
     ir en el medio, fundamentals construcción e implementación 2h, 4h, 2h" — **reordena** la
     secuencia (Construcción pasa a ir entre Fundamentals e Implementación, no después del
     Kick-off) y pide 10h totales. Claude infirió Kick-off 1h→2h para cuadrar 10h — **esa
     inferencia resultó incorrecta**.
   - 5ta: "hazle una lámina como se lo hiciste a las demás y debe cumplir el orden" —
     Construcción pasa a tener su propia schedule slide (Temas/Timebar/3 columnas), igual que
     Fundamentals e Implementación — antes solo vivía en roadmap + calendario.
   - 6ta: "nooo, el kick off es máximo 1h" + "y no se cuenta dentro de las horas de
     propuesta" — corrige la inferencia de la 4ta: Kick-off vuelve a 1h y queda **fuera** del
     total de horas cotizadas. Con Fundamentals(2h)+Construcción(4h)+Implementación(2h)=8h,
     no 10h — Claude señaló el desfase de 2h.
   - **7ma y vigente**: "sube implementación a 4h" — cierra el desfase: Implementación pasa
     de 2h (1 sesión) a **4h (2 sesiones)**, matching el mismo patrón de Construcción.
2. **Orden y horas finales**: Kick-off (1h, **aparte, no cuenta en el total**) → Fundamentals
   (2h) → Construcción (4h, 2 sesiones de revisión con Mercadeo) → Implementación (4h, 2
   sesiones). **Total de la propuesta: 10h** (2+4+4), kick-off por fuera.
3. **Roadmap de 4 etapas, dividido en 2 páginas**: página 1 = Kick-off + Fundamentals;
   página 2 = Construcción + Implementación (mismo patrón que
   `amv-tecnologia-cerebro-digital/` al pasar de 3 a 4 etapas).
4. **Construcción = 1 mes de producción + 2 sesiones de revisión de 2h con Mercadeo (4h)**,
   secuenciada **después** de Fundamentals (el equipo ya tiene base de Claude antes de
   participar en las revisiones) — se retira el framing "en paralelo" del brief original, ya
   superado por la secuencia estricta de 4 etapas que pidió el usuario.
5. **Construcción SÍ tiene schedule slide propia** (Temas + Timebar + 3 columnas, igual
   tratamiento que Fundamentals/Implementación) — a diferencia de la decisión original. El
   Kick-off sigue siendo la única etapa sin schedule slide dedicada (vive en roadmap +
   calendario), por ser una sesión de alineación, no una sesión curricular.
4. **Sin mención de "Jean"** ni de que Intezia hace esto para su propio mercadeo — dato
   interno para dimensionar el servicio, nunca de cara al cliente.
5. **Sin afirmar migración de Microsoft/Copilot (§4.11)**: Claude se suma al ecosistema que
   el banco ya usa, para un caso puntual (producción de creativos) que Copilot no cubre. No
   se dice que el banco "migra" ni "reemplaza" Copilot.
6. **Licencia Claude — decisión ya tomada por el cliente**, se menciona con confianza (mismo
   criterio que Venezolano de Crédito), no como recomendación preliminar a validar.
7. **Modalidad: a definir con Daisy González** (dato pendiente, igual criterio que Puro
   Lomo/Adriana) — no se asume presencial ni remota.
8. **`fecha_arranque_deseada`** (dato directo del usuario, 2026-09-23): Kick-off **jueves 1
   de octubre de 2026, 10:00-11:00**. Sesiones de Capacitación: **lunes y miércoles, 10:00 a
   12:00**, a partir del 5 de octubre → Fundamentals lunes 5 de octubre, Construcción de la
   Skill miércoles 7 de octubre (2 sesiones cubren el alcance de esta propuesta — no hace
   falta más cadencia). `resultados_esperados`: no se preguntó explícitamente — la
   proyección del calendario y el ROI se redactan desde el alcance ya definido (contenido del
   mes + Skill operativa al cierre).
9. **Con certificado de participación INTEZIA** — es Habilidades con capacitación real, no
   Detección (mismo criterio que Venezolano de Crédito / Puro Lomo).
10. **Garantía 30-60-90 y slide de Seguimiento**: aplican — servicio = habilidades. Nuevo
    estándar del sistema desde 2026-09-23 (ver `clientes/propuestas/
    amv-tecnologia-cerebro-digital/`).

## Impacto (§4.9)

Reutiliza las cifras ya verificadas de `puro-lomo-bajo-mercadeo/` (mismo eje temático:
adopción de IA en tareas de mercadeo/creatividad) — HubSpot (State of AI for Marketers,
2025), Salesforce (State of Marketing, 10ª edición, 2026), McKinsey (The Economic Potential
of Generative AI, 2023). Mismo criterio de reutilización que ya aplica entre otros decks del
sistema (ej. `amv-tecnologia-cerebro-digital/` reutilizó la cifra de McKinsey 2012 ya usada
en `pago-tronic/`).

## Entregables

- 50 creativos publicitarios del mes (bocetos, bases, llamados a la acción), producidos por
  Intezia según los parámetros de marca del banco.
- Skill de Claude operativa para reproducir el proceso de generación de creativos.
- Workbook digital y certificado de participación INTEZIA.

## Corrección de copy (2026-09-24) — título de portada y cita de la slide 2

Instrucción directa del usuario: los títulos de portada de las 3 propuestas de Banco Plaza
"no son atractivos a simple vista" y no causan el impacto buscado; además, la cita de la
slide 2 ("Necesitamos más contenido, no más personas.") **no fue algo que el cliente dijo** —
riesgo de atribuirle una frase textual que no pronunció.

- **Portada**: "El contenido del mes, y la skill para repetirlo." → **"Contenido que atrae,
  solo y sin sumar más personas."** — mismo mensaje de fondo (autonomía, sin más headcount)
  pero como propuesta de valor directa, no descripción de mecánica.
- **Slide 2 (Pain)**: la cita se reescribió como una síntesis estratégica del enfoque
  (ahorro de tiempo + el departamento atrayendo por sí solo), no como frase textual atribuida
  al cliente: **"Que el contenido trabaje solo, mientras el equipo hace lo demás."**
  El párrafo de contexto y el Diagnóstico (5 puntos) no cambiaron — ya eran descriptivos, no
  citas inventadas.

## Notas internas

- Caso base estructural: `amv-tecnologia-cerebro-digital/` (CAI-023) — mismo shell
  (`toyocentro/`), mismos estándares nuevos de 2026-09-23 (descuento urgente, calendario
  completo, ROI, garantía + slide de Seguimiento 30-60-90, `.timebar` en cronogramas).
  Simplificado a 1 solo track (sin 2 funciones) y 3 etapas (sin la 4ta etapa de
  Implementación de CAI-023, que aquí ya está cubierta por la etapa de Capacitación).
- Precedentes de contenido: `puro-lomo-bajo-mercadeo/` (CAP-101, Aprobada — patrón "Skills
  por proceso", datos de Impacto) y `venezolano-de-credito/` (CAI-018 — banco + Mercadeo,
  tono y encuadre de Claude "ya decidida por el cliente").
- **Pendientes de confirmar con Flavia antes de enviar**: modalidad de las sesiones, y si
  Mercadeo arranca con 2 o más personas (afecta solo la logística, no el precio ni el
  contenido del programa).
