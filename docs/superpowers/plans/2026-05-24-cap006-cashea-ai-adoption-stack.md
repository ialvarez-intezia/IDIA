# CAP-006 Cashea · Reconversión a AI Adoption Stack — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconvertir el deck CAP-006 de un curso Claude para power users a la propuesta del *Cashea AI Adoption Stack* (3 tiers escalables, Claude-céntrico, sin montos) que responde al ask real de Cashea: escalable + persistente para nuevos ingresos, 1.000 colaboradores + 50 directivos.

**Architecture:** Edición del deck HTML existente (`index.html`) slide por slide, reaprovechando clases CSS probadas (`.modules`/`.module`, `s-roadmap`, `s-impact`) para minimizar CSS nuevo y riesgo de overflow. Reescritura de `brief.md` y `programa.md`. Actualización del pre-llenado de AcroForms (`customize-cashea-cap006.py`). Verificación con `verificar-propuesta.sh` + `verificar-overflow.js` + revisión visual del PDF.

**Tech Stack:** HTML/CSS estático · Python (pypdf) para AcroForms · scripts bash del repo (`generar-pdf.sh`, `verificar-propuesta.sh`).

**Slug:** `clientes/propuestas/cashea/CAP-006 Claude Power - Skills MCP y Workflows`
(las rutas abajo usan `<SLUG>/` por brevedad; sustituir por la ruta completa entre comillas).

---

## Estructura objetivo (11 slides, antes 16)

| # nuevo | Clase | Antes | Acción |
|---|---|---|---|
| 01 | `s-cover` | Portada Claude Power | Reescribir copy |
| 02 | `s-pain` | Diagnóstico power user | Reescribir a dolores Cashea |
| 03 | `s-goals` | Objetivos power user | Reescribir |
| 04 | `s-program` | Programa Parte 1 (3 módulos) | Reconvertir a 4 Componentes del Stack |
| 05 | `s-roadmap` (NUEVO) | — (reemplaza Parte 2 + 5 sesiones) | Arquitectura de 3 tiers, Tier 2 recomendado |
| 06 | `s-orange` | Metodología | Reescribir copy |
| 07 | `s-benefits` | Beneficios | Reescribir copy |
| 08 | `s-impact` | Impacto (técnico) | Reescribir a McKinsey 2025 |
| 09 | `s-price` | Propuesta Económica | Mantener AcroForm vacío; ajustar duración |
| 10 | `s-steps` | Próximos pasos | Reescribir bodies |
| 11 | `s-end` | Cierre | Reescribir mensaje |

Se **eliminan**: la 2ª slide `s-program` (Parte 2 · Advanced WOW) y las 5 slides `s-schedule` (Sesión 1-5). Los contadores pasan de `NN / 16` a `NN / 11`.

**Reglas críticas a respetar en todo el copy:** sin guion largo/mediano (§4.13, usar coma/paréntesis/dos puntos/punto/·) · glosar acrónimos en primer uso por slide (§4.12) · Claude como stack recomendado, nunca afirmar que Cashea ya migró/adoptó (§4.11) · **MaratonIA** escrito así y descrito en su primer uso como «la plataforma educativa en línea de Intezia» · `<strong>` solo en cuerpo, 2-3 por slide, no en `<li>` con `display:flex` (memoria [[project_spain_no_strong]]).

---

## Task 1: Portada (s-cover)

**Files:**
- Modify: `<SLUG>/index.html` (comentario de cabecera líneas 2-16; slide cover líneas 29-49)

- [ ] **Step 1: Reemplazar el comentario de cabecera HTML**

Reemplazar el bloque `<!-- ... -->` (líneas 2-16) por:

```html
<!--
  Propuesta · Cashea (CAP-006)
  Programa: Cashea AI Adoption Stack · Adopción de IA a escala con Claude
  División: Educación · Tipo: Capacitación in-company (stack multi-tier)
  Audiencia: 1.000 colaboradores + 50 directivos · cobertura de nuevos ingresos
  Modalidad: Presencial u Online (un solo deck cubre ambas)
  Stack: Claude-céntrico · MaratonIA (plataforma educativa en línea de Intezia)
  Estructura: 3 tiers escalables (Fundamentals / Ecosystem / Enterprise) · Tier 2 recomendado
  Sin montos en el deck (precio = AcroForm para ventas).

  Paths de imagen: 4 niveles arriba (../../../../logos/)
  v4 (2026-05-24): reconversión a AI Adoption Stack. Total: 11 slides.
-->
```

- [ ] **Step 2: Reemplazar el `<title>` (línea 21)**

```html
  <title>Propuesta · Cashea · CAP-006 · AI Adoption Stack · Intezia Educación</title>
```

- [ ] **Step 3: Reemplazar el contenido de la portada (líneas 30-48)**

```html
      <span class="counter">01 / 11</span>
      <div class="logo-big">
        <img src="../../../../logos/educacion/BLANCO.png" alt="Intezia Educación">
      </div>
      <div class="body">
        <p class="eyebrow">Propuesta · Adopción de IA a escala · Presencial u Online</p>
        <h1>
          AI Adoption<br>
          <span class="hl">Stack</span><br>
          Cashea
        </h1>
        <p class="lead">
          Un sistema, no un taller. Nivelamos a los <strong>1.000 colaboradores</strong> y a los 50 directivos de Cashea en un piso común de IA con Claude, y dejamos una <strong>plataforma persistente</strong> que onboarda a cada nuevo ingreso de forma automática.
        </p>
      </div>
      <div class="id-line">
        <span class="codigo">Código: CAP-006</span>
        <span class="cliente">Cashea</span>
      </div>
```

- [ ] **Step 4: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): portada AI Adoption Stack"
```

---

## Task 2: Diagnóstico (s-pain)

**Files:**
- Modify: `<SLUG>/index.html` (líneas 53-72, contenido del slide s-pain)

- [ ] **Step 1: Reemplazar contenido del slide (counter, h2, context, diagnóstico)**

```html
      <span class="counter">02 / 11</span>
      <span class="quote-mark">"</span>
      <div class="body">
        <h2>Capacitar una vez no escala. Cada nuevo ingreso vuelve a empezar de cero.</h2>
        <p class="context">
          Cashea repite dos palabras en cada conversación: necesita una adopción de IA <strong>escalable</strong> y <strong>persistente</strong>. Un taller puntual nivela a quien estuvo ese día, pero el equipo crece, la gente rota y el conocimiento se va con las personas. El reto no es dar una clase: es construir un sistema que sostenga la adopción en el tiempo.
        </p>
        <p class="diag-title">Diagnóstico</p>
        <ol>
          <li>La capacitación puntual no persiste: cada nuevo ingreso entra sin el piso común de IA que ya tiene el resto.</li>
          <li>Los 1.000 colaboradores están en niveles muy dispares y el conocimiento de IA vive en personas, no en un sistema consultable.</li>
          <li>Los 50 directivos necesitan liderar la adopción con criterio, no solo aprobarla desde afuera.</li>
          <li>Cashea pidió de forma explícita algo escalable y persistente, no un modelo tradicional por horas que no crece con la empresa.</li>
        </ol>
      </div>
```

Nota: la `<ol>` usa lista simple, no `display:flex`, así que `<strong>` inline es seguro; aun así se mantiene en el `context`, no en los `<li>` (memoria [[project_spain_no_strong]]).

- [ ] **Step 2: Verificar visualmente que el bloque no desborda** (4 items de longitud pareja, §4.10). Se confirma en Task 16 con el PDF.

- [ ] **Step 3: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): diagnóstico a dolores reales de Cashea"
```

---

## Task 3: Objetivos (s-goals)

**Files:**
- Modify: `<SLUG>/index.html` (líneas 77-101)

- [ ] **Step 1: Reemplazar contenido del slide**

```html
      <span class="counter">03 / 11</span>
      <p class="eyebrow">02 · Objetivos</p>
      <h2>A dónde llevamos<br>la adopción de IA en Cashea.</h2>
      <div class="columns">
        <div class="general">
          <p class="label">Objetivo general</p>
          <p>
            Instalar en Cashea un <strong>sistema de adopción de IA con Claude</strong> que nivela a los 1.000 colaboradores y a los 50 directivos en un piso común, y que se sostiene en el tiempo: cada nuevo ingreso se incorpora de forma automática a través de <strong>MaratonIA</strong>, la plataforma educativa en línea de Intezia. La meta no es un evento de capacitación: es una capacidad organizacional persistente.
          </p>
        </div>
        <div class="specifics">
          <p class="label">Objetivos específicos</p>
          <ol>
            <li>Nivelar a los 1.000 colaboradores en un piso común de IA con Claude, en cohortes escalables.</li>
            <li>Llevar a los 50 directivos a liderar la adopción con criterio, con un entregable de Mapa de Calor de oportunidades.</li>
            <li>Dejar un sistema persistente que onboarda a cada nuevo ingreso sin depender de un nuevo taller.</li>
            <li>Dar a Cashea visibilidad del avance con un panel ejecutivo del progreso de la adopción.</li>
            <li>Identificar y atacar las áreas críticas con una auditoría de procesos con IA cuando Cashea decida profundizar.</li>
          </ol>
        </div>
      </div>
```

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): objetivos del stack de adopción"
```

---

## Task 4: Componentes del Stack (s-program · 4 cards)

**Files:**
- Modify: `<SLUG>/index.html` (slide s-program "Parte 1", líneas 105-152)
- Modify: `<SLUG>/styles.css` (si el grid de 4 cards desborda; ver Step 3)

- [ ] **Step 1: Reemplazar el slide s-program (Parte 1) por los 4 componentes**

Reemplazar líneas 105-152 (todo el `<section class="slide s-program">` de la Parte 1) por:

```html
    <section class="slide s-program">
      <span class="counter">04 / 11</span>
      <p class="eyebrow">03 · Componentes del Stack</p>
      <h2>Cuatro piezas, un sistema.</h2>
      <p class="meta">Nivelación masiva, liderazgo directivo, plataforma persistente y auditoría. Se combinan en tiers escalables (slide siguiente).</p>
      <div class="modules">
        <div class="module">
          <span class="roman">01</span>
          <h3>Nivelación masiva con Claude</h3>
          <p class="obj">Llevamos a los 1.000 colaboradores a un piso común de IA con <strong>Claude</strong>. Cohortes de 250, 6 facilitadores en paralelo, 4 a 6 semanas. Certificación al cierre.</p>
          <ul class="topics">
            <li>Fundamentos de IA aplicada</li>
            <li>Cohortes de 250 personas</li>
            <li>Online síncrono o presencial</li>
            <li>Kit de prompts por rol</li>
          </ul>
        </div>
        <div class="module">
          <span class="roman">02</span>
          <h3>Masterclass ejecutiva · 50 directivos</h3>
          <p class="obj">Sprint para que los directivos lideren la adopción, no solo la aprueben. Entregable: un <strong>Mapa de Calor</strong> de oportunidades de IA por área.</p>
          <ul class="topics">
            <li>Visión y estrategia de IA</li>
            <li>Casos de uso por área</li>
            <li>Mapa de Calor de oportunidades</li>
            <li>Criterio de priorización</li>
          </ul>
        </div>
        <div class="module">
          <span class="roman">03</span>
          <h3>MaratonIA · plataforma persistente</h3>
          <p class="obj"><strong>MaratonIA</strong>, la plataforma educativa en línea de Intezia, con branding Cashea. Onboarda a cada nuevo ingreso de forma automática mediante un asistente de ruta de aprendizaje.</p>
          <ul class="topics">
            <li>Branding Cashea</li>
            <li>Asistente de ruta por rol</li>
            <li>Onboarding de nuevos ingresos</li>
            <li>Catálogo actualizable</li>
          </ul>
        </div>
        <div class="module">
          <span class="roman">04</span>
          <h3>Auditoría de procesos con IA</h3>
          <p class="obj">Bootcamp consultivo que identifica y ataca las áreas críticas. Entregables de diagnóstico, rediseño y resultados para escalar la adopción con datos.</p>
          <ul class="topics">
            <li>Diagnóstico por área</li>
            <li>Rediseño de procesos</li>
            <li>Talleres especializados</li>
            <li>Plan de acción medible</li>
          </ul>
        </div>
      </div>
      <div class="foot">
        <img src="../../../../logos/educacion/NEGRO.png" alt="">
        <span class="meta">Cashea · Propuesta · CAP-006</span>
      </div>
    </section>
```

- [ ] **Step 2: Eliminar la 2ª slide s-program (Parte 2 · Advanced WOW)**

Borrar por completo el `<section class="slide s-program">` que va del comentario `<!-- 5 · Programa · Parte 2 (Módulos IV-V) -->` hasta su `</section>` (líneas 154-190 del original).

- [ ] **Step 3: Verificar grid de 4 cards y aplicar modo compacto si desborda**

Confirmar en `styles.css` que existe la regla `:has(> .module:nth-child(4))` (modo compacto para 4 cards). Si no existe, añadir al final del archivo:

```css
/* s-program · modo compacto para 4 componentes */
.s-program .modules:has(> .module:nth-child(4)) { gap: 14px; }
.s-program .modules:has(> .module:nth-child(4)) .module { padding: 14px 16px; }
.s-program .modules:has(> .module:nth-child(4)) .module h3 { font-size: 15px; }
.s-program .modules:has(> .module:nth-child(4)) .topics li { font-size: 11px; }
```

(Verificar primero si ya existe una regla equivalente para no duplicar.)

- [ ] **Step 4: Commit**

```bash
git add "<SLUG>/index.html" "<SLUG>/styles.css"
git commit -m "feat(cap-006): componentes del stack (4 piezas) y elimina slide power-user"
```

---

## Task 5: Arquitectura de 3 tiers (s-roadmap NUEVO)

**Files:**
- Modify: `<SLUG>/index.html` (reemplaza las 5 slides s-schedule, líneas 192-570 del original)
- Modify: `<SLUG>/styles.css` (CSS del badge recomendado)

- [ ] **Step 1: Reemplazar las 5 slides s-schedule por una sola slide de tiers**

Borrar las 5 `<section class="slide s-schedule">` (comentarios 6-10, Sesión 1 a 5) y poner en su lugar:

```html
    <!-- 05 · Arquitectura de 3 tiers -->
    <section class="slide s-program s-tiers">
      <span class="counter">05 / 11</span>
      <p class="eyebrow">04 · Arquitectura escalable</p>
      <h2>Tres tiers. Empiezas donde estás, escalas cuando quieras.</h2>
      <p class="meta">Cada tier incluye todo lo anterior. Tier 2 es el recomendado: resuelve nivelación y persistencia a la vez.</p>
      <div class="modules">
        <div class="module tier">
          <span class="roman">T1</span>
          <h3>Fundamentals</h3>
          <p class="obj">Nivelación masiva de los 1.000 colaboradores con Claude más la masterclass ejecutiva para los 50 directivos.</p>
          <ul class="topics">
            <li>Nivelación masiva (cohortes)</li>
            <li>Masterclass directivos</li>
            <li>Certificación + kit de prompts</li>
            <li>Mapa de Calor ejecutivo</li>
          </ul>
        </div>
        <div class="module tier tier-rec">
          <span class="tier-badge">Recomendado</span>
          <span class="roman">T2</span>
          <h3>Ecosystem</h3>
          <p class="obj">Todo Fundamentals más <strong>MaratonIA</strong> con branding Cashea: el sistema persistente que onboarda a cada nuevo ingreso de forma automática.</p>
          <ul class="topics">
            <li>Incluye todo Fundamentals</li>
            <li>MaratonIA + asistente de ruta</li>
            <li>Onboarding de nuevos ingresos</li>
            <li>Panel ejecutivo de avance</li>
          </ul>
        </div>
        <div class="module tier">
          <span class="roman">T3</span>
          <h3>Enterprise</h3>
          <p class="obj">Todo Ecosystem más la auditoría de procesos con IA, talleres por área crítica y acompañamiento dedicado.</p>
          <ul class="topics">
            <li>Incluye todo Ecosystem</li>
            <li>Auditoría de procesos con IA</li>
            <li>Talleres por área crítica</li>
            <li>Acompañamiento dedicado</li>
          </ul>
        </div>
      </div>
      <div class="foot">
        <img src="../../../../logos/educacion/NEGRO.png" alt="">
        <span class="meta">Cashea · Propuesta · CAP-006</span>
      </div>
    </section>
```

Nota: reutiliza la grid `.modules`/`.module` (3 cards, layout probado). No usa montos (§ decisión usuario).

- [ ] **Step 2: Añadir CSS del tier recomendado al final de `styles.css`**

```css
/* s-tiers · tier recomendado */
.s-tiers .module.tier { position: relative; }
.s-tiers .module.tier-rec {
  border: 2px solid #F4BA1A;
  background: rgba(244, 186, 26, 0.06);
}
.s-tiers .tier-badge {
  position: absolute;
  top: -11px;
  left: 16px;
  background: #F4BA1A;
  color: #000000;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 999px;
}
```

- [ ] **Step 3: Verificar visualmente que las 3 tier-cards no desbordan** (confirmación en Task 16).

- [ ] **Step 4: Commit**

```bash
git add "<SLUG>/index.html" "<SLUG>/styles.css"
git commit -m "feat(cap-006): slide de 3 tiers escalables (Tier 2 recomendado)"
```

---

## Task 6: Metodología (s-orange)

**Files:**
- Modify: `<SLUG>/index.html` (slide s-orange, líneas 573-599 del original)

- [ ] **Step 1: Reemplazar el contador y los 3 pilares**

```html
      <span class="counter">06 / 11</span>
      <p class="eyebrow">05 · Metodología</p>
      <h2>Aprendizaje<br>Basado en Retos</h2>
      <p class="sub">Modelo Intezia · Tres pilares</p>
      <div class="pillars">
        <div class="pillar">
          <span class="num">01</span>
          <h3>Escala sin perder calidad</h3>
          <p>Capacitamos a los 1.000 colaboradores en cohortes de 250 con 6 facilitadores en paralelo, presencial u online. Cada cohorte trabaja sobre casos reales de su rol, no demos genéricas.</p>
        </div>
        <div class="pillar">
          <span class="num">02</span>
          <h3>Persistencia, no eventos</h3>
          <p>La adopción vive en <strong>MaratonIA</strong>, la plataforma educativa en línea de Intezia. Cada nuevo ingreso entra a una ruta guiada por un asistente, así el conocimiento queda en un sistema y no en personas.</p>
        </div>
        <div class="pillar">
          <span class="num">03</span>
          <h3>Diagnóstico antes de escalar</h3>
          <p>En el tier Enterprise, una auditoría de procesos con IA define qué automatizar y en qué orden. La inversión sigue al dato, no al revés.</p>
        </div>
      </div>
      <div class="foot">
        <img src="../../../../logos/educacion/NEGRO.png" alt="">
        <span class="meta">Intezia · Modelo ABR</span>
      </div>
```

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): metodología a escala + persistencia"
```

---

## Task 7: Beneficios (s-benefits)

**Files:**
- Modify: `<SLUG>/index.html` (slide s-benefits, líneas 602-656 del original)

- [ ] **Step 1: Reemplazar contador, grid de perfil/beneficio y el copy del equipo**

Mantener intactos los `<div class="multi-box ...>` (AcroForm Entregables/Acreditacion) y el bloque `.team`/`.foot`. Reemplazar:

```html
      <span class="counter">07 / 11</span>
      <p class="eyebrow">06 · Beneficios</p>
      <h2>Lo que queda instalado.</h2>
      <div class="grid">
        <div class="block">
          <p class="label">Para la organización</p>
          <ul>
            <li><strong>Escala:</strong> 1.000 colaboradores nivelados en un piso común de IA.</li>
            <li><strong>Persistencia:</strong> cada nuevo ingreso se onboarda solo en MaratonIA.</li>
            <li><strong>Visibilidad:</strong> panel ejecutivo del avance de la adopción.</li>
          </ul>
        </div>
        <div class="block">
          <p class="label">El cambio de fondo</p>
          <p>
            Cashea deja de depender de talleres puntuales. La adopción de IA pasa de ser un <strong>evento</strong> a ser una <strong>capacidad organizacional</strong> que crece con la empresa: el conocimiento vive en un sistema consultable, no en las personas que un día tomaron la clase.
          </p>
        </div>
        <div class="block">
          <p class="label">Entregables</p>
        </div>
        <div class="block">
          <p class="label">Acreditación</p>
        </div>
      </div>
```

- [ ] **Step 2: Reemplazar el copy de Isaac en el bloque `.team` (sin tocar el de Flavia)**

```html
              <p class="role">Consultor · Facilitador Senior</p>
              <p>Lidera el diseño y la facilitación del stack de adopción: nivelación en cohortes, masterclass ejecutiva y puesta en marcha de MaratonIA para Cashea.</p>
```

- [ ] **Step 3: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): beneficios del sistema de adopción"
```

---

## Task 8: Impacto (s-impact) — datos McKinsey 2025 (§4.9)

**Files:**
- Modify: `<SLUG>/index.html` (slide s-impact, líneas 659-719 del original)

Fuentes verificadas (WebSearch 2026-05-24): McKinsey, *The State of AI 2025* (nov 2025), encuesta a 1.993 organizaciones en 105 países. 88% usan IA en al menos una función · dos tercios (67%) en múltiples funciones · 62% experimentan con agentes · 6% «high performers» capturan valor desproporcionado.

- [ ] **Step 1: Reemplazar barras, panel-source, gauge, chips y hook**

```html
      <span class="counter">08 / 11</span>

      <div class="impact-head">
        <p class="eyebrow">07 · Impacto</p>
        <h2>Todos adoptan IA.<br><span class="hl">Pocos capturan el valor</span>.</h2>
      </div>

      <div class="impact-body">
        <div class="chart-panel">
          <p class="panel-title">Adopción de IA generativa en organizaciones</p>
          <div class="bars">
            <div class="bar-row">
              <span class="bar-label">Usan IA en al menos una función</span>
              <div class="bar-track"><div class="bar-fill" style="--w:88%"><span class="bar-val">88%</span></div></div>
            </div>
            <div class="bar-row">
              <span class="bar-label">Usan IA en múltiples funciones</span>
              <div class="bar-track"><div class="bar-fill" style="--w:67%"><span class="bar-val">67%</span></div></div>
            </div>
            <div class="bar-row">
              <span class="bar-label">Experimentan con agentes de IA</span>
              <div class="bar-track"><div class="bar-fill" style="--w:62%"><span class="bar-val">62%</span></div></div>
            </div>
          </div>
          <div class="bar-axis"><span class="scale"><span>0</span><span>25</span><span>50</span><span>75</span><span>100%</span></span></div>
          <p class="panel-source">Fuente: McKinsey · The State of AI 2025 (noviembre 2025) · encuesta a 1.993 organizaciones en 105 países.</p>
        </div>

        <div class="gauge-panel">
          <div class="gauge" style="--pct:88">
            <div class="gauge-core">
              <span class="gauge-num">88<span class="pct">%</span></span>
              <span class="gauge-cap">ya usan IA en su operación</span>
            </div>
          </div>
          <div class="chips">
            <div class="chip">
              <span class="chip-num">62%</span>
              <span class="chip-lbl">prueban agentes</span>
            </div>
            <div class="chip">
              <span class="chip-num">6%</span>
              <span class="chip-lbl">capturan el valor</span>
            </div>
          </div>
        </div>
      </div>

      <div class="impact-hook">
        <span class="hook-mark">&#9656;</span>
        <p class="hook-text">
          El acceso a la IA ya no distingue a nadie: <strong>88% de las organizaciones ya la usan</strong>. Lo que separa al 6% que captura valor real no es la herramienta, es un <strong>sistema de adopción sostenido</strong>. Eso es lo que el Stack construye para Cashea.
        </p>
      </div>

      <div class="foot">
        <img src="../../../../logos/educacion/BLANCO.png" alt="">
        <span class="meta">Cashea · Propuesta · CAP-006</span>
      </div>
```

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): impacto con datos McKinsey State of AI 2025"
```

---

## Task 9: Propuesta Económica (s-price) — duración

**Files:**
- Modify: `<SLUG>/index.html` (slide s-price, líneas 722-764 del original)

No tocar los `multi-box`, `cot-frame` ni AcroForms (los llena ventas). Solo:

- [ ] **Step 1: Actualizar contador y el valor de Duración**

```html
      <span class="counter">09 / 11</span>
```

y reemplazar el bloque Duración:

```html
      <div class="block">
        <span class="block-eyebrow">Duración</span>
        <p class="block-value">Cohortes de 4 a 6 semanas, según el tier.</p>
      </div>
```

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): ajusta duración del slide económico al modelo por tiers"
```

---

## Task 10: Próximos pasos (s-steps)

**Files:**
- Modify: `<SLUG>/index.html` (slide s-steps, líneas 767-807 del original)

Los textos visibles `acro-default-text` deben coincidir con lo que pre-llena el customize (Task 15).

- [ ] **Step 1: Actualizar contador y los 3 `acro-default-text` de body/título**

```html
      <span class="counter">10 / 11</span>
```

Paso 01 (título/body):
```html
        <span class="acro-default-text">Confirmar alcance y fechas</span>
```
```html
        <span class="acro-default-text">Definimos el tier, la modalidad y el calendario de cohortes, más la zona horaria de las sesiones online.</span>
```

Paso 02:
```html
        <span class="acro-default-text">Firmar el acuerdo</span>
```
```html
        <span class="acro-default-text">Firmamos el acuerdo con el 50% de anticipo y coordinamos el arranque. Intezia te acompaña en cada paso.</span>
```

Paso 03:
```html
        <span class="acro-default-text">Reunión de arranque</span>
```
```html
        <span class="acro-default-text">Kickoff de unos 30 minutos para alinear casos reales por rol y preparar las cohortes y MaratonIA.</span>
```

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): próximos pasos del stack"
```

---

## Task 11: Cierre (s-end)

**Files:**
- Modify: `<SLUG>/index.html` (slide s-end, líneas 810-835 del original)

- [ ] **Step 1: Actualizar contador y mensaje de cierre**

```html
      <span class="counter">11 / 11</span>
```
```html
      <p class="end-message">
        De un <span class="hl-orange">taller puntual</span><br>a un <span class="hl-yellow">sistema que escala</span>.
      </p>
```

Mantener el `cta`, `end-contact` y datos de Flavia/empresa.

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/index.html"
git commit -m "feat(cap-006): cierre del AI Adoption Stack"
```

---

## Task 12: Verificar contadores y conteo de slides

**Files:**
- Modify: `<SLUG>/index.html` (verificación global)

- [ ] **Step 1: Confirmar que hay exactamente 11 `<section class="slide`**

Run: `grep -c 'class="slide' "<SLUG>/index.html"`
Expected: `11`

- [ ] **Step 2: Confirmar que los contadores van 01/11 … 11/11 sin saltos**

Run: `grep -oE '[0-9]{2} / 11' "<SLUG>/index.html"`
Expected: 01/11, 02/11, …, 11/11 (11 líneas, en orden).

- [ ] **Step 3: Si algún contador quedó como `/ 16` o desordenado, corregir con Edit y commit**

```bash
git add "<SLUG>/index.html"
git commit -m "fix(cap-006): renumera contadores a 11 slides"
```

---

## Task 13: Reescribir brief.md

**Files:**
- Modify: `<SLUG>/brief.md` (reescritura completa)

- [ ] **Step 1: Reescribir el brief al nuevo enfoque**

Sustituir el contenido por un brief que refleje: programa = *Cashea AI Adoption Stack*; eje = adopción de IA a escala con Claude; audiencia = 1.000 colaboradores + 50 directivos + cobertura de nuevos ingresos; estructura = 3 tiers (Fundamentals / Ecosystem / Enterprise), Tier 2 recomendado; componentes = nivelación masiva, masterclass directivos, MaratonIA (plataforma educativa en línea de Intezia) + asistente de ruta, auditoría de procesos; diagnóstico = los 4 puntos del Task 2; capacidad operativa = 6 facilitadores, cohortes de 250, 4-6 semanas; sin montos en el deck (referencia interna 18K/48K/78K REF queda fuera del entregable); contacto Flavia Martínez + Isaac Rodriguez; notas comerciales estándar (50% anticipo, vigencia 30 días, divisas 7 días). Eliminar todo el contenido «power user / Skills / MCP / Computer Use» como eje.

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/brief.md"
git commit -m "docs(cap-006): brief reescrito a AI Adoption Stack"
```

---

## Task 14: Reescribir programa.md

**Files:**
- Modify: `<SLUG>/programa.md` (reescritura completa)

- [ ] **Step 1: Reescribir el diseño curricular al modelo de stack**

Sustituir por un documento que describa: información general (nombre, empresa, modalidad, acreditación); fundamentación = escalable + persistente (no «techo del power user»); los 4 componentes del stack con su objetivo instructivo y entregables; la arquitectura de 3 tiers y qué incluye cada uno; §5.2 desglose instructivo orientado a derivar los Entregables del Task 15 (nivelación masiva con cohortes → certificación + kit de prompts; masterclass → Mapa de Calor; MaratonIA → onboarding automático + panel; auditoría → diagnóstico + plan). Mantener el formato de las secciones del programa.md actual (1-7) pero con contenido del stack.

- [ ] **Step 2: Commit**

```bash
git add "<SLUG>/programa.md"
git commit -m "docs(cap-006): programa reescrito al modelo de stack por tiers"
```

---

## Task 15: Actualizar customize-cashea-cap006.py (AcroForms)

**Files:**
- Modify: `scripts/customize-cashea-cap006.py` (dict `updates`, líneas 29-59)

- [ ] **Step 1: Reemplazar el dict `updates` por contenido del stack**

```python
    updates = {
        "Entregables": "\r".join([
            "Nivelación de 1.000 colaboradores",
            "Masterclass para 50 directivos",
            "Mapa de Calor de oportunidades",
            "MaratonIA con branding Cashea",
            "Panel ejecutivo de avance",
            "Kit de prompts por rol",
            "Certificado de asistencia INTEZIA",
        ]),
        "Acreditacion": "\r".join([
            "Programa registrado en INTEZIA Education como CAP-006.",
            "Cumple con el modelo pedagógico oficial (ABR).",
            "Material curado y revisado por el equipo académico.",
        ]),
        "Paso01Titulo": "Confirmar alcance y fechas",
        "Paso01Body": (
            "Definimos el tier, la modalidad y el calendario de cohortes, "
            "más la zona horaria de las sesiones online."
        ),
        "Paso02Titulo": "Firmar el acuerdo",
        "Paso02Body": (
            "Firmamos el acuerdo con el 50% de anticipo y coordinamos el "
            "arranque. Intezia te acompaña en cada paso."
        ),
        "Paso03Titulo": "Reunión de arranque",
        "Paso03Body": (
            "Kickoff de unos 30 minutos para alinear casos reales por rol y "
            "preparar las cohortes y MaratonIA."
        ),
    }
```

Nota: cada `PasoNNBody` ≤ 130 chars (memoria [[project_pasos_body_max_chars]]); la caja Entregables ≤ ~8-9 líneas cortas (memoria [[project_entregables_lineas_cortas]]). 7 líneas, todas de un renglón. OK.

- [ ] **Step 2: Actualizar el docstring del script** para que diga «Cashea AI Adoption Stack» en vez de «Claude Power».

- [ ] **Step 3: Commit**

```bash
git add scripts/customize-cashea-cap006.py
git commit -m "feat(cap-006): pre-llenado AcroForms del AI Adoption Stack"
```

---

## Task 16: Generar PDF, customizar, verificar y revisar visualmente

**Files:** ninguno nuevo (ejecución de scripts)

- [ ] **Step 1: Verificación automática estática**

Run: `./scripts/verificar-propuesta.sh "cashea/CAP-006 Claude Power - Skills MCP y Workflows"`
Expected: sin errores de guion largo (§4.13), sin comillas tipográficas en atributos, sin `[CÓDIGO]` sin llenar, customize presente.
Si reporta fallos, corregir en el archivo señalado y volver a correr.

- [ ] **Step 2: Generar el PDF + customizar (par obligatorio §10)**

Run:
```bash
./scripts/generar-pdf.sh "cashea/CAP-006 Claude Power - Skills MCP y Workflows"
python3 scripts/customize-cashea-cap006.py "<SLUG>/propuesta.pdf"
```
(usar la ruta real del PDF que genere el script).
Expected: PDF generado y mensaje «Cashea CAP-006 … customizados».

- [ ] **Step 3: Verificación de overflow**

Run: `node scripts/verificar-overflow.js "<SLUG>/index.html"` (o el invocador estándar del repo).
Expected: 0 slides con overflow. Si hay overflow en Componentes (4 cards) o Tiers, aplicar modo compacto / acortar copy (chips ≤ 28 chars) y regenerar (repetir Step 2).

- [ ] **Step 4: Revisión visual del PDF slide por slide (§4.10, no automatizable)**

Abrir el PDF y confirmar, slide por slide: sin texto cortado, sin chips con `...`, footer/logo sin solape, las 4 cards de Componentes completas, las 3 tier-cards con el badge «Recomendado» visible en Tier 2, AcroForms (Entregables/Acreditación/Pasos) con contenido real, slide de precio con campos de cotización vacíos. Verificar checklist §10 puntos 1-5.

- [ ] **Step 5: Commit del PDF final**

```bash
git add "<SLUG>/propuesta.pdf"
git commit -m "build(cap-006): PDF del AI Adoption Stack generado y customizado"
```

---

## Self-review (cobertura del spec)

- Identidad/eje (spec §3.4) → Task 1, 13, 14. ✓
- 3 tiers escalables, Tier 2 recomendado, sin montos (spec §3.2/§3.3) → Task 5. ✓
- Diagnóstico dolores reales (spec §5 fila 01) → Task 2. ✓
- Componentes incl. MaratonIA descrita en primer uso (spec §3.5) → Task 4 (y 3, 6). ✓
- Impacto con estudios reales citados (spec §4 §4.9) → Task 8 (McKinsey 2025). ✓
- AcroForms no-precio pre-llenados; precio vacío (spec §5 filas 08/09) → Task 9, 10, 15. ✓
- Sin guion largo, acrónimos glosados, sin overflow (spec §4) → reglas en cada task + Task 16. ✓
- brief y programa reescritos (spec §6) → Task 13, 14. ✓
- Verificación + par PDF-customize (spec §8) → Task 16. ✓

Sin placeholders pendientes. Tipos/clases consistentes (`.module.tier`, `.tier-rec`, `.tier-badge`, contadores `/ 11`).
