# Rediseño · Catálogo de Talleres Intezia 2026

> Spec de diseño. Fecha: 2026-05-17. Estado: aprobado por el usuario apartado por apartado vía companion visual.

## 1. Contexto y objetivo

El catálogo de talleres vive en `clientes/propuestas/catalogo/Catalogo Talleres 2026/`
(`index.html` + `styles.css` + PDF). Es un deck institucional de 28 slides que ventas
usa en reuniones, normalmente **compartido en un televisor**.

**Objetivo:** rediseñar el catálogo para que se vea novedoso, tecnológico y muy claro,
con elementos de tamaño grande (legibles a distancia en TV), y añadir dos elementos
interactivos: un botón de video por taller y un botón "aplica aquí" por taller.

**El contenido NO cambia.** Cada taller conserva su desglose completo (módulos con
numeral, título, objetivo y temas) exactamente como en el catálogo actual. Solo cambia
el diseño y se añaden los botones.

## 2. Alcance

### Se rediseñan (7 apartados)

1. Portada
2. Separadora de sección (apartado nuevo — ver §4)
3. Manifiesto
4. Slide de programa (×20 talleres)
5. Rutas Diamond
6. Conclusión
7. CTA de cierre

### Se mantienen intactas (3 slides imagen importadas)

- **Detrás de la empresa** — `_assets-paginas-viejas/pagina-02.png` (foto de Alejandro
  Moreno y Jean Iovino).
- **La rueda / Áreas Intezia** — `_assets-paginas-viejas/pagina-03.png` (rueda central
  INTEZIA: Consultoría · Educación · Evento · Fundación · Desarrollo).
- **Ecosistema de Confianza** — `_assets-paginas-viejas/pagina-05.png` (logos de clientes).

Estas tres slides siguen siendo `<section class="slide s-img-page">` sin cambios.

## 3. Sistema de diseño — lenguaje "HUD Tecnológico"

Dirección visual elegida entre tres opciones (HUD · Editorial Bento · Cinético).
Estética de **panel de control / interfaz de software de vanguardia**, dentro de la
marca canónica de Intezia (`empresa/marca-visual.md`) — sin colores ni fuentes nuevas.

| Elemento | Definición |
|---|---|
| Paleta | Solo `#000000`, `#F4BA1A`, `#E58423`, `#FFFFFF` (canónica, sin excepción) |
| Tipografía | Graphit Bold / Regular. Fallback Inter/Poppins. Etiquetas técnicas en monoespaciada del sistema (`ui-monospace`) |
| Fondo | Negro `#050505` con **rejilla técnica** sutil amarilla (líneas a baja opacidad) |
| Marco | **Brackets en las 4 esquinas** (líneas amarillas en ángulo) en cada slide rediseñada |
| Eyebrow | Etiqueta monoespaciada amarilla en mayúsculas (código + sección + nivel) |
| Contador | `NN / 33` monoespaciado, gris, esquina superior derecha |
| Acentos | Amarillo dominante; naranja como secundario/alterno |
| Logo | Logo Intezia Educación (división `educacion`) en portada y CTA; footer en cada slide según el patrón actual |

Las unidades se expresan en `cqw` (container query width) para que todo escale con el
tamaño de la slide. Formato de slide: **A4 landscape** (ratio 1.414:1), igual que hoy.

## 4. Especificación por apartado

### 4.1 Portada
Logo Intezia Educación · eyebrow "Catálogo de Capacitaciones · Talleres y Programas" ·
título gigante "Catálogo de / talleres 2026" (segunda línea en bloque amarillo sólido,
con interlineado y padding que la separen de la primera) · párrafo lead con las 5
secciones resaltadas · badge institucional inferior ("Consultoría de IA #1 en LATAM" /
"Respaldados por Microsoft for Startups"). Banda diagonal cálida decorativa.

### 4.2 Separadora de sección (×5 — apartado NUEVO)
Abre cada una de las 5 secciones. Número de sección **gigante** a la izquierda
(`01 / 05` en amarillo) + nombre de la sección + descripción breve. A la derecha, la
**lista de talleres de esa sección** con sus códigos `TA-###` en chip amarillo. Sirve
de índice y orienta al ver el catálogo en TV.

### 4.3 Manifiesto
Slide de declaración: H2 amarillo grande ("Bienvenidos a la era de la Inteligencia
Operativa") · párrafos del catálogo actual, en la versión ligeramente condensada
aprobada en el companion (se acorta para dar aire, sin perder el mensaje) · frase de
cierre destacada con borde naranja a la izquierda.

### 4.4 Slide de programa (×20) — apartado central
- Eyebrow monoespaciado: `TA-### · Sección N · <nivel>`.
- Título del taller grande, con palabra clave en amarillo.
- **Botón "Más información"** junto al título — amarillo con glow. **Un único botón por
  taller** (no por módulo); enlaza al video pregrabado que explica todo el taller.
- Módulos en rejilla (2×2 / 3+2 / 3×2 según cantidad). Cada módulo: numeral romano en
  chip amarillo + título + objetivo + lista de temas en 2 columnas con viñeta `▸`.
  Elementos dimensionados para **llenar el recuadro por su propio tamaño** (sin huecos
  por distribución).
- **Banda "Aplica aquí"** inferior, full-width, amarilla — todo el recuadro es el botón
  clicable. Enlaza a la herramienta de aplicación.
- Footer con logo y código del taller (patrón actual).

### 4.5 Rutas Diamond
Producto estrella. H2 grande + subtítulo. Las 3 fases como **bandas horizontales
secuenciales** (no columnas): número de fase gigante a la izquierda (01 · 02 · 03) +
contenido al centro (tag, título, descripción) + resultado en recuadro oscuro a la
derecha. Las 3 bandas llenan la altura de la slide.

### 4.6 Conclusión
Misma familia que el manifiesto: H2 amarillo ("Su traje a la medida") · párrafos del
catálogo actual, en la versión ligeramente condensada aprobada en el companion · cita
final ("La tecnología es la herramienta. Su equipo es la clave. Intezia es el puente.")
en grande, naranja, itálica, con borde.

### 4.7 CTA de cierre
Logo · mensaje grande ("Rellena el formulario y empieza a ver cambios en tu empresa" —
"formulario" en amarillo, "cambios" en naranja) · botón **"Aplica Aquí"** prominente
(sombra dura naranja + glow) · footer institucional. El botón enlaza a la herramienta
(mismo destino que los botones "Aplica aquí" de cada taller).

## 5. Estructura del deck — 28 → 33 slides

Se mantiene el orden; se insertan 5 separadoras de sección.

| # | Slide | Acción |
|---|---|---|
| 1 | Portada | rediseño |
| 2 | Detrás de la empresa (img) | intacta |
| 3 | La rueda · Áreas Intezia (img) | intacta |
| 4 | Manifiesto | rediseño |
| 5 | Ecosistema de Confianza (img) | intacta |
| 6 | Separadora · Sección 1 · Cultura y Estrategia | nueva |
| 7–11 | TA-003, TA-017, TA-004, TA-001, TA-019 | rediseño |
| 12 | Separadora · Sección 2 · Especialización Funcional | nueva |
| 13–21 | TA-005, TA-006, TA-007, TA-008, TA-009, TA-010, TA-011, TA-013, TA-002 | rediseño |
| 22 | Separadora · Sección 3 · Claude Deep-Dive | nueva |
| 23–24 | TA-016, TA-018 | rediseño |
| 25 | Separadora · Sección 4 · Stack Microsoft | nueva |
| 26 | TA-020 | rediseño |
| 27 | Separadora · Sección 5 · Bootcamps Técnicos | nueva |
| 28–30 | TA-012, TA-014, TA-015 | rediseño |
| 31 | Rutas Diamond | rediseño |
| 32 | Conclusión | rediseño |
| 33 | CTA de cierre | rediseño |

Todos los contadores pasan de `NN / 28` a `NN / 33`.

## 6. Elementos interactivos

| Botón | Cantidad | Destino | Estado |
|---|---|---|---|
| "Más información" (video) | 1 por taller = 20 | Video pregrabado del taller (URL única por taller) | **URLs pendientes** — el usuario las suministrará |
| "Aplica aquí" (taller) | 1 por taller = 20 | Herramienta de aplicación (URL única, igual para todos) | **URL pendiente** — herramienta aún no definida |
| "Aplica Aquí" (CTA cierre) | 1 | Misma herramienta de aplicación | **URL pendiente** |

Implementación: cada botón es un `<a href>`. Hasta tener las URLs, el `href` apunta a
un placeholder (`#`) y cada `<a>` lleva un identificador claro (p. ej. `data-taller="TA-008"`)
para que actualizar las URLs sea solo sustituir valores. Chrome headless `--print-to-pdf`
conserva los `<a href>` como hipervínculos reales, por lo que los botones funcionan al
hacer clic dentro del PDF final.

## 7. Generación del PDF

Se mantiene el flujo HTML → PDF con Chrome headless (`--print-to-pdf`, sin header/footer).
El PDF resultante conserva los hipervínculos. El catálogo **no usa AcroForms** (no lleva
campo de precio); no aplica `agregar-campo-precio.py`.

## 8. Forma de trabajo en implementación

- Se edita `index.html` + `styles.css` del catálogo de talleres **en sitio**.
- Cada apartado se construye y se revisa en el **servidor local** con el deck real
  antes de aprobarlo (flujo paso a paso solicitado por el usuario).
- El diseño aprobado en el companion visual es la referencia; el deck real usa la
  marca canónica completa (logos PNG reales, fuente Graphit).

## 9. Pendientes (no bloquean el rediseño visual)

1. **20 URLs de video** — una por taller.
2. **URL de la herramienta de aplicación** — una, compartida por todos los botones
   "Aplica aquí" y el CTA de cierre.

El rediseño se construye con placeholders; cuando lleguen las URLs es solo actualizar.

## 10. Cumplimiento de reglas del sistema (`CLAUDE.md`)

- §4.1 Marca visual: división `educacion`, paleta canónica, Graphit, logo en portada y
  cada slide. ✔
- §4.4 Idioma: todo en español; términos nativos de herramientas se mantienen. ✔
- §4.8 Resaltado de palabras clave en el cuerpo con `<strong>`/negrita: se respeta el
  contenido actual, que ya trae sus resaltados.
- §8: `clientes/<slug>/` no requiere confirmación adicional; el usuario inició el trabajo.
