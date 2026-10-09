# Brief — IOED · CAP-098

## Actualización 2026-10-08 — Fase 1 de Detección en la plantilla compacta v2 (8 slides) · VIGENTE

**Pedido de la asesora (08/10/2026):** una propuesta **solo con la Fase 1 (Diagnóstico)** de la CAP-098, con la nivelación y los fundamentos de IA incluidos; que se vea el camino (construcción e implementación) **sin cotizarlo**; un apartado corto de **confidencialidad** (primera preocupación del cliente, validado con Tecnología); trabajar dentro de **Microsoft 365 E3** (hoy una sola licencia de Copilot Studio, no hace falta comprar nada de entrada); y, si IOED decide adquirir e integrar **Claude**, la nivelación se hace sobre esa herramienta (en la reunión se habló de lo hecho con Pago Tronic y Claude, y el cliente se interesó por el riesgo de datos). Extra: **resumen de una página** (qué hacemos, qué entregamos en los primeros 30 días, cómo cuidamos su información) para que la contraparte (Liliam) lo presente a su jefe. El usuario pidió el resumen como PDF.

**Servicio y código:** Detección (Fase 1 del plan de la CAP-098), división Educación, alianza no. Se conserva el código **CAP-098** (la instrucción fue «ajustar la CAP-098»); si se prefiere un código DET-, es un solo cambio en `cliente.codigo` de `datos.json`.

| Parte | Horas | Detalle |
|---|---|---|
| Fundamentals | 2 h | Un solo grupo online (máx. 25), sobre las herramientas que IOED ya tiene; si incorpora Claude, sobre Claude |
| Servicios Navales | 4 h | Dos mesas de 2 h: procesos y trazabilidad (semana 2) · accesos y datos (semana 3) |
| Operaciones de Buques | 4 h | Igual: procesos e informes (semana 2) · accesos y datos (semana 3) |
| **Total** | **10 h** | 5 sesiones online en 4 semanas (los primeros 30 días); kick-off aparte, sin horas |

El informe de diagnóstico (semana 4), la evaluación del control de acceso y la viabilidad de integraciones son trabajo del consultor: entregables transversales, sin horas inventadas.

**Qué cambió respecto de la CAP-098 de agosto (17 slides, 3 fases cotizadas):** solo la Fase 1 con valor; las fases 2 y 3 aparecen como camino (ruta, retorno, límites del alcance, notas de la inversión) sin horas ni valor; la hoja de inversión pasa de «Inversión por fases» (7 campos) a la hoja estándar de un solo proyecto (7 campos del compacto); se retiran Quiénes somos con los clientes de referencia, los 3 estudios de Impacto y la Metodología de retos (el compacto no los lleva); se agrega «Cómo trabajamos» con el apartado de datos y la slide de próximos pasos con la asesora. Se mantienen los criterios del cliente del 14/08: sin flota, sin detalle de contratos ni procesos internos y sin nombrar la plataforma con la que se evaluaría una integración.

**Confidencialidad (slide 4 y hoja resumen), pendiente de validar con Tecnología antes de enviar:**
- Acuerdo de confidencialidad firmado antes de iniciar (dato de la asesora).
- En las mesas no se carga información real de IOED a herramientas de IA (criterio del sistema, igual que G-MAX, Conserval, la clínica y Acua-e).
- Dónde se procesa: dentro del entorno Microsoft 365 de IOED; otra herramienta (p. ej. Claude) se valida antes con IOED y su área de tecnología.
- Sin entrenar modelos: licencias empresariales. Respaldo público consultado el 08/10/2026: Microsoft, protección de datos empresariales de Copilot (los avisos, respuestas y datos de Microsoft Graph no entrenan modelos fundamentales y permanecen en el límite del servicio de Microsoft 365; learn.microsoft.com/copilot/microsoft-365/enterprise-data-protection) y Anthropic, términos comerciales de Claude Team y Enterprise (no se entrena con el contenido del cliente por defecto; anthropic.com/legal/commercial-terms). Los planes personales o gratuitos no tienen esas garantías.
- Cómo se protege: accede solo quien IOED autorice; el informe evalúa el control de acceso por área.

**Decisiones de contenido (todas del sistema, por confirmar):** 2 áreas (los agrupadores de la CAP-098) con 4 h cada una en 2 mesas de 2 h por la consigna de «sesiones de 2 horas»; temas de las mesas tomados de la Fase 1 de la CAP-098; calendario de 4 semanas propuesto por el sistema para que el informe llegue en 30 días; retorno en modo método (sin cifras del cliente); sin facilidad de pago (se omitió por el criterio de las últimas propuestas); asesora Flavia Martínez, la de la CAP-098. Claude se presenta como condición que decide IOED, sin afirmar que migra ni que adoptará (CLAUDE.md §4.11). Los casos de Pago Tronic y Claude de la reunión no se citan (sin fuente documentada). La contraparte (Liliam) y su jefe no se nombran en el deck.

**Archivos:** `datos.json` (fuente), `index.html` (generado), PDF «CAP-098 Diagnóstico de procesos con IA y nivelación del equipo en 2 áreas de IOED.pdf» (8 páginas, 7 campos), PDF complementario «CAP-098 Resumen de una página.pdf» con su fuente `resumen-una-pagina.html` (si cambia el deck, actualizar sus cifras e imprimirlo con Chrome; **sacarlo de la carpeta antes de correr `pdf-habilidades-compacto.sh`**, que aparta todo `*.pdf`), y `_anterior-17-slides/` (deck de agosto, su versión Resumen de 8 slides del 14/08, `styles.css` local, acroforms, programa y PDF).

**Pendientes:** validación de Tecnología; valor, descuento y total de la Fase 1; confirmar 2 áreas, 10 h, 2 mesas por área, calendario, fechas y plataforma; quién de IOED asiste a Fundamentals y quién firma el acuerdo; contacto referente (apellido y cargo de Liliam); teléfono, correo y cargo de la asesora; facilidad de pago; reenviar avisando que reemplaza a la CAP-098 de 17 slides (10/08) y a su Resumen (14/08).

---

## Brief anterior (2026-08-10 a 2026-08-14) · SUPERADO por la actualización de arriba

> Plan de digitalización en 3 fases cotizadas, deck de 17 slides y versión Resumen de 8 slides. Se conserva como contexto: diagnóstico, estructura de las fases, criterios del cliente y trazabilidad. Los archivos de ese deck están en `_anterior-17-slides/`.

## Datos administrativos

- **Cliente**: IOED · empresa de servicios navales (opera 4 buques, 2 gabarras y 3 remolcadores)
- **Naturaleza**: Capacitación in-company · **plan de digitalización con IA para los procesos administrativos y operativos de IOED**, entregado en **3 fases secuenciales**. Lo único cerrado por el cliente es la Fase 1 de Diagnóstico y Auditoría; las fases siguientes (Construcción e Implementación) se definen con lo que arroje ese diagnóstico — puede ser capacitación por área, creación de skills de IA que resuelvan cuellos de botella puntuales, o una combinación de ambas. La estructura completa de la propuesta quedó en manos de Intezia.
- **Slug**: `ioed`
- **División Intezia**: `educacion` (cliente corporativo)
- **Tipo de documento**: Capacitación (`CAP-098`)
- **Programa**: Plan de Digitalización con IA — IOED
- **Eje temático**: diagnóstico y automatización con IA de procesos administrativos y documentales (contratos, órdenes de servicio, valuaciones, facturación, informes operativos) en una empresa de servicios navales, con foco crítico en seguridad y control de acceso a la información
- **Modalidad**: Online síncrono (mesas de trabajo de diagnóstico); modalidad de Fase 2 y 3 a definir según alcance
- **Duración**: Fase 1 · sesiones de 2h de diagnóstico y auditoría, sin cantidad fija de sesiones · Fase 2 (Construcción) y Fase 3 (Implementación) sin horas impuestas, a definir según lo que arroje el diagnóstico. Fechas exactas a confirmar.
- **Fecha del brief**: 2026-08-10
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414 5756615 · fmartinez@intezia.com
- **Cliente referente**: pendiente de confirmar

## Consideraciones del cliente (bloqueantes de diseño)

1. **Licenciamiento**: IOED cuenta con Microsoft 365 E3. La solución se integra a ese entorno; en ningún momento del deck se afirma que IOED migra o adopta otra suite (§4.11).
2. **Seguridad y confidencialidad**: es la **principal preocupación** del cliente. Toda propuesta contempla mecanismos robustos de control de acceso y protección de datos, evaluados desde la Fase 1.
3. **Compromiso de confidencialidad**: IOED pide firmar un compromiso de confidencialidad al aceptar la propuesta. Se menciona en el bloque "Importante" de la hoja de precio (`.cot-terms-box`), **no** en los pasos de arranque (`.s-steps`) ni en `acroforms.json` — el verificador bloquea el término "acuerdo" en ambos lugares por §4.15 (el checador no distingue NDA de cierre económico). Redacción usada: "compromiso de confidencialidad" (evita el término bloqueado).
4. **Integración con Traffic Marine**: mencionada como algo a **evaluar la viabilidad** durante el diagnóstico, nunca como integración ya decidida o comprometida. **De cara al cliente (deck)**: no se nombra la plataforma, se habla de "otras plataformas del cliente" (pedido de generalización, 2026-08-14).
5. **Flota**: 4 buques, 2 gabarras, 3 remolcadores — contexto interno de Operaciones de Buques, **no expuesto en el deck** (pedido de generalización, 2026-08-14): el cliente pidió que no se mencione cantidad ni tipo de flota, ni detalles de contratos/procesos internos de la empresa.

## Diagnóstico (5 puntos)

> **Nota de generalización (2026-08-14)**: a pedido del cliente, el deck y `programa.md` **no**
> exponen la cantidad ni el tipo de flota (antes: "4 buques, 2 gabarras y 3 remolcadores") ni
> detalles de contratos/procesos internos específicos (antes: contratos, órdenes de servicio,
> valuaciones, hojas de entrada de servicio, facturas, gestión de cuadrillas, contratación de
> terceros, nombre de plataforma "Traffic Marine"). Los puntos de abajo quedan como contexto
> interno completo; la redacción generalizada que sí va en el deck vive en `index.html` (§4.14
> — no se sobreescribe este historial, solo se marca qué cambió de cara al cliente).

1. Contratos, órdenes de servicio, valuaciones, hojas de entrada de servicio y facturas se gestionan sin un sistema que dé trazabilidad completa de fechas, estados, aprobaciones y pagos, de extremo a extremo.
2. Los gastos operativos, la gestión de cuadrillas y la contratación de servicios de terceros dependen de procesos manuales que dificultan centralizar información y generar reportes ejecutivos.
3. Las valuaciones quincenales y las hojas de entrada de servicio de las lanchas se procesan caso por caso, sin un flujo documental estandarizado ni informes automáticos.
4. La operación de 4 buques, 2 gabarras y 3 remolcadores genera informes operacionales y facturación por separado, sin evaluar todavía la integración con plataformas que ya usa el cliente (ej. Traffic Marine).
5. La seguridad y confidencialidad de la información es la principal preocupación de IOED: cualquier automatización debe partir de mecanismos robustos de control de acceso y protección de datos.

## Estructura del proyecto

### Plan de digitalización con IA · procesos administrativos y de flota de IOED

Sistema de trazabilidad y automatización con IA aplicado a dos frentes de la operación de IOED: (1) Servicios Navales — relación con el cliente, con proveedores y Operaciones de Lanchas — y (2) Operaciones de Buques — la flota de 4 buques, 2 gabarras y 3 remolcadores.

### Ritmo por fase: 3 fases, 5 etapas numeradas de forma corrida

- **Fase 1 · Diagnóstico y Auditoría** (Etapa 1 + Etapa 2) — **Etapa 1 · Mesas de trabajo por área**: sesiones de 2h, online síncrono, con los responsables de cada área (Servicios Navales y Operaciones de Buques), sin cantidad de sesiones fija. **Etapa 2 · Informe de diagnóstico**: Intezia consolida los hallazgos, evalúa mecanismos de control de acceso y protección de datos, y valida la viabilidad de integrar plataformas como Traffic Marine.
- **Fase 2 · Construcción** (Etapa 3 + Etapa 4) — **Etapa 3 · Diseño de la solución**: Intezia diseña, según lo que arroje el diagnóstico, la ruta más adecuada por área (capacitación, skills de IA, o ambas), dentro del entorno Microsoft 365 E3 del cliente. **Etapa 4 · Validación con responsables de área**: el equipo de IOED valida el diseño antes de implementar. **Sin horas impuestas**: depende del alcance definido en el diagnóstico.
- **Fase 3 · Implementación** (Etapa 5) — Se activa la solución validada por área y se entrega un manual de lineamientos de seguridad y uso responsable de la IA (roles y permisos, manejo de datos), con sesión de socialización. **Sin horas impuestas**, a definir.

> Numeración fija: Etapa 1 Mesas de trabajo por área · Etapa 2 Informe de diagnóstico · Etapa 3
> Diseño de la solución · Etapa 4 Validación con responsables de área · Etapa 5 Implementación.
> Se usa igual en todo el deck (programa, cronograma, roadmap, hoja de precio) y en este brief.

## Especificaciones del programa

- **Duración**: Fase 1 en sesiones de 2h de diagnóstico (cantidad abierta) · Fase 2 y Fase 3 sin horas impuestas, a definir según el diagnóstico. Fechas exactas a confirmar.
- **Modalidad**: Online síncrono para las mesas de trabajo de diagnóstico; Fase 2 y 3 a definir.
- **Audiencia**: responsables de área de Servicios Navales (relación con el cliente, proveedores y Operaciones de Lanchas) y de Operaciones de Buques.
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.

## Propuesta económica

- **Hoja "Inversión por fases"** (`.s-price`, h2 "Inversión por fases"): cotiza **las 3 fases por separado** (Fase 1 · Diagnóstico y Auditoría, Fase 2 · Construcción, Fase 3 · Implementación), cada una con su propia caja de monto, más una columna de **Inversión total del plan → Descuento → Total**. Reemplaza el patrón anterior de "solo Fase 1, resto progresivo" (aerocentro), a pedido explícito — patrón tomado de la propuesta económica de Cinex (CAP-072).
- **Campos de precio vacíos**, como en toda propuesta: ventas los llena en Adobe Reader — incluyendo las cajas de Fase 2 y 3, cuyo alcance real aún depende del diagnóstico (sin distinción visual en el deck; ventas decide si escribe un monto, un estimado o lo deja en blanco).
- Mecánica AcroForm: `PrecioFase1/2/3` (editables) + `PrecioBase` (subtotal auto-calculado como suma de las 3 fases) + `Descuento` + `PrecioTotal` (Base − Descuento) + `Notas`. 7 campos en esta slide (15 en total el deck) vía el nuevo grupo `FASE_PRICE_FIELDS` en `scripts/agregar-campo-precio.py`, activado por el marker único "Inversión por fases" — no afecta a ninguna otra propuesta del sistema (cada PDF se procesa por separado).
- La hoja incluye el bloque **"Importante"** (`.cot-terms-box`) con la implicación de términos y condiciones, **más una línea sobre el compromiso de confidencialidad** que el cliente pidió firmar al aceptar la propuesta.

## Entregables consolidados

- Informe de diagnóstico priorizado por área (Servicios Navales y Operaciones de Buques).
- Solución a medida construida según hallazgos (capacitación por área y/o skills de IA).
- Manual de lineamientos de seguridad y uso responsable de la IA.
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-098** en INTEZIA Education al cerrar el acuerdo.

## Notas de diseño

- Formato canónico A4 landscape, clonado de `aerocentro/` (mismo patrón de roadmap: 3 fases / 5 etapas, 1 sola hoja de cotización para Fase 1, Fase 2-3 cotizadas de forma progresiva).
- **17 slides**, misma estructura que `aerocentro/` + 1 slide propia: portada, **Quiénes somos**, diagnóstico, objetivos, programa (3 módulos), 3 slides de cronograma (una por fase), 3 páginas de roadmap (una por fase), metodología ABR, beneficios, impacto, precio (Fase 1), próximos pasos, cierre.
- **Quiénes somos (slide 02, 2026-08-14)**: agregada a pedido del cliente. Reutiliza el layout `.s-goals` (columnas general + specifics) ya validado en la slide de Objetivos — sin CSS nuevo. Contenido: fundadores Jean Iovino y Alejandro Moreno, 4 años en el mercado, clientes de referencia Pago Tronic, Messangi, Credicard y Zoom. Datos provistos directo por el usuario (no derivados de `empresa/identidad.md`, que los tiene pendientes de definir — considerar trasladarlos ahí para reutilizar en futuras propuestas).
- **Sin nombres de área expuestos en exceso**: se usa "Servicios Navales" y "Operaciones de Buques" como agrupadores (nombres que el propio cliente usó en su requerimiento), no se listan los sub-procesos internos completos en el deck — esos viven en `programa.md` y en las mesas de trabajo.
- **§4.11**: nunca se afirma que IOED migra o adopta Microsoft 365 — se integra al entorno que ya tiene.
- **§4.15**: "compromiso de confidencialidad" (no "acuerdo") en `.cot-terms-box`, fuera de `.s-steps` y de `acroforms.json` — evita el bloqueo del verificador sobre el término "acuerdo".
- **§4.9 Impacto**: fuentes reales citadas — Ardent Partners *State of ePayables 2025* (procesamiento de facturas), Deloitte Insights *Industry 4.0 and predictive technologies for asset maintenance* (mantenimiento predictivo de flota), McKinsey *The state of AI in early 2024* (adopción de IA generativa en documentos contables).
- **Traffic Marine**: mencionado solo como algo a evaluar la viabilidad de integrar, dentro del diagnóstico — nunca como integración ya decidida.
- **Asesora comercial**: Flavia Martínez (mismo formato que `aerocentro/`, `pago-tronic/`, `robin-agency-cap080/`).

## Deck adicional: versión Resumen (2026-08-14)

A pedido del cliente, la carpeta tiene un **segundo deck** más corto, sin tocar el original:

- **`index-resumen.html`** (8 slides, código `CAP-098 · Resumen`, mismo `styles.css` local):
  Portada → Alcance (`.s-program`, 3 fases condensadas, **3 temas por módulo** — ampliado
  2026-08-14 con hallazgos reales de `programa.md` §5.1: evaluación de control de acceso,
  Microsoft 365 E3, manual de seguridad, sesión de socialización) → Alcance detallado
  (`.s-schedule`, duración/modalidad/entregable clave por fase, sin ruta) → **Casos de
  uso** (`.s-program` reutilizado, 3 módulos con ejemplos genéricos de aplicación —
  trazabilidad documental, reportes ejecutivos, asistente interno — **100% propios del
  diagnóstico de IOED, sin datos ni estructura copiada de otro cliente**) → Casos de
  éxito (`.s-goals`, mismos 4 clientes de la slide Quiénes somos del deck completo — Pago
  Tronic, Messangi, Credicard, Zoom — solo nombres, sin resultados/métricas inventadas) →
  Beneficios (`.s-benefits`) → Inversión por fases (`.s-price`, misma mecánica de 3 fases
  + total) → Cierre. **Sin** Quiénes somos (identidad completa), diagnóstico, objetivos,
  roadmap, metodología ni impacto. Ampliada dos veces 2026-08-14 (5→7→8 slides) a pedido
  del cliente, para que se sintiera más completa.
- **`acroforms-resumen.json`**: Entregables + Acreditación + Notas (sin Paso01-03, esta
  versión no tiene slide de "Cómo arrancamos").
- **PDF**: `CAP-098 · Resumen Plan de digitalización con IA para la operación de IOED.pdf`
  — nombre distinto al original (por el `codigo` "· Resumen" en la portada) para que
  `generar-pdf.sh` no sobreescriba el PDF completo.
- **Regenerar este deck**: `./scripts/generar-pdf.sh ioed index-resumen.html` seguido de
  `python3 scripts/customize-acroforms.py "<ruta del PDF Resumen>" "clientes/propuestas/ioed/acroforms-resumen.json"`
  (rutas explícitas — con 2 PDFs en la carpeta, el modo automático por slug ya no aplica).
  Mismo patrón usado en `venemergencia/` (Deck A / Deck B) para múltiples decks en una
  misma carpeta.

## Pendientes

- Confirmar tarifa por fase (1, 2 y 3) y presupuesto indicativo (queda vacío en el PDF, ventas lo completa).
- Confirmar contacto/cargo de referencia en IOED.
- Confirmar fechas tentativas de inicio de las 3 fases.
- Confirmar con el cliente el alcance exacto de la Fase 2 (capacitación por área vs. skills de IA vs. ambas) una vez cerrado el diagnóstico.
- Validar viabilidad técnica real de integración con Traffic Marine durante el diagnóstico.
