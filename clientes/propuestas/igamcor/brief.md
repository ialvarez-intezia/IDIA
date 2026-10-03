# Brief — Igamcor (DET-012)

## Datos administrativos

- **Empresa**: Igamcor
- **Sector**: Construcción e interiorismo (locales comerciales, oficinas y vivienda)
- **Tamaño**: Micro / Pyme (menos de 50 empleados)
- **Slug**: `igamcor`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — el cliente pidió explícitamente cotizar Detección y
  Habilidades **por separado**, para evaluar ambas opciones. Este documento cubre solo
  Detección; Habilidades queda como propuesta futura aparte.
- **Tipo de documento**: Detección (`DET-012`) · Fundamentals (2h grupal) + auditoría de 4
  áreas, 4 horas por área (18h totales), modalidad presencial.
- **Eje temático**: Pasar de un uso disperso y sin criterio de IA a un criterio unificado de
  adopción, empezando por la automatización de informes de obra y la documentación de
  instalaciones a partir de fotos.
- **Fecha del brief**: 2026-09-10
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Igamcor**
(`Levantamiento_Igamcor_2026-09-09.pdf`, registrada 2026-09-09), elaborada por la asesora
**Flavia Martínez**.

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
  (contacto ya registrado en el sistema — `ailyn-gruszka/`, `diego/`; no viene en la ficha de
  este cliente).
- **Contacto cliente**: Claudio Gamboa · Director · patrocinador y líder de la iniciativa,
  decide en conjunto con su socio ("nos sentamos con números").
- **Servicio previo con Intezia**: ninguno — primer contacto. Sin propuesta previa sin aprobar.

## Decisiones confirmadas con el usuario (2026-09-10)

1. **4 áreas** (Diseño/Arquitectura, Construcción, Mantenimiento, Administración) — la ficha
   las lista de forma consistente en Bloque A y en el Bloque específico de Detección, sin la
   discrepancia de conteo que sí tuvieron Farmacéutica 24 y Hoteles Cumberland.
2. **4 horas de Detección por área** (16h) + **Fundamentals de 2h grupal** para las 10-12
   personas del universo (una sola sesión, dentro del máximo de 25) = **18h totales**.
   Confirmado con el usuario — Igamcor es una empresa mucho más chica que los clientes
   recientes (10-12 personas en total, sesiones de grupo pequeño de 3-4 personas por área, no
   1 referente), y la ficha en sí sugiere sesiones de 45-60 min como campo genérico, pero se
   mantuvo el lineamiento estándar de Detección sin ajustar por tamaño de empresa, mismo
   criterio que `farmaceutica-24/` y `hoteles-cumberland/`.
3. **Sesiones grupales, no 1 referente por área**: cada sesión de área la lidera el
   responsable del área, con 2-3 personas más sumándose (grupo de 3-4 en total por sesión) —
   distinto del patrón "1 referente" de otros clientes. Reflejado en el roadmap y cronograma.
4. **Recomendación preliminar de Gemini** (no Claude): Claudio ya usa Gemini a título personal
   (incluido en su plan pagado de Google) para correos y descripciones de fotos — mismo
   criterio ya aplicado en `farmaceutica-24/` (Claude, por Jesús Mora) y
   `hoteles-cumberland/` (Claude, por Leudo Gonzalez): se recomienda preliminarmente la
   herramienta que el patrocinador/decisor ya usa personalmente, mención breve en el Reporte
   Final del roadmap, sin contradecir la metodología ABR. **No fue una pregunta explícita al
   usuario** — se aplicó el patrón ya establecido; confirmar si no aplica.
5. **Modalidad presencial** (no mixta) — la ficha es explícita: "Presencial en sus oficinas"
   (Caracas). Se usa "presencial" en todo el deck, no "modalidad mixta" como en los clientes
   anteriores.
6. **Sin certificado de participación** — Detección pura, mismo criterio que
   `deteccion-sin-certificado.md`.
7. **Sin slide de Mapa de Calor** (tabla ilustrativa) — mismo ajuste ya aplicado a
   `farmaceutica-24/` y `hoteles-cumberland/`. "Mapa de Calor" sigue como nombre del
   entregable de la Etapa de Priorización, sin slide propia.
8. **Código**: `DET-012` (verificado libre — sigue a DET-010 Farmacéutica 24, DET-011 Hoteles
   Cumberland).

## Necesidad detectada (ficha, Bloque C y D)

Objetivo central citado (cita textual): *"La idea es incorporar IA sobre todo con los medios
electrónicos, con la lectura de la cantidad de cuadros de Excel que llevamos en cada obra
tenemos diez contratistas, cincuenta compras, para ver si nos ayuda a automatizar todo esto y
a leer y responder esa información."* El cliente busca automatizar la mayor cantidad de carga
operativa posible, pero aún no sabe el alcance exacto — por eso empieza con Detección.

1. **Informes de obra** (semanal, dato interno): las herramientas actuales (Gemini) no generan
   el informe como Claudio lo necesita; termina redactándolo manualmente.
2. **Gestión de información de obra en Excel** (semanal, dato público): 10 contratistas y 50
   compras por obra, gran volumen sin automatización para leerlo ni resumirlo.
3. **Documentación de instalaciones a partir de fotos** (diaria, dato interno): generar
   explicaciones detalladas a partir de fotos (ej. mueble con múltiples detalles) hoy se hace
   de forma manual/artesanal con IA genérica.
4. **Uso de IA disperso y sin criterio**: los arquitectos la usan a veces para mejorar
   presentaciones sin sacarle provecho completo; Claudio la usa personalmente (Gemini) pero
   sin extenderla al equipo; el resto de las áreas no la ha adoptado.
5. **Sin diagnóstico previo de IA** — primer acercamiento formal de la empresa con la
   tecnología.

## Universo y modalidad

- **10 a 12 personas** en total, repartidas en las 4 áreas.
- **Sesiones grupales por área**: el líder de cada área + 2-3 personas más (grupo de 3-4 por
  sesión), no 1 referente como en otros clientes. 4 sesiones de área + 1 sesión grupal de
  Fundamentals para las 10-12 personas.
- **Modalidad**: Presencial, en las oficinas de Igamcor (Caracas).
- **Nivel de partida con IA**: la usan de forma suelta y sin criterio. Sin formación previa.
- **Presupuesto**: en evaluación. **Apertura al cambio**: Alta. **Patrocinio ejecutivo**:
  fuerte y visible (Claudio).
- **Urgencia**: ninguna declarada. Horizonte deseado: corto plazo (0-3 meses).
- **Quién decide**: Claudio Gamboa junto con su socio, revisando números en conjunto — no
  decide unilateralmente pese a ser un patrocinador fuerte.

## Contexto adicional (ficha, no expuesto directamente en el deck)

- **Datos históricos sensibles**: Igamcor mantiene un servidor físico en oficina con 400
  proyectos históricos de arquitectura; prefieren no migrar ese historial a la nube (costo),
  solo lo que esté en curso, y bajar el servidor físico al finalizar cada proyecto. Contexto
  interno de diseño (relevante sobre todo para el área de Diseño/Documentación), no una
  restricción que se afirme en el deck visible.
- **Bloque F (observaciones internas, OCR parcialmente ilegible)**: primer contacto muy bien
  encaminado — el cliente investigó por su cuenta qué ofrece Intezia y valoró explícitamente
  el enfoque "con datos, no con intuición". Pidió cotizar Detección y Habilidades por separado
  (ver decisión 1). Cotizar Habilidades hoy es complicado porque el cliente aún no sabe cuáles
  son los procesos exactos — se podrá estimar en base a la cantidad de personas/áreas cuando
  se retome como propuesta aparte.
- **Sin regulación sectorial aplicable** ni calendario de sesiones aún definido.

## Hacia dónde va esto (contexto, no cotizado en este documento)

El Reporte Final debe entregar un roadmap de adopción de IA basado en datos reales (no en
intuición, cita textual del cliente) que priorice qué procesos automatizar primero, con foco
en el manejo de grandes volúmenes de información en Excel por obra y la generación de reportes.
La futura propuesta de Habilidades (procesos aún por definir con el cliente) se cotiza aparte.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Flavia Martínez.

## Notas de diseño

- **Estructura (12 slides)**: mismo patrón ya usado en `farmaceutica-24/` (DET-010, tras su
  ajuste de Fundamentals) y `hoteles-cumberland/` (DET-011) — Portada → Diagnóstico →
  Objetivos → Programa (4 módulos) → Roadmap (3 etapas + resultado) → Cronograma · Fundamentals
  → Cronograma · Estructura por área → Beneficios v3 → Impacto → Precio → Pasos → Cierre
  escalera.
- **Base estructural**: clon del *shell* de `farmaceutica-24/` (roadmap `.rmx-linear`,
  Beneficios v3, Cierre escalera, ya con Fundamentals integrado desde el inicio, a diferencia
  de esos dos casos que lo agregaron después).
- **Impacto (§4.9)**: Autodesk — 2025 State of Design & Make Report (46% ya usa herramientas de
  IA/ML, 39% ya usa IA para mejorar resultados de sostenibilidad) + Autodesk — 2024
  Construction Digital Adoption Report (68% usaría IA una vez completada la implementación ya
  planeada). Chip "+22 pts" = diferencia derivada entre 68% y 46% (no un dato adicional
  inventado).

## Bugs encontrados y corregidos durante la construcción (2026-09-10)

1. **Roadmap con overflow (+19px)**: al integrar Fundamentals desde el inicio, el texto de la
   Etapa 1 ("Con quién": personas + Fundamentals entre paréntesis) y de la Etapa 3 ("Qué pasa"
   con una cláusula extra sobre el roadmap) quedaron más largos de lo necesario y desbordaron
   la slide. Se acortaron ambos, mismo tipo de ajuste ya visto en `farmaceutica-24/` al agregar
   Fundamentals.
2. **Colisión `.rmx-ethics` vs `.foot`**: el párrafo de ética del roadmap envolvió a 2 líneas y
   su segunda línea chocó con "IGAMCOR · DET-012" — pese a que "Igamcor" es un nombre corto,
   contradiciendo el umbral de la memoria `bug-rmx-ethics-choca-nombre-cliente-largo.md`
   ("nombre largo, >15-18 caracteres"). Esa memoria se corrigió: el disparador real es si el
   párrafo envuelve a 2 líneas, no la longitud del nombre. Fix aplicado:
   `.rmx-ethics p { padding-right: 230px; }` en `overrides.css` — a partir de ahora, este fix
   se agrega por defecto en todo deck nuevo con roadmap `.rmx-linear`, no solo cuando el
   nombre del cliente "parece largo".

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh igamcor
python3 scripts/customize-acroforms.py igamcor
python3 scripts/customize-igamcor.py "clientes/propuestas/igamcor/<PDF generado>.pdf"
```

## Pendientes

- Confirmar con el usuario si la recomendación preliminar de Gemini (decisión 4) es correcta,
  o si prefiere no mencionar ninguna herramienta dado que el cliente "aún no sabe" y pidió
  evaluar Detección y Habilidades por separado.
- Confirmar contacto/cargo del socio de Claudio (mencionado pero no nombrado en la ficha).
- Calendario de las 4 sesiones + Fundamentals: sin fecha definida aún.
- Propuesta de Habilidades (separada): pendiente de que el cliente defina procesos exactos.
