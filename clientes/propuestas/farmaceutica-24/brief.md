# Brief — Farmacéutica 24

---

## Datos administrativos

- **Empresa**: Farmacéutica 24 C.A
- **Sector**: Farmacéutica
- **Tamaño**: Mediana (50-250 empleados)
- **Slug**: `farmaceutica-24`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Tipo de documento**: Detección (`DET-010`) · Fundamentals (2h grupal) + auditoría de 10
  áreas, 4 horas por área (42h totales), modalidad mixta.
- **Eje temático**: Unificar el manejo de indicadores entre las 10 áreas, con un logro
  inmediato por área y recomendación preliminar de ecosistema de IA (Claude).
- **Fecha del brief**: 2026-09-09
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Farmacéutica 24**
(`Levantamiento_Farmaceutica_24_2026-09-08.pdf`, reunión del 2026-09-08), elaborada por la
asesora **Verónica Rubio**.

## Contacto

- **Asesora comercial**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Contacto cliente**: Jesús Mora · Gerente de Tecnología
- **Servicio previo con Intezia**: ninguno — primer contacto

## Áreas a auditar (10, confirmadas con el usuario 2026-09-09)

La ficha lista 10 áreas en el Bloque A (Datos generales) y luego, en el Bloque específico de
Detección, las vuelve a listar dividiendo "Operaciones y Flota" en dos y agregando
"Almacenamiento" (12 en total). **El usuario contó y confirmó 10 áreas** — se usa la lista del
Bloque A, sin dividir Operaciones/Flota ni agregar Almacenamiento como área aparte:

1. Ventas
2. Compras
3. Mercadeo
4. Cuentas por Cobrar
5. Cuentas por Pagar
6. Tesorería
7. Operaciones y Flota
8. Infraestructura
9. Tecnología
10. Talento Humano

## Ajuste (2026-09-09) — sin certificado en Entregables

Corrección del usuario: los procesos de Detección son una auditoría, no un curso, y no llevan
Certificado de participación INTEZIA. Se retiró esa línea de `acroforms.json` → `Entregables`
y de `programa.md` §6. Regla general (no solo de este cliente): el certificado aplica cuando
el servicio incluye un componente real de Habilidades/capacitación con participación
(confirmado comparando `grupo-corpos/DET-009` y `everest/DET-006`, ambas Detección pura, sin
certificado, contra `yocoima/` y `grupo-ferrara/`, que sí lo llevan por tener un tronco de
Habilidades/Fundamentals dentro del mismo servicio).

## Decisiones confirmadas con el usuario (2026-09-09)

1. **10 áreas** (no 12) — ver arriba.
2. **4 horas de Detección por área** (40h) + **Fundamentals de 2h grupal**, antes de arrancar
   las sesiones de área, para los referentes de las 10 áreas (10 personas, muy por debajo del
   máximo de 25 del lineamiento de Detección — 1 sola sesión) = **42h totales**. Ajuste
   solicitado por el usuario en una segunda pasada (2026-09-09), para alinear DET-010 con el
   lineamiento estándar de Detección (`empresa/politicas-comerciales.md` → *Dimensionamiento
   por servicio*) que ya aplican `hoteles-cumberland/` DET-011 y otras Detecciones recientes.
3. **Logro inmediato en cada área**: cada una de las 10 sesiones de 4h no es solo diagnóstico
   — deja un artefacto aplicable de inmediato (ej. una plantilla o prompt reutilizable para la
   tarea más repetitiva del área), además de alimentar el Mapa de Calor y el Reporte Final.
4. **Recomendación de Claude, mención breve**: la ficha indica que el cliente "aún no sabe
   qué herramienta, espera la recomendación" — Jesús Mora (Gerente de Tecnología) ya usa
   Claude a título personal. Por instrucción del usuario, el deck menciona a Claude como
   recomendación preliminar en el roadmap (etapa de Reporte Final), sin contradecir la
   metodología ABR ("diagnóstico antes de recomendar"): se presenta como lectura inicial del
   contexto, a confirmar con los hallazgos reales de las 10 áreas.

## Necesidad detectada

Objetivo central citado (parafraseado de la ficha, cita larga y algo desordenada): Jesús Mora
busca mejorar el manejo de indicadores de la empresa — hoy muy desigual entre áreas
("a nivel comercial se manejan bastantes [indicadores], otras áreas todavía no") — y quiere
"acelerar ese tipo de cosas" con IA.

1. **Cobranza** (Cuentas por Cobrar): diaria, dato confidencial, ocupa el día completo del
   equipo dedicado. Señalado por el cliente como uno de los procesos con más fricción.
2. **Cuentas por Pagar y Tesorería** (conciliaciones bancarias): diaria, dato confidencial,
   ocupa el día completo. Cuello de botella: "todo el tema de bancos y conciliaciones."
3. **Indicadores dispares entre áreas**: Ventas ya los maneja bien; el resto no tiene ese
   hábito consolidado — es el hilo conductor de toda la propuesta (Índice de Madurez
   unificado).
4. **Uso de IA hoy**: solo en Tecnología — Jesús usa principalmente Claude; el equipo también
   usa DeepSeek, Copilot y Gemini, cambiando de herramienta según salen actualizaciones, sin
   gobernanza ni criterio común. El resto de la empresa no ha adoptado IA de forma
   consolidada.
5. **Sin política de datos**: no existe una política de seguridad de datos interna a nivel de
   empleados — relevante dado que Cobranza y Conciliaciones manejan información confidencial.

## Universo y modalidad

- **~60-70 administrativos + ~70-80 operativos** en total (empresa completa); el universo
  directamente involucrado en la Detección son los líderes/gerentes de las 10 áreas.
- **1 persona por área a entrevistar** (10 sesiones) + Fundamentals grupal para los 10
  referentes (dentro del máximo de 25 personas por sesión).
- **Modalidad**: Mixta (híbrida).
- **Nivel de partida con IA**: muy desigual entre áreas. Muy pocas personas (sobre todo
  líderes) han recibido algo de formación en IA, y no necesariamente la aplican.
- **Presupuesto**: no definido aún.
- **Apertura al cambio**: Media. **Patrocinio ejecutivo**: aún no asegurado.
- **Urgencia**: ninguna declarada — iniciativa exploratoria (scouting) impulsada por el
  Gerente de Tecnología, sin planificación formal todavía. El objetivo final se termina de
  definir con esta propuesta (confirmado en la ficha).
- **Quién decide**: los directores de la empresa junto con Jesús Mora.

## Hacia dónde va esto (contexto, no cotizado en este documento)

La ficha registra que el cliente ya piensa en fasear una capacitación posterior en 3 bloques:
comercial (ventas, compras, mercadeo) → financiera (cuentas por cobrar/pagar, tesorería) →
tecnología, como puerta de entrada a Habilidades. Este DET-010 **no cotiza esa fase** — el
Reporte Final la deja como recomendación, junto con la recomendación preliminar de Claude.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Notas internas

- Caso base estructural: `bidzi/` (roadmap `.rmx-linear` de 3 etapas + resultado, mismo
  criterio "auditar antes de recomendar").
- **Ajuste (2026-09-09)**: la slide de Mapa de Calor (tabla ilustrativa portada de
  `pilotes-perforados/`) se retiró por instrucción del usuario. "Mapa de Calor" sigue como
  nombre del entregable de la Etapa 2 del roadmap y en Beneficios/Entregables — solo sin una
  slide propia de tabla. Deck pasó de 12 a 11 slides, renumerado.
- **Ajuste (2026-09-09, segunda pasada)**: se agregó una sesión de Fundamentals (2h grupal)
  antes de las 10 sesiones de área, mismo patrón ya aplicado en `hoteles-cumberland/` DET-011.
  Se insertó una nueva slide de Cronograma · Fundamentals antes de la de Cronograma · Estructura
  por área. Deck pasó de 11 a 12 slides, renumerado. Módulo I de Programa se dividió en
  "Fundamentals" + "Trabajo por Área" (4 módulos en total, antes 3), y la Etapa 1 del roadmap
  pasó a llamarse "Fundamentals y Trabajo por Área". El primer texto de esa Etapa 1
  ("Los 10 referentes (Fundamentals) y un referente por área.") desbordó la slide del roadmap
  en +46px (detectado por `verificar-overflow.js`) — se acortó a "Los 10 referentes y un
  referente por área." (el tag de la etapa ya nombra Fundamentals, no hacía falta repetirlo).
- Impacto (§4.9): McKinsey — The State of AI, cómo las organizaciones se reorganizan para
  capturar valor (2025): 78% de organizaciones ya usa IA en alguna función, 63% de las que
  usan IA generativa no tiene gobernanza estructurada, solo 21% ha rediseñado sus flujos de
  trabajo antes de escalar IA. Encaja directo con el caso de Tecnología de Farmacéutica 24
  (uso disperso, sin gobernanza).
- Sin slide de Metodología ABR expuesta ni Equipo facilitador (§4.10a) — Beneficios v3,
  Cierre escalera, correo `servicio@intezia.com`.
