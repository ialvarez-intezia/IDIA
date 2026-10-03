# Plantilla: Brief de Kickoff (hoja de ruta del servicio)

> Herramienta **de cara al cliente**, distinta del deck de propuesta, que la líder de
> proyectos y el consultor navegan **en vivo** durante el kickoff (primer encuentro del
> equipo de servicio con el cliente, ya cerrada la venta). No confundir con el `brief.md`
> interno de cada carpeta (ficha de trabajo del sistema). Acompaña al deck de propuesta,
> no lo reemplaza. Origen: reunión con Keiber Quintana (CPO), 2026-08-26; formato definido
> por Ivana con ejemplo de referencia ("Gato"), 2026-08-30.
>
> **Formato: archivo HTML local autocontenido**, no un PDF de propuesta ni un Artifact
> publicado en claude.ai. Vive en `clientes/propuestas/<slug>/kickoff.html`, se abre
> directamente en el navegador (doble clic / `file://`). Genera su propio PDF al cerrar la
> sesión (impresión del navegador) y un `.ics` para agendar. Ver §3.
>
> **CANÓNICO**: `plantillas/kickoff-canonico/kickoff.html` (servicio Habilidades, cliente
> demo "Gato" — único piloto construido hasta ahora, ver §5).
> **MARCA**: `empresa/marca-artefactos.md` — paleta y tipografía distintas de las de
> propuesta (`marca-visual.md`). No mezclar los dos sistemas.

---

## 0. Historial de esta plantilla (para no repetir el error)

La primera versión (2026-08-26) se construyó como deck A4 landscape con la paleta oficial de
propuesta, pensado para publicarse como Artifact de claude.ai. El usuario la rechazó dos
veces:
1. *"No me gustó generarla como propuesta, la idea es que se pueda ir rellenando de forma
   interactiva."* → se reconstruyó como Artifact interactivo (negro/blanco/amarillo/naranja
   puro, campos en vivo solo en Logística).
2. *"El diseño sea muy parecido al de mis artefactos comerciales... en blanco y negro no se
   ve."* Con un ejemplo completo (Gato) que usa un patrón totalmente distinto: **archivo
   HTML local** (no Artifact publicado), paleta cálida (`empresa/marca-artefactos.md`),
   sesiones con fecha/hora editables, exportación a `.ics`, PDF vía impresión del navegador,
   y un toggle "Modo interno / Modo cliente".

Esta es la versión vigente. No volver a la de Artifact/paleta oficial salvo instrucción
explícita nueva.

---

## 1. Regla bloqueante — propuesta aprobada antes de generar

1. **Antes de generar el brief de un cliente, pregunta al usuario si la propuesta está
   aprobada.** Sin confirmación explícita → **no generes el brief**. (Confirmado de nuevo
   2026-08-30: no se genera junto con la propuesta por defecto, sigue siendo un paso aparte
   gateado por la aprobación.)
2. Si la propuesta tenía varios caminos de cotización, **pregunta cuál camino aprobó el
   cliente** — determina qué etapas entran en la ruta.
3. La aprobación la da **el usuario** (Ivana), no se infiere del `meta.json`.

---

## 2. Fuentes de verdad (leer antes de generar — §4.14)

| Fuente | Qué aporta |
|---|---|
| `clientes/propuestas/<slug>/index.html` (propuesta aprobada) | Código, cliente, división, servicio (§4.1a), eje temático |
| `clientes/propuestas/<slug>/programa.md` | Etapas reales, número de sesiones por etapa, entregables |
| `clientes/propuestas/<slug>/brief.md` (interno) | Contacto, asesora comercial, área priorizada |

El **número exacto de sesiones** de cada etapa sale de `programa.md`/`brief.md` del cliente
específico — el brief de kickoff no tiene número fijo de sesiones, igual que el deck de
propuesta no tiene número fijo de slides.

---

## 3. Mecánica técnica (no rediseñar — reutilizar tal cual del canónico)

| Pieza | Cómo funciona |
|---|---|
| **Modo interno / Modo cliente** | Botón en la topbar alterna `body.classList('cliente')`. Todo texto dirigido al consultor (qué decir, qué confirmar) lleva `class="interno"` y se oculta en modo cliente antes de compartir pantalla. |
| **Fecha/hora por sesión** | `<input type="date">` / `<input type="time">` reales dentro de cada `.scard[data-session]`, con `data-title` y `data-desc` para el `.ics`. |
| **Numeración de sesiones** (estándar desde 2026-09-28) | `.sc-no` es un número grande (`1`, `2`, `3`…) **corrido a través de todas las etapas con sesiones** — no reinicia por etapa. Sin `<h4>` de título temático dentro de `.scard`: el tema de la sesión va como primera frase (en negrita) de `.sc-desc`, o se omite si el tema ya es evidente. Los check-ins de Seguimiento (30-60-90) son la excepción: mantienen `.sc-no` = "Check-in" en vez de número, porque no son sesiones de trabajo secuencial — `filaSesiones()` en el JS ya distingue ambos casos (antepone "Sesión " solo si `.sc-no` es puramente numérico). |
| **Agendar todo (`.ics`)** | JS puro arma un único `.ics` con `Blob`+`URL.createObjectURL` a partir de todas las `[data-session]` con fecha llena, y lo descarga. Se importa **a mano, una sola vez**, al calendario de `servicio@intezia.com`. Sin backend, sin autenticación embebida — eso sería la integración MCP de `plantillas/calendario.md`, un paso aparte que la página no intenta hacer sola. |
| **Generar PDF** | Botón arma un `#print-view` oculto (visible solo en `@media print`, generado dinámicamente con lo llenado en vivo) y dispara `window.print()`. El usuario elige "Guardar como PDF". |
| **Entregables en línea de tiempo** | `.deliv`/`.drow`, asociados a la etapa que los produce — nunca una lista plana al final. |
| **Sin persistencia** | Todo vive en el DOM de esa sesión del navegador. Es una herramienta de una sola sesión de trabajo. |

Detalle completo de tokens/componentes: `empresa/marca-artefactos.md`.

---

## 4. Estructura de contenido

1. **Topbar**: logo genérico de Intezia + pills (cliente, servicio, fecha de kick-off) + botón de modo.
2. **Encabezado** (hero): kicker, `h1` con cliente y servicio, sub `interno` explicando el instrumento.
3. **Callout `interno`**: de dónde sale la información (Ficha Comercial del cliente, área priorizada, eje temático, asesora comercial).
4. **Sin sección de objetivos** (decisión 2026-08-30): se arranca directo del encabezado a la ruta. El objetivo general/específicos ya vive en la propuesta; repetirlo aquí es redundante para una herramienta que se usa hablando, no leyendo.
5. **La ruta**: TODAS las etapas del servicio contratado, cada una en una `.stage` con nombre + una frase de qué implica. La etapa de hoy lleva `.now` + badge "Hoy"; una etapa sin sesión con el cliente lleva `.auto` + badge "Automático".
6. **Por cada etapa con sesiones**: un `.sect-head` + grid de `.scard` (una por sesión) con fecha/hora editables.
7. **Botón "Agendar todo"** después de la última etapa con sesiones.
8. **Entregables en línea de tiempo**, asociados a su etapa.
9. **Cierre**: "Generar PDF" + "Agendar todo" (duplicado, conveniencia).
10. **Footer**: Dirección de Productos y Servicios · Intezia C.A. · J-505657950 · `servicio@intezia.com` (nunca `info@intezia.com`).

---

## 5. Adaptación por servicio — las 4 rutas reales

Todo servicio abre con **Kick-off (Etapa 1)**: sesión de 30-60 minutos donde se presenta la
ruta completa y se agendan ahí mismo las fechas y logística de **todos** los encuentros del
servicio. El brief nace sabiendo la ruta completa porque todo se cierra en esa sesión.

| Servicio | Ruta (etapas) | Casillas de horario | Estado |
|---|---|---|---|
| **Detección** | Kick-off (Acta + Cronograma) → Auditoría (1 sesión de 45-60' por área, Guión A.E.V.C., cada una cierra con un quick win) → Diagnóstico (Matriz de Madurez + Protocolo de Clasificación de IA, **sin sesión con el cliente**) → Diseño (sesión ejecutiva de cierre, 60-90') | Una por sesión de área + la sesión de cierre | Sin piloto propio — construir caso por caso siguiendo esta tabla, adaptando el canónico de Habilidades |
| **Habilidades** | Kick-off → Capacitación sobre tareas reales (1 sesión por módulo/área, hasta 2h o más) → Cierre y medición (**automático**, 72h, sin sesión) → Seguimiento 30-60-90 (3 check-ins: 30d uso, 60d nuevas construcciones, 90d tiempo/productividad — detalle en `empresa/tipos-de-documento.md §0.2`) | Una por sesión de capacitación + una por check-in | **Vigente** — piloto: `plantillas/kickoff-canonico/kickoff.html` (cliente demo Gato) |
| **Políticas** | Kick-off → Diagnóstico de madurez por área (1 sesión por dirección) → Cuestionario dirigido por hallazgos (sin sesión) → Redacción y validación (sesión de validación con responsables de área + aprobación del comité de gobernanza) | Una por sesión de diagnóstico + la sesión de validación | Sin piloto propio — construir caso por caso |
| **Innovación** | Kick-off (aplica la primera Matriz de Madurez como línea base) → Ciclo mensual (1 sesión/mes rotando charla / masterclass / actualización — tantas casillas como meses tenga el ciclo: 3, 6 o 12) → Evaluación recurrente de madurez (cada 3 meses, **coincide** con una sesión mensual, no es una etapa aparte) | Una por cada sesión mensual del ciclo | Sin piloto propio — construir caso por caso |
| **Integral** | Combina las 4 rutas de arriba como fases secuenciales | — | No cubierto todavía — mismo estado que su deck de propuesta (`CLAUDE.md §4.1b`) |

**Sin piloto propio** = mismo criterio que el resto del sistema aplica a Detección/Políticas
en sus decks de propuesta (`CLAUDE.md §4.1a`): no hay un HTML construido para clonar todavía,
pero la estructura (mecánica de §3 + tabla de arriba) ya está definida. Al llegar el primer
caso real de alguno de estos tres servicios, se adapta el canónico de Habilidades a esta ruta
y **ese** se vuelve el piloto de referencia — no se construye de cero.

### Entregables por servicio

**No inventar una lista de entregables nueva.** Los entregables tangibles de cada servicio
ya están definidos en el manual del consultor correspondiente (fuente que este repo no tiene
cargada todavía). Para Habilidades, el canónico ya los toma correctamente (plan y cronograma
en el kick-off, workbook en cada sesión, certificados y dashboard 72h después del cierre,
reporte de adopción en cada check-in). Para Detección/Políticas/Innovación: **pedir la lista
real al usuario o al manual del consultor antes de escribir la sección de entregables** — no
completar con una lista genérica ni con suposiciones.

---

## 6. Marca y copy

- **Paleta y tipografía**: `empresa/marca-artefactos.md` — NO la paleta oficial de propuesta.
- **Logo**: genérico de Intezia (`logos/intezia/{BLANCO,NEGRO}.png`), sin sufijo de división.
- **Correo**: `servicio@intezia.com` en footer, `.ics` y toasts — nunca `info@intezia.com`.
- **Idioma español, sin Spanglish** (§4.4 de `CLAUDE.md`). Nunca «cohort/cohorts» → «grupos».
- **Sin guion largo `—`** como separador (§4.13) en todo texto visible (no en comentarios internos del `.html`, esos no los ve nadie fuera del equipo).
- **Sin acuerdos económicos** en el brief (§4.15): esta herramienta es logística y narrativa de la ruta, no cierre comercial.

---

## 7. Flujo de generación (clon del canónico)

```bash
# 0) Confirmar con el usuario que la propuesta del cliente está APROBADA (§1, bloqueante).
#    Si tenía varios caminos de cotización, confirmar cuál se aprobó.

# 1) Leer (§4.14): index.html + programa.md + brief.md del cliente, y este spec.

# 2) Clonar el canónico:
cp plantillas/kickoff-canonico/kickoff.html clientes/propuestas/<slug>/kickoff.html

# 3) Ajustar la profundidad de los logos: el canónico usa "../../logos/..." (vive en
#    plantillas/kickoff-canonico/); en clientes/propuestas/<slug>/ es "../../../logos/..."
#    (3 niveles) — un solo find/replace.

# 4) Editar: cliente, servicio, eje temático, la ruta COMPLETA de etapas del servicio
#    contratado (tabla §5), las sesiones de cada etapa que tenga (título + descripción +
#    casillas VACÍAS de fecha/hora — no inventar fechas), y los entregables en línea de
#    tiempo (§5, no inventar la lista).

# 5) Abrir el archivo en el navegador y revisar visualmente: sin overflow horizontal,
#    todas las etapas y sesiones legibles, "Modo cliente" oculta correctamente todo lo
#    marcado interno.

# 6) Durante el kickoff real: el consultor llena fecha/hora en vivo, usa "Agendar todo"
#    para el .ics (importar a mano a servicio@intezia.com) y "Generar PDF" al cerrar.
```

No hay paso de "resolver logos" ni build intermedio: los `<img>` usan rutas relativas
normales porque el archivo se abre localmente desde dentro del repo (igual que `index.html`
de cualquier propuesta) — no es un Artifact con CSP que bloquee rutas del filesystem.

---

## 8. Checklist pre-entrega

- [ ] **Propuesta aprobada confirmada por el usuario** (§1), incluyendo el camino si la propuesta era multi-camino
- [ ] Paleta y tipografía de `empresa/marca-artefactos.md` (no la de propuesta)
- [ ] Logo genérico de Intezia, sin división, blanco en topbar / negro en `#print-view`
- [ ] Sin sección de objetivos — arranca directo en la ruta
- [ ] Ruta completa: todas las etapas del servicio contratado, con nombre + frase de qué implica cada una
- [ ] Etapas sin sesión con el cliente marcadas `.auto` (badge "Automático"), no con casillas vacías sin explicación
- [ ] Casillas de fecha/hora **vacías** en cada sesión (no inventar fechas ni "a confirmar" como placeholder)
- [ ] Sesiones numeradas de forma corrida (`1, 2, 3…` en `.sc-no`, sin reiniciar por etapa) y sin `<h4>` de título temático dentro de `.scard` (§3)
- [ ] Entregables en línea de tiempo, asociados a su etapa, tomados de una fuente real (no inventados)
- [ ] Todo texto dirigido al consultor lleva `class="interno"` (probar el toggle "Modo cliente")
- [ ] Footer y `.ics` con `servicio@intezia.com`, cero ocurrencias de `info@intezia.com`
- [ ] `grep -nE "—|–"` en el `.html` = 0 fuera de comentarios internos
- [ ] Botón "Agendar todo" probado con al menos una fecha llena (no revienta si no hay ninguna)
- [ ] Botón "Generar PDF" probado: el `#print-view` se arma con lo llenado y `window.print()` abre el diálogo
- [ ] Sin overflow horizontal en el ancho de ventana habitual del equipo (laptop, no celular — esta herramienta se usa en la llamada, no en el bolsillo)
