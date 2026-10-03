# Documento Oficial de Diseño Curricular e Instruccional

**[LOGO INTEZIA — `logos/educacion/NEGRO.png`]**  /  **[LOGO Fasto]**

# Capacitación In-Company
## Calculador de Pedidos Óptimos de Inventario — Fasto

**Código**: CAP-104
**Versión**: Propuesta inicial
**Elaborado por**: Coordinación INTEZIA Education
**Aprobado por**: Coordinación INTEZIA Education
**Fecha de Aprobación**: 2026-08-13

---

## 1. Información general del programa

- **Nombre del programa**: Calculador de Pedidos Óptimos de Inventario — Fasto
- **Empresa**: Fasto
- **Modalidad**: a definir en próxima reunión (Presencial / Online Síncrono / Híbrido)
- **Duración**: 1 sola fase · Etapas 1 a 3, sin horas impuestas, a definir según el diagnóstico
- **Acreditación**: INTEZIA Education

---

## 2. Fundamentación y justificación pedagógica

### 2.1 Planteamiento de la necesidad

Fasto quiere abrir 1 a 2 tiendas nuevas por año, y ese ritmo hace insostenible su proceso actual de pedidos de inventario. El equipo de Compras (3 personas) calcula los pedidos a mano, producto por producto, sin considerar el lead time del proveedor ni el tiempo de recepción, codificación y almacenamiento — no por negligencia, sino porque ese cálculo manual es inviable a la escala de un supermercado. El resultado son quiebres de stock recurrentes (ventas que no se recuperan) y, en el otro extremo, sobrestock cuando los proveedores entregan de más. La data ya existe en el sistema **Estelar** (stock actual, última cantidad pedida, ventas de 7 y 30 días, precio): el problema es el procesamiento, no la fuente. El programa responde con un **piloto enfocado en el equipo de Compras**, sin fases adicionales, para atacar directamente el quiebre de stock y mostrar resultados inmediatos en las finanzas de Fasto.

### 2.2 Enfoque pedagógico (Modelo INTEZIA)

El programa se fundamenta en un modelo de **Aprendizaje Basado en Retos (ABR)** priorizando:

- **Tutoría activa**: el equipo Intezia acompaña al equipo de Compras a lo largo de las 3 etapas, con devolución concreta en cada una.
- **Transferibilidad inmediata**: el calculador se diseña sobre los datos reales de Estelar y las reglas reales de reposición de Fasto, no sobre un temario genérico.
- **Curaduría de contenidos**: la implementación **construye una herramienta funcional mientras enseña a usarla** — no es formación teórica que después haya que aterrizar; sale un entregable operativo (el calculador de pedidos) desde la Etapa 2.

---

## 3. Perfiles académicos

> Como **Capacitación In-Company**, este programa no exige Perfil de ingreso: la audiencia está definida por la empresa (equipo de Compras de Fasto, 3 personas).

### Perfil de egreso

- **Saber (Cognitivo)**: el equipo de Compras entiende por qué el cálculo manual de pedidos no alcanza a cubrir la demanda durante el lead time, y qué variables ordena el calculador (stock, tendencia de ventas, lead time, tiempo de recepción y almacenamiento).
- **Saber hacer (Procedimental)**: el equipo de Compras usa el calculador en su operación diaria para generar órdenes de compra óptimas a partir de los reportes de Estelar, incluyendo su uso como documento formal frente a entregas en exceso de proveedores.
- **Saber ser (Actitudinal)**: Fasto sostiene su ritmo de expansión (1 a 2 tiendas nuevas por año) sin tener que sumar personal de Compras, con un proceso de reposición ordenado y consistente.

---

## 4. Objetivos estratégicos

### 4.1 Objetivo general

Automatizar, para el equipo de Compras de Fasto, el cálculo de pedidos óptimos de inventario a partir de los datos ya disponibles en Estelar, considerando stock actual, tendencias de venta, lead time del proveedor y tiempo de recepción y almacenamiento, para reducir los quiebres de stock y sostener la expansión de nuevas tiendas sin sumar personal de Compras.

### 4.2 Objetivos específicos

1. **Diagnosticar** y mapear con el equipo de Compras las reglas reales de reposición: lead time de cada proveedor y tiempo de recepción, codificación y almacenamiento por categoría.
2. **Construir** el calculador que lee los reportes de Estelar y genera automáticamente la orden de compra óptima, sin sesiones con el equipo.
3. **Implementar** el calculador con el equipo de Compras, entrenando su uso diario, incluido su uso como documento formal frente a entregas en exceso de proveedores.

> Cada específico responde al objetivo general → al perfil de egreso → al planteamiento de la necesidad. Los 3 específicos mapean 1 a 1 con los 3 módulos del programa.

---

## 5. Estructura curricular y diseño instruccional

### 5.1 Estructura modular

| Módulo | Objetivo Instructivo | Temas | Elaboración (Trabajo del cliente) |
|---|---|---|---|
| **I: Diagnóstico** (Etapa 1) | Mapea con el equipo de Compras las reglas reales de reposición: lead time por proveedor y tiempo de recepción, codificación y almacenamiento por categoría, antes de construir nada. | 1.1 Reporte Estelar (stock, última cantidad pedida, ventas 7/30 días, precio)<br>1.2 Lead time por proveedor<br>1.3 Tiempo de recepción, codificación y almacenamiento<br>1.4 Priorización por categoría/producto crítico | El equipo de Compras describe su proceso real de pedidos y valida las variables de cada proveedor en las sesiones de diagnóstico. |
| **II: Construcción** (Etapa 2) | Intezia construye el calculador que lee los datos de Estelar y aplica las reglas mapeadas en el diagnóstico para generar automáticamente la orden de compra óptima. Sin sesiones con el equipo. | 2.1 Lógica de cálculo de pedido óptimo<br>2.2 Formato de la orden de compra<br>2.3 Recomendación de herramienta: Gemini como punto de partida (ya disponible), Claude sugerido para sostener el proceso reglado de punta a punta | Fasto facilita acceso a los reportes de Estelar y valida el formato de la orden de compra propuesto. |
| **III: Implementación** (Etapa 3) | Activa el calculador con el equipo de Compras y entrena su uso diario, incluido el uso de la orden de compra como documento formal frente a entregas en exceso de proveedores. | 3.1 Uso diario del calculador<br>3.2 Lectura e interpretación de la orden de compra generada<br>3.3 Uso de la orden de compra para negociar/rechazar excesos de proveedores | El equipo de Compras participa en las sesiones de activación y prueba el calculador con pedidos reales. |

> Numeración de etapas, fija en todo el documento: **Etapa 1** Diagnóstico · **Etapa 2**
> Construcción · **Etapa 3** Implementación. Una sola fase, sin réplica ni fases adicionales.

### 5.2 Desglose instructivo (cronograma y ruta)

| M | Etapa | Temas y subtemas | Tiempo de ejecución | Qué se hace | Qué se logra | Recursos y entornos |
|---|---|---|---|---|---|---|
| I | Etapa 1 Diagnóstico | Reporte Estelar (stock, última cantidad pedida, ventas 7/30 días, precio); lead time por proveedor; tiempo de recepción, codificación y almacenamiento | Sin horas impuestas, a definir según el diagnóstico | Sesionamos con el equipo de Compras para mapear las reglas reales de reposición por proveedor y categoría | Reglas de reposición mapeadas y priorizadas, listas para construir el calculador | Cuentas para el equipo de Compras (3 personas), acceso a reportes de Estelar, guion de diagnóstico Intezia |
| II | Etapa 2 Construcción | Lógica de cálculo de pedido óptimo, formato de la orden de compra, recomendación de herramienta (Gemini + Claude sugerido) | Sin horas impuestas, a definir según el diagnóstico | Intezia construye el calculador con los hallazgos del diagnóstico, sin sesiones con el equipo | Calculador operando: lee Estelar y genera automáticamente la orden de compra óptima | Datos de Estelar, entorno Google Workspace/Gemini Pro de Fasto, Claude sugerido para el proceso reglado |
| III | Etapa 3 Implementación | Uso diario del calculador, lectura de la orden de compra, uso frente a excesos de proveedores | Sin horas impuestas, a definir según el diagnóstico | Activamos el calculador con el equipo de Compras y entrenamos su uso diario | Equipo de Compras generando pedidos óptimos de forma autónoma, con documento formal frente a proveedores | Calculador construido en la Etapa 2, equipo de Compras de Fasto, modalidad a definir |

> Es un piloto de alcance cerrado: las 3 etapas son la única cotización de esta propuesta. No
> hay fase de réplica ni cotización progresiva — a diferencia de otros pilotos del catálogo,
> Fasto pidió la solución directamente sobre el equipo de Compras.

---

## 6. Garantía de calidad y mejora continua

- **Construcción curricular**: el calculador se diseña sobre las reglas reales de reposición del diagnóstico, no sobre un temario genérico; se valida con el equipo de Compras antes de darlo por terminado.
- **Medición de resultados**: seguimiento de quiebres de stock antes/después de la implementación (indicador de negocio del propio Fasto, no requiere Dashboard EduTrace en este piloto).
- **Entregables**: calculador de pedidos óptimos operando, orden de compra como documento formal, informe de diagnóstico con reglas de reposición mapeadas, workbook digital y constancia de participación INTEZIA.
- **Beneficio del programa formativo**: al finalizar el piloto, Fasto cuenta con un proceso de pedidos automatizado que reduce los quiebres de stock y sostiene la expansión de nuevas tiendas sin sumar personal de Compras.

---

## 7. Perfil del equipo facilitador

- **Formación académica**: certificación experta demostrable en implementación de IA aplicada a negocio, con experiencia en retail y cadena de suministro.
- **Experiencia profesional**: ≥ 2 años trabajando activamente en consultoría de procesos y adopción de IA.
- **Competencias pedagógicas**: facilitación de sesiones de diagnóstico con equipos operativos, traducción de reglas de negocio a lógica de cálculo, dominio de sesiones presenciales y virtuales.
