# Capacitación RRHH con IA · APB Group (CAP-033) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir la propuesta-deck de APB Group (Capacitación RRHH con IA sobre ecosistema Google), 6 h / 3 sesiones, clonando el canónico cumbre-andina, sin slide de precio (es un regalo) y con Douglas Vásquez como facilitador.

**Architecture:** Clonar `cumbre-andina/` (13 slides, cronograma 1-slide-por-sesión + Impacto, enlaza `../_base/styles.css`). Editar el contenido estático de cada slide, eliminar la slide de Propuesta Económica (el script de AcroForms omite sus campos solos al no hallar el marker "Propuesta Económica"), renumerar contadores a `/12`. Crear `brief.md`, `programa.md` y `customize-apb-group.py`. Generar PDF con el par `generar-pdf.sh` → `customize-apb-group.py`. Verificar con `verificar-propuesta.sh` + revisión visual.

**Tech Stack:** HTML/CSS estático (deck A4 landscape), Chrome headless (PDF), pypdf (AcroForms), bash + python scripts del repo.

**Spec:** `docs/superpowers/specs/2026-05-25-apb-group-rrhh-ia-google-design.md`

---

## File Structure

- Create: `clientes/propuestas/apb-group/brief.md` — datos administrativos, contacto, necesidad, contexto, equipo.
- Create: `clientes/propuestas/apb-group/programa.md` — diseño curricular (§5.1 modular + §5.2 desglose, fuente de los Entregables).
- Create/Clone: `clientes/propuestas/apb-group/index.html` — deck de 12 slides (clon editado).
- Inherited: `clientes/propuestas/apb-group/` enlaza `../_base/styles.css` (no se copia CSS).
- Create: `scripts/customize-apb-group.py` — pre-llena Entregables, Acreditacion (CAP-033) y 3 pasos (logística, sin términos económicos §4.15).
- Generated: `clientes/propuestas/apb-group/CAP-033 <Título>.pdf`.

---

## Task 1: Clonar el canónico y limpiar artefactos

**Files:**
- Create dir: `clientes/propuestas/apb-group/` (desde `cumbre-andina/`)

- [ ] **Step 1: Clonar**

```bash
cd /Users/isaacgabrielrodriguezalvarez/Downloads/IsaIA
cp -r clientes/propuestas/cumbre-andina/ clientes/propuestas/apb-group/
```

- [ ] **Step 2: Borrar artefactos del clon (PDF demo, calendario, programa/brief demo que reescribimos)**

```bash
cd /Users/isaacgabrielrodriguezalvarez/Downloads/IsaIA/clientes/propuestas/apb-group
rm -f propuesta.pdf calendario.md
```

- [ ] **Step 3: Verificar estado**

Run: `ls clientes/propuestas/apb-group/`
Expected: `brief.md  index.html  programa.md` (sin PDF ni calendario.md)

---

## Task 2: Escribir `brief.md`

**Files:**
- Modify: `clientes/propuestas/apb-group/brief.md` (sobrescribir el de cumbre-andina)

- [ ] **Step 1: Sobrescribir con el brief de APB Group**

Contenido completo (Write):

```markdown
# Brief — APB Group · Recursos Humanos

## Datos administrativos

- **Empresa**: APB Group
- **Slug**: `apb-group`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación in-company (`CAP-033`)
- **Programa**: Recursos Humanos potenciado con IA (ecosistema Google)
- **Eje temático**: IA aplicada al ciclo de RRHH (reclutamiento, onboarding, operaciones) con Gemini, Gemas y NotebookLM
- **Audiencia objetivo**: equipo de Recursos Humanos de APB Group
- **Fecha del brief**: 2026-05-25
- **Estado**: propuesta en elaboración

## Contacto

- **Persona contacto**: (a completar por ventas)
- **Cargo**: Recursos Humanos · APB Group

## Necesidad detectada

RRHH de APB Group solicitó una formación 100% práctica, sin fundamentos ni teoría, centrada en construir Gemas de Gemini y flujos sobre el ecosistema Google para automatizar reclutamiento, onboarding y operaciones del área.

## Contexto

- Reencuadre del producto de catálogo TA-006 "Gestión del Talento y Cultura (RRHH)" hacia 6 horas prácticas.
- Douglas Vásquez estuvo en la reunión y será el facilitador.
- Propuesta entregada como regalo / cortesía: el deck no lleva apartado económico.

## Especificaciones del programa

- **Duración**: 6 horas · 3 sesiones de 2 horas.
- **Modalidad**: a definir con el cliente (presencial / online síncrono / híbrido).
- **Stack**: Gemini + Gemas, NotebookLM, Gamma App / Canva (manuales visuales).
- **Enfoque**: elaboración práctica; se omiten fundamentos y teoría.

## Equipo asignado

- **Facilitador**: Douglas Vásquez.
- **Coordinación**: Equipo INTEZIA Education (punto de contacto durante el programa y los 30 días posteriores).

## Decisiones de propuesta

- **Sin slide de Propuesta Económica** (regalo): el script omite el grupo de precio solo.
- **Facilitador nombrado** en el deck: Douglas Vásquez.
- Módulos de L&D y Clima del TA-006 original quedan fuera de alcance.
```

- [ ] **Step 2: Verificar**

Run: `head -12 clientes/propuestas/apb-group/brief.md`
Expected: encabezado "Brief — APB Group · Recursos Humanos" y slug `apb-group`.

---

## Task 3: Escribir `programa.md` (incluye §5.2 desglose — fuente de Entregables)

**Files:**
- Modify: `clientes/propuestas/apb-group/programa.md` (sobrescribir)

- [ ] **Step 1: Sobrescribir** con el diseño curricular. Secciones obligatorias: 1 info general · 4 objetivos · 5.1 estructura modular (3 módulos) · 5.2 desglose instructivo (3 sesiones × 2 h) · 6 entregables/beneficio · 7 perfil del facilitador.

Estructura modular (§5.1) y desglose (§5.2) deben reflejar exactamente:

- **Módulo I · Reclutamiento Inteligente (Sesión 1, 2 h)** — elaboración del participante: construye 4 Gemas (Descripción de Cargo + Creativo de Vacante; Screening Semántico de CVs con ranking por % de ajuste; Generadora de Entrevistas Estructuradas; Roleplay de Entrevista con la IA como candidato).
- **Módulo II · Onboarding y Experiencia (Sesión 2, 2 h)** — Kit de Bienvenida automatizado (correo, agenda 1ª semana, lista de tareas); Manuales Visuales con Gamma/Canva; hub de conocimiento del nuevo ingreso en NotebookLM; Buddy System digital (guías para mentores).
- **Módulo III · Operaciones de RRHH (Sesión 3, 2 h)** — diseño de la lógica de un Chatbot de Servicio al empleado (FAQs: vacaciones, seguro médico); automatización de redacción de cartas patronales, constancias de trabajo y correos de cumpleaños masivos personalizados.

§6 — Entregables insignia (fuente del campo AcroForm `Entregables`):
Gema de Descripción de Cargo + Creativo de Vacante · Gema de Screening de CVs con % de ajuste · Gema de Entrevistas Estructuradas · Kit de Bienvenida + manual visual · Guía de Buddy System · Estructura de Chatbot de servicio · Plantillas de automatización (cartas, constancias, cumpleaños).

§7 — Facilitador: Douglas Vásquez (IA aplicada a RRHH).

- [ ] **Step 2: Verificar** que §5.2 tiene 3 filas (una por sesión) y que §6 lista los entregables.

Run: `grep -n "Sesión 1\|Sesión 2\|Sesión 3\|Entregable" clientes/propuestas/apb-group/programa.md`
Expected: 3 sesiones + bloque de entregables presentes.

---

## Task 4: Editar `index.html` (12 slides)

**Files:**
- Modify: `clientes/propuestas/apb-group/index.html`

Editar con `Edit` (old_string/new_string precisos sobre el clon). El comentario de cabecera y el `<title>` se actualizan a APB Group. **Quitar `<div class="demo-banner">Demo</div>`.**

- [ ] **Step 1: Portada (s-cover)** — counter `01 / 12`; eyebrow `Propuesta formativa · Recursos Humanos`; h1 `Recursos Humanos<br>potenciado con <span class="hl">IA de Google</span>`; lead: taller de 6 horas, 100% práctico, para que RRHH construya sus propias **Gemas** (asistentes personalizados de **Gemini**) y use **NotebookLM** en reclutamiento, onboarding y operaciones. id-line: `Código: CAP-033` · `APB Group`. (Glosar Gema y NotebookLM, §4.12. Sin guion largo, §4.13.)

- [ ] **Step 2: Diagnóstico (s-pain)** — counter `02 / 12`; meta foot `APB Group · Propuesta`. h2: el equipo de RRHH de APB Group invierte más horas en tareas repetitivas que con las personas; la IA invierte esa proporción. Lista de 5 puntos de longitud pareja (§4.10):
  1. El filtrado manual de CVs consume horas y arrastra sesgos inconscientes.
  2. Las entrevistas se improvisan sin un guion estructurado por candidato.
  3. El onboarding es inconsistente y depende de quién recibe al nuevo ingreso.
  4. Las políticas y manuales viven en documentos densos que casi nadie lee.
  5. Cartas, constancias y respuestas frecuentes se redactan una por una.

- [ ] **Step 3: Objetivos (s-goals)** — counter `03 / 12`. General: capacitar a RRHH de APB Group para construir y usar Gemas de Gemini en el ecosistema Google y automatizar reclutamiento, onboarding y operaciones, con práctica aplicada a sus propios casos. Específicos (3, uno por sesión):
  1. Construir Gemas para describir cargos, publicar vacantes y filtrar CVs por ajuste con ranking.
  2. Diseñar un onboarding completo: kit de bienvenida, manuales visuales y guía de buddy system.
  3. Estructurar un chatbot de servicio al empleado y automatizar documentos repetitivos.

- [ ] **Step 4: Programa (s-program)** — counter `04 / 12`; h2 `3 módulos · 6 horas.`; meta `Reclutamiento, onboarding y operaciones de RRHH, todo práctico sobre el ecosistema Google.` Tres módulos (chips ≤28 chars, §4.10):
  - **I · Reclutamiento Inteligente** — obj: construye Gemas que describen cargos, publican vacantes, filtran CVs por ajuste y preparan entrevistas. topics: `1.1 Gema de descripción de cargo` · `1.2 Creativo de vacante` · `1.3 Screening semántico de CVs` · `1.4 Ranking por % de ajuste` · `1.5 Gema de entrevistas` · `1.6 Roleplay con IA`.
  - **II · Onboarding y Experiencia** — obj: diseña un onboarding consistente con kit, manuales visuales y mentores. topics: `2.1 Kit de bienvenida` · `2.2 Agenda primera semana` · `2.3 Manuales visuales` · `2.4 Hub en NotebookLM` · `2.5 Buddy System digital`.
  - **III · Operaciones de RRHH** — obj: estructura un chatbot de servicio y automatiza documentos repetitivos. topics: `3.1 Lógica del chatbot` · `3.2 FAQs del empleado` · `3.3 Cartas y constancias` · `3.4 Correos personalizados` · `3.5 Plantillas reutilizables`.

- [ ] **Step 5: Cronograma Sesión 1 (primera s-schedule)** — counter `05 / 12`; ruta node `1`, fill `33.33%`, `Sesión 1 de 3`; ses-mod `Módulo I · Práctico`; h2 `Sesión 1: Reclutamiento Inteligente`; ses-dur `2 h`.
  - chips Temas: `Gema de cargo y vacante` · `Screening semántico de CVs` · `Informe con % de ajuste` · `Entrevistas y roleplay con IA`.
  - timebar (Total 2 h): `30' Gema de cargo y vacante` · `40' Screening y % de ajuste` · `35' Entrevistas y roleplay` · `15' Cierre`.
  - enseñanza: demostración en vivo de construcción de Gemas · screening de CVs anonimizados · modelado del roleplay.
  - aprendizaje: cada participante construye sus Gemas · corre un screening sobre lote anonimizado · practica el roleplay.
  - recursos: Gemini y Gemas · NotebookLM (CVs como fuente) · lote de CVs anonimizados · descripción de cargo real · workbook.

- [ ] **Step 6: Cronograma Sesión 2 (segunda s-schedule)** — counter `06 / 12`; ruta node `2`, fill `66.66%`, `Sesión 2 de 3`; ses-mod `Módulo II · Práctico`; h2 `Sesión 2: Onboarding y Experiencia`; ses-dur `2 h`.
  - chips: `Kit de bienvenida` · `Manuales visuales (Gamma/Canva)` · `Hub en NotebookLM` · `Buddy System digital`.
  - timebar (Total 2 h): `35' Kit de bienvenida` · `40' Manuales visuales` · `30' Buddy y NotebookLM` · `15' Cierre`.
  - enseñanza: demo de kit de bienvenida en segundos · transformación de un manual a visual · armado del hub en NotebookLM.
  - aprendizaje: construye un kit de onboarding completo · convierte una política real en manual visual · crea una guía de buddy.
  - recursos: Gemini · NotebookLM · Gamma App / Canva · políticas y manuales reales · plantillas de onboarding.

- [ ] **Step 7: Cronograma Sesión 3 (tercera s-schedule)** — counter `07 / 12`; ruta node `3`, fill `100%`, `Sesión 3 de 3`; ses-mod `Módulo III · Práctico`; h2 `Sesión 3: Operaciones de RRHH`; ses-dur `2 h`.
  - chips: `Lógica del chatbot de servicio` · `FAQs del empleado` · `Cartas y constancias` · `Correos masivos personalizados`.
  - timebar (Total 2 h): `50' Diseño del chatbot` · `50' Automatización de documentos` · `20' Cierre y plan`.
  - enseñanza: estructuración del chatbot paso a paso · demo de cartas patronales y constancias · correos masivos personalizados.
  - aprendizaje: diseña la estructura de su chatbot · genera una carta patronal y una constancia · arma un envío de cumpleaños personalizado.
  - recursos: Gemini y Gemas · plantillas de cartas y constancias · base de FAQs de RRHH · datos demo.

- [ ] **Step 8: Metodología ABR (s-orange)** — counter `08 / 12`. Texto fijo; en pilar 02 ajustar el ejemplo a RRHH: "cada actividad entrega un activo reutilizable (una Gema de screening, un kit de onboarding, un chatbot de servicio)".

- [ ] **Step 9: Beneficios (s-benefits)** — counter `09 / 12`. Perfil de egreso:
  - Saber: conoce dónde la IA aporta valor en el ciclo de RRHH y sus límites.
  - Saber hacer: construye Gemas de Gemini y flujos para reclutamiento, onboarding y operaciones.
  - Saber ser: usa la IA con criterio, mitiga sesgos y cuida los datos del candidato y del empleado.

  Beneficio: el equipo de RRHH se lleva un set de Gemas y plantillas listo para usar y recupera horas operativas para enfocarse en las personas. **Mantener vacías** las cajas `multi-box entregables-box` y `acreditaciones-box` (las llena el AcroForm). **Equipo facilitador** = reemplazar las 2 personas demo por:
  - Douglas Vásquez · avatar `DV` · rol `Facilitador · IA aplicada a RRHH` · bio: experiencia formando equipos de RRHH en IA aplicada al talento.
  - Equipo INTEZIA Education · avatar `IE` · rol `Coordinación` · bio: punto único de contacto durante el programa y los 30 días posteriores.

- [ ] **Step 10: Impacto (s-impact)** — counter `10 / 12`. **§4.9 bloqueante**: reescribir barras/gauge/chips/hook con datos reales de IA en RRHH/reclutamiento, citando la fuente verbatim. Ejecutar WebSearch (p. ej. "AI recruiting productivity statistics 2025/2026", "AI in HR adoption survey SHRM / McKinsey State of AI / LinkedIn Future of Recruiting / Stanford HAI AI Index"). Tomar 3 métricas verificables para las barras, una para el gauge y citarlas en `panel-source` tal cual. **No inventar ninguna cifra**; si no hay fuente sólida para una métrica, omitirla.

- [ ] **Step 11: Eliminar la slide de Propuesta Económica (s-price)** — borrar el `<section class="slide s-price">…</section>` completo (líneas del bloque `11 · Propuesta Económica` del clon). Al desaparecer el texto "Propuesta Económica", `agregar-campo-precio.py` omite los 5 campos de precio solo.

- [ ] **Step 12: Próximos pasos (s-steps)** — counter `11 / 12`. Reescribir los 3 `acro-default-text` (logística, §4.15 sin acuerdo/factura/anticipo):
  - Paso01 título `Confirmamos fechas` · body `Validamos las fechas de las 3 sesiones de 2 horas y la zona horaria si es online.`
  - Paso02 título `Acceso y logística` · body `Coordinamos el acceso de los participantes, la agenda de las sesiones y el entorno presencial u online.`
  - Paso03 título `Reunión de arranque` · body `Kickoff de unos 30 minutos para alinear los casos reales de RRHH que entrarán a la práctica.`

- [ ] **Step 13: Cierre (s-end)** — counter `12 / 12`. end-message: `De la carga operativa<br>a la <span class="hl-orange">arquitectura</span> <span class="hl-yellow">humana</span>.` Mantener el CTA Calendly (`<a class="cta" href="https://calendly.com/intezia/30min?month=2026-05" …>`). Mantener líneas de contacto institucionales (asesora de ventas + empresa) tal cual del canónico.

- [ ] **Step 14: Sustituir todos los `meta` de foot** restantes de `Cumbre Andina · Propuesta` → `APB Group · Propuesta` (usar Edit replace_all). Mantener `Intezia · Modelo ABR` en la slide ABR.

- [ ] **Step 15: Verificar contadores y limpieza**

Run:
```bash
cd /Users/isaacgabrielrodriguezalvarez/Downloads/IsaIA
grep -c "/ 12<" clientes/propuestas/apb-group/index.html
grep -ci "cumbre\|demo-banner\|s-price\|Propuesta Económica" clientes/propuestas/apb-group/index.html
```
Expected: 12 contadores `/ 12`; 0 referencias a cumbre/demo/precio.

---

## Task 5: Crear `scripts/customize-apb-group.py`

**Files:**
- Create: `scripts/customize-apb-group.py`

- [ ] **Step 1: Crear el script** (copiar el patrón de `customize-cashea-cap006.py`; cambiar el nombre, los Entregables, el código a CAP-033 y los pasos a logística §4.15). Contenido:

```python
#!/usr/bin/env python3
"""
Customizador de AcroForms para la propuesta APB Group (CAP-033).
Pre-llena Entregables, Acreditacion y los 6 campos de Próximos pasos.
Sin campos de precio: la slide de Propuesta Económica no existe (regalo).
Los campos quedan EDITABLES (solo se reescribe /V y /DV).

Uso:
    python customize-apb-group.py <pdf>
"""
import sys
from pathlib import Path

from acroform_appearance import rebake_bold_fields
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Uso: customize-apb-group.py <pdf>")

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        sys.exit(f"ERROR: no existe {pdf_path}")

    updates = {
        "Entregables": "\r".join([
            "Gema de descripción de cargo y vacante",
            "Gema de screening de CVs con % de ajuste",
            "Gema de entrevistas estructuradas",
            "Kit de bienvenida y manual visual",
            "Estructura de chatbot de servicio",
            "Plantillas de cartas y constancias",
            "Certificado de asistencia INTEZIA",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-033.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmamos fechas",
        "Paso01Body": (
            "Validamos las fechas de las 3 sesiones de 2 horas y la "
            "zona horaria si es online."
        ),
        "Paso02Titulo": "Acceso y logística",
        "Paso02Body": (
            "Coordinamos el acceso de los participantes, la agenda de las "
            "sesiones y el entorno presencial u online."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kickoff de unos 30 minutos para alinear los casos reales de "
            "RRHH que entrarán a la práctica."
        ),
    }

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    for name, value in updates.items():
        for page in writer.pages:
            if "/Annots" not in page:
                continue
            for annot_ref in page["/Annots"]:
                obj = annot_ref.get_object()
                if obj.get("/T") == name:
                    obj[NameObject("/V")] = TextStringObject(value)
                    obj[NameObject("/DV")] = TextStringObject(value)

    catalog = writer._root_object
    if NameObject("/AcroForm") in catalog:
        acro = catalog[NameObject("/AcroForm")]
        acro[NameObject("/NeedAppearances")] = BooleanObject(True)

    rebake_bold_fields(writer)

    with open(pdf_path, "wb") as f:
        writer.write(f)

    print(f"APB Group CAP-033 · Entregables + Acreditación + Próximos pasos customizados en {pdf_path.name}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verificar Entregables ≤ ~8-9 líneas cortas (memoria `project_entregables_lineas_cortas`) y bodies de paso ≤130 chars (`project_pasos_body_max_chars`).** Los del script cumplen (7 líneas, bodies < 130). Confirmar con lectura.

---

## Task 6: Generar PDF, customizar y verificar (par obligatorio + checklist §10)

**Files:**
- Generated: `clientes/propuestas/apb-group/CAP-033 *.pdf`

- [ ] **Step 1: Generar el PDF base + AcroForms**

```bash
cd /Users/isaacgabrielrodriguezalvarez/Downloads/IsaIA
./scripts/generar-pdf.sh apb-group
```
Expected: imprime `✓ Listo: …/CAP-033 ….pdf` y sugiere el customize con el path exacto.

- [ ] **Step 2: Customizar (inmediatamente después, §10 par PDF-customize)**

```bash
python3 scripts/customize-apb-group.py "$(ls clientes/propuestas/apb-group/CAP-033*.pdf)"
```
Expected: `APB Group CAP-033 · Entregables + Acreditación + Próximos pasos customizados…`

- [ ] **Step 3: Verificación automática (§10 paso 1)**

```bash
./scripts/verificar-propuesta.sh apb-group
```
Expected: sin hallazgos de guion largo, comillas tipográficas, `[CÓDIGO]` sin sustituir, términos económicos en "Cómo arrancamos" ni desborde (verificar-overflow.js). Si reporta overflow (riesgo: Programa con 5-6 topics, o cronograma con 4 chips), ajustar contenido (acortar), no diseño (§4.10).

- [ ] **Step 4: Revisión visual manual (§10 paso 2)** — abrir el PDF y revisar slide por slide: logos Educación correctos, sin solapes, contadores `01/12 … 12/12`, NO aparece slide de precio, Entregables/Acreditación/Pasos llenos en el PDF, Douglas Vásquez como facilitador, Impacto con fuente verbatim, ningún claim de que APB migra/ya adoptó la herramienta (§4.11), acrónimos glosados (§4.12).

```bash
open "$(ls clientes/propuestas/apb-group/CAP-033*.pdf)"
```

- [ ] **Step 5: Registrar aprendizaje** — anteponer entrada con fecha 2026-05-25 en `aprendizajes.md` (CAP-033 APB Group: clon de cumbre sin slide de precio por ser regalo + facilitador nombrado Douglas Vásquez). Si hubo algo no escrito que se repita, codificarlo donde corresponda (§9).

---

## Self-Review

- **Spec coverage:** Sesión 1/2/3 (spec §4) → Tasks 4 steps 5-7 + programa.md §5.2 (Task 3). Creativo de vacante (spec §4, decisión del usuario) → topic 1.2 + chip Sesión 1. Sin precio (spec §2/§6) → Task 4 step 11 + script sin price fields. Douglas facilitador (spec §2) → Task 4 step 9 + brief + programa §7. Entregables/Acreditación/Pasos (spec §7) → Task 5. Impacto datos reales (spec §8, §4.9) → Task 4 step 10. Marca/overflow/acrónimos/§4.13/§4.15 (spec §8) → Task 6 steps 3-4.
- **Placeholder scan:** el único punto sin texto literal es la slide de Impacto (step 10), por diseño: §4.9 prohíbe inventar cifras, así que la data se obtiene por WebSearch y se cita verbatim en ejecución. No es un placeholder de redacción sino una acción definida.
- **Type/marker consistency:** nombres de campo AcroForm (`Entregables`, `Acreditacion`, `Paso0NTitulo/Body`) coinciden con `agregar-campo-precio.py`. Marker "Cómo arrancamos" y "Lo que se llevan"+"Entregables" presentes en el clon → los grupos se añaden; "Propuesta Económica" ausente → grupo de precio omitido.
```
