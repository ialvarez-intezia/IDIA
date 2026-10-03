# Plantilla operativa: Curso / Diplomado

> Refleja el formato oficial `fuentes/formatos-oficiales/curso-diplomado.pdf`. Genera `clientes/propuestas/<slug>/programa.md` con esta estructura cuando el tipo sea **Curso** o **Diplomado**.

> **Pre-requisitos**: `brief.md` con `division: fundacion | educacion`. Si no está, pregunta primero.

---

## Diferencias entre subtipos

| Aspecto | Curso (`CU-`) | Diplomado (`DIP-`) |
|---|---|---|
| Código | `CU-###` | `DIP-###` |
| Mínimo de módulos | **4** | **8** |
| Mínimo de temas por módulo | **5** | **6** |

Todo lo demás es idéntico (acreditación obligatoria con aliado, evaluación 30/50/20, mín 70/100, facilitador ≥ 3 años, ABR, actualización trimestral).

---

## Estructura del documento

```markdown
# Documento Oficial de Diseño Curricular e Instruccional

**[LOGO INTEZIA — `logos/{division}/NEGRO.png`]**  /  **[LOGO Instituto o Universidad]**

# {{Curso | Diplomado}}
## {{Título Oficial}}

**Código**: {{CU | DIP}}-{{NNN}}
**Versión**: (Propuesta Optimizada)
**Elaborado por**: {{nombre_responsable}}
**Aprobado por**: {{nombre_aprobador}}
**Fecha de Aprobación**: {{YYYY-MM-DD}}

---

## 1. Información General del Programa

- **Nombre del Programa**: {{nombre_completo}}
- **Modalidad**: Presencial / Online Síncrono / Online Asíncrono / Híbrido
- **Duración**: {{N}} semanas / {{H}} horas académicas totales
- **Acreditación**: INTEZIA y {{aliado_universitario_o_institucional}}     <!-- aliado obligatorio -->

---

## 2. Fundamentación y justificación pedagógica

### 2.1 Planteamiento de la necesidad

{{Contexto, brecha de conocimiento en el mercado, problema profesional que resuelve.}}

### 2.2 Enfoque pedagógico (Modelo INTEZIA)

Aprendizaje Basado en Retos (ABR):

- **Tutoría activa**: facilitador del éxito, no expositor.
- **Transferibilidad inmediata**: productos aplicables a proyectos reales.
- **Curaduría de contenidos**: actualizado, sin redundancia.

---

## 3. Perfiles académicos

### Perfil de ingreso

- **Requisitos académicos**: {{nivel mínimo / titulación}}
- **Competencias previas**: {{habilidades técnicas o blandas}}
- **Requerimientos técnicos**: {{conectividad, software, hardware}}

### Perfil de egreso

- **Saber (Cognitivo)**: {{...}}
- **Saber hacer (Procedimental)**: {{...}}
- **Saber ser (Actitudinal)**: {{...}}

---

## 4. Objetivos estratégicos

### 4.1 Objetivo general

{{Verbo + Objeto + Condición + Finalidad.}}

### 4.2 Objetivos específicos

1. {{...}}
2. {{...}}
3. {{...}}

---

## 5. Estructura curricular y diseño instruccional

### 5.1 Estructura modular

> **[Solo Curso]**: mínimo **4 módulos**, mínimo **5 temas por módulo**.
> **[Solo Diplomado]**: mínimo **8 módulos**, mínimo **6 temas por módulo**.

| Módulo | Objetivo Instructivo | Temas |
|---|---|---|
| **I: {{nombre}}** | {{...}} | 1.1 / 1.2 / 1.3 / 1.4 / 1.5{{ / 1.6 si diplomado}} |
| ... | ... | ... |

### 5.2 Desglose instructivo (cronograma y ruta de aprendizaje)

| M | Semana | Temas y subtemas | Tiempo | Estrategias enseñanza | Estrategias aprendizaje | Recursos y entornos |
|---|---|---|---|---|---|---|
| I | Semana 1 | Módulo I: {{nombre}} — 1.1, 1.2, 1.3 | Total 2h | Demostración guiada, preguntas socráticas | Plenaria, mini-caso, problema real | Presentación, Miro, Meet |

> **Render en el deck (2026-05-16)**: esta tabla se maqueta como **1 slide por sesión/semana** (`.s-schedule`), no como un slide único. Cada fila → un slide con encabezado de ruta de aprendizaje + los 5 elementos en layout flexible. Ver `plantillas/propuesta-comercial.md` §5.

### 5.3 Sistema de evaluación de los aprendizajes

| Tipo de evaluación | Instrumento / Herramienta | Ponderación | Entrega |
|---|---|---|---|
| Formativa | Participación en foros / Quizzes cortos | **30%** | Continua |
| Sumativa (Parcial) | Entregables modulares / Estudios de caso | **50%** | Al cierre de módulos |
| Sumativa (Final) | Proyecto Final Integrador (Defensa o Dossier) | **20%** | Última semana |
| **Total** | | **100%** | |

> **Calificación mínima para certificación**: 70/100.

---

## 6. Garantía de calidad y mejora continua

- **Actualización curricular**: revisión cada **3 meses** según tendencias de industria.
- **Encuesta de satisfacción**: monitoreo constante.
- **Entregable**: Workbook · Dashboard · **Certificado avalado por INTEZIA y {{aliado}}**.
- **Beneficio del programa formativo**: {{descripción del perfil de egreso + proyectos de [Eje temático del programa] que realizarán}}.

---

## 7. Perfil del equipo facilitador

- **Formación académica**: Certificación experta demostrable.
- **Experiencia profesional**: ≥ **3 años** en el sector.
- **Competencias pedagógicas**: facilitación, entornos virtuales, metodologías activas.
```

---

## Reglas duras (no romper)

| Regla | Curso | Diplomado |
|---|:---:|:---:|
| Código | `CU-###` | `DIP-###` |
| Mínimo de módulos | 4 | 8 |
| Mínimo de temas por módulo | 5 | 6 |
| Aliado obligatorio | ✅ | ✅ |
| Evaluación 30/50/20 | ✅ | ✅ |
| Mín 70/100 para certificación | ✅ | ✅ |
| Actualización curricular trimestral | ✅ | ✅ |
| Eje temático parametrizado | ✅ | ✅ |
| Logo en portada (división) + aliado | ✅ | ✅ |
| Facilitador ≥ 3 años | ✅ | ✅ |

## Antes de entregar — checklist

- [ ] División confirmada (logo correcto)
- [ ] Código asignado (`CU-` o `DIP-`)
- [ ] Aliado universitario/institucional definido
- [ ] Mínimos de módulos y temas según subtipo
- [ ] Evaluación 30/50/20 presente y suma 100%
- [ ] Cadena de coherencia validada
- [ ] Eje temático parametrizado en sección 6
- [ ] Sin placeholders sin llenar
