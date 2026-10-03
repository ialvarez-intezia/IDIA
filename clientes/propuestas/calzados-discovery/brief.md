# Brief — Calzados Discovery · Agente de IA para atención de leads (CAP-097)

## Datos administrativos

- **Cliente**: Calzados Discovery
- **Naturaleza**: Capacitación in-company · **agente de IA que califica y atiende los leads de Meta Ads hasta el punto de venta**, entregado como **proyecto único de 3 etapas secuenciales** (Auditoría/Diagnóstico → Desarrollo → Implementación), con el equipo comercial y de marketing trabajando en conjunto. No es una herramienta preconstruida entregada llave en mano: el equipo de Calzados Discovery la construye junto a nuestros consultores. **Sin bloque de formación en Claude** (Skill/Project/Artifact): el proyecto arranca directo con el diagnóstico del proceso de atención de leads.
- **Slug**: `calzados-discovery`
- **División Intezia**: `educacion` (cliente corporativo)
- **Tipo de documento**: Capacitación (`CAP-097`)
- **Programa**: Agente de IA para atención de leads — Calzados Discovery
- **Eje temático**: agente de IA que detecta el anuncio de origen de un lead de Meta Ads, consulta la información del producto, atiende y califica al cliente hasta el punto de venta, y lo entrega al equipo comercial para el cierre
- **Modalidad**: a definir en próxima reunión
- **Duración**: 3 etapas sin bloque de nivelación en Claude — Etapa 1 Auditoría/Diagnóstico (sesiones de 2h, cantidad abierta), Etapa 2 Desarrollo y Etapa 3 Implementación (ambas sin horas impuestas, a definir según el diagnóstico). Fechas exactas a confirmar.
- **Cotización**: **una sola hoja, cubre las 3 etapas completas** (no hay cotización progresiva por fase — decisión del usuario 2026-08-07, revierte el patrón de "Fase 1 solamente + progresivo" heredado de CAP-082 Aerocentro).
- **Fecha del brief**: 2026-08-07 (revisado el mismo día: se quitó el bloque de Fundamentos en Claude y se pasó a cotización única)
- **Estado**: `Borrador`
- **Esquema de referencia**: estructura de 3 etapas / cotización única, adaptada del esquema base CAP-082 Aerocentro pero **sin fases separadas ni Fundamentos**. Roadmap en 2 páginas (Etapas 1-2 / Etapa 3 + entregable final), reutilizando el componente `.rmx-linear` ya probado.

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Cliente referente**: Sebastián · Calzados Discovery (cargo pendiente de confirmar)

## Antecedente de la reunión

Sebastián llegó a la reunión con la solución ya visualizada, no con una duda abierta: quiere
un agente de IA que califique y atienda automáticamente los leads de Meta Ads hasta el punto
de venta. Su referencia es Meta AI, que usa en el extranjero y le funciona.

El dolor es concreto y le está costando ventas hoy: las campañas publicitarias generan un
volumen de leads que un equipo comercial de solo 3 personas no da abasto para atender. Los
leads se enfrían esperando respuesta y se pierden antes de llegar al punto de venta. **No es
un problema de generación de demanda** — la demanda ya la tienen — **es un problema de
capacidad de respuesta**.

El flujo que describió es específico:
1. Detectar de qué anuncio viene el lead.
2. Acceder a la información del producto.
3. Atender al cliente hasta el punto de venta.
4. Entregar el lead al equipo humano para el cierre final.

Ese último tramo lo tiene claro: **no quiere que la IA cierre la venta**, quiere que le
entregue al vendedor un lead caliente y calificado.

Se le explicó el modelo de Intezia (capacitación, no soluciones preconstruidas): su equipo
construye la herramienta junto a nuestros consultores. El argumento que hizo sentido: el
patrón de fracaso más común en estos proyectos es que un tercero construye algo complejo, se
va, y el equipo interno no puede mantenerlo — con nuestro modelo la herramienta queda
funcionando y el conocimiento se queda adentro.

**Punto de atención comercial**: Sebastián está evaluando otras ofertas de IA en paralelo y
lo dijo abiertamente — no es una conversación exclusiva. El riesgo competitivo es que otros
proveedores le ofrezcan construir el agente llave en mano, lo que sobre el papel se ve más
rápido y más cómodo que "usted lo construye con nosotros". La propuesta hace explícito el
costo de esa otra opción: un agente construido por un tercero necesita ajustes pagados cada
vez que cambia un producto, un anuncio o una promoción — cada ajuste es una factura nueva y
una espera. Con nuestro modelo, esos ajustes los hace el propio equipo de Calzados Discovery,
sin depender de nadie más. Este contraste se hace explícito en el roadmap de la página 1 de 2
(Etapas 1-2, `rmx-ethics`) y refuerza los objetivos específicos y la metodología ABR.

## Revisión 2026-08-07 (2ª pasada) — pedido explícito del usuario

1. **Se quitó el bloque de Fundamentos en Claude** (qué es un Skill, un Project y un
   Artifact). El proyecto arranca directo con la Etapa 1 · Auditoría/Diagnóstico, sin sesión
   de nivelación previa. Se retiró de: objetivos específicos, programa curricular, slide
   "El camino", schedule de la Etapa 1 y sus chips/recursos.
2. **Se eliminó la cotización por fase.** El esquema de CAP-082 Aerocentro cotizaba solo la
   Fase 1 y dejaba Fase 2-3 "a cotizar de forma progresiva". Para Calzados Discovery, el
   usuario pidió **una sola hoja de cotización que cubra todo**: Auditoría/Diagnóstico +
   Desarrollo conjunto + Implementación. Se quitó el párrafo `.cot-progressive` y el bloque
   `Duración` del `.s-price` ya no dice "Fase 1 de 3", sino que resume las 3 etapas.
3. **Se retiró la Fase 3 "Manual de políticas y uso de la IA" como etapa separada.** El
   usuario enumeró solo 3 componentes (auditoría/diagnóstico, desarrollo, implementación); el
   contenido de manual de uso/roles y permisos/protocolo de escalamiento se dobló hacia
   adentro de la Etapa 3 · Implementación como uno de sus entregables, no como una etapa con
   cronograma propio.
4. **Roadmap de 3 páginas → 2 páginas.** Con 3 etapas (no 5), el roadmap en `.rmx-linear` se
   reparte en Página 1 (Etapa 1 + Etapa 2 + checkpoint intermedio) y Página 2 (Etapa 3 +
   entregable insignia final), reutilizando el mismo componente sin tocar CSS.
5. **Deck pasó de 16 a 15 slides** (se fusionaron 3 páginas de roadmap en 2).

## Diagnóstico (5 puntos)

1. Las campañas de Meta Ads generan más leads de los que el equipo comercial (3 personas) puede atender a tiempo.
2. Cada lead espera respuesta mientras el equipo atiende uno por uno; se enfría y se pierde antes de llegar al punto de venta.
3. No hay un paso automático que identifique de qué anuncio viene cada lead ni que lo conecte con la información del producto correcto.
4. El cierre de la venta depende del equipo comercial, que hoy también atiende leads que todavía no están listos para comprar.
5. El problema no es de demanda: las campañas ya la generan. El problema es la capacidad de respuesta del equipo humano.

## Estructura del proyecto

### Agente de IA para atención de leads · equipo comercial y de marketing

Agente de IA que detecta el anuncio de origen de cada lead de Meta Ads, consulta la
información del producto, atiende y califica al cliente hasta el punto de venta, y lo
entrega al equipo comercial para el cierre final. Construido en conjunto con el equipo
comercial y de marketing de Calzados Discovery, no entregado llave en mano.

### Proyecto único de 3 etapas, cotizadas juntas

- **Etapa 1 · Auditoría/Diagnóstico** — sesiones de 2h con el equipo comercial y de marketing, mapeando cómo se atienden hoy los leads de Meta Ads, desde el anuncio hasta el punto de venta.
- **Etapa 2 · Desarrollo** — Intezia guía la construcción del agente con los hallazgos del diagnóstico, con el equipo participando en la validación. Duración según el diagnóstico.
- **Etapa 3 · Implementación** — el equipo comercial adopta el agente en su flujo diario, y se formaliza el manual de uso (qué datos procesa, quién lo ajusta, cuándo escala a un vendedor humano). Duración según el diagnóstico.

> Las 3 etapas se cotizan **juntas, en una sola hoja** — no hay cotización progresiva por
> etapa. Se usa igual en todo el deck (programa, cronograma, roadmap, hoja de precio) y en
> este brief.

## Especificaciones del programa

- **Duración**: Etapa 1 en sesiones de 2h (cantidad abierta) · Etapa 2 y 3 sin horas impuestas, a definir según el diagnóstico. Fechas exactas a confirmar.
- **Modalidad**: a definir en próxima reunión con el cliente (Presencial / Online Síncrono / Híbrido).
- **Audiencia**: equipo comercial y de marketing de Calzados Discovery (tamaño total a confirmar; incluye al equipo comercial de 3 personas que hoy atiende los leads).
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.

## Propuesta económica

- **1 sola hoja de cotización** (`.s-price`), cubre **las 3 etapas completas** (Auditoría/Diagnóstico + Desarrollo + Implementación). Sin cotización progresiva.
- La hoja incluye el bloque destacado **"Importante"** (caja con borde naranja) con la implicación comercial: el servicio se presta bajo los **términos y condiciones**, aceptados por ambas partes al avanzar con la propuesta. Enlace de referencia (mismo documento institucional que otras propuestas): https://drive.google.com/file/d/1PA-ZSt4KnyY5dpxXzgkIk6-yfGlV2eF8/view?usp=drive_link — confirmar con Legal/Ventas si Calzados Discovery necesita un enlace propio antes de enviar.

## Entregables consolidados

- Agente de IA operando: detecta el anuncio de origen, consulta el producto y atiende al lead hasta el punto de venta.
- Informe de diagnóstico del proceso actual de atención de leads.
- Manual de uso del agente (entregable de la Etapa 3 · Implementación).
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-097** en INTEZIA Education al cerrar el acuerdo.
- Sebastián está evaluando otras ofertas en paralelo — no es una conversación exclusiva. Ver *Antecedente de la reunión* arriba para el posicionamiento competitivo.

## Notas de diseño

- Formato canónico A4 landscape. Estructura base tomada de `aerocentro/` (CAP-082) y adaptada: **sin Fundamentos en Claude, sin fases, cotización única para 3 etapas, roadmap en 2 páginas** (no 3).
- **15 slides**: 3 module cards en "El camino" (una por etapa), 3 `.s-schedule` (uno por etapa), roadmap en **2 páginas** (`.rmx-linear`: página 1 = Etapa 1+2 con checkpoint, página 2 = Etapa 3 + entregable insignia), 1 sola hoja de cotización sin nota de progresividad.
- **Diferenciación competitiva explícita en el roadmap página 1** (`rmx-ethics`): contrasta el costo de un agente construido por un tercero (factura nueva por cada ajuste) contra el modelo Intezia (el propio equipo ajusta el agente que construyó).
- **Slide de Impacto**: estudios reales sobre tiempo de respuesta a leads e IA en ventas — Harvard Business Review (Oldroyd, McElheran, Elkington, 2011, "The Short Life of Online Sales Leads") y McKinsey/Salesforce (2023-2026). Fuente citada verbatim (§4.9).
- `[CÓDIGO]` sustituido por CAP-097 en Acreditación.
- Reglas §4.11 y §4.13 respetadas: no se afirma que Calzados Discovery migra de ningún stack tecnológico; sin guion largo en el copy de cara al cliente.
- **Asesora comercial**: Verónica Rubio (contacto en slide de cierre y aquí).

## Pendientes

- Confirmar modalidad (Presencial / Online Síncrono / Híbrido) en la próxima reunión.
- Confirmar apellido y cargo de Sebastián en Calzados Discovery.
- Confirmar tamaño total de la audiencia (equipo comercial de 3 + equipo de marketing).
- Confirmar fechas tentativas de inicio de las 3 etapas.
- Confirmar presupuesto indicativo del proyecto completo (las 3 etapas se cotizan juntas).
- Validar con Legal/Ventas si el enlace de términos y condiciones debe personalizarse para Calzados Discovery.
