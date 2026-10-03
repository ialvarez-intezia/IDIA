# Brief — Everest (DET-006)

> **Fuente primaria: Ficha de Levantamiento Intezia — Everest** (levantada por María
> Iribarren, 2026-09-02). Servicio de interés registrado en la ficha: Detección. Los datos
> de abajo se extraen de esa ficha; no se cotiza a ciegas.

## Datos administrativos

- **Empresa**: Everest
- **Sector**: Transporte, logística y courier (carga pesada + paquetería puerta a puerta,
  licencia certificada)
- **Tamaño**: Mediana (50-250 empleados). ~20-25 personas del equipo administrativo/
  corporativo involucradas (no incluye la parte operativa, ~42-45 personas).
- **Slug**: `everest`
- **División Intezia**: `educacion` (cliente corporativo; inferencia razonada, no
  confirmada explícitamente con el usuario)
- **Servicio** (Modelo Intezia): `deteccion` — pura, es lo único que se cotiza en detalle.
  El deck también muestra (sin cotizar) las etapas de Habilidades y Políticas, a pedido
  explícito del patrocinador — ver "Notas de diseño" abajo. No es `integral` (§4.1b): no
  se están vendiendo las 3 (ni las 4) etapas como un plan secuencial ya contratado, solo
  Detección; las otras 2 son contexto/visión.
- **Alianza**: no
- **Código**: `DET-006` (verificado libre)
- **Eje temático**: diagnóstico de gobernanza y uso desigual de Claude, para preparar la
  certificación ISO 9001, con roadmap hacia Habilidades y Políticas.
- **Fecha del brief**: 2026-09-03
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414 0570056 · miribarren@intezia.com
- **Cliente / patrocinador**: Aramis Monge, Dirección Ejecutiva — decide presupuesto y
  calendario junto con Nataly (Talento Humano) vía comité. **No se nombra en el contenido
  del deck** (mismo criterio que el resto del sistema: se habla de "Dirección Ejecutiva",
  no de Aramis por nombre) — sí queda registrado aquí para uso interno y logística.
- **Otros stakeholders** (ficha, Bloque específico Detección): Miguel · Gerente Comercial;
  Nataly · Gerente de Talento Humano (a contactar antes de poder cerrar fechas — coordina
  presupuesto y calendario vía comité).
- **Servicio previo con Intezia**: no, es el primer contacto.

## Contexto (Ficha, Bloques A/B/C)

- **Ecosistema tecnológico**: Microsoft 365. La información del negocio vive en varios
  sistemas separados por área.
- **Herramientas de IA que ya usan**: licencias corporativas de Claude (Anthropic), tipo
  Teams. Uso muy disperso: algunos le sacan el máximo provecho, otros casi no lo tocan.
  Además desarrollan internamente 2 apps con apoyo de IA (**Everest Ops** y **Everest
  Tracker**), lideradas por los 2 socios sin formación técnica formal, con apoyo de 1
  persona de IT y 1 de seguridad/nube.
- **Equipo involucrado**: ~20-25 personas del equipo administrativo/corporativo. Roles:
  Dirección ejecutiva, gerencia comercial, administración, talento humano, operaciones
  (corporativo), transformación digital (vacante), más el equipo técnico de las apps
  internas. Nivel de partida: "muy desigual entre áreas". Sin formación formal en IA — el
  propio director ha dado capacitación informal con lo que sabe, sin programa ni
  gobernanza.
- **Objetivo central (cita textual)**: "Necesitamos como darle sentido a esto y que tenga
  como un plan de desarrollo, un plan de capacitación." Certificados en ISO 9001, lo que
  exige gobernanza y procesos documentados que hoy no tienen formalizados en el uso de IA.
- **Restricciones**: regulación ISO 9001 (exige gobernanza y procesos documentados).
  Presupuesto "en evaluación". Patrocinio ejecutivo: **fuerte y visible** (a diferencia de
  otros clientes recientes con patrocinio tibio).

## Bloque específico de Detección (Ficha)

- **Stakeholders clave por área**: Aramis · Dirección Ejecutiva; Miguel · Gerente
  Comercial; Nataly · Gerente de Talento Humano — estas son las **3 áreas** auditadas.
- **Diagnóstico previo de IA**: no hay (sí hicieron un levantamiento propio de
  transformación digital/licencias anterior, no relacionado a IA).
- **Modalidad**: Presencial en sus oficinas (sede administrativa en Caracas; la empresa
  opera además en Maracay, Valencia y Miami — no se especifica si esas sedes participan de
  la Detección; se asume que las 3 sesiones son en Caracas, con los 3 stakeholders
  corporativos).
- **Quién firma y decide**: Aramis decide; presupuesto y calendario los coordina Nataly
  (Talento Humano) vía comité.
- **Objetivo del Reporte Final**: "Un roadmap claro, oportunidades reales de optimización e
  inversión de IA, plan estratégico, equipo nivelado, oportunidades identificadas de
  reducción de costos."
- **Duración por área**: no especificada en la ficha — se usó el estándar del sistema
  (2h por área, confirmado con el usuario) = 6h en total para las 3 áreas.

## Restricciones de copy

1. **Sin nombres propios de personas ni de departamentos específicos** en el contenido del
   diagnóstico/objetivos — se habla de "las áreas administrativas" y la empresa, en
   genérico (ajuste 2026-09-03, 2ª ronda — antes se nombraba Dirección Ejecutiva, Comercial
   y Talento Humano). El nombre de María sí aparece en el bloque de contacto del Cierre.
2. **Sin presupuesto real** ni condiciones de pago en el deck (§4.15) — tanto la
   cotización de Detección como el presupuesto global de referencia quedan con campos
   vacíos, los llena ventas.
3. **§4.11**: no se afirma que Everest migra o adopta un nuevo stack — Claude y Microsoft
   365 son su entorno actual.
4. **ISO 9001** no se expande (§4.12 excepción: sigla de uso general en su sector/
   ampliamente reconocida, no jerga interna de Intezia).

## Petición explícita del patrocinador (Bloque F/G de la ficha) — 2 elementos nuevos

Aramis (patrocinador directo) ya está convencido de arrancar con Detección, pero pidió dos
cosas adicionales para esta propuesta, tomadas casi textuales de la ficha:

1. **"Una hoja con la ruta de los 3 servicios a la propuesta (Detección, Habilidades y
   Políticas)"** — resuelto con la slide `.s-journey` ("Hoja de ruta completa"): 3
   tarjetas — Detección (esta propuesta, destacada), Habilidades (más desarrollada, hay
   plantilla vigente en el sistema), Políticas (tarjeta resumen, sin plantilla propia
   todavía — `empresa/tipos-de-documento.md §0`, pendiente de decisión de formato).
2. **"Un espacio para darles un presupuesto base global para las 3 etapas, aparte de la
   cotización que se le hará en Detección"** — resuelto originalmente con una segunda hoja
   de precio (`.s-price-plan`), consolidado en una sola hoja el mismo día, y **vuelto a
   separar en 2 hojas en la 2ª ronda** de ajustes — ver "Ajuste 2026-09-03 (2ª ronda)" más
   abajo para el estado final.

## Ajuste 2026-09-03 (segunda pasada, tras revisión del usuario)

El usuario revisó el primer borrador y pidió 4 cambios puntuales:

1. **Beneficios sin certificado**: como esta propuesta es solo Detección (no incluye
   capacitación), se quitó "Certificado de participación INTEZIA" de `Entregables` — un
   diagnóstico no emite certificado de participación, eso es propio de Habilidades.
2. **Hoja de ruta sin etiquetas**: se quitaron las etiquetas de texto ("Esta propuesta",
   "Se cotiza tras el diagnóstico", "Formato en definición") que iban encima de "Etapa 1/2/3"
   en cada tarjeta — la diferencia entre la etapa activa y las futuras queda solo en el
   estilo visual (tarjeta amarilla vs. tarjetas oscuras con borde punteado).
3. **Una sola hoja de cotización, no dos**: se eliminó la Propuesta Económica estándar de
   Detección sola. Ahora hay **una única hoja "Inversión por fases"** con las 3 fases
   (Detección/Habilidades/Políticas) + Notas + Términos y condiciones — el usuario pidió
   explícitamente "añade a esa [la de los 3 pasos] la parte de términos y condiciones como
   están las [demás] hojas de cotización". Con una sola hoja de precio en todo el
   documento, ya no hay riesgo de colisión de nombres de campo (ver nota técnica abajo) —
   se simplificó a usar el marker y los campos ESTÁNDAR de `agregar-campo-precio.py`
   (`PrecioFase1-3`, `PrecioBase`, `Descuento`, `PrecioTotal`, `Notas`), eliminando los
   campos custom `Plan*` y el namespace CSS `.s-price-plan` de la primera versión.
4. **Cronograma también para Habilidades y Políticas**: se agregaron 2 slides de
   cronograma genéricas (mismo formato visual que la de Detección — Temas, Qué se
   hace/Qué se logra/Recursos — pero **sin timebar de horas**, porque esas 2 etapas no
   tienen alcance ni duración definida todavía). Contenido a nivel de qué se lograría con
   cada etapa, sin comprometer fechas, horas ni entregables específicos que dependen del
   resultado de la Detección.

**Nota técnica (histórico, ver estado final en "Ajuste 2026-09-03, 2ª ronda" arriba):** la
primera versión de este deck tenía dos slides `.s-price` (Propuesta Económica de Detección +
presupuesto global de 3 fases) con campos custom `Plan*`. Se consolidó a 1 sola hoja el
mismo día (este ajuste, 1ª ronda). El usuario luego pidió volver a 2 hojas (2ª ronda) — el
resultado final usa el mismo principio (título que no coincide con ningún marker + campos
custom a mano), pero con nombres de campo `Det*` en vez de `Plan*`, y sin namespace CSS
propio para la hoja de Detección (usa los defaults de `_base/styles.css` tal cual — es la
hoja de "Inversión por fases" la que ahora lleva el namespace `.s-price-fases`, al revés
del diseño original). Ver memoria `patron-dos-slides-precio-mismo-deck`.

## Ajuste 2026-09-03 (2ª ronda) — 7 correcciones del usuario

1. **Sin "2 socios"**: a la reunión de levantamiento fue un solo socio y el gerente
   comercial (Miguel), no los 2 socios — se corrigió el punto 2 del Diagnóstico ("un socio
   y el gerente comercial impulsan Everest Ops y Everest Tracker...", antes decía "los dos
   socios").
2. **Áreas administrativas, no 3 departamentos nombrados**: se retiró "Dirección
   Ejecutiva, Comercial y Talento Humano" de toda la prosa del deck (Diagnóstico,
   Objetivos, Programa, Cronograma, Hoja de ruta, Pasos) — ahora dice "áreas
   administrativas" o "las áreas administrativas de Everest". Se preguntó y se confirmó
   con el usuario: se mantiene la estructura de 3 sesiones de 2h (6h) ya presupuestada,
   solo se generaliza el nombre, no la cantidad — el cronograma de Detección ahora dice
   "Área administrativa 1/2/3" en el timebar, sin nombrar los departamentos reales.
3. **Diagnóstico de Claude afinado**: "Hoy solo algunas personas usan Claude de forma
   activa; el resto del equipo tiene un desnivel marcado en su manejo de la herramienta"
   (antes: "algunos le sacan el máximo provecho, otros casi no lo tocan" — más suave).
4. **Fundamentals agregado a Habilidades**: la tarjeta de Habilidades en la Hoja de ruta
   ahora dice "Empieza con Fundamentals de Claude para nivelar a todo el equipo, y luego
   construye sobre los hallazgos del diagnóstico..." — Fundamentals es parte de la oferta
   de Habilidades en todo el sistema y no estaba mencionado.
5. **Habilidades y Políticas solo en la Hoja de ruta**: se retiraron las 2 slides de
   cronograma detallado que existían para esas 2 etapas (Temas/Qué se hace/Qué se
   logra/Recursos, sin timebar) — quedan mencionadas únicamente al nivel de resumen de la
   Hoja de ruta (`.s-journey`), no con una slide de detalle propia. El deck baja de 13 a
   12 slides.
6. **Cantidad de personas y áreas en ambas cotizaciones**: se agregó "3 áreas
   administrativas · ~20-25 personas del equipo administrativo" a la Duración de la nueva
   hoja de Detección y al `price-intro` de "Inversión por fases", para que ventas tenga un
   estimado correcto de tamaño al cotizar.
7. **2 hojas de cotización de nuevo** (revierte la consolidación de la 1ª ronda, ver nota
   técnica más abajo): se preguntó y se confirmó con el usuario mantener el mismo desglose
   de 3 filas para la hoja de referencia. Resultado:
   - **Hoja A · "Cotización · Detección"** (nueva, standalone): SOLO Detección, patrón
     estándar de una sola línea (Duración + Propuesta/Inversión + Descuento + Total +
     Notas + T&C). Campos custom `DetPrecioBase/DetDescuento/DetPrecioTotal/DetNotas`
     (`scripts/customize-everest.py`) — título "Cotización · Detección" no coincide con
     ningún marker de `agregar-campo-precio.py`, así que no se autoinyecta nada ahí.
   - **Hoja B · "Inversión por fases"** (la que ya existía): 3 filas
     Detección/Habilidades/Políticas, marker y campos ESTÁNDAR
     (`PrecioFase1-3/PrecioBase/Descuento/PrecioTotal/Notas`), ahora con namespace CSS
     propio `.s-price-fases` en `overrides.css` para no pisar los defaults que usa la Hoja
     A (ambas comparten la clase base `.s-price`).
   - Ver memoria `patron-dos-slides-precio-mismo-deck` para el patrón completo y su
     historial (se había consolidado a 1 hoja el mismo día, ahora se revierte a pedido
     explícito del usuario).

## Ajuste 2026-09-03 (3ª ronda) — 2 correcciones puntuales del usuario

1. **Fundamentals no quedaba claro como algo enseñado**: la tarjeta de Habilidades en la
   Hoja de ruta decía "Empieza con Fundamentals de Claude..." (sonaba a método/punto de
   partida, no a contenido enseñado). Se reescribió a "Se **enseñan** los Fundamentals de
   Claude para nivelar a todo el equipo, y se construye sobre los hallazgos del
   diagnóstico...", dejando explícito que Fundamentals es parte de lo que se enseña/logra.
2. **"3 áreas" fuera de las hojas de cotización**: en la 2ª ronda se había mantenido el
   conteo "3" junto con "áreas administrativas" (ej. "3 áreas administrativas · ~20-25
   personas"). El usuario pidió que las hojas de cotización digan solo "áreas
   administrativas", sin el número — se quitó el "3" en 3 lugares: Duración de "Cotización
   · Detección", `price-intro` de "Inversión por fases", y la descripción de Fase 1 en esa
   misma hoja ("Diagnóstico de 3 áreas" → "Diagnóstico de áreas administrativas"). También
   se quitó "(3 áreas, ...)" del default de `DetNotas` en `customize-everest.py`. El
   Cronograma y el Cierre siguen diciendo "3 sesiones"/"3 áreas" sin cambios — ahí sí
   describe la estructura operativa real (3 sesiones de 2h), y el usuario no pidió tocarlo;
   la corrección fue específica a las hojas de cotización.

## Ajuste 2026-09-03 (4ª ronda) — Fundamentals va en Detección, no en Habilidades

Corrección sobre la 3ª ronda: el usuario aclaró que la mención de Fundamentals debe ir
**dentro de la Detección** (esta propuesta), no en la tarjeta de Habilidades de la Hoja de
ruta. Se revirtió la tarjeta de Habilidades a su redacción anterior (sin Fundamentals) y se
agregó nivelación en los Fundamentals de Claude, en paralelo a la auditoría, en 4 lugares
de la parte de Detección:

1. **Objetivos específicos** (punto 2): "...y nivelar al equipo en sus Fundamentals en
   paralelo a la auditoría."
2. **Programa**, módulo II · Auditoría: "...con nivelación en los Fundamentals de Claude en
   paralelo."
3. **Cronograma de Detección**: chip nuevo "Fundamentals de Claude" en Temas; bullet nuevo
   en "Qué se hace" ("En paralelo, nivelamos al equipo...") y en "Qué se logra" ("Equipo
   nivelado en los Fundamentals de Claude...").
4. **Beneficios** (Acreditacion / Valor inmediato, `acroforms.json`): nueva línea "Equipo
   nivelado en los Fundamentals de Claude, en paralelo a la auditoría."

Mismo patrón que DHL DET-004 (Fase 1 = Detección + nivelación de Copilot, en paralelo) —
Everest ahora tiene el mismo componente de nivelación integrado dentro de su Fase de
Detección.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh everest
python3 scripts/customize-acroforms.py everest
python3 scripts/customize-everest.py "clientes/propuestas/everest/<PDF generado>.pdf"
```

## Pendientes

- Confirmar fechas y horario de las 3 sesiones de auditoría (dependen de Nataly, Talento
  Humano, vía comité).
- Confirmar si las sedes de Maracay, Valencia o Miami participan de la Detección, o si las
  3 sesiones son solo en la sede administrativa de Caracas (asumido).
- Confirmar presupuesto — tanto el de Detección como el estimado global quedan vacíos en
  el PDF, los llena ventas.
- Si el usuario confirma que "Luis Vicente" u otro precedente aplica aquí también, revisar
  (no se identificó ninguna relación con este caso).
