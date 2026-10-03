# Brief — Val-U · Bootcamp Finanzas e Inteligencia Artificial (CU-005)

## Datos administrativos

- **Empresa / Aliado**: **Val-U** — alianza de co-facilitación con Intezia (no es cliente
  destinatario ni institución que solo acredita: Val-U **dicta** 2 h de cada sesión).
- **Tipo de relación**: alianza 50/50 de co-facilitación. Cada sábado de 4 h se reparte en
  **2 h a cargo de Val-U** (finanzas) + **2 h a cargo de Intezia** (IA), en las 8 sesiones
  sabatinas del programa.
- **Slug**: `val-u`
- **División Intezia**: `educacion`
- **Tipo de documento**: Curso (`CU-005`)
- **Programa**: Bootcamp Val-U & Intezia · Finanzas e Inteligencia Artificial
- **Eje temático**: educación financiera personal + IA generativa aplicada a presupuestos,
  ahorro e inversión
- **Modalidad**: Híbrido (presencial en el hub tecnológico Wave y alternativos / online síncrono)
- **Sin fecha**: esta versión no fija fechas de arranque ni de sesión — se coordinan con Val-U
  antes de confirmar el cronograma real.
- **Sin número de propuesta visible como cotización**: el código interno **CU-005** se
  mantiene como identificador del programa (subido a **versión 3.0** en esta revisión), pero
  la propuesta no lleva folio de cotización.
- **Sin duración total en horas**: por instrucción del usuario, ni el documento ni ningún
  resumen mencionan una cifra total de horas (ni "32 h" ni "16 h"). La duración se describe
  como **"2 meses de clases sabatinas"**, con el detalle de que cada sábado dura 4 h.
- **Estado**: `Borrador`

## ⚠️ Formato especial — no usar como plantilla para otras propuestas

Esta propuesta es un **caso particular**: por pedido explícito del usuario (2026-08-10), el
entregable es un **documento de diseño curricular en PDF con branding real de Intezia**
(logo, paleta, tipografía) — **no** el deck de slides estándar del sistema (`index.html` de
16 diapositivas horizontales con AcroForms). El usuario aclaró textualmente: *"toma en cuenta
que esta propuesta es particular no tienes que hacer lo mismo con las demás"*. No generalizar
este patrón a otras propuestas de catálogo sin instrucción explícita.

- Se eliminaron los artefactos del deck anterior (`index.html`, `overrides.css`,
  `acroforms.json`, el PDF de slides) — quedaron obsoletos al cambiar de formato.
- El entregable vive en `documento.html` → PDF vertical (carta/A4), generado directo con
  Chrome headless (no usa `scripts/generar-pdf.sh`, que asume el formato de deck horizontal
  con AcroForms de precio).
- **Hoja de Cotización (2026-08-11)**: se agregó como página 6 (§09), a pedido del usuario.
  Incluye "Qué incluye" (alcance) + tabla de Inversión (Inversión del programa / Descuento /
  Total) con 3 campos AcroForm reales (`Inversion`, `Descuento`, `Total` — vacíos, ventas los
  llena en Adobe Reader; `Total` autocalcula vía JS). **Sin términos y condiciones** (sin
  anticipo, forma de pago, ni cláusulas) — solo una línea de vigencia ("Cotización válida por
  30 días."), por pedido explícito del usuario. Los campos se inyectan con
  `scripts/agregar-cotizacion-val-u.py <ruta-al-pdf>` (script propio de este caso especial,
  con rects medidos empíricamente sobre el render a 150dpi — no reutiliza
  `agregar-campo-precio.py`, que asume el layout del deck horizontal). **Par obligatorio si se
  regenera el HTML**: volver a exportar el PDF con Chrome headless y correr ese script
  inmediatamente después, o los campos de precio no aparecerán.

## Contacto

- **Asesora comercial Intezia**: por confirmar
- **Contacto Val-U**: por confirmar
- **Equipo facilitador**: Intezia designa al facilitador de IA; Val-U designa al facilitador
  financiero, ambos antes del arranque

## Por qué esta revisión (v3.0)

La versión original de este bootcamp (elaborada por Keiber Quintana) estaba pensada para
**temporada vacacional**: 4 semanas, 8 sesiones de 4 h, con 2 clases por semana. Una primera
revisión (v2.0) lo comprimió a 4 sábados (16 h), lo que obligó a reescribir los Módulos II y
IV en "versión exprés" para caber en 2 h.

El usuario pidió **reacomodar la duración**: en vez de comprimir, **estirar el calendario a 2
meses de clases sabatinas**, retomando el **cronograma original completo** (8 sesiones de 4
h, sin recortar temario). Con 2 meses de margen, cada sábado equivale a una de las 8 sesiones
originales — **ningún módulo necesita versión exprés**: los 4 módulos conservan sus 5 temas
completos, tal como en el documento original. Lo único que cambia frente al documento
original es que cada sábado (antes "clase" indistinta dentro de la semana) ahora se reparte
explícitamente en 2 h Val-U + 2 h Intezia.

También se pidió **quitar ChatGPT** del ecosistema de herramientas — el programa queda con
**Claude y Gemini** únicamente — y producir el documento con el **branding real de Intezia**
(logo, paleta, tipografía) en vez del deck de slides.

## Diagnóstico (5 puntos)

1. El bootcamp original se diseñó para vacaciones (4 semanas seguidas); ese calendario ya no
   aplica, y comprimirlo a 4 sábados obligaba a recortar temario real.
2. Estirar el calendario a 2 meses de sabatinos permite recuperar el cronograma original
   completo (8 sesiones, 4 módulos de 5 temas cada uno) sin perder contenido.
3. El mercado exige a jóvenes y profesionales no solo entender el dinero, sino potenciar sus
   decisiones con tecnología — la brecha entre alfabetización financiera y herramientas de IA
   sigue vigente.
4. El ecosistema de herramientas se simplifica a **Claude y Gemini** (se retira ChatGPT),
   evitando dispersión de herramientas en un programa de solo 2 facilitadores.
5. Sin una alianza clara de quién dicta qué, la doble certificación pierde credibilidad — cada
   sábado necesita mostrar la mano de ambas partes, no solo el logo compartido al final.

## Especificaciones del programa

- **Duración**: 2 meses de clases sabatinas (8 sábados) · 4 h por sábado — **no se menciona
  un total de horas** en ningún resumen ni portada.
- **Modalidad**: Híbrido (presencial en el hub tecnológico Wave y alternativos / online síncrono)
- **Audiencia**: jóvenes y profesionales, sin experiencia previa requerida en IA ni finanzas
- **Estructura**: 4 módulos (5 temas cada uno · regla Curso) · 2 sábados por módulo
- **Reparto por sábado**: 2 h Val-U + 2 h Intezia, en las 8 sesiones
- **Ecosistema**: Claude y Gemini (se retiró ChatGPT de esta versión)
- **Acreditación**: certificación conjunta INTEZIA + Val-U
- **Calificación mínima**: 70 / 100
- **Entregables comprometidos**: Workbook del Bootcamp + plantillas de presupuestos automatizados + Certificado conjunto

## Notas comerciales internas (no entran al documento)

- Sin apartado de precio en esta versión (es un documento de diseño curricular, no un deck
  comercial con cotización).
- Vigencia general de la propuesta: 30 días · Anticipo del 50 % (política estándar Intezia;
  confirmar con Val-U si el reparto de ingresos sigue otro esquema interno entre ambas partes).

## Decisiones de esta versión (v3.0)

- **Documento, no deck**: PDF de diseño curricular con logo real de Intezia
  (`logos/educacion/NEGRO.png`), paleta oficial (`#000000` / `#F4BA1A` / `#E58423` /
  `#FFFFFF`) y tipografía Graphit/Inter (§ `empresa/marca-visual.md`).
- **Cronograma restaurado**: 8 sábados (2 por módulo), sin versión exprés — ver
  `programa.md` §5.2.
- **Sin ChatGPT**: ecosistema reducido a Claude y Gemini en todo el documento.
- **Sin cifra de duración total**: ni "32 h" ni "16 h" aparecen en el documento; se describe
  como "2 meses de clases sabatinas".
- **Marca**: solo logo y paleta INTEZIA (§4.1) — Val-U se menciona como aliado en texto
  ("alianza Val-U × Intezia", certificación conjunta), mismo patrón que las alianzas SFIC.
- **Caso particular**: no replicar este formato de documento branded en otras propuestas sin
  instrucción explícita del usuario (ver advertencia arriba).

## Pendientes

- Confirmar contacto/cargo de referencia en Val-U.
- Confirmar nombre del facilitador de Val-U y del facilitador de Intezia.
- Confirmar sede exacta del hub tecnológico Wave (o alternativo) y modalidad real por sábado
  (presencial / online) una vez haya fechas.
- Confirmar esquema de reparto de ingresos entre Val-U e Intezia (no se factura en el documento).
