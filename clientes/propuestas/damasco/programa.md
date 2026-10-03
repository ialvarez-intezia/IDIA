# Documento Oficial de Diseño Curricular e Instruccional

**[LOGO INTEZIA — `logos/educacion/NEGRO.png`]**  /  **[LOGO DAMASCO]**

# Capacitación in-company · Fase 1
## Inteligencia Artificial aplicada a la operación retail

**Código**: CAP-037
**Versión**: 2026-06 (propuesta DAMASCO)
**Elaborado por**: Equipo INTEZIA Education
**Facilitador / Consultor**: Rafael Carreño
**Asesora de proyecto**: Isabella Palazzone
**Fecha**: 2026-06-01

---

## 1. Información general del programa

- **Nombre**: Inteligencia Artificial aplicada a la operación retail (Fase 1)
- **Modalidad**: Presencial
- **Duración**: 12 horas · 2 rutas departamentales (Desarrollo 8 h · Soporte 4 h)
- **Stack de enseñanza**: Claude, Claude Code y Cowork como eje común; Desarrollo suma ChatGPT/Codex (ya no Gemini, actualización 2026-09-15). Todo integrado al entorno híbrido (Google + Microsoft, SAP Business One, Power BI) que DAMASCO ya usa.
- **Acreditación**: INTEZIA

---

## 2. Fundamentación y justificación pedagógica

### 2.1 Planteamiento de la necesidad

DAMASCO mueve un catálogo grande y rápido: entran entre 60 y 100 productos nuevos los viernes por la tarde, los precios cambian a diario y la operación procesa del orden de 100.000 facturas diarias sobre 16.000 artículos en 54 sucursales. Los equipos ya usan IA, pero cada uno a un nivel distinto y sin un método común que la convierta en automatización. El cliente pidió expresamente segmentar por departamento según su madurez real, no una charla pareja para todos.

### 2.2 Enfoque pedagógico (Modelo INTEZIA)

Aprendizaje Basado en Retos (ABR):

- **Tutoría activa**: el facilitador acompaña cada práctica con feedback inmediato. En Desarrollo trabaja con dos mesas en paralelo; en Soporte acompaña paso a paso con casos reales de infraestructura, ya en nivel intermedio.
- **Transferibilidad inmediata**: cada ejercicio sale de un proceso real de DAMASCO (automatización de flujos, atención de incidencias, auditoría de datos). Lo que se practica se aplica al día siguiente.
- **Curaduría de contenidos**: solo lo que sirve a cada departamento según su nivel, sin teoría desconectada de la operación retail.

> **Regla de stack (CLAUDE.md §4.11):** el programa se integra al entorno híbrido del cliente, no lo cambia. El equipo de BI centraliza en Power BI: la ruta de datos de Desarrollo **alimenta esos tableros, no construye dashboards en otra herramienta**.

---

## 3. Perfil de egreso

- **Saber (Cognitivo)**: identifica qué procesos de su área se pueden automatizar con IA.
- **Saber hacer (Procedimental)**: aplica IA a un cuello de botella real con flujos y prompts replicables.
- **Saber ser (Actitudinal)**: usa la IA con criterio, verifica resultados y cuida la información sensible de la empresa y de sus clientes.

> Capacitación in-company: no se exige perfil de ingreso. Cada ruta entra al nivel real de su equipo (Desarrollo avanzado, Soporte intermedio).

---

## 4. Objetivos estratégicos

### 4.1 Objetivo general

Llevar a los equipos de Desarrollo y Soporte de DAMASCO a aplicar IA sobre los cuellos de botella reales de su operación, con práctica segmentada por nivel de madurez, para pasar de un uso disperso a una automatización con método.

### 4.2 Objetivos específicos

1. **Desarrollo**: profundizar con todo el equipo en el dominio fino de Claude Code, Cowork y ChatGPT/Codex, con prompting estructurado, y abrir dos frentes de práctica: agentes eficientes con balance de carga y control de costos de tokens (programadores) y bases de datos con IA que alimentan Power BI (SAP y BI).
2. **Soporte**: profundizar al equipo en IA generativa aplicada a infraestructura y resolución de incidencias técnicas cotidianas, y sumar un bloque administrativo (resumen de reuniones, correo conectado a IA, sugerencias) a su propia gestión del área.

---

## 5. Estructura curricular y diseño instruccional

### 5.1 Estructura por rutas (una por departamento)

| Ruta | Nivel · Personas | Objetivo Instructivo | Temas | Elaboración (Práctica) |
|---|---|---|---|---|
| **1 · Desarrollo · Ingeniería de IA** (8 h · 9 personas) | Avanzado parejo · un solo grupo, dos mesas en la práctica | Industrializar flujos del equipo con IA, atacando flujos sin automatizar y costos de tokens sin control. | Dominio de Claude Code, Cowork y ChatGPT/Codex · Prompting estructurado y de lógica compleja · Agentes eficientes con balance de carga (Claude Code + OpenCode) · Control de costos de tokens · Bases de datos con IA · Resultados que alimentan Power BI | Mesa A (4 programadores): construye un agente eficiente, con balance de carga, que automatiza una auditoría o flujo repetitivo. Mesa B (2 SAP + 2 BI): consulta bases de datos en lenguaje natural y deja los resultados listos para sus tableros de Power BI. |
| **2 · Soporte · Infraestructura e IA** (4 h · 6 personas) | Intermedio · aplicación práctica | Profundizar al equipo en IA generativa aplicada a infraestructura, incidencias y su propia gestión administrativa. | Prompting de infraestructura y diagnóstico · Incidencias reales · Asistente de conocimiento · Resumen de reuniones con IA · Correo conectado a IA y sugerencias | Arma un asistente de consulta con los procedimientos de soporte de DAMASCO, lo prueba contra un set de incidencias reales, y arma su propio flujo de resumen de reuniones y correo con IA. |

### 5.2 Desglose instructivo (cronograma y ruta de aprendizaje)

| Ruta | Temas y subtemas | Tiempo de ejecución | Estrategias de enseñanza (facilitador) | Estrategias de aprendizaje (participante) | Recursos y entornos |
|---|---|---|---|---|---|
| **1 · Desarrollo** (8 h) | Dominio de Claude Code/Cowork/ChatGPT/Codex · Prompting estructurado y de lógica compleja · Agentes eficientes con balance de carga (Mesa A) · Bases de datos con IA → Power BI (Mesa B) | Total 8 h (90' dominio de herramientas · 75' prompting estructurado · 105' Mesa A agentes eficientes y flujos · 90' Mesa B bases de datos con IA · 120' reto integrador por mesa y cierre) | Demostración de flujos en vivo, vibe coding guiado con Claude Code, dos mesas de trabajo en paralelo, feedback con rúbrica técnica | Construye un agente eficiente, con balance de carga, en dupla (Mesa A); consulta bases de datos en lenguaje natural y prepara datos para Power BI (Mesa B); resuelve un reto integrador con datos de prueba | Claude Code, Cowork y ChatGPT/Codex · OpenCode · Datos de prueba de DAMASCO · Power BI del cliente |
| **2 · Soporte** (4 h) | Prompting de diagnóstico e infraestructura · Asistente de conocimiento e incidencias reales · Resumen de reuniones con IA · Correo conectado a IA · Sugerencias y buenas prácticas | Total 4 h (30' encuadre y prompting de infraestructura · 90' asistente de conocimiento e incidencias reales · 60' tema administrativo: resumen de reuniones, correo con IA y sugerencias · 60' aplicación práctica al área y cierre) | Clase interactiva, demostración guiada, casos reales de infraestructura y administración | Práctica guiada; arma un asistente de consulta; resuelve incidencias con lista de cotejo; arma su propio flujo de resumen de reuniones y correo con IA | Cuentas de IA generativa · Procedimientos de soporte de DAMASCO · Set de incidencias reales · Correo y calendario del equipo |

---

## 6. Garantía de calidad y mejora continua

- **Construcción curricular**: cada ruta se adapta a los cuellos de botella reales de su departamento (auditoría, agentes eficientes y costos de tokens en Desarrollo; infraestructura, incidencias y administración en Soporte).
- **Encuesta de satisfacción**: al cierre de cada ruta.
- **Entregables insignia**: un proceso real automatizado por departamento · agente o flujo documentado (Desarrollo) · asistente de consulta de soporte probado contra incidencias reales (Soporte) · Workbooks digitales · Informe de desempeño por área · Certificado de participación INTEZIA.
- **Beneficio del programa formativo**: cada departamento sale con al menos un proceso real automatizado y con flujos replicables de IA, listos para escalar al resto del equipo y para abrir la Fase 2.

---

## 7. Perfil del equipo facilitador

- **Facilitador / Consultor**: Rafael Carreño, con dominio técnico de IA aplicada a desarrollo y operación. Lidera la ruta de Desarrollo (dos mesas) y refuerza el contenido técnico de las demás rutas.
- **Asesora de proyecto**: Isabella Palazzone, enlace directo con DAMASCO de principio a fin.
- **Coordinación**: Equipo INTEZIA Education como punto de contacto durante el programa y los 30 días posteriores.

---

## 8. Roadmap por fases

- **Fase 1 (cotizada ahora)**: las 2 rutas departamentales (este documento).
- **Fase 2 (plus diferenciador)**: (a) agentes departamentales (un agente por área que automatiza su trabajo repetitivo) y (b) agentes integrados a la medida, conectados a las herramientas internas (SAP, Power BI, CRM), con auditoría de uso de IA y acompañamiento para estandarizar esos agentes. Alcance y cotización aparte, sobre lo aprendido en la Fase 1.
