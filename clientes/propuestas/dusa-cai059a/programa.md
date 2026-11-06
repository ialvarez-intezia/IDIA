# Programa interno · DUSA · Servicio de Habilidades (CAI-059A)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Estructura y horas de la etapa (04/11/2026) y fichas de levantamiento de septiembre de 2026.

## 1. Resumen

- **5 soluciones en 4 áreas**, **42 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Microsoft 365 Copilot**: 5 soluciones, 42 h.
- Horas por fase: F0 0 h (0 sol.) · F1 38 h (3 sol.) · F2 4 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Los cinco procesos de {cliente_corto} | Microsoft 365 Copilot | Contabilidad, Tesorería, Nómina, Cuentas por Cobrar | 42 | 5 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Construcción (construcción y testeo de las tres soluciones) | Adopción (adopción e instalación de los agentes) |
|---|---|---|
| Los cinco procesos de {cliente_corto} | 38 h · 3 sol. | 4 h · 2 sol. |

- **Línea base**: Preparación en línea (2 h): los cinco procesos cronometrados antes de tocarlos.
- **Soluciones construidas**: Depurador, clasificador y archivo de pago, probados con casos reales.
- **Agentes instalados**: Validador de cobros y estados financieros, con cuenta activa.
- **Antes y después**: Horas liberadas medidas por proceso.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Contabilidad · 2 soluciones · 11 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Reportes limpios y estados financieros en uso para todo el equipo

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CP-2 | Depurador de reportes de JD Edwards, por formato | Depurador de reportes exportados de JD Edwards: quita columnas y filas vacías, espacios y dispersión, con una plantilla por formato. | 4 | 2 | 3 | 9 | F1 |
| CP-3 | Agente de estados financieros, instalado | Instalación del agente de estados financieros, ya construido, con cuenta activa y uso verificado. | - | - | - | 2 | F2 |

### Tesorería · 1 solución · 14 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Solicitudes de pago ordenadas en un resumen diario

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| TS-1 | Clasificador de la bandeja del tesorero, con resumen diario | Clasificador de la bandeja del tesorero: separa las solicitudes de pago y entrega un resumen diario. | 7 | 4 | 3 | 14 | F1 |

### Nómina · 1 solución · 15 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Archivo de pago listo desde el reporte, con cuadro y correos

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NM-3 | Archivo de pago desde el reporte 337, con cuadro y correos | Archivo de pago desde el reporte 337, con cuadro resumen y correos a Tesorería. | 8 | 4 | 3 | 15 | F1 |

### Cuentas por Cobrar · 1 solución · 2 h · Microsoft 365 Copilot · línea A

Para qué (lo que ve el cliente): Cobros validados con el agente ya construido

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CC-1 | Validador de cobros, instalado | Instalación del validador de cobros, ya construido, con cuenta activa y uso verificado. | - | - | - | 2 | F2 |

## 4. Fuera de alcance

- El resto de las 44 soluciones del plan.
- Los procesos anuales del plan financiero: plan y presupuesto de nómina, integración del plan de nómina y plan de ventas.
- Llevar los estados financieros al cierre completo de 10 estados.
- Los otros escenarios de Cuentas por Cobrar.

## 5. Supuestos a confirmar (antes del método)

- Código: Ivana pidió «mismo código con sufijo A» sin decir cuál; se tomó CAI-059 (última propuesta de DUSA, con tres opciones). Si era CAI-035, cambiar `cliente.codigo` y el slug.
- El «piloto» y su opción 3 no están en el repositorio: la estructura y las horas son las enviadas a Ivana el 04/11/2026.
- Fecha: «antes del 11 de noviembre» va en la portada y en el retorno por pedido expreso (excepción a §4.23; en `frases_ok`).
- Las fichas de septiembre se citan dentro del texto de la portada, sin línea de fuente (regla del 30/10/2026).
- Todo en Copilot Premium (6 cuentas aportadas por DUSA); la CAI-059 usaba Claude Team para Nómina.
- Sin facilidad de pago: no se pidió; la propuesta económica es una hoja con 42 h y licencias aparte.
- Horas: 42 en total = construcción 19, testeo 10, adopción 9 e instalación 4; por etapa, preparación en línea 2 h, construcción presencial 27 h y adopción e instalación presencial 13 h. Ivana las pidió visibles (excepción a la regla del 27/10/2026): se usa `sin_horas_trabajo` con las horas escritas a mano. Lectura propia: las 29 h de construcción y testeo (19 + 10) se dividen en 2 h de preparación en línea y 27 h presenciales; es la única que cuadra con el total.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero la fase 1 (construcción y testeo de las tres soluciones); al final la fase 2 (adopción e instalación de los agentes).

- **Construimos**: Junto a quien ejecuta el proceso, con sus casos reales.
- **Probamos**: Con ese equipo y con el equipo de tecnología de DUSA.
- **Adoptamos**: El equipo la usa en su trabajo diario.
- **Medimos**: El retorno en tiempo y las oportunidades de optimización para la empresa.

- En la práctica, **Cuentas de Copilot**: DUSA aporta 6 cuentas de Copilot Premium.
- En la práctica, **Un ejecutor por proceso**: Con hasta 4 horas por día para trabajar su solución.
- En la práctica, **Insumos y formato**: Muestras de cada proceso y el formato del resumen de nómina acordado con Tesorería.
- Datos: Trabajamos con muestras reales de cada proceso, sin sacar información financiera ni datos de nómina de DUSA. Las soluciones usan solo las cuentas autorizadas por tecnología, y sus sistemas no se modifican.

**Logística:** modalidad: Preparación en línea; construcción, adopción e instalación presenciales. · participantes: Un ejecutor por proceso, con hasta 4 h por día. · ritmo: Según la disponibilidad de cada área, sin frenar su operación diaria. · arranque: La fecha la fija DUSA al confirmar la propuesta..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Línea base cronometrada; Medición después; Cinco indicadores; Informe por proceso.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: María Iribarren, Directora comercial · miribarren@intezia.com · +58 414 0570056.

