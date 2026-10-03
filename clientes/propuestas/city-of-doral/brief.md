# Brief — City of Doral · Cómo vender más con IA en Estados Unidos (CH-014)

> **Base estructural**: clon conceptual de `doral-comunidad-sfic/` (CH-008, "IA Para Todos"),
> adjuntado por el usuario como referencia. Mismo formato (charla online gratuita de 90
> minutos, alianza institucional, división Fundación), pero con alianza, audiencia, eje
> temático y certificación distintos — no es un clon literal, se reconstruyó el contenido.

## Datos administrativos

- **Cliente / aliado**: City of Doral (gobierno municipal — nueva alianza, distinta de
  `doral-comunidad-sfic/` que era con South Florida International College)
- **Slug**: `city-of-doral`
- **División Intezia**: `fundacion`
- **Servicio (§4.1a)**: `habilidades` — categoría Charla
- **Alianza**: `sí` — City of Doral convoca/promueve el evento junto con Intezia
- **Código**: `CH-014` (verificado libre — sigue a CH-013 Grupo Ferrara)
- **Eje temático**: Cómo vender más con inteligencia artificial generativa en el mercado de
  Estados Unidos, dirigido a dueños y gerentes de empresa de Doral
- **Duración**: 90 minutos, online, gratuita
- **Fecha del brief**: 2026-09-10
- **Estado**: `Borrador`

## Contacto

- **Asesora Intezia**: Carolain Fernández · PR & Partnerships / COO Intezia Foundation ·
  cfernandez@intezia.com (sin teléfono — confirmado con el usuario que el bloque de contacto
  del cierre queda solo con correo).
- **Contacto en City of Doral**: por confirmar.

## Decisiones confirmadas con el usuario (2026-09-10)

1. **Audiencia**: dueños o gerentes de empresa (no "toda la comunidad" como en CH-008) — la
   charla se reorienta de alfabetización general de IA a **venta y crecimiento de negocio**.
2. **Eje temático nuevo**: "Cómo vender más con IA en Estados Unidos" — reemplaza por completo
   el eje de CH-008 (fundamentos de IA + empleabilidad general).
3. **Certificación — sin QR, sin co-branding**: confirmado con el usuario — el certificado se
   emite **solo por Intezia**, sin el mecanismo de verificación por código QR ni cobranding con
   City of Doral que sí tenía CH-008 con SFIC (una institución académica; City of Doral es un
   gobierno municipal, no coemite credenciales). Es un certificado de participación estándar,
   mismo criterio que otras Charlas/Capacitaciones de Habilidades.
4. **Modalidad**: online y gratuita, igual que CH-008 (confirmado, no se cambia a presencial
   pese al cambio de audiencia a dueños/gerentes de empresa).
5. **Sin teléfono de Carolain** en el bloque de contacto del cierre — solo nombre, cargo y
   correo (confirmado con el usuario).
6. **Sin Metodología ABR ni Equipo facilitador expuestos** (§4.10a) — CH-008 sí tenía un bloque
   "Equipo INTEZIA Fundación" dentro de Beneficios (formato viejo, previo a esta regla); CH-014
   usa Beneficios v3 (4 tarjetas oscuras) sin ese bloque, y Cierre escalera en vez del cierre
   fijo + link de Calendly que tenía CH-008.

## Estructura de contenido (adaptada de CH-008, mismo patrón de 4 módulos / 90 min)

| # | CH-008 (comunidad general) | CH-014 (dueños/gerentes de empresa) |
|---|---|---|
| I | Qué es (y qué no es) la IA | Qué es (y qué no es) la IA — sin cambios, sigue siendo la base |
| II | IA en tu día a día (redactar, buscar, negocio propio) | IA para vender más (anuncios, atención al cliente, contenido para redes) |
| III | IA y empleabilidad (currículum, entrevistas, portafolio) | IA y el mercado de Estados Unidos (contenido bilingüe, cliente en EE.UU., reseñas) |
| IV | Cierre y certificación (QR) | Cierre y certificación (sin QR, solo Intezia) |

## Impacto (§4.9) — estudios reales, distintos de CH-008

CH-008 usaba Brynjolfsson/NBER (productividad de trabajadores nuevos) + WEF Future of Jobs —
estudios enfocados en empleabilidad individual, no en negocios. Para CH-014 (dueños de
empresa, venta), se usaron en su lugar:

- **U.S. Chamber of Commerce — Empowering Small Business Report (2025)**: 58% de los pequeños
  negocios en EE.UU. ya usa IA generativa (vs. 40% en 2024).
- **Salesforce — SMB Trends Report (2025)**, encuesta ago-sep 2024, 3,350 respuestas: 91% de
  los pequeños negocios que ya usan IA reporta un aumento medible en sus ingresos; 77%
  prioriza marketing y atención al cliente como su área de aplicación de IA.

## Equipo asignado

- **Coordinación / PR & Partnerships**: Carolain Fernández.
- **Facilitación**: Equipo INTEZIA Fundación (sin nombre propio en el deck, mismo criterio
  que CH-008 y el resto del sistema — §4.10a).

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh city-of-doral
python3 scripts/customize-acroforms.py city-of-doral
python3 scripts/customize-city-of-doral.py "clientes/propuestas/city-of-doral/<PDF generado>.pdf"
```

## Pendientes

- Confirmar fecha y plataforma de registro con City of Doral.
- Confirmar contacto/cargo de referencia en City of Doral.
- Confirmar si Carolain tiene teléfono para agregar más adelante (por ahora, el cierre queda
  solo con correo).
