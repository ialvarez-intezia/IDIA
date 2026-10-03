# Biblioteca de bloques de slide

Bloques reutilizables para **componer** un deck o **agregar una slide a la medida** para un
cliente especial, sin parchear a mano y sin romper el diseño.

## Cómo funciona el sistema de CSS
- El núcleo visual vive en `clientes/propuestas/_base/styles.css` (compartido). Cada deck lo
  enlaza por ruta relativa: `<link rel="stylesheet" href="../_base/styles.css">`.
- Lo propio de un deck (un bloque add-on, un retoque) va en un `overrides.css` local,
  enlazado **después** del base: `<link rel="stylesheet" href="overrides.css">`.
- Así un clon no copia ~1.840 líneas de CSS: hereda el base y solo lleva sus diferencias.

## Slides estándar (ya vienen en cada clon)
La mayoría de propuestas se clonan de un deck canónico, así que estas slides ya están:

| Slide | Clase | Deck fuente para copiar |
|---|---|---|
| Portada | `s-cover` | cumbre-andina |
| Dolor + Diagnóstico | `s-pain` | cumbre-andina |
| Objetivos | `s-goals` | cumbre-andina |
| Programa | `s-program` | cumbre-andina |
| Cronograma / sesión | `s-schedule` | cumbre-andina |
| Metodología ABR | `s-orange` | cumbre-andina |
| Beneficios | `s-benefits` | cumbre-andina |
| Impacto | `s-impact` | cumbre-andina |
| Propuesta económica | `s-price` | cumbre-andina |
| Próximos pasos | `s-steps` | cumbre-andina |
| Cierre | `s-end` | cumbre-andina |

> Para copiar una de estas, toma el `<section>` correspondiente del `index.html` de
> cumbre-andina. Su CSS ya está en el base: no requiere overrides.

## Bloques add-on (para clientes especiales)
Slides que NO vienen en el deck mono-fase estándar. Cada una trae su HTML y su CSS:

| Bloque | HTML | CSS a copiar en overrides.css |
|---|---|---|
| Roadmap multi-fase (`s-roadmap`) | `roadmap.html` | `roadmap.css` |
| Mapa de Calor (`s-heatmap`) | `mapa-de-calor.html` | `mapa-de-calor.css` |

Sus selectores (`.rmx-*`, `.hm-*`) no existen en el base, así que se añaden sin conflicto.

## Procedimiento para agregar una slide o paso
1. **Pega el `<section>`** del bloque en `index.html`, en la posición deseada.
2. **Copia el CSS** del bloque (`<bloque>.css`) al `overrides.css` de la propuesta y
   asegúrate de que el deck enlaza `overrides.css` tras `../_base/styles.css`.
3. **Renumera los contadores.** Cada slide tiene `<span class="counter">NN / TOTAL</span>`.
   Al insertar o quitar una slide cambia el TOTAL en todas y el NN de las siguientes.
4. **Certifica con el detector** (no revises a ojo):
   ```bash
   node scripts/verificar-overflow.js <slug>
   ```
   0 desbordes = la slide cabe. Si reporta desborde, ajusta el **contenido** según
   `plantillas/capacidad-cajas.md` (no el diseño).

## Crear un bloque totalmente nuevo
Si ningún bloque sirve, crea un `<section class="slide s-<nombre>">` con su estilo en
`overrides.css` (usa solo la paleta de marca, §4.1). El detector lo cubre igual que a los
demás. Si será reutilizable, extráelo aquí como nuevo bloque + su `.css`.
