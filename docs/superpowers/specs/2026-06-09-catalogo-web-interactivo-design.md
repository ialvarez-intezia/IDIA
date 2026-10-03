# Catálogo web interactivo de Intezia — Diseño

> Fecha: 2026-06-09 · Rama: `rediseno-catalogo-talleres`
> Objetivo: migrar el catálogo de Intezia de PDF a una página web interactiva, ligera y
> desplegable, donde el cliente explore todo el catálogo desde una sola URL.

---

## 1. Contexto y objetivo

Hoy el catálogo vive como un deck A4 landscape de 33 slides (estilo HUD) pensado para
exportar a PDF (`clientes/propuestas/catalogo/Catalogo Talleres 2026/`). Es un documento
para imprimir/enviar, no para navegar.

**Meta:** una web interactiva (no una landing completa, no un PDF) en una sola URL que el
usuario despliega para todo el mundo. El cliente entra, explora, busca, filtra, abre la
ficha de cualquier programa y agenda. Debe verse **novedosa y de alto nivel de diseño**.

**No-objetivos:** no es un sitio corporativo completo, ni un LMS, ni e-commerce con pagos.
Es un explorador de catálogo.

---

## 2. Alcance

**v1 (lo que se despliega ahora):**
- ~20 Talleres y Capacitaciones (`TA-###` / `CAP-###`).
- Rutas: Diamond (producto estrella anual) y Ruta Integral Claude.

**Diseñado para extender después sin rehacer nada:** Charlas/Eventos y Cursos/Diplomados se
suman agregando entradas de datos y, si hace falta, una categoría nueva. No entran en v1.

**Capacidades nuevas que el PDF no da (confirmadas):**
1. Buscador por texto + filtros (por sección, modalidad, división, eje).
2. Vista de detalle por programa con **URL propia compartible**.
3. CTA "Aplica aquí" + contacto directo.

**Fuera de v1:** descarga de PDF por programa (se descartó: el objetivo es migrar fuera del
PDF), login, carrito, multi-idioma, CMS.

---

## 3. Decisiones cerradas

| Tema | Decisión |
|---|---|
| Base técnica | **Estático sin build**: HTML + CSS + JS + `data/programas.json`. Deploy = subir la carpeta (Netlify/Vercel/GitHub Pages). |
| Ubicación | Carpeta de primer nivel **`catalogo-web/`**, autocontenida, separada de `clientes/propuestas/` (no interfiere con el flujo de propuestas). |
| Estructura de navegación | **Grid explorador**: hero → barra de búsqueda + filtros en chips → cuadrícula de tarjetas → clic abre ficha. |
| Look | **HUD claro**: paleta de marca sobre fondo claro, esquinas HUD, scanline sutil, dorado/naranja como acento. |
| Ficha de detalle | **v4 diagramática** (ver §6.2): hero con bloque negro de corte diagonal + número gigante + anillo de duración (completo), banda "Para quién" oscura, herramientas en círculos, **temario como diagrama de recorrido** (nodos circulares conectados + bandera de meta), entregables como sellos, banda CTA. |
| Indicador de duración | **Anillo completo** (no parcial: un anillo a medias se lee como porcentaje y confunde). |
| Apertura de la ficha | **Overlay** sobre el catálogo con **deep-link por hash** (`index.html#ta-008`) para compartir el enlace directo a un programa. |
| Tipografía | **Graphit** (Bold + Regular) incrustada como webfont (`.woff2`, los suministra el usuario). Fallback: geométrica (Space Grotesk / Inter), nunca serif. |
| CTA "Aplica aquí" | Campo editable en `programas.json` (`cta_url`), placeholder por ahora; el usuario lo reemplaza sin tocar código. |
| Contacto "Hablar con un asesor" | **WhatsApp** (`wa.me`), número como campo editable (placeholder si no se suministra). |

---

## 4. Arquitectura

Sitio **data-driven**: el contenido vive en `programas.json`; el HTML/JS lo renderiza. Sumar,
editar o reordenar programas = editar datos, no código.

```
catalogo-web/
├── index.html              ← una sola página: catálogo (hero+buscador+filtros+grid) y ficha
├── assets/
│   ├── css/
│   │   └── styles.css       ← design system: tokens de marca + HUD claro + componentes
│   ├── js/
│   │   └── catalogo.js      ← carga datos, render grid, búsqueda, filtros, hash-routing, ficha
│   ├── fonts/               ← Graphit-Bold.woff2, Graphit-Regular.woff2 (los aporta el usuario)
│   └── img/
│       └── logo-educacion.png (copiado de /logos para autocontención) + íconos
├── data/
│   └── programas.json       ← fuente de verdad del contenido
└── README.md                ← contexto, cómo editar datos, cómo desplegar
```

**Flujo de datos:** `index.html` carga `catalogo.js` → `fetch('data/programas.json')` → render
del grid → eventos de búsqueda/filtro re-renderizan el grid → clic en tarjeta (o hash al
cargar) renderiza la ficha en un overlay y actualiza la URL con `#<slug>`.

**Routing:** hash-based. `#` o vacío = catálogo. `#ta-008` = ficha de TA-008 abierta. El botón
atrás del navegador y "Volver al catálogo" funcionan; el enlace es compartible.

**Sin servidor.** `fetch` de un JSON local funciona al servir la carpeta (cualquier host
estático; en local con un `python3 -m http.server`). Si se quisiera abrir con `file://` sin
servidor, el JSON se puede inlinear como fallback — no requerido para deploy.

**Responsive:** móvil primero en comportamiento.
- Grid: 1 columna (móvil) → 2 (tablet) → 3 (desktop).
- Hero: apila texto y ficha rápida; el bloque diagonal pasa a recto en móvil.
- Temario-diagrama: en móvil el recorrido horizontal se vuelve **vertical** (nodos en
  columna con la línea a la izquierda y el texto a la derecha), nunca scroll horizontal forzado.

---

## 5. Modelo de datos — `programas.json`

Arreglo de objetos. Campos por programa:

```json
{
  "codigo": "TA-008",
  "slug": "ta-008",
  "titulo": "Inteligencia Artificial para Ventas",
  "categoria": "taller",                // taller | capacitacion | ruta
  "seccion": "especializacion-area",    // cultura-estrategia | especializacion-area | deep-dive-claude | stack-microsoft | bootcamps | rutas
  "division": "educacion",              // educacion | fundacion
  "eje": "IA en ventas",
  "audiencia": "Ejecutivos de ventas, SDRs y líderes comerciales. No requiere base técnica.",
  "duracion_horas": 8,
  "duracion_label": "8 h",
  "sesiones": "2 sesiones de 4 h",
  "modalidad": "Híbrido",               // Presencial | Online Síncrono | Online Asíncrono | Híbrido
  "objetivo": "Equipa a tu fuerza comercial para prospectar, personalizar y cerrar más rápido con IA…",
  "requisitos": ["Laptop con internet", "Correo corporativo", "Disposición a practicar en vivo"],
  "herramientas": ["Claude", "ChatGPT", "Gemini", "CRM del cliente"],
  "modulos": [
    { "n": "01", "titulo": "Prospección aumentada", "desc": "Señales de compra y primeros mensajes que abren conversación." }
  ],
  "meta_resultado": "Cierra más y más rápido",
  "entregables": ["Biblioteca de prompts de ventas", "Plantilla de propuesta con IA", "Secuencia de prospección lista", "Certificado avalado por INTEZIA"],
  "acredita": "INTEZIA",
  "cta_url": "",                        // placeholder editable (Calendly u otro)
  "whatsapp": "",                       // placeholder editable (número o link wa.me)
  "destacado": false                    // true para Rutas Diamond y piezas estrella
}
```

Notas:
- `seccion` alimenta los filtros del catálogo (las 5 secciones del catálogo actual + `rutas`).
- Las **Rutas** (Diamond, Integral Claude) usan el mismo esquema con `categoria: "ruta"` y
  `destacado: true`; en el grid se muestran con tratamiento de tarjeta estrella (degradado
  dorado→naranja). Su ficha puede omitir campos no aplicables sin romper el render.
- Charlas/Cursos futuros: misma forma, nueva `categoria`/`seccion`.

---

## 6. Componentes y vistas

### 6.1 Catálogo (vista principal)

- **Hero HUD claro:** eyebrow ("Intezia · Catálogo de Capacitaciones 2026"), título grande
  con palabra acentuada, lead, fila de stats (20 talleres · 5 áreas · ★ Rutas Diamond),
  **buscador** (placeholder con ejemplo), **chips de filtro** por sección (incl. "Todos").
  Esquinas HUD + scanline sutil + radial dorado.
- **Barra de búsqueda/filtros fija** al hacer scroll (sticky) para filtrar sin volver arriba.
- **Grid de tarjetas de programa:** código, título, meta (duración · modalidad), tag de
  sección, flecha de hover. Rutas Diamond = tarjeta destacada (degradado). Hover con realce.
- **Búsqueda:** match por título, código, eje y audiencia (case/acentos-insensible).
- **Filtros:** por sección (chips). Extensible a modalidad/división si se desea (mismo patrón).
- **Estado vacío:** mensaje claro si la búsqueda no arroja resultados (sin caja vacía muda).

### 6.2 Ficha de detalle (overlay, deep-link `#slug`) — diseño v4

Distribución por **bandas de ancho completo** con **variedad de formas** (sin "todo rectángulo"):

1. **Hero de ficha:** izquierda clara (eyebrow/breadcrumb, título grande, objetivo, anillo
   **completo** de duración + datos en pills) · derecha **bloque negro con corte diagonal**
   (clip-path) con el **número del programa gigante** (outline dorado), ficha rápida (código,
   eje, acredita) y CTAs ("Aplica aquí" pill dorada + "Hablar con un asesor").
2. **Banda Para quién / Herramientas:** "Para quién es" en tile **oscuro dominante** con
   semicírculo decorativo; "Herramientas" como **círculos** (badges redondos legibles).
3. **Temario = diagrama de recorrido:** nodos circulares numerados conectados por una línea
   dorada con flecha, títulos alternados (zig-zag), y **bandera de meta** (banderín clip-path)
   al final con el resultado. En móvil: vertical.
4. **Entregables = sellos circulares** (medallones con ✓ / ★) en fila.
5. **Banda CTA de cierre** (negra con halo dorado): titular + "Aplica aquí".
6. **Barra superior:** ← Volver al catálogo · código · compartir · cerrar.

---

## 7. Sistema visual (tokens)

- **Color:** marca estricta — `#000000`, `#F4BA1A` (dorado), `#E58423` (naranja), `#FFFFFF`.
  Neutros claros derivados para fondos/bordes (ej. `#faf9f6`, `#f4f3ee`, `#e7e7dd`, textos
  `#0a0a0a`/`#4f4e49`). No se inventan colores fuera de esta familia.
- **Tipografía:** Graphit Bold (títulos) + Graphit Regular (cuerpo). Fallback geométrico
  (Space Grotesk / Inter). Nunca serif.
- **Formas:** mezcla intencional — rectángulos redondeados para texto, **círculos** (anillo,
  nodos, badges, sellos), **cortes diagonales** (clip-path), **banderín** de meta, **arcos/
  semicírculos** decorativos. La variedad es un requisito de diseño, no accidental.
- **Movimiento (en build):** entrada suave de tarjetas, hover con realce, transición de
  apertura de la ficha, número del hero con leve parallax. Sutil, nunca estorba la lectura.

---

## 8. Reglas de calidad (heredadas del sistema Intezia)

Aplican al copy y al render de cara al cliente:

1. **Legibilidad — bloqueante:** tamaños mínimos legibles (cuerpo ≥ ~13px, labels ≥ ~11px),
   contraste suficiente (WCAG AA; nada de dorado o gris claro sobre fondo claro en texto
   pequeño), cajas que se ajustan al contenido.
2. **Cero truncado / sin overflow (§4.10):** ningún texto cortado, ni `…`, ni recorte por
   altura fija. El contenido se acota o el contenedor crece; nunca se esconde.
3. **Sin guion largo (§4.13):** ni `—` ni `–` como separador en copy de cara al cliente.
4. **Acrónimos glosados (§4.12):** jerga (RCTF, AUP, GenAI…) expandida en su primer uso.
5. **Idioma español (§4.4)**, salvo nombres propios de herramientas.
6. **Marca (§4.1):** logo Intezia Educación presente; paleta y tipografía respetadas.

---

## 9. Contenido: origen y vacíos

`programas.json` se compila desde:
- `empresa/catalogo.md` (fuente curada; hoy solo TA-021 y TA-023 están completos).
- El deck `clientes/propuestas/catalogo/Catalogo Talleres 2026/index.html` (slides de los 20
  talleres: títulos, ejes, módulos).
- Briefs por taller en `clientes/propuestas/catalogo/TA-### …/brief.md` cuando existan.

**Riesgo conocido:** parte del contenido por taller puede estar incompleto o disperso. El
plan incluirá un paso de **auditoría de contenido**: compilar lo disponible, marcar campos
faltantes por programa y entregar al usuario una lista de huecos a completar antes de
publicar. No se inventan módulos, entregables ni cifras (coherente con §4.9).

---

## 10. Criterios de aceptación

- [ ] Una sola URL abre el catálogo con hero, buscador, filtros y grid de los ~20 talleres + Rutas.
- [ ] Buscar y filtrar actualiza el grid al instante; estado vacío claro.
- [ ] Clic en una tarjeta abre la ficha v4; `#slug` en la URL abre esa ficha directo y es compartible.
- [ ] La ficha respeta el diseño v4 (formas variadas, temario-diagrama, anillo completo) en desktop y móvil.
- [ ] "Aplica aquí" y "WhatsApp" leen sus destinos de `programas.json` (editables sin tocar código).
- [ ] Sin overflow, sin truncado, contraste AA, copy sin guion largo (verificable).
- [ ] La carpeta `catalogo-web/` se despliega tal cual en un host estático.
- [ ] Sumar un programa nuevo = agregar un objeto a `programas.json`, sin tocar HTML/JS.

---

## 11. Futuro (no v1)

- Charlas/Eventos y Cursos/Diplomados como categorías nuevas.
- Filtros adicionales (modalidad, división, duración).
- Páginas estáticas por programa (SEO) generadas por script desde `programas.json`.
- Animaciones avanzadas / modo comparación / "arma tu ruta".
