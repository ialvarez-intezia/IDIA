# Brief — Grupo Ferrara · Charla para creadores de contenido (CH-013)

> **Posible seguimiento de una nota histórica**: `clientes/propuestas/grupo-ferrara/brief.md`
> (DET-005, Bloque F de la ficha) dejó registrada una mención parcialmente ilegible de un
> "evento/conferencia bajo alianza" sin suficiente claridad para actuar. Esta charla llega con
> detalles concretos directamente del usuario (2026-09-09) — probablemente sea esa misma
> iniciativa ya madurada, aunque no se confirmó explícitamente el vínculo con el usuario.

## Instrucción del usuario y decisiones resueltas (2026-09-09)

1. **Naturaleza del documento**: propuesta de **contenido/estructura** para una charla pública
   de 2 horas — no lleva hoja de cotización (instrucción explícita del usuario). El objetivo de
   este documento es que Grupo Ferrara valide el enfoque del contenido antes de cerrar fecha,
   hora y sede del evento (que gestiona Ferrara por su cuenta).
2. **Código**: `CH-013` (instrucción directa del usuario). No existe CH-012 en el sistema —
   salto de numeración intencional, no un error a corregir.
3. **Asesora comercial**: Verónica Rubio (misma que en `grupo-ferrara/` y
   `grupo-ferrara-cai007/`).
4. **Tipo de acuerdo (`alianza`)**: confirmado con el usuario — **servicio pagado normal**,
   `alianza: no`. Grupo Ferrara aporta la sede/convocatoria/logística del evento; Intezia factura
   el servicio de Habilidades (Charla) como cualquier otro.
5. **Perfil del consultor**: el cliente pidió explícitamente poder "validar el perfil del
   consultor" antes de cerrar. No hay un facilitador nombrado en el sistema para este evento —
   confirmado con el usuario: **se omite esa sección en esta primera versión** del documento.
   Se agrega en una siguiente iteración, una vez asignado el facilitador (ver Paso 2 de "Cómo
   arrancamos" en el deck).
6. **Los 2 ejercicios prácticos de cierre**: confirmado con el usuario — **orientados solo a
   creación de contenido** (ideación, guion, caption, calendario de publicaciones), no a
   logística familiar/hogar como eje separado. El nicho de audiencia (mamás/vida familiar/
   recetas/logística escolar) se usa como **ejemplos y encuadre** dentro de esos ejercicios de
   contenido, no como un tercer bloque temático aparte.
7. **Herramienta**: **Gemini gratis** (instrucción explícita del usuario) — sin VPN, sin laptop,
   solo el teléfono propio de cada asistente. Contrasta con el patrón Claude+VPN+laptop usado en
   `venemergencia-ch009/` (audiencia interna de empresa, grupo chico) — aquí es evento público,
   aforo grande, herramienta de acceso más simple.
8. **Fecha, hora y sede**: **no se mencionan en el deck** (IESA es solo tentativo, sin
   confirmar) — mismo criterio que "Omitir, no inventar placeholder": si el dato no está
   cerrado, se omite del todo, no se escribe "a confirmar" ni se nombra la sede tentativa.

## Datos administrativos

- **Cliente**: Grupo Ferrara · Diseño de interiores (cocinas e interiores de lujo)
- **Slug**: `grupo-ferrara-ch013`
- **División Intezia**: `educacion` (mismo criterio que `grupo-ferrara/` y
  `grupo-ferrara-cai007/` — cliente corporativo que organiza el evento; el público asistente son
  creadores de contenido externos, no empleados de Ferrara)
- **Servicio** (Modelo Intezia, §4.1a): `habilidades` — categoría **Charla**
- **Alianza**: `no`
- **Eje temático**: creación de contenido con Gemini (gratis) para creadores enfocados en vida
  familiar, logística escolar y cocina/recetas — nicho que conecta con el foco de Ferrara en
  diseño de cocinas e interiores de lujo, sin convertir la charla en un pitch de marca
- **Duración**: 2 horas (120 min)
- **Fecha del brief**: 2026-09-09
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Contacto de referencia en Grupo Ferrara**: por confirmar

## Contexto del evento (instrucción del usuario, verbatim resumido)

- **Audiencia**: creadores de contenido, aforo estimado **100 a 120 personas**. Público
  diverso, con énfasis en mamás/amas de casa que hacen contenido de vida familiar, logística
  escolar de sus hijos y recetas de cocina.
- **Logística**: la maneja Grupo Ferrara por completo (sede, fecha, hora). Sede tentativa: IESA
  (sin confirmar — no se menciona en el deck, ver decisión 8).
- **Validación previa del cliente**: antes de cerrar fecha/hora/sede, Ferrara quiere revisar la
  propuesta de contenido y el perfil del consultor.
- **Pedido concreto a Intezia**: propuesta de contenido/estructura para una charla de 2 horas
  que aporte valor real y cierre con **2 ejercicios prácticos** que el público pueda aplicar en
  el momento, con su propio teléfono.
- **Herramienta**: Gemini gratis.

## Restricciones de copy

1. **Sin fecha, hora ni sede** en ningún lugar del deck (decisión 8).
2. **Sin perfil de consultor** en esta versión (decisión 5).
3. **Sin propuesta económica** — no hay slide `.s-price`, no hay campos de precio en el PDF
   (`agregar-campo-precio.py` los omite automáticamente al no encontrar el marcador "Propuesta
   Económica" en el HTML — mismo mecanismo confirmado en `venemergencia-ch009/`).
4. **Sin Metodología ABR ni Equipo facilitador** expuestos (§4.10a CLAUDE.md — aplica a toda
   propuesta nueva).
5. **Sin acuerdos económicos en "Cómo arrancamos"** (§4.15) — los 3 pasos son: validar
   contenido → asignar facilitador → cerrar fecha/hora/sede con Ferrara.
6. **Sin mencionar Claude, n8n ni Cerebro Digital** — solo Gemini gratis, coherente con el resto
   del ecosistema Google usado en otras propuestas cuando el cliente lo pide explícitamente.
7. **Ejercicios prácticos = creación de contenido**, usando el nicho (familia/recetas/hogar)
   como ejemplo, no como bloque temático propio (decisión 6).
8. **Impacto (§4.9)**: estadísticas de estudios reales — Capterra (Encuesta GenAI para
   Contenido Social, 2025) y Sprout Social Index (Pulse Survey Q3 2025), citadas verbatim en el
   deck.

## Notas de diseño

- **Estructura (9 slides)**: Portada → Diagnóstico → Objetivos → Programa (4 módulos) →
  Cronograma (4 sesiones, componente `.sessions`/`.session`/`.grid`, sin roadmap — mismo patrón
  liviano de charla que `venemergencia-ch009/`) → Beneficios v3 → Impacto → Próximos pasos →
  Cierre escalera.
- **Base estructural**: clon del *shell* de `farmaceutica-24/` para Beneficios v3 + Cierre
  escalera (CSS y mecánica de horneado AcroForm ya verificadas esta sesión), combinado con la
  estructura de charla (sin roadmap, sin precio, componente `.sessions`) de
  `venemergencia-ch009/` (clon original de `dusa`, CH-007).
- **Sin roadmap**: las charlas de sesión única no llevan slide de roadmap multi-etapa (no hay
  fases que mostrar).
- **`../_base/styles.css` + `overrides.css` local**: mismo patrón que `venemergencia-ch009/` —
  el componente de cronograma (`.sessions`), Beneficios v3 y Cierre escalera viven en
  `overrides.css`, no en `_base`.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh grupo-ferrara-ch013
python3 scripts/customize-acroforms.py grupo-ferrara-ch013
python3 scripts/customize-grupo-ferrara-ch013.py "clientes/propuestas/grupo-ferrara-ch013/<PDF generado>.pdf"
```

## Ajuste posterior (2026-09-09)

Se quitó "Certificado de participación INTEZIA" de `Entregables` (instrucción directa del
usuario) — a diferencia de `good-latam-cai010/` (Habilidades in-company con certificado), esta
charla es un evento público de audiencia externa, no un programa formal inscrito por Grupo
Ferrara. Regenerado el PDF completo (trío) tras el cambio en `acroforms.json`.

## Ajuste posterior (2026-09-11) — se agregó hoja de cotización

Instrucción directa del usuario: incluir la hoja de cotización (`.s-price`), revirtiendo la
decisión original (§ decisión 1, "no lleva hoja de cotización"). Se agregó la slide estándar
(Duración + Programa + Notas + Cotización) entre Impacto y Próximos pasos, con los 5 campos de
precio vacíos (`PrecioBase`, `Descuento`, `PrecioTotal` — los llena ventas en Adobe Reader,
`agregar-campo-precio.py` los detecta automáticamente al encontrar el marcador "Propuesta
Económica" que antes no existía en este deck) y `Programa`/`Notas` pre-llenados en
`acroforms.json`. Deck pasó de 9 a 10 slides, todos los contadores renumerados. Sin
certificado en el Programa (coherente con el retiro de esa línea de `Entregables`, ver ajuste
anterior). Sin mención de fecha/hora/sede en Notas, mismo criterio de "omitir, no inventar
placeholder" ya aplicado al resto del deck.

## Ajuste posterior (2026-09-14) — se quitó el recuadro de Descuento

Instrucción directa del usuario: retirar el recuadro de Descuento de la hoja de cotización.
La cotización queda con solo 2 cajas: "Propuesta + Inversión" y "TOTAL". Cambios:

- `index.html`: se eliminaron el `<span class="cot-label-discount">` y el
  `<div class="discount-frame">`.
- `overrides.css`: `.s-price .cot-label-total` y `.s-price .total-frame` se reposicionan y
  agrandan (top 320/344, height 130, font-size del placeholder a 36px) para ocupar el espacio
  que dejó el recuadro retirado.
- `scripts/customize-grupo-ferrara-ch013.py`: el campo AcroForm "Descuento" lo sigue
  inyectando `agregar-campo-precio.py` (grupo compartido por todo el sistema, marker
  "Propuesta Económica" — no se modificó ese script global). El customize propio de este
  deck ahora **elimina** ese campo del PDF final y **reposiciona** "PrecioTotal" (nuevo
  `/Rect` (435, 239.5, 800, 337), fuente 32pt) con un `/AA/C` reescrito que ya no referencia
  a Descuento (`Total = Base`, sin resta) — evita el error de JavaScript que lanzaría el
  cálculo original al intentar leer un campo que ya no existe.
- Regenerado el trío completo (`generar-pdf.sh` → `customize-acroforms.py` →
  `customize-grupo-ferrara-ch013.py`), verificador automático en verde, revisión visual de la
  slide 08/10 sin overflow ni cajas huérfanas.

## Bug encontrado y corregido al construir (2026-09-09)

Item 1 de "Objetivos específicos" (`.s-goals .specifics li`) llevaba `<strong>Gemini</strong>` y
rompía el layout flex del `<li>` (texto superpuesto/desalineado) — mismo bug ya documentado en
memoria `bug-strong-flex-specifics.md` (`<strong>` dentro de cualquier `<li>` flex de
`.s-goals .specifics` o `.s-schedule .ses-block`). Se quitó la negrita de "Gemini" en ese ítem
puntual; el resto de la slide no la necesitaba.

## Pendientes

- Confirmar fecha, hora y sede definitivas con Grupo Ferrara (fuera de este documento).
- Asignar y documentar el perfil del consultor/facilitador una vez el cliente valide el
  contenido (decisión 5) — agregar esa sección en una siguiente iteración del deck.
- Confirmar contacto/cargo de referencia en Grupo Ferrara para este evento.
- Confirmar si existe vínculo directo con la nota "evento/alianza" de `grupo-ferrara/brief.md`
  (Bloque F) — no asumido, ver nota al inicio de este documento.
