# Brief — Hoteles Cumberland

---

## Actualización 2026-09-30 — de 8 áreas a 7: unificación + 2 áreas nuevas

Instrucción directa del usuario, comunicada por el cliente: las áreas se reorganizan y se
amplían. **Por escrito, para que quede explícito en el sistema:**

**Se unifican en una sola sesión cada uno de estos 2 grupos** (antes eran sesiones separadas):

1. **Ventas + Marketing + Reservaciones** → 1 sola área, "Ventas, Marketing y Reservaciones".
2. **Administración + Contabilidad** → 1 sola área, "Administración y Contabilidad".

**Se agregan 2 áreas nuevas al alcance de la estructura de sesiones** (no estaban en el
alcance original de 8 áreas):

3. **Recursos Humanos** — sin ficha propia; se construye su sesión en términos genéricos
   (selección, nómina, comunicados), sin inventar headcount ni herramientas específicas
   (decisión confirmada con el usuario).
4. **Auditoría** — función de auditoría interna/financiera (confirmado con el usuario, no se
   refiere a "night audit" operativo de hotelería, que quedaría fuera de alcance por ser área
   operativa).

**Cuentas por Pagar, Fiscal y Tesorería siguen como áreas separadas**, sin cambio de alcance.

### Nuevo dimensionamiento de horas

Instrucción directa del usuario: *"Si vamos a hacer, por ejemplo, Ventas y Reservaciones, una
auditoría de 3 horas, Administración y Contabilidad, una auditoría de 3 horas, y las demás
áreas, 2 horas, y dejamos los Fundamentals en las 2 horas en que está."*

| Área | Horas |
|---|---|
| Ventas, Marketing y Reservaciones (unificada) | 3h |
| Administración y Contabilidad (unificada) | 3h |
| Cuentas por Pagar | 2h |
| Fiscal | 2h |
| Tesorería | 2h |
| Recursos Humanos (nueva) | 2h |
| Auditoría (nueva) | 2h |
| **Subtotal 7 áreas** | **16h** |
| Fundamentals (sin cambio) | 2h |
| **Total** | **18h** |

**El total no cambia** (18h, igual que antes de este ajuste) — antes eran 8 áreas × 2h = 16h de
áreas; ahora son 2 áreas × 3h + 5 áreas × 2h = 16h de áreas también. Coincidencia útil para la
conversación comercial: se amplía el alcance (2 áreas nuevas) y se profundiza en las 2 áreas
unificadas, sin subir la inversión total.

### Decisiones confirmadas con el usuario (preguntas hechas antes de aplicar el cambio)

1. **Auditoría = función interna/financiera**, no "night audit" operativo. Encaja con el resto
   de las áreas corporativas/administrativas ya en alcance (Fiscal, Tesorería, etc.).
2. **Recursos Humanos, sin ficha específica**: se redacta en genérico, sin inventar cifras de
   headcount ni herramientas que el cliente no confirmó.
3. **Reservaciones mantiene más peso dentro de la sesión unificada** de Ventas/Marketing/
   Reservaciones (3h) — sigue siendo el dolor #1 citado por Leudo Gonzalez (2 personas, alto
   volumen, sin cobertura 24/7); Ventas y Marketing se auditan con menos profundidad dentro de
   esa misma sesión.
4. **El universo de 12 a 16 personas se mantiene igual** — Recursos Humanos y Auditoría ya
   estaban contempladas dentro de ese headcount, solo no tenían sesión propia antes.

### Qué cambió en el deck

13 slides (antes 12) — se agregó la slide 07/13 "Cronograma · Estructura de las 3 horas"
(mismas clases `.s-schedule` compartidas, sin CSS nuevo) para las 2 sesiones unificadas; la
slide de "Estructura de las 2 horas" (ahora 08/13) pasa a representar las 5 áreas restantes.
Se actualizaron Portada, Diagnóstico, Objetivos, Programa (h2, meta, Módulo II con la nota
explícita de unificación + áreas nuevas), Roadmap, ambos Cronogramas, Beneficios, Propuesta
Económica (Duración), Próximos pasos y Cierre. AcroForms (`Entregables`, `Programa`, `Notas`)
actualizados en `acroforms.json` — `Programa` se resume en vez de listar las 7 áreas por nombre
compuesto, por el mismo bug ya documentado abajo (caja `Programa` se corta en silencio con
listas largas). `CierreResultado` actualizado en
`scripts/customize-hoteles-cumberland.py`.

---

## Datos administrativos

- **Empresa**: Hoteles Cumberland (cadena hotelera, 4 establecimientos)
- **Sector**: Hotelería
- **Tamaño**: Mediana (50-250 empleados, ~100 personas en toda la empresa)
- **Slug**: `hoteles-cumberland`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Tipo de documento**: Detección (`DET-011`) · Fundamentals (2h grupal) + auditoría de 8
  áreas corporativas y administrativas, 4 horas por área (34h totales), modalidad mixta.
- **Eje temático**: Llevar la adopción de IA de cero a una base real en el área corporativa y
  administrativa, empezando por Reservaciones y el área contable.
- **Fecha del brief**: 2026-09-09
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Hoteles Cumberland**
(`Levantamiento_Hoteles_Cumberland_2026-09-08.pdf`, reunión del 2026-09-08), elaborada por la
asesora **Verónica Rubio**.

## Contacto

- **Asesora comercial**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Contacto cliente**: Leudo Gonzalez · Director General · punto de contacto único y decisor
  (firma y decide directamente)
- **Servicio previo con Intezia**: ninguno — primer contacto (Leudo conocía Intezia por un
  evento de FEDECÁMARAS, pero nunca se ejecutó ningún servicio)

## Áreas a auditar (8, ajustado con el usuario 2026-09-09 — reemplaza el alcance de 13 áreas) — superado 2026-09-30, ver arriba

> **Corrección de alcance (2026-09-09)**: la versión anterior de este documento cubría las 13
> áreas de "toda la operación". Al revisar la información compartida por Leudo con más
> detalle, el usuario determinó que su explicación estuvo más enfocada en **procesos** que en
> departamentos tradicionales, y que la empresa opera dividida entre **área operativa**
> (atención directa del hotel y huéspedes: Habitaciones/Recepción, Alimentos y Bebidas,
> Mantenimiento, Seguridad) y **área corporativa/administrativa**. **Esta propuesta se limita
> únicamente al área corporativa y administrativa** — el área operativa queda fuera de este
> documento (varias de sus funciones se complementan con servicios subcontratados). El usuario
> aclarará este punto nuevamente con Leudo al presentar la propuesta, para que el alcance quede
> completamente definido.

Las 8 áreas corporativas/administrativas a auditar:

1. Ventas
2. Reservaciones
3. Marketing
4. Contabilidad
5. Administración
6. Cuentas por Pagar
7. Fiscal
8. Tesorería

**Headcount del alcance**: 12 a 16 personas aproximadamente, incluyendo al Director General.

## Decisiones confirmadas con el usuario (2026-09-09)

1. **8 áreas corporativas y administrativas** (no las 13 de "toda la operación" de la versión
   anterior) — ver corrección de alcance arriba. Reservaciones se mantiene (dolor #1 citado por
   Leudo), pero Recepción queda fuera por ser atención operativa directa al huésped.
2. **4 horas de Detección por área** (32h) + **Fundamentals de 2h grupal** (12 a 16 personas,
   una sola sesión, dentro del máximo de 25 del lineamiento de Detección) = **34h totales**.
   Cada sesión de área deja un **logro inmediato** aplicable, mismo criterio que
   `farmaceutica-24/` DET-010.
3. **Fundamentals como sesión real dentro de este servicio** (no solo una recomendación a
   futuro): 2h grupales, antes de las 8 sesiones de área, dado que la adopción de IA hoy es
   cero a nivel corporativo. Se enmarca como preparación para la auditoría (nivelar
   vocabulario y expectativas), no como una capacitación certificada aparte — sigue sin
   certificado (ver punto 5).
4. **Recomendación de Claude, mención única y breve**: en la Etapa "Reporte Final" del
   roadmap únicamente — el resto del deck (incluido cualquier mapa de calor/tabla ilustrativa,
   que de todas formas no se incluye, ver punto 6) permanece neutral. Leudo ya conoce Claude a
   título personal e informal.
5. **Sin Certificado de participación INTEZIA** en Entregables ni en Programa — la Detección
   (incluida la sesión de Fundamentals, que es preparación, no capacitación certificada) es
   una auditoría, no un curso. Ver memoria `deteccion-sin-certificado.md`.
6. **Sin slide de Mapa de Calor** (tabla ilustrativa) — instrucción explícita del usuario,
   mismo ajuste ya aplicado a `farmaceutica-24/`. "Mapa de Calor" sigue como nombre del
   entregable de la Etapa de Priorización, sin slide propia.

## Necesidad detectada

Objetivo central citado textualmente por Leudo Gonzalez, Director General: *"Para mí la
aplicabilidad de la inteligencia artificial, por excelencia, es en mi departamento de
reservación... no solamente por atender a mis clientes 24/7, sino que hay mucha repetición de
solicitudes. Luego lo vi en la recepción del hotel, hay mucha interacción de mi personal con
los huéspedes atendiendo solicitudes bastante frecuentes... y esto puede ir hasta tareas
repetitivas como la conciliación bancaria, los impuestos municipales, y la fabricación de
estados financieros por unidad de negocio, que toma mucho tiempo a mi personal de
contabilidad."*

1. **Reservaciones**: 2 personas procesan reservas para los 4 hoteles, alto volumen de
   solicitudes repetitivas, sin cobertura fuera de horario laboral (Leudo busca 24/7). Único
   punto de contacto con el huésped que queda dentro del alcance corporativo de este
   documento — Recepción (atención presencial en las 4 sedes) queda fuera, por ser área
   operativa.
2. **Conciliación bancaria y cuentas por pagar**: 2-3 analistas contables, señalado
   explícitamente por el cliente como uno de los procesos más evidentes para automatizar.
3. **Gestión fiscal**: 1 persona centraliza impuestos municipales de las 4 sedes, SENIAT y
   contribuciones al Ministerio de Turismo — tarea repetitiva de alta frecuencia concentrada
   en una sola persona.
4. **Estados financieros por unidad de negocio**: procesamiento manual lento; el cliente
   quisiera que, además de generarse automáticamente, el sistema dé una opinión/análisis
   crítico sobre los estados.
5. **Ventas, Marketing y Administración**: sin un criterio común de uso de IA ni referencia de
   por dónde empezar, mismo punto de partida que el resto del área corporativa.
6. **Adopción de IA hoy = 0** a nivel corporativo. Solo Leudo ha explorado IA de forma
   personal e informal (OpenAI, Claude), sin implementación ni formación para el equipo. Hubo
   un intento fallido hace un par de años de chatbots de reservaciones con proveedores
   extranjeros, descartado por limitaciones administrativas (pagos en dólares con tarjeta
   personal, sin facturas para justificar el gasto).

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: no está definido.
- **Información del negocio**: mezcla de sistemas y hojas de cálculo.
- **Comunicación**: WhatsApp y correo corporativo.
- Sin política de seguridad de datos formal. Regulación sectorial: Ministerio de Turismo +
  cumplimiento de la ley contra la delincuencia organizada, tráfico de estupefacientes y
  lavado de dinero (relevante para el manejo de datos financieros/fiscales, no se detalla en
  el deck visible, solo contexto interno de diseño).

## Universo y modalidad

- **~100 personas en toda la empresa**. Área corporativa/administrativa (alcance de este
  documento): **12 a 16 personas, incluyendo al Director General**. Cada hotel (área
  operativa, fuera de alcance) opera con menos de 20 personas.
- **1 persona por área a entrevistar** (8 sesiones) + Fundamentals grupal para el equipo
  corporativo/administrativo completo (dentro del máximo de 25 personas por sesión).
- **Modalidad**: Mixta.
- **Nivel de partida con IA**: nunca la han usado (adopción = 0). Sin formación previa, ni
  para Leudo ni para el equipo.
- **Presupuesto**: no definido aún. **Apertura al cambio**: Media. **Patrocinio ejecutivo**:
  fuerte y visible (Leudo es el patrocinador/campeón directo de esta iniciativa).
- **Urgencia**: ninguna declarada como evento de negocio. (Contexto interno no expuesto en el
  deck: la empresa compite por presupuesto con reparaciones estructurales por sismos recientes
  en sedes de Caracas — dato de venta, no de cara al cliente.)
- **Quién decide**: Leudo Gonzalez firma y decide directamente.

## Hacia dónde va esto (contexto, no cotizado en este documento)

El objetivo del Reporte Final es validar en qué procesos aplicar IA dado el tamaño reducido de
la empresa, con el equipo ya nivelado (Fundamentals, incluido en este DET-011), y sentar base
para una **futura capacitación puntual** en los cuellos de botella más evidentes (conciliación
bancaria/área contable) — mencionada como recomendación en el Reporte Final, **no cotizada**
en este documento.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Ajuste posterior (2026-09-14) — de 4h a 2h por área

Instrucción directa del usuario: reducir la duración de la sesión de área de **4h a 2h**
(16h en vez de 32h; 18h totales con Fundamentals en vez de 34h), manteniendo el **logro
inmediato dentro de la misma sesión**, solo que "algo corto" — es decir, no se elimina el
entregable insignia de cada sesión de área, se acorta su alcance para caber en la mitad del
tiempo.

- Todas las menciones de "4 horas"/"4h"/"32h"/"34h" en `index.html`, `programa.md`,
  `meta.json` y `acroforms.json` se actualizaron a 2h/16h/18h.
- El cronograma de la Etapa II (`.s-schedule`, slide 07/12, "Estructura de las 2 horas") se
  redistribuyó de 45'/90'/75'/30' (total 240') a **15'/45'/45'/15'** (total 120'): el bloque de
  "Construcción del logro inmediato" pasa de 75' a 45' (se acorta, pero sigue siendo el bloque
  más largo junto al levantamiento de procesos, no se recorta a un residual simbólico).
- No se tocó el alcance de las 8 áreas ni el resto de la estructura (Fundamentals sigue en 2h
  grupal, sin cambios).
- Regenerado el trío completo (`generar-pdf.sh` → `customize-acroforms.py` →
  `customize-hoteles-cumberland.py` si existe, o el genérico si no), verificador automático y
  revisión visual pendientes de confirmar tras este ajuste.

## Ajuste de alcance y bug encontrado (2026-09-09, segunda pasada)

Al reducir el alcance de 13 a 8 áreas (ver arriba), se alargó el `.hook-text` de la slide de
Impacto con una cláusula extra sobre el resto del área corporativa. Eso empujó la banda
`.impact-hook` una línea más, y tapó la última línea del chip `-57%` en `.gauge-panel .chips`
— colisión que `verificar-overflow.js` no detecta (mismo blindspot que las cajas AcroForm: son
dos elementos hermanos que se solapan, no un overflow de contenedor). Se corrigió acortando el
`.hook-text` de vuelta a ~4 líneas. Ver memoria `bug-impact-gauge-chips-collision.md`
(actualizada con esta segunda causa raíz).

## Bugs encontrados y corregidos durante la construcción (2026-09-09)

1. **Roadmap: choque horizontal `.rmx-ethics p` vs `.foot`**. El párrafo de la barra de ética
   (Etapa final) chocaba con el meta del pie ("HOTELES CUMBERLAND · DET-011") porque el nombre
   del cliente es más largo que en `farmaceutica-24/` — el mismo texto/CSS no colisionaba ahí
   por pura coincidencia de longitud de nombre. Fix: `padding-right: 230px` en `.rmx-ethics p`
   (aislado a este deck), en vez de acortar el texto (frágil ante cambios futuros de nombre).
2. **Precio: texto de "Cobertura" cortado dentro de la caja `Programa`**. Listar las 13 áreas
   completas (con nombres largos como "Ventas/Comercialización/Reservaciones/Marketing")
   excedía la capacidad visual de la caja AcroForm — se corta en el PDF sin que
   `verificar-overflow.js` lo detecte (ese script solo renderiza el HTML; el contenido de las
   cajas AcroForm se hornea después, fuera de su alcance). Fix: resumir a "toda la operación
   (Habitaciones, Alimentos y Bebidas, Comercial, back-office y sedes)" en vez de listar las 13
   por nombre — el detalle completo ya vive en el roadmap y en `programa.md`.

> Ambos bugs no los detecta el script automático — se encontraron por revisión visual del PDF
> renderizado, no del HTML. Confirmar siempre así antes de entregar (§4.10, checklist manual).

## Notas internas

- Caso base estructural: `farmaceutica-24/` (DET-010) — mismo patrón de 4h por área, logro
  inmediato, mención única de Claude, sin certificado, sin slide de Mapa de Calor. Se agrega
  una sesión de Fundamentals real (2h grupal) que Farmacéutica 24 no tenía.
- Impacto (§4.9): Hotel Tech Report — 2025 State of Hotel Guest Technology Report (58% de
  huéspedes cree que la IA puede mejorar su estadía, 70% encuentra útil un chatbot para
  solicitudes simples) + Kamran y Dastgeer (2025) — "The Impact of AI on Guest Satisfaction in
  Hotels" (tiempo de respuesta de 30 a 18 segundos, tasa de resolución de 90.6% a 95.5%, quejas
  negativas de 28% a 12%). Ambos verificados por fetch directo a la fuente.
