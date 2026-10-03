# Brief — Meru

## Datos administrativos

- **Empresa**: Meru (alianza / consorcio de profesionales independientes)
- **Sector**: Administración de empresas y emprendimientos independientes
- **Slug**: `meru`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-056`)
- **Eje temático**: IA aplicada con Claude (productividad y automatización administrativa, dominio de la herramienta de la A a la Z)
- **Fecha del brief**: 2026-06-12
- **Estado**: borrador / propuesta inicial

## Contacto

- **Persona contacto**: Loredana
- **Asesora de ventas Intezia**: María Iribarren
- **Facilitación**: Equipo Education (sin consultor nominado en el deck)

## Necesidad detectada

Un grupo de **4 mujeres profesionales independientes** que operan dentro de una misma alianza, repartidas en distintas empresas y áreas. Ya **pagan Claude Pro ($20/mes por usuaria)** pero lo desaprovechan casi por completo: sufren el «síndrome de la hoja en blanco», no estructuran prompts, desconocen la lógica de los tokens (la barra de consumo) y no usan módulos avanzados como **Projects** o **Artifacts**. Confunden además limitaciones de hardware y conectividad con problemas de la IA. El objetivo es que dominen Claude **de la A a la Z**: que dejen de usarlo como un chat básico y lo operen como un entorno de productividad que les ahorre horas y les evite contratar personal administrativo extra.

## Contexto

- Capacitación **grupal pequeña** (4 participantes), perfil pragmático: buscan herramientas listas para usar, no código.
- Operan de forma **descentralizada**, sin LMS ni servidores propios. Sí tienen licencias Claude Pro activas y data real e histórica de sus negocios para casos prácticos 100% personalizados.
- Realidad **Venezuela**: lidian con conectividad inestable, bloqueos geográficos para acceder a las IA, uso confuso de la red privada virtual (VPN) y optimización de la memoria de sus computadoras. El programa incluye dejar resuelto ese entorno técnico.
- Stack actual: Microsoft Excel intermedio, Dropbox, Gmail y CRM/sistemas administrativos de su sector (exportan reportes en PDF/Excel). Usan Gemini y ChatGPT gratuitos en el teléfono de forma empírica.
- Casos reales del día a día: conciliación de cuentas por pagar, control de facturas vs. abonos (información dispersa en imágenes, chats y correos), redacción de correos de cobranza y seguimiento, transcripción de datos y reportes semanales/mensuales.

## Especificaciones del programa

- **Duración**: 12 horas académicas (6 sesiones de 2 horas, 6 módulos).
- **Modalidad**: **sin definir** (no se afirma online ni presencial en el deck; «sesión en vivo» = síncrona). A confirmar con el cliente.
- **Fechas**: no definidas (a coordinar).
- **Audiencia**: 4 participantes (mujeres, 30-45 años, nivel principiante en IA corporativa).
- **Ecosistema**: Claude (preferencia explícita). Gemini se enmarca como herramienta complementaria para consultas rápidas.
- **Precio**: la propuesta lleva slide de Propuesta Económica; ventas llena los campos de cotización en Adobe Reader.

## Entregables esperados por el cliente (ficha)

- Workbooks.
- Certificados.
- **Repositorio de Prompts Maestros y Plantillas de Proyectos organizadas por área**.

## Decisiones de diseño

- Clonada de la capacitación canónica mono-fase, vía `crediya/` (mismo eje Claude, misma asesora María).
- **6 módulos / 12 h** (un módulo extra dedicado al setup técnico de Venezuela: VPN, RAM, app de escritorio y gestión de tokens), porque el grupo es principiante y la fricción técnica es parte explícita del dolor.
- **Capacidades nativas de Claude como fundamento** (instrucción del usuario, 2026-06-12): el programa cubre explícitamente **qué modelo usar y cuándo** (Opus, Sonnet, Haiku) y **cómo optimizar el consumo de tokens** (Módulo II), y **Skills, plugins y conectores (MCP)** además de Projects (Módulo V). No se queda en fundamentos/prompting. Alinea con la regla de incluir capacidades actuales de Claude.
- Sin consultor nominado en la slide de Beneficios (Equipo Education presentado de forma genérica).
- Slide de Impacto con datos de estudios reales citados (Stanford HAI AI Index 2026, McKinsey State of AI 2025, Anthropic Economic Index 2025).
- No se afirma que Meru migra de stack: Claude es la herramienta que **ya pagan** y subutilizan; Gemini queda como complemento (§4.11).
