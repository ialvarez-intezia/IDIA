# Brief — Ailyn Gruszka

## Datos administrativos

- **Cliente**: Ailyn Gruszka (capacitación personal para 2 hermanas · familia Gruszka)
- **Sector**: personal (particular, no corporativo)
- **Slug**: `ailyn-gruszka`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company personalizada (2 participantes) (`CAP-070`)
- **Eje temático**: **Claude** (Claude Fundamentals): dominar la herramienta a fondo, 100% práctico
- **Fecha del brief**: 2026-07-03
- **Estado**: borrador / propuesta inicial
- **Fuentes**: Ficha de Requerimientos (Google Forms, 2026-07-03, solicitante Flavia Martínez) + correo de contexto de Flavia Martínez (2026-07-03)

## Contacto

- **Persona contacto (cliente)**: Ailyn Gruszka (y su hermana; 2 participantes)
- **Asesora de ventas Intezia**: Flavia Martínez (+58 414-5756615 · fmartinez@intezia.com)
- **Facilitador asignado**: David Prato (Consultor IA Intezia · dprato@intezia.com)

## Perfil de las participantes

- 2 personas: Ailyn Gruszka y su hermana (familia Gruszka, familia de los Cohen).
- Nivel **principiante**. No les interesa la teoría: quieren **práctica**. Han visto algunos cursos y videos, pero lo que buscan es el **manejo experto de Claude**.
- Retos del día a día: **levantados el 2026-07-16** (ver abajo). La reunión de arranque queda para elegir el proyecto final y los archivos reales.

## Casos reales levantados (2026-07-16)

Contenido que el programa debe cubrir, en orden de peso:

1. **Excel y análisis de datos — caso #1**: unificar los Excel de nóminas de varias organizaciones, analizarlos (ej. los 10 cargos más altos) y graficarlos. Es RRHH/nóminas, recurrente, y **candidato principal a proyecto final**. Va en el Módulo I (tema 1.5).
2. **Organización documental con Projects**: quieren Claude como «la carpeta de la empresa» — registro mercantil, pagos, gastos — y consultarlo con facilidad. Ancla los ejemplos de 3.1 y 3.5.
3. **Presentaciones y Word**: crear una presentación a partir de un documento, sin ir lámina por lámina (3.4).
4. **Diseño de tarjetas y arte sencillo**: invitaciones, tarjetas, comunicaciones. **Danae ya usa Canva**, así que 3.3 cubre Claude Design junto con la integración de Claude con Canva.
5. **Claude como asistente**: consultas y seguimiento sobre sus propios documentos (gastos, pagos, historial, viajes y vuelos) — 3.5.

## Expectativas delimitadas (2026-07-16)

Van en la slide **05 · Alcance** del deck, para no sobreprometer:

- **Video: no.** Ailyn preguntó por generar video (estilo Nano Banana). Claude no genera video; el programa no lo cubre.
- **Agente tipo WhatsApp: no.** Mencionaron el del primo Gabriel. No es el nivel de este programa.
- **Recordatorios y conexión con calendario: a evaluar.** Lo pidieron (citas, pagos, recordatorios). Se puede explorar con conectores, pero es avanzado: se plantea como tema a evaluar en el arranque, **no como entregable garantizado**.

## Necesidad detectada

Aprender a usar **Claude** de verdad y sacarle todo el provecho en su día a día. Han pagado licencias de varias plataformas de IA y no saben ni cómo usarlas ni cómo aprovecharlas; hoy quieren **enfocarse y profundizar en Claude**. De primera instancia es algo introductorio y sencillo; el cierre es un **proyecto final aplicado** que les resuelva un problema real.

## Fase futura (fuera de este deck)

- Posterior a la capacitación, se evalúa apoyarlas en la creación de su **clon digital**, pero **dependerá de su dominio de la herramienta**. No entra en esta propuesta; el proyecto final deja la base para esa fase (contexto del correo de Flavia, 2026-07-03).

## Especificaciones del programa

- **Duración**: 8 horas académicas (4 sesiones de 2 horas, 4 módulos). Decisión del usuario 2026-07-03 (la ficha pedía «lo que consideren necesario»).
- **Modalidad**: **Presencial** (ficha).
- **Fechas**: después del **10 de julio** (ficha). Sin fechas exactas.
- **Ecosistema**: **Claude** (ficha). Programa 100% Claude.
- **Infraestructura**: **no cuentan con infraestructura tecnológica propia** (ficha). Ya tienen licencia de Claude y quieren profundizar en ella.
- **Entregables esperados (ficha)**: Workbooks, Certificados (informe de desempeño NO seleccionado).
- **Aliado institucional**: no.
- **Precio**: la propuesta lleva slide de Propuesta Económica; ventas llena la cotización en Adobe Reader (decisión del usuario 2026-07-03).

## Decisiones de diseño

- Clonada de `anabella/` (canónica mono-fase, Educación, misma estructura 4 mód / 8h / 1 slide por sesión). Reescrita 100% a Claude (anabella era Google + Claude).
- 15 slides: 4 sesiones = 4 slides de cronograma, más la slide **05 · Alcance** (`.s-scope`, CSS propio en `overrides.css`) añadida el 2026-07-16 para delimitar expectativas. Modalidad **Presencial** en el cronograma.
- Módulos I y III pasan a 5 temas cada uno (el modo compacto 2×2 de `_base/styles.css` ya los soporta). Sin desbordes: `verificar-overflow.js` da 0.
- Facilitador nombrado: **David Prato**; asesora en cierre: **Flavia Martínez**.
- Arco pedagógico para principiantes → proyecto final: I Claude desde cero · II Prompting con método · III Claude trabaja contigo (Projects, Artifacts, Claude Design) · IV Tu proyecto final.
- Copy en **plural** («ustedes / ambas / las») por ser 2 hermanas.
- Slide de Impacto con datos de estudios reales citados heredados de la canónica (Stanford HAI AI Index 2026, McKinsey State of AI 2025, Anthropic Economic Index 2025); hook reencuadrado a «saber usarla con método».
