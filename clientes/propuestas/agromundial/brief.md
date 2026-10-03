# Brief — AgroMundial · Piloto de Previsión de Demanda y Gobernanza de IA (CAP-096)

## Datos administrativos

- **Cliente**: AgroMundial · importadora de insumos alimentarios para la industria (panaderías, hoteles y similares)
- **Naturaleza**: Capacitación in-company · **piloto en Compras y Comercial** (7 personas) con doble objetivo — atacar el problema de previsión de demanda y corregir el uso ya existente de Claude — con **escalamiento ya proyectado por el cliente hacia Finanzas** (no cotizado en esta propuesta).
- **Slug**: `agromundial`
- **División Intezia**: `educacion` (cliente corporativo)
- **Tipo de documento**: Capacitación (`CAP-096`)
- **Programa**: Piloto de Previsión de Demanda y Gobernanza de IA — AgroMundial
- **Eje temático**: previsión de demanda con IA + gobernanza de un ecosistema de IA controlado por la empresa, aplicado a la cadena de valor de importación de insumos alimentarios (Compras → Importación → Almacenamiento → Ventas → Cobranza)
- **Modalidad**: a definir en próxima reunión
- **Duración**: a confirmar (ver Pendientes)
- **Fecha del brief**: 2026-08-06
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414 5756615 · fmartinez@intezia.com
- **Cliente referente**: **Cira** · Directora — el argumento que más la movió fue el de un ecosistema de IA controlado por la empresa (seguridad de datos, gobernanza y que el conocimiento no se vaya con la gente cuando rota); le pesa especialmente porque tiene equipo nuevo.

## Por qué este proyecto

AgroMundial importa insumos alimentarios para panaderías, hoteles y clientes similares. Su cadena de valor es **Compras → Importación → Almacenamiento → Ventas → Cobranza**, y el dolor está concentrado en el primer eslabón: **no logran determinar qué, cuándo y cuánto comprar**. Cuando se quedan cortos pierden ventas que no se recuperan; cuando se pasan, cargan con costos de almacenamiento — el problema les cuesta plata en ambas direcciones.

La raíz es de **data, no de criterio**: su histórico de ventas 2025–2026 está contaminado. Las caídas de venta que registran no siempre son caídas de demanda reales — muchas veces fueron quiebres de stock. Y hay factores externos que nunca quedaron registrados, como la entrada de nuevos competidores. El resultado es que no pueden distinguir estacionalidad real de volatilidad de mercado, así que compran con información que parece dura pero no lo es.

**Dato clave**: AgroMundial ya usa Claude, pero sin licencias corporativas — son los propios colaboradores quienes las compraron por su cuenta — y están generando reportes erróneos por prompts mal construidos y data incompleta. Esto cambia la conversación: no hay que convencerlos del valor de la IA, ya invirtieron tiempo en ella y están frustrados con el resultado. Lo que necesitan es **método**, no una primera introducción a la herramienta.

El argumento que más movió a Cira fue el de un **ecosistema de IA controlado por la empresa**: seguridad de datos, gobernanza y, sobre todo, que el conocimiento no se vaya con la gente cuando rota. AgroMundial tiene equipo nuevo, y eso le pesa como directora.

## Diagnóstico (5 puntos)

1. AgroMundial no logra determinar **qué, cuándo y cuánto comprar** — el dolor de toda la cadena de valor está concentrado en el primer eslabón (Compras).
2. Los quiebres de stock generan ventas perdidas que no se recuperan; el exceso de compra genera costos de almacenamiento — el problema pega en ambas direcciones.
3. El histórico de ventas 2025–2026 está contaminado: caídas registradas como demanda que en realidad fueron quiebres de stock, y factores externos (como la entrada de nuevos competidores) que nunca quedaron registrados.
4. El equipo no puede distinguir estacionalidad real de volatilidad de mercado, así que compra con información que parece dura pero no lo es.
5. El equipo ya usa Claude por cuenta propia (sin licencias de la empresa), generando reportes erróneos por prompts mal construidos y data incompleta — hay inversión de tiempo ya hecha, pero sin método ni gobernanza.

## Estructura del proyecto

### Piloto · Compras y Comercial (7 personas)

Se eligen estas dos áreas porque concentran la mayor cantidad de empleados nuevos de AgroMundial y son, además, quienes están usando Claude de forma incorrecta hoy. El piloto tiene **doble objetivo**: atacar el problema de previsión de demanda y corregir el uso de la herramienta.

### Ritmo: diagnóstico + construcción + implementación

- **Diagnóstico** — sesiones con el equipo de Compras y Comercial para levantar el histórico real de ventas, identificar los quiebres de stock mal registrados como caídas de demanda, y mapear cómo está usando cada persona Claude hoy (prompts, reportes, criterio).
- **Construcción** — a cargo de Intezia: se diseña el marco de previsión de demanda (separando estacionalidad real de ruido de mercado) y el ecosistema de IA gobernado (roles, permisos, prompts estandarizados) con los hallazgos del diagnóstico.
- **Implementación** — se activa el ecosistema con el equipo de Compras y Comercial: previsión de demanda con criterio validado y uso correcto y gobernado de Claude en el día a día.

## Especificaciones del programa

- **Duración**: a confirmar (ver Pendientes).
- **Modalidad**: a definir en próxima reunión con el cliente.
- **Audiencia**: 7 personas del piloto — equipo de Compras y Comercial de AgroMundial.
- **Fechas tentativas**: a confirmar en kick-off.
- **Acreditación**: constancia de participación INTEZIA Education.

## Propuesta económica

- **Cotización única** del piloto (Compras y Comercial, 7 personas). El escalamiento hacia Finanzas se cotiza de forma progresiva, según los resultados del piloto — no se pre-cotiza en esta propuesta.
- La hoja de cotización incluye un bloque destacado **"Importante"** (caja con borde naranja) con la implicación comercial: el servicio se presta bajo los **términos y condiciones**, aceptados por ambas partes al avanzar con la propuesta. Enlace real y clicable: https://drive.google.com/file/d/1PA-ZSt4KnyY5dpxXzgkIk6-yfGlV2eF8/view?usp=drive_link (mismo enlace y formato que CAP-082 Aerocentro; no vive en el AcroForm porque los campos de formulario no soportan hipervínculos). El enlace depende de los permisos de Drive del archivo — si el cliente reporta que no abre, revisar que esté compartido como "Cualquier persona con el enlace puede ver".

## Escalamiento (proyectado, no cotizado)

Cira ya proyecta el escalamiento hacia **Finanzas**, con cuatro frentes concretos que ella misma levantó:

1. **Análisis de Cuentas por Cobrar y Pareto** de clientes y productos.
2. **Conciliación bancaria.**
3. **Cálculo de comisiones** para la fuerza de ventas freelance — hoy manual, lento, y les está haciendo incumplir plazos de pago.
4. **Seguimiento de los compromisos de pago de importaciones** para tener visibilidad real de flujo de caja.

Este escalamiento se menciona en el deck (roadmap / notas) como próximo paso proyectado por el cliente, sin cotizarlo — se cotiza por separado tras los resultados del piloto.

## Entregables consolidados

- Ecosistema de IA gobernado operando en Compras y Comercial.
- Marco de previsión de demanda que separa estacionalidad real de volatilidad de mercado.
- Informe de diagnóstico del histórico de ventas 2025–2026 y su contaminación por quiebres de stock.
- Estándares de uso de Claude (prompts, roles, permisos) para el equipo del piloto.
- Workbook digital y constancia de participación INTEZIA.

## Notas comerciales

- Vigencia de la propuesta: 30 días.
- Programa registrado como **CAP-096** en INTEZIA Education al cerrar el acuerdo.

## Notas de diseño

- Formato canónico A4 landscape, clonado de `pago-tronic/` (multi-área, roadmap de 3 etapas por defecto: Diagnóstico → Construcción → Implementación).
- `.s-program`: **2 module cards** (Compras, Comercial) — se agrega regla CSS local para 2 módulos (grid de 2 columnas anchas, tomada del patrón ya usado en `robin-agency/`), en vez del grid de 3 columnas por defecto pensado para 3+ módulos.
- `.s-schedule`, una por área (Compras y Comercial), mismo patrón de 3 columnas (Diagnóstico / Implementación / Recursos) que `pago-tronic/`.
- `.s-heatmap`: 2 filas (Compras, Comercial).
- Roadmap 3 etapas (`.rmx-*`): Diagnóstico → Construcción (Intezia) → Implementación, resultado = "Piloto de previsión de demanda y ecosistema de IA gobernado operando en Compras y Comercial", con mención del escalamiento a Finanzas en el bullet final.
- Slide de Impacto con datos reales (§4.9): McKinsey — *Supply Chain 4.0 – the next-generation digital supply chain* (2016), sobre reducción de error de previsión y de quiebres de stock con IA · IBM — *Cost of a Data Breach Report 2025* (Ponemon Institute), sobre el costo de la IA sin gobernanza ("shadow AI") — conecta directamente con el argumento de Cira.
- Hoja de cotización (`.s-price`): se agrega `.cot-terms-box` + enlace de términos y condiciones, tomado tal cual de `aerocentro/` (CAP-082) — bloque "Importante" con borde naranja, enlace real clicable a Drive.
- `[CÓDIGO]` sustituido por CAP-096 en Acreditación.
- Reglas §4.11 y §4.13 respetadas: no se afirma que AgroMundial migra de ningún stack tecnológico (Claude se integra a su operación, no la reemplaza); sin guion largo en el copy de cara al cliente. §4.4: sin "cohort/cohorts" — se usa "grupos"/"equipo" del piloto (7 personas).
- **Asesora comercial**: Flavia Martínez, mismo formato que el resto de propuestas recientes.

## Pendientes

- Confirmar modalidad (Presencial / Online Síncrono / Híbrido).
- Confirmar duración exacta (horas/sesiones) del diagnóstico, construcción e implementación.
- Confirmar fechas tentativas de inicio del piloto.
- Confirmar presupuesto indicativo del piloto.
- Confirmar cargo exacto de Cira y datos de contacto directo.
- Validar con el cliente el alcance exacto de los 4 frentes de escalamiento a Finanzas cuando se cotice esa fase.
