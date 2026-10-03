# Plantilla operativa: Taller / Capacitación In-Company

> Refleja el formato oficial `fuentes/formatos-oficiales/taller-capacitacion.pdf`. Genera `clientes/propuestas/<slug>/programa.md` con esta estructura cuando el tipo sea **Taller** o **Capacitación**.

> **Pre-requisitos**: `brief.md` con `division: fundacion | educacion`. Si no está, pregunta primero.

---

## Diferencias entre subtipos

> **Código de Capacitación**: `CAI-###` desde 2026-08-30 (antes `CAP-###` — ver
> `empresa/catalogo.md#talleres-y-capacitaciones-in-company`). No retroactivo.

| Aspecto | Taller (`TA-`) | Capacitación (`CAI-`) |
|---|---|---|
| Código | `TA-###` | `CAI-###` |
| Campo `Empresa` en sección 1 | opcional | **obligatorio** |
| Perfil de ingreso (sección 3) | **incluido** | **omitido** |
| Acreditación | INTEZIA + aliado opcional | solo INTEZIA |
| Foco de la necesidad | participante individual | equipo de la empresa |

Todo lo demás es idéntico.

---

## Estructura del documento

```markdown
# Documento Oficial de Diseño Curricular e Instruccional

**[LOGO INTEZIA — `logos/{division}/NEGRO.png`]**  /  **[LOGO Empresa o Aliado]**

# {{Taller | Capacitación In-Company}}
## {{Título Oficial}}

**Código**: {{TA | CAP}}-{{NNN}}
**Versión**: (Propuesta Optimizada)
**Elaborado por**: {{nombre_responsable}}
**Aprobado por**: {{nombre_aprobador}}
**Fecha de Aprobación**: {{YYYY-MM-DD}}

---

## 1. Información general del programa

- **Nombre**: {{nombre_completo}}
- **Empresa**: {{empresa_cliente}}     <!-- [Solo Capacitación] obligatorio -->
- **Modalidad**: Presencial / Online Síncrono / Online Asíncrono / Híbrido
- **Duración**: {{N}} sesiones / {{H}} horas académicas totales
- **Acreditación**: INTEZIA{{ + aliado si aplica}}     <!-- aliado solo en Taller, opcional -->

---

## 2. Fundamentación y justificación pedagógica

### 2.1 Planteamiento de la necesidad

{{Contexto actual, brecha de conocimiento, qué problema resuelve.}}

> **[Solo Taller]**: foco en el problema profesional **del participante individual**.
> **[Solo Capacitación]**: foco en el problema **del equipo de la empresa**.

### 2.2 Enfoque pedagógico (Modelo INTEZIA)

Aprendizaje Basado en Retos (ABR) — tres pilares:

- **Tutoría activa**: facilitador del éxito del estudiante, no expositor.
- **Transferibilidad inmediata**: productos académicos aplicables a proyectos reales.
- **Curaduría de contenidos**: información actualizada y relevante, sin redundancia.

---

## 3. Perfiles académicos

### [Solo Taller] Perfil de ingreso

- **Requisitos académicos**: {{nivel mínimo / titulación}}
- **Competencias previas**: {{habilidades técnicas o blandas}}
- **Requerimientos técnicos**: {{conectividad, software, hardware}}

> **[Solo Capacitación]**: NO incluye Perfil de ingreso. La empresa define quién entra.

### Perfil de egreso (ambos)

- **Saber (Cognitivo)**: {{Comprender, analizar, evaluar... + objeto}}
- **Saber hacer (Procedimental)**: {{Diseñar, implementar, gestionar... + objeto}}
- **Saber ser (Actitudinal)**: {{Liderar, actuar con ética, colaborar... + objeto}}

---

## 4. Objetivos estratégicos

### 4.1 Objetivo general

{{Verbo en infinitivo + Objeto + Condición + Finalidad. Engloba el propósito máximo.}}

### 4.2 Objetivos específicos

1. {{Objetivo específico 1}}
2. {{Objetivo específico 2}}
3. {{Objetivo específico 3}}

> **Regla**: cada específico responde al general → al perfil de egreso → a la necesidad.

---

## 5. Estructura curricular y diseño instruccional

### 5.1 Estructura modular

| Módulo | Objetivo Instructivo | Temas | Elaboración (Práctica del participante) |
|---|---|---|---|
| **I: {{nombre}}** | {{lo que se logrará al finalizar}} | 1.1 / 1.2 / 1.3 / 1.4 | {{aplicación práctica}} |
| **II: {{nombre}}** | {{...}} | 2.1 / 2.2 / 2.3 / 2.4 | {{...}} |

> Cada objetivo instructivo se alinea con uno o varios objetivos específicos.

### 5.2 Desglose instructivo (cronograma y ruta de aprendizaje)

| M | Sesión / Semana | Temas y subtemas | Tiempo | Estrategias enseñanza | Estrategias aprendizaje | Recursos y entornos |
|---|---|---|---|---|---|---|
| I | Sesión 1 | {{...}} | Total Xh | {{...}} | {{...}} | {{...}} |

> **Render en el deck (2026-05-16)**: esta tabla se maqueta como **1 slide por sesión** (`.s-schedule`), no como un slide único. Cada fila → un slide con encabezado de ruta de aprendizaje + los 5 elementos en layout flexible. Ver `plantillas/propuesta-comercial.md` §5.

---

## 6. Garantía de calidad y mejora continua

- **Construcción curricular**: adaptación al interés real {{de la empresa | del participante}}.
- **Encuesta de satisfacción**: monitoreo constante de la experiencia.
- **Entregable**: Workbook · Dashboard · **Certificado de participación**.
- **Beneficio del programa formativo**: {{descripción del perfil de egreso + proyectos de [Eje temático del programa] que realizarán}}.

---

## 7. Perfil del equipo facilitador

- **Formación académica**: Certificación experta demostrable.
- **Experiencia profesional**: ≥ **2 años** en el sector.
- **Competencias pedagógicas**: facilitación, entornos virtuales, metodologías activas.
```

---

## Reglas duras (no romper)

| Regla | Taller | Capacitación |
|---|:---:|:---:|
| Código `TA-` o `CAI-` | TA | CAI |
| Empresa obligatoria | — | ✅ |
| Perfil de ingreso | ✅ | — |
| Aliado de acreditación | opcional | — |
| ABR | ✅ | ✅ |
| Tabla 5.1 con columna "Elaboración" | ✅ | ✅ |
| Cronograma con Sesión/Semana | ✅ | ✅ |
| Sistema de evaluación 30/50/20 | — | — |
| Eje temático parametrizado | ✅ | ✅ |
| Logo en portada (división) | ✅ | ✅ |
| Facilitador ≥ 2 años | ✅ | ✅ |

## Antes de entregar — checklist

- [ ] División confirmada (logo correcto)
- [ ] Código asignado (`TA-` o `CAI-`)
- [ ] Si Capacitación: campo Empresa lleno; **sin** Perfil de ingreso
- [ ] Si Taller: Perfil de ingreso lleno
- [ ] Cadena de coherencia: Necesidad → Egreso → Objetivo general → Específicos → Instructivos
- [ ] Eje temático parametrizado en sección 6
- [ ] Sin placeholders `{{...}}` sin llenar
