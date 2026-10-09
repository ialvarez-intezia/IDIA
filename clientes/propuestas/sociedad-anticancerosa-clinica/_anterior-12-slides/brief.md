# Brief — Sociedad Anticancerosa de Venezuela (Clínica)

---

## Datos administrativos

- **Empresa**: Sociedad Anticancerosa de Venezuela (Clínica) — organización sin fines de lucro,
  sector salud (oncología)
- **Sector**: Salud / oncología, ONG
- **Tamaño**: Micro / Pyme (menos de 50 empleados)
- **Slug**: `sociedad-anticancerosa-clinica`
- **División Intezia**: `educacion` — **confirmada explícitamente con el usuario** (vía
  `AskUserQuestion`, 2026-09-25): aunque la ficha describe a la Sociedad como "organización sin
  fines de lucro", el servicio contratado es una Detección corporativa estándar (auditoría de
  Administración y Central de Citas, pagada), no un programa social/comunitario — el carácter de
  ONG explica su restricción de presupuesto, no cambia la naturaleza del servicio. Se preguntó
  porque `empresa/divisiones.md` es explícito: "No se asume ni se infiere."
- **Servicio (§4.1a)**: `deteccion` — servicio de interés declarado en la ficha junto con
  Habilidades, pero el usuario solo pidió esta propuesta (código DET-, singular). Ver "Alcance"
  abajo.
- **Tipo de documento**: Detección (`DET-023`) · Fundamentals (2h grupal) + auditoría de 2 áreas
  (Administración operativa, Central de Citas), 4 horas por área (8h), 10h totales, modalidad
  mixta.
- **Eje temático**: Auditar Administración operativa y Central de Citas con un logro inmediato
  en cada área, empezando por automatizar las respuestas repetitivas de los 400 mensajes diarios
  de Central de Citas y revisar la conciliación bancaria que hoy toma 2 días a la semana.
- **Fecha del brief**: 2026-09-25
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Sociedad Anticancerosa de
Venezuela (Clínica)** (`Levantamiento_Sociedad_Anticancerosa_de_Venezuela_Clinica_2026-09-25.pdf`,
registrada 2026-09-24), elaborada por la asesora **Verónica Rubio**.

## Contacto

- **Asesora comercial**: Verónica Rubio.
- **Contacto**: Lino L. Olivieri, Director de la Clínica — alto compromiso personal, "voz
  cantante" de la reunión, pero **no confirmado como firmante final**: la ficha aclara que Lino
  "está un paso por debajo de la dirección general" y que "no confirmó quién firma en
  definitiva". Se trata a Lino como champion/contacto operativo en el deck, sin asumir que
  aprueba la contratación por sí solo (Próximos pasos y Cierre lo reflejan así).
- **Servicio previo con Intezia**: ninguno — primer contacto.

## Alcance — solo Detección (Propuesta única, sin combo Habilidades)

La ficha registra "Servicios de interés: Detección, Habilidades" y trae un
`Bloque específico · Habilidades` completo (qué debe poder hacer el equipo, tareas reales,
modalidad preferida: Mixta). **El usuario pidió una sola propuesta, bajo DET-023** — se
construye como Detección pura (con Fundamentals incluido, lineamiento por defecto), sin combo de
Habilidades. El contenido del Bloque específico de Habilidades queda documentado aquí como
contexto para una eventual Propuesta 2, **no solicitada todavía** (mismo patrón que
Toyocentro/AMV con su fase de Habilidades futura mencionada solo como nota interna).

## 2 áreas de Detección (dato directo de la ficha, sin ambigüedad)

1. **Administración operativa de la clínica** (compras, pagos, conciliación) — responsable:
   Coordinador de administración. ~4 personas.
2. **Central de Citas / Atención al cliente** (confirmación de pacientes, médicos y
   procedimientos). ~5 personas.

**Headcount total del universo**: ~4 en administración operativa + 5 en Central de Citas + ~6
más en sede administrativa (Gerente de Administración, Gerente de Operaciones, analistas) — el
universo de Fundamentals queda cómodamente bajo el máximo de 25 personas.

## Dimensionamiento (lineamiento por defecto — sin instrucción de acortar horas)

- **4 horas por área** × 2 áreas = **8 horas**.
- **+ 2 horas de Fundamentals grupal** (dentro del máximo de 25 personas).
- **Total: 10 horas.**
- **Modalidad mixta**: la ficha no especifica modalidad explícita para las sesiones de
  Detección en sí (a diferencia de otras fichas de esta serie), pero el `Bloque específico ·
  Habilidades` sí registra "Modalidad preferida: Mixta" para el proyecto en general, y hay 2
  sedes físicas involucradas (Clínica y sede administrativa). Se infiere modalidad mixta para
  toda la propuesta por estas dos señales — **confirmar con Verónica antes de enviar** si el
  cliente prefiere una combinación distinta.

## Logro inmediato — con 2 candidatos reales ya identificados por el cliente

A diferencia de Andrómeda (diagnóstico puro) y más parecido a Toyocentro/AMV Tecnología, aquí el
cliente **ya identificó explícitamente 2 quick wins** en la propia reunión (Bloque F, "Logro(s)
inmediato(s) ya identificado(s)"):

1. **Central de Citas**: automatizar respuestas repetitivas y la integración con el sistema de
   agendamiento (400 mensajes/día, con mensajes que quedan sin responder o mal respondidos —
   cita textual: *"son cosas que son bastante repetitivas, sin embargo, salen mucho mal... es
   como 400 mensajes al día, y se quedan mensajes sin responder, no se responden de la manera
   adecuada"*).
2. **Administración**: revisar la continuidad de un bot de conciliación **ya comprado pero
   abandonado por resistencia al cambio del equipo** — cita textual: un analista *"gasta dos
   días de la semana haciendo conciliación en el caché"*.

Se usa el patrón `toyocentro/velas-3n` (auditoría + construcción de un logro tangible en la
misma sesión de 4h), **no** el patrón `pilotes-perforados/andromeda`.

## Resistencia al cambio — tema explícito a abordar en Fundamentals

Observación clave del Bloque F (cita textual): *"Adopción actual desordenada: Copilot
subutilizado, ChatGPT personal no oficial, y un bot de conciliación ya comprado pero abandonado
por resistencia al cambio — esto valida fuertemente arrancar con Detección + Fundamentos de IA
para bajar esa resistencia."* Este es un dato de diseño real y explícito: la sesión de
Fundamentals no es solo nivelación técnica, es la palanca para reducir la resistencia que ya
hizo fracasar una automatización anterior (el bot de conciliación). Se refleja en el framing de
la slide de Fundamentals y en el Diagnóstico.

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: Microsoft 365.
- **Uso de IA hoy**: licencia de Copilot (Microsoft) genérica, sin la base de datos de la
  sociedad cargada — "nos pagan la suscripción" y prácticamente no se usa a nivel organizativo.
  Lino usa ChatGPT personal, no integrado a la información de la empresa. Existe un bot
  comprado para conciliación bancaria que no se usa por resistencia al cambio del equipo.
- **Equipos médicos con IA embebida** (endoscopio Fuji, dos ultrasonidos): "no trasciende" del
  equipo — **fuera de alcance** de esta Detección (no son parte de Administración ni Central de
  Citas); no se menciona en el deck.
- **Cuál les gustaría incorporar**: "aún no lo saben, esperan la recomendación" — 100%
  Metodología ABR, mismo criterio que Toyocentro.
- **Sin certeza de política de datos/seguridad formal** — nunca se la han informado a Lino en
  su tiempo trabajando ahí.
- **Presupuesto**: no definida aún — es una ONG que funciona con financiamiento por proyecto,
  sin disponibilidad garantizada. **Apertura al cambio: Media. Patrocinio ejecutivo: aún no
  asegurado** — el deck no debe asumir ni proyectar un compromiso ejecutivo más fuerte del que
  la ficha confirma (mismo criterio que Dumogas).

## Objetivo final esperado del Reporte Final (Bloque G)

Optimizar sustancialmente Central de Citas (respuestas automatizadas, integración con el
sistema de citas) y los procesos administrativos (conciliación), reduciendo tiempo y errores en
estas dos áreas priorizadas. Horizonte: corto plazo (0-3 meses) — urgencia explícita confirmada
por Lino: *"son los dos sitios donde voy a llevar con urgencia a hacer un cambio."*

## Decisiones confirmadas / sin ambigüedad

1. **2 áreas de Detección** (Administración operativa, Central de Citas) — dato directo de la
   ficha.
2. **Solo Detección, sin combo Habilidades** — el usuario pidió una sola propuesta.
3. **Con logro inmediato por sesión**, con 2 candidatos reales ya validados por el propio
   cliente (no inventados).
4. **División Educación** — confirmada explícitamente con el usuario pese al carácter de ONG.
5. **Sin nombrar los equipos médicos con IA embebida** (fuera de alcance).
6. **Sin afirmar patrocinio ejecutivo fuerte ni a Lino como firmante final** — la ficha aclara
   que la decisión probablemente escale a Dirección General.
7. **Sin certificado de participación** en Entregables — Detección es una auditoría, no un
   curso (`deteccion-sin-certificado.md`).

## Impacto (§4.9, verificado por WebSearch 2026-09-25)

- **Robotham D, Satkunanathan S, Reynolds J, Stahl D, Wykes T — "Using digital notifications to
  improve attendance in clinic: systematic review and meta-analysis", BMJ Open, 2016**: los
  pacientes que reciben notificaciones automatizadas de sus citas tienen 23% más probabilidad de
  asistir (67% vs. 54% sin notificaciones) y 25% menos probabilidad de faltar (15% vs. 21%).
  Fuente académica verificada directamente (BMJ Open, revista revisada por pares) — conecta
  directo con el dolor real de Central de Citas (400 mensajes/día, confirmaciones manuales).
- **Ardent Partners — Accounts Payable Metrics That Matter (2025)**: 32.6% de tasa promedio de
  procesamiento de facturas sin intervención manual en la industria — mismo dato ya verificado y
  usado en AMV Tecnología (DET-019), reutilizado aquí porque conecta directo con la conciliación
  manual de Administración (2 días a la semana, factura por factura).

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Notas internas

- Caso base estructural: `toyocentro/` (DET-014) — mismo patrón de Fundamentals + N áreas a 4h
  con logro inmediato, roadmap `.rmx-linear` de 3 etapas, Beneficios v3, Cierre escalera, precio
  estándar. Adaptado de 2 áreas (Ventas/Tecnología) a 2 áreas distintas (Administración/Central
  de Citas), y de presencial puro a modalidad mixta.
- **Bloque específico Habilidades (no usado en este documento, contexto para una Propuesta 2
  futura si se solicita)**: qué debe poder hacer el equipo — los procesos de atención al
  paciente y conciliación; tareas reales: conciliación bancaria/de caché, manejo de Central de
  Citas; modalidad preferida: Mixta.
- **Pendientes (a confirmar con Verónica antes de enviar)**: modalidad exacta por sesión (se
  infirió mixta, sin dato explícito para Detección específicamente), fechas del kick-off y de
  las 2 sesiones de área, y quién firma en definitiva (pendiente de escalar a Dirección General
  según la propia ficha).
