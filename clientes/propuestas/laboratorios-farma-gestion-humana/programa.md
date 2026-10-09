# Programa interno · Laboratorios Farma · Servicio de Detección y Habilidades (CAI-032)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: PDF de 8 slides de la CAI-032 (horas y piezas) y correcciones de Keiber Quintana del 08/10/2026 (estructura).

## 1. Resumen

- **4 soluciones en 2 subáreas (más 2 pasos previos)**, **20 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Microsoft Copilot**: 4 soluciones, 20 h.
- Horas por fase: F1 4 h (1 sol.) · F2 8 h (1 sol.) · F3 8 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Gestión Humana regional | Microsoft Copilot | Las 6 subáreas, Las 20 personas, Nómina, Selección | 20 | 4 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Detección (con los líderes, antes de construir) | Entrenamiento (todo el equipo junto, en Copilot) | Proyectos finales (uno para Nómina y otro para Selección) |
|---|---|---|---|
| Gestión Humana regional | 4 h · 1 sol. | 8 h · 1 sol. | 8 h · 2 sol. |

- **Detección**: Diagnóstico de cada subárea, mapa de licencias por proceso y línea base de tiempos.
- **Entrenamiento**: Las 20 personas usan Copilot con un mismo lenguaje y criterio.
- **Proyectos finales**: Los 2 asistentes funcionan con casos reales en Nómina y Selección.
- **30 · 60 · 90 días**: Seguimiento: uso, nuevas construcciones y tiempo recuperado contra la línea base.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Las 6 subáreas · 1 solución · 4 h · Microsoft Copilot · línea A · paso previo

Para qué (lo que ve el cliente): Saber cómo trabaja hoy cada subárea y qué licencia de Copilot necesita cada proceso.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DET-1 | Diagnóstico de las 6 subáreas y mapa de licencias de Copilot por proceso (incluye: Cómo trabaja hoy cada subárea: procesos, herramientas y permisos; Qué licencia de Copilot necesita cada proceso, y por qué) | Detección de 4 h con los líderes de las 6 subáreas (Selección, Desarrollo, Nómina, Seguros, Bienestar y Seguridad y Salud Laboral) y el tema transversal de indicadores de gestión: procesos, herramientas (Microsoft 365, SAP, Excel, portal de selección, control de acceso) y permisos. Entrega el diagnóstico real y, proceso por proceso, qué licencia de Copilot necesita cada subárea y por qué (insumo para que Gestión Humana gestione Copilot Business ante la Gerencia Corporativa de TI). Registra la línea base del tiempo actual de Ausentismo y Selección y cura el contenido del entrenamiento. | - | - | - | 4 | F1 |

### Las 20 personas · 1 solución · 8 h · Microsoft Copilot · línea A · paso previo

Para qué (lo que ve el cliente): Usar Copilot para su productividad y efectividad, con un mismo lenguaje y criterio.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ENT-1 | Las 20 personas entrenadas en Copilot, con su workbook digital (incluye: Ecosistema Microsoft y Copilot; Asistentes y agentes de IA: qué son y para qué sirven; Copilot en Outlook y Teams; Copilot en Excel y Word) | Entrenamiento compartido de 8 h para las 20 personas de Gestión Humana: ecosistema Microsoft y Copilot; asistentes y agentes de IA, qué son y para qué sirven; Copilot en Outlook y Teams; Copilot en Excel y Word. Se calibra con los hallazgos de la Detección. Cuántos encuentros y de cuántas horas se acuerda en la reunión de arranque (el PDF anterior proponía 4 de 2 h). | - | - | - | 8 | F2 |

### Nómina · 1 solución · 4 h · Microsoft Copilot · línea A

Para qué (lo que ve el cliente): Cruzar a diario el control de acceso con la macro de Excel, sin hacerlo a mano.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NOM-1 | Asistente de ausentismo, probado con un caso real anonimizado | Proyecto final de 4 h sobre el cruce diario del reporte de control de acceso contra la macro de Excel, por hora, puerta y día de la semana. Se construye en una versión acotada al límite de 5 solicitudes diarias de Copilot básico, con el reporte anonimizado (códigos en lugar de personas); la versión a pleno volumen pasa a la Etapa 2. | - | - | - | 4 | F3 |

### Selección · 1 solución · 4 h · Microsoft Copilot · línea A

Para qué (lo que ve el cliente): Filtrar por perfil los currículos del portal, que hoy se revisan uno a uno.

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SEL-1 | Asistente de filtro de currículos, probado con casos reales anonimizados | Proyecto final de 4 h sobre la revisión de los currículos que llegan por el portal web, uno por uno. Selección los descarga del portal como hoy y los carga en lote a Copilot (sin conexión al portal); se construye dentro del límite de 5 solicitudes diarias de Copilot básico. La versión a pleno volumen pasa a la Etapa 2. | - | - | - | 4 | F3 |

## 4. Fuera de alcance

- La conexión directa de Copilot con SAP o con el portal de selección: requiere permisos de Tecnología.
- Los proyectos de las otras subáreas: pasan a una Etapa 2, sin cotizar, cuando Tecnología active Copilot Business.
- Las licencias de Copilot: el proyecto se hace con la básica que el equipo ya tiene.

## 5. Supuestos a confirmar (antes del método)

- Estructura (Keiber Quintana, 2026-10-08): Detección de las 6 subáreas primero, después un entrenamiento compartido para las 20 personas (Copilot para su productividad y efectividad) y al final solo 2 proyectos finales, Nómina y Selección. Se muestra agrupada por fase en el alcance, la ruta y los entregables (por_fases); «Cómo trabajamos» pasa a la tercera página (metodo_antes_de_ruta).
- Horas tomadas del PDF de 8 slides enviado: Detección 4 h, entrenamiento 8 h y 2 proyectos finales de 4 h; 20 h en total. El número de encuentros del entrenamiento (el PDF decía 4 sesiones de 2 h) y el calendario se acuerdan en la reunión de arranque (sin semanas ni sesiones en la propuesta, v3).
- Keiber mencionó un hilo de correos con lo que se terminó de establecer con el cliente; no se recibió. Si difiere de esta versión (horas, piezas o participantes), corregir datos.json y regenerar.
- Plazo del cliente (minuta): ejecución antes del 11 de diciembre por las vacaciones colectivas, orden de compra en octubre y factura a más tardar la primera semana de noviembre. El deck solo dice que el proyecto cierra antes de las vacaciones colectivas (v3: sin fechas).
- Participantes: 20 personas (la minuta cuenta ~18 en 4 países más Nelson y María Ángel, temporales); por confirmar si participa la jefa de Gestión Humana.
- La línea base del tiempo actual de Ausentismo y Selección se levanta dentro de las 4 h de la Detección: confirmar con servicio que cabe.
- Copilot básico es la licencia que el cliente ya tiene (indicación del usuario del 2026-10-01; en la minuta Claudia debía confirmarlo con Leonardo de Tecnología).
- Etapa 2 sin cotizar y sin fecha, condicionada a que Tecnología active Copilot Business (5 procesos: Desarrollo, Seguros, Bienestar, Seguridad y Salud Laboral e Indicadores de Gestión).
- Retorno en modo método: la ficha no trae volúmenes, tiempos ni valor hora del cliente. Pasar a modo 'cifras' cuando se completen (hoja retorno-captura.xlsx).

## 6. Cómo trabajamos (slide 3)

**Por qué en este orden:** Primero se levanta cómo trabaja cada subárea; después todo el equipo se entrena con un mismo lenguaje en Copilot; al final, los 2 proyectos finales construyen un asistente en Nómina y otro en Selección.

- **Construimos**: Junto a Nómina y Selección, con sus casos reales anonimizados.
- **Probamos**: Con el equipo y dentro del límite de Copilot básico.
- **Adoptamos**: El equipo usa cada asistente en su trabajo diario.
- **Medimos**: El tiempo recuperado contra la línea base, a 30, 60 y 90 días.

- En la práctica, **Límite de 5 solicitudes al día**: Una carga el lote con el perfil buscado; las demás afinan el filtro.
- En la práctica, **Currículos sin conexión al portal**: Selección los descarga como hoy y los carga en lote a Copilot.
- En la práctica, **Ausentismo con reporte anonimizado**: Con códigos en lugar de nombres y documentos.
- Datos: Los 2 proyectos finales se trabajan con casos reales anonimizados: sin nombres, documentos de identidad ni datos de contacto de candidatos o del personal. El equipo prepara los casos antes de empezar.
- Quién construye: Intezia construye cada asistente en vivo, con los equipos de Nómina y Selección, dentro de Copilot y de los archivos que ya manejan.

**Logística:** modalidad: 100 % virtual por Teams. · participantes: 20 personas de Gestión Humana, en 4 países: Venezuela, Ecuador, Perú y Colombia. · ritmo: Según la disponibilidad de cada subárea, sin frenar la nómina semanal de la planta. · arranque: La fecha se acuerda en la reunión de arranque y el proyecto cierra antes de las vacaciones colectivas..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen semanal; Tiempo actual por ejecución; Tiempo con el asistente; Horas recuperadas a la semana; Valor en dinero.

## 8. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056.

