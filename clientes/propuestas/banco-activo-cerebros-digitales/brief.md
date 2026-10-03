# Brief — Banco Activo · Cerebros Digitales para la línea directiva (CAI-027)

## Corrección 2026-10-01 (3ra vuelta) — "TOTAL" sin autocálculo

Instrucción directa del usuario: al escribir el monto de "Obsequio de Intezia" en Adobe, el
campo "TOTAL" no se actualizaba de forma confiable. Causa real: el JS de cálculo de
`agregar-campo-precio.py` (Total = Propuesta+Inversión − Obsequio) solo corre en el motor JS
completo de Adobe Acrobat/Reader — no en Preview de macOS ni en el lector PDF de Chrome, donde
abre el PDF la mayoría de los usuarios. El usuario pidió que el monto final se escriba
directo, sin depender de las otras casillas.

- `scripts/customize-banco-activo-cerebros-digitales.py` ahora busca el campo `PrecioTotal` y
  le quita su `/AA` (acción de cálculo) y su entrada en `/CO` (orden de cálculo) — queda como
  campo de texto plano, igual que "Propuesta + Inversión" y "Obsequio de Intezia".
- Tooltip (`/TU`) actualizado para que quede claro en Adobe: "Total final: escribe el monto
  directamente, ya no se recalcula solo...".
- Verificado con pypdf tras regenerar: `/AA` ausente, `/CO` vacío.
- Correr el trío completo (`generar-pdf.sh` → `customize-acroforms.py` →
  `customize-banco-activo-cerebros-digitales.py`) en cualquier regeneración futura — el
  desenganche del cálculo vive en el script, no en `acroforms.json` ni en el HTML.

## Datos administrativos

- **Empresa**: Banco Activo
- **Sector**: Banca / servicios financieros, entidad regulada
- **Tamaño**: Grande / Enterprise (más de 250 empleados)
- **Slug**: `banco-activo-cerebros-digitales`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades` — construcción de Cerebros Digitales, mismo encuadre
  y misma tarifa que `banco-plaza-cerebros-digitales/` (CAI-025), "Excepción — Cerebros
  Digitales" en `empresa/politicas-comerciales.md`.
- **Tipo de documento**: Capacitación In-Company (`CAI-027`, dado directo por el usuario).
- **Fuente**: Ficha de Levantamiento Banco Activo (Verónica Rubio, elaborada 2026-09-22,
  registrada 2026-09-23) + instrucción directa del usuario (2026-09-24).
- **Base estructural**: clonado de `banco-plaza-cerebros-digitales/` (CAI-025) — plantilla
  ligera ya establecida como patrón reusable para "N Cerebros Digitales, 6h c/u" (ver memoria
  `tarifa-cerebros-digitales-primer-uso-completo`).

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com.
- **Contacto cliente**: Nahir, VP Vicepresidencia de Negocios (persona de la sesión de
  levantamiento). Patrocinador y decisor final de la contratación: Giancarlo, Presidente.
- **Sin nombres ni cargos en el deck**: aunque el grupo de 6 personas ya está identificado
  (a diferencia de CAI-025/Banco Plaza, donde el grupo estaba por designar), el usuario pidió
  explícitamente mantenerlo genérico — se usa el colectivo "línea directiva de Banco Activo",
  sin enumerar VPs por nombre ni por área.

## Dos propuestas en paralelo, mismo levantamiento

El usuario indicó que este levantamiento alimenta **2 propuestas separadas**, construidas una
después de la otra:

- **Propuesta A (esta carpeta, CAI-027)**: Cerebros Digitales en Claude para la línea
  directiva — 5 Vicepresidentes + el Presidente Giancarlo.
- **Propuesta B (`DET-021`, carpeta aparte, pendiente de construir)**: Detección + Fase 1 de
  Habilidades para la Vicepresidencia de Negocios de Nahir (13 gerencias, incluye Adquirencia
  y Medios de Pago bajo su tutela temporal). Foco fuerte de Habilidades en puntos de venta y
  medios de pago (dolor explícito de Nahir: sin visibilidad de facturación, churn ni
  instalaciones pendientes). Posible ampliación a ~3 gerencias adicionales, aún sin decidir,
  a confirmar con lo que arroje la Detección — anotado como algo a considerar en el alcance,
  no como decidido.

## Qué pide el cliente (mensaje directo del usuario, 2026-09-24)

> "Propuesta A — Cerebros Digitales en Claude: Para 5 Vicepresidentes + el Presidente
> Giancarlo. Mismo esquema que hicimos con la línea directiva de Venemergencia: cada uno con
> su cerebro digital entrenado según su rol y forma de decidir."

La Ficha de Levantamiento (Bloque de Universo total de personas, pág. 2) registra el mismo
grupo como "4 Vicepresidentes + el Presidente Giancarlo (5 personas)" — una persona menos que
lo que indicó el usuario. Se preguntó directamente y el usuario confirmó **6 personas** (5
Vicepresidentes + Presidente), no 5. Ver "Decisiones de diseño" abajo.

## Decisiones de diseño (2026-09-24, confirmadas con el usuario vía preguntas directas)

1. **Cantidad de personas — 6, no 5**: pese a que la ficha registra "4 Vicepresidentes +
   Presidente = 5 personas", el usuario confirmó explícitamente 6 (5 Vicepresidentes +
   Presidente Giancarlo) al preguntársele por la discrepancia. **36h totales de propuesta**
   (6 personas × 6h c/u), no 30h.
2. **Genérico, sin roles ni nombres**: aunque la ficha describe el mecanismo como "un cerebro
   digital entrenado según su rol y forma de decidir" (lo que sugeriría nombrar cargos), el
   usuario eligió explícitamente mantenerlo genérico, igual que en Banco Plaza (CAI-025) — el
   deck no enumera qué Vicepresidencia hace qué. La diferencia con CAI-025 es que ahí el grupo
   estaba **por designar** por Presidencia; aquí el grupo **ya está decidido** (es la línea
   directiva completa), así que en vez de "para quienes usted designe" se usa el colectivo
   "línea directiva de Banco Activo" — genérico en cuanto a roles individuales, pero sin
   fingir que la asignación sigue abierta.
3. **Referencia "Venemergencia" — confirmada como la plantilla ligera, no el modelo IESA**:
   el usuario invocó "el mismo esquema que hicimos con la línea directiva de Venemergencia"
   como referencia. La propia ficha, en el Bloque de Habilidades (pág. 4), anota además
   "mismo esquema aplicado a la línea directiva de IESA" — un cliente distinto, con un
   formato de propuesta muy diferente (`propuesta-alianza-bespoke-sin-acroforms`: deck maestro
   de solo negociación, sin AcroForms). Se preguntó directamente al usuario cuál de las dos
   referencias seguir; confirmó la plantilla ligera ya vigente (CAI-025/CAI-023: 6h por
   persona, Projects+Skills+Obsidian, sin Claude Code), **no** el formato bespoke de IESA ni
   el modelo pesado de la Fase 2 de `venemergencia/` (12h/persona, Claude Code).
4. **Horas — 6h por persona, 3 sesiones de 2h**: coincide con la tarifa de "Excepción —
   Cerebros Digitales" y con el dato de la propia ficha (Bloque Habilidades, "Duración y
   frecuencia": "sesiones de 2 horas, 1 a 2 veces por semana, en un programa de 2 a 3 semanas
   — referencia directa al esquema de cerebro digital en Claude").
5. **Sin fase colectiva previa**: cada uno de los 6 líderes va directo a construir su propio
   Cerebro Digital, igual que en CAI-025 — no hay una fase grupal de fundamentos antes.
6. **Sin calendario de inicio con fechas**: la ficha da una fecha de reunión para
   presentar/dimensionar la propuesta (semana del 6 de octubre de 2026, alternativa 29 de
   septiembre) — no fechas de sesión reales. Se omite `.steps-calendar` en vez de inventar
   fechas (regla del sistema, "Omitir, no placeholder").
7. **Sin afirmar migración de stack (§4.11)**: Banco Activo opera dentro de **Google
   Workspace**, con licencias corporativas de Copilot y Gemini (uso mayoritariamente básico
   según la ficha). Claude se suma a ese entorno para este caso puntual, sin afirmar que el
   banco migra o reemplaza su stack.
8. **Con certificado de participación INTEZIA** — Habilidades con capacitación real.
9. **Sensibilidad regulatoria (contexto, no contenido del deck)**: la ficha señala que Banco
   Activo es una entidad bancaria regulada, con preocupación explícita de Nahir por no
   exponer documentos sensibles de clientes (ej. cédulas) a IA en la nube, y sin política
   formal de IA todavía. Esto es más relevante para la Propuesta B (Detección, que sí procesa
   datos operativos de clientes) que para esta Propuesta A (agentes personales ejecutivos);
   se documenta aquí como contexto interno, no se traduce en una slide nueva de esta
   propuesta.
10. **Impacto (§4.9)**: reutiliza las mismas fuentes ya verificadas de la plantilla clonada
    (Stanford HAI AI Index Report 2026, McKinsey The State of AI 2025, Anthropic Economic
    Index 2025) — datos generales de adopción/productividad de IA, válidos para este eje
    temático.

## Entregables (por persona, ×6)

- Cerebro Digital propio: un Project de Claude configurado con su conocimiento.
- Su grafo relacional en Obsidian.
- Una Skill funcional reutilizable.
- Certificado de participación INTEZIA.

## Corrección 2026-09-29 — el grupo real es de 4 personas, no 6

Instrucción directa del usuario: la portada (y el resto del deck) decía 6 Cerebros Digitales,
pero la propuesta real es para **4 personas**. Se corrigió el conteo en todo el documento:

- Portada, Objetivos, Programa, Beneficios (ROI), Propuesta Económica, Próximos pasos y Cierre:
  "6" → "4", "36h" → "24h" (4 personas × 6h c/u).
- Calendario de inicio: se quitaron las filas "Cerebro Digital 5" y "Cerebro Digital 6" (ya no
  aplican con solo 4 tracks); el cierre pasó de 10 de diciembre a 19 de noviembre, y el resumen
  de "9 semanas" bajó a "6 semanas".
- `acroforms.json` (Programa, Notas, Paso01Body) y el script
  `scripts/customize-banco-activo-cerebros-digitales.py` (default de `CierreResultado`)
  actualizados igual.
- **No se inventó una nueva composición por cargo**: la versión anterior documentaba "5
  Vicepresidentes + el Presidente Giancarlo" (confirmado en su momento tras pregunta directa al
  usuario); esta corrección solo cambia el número a 4, sin que el usuario haya indicado los
  nuevos 4 cargos — el deck sigue usando el colectivo genérico "línea directiva de Banco
  Activo" en vez de asumir una composición no confirmada.
- Verificado sin desbordes (`verificar-overflow.js`) tras el cambio, y revisado visualmente el
  PDF regenerado.

## Corrección 2026-10-01 — grupo a 5 personas, slide de Impacto y cotización

Instrucción directa del usuario:

1. **Grupo: 4 → 5 personas.** Sin nueva composición por cargo especificada; se mantiene el
   colectivo genérico "línea directiva de Banco Activo". Horas: 30h de propuesta (5 × 6h, antes
   24h). Actualizado en portada, Objetivos, Programa, Propuesta Económica (Duración + ROI),
   Notas, Paso01 de Próximos pasos, Calendario de inicio (se agregó la fila "Cerebro Digital 5":
   24, 26 nov y 1 dic, cierre en 8 semanas en vez de 6) y Cierre (`CierreResultado`, tanto en
   `index.html` como en el default de `scripts/customize-banco-activo-cerebros-digitales.py`).
2. **Slide de Impacto (10/14): se retiran las gráficas de Stanford HAI/McKinsey.** Primer
   intento (mismo día): apoyar la propuesta en "Banco Activo ya confió antes en Intezia" — dato
   tomado de `../banco-activo-deteccion-negocios/brief.md`, Bloque A de la Ficha de
   Levantamiento. **Corrección, mismo día, 2da vuelta**: el usuario confirmó directamente que
   ese dato es **FALSO** — Intezia nunca ha trabajado con Banco Activo. Se retractó también en
   `banco-activo-deteccion-negocios/brief.md`. Reemplazo final: una referencia anónima real y
   verificada — cliente del sector financiero (procesamiento y adquirencia de medios de pago,
   caso Credicard CAP-041, no se nombra en el deck), Índice de Impacto 86/100 y 91.8% de
   retención medida al cierre (`clientes/dashboards/credicard/resultados.json`, cruzado con
   `clientes/banco-casos-de-exito/index.html`). Se reemplazó `.chart-panel`/`.gauge-panel` por
   un bloque `.proof-panel` ("Ya lo hicimos en el sector financiero") y se reescribió
   `.hook-text` sin las cifras del estudio (también se quitó el `<strong>` que tenía: ver
   memoria `bug-strong-glitch-impact-hook-text`, glitch de renderizado confirmado en ese
   contenedor). Sin cifras inventadas (§4.9).
   **Alerta sobre `banco-casos-de-exito/index.html`**: ese catálogo interno tiene AL MENOS 3
   entradas bancarias con el mismo patrón de dato falso (Banco Activo, Banco Plaza, Banco de
   Venezuela — cifras de "+N personas" que contradicen los `meta.json`/brief.md reales de esos
   clientes). No usar ese documento como fuente de un caso de banca sin cruzarlo primero contra
   un `meta.json` en estado "Aprobada" o un `resultados.json` real.
3. **Cotización: "Descuento" → "Obsequio de Intezia".** La fila sigue siendo el mismo campo
   AcroForm editable (ventas escribe el monto; el nombre técnico del campo sigue siendo
   "Descuento" en `agregar-campo-precio.py`, solo cambia el label visible) y se agregó una
   línea fija debajo de "Importante": *"Como muestra de nuestro compromiso con Banco Activo, el
   Cerebro Digital de la Presidencia va por cuenta de Intezia."* El badge de urgencia
   ("Descuento válido por 15 días") se quitó: "Obsequio de Intezia" ya no cabía junto a él en la
   misma fila, el hueco libre debajo era insuficiente (probado, 28px, colisionaba con "TOTAL" —
   corregido tras revisión visual del PDF), y el tono de urgencia no calzaba con un gesto de
   regalo.
4. **Trío pendiente de correr tras esta corrección**: `verificar-propuesta.sh` →
   `generar-pdf.sh` → `customize-acroforms.py` → `customize-banco-activo-cerebros-digitales.py`
   (en ese orden). `estado` en `meta.json` se puso en `En corrección`; vuelve a `Enviada`
   automáticamente al regenerar el PDF (§4.19). Borrar el PDF viejo ("CAI-027 4 Cerebros
   Digitales...") una vez confirmado el nuevo, el nombre de archivo cambia con el conteo.

## Notas internas

- **Precedente de tarifa**: `empresa/politicas-comerciales.md` → "Excepción — Cerebros
  Digitales". Esta es la tercera propuesta que aplica esa tarifa de extremo a extremo, tras
  `banco-plaza-cerebros-digitales/` (CAI-025) y `amv-tecnologia-cerebro-digital/` (CAI-023).
- **Pendiente**: construir la Propuesta B (DET-021, Detección + Fase 1 de Habilidades para la
  Vicepresidencia de Negocios de Nahir) en carpeta aparte, con foco fuerte en puntos de venta
  y medios de pago.
- **Discrepancia de fuente resuelta**: la ficha dice 5 personas (Grupo 1), el usuario confirmó
  6 — la propuesta se construyó con 6, según la confirmación explícita más reciente del
  usuario. Si más adelante la propia Nahir/Giancarlo confirman 5 en vez de 6, ajustar horas
  totales (36h → 30h) y el conteo en portada, Objetivos, Programa y Cierre.
- **Script propio**: `scripts/customize-banco-activo-cerebros-digitales.py` (clonado de
  `customize-banco-plaza-cerebros-digitales.py`) agrega la escalera de Cierre (4 cajas) y
  re-hornea Beneficios v3 con fondo oscuro — correr siempre como 3er paso, después de
  `generar-pdf.sh` y `customize-acroforms.py`.
- **Trío ejecutado y verificado (2026-09-24)**: `verificar-propuesta.sh` OK (sin desbordes) →
  `generar-pdf.sh` → `customize-acroforms.py` → `customize-banco-activo-cerebros-digitales.py`.
  Revisión visual de las 14 slides sin defectos. PDF: "CAI-027 6 Cerebros Digitales, y el fin
  de empezar de cero..pdf".

## Calendario de inicio (agregado 2026-09-24, mismo día)

Instrucción directa del usuario: *"coloca el calendario con kick off para el 8 y las sesiones
a partir del 13 martes y jueves"*. Se preguntó primero si las 6 personas comparten un solo
track de 3 sesiones o si cada una tiene su propio track individual (18 sesiones en total,
como en `amv-tecnologia-cerebro-digital/` CAI-023) — el usuario confirmó **6 tracks
individuales, 18 sesiones**.

- **Kick-off**: jueves 8 de octubre de 2026, 10-11.
- **18 sesiones** (3 por cada uno de los 6 líderes), martes y jueves desde el 13 de octubre,
  10-12, corridas sin solaparse: del 13 de octubre al 10 de diciembre (~9 semanas).
- **Compresión visual (para no desbordar `.steps-calendar-grid`)**: en vez de 18 filas
  individuales, cada líder se muestra en **una sola fila** con sus 3 fechas juntas ("Cerebro
  Digital 1" a "Cerebro Digital 6", ej. "13, 15 y 20 oct") — mismo recurso que usó
  `la-tienda-del-blumer/` (DET-020) para combinar 2 fechas por área; aquí se extiende a 3
  fechas por fila. Resultado: 7 filas totales (kick-off + 6), la misma densidad ya probada sin
  desborde en CAI-023/CAI-026 (7 filas) y Blumer (9 filas). Verificado con
  `node scripts/verificar-overflow.js banco-activo-cerebros-digitales` (sin desbordes) y
  revisión visual del PDF.
- **Hora de las sesiones (10-12) no especificada por el usuario**: se usó el mismo horario
  por defecto que CAI-023 (el precedente directo de este patrón) — confirmar con Verónica
  antes de enviar si el cliente prefiere otro horario.
- Etiquetas "Cerebro Digital 1"–"6" son ordinales anónimos (no nombran rol ni persona),
  consistentes con la decisión de mantener el deck genérico.
