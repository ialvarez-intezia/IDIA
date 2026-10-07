# Programa interno · Clínica Santiago de León · Servicio de Detección (DET-027)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento de la Clínica Santiago de León.

## 1. Resumen

- **7 entregables en 4 áreas (más 1 etapa previa)**, **22 h** de sesión.
- Carril **Detección**: 7 entregables, 22 h.
- Horas por fase: F1 6 h (3 sol.) · F2 8 h (2 sol.) · F3 8 h (2 sol.).

## 2. Frentes y ruta

| Frente | Carril | Áreas | Semanas | Horas | Soluciones |
|---|---|---|---|---|---|
| A | Detección | Fundamentals, Admisión, Finanzas y Facturación, Atención al Paciente, Almacén (Inventario) | S1-S4 | 22 | 7 |

| Frente | Inicio (Semana 1) | Seguro (Semana 2) | Logros (Semana 3) |
|---|---|---|---|
| A | 6 h · 3 sol. | 8 h · 2 sol. | 8 h · 2 sol. |

- **Semana 1 · Nivelación**: Kick-off y Fundamentals de 2 h en 3 grupos, de hasta 25 personas cada uno.
- **Semana 2 · Seguros y presupuestos**: Admisión y Finanzas, 4 h cada una, con el flujo del seguro y el presupuesto como foco.
- **Semana 3 · Pacientes e inventario**: Atención al Paciente y Almacén, 4 h cada una, con un logro inmediato por área.
- **Semana 4 · Reporte Final**: Mapa de Calor, Índice de Madurez, hoja de ruta y caso para la Junta Directiva.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Fundamentals · 3 entregables · 6 h · carril Detección · frente A · etapa previa

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FUN-1 | Primera sesión de nivelación en IA | Fundamentals de 2 h para el primer grupo (máximo 25 personas por sesión). El universo declarado en la ficha es de unas 60 a 70 personas de las 4 áreas, con turnos de guardia de mañana, tarde y noche en Admisión y Almacén; por eso son 3 grupos de 2 h, armados con la clínica por áreas y turnos. Temas: qué es y qué no es la IA, y en qué se diferencia de la automatización; ejemplos aplicados a salud y a sus áreas; cuidado de la información de pacientes; preguntas y expectativas. El kick-off de arranque se hace aparte y no suma horas. | - | - | - | 2 | F1 |
| FUN-2 | Segunda sesión de nivelación en IA | Fundamentals de 2 h para el segundo grupo, con el mismo contenido que el primero. | - | - | - | 2 | F1 |
| FUN-3 | Tercera sesión de nivelación en IA | Fundamentals de 2 h para el tercer grupo, con el mismo contenido que el primero. | - | - | - | 2 | F1 |

### Admisión · 1 entregable · 4 h · carril Detección · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ADM-1 | Inventario de procesos y logro inmediato de Admisión | Sesión de 4 h con 1 o 2 personas del área (jefe o gerente de la unidad). Proceso a levantar: aprobación del seguro para el ingreso de pacientes (cerca de 1 hora, frente a unos 5 minutos del triaje con IA ya instalado, que hoy está aislado de la aprobación del seguro y del presupuesto). Candidato a logro inmediato identificado en la ficha: conectar el resultado del triaje con la aprobación del seguro y el presupuesto. El primer paso aplicable se define en la sesión con lo que la clínica ya tiene; se trabaja en conjunto con Finanzas y Facturación. | - | - | - | 4 | F2 |

### Finanzas y Facturación · 1 entregable · 4 h · carril Detección · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| FIN-1 | Inventario de procesos y logro inmediato de Finanzas y Facturación | Sesión de 4 h con 1 o 2 personas del área. Proceso a levantar: generación de presupuesto y facturación en SAP (cerca de 15 minutos por presupuesto, ítems seleccionados uno por uno, nada predeterminado, dependiente de la persona y propenso a error). Se trabaja en conjunto con Admisión: el presupuesto es el paso siguiente a la aprobación del seguro. | - | - | - | 4 | F2 |

### Atención al Paciente · 1 entregable · 4 h · carril Detección · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ATP-1 | Inventario de procesos y logro inmediato de Atención al Paciente | Sesión de 4 h con 1 o 2 personas del área. Proceso a levantar: la comunicación de precios y de estado al paciente, con las inconsistencias que generan quejas (precio distinto por teléfono que al llegar a la clínica). Se apoya en lo levantado en Admisión y Finanzas. | - | - | - | 4 | F3 |

### Almacén (Inventario) · 1 entregable · 4 h · carril Detección · frente A

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| ALM-1 | Inventario de procesos y logro inmediato de Almacén | Sesión de 4 h con 1 o 2 personas del área. Proceso a levantar: control y reposición de inventario. Hoy el consumo de insumos por patología y por mes se calcula a mano a partir de unos 2.000 pacientes atendidos al mes; no hay reposición automática basada en estadísticas de pacientes. | - | - | - | 4 | F3 |

## 4. Fuera de alcance

- El área de Tecnología: se mapea más adelante, como indicó la clínica.
- Desarrollos e integraciones a medida: son la etapa que sigue a la Detección.
- Licencias de IA: no se incluyen en esta propuesta.

## 5. Supuestos a confirmar

- División Educación inferida: clínica privada, cliente corporativo. Alianza: no (la ficha no menciona ninguna). Confirmar con la asesora.
- Horas por el lineamiento de Detección: Fundamentals de 2 h con un máximo de 25 personas por sesión y 4 h por área en 4 áreas. Con un universo declarado de unas 60 a 70 personas (con turnos de guardia) salen 3 grupos de Fundamentals (6 h) y 16 h de áreas: 22 h en total. El kick-off de arranque va aparte y no suma horas (convención general).
- Los 3 grupos de Fundamentals se arman con la clínica por áreas y turnos, que la ficha no detalla (cuántas personas hay por área ni cómo se reparten las guardias de mañana, tarde y noche). Si los turnos obligan a más grupos, suben las horas: confirmar.
- Calendario propuesto por el sistema, no dictado por la ficha: 4 semanas (S1 kick-off y Fundamentals en 3 grupos, S2 Admisión y Finanzas, S3 Atención al Paciente y Almacén, S4 Reporte Final). Admisión y Finanzas van juntas porque comparten el flujo del seguro y el presupuesto. El Reporte Final va una semana después de la última sesión para dar tiempo al caso para la Junta. Orden y calendario por confirmar con servicio y con la asesora.
- Cada sesión de área es de 4 h con 1 o 2 personas (la ficha dice «1 o 2 por área»: jefes y gerentes de cada unidad, sin nombres). Cada sesión de área se presenta como un entregable; el Mapa de Calor, el Índice de Madurez y el Reporte Final son trabajo del equipo consultor, sin sesión con el cliente ni horas propias: van como entregables transversales.
- Caso para la Junta Directiva: la ficha pide «un caso con presupuesto que se pueda defender ante la Junta». El deck lo lleva como entregable del Reporte Final («con retorno e inversión»). Confirmar con servicio que el Reporte Final estándar incluye una estimación de inversión de la ruta que sigue.
- El deck no cita el modelo HIPAA ni ninguna norma: la ficha dice que la clínica lo usa solo como referencia. Las sesiones se trabajan sin datos que identifican a pacientes (decisión de diseño por la sensibilidad de los datos médicos); confirmar con la clínica.
- Logro inmediato: la ficha identifica conectar el triaje con la aprobación del seguro y el presupuesto. El deck lo presenta como el foco de la semana 2, no como un logro prometido; el primer paso aplicable se define en la sesión.
- Modalidad, fechas y horarios se omiten: la ficha no los trae.
- Retorno en modo método: la ficha trae tiempos declarados (aprobación del seguro cerca de 1 hora, presupuesto cerca de 15 minutos, triaje unos 5 minutos) y un volumen (unos 2.000 pacientes al mes), pero no costo hora ni tiempos con la solución; el Reporte Final los estima. Sin compromiso de resultado.
- Reglas de Detección que se conservan: sin certificado, sin garantía 30-60-90, sin pre-recomendar herramienta de IA (el Reporte Final recomienda), sin dolor dramatizado ni citas textuales, sin nombres de personas del cliente ni su cargo, sin el uso personal de IA del contacto.
- Fuera del deck y del alcance: el proceso 4 de la ficha (seguimiento de proyectos internos en Notion) no pertenece a ninguna de las 4 áreas priorizadas; el área de Tecnología (la ficha la deja para después) y el proyecto paralelo de investigación médica con IA que mencionó el contacto.

## 6. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Volumen; Tiempo actual; Tiempo con la solución; Horas recuperables; Prioridad.

