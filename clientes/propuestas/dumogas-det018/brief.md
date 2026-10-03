# Brief — Dumogas (Propuesta 2 · DET-018)

---

## Relación con `dumogas/` (DET-017 · Propuesta 1)

Este es el **segundo de los 2 caminos de cotización** que la propia ficha de levantamiento pidió
armar (Bloque F), cita textual:

> *"Trabajemos en este esquema hagamos 2 propuestas: 1 propuesta: Detección con fundamentals
> completo. 1 propuesta: 2 horas de detección por cada área, fundamentals prácticos compartidos
> y un extra de horas enfocada en sus procesos a cada área."*

- **Propuesta 1** (`clientes/propuestas/dumogas/`, DET-017): Detección con fundamentals
  completo, 4h por área, 30h totales — construida primero, el 2026-09-21.
- **Propuesta 2** (este documento, `dumogas-det018/`, DET-018): la versión más liviana de
  entrada descrita arriba. **Documento separado con código propio**, mismo criterio que
  Maurel & Prom (`maurel-prom/` ALL-003 y `maurel-prom-copilot/` CAI-021) — dos propuestas reales
  distintas para el mismo cliente, no dos secciones de un mismo PDF.

Todos los datos administrativos, de contacto, stack tecnológico y restricciones son los mismos
que en `dumogas/brief.md` (misma Ficha de Levantamiento, `Levantamiento_Dumogas_2026-09-21.pdf`)
— **no se repiten en detalle aquí**, solo lo que cambia por la estructura de esta propuesta.

## Datos administrativos

- **Empresa**: Dumogas (venta de gas) · **Slug**: `dumogas-det018` · **División**: `educacion`
- **Servicio (§4.1a)**: `deteccion` — combo Detección (diagnóstico) + un componente tipo
  Habilidades (construcción a la medida) cotizado aparte, sigue bajo el servicio de entrada
  (`deteccion`), mismo criterio que cualquier combo Detección+Habilidades de esta sesión.
- **Asesora comercial**: Verónica Rubio · **Contacto**: Daviana, Gerente (logística; la firma es
  de "toda la gerencia", ver `dumogas/brief.md`).

## Decisión de dimensionamiento — revisada 2026-09-21 a pedido explícito del usuario

Primera versión de este documento dejó las horas de construcción como "fase de alcance abierto,
cotizada aparte" (mismo patrón que `pilotes-perforados/`). El usuario pidió explícitamente una
cifra fija: *"no puede quedar sin horas exactas la propuesta, cuantas horas sugieres colocar
como extra?"*

**Recomendación aplicada: 2 horas de construcción por área** (mismo bloque de tiempo que el
diagnóstico). Razonamiento:

- **No inventa un número nuevo**: reutiliza el lineamiento por defecto de Detección (4h/área,
  `empresa/politicas-comerciales.md`) ya usado en la Propuesta 1 — solo lo particiona en 2
  sesiones de 2h (diagnóstico + construcción) en vez de 1 sesión de 4h.
- **Total**: 2h Fundamentals + 7×(2h diagnóstico + 2h construcción) = 2h + 28h = **30h** — el
  mismo total que la Propuesta 1 (`dumogas/`, DET-017).
- **El diferenciador entre las 2 propuestas deja de ser el costo** (ambas cotizan 30h) **y pasa
  a ser la estructura**: Propuesta 1 = 1 sesión de 4h por área (diagnóstico y construcción
  integrados, con logro inmediato dentro de la misma sesión); Propuesta 2 = 2 sesiones de 2h por
  área (diagnóstico completo de las 7 áreas primero, con el Mapa de Calor ya armado, y
  construcción después, en una sesión separada).

## Por qué esto SÍ es una propuesta distinta a la 1 (no una variación cosmética)

1. **Sesiones más cortas y fáciles de agendar**: 2h + 2h en 2 encuentros, en vez de 4h
   continuas — más viable para un equipo de 1 analista por área que sostiene procesos completos
   solo.
2. **Diagnóstico completo antes de construir en ninguna área**: las 7 sesiones de diagnóstico se
   corren primero; el Mapa de Calor completo queda armado antes de la primera sesión de
   construcción — útil para la gerencia (que no participó del levantamiento) al decidir el orden
   de construcción con más información en mano.
3. **Fundamentals más práctico y compartido**: mismo total de horas que la Propuesta 1, pero un
   encuadre inicial más ágil (menos teoría, más ejercicio guiado), pedido explícitamente en la
   ficha ("fundamentals prácticos").

## Uso del Bloque específico · Habilidades de la ficha (antes sin usar en DET-017)

La Propuesta 1 no usó el `Bloque específico · Habilidades` de la ficha porque era pura
Detección. Esta Propuesta 2, al incluir una sesión de construcción (de naturaleza Habilidades),
sí se apoya en ese bloque para enmarcar **qué busca la construcción**:

- **Qué debe poder hacer el equipo al terminar** (cita de la ficha): analizar datos, manejar
  datos con precisión en tiempo real, automatizar procesos, **usar el sistema administrativo
  con IA y no como una hoja de cálculo**. Se usa esta última frase (concreta y citable) para
  enmarcar el objetivo de la Etapa de Construcción en el roadmap y en Beneficios.
- **Tareas reales**: conciliación, entre otras — mismo hilo conductor que la Propuesta 1.
- **Modalidad de la construcción**: se fijó como **Virtual**, igual que el diagnóstico, para
  mantener una sola modalidad en toda la propuesta y una cotización simple. La ficha declaraba
  "Mixta" como preferencia para esa fase (Bloque específico Habilidades) — queda como nota para
  Verónica, a confirmar con el cliente si prefiere ajustar a mixta antes de enviar.
- **Responsable interno de logística**: Daviana (igual que en Propuesta 1).

## Decisiones heredadas de la Propuesta 1 (sin cambios)

- 7 áreas: Tesorería, Cuentas por pagar, Cuentas por cobrar, Caja, Recursos Humanos, Tributos,
  Almacén — 1 analista por área.
- 9 personas para Fundamentals (headcount específico de la ficha para esa sesión).
- Modalidad virtual para diagnóstico y construcción.
- Sin patrocinio ejecutivo fuerte asumido — mismo criterio que la Propuesta 1: no se afirma un
  compromiso que la ficha no confirma ("Patrocinio ejecutivo: Aún no asegurado").
- Sin nombre del sistema administrativo (Galex) de cara al cliente.
- Sin certificado de participación — Detección/diagnóstico no es un curso.
- Cita textual del objetivo central: "Automatizar procesos claves para ir de la mano de la
  tecnología avanzada." — se reutiliza como quote de apertura, igual que en la Propuesta 1
  (mismo dato real, aplica a ambas propuestas).
- Mismo proceso específico como hilo conductor: conciliación diaria (cuello de botella: "llevarlo
  a tiempo real y no atrasado").

## Impacto (§4.9)

Se reutilizan las mismas fuentes ya verificadas en la Propuesta 1 (mismo cliente, mismo sector,
mismo momento de investigación): OCDE — *AI adoption by small and medium-sized enterprises*
(diciembre 2025) + McKinsey — *The state of AI in early 2025* (abril 2025). No hace falta una
nueva búsqueda: los datos no dependen de la estructura de horas de la propuesta.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Notas internas

- Caso base estructural: `toyocentro/` (mismo shell que `dumogas/`) — adaptado a 13 slides
  (se sumó una slide de cronograma de Construcción, slide 8) para reflejar diagnóstico puro
  (slide 7, 2h) y construcción con logro (slide 8, 2h) como 2 sesiones separadas por área.
- **Al presentar ambas propuestas juntas a Dumogas**: aclarar que son 2 caminos alternativos
  (no complementarios) para el mismo servicio de Detección, con el mismo total de 30 horas — el
  cliente elige la estructura que más le convenga (1 sesión de 4h vs. 2 sesiones de 2h por
  área), no ambos documentos a la vez.
