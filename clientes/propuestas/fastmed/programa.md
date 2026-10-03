# Programa — Agente conversacional para atención al paciente, FastMed (CAI-030)

> Capacitación In-Company · División Educación · 8 personas (equipo de Tecnología/Sistemas)
> · 3 módulos / 12 h (6 sesiones de 2 h). Dimensionado según
> `empresa/politicas-comerciales.md` → Dimensionamiento por servicio → Habilidades: 8-12h por
> área, hasta 5 procesos (FastMed tiene 2: gestión de citas, entrega de resultados). Base
> estructural adaptada de `luis-sosa-cerebro-digital/` (CAI-029), un deck Habilidades
> mono-fase de 6 sesiones ya verificado.

## 1. Información general del programa

- **Código**: CAI-030
- **Tipo**: Capacitación In-Company (sin perfil de ingreso restrictivo)
- **Empresa**: FastMed (Salud, servicios médicos corporativos)
- **Participantes**: equipo de Tecnología/Sistemas de FastMed, 8 personas, liderado por su
  Gerente de Tecnología.
- **Eje temático**: agente conversacional omnicanal (WhatsApp) para atención al paciente,
  con 2 flujos (gestión de citas/orientación de casos, entrega segura de resultados de
  laboratorio e informes dentro del plazo legal de 24-48h) y doble autenticación sobre datos
  médicos.
- **Duración**: 12 h en 6 sesiones de 2 h (1 módulo cubre 2 sesiones).
- **Modalidad**: Mixta (remota, con alguna sesión presencial puntual para la conexión de
  bases de datos, según la Ficha).
- **Acreditación**: constancia de participación INTEZIA Education.

> **Restricción de diseño (§4.11)**: FastMed ya usa Google Workspace y tiene interoperabilidad
> propia entre sus sistemas (FastTech/SoaInt). El agente se integra a ese entorno — nunca se
> afirma que la empresa migra o reemplaza su stack actual.

---

## 2. Fundamentación y justificación pedagógica

### 2.1 Planteamiento de la necesidad

FastMed gestiona hoy la entrega de resultados de laboratorio vía un sistema de tickets
integrado a WhatsApp a través de Meta, cuyo costo por iteración es alto, mientras enfrenta una
exigencia legal de entregar esos resultados en menos de 24 a 48 horas. Un **agente
conversacional** propio, construido y sostenido por su propio equipo de Tecnología, resuelve
ambas cosas: automatiza la gestión de citas y la entrega de resultados, con **doble
autenticación** que protege la data médica del paciente, algo crítico después de los 2
hackeos que la empresa sufrió este año.

### 2.2 Enfoque pedagógico (Modelo INTEZIA)

Aprendizaje Basado en Retos (ABR) — tres pilares:

- **Tutoría activa**: el facilitador acompaña la construcción del agente con feedback en
  tiempo real, sobre los sistemas y casos reales de FastMed.
- **Transferibilidad inmediata**: cada sesión construye una pieza real del agente que
  termina en producción, no un ejercicio de práctica aislado.
- **Curaduría de contenidos**: el temario se centra en los 2 flujos y la seguridad que
  FastMed necesita, no en una introducción genérica a agentes conversacionales.

---

## 3. Perfil académico

> Sin perfil de ingreso restrictivo. Requisito: el equipo de Tecnología designado por el
> Gerente de Tecnología, con acceso a los repositorios y al sistema de citas online
> existentes.

### Perfil de egreso

- **Saber**: el equipo comprende la arquitectura de un agente conversacional y los
  principios de doble autenticación y seguridad sobre datos médicos.
- **Saber hacer**: construye ambos flujos (citas, resultados), conecta el agente a los
  sistemas reales de FastMed, y lo pone en producción.
- **Saber ser**: opera y sostiene el agente con criterio de seguridad y cumplimiento legal,
  sin depender de Intezia.

---

## 4. Objetivos estratégicos

### 4.1 Objetivo general

Desarrollar en el equipo de Tecnología de FastMed la competencia de construir y sostener,
sin depender de Intezia, un agente conversacional propio para atención al paciente sobre
WhatsApp, que gestione citas y entregue resultados de laboratorio dentro del plazo legal de
24 a 48 horas, con doble autenticación y buenas prácticas de seguridad sobre la data médica.

### 4.2 Objetivos específicos

1. Diseñar la arquitectura del agente conversacional y su conexión a los sistemas
   existentes.
2. Construir el flujo de gestión de citas y el flujo de entrega segura de resultados.
3. Implementar doble autenticación y controles de seguridad sobre la data médica.
4. Poner el agente en producción y dejarlo listo para que el equipo lo sostenga y escale.

---

## 5. Estructura curricular y diseño instruccional

### 5.1 Estructura modular

| Módulo | Objetivo Instructivo | Temas | Elaboración |
|---|---|---|---|
| **I: Diseño del agente** | Comprender la arquitectura de un agente conversacional y diseñar sus dos flujos críticos | 1.1 Agente por WhatsApp / 1.2 Arquitectura del agente / 1.3 Conexión a sus sistemas / 1.4 Diseño del flujo de citas / 1.5 Diseño del flujo de resultados / 1.6 Seguridad desde el diseño | El equipo diseña ambos flujos y define principios de seguridad antes de construir |
| **II: Construcción del agente** | Construir ambos flujos y la doble autenticación que protege la data médica | 2.1 Construye flujo de citas / 2.2 Construye flujo de resultados / 2.3 Doble autenticación / 2.4 Datos médicos seguros / 2.5 Conecta sus repositorios / 2.6 Primera prueba integrada | El equipo construye ambos flujos, implementa doble autenticación y corre la primera prueba conectada a sus sistemas reales |
| **III: Producción y sostenibilidad** | Poner el agente en producción y dejar el criterio para sostenerlo y escalarlo | 3.1 Cumple el plazo legal / 3.2 Pruebas de seguridad / 3.3 Puesta en producción / 3.4 Monitoreo del agente / 3.5 Criterio de escalamiento / 3.6 Sostener el agente | El equipo verifica cumplimiento y seguridad, pone el agente en producción y define su plan de monitoreo y escalamiento |

### 5.2 Desglose instructivo (cronograma y ruta de aprendizaje)

| M | Sesión | Temas y subtemas | Tiempo | Estrategias enseñanza | Estrategias aprendizaje | Recursos y entornos |
|---|---|---|---|---|---|---|
| I | Sesión 1 (2 h) | El agente y su arquitectura: qué es un agente conversacional por WhatsApp, arquitectura del agente, conexión a sus sistemas | 30' conceptos · 30' demo · 45' práctica guiada · 15' cierre | Demostración guiada en vivo · análisis de la arquitectura del agente | Primeros conceptos de agentes conversacionales · bitácora · mapea sus sistemas actuales | Cuenta de desarrollo del agente · workbook · mapa de repositorios y citas online |
| I | Sesión 2 (2 h) | Diseño de los flujos: flujo de citas, flujo de resultados, seguridad desde el diseño | 30' demo de diseño · 60' diseño guiado · 30' revisión y ajuste | Demostración de diseño de flujos conversacionales · revisión guiada | Diseña el flujo de citas · diseña el flujo de resultados · define principios de seguridad | Plantilla de diseño de flujos · casos reales de tickets actuales |
| II | Sesión 3 (2 h) | Construcción de los flujos: construye flujo de citas, construye flujo de resultados | 30' demo de construcción · 60' construcción guiada · 30' prueba con caso real | Demostración de construcción de flujos · construcción guiada paso a paso | Construye el flujo de citas · construye el flujo de resultados | Entorno de desarrollo del agente · casos reales de citas y resultados |
| II | Sesión 4 (2 h) | Seguridad y conexión: doble autenticación, datos médicos seguros, conecta repositorios, primera prueba integrada | 40' doble autenticación y controles · 50' conexión guiada · 30' primera prueba integrada | Demostración de doble autenticación · conexión guiada a sistemas | Implementa controles de seguridad · conecta el agente a sus sistemas reales · corre la primera prueba integrada | Repositorio de resultados · sistema de citas online · checklist de seguridad |
| III | Sesión 5 (2 h) | Cumplimiento y producción: cumple el plazo legal, pruebas de seguridad, puesta en producción | 30' demo de pruebas · 50' pruebas guiadas · 40' preparación para producción | Demostración de pruebas de seguridad · análisis de casos de cumplimiento | Verifica el cumplimiento del plazo legal · prueba la seguridad del agente · prepara el paso a producción | Casos reales de solicitudes · checklist de cumplimiento |
| III | Sesión 6 (2 h) | Monitoreo y continuidad: monitoreo del agente, criterio de escalamiento, sostener el agente | 45' monitoreo del agente · 45' plan de escalamiento · 30' cómo sostenerlo | Demostración de monitoreo del agente · análisis de criterios de escalamiento | Define su plan de monitoreo · define su criterio de escalamiento · deja su plan para sostener el agente | Su agente ya construido · checklist de monitoreo · plan de mantenimiento |

> **Render en el deck**: 1 slide por sesión (`.s-schedule`) — 6 slides en total, cada una con
> su propio avance en `.ruta` (1/6 a 6/6). La slide "Cómo funciona el agente" (arquitectura)
> tiene su propia slide a la medida (`.s-graph`, reutilizada del clon de origen). **12h de
> propuesta** = 6 sesiones de 2h para el equipo de Tecnología (8 personas), que construye UN
> agente compartido, no 8 agentes individuales.

---

## 6. Garantía de calidad y seguimiento

- **Construcción curricular**: el agente se construye sobre los sistemas y casos reales de
  FastMed (repositorios, sistema de citas online), no sobre supuestos genéricos.
- **Encuesta de satisfacción**: al cierre de la Capacitación.
- **Entregables**: agente conversacional propio en producción (2 flujos + doble
  autenticación), equipo capacitado para sostenerlo y escalarlo, constancia de participación
  INTEZIA.
- **Seguimiento 30-60-90**: ver `empresa/tipos-de-documento.md §0.2` — verifica que el
  agente esté en producción, que el equipo lo escale por su cuenta, y que el cumplimiento del
  plazo legal se sostenga en el tiempo.

---

## 7. Perfil del equipo facilitador

- **Facilitación**: Equipo INTEZIA Education, con dominio de construcción de agentes
  conversacionales, seguridad de datos y doble autenticación.
- **Asesora comercial**: Verónica Rubio.
- **Competencias pedagógicas**: acompañamiento técnico personalizado, construcción de
  agentes de producción junto al equipo, curaduría de casos reales del cliente.
