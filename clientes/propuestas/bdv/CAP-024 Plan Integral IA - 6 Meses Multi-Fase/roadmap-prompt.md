# Prompt — Rediseñar la slide «Roadmap de Transformación IA» (BDV · CAP-024)

> Pásale este prompt a un agente con la skill de diseño de slides (`ckm-slides`).
> Es un **CASO ÚNICO**: esta slide NO modifica la plantilla canónica de Intezia —
> es exclusiva de la propuesta BDV CAP-024. El resto del deck no se toca.

---

## Tarea

Rediseña **una sola slide HTML/CSS**: el *Roadmap de Transformación IA* de la propuesta
del Banco de Venezuela. Es la slide **14 de 15** del deck, justo antes del cierre.
La versión actual existe (`<section class="slide s-roadmap">` en `index.html` +
bloque `.s-roadmap` / `.rm-*` en `styles.css`) pero **no convence visualmente**:
los conectores se ven sucios y la jerarquía no comunica el viaje. Reemplázala por
completo — puedes traer tu propio HTML y CSS para esta slide.

## Qué debe comunicar el roadmap (un mapa visual del viaje)

Es un **mapa de transformación**: muestra cómo el banco avanza de un colaborador
suelto a una **organización con implementación exitosa de IA**. Estructura de
**3 fases en 2 rutas** que arrancan juntas, se bifurcan y vuelven a converger:

```
                    ┌─► FASE 2 (áreas corporativas) ─┐
FASE 1 (todos) ─────┤                                 ├──► RESULTADO FINAL
                    └─► FASE 3 (solo Tecnología) ─────┘
```

### Fase 1 · Gemini Fundamentals — punto de partida común
- **Perfil / audiencia:** los 600 colaboradores del banco, **todos**, incluido el
  equipo de Tecnología. 100 capacitados por mes, 6 cohorts escalonados.
- **Qué hacen:** fundamentos de IA, Gemini integrado a Google Workspace, prompting
  estructurado RCTF, ética y privacidad bancaria, construyen el AUP corporativo.
- **Beneficio:** una base común — todo el banco habla el mismo idioma de IA.
- **Resultado de la fase:** 600 colaboradores activados + biblioteca de prompts BDV.

### Fase 2 · Bootcamps Verticales — ruta de las áreas corporativas
- **Perfil / audiencia:** todas las áreas del banco **excepto Tecnología**
  (Operaciones, Banca Comercial, Retail, Crédito y Riesgo, Marketing, Talento
  Humano, Legal y Compliance, Tesorería — 8 áreas).
- **Qué hacen:** levantamiento de información previo por área, temario 100%
  personalizado al rol, práctica con casos reales del banco, proyecto final aplicado.
- **Beneficio:** cada área domina la IA en su trabajo concreto, no en abstracto.
- **Resultado de la fase:** dominio aplicado al rol + 8 Libretas Vivas de Prompts +
  8 proyectos finales + 8 casos de éxito documentados.

### Fase 3 · Automatización y Agentes IA — ruta del equipo de Tecnología
- **Perfil / audiencia:** **solo el equipo de Tecnología** del BDV. (Tecnología
  hace F1 para nivelarse con el banco y luego salta directo a F3 — no pasa por F2.)
- **Qué hacen:** Google AI Studio avanzado, diseño y despliegue de agentes IA
  funcionales, integración con APIs y procesos internos, gobernanza técnica de IA.
- **Beneficio:** Tecnología pasa de usuario a constructor — emerge como el
  Centro de Excelencia IA interno del banco.
- **Resultado de la fase:** ≥2 agentes IA desplegados + framework de gobernanza
  técnica + roadmap del año 2.

### Resultado final (cierre del mapa)
Las dos rutas convergen en: **«BDV — una organización con implementación exitosa
de IA»** (banco aumentado). Puntos del estado final: 600 colaboradores capacitados ·
cada área con IA aplicada al rol · Tecnología con agentes reales desplegados ·
ética y gobernanza integradas · métricas y roadmap del año 2 listos para el comité.

### Ética y gobernanza — debe verse en todo el recorrido
Requisito del sector bancario: la **ética, la privacidad de datos financieros y la
gobernanza** no son una fase aparte — son **transversales a las 3 fases**. El diseño
debe reflejarlo (p. ej. una banda/eje que cruza todo el roadmap, o un elemento
presente en cada fase). No la dejes como una nota al pie aislada.

## Restricciones técnicas (obligatorias)

- **Una slide A4 landscape**: `1123 × 794 px` (`--slide-w` / `--slide-h`).
  Estructura: `<section class="slide s-roadmap"> … </section>`.
- Debe incluir, como el resto del deck: `<span class="counter">14 / 15</span>`,
  un `<p class="eyebrow">`, un `<h2>` de título, y al pie
  `<div class="foot"><img …NEGRO o BLANCO…><span class="meta">BDV · CAP-024</span></div>`.
- **CSS puro, sin JavaScript y sin `<svg>` complejos.** El deck se exporta a PDF con
  Chrome headless; todo debe renderizar fiel en impresión. Conectores/líneas: usar
  `border`, `::before/::after`, gradientes o grid — nada que dependa de JS.
- **Paleta exclusiva Intezia** — solo estos 4 colores, ningún otro:
  `#000000` negro · `#F4BA1A` amarillo · `#E58423` naranja · `#FFFFFF` blanco.
  Gradiente cálido disponible: `linear-gradient(135deg,#F4BA1A,#E58423)`.
- **Tipografía:** `"Graphit","Inter",system-ui,sans-serif`. Títulos en bold (700).
- **Logo:** división Educación. Ruta desde esta carpeta:
  `../../../../logos/educacion/BLANCO.png` (fondo oscuro) ·
  `../../../../logos/educacion/NEGRO.png` (fondo claro).
- El contenido es **estático** (sin campos AcroForm editables) — no usar las frases
  marcador `Lo que se llevan`, `Propuesta Económica` ni `Cómo arrancamos`.
- Entrega el HTML de la `<section>` + el CSS de `.s-roadmap` (y sus sub-clases) para
  pegarlos en `index.html` y `styles.css`. El CSS nuevo reemplaza el bloque
  `.s-roadmap` / `.rm-*` actual.

## Dirección creativa sugerida (libre)

Piensa en un **mapa de viaje / metro line / sendero** que se lee de izquierda a
derecha: un origen común, una bifurcación clara en dos rutas etiquetadas (áreas vs.
Tecnología), y una convergencia en el destino. Cada fase debe mostrar de un vistazo
su **perfil (quién)**, su **beneficio (qué gana)** y su **resultado (qué entrega)**.
Fondo oscuro de alto contraste para que la slide "golpee" antes del cierre. Prioriza
claridad de la narrativa sobre densidad de texto.
