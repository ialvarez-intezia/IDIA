# Brief — Grupo Corpos (Toyomax / Densa) · Construcción de Agentes de IA para Atención al Cliente (CAP-026)

## Datos administrativos

- **Cliente**: Grupo Corpos · holding venezolano con varias unidades de negocio · alcance de este proyecto: concesionarios Toyota **Toyomax** y **Densa Venezuela**
- **Naturaleza**: Capacitación in-company integral · una sola fase formativa · 100% asesoría, guía y enseñanza (sin componente de desarrollo · per nota explícita del consultor)
- **Slug**: `grupo-corpos/CAP-026 Construccion de Agentes de IA para Atencion al Cliente`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación (`CAP-026`)
- **Programa**: Construcción de Agentes de IA para Atención al Cliente · Sector Automotriz
- **Eje temático**: Diseño y construcción de 2 agentes de IA (Generador de Leads + Atención al Cliente) que se integran al stack actual del cliente (Odoo 17 + Claude + WhatsApp BSP + redes sociales) · formación práctica para que el equipo interno construya, mantenga y expanda los agentes por sí mismo · seguridad informática LLM ↔ ERP como módulo dedicado por antecedente del cliente
- **Antecedente**: Levantamiento técnico del 2026-05-12 elaborado por **David Prato** (Consultor IA Intezia · dprato@intezia.com) · 4 páginas con contexto, stack, requerimientos por agente, antecedentes técnicos y hallazgos clave
- **Fecha del brief**: 2026-05-13
- **Estado**: propuesta formativa cerrada · alcance limitado a asesoría/guía/enseñanza (per directiva explícita del consultor asignado)

## Contacto

- **Asesora comercial Intezia**: **Flavia Martínez** · +58 414-5756615 · fmartinez@intezia.com
- **Consultor / Facilitador**: **Juan Figuera** · jfiguera@intezia.com · perfil automation + customer experience con IA · facilita las 6 sesiones del programa
- **Levantamiento técnico previo**: **David Prato** · Consultor IA Intezia · dprato@intezia.com (autor del documento de levantamiento · referente técnico interno)
- **Cliente referente**: a confirmar en kick-off · líderes de TI + ventas + postventa de Toyomax y Densa

## Por qué este proyecto

Grupo Corpos opera Toyomax y Densa con un proceso de atención al cliente altamente dependiente del asesor humano. Un anuncio promocional reciente generó **+900 mensajes en pocos días** sin capacidad operativa para responder a tiempo · evidencia objetiva del ROI de automatizar con agentes de IA. El cliente ya tiene madurez técnica media (Odoo 17 en producción, suscripción Claude activa, intentaron MCP por su cuenta) por lo que la formación debe ser **práctica, no introductoria**.

Adicionalmente, el intento previo de conectar Claude a Odoo vía MCP generó **incidentes de ciberseguridad** que dejaron una cicatriz operativa. Cualquier propuesta debe abrir reconociendo ese antecedente y dedicar un **módulo completo a seguridad informática LLM ↔ ERP** · es condición indispensable para que el cliente avance con tranquilidad.

**Alcance del rol del consultor (per nota explícita de Juan Figuera)**:
- Intezia asume rol **exclusivo de asesoría, guía y enseñanza** · NO realiza desarrollo de los agentes.
- El cliente construye los agentes por sí mismo con el criterio que recibe en el programa.
- Sobre Odoo: Juan **no es experto** en la plataforma, se documenta para tener base sólida, pero el cliente es responsable de las configuraciones pertinentes en su ERP según su flujo.

Este alcance acotado **es el valor** de la propuesta: el cliente egresa con capacidad técnica propia para construir, mantener y expandir los agentes · sin dependencia continua de un proveedor de desarrollo externo.

## Diagnóstico (5 puntos · levantamiento técnico)

1. **Cicatriz de ciberseguridad** · intento previo con MCP (Claude ↔ Odoo) generó incidentes hace ~7 meses · mitigación interna con encriptación de claves vía Python · **condición indispensable: módulo dedicado a seguridad informática**.
2. **Caso de uso bien acotado · 2 agentes complementarios** · Generador de Leads (Toyomax) y Atención al Cliente (postventa Densa/Toyomax) · funciones claras y métricas medibles (leads capturados, citas confirmadas, encuestas completadas, clientes recuperados).
3. **Volumen real validado** · +900 mensajes por una sola promoción IG · justifica el ROI · la formación debe dimensionar arquitectura para ese volumen sin saturar al equipo comercial.
4. **Stack actual del cliente** · Odoo 17 (ERP/CRM principal · no se reemplaza) · sitios Densa Venezuela (en Odoo) y Toyomax (en GoDaddy) · Claude (suscripción activa) · Codex en evaluación · WhatsApp BSP integrado a Odoo como canal prioritario · IG/FB/LI deseables.
5. **Madurez técnica media** · cliente NO parte de cero · ya intentó MCP por su cuenta · formación práctica (no introductoria) con foco en arquitectura, integración y seguridad.

## Estructura del proyecto

Capacitación in-company integral · **una sola fase formativa de 12 horas** · cohort cerrado · modalidad presencial (a confirmar híbrido si el cliente lo prefiere).

- **6 sesiones × 2 horas** · una por dominio técnico · contenido práctico sobre el caso real del cliente
- **Cronograma flexible** a consideración del cliente (consistente con últimas propuestas)
- **Práctica sobre material real**: arquitectura de los 2 agentes específicos que el cliente necesita, no demos académicas
- **Alcance limitado a asesoría/guía/enseñanza** · ningún entregable es código de producción · todos son artefactos de diseño + criterio + plantillas que el cliente usa para construir

## Especificaciones del programa

- **Duración formativa total**: **12 horas académicas** · 6 sesiones × 2h
- **Modalidad**: presencial · oficinas Grupo Corpos (a confirmar híbrido si conviene)
- **Audiencia**: cohort cerrado · a confirmar (estimado 8-15 colaboradores · perfiles TI + ventas + postventa + marketing digital de Toyomax y Densa)
- **Pre-requisitos**: acceso a la suscripción Claude del cliente · contexto operativo del flujo actual (capturas de pantalla del Odoo, ejemplos de mensajes IG recibidos, plantillas de cita actual) · 1 representante de TI presente para validaciones de seguridad
- **Acreditación**: Certificado de participación INTEZIA Education al completar las 6 sesiones

## Entregables consolidados

- **Workbook digital** por participante (estándar institucional)
- **Dashboard de progreso individual** (estándar institucional)
- **Certificado INTEZIA** al completar las 6 sesiones (estándar institucional)
- **Documento de Arquitectura de los 2 Agentes** · diseño conceptual firmable que el cliente usa como referencia para construir (entregable insignia)
- **Matriz de Stack y Herramientas Integrables** · qué se usa para qué dentro del ecosistema Odoo + Claude + redes sociales
- **AUP de Seguridad LLM ↔ ERP** · marco corporativo para integraciones IA con sistemas internos · evita que se repita la cicatriz de MCP
- **Checklist de Configuraciones Odoo** · lectura técnica de qué debe configurar el cliente en su ERP (sin que Juan ejecute · el cliente es responsable)
- **Plantillas de Métricas y Observabilidad** · qué medir en cada agente (leads, citas, encuestas, recuperación)

## Alcance que NO cubre la propuesta (claridad explícita)

- **No incluye desarrollo de los agentes** · Intezia entrega arquitectura, criterio, plantillas y formación · el cliente construye.
- **No incluye configuración de Odoo** · Juan se documenta sobre la plataforma para tener base sólida · pero las configuraciones del ERP las ejecuta el equipo del cliente.
- **No incluye contratación de BSP de WhatsApp** · se recomienda en la formación cuál tipo de BSP elegir · la contratación corre por cuenta del cliente.
- **No incluye implementación de scripts de seguridad** · se enseña el AUP y los patrones seguros · el cliente los implementa.

## Estructura del programa formativo (6 módulos · 12 h · 4-5 temas por módulo)

### Módulo I · Fundamentos de Agentes de IA y Arquitectura (2 h)
1.1 Qué es un agente IA · diferencia con chatbot, asistente y automatización tradicional
1.2 Tipologías y patrones de diseño · agentes reactivos, agentes con memoria, agentes orquestadores
1.3 Arquitectura conceptual de los 2 agentes del cliente · Generador de Leads + Atención al Cliente
1.4 Selección de modelo · Claude vs Codex vs otros · criterio para cada caso

### Módulo II · Stack y Herramientas para Construir Agentes (2 h)
2.1 Frameworks y SDKs · Claude Agent SDK · function calling · tool use
2.2 Herramientas integrables al stack del cliente · WhatsApp BSP, IG/FB API, redes sociales
2.3 Modelos de orquestación · síncrono, asíncrono, colas, escalado humano
2.4 Buenas prácticas de prompt engineering para agentes · RCTF aplicado a casos del sector automotriz

### Módulo III · Diseño del Agente Generador de Leads (Toyomax) (2 h)
3.1 Lógica funcional · verificación contra base de datos · alta de nuevos leads
3.2 Identificadores robustos (nombre, cédula, teléfono) · normalización y deduplicación
3.3 Dimensionamiento para volumen real · +900 mensajes sin saturar al equipo comercial
3.4 Métricas del agente · leads capturados, conversión, tiempo de respuesta, tasa de error

### Módulo IV · Diseño del Agente de Atención al Cliente (Postventa Toyomax/Densa) (2 h)
4.1 Flujo de identificación + conversación natural + escalado a humano
4.2 Recordatorios de cita (1 semana antes) + promociones segmentadas + recuperación de inactivos
4.3 Encuestas bajo estándares Toyota · diseño conversacional y disparo automático
4.4 Métricas del agente · citas confirmadas, encuestas completadas, clientes recuperados

### Módulo V · Lectura Técnica de Odoo · Email y Social Marketing (2 h)
5.1 Mapa de módulos relevantes · Email Marketing + Social Marketing + integración con redes
5.2 Lectura técnica de la integración · qué expone Odoo, qué necesita el agente, qué configura el cliente
5.3 Por qué el canal de email está subutilizado · señales de segmentación y captación
5.4 Checklist de configuraciones que el cliente ejecuta en su Odoo (alcance del cliente · Intezia asesora, no ejecuta)

### Módulo VI · Seguridad Informática LLM ↔ ERP (2 h)
6.1 Lectura del incidente MCP previo · qué falló, por qué, qué aprender
6.2 Patrones seguros de integración · gestión de secrets, vault, scopes mínimos
6.3 AUP de Seguridad LLM ↔ ERP · marco corporativo Grupo Corpos
6.4 Auditoría y observabilidad · cómo detectar incidentes a tiempo · cierre del programa

## Stack 2026 incorporado · Multi-vendor según realidad del cliente

- **Claude** (subscripción activa del cliente): motor principal de los agentes · Claude Agent SDK · long-context para análisis de mensajes y conversaciones
- **Codex** (cliente en evaluación · sin suscripción aún): se incluye comparativa en Mod I-II · cliente decide si suscribe post-formación
- **Odoo 17** (no se reemplaza): integraciones por API · módulos Email Marketing y Social Marketing como pieza nativa para el Agente de Leads
- **WhatsApp BSP** (a contratar por el cliente · recomendación en formación): canal prioritario integrado a Odoo · evita bloqueos de Meta
- **IG, FB, LinkedIn** (deseables): canales secundarios para el Agente de Leads
- **MCP responsable**: se enseña pero con marco de seguridad post-cicatriz · NO conectar a producción sin AUP firmado

## Equipo

- **Facilitador / Consultor**: **Juan Figuera** · jfiguera@intezia.com · perfil automation + customer experience con IA · facilita las 6 sesiones · **rol exclusivo de asesoría, guía y enseñanza** (per nota del consultor) · NO desarrolla los agentes · enseña al cliente a construirlos.
- **Coordinación / Project Management**: Equipo INTEZIA Education · punto único de contacto durante las 6 sesiones y los 30 días posteriores · gestión del cronograma flexible.
- **Referente técnico interno Intezia**: David Prato (autor del levantamiento · disponible para validaciones técnicas con Juan durante el diseño fino post-aprobación).
- **Asesora comercial**: **Flavia Martínez** · +58 414-5756615 · fmartinez@intezia.com

## Notas comerciales

- Pago en Bolívares a tasa EURO BCV.
- Vigencia general de la propuesta: 30 días.
- Anticipo del 50 % al firmar el acuerdo.
- Programa registrado como **CAP-026** en INTEZIA Education al cerrar el acuerdo.
- **Estructura de cotización**: una sola cotización formativa estándar (sin componentes de desarrollo · per alcance del consultor).
- **Upsell natural post-cohort**: si el cliente desea acompañamiento durante la construcción real de los agentes, se cotiza por separado como consultoría continua (asesoría en sprints, code review de criterio, validación de seguridad) · no incluido en este deck.

## Notas de diseño

- **Estructura 11 slides estándar** · per regla 4.6 canónica · no multi-fase.
- **Slide 2 Pain abre con la cicatriz MCP** · per hallazgo clave del levantamiento (David Prato indicó que "cualquier propuesta debe abrir con esto").
- **Slide 4 Programa** · 6 módulos como cards (grid 3×2 del CSS canónico para 5-6 módulos · ajustar si conviene).
- **Slides 5-6 Cronograma** · sesiones 1-2-3 (parte 1) y sesiones 4-5-6 (parte 2).
- **Slide 7 Metodología** · pilar dedicado a "Ustedes construyen, nosotros enseñamos" (alcance del consultor explícito en deck).
- **Slide 8 Beneficios + Equipo** · descripción de Juan deja claro el rol de asesoría/guía/enseñanza · NO desarrollo.
- **Equipo named**: Juan Figuera (facilitador) · Flavia en cierre · David Prato mencionado en el brief pero no en el deck (es interno).
- **Defaults institucionales** en AcroForms (Workbook · Dashboard · Certificado / ABR · Material curado · `[CÓDIGO]` → CAP-026).
- **Modalidad presencial** mayoritaria (a confirmar híbrida si el cliente lo solicita).
- **Cronograma flexible** dentro del marco a consideración del cliente.
- **Sector automotriz + cicatriz MCP + caso de uso acotado de 2 agentes** como contexto editorial · narrativa "construyen su propio equipo aumentado, con seguridad desde el día 1".
