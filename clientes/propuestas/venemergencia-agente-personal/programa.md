# Documento de Alcance del Proyecto

> Desarrollo de Agente Personal · División Educación · Cliente Venemergencia · Construcción
> nueva desde cero (no es optimización de un asistente ya existente). Este documento NO sigue
> el formato de un currículo de Habilidades (no hay perfil de ingreso, módulos con horas ni
> cronograma de sesiones de clase) porque el servicio no lo es: es un proyecto de desarrollo
> de software a la medida. Se documenta aquí igual, en el formato más cercano posible, por
> ser la fuente de verdad de Entregables que exige CLAUDE.md §4.14.

## 1. Información general del proyecto

- **Código**: CAI-028
- **Cliente**: Venemergencia (empresa venezolana de servicios de emergencia y atención,
  marco de alianza con Intezia — ver `venemergencia/brief.md`)
- **Destinatario**: Andrés Simón
- **Naturaleza**: Desarrollo de un asistente personal a la medida sobre **una plataforma de
  automatización**, integrado a WhatsApp (canal de comunicación principal) y Google Workspace.
- **Punto de partida**: construcción **nueva**, no hay asistente previo de Andrés Simón que
  optimizar o ampliar.
- **Acreditación**: sin certificado — es una entrega de software, no una capacitación.
- **Advertencia de plataforma**: la herramienta de automatización utilizada es de reciente
  lanzamiento, en fase temprana. Intezia no tiene control ni asume responsabilidad sobre su
  seguridad ante
  posibles vulnerabilidades o filtraciones de datos propias de la plataforma. Se implementan
  medidas de prevención y manejo adecuado de la información como parte del alcance.

## 2. Por qué este proyecto

Andrés Simón necesita un asistente personal capaz de operar en múltiples grupos de WhatsApp
a la vez, manteniendo el contexto de cada conversación por separado, y de automatizar tareas
operativas repetitivas (correos, agenda, contactos) que hoy consumen tiempo manual. Al mismo
tiempo, dado que la solución se apoya en una plataforma de automatización en fase temprana,
el proyecto incorpora desde el diseño medidas de prevención y control sobre el consumo de IA y
el manejo de la información.

## 3. Alcance funcional

La solución permite:

- Gestionar múltiples conversaciones de WhatsApp de forma simultánea, cada una con su propio
  contexto (memoria aislada por grupo/canal).
- Automatizar tareas operativas: lectura y gestión de correos, agenda (crear/consultar/
  eliminar eventos, incluidos los que llevan Google Meet e invitados) y contactos.
- Integrar Google Workspace de forma completa: Gmail, Calendar, Drive, Docs, Sheets,
  Contacts, Tasks.
- Mantener privacidad y control de acceso por tipo de usuario.
- Escalar el uso sin comprometer la estabilidad del sistema.

## 4. Objetivos

### 4.1 Objetivo general

Diseñar y construir el asistente personal de Andrés Simón para operar de forma eficiente en
múltiples grupos de WhatsApp, integrando gestión de contactos, automatización de correos y
control de consumo de inteligencia artificial, con estabilidad operativa y control sobre su
información.

### 4.2 Objetivos específicos

1. Gestionar múltiples conversaciones de WhatsApp de forma simultánea, cada una con su propio
   contexto.
2. Automatizar tareas operativas del día a día: correos, agenda y contactos.
3. Mantener privacidad y control de acceso por tipo de usuario.
4. Prevenir y manejar con cuidado la información, dado que la solución se apoya en una
   herramienta de automatización de reciente lanzamiento en fase temprana.

## 5. Fases del proyecto y cronograma

| Fase | Qué comprende | Sesión con el cliente |
|---|---|---|
| Kick-off | Confirmación de accesos y alcance | Sí (30-60 min) |
| Auditoría y configuración inicial | Revisión del agente, canal de WhatsApp, modelo y skills activas | Sí |
| Integración con Google Workspace | Conexión de Gmail, Calendar, Drive, Docs, Sheets, Contacts, Tasks | Sí |
| Memoria y comportamiento del agente | Reglas de comportamiento, contexto persistente entre canales | Sí |
| Operación multigrupo de WhatsApp | Aislamiento de contexto por grupo/conversación | Sí |
| Validación funcional | Pruebas de las capacidades entregadas junto con Andrés Simón | Sí |
| Ajustes y entrega | Correcciones finales y entrega del proyecto con credenciales | Sí |

> **Nota**: la división de las 6 sesiones de seguimiento (una por fase técnica) es una
> interpretación del ritmo martes/jueves pedido por el usuario para el calendario — no viene
> de un desglose de horas explícito. Confirmar con el usuario/Venemergencia antes de enviar.

## 6. Garantía y entregables

- **Entregables**: asistente personal operando sobre la plataforma de automatización e
  integrado a WhatsApp; automatización de correos, agenda y contactos vía Google Workspace;
  documentación técnica y credenciales de acceso; medidas de prevención y manejo seguro de la
  información.
- **Mantenimiento y Soporte (opcional, no incluido en esta cotización)**: soporte correctivo,
  acompañamiento técnico ante incidencias, actualizaciones de los componentes ya instalados y
  atención de fallas de conectividad — no incluye nuevas integraciones, herramientas o
  cambios fuera del alcance actual. Se cotiza aparte, de forma mensual.

## 7. Perfil del equipo

- **Consultoría técnica**: Equipo INTEZIA, con dominio de configuración de agentes de IA
  sobre WhatsApp, integración con Google Workspace y manejo de memoria/comportamiento
  persistente del agente.
- **Asesora comercial**: María Iribarren.
