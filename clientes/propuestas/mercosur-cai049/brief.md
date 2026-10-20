# Brief · Mercosur · Servicio de Habilidades (CAI-049)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Mercosur
- **Slug**: `mercosur-cai049`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-049`), presentada al cliente como **propuesta de proyecto**; formato compacto de 8 slides (con hoja de inversión (campos de monto vacíos para ventas))
- **Eje temático**: Nivelación en inteligencia artificial con Microsoft 365 Copilot para las 50 personas de una casa de bolsa digital, en cinco grupos por área, con ética y uso seguro de la información y un proyecto final por participante
<!--auto:inicio-->
- **Alcance**: 15 entregables en 5 grupos · 40 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Inversión · 8 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: María Iribarren, Asesora comercial · miribarren@intezia.com · +58 414 0570056
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: no hay Ficha de Levantamiento. Se usó la minuta de la reunión (sin fecha en el deck, por indicación del usuario) y las indicaciones de la asesora (María). Donde se contradicen (composición de los grupos), el usuario confirmó la de María.
- **fecha_arranque_deseada**: no se dio (se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones). El kickoff es por grupo y se agenda tras la aprobación; el cliente pide fuera del horario de mercado (9:00 am a 1:00 pm), sugerido de 5:00 a 7:00 pm.
- **resultados_esperados**: no se dieron; sin esta respuesta no se agrega ROI, no se inventa (retorno en modo método).

## Origen y fuente

- **Origen**: Minuta de la reunión con Mercosur, indicaciones de la asesora María Iribarren y respuestas del usuario del 13/10/2026 (grupos de María, 8 h por grupo, Microsoft 365 Copilot, sin facilidad de pago, sin nómina ni políticas)
- **Fuente del insumo**: Minuta de la reunión e indicaciones de la asesora: casa de bolsa de 50 personas en 8 unidades, nivelación en Copilot en 5 grupos por área de máximo 12 personas, 8 h por grupo, presencial y fuera del horario de mercado
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Fuentes: minuta de la reunión con Mercosur, indicaciones de la asesora (María) y respuestas del usuario del 13/10/2026. División Educación, servicio Habilidades, sin alianza, código CAI-049. Por indicación del usuario, la propuesta no lleva fecha de la reunión ni de nada.
- Composición de los 5 grupos según María (confirmada por el usuario): Atención al cliente; Tecnología; Mercadeo, Contabilidad, Administración y Talento Humano; Operaciones y Cumplimiento; Negocios. La minuta traía otra (Cumplimiento solo; Clientes personales con Operaciones y Negocios) y Talento Humano no aparecía: manda la de María.
- 8 h por grupo para los 5 (decisión del usuario; María hablaba de 6 a 8 h): 2 h de IA y uso seguro, 4 h de práctica con Copilot y 2 h de proyecto final, 40 h en total. Interno para el kickoff: sesiones presenciales de 2 h (4 por grupo), horario sugerido de 5:00 a 7:00 pm por confirmar, fuera del horario de mercado (9:00 am a 1:00 pm). Nada de esto va en el deck (§4.23).
- Máximo 12 personas por grupo (capacidad de la sala; no hay computadoras para todos). Si un grupo pasa de 12, se añaden horas: el deck lo aclara en el alcance, la logística y la inversión. No se conoce el número de personas por grupo; Atención al cliente es el más grande y podría superar las 12. Tecnología son 5 personas y un equipo externo pequeño: por confirmar si participa.
- Herramienta: Microsoft 365 Copilot en los 5 grupos (el usuario confirmó que tienen la licencia), incluido Negocios, que ya usa Claude a nivel avanzado (no se menciona). No hay licencias adicionales: el cliente no puede pagar una suscripción extra.
- Fuera de la propuesta por indicación del usuario: la automatización de la nómina de RRHH (la minuta pedía incluirla, con licencia de Claude y conector de Excel), el borrador de políticas de uso de IA y los valores. El kit de onboarding de la minuta se cubre con los workbooks. En el deck solo se aclara que la política de uso se trabaja aparte.
- Sin facilidad de pago (omitir: pago), por indicación del usuario. El seguimiento a 30, 60 y 90 días va incluido; se dejó la garantía 30-60-90 estándar de Habilidades porque el usuario dijo «sí coloca el seguimiento»: confirmar si va como garantía o solo como medición.
- Los tres datos de la portada salen de la minuta y de María, sin la fecha de la reunión y sin los incidentes con pasantes que suben documentos (indicación del usuario). La cita del líder de Tecnología no se usa.
- Las prácticas sugeridas de cada grupo las propuso el sistema para mostrar el tipo de trabajo (Word, Excel, Outlook y Teams con Copilot): no salen de tareas confirmadas por el cliente y se ajustan en el kickoff con cada grupo.
- Retorno en modo método: no hay datos del cliente (volúmenes, tiempos ni valor de la hora). La cifra de la nómina de RRHH (un día frente a unas 3 horas) no se usa.
- Asesora: María Iribarren, con los datos de la CAI-045 (confirmados por el usuario).

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total: vacíos, los llena ventas.

## Pendientes

- Definir la inversión, el descuento y el total (campos vacíos para ventas).
- Confirmar cuántas personas hay en cada grupo, sobre todo en Atención al cliente (si pasa de 12 se añaden horas), y si el equipo externo de Tecnología participa.
- Confirmar el horario (sugerido de 5:00 a 7:00 pm) y las computadoras disponibles por grupo.
- Confirmar si el seguimiento a 30, 60 y 90 días va como garantía o solo como medición.
- La minuta acordó enviar también una propuesta de automatización de la nómina de RRHH: el usuario la dejó fuera de la CAI-049. Decidir si va como propuesta aparte.
- La propuesta lleva los campos de monto vacíos: dejar meta.json en Borrador hasta que ventas los llene y la envíe.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py mercosur-cai049      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh mercosur-cai049             # verifica, genera el PDF y ajusta los campos
```
