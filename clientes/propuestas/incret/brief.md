# Brief — INCRET · Fundamentos y Gemas con Gemini (CH-011)

## Corrección de código (resuelta con el usuario)

El usuario pidió originalmente el código `CAI-009` para esta propuesta, pero también la
describió como "una charla". Por catálogo (`empresa/catalogo.md#charlas`), las Charlas usan
la serie `CH-###`, no `CAI-###` (esa serie es de Capacitación In-Company). `CAI-009` está
libre, pero `CH-009` y `CH-010` ya están tomados (Venemergencia y DUSA respectivamente). Se
preguntó al usuario y se confirmó: **Charla → código corregido a `CH-011`** (siguiente
correlativo libre de la serie).

## Instrucción original del usuario

- Cliente: INCRET.
- Asesor comercial: Diego.
- Es una **alianza** → **sin hoja de cotización** en el deck.
- Charla de **3 horas**, de fundamentos hasta lograr construir **Gemas (Gems) con Gemini**.

## Datos administrativos

- **Cliente**: INCRET — empresa (confirmado por el usuario).
- **Slug**: `incret`
- **División Intezia**: `educacion` (confirmado por el usuario — cliente corporativo)
- **Servicio** (Modelo Intezia): `habilidades` (toda Charla cae bajo Habilidades, §1 Identidad
  — categorías curriculares: Charla, Curso/Diplomado, Taller/Capacitación In-Company)
- **Alianza**: sí
- **Código**: `CH-011`
- **Eje temático**: de los fundamentos de Gemini a la construcción de Gemas (Gems) propias
- **Fecha del brief**: 2026-09-03
- **Estado**: `Borrador`

## Contacto

- **Asesor comercial Intezia**: Diego Pérez, Director de Talento Humano (cargo confirmado por
  el usuario 2026-09-03). Sin teléfono. Sin correo — no fue suministrado, no se inventa (ver
  memoria `omitir-no-inventar-placeholder`). En el bloque de contacto del Cierre aparece solo
  su nombre y cargo, sin la etiqueta "Asesor de ventas" (instrucción del usuario).
- **Cliente / interlocutor**: no se suministró un contacto individual de INCRET — el deck se
  refiere a "el equipo administrativo de INCRET".

## Alcance pedido por el cliente

- Charla de **3 horas**, sesión única (no multi-sesión).
- Audiencia: **aproximadamente 4 personas**, del área **administrativa** de INCRET. Sin más
  detalle de perfil — se mantiene genérico ("equipo administrativo"), sin inventar roles o
  procesos específicos que el usuario no dio.
- Arco de contenido: de **fundamentals** (fundamentos de Gemini) hasta lograr **construir
  Gemas (Gems)** — la función de Gemini para crear asistentes personalizados.
- **Alianza**: sí. **Sin hoja de cotización** — instrucción directa del usuario, se omite la
  slide de Propuesta Económica (y con ella, no se agregan campos de precio al PDF).
- **Logo de INCRET**: no suministrado — el deck lleva solo el logo de Intezia, sin co-marca
  (a diferencia de RUSH Academy, TA-034, donde sí hubo logo del aliado). Si más adelante se
  suministra, se puede incorporar co-marca siguiendo el precedente de `rush-academy/`.
- **Modalidad**: no especificada por el usuario — se deja "a definir en la próxima reunión"
  (mismo criterio que Aerocentro CAI-008), sin asumir Presencial u Online.

## Curriculum (3 bloques, 3h, sesión única)

1. **Bloque I · Fundamentos de Gemini** (60'): qué es la herramienta y cómo funciona,
   anatomía de un buen prompt, primeros resultados con casos reales.
2. **Bloque II · Prompting efectivo** (60'): instrucciones claras con contexto, casos
   administrativos de INCRET, errores comunes al empezar.
3. **Bloque III · Construcción de Gemas** (60'): qué es una Gema (Gem) y para qué sirve,
   construcción guiada de una Gema propia, plan de continuidad.

Cada bloque cierra con un logro concreto aplicado (patrón "Fundamentals con logros
inmediatos"), consistente con el resto del sistema para capacitaciones introductorias.

## Restricciones de copy

1. **Sin nombres propios de personas del lado de INCRET** — el deck se refiere a "el equipo
   administrativo de INCRET". El nombre de Diego (asesor) sí aparece en el bloque de contacto
   del Cierre, sin cargo ni teléfono (instrucción del usuario) y sin correo (no suministrado).
2. **Sin hoja de cotización ni montos** en el deck (alianza, instrucción directa + §4.15).
3. **Sin logo de INCRET** — no suministrado, no se inventa ni se usa un logo genérico.
4. **"Gema" / "Gem"**: término nativo de Gemini (función de asistentes personalizados) — se
   usa "Gema" en el copy general y se aclara "(Gem)" en su primera aparición por slide donde
   corresponde, mismo criterio que "Skill"/"Project"/"Artifact" para Claude (§4.4, §4.12).

## Notas de diseño

- Clonado de `aerocentro-cai008/` (mismo Beneficios v3 + Cierre escalera, esquema
  2026-08-26: sin Metodología ABR, sin Equipo facilitador). Adaptado a formato **Charla**:
  - **Sesión única** (patrón `fivenca-claude-express/`: `.ruta` con 1 solo nodo, `ruta-fill`
    al 100%, label "Sesión única"), no 3 slides de cronograma como en Aerocentro/Ferrara —
    los 3 bloques viven en la MISMA sesión de 3h, no en sesiones separadas.
  - **Sin slide de Propuesta Económica**: la alianza no cotiza en este documento. 9 slides en
    total (vs. 12 en el patrón Capacitación estándar): Portada, Diagnóstico, Objetivos,
    Programa, Cronograma (única), Beneficios, Impacto, Próximos pasos, Cierre.
  - `plantillas/diseno-charla.md` rige el documento curricular interno (`programa.md`):
    sin código de programa dentro del documento, sin módulos formales, una sola tabla de
    contenido. El deck visual (`index.html`) sí usa el sistema estándar de tarjetas de
    Programa (por consistencia visual con el resto del sistema) — mismo criterio ya usado en
    el precedente `doral-comunidad-sfic/` (CH-008).
- **Beneficios (Habilidades)**: formato v3 — Resultados / Por qué Habilidades / Entregables /
  Valor inmediato. Entregables incluye certificado de participación (capacitación real,
  aunque corta).
- **Impacto (§4.9)**: se reutilizan las fuentes reales ya verificadas esta semana (Stanford
  HAI AI Index Report 2026, McKinsey The State of AI 2025, Anthropic Economic Index 2025) —
  mismo fenómeno de fondo (equipo sin dominio de una herramienta de IA, adopción dispareja).
- **§4.11**: no se afirma que INCRET migra o adopta un nuevo stack — Gemini se presenta como
  la herramienta que el equipo aprende a usar.
- **Correo de cierre**: `servicio@intezia.com` (estándar).

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh incret
python3 scripts/customize-acroforms.py incret
python3 scripts/customize-incret.py "clientes/propuestas/incret/<PDF generado>.pdf"
```

## Pendientes

- Confirmar modalidad (Presencial / Online Síncrono / Híbrido) en la próxima reunión.
- Confirmar fecha y horario de la sesión con el grupo de ~4 personas.
- Confirmar correo de Diego Pérez si se quiere completar su ficha de contacto (opcional —
  el deck funciona igual sin él).
- Confirmar si más adelante INCRET suministra un logo para agregar co-marca.
