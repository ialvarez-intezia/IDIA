# Brief — Amcor Rigid Packaging de Venezuela S.A (DET-001)

> **Fuente primaria: Ficha Comercial Intezia — Amcor** (levantada por Flavia Martínez,
> 2026-08-26) + resumen de reunión de la asesora. Primera propuesta del sistema bajo el
> modelo nuevo de 4 servicios (`empresa/tipos-de-documento.md §0`), y primera nacida de una
> Ficha Comercial. Los datos de abajo se extraen de esa ficha; no se cotiza a ciegas.

## Datos administrativos

- **Empresa**: Amcor Rigid Packaging de Venezuela S.A
- **Sector**: Manufactura · Grande / Enterprise (+250 empleados)
- **Slug**: `amcor`
- **División Intezia**: `educacion` (cliente corporativo; la división gobierna logo/marca)
- **Servicio** (Modelo Intezia): `deteccion` — Detección con foco inicial en el área de Compras
- **Alianza**: no
- **Código**: `DET-001` (primer código de la serie Detección)
- **Frente Intezia**: Consultoría (auditoría + capacitación in-company)
- **Eje temático**: diagnóstico de oportunidades de IA en el área de Compras (y Atención al
  Cliente), con nivelación básica de Copilot en paralelo, dentro del entorno Microsoft 365
- **Fecha del brief**: 2026-08-26
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414 5756615 · fmartinez@intezia.com
- **Cliente / interlocutor**: Jomar Vizcaya · Líder de Procesos de Compra · jomar.vizcaya@amcor.com
- **Servicio previo con Intezia**: no, es el primer contacto.

## Estructura del proyecto (2 fases)

> Definida con el cliente en la reunión (resumen de Flavia). Debe reflejarse así en la propuesta.

- **Fase 1 · Detección + nivelación básica de Copilot, en paralelo.** Es lo **único que se
  cotiza** en esta etapa. La Detección audita el área de Compras (y Atención al Cliente),
  mide la Matriz de Madurez Digital, prioriza cuellos de botella por impacto y esfuerzo, y
  entrega un Reporte Final con la hoja de ruta. En paralelo, el equipo se nivela en el uso
  básico de Copilot (prompts efectivos, cómo instruir a la IA, resultados rápidos).
- **Fase 2 · Habilidades**, para atacar los cuellos de botella detectados en la Fase 1.
  **Aparece contemplada** en la propuesta como el camino completo, pero su **contenido y su
  valor se definen después del diagnóstico, no ahora** (cotización progresiva, patrón
  aerocentro).

## Contexto y pain points (Ficha Comercial, Bloques C/D)

- El área de Compras gestiona un flujo de **cerca de 9.000 solicitudes** de forma manual; el
  equipo de **4 personas** debe dar respuesta inmediata a cada requerimiento de la operación
  (repuestos, servicios, bienes, insumos) para mantener la continuidad del negocio.
- **No usan IA hoy** (Bloque B: IA en uso = Ninguna). Desean reducir tiempo en todos los
  procesos manuales.
- Urgencia real: se sienten **estancados**, saben que 4 personas no se dan abasto y quieren
  avanzar rápido. Horizonte: **corto plazo (0-3 meses)**.
- Sistema administrativo interno: SAAP (el usuario carga solicitudes, Compras las gestiona).
  Están **evaluando por su cuenta**, con otras empresas, integrar ODOO para el módulo de
  gestión de solicitudes. **Nada de esto va en el deck** (es su evaluación interna con
  terceros, no un servicio de Intezia).

## Restricciones (Ficha Comercial, Bloque E) — bloqueantes de diseño

1. **Solo Microsoft, por ahora.** Por ser transnacional, Amcor tiene permitido trabajar
   únicamente con Microsoft en este momento. La IA que quieren incorporar es **Copilot
   (Microsoft)**.
2. **Claude no se asume.** Preguntaron por Claude, pero **deben validarlo internamente**. El
   deck **no menciona Claude** en ningún lugar.
3. **§4.11**: el deck **no afirma** que Amcor migra ni adopta un nuevo stack. Copilot se
   enmarca como algo que se usa **dentro de su entorno Microsoft 365 actual**; la nivelación
   es formación en una herramienta de ese entorno, no una migración.
4. Apertura al cambio: **media**. Presupuesto: **en evaluación**. Patrocinio ejecutivo y
   quién decide la contratación: no registrados en la ficha (pendientes de confirmar).

## Bloque específico de Detección (Ficha Comercial)

- **Áreas a auditar**: Compras y Atención al Cliente (foco inicial: Compras).
- **Stakeholder clave**: Jomar Vizcaya. **Personas por área**: 4. **Diagnóstico previo**: no.
- **Modalidad**: Presencial, en las oficinas de Amcor. **Sedes distintas**: no.
- **Calendario**: por confirmar (el cliente no lo tenía definido).
- **Urgencia/disparador**: sí, avanzar lo antes posible (se sienten estancados).
- **Expectativa de madurez**: mejora sustancial de sus procesos y operatividad.
- **Quick wins identificados** (van al bloque "Valor inmediato" del deck): **manual de
  prompts** y **workbooks** aplicables por el equipo tras la detección.
- **Objetivo del Reporte Final**: ver cómo pasan de un punto A a un punto B, cómo opera el
  departamento hoy y qué beneficios se obtienen.
- **Definición de éxito del cliente**: identificar los cuellos de botella, priorizarlos por
  peso, y saber qué herramienta usar para cada uno.

## Expectativas y horizonte (Bloque G)

- Reducir la mayor cantidad de tiempo posible en su operatividad, ser más eficientes y
  dominar las herramientas de IA para aplicarlas en el día a día.
- Áreas que el cliente marcó para capacitar/optimizar con IA: Finanzas y Administración,
  Atención al Cliente, Compras y Proveedores, Dirección General. (El foco cotizado ahora es
  Compras; el resto puede entrar en fases posteriores.)

## Propuesta económica

- **Hoja "Inversión por fases"** (`.s-price`): solo **Fase 1** tiene caja de precio editable
  (`PrecioFase1`); la **Fase 2** aparece con la nota estática **"Se cotiza tras el
  diagnóstico"** (sin caja). Columna derecha: Inversión de la Fase 1 (`PrecioBase`,
  auto = Fase 1) → Descuento → Total. Campos vacíos: los llena ventas en Adobe Reader.
- Mecánica: el grupo `FASE_PRICE_FIELDS` de `agregar-campo-precio.py` inyecta
  PrecioFase1/2/3; **`customize-amcor.py` quita PrecioFase2 y PrecioFase3** (solo Fase 1 se
  cotiza) y recalcula `PrecioBase` = Fase 1. Además agrega las 4 cajas del cierre escalera.
- Vigencia: 30 días. Sin montos, anticipos ni condiciones de pago en el deck (§4.15).

## Notas de diseño

- Base clonada de `go-pharma/` (esquema nuevo: sin Metodología ABR ni Equipo facilitador
  §4.10a; cierre tipo escalera editable; inversión por fases). **12 slides.**
- **Beneficios por servicio (Detección)**: se omiten Perfil de egreso y Acreditación; las dos
  cajas AcroForm se reutilizan como **"Entregables del diagnóstico"** (campo `Entregables`) y
  **"Valor inmediato"** (campo `Acreditacion`, repurposado — el nombre interno del campo se
  conserva por compatibilidad con `agregar-campo-precio.py`; su contenido ya no es una
  acreditación). Ver `plantillas/propuesta-comercial.md → Beneficios por servicio`.
- **Impacto (§4.9)** — fuentes reales citadas verbatim:
  - McKinsey, *Transforming procurement for an AI-driven world*: copilots de IA mejoran la
    productividad de compras 25-40%; decisiones asistidas por IA aceleran la selección de
    proveedores ~30%.
  - Microsoft, *Work Trend Index 2024* (*What Can Copilot's Earliest Users Teach Us About AI
    at Work?*): 77% de usuarios empresariales reportó aumento medible de productividad; 29%
    más rápidos en tareas de búsqueda, redacción y resumen.
- **No expuesto en el deck**: nombre del sistema SAAP, evaluación de ODOO, cifras de flota o
  procesos internos que no aporten a la venta. El volumen (9.000 solicitudes, 4 personas) sí
  se usa como gancho del diagnóstico (dato propio del cliente, de su ficha).
- **Beneficios v3, layout ampliado (retrofit 2026-08-28, solo aspecto visual)**: el deck nació
  en v2 (2 tarjetas oscuras + 2 blancas, grid de 240px) y se actualizó al estándar vigente por
  pedido directo del usuario — mismo contenido, mismas horas, sin cambios de texto salvo el
  bullet `•` agregado al inicio de cada línea de Entregables/Valor inmediato (parte del look
  de checklist del formato v3, no un cambio de redacción). Las 4 tarjetas quedan oscuras, el
  grid sube a 570px, tipografía y padding ampliados, y las cajas AcroForm se agrandan de
  158×117pt a 145×355pt con fuente de 10 a 13pt vía `BENEFICIOS_LAYOUT` en
  `customize-amcor.py`. Ver `plantillas/propuesta-comercial.md` → *Layout ampliado*.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh amcor
python3 scripts/customize-acroforms.py amcor
python3 scripts/customize-amcor.py "clientes/propuestas/amcor/DET-001 Detección de IA para el área de Compras de Amcor.pdf"
```

El 3er paso (`customize-amcor.py`) quita PrecioFase2/3, recalcula el subtotal a Fase 1 y
agrega las 4 cajas editables del cierre escalera. Sin él, quedan cajas de precio huérfanas y
el cierre sin campos editables.

## Pendientes

- Confirmar fechas de inicio de la Fase 1 (el cliente no tenía calendario).
- Confirmar quién decide/aprueba la contratación y el patrocinio ejecutivo (no en la ficha).
- Confirmar disponibilidad real de licencias Copilot en el entorno del cliente antes del
  arranque (tienen M365; Copilot "no centralizado").
- Validar internamente (del lado del cliente) si pueden integrar Claude a futuro; hoy fuera
  de alcance.
- Alcance, horas y valor de la Fase 2 (Habilidades): se definen tras el diagnóstico.
