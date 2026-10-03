# Brief — DUSA · Servicio de Habilidades, 5 áreas (CAI-012)

## Datos administrativos

- **Cliente**: DUSA · industria licorera (producción, envasado y distribución de bebidas alcohólicas)
- **Naturaleza**: Capacitación in-company · **servicio de Habilidades como siguiente paso del servicio de Detección ya entregado** (Informe Final de Auditoría IA — DUSA, Fase IV, 2026-09-04). No repite diagnóstico: parte directo de la hoja de ruta priorizada de la sección 07 de ese informe, construyendo y adoptando con el equipo operativo de las 5 áreas auditadas.
- **Slug**: `dusa-cai012`
- **División Intezia**: `educacion` (cliente corporativo)
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: Capacitación (`CAI-012`)
- **Programa**: Servicio de Habilidades — DUSA (5 áreas)
- **Eje temático**: construcción y adopción de automatización con IA sobre el ecosistema Microsoft 365, con Copilot como capa de asistencia y Copilot Studio como motor de agentes (recomendación explícita del informe de Detección, sección 06), aplicada a las 5 áreas auditadas
- **Modalidad**: **Presencial** (confirmado por el usuario, igual que las sesiones de auditoría)
- **Duración**: sin cifras de sesiones/semanas comprometidas — el informe de Detección no da cronograma temporal, solo el orden de construcción por prioridad (sección 07). Frecuencia y duración de sesiones a definir en kick-off.
- **Fecha del brief**: 2026-09-07
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: María Iribarren · +58 414 0570056 · miribarren@intezia.com
- **Cliente referente**: **DUSA** (instrucción explícita del usuario — sin nombre de contacto ejecutivo individual; no confundir con los líderes de área, que sí están documentados en el informe de auditoría pero no son el referente de cierre del deck)

## Antecedente — no es la primera propuesta de DUSA en el sistema

DUSA ya tiene 4 propuestas previas en `clientes/propuestas/`: `CH-007` (charla, 2026-08-03), `CAP-087` (Manual de Políticas y Gobernanza Ética de IA, 2026-08-03), `CAP-088` (Auditoría de automatización acotada a Comercial + Finanzas, 2026-08-03/13) y `CH-010` (charla, 2026-08-31). **Esta propuesta (CAI-012) no las reemplaza ni las modifica** — nace de un informe de Detección posterior y más amplio (5 áreas, 2026-09-04) que **CAP-088** (2 áreas, agosto 2026). Se deja constancia por si el usuario quiere reconciliar ambos proyectos más adelante; no se tocó ningún archivo de `dusa-cap088/`.

**Diferencia de posicionamiento con CAP-088**: CAP-088 evitaba nombrar herramientas ("Claude", "Copilot", "Microsoft 365") por instrucción explícita del cliente en ese momento (evaluación caso por caso de Claude frente a Copilot). El informe de Detección que sustenta esta propuesta (CAI-012) **recomienda explícitamente Microsoft 365 + Copilot + Copilot Studio** como el ecosistema a construir (sección 06) y no menciona a Claude en ningún punto — por lo tanto, aquí sí se nombra Microsoft 365/Copilot/Copilot Studio abiertamente, consistente con la fuente. No hay conflicto: son documentos de alcance distinto en momentos distintos.

## Fuente primaria — Informe Final de Auditoría IA (Detección, ya entregado)

Los 3 documentos que sustentan esta propuesta (aportados por el usuario, no generados por este sistema):
- `Informe_Final_Auditoria_IA_DUSA.pdf` — informe completo, 10 páginas.
- `OnePager_Requerimientos_Tecnicos_DUSA.pdf` — dirigido a Sistemas de DUSA.
- `Resumen_Informe_Final_Auditoria_IA_DUSA.pdf` — resumen ejecutivo.

Índice de Madurez consolidado: **2,6** (Cultura 4 · Herramientas 3 · Datos 2 · Talento 2 · Gobernanza 2). El techo de complejidad admisible es 3,6. La recomendación explícita del informe (sección 10) es activar el servicio de Habilidades como siguiente paso.

**3 agentes ya construidos durante las sesiones de fundamentos y auditoría** (no prototipos, ya en manos del equipo): generador de creativos para puntos de activación (Comercial), validador del consolidado de cobros (Cuentas por Cobrar), agente de estructuración de estados financieros (Contabilidad y Cuentas por Pagar). Esta propuesta **extiende** ese trabajo ya hecho, no parte de cero.

## Diagnóstico (5 puntos — resumen del informe de Detección, uno por área)

1. **Contabilidad y Cuentas por Pagar** — más de 300 facturas al mes registradas 100% a mano, con la jornada completa de un equipo dedicada a digitar datos que ya existen en la factura escaneada y la orden de compra del sistema.
2. **Tesorería** — 130 cuentas bancarias de 15 empresas, cerca de 5.000 movimientos mensuales, atendidos por 2 personas donde antes había 5; la mitad de la jornada se consume descargando y cargando extractos banco por banco.
3. **Cuentas por Cobrar** — cerca de 15.000 partidas de ingreso por contrastar, con una cartera que creció de 105 a 500 clientes mientras el equipo se reducía de 4 analistas a 2.
4. **Finanzas** — más de 20 archivos de Excel encadenados por fórmulas, con toda la lógica de vínculos concentrada en una sola persona; el cuello de botella real es la espera por la entrega de información de otras áreas.
5. **Comercial (Región Centro-Sur)** — falso estatus de mora por desfase de conciliación (afecta a ~18 clientes por semana) y seguimiento de cobranza llevado en cuaderno, a mano.

## Estructura del proyecto

### 5 áreas · mismo recorrido: Construcción (Intezia) → Adopción

El **diagnóstico ya se hizo** (servicio de Detección, informe adjunto) — esta propuesta no lo repite. Cada área recorre, de forma independiente, sobre las prioridades ya definidas en la hoja de ruta del informe (sección 07):

1. **Contabilidad y Cuentas por Pagar** — lectura automática de factura escaneada y extracción de campos (depósito en tablas de interfaz de JD Edwards) → validador fiscal (retenciones, IVA, tasa del dólar) → asistente de asignación y aprobación de pagos → extensión del agente de estados financieros ya construido → plantilla única de reporte y tablero.
2. **Tesorería** — validación de movimientos bancarios con alerta de descuadre (declarada por el líder "la columna vertebral de la tesorería") → disponibilidad bancaria neta → comparativa de flujo de caja proyectado contra real → bandeja de correo segmentada → seguimiento de tareas.
3. **Cuentas por Cobrar** — extensión del validador ya construido a la depuración y sinceración de la cuenta por cliente → imputación de pagos → determinación del descuento financiero aplicable → normalización del cuadro nacional de descuentos comerciales.
4. **Finanzas** — extensión del agente de presentación de premisas al comité ya construido → agente del plan de nómina → agente del plan de producción de alcohol → consolidador de los factores de mano de obra → contratos de datos con cada área proveedora.
5. **Comercial (Región Centro-Sur)** — extensión del generador de creativos ya construido al ciclo completo de activación → asistente de recordatorios de cobranza → gestor de descuentos por cliente con tasa del día → diseñador de cabezal y exhibición en punto de venta.

### Ritmo por área: Kick-off → Construcción (Intezia) → Adopción

- **Kick-off** — se presenta la hoja de ruta ya priorizada por el informe de Detección y se valida con cada líder de área; se agenda todo en esta misma sesión.
- **Construcción (Intezia)** — Intezia construye cada caso priorizado, con el equipo operativo de cada área participando en la validación, sobre el ecosistema Microsoft 365 que DUSA ya opera (Copilot como capa de asistencia, Copilot Studio como motor de agentes — recomendación del informe de Detección, sección 06).
- **Adopción** — se activan los casos construidos en el día a día de cada equipo y se transfiere el conocimiento para que cada líder los mantenga de forma independiente.

Sin cifras de sesiones o semanas comprometidas — el orden de construcción está fijado por el informe (prioridades 1 a N por área), pero la frecuencia y duración exacta de sesiones se define en el kick-off, igual que otras propuestas multi-fase de la casa (aerocentro, aerocentro-clon-salomon).

## Especificaciones del programa

- **Duración**: sin horas ni número de sesiones comprometido de antemano; el orden de construcción sigue las prioridades ya definidas en la sección 07 del informe de Detección. A definir en kick-off.
- **Modalidad**: Presencial.
- **Audiencia**: equipo operativo de las 5 áreas auditadas — 23 personas identificadas en el informe de Detección como quienes ejecutan los procesos (6 Contabilidad y CxP, 9 Comercial, 4 Cuentas por Cobrar, 2 Tesorería, 2 Finanzas), con cada líder de área participando en la validación.
- **Fechas tentativas**: sin fechas — a confirmar en kick-off (instrucción explícita del usuario).
- **Acreditación**: constancia de participación INTEZIA Education.

## Propuesta económica

- **Cotización única consolidada** (confirmado por el usuario): las 5 áreas se cotizan juntas como un solo sistema, 1 sola hoja de precio (`.s-price`), sin desglose por área.
- **El monto cubre el servicio de Habilidades de Intezia únicamente.** El licenciamiento tecnológico (Microsoft 365 Copilot + paquete de capacidad de Copilot Studio, estimado en USD 890/mes en el informe de Detección) es un costo aparte que DUSA contrata directamente con Microsoft — no está incluido en esta cotización ni Intezia lo factura. Se aclara en el campo `Notas` del AcroForm para evitar confusión.
- Bloque `cot-terms-box` con enlace a términos y condiciones institucionales (mismo patrón que el resto de la casa).

## Entregables consolidados

- Casos construidos y activados en las 5 áreas, extendiendo los 3 agentes ya construidos en las sesiones de fundamentos y auditoría.
- Hoja de ruta priorizada ya entregada (informe de Detección) — se ejecuta, no se rehace.
- Transferencia de conocimiento documentada por área — cada líder capacitado para mantener y evaluar nuevos casos por su cuenta.
- Constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAI-012** en INTEZIA Education al cerrar el acuerdo.

## Notas de diseño

- **Base estructural**: clon adaptado de `dusa-cap088/` (mismo cliente, roadmap de 3 etapas ya extendido en su `styles.css` local, multi-área con `.s-schedule` una por área) — extendido de 2 a 5 áreas, y de "Diagnóstico + Construcción + Implementación" a "Construcción + Adopción" (el Diagnóstico ya no es parte de esta propuesta: lo cubrió el servicio de Detección, informe adjunto).
- **Formato de Beneficios v3** (2026-08-28, ver `plantillas/propuesta-comercial.md`): Resultados · Por qué Habilidades · Entregables · Valor inmediato, tarjetas oscuras, tomado de `simple-tv-cai002/`. **Sin Metodología ABR ni Equipo facilitador** (§4.10a, retirados 2026-08-26) — `dusa-cap088/` todavía los tenía por ser anterior a esa fecha; no se propaga a `dusa-cap088/` (no retroactivo).
- **Cierre tipo escalera** (2026-08-26): 4 cajas AcroForm editables (`CierreResultado`, `CierrePaso1-3`), tomado de `simple-tv-cai002/`. Correo `servicio@intezia.com` en `.end-contact` (no `info@intezia.com`, que sí aparecía en `dusa-cap088/` por ser anterior).
- **Portada**: eyebrow "Propuesta formativa · Servicio de Habilidades" (regla bloqueante 2026-09-01, §4.1a punto 4).
- **`.s-program`**: 5 module cards en modo compacto (3×2, ya soportado por el CSS heredado de `dusa-cap088/`).
- **`.s-schedule`**: 5 slides, una por área. 3 columnas por slide: "Punto de partida (ya auditado)" (resumen breve del hallazgo de Detección, sin repetir el diagnóstico completo) · "Construcción (Intezia)" (`block-rec`, prioridades de la sección 07) · "Adopción" (transferencia).
- **`.s-roadmap`**: 3 etapas (Kick-off/Validación → Construcción → Adopción), `rmx-origin` "Recorrido por área" con las 5 áreas listadas, mismo componente `.rmx-*` de `dusa-cap088/` reencuadrado sin la etapa de Diagnóstico.
- **Sin heatmap**: se optó por no incluir `.s-heatmap` (mismo criterio que la revisión final de `dusa-cap088/`) — la distribución IA Generativa/Analítica de la sección 05 del informe es información de Detección, no aporta a la propuesta de Habilidades en sí.
- **Impacto**: se reutilizan los 2 estudios reales ya validados en `dusa-cap088/` (McKinsey 2023 para productividad de marketing/ventas — aplica a Comercial; Ardent Partners 2025 State of ePayables — aplica al ciclo compra-pago de Contabilidad y CxP), ambos siguen siendo estudios reales y verificables, sin necesidad de repetir la búsqueda.
- **Nombres de herramientas SÍ aparecen** (Microsoft 365, Copilot, Copilot Studio) — a diferencia de `dusa-cap088/`, porque el informe de Detección que sustenta esta propuesta los recomienda explícitamente (sección 06) y no hay instrucción del cliente de ocultarlos en este alcance.
- **Sin afirmar migración de stack** (§4.11): DUSA ya opera Microsoft 365; el copy dice que el servicio activa/expande su uso, nunca que DUSA migra a él.
- **Acrónimos**: "IA", "SEO" no aplica aquí. "JD Edwards", "SQL Server" son nombres propios de sistemas ya usados por el cliente, no siglas de jerga — no requieren expansión. "IVA" es de uso general en Venezuela, no requiere expansión.
- **Sin guion largo** (§4.13), sin "cohorts" (§4.4).

## Pendientes

- Confirmar con el usuario si quiere reconciliar esta propuesta con `dusa-cap088/` (2 áreas, agosto 2026) — por ejemplo, marcar CAP-088 como superada o mantenerla como propuesta independiente ya enviada.
- Confirmar número exacto de sesiones/semanas por área con el usuario o el consultor asignado, una vez agendado el kick-off.
- Confirmar presupuesto indicativo del servicio de Habilidades (no discutido aún).
- Confirmar si el orden de construcción por área (Contabilidad y CxP → Tesorería → Cuentas por Cobrar → Finanzas → Comercial, tomado del orden de la sección 07 del informe) es el que DUSA quiere seguir, o si prefiere otro orden de arranque.
