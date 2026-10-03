# Diseño — Capacitación RRHH con IA · APB Group (CAP-033)

**Fecha:** 2026-05-25
**Cliente:** APB Group · Área: Recursos Humanos
**División Intezia:** Educación
**Tipo de documento:** Capacitación in-company (sin perfil de ingreso)
**Código:** CAP-033 (siguiente libre tras CAP-032)
**Slug:** `apb-group`
**Origen:** reencuadre del catálogo TA-006 "Gestión del Talento y Cultura (RRHH)" hacia un programa 100% práctico, más corto y centrado en el ecosistema Google.
**Contexto comercial:** propuesta solicitada por RH de APB Group tras reunión. Douglas Vásquez estuvo presente en la reunión y **será el facilitador** de la capacitación. La propuesta es un **regalo / cortesía de Intezia**: el deck **no lleva slide de apartado económico** (ni campos de precio).

---

## 1. Objetivo del programa

Capacitar al equipo de Recursos Humanos de APB Group para que **construya sus propias Gemas de Gemini** y use el ecosistema Google (Gemini, NotebookLM) más Gamma/Canva para automatizar el ciclo de reclutamiento, onboarding y operaciones de RRHH. Formación **100% práctica**: cada actividad produce un activo reutilizable. **Se omiten** las sesiones de fundamentos y teoría.

## 2. Parámetros fijos

- **Duración:** 6 horas · 3 sesiones de 2 horas cada una.
- **Stack núcleo:** Gemini + Gemas, NotebookLM. Complementos: Gamma App / Canva (manuales visuales).
- **Modalidad:** a definir con el cliente (ventas la ajusta).
- **Enfoque:** elaboración práctica de Gemas y flujos; nada de fundamentos/teoría.
- **Facilitador:** Douglas Vásquez (nombrado en el deck, no genérico).
- **Sin precio:** es un regalo. El deck **omite la slide de Propuesta Económica** y sus 5 campos AcroForm de precio (mismo mecanismo que las propuestas de Fundación: el script omite el grupo solo).

## 3. Decisión de encuadre

Se **ignora** el pedido original de "reforzar módulos 2/3/6" del TA-006. La estructura definitiva son los **3 bloques** entregados por el cliente, mapeados 1:1 a las 3 sesiones. Lo que el comentario original pedía (análisis de CV, descripción de cargo, informe de métricas con % de ajuste, creativo de vacante) se integra dentro de estos bloques (ver §4).

## 4. Estructura curricular — 3 módulos / 3 sesiones

### Módulo I · Reclutamiento Inteligente (Sesión 1 · 2 h)
Cuatro actividades prácticas:

1. **Gema de Descripción de Cargo → Creativo de Vacante** *(integra el pedido original de "descripción de cargo" + "estructura del creativo para publicar vacantes")*: a partir de los requisitos del cargo, la Gema produce la descripción de cargo pulida y la estructura del aviso/creativo para publicar la vacante.
2. **Gema de Screening Semántico de CVs** *(integra "análisis de CV" + "informe con métricas y % de ajuste")*: anonimiza y procesa lotes de currículums, los compara objetivamente contra los requisitos del cargo y genera un ranking por competencias (no por sesgos inconscientes), con porcentaje de ajuste por candidato.
3. **Gema Generadora de Entrevistas Estructuradas**: guiones de entrevista personalizados por candidato, con preguntas situacionales para detectar soft skills específicas o validar lagunas del CV.
4. **Roleplay de Entrevista**: la IA actúa como el candidato en una entrevista difícil; los reclutadores junior practican técnicas de indagación.

Herramientas: Gemini + Gemas; NotebookLM como fuente de CVs anonimizados.

### Módulo II · Onboarding y Experiencia (Sesión 2 · 2 h)
Tres actividades prácticas:

1. **Kit de Bienvenida Automatizado**: flujo de onboarding completo (correo de bienvenida, agenda de la primera semana, lista de tareas) generado en segundos.
2. **Manuales Visuales (Gamma App / Canva)**: transforma documentos de texto (políticas, manuales de usuario) en presentaciones visuales interactivas y amigables.
3. **Buddy System Digital**: guías rápidas para los mentores internos, para que sepan exactamente cómo acompañar al nuevo ingreso.

Herramientas: Gemini, NotebookLM (hub de conocimiento del nuevo ingreso), Gamma, Canva.

### Módulo III · Operaciones de RRHH (Sesión 3 · 2 h)
Dos actividades prácticas:

1. **Diseño de Chatbot de Servicio (concepto)**: estructuración lógica de un asistente virtual que responde preguntas frecuentes ("¿cuántos días de vacaciones me tocan?", "¿cómo accedo al seguro médico?").
2. **Automatización de Tareas Repetitivas**: uso de IA para redactar cartas patronales, constancias de trabajo o correos de cumpleaños masivos pero personalizados.

Herramientas: Gemini + Gemas.

## 5. Entregables insignia (lo que se llevan)

- Gema de Descripción de Cargo + Creativo de Vacante.
- Gema de Screening Semántico de CVs (con ranking por % de ajuste).
- Gema Generadora de Entrevistas Estructuradas.
- Kit de Bienvenida automatizado + manual visual en Gamma/Canva.
- Guía de Buddy System.
- Estructura/Gema de Chatbot de servicio al empleado.
- Plantillas de automatización (cartas patronales, constancias, cumpleaños).
- (3 entregables institucionales estándar añadidos al campo AcroForm `Entregables`.)

## 6. Estructura del deck (clon de cumbre-andina, mono-fase)

Clonar `clientes/propuestas/cumbre-andina/` (enlaza `../_base/styles.css`). El canónico trae **13 slides** con cronograma en **una slide por sesión** (ideal para nuestras 3 sesiones) + slide de Impacto. Al **eliminar la slide de Propuesta Económica** quedan **12 slides** (renumerar contadores a `0X / 12`):

1. `01/12` Portada — APB Group · Recursos Humanos · código CAP-033.
2. `02/12` Punto de dolor + Diagnóstico — adaptado a RRHH de APB (carga operativa).
3. `03/12` Objetivos — general + 3 específicos (uno por sesión).
4. `04/12` Programa — 3 módulos con sus actividades (chips ≤28 chars).
5. `05/12` Cronograma · Sesión 1 — Reclutamiento Inteligente (ruta 1/3, 33%).
6. `06/12` Cronograma · Sesión 2 — Onboarding y Experiencia (ruta 2/3, 66%).
7. `07/12` Cronograma · Sesión 3 — Operaciones de RRHH (ruta 3/3, 100%).
8. `08/12` Metodología ABR (fija).
9. `09/12` Beneficios + Entregables + Acreditación + **facilitador Douglas Vásquez**.
10. `10/12` Impacto — datos reales de IA en RRHH/reclutamiento con fuente verbatim (§4.9).
11. ~~Propuesta Económica~~ → **eliminada** (regalo); el script omite sus 5 campos solo.
12. `11/12` Próximos pasos — logística del arranque (sin acuerdos económicos, §4.15).
13. `12/12` Cierre — CTA Calendly.

Los eyebrows numerados (`02 · Objetivos` … `08 · Próximos pasos`) **no cambian** al quitar la slide de precio (no tiene eyebrow numerado).

## 7. Campos AcroForm a pre-llenar (§4.14)

Sin slide de precio, aplican **8 campos** (los 5 de precio no existen):

- `Entregables`: 2–4 destacados de §5 + 3 institucionales.
- `Acreditacion`: 3 líneas fijas con `[CÓDIGO]` → `CAP-033`.
- `Paso01–03 Titulo` y `Paso01–03 Body`: logística (≤130 chars body), sin términos económicos.
- Campos de precio (base, descuento, total, Programa, Notas): **no aplican** — la slide se elimina.

**Facilitador en slide 7:** Douglas Vásquez como facilitador nombrado. Si el cliente aporta cargo/bio, se afina; por defecto, rol corto "Facilitador · IA aplicada a RRHH".

## 8. Reglas del sistema que aplican (CLAUDE.md)

- §4.1 marca visual (logos Educación, paleta, tipografía).
- §4.8 negrita en palabras clave del cuerpo.
- §4.9 datos de impacto solo de estudios reales con fuente verbatim (slide Impacto si el clon la incluye; adaptar al eje RRHH/IA).
- §4.10 sin overflow (verificar con `verificar-overflow.js`); Sesión 1 tiene 4 actividades → vigilar la card del Módulo I.
- §4.11 no afirmar que APB migra de stack; Google se presenta como su entorno / como opción.
- §4.12 glosar acrónimos (Gema, NotebookLM, soft skills) en su primer uso por slide.
- §4.13 sin guion largo/mediano como separador en copy de cara al cliente.
- §4.15 "Cómo arrancamos" = logística, nunca acuerdo/factura/anticipo.

## 9. Fuera de alcance

- Módulos de L&D (Formación y Desarrollo) y Clima/Comunicación del TA-006 original: **no entran**.
- Sesiones de fundamentos/teoría: **no entran**.
- Slide de Propuesta Económica y cualquier cifra: **no entra** (es un regalo).

## 10. Flujo de implementación

1. `cp -r clientes/propuestas/cumbre-andina/ clientes/propuestas/apb-group/` y limpiar artefactos (PDF, calendario).
2. Crear `brief.md` y `programa.md` (con §5.2 desglose instructivo, fuente de los Entregables).
3. Editar `index.html`: portada, diagnóstico, objetivos, programa (3 módulos), cronograma (3 sesiones), beneficios, cierre.
4. `./scripts/generar-pdf.sh apb-group` → `python3 scripts/customize-apb-group.py` (par obligatorio).
5. `./scripts/verificar-propuesta.sh apb-group` y revisión visual slide por slide.
