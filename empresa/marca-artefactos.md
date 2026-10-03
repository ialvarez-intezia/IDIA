# Marca visual — Artefactos comerciales (herramientas de trabajo en vivo)

> Segundo sistema de marca de Intezia, **distinto** del oficial para decks de propuesta
> (`empresa/marca-visual.md`: negro/blanco/amarillo/naranja puro + Graphit). Este archivo
> aplica a la familia de **artefactos comerciales**: herramientas HTML locales que el equipo
> usa en vivo frente al cliente para narrar, agendar y cerrar (no documentos ya cerrados que
> se presentan). Origen: "Ficha Comercial", "Resumen modelo", "Ruta del servicio" y el
> **Brief de Kickoff** (`plantillas/kickoff-canonico/`), 2026-08-30.

---

## 1. Por qué un sistema aparte

Un deck de propuesta es un documento **ya cerrado** que se le presenta al cliente: la paleta
oficial pura negro/blanco/amarillo/naranja y Graphit comunican esa formalidad. Un artefacto
comercial es distinto: es una **herramienta de trabajo** que el consultor abre en vivo,
mientras conversa con el cliente, para narrar una ruta y llenar datos en el momento. Necesita
verse cálido y utilitario, no como una pieza de imprenta.

> Ver también `[[artifact-vs-pdf-para-vivo]]` en memoria — la distinción de fondo (documento
> cerrado vs. herramienta que se llena en vivo) es la misma; este archivo fija los tokens
> concretos para el segundo caso.

## 2. Paleta

| Token | Uso | Hex |
|---|---|---|
| `--black` | Fondo base | `#0A0A0A` |
| `--panel` | Superficie de card | `#1c1a16` |
| `--panel-2` | Superficie de card secundaria (rutas, headers de sesión) | `#141310` |
| `--line` | Bordes sutiles | `#2c2922` |
| `--gold` | Acento primario (CTA, etapa activa, hitos) | `#F4BA1A` |
| `--orange` | Acento secundario (tags, hover) | `#E58423` |
| `--cream` | Texto principal sobre fondo oscuro | `#F5EFE0` |
| `--dim` | Texto secundario / atenuado | `#9a948a` |
| `--ok` | Estado positivo (uso puntual, no es el acento) | `#43d76a` |
| `--bad` | Estado negativo (uso puntual, no es el acento) | `#E8634A` |

No mezclar con la paleta oficial pura (`#000000`/`#FFFFFF`) de `marca-visual.md` — un
artefacto comercial en blanco y negro puro "no se ve" (feedback directo del usuario,
2026-08-30): el cream y el dim son los que le dan calidez y jerarquía tipográfica.

## 3. Tipografía

- **Poppins** (400/500/600/800) — texto general, títulos, botones.
- **Space Grotesk** (500/700) — cifras, etiquetas en mayúscula, datos (`.mono`), inputs de
  fecha/hora.
- Ambas por Google Fonts CDN (`fonts.googleapis.com`), con `preconnect`. Esto es válido
  porque estos artefactos son **archivos locales abiertos directamente en el navegador**
  (`file://`), no Artifacts publicados en claude.ai — no aplica el CSP que bloquea fuentes
  externas ahí. Si algún día un artefacto de esta familia se publica como Artifact, hay que
  volver a un stack de fuentes del sistema (ver `[[artifact-vs-pdf-para-vivo]]`).

```css
:root{
  --black:#0A0A0A; --panel:#1c1a16; --panel-2:#141310; --line:#2c2922;
  --gold:#F4BA1A; --orange:#E58423; --cream:#F5EFE0; --dim:#9a948a;
  --ok:#43d76a; --bad:#E8634A;
  --sans:'Poppins',Arial,'Helvetica Neue',Helvetica,sans-serif;
  --mono:'Space Grotesk','Poppins',Arial,sans-serif;
}
```

## 4. Logo — genérico, sin división

Estos artefactos usan el logo **plano de Intezia** (sin sufijo Fundación/Educación, a
diferencia de los decks de propuesta):

| Variante | Ruta | Uso |
|---|---|---|
| Blanco | `logos/intezia/BLANCO.png` | Fondo oscuro (topbar, header de la app) |
| Negro | `logos/intezia/NEGRO.png` | Fondo claro (`#print-view`, PDF resultante) |

Rutas relativas: desde `clientes/propuestas/<slug>/` son `../../../logos/intezia/...` (3
niveles, igual convención que el resto del sistema); desde `plantillas/kickoff-canonico/` son
`../../logos/intezia/...` (2 niveles).

## 5. Componentes de referencia (ver `plantillas/kickoff-canonico/kickoff.html`)

- **Topbar sticky**: logo + texto de marca a la izquierda, pills de estado (`cliente`,
  `servicio`, `fecha`) + botón de modo a la derecha.
- **Pills** (`.pill`): borde sutil, `.on` para el estado activo (borde naranja).
- **Stage cards** (`.stage`): ruta de etapas, `.now` para la etapa activa (borde dorado +
  degradé sutil), `.auto` para una etapa sin sesión que agendar (badge gris, no dorado).
- **Session cards** (`.scard`): una por sesión, con inputs reales `type="date"`/`type="time"`.
- **Timeline de entregables** (`.deliv`/`.drow`): línea vertical con nodos, no lista plana.
- **Botones** (`.btn` / `.btn.ghost`): dorado sólido para la acción primaria, fantasma para
  la secundaria.
- **Toast** (`.toast`): confirmación no intrusiva, esquina inferior, autodesaparece.

## 6. Mecánica compartida (no rediseñar, reutilizar)

1. **Modo interno / Modo cliente** (`body.cliente .interno { display:none }`): todo texto
   dirigido al consultor (instrucciones de qué decir, qué confirmar) lleva `class="interno"`.
   El botón de la topbar alterna la clase en `<body>`.
2. **`.ics` para agendar**: un único archivo por sesión de trabajo, generado con JS puro
   (`Blob` + `URL.createObjectURL`), sin backend ni autenticación embebida. Se importa a mano
   una vez al calendario de `servicio@intezia.com`.
3. **PDF vía impresión**: un `#print-view` oculto (`display:none`, visible solo en
   `@media print`) se arma en el momento con lo llenado en vivo, y `window.print()` abre el
   diálogo nativo del navegador ("Guardar como PDF").
4. **Sin backend, sin persistencia**: todo vive en el DOM de esa sesión del navegador. Cerrar
   la pestaña sin generar el PDF pierde lo llenado — está bien, es una herramienta de una sola
   sesión de trabajo, no un documento que se retoma después.

## 7. Correo institucional

**`servicio@intezia.com`**, nunca `info@intezia.com`, en toda comunicación de estos
artefactos (footer, `.ics`, toasts). Mismo criterio que el correo de cierre de los decks de
propuesta desde 2026-08-27 (`CLAUDE.md §4.10a`).
