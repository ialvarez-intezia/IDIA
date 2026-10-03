# Brief — Universidad Metropolitana (Unimet) · Investiga con Criterio (TA-035)

## Datos administrativos

- **Institución**: Universidad Metropolitana (Unimet)
- **Aliado / dirección contraparte**: Gerencia de Atención Socioeconómica Estudiantil
- **Slug**: `unimet`
- **División Intezia**: `educacion`
- **Servicio (Modelo Intezia)**: `habilidades`
- **Alianza**: sí — Gerencia de Atención Socioeconómica Estudiantil de la Unimet
- **Tipo de documento**: Taller (`TA-035`) · mono-fase, canon `cumbre-andina/` + formato vigente
  de `simple-tv-cai002/` (Beneficios v3, Cierre escalera, eyebrow con servicio)
- **Programa**: Investiga con Criterio · IA para tus Estudios
- **Eje temático**: uso de la IA generativa para los estudios universitarios — ecosistema
  Gemini (Gmail, Docs, Slides, Drive, agentes), Perplexity y Elicit para investigación
  académica, con un módulo propio de ética y uso responsable
- **Fecha del brief**: 2026-09-30
- **Estado**: borrador

## Origen

Pedido directo del usuario: taller de 4 horas para estudiantes de la Unimet sobre el uso de
la IA para sus estudios. Enfoque **100% práctico, con teoría breve solo al inicio**. Contenido
pedido explícitamente: ecosistema de Google Gemini (correo, presentaciones, documentos),
Gemini como agente e integraciones con Drive, generación de documentos/presentaciones/PDF,
Perplexity para investigación y Elicit para citas y bibliografía. El usuario agregó después,
como requisito explícito: un bloque de **ética y responsabilidad en el uso de la IA para
investigación** — revisión, iteración, análisis crítico y verificación humana siempre.

**Sin hoja de cotización** (instrucción directa del usuario, 2026-09-30): el deck **no**
lleva slide de Propuesta Económica (`.s-price`). Los 5 campos de precio y los campos
`Programa`/`Notas` (que viven dentro de esa slide) no aplican — mismo criterio que
`clientes/propuestas/urbe/` (CU-012). Los 8 campos no económicos (`Entregables`,
`Acreditacion`, `Paso01-03 Titulo/Body`) siguen siendo obligatorios, más las 4 cajas del
Cierre escalera (`CierreResultado`, `CierrePaso1-3`).

**Nombre del programa**: "Investiga con Criterio" — propuesto por Intezia (el usuario pidió
un nombre creativo). Incluido en el H1 de portada y en `programa.md`; fácil de ajustar si el
usuario prefiere otro.

## Contacto

- **Asesora comercial Intezia**: por confirmar
- **Aliado**: Gerencia de Atención Socioeconómica Estudiantil, Universidad Metropolitana
  (Unimet). Sin nombre de contacto individual todavía — el usuario lo puede agregar después.
- **Facilitador**: por confirmar — Equipo INTEZIA Education designa al facilitador antes del
  arranque.

## Especificaciones del programa

- **Duración**: 4 horas académicas · sesión única (2 bloques de 2h)
- **Modalidad**: Presencial (default razonable para un taller estudiantil de la Unimet;
  ajustar si el usuario indica otra modalidad)
- **Audiencia**: estudiantes de la Universidad Metropolitana, cualquier carrera, convocados
  a través de la Gerencia de Atención Socioeconómica Estudiantil. Sin experiencia previa en
  IA necesaria.
- **Perfil de ingreso** (Taller — obligatorio, `plantillas/diseno-taller-capacitacion.md`):
  estudiante activo de la Unimet, cualquier carrera o semestre; cuenta de Google (personal o
  institucional) activa; sin requisitos técnicos ni de hardware especiales más allá de un
  dispositivo con navegador.
- **Acreditación**: INTEZIA + Unimet (certificado de participación conjunto, mismo patrón que
  `universidad-de-nueva-esparta/` y `rush-academy/`) — se agrega a `Entregables`, no se
  modifican las 3 líneas fijas de `Acreditacion`.
- **Fechas**: por confirmar — el usuario indicó que enviaría la dirección de contacto exacta
  aparte; sin `fecha_arranque_deseada` ni `resultados_esperados` confirmados todavía, así que
  el bloque de calendario de inicio en "Cómo arrancamos" se omite (no se inventa fecha ni
  proyección de resultado).

## Contenido (4 módulos, 2 bloques de 2h)

1. **Fundamentos de la IA generativa** — teoría breve (qué es un modelo de lenguaje, cómo
   funciona una conversación con IA) + primer contacto práctico con Gemini.
2. **Ecosistema Gemini para tus estudios** — Gemini en Gmail, Docs, Slides y Drive; Gemini
   como agente (Gems) e integraciones; generación de documentos, presentaciones y PDF.
3. **Perplexity y Elicit para investigación académica** — búsqueda de fuentes confiables,
   citas y bibliografía organizada.
4. **Ética y uso responsable de la IA en la investigación** — revisión humana, iteración,
   análisis crítico, integridad académica, cuándo no usar IA.

Ver desglose instructivo completo en `programa.md`.

## Notas de plantilla (esta versión)

- Clonado de `simple-tv-cai002/` (ya trae Beneficios v3 ampliado + Cierre escalera + eyebrow
  con servicio, todos vigentes) en vez del canónico `cumbre-andina/` — evita tener que
  retrofitear manualmente ABR/Equipo facilitador/formato viejo de Beneficios. `overrides.css`
  se mantiene **verbatim** (es CSS de componente, no contenido de cliente).
- **Slide `.s-price` eliminada por completo** (instrucción del usuario) — de 12 a 10 slides
  totales (2 slides de cronograma, no 3, porque es sesión única de 4h en 2 bloques, no 3
  módulos de 8-20h como Simple TV).
- Slide de Impacto con datos reales de Digital Education Council — *Global AI Student Survey
  2024* (n=3.839, 16 países) y *AI in Higher Education Global Survey 2026* (n=45.398, 35
  países): 88% de estudiantes ya usa IA en su aprendizaje, 66% teme que vuelva superficial su
  aprendizaje, solo 29% cree que su profesor está preparado para guiarlo, 75% cree que la IA
  lo ayuda a alcanzar sus metas académicas más rápido, 68% pide más recursos de IA integrados,
  54% la usa semanalmente o más.
- Sin slide de Metodología ABR ni bloque de Equipo facilitador (§4.10a CLAUDE.md, ya ausentes
  en la base clonada).
- Necesita `scripts/customize-unimet.py` propio (caso especial, igual que
  `customize-cavedatos.py`/`customize-fastmed.py`): inyecta las 4 cajas del Cierre escalera y
  re-hornea Entregables/Acreditacion con el layout oscuro ampliado de Beneficios v3. Sin
  limpieza de campos de fase (no aplica, nunca hubo slide de precio).
