# Ficha de capacidad de cajas

> Cuánto contenido cabe **legible** en cada caja del deck antes de desbordar (CLAUDE.md §4.10).
> Sirve para **acotar las preguntas de contenido** al armar una propuesta: pide la cantidad
> que cabe, en vez de recibir contenido sin límite y luego pelear con el desborde.
>
> **Autoridad final = el detector.** Estos números son la guía para preguntar bien; la
> verdad la dicta `node scripts/verificar-overflow.js <slug>`. Si el detector da 0, cabe.
> Si reporta desborde, ajusta el contenido (no el diseño).

## Cómo usar esta ficha
1. Al recolectar contenido, **pide dentro del rango** ("dame 4 a 6 objetivos", "máx 5 puntos
   de diagnóstico de 3-4 líneas cada uno").
2. Si el cliente trae más de lo que cabe, **resume o reparte** (no encojas el diseño): es una
   decisión de contenido, que el usuario responde.
3. Antes de entregar, corre el detector. Cero desbordes = listo.

## Capacidades por caja

| Slide / caja | Selector | Capacidad legible | Notas |
|---|---|---|---|
| Programa · módulos | `.s-program .modules` | 3 a 6 módulos | 5-6 activan modo compacto automático (fuentes/padding reducidos) |
| Programa · temas por módulo | `.s-program .topics li` | hasta 7 temas (3 módulos) · ~5 (4 módulos) | a más módulos, menos temas por módulo. Chip de tema ≤ 28 chars. **El chip ya NO trunca con «…» (envuelve); si no cabe, acórtalo. Prohibido `nowrap`+`ellipsis` (§4.10.5)** |
| Diagnóstico | `.s-pain ol` | máx 5 puntos | 3-4 líneas por punto; mantener longitud pareja entre puntos (§4.10) |
| Objetivos específicos | `.s-goals .specifics ol` | 3 a 4 | objetivo general aparte, 1 párrafo |
| Cronograma · temas (chips) | `.s-schedule .chips` | 4 a 5 chips | una línea por chip, sin truncar |
| Cronograma · estrategias/recursos | `.s-schedule .ses-cols ul` | 3 a 5 ítems por columna | 3 columnas; ítems cortos de una línea |
| Beneficios · perfil de egreso | `.s-benefits .block ul` | 3 (saber / saber hacer / saber ser) | estructura fija |
| Impacto · barras | `.s-impact .bars` | 3 a 5 barras | cada cifra de estudio real con fuente citada (§4.9) |
| Impacto · chips | `.s-impact .gauge-panel .chips` | 1 a 3 | número + label corto |
| Entregables (AcroForm) | `.entregables-box` | 8 a 9 líneas visuales | destacados en líneas cortas de un renglón |
| Próximos pasos · body | `.acro-paso-NN-body` | ≤ ~130 chars (≈5 líneas) | más largo se corta en el PDF sin click |
| Equipo facilitador | `.s-benefits .team .members` | 2 a 3 personas | foto + nombre + rol + 1 línea |

## Slides multi-fase (deck pilotes-perforados)
| Slide / caja | Selector | Capacidad legible | Notas |
|---|---|---|---|
| Roadmap · fases | `.s-roadmap` | 3 a 5 fases | cada fase con título corto + meta de 1-2 líneas |
| Mapa de calor · filas | `.s-heatmap .hm-wrap` | ~7-8 filas | tabla de tamaño fijo; filas extra se recortan abajo (ver pendiente abajo) |

> **Pendiente conocido (2026-05-23):** la slide Mapa de Calor de pilotes-perforados desborda
> ~44px (la última fila se recorta). Detectado por `verificar-overflow.js`. Pendiente de fix
> de contenido (quitar 1 fila o repartir) cuando se retome ese deck.
