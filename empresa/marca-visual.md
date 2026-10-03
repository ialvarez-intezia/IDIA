# Marca visual — Sistema oficial de Intezia

> Activos visuales **obligatorios** de Intezia. **Toda propuesta y documento aplica esta marca sin excepción**: logos, paleta y tipografía. Si una salida no usa esta marca, está mal hecha.

---

## 1. Logos (obligatorios)

### Inventario

| División | BLANCO (sobre fondo oscuro) | NEGRO (sobre fondo claro) |
|---|---|---|
| Fundación | `logos/fundacion/BLANCO.png` | `logos/fundacion/NEGRO.png` |
| Educación | `logos/educacion/BLANCO.png` | `logos/educacion/NEGRO.png` |

### Reglas de uso (no negociables)

1. **Toda propuesta lleva logo en portada** y en cada slide del cuerpo (footer o esquina).
2. **Variante por contraste**: BLANCO sobre fondos oscuros, NEGRO sobre fondos claros.
3. **División**: la decide el usuario al inicio. Ver `empresa/divisiones.md`.
4. **No deformar** el logo. Mantener proporciones al escalar.
5. **Aire mínimo** alrededor: ≥ 1× la altura del logo libre de otros elementos.
6. **Logo aliado**: si la propuesta lleva logo de cliente o universidad aliada, va junto al de Intezia separado por línea diagonal o vertical, mismo peso visual.

### Uso en HTML (skill `ckm-slides`)

Rutas relativas desde `clientes/<slug>/propuesta/index.html`:

```html
<img src="../../../logos/fundacion/NEGRO.png" alt="Intezia Fundación" class="logo">
<img src="../../../logos/educacion/BLANCO.png" alt="Intezia Educación" class="logo">
```

---

## 2. Paleta de colores oficial

Tres colores principales. Alto contraste, estética premium tech-focused.

### Tokens

| Token | Nombre | Hex | RGB |
|---|---|---|---|
| `--intezia-black` | Deep Black | `#000000` | `rgb(0, 0, 0)` |
| `--intezia-yellow` | Bright Golden Yellow | `#F4BA1A` | `rgb(244, 186, 26)` |
| `--intezia-orange` | Vibrant Ochre Orange | `#E58423` | `rgb(229, 132, 35)` |

### Reglas de uso

- **Negro `#000000`**: fondo dominante de slides "premium". Texto sobre fondo claro.
- **Amarillo `#F4BA1A`**: color principal de marca. Llamadas a la acción, énfasis, números/estadísticas destacadas, acentos sobre fondo negro.
- **Naranja `#E58423`**: secundario / cálido. Highlights, divisores, elementos geométricos, gradientes con el amarillo.
- **Blanco `#FFFFFF`**: superficie clara opcional, texto sobre fondo negro.

### Combinaciones recomendadas

| Combinación | Uso |
|---|---|
| Fondo negro + texto blanco + acentos amarillos/naranjas | Slides hero, portada, cierre |
| Fondo blanco + texto negro + acentos amarillos | Slides de contenido denso |
| Gradiente amarillo → naranja | Banners, separadores, llamadas a la acción |
| Negro + amarillo (sin naranja) | Estilo minimalista, máxima legibilidad |

### Variables CSS recomendadas

```css
:root {
  --intezia-black: #000000;
  --intezia-yellow: #F4BA1A;
  --intezia-orange: #E58423;
  --intezia-white: #FFFFFF;

  /* Aplicaciones derivadas */
  --bg-dark: var(--intezia-black);
  --bg-light: var(--intezia-white);
  --text-on-dark: var(--intezia-white);
  --text-on-light: var(--intezia-black);
  --accent-primary: var(--intezia-yellow);
  --accent-secondary: var(--intezia-orange);
  --gradient-warm: linear-gradient(135deg, var(--intezia-yellow), var(--intezia-orange));
}
```

### ¿Diferencia entre Fundación y Educación?

Misma paleta para ambas divisiones. La distinción la hace el **logo**, no el color. Si en el futuro cada división adopta una variante cromática propia, registrarlo aquí y en `aprendizajes.md`.

---

### Descuento con urgencia — excepción de color explícita (2026-09-23)

> Origen: pedido de convertir el descuento de la hoja de cotización en palanca de cierre con
> "letra roja, fondo rosado". Primera propuesta de Claude fue una variante tintada del
> naranja de marca (dentro de paleta, siguiendo la regla de este archivo de proponer
> alternativa antes de aceptar un color fuera de marca) — **el usuario la rechazó
> explícitamente** ("tiene que ser a juro rojo... sino no es visualmente atractivo", mismo
> hilo) y pidió el rojo/rosado literal. Queda como **excepción de color permanente, pero
> acotada a este único elemento**: el resto del sistema (fondos, textos, acentos, gráficas de
> Impacto, roadmap, etc.) sigue exclusivamente en `#000000` / `#F4BA1A` / `#E58423` /
> `#FFFFFF` — esta excepción no abre la puerta a otros colores en ningún otro lugar del deck.

- **Tokens de la excepción** (fijos, no se improvisan por deck):
  ```css
  --discount-urgent-red: #D32F2F;
  --discount-urgent-pink-bg: #FCE4EC;
  ```
- **Texto**: `--discount-urgent-red` (`#D32F2F`), `font-weight: 700`. Es la única pieza de
  toda la propuesta que usa este color — en ningún otro título, acento o gráfica.
- **Fondo**: `--discount-urgent-pink-bg` (`#FCE4EC`), aplicado únicamente a la caja/etiqueta
  del descuento (`.cot-urgent-note`), nunca a la slide completa ni a otros bloques.
- **Monto con signo menos**: el campo AcroForm `Descuento` sigue vacío para que ventas
  escriba solo el número (mismo criterio que el resto de precio) — el signo y el símbolo de
  moneda van **fuera del campo**, como prefijo estático `−$` inmediatamente antes de la caja
  (clase `.cot-sign-minus`, mismo rojo bold de la excepción). Así se lee `−$400` sin tocar el
  JS de cálculo (`agregar-campo-precio.py` ya aplica `Math.abs()` al valor del descuento,
  compatible con que ventas escriba el número con o sin signo).
- **Texto de urgencia (corregido 2026-09-23 — texto más corto, letra más grande)**:
  **"Descuento válido por 15 días"** (sin "por aprobación en"). Etiqueta `.cot-urgent-note`,
  `font-size: 13px` (antes 9px, muy chica para su función de urgencia), fondo rosado de la
  excepción, texto rojo bold, `border-radius: 6px`, `padding: 5px 12px`. Convive con
  "Cotización válida por 30 días" (vigencia general) — no lo reemplaza.
- **Checklist visual**: la excepción NO exime del resto de la revisión de marca (§4.1
  CLAUDE.md) — todo lo demás de la slide y del deck sigue en paleta oficial. Si un futuro
  QA ve rojo/rosado en cualquier otro elemento que no sea este badge de descuento, es un bug,
  no una extensión de esta excepción.
- Implementación completa (HTML/CSS + las 3 variantes de cotización): `plantillas/
  propuesta-comercial.md` → *Propuesta Económica — descuento urgente, ROI y garantía*.

---

## 3. Tipografía oficial

**Familia única**: **Graphit** (sans-serif).

| Uso | Familia | Peso | Notas |
|---|---|---|---|
| Títulos / encabezados | **Graphit Bold** | 700 | Mayúsculas o capitalización dependiendo del nivel |
| Cuerpo / párrafos | **Graphit Regular** | 400 | Interlineado 1.4–1.5 |
| Énfasis dentro del cuerpo | **Graphit Bold** | 700 | Para resaltar términos clave |
| Citas / legales | **Graphit Regular** | 400 | Tamaño reducido |

### Reglas de uso

- **Sans-serif siempre**. Lettering "sharp", limpio, geométrico.
- **Sin serifas, sin script, sin display fuentes decorativas**.
- **Jerarquía clara** por tamaño y peso, no por colores caprichosos.
- **Mayúsculas** ok en títulos cortos para reforzar el carácter premium/tech; nunca en párrafos completos.

### CSS sugerido

```css
:root {
  --font-display: "Graphit Bold", "Graphit", system-ui, -apple-system, sans-serif;
  --font-body: "Graphit Regular", "Graphit", system-ui, -apple-system, sans-serif;
}

h1, h2, h3 { font-family: var(--font-display); font-weight: 700; }
body, p, li { font-family: var(--font-body); font-weight: 400; line-height: 1.45; }
```

### Fallback si Graphit no está disponible

Si en el entorno de generación (HTML local del cliente, web) Graphit no está instalada o no se puede embeber, usar como fallback **Inter** o **Poppins** (sans-serif geométrica). **Nunca** Times, Georgia ni similares serif.

---

## 4. Estilo gráfico

- **Formas**: geométricas, bordes nítidos. Rectángulos, líneas, ángulos.
- **Composición**: minimalista. Mucho aire negativo. Sin elementos decorativos sin función.
- **Estética general**: corporativa, premium, tech-focused, energética.
- **Iconografía**: line icons o filled de un único peso. Coherentes entre sí.
- **Imágenes**: si se usan fotos, preferir alto contraste y composición geométrica que dialogue con la paleta cálida.

---

## 5. Aplicación en propuestas (slides HTML)

Toda slide de `clientes/<slug>/propuesta/` cumple:

1. **Logo Intezia** (división correcta, variante por contraste).
2. **Fondo** dentro de la paleta oficial (negro dominante, blanco para slides de detalle).
3. **Texto** en Graphit Bold (títulos) + Graphit Regular (cuerpo).
4. **Acentos** en `--intezia-yellow` o `--intezia-orange`.
5. **Sin colores fuera de la paleta** salvo logos de aliados (que mantienen su identidad propia).

Si el sistema de tipografía no puede cargar Graphit, **avisar** al usuario y usar el fallback. **No proceder en silencio** con una fuente desalineada.

---

## Notas para Claude

- Si vas a generar slides → carga este archivo y aplica los tokens. **No inventes colores ni fuentes.**
- Si una propuesta sale con colores ajenos a esta paleta o fuente distinta a Graphit → está mal y hay que rehacerla.
- Si el usuario pide un color "fuera de marca" para un caso puntual, **propón una alternativa dentro de la paleta** antes de aceptar.
- Cualquier ajuste a esta marca en el futuro **se registra aquí y en `aprendizajes.md`**.
