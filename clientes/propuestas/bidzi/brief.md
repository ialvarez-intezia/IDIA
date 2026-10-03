# Brief — Bidzi (CAI-011)

> **Fuente primaria: Ficha de Levantamiento Intezia — Bidzi** (elaborada por Verónica Rubio,
> 2026-09-04) + precisiones directas del usuario. Primer contacto del cliente, sin servicio ni
> propuesta previa con Intezia.

## Ajuste (2026-09-08) — hoja de precio vuelve al patrón estándar

La hoja de cotización usaba "Inversión por fases" (2 cajas de precio, Fase 1 Detección y
Fase 2 Habilidades, desglosadas a la izquierda). Instrucción explícita del usuario: dejar
solo la columna de la derecha, como se cotiza regularmente en el resto del sistema. Cambios:

- `index.html`: marcador cambiado de "Inversión por fases" a "Propuesta Económica" — bloque
  `.fase-price-list` (2 filas) reemplazado por `.block`/`.block-programa`/`.programa-box` +
  cotización estándar (Propuesta + Inversión / Descuento / TOTAL).
- `acroforms.json`: se agregó la clave `Programa` (resume Fase 1 + Fase 2 + nota de pistas
  adicionales) — el marcador nuevo la usa; el viejo no la creaba.
- `overrides.css`: se retiró el bloque completo "Inversión por fases" (~180 líneas: `.fase-price-*`,
  reposicionamiento de `.notas-box`/`.block-notes-container`/`.cot-label-*`/`.base-frame`/
  `.discount-frame`/`.total-frame`/`.cot-validity`/`.cot-terms-box`) — esas posiciones ya viven
  correctas en `_base/styles.css` para el patrón estándar; dejarlas habría vuelto a desplazar
  la hoja de precio.
- `scripts/customize-bidzi.py`: se quitó toda la lógica de `PrecioFaseN` (eliminar
  `PrecioFase3` huérfana + JS de subtotal Fase1+Fase2) — el marcador nuevo nunca crea esos
  campos, así que no hay nada que sumar ni limpiar.

Regenerado con el trío completo (`generar-pdf.sh` → `customize-acroforms.py` →
`customize-bidzi.py`), verificado sin desbordes y revisado visualmente.

## Ronda 1 (2026-09-04, entrega inicial) — Habilidades pura, luego corregida

La Ficha marca "Servicios de interés: Detección, Habilidades", pero la 1ra versión de este
deck se construyó como **Habilidades sola**, razonando que el Bloque específico de Detección
de la Ficha venía casi vacío frente a un Bloque de Habilidades más completo. El usuario
corrigió esta lectura: *"fíjate que la propuesta tenía detección y no la colocaste en la
propuesta"* — la Ficha sí pedía ambos servicios, y la respuesta correcta no era omitir
Detección sino construirla con lo poco que había, en vez de asumir que el Bloque vacío
significaba "no hace falta".

## Ronda 2 (2026-09-04, corrección) — reconstrucción como combo Detección + Habilidades

**Contexto adicional del usuario**: la reunión con Alejandro fue limitada — fue directo a
pedir cotización, sin detallar cómo opera la empresa. Lo único que se logró sacar fue que
Bidzi tiene 12 departamentos y algunos procesos mencionados de pasada. Instrucción explícita:
*"Eso no debería ser el techo de la propuesta, sino el punto de partida."*

**Pedido del usuario**:
1. Mantener Claude como eje central (ya es la herramienta que el cliente contempla).
2. Sumar una fase de Detección/diagnóstico, no solo capacitación de Habilidades.
3. Dejar abierta la posibilidad de identificar oportunidades en las otras 11 áreas de Bidzi,
   más allá del único proceso que Alejandro mencionó (administrativo, onboarding, facturación).
4. Potenciar la propuesta de Habilidades: no "Claude para todos" de forma genérica, sino
   "Claude por áreas".

**Preguntas resueltas con el usuario (AskUserQuestion)**:

1. **Código**: se mantiene **CAI-011** (no se recodifica a un prefijo DET-, pese a que el
   servicio de entrada pasa a ser Detección) — decisión explícita del usuario, por
   continuidad con lo ya enviado al cliente. Nota de coherencia interna: `meta.json` registra
   `servicio: "deteccion"` (el servicio de entrada real, Detección ocurre primero y decide el
   resto), aunque el código no lleve el prefijo `DET-` — es un caso sin precedente exacto en
   el sistema (los combos Detección+Habilidades documentados hasta ahora, como Everest
   DET-006, sí llevan prefijo DET-). Se deja constancia aquí por si el sistema quiere
   resolver esta inconsistencia código/servicio más adelante.
2. **Alcance de Detección**: **auditoría amplia de las 12 áreas**, no solo del proceso
   administrativo ya mencionado — el roadmap de Detección (slide 05) audita las 12 áreas de
   forma explícita, con el proceso conocido como punto de partida, no como límite.
3. **"Claude por áreas" en Habilidades**: **programa único con pistas por área prioritaria**
   — un solo programa de Habilidades (3 módulos/6h), con un tronco común (Fundamentals + datos
   confidenciales) + una pista ya identificada (Administración/Onboarding/Facturación) +
   pistas adicionales para otras áreas, cuya cantidad y contenido se define según lo que
   arroje la Detección (Módulo III lo deja trazado como plan, sin inventar contenido de las
   otras 11 áreas).

**Principio aplicado, mismo que en `good-latam-cai010/`**: nunca se inventan procesos de las
áreas que no se han auditado. El roadmap de Detección y el Módulo III de Habilidades dejan
esas áreas explícitamente "a definir", no rellenas con contenido genérico o inventado.

## Datos administrativos

- **Empresa**: Bidzi · institución financiera pequeña (México)
- **Sector**: Financiero (institución financiera) · Micro/Pyme (menos de 50 empleados)
- **Slug**: `bidzi`
- **División Intezia**: `educacion`
- **Servicio** (Modelo Intezia): `deteccion` — combo Detección + Habilidades, servicio de
  entrada Detección (ver nota sobre el código en el punto 1 de arriba)
- **Código**: `CAI-011` (mantenido por decisión del usuario, ver arriba)
- **Eje temático**: auditoría de las 12 áreas de Bidzi (Mapa de Calor) + nivelación
  introductoria en Claude (fundamentos, Projects, Skills y Artifacts), con pista en procesos
  administrativos, onboarding y facturación, y manejo seguro de datos confidenciales propio
  de una institución financiera regulada
- **Fecha del brief**: 2026-09-04 (revisado 2026-09-04, misma fecha — corrección same-day)
- **Estado**: `En corrección` (la propuesta ya se había marcado "Enviada" en la ronda 1; al
  regenerar el PDF corregido vuelve a "Enviada" automáticamente, §4.19)

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Cliente / interlocutor**: Alejandro Rodríguez · alejandro.rodriguez@bidzi.mx. Dato interno,
  **no se nombra en el deck**: el deck habla de "Bidzi" o "las 12 áreas de Bidzi".
- **Servicio previo con Intezia**: no, es el primer contacto. Sin propuesta previa sin aprobar.

## Contexto y pain points (Ficha, Bloques A/B/D + Contexto del equipo + comentarios del usuario)

- **Stack**: Microsoft 365. La información del negocio vive en varios sistemas separados por
  área. Coordinación por WhatsApp y correo. No se menciona el entorno Microsoft en el deck
  (Claude ya es la herramienta de foco, no Copilot; §4.11 no aplica, no se afirma migración).
- **IA hoy**: la Ficha registra la herramienta como "Cloud", transcripción casi segura de
  **Claude (Anthropic)** — es la que ya usan de forma informal. Sobre qué incorporar a futuro,
  "aún no lo saben, esperan la recomendación": se mantiene Claude como continuidad de lo que
  ya empezaron a usar, y como pedido explícito del usuario en esta ronda.
- **Adopción actual**: menos de 10 personas usan Claude hoy, de forma consistente pero suelta y
  sin criterio. Sin proceso de adopción de IA formal. Todo el conocimiento del equipo es
  **empírico**, sin formación previa.
- **Estructura organizacional**: **12 departamentos en total**; mencionados explícitamente:
  Operaciones, Tecnología, Finanzas, Legal, Recursos Humanos, Contabilidad, Marketing, Ventas
  (8 de 12 — las otras 4 no se nombraron en la reunión, tampoco se inventan).
- **Objetivo central** (cita de la Ficha, Bloque D): "Reducir tiempos."
- **Único proceso detallado** (Bloque C): procesos administrativos, onboarding y facturación,
  frecuencia diaria, **tipo de dato confidencial**, la gran mayoría de las 8 horas del día se
  dedica a tareas manuales (estimación cualitativa), cuello de botella principal: todo el
  proceso es manual. **Las otras 11 áreas no tienen proceso documentado** — se auditan en la
  Fase 1 (Detección), no se asume su contenido.
- **Horizonte**: corto plazo (0-3 meses). Expectativa: automatizar procesos, reducir tiempos.
- **Reunión limitada** (precisión del usuario, ronda 2): Alejandro fue directo a pedir
  cotización, sin entrar en detalle operativo de la empresa — de ahí que el sistema solo
  cuente con 1 proceso real y una lista parcial de departamentos. La Detección existe
  precisamente para llenar ese vacío con datos reales, no para que la propuesta finja
  conocerlos de antemano.

## Restricciones (Ficha, Bloque E)

1. **Sí existe política de datos/seguridad** y **sí aplica regulación sectorial** (institución
   financiera) — el manejo seguro de datos no es solo una buena práctica genérica sino un
   requisito regulatorio real. Tema propio del Módulo I de Habilidades (no slide aparte, §4.10a).
2. **Presupuesto**: en evaluación. **Apertura al cambio**: media. **Patrocinio ejecutivo**:
   presente pero tibio (dato interno de seguimiento comercial, no cambia el contenido del deck).
3. **Restricciones operativas**: hay restricciones para sacar colaboradores de su puesto durante
   el año; **diciembre es la ventana favorable** (baja el volumen de operaciones) — nota interna
   de logística (AcroForm `Notas`), sin comprometer fechas exactas en el cuerpo del deck.
4. **Sin indicador de éxito definido**: tanto en Detección como en Habilidades, la Ficha
   registra "no cuentan con un indicador definido que justifique la inversión" — parte del
   diagnóstico (falta de método común, no solo falta de herramienta).

## Bloque específico de Detección (Ficha)

- **Modalidad de las sesiones**: Virtual.
- **Calendario disponible para sesiones por área (45-60 min c/u)**: dato real y concreto —
  confirma que la Detección se ejecuta como entrevistas cortas, una por área (hasta 12),
  no como un único taller grupal. Diciembre es la ventana preferida (bajo volumen operativo).
- **Indicador de éxito**: no definido — se usa como parte del diagnóstico.

## Bloque específico de Habilidades (Ficha)

- **Tareas reales de las sesiones**: procesos administrativos, onboarding y facturación (único
  proceso con detalle real; pista II del programa).
- **Modalidad**: Virtual en vivo (confirmada).
- **Calendario**: diciembre es la ventana preferida.
- **Restricciones operativas**: existen para sacar colaboradores de su puesto durante el año;
  diciembre es favorable.
- **Definición de éxito a 3 meses**: no cuentan con un indicador definido.

## Propuesta económica

- **Hoja "Inversión por fases"** (`.s-price`, patrón B "todo cotizado" — memoria
  `patron-fases-cotizadas-vs-diferidas`): Fase 1 (Detección) y Fase 2 (Habilidades) **ambas
  cotizadas ahora**, porque el cliente pidió explícitamente algo concreto ("mándame una
  propuesta puntual, cuánto tardaría y cuánto costaría"). Solo las **pistas adicionales** de
  Habilidades para otras áreas (más allá de la ya identificada) quedan diferidas, cotizadas
  tras la Detección — es la única pieza que genuinamente no se puede cotizar todavía sin
  inventar alcance.
- Mecánica técnica: `agregar-campo-precio.py` inyecta PrecioFase1/2/3 fijo; este deck usa
  solo Fase 1 y 2, así que `customize-bidzi.py` elimina `PrecioFase3` (huérfana) y recalcula
  el subtotal como `make_fase_subtotal_js(2)`.

## Notas de diseño

- **Base**: se parte de la propia ronda 1 de este mismo deck (clon original de
  `aerocentro-cai008/`, 12 slides, Habilidades pura) — se le inserta la Fase 1 de Detección
  (roadmap + reencuadre de Diagnóstico/Objetivos/Programa) y se reconvierte la hoja de precio
  de "Propuesta Económica" estándar a "Inversión por fases". 12 → 14 slides.
- **Roadmap de Detección** (slide 05): 3 etapas lineales (Kick-off+Entrevistas por área →
  Priorización/Mapa de Calor → Reporte Final), componente `.rmx-linear` portado de
  `good-latam-cai010/styles.css` (mismo componente, aquí vive en `overrides.css` porque este
  deck usa `../_base/styles.css` + overrides, no un `styles.css` autocontenido).
- **Sin Mapa de Calor con datos inventados**: a diferencia de `pilotes-perforados/` (que sí
  muestra un Mapa de Calor con puntuaciones Impacto/Esfuerzo/Riesgo por tener información real
  de 4 áreas ya levantada), aquí el Mapa de Calor se presenta como **entregable de la Fase 1**
  (lo que la Detección va a producir), no como una tabla ya llena — no hay datos reales de
  11 de las 12 áreas todavía.
- **Programa de Habilidades reestructurado**: Módulo I (tronco común, sin cambios de fondo) +
  Módulo II renombrado "Pista: Administración, Onboarding y Facturación" (mismo contenido de
  la ronda 1, reencuadrado como una pista entre varias posibles) + Módulo III con un nuevo
  tema "Plan de pistas adicionales por área" (reemplaza "Plan de continuidad entre áreas").
- **Impacto (§4.9)**: se mantienen las mismas fuentes de la ronda 1 (McKinsey 2023, Ardent
  Partners 2025) — con una frase añadida al hook aclarando que la Detección determinará si un
  potencial similar existe en las otras 11 áreas.
- **customize-bidzi.py**: se le agregó la limpieza de `PrecioFase3` + `make_fase_subtotal_js(2)`
  (nuevo en este script; ya usado en `customize-amcor.py` y `customize-good-latam-cai010.py`
  con `fase_count=1`). El resto (Cierre escalera, Beneficios v3) no cambió de mecánica, solo
  los textos por defecto.
- **Sin mención del stack Microsoft 365 del cliente en el deck**: se mantiene el criterio de
  la ronda 1 — Claude ya es la herramienta de foco, no hace falta encuadrarla en su ecosistema
  de productividad para este alcance.
- **No expuesto en el deck**: nombre del interlocutor (Alejandro), su correo corporativo, el
  patrocinio ejecutivo "tibio", la ventana de diciembre (queda en `Notas`, no en el cuerpo).

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh bidzi
python3 scripts/customize-acroforms.py bidzi
python3 scripts/customize-bidzi.py "clientes/propuestas/bidzi/<PDF generado>.pdf"
```

## Pendientes

- Confirmar con el usuario si la inconsistencia código (`CAI-011`) / servicio (`deteccion`)
  amerita ajuste futuro del sistema (§4.20, agrupamiento por servicio, todavía pendiente).
- Ejecutar la Fase 1 (Detección) real: entrevistas por área, Mapa de Calor, Reporte Final.
- Confirmar fechas de diciembre para las entrevistas y las 3 sesiones de Habilidades.
- Confirmar presupuesto indicativo — cajas de cotización vacías, las llena ventas.
