# Brief — Docencia con IA · Ecosistema Google (TA-031)

## Datos administrativos

- **Empresa / Institución**: ninguna en particular. **Producto de catálogo para
  presentar a varios colegios** a través de una aliada externa a Intezia. No es un
  requerimiento formal de un cliente — se arma para que la aliada lo muestre a los
  colegios de su red y, según el interés que genere, se personalice por institución.
- **Slug**: `docencia-ia-google`
- **División Intezia**: `educacion`
- **Tipo de documento**: Taller (`TA-031`)
- **Programa**: Docencia con IA · Ecosistema Google
- **Eje temático**: IA aplicada a la práctica diaria del profesor de colegio, con foco
  exclusivo en el ecosistema de Google (Gemini, NotebookLM, Google Workspace) — no es
  la versión multi-herramienta de `catalogo/TA-013 Docencia con IA` (esa convive
  intacta como oferta agnóstica de proveedor).
- **Fecha del brief**: 2026-07-28
- **Estado**: borrador — propuesta genérica, sin colegio asignado aún

## Origen

Una aliada comercial (externa a Intezia) pidió apoyo para armar una propuesta de
capacitación en IA para profesores de colegio, que ella quiere presentar a varios
colegios de su red. No hay un colegio específico todavía: el objetivo es tener un
deck atractivo y flexible que sirva como pieza de venta general, personalizable por
institución una vez haya interés concreto.

## Por qué Google / NotebookLM

Pedido explícito del usuario: enfocar el programa en las herramientas de IA de
Google, con **NotebookLM** como pieza central (source-grounded: convierte el
currículo y material propio del profesor en planificaciones, guías de estudio y
Audio Overviews), más Gemini dentro de Workspace (Docs, Slides, Sheets, Vids, Gmail,
Classroom). Muchos colegios ya usan Google Workspace for Education a diario — el
programa se apoya en ese entorno que ya tienen, no exige adoptar herramientas nuevas
(coherente con §4.11: nunca se afirma que el colegio migra de stack).

## Necesidad detectada (genérica del aula)

1. El profesor está saturado entre planificar clases, corregir y redactar reportes
   — el tiempo no alcanza para lo que de verdad importa: enseñar y acompañar.
2. Preparar material de calidad (guías, presentaciones, videos) consume horas fuera
   del horario de trabajo, casi siempre en la casa y de noche.
3. Revisar y retroalimentar el trabajo de decenas de estudiantes se lleva noches y
   fines de semana enteros.
4. La comunicación con representantes (informes, correos, seguimientos) se acumula
   sin un sistema, y cada profesor la resuelve a su manera.
5. El colegio ya paga y usa Google Workspace a diario, pero pocos profesores saben
   que Gemini y NotebookLM viven ahí mismo, listos para usarse sin curva de entrada.

## Especificaciones del programa

- **Duración**: 12 horas académicas (3 sesiones × 4 horas · 1 sesión por semana)
- **Modalidad**: Híbrido — Sesión 1 presencial (introducción práctica en el colegio),
  Sesiones 2 y 3 online síncronas. Ajustable por colegio en la personalización.
- **Audiencia**: docentes de educación primaria, secundaria y bachillerato. Base
  mínima piloto de **50 personas** (cotización del lado del usuario, fuera de este
  sistema) — pensada para agrupar varios colegios o todo el cuerpo docente de uno
  grande en un solo piloto.
- **Estructura**: 6 módulos · 5 temas por módulo · agrupados en 3 sesiones de 2
  módulos cada una (mismo patrón de `corpoez-cu009`: "Módulos I-II", "III-IV", "V-VI")
- **Ecosistema**: Google — Gemini, NotebookLM, Google Workspace (Docs, Slides,
  Sheets, Vids, Gmail, Classroom, Calendar)
- **Acreditación**: certificado de participación INTEZIA Education
- **Fechas**: por confirmar según el colegio interesado

## Módulos (a la medida — el colegio elige énfasis, no todo es obligatorio)

1. Planificación curricular con NotebookLM
2. Fábrica de contenido pedagógico (Slides, Vids, material visual)
3. Evaluación y feedback con IA
4. Comunicación con representantes
5. Gestión administrativa y tiempo
6. Ética y uso responsable en el aula

## Equipo asignado

- **Facilitador**: por confirmar — Equipo INTEZIA Education designa según el colegio.
- **Coordinación**: Equipo INTEZIA Education, punto único de contacto.

## Notas comerciales internas (no entran al deck)

- Cotización a cargo del usuario sobre una base piloto mínima de 50 docentes; grupos
  o colegios adicionales se cotizan por separado según el interés que genere la
  aliada. Los 5 campos de precio del AcroForm quedan vacíos — los llena ventas por
  colegio.
- Vigencia de la propuesta: 30 días (§3). Anticipo 50 %, cancelación <7 días no
  reembolsable — políticas estándar, no se detallan en el deck salvo que el colegio
  lo pida.
- Slide de Impacto con datos reales de Gallup / Walton Family Foundation — *Teaching
  for Tomorrow: Unlocking Six Weeks a Year With AI* (2025, n=2,232 docentes públicos
  EE. UU.): 60 % de docentes usó IA en el año escolar 2024-25; quienes la usan cada
  semana ahorran 5.9 h/semana (~6 semanas al año); mejora de calidad percibida de 57 %
  (evaluación/feedback) a 74 % (trabajo administrativo).

## Decisiones de plantilla (esta versión)

- Clonado del canónico mono-fase `cumbre-andina/` (Taller, división Educación).
- **6 módulos** (no 3): el pedido explícito del usuario es mostrar varios frentes de
  capacitación a la medida — activa el modo compacto de `.s-program` ya soportado en
  `_base/styles.css` para 5-6 módulos. Sin `overrides.css` necesario.
- **3 slides de cronograma** (no 6): 2 módulos por sesión, mismo patrón que
  `corpoez-cu009` — evita inflar el deck a 16 slides, mantiene los 13 canónicos.
- Sin "Empresa" en portada/pie — es Taller genérico sin cliente asignado; los pies de
  slide dicen "Docencia con IA · Google · Propuesta" en vez de nombre de empresa.
- Slide de Propuesta Económica presente pero con los 5 campos de precio vacíos
  (§4.14) — el usuario cotiza aparte sobre la base de 50 personas.
- Próximos pasos: logística genérica (fechas, acceso/agenda, kick-off), sin nombrar
  un colegio — listo para que ventas lo adapte al colegio real cuando aparezca.
