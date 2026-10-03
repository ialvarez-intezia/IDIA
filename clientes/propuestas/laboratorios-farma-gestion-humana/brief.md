# Brief — Laboratorios Farma · Gestión Humana regional (CAI-032)

## Actualización 2026-10-01 — Etapa 1 se recorta a 2 prácticas en básico; Etapa 2 (7 proyectos) pasa a ruta sin cotizar

Instrucción directa del usuario, 2026-10-01, con el detalle de "lo que debe incluir la Etapa 1".
Reestructura la propuesta: separa explícitamente una **Etapa 1** (lo que se cotiza ahora) de una
**Etapa 2** (la ruta que sigue, sin cotizar todavía) — vocabulario nuevo, distinto del "Etapa
1/2/3" interno del roadmap (ver nota de vocabulario más abajo).

### Etapa 1 — qué se cotiza

1. **Detección (2h, sin cambio de duración)**: sesión con los líderes o personas clave de las 6
   subáreas (Selección, Desarrollo, Nómina, Seguros, Bienestar, Seguridad y Salud Laboral), más
   el tema transversal de indicadores de gestión. Objetivo explícito: levantar cómo trabajan
   hoy, con qué herramientas (Microsoft 365, SAP, Excel, portal web de selección, control de
   acceso) y con qué permisos, para curar y cerrar los entrenamientos y las prácticas.
   - **Punto clave para el cliente (bloqueante de visibilidad)**: el resultado de la Detección
     debe dejar mapeado, proceso por proceso, qué licencia de Copilot necesita cada subárea y
     por qué. Ese mapa es el insumo con el que Claudia justifica ante la Gerencia Corporativa de
     TI la compra de licencias Business — en palabras del usuario, "lo que hizo que el cliente
     decidiera avanzar ya". **Decisión confirmada con el usuario (2026-10-01)**: la slide
     `.s-licenses` ("Licencias de Copilot por proceso") se reencuadra — deja de presentarse como
     una clasificación de Intezia a validar con Tecnología, y pasa a presentarse como el
     **entregable que produce la Detección**.
2. **Habilidades completo, para todo el equipo**: módulo compartido (3h, sin cambio de contenido
   ni duración) + **2 prácticas** de 2h cada una, no 7 proyectos finales:
   - **Ausentismo (Nómina)**: hoy Nómina cruza a diario el reporte de control de acceso con una
     macro de Excel, por hora, puerta y día de la semana.
   - **Selección (filtro de currículos)**: hoy revisan uno por uno los currículos que llegan por
     el portal web.
   - Ambas prácticas corren con **Copilot básico** (límite de 5 solicitudes diarias, el que el
     cliente ya tiene), trabajadas en una versión acotada a ese límite. La propuesta explica
     cómo se trabajan dentro del límite y qué mejora tendrían con Business (más volumen, sin
     tope diario). **Esto no contradice la clasificación de licencias ya escrita en el deck**
     (que marca Selección y Nómina como "Requiere Business"): esa clasificación describe la
     versión a **pleno volumen** de esos dos procesos, que pasa a la Etapa 2; la práctica de
     Etapa 1 es una primera versión, acotada al límite básico.
   - Audiencia de las 2 prácticas: **abiertas a todo el equipo** que quiera participar de otras
     áreas, mismo patrón que el resto del deck (confirmado con el usuario) — no restringidas
     solo a Nómina/Selección.
3. **Nuevo total Etapa 1**: Detección (2h) + módulo compartido (3h) + práctica Ausentismo (2h) +
   práctica Selección (2h) = **9h** (antes 19h en la versión 2026-09-30, que cotizaba los 7
   procesos completos).

### Etapa 2 — ruta sin cotizar (visión)

Los proyectos finales de 2h por subárea (Selección, Desarrollo, Nómina, Seguros, Bienestar,
Seguridad y Salud Laboral e Indicador de Gestión — 7 en total) pasan a la Etapa 2, una vez
Tecnología active las licencias Business. Quedan en la propuesta como la ruta que sigue, **sin
cotizarse todavía**, para que el cliente vea la visión completa y la Detección conecte directo
con ella.

- **Selección y Nómina en Etapa 2** (confirmado con el usuario): su proyecto final es una
  **profundización** de la práctica ya hecha en básico durante Etapa 1 — mismo proceso, ahora a
  pleno volumen, sin el límite de 5 solicitudes diarias. No es una entrada independiente ni una
  repetición.
- **Desarrollo, Seguros, Seguridad y Salud Laboral, Bienestar e Indicador de Gestión**: primera
  vez que tienen su proyecto final, con la licencia que la clasificación de Intezia ya señala
  para cada uno (ver tabla de 2026-09-30 más abajo, vigente para Etapa 2).
- Etapa 2 no tiene fecha fija: sigue condicionada a que Tecnología active Copilot Business, sin
  el plazo del 11 de diciembre (ver más abajo).

### Plazo de ejecución y orden de compra

"Ejecución antes del 11 de diciembre: la orden de compra debe salir en octubre." **Confirmado
con el usuario**: este plazo aplica **solo a Etapa 1** (lo cotizado). Etapa 2 sigue sin fecha
fija, condicionada a Tecnología.

### Calendario de Etapa 1 (borrador de Intezia, a confirmar con María/Claudia)

El usuario pidió que Intezia proponga un borrador (sin fechas concretas propias). Respetando
jueves/viernes/lunes, que Nómina no pare 2 días seguidos, y el cierre antes del 11 de diciembre
(con margen amplio, ya que la OC sale en octubre):

| Fecha | Sesión |
|---|---|
| Miércoles 14 de octubre | Kick-off · alcance y logística |
| Lunes 19 de octubre | Detección · mapeo con las 6 subáreas |
| Jueves 22 de octubre | Módulo compartido · Copilot |
| Lunes 26 de octubre | Práctica Ausentismo (Nómina) |
| Jueves 29 de octubre | Práctica Selección |

Verificación de la restricción de Nómina: el módulo compartido (jueves 22, incluye a Nómina) y
la práctica de Ausentismo (lunes 26) no caen en días consecutivos. **Pendiente de confirmar con
María/Claudia** antes de enviar — sin hora indicada todavía, mismo criterio que el calendario
anterior (`omitir-no-inventar-placeholder.md`).

### Estado de la propuesta

La propuesta ya estaba en `estado: "Enviada"` (`fecha_entrega: "2026-09-29"`). Por tratarse de
un reajuste sustancial de lo ya enviado, el `meta.json` pasa a `estado: "En corrección"`
(confirmado con el usuario, §4.19) — vuelve a `"Enviada"` automáticamente cuando se regenere el
PDF.

### Qué cambió en el deck (15 slides, sin cambio de cantidad)

Portada (lead), Objetivos (específicos), Programa (h2, meta, Módulo III), Licencias de Copilot
(reencuadre completo como entregable + nota de Etapa 1/Etapa 2 en las filas de Selección y
Nómina), Roadmap (tags internos renombrados de "Etapa 1/2/3" a "Paso 1/2/3" para no chocar con
el vocabulario nuevo; tarjetas de Habilidades/Resultado/insignia actualizadas a 2 asistentes),
Cronograma de prácticas (slide 09, antes "Proyecto final por proceso", ahora específico a
Ausentismo y Selección), Beneficios, Propuesta Económica (Duración 9h, Programa, ROI, Notas),
Seguimiento 30-60-90, Próximos pasos (Paso01-03, calendario con fechas fijas de Etapa 1) y Cierre
(`CierreResultado`/`CierrePaso3`, también en
`scripts/customize-laboratorios-farma-gestion-humana.py`). Diagnóstico e Impacto se mantienen
sin cambios: ninguno de los dos afirma algo que la nueva Etapa 1 contradiga.

### Nota de vocabulario — dos sentidos de "Etapa" en el mismo deck

El roadmap (slide 06) ya usaba "Etapa 1 · Detección / Etapa 2 · Habilidades / Etapa 3 ·
Resultado" como pasos internos de lo cotizado. El vocabulario nuevo del usuario usa "Etapa 1"
para **todo** lo cotizado (Detección + Habilidades) y "Etapa 2" para los 7 proyectos finales sin
cotizar. Para no mezclar ambos sentidos, los tags internos del roadmap se renombran a "Paso
1/2/3"; "Etapa 1" y "Etapa 2" quedan reservados, en todo el deck, al sentido nuevo (cotizado vs.
ruta futura).

---

## Actualización 2026-09-30 — de 5 grupos a 7 procesos, con licencia de Copilot por proceso

> **Vigencia actualizada (2026-10-01)**: esta sección describía el total cotizado (19h, 7
> procesos) en la versión anterior. Tras la actualización de arriba, el contenido de esta
> sección (los 7 procesos y su clasificación de licencia) sigue vigente, pero ahora describe la
> **Etapa 2** (ruta sin cotizar), no la Etapa 1. Ver la sección nueva arriba para el detalle de
> qué se cotiza hoy.

El usuario reportó un dato nuevo de la Ficha/conversación con el cliente: Copilot básico (GPT
5.6) trae un **límite de 5 requerimientos diarios**, y Gestión Humana evaluaría gestionar ante
la **Gerencia Corporativa de TI** la adquisición de licencias **Copilot Business**, con una
adopción por etapas que priorice primero las subáreas de mejor rendimiento. Instrucción
explícita del usuario: recotizar a **2h por proceso, 7 procesos en total**, dejando claro en la
propuesta cuáles procesos corren con la licencia básica y cuáles necesitan Business —
"seccionar la propuesta por área dejando claro quién usaría qué" — asumiendo el aumento de
horas que esto implica.

### De 5 grupos a 7 procesos

La agrupación de 5 grupos (Seguros + Seguridad y Salud Laboral combinadas, decidida el
2026-09-29) se **destraba**: cada subárea vuelve a tener su propia sesión, y se suma un 7mo
proceso que antes solo vivía dentro del módulo compartido:

1. Selección
2. Nómina
3. Desarrollo
4. Seguros
5. Seguridad y Salud Laboral
6. Bienestar
7. **Indicador de Gestión** (nuevo como proceso propio — antes era transversal, cubierto solo
   dentro del módulo compartido; ahora tiene su propio proyecto final de 2h porque cruza datos
   de las 6 subáreas y es, en sí mismo, un caso de uso real de Copilot)

**Nota de alcance**: la Ficha original no especificó una lista cerrada de "7 procesos" — se
reconstruyó como las 6 subáreas ya identificadas (sin agrupar) más Indicador de Gestión, que es
la pieza que quedaba pendiente de asignar una sesión propia. Confirmar con María/Claudia antes
de enviar si esta es la lectura correcta de los "7 procesos".

### Clasificación por licencia de Copilot (a validar con Tecnología antes de enviar)

Criterio aplicado: frecuencia de uso (diario vs. puntual) + sensibilidad del dato (personal, de
salud o de nómina vs. genérico) + volumen de interacción esperado en una sesión de 2h:

| Proceso | Licencia | Por qué |
|---|---|---|
| Desarrollo | **Copilot básico** | Detección de necesidades y comunicados: uso puntual, sin dato sensible. |
| Bienestar | **Copilot básico** | Redacción de comunicados de actividades: uso puntual, sin dato sensible. |
| Selección | Copilot Business | Filtra currículos y datos de candidatos a diario: volumen alto, dato personal. |
| Nómina | Copilot Business | Cruce diario de asistencia y datos de SAP: uso diario, dato de nómina. |
| Seguros | Copilot Business | Verificación de datos y reportes de pólizas: dato personal sensible. |
| Seguridad y Salud Laboral | Copilot Business | Inspecciones y cumplimiento normativo: dato de salud, sector regulado. |
| Indicador de Gestión | Copilot Business | Cruza datos de las 6 subáreas en un solo reporte: volumen alto de consultas. |

Esta clasificación es un **criterio razonado de Intezia, no un dato confirmado por Microsoft o
por Tecnología de Laboratorios Farma** — se muestra en la nueva slide 05/15 "Licencias de
Copilot por proceso" (`.s-licenses`) precisamente para que Claudia lo lleve a Gerencia
Corporativa de TI y lo valide antes de comprar licencias.

### Nuevo dimensionamiento

- **Detección**: 2h, sin cambios (sigue siendo 1 sesión conjunta con los líderes de las 6
  subáreas).
- **Habilidades**: módulo compartido 3h (sin cambios) + proyecto final 2h × 7 procesos = 14h.
- **Total: 19h** (antes 15h) — Detección (2h) + Habilidades (17h).

### Calendario (revisado)

Kick-off, Detección y módulo compartido mantienen sus fechas (7, 12 y 15 de octubre). Desarrollo
(viernes 16) y Bienestar (lunes 19) mantienen fecha fija porque arrancan ya con la licencia
básica. Los 5 procesos que dependen de Copilot Business **no llevan fecha fija** en el
calendario tentativo — se muestran como un solo bloque ("en cuanto Tecnología active Copilot
Business") para no crear una expectativa falsa sobre cuándo estará aprobada la licencia
(`omitir-no-inventar-placeholder.md`). Verificación de la restricción de Nómina: al no tener
fecha fija todavía, no hay riesgo de violar la regla de "no 2 días seguidos" — se revisará al
confirmar la fecha real.

### Qué cambió en el deck

15 slides (antes 14) — se agregó la slide 05/15 "Licencias de Copilot por proceso"
(`.s-licenses`, tarjetas propias reutilizando la paleta de marca, sin markers de AcroForm).
Se actualizaron: Portada, Diagnóstico (punto 5), Objetivos, Programa (h2, meta, Módulo III),
Roadmap (Etapa 2, Etapa 3, tarjeta de resultado), los 3 Cronogramas (chips, timebar, "Qué se
hace"/"Qué se logra"/"Recursos y entornos" del proyecto final ahora con 7 procesos), Beneficios,
Impacto (última frase del hook), Propuesta Económica (Duración, ROI), Seguimiento 30-60-90,
Próximos pasos (Paso01-03, calendario) y Cierre. AcroForms (`Entregables`, `Programa`, `Notas`,
`Paso01-03Body`) actualizados en `acroforms.json`; `CierreResultado`/`CierrePaso3` actualizados
en `scripts/customize-laboratorios-farma-gestion-humana.py`.

---

## Datos administrativos

- **Empresa**: Laboratorios Farma — farmacéutico, laboratorio con planta en Maracay, sede en
  Caracas (Los Ruices) y operación en Ecuador, Perú y Colombia.
- **Slug**: `laboratorios-farma-gestion-humana` (no `laboratorios-farma`: ese slug ya está
  tomado por `CAP-049`, un plan integral distinto de 2026-06-10, cliente Pedro, sin relación
  con este proyecto de Gestión Humana).
- **División Intezia**: `educacion` — cliente corporativo, sin ambigüedad.
- **Servicio (§4.1a)**: combo **Detección + Habilidades** — se registra `servicio: "deteccion"`
  en `meta.json`, mismo criterio de sistema que `simple-tv-det002/` y
  `banco-plaza-copilot-producto/` (memoria `combo-deteccion-habilidades-codigo-vs-servicio.md`).
  **Código**: el usuario pidió explícitamente `CAI-032` — se respeta tal cual, independiente del
  prefijo `DET-` que tomaría una Detección sola.
- **Tipo de documento**: Capacitación In-Company con fase previa de Detección (`CAI-032`).
- **Fecha del brief**: 2026-09-29
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Laboratorios Farma**
(`Levantamiento_Laboratorios_Farma_2026-09-29.pdf`, registrada 2026-09-29), elaborada por la
asesora **María Iribarren**, más instrucciones directas del usuario sobre estructura, calendario
y agrupación de subáreas.

## Contacto

- **Asesora comercial**: María Iribarren.
- **Contacto cliente**: Claudia Hernández · Gestión Humana, planta Maracay (20 años en la
  empresa) · campeona interna, presenta la propuesta a su gerencia y dirección.
- **Canal operativo**: Nelson González Colmenares · Gestión Humana (temporal).
- **Servicio previo con Intezia**: **sí** — Tecnología de Laboratorios Farma ya recibió
  capacitación (+120 personas en 2 verticales: 80 líderes en fundamentos y agentes en Caracas,
  40 de TI en ética y ciberseguridad) y un webinar de 1h en 2025. Intezia está registrada como
  proveedor. Esta propuesta es la **primera de Gestión Humana**, área nueva, sin relación con la
  cuenta de Tecnología ni con el plan integral `CAP-049` (2026-06-10, contacto Pedro, sin
  avanzar) que ya vive en la carpeta `laboratorios-farma/`.

## Qué pide el cliente (ficha + instrucción directa del usuario)

1. **Detección (2h)**: una sola sesión conjunta con los líderes o personas clave de cada una de
   las 6 subáreas, para levantar cómo trabajan hoy (herramientas, portal, SAP, Excel, permisos)
   y curar el contenido y las prácticas de Habilidades antes de construir nada.
2. **Habilidades**:
   - **Módulo compartido** (todo el equipo junto): ecosistema Microsoft y Copilot, qué es un
     asistente y para qué sirve, cómo conectarlo con Outlook, Teams, Excel y Word.
   - **Proyecto final por subárea** (2h cada una): cada subárea construye en vivo su asistente
     sobre su cuello de botella principal, con las sesiones abiertas a quien quiera participar
     de otras áreas.
3. **Modalidad**: virtual por Teams, en sesiones de 2h, preferible jueves, viernes o lunes.
   Nómina no puede parar 2 días seguidos (nómina semanal en la planta).
4. **Pedido explícito de Claudia** (ficha, cita textual): responder con claridad cuántos
   subgrupos o proyectos finales incluye la propuesta y qué queda fuera, "para no crearnos una
   expectativa falsa".

## 6 subáreas → 5 grupos (decisión de agrupación, a pedido del usuario) — superada 2026-09-30

> **Superada por la actualización 2026-09-30** (ver arriba): la agrupación de Seguros +
> Seguridad y Salud Laboral se deshizo y el indicador de gestión pasó de "cubierto dentro del
> módulo compartido" a ser su propio 7mo proceso. Se conserva esta sección por trazabilidad del
> razonamiento original (por qué Seguros y Seguridad y Salud Laboral se veían como un mismo
> perfil de tarea), no como estado vigente.

La ficha lista **6 subáreas** de Gestión Humana (Selección, Desarrollo, Nómina, Seguros,
Bienestar, Seguridad y Salud Laboral) pero registra una nota interna sin resolver: *"Son 6
subáreas (María dijo 5 en la sesión): definir si Seguridad y Salud Laboral va sola o se agrupa
con Bienestar o Seguros."* El usuario pidió explícitamente ayuda para decidir esta agrupación y
dejarla clara en la propuesta. Decisión tomada:

**Seguridad y Salud Laboral se agrupa con Seguros** (no con Bienestar) — ambas subáreas comparten
el mismo perfil de tarea: verificación de datos contra una base y generación de reportes/
cumplimiento, mientras que Bienestar es 100% redacción de comunicados, un perfil distinto. Esto
da **5 grupos** (el número que María ya había anticipado en la sesión), cubriendo las **6
subáreas sin dejar ninguna fuera**:

1. **Selección** — revisión y filtrado de currículos, mensajes a candidatos por etapa y de
   cierre, solicitud de documentos y verificación de referencias.
2. **Nómina** — cruce diario de asistencia (control de acceso vs. Excel) y verificación de datos
   de SAP en Excel.
3. **Desarrollo** — detección de necesidades de capacitación, búsqueda de proveedores y
   comunicados.
4. **Seguros y Seguridad y Salud Laboral** (combinadas) — verificación de datos y reportes de
   Seguros + inspecciones y cumplimiento del plan de Seguridad y Salud Laboral.
5. **Bienestar** — redacción de comunicados de actividades.

El indicador de gestión (transversal a las 6 subáreas) no es un grupo aparte: se cubre dentro
del módulo compartido (ecosistema Microsoft/Copilot aplicado a reportes) y como hilo conductor
del Reporte Final, no como una 6ta sesión de proyecto final.

## Dimensionamiento — superado 2026-09-30, ver "Nuevo dimensionamiento" arriba

- **Detección**: 2h, sesión única conjunta (no 4h por subárea: el propio usuario definió la
  Detección como "una sesión" con los líderes de las 6 subáreas, consistente con la ESTRUCTURA
  ACORDADA de la ficha). Sin cambios tras la actualización 2026-09-30.
- **Habilidades (histórico, antes de 2026-09-30)**: módulo compartido 3h (dato explícito de la
  ficha, "3h mencionadas" en la ESTRUCTURA ACORDADA) + proyecto final 2h × 5 grupos = 10h.
- **Total histórico: 15h** (2h Detección + 13h Habilidades) — reemplazado por 19h (ver arriba).
- No se aplicó la regla general de Habilidades (8-12h/área) de
  `empresa/politicas-comerciales.md`: esa regla está pensada para automatizar procesos
  discretos de una sola área con profundidad, no para varios procesos con 1 proyecto final de
  2h cada uno más un módulo compartido — mismo criterio de juicio razonado ya aplicado en
  `hjb-quimica/CAI-031` (ver su brief.md, "Decisiones de diseño"). Este criterio sigue vigente
  con 7 procesos.

## Universo

- **20 personas** de Gestión Humana en 4 países: Venezuela (planta Maracay + Caracas, la
  mayoría), Ecuador (3), Perú (2), Colombia (3) + Nelson González y María Ángel (temporales).
  Por confirmar si participa la jefa de Gestión Humana.
- En Perú y Ecuador, equipos pequeños: una misma persona puede llevar varias subáreas a la vez
  (selección, nómina, capacitación) — no cambia la estructura de 7 procesos, cambia quién asiste
  a cuál sesión desde esos países.

## Stack y restricciones (contexto interno, §4.11 — sin afirmar migración)

- **Ecosistema**: Microsoft 365. Copilot ya estaría licenciado (Claudia cree que todos tienen
  licencia, pero debe confirmarlo con Leonardo de Tecnología). **No se afirma en el deck que
  las licencias ya están confirmadas** — se deja como nota interna (`Notas` del AcroForm).
- **Otros sistemas**: SAP (nómina), portal propio "Trabaja con Nosotros" (selección), sistema
  de control de acceso (asistencia), Excel con macros, Word.
- **Dato sensible**: SAP es delicado — toda conexión con IA requiere permisos de Tecnología
  (Leonardo) y validación de la normativa interna (Pedro Romero). El deck deja explícito que
  los asistentes trabajan dentro de Copilot y los archivos que cada grupo ya maneja, sin tocar
  SAP ni el portal de selección directamente — esa conexión queda fuera de este alcance
  (`rmx-ethics` en el roadmap + `Notas` del AcroForm).
- **Regulación**: sector Salud.

## Calendario tentativo (a pedido explícito del usuario, 2026-09-29) — revisado 2026-09-30

Histórico (previo a la actualización 2026-09-30): kick-off miércoles 7 de octubre, Detección
lunes 12, módulo compartido jueves 15, y los 5 grupos entre el viernes 16 y el viernes 23 de
octubre (Seguros y Seguridad y Salud Laboral combinadas, Bienestar el mismo día en otro
horario). Verificación de la restricción de Nómina (no 2 días seguidos) sin violaciones en ese
calendario.

**Calendario vigente (2026-09-30)**: Kick-off, Detección y módulo compartido mantienen sus
fechas (miércoles 7, lunes 12 y jueves 15 de octubre). Desarrollo (viernes 16) y Bienestar
(lunes 19) mantienen fecha fija porque corren con la licencia básica actual. Los 5 procesos que
dependen de Copilot Business (Selección, Nómina, Seguros, Seguridad y Salud Laboral, Indicador
de Gestión) **no llevan fecha fija todavía** — se calendarizan en cuanto Tecnología confirme la
activación de las licencias Business, para no crear una expectativa falsa sobre cuándo estará
disponible (mismo criterio de `omitir-no-inventar-placeholder.md`). Al confirmar esas fechas,
revisar de nuevo la restricción de Nómina (no 2 días seguidos).

Sin horario indicado por el usuario para ninguna sesión — se omiten los `.cal-time` de
`.steps-calendar` en vez de inventar un horario (`omitir-no-inventar-placeholder.md`), igual
que en `fibraspol/DET-024`. Confirmar horario con María antes de enviar.

## Impacto (§4.9)

**Microsoft & LinkedIn — 2024 Work Trend Index Annual Report** (encuesta a 31,000 trabajadores
en 31 mercados, Edelman Data & Intelligence, 2024) — memoria
`fuente-impacto-byoai-gobernanza-dispersa.md`, perfil de uso disperso de IA sin gobernanza,
exactamente el caso de Gestión Humana (uso autodidacta, sin criterio común, licencias de
Copilot sin confirmar):

- **78%** de quienes usan IA hoy llevan sus propias herramientas al trabajo, sin gobernanza
  corporativa.
- **39%** de los usuarios de IA recibió alguna capacitación formal de su empresa.
- **60%** de los líderes admite que su empresa no tiene una visión ni un plan de IA.
- **59%** de los líderes no sabe cómo cuantificar el retorno de la IA (conecta con el ROI de la
  Propuesta Económica).

## Decisiones confirmadas / sin ambigüedad

1. **7 procesos, 6 subáreas cubiertas** (actualizado 2026-09-30) — Seguros y Seguridad y Salud
   Laboral ya no comparten sesión, y se suma Indicador de Gestión como 7mo proceso. Cada
   proceso lleva marcada su licencia de Copilot (básico o Business). Explícito en Objetivos,
   Programa, la slide de Licencias y Beneficios del deck, respondiendo directo al pedido de
   Claudia de claridad de alcance.
2. **Con certificado de participación INTEZIA** — hay componente real de Habilidades (7h de
   práctica en Etapa 1: 3h módulo compartido + 2h Ausentismo + 2h Selección; 14h adicionales en
   Etapa 2, sin cotizar), a diferencia de una Detección pura (`deteccion-sin-certificado.md`).
3. **Con Garantía y Seguimiento 30-60-90** — mismo criterio que cualquier deck con Habilidades
   real (`seguimiento-30-60-90-habilidades.md`).
4. **Con descuento urgente, ROI y calendario de inicio** en la Propuesta Económica
   (`hoja-cotizacion-cierre-venta.md`) — Ficha Comercial disponible.
5. **Sin afirmar migración de stack (§4.11)**: Microsoft 365 y Copilot ya son el entorno del
   cliente: el deck dice que los asistentes se integran a ese entorno, nunca que Laboratorios
   Farma migra o adopta un stack nuevo.
6. **Sin prometer conexión directa con SAP ni el portal de selección** — límite explícito,
   reforzado en el roadmap (`rmx-ethics`) y en `Notas`.

## Hallazgo de diseño (2026-09-29) — glitch de `<strong>` también en `.impact-hook .hook-text`

El párrafo largo de `.impact-hook .hook-text` (slide de Impacto) mostró el mismo glitch de
renderizado ya documentado para `.s-goals .general p` (§4.8): una línea tipo subrayado bajo el
`<strong>`, sin importar qué palabra se envuelva. Se probó con una frase larga envuelta y luego
con una sola palabra corta ("Detección") en medio de línea — el glitch persistió en ambos
casos, así que no es un problema de wrap sino del contenedor. Se resolvió quitando el
`<strong>` de ese párrafo por completo. Vale la pena confirmar en el sistema si `.impact-hook
.hook-text` debería sumarse a la lista de contenedores sin `<strong>` de §4.8, además de
`.s-goals .general p`.

## Notas internas

- Caso base estructural para la mecánica de "sesión compartida + N sesiones por subgrupo, una
  sola cotización": `farmaceutica-24/DET-010`. Caso base para el shell visual vigente
  (Beneficios v3, Cierre escalera, roadmap `.rmx-linear`, descuento urgente + ROI + garantía
  30-60-90 + `.s-followup`, `.steps-calendar`): `hjb-quimica/CAI-031` (overrides.css clonado de
  ahí, recortando los bloques `.s-vision`/`.s-incluye` que no aplican a este deck de 1 sola
  ruta).
- **Pendientes (a confirmar con María/Claudia antes de enviar)**:
  - Calendario de Etapa 1 (borrador de Intezia, 2026-10-01): confirmar las 5 fechas propuestas
    (14, 19, 22, 26 y 29 de octubre) y la hora de cada sesión — solo hay día, no hora.
  - Licencias de Copilot para Etapa 2: validar con Leonardo (Tecnología) la clasificación
    básico/Business de los 5 procesos que todavía no se practican (criterio razonado de
    Intezia) y gestionar la compra de Business ante la Gerencia Corporativa de TI.
  - Fecha de Etapa 2, una vez Tecnología confirme la activación de Copilot Business (sin plazo
    del 11 de diciembre, que aplica solo a Etapa 1).
  - Si participa la jefa de Gestión Humana (por confirmar según la ficha).
  - ~~Confirmar si "Indicador de Gestión" como 7mo proceso es la lectura correcta~~ — resuelto:
    queda como 7mo proceso de Etapa 2 (ver actualización 2026-10-01).
