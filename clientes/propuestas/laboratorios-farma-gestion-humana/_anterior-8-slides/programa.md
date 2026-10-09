# Programa interno · Laboratorios Farma · Servicio de Detección y Habilidades (CAI-032)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de Laboratorios Farma (Gestión Humana regional).

## 1. Resumen

- **7 soluciones en 3 áreas (más 1 etapa previa)**, **20 h** de sesión, más seguimiento a 30, 60 y 90 días.
- Herramienta **Microsoft Copilot**: 7 soluciones, 20 h.
- Horas por fase: F1 4 h (1 sol.) · F2 8 h (4 sol.) · F3 8 h (2 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Semanas | Horas | Soluciones |
|---|---|---|---|---|---|
| Gestión Humana regional | Microsoft Copilot | Detección de las 6 subáreas, Entrenamiento para todo el equipo, Nómina, Selección | 1 a 4 | 20 | 7 |

| Línea de trabajo | Detección (Semana 1) | Equipo (Semanas 2 y 3) | Casos (Semana 4) |
|---|---|---|---|
| Gestión Humana regional | 4 h · 1 sol. | 8 h · 4 sol. | 8 h · 2 sol. |

- **Semana 1 · Detección**: 4 h con los líderes: diagnóstico, mapa de licencias y línea base de tiempos.
- **Semanas 2 y 3 · Equipo**: 8 h con las 20 personas, 2 sesiones por semana: todos con un mismo lenguaje en Copilot.
- **Semana 4 · Prácticas**: Ausentismo y Selección, 4 h cada una: 2 asistentes funcionando con casos reales.
- **30 · 60 · 90 días**: Seguimiento: uso, nuevas construcciones y tiempo recuperado contra la línea base.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Detección de las 6 subáreas · 1 solución · 4 h · Microsoft Copilot · línea A · etapa previa

Para qué (lo que ve el cliente): Saber cómo trabaja cada subárea y qué licencia de Copilot necesita cada proceso

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| DET-1 | Diagnóstico de las 6 subáreas y mapa de licencias de Copilot por proceso | Detección de 4 h con los líderes de las 6 subáreas (Selección, Desarrollo, Nómina, Seguros, Bienestar y Seguridad y Salud Laboral) y el tema transversal de indicadores de gestión: procesos, herramientas (Microsoft 365, SAP, Excel, portal de selección, control de acceso) y permisos. Entrega el diagnóstico real y, proceso por proceso, qué licencia de Copilot necesita cada subárea y por qué (insumo para que Gestión Humana gestione Copilot Business ante la Gerencia Corporativa de TI). Registra la línea base del tiempo actual de Ausentismo y Selección. | - | - | - | 4 | F1 |

### Entrenamiento para todo el equipo · 4 soluciones · 8 h · Microsoft Copilot · línea A

Para qué (lo que ve el cliente): Que las 20 personas usen Copilot con un mismo lenguaje y criterio

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| MOD-1 | Sesión 1: ecosistema Microsoft y Copilot | Sesión de 2 h para las 20 personas de Gestión Humana: el ecosistema Microsoft (Outlook, Teams, Excel y Word), qué es Copilot, qué puede hacer y cuáles son los límites de la licencia básica (5 solicitudes diarias). Se calibra con los hallazgos de la Detección. | - | - | - | 2 | F2 |
| MOD-2 | Sesión 2: asistentes y agentes de IA, qué son y para qué sirven | Sesión de 2 h: qué es un asistente y qué es un agente de IA, para qué sirve cada uno y cómo se usan en el trabajo de Gestión Humana. Prepara a todo el equipo para las prácticas de Nómina y Selección. | - | - | - | 2 | F2 |
| MOD-3 | Sesión 3: Copilot en Outlook y Teams | Sesión de 2 h: uso de Copilot en Outlook y en Teams con casos del trabajo diario de Gestión Humana. | - | - | - | 2 | F2 |
| MOD-4 | Sesión 4: Copilot en Excel y Word | Sesión de 2 h: uso de Copilot en Excel y en Word con casos de Gestión Humana (reportes, indicadores y documentos). Cierra el entrenamiento y entrega el workbook digital del módulo. | - | - | - | 2 | F2 |

### Nómina · 1 solución · 4 h · Microsoft Copilot · línea A

Para qué (lo que ve el cliente): Cruzar a diario el control de acceso con la macro de Excel, sin hacerlo a mano

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| NOM-1 | Asistente de ausentismo, probado con un caso real anonimizado | Práctica de 4 h sobre el cruce diario del reporte de control de acceso contra la macro de Excel, por hora, puerta y día de la semana. Se trabaja con un caso real anonimizado: el equipo de Nómina prepara el reporte sin nombres ni documentos de identidad (códigos en lugar de personas), de modo que Copilot no recibe datos que identifiquen a nadie. Se construye en una versión acotada al límite de 5 solicitudes diarias de Copilot básico; la versión a pleno volumen pasa a la Etapa 2. | - | - | - | 4 | F3 |

### Selección · 1 solución · 4 h · Microsoft Copilot · línea A

Para qué (lo que ve el cliente): Filtrar por perfil los currículos del portal, que hoy se revisan uno a uno

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| SEL-1 | Asistente de filtro de currículos, probado con casos reales anonimizados | Práctica de 4 h sobre la revisión de los currículos que llegan por el portal web, uno por uno. Copilot no tiene conexión con el portal: Selección descarga los currículos como lo hace hoy, los anonimiza (sin nombre, documento ni datos de contacto) y los carga en lote a Copilot. Con el límite de 5 solicitudes diarias, una solicitud carga el lote y aplica el perfil buscado y las demás se reservan para afinar el filtro y redactar. Cuántos archivos admite cada solicitud se confirma en la Detección con Tecnología. La versión a pleno volumen pasa a la Etapa 2. | - | - | - | 4 | F3 |

## 4. Fuera de alcance

- La conexión directa de Copilot con SAP o con el portal de selección: requiere permisos de Tecnología.
- La Etapa 2, sin cotizar: depende de que Tecnología active Copilot Business.
- Las licencias de Copilot: la Etapa 1 se hace con la básica que el equipo ya tiene.

## 5. Supuestos a confirmar (antes del método)

- Horas de la Etapa 1 (instrucción del usuario, 2026-10-08): Detección 4 h, entrenamiento para todo el equipo 8 h (4 sesiones de 2 h, antes un módulo de 3 h) y prácticas 4 h cada una: 20 h en total (antes 15 h). El valor del proyecto debe recalcularse con ventas. «4 h para prácticas» (2026-10-05) sigue interpretado como 4 h CADA una; si son 4 h en total, cambiar h de NOM-1 y SEL-1 a 2 y regenerar (16 h).
- Semanas: 4 semanas (Detección en la 1, entrenamiento en la 2 y la 3 con 2 sesiones por semana, prácticas en la 4) es una proyección de Intezia; confirmar con servicio y con el cliente. Las 4 sesiones del entrenamiento (ecosistema Microsoft y Copilot · asistentes y agentes · Outlook y Teams · Excel y Word) y sus nombres son propuesta del sistema a partir del temario que pidió el cliente.
- Logística (instrucción del usuario, 2026-10-08): 100 % virtual por Teams, 20 personas en 4 países (Venezuela, Ecuador, Perú y Colombia, según la Ficha) y ejecución antes del 11 de diciembre. El plazo es una fecha calendario: el generador avisa y es deliberado; la ruta sigue en semanas.
- Datos sensibles: las prácticas de Selección y Nómina se trabajan con casos reales anonimizados, preparados por el equipo del cliente antes de cada práctica (sin nombres, documentos de identidad ni datos de contacto; códigos en lugar de personas). Quién anonimiza y con qué criterio lo confirma servicio con Tecnología en la Detección.
- Currículos y límite de 5 solicitudes (decisión del usuario, 2026-10-08): carga manual en lote, sin conexión con el portal; una solicitud carga el lote y aplica el perfil y las demás afinan. NO verificado: cuántos archivos o cuántos currículos admite una solicitud de Copilot básico; el deck dice que se define en la Detección. Confirmarlo con Tecnología antes de comprometer un volumen.
- Copilot dentro de Outlook, Teams, Excel y Word (temario pedido por el cliente) frente a la licencia básica de la Etapa 1: confirmar con Tecnología qué parte de Copilot en esas aplicaciones cubre la licencia que ya tienen, porque el deck dice que la Etapa 1 se hace con la básica.
- Copilot básico es la licencia que el cliente ya tiene (indicación del usuario del 2026-10-01); no confirmada con Tecnología.
- Etapa 2 sin cotizar y sin fecha, condicionada a que Tecnología active Copilot Business. Los 5 procesos nombrados en la ruta son Desarrollo, Seguros, Bienestar, Seguridad y Salud Laboral e Indicadores de Gestión (instrucción del 2026-10-08); Selección y Nómina siguen en la Etapa 2 solo como versión a pleno volumen de sus prácticas. Incoherencia heredada sin resolver: la clasificación marca Desarrollo y Bienestar como Copilot básico, pero la propuesta condiciona toda la Etapa 2 a Business; confirmar la intención con el usuario.
- Sin facilidad de pago (instrucción del usuario, 2026-10-08, «no la agregues»): la slide se omite con omitir: ["pago"]. Ventas comunica el plan de pago por otro medio. El generador avisa que Ventas la pide en toda propuesta.
- Asesora (slide de próximos pasos): María Iribarren, con el teléfono y el correo que figuran en sus otras propuestas; el cargo «Asesora comercial» es supuesto. Confirmar con ella antes de enviar.
- La línea base del tiempo actual de Ausentismo y Selección se levanta dentro de las 4 h de la Detección: confirmar con servicio que cabe.
- Retorno en modo método: la ficha no trae volúmenes, tiempos ni valor hora del cliente. Pasar a modo 'cifras' cuando se completen (hoja retorno-captura.xlsx). Sin casos ya logrados con el cliente y sin contratación evitada: no hay fuente documentada.
- «Hacia la semana N» del retorno es aritmética (semanas de construcción + 13): confirmar con el equipo de servicio.
- Lenguaje de inversión (instrucción del usuario, 2026-10-08): el proyecto se cobra por proyecto, no por hora. La plantilla v2 ya titula la slide «Inversión del proyecto» y verifica que el deck diga «valor», no «precio» ni «costo». Los nombres internos de los campos del PDF (PrecioBase, PrecioTotal) y sus descripciones emergentes no se tocaron: son del sistema.
- Migración a la plantilla v2 (2026-10-08): versión 1 a 2 según la spec §13. «Módulo conjunto» deja de ser etapa previa y pasa a área con 4 entregables; «Detección» se muestra como «etapa previa» (vocabulario). Fuera de esta versión, por el formato compacto: slide de Impacto con estudio (§4.9 no aplica), Cierre, calendario con fechas, certificado de participación y el detalle de 7 procesos de la slide de licencias (queda en el mapa que entrega la Detección y en programa.md/brief.md).
- Cotización por partes (instrucción del usuario, 2026-10-08): la hoja de inversión lleva 2 cajas de valor a la izquierda, «Detección» y «Habilidades», sin más texto (el usuario pidió «solo 2 cuadros, uno que diga detección y otro habilidades, más nada»), y la suma automática en la caja de la derecha, con Descuento y TOTAL como antes. Habilidades agrupa el entrenamiento del equipo (8 h) y los 2 asistentes (8 h): 16 h; Detección son 4 h. Las tarjetas de licenciamiento salieron de esta slide (comparten zona con las partes): su contenido pasó a Notas (Copilot básico en la Etapa 1, Copilot Business a cargo de Tecnología en la Etapa 2) y el mapa de licencias sigue en el entregable de la Detección.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero se levanta cómo trabaja cada subárea; después todo el equipo se entrena con un mismo lenguaje en Copilot; al final se construyen los 2 asistentes con casos reales.

- **Construimos**: Junto a Nómina y Selección, con sus casos reales anonimizados.
- **Probamos**: Con el equipo y dentro del límite de Copilot básico.
- **Adoptamos**: El equipo usa cada asistente en su trabajo diario.
- **Medimos**: El tiempo recuperado contra la línea base, a 30, 60 y 90 días.

- En la práctica, **Límite de 5 solicitudes al día**: Copilot básico admite 5 solicitudes diarias: una carga el lote y aplica el perfil buscado, y las demás se reservan para afinar el filtro.
- En la práctica, **Currículos sin conexión al portal**: Selección los descarga del portal, como lo hace hoy, y los carga en lote a Copilot. Cuántos por lote se define en la Detección.
- En la práctica, **Ausentismo con reporte anonimizado**: Nómina practica con el reporte de control de acceso sin nombres ni documentos, con códigos en lugar de personas.
- Datos: Las dos prácticas se trabajan con casos reales anonimizados: sin nombres, documentos de identidad ni datos de contacto de candidatos o del personal. El equipo prepara los casos antes de cada práctica.
- Quién construye: Intezia construye cada asistente en vivo, con los equipos de Nómina y Selección, dentro de Copilot y de los archivos que ya manejan.

**Logística:** modalidad: 100 % virtual por Teams. · participantes: 20 personas de Gestión Humana, en 4 países: Venezuela, Ecuador, Perú y Colombia. · arranque: La fecha se acuerda con Laboratorios Farma y la ejecución termina antes del 11 de diciembre..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.
Hacia la semana 17: construcción (4 semanas) más 90 días de seguimiento; aritmética a confirmar con servicio.

Pasos del método: Volumen semanal; Tiempo actual por ejecución; Tiempo con el asistente; Horas recuperadas a la semana; Valor en dinero.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056.

