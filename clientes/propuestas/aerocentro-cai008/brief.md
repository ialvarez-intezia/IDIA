# Brief — Aerocentro · Nivelación en Claude (CAI-008)

## Origen y contexto comercial

Aerocentro venía conversando con Intezia sobre **CAP-082** (Torre de Control de IA, 3 fases,
15-20 personas, `clientes/propuestas/aerocentro/`). Ante esa escala, Flavia propuso reenfocar
el proyecto en algo más introductorio y escalable: nivelar al corporativo en el uso de Claude
primero, para que empiecen a tener capacidades instaladas y las apliquen en su día a día. Más
adelante, si les hace sentido, se retoma la conversación del proyecto de mayor escala.

**Isaac** (contacto del lado de Aerocentro) aceptó este reenfoque y pidió la nueva propuesta.
Por instrucción del usuario, **esta propuesta se presenta como autónoma**: no menciona CAP-082
ni el proyecto de mayor escala en ningún lugar del deck — es una capacitación en sí misma.

## Preguntas resueltas con el usuario

1. **Servicio**: Habilidades (pura, sin auditoría ni fases posteriores).
2. **Duración**: 3 sesiones de 2h (6h total) — no 8h ni 12h.
3. **Modalidad**: se deja abierta, "a definir en la próxima reunión" (mismo criterio que
   CAP-082), no se confirma Presencial pese a que el usuario mencionó que "podría ser".
4. **Narrativa**: propuesta autónoma, sin referencias a CAP-082 ni al proyecto de mayor escala.

## Datos administrativos

- **Empresa**: Aerocentro · empresa de aviación (operación de aeronaves, taller/mantenimiento
  y charters) — mismo cliente de `aerocentro/` (CAP-082), contexto reutilizado.
- **Slug**: `aerocentro-cai008`
- **División Intezia**: `educacion` (cliente corporativo, heredado de CAP-082)
- **Servicio** (Modelo Intezia): `habilidades`
- **Código**: `CAI-008` (confirmado libre — CAI-001 a CAI-007 pertenecen a otros clientes)
- **Eje temático**: nivelación introductoria en Claude (fundamentos, Projects, Skills y
  Artifacts) para el corporativo de Aerocentro
- **Fecha del brief**: 2026-09-03
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414 5756615 · fmartinez@intezia.com
  (misma asesora de CAP-082).
- **Cliente / interlocutor**: Isaac — aceptó el reenfoque de la propuesta. Dato interno, **no
  se nombra en el deck** (mismo criterio que el resto del sistema): el deck habla de "el
  equipo" o "el corporativo de Aerocentro".
- **Servicio previo con Intezia**: no cerrado todavía — CAP-082 sigue como propuesta separada,
  sin tocar por este ajuste.

## Alcance pedido por el cliente

- Enfocada **únicamente en la capacitación/nivelación inicial** del personal, sin auditoría ni
  las fases posteriores por ahora.
- Debe indicar claramente **qué temas se van a dar y con qué nivel**: perfiles sin
  conocimientos previos sobre la herramienta, así que se empieza por algo introductorio (qué
  es Claude, cómo funciona) y luego se desglosa todo lo que se les enseñará.
- Grupo estimado: **aproximadamente 10 personas**.
- Modalidad: podría ser presencial — se deja abierta en el deck (ver preguntas resueltas).

## Curriculum (3 módulos, 6h)

Reutiliza el vocabulario de Fundamentos ya trabajado con Aerocentro en CAP-082 (Skill, Project
y Artifact) — continuidad de contenido pedagógico, no de narrativa comercial (la propuesta no
referencia CAP-082 explícitamente).

1. **Módulo I · Fundamentos de Claude** (2h): qué es la herramienta y cómo funciona, anatomía
   de un buen prompt, primeros resultados con casos reales, errores comunes al empezar.
2. **Módulo II · Projects y contexto propio** (2h): qué es un Project, organización de
   información real de Aerocentro, consultas con contexto propio, reportes asistidos.
3. **Módulo III · Skills y Artifacts** (2h): qué son, automatización de una tarea real, uso
   responsable de la información, plan de continuidad.

Cada módulo cierra con un logro concreto aplicado a un caso real de Aerocentro (patrón
"Fundamentals con logros inmediatos").

## Restricciones de copy

1. **Sin nombres propios de personas** en el contenido — solo "el equipo" / "el corporativo de
   Aerocentro". El nombre de Flavia sí aparece en el bloque de contacto del Cierre.
2. **Sin presupuesto** ni condiciones de pago en el deck (§4.15) — cotización vacía, la llena
   ventas.
3. **Sin referencias a CAP-082** ni al proyecto de mayor escala (Torre de Control de IA) — ver
   "Preguntas resueltas", punto 4.
4. **Modalidad abierta**: "a definir en la próxima reunión", no se afirma Presencial.

## Propuesta económica

- **Hoja "Propuesta Económica"** estándar (`.s-price`, no multi-fase): Duración + Programa +
  Cotización + Notas. Todas las cajas vacías — las llena ventas. Vigencia: 30 días + T&C.

## Notas de diseño

- Clonado de `grupo-ferrara-cai007/` (CAI-007, mismo patrón de 3 módulos/6h con 1 slide de
  cronograma por sesión, Beneficios v3, Cierre escalera). Se adapta de una capacitación
  personalizada de 2 participantes (con visita a domicilio) a una capacitación de grupo (~10
  personas), un solo tema (Claude, no Gemini+Claude), y modalidad abierta en vez de confirmada.
  12 slides.
- **Beneficios por servicio (Habilidades)**: formato v3 — Resultados / Por qué Habilidades /
  Entregables / Valor inmediato. Entregables SÍ incluye certificado de participación (grupo
  con capacitación real de 6h).
- **Impacto (§4.9)**: se reutilizan las fuentes reales ya verificadas para este tipo de
  narrativa de adopción de IA (Stanford HAI AI Index Report 2026, McKinsey The State of AI
  2025, Anthropic Economic Index 2025) — mismo fenómeno que describe el diagnóstico (equipo
  sin dominio de la herramienta, adopción dispareja).
- **Correo de cierre**: `servicio@intezia.com` (estándar).
- **§4.11**: no se afirma que Aerocentro migra o adopta un nuevo stack — Claude se presenta
  como la herramienta que el equipo aprende a usar, no como un cambio de plataforma existente.
- **§4.12**: "Skill", "Project" y "Artifact" se mantienen en inglés (términos nativos de la
  herramienta Claude), explicados en su primera aparición en cada slide donde aparecen.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh aerocentro-cai008
python3 scripts/customize-acroforms.py aerocentro-cai008
python3 scripts/customize-aerocentro-cai008.py "clientes/propuestas/aerocentro-cai008/<PDF generado>.pdf"
```

## Pendientes

- Confirmar modalidad (Presencial / Online Síncrono / Híbrido) en la próxima reunión.
- Confirmar fechas de las 3 sesiones y disponibilidad del grupo de ~10 personas.
- Confirmar presupuesto — cajas de cotización vacías en el PDF, las llena ventas.
