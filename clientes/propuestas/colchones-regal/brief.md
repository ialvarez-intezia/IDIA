# Brief — Colchones Regal

---

## Datos administrativos

- **Empresa**: Colchones Regal
- **Sector**: Manufactura y retail (fábrica de colchones, venta al detal y al mayor)
- **Slug**: `colchones-regal`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-043`)
- **Eje temático**: Automatización con IA en dos fases — Marketing (IA generativa + bot de Instagram) y Desarrollo (IA agéntica omnicanal con n8n)
- **Fecha del brief**: 2026-06-04 · **Actualizado**: 2026-06-08
- **Estado**: propuesta de dos fases, ambas cotizadas en el mismo deck

## Contacto

- **Persona contacto**: Norkis (Directora General) — datos por confirmar
- **Solicitante interno (ficha)**: Isabella Palazzone (Intezia)

## Necesidad detectada

El volumen de mensajes directos (DM) de Instagram que llegan desde los anuncios pagados de Colchones Regal crece más rápido de lo que el equipo puede responder a mano. Hoy la directora gestiona personalmente los DM mientras atiende la tienda física, lo que genera demoras y pérdida de clientes. La empresa tiene dos perfiles con necesidades distintas: un **equipo de marketing** que produce contenido y atiende redes de forma empírica, y un **perfil de desarrollo** con base técnica. Por eso la formación se separa en dos fases independientes, ambas cotizadas.

El equipo de desarrollo de Intezia está copado hasta septiembre, así que en lugar de construirles las automatizaciones, **se les capacita para que las construyan y mantengan ellos mismos** (autosuficiencia, sin cuotas de mantenimiento de un tercero).

## Reestructuración 2026-06-08 (decisión del usuario)

La propuesta deja de unir ambos departamentos en una sola formación. Ahora son **dos formaciones separadas, ambas cotizadas en este deck**:

- **Fase 1 · Marketing** (8 h · 4 sesiones de 2 h): potenciar al equipo de marketing con IA generativa (**Gemini** para copy/ideas, **Higgsfield** para imágenes y video) y su primer bot de atención en Instagram con **ManyChat** (automatización del primer acercamiento al chatbot).
- **Fase 2 · Desarrollo** (10 h · 5 sesiones de 2 h, **1 a 1**, facilitada por **Isaac**): IA agéntica con **n8n** para crear automatizaciones y agentes conversacionales **omnicanales** que centralizan y automatizan el seguimiento de todos los canales/redes desde un único sitio (Instagram + WhatsApp vía Kommo o API directa).

Cada fase tiene su **propio desglose instructivo** con sus horas específicas.

## Contexto

- Empresa grande de operación pero con poco personal: la dirección termina atendiendo mensajes y tienda a la vez.
- Equipo de TI de 2 personas; el perfil de programación es el público de la Fase 2.
- Marketing usa Gemini de forma empírica; es el público de la Fase 1.
- Quieren evitar el retainer de un desarrollador externo; una cuota baja de SaaS que ellos controlan es aceptable.

## Decisión de herramienta (analizada con el cliente)

- **Fase 1 (Marketing)**: **Gemini** (copy, ideas, calendario), **Higgsfield** (imágenes y video) y **ManyChat** (bot de Instagram no-code, partner oficial de Meta).
  - **IA nativa de ManyChat** (Intention Recognition + AI Step) para entender intención y responder; no se integra un modelo externo en esta fase.
  - **Matices verificados** (van al deck, §4.9): la API de Instagram solo permite responder a quien escribió en las últimas 24 h (no DM en frío) y tiene un tope de 200 llamadas/hora (2026). No afecta el caso (responden a leads que ya escribieron), pero se monitorea.
  - **ManyChat queda solo para Instagram** en la Fase 1 porque su integración con WhatsApp da errores. El canal omnicanal con WhatsApp se construye en la Fase 2 con n8n.
- **Fase 2 (Desarrollo)**: **n8n** como centro de automatización; mensajería omnicanal vía **Kommo** o la **API directa de WhatsApp** (las dos opciones se presentan al cliente). IA agéntica para automatizar el seguimiento centralizado.

## Especificaciones del programa

- **Duración**: Fase 1 = 8 h (4 sesiones × 2 h) · Fase 2 = 10 h (5 sesiones × 2 h).
- **Modalidad**: **por confirmar** (no afirmar en el deck). Las sesiones son en vivo; la modalidad se fija en la reunión de arranque.
- **Audiencia**: Fase 1 = equipo de marketing · Fase 2 = perfil de desarrollo (formato 1 a 1).
- **Aliado**: ninguno.
- **Infraestructura del cliente**: licencia de Google; cuenta de Instagram profesional (Meta Business).
- **Entregables esperados por el cliente**: Workbooks + Certificados.
- **Fechas tentativas**: junio 2026 ("este mes"), por confirmar.

## Equipo asignado

- **Facilitador Fase 1 (Marketing)**: Equipo INTEZIA Education (sin nombrar persona específica).
- **Facilitador Fase 2 (Desarrollo)**: **Isaac**.
- **Asesora comercial**: Isabella Palazzone.

## Notas internas

- Cliente con alto potencial de recurrencia. Ahora ambas fases se cotizan juntas; pueden contratarse en bloque o por separado.
- Perfil de egreso completo cubre Fase 1 + Fase 2; este deck entrega ambas.
