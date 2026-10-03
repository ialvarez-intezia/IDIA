# Brief — DUSA · La Próxima Destilación (CH-007) · Charla 1 — Finanzas y Sistemas

> **Dos charlas en carpetas separadas** (instrucción del usuario, 2026-08-31): esta carpeta
> (`dusa/`, CH-007) queda dedicada a la **Charla 1 — Finanzas y Sistemas**. Una eventual
> Charla 2 (otra audiencia) vive en una carpeta distinta, con su propio código — no
> confundir ni mezclar contenido entre ambas.

## Datos administrativos

- **Cliente**: DUSA
- **Sector**: industrial · bebidas / licores
- **Slug**: `dusa`
- **División Intezia**: `educacion`
- **Tipo de documento**: Charla (`CH-007` — séptima charla del catálogo)
- **Programa**: La Próxima Destilación · Cómo Copilot Optimiza los Procesos de DUSA
- **Eje temático**: **Microsoft Copilot** en Excel para análisis financiero, más
  **Power Automate** y **Copilot Studio** para automatizar facturación y recordatorios de
  pago, y una mirada de **gobierno y seguridad** para el equipo de Sistemas
- **Audiencia**: equipos de **Finanzas y Sistemas** de DUSA (Charla 1 de 2)
- **Naturaleza**: Charla sin propuesta económica
- **Fecha del brief**: 2026-08-03 · **actualizada**: 2026-08-28 (Claude → Copilot,
  audiencia interdepartamental) · **2026-08-31** (Charla 1: Finanzas y Sistemas, agenda de
  6 bloques / 2 horas, instrucción directa del usuario)
- **Estado**: `Borrador`

## Contacto

- **Asesor/a comercial Intezia**: sin asignar — pattern team-single, cierre del deck solo con
  contacto institucional
- **Consultor / Facilitador**: NO se asigna en la propuesta inicial — INTEZIA designa al
  facilitador al confirmar la fecha con DUSA

## Fuente de este brief

Ficha de requerimientos completada por DUSA (`Ficha de requerimientos DUSA.csv`, recibida
2026-08-28) + agenda directa del usuario para la Charla 1 (2026-08-31): **equipos de
Finanzas y Sistemas**, **2 horas**, herramientas **Copilot** (Excel), **Power Automate** y
**Copilot Studio** (automatización de facturación), con un bloque técnico de gobierno y
seguridad para Sistemas.

## Contexto del cliente (para diseño interno, no aparece como afirmación de stack en el deck — §4.11)

- Compañía industrial del sector bebidas / licores, ~500 colaboradores.
- Ecosistema Microsoft ya en uso (Word / Excel) — confirmado también en `dusa-cap088`
  ("ecosistema Copilot que DUSA ya usa"). Copilot es la herramienta natural para esta charla,
  no un cambio de stack: opera dentro de Word, Excel y PowerPoint que DUSA ya tiene.
- Nivel de los participantes (ficha): principiante e intermedio. Ya usan herramientas de IA
  generativa y aplicaciones de productividad digital, pero no han identificado cómo aplicar
  esas herramientas a sus propios procesos de negocio. Sin conocimientos avanzados de
  programación.
- Iniciativa de transformación digital de DUSA: aumentar eficiencia operativa, fortalecer la
  integración entre áreas y mejorar la productividad — la IA como habilitador, no como
  reemplazo de sistemas.

## Por qué este programa (Charla 1 — Finanzas y Sistemas)

Finanzas ya tiene fundamentos de Copilot, pero no lo aplica a sus tareas reales: análisis
financiero repetitivo en Excel y un flujo manual de facturación y recordatorios de pago.
Sistemas, por su parte, necesita la mirada de gobierno para administrar esa adopción con
criterio (permisos, datos, buenas prácticas de agentes). Esta charla de 2 horas, práctica y
en vivo, muestra a Finanzas cómo resolver esas tareas dentro de su ecosistema Microsoft, y
le da a Sistemas lo que necesita para sostenerlo con seguridad.

## Diagnóstico (5 puntos, Charla 1)

1. Finanzas invierte tiempo en análisis y reportes que podrían resolverse con Copilot
   dentro de Excel, sin salir de su flujo habitual.
2. La facturación y el seguimiento de pagos siguen procesos manuales, con recordatorios y
   aprobaciones que se gestionan uno por uno.
3. El equipo ya tiene fundamentos de Copilot; falta pasar de usar la herramienta a
   aplicarla a tareas financieras concretas.
4. Sistemas necesita administrar la adopción de Copilot: permisos, manejo de datos y
   buenas prácticas al construir agentes.
5. DUSA busca que Finanzas gane velocidad sin perder control, y que Sistemas tenga la
   gobernanza para sostenerlo.

## Especificaciones del programa (Charla 1)

- **Duración**: 2 horas / 120 minutos (6 bloques: 10 + 10 + 30 + 30 + 20 + 20 min)
- **Audiencia**: equipos de Finanzas y Sistemas
- **Herramientas**: Microsoft Copilot (Excel), Power Automate, Copilot Studio
- **Formato**: práctica, con demostraciones en vivo sobre casos reales de Finanzas
- **Propuesta económica**: sin slide `.s-price` — no se muestra cotización en el deck
  (confirmado de nuevo por el usuario, 2026-08-31: "no lleva hoja de cotización")
- **Acreditación**: Certificado de participación INTEZIA Education

## Estructura de la charla (6 bloques · 2 horas) — agenda dada por el usuario, 2026-08-31

1. **Apertura y encuadre** (10 min) — quiénes somos, qué es la sesión (no es venta), foco:
   Finanzas + mirada técnica de Sistemas.
2. **Dónde está DUSA hoy** (10 min) — diagnóstico rápido de herramientas y nivel actual; ya
   alfabetizados en fundamentos → directo a lo aplicado.
3. **Copilot en Excel para análisis financiero** (30 min) — fórmulas, análisis de datos,
   gráficas y resúmenes automáticos en vivo.
4. **Automatización de facturación y recordatorios** (30 min) — flujo de aprobación de
   facturas y recordatorios de pago con Power Automate + Copilot Studio.
5. **Sistemas: gobierno y seguridad de Copilot** (20 min) — administración de asientos y
   permisos, manejo de datos dentro de M365, buenas prácticas al construir y usar agentes.
6. **Cierre, preguntas y recursos** (20 min) — recapitulación de lo mostrado, espacio
   abierto de preguntas, materiales que se llevan.

> **Programa (slide 4) vs. Cronograma (slide 5)**: el Programa agrupa los 6 bloques como 6
> módulos compactos (h3 corto, sin `<p class="obj">`, máx 2 topics — capacidad real de 5-6
> módulos, ver memoria `bug-program-modules-5-6-no-compact`), y el Cronograma desarrolla el
> detalle completo de cada bloque (temas, tiempo, estrategias, recursos), fiel a los tiempos
> exactos dados por el usuario.

## Notas comerciales

- **Sin propuesta económica en el deck**: no hay slide de cotización (reconfirmado
  2026-08-31).
- **Vigencia de la propuesta**: 30 días para coordinar fecha.
- Programa registrado como **CH-007** en INTEZIA Education.

## Notas de diseño

- **Actualización 2026-08-28**: cambio completo de eje (Claude → Copilot) y de audiencia
  (líderes de Comercial/Finanzas/Talento Humano → 30 participantes de procesos
  interdepartamentales), a partir de la nueva ficha de requerimientos de DUSA. Se conserva el
  código `CH-007`, el título de marca "La Próxima Destilación" (la metáfora de destilar un
  proceso a su forma más eficiente sigue aplicando) y la estructura de 9 slides ya establecida
  para este deck. Se reemplazó por completo: Portada, Diagnóstico, Objetivos, Programa,
  Cronograma, Beneficios (Entregables), gancho de la slide de Impacto, Próximos pasos y
  Cierre.
- **Slide `.s-impact`**: se conservan las barras y fuentes ya citadas (Stanford HAI, McKinsey,
  Anthropic Economic Index) — son datos genéricos de productividad por función, siguen siendo
  válidos. Se reescribió el texto de gancho (`hook-text`) porque mencionaba específicamente
  "Comercial y Finanzas ya priorizadas por el liderazgo", framing que ya no aplica con la
  audiencia interdepartamental de 30 participantes.
- **Sin slide `.s-orange` (ABR)** y **sin slide `.s-price`**: reglas ya vigentes para charlas,
  sin cambios.
- **Sin afirmación de migración de stack (§4.11)**: Copilot se enmarca como la herramienta que
  ya vive dentro de Word, Excel y PowerPoint de DUSA, nunca como un cambio de ecosistema.
- **Sin datos de contacto de asesor Intezia en el deck**: cierre solo con contacto
  institucional (Intezia C.A / info@intezia.com), mismo patrón que la versión anterior.
- **Actualización 2026-08-31 (Charla 1 — Finanzas y Sistemas)**: el usuario decidió dividir
  la charla en 2 documentos, en carpetas separadas. Esta carpeta (`dusa/`, CH-007) se
  especializó para Finanzas + Sistemas con la agenda de 6 bloques / 2 horas dada
  directamente por el usuario (reemplaza la versión interdepartamental de 30
  participantes / 90 min del 2026-08-28). Se reemplazó por completo: Portada, Diagnóstico,
  Objetivos, Programa (ahora 6 módulos compactos), Cronograma (6 bloques con tiempos
  exactos), Beneficios (Entregables), gancho de Impacto y Próximos pasos. Slide `.s-impact`
  conserva barras/fuentes (dato genérico); se reescribió el hook-text para Finanzas. Una
  eventual Charla 2 (otra audiencia) irá en una carpeta nueva, con su propio código — no se
  crea todavía, pendiente de instrucción del usuario.
