# Programa interno · Laboratorios Farma · Servicio de Detección y Habilidades (CAI-032)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Laboratorios Farma (Gestión Humana regional).

## 1. Resumen

- **4 soluciones en 2 áreas (más 2 procesos base)**, **15 h** de sesión, más seguimiento a 30, 60 y 90 días.
- Carril **Microsoft Copilot**: 4 soluciones, 15 h.
- Horas por fase: F1 4 h (1 sol.) · F2 3 h (1 sol.) · F3 8 h (2 sol.).

## 2. Frentes y ruta

| Frente | Carril | Áreas | Semanas | Horas | Soluciones |
|---|---|---|---|---|---|
| A | Microsoft Copilot | Detección de las 6 subáreas, Módulo conjunto de Copilot, Nómina, Selección | S1-S3 | 15 | 4 |

| Frente | Detección (Semana 1) | Nivelación (Semana 2) | Prácticas (Semana 3) |
|---|---|---|---|
| A | 4 h · 1 sol. | 3 h · 1 sol. | 8 h · 2 sol. |

- **Semana 1 · Detección**: 4 h con los líderes: diagnóstico, mapa de licencias y línea base de tiempos.
- **Semana 2 · Nivelación**: 3 h con las 20 personas: el equipo comparte un mismo lenguaje en Copilot.
- **Semana 3 · Prácticas**: Ausentismo y Selección, 4 h cada una: 2 asistentes funcionando con un caso real.
- **30 · 60 · 90 días**: Seguimiento: uso, nuevas construcciones y tiempo recuperado contra la línea base.
- **Etapa 2 · Sin fecha**: Proyectos finales por proceso, cuando Tecnología active Copilot Business.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Detección de las 6 subáreas · 1 solución · 4 h · carril Microsoft Copilot · frente A · proceso base

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DET-1 | Diagnóstico de las 6 subáreas y mapa de licencias de Copilot por proceso | Detección de 4 h con los líderes de las 6 subáreas (Selección, Desarrollo, Nómina, Seguros, Bienestar y Seguridad y Salud Laboral) y el tema transversal de indicadores de gestión: procesos, herramientas (Microsoft 365, SAP, Excel, portal de selección, control de acceso) y permisos. Entrega el diagnóstico real y, proceso por proceso, qué licencia de Copilot necesita cada subárea y por qué (insumo para que Gestión Humana gestione Copilot Business ante la Gerencia Corporativa de TI). Registra la línea base del tiempo actual de Ausentismo y Selección. | - | - | - | 4 | F1 |

### Módulo conjunto de Copilot · 1 solución · 3 h · carril Microsoft Copilot · frente A · proceso base

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| MOD-1 | Sesión conjunta de nivelación para las 20 personas y workbook digital | Módulo conjunto de 3 h para las 20 personas de Gestión Humana: ecosistema Microsoft y Copilot, qué es un asistente y para qué sirve, y Copilot en Outlook, Teams, Excel y Word. Se calibra con los hallazgos de la Detección. | - | - | - | 3 | F2 |

### Nómina · 1 solución · 4 h · carril Microsoft Copilot · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NOM-1 | Asistente de ausentismo en Copilot, probado con un caso real | Práctica de 4 h sobre el cruce diario del reporte de control de acceso contra la macro de Excel, por hora, puerta y día de la semana. Se construye en una versión acotada al límite de 5 solicitudes diarias de Copilot básico; la versión a pleno volumen pasa a la Etapa 2. | - | - | - | 4 | F3 |

### Selección · 1 solución · 4 h · carril Microsoft Copilot · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SEL-1 | Asistente de filtro de currículos en Copilot, probado con un caso real | Práctica de 4 h sobre la revisión de los currículos que llegan por el portal web, uno por uno. Se construye en una versión acotada al límite de 5 solicitudes diarias de Copilot básico; la versión a pleno volumen pasa a la Etapa 2. | - | - | - | 4 | F3 |

## 4. Fuera de alcance

- La conexión directa con SAP o el portal de selección, que requiere permisos de Tecnología.
- La Etapa 2, sin cotizar, cuando Tecnología active Copilot Business.
- Las licencias de Copilot: la Etapa 1 usa la básica que ya tienen.

## 5. Supuestos a confirmar

- Horas de la Etapa 1 (instrucción del usuario, 2026-10-05): Detección 4 h, módulo conjunto 3 h y 4 h para las prácticas. «4 h para prácticas» se interpretó como 4 h CADA una (2 prácticas, 8 h; total 15 h). Si son 4 h en total, cambiar h de NOM-1 y SEL-1 a 2 y regenerar.
- Semanas: 3 semanas con 1 fase por semana (Detección, Nivelación, Prácticas) es una proyección de Intezia a partir del calendario borrador anterior (kick-off, Detección, módulo y 2 prácticas en 3 semanas calendario); confirmar con servicio y con el cliente. El deck ya no lleva fechas ni el plazo del 11 de diciembre del cliente (queda en brief.md).
- La línea base del tiempo actual de Ausentismo y Selección se levanta dentro de las 4 h de la Detección: confirmar con servicio que cabe.
- Copilot básico es la licencia que el cliente ya tiene (indicación del usuario del 2026-10-01); no confirmada con Tecnología.
- Etapa 2 sin cotizar y sin fecha, condicionada a que Tecnología active Copilot Business. Incoherencia heredada sin resolver: la clasificación marca Desarrollo y Bienestar como Copilot básico, pero la propuesta condiciona toda la Etapa 2 a Business; confirmar la intención con el usuario.
- Retorno en modo método: la ficha no trae volúmenes, tiempos ni costo hora del cliente. Pasar a modo 'cifras' cuando se completen (hoja retorno-captura.xlsx).
- «Hacia la semana N» del retorno es aritmética (semanas de construcción + 13): confirmar con el equipo de servicio.
- Fuera de esta versión, por el formato compacto: slide de Impacto con estudio (§4.9 no aplica al compacto), Próximos pasos, Cierre con contacto de la asesora, calendario con fechas, certificado de participación y el detalle de 7 procesos de la slide de licencias (queda en el mapa que entrega la Detección y en programa.md/brief.md).

## 6. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.
Hacia la semana 16: construcción (3 semanas) más 90 días de seguimiento; aritmética a confirmar con servicio.

Pasos del método: Volumen semanal; Tiempo actual por ejecución; Tiempo con el asistente; Horas recuperadas a la semana; Valor en dinero.

