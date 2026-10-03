# Brief — IESA · Maestría en Gestión de Sistemas Autónomos (alianza académica)

## Datos administrativos

- **Empresa / Institución**: IESA (Instituto de Estudios Superiores de Administración).
- **Slug**: `iesa-maestria`
- **División Intezia**: `educacion`
- **Tipo de documento**: Propuesta de alianza académica — **bespoke**, no clasifica en el
  catálogo estándar (§4.2: charla/taller/curso/diplomado). Es una propuesta de socio
  institucional, hermana de `iesa-especializacion-tecnica/` (misma estructura de 12 slides,
  mismo modelo de micro-credenciales). **Sin código de catálogo** (no CAP/TA/CU/DIP).

## Contacto

- Datos institucionales genéricos de Intezia en el cierre (correo, web), igual que en el
  resto de las propuestas de alianza IESA.

## Origen

Re-planteamiento de la alianza IESA × Intezia para la Maestría en Gestión de Sistemas
Autónomos. El modelo original (Intezia como socio directo del programa de postgrado) no
encajaba en la estructura de costos institucional del IESA; el nuevo modelo reagrupa el
pensum ya aprobado en **cinco micro-credenciales ejecutivas** vendibles por separado, cuya
suma otorga el grado de Magíster.

- 34 UC · 544h · 4 trimestres · 26 componentes académicos
- 3 certificaciones intermedias ya nombradas en la malla (Trimestres I, II, III) + un cierre
  de Trabajo de Grado (Trimestre IV) que otorga el grado final.

## Fuentes usadas

1. `Malla Curricular INTEZIA - IESA - Maestría.pdf` — pensum completo (asignaturas,
   descripciones, objetivos de aprendizaje, herramientas, UC/horas por trimestre). Fuente de
   verdad para el contenido curricular de las cinco micro-credenciales.
2. `Propuesta_IESA_Intezia (MIA).pdf` (v4) — propuesta ya redactada con la estructura, el
   diagnóstico, las tres vías evaluadas, el esquema legal y el modelo económico. Es la fuente
   de contenido principal de este deck: se porta a la plantilla HTML/CSS de marca Intezia
   (mismo esqueleto bespoke de `iesa-especializacion-tecnica/`), no se rediseña desde cero.

## Decisiones tomadas con el usuario (2026-08-24)

- **Duración del contrato — inconsistencia en la fuente**: el PDF v4 se contradice: la
  portada dice "contrato de servicio de cinco años renovable por KPIs", pero Objetivos y
  Esquema Legal dicen "diez años + renovación automática por cinco años". El usuario decidió
  **no fijar la cifra**: el deck deja la vigencia y las condiciones de renovación como **"a
  confirmar en la mesa de validación financiera"** en toda mención (portada, objetivos,
  esquema legal), sin comprometerse a 5 ni a 10 años hasta que IESA lo valide.
- **Fechas de calendario vencidas**: el PDF v4 traía fechas ya pasadas para el momento de
  esta entrega (apertura de preventa 15 junio 2026, inicio de clases 7 julio 2026 — hoy es
  2026-08-24). El usuario decidió **omitir las fechas concretas** (§ regla de "omitir, no
  inventar placeholder"): el deck usa solo plazos relativos (14 días desde NDA, 30 días desde
  paso 01) y deja el lanzamiento de la MC1 sujeto al calendario académico de IESA, sin fecha
  fija.
- **Narrativa interna del diagnóstico**: el PDF v4 nombraba personas reales (dos
  responsables de la negociación), una conversación fechada y una cifra de negociación previa
  (35% de participación en el modelo descartado). El usuario decidió **generalizar**: el
  diagnóstico queda en términos institucionales (IESA e Intezia, sin nombres propios, sin
  fecha de conversación ni la cifra del 35%), igual que se hizo en `iesa-especializacion-tecnica/`.
- **Micro-credenciales**: **5 MC**, mapeadas 1:1 con las certificaciones intermedias ya
  nombradas en la malla + Trimestre II dividido en dos MC (II A / II B) tal como lo define el
  PDF v4 (MC2 = asignaturas de gestión/gobernanza responsables IESA, MC3 = arquitectura de
  agentes responsable Intezia).
- **Modelo económico**: mismo estándar vigente en otras alianzas Intezia — reparto 50/50
  post-gastos (Vía 3, recomendada) y anclas de tarifa $32/$50/$100 por hora-clase (Vía 2,
  complementaria) — cifras ya reales y vigentes, tal como las trae el PDF v4.
- **Formato de salida**: HTML/PDF bespoke replicando el estilo visual de la propuesta
  hermana `iesa-especializacion-tecnica/` (no el patrón canónico de AcroForms de
  talleres/cursos). "Próximos pasos" (no "Cómo arrancamos" — ese texto literal dispara la
  inyección de AcroForms de precio en `agregar-campo-precio.py`, ver
  `plantillas/slides/README.md` y memoria `propuesta-alianza-bespoke-sin-acroforms`).
- **Generación de PDF**: el usuario pidió generar el PDF de inmediato con
  `./scripts/generar-pdf.sh iesa-maestria`, lo que marca automáticamente el `meta.json` como
  `"Enviada"` (§4.19).

## Mapeo académico → micro-credenciales

| MC | Nombre comercial | Certificación / grado | Trimestre | UC | Horas | Responsable |
|---|---|---|---|---|---|---|
| 1 | Estrategia y Economía de la IA | Cert. Ejecutiva en Estrategia y Economía de la IA | I | 8 | 128h | IESA + Intezia |
| 2 | Liderazgo, Gobernanza y Cumplimiento | Cert. en Liderazgo Organizacional y Gobernanza de IA | II A | 4 | 64h | IESA |
| 3 | Arquitectura de Agentes y Automatización | (complemento operativo, eje Intezia) | II B | 6 | 96h | Intezia |
| 4 | Operaciones, Analítica y Viabilidad Financiera | Cert. en Dirección de Operaciones y Viabilidad Financiera | III | 10 | 160h | IESA + Intezia |
| 5 | Consultoría Aplicada y Trabajo de Grado | Magíster en Gestión de Sistemas Autónomos (grado final) | IV | 6 | 96h | IESA + Intezia |
| ∑ | — | Título de Magíster al completar las cinco MC | — | 34 | 544h | — |

Detalle de asignaturas por MC en `programa.md`.

## Pendiente (no se fija en el deck sin validar con IESA)

- Vigencia final del contrato de servicio (5 vs. 10 años — inconsistencia de la fuente, sin
  resolver) y sus condiciones de renovación.
- Cifras finales del reparto económico por MC (Vía 3) y tarifa de hora-clase (Vía 2).
- KPIs de renovación específicos (el deck presenta categorías propuestas, no compromisos
  cerrados).
- Fecha de lanzamiento de la primera cohorte (MC1) — sujeta al calendario académico de IESA.
