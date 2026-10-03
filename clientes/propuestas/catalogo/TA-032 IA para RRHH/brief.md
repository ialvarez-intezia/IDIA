# Brief — Catálogo · IA para RRHH (TA-032)

> **Producto de catálogo, no propuesta a cliente final.** Plantilla lista para cotizar a
> cualquier empresa que quiera nivelar a su equipo de RRHH en IA. Cotización y datos del
> cliente final se completan al personalizar. Mismo patrón que `TA-001` / `TA-014`.

## Datos administrativos

- **Slug**: `catalogo/TA-032 IA para RRHH`
- **División Intezia**: `educacion` (corporativo/profesional)
- **Tipo de documento**: Taller (`TA-032`) · mono-fase, mismo canon de `cumbre-andina/`
- **Programa**: IA para RRHH, prompting legal, asistentes de selección (Gemas), acceso a
  Claude, análisis de datos e indicadores, y sistemas de gestión del desempeño
- **Eje temático**: uso de IA generativa en el día a día de RRHH con **Gemini** (Módulos I-II)
  y **Claude** (Módulos III-V, acceso mediante VPN), con foco explícito en Venezuela (LOTTT)
  heredado del contenido fuente
- **Alianza**: **GerenSer Venezuela C.A.** (J-41249018-4) participa como **tutor aliado**,
  aportando ejemplos prácticos y aplicabilidad real del contenido en cada módulo. Co-marca en
  portada y pie de cada slide (logo GerenSer junto al de Intezia, separados por línea vertical,
  mismo peso visual — `empresa/marca-visual.md` regla 6).
- **Fecha del brief**: 2026-08-07
- **Estado**: `Borrador`

## Origen del contenido

Contenido curricular aportado por GerenSer Venezuela (carta del 2026-07-07, "Formación de IA
para RRHH", 8 módulos). Se adaptó a formato taller de catálogo Intezia:

1. **Herramienta**: el brief original mencionaba GPTs personalizados (ChatGPT) para asesoría
   legal, reclutamiento, evaluación, etc. Una primera versión tradujo todo el contenido a
   Claude como herramienta única. **Ajuste 2026-08-12, a pedido de GerenSer Venezuela**: en
   Venezuela, tanto ChatGPT como Claude requieren VPN para uso corporativo estable; **Gemini**
   no, por lo que es la opción más idónea para el perfil real de los clientes de este catálogo.
   El taller queda así: **Gemini como herramienta principal de práctica** (todo el programa es
   ejecutable con una cuenta Gemini gratuita), **Claude integrado como complemento** (mismas
   plantillas de prompt, portables a Claude cuando el participante tenga acceso), y **ChatGPT
   excluido definitivamente**: nulo uso registrado en las últimas ediciones del taller. El
   programa enseña a construir y guardar **plantillas de prompt reutilizables** (biblioteca de
   prompts en un documento) que funcionan solo copiando y pegando, sin depender de Projects,
   API ni ningún plan de pago. Módulo I conserva un panorama comparativo breve de otros modelos
   (Gemini, Claude, DeepSeek, Copilot; sin ChatGPT), no como herramienta de práctica, solo
   contexto. La mayoría de los participantes son profesionales de RRHH que aprenden IA desde
   cero: todo el programa asume cero conocimientos previos de programación.
2. **Sin fechas**: producto de catálogo, sin calendario fijo — se agenda al cerrar con cada
   cliente.
3. **8 módulos → 4 módulos de programa + 4 sesiones**: la Programa slide (`.s-program`) admite
   3-6 módulos legibles (`plantillas/capacidad-cajas.md`); se agruparon los 8 módulos
   originales en pares por sesión, 1 macro-módulo = 1 sesión = 2h:
   - **Módulo I** (Sesión 1): Fundamentos de IA en RRHH + Prompt Engineering y asesoría legal
     laboral (client Módulos 1-2)
   - **Módulo II** (Sesión 2): Reclutamiento y selección + Experiencia del empleado (client
     Módulos 3-4)
   - **Módulo III** (Sesión 3): Evaluación de desempeño + Cálculos laborales (client Módulos
     5-6)
   - **Módulo IV** (Sesión 4): Auditoría de RRHH + IA operativa (client Módulos 7-8)
   Orden de los 8 módulos originales y carga horaria respetados: 1 sesión semanal de 2h, 2
   módulos por sesión, 4 semanas — igual que la carta original de GerenSer.
4. **Sin Mapa de Calor**: `cumbre-andina` (deck base) no lo incluye por defecto; se confirma
   explícitamente que este taller no lleva esa slide (es un bloque add-on de
   `plantillas/slides/`, solo para diagnósticos previos — no aplica a un producto de catálogo
   sin cliente auditado).
5. **Términos y condiciones en la hoja de cotización** (formato adoptado de `CAP-082`
   Aerocentro, 2026-08-06): caja "Importante" con borde naranja en `.s-price`, enlace real y
   clicable a los T&C institucionales. Mismo enlace que usa CAP-082:
   `https://drive.google.com/file/d/1PA-ZSt4KnyY5dpxXzgkIk6-yfGlV2eF8/view?usp=drive_link`
   (no vive en el AcroForm porque los campos de formulario no soportan hipervínculos).
6. **Estrategia comercial 2026-08-12 (cierre con producto instalable)**: el Módulo IV deja de
   cerrar solo con un plan de acción en papel. El taller construye un **prototipo real de
   automatización de cribado de currículums**: una plantilla de Google Sheets + Apps Script
   pre-armada (sin necesidad de programar) que cada participante personaliza con sus propios
   criterios y activa con Gemini, lista para instalarse en el subsistema de Reclutamiento de su
   empresa. Objetivo: dejar un entregable tangible que abra la puerta a fidelizar al cliente y
   ofertar proyectos de automatización futuros (mantenimiento, extensión a otros subsistemas de
   RRHH, integración más profunda). No se afirma que el cliente migra de stack (§4.11): la
   automatización se integra a su entorno de trabajo existente.
7. **Reestructuración 2026-08-18 (contenido curricular de GerenSer Venezuela, versión
   ampliada): 4 módulos/8h → 5 módulos/10h, 5 semanas.** GerenSer entregó una ruta formativa
   nueva y más completa, ya organizada en 5 módulos (uno por semana, 2h cada uno), que
   **reemplaza** la agrupación de 8 sub-módulos en 4 macro-módulos de la versión anterior:
   - **Módulo I** — Fundamentos de IA y consultas especializadas en materia laboral (Gemini).
   - **Módulo II** — Creación de asistentes especializados (Gemas) para el proceso integral
     de selección (Gemini, Gestor de Gemas).
   - **Módulo III** — Introducción a Claude, acceso desde Venezuela y análisis de data
     laboral (Claude + una herramienta de VPN gratuita).
   - **Módulo IV** — Procesamiento de data compleja e indicadores de desempeño con Claude.
   - **Módulo V** — Sistemas expertos interactivos para gestión del desempeño con Claude
     Projects y Artifacts.
   Este cambio **reintroduce a Claude como herramienta central** (Módulos III-V, no solo
   complementaria) y con ella la necesidad de VPN para acceder desde Venezuela — GerenSer
   decidió sumar ese módulo de acceso en vez de evitarlo como en el ajuste de 2026-08-12.
   **Instrucción explícita del usuario**: no nombrar la marca de la VPN en ningún material de
   cara al cliente (deck, AcroForms) — solo mencionar genéricamente "una herramienta de VPN
   gratuita" o "una VPN gratuita". El deck pasa de 14 a 15 slides (5 slides de cronograma en
   vez de 4). El prototipo instalable de automatización de cribado de currículums descrito en
   el punto 6 **se retira** de este programa: el cierre ahora es el sistema de gestión del
   desempeño en Claude Projects (Módulo V).

## Diagnóstico (5 puntos, genérico de la audiencia RRHH)

1. Cada colaborador de RRHH usa IA (o no la usa) por su cuenta, sin método ni criterio común.
2. Las tareas de cálculo laboral, redacción de cartas y reportes dependen de tiempo manual,
   repetido caso por caso.
3. El filtrado de currículums y el diseño de perfiles de cargo se hacen sin apoyo de IA, o de
   forma improvisada.
4. No hay plantillas de prompt reutilizables: el conocimiento vive en la cabeza de quien lo usa,
   no se comparte en el equipo.
5. Falta un criterio común para auditar procesos de RRHH y sostener indicadores clave (rotación,
   ausentismo, clima laboral) con apoyo de IA.

## Especificaciones del programa

- **Duración**: 10 horas académicas · 5 sesiones de 2h · 1 sesión semanal (ruta formativa de
  5 semanas, actualizada 2026-08-18).
- **Modalidad**: Online Síncrono recomendado (ajustable a Presencial/Híbrido al personalizar).
- **Estructura**: 5 módulos de programa (1 macro-módulo = 1 sesión) · ver mapeo arriba.
- **Perfil de ingreso** (Taller): profesionales de RRHH (analistas, generalistas, líderes de
  talento humano) que aprenden IA desde cero · sin conocimientos previos de programación ·
  cuenta de Gemini (Módulos I-II, plan gratuito, sin VPN) y cuenta de Claude (Módulos III-V,
  acceso mediante una herramienta de VPN gratuita) y conexión a internet.
- **Audiencia objetivo**: equipos de RRHH de empresas medianas y grandes.
- **Acreditación**: INTEZIA Education + GerenSer Venezuela (aliado tutor).

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Producto de catálogo: cotización personalizada por cliente y número de participantes.
- Programa registrado como **TA-032** en INTEZIA Education al cerrar el acuerdo.

## Notas de diseño

- Clon de `cumbre-andina/` (canónico mono-fase), enlaza `../../_base/styles.css` (ruta desde
  `catalogo/TA-032.../`) + `overrides.css` local para: caja de T&C en `.s-price` (patrón
  CAP-082) y co-marca de GerenSer en portada/pie (logo propio, mantiene su identidad de color;
  `empresa/marca-visual.md` regla 6).
- **15 slides** (13 del canon + 2 slides de cronograma extra, porque el programa tiene 5
  sesiones en vez de 3, actualizado 2026-08-18).
- CTA de cierre como `<span class="cta">Solicita tu Propuesta</span>` (no `<a>` con Calendly),
  mismo criterio que `TA-001`/`TA-014`: producto de catálogo sin fecha de entrega específica a
  la que atar el mes de un link de agenda.
- Cierre con asesora comercial nombrada: Verónica Rubio (+58 412 4723186 · vrubio@intezia.com),
  además de los datos institucionales (actualizado 2026-08-07, a pedido del usuario).
- §4.12: LOTTT (Ley Orgánica del Trabajo, los Trabajadores y las Trabajadoras) se expande la
  primera vez que aparece, en cada slide donde aparece. VPN no se expande (excepción §4.12:
  sigla de uso general) y **no se nombra su marca** en ningún material de cara al cliente
  (instrucción del usuario, 2026-08-18): siempre "una VPN" o "una herramienta de VPN gratuita".
- §4.11: en ningún momento se afirma que el cliente migra de su stack de RRHH. Gemini y Claude
  se presentan como herramientas que se integran al flujo de trabajo existente; la
  automatización final (Módulo IV) se presenta como algo que se instala dentro del subsistema
  de Reclutamiento del cliente, no como un cambio de plataforma.
- **2026-08-12: título neutro.** El nombre del producto y la portada dejan de nombrar una
  herramienta específica ("IA para RRHH", sin "con Claude"). Dentro del contenido sí se nombra
  a Gemini (principal) y Claude (complementario) donde ayuda a que ventas entienda el enfoque.

## Pendientes

- Confirmar con GerenSer si desea aparecer también en el AcroForm `Acreditacion` (hoy dice
  "INTEZIA Education"; se puede sumar una línea de acreditación conjunta).

## Estado de entrega

- Logo de GerenSer recibido y guardado en `logos/gerenser/logo.jpeg` (2026-08-07).
- PDF generado y AcroForms pre-llenados (`generar-pdf.sh` + `customize-acroforms.py`).
- Verificador automático (`verificar-propuesta.sh`) y detector de desborde
  (`verificar-overflow.js`) en verde. Revisión visual de las 14 slides del PDF hecha a 220dpi:
  sin overflow, sin logos solapados. Se corrigieron 2 defectos que el detector automático no
  cazó (no visibles en HTML, solo en el PDF renderizado):
  - Slide 10 (Beneficios): caja `Entregables` desbordaba con 4 destacados largos + 3
    institucionales (11+ líneas visuales en una caja con capacidad ~9-11). Se redujo a 3
    destacados cortos de una línea.
  - Slide 11 (Impacto): el valor `+10 a 30%` de la barra "Productividad esperada" desbordaba
    el ancho de un fill de 25% y se solapaba con el label. Se acortó a `+20%` (representativo)
    con el rango completo movido al label de la fila (`Productividad esperada (10-30%)`).
- **2026-08-12: reposicionamiento de herramientas + cierre comercial (feedback GerenSer).**
  Gemini pasa a ser la herramienta principal de práctica en todo el taller (Módulos I-IV),
  Claude queda como complemento y ChatGPT se excluye definitivamente. Título y portada se
  vuelven neutros ("IA para RRHH", sin nombrar herramienta). El Módulo IV cambia su cierre de
  "plan de acción" a un prototipo instalable de automatización de cribado de currículums
  (Google Sheets + Apps Script + Gemini, sin programar), pensado como gancho de fidelización
  y venta futura. Se actualizaron `brief.md`, `programa.md`, `index.html`, `acroforms.json`,
  `meta.json` y `overrides.css`. Regenerado el PDF (`generar-pdf.sh` + `customize-acroforms.py`,
  par obligatorio), `verificar-propuesta.sh` en verde, y revisión visual de las 14 slides a
  130dpi: sin overflow, sin logos solapados, sin ChatGPT ni acuerdos económicos en "Cómo
  arrancamos".
- **2026-08-18: reestructuración a ruta formativa de 5 semanas / 10 horas (contenido nuevo de
  GerenSer Venezuela, ver punto 7 de Origen del contenido).** El programa pasa de 4 módulos/8h
  a **5 módulos/10h**: Legal Laboral con IA (Gemini) → Selección con Gemas (Gemini) → Acceso y
  Uso de Claude (VPN) → Datos y Desempeño (Claude) → Proyectos con Claude (Projects/Artifacts).
  Claude vuelve a ser herramienta central (no solo complemento) en 3 de los 5 módulos. Se
  actualizaron `brief.md`, `programa.md`, `index.html` (14→15 slides, 5 slides de cronograma)
  y `acroforms.json` (Entregables, Programa, Paso01-02 Body). Por instrucción del usuario, la
  VPN se menciona siempre de forma genérica ("una VPN", "una herramienta de VPN gratuita"),
  sin nombrar la marca en ningún lugar del deck ni de los AcroForms. El prototipo instalable de
  automatización de cribado de currículums (cierre del Módulo IV anterior) se retira: el cierre
  ahora es el sistema de gestión del desempeño en Claude Projects (Módulo V). Pendiente:
  regenerar el PDF (`generar-pdf.sh` + `customize-acroforms.py`), correr `verificar-propuesta.sh`
  y `verificar-overflow.js`, y revisar visualmente las 15 slides antes de declarar entregable.
