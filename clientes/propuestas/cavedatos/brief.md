# Brief — Cavedatos (CAI-001)

> **Sin Ficha Comercial** (modalidad vieja). Contenido adaptado de la propuesta previa de
> Cavedatos en formato viejo (CAP-002, «Capacitación Avanzada en IA Generativa para Equipos
> de Prensa») + instrucciones directas del usuario. Se re-emite bajo el modelo nuevo:
> servicio **Habilidades**, código nuevo **CAI-001**.

## Datos administrativos

- **Empresa**: Cavedatos
- **Slug**: `cavedatos`
- **División Intezia**: `educacion` (cliente corporativo; la división gobierna logo/marca)
- **Servicio** (Modelo Intezia, `empresa/tipos-de-documento.md §0`): `habilidades` — es una
  capacitación in-company (Habilidades puede ser taller o capacitación; aquí, capacitación).
- **Alianza**: no
- **Código**: `CAI-001` (primer código de la serie Habilidades / Capacidad Instalada)
- **Tipo de documento**: Capacitación In-Company
- **Eje temático**: IA generativa avanzada para el equipo de prensa — producción multimedia
  (texto, visual, video, voz), incorporando la IA a los flujos existentes sin reemplazar el
  criterio humano, con seguridad legal e identidad corporativa
- **Fecha del brief**: 2026-08-27
- **Estado**: `Borrador`

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414 5756615 · fmartinez@intezia.com

## Necesidades y objetivos de la capacitación (instrucción del usuario)

- **Meta principal**: **incorporar la IA a los flujos de trabajo existentes, no
  reemplazarlos** (videos, reels, presentaciones, flyers, boletines, Notipuerto). Optimizar
  velocidad y calidad, **sin eliminar el criterio humano**.
- **Entregables concretos esperados** (quick wins / entregables destacados):
  - Avatar de IA para uso interno de comunicaciones.
  - Presentaciones tipo Canva de alta calidad en menor tiempo.
  - Flyers y piezas audiovisuales más ágiles.

## Especificaciones del programa

- **Duración**: 10 horas en total · **2 sesiones presenciales de 5 h** (ajuste respecto a la
  propuesta vieja, que eran 4 sesiones). El currículo de 4 módulos se mantiene y se agrupa en
  las 2 sesiones: Sesión 1 = Módulos I+II (Legalidad+Texto y Diseño Visual), Sesión 2 =
  Módulos III+IV (Audiovisual+Voz e Integración/Hackathon).
- **Modalidad**: Presencial.
- **Audiencia**: equipo de prensa de Cavedatos (cantidad de participantes a confirmar).
- **Stack del cliente** (ya con licencias, se integra a sus flujos): **Gemini**, Canva,
  CapCut, Luma Labs, Freepik, Envato.
- **Acreditación**: doble certificación INTEZIA + Cavedatos (heredada de la propuesta vieja).

## Estructura curricular (4 módulos, heredados de la propuesta vieja, actualizados)

1. **Prompting Técnico Avanzado** — prompt avanzado, Gemini, estilo y línea editorial,
   refinamiento. (Se retiró el foco legal/derechos de autor del deck a pedido del usuario:
   esta es una propuesta de Habilidades, no de gobierno/políticas.)
2. **Diseño Visual Generativo** — prompting de imágenes, Freepik/Envato, Canva, consistencia
   de marca.
3. **Producción Audiovisual y Voz** — Luma Labs (video), prompting de video, voz generativa
   (texto a voz), CapCut.
4. **Integración y Flujo de Trabajo** — stack conectado, curaduría humana, Hackathon: Media
   Kit + Avatar interno.

## Impacto (§4.9) — fuentes reales citadas

- **MIT — Noy y Zhang, Science 2023**: un asistente de IA redujo cerca del 40% el tiempo de
  tareas de redacción profesional, mejorando la calidad.
- **Canva — Visual Economy Report 2024**: la IA reduce hasta un 70% el tiempo de diseño
  gráfico.
- **McKinsey — The State of AI 2024**: ~65% de las organizaciones ya usa IA generativa.
- **McKinsey — The economic potential of generative AI 2023**: la IA puede aumentar la
  productividad de marketing entre 5% y 15% del gasto total.

## Propuesta económica

- **Hoja estándar "Propuesta Económica"** (`.s-price`, PRECIO_FIELDS): Duración + Programa +
  Notas + Cotización (Propuesta+Inversión / Descuento / Total). Campos de precio vacíos:
  los llena ventas en Adobe Reader.
- `Programa` pre-llenado con nombre del programa + doble certificación + stack. `Notas`
  vacío (se evita cualquier término económico, §4.15; ventas lo redacta si aplica).
- Vigencia: 30 días + bloque de términos y condiciones (estándar). **Sin** las condiciones de
  pago que traía la propuesta vieja («pago en Bolívares a tasa EURO BCV», «7 días»,
  «anticipo del 50%») — el esquema nuevo no las incluye.

## Notas de diseño

- Base clonada de `cumbre-andina/` (mono-fase canónico, enlaza `../_base/styles.css`) +
  `overrides.css` local con el **cierre tipo escalera** (que `_base` todavía no trae).
  **11 slides.**
- **Esquema nuevo aplicado** (§4.10a): se retiró la slide de **Metodología ABR** y el bloque
  de **Equipo facilitador** que traía la propuesta vieja; cierre tipo escalera editable; CTA
  sin link; correo del cierre `servicio@intezia.com`.
- **Beneficios — bloques Resultados · Por qué [Servicio] · Entregables · Valor inmediato**
  (estándar 2026-08-27, unificado para todos los servicios; se retiran «Perfil de egreso» y
  «Acreditación» del deck — la certificación se comunica en el `Programa` de la hoja de
  precio). El campo AcroForm `Acreditacion` se reutiliza como «Valor inmediato» (nombre
  interno conservado por compatibilidad).
- **Beneficios v3, layout ampliado (retrofit 2026-08-28, solo aspecto visual)**: el deck
  nació en v2 (2 tarjetas oscuras + 2 blancas, grid de 240px) y se actualizó al estándar
  vigente por pedido directo del usuario — mismo contenido, mismas horas, sin cambios de
  texto salvo el bullet `•` agregado al inicio de cada línea de Entregables/Valor inmediato
  (parte del look de checklist del formato v3, no un cambio de redacción). Las 4 tarjetas
  quedan oscuras, el grid sube a 570px, tipografía y padding ampliados, y las cajas AcroForm
  se agrandan de 158×117pt a 145×355pt con fuente de 10 a 13pt vía `BENEFICIOS_LAYOUT` en
  `customize-cavedatos.py`. Ver `plantillas/propuesta-comercial.md` → *Layout ampliado*.
- **Sin foco legal**: a pedido del usuario, el deck no menciona «legalidad», derechos de autor
  ni propiedad intelectual (era el eje del módulo I en la propuesta vieja). El módulo I pasa a
  «Prompting Técnico Avanzado».
- **§4.15 corregido respecto a la propuesta vieja**: los «Próximos pasos» ya **no** mencionan
  «Firmamos acuerdo · contrato + factura del 50%»; ahora son logística (fechas/sede, acceso,
  kick-off).
- **Gemini** en vez de «Google One (Gemini)» de la propuesta vieja (el cliente usa Gemini).
- El nombre «Notipuerto» y los formatos del cliente (videos, reels, flyers, boletines) se
  usan en el diagnóstico y el objetivo como su realidad operativa.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh cavedatos
python3 scripts/customize-acroforms.py cavedatos
python3 scripts/customize-cavedatos.py "clientes/propuestas/cavedatos/CAI-001 IA Generativa Avanzada para Equipos de Prensa.pdf"
```

El 3er paso agrega las 4 cajas editables del cierre escalera (no las inyecta
`agregar-campo-precio.py`). Sin él, el cierre queda sin campos editables.

## Pendientes

- Confirmar cantidad de participantes del equipo de prensa.
- Confirmar fechas de las 2 sesiones y la sede.
- Confirmar que la doble certificación INTEZIA + Cavedatos sigue vigente para este acuerdo.
