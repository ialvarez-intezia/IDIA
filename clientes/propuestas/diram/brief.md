# Brief — Diram · Auditoría técnica y hoja de ruta de automatización con IA sobre AutoCAD (CAP-078)

## Datos administrativos

- **Cliente**: Diram · empresa mexicana (capital mexicano) de ingeniería eléctrica especializada en **calidad de energía**. Cadena de valor: consultoría → diseño de producto → proyectos EPC (ingeniería, procura y construcción). Alcance continental: Canadá a Santiago de Chile, presencia en España, obra por abrir en Ecuador.
- **Naturaleza**: Capacitación in-company · proyecto de automatización de ingeniería centrado en una **auditoría técnica** (Fase 1, cotizada) + **formación** en IA aplicada (Fase 2, plan abierto)
- **Slug**: `diram`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación (`CAP-078`)
- **Programa**: Auditoría técnica y hoja de ruta de automatización con IA sobre AutoCAD
- **Eje temático**: automatización de flujos de trabajo de ingeniería eléctrica con IA · la IA escribe y opera el **código** (Python/ezdxf, AutoLISP, scripts) que automatiza el trabajo mecánico alrededor del dibujo CAD
- **Antecedente**: levantamiento técnico de David Prato (reunión del 2026-07-13 con Ariel Berrueto y Felipe Rangel)
- **Fecha del brief**: 2026-07-16
- **Estado**: Borrador · formato canónico multi-fase de 14 slides

## Contacto

- **Asesora comercial Intezia**: **Flavia Martínez** · +58 414-5756615 · fmartinez@intezia.com
- **Consultor / Facilitador**: **David Prato** · dprato@intezia.com · consultor IA · condujo el levantamiento técnico y tiene el contexto completo del caso
- **Cliente**: **Ariel Berrueto** (Director de Proyectos EPC) · **Felipe Rangel** (Coordinador de Ingeniería)
- **Contacto inicial**: María de los Ángeles Ibarren (LinkedIn)

## Por qué este proyecto

El equipo técnico de Diram lo forman **7 ingenieros eléctricos** (no programadores). Ariel lo resumió así: «lo que nos cuesta mucho trabajo para escalar es generar ingenieros que sepan hacer ingenierías». El cuello de botella no es la creatividad de la ingeniería, sino el **volumen de trabajo mecánico y repetitivo** que rodea a cada proyecto.

Diram **nunca parte de cero**: toman el proyecto anterior más parecido y construyen encima («el que más se parece a Peñasquito es NEMAC; agarramos todo lo de NEMAC y sobre eso empezamos a construir»). Es su modo de trabajo declarado y tiene consecuencias técnicas directas (los planos arrastran datos del proyecto anterior).

### El reencuadre que sostiene toda la propuesta

- **Lo que pidió el cliente**: «¿hay alguna herramienta que ayude a dibujar?» (Ariel, LinkedIn).
- **Lo que ya probó y falló**: «Lo hice jugando con Claude… ¿qué tal te fue? Mal. Es que no puede generar DWGs».
- **Por qué falló**: usó claude.ai en el navegador (producto de consumo), porque **TI no le dejó instalar Claude Desktop**. Probó la vía que estructuralmente no podía funcionar.
- **La verdad técnica**: Ariel **tiene razón en el hecho** (un modelo de lenguaje no genera ni lee un DWG: es un formato binario, propietario y cerrado de Autodesk) y **se equivoca en la conclusión**. La vía real nunca fue que la IA escriba el DWG, sino que la IA **escriba el código** (Python con ezdxf, AutoLISP, scripts) y que ese código, o el propio AutoCAD, produzca el archivo.
- **El eje**: de «IA que dibuja» a «IA que programa la automatización».

> **Regla de oro del expediente**: Ariel ya se quemó una vez. Una segunda promesa incumplida cierra la cuenta. La única forma de recuperar autoridad técnica es dar la mala noticia junto con la buena, nosotros primero.

## Diagnóstico (5 puntos)

1. El equipo lo forman 7 ingenieros eléctricos, no programadores: el cuello de botella para escalar es el volumen de trabajo mecánico que rodea a cada proyecto, no la ingeniería en sí.
2. Los entregables de los proveedores llegan con simbología y formato ajenos al estándar Diram, y reconstruirlos a formato propio cuesta cerca de 2 días de ingeniero por plano.
3. La prueba con IA en el navegador falló porque un modelo de lenguaje no genera archivos DWG. El diagnóstico del hecho fue correcto; la conclusión sobre la vía, no.
4. Los errores entre planos (el arreglo general y las cimentaciones quedaron 50 cm desfasados) se detectan a mano y encontrarlos es, en palabras del equipo, «dificilísimo».
5. Diram nunca parte de cero: al construir sobre el proyecto anterior, los planos arrastran datos heredados que hoy nadie audita de forma sistemática.

## Casos de uso — priorización del cliente vs. viabilidad real

Ariel enumeró cuatro casos «del más complejo al más fácil». Su orden de **dificultad** es correcto; su orden de **ataque**, no.

| # | Caso | Viabilidad real | Decisión |
|---|---|---|---|
| 1 | **Tropicalización** del plano del proveedor chino (el que MÁS quiere) | **BAJA** como resultado de una capacitación. Es desarrollo a medida. **Bloqueador previo**: el proveedor «no usa AutoCAD… exporta la información al DWG», y un DWG exportado suele llegar como geometría «tonta» (líneas sueltas, sin bloques ni atributos). Sin semántica no hay nada que sustituir. | Solo tras auditar archivos reales. Proyecto aparte. |
| 2 | **Auditoría cruzada entre planos** (Ariel: «el más fácil») | **MEDIA-ALTA**. Es el quick win y el arranque recomendado: caso de solo lectura, no corrompe entregables, un ingeniero valida cada hallazgo en segundos. Matiz honesto: produce «sospechas», no certezas; la causa raíz es disciplina de versiones/XREF. DWG Compare no lo resuelve (compara revisiones del mismo plano, no planos distintos). | **Punto de arranque.** |
| 3 | **Volumetría / catálogos de conceptos** | **MEDIA**. Viable como *borrador auditado*, nunca como número final. Un unifilar no está a escala (una línea = un circuito, no metros); una trayectoria lleva varios conductores; la longitud 2D subestima la real. DATAEXTRACTION ya cubre parte. El valor de IA está en normalizar capas sucias y mapear al catálogo mexicano, no en «contar». | Segundo en la fila. |
| 4 | **Generar ingeniería completa desde cero** | **NO viable hoy.** El propio Ariel lo dijo: «creo que todavía no estamos ahí». | **Fuera de alcance.** Confirmárselo es una jugada de confianza. |

## Estructura del proyecto

### Fase 1 · Auditoría técnica y arquitectura — lo único cotizado en esta propuesta

- **Modalidad**: online síncrono o híbrido · calendario a consideración del cliente
- **Audiencia**: Ariel Berrueto, Felipe Rangel, el equipo de ingeniería y el área de TI de Diram
- **Contenido**: 2 sesiones de levantamiento
  - **Sesión 1 — Auditoría de archivos DWG reales**: con 2 o 3 archivos del proveedor + uno en formato Diram, se determina si traen bloques con atributos o geometría explotada, si las capas están normalizadas y qué porcentaje llega en PDF. Decide la mitad del alcance y se resuelve en una tarde.
  - **Sesión 2 — Arquitectura y sesión con TI**: se lleva la arquitectura dibujada (no se pide permiso) para obtener aprobación escrita del stack.
- **Entregables**: Mapa de viabilidad de los 4 casos de uso · informe de auditoría de archivos · arquitectura de despliegue aprobada por TI · plan de formación por fases.

### Fase 2 · Formación en automatización con IA — plan abierto, no cotizado

- Módulos, herramientas y duración se definen **a partir del Mapa de viabilidad**. No se fijan en esta propuesta.
- Contenido previsto según el levantamiento: fundamentos de instrucción a la IA, creación de skills y agentes, Claude Code sobre archivos locales, Python con ezdxf, QA obligatorio y seguridad aplicada.
- Se cotiza por separado tras la entrega de la Fase 1.

## Restricción #1 — el TI de Diram (bloqueador existencial)

El mayor riesgo NO es técnico, es de TI y procurement. Sin aprobación escrita del área de TI sobre el stack, toda la capacitación es papel mojado.

- TI descrito como «medio paranoico» tras **dos eventos de ciberseguridad** que les han costado.
- **No le permitieron a Ariel, que es Director, instalar Claude Desktop.**
- El firewall casi le impide entrar a la propia video-llamada de la reunión.
- Son **Microsoft-first** (Teams, ecosistema Microsoft). Ariel aclaró: «somos completamente agnósticos… podríamos evaluar migrar». Es restricción de infraestructura, no capricho.

**La carta a jugar**: Claude está disponible en **Microsoft Foundry** (Disponibilidad General desde el 2026-06-29), sobre Azure, con autenticación Entra ID, control por roles y facturado en la factura de Azure que Diram **ya tiene**. Anthropic está incorporado como subprocesador de Microsoft para Microsoft 365 Copilot.

> **§4.11 — dato de contexto interno, no afirmación de cara al cliente.** El deck NUNCA dice que Diram migra ni migrará de stack. Se enmarca en el entorno Microsoft/Azure que **ya usan** y en herramientas que **se integran** a él.

### Verdades incómodas que se declaran, no se esconden

- No existe *data zone* de México para Claude en Foundry (los datos salen del país; relevante por los acuerdos de confidencialidad con clientes finales como la minera de Peñasquito).
- Claude Code sigue siendo una instalación local con salida a internet, aun apuntando a Foundry.
- Las suscripciones Azure vía partner CSP no están soportadas para Claude en Foundry (verificar cómo compra Azure Diram).
- **Riesgo país de Intezia**: Venezuela no figura en la lista de países soportados por Anthropic. Con el consultor técnico basado allí, hay que resolver la vía de acceso y facturación **antes** de firmar.

## Hallazgo incómodo — parte de esto ya se resuelve sin IA

Honestidad comercial: parte del dolor de Diram se resuelve con licencias que **probablemente ya pagan**. Decirlo nosotros primero es lo que hace creíble todo lo demás.

- **AutoCAD Electrical** (toolset incluido sin costo extra en la suscripción de AutoCAD completo, no en LT): bibliotecas de símbolos IEEE/ANSI, IEC 60617, NFPA/JIC **y GB (el estándar chino del proveedor)**, numeración automática de cables, tagging y generación de reportes. Cubre parte del #1 y del #3.
- **DATAEXTRACTION** (nativo de AutoCAD full): extrae atributos y cuenta objetos a Excel/CSV. Es parte de la volumetría del #3 y existe hace más de una década.
- **DWG Compare** (nativo, incluso en LT): resalta diferencias entre dos revisiones. Punto de partida gratis para el #2.
- Probablemente ya modelan en **ETAP / EasyPower / SKM / PowerFactory**. Varios exportan el unifilar a DXF. Nadie lo preguntó en la reunión.

**Posicionamiento correcto**: la IA es la **capa de arriba** que hace lo que ninguna herramienta de estantería hace (normalizar capas sucias, mapear al catálogo mexicano, cruzar semánticamente N planos). Pero eso solo es posible después de que Diram tenga un estándar destino formalizado, que hoy no tiene.

## Notas técnicas verificadas (sostienen el alcance)

- **ezdxf** (librería Python, licencia MIT, uso comercial libre) lee, crea y modifica **DXF** (el formato abierto y de texto de Autodesk) con capas, bloques, atributos, cotas y layouts. Es el caballo de batalla. **Pero no habla DWG**: hay que convertir.
- El puente **DXF↔DWG** se hace con el propio **AutoCAD que Diram ya paga** (consola headless). Las alternativas «gratis» tienen trampa: ODA File Converter es de uso NO comercial para no-miembros (la membresía comercial arranca en ~USD 3.000/año) y **LibreDWG corrompe datos en silencio** al escribir (en pruebas, «52-1» quedó como «5» y «115 kV» como «1», devolviendo 'éxito'). Para planos de subestación eso es inaceptable.
- **Ningún modelo «ve» el plano completo**: un DXF real pesa decenas de MB y no cabe en su ventana de contexto. La IA escribe **consultas** sobre el plano y recibe resúmenes.
- **No existe un servidor MCP maduro para AutoCAD**. El referente comunitario (puran-water/autocad-mcp, ~390 estrellas, un mantenedor, hardcodeado para AutoCAD LT) se autodeclara no apto para producción. Intezia no puede vender «les instalamos el MCP de AutoCAD».
- **Corrección obligatoria en la propuesta**: en la reunión David dejó dicho que investigaría si «Claude Code sí funciona con DWG» y sugirió que la IA podría leer los DWG directamente. **Esa promesa se corrige explícitamente**: Claude no lee DWG directamente; requiere convertir a DXF primero.

## Especificaciones del programa

- **Duración**: Fase 1 · 2 sesiones de levantamiento (≈2 h cada una) + trabajo consultivo de Intezia
- **Modalidad**: online síncrono o híbrido · cronograma a consideración del cliente
- **Audiencia**: dirección de proyectos, coordinación de ingeniería, los 7 ingenieros y el área de TI
- **Pre-requisitos**: 2 o 3 archivos DWG reales del proveedor + uno en formato Diram · disponibilidad del área de TI
- **Acreditación**: constancia de participación INTEZIA Education

## Modelo de capacidad instalada

Con **7 ingenieros no programadores**, la propuesta elige explícitamente qué significa «capacidad instalada»:

- Formar a **uno o dos campeones internos** (Felipe es el candidato natural) que escriben, versionan y mantienen los scripts.
- Capacitar a los otros para **operar y validar**, no para automatizar de forma autónoma.
- **Prometer «7 automatizadores autónomos» es prometer algo que no ocurre en ninguna empresa.**
- Sostenibilidad: un juego de scripts en manos de 7 no-programadores muere en 3 meses si nadie lo mantiene. El campeón interno es arquitectura, no un detalle.

## Entregables consolidados (Fase 1)

- **Mapa de viabilidad de los 4 casos de uso** (impacto × esfuerzo × riesgo) — entregable insignia
- **Informe de auditoría** de los archivos DWG reales del proveedor
- **Arquitectura de despliegue** validada con el área de TI de Diram
- **Plan de formación por fases** para el equipo de ingeniería
- **Workbook digital** y **constancia de participación INTEZIA** (estándar institucional)

## Equipo

- **Facilitador / Consultor**: **David Prato** · dprato@intezia.com · consultor IA · condujo el levantamiento técnico y la investigación sobre DWG/DXF, ezdxf y el ecosistema CAD para IA.
- **Coordinación / Project Management**: Equipo INTEZIA Education · punto único de contacto durante la Fase 1.
- **Asesora comercial**: **Flavia Martínez** · +58 414-5756615 · fmartinez@intezia.com

## Lo que NO se promete (lista de control aplicada al deck)

- ❌ Que Claude genera o lee archivos DWG. Falso, y Ariel lo verifica en 5 minutos.
- ❌ El caso #1 («de 2 días a una noche») como resultado del curso.
- ❌ El 4x de Ariel («de 2 a 8 proyectos por ingeniero»). No hay evidencia que lo sustente.
- ❌ **Cifras de ahorro de tiempo o % de productividad en CAD.** No existe fuente que mida ganancia de IA en unifilares o layouts. Cualquier número sería inventado (§4.9).
- ❌ Volumetría lista para licitar. Se entrega un borrador auditado; los factores de holgura los fija y firma el ingeniero.
- ❌ Autonomía sin revisión humana en cálculos de ingeniería. En calidad de energía, un error no es un bug: es un accidente que se construye.
- ❌ Que no haya que tocar a TI, o que TI apruebe rápido.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Anticipo del 50 % al firmar el acuerdo.
- Programa registrado como **CAP-078** en INTEZIA Education al cerrar el acuerdo.
- **Solo se cotiza la Fase 1 (auditoría técnica).** La Fase 2 (formación) se cotiza por separado a partir del Mapa de viabilidad.

## Notas de diseño

- Formato canónico **multi-fase de 14 slides** A4 landscape (clonado de `pilotes-perforados`).
- Slide `08 · Impacto` con datos de **estudios reales sobre generación de código**, que es literalmente lo que la propuesta enseña (la IA escribe scripts). **No se extrapola a CAD.** Incluye deliberadamente el estudio METR (resultado negativo) como argumento de por qué se capacita con método.
- Slide `07 · Mapa de viabilidad`: los 4 casos de uso priorizados por viabilidad real, con las herramientas nativas de AutoCAD declaradas en las filas donde aplican (honestidad comercial del §9 del levantamiento).
- Equipo named: David Prato (DP) + Coordinación (CO) en slide 9 · Flavia Martínez en el cierre.
- Defaults institucionales en AcroForms · `[CÓDIGO]` → CAP-078.
- Sin guion largo (§4.13) · acrónimos expandidos (§4.12) · sin afirmar migración de stack (§4.11).
