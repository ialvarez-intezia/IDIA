# Programa — Diram · CAP-078

**Auditoría técnica y hoja de ruta de automatización con IA sobre AutoCAD**

- **Cliente**: Diram · ingeniería eléctrica de calidad de energía · proyectos EPC
- **División**: Educación
- **Código**: CAP-078
- **Tipo**: Capacitación In-Company · multi-fase (Fase 1 cotizada · Fase 2 abierta)
- **Modalidad**: Online síncrono o híbrido
- **Audiencia**: Dirección de Proyectos EPC, Coordinación de Ingeniería, los 7 ingenieros del equipo técnico y el área de TI
- **Duración Fase 1**: 2 sesiones de ≈2 h + trabajo consultivo de Intezia

---

## 1. Justificación

Diram pidió «una herramienta que ayude a dibujar». Ya probaron con IA en el navegador y falló: un modelo de lenguaje no genera archivos DWG. **El hecho es correcto y la conclusión no.** El DWG es un formato binario, propietario y cerrado de Autodesk, y ningún modelo puede emitir esos bytes. Pero la vía real nunca fue que la IA escriba el DWG: es que la IA **escriba y opere el código** (Python con la librería ezdxf, AutoLISP, scripts) y que ese código, o el propio AutoCAD, produzca el archivo.

Ese reencuadre, de «IA que dibuja» a «IA que programa la automatización», es el eje del programa.

Antes de diseñar formación alguna hay dos incógnitas que **deciden la mitad del alcance** y que no se pueden responder desde un escritorio:

1. **¿Los archivos DWG del proveedor tienen semántica?** El proveedor «no usa AutoCAD, exporta la información al DWG». Un DWG exportado de otro software suele llegar como geometría explotada (líneas sueltas, sin bloques ni atributos). Si es así, no hay nada que sustituir y el caso de tropicalización se cae.
2. **¿Qué aprueba el área de TI?** No le permitieron a un Director instalar una aplicación de escritorio. Sin aprobación escrita del stack, cualquier formación es papel mojado.

Por eso el programa **empieza por una auditoría técnica**, no por un temario.

---

## 2. Objetivos

### 2.1 Objetivo general

Auditar los archivos y el entorno técnico reales de Diram para determinar, con evidencia, cuáles de sus cuatro casos de uso son automatizables con IA, en qué orden y sobre qué arquitectura aprobada por su área de TI. Con ese análisis se define el plan de formación que deja capacidad instalada en el equipo de ingeniería.

### 2.2 Objetivos específicos

1. Auditar 2 o 3 archivos DWG reales del proveedor y uno en formato Diram para determinar si conservan bloques con atributos o llegan como geometría explotada, y qué porcentaje de entregas llega en PDF.
2. Construir el Mapa de viabilidad de los 4 casos de uso, priorizados por impacto, esfuerzo y riesgo, distinguiendo lo que resuelve la IA de lo que ya resuelven las licencias de AutoCAD que Diram probablemente ya paga.
3. Obtener del área de TI la aprobación escrita de una arquitectura de despliegue de mínima fricción, y definir sobre ella el plan de formación por fases.

---

## 3. Estructura del proyecto

### Fase 1 · Auditoría técnica y arquitectura (cotizada)

| Sesión | Foco | Duración |
|---|---|---|
| 1 | Auditoría de archivos DWG reales | ≈2 h |
| 2 | Arquitectura de despliegue y sesión con TI | ≈2 h |

### Fase 2 · Formación en automatización con IA (plan abierto, no cotizado)

Módulos, herramientas y duración se definen **a partir del Mapa de viabilidad**. Contenido previsto según el levantamiento:

- Fundamentos de instrucción a la IA (cómo se le pide bien a un modelo).
- Creación de skills y agentes personalizados para tareas recurrentes.
- Claude Code operando sobre archivos locales, para preservar el contexto del proyecto.
- Python con ezdxf sobre DXF, y el puente DXF↔DWG con el AutoCAD que Diram ya paga.
- Control de calidad obligatorio y seguridad informática aplicada.

---

## 4. Modelo de capacidad instalada

Con **7 ingenieros eléctricos que no son programadores**, «capacidad instalada» se define explícitamente:

- **1 o 2 campeones internos** (Felipe Rangel es el candidato natural): escriben, versionan y mantienen los scripts.
- **Los demás operan y validan**: reciben reportes y archivos revisados, no escriben código.
- Prometer 7 automatizadores autónomos es prometer algo que no ocurre en ninguna empresa.

---

## 5. Desglose instructivo

### 5.1 Vista general

| # | Sesión | Temas | Entregable de sesión |
|---|---|---|---|
| 1 | Auditoría de archivos DWG reales | Anatomía del entregable Diram · semántica del DWG del proveedor · ruta PDF · capas y bloques | Informe de auditoría de archivos |
| 2 | Arquitectura y sesión con TI | Arquitectura de mínima fricción · gobernanza y datos · qué resuelve AutoCAD sin IA · priorización de los 4 casos | Arquitectura aprobada + Mapa de viabilidad |

### 5.2 Desglose por sesión

#### Sesión 1 · Auditoría de archivos DWG reales

**Objetivo**: determinar con archivos reales si los casos de uso #1 y #3 son técnicamente posibles, antes de comprometer alcance.

| Componente | Contenido |
|---|---|
| **Temas** | Anatomía del entregable en formato Diram (cuerpo, equipos, anotación, cajetín) · Semántica del DWG del proveedor: bloques con atributos o geometría explotada · Estado de las capas: normalizadas o sucias · La ruta PDF: qué porcentaje de entregas llega así |
| **Estrategias de enseñanza** | Auditoría técnica en vivo sobre los archivos del cliente · Conversión DWG a DXF y lectura del resultado · Demostración de lo que la IA sí puede consultar y lo que no · Registro de evidencia por archivo |
| **Estrategias de aprendizaje** | El equipo abre sus propios archivos y observa qué contienen realmente · Felipe explica el flujo del proveedor de principio a fin · El equipo distingue geometría de semántica en sus propios planos |
| **Recursos y entornos** | 2 o 3 archivos DWG reales del proveedor + uno en formato Diram · Guion de auditoría de archivos Intezia · Entorno Python con ezdxf · AutoCAD de Diram para el puente DXF↔DWG · Google Meet o Teams |

#### Sesión 2 · Arquitectura de despliegue y sesión con TI

**Objetivo**: obtener aprobación escrita del stack y cerrar el Mapa de viabilidad con la prioridad real de los 4 casos.

| Componente | Contenido |
|---|---|
| **Temas** | Arquitectura de mínima fricción: una máquina controlada, no 7 instalaciones · Gobernanza y tratamiento de datos: retención, certificaciones y límites declarados · Qué resuelve AutoCAD sin una línea de IA (AutoCAD Electrical, DATAEXTRACTION, DWG Compare) · Priorización conjunta de los 4 casos de uso |
| **Estrategias de enseñanza** | Se llega con la arquitectura dibujada, no se pide permiso · Declaración anticipada de las limitaciones, antes de que TI pregunte · Taller de priorización impacto, esfuerzo y riesgo · Contraste entre licencia existente y desarrollo nuevo |
| **Estrategias de aprendizaje** | TI evalúa una arquitectura concreta y fija sus condiciones por escrito · La dirección decide qué caso arranca primero con la evidencia de la Sesión 1 · El equipo identifica qué parte de su dolor ya cubre su licencia actual |
| **Recursos y entornos** | Arquitectura de despliegue Intezia sobre el entorno Azure que Diram ya usa · Matriz de priorización de los 4 casos · Informe de auditoría de la Sesión 1 · Documentación verificada de certificaciones y retención · Google Meet o Teams |

---

## 6. Entregables

### Destacados del programa

- **Mapa de viabilidad de los 4 casos de uso** (impacto × esfuerzo × riesgo): entregable insignia.
- **Informe de auditoría** de los archivos DWG reales del proveedor.
- **Arquitectura de despliegue** validada por el área de TI de Diram.
- **Plan de formación por fases** para el equipo de ingeniería.

### Institucionales

- Workbook digital del programa.
- Constancia de participación INTEZIA Education.
- Acceso al material curado por el equipo académico.

---

## 7. Lo que este programa NO promete

Lista de control aplicada al deck. Ariel ya se quemó con una promesa incumplida; una segunda cierra la cuenta.

- ❌ Que Claude genera o lee archivos DWG directamente. Requiere convertir a DXF primero.
- ❌ La tropicalización automática («de 2 días a una noche») como resultado de una capacitación.
- ❌ El 4x de proyectos por ingeniero. No hay evidencia que lo sustente.
- ❌ Cifras de ahorro de tiempo o productividad en CAD. No existe estudio que las mida (§4.9).
- ❌ Volumetría lista para licitar. Se entrega un borrador auditado; el ingeniero fija y firma los factores de holgura.
- ❌ Autonomía sin revisión humana en cálculos de ingeniería.
- ❌ Que TI apruebe rápido, o que no haya que tocar a TI.

---

## 8. Acreditación

- Programa registrado en INTEZIA Education como **CAP-078**.
- Cumple con el modelo pedagógico oficial (ABR).
- Material curado y revisado por el equipo académico.
