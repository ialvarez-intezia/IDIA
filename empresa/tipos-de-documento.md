# Tipos de documento curricular — Intezia

> Este archivo tiene dos ejes. El **§0 Servicio** es el eje primario y bloqueante (ver
> también `CLAUDE.md §4.1a`): toda propuesta se adscribe a uno de los 4 servicios del
> Modelo Intezia antes de generar nada. El resto del archivo (§1 en adelante) describe
> las **tres categorías curriculares**, que hoy en la práctica solo aplican **dentro de
> Habilidades** — los otros tres servicios tienen (o tendrán) su propia estructura de
> entregable, no un deck de charla/taller/curso/diplomado forzado. Desde 2026-10-05 el
> propio servicio de Habilidades se entrega por defecto con la **plantilla compacta**
> (`plantillas/habilidades-compacto.md`); el deck de ~13 slides por categoría queda para
> los casos de la guardia de `CLAUDE.md §4.21`.

---

## 0. Servicio — eje primario y bloqueante

> Origen: `MODELO MAESTRO DE SERVICIO` (Dirección de Productos y Servicios, agosto 2026).
> Antes de generar cualquier salida visual, además de la división (`empresa/divisiones.md`),
> se pregunta y se registra el servicio. Campo obligatorio en `brief.md`:
> `servicio: deteccion | habilidades | politicas | innovacion | integral`.

| Servicio | En una frase | Duración típica | Estado de la estructura de deck |
|---|---|---|---|
| **Detección** | Diagnosticar el negocio, nivelar al equipo y entregar logros inmediatos antes del informe final. | Kick-off + 4 etapas · 5 a 15 días | **Pendiente** — base reaprovechable: clonar y adaptar `clientes/propuestas/pilotes-perforados/` (roadmap origen→bifurcación→rutas→convergencia→resultado + mapa de calor de 6 columnas es estructuralmente cercano a Matriz de Madurez Digital + Protocolo de Clasificación de IA por Impacto vs. Esfuerzo). Sin piloto canónico propio todavía. |
| **Habilidades** | Capacitar al equipo sobre sus propias tareas reales y dejar la capacidad instalada, con adopción verificada a 30-60-90 días. | Kick-off + 3 sesiones de hasta 2h o más | **Vigente — formato por defecto desde 2026-10-05: plantilla compacta** (`plantillas/habilidades-compacto.md`, `CLAUDE.md §4.21`): 5 slides (Portada con titular-objetivo · Alcance · Ruta · Inversión · Entregables) + 1 de retorno esperado opcional, dirigida por `datos.json`; caso base `clientes/propuestas/dusa-cai035/`. Las categorías Charla / Taller / Capacitación In-Company / Curso / Diplomado (§1 de este archivo) siguen existiendo como tipos de catálogo; su deck canónico de ~13 slides solo se usa si el usuario lo elige en la guardia de §4.21 punto 5. Seguimiento 30-60-90 especificado en §0.2. Ajuste pendiente de vocabulario: nombrar Kick-off como Etapa 1, Workbook como entregable insignia. |
| **Políticas** | Formalizar cómo la empresa usa la IA, con gobierno, roles claros y su Brújula IA de herramientas recomendadas. | Kick-off + 3 · 3 a 5 semanas | **Especificación completa desde 2026-09-09** — ver §0.1 (metodología, 4 etapas, roles, entregables). Sigue **pendiente solo la decisión de formato de la propuesta comercial** (Ivana + David: deck vs. informe de consultoría) — se paga por entregable, no por horas de clase, no tiene "Programa de módulos" con sentido real. No construir la estructura de la propuesta hasta que esa decisión de formato se resuelva. |
| **Innovación** | Sostener la madurez con cadencia mensual de charlas y masterclasses, y evaluación continua de adopción de IA. | Kick-off + 2 · 3, 6 o 12 meses | **Piloto**: `clientes/propuestas/zoom-innovacion/` (INN-001, 2026-08-30). Reemplaza "Programa = N módulos" por 3 sesiones/mes de distribución flexible (Opción A, sin desglose por sesión fijo) y resuelve el cronograma recurrente con un roadmap `.rmx-linear` adaptado (Kick-off → Ejecución → Medición → se repite, en vez de fases con fin). Cotización propia: "Inversión por Permanencia" (`CICLO_PRICE_FIELDS`, ver `plantillas/generar-pdf.md`). |
| **Integral** | Ofrecer los 4 servicios de arriba como fases secuenciales de un mismo plan estratégico (Detección → Habilidades → Políticas → Innovación). | Variable — 4 fases, duración de cada una a definir tras el diagnóstico | **Piloto**: `clientes/propuestas/simple-tv-all001/` (ALL-001, 2026-08-28). Clona `aerocentro/` (multi-fase) y extiende su roadmap de 3 a 4 fases. Políticas e Innovación se representan a nivel de resumen de roadmap (tarjeta de etapa + resultado), no con su plantilla dedicada — esa sigue pendiente. Ver `CLAUDE.md §4.1b`. |

**Alianza** — bandera aparte, **no** un valor más de `servicio`: `alianza: sí | no`. Una
propuesta de alianza puede ofrecer cualquiera de los 5 servicios de arriba (con más
frecuencia se parece a Habilidades, pero no asumir). Suele no llevar hoja de cotización y
es menos detallada en el resto del deck — confirmar alcance con el usuario caso por caso.

**Cómo se elige:** igual que división, no se asume ni se infiere — pregunta bloqueante
*"¿Detección, Habilidades, Políticas o Innovación?"* antes de generar nada. Si el cliente pide
los 4 servicios como un solo plan, confirma con el usuario si corresponde `integral` (no se
asume tampoco). División y servicio son ejes **ortogonales**: un cliente puede adquirir
cualquiera de los 5 servicios sin importar su división.

**Habilidades no se clona:** se usa la plantilla compacta dirigida por datos (`CLAUDE.md §4.21`).

**Al clonar (Paso 0 de `CLAUDE.md §6`):** el criterio de reutilización ya no es solo "mismo
tipo de documento + misma división" — ahora es **mismo servicio + mismo tipo de documento +
misma división**. No clonar un deck de Habilidades cuando lo que hace falta es uno de
Detección, aunque los dos sean nominalmente "capacitación in-company".

---

## 0.1 Servicio Políticas — especificación completa

> Fuente: Documento maestro interno de Dirección de Productos y Servicios (compartido por el
> usuario 2026-09-09) — **no distribuir sin adaptar al cliente**. Resuelve el "qué incluye el
> servicio" (metodología, etapas, entregables). **No resuelve** la decisión pendiente de
> formato de la *propuesta comercial* de venta (deck vs. informe de consultoría, fila de la
> tabla de arriba) — esa sigue bloqueante hasta que Ivana + David la definan explícitamente.

**En una frase**: de un uso capacitado a un uso gobernado, con reglas claras para toda la
empresa.

### Metodología y duración

Marco propio: proceso de auditoría con un cuestionario de levantamiento (Bloque Genérico +
Bloque Específico por área) y las **nueve dimensiones de gobernanza de IA** (Annex, AI Verify
Foundation / IMDA) como checklist de cobertura. Duración típica: **3 a 5 semanas** —
diagnóstico por área → cuestionario dirigido por hallazgos → consolidación → borrador de
política → validación y aprobación.

### Las 4 etapas

1. **Kick-off** — sesión de 30 a 60 minutos: se presenta la ruta al cliente y se agendan
   fechas y logística de todos los encuentros del servicio.
2. **Diagnóstico de madurez por área** — sesiones por función con un banco de preguntas y
   evidencia tipificada (documental, entrevista, encuesta, técnica u observación) contra
   bandas de madurez, para saber dónde está parada cada dirección/área antes de escribir
   ninguna regla.
3. **Cuestionario dirigido por hallazgos** — un **Bloque Genérico** común (usos prohibidos,
   datos sensibles, incidentes, rol de responsable de IA, capacitación, KPIs, autonomía) más
   un **Bloque Específico** por dirección/área, redactado desde el hallazgo real de esa área,
   más solicitud de documentación de soporte (inventario de herramientas, gasto, contratos
   con proveedores).
4. **Redacción y validación de la política** — borrador de política priorizado por las
   brechas más críticas, sesión de validación con los responsables de cada área y aprobación
   formal, con calendario de re-diagnóstico. **En paralelo** se elabora la **«Brújula IA»**:
   un documento corto y visual con la recomendación de herramientas de IA que la empresa
   debería adoptar, alineado a las políticas y a la madurez detectada.

### Herramientas y plantillas del servicio

- Cuestionario de levantamiento (Bloque Genérico + Bloque Específico por dirección/área).
- Checklist de las **nueve dimensiones de gobernanza de IA**: Accountability, Datos,
  Desarrollo y Despliegue Confiable, Reporte de Incidentes, Pruebas y Aseguramiento,
  Seguridad, Procedencia de Contenido, I+D de Seguridad y Alineación, IA para el Bien
  Público.
- Matriz de riesgos por dirección/área y por dimensión.
- Plantilla de política de IA organizada por eje/dimensión.
- Estructura de gobernanza propuesta (comité, sponsor ejecutivo, cadencia de revisión).
- **«Brújula IA»**: mapa visual de recomendación de herramientas de IA por área, con el
  nivel de gobernanza que requiere cada una.

### Roles involucrados

- **Consultor líder de Políticas**: conduce el diagnóstico y redacta la política.
- **Directores / líderes de área del cliente**: responden el cuestionario y validan el
  borrador.
- **Comité de gobernanza propuesto**: aprueba la política final y su calendario de revisión.

### Entregables tangibles para el cliente

- Ruta del servicio confirmada en el Kick-off: fechas, logística y responsables de todos los
  encuentros acordados.
- Informe de diagnóstico de madurez por área, con hallazgos y evidencia documentada.
- Manual de políticas de uso responsable de IA, listo para difundir en la empresa.
- Matriz de riesgos y plan de acción, con responsables, plazos y prioridad.
- Marco de gobernanza: roles, permisos y responsables de aprobación.
- Sesión de socialización del manual con todo el equipo, y calendario de re-diagnóstico.
- **«Brújula IA»**: documento de recomendación de herramientas de IA que la empresa debería
  adoptar, alineado a las políticas y a la madurez detectada.

### Precio

Se cotiza **por entregable, no por horas** — una sola entrega del paquete completo de
arriba. Ver `empresa/politicas-comerciales.md` → "Dimensionamiento por servicio".

---

## 0.2 Servicio Habilidades — Seguimiento 30-60-90

> Fuente: explicación del equipo de servicio (compartida por el usuario, 2026-09-23).
> Reemplaza la lectura anterior de los 3 check-ins ("uso vs. esperado → refuerzo → escala o
> cierra Habilidades / pasa a Innovación", antes escrita en `plantillas/kickoff-canonico/
> kickoff.html`). El objetivo del seguimiento no es solo confirmar que se usa lo entregado,
> sino verificar que las habilidades instaladas **se usen, se multipliquen y generen impacto
> real en la productividad** del cliente. Cada check-in mide algo distinto — no se salta de
> "cuántos skills" a "impacto" sin pasar por la etapa de multiplicación.

| Check-in | Pregunta que responde | Qué mide | Qué aporta Intezia |
|---|---|---|---|
| **30 días** | ¿Se usa lo que instalamos? | Uso real de lo entregado en sesión: visita a la compañía para observar si el equipo está utilizando el/los skill(s) instalados. | Nivelación, estrategias y recomendaciones para el uso correcto. |
| **60 días** | ¿Qué más construyeron a partir de ello? | Ya no se revisa el skill entregado en sesión, sino la cantidad y el tipo de skills o soluciones **nuevas** que el equipo construyó por su cuenta a partir del conocimiento recibido. | Mapeo de esas construcciones nuevas y arranque de la medición de ahorro de tiempo y mejora de productividad. |
| **90 días** | ¿Cuánto tiempo ahorraron y en qué lo invierten ahora? | No se cuentan skills: se contabiliza el **tiempo** ahorrado por el equipo gracias a todo lo aprendido, creado y automatizado con IA, en qué se está reinvirtiendo ese tiempo (nuevas tareas o iniciativas asumidas) y qué tan productivo es hoy el área/persona. | Análisis de impacto en productividad — cierre del ciclo de seguimiento. |

**Vigente para:** `plantillas/kickoff-canonico/kickoff.html` (y sus clones ya generados que
se regeneren) y `plantillas/brief-kickoff.md §5`, fila Habilidades. No retroactivo a decks de
propuesta ya entregados (mismo criterio de `CLAUDE.md §4.10a`).

---

## 1. Las tres categorías (dentro de Habilidades)

| Categoría | Subtipos | Plantilla operativa | Formato oficial |
|---|---|---|---|
| **Charla** | — | `plantillas/diseno-charla.md` | `fuentes/formatos-oficiales/charla.pdf` |
| **Taller / Capacitación In-Company** | Taller (`TA-`), Capacitación (`CAI-` desde 2026-08-30, antes `CAP-`) | `plantillas/diseno-taller-capacitacion.md` | `fuentes/formatos-oficiales/taller-capacitacion.pdf` |
| **Curso / Diplomado** | Curso (`CU-`), Diplomado (`DIP-`) | `plantillas/diseno-curso-diplomado.md` | `fuentes/formatos-oficiales/curso-diplomado.pdf` |

> "Online" no es categoría — es atributo del campo Modalidad (Presencial / Online Síncrono / Online Asíncrono / Híbrido) que aplica transversalmente.

---

## 2. Tabla comparativa de campos obligatorios

| Sección | Charla | Taller | Capacitación | Curso | Diplomado |
|---|:---:|:---:|:---:|:---:|:---:|
| Portada con logos (división) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Información general | ✅ | ✅ | ✅ | ✅ | ✅ |
| Empresa (campo) | — | — | ✅ | — | — |
| Acreditación con aliado | — | opcional | — | ✅ | ✅ |
| Planteamiento de la necesidad | ✅ | ✅ | ✅ | ✅ | ✅ |
| Objetivo único (sin específicos) | ✅ | — | — | — | — |
| Enfoque pedagógico ABR | — | ✅ | ✅ | ✅ | ✅ |
| Perfil de participantes (libre) | ✅ | — | — | — | — |
| Perfil de ingreso (formal) | — | ✅ | — | ✅ | ✅ |
| Perfil de egreso (Saber/Saber hacer/Saber ser) | — | ✅ | ✅ | ✅ | ✅ |
| Objetivo general + específicos | — | ✅ | ✅ | ✅ | ✅ |
| Estructura modular (5.1) | — | ✅ | ✅ | ✅ | ✅ |
| Desglose instructivo (5.2) | — | ✅ | ✅ | ✅ | ✅ |
| Sistema de evaluación 30/50/20 (5.3) | — | — | — | ✅ | ✅ |
| Garantía de calidad y mejora continua | ✅ | ✅ | ✅ | ✅ | ✅ |
| Perfil del equipo facilitador | ✅ | ✅ | ✅ | ✅ | ✅ |

> Esta tabla describe los campos del **documento curricular** (`programa.md`). No confundir
> con las slides visuales del deck — la slide de Metodología ABR y el bloque de Equipo
> facilitador **ya no se muestran al cliente** (ver `CLAUDE.md §4.10a`), aunque el enfoque
> ABR y el perfil del facilitador se sigan documentando aquí para uso interno.

---

## 3. Modelo pedagógico oficial: Aprendizaje Basado en Retos (ABR)

Aplica a **Taller, Capacitación, Curso, Diplomado** (NO a Charla). Tres pilares textuales que aparecen en sección 2.2 del programa (documento interno — no se expone como slide, ver `CLAUDE.md §4.10a`):

1. **Tutoría activa** — facilitador del éxito, no expositor.
2. **Transferibilidad inmediata** — productos aplicables a proyectos reales.
3. **Curaduría de contenidos** — actualizado, sin redundancia académica.

---

## 4. Regla de coherencia (alineación constructiva)

```
Necesidad → Perfil de egreso → Objetivo general → Objetivos específicos
        → Objetivos instructivos (de cada módulo) → Temas → Estrategias → Evaluación
```

Si en una propuesta detectas que un objetivo específico **no se conecta** con el general, o que un módulo **no aborda** ningún específico, **flagéalo** y sugiere ajuste antes de entregar.

---

## 5. Eje temático del programa

El campo "Beneficio del programa formativo" en los formatos oficiales menciona "proyectos de IA". Esto es un **placeholder parametrizable**: `[Eje temático del programa]`. Cada propuesta inserta su área concreta (IA, liderazgo, ventas, comunicación, etc.). **No asumir IA por defecto.**

---

## 6. Notas para Claude

- Para detalles operativos por subtipo (códigos, mínimos de módulos, ponderaciones, años de experiencia del facilitador), **lee la plantilla correspondiente en `plantillas/`** — no los repitas aquí.
- En caso de duda entre subtipos cercanos (¿curso o diplomado? ¿taller o capacitación?), **pregunta al usuario**: las diferencias tienen implicaciones reales (mínimo de módulos, perfil de ingreso, código).
- Si el PDF oficial cambia, actualizar primero la plantilla `.md` correspondiente y registrar en `aprendizajes.md`.
- Antes de cualquiera de estas preguntas de subtipo, confirma primero el **servicio** (§0) — el subtipo de categoría curricular solo existe dentro de Habilidades.
