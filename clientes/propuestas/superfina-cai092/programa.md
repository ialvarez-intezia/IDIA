# Programa interno · Superfina · Servicio de Habilidades (CAI-092)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Especificación de la propuesta (Ivana, 09/11/2026) y tabla de distribución de horas.

## 1. Resumen

- **6 entregables en 2 partes del proceso**, **42 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Claude con Estelar y Vilches**: 6 entregables, 42 h.
- Horas por fase: F1 22 h (3 sol.) · F2 20 h (3 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Compras de {cliente_corto} | Claude con Estelar y Vilches | Conexiones, Proceso de compra | 42 | 6 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Conexión (Estelar y Vilches conectados) | Compra (la compra, de punta a punta) |
|---|---|---|
| Compras de {cliente_corto} | 22 h · 3 sol. | 20 h · 3 sol. |

- **Checklist previo**: Compras entrega el cronograma, los parámetros por departamento, los lead times y los formatos.
- **Conexiones**: En línea, con TI: Estelar con lectura y carga controlada, y Vilches con ventas completas.
- **Proyecto y Skills**: En línea: el proyecto del comprador y su manual, las tareas programadas y las Skills.
- **Prueba en sitio**: Presencial: un ciclo real de compra con proveedores, comparado con la carga manual.
- **Adopción en sitio**: Presencial: los compradores ejecutan con acompañamiento; evaluación del proceso y acta.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Conexiones · 3 entregables · 22 h · Claude con Estelar y Vilches · línea A

Para qué (lo que ve el cliente): Dar a Claude las ventas completas y la lectura de Estelar, con el sistema protegido

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CN-1 | Conexiones habilitadas con TI (incluye: Puertos, usuarios y pruebas de conexión; Ruta de escritura acordada con TI y con el proveedor de Estelar) | Seis horas: cuatro de construcción en línea, una de testeo en sitio y una de adopción. TI de Superfina habilita puertos y usuarios y se prueban las conexiones y la ruta de escritura, guiadas por Intezia. Se parte de solo lectura; la escritura se acuerda con TI y con el proveedor de Estelar. Entrega las conexiones probadas. | 4 | 1 | 1 | 6 | F1 |
| CN-2 | Conexión de Claude con Estelar (incluye: Lectura de Estelar adaptada a Superfina; Herramienta de carga de orden de compra, controlada) | Siete horas: cinco de construcción en línea, una de testeo y una de adopción. Se adapta a Superfina la lectura de Estelar que ya existe y se agrega una herramienta controlada de carga de orden de compra; se compara contra la carga manual y se registran los errores. Entrega la conexión funcionando, con cada acción registrada. | 5 | 1 | 1 | 7 | F1 |
| CN-3 | Conexión con Vilches: ventas completas (incluye: Su base de datos, identificada; Consultas de ventas completas y cruce con Estelar) | Nueve horas: siete de construcción en línea, una de testeo y una de adopción. Se identifica la base de datos de Vilches, se arman las consultas de ventas completas y se cruzan con Estelar, que cubre entre el 70 y el 80 % de las ventas. Entrega las ventas completas disponibles para la compra. | 7 | 1 | 1 | 9 | F1 |

### Proceso de compra · 3 entregables · 20 h · Claude con Estelar y Vilches · línea A

Para qué (lo que ve el cliente): Que la compra corra de punta a punta, con una persona que valida

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PC-1 | Proyecto del comprador y manual de proceso (incluye: Cronograma, parámetros por departamento, lead times y reglas; Con las reglas ya detectadas en el grupo) | Siete horas: cuatro de construcción en línea, una de ajustes y dos de entrega de la cuenta y del manual en sitio. Se arma en Claude el proyecto del comprador con su manual: cronograma de compras, parámetros por departamento, lead times y reglas, con las ya detectadas en un proyecto anterior del grupo (múltiplos de bulto, existencia igual a piso más almacén y proveedor habitual igual al de la última compra). Entrega el proyecto configurado y el proceso por escrito. | 4 | 1 | 2 | 7 | F2 |
| PC-2 | Tareas programadas de compra (incluye: Reporte semanal; Sugeridos de compra automáticos) | Cuatro horas: dos de construcción en línea, una de testeo y una de adopción. Se programan el reporte semanal y los sugeridos de compra automáticos, y quedan listos antes de la visita. Entrega las tareas funcionando. | 2 | 1 | 1 | 4 | F2 |
| PC-3 | Skills de compra (incluye: Análisis de existencia a orden de compra; Validación de la carga y envío por el WhatsApp de compras) | Nueve horas: cuatro de construcción en línea, tres de testeo y dos de adopción en sitio. Se construyen las Skills que convierten el análisis de existencia en orden de compra, validan la carga y la envían por el WhatsApp de compras. Se prueban con un ciclo real de compra con un proveedor y con otros proveedores, y los compradores las ejecutan con acompañamiento. Entrega el ciclo completo en uso. | 4 | 3 | 2 | 9 | F2 |

## 4. Fuera de alcance

- Los demás departamentos: cada uno se abre después, con su propia propuesta.
- La conexión de Vilches para otras empresas del grupo: presupuesto aparte.
- La depuración de los datos de Superfina.
- Licencias de Claude: van aparte de esta inversión.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (09/11/2026): propuesta CAI-092 para Superfina, asesora Verónica Rubio, con la especificación completa (qué pide el cliente, flujo, alcance, modelo de entrega, distribución de 42 h, requisitos, riesgos, inversión y hoja de ruta) y la tabla de construcción. Educación y sin alianza: confirmados con Ivana. Sin ficha ni transcripción en el repositorio.
- Horas (de Ivana): 42 h = construcción 26 h en línea (sesiones con TI 4, conexión de Estelar 5, Vilches 7, proyecto del comprador y manual 4, tareas programadas 2, Skills 4), testeo 8 h presencial (conexiones en sitio 1, ciclo real con un proveedor 3, ciclo con otros proveedores 2, comparación contra la carga manual 1, ajustes 1) y adopción 8 h presencial (entrega de la cuenta y del manual 2, ejecución con acompañamiento 4, evaluación y acta 1, plan 30/60/90 y siguiente propuesta 1). El reparto del testeo y la adopción entre las seis piezas es mío: Ivana dio los totales por actividad, no por entregable. Las 16 h presenciales caben en 3 jornadas de 6, 6 y 4 h: dato interno, el deck no cuenta sesiones ni jornadas (§4.23).
- No se nombra a Fasto (decisión de Ivana, 09/11/2026): el deck dice «un proyecto anterior del grupo», «otras empresas del grupo» y «el equipo de TI del grupo». Tampoco se nombra a Polar (proveedor de ejemplo del ciclo real, y cliente de Intezia: «un proveedor») ni a las personas (Alejandro, socio del grupo, patrocinio: «la dirección»).
- VPN: Ivana pidió dejar «VPN estable» como requisito del cliente en el deck (09/11/2026). Va sin explicar el riesgo ni prometer acceso a Claude desde Venezuela (regla de memoria). Riesgo interno: el bloqueo de acceso a Claude no es nuevo pero puede endurecerse el día 12; mitigación: VPN a nivel de red, tareas programadas antes de la visita y sin conexiones nuevas durante ella.
- Supuestos de las 26 h de construcción (internos): Vilches se puede conectar de forma directa y el envío por WhatsApp usa una ruta sencilla. Si no, las alternativas son una exportación programada de Vilches o un archivo de importación para Estelar. Otros riesgos: escrituras erróneas (validación humana y registro de cada acción) y calidad de datos (mínimos desactualizados, códigos duplicados y productos sin proveedor); la depuración de datos está fuera de alcance.
- Licencias de Claude aparte y cuenta con el dominio de la compañía dentro de su Claude Team: requisito del cliente, en el deck. Presupuesto separado del de Fasto (el deck dice «otros proyectos del grupo»). Acompañamiento 30/60/90 como postservicio: seguimiento por defecto de Habilidades.
- Impacto (cuadro de «Lo que se llevan»): enfoque «operación», elegido por Ivana (09/11/2026): errores, tiempo y control, sin hablar de personas ni de nómina.
- Hoja de ruta posterior sin precio (Recepción y Costeo y márgenes, con la meta de bajar el lead time de 24 a 12 horas) y requisitos del cliente: dos páginas «Requisitos y hoja de ruta» después de la ruta (opción respuesta_solicitud). Sin facilidad de pago (omitida): decisión mía por ser lo que se ha pedido en las últimas propuestas; confirmar con Ivana.
- Sin sesiones ni horas de trabajo internas (§4.23): el deck dice «horas con el equipo». Herramienta: Claude (nombrada por Ivana). No se afirma que migren de stack (§4.11).

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero las conexiones, porque la compra depende de la venta completa. Después Claude arma la orden con esas ventas, una persona la valida y se carga en Estelar; compras la envía por WhatsApp.

- **Conectamos**: Estelar y Vilches, con TI y en solo lectura al principio.
- **Construimos**: El proyecto del comprador, las tareas programadas y las Skills, en línea.
- **Testeamos**: Un ciclo real de compra en sitio, comparado con la carga manual.
- **Adoptamos**: Los compradores ejecutan; seguimos a 30, 60 y 90 días.

- En la práctica, **Una persona valida**: Cada carga en Estelar pasa por validación humana y cada acción queda registrada.
- En la práctica, **Solo lectura primero**: La escritura en Estelar se acuerda con TI y con el proveedor del sistema.
- En la práctica, **Solución lista**: El equipo recibe el proyecto armado y el proceso por escrito; se evalúa si carga bien.
- Datos: Se parte de solo lectura y los sistemas no se modifican más allá de la carga controlada. Claude corre en una cuenta con el dominio de la compañía y trabaja con los datos que Superfina autoriza.
- Quién construye: Se construye en línea con TI de Superfina, que habilita puertos y usuarios mientras Intezia guía la conexión; el equipo de TI del grupo participa solo cuando su experiencia aporte.

**Logística:** modalidad: Construcción en línea; testeo y adopción presenciales, en Superfina. · participantes: 2 compradores, el equipo de TI de Superfina y un responsable dedicado al 100 %. · ritmo: Se agenda sin frenar la operación de compra. · arranque: Apenas se apruebe la propuesta; el checklist previo y la reunión de arranque acuerdan el calendario..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Órdenes de hoy; Tiempo de carga; Con la solución; Errores y atrasos; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> Las órdenes de compra salen bien cargadas y a tiempo: Claude las prepara con las ventas reales y una persona las valida antes de cargarlas en Estelar. Menos errores, sin órdenes pendientes y una recepción sin atrasos.

## 9. Próximos pasos (slide 10)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

