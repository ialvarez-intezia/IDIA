# Brief — Zoom · Relaciones Laborales

---

## Datos administrativos

- **Empresa**: Zoom (Gestión Humana: 6ta área independiente del megaproyecto)
- **Sector**: Servicios / corporativo
- **Slug**: `zoom-relaciones-laborales`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Tipo de documento**: Capacitación In-Company (`CAI-017`) · 1 formación independiente, 2
  módulos / 1 sesión / 4 horas (mismo patrón uniforme que las 5 formaciones de `zoom-rh/`
  CAP-050, extendido a un 6to frente: **Relaciones Laborales**).
- **Eje temático**: Inteligencia para Relaciones Laborales — cálculos, pagos y cumplimiento
  ante entes gubernamentales, cuentas por cobrar, nóminas especiales, fideicomiso y casos
  excepcionales, con Gemini, Gems y NotebookLM.
- **Fecha del brief**: 2026-09-08
- **Alianza**: no

## Fuente primaria del contenido

El usuario adjuntó una foto de la tabla **"Funciones Relaciones Laborales"** (12 funciones,
manual/ficha interna del cargo). Es la fuente primaria del contenido curricular de este
deck — no se completó por instrucción suelta sino a partir de esa lista literal:

1. Supervisar y apoyar las finalizaciones de la relación laboral para validación de los cálculos.
2. Supervisar y controlar que se realicen los pagos a los entes gubernamentales, y generar la solicitud de solvencia.
3. Registrar, analizar y revisar el egreso del personal.
4. Supervisar el manejo de los viáticos.
5. **Manejar y controlar las cuentas por cobrar de los trabajadores.** (resaltada por el usuario en la fuente — tratada como función prioritaria del track)
6. Supervisar y garantizar el abono o la ejecución de las nóminas especiales inherentes al cargo o al área.
7. Supervisar y garantizar el abono mensual del fideicomiso a los trabajadores.
8. Garantizar que se lleven a cabo los procesos de registro, cambios y actualización de los diferentes entes gubernamentales.
9. Supervisar y controlar el registro de los reposos de los trabajadores.
10. Supervisar la publicación de los horarios laborales y el cumplimiento de acuerdo a lo establecido por los entes gubernamentales.
11. Atender los casos excepcionales en materia judicial y contable.
12. Evaluación de solicitudes de beneficios otorgados por la empresa.

**Agrupación curricular en 2 módulos** (síntesis para el Programa, mismo criterio que las 5
formaciones de `zoom-rh/`: 3 temas por módulo, no una enumeración literal de las 12 líneas):

- **Módulo I · Cálculos, Pagos y Cumplimiento Legal** (funciones 1, 2, 3, 4, 8, 9, 10): el
  bloque más regulatorio — finiquitos, pagos y solvencias ante entes gubernamentales, egresos,
  viáticos, reposos y horarios laborales.
- **Módulo II · Cuentas, Beneficios y Casos Excepcionales** (funciones 5, 6, 7, 11, 12): el
  bloque de cara al trabajador — cuentas por cobrar (función priorizada), nóminas especiales,
  fideicomiso, casos judiciales/contables excepcionales y evaluación de solicitudes de
  beneficios. Cierra con el Reto IA ZOOM (§ puntos transversales).

## Contacto

- **Asesora comercial**: María Iribarren · +58 414 0570056 · miribarren@intezia.com
- **Servicio previo con Intezia**: sí — Zoom es cliente recurrente, con `zoom-rh/` (CAP-050,
  5 formaciones de Gestión Humana), `zoom-comercial/`, `zoom-operaciones/`, `zoom-innovacion/`,
  `zoom-it/`, `zoom-miami/` y `zoom/` (Legal, CAP-029) ya entregados.

## Forma del deck — mirror de CAP-050 (`zoom-rh/`), por instrucción explícita del usuario

1. **Un solo track** (no multi-track como CAP-050): Portada → Diagnóstico → Objetivos →
   Programa → Cronograma (1 sesión) → Beneficios → Impacto → Próximos pasos → Cierre.
2. **Cronograma con el mismo lenguaje que CAP-050**: barra `.ruta` de progreso (sesión única,
   100%), bloque "Temas" (chips), bloque "Tiempo · Total 4h" (`.timebar` con minutos
   literales: 15' contexto + 100' Módulo I + 100' Módulo II + 25' Reto IA ZOOM y cierre),
   columnas **"Estrategias de enseñanza" / "Estrategias de aprendizaje" / "Recursos y
   entornos"** (no "Qué se hace / Qué se logra", que es el lenguaje usado en otras cuentas
   esta misma semana — aquí se respeta el vocabulario ya establecido para Zoom).
3. **Puntos transversales de la ruta Zoom** (replicados en las 5 formaciones de CAP-050,
   aplican igual a este 6to frente):
   - **Reto IA ZOOM**: cierre del último módulo (presentación cruzada de 3 minutos).
   - **Expectativas realistas sobre los Gems**: sin lenguaje de autonomía — un Gem traduce o
     consolida información; la decisión sobre una persona (pagos, beneficios, casos
     judiciales) la toma siempre el equipo humano. Crítico aquí por la sensibilidad de cuentas
     por cobrar, fideicomiso y casos judiciales.
   - **Medición de tiempo ahorrado (antes/después, 30 días)**: línea base en el Paso 03 de
     "Cómo arrancamos" + remedición a los 30 días.
   - **Protección de datos por diseño**: este track maneja datos personales y financieros
     especialmente sensibles (cuentas bancarias para cuentas por cobrar, expedientes de
     fideicomiso, casos judiciales) — se refuerza el protocolo de anonimización antes de
     cualquier carga a Gemini.
4. **Herramienta: Gemini** (no Claude) — stack ya establecido para toda la cuenta Zoom
   Gestión Humana: Google Workspace + Gemini + Gems + NotebookLM. Sin AppSheet, n8n, Apps
   Script, APIs ni otra herramienta de desarrollo (mismas restricciones de contenido del
   cliente que `zoom-rh/`, confirmadas 2026-08-17). Sin cálculo de nómina ni analítica
   salarial, sin pruebas psicométricas (no aplica a este track, pero se mantiene la
   restricción general).
5. **Sin slide de Propuesta Económica**: este 6to frente se cotiza dentro del **acuerdo
   marco** ya en curso con Zoom (mismo criterio que `zoom-rh/`, `zoom-comercial/` y
   `zoom-operaciones/`). Los 8 campos AcroForm no económicos (Entregables, Acreditacion,
   Paso01-03 Título/Body) siguen siendo obligatorios; los 5 campos de precio no aplican
   (§4.14).
6. **Actualizado a estándar vigente** (a diferencia del `zoom-rh/` original, de 2026-08-17,
   anterior a estas reglas): sin slide de Metodología ABR ni bloque "Equipo facilitador"
   (§4.10a), Beneficios formato v3 (tarjetas oscuras), Cierre tipo escalera, correo
   `servicio@intezia.com` en el bloque Empresa del cierre.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: María Iribarren.

## Notas internas

- Slug distinto de `zoom-rh/`, `zoom-miami/`, `zoom-comercial/`, `zoom-operaciones/`,
  `zoom-innovacion/`, `zoom-it/` y `zoom/` (Legal, CAP-029): mismo cliente, formaciones
  independientes.
- Caso base estructural: `zoom-rh/` (CAP-050), específicamente el patrón de un track
  individual (Objetivos + Programa + Cronograma de 1 sesión), sin clonar el archivo completo
  de 5 tracks.
- Impacto (§4.9): McKinsey — HR Monitor 2025 (encuesta a 1.925 empresas y 4.000 empleados en
  Europa y EE. UU., cifras de seguimiento de tiempo/ausencias y administración de datos de
  empleados) + SHRM — State of AI in HR 2026 (43% de organizaciones ya integran IA en RRHH,
  cifra reutilizada de `zoom-rh/` como ancla consistente dentro del mismo megaproyecto).
