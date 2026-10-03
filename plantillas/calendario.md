# Plantilla: Calendario y seguimiento

> Define cómo modelar una capacitación en **eventos de Google Calendar** y cómo registrar el seguimiento. Usa el MCP `claude_ai_Google_Calendar`.

---

## Tipos de evento

Toda capacitación se descompone en eventos de cuatro tipos:

| Tipo | Cuándo | Qué representa |
|---|---|---|
| **SES** — Sesión sincrónica | Cada sesión presencial o virtual en vivo | Hora exacta, ubicación o link. |
| **DLN** — Deadline asincrónico | Solo en formaciones online y cursos largos | Fecha límite de entrega de actividad. |
| **HIT** — Hito de seguimiento | Mediano y largo plazo | Reunión interna o con cliente para revisar avance. |
| **CRR** — Cierre / impacto | Una vez, 30–60 días post-programa | Reunión de evaluación de impacto. |

---

## Convención de nombre del evento

```
[Intezia] {{tipo}} {{empresa}} — {{programa}} — {{detalle}}
```

Ejemplos:

- `[Intezia] SES Banco Pacífico — Liderazgo — Sesión 2/4`
- `[Intezia] DLN Banco Pacífico — Liderazgo — Entrega caso módulo 3`
- `[Intezia] HIT Banco Pacífico — Liderazgo — Revisión de avance con RH`
- `[Intezia] CRR Banco Pacífico — Liderazgo — Evaluación de impacto`

---

## Campos por evento

Cuando crees el evento vía MCP, usa estos campos:

| Campo GCal | Cómo llenarlo |
|---|---|
| `summary` | Según convención de nombre. |
| `description` | Objetivo de la sesión + link a `clientes/<empresa-slug>/programa.md` + facilitador. |
| `start` / `end` | Hora local del cliente. Validar zona horaria con el usuario. |
| `location` | Dirección física **o** link de videollamada. |
| `attendees` | Solo si el usuario lo confirma. Por defecto, no añadir asistentes externos automáticamente. |
| `reminders` | Por defecto: 1 día antes (popup) y 1 hora antes (email) para `SES` y `CRR`. |
| `colorId` | Asignar color por programa para distinción visual (opcional). |

---

## Antes de crear los eventos

**Confirmar siempre con el usuario**:

1. Calendario destino (¿personal o de Intezia?).
2. Fechas y horas exactas.
3. Si se invita o no a contactos del cliente.
4. Zona horaria.

No crees eventos sin confirmación. Crear eventos en GCal es una acción visible y difícil de revertir si son muchos.

---

## Registro local de seguimiento

Después de crear los eventos en GCal, registra los IDs en `clientes/<empresa-slug>/calendario.md` con esta estructura:

```markdown
# Calendario — {{empresa_cliente}} / {{programa}}

**Calendario destino**: {{nombre_calendario_gcal}}
**Zona horaria**: {{tz}}
**Estado**: {{planificado | en curso | finalizado}}

## Eventos

| # | Tipo | Fecha | Hora | Título | GCal ID | Estado |
|---|---|---|---|---|---|---|
| 1 | SES | 2026-05-12 | 09:00–13:00 | Sesión 1/4 | `abc123...` | confirmado |
| 2 | SES | 2026-05-19 | 09:00–13:00 | Sesión 2/4 | `def456...` | pendiente |
| ... | | | | | | |

## Notas de seguimiento

- _ej. 2026-05-12: Sesión 1 ejecutada. 14/15 asistentes. Feedback: ___._
- _ej. 2026-05-15: Cliente pide adelantar sesión 3 — se reagenda al 26/05._
```

Este archivo es la **fuente de verdad local** del seguimiento. Google Calendar es la fuente de verdad de los eventos en sí.

---

## Operaciones comunes

### Reagendar una sesión

1. Pedir nueva fecha al usuario.
2. Actualizar el evento en GCal vía MCP `update_event` usando el ID guardado.
3. Actualizar la tabla en `calendario.md`.
4. Añadir nota en "Notas de seguimiento" con el cambio y la razón.

### Cancelar una sesión

1. Confirmar con el usuario.
2. Eliminar evento en GCal vía MCP `delete_event`.
3. Marcar el evento como **cancelado** en la tabla (no borrar la fila — queda como historial).
4. Añadir nota explicando la razón.

### Cerrar el programa

1. Cuando se complete el evento `CRR`, cambia el campo `Estado` a `finalizado`.
2. Resume en "Notas de seguimiento" los hallazgos clave del programa.

---

## Notas para Claude

- **Nunca** crees eventos masivos sin confirmar fechas, horas, calendario destino y asistentes.
- Si el usuario te pide "agenda todo el programa", primero **muestra una tabla preview** de los eventos que vas a crear y pide confirmación.
- Si encuentras un conflicto de horario al consultar GCal, avisa al usuario antes de crear.
