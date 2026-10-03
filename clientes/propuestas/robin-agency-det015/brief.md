# Brief — Robin Agency (DET-015)

---

## Datos administrativos

- **Empresa**: Robin Agency (agencia de publicidad)
- **Sector**: Publicidad
- **Tamaño**: Mediana (50-250 empleados)
- **Slug**: `robin-agency-det015` (slug deliberadamente distinto de `robin-agency/`, ver
  "Nota sobre carpetas de este cliente" al final)
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Tipo de documento**: Detección (`DET-015`) · 4 sesiones de 2h (Fundamentos, Detección,
  Construcción, Adopción) · 8h totales, modalidad presencial.
- **Eje temático**: Llevar el uso suelto y sin criterio de IA en Talento Humano a una
  adopción con método, confirmando si Claude es el ecosistema indicado para reclutamiento,
  compensación y desempeño.
- **Fecha del brief**: 2026-09-16
- **Alianza**: no

## Ajuste 2026-09-18 — reestructuración a 4 sesiones (Fundamentos → Detección → Construcción → Adopción)

Instrucción directa del usuario: se abandona el esquema anterior (Fundamentals 2h + "Trabajo
por Área" 4h con logro inmediato incluido, 6h totales) por uno de **4 sesiones de 2h cada
una, 8h totales**:

1. **Fundamentos (2h)**: qué es la IA, prompting, y el vocabulario de Artefacto, Skill y
   Proyecto (los 3 tipos de entregable que Construcción puede producir). Los primeros pasos
   con Claude (pedido explícito del cliente, ver punto 4 más abajo) se practican aquí, dentro
   del bloque de prompting.
2. **Detección (2h)**: auditoría y diagnóstico de los procesos reales del área. **Sin logro
   inmediato** — instrucción explícita del usuario: esta sesión ya no compromete una
   construcción a mitad de la auditoría, para no mezclar el rol de "auditar" con el de
   "construir".
3. **Construcción (2h)**: se construye a partir de lo detectado en la sesión anterior.
   **Logros tangibles** — aquí es donde ahora vive el logro que antes estaba dentro de la
   sesión de Detección (ejemplo ilustrativo: la skill que lee currículums y arroja los
   mejores candidatos, ligada a Reclutamiento y Selección — ver punto 6 de la sección
   "Decisiones confirmadas" abajo, reubicado de Detección a Construcción).
4. **Adopción (2h)**: se capacita al equipo en el uso y gestión de lo construido en la
   sesión anterior. Cierra con el Reporte Final (Índice de Madurez + recomendación de
   ecosistema de IA + retorno de inversión estimado) — mismos 3 componentes que ya pedía el
   cliente (punto 5 de "Decisiones confirmadas"), ahora entregados al cierre de Adopción en
   vez de en una fase de "Reporte Final" separada sin sesión con el cliente.

**Recomendación de cadencia (instrucción directa del usuario, reflejada en Próximos
pasos)**: 2 sesiones por semana, o dejar al menos 2 días de por medio entre las sesiones 2
(Detección) y 3 (Construcción) — ese espacio es lo que reemplaza la antigua fase interna de
"Priorización" (Mapa de Calor): Intezia usa esos días para consolidar los hallazgos de
Detección y decidir qué construir en la sesión 3, sin necesitar una sesión propia con el
cliente para eso.

**Roadmap dividido en 2 slides** (2 etapas + resultado cada una, mismo patrón ya usado en
`simple-tv-all002/`/`maurel-prom/` para planes de varias fases) en vez de 1 sola slide de 3
etapas: cablear 4 etapas + resultado en una sola fila de `.rmx-linear` habría exigido un 4º
color de nodo que no existe en la paleta de marca (§4.1: solo amarillo/naranja/blanco/negro,
ya usados por las etapas 1-3 del roadmap anterior) y habría angostado las cards por debajo
del ancho ya usado con texto de longitud similar — se prefirió reutilizar el patrón de 2
roadmaps de 2 etapas, ya probado sin desborde.

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Robin Agency**
(`Levantamiento_Robin_Agency_2026-09-16.pdf`, registro 2026-09-15), elaborada por la asesora
**Flavia Martínez**.

## Contacto

- **Asesora comercial**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
- **Contacto cliente**: María Silva · Directora de Talento Humano · mmoser@robin-agency.com —
  única stakeholder identificada, firma y decide la contratación directamente.
- **Servicio previo con Intezia**: ninguno — primer contacto.
- **¿Hubo una propuesta previa sin aprobar?**: Sí — un proyecto que abarcaba 3 departamentos
  (medios digitales, cuentas, talento), enfocado en Habilidades, rechazado por presupuesto y
  porque el enfoque cambió (se había estructurado antes del esquema actual de servicios). **No
  se menciona en el deck de cara al cliente** (evitar reabrir una propuesta rechazada); queda
  aquí solo como contexto de por qué ahora se aborda con Detección y un alcance más puntual
  (1 área) en vez de un proyecto de Habilidades multi-departamental.

## Área a auditar (1 — dato directo de la ficha, sin ambigüedad)

**Talento Humano**, 4 a 6 personas, responsable María Silva (Directora del área).

## Decisiones confirmadas / sin ambigüedad

1. **1 área** (Talento Humano) — la ficha lo declara directo. No se necesitó preguntar
   alcance ni headcount (rango de 4-6 personas ya es preciso).
2. **4 sesiones de 2h cada una** (Fundamentos, Detección, Construcción, Adopción), mismas 4-6
   personas en las 4 sesiones (dentro del máximo de 25 del lineamiento) = **8h totales**
   (ajuste 2026-09-18, instrucción directa del usuario — ver sección propia arriba).
3. **Modalidad presencial**, en las oficinas de Robin Agency — dato explícito de la ficha,
   sin sedes adicionales.
4. **Herramienta — Claude, mencionado con confianza pero no como decisión cerrada.** A
   diferencia de otras Detecciones (Gemini/Claude como contexto informal apenas mencionado),
   aquí el cliente es explícito y detallado: *"cuál herramienta es la indicada para sus
   procesos (que probablemente sea Claude pero ellos aún no tienen las licencias corporativas
   adquiridas)... que se les dé el AI Fundamentals en base a esa herramienta"*. La propia
   directora de Talento ya usa Claude con licencia personal. Decisión de diseño: se nombra
   **Claude explícitamente** en Fundamentals (uno de los 4 temas: "Primeros pasos con
   Claude") y en Beneficios/Notas, pero el Reporte Final sigue enmarcado como **confirmación**
   ("recomendación de ecosistema de IA, a confirmar con los hallazgos"), no como una decisión
   ya tomada por Intezia — la Metodología ABR se respeta porque es el **cliente** quien ya
   lidera hacia Claude y pide ayuda para validarlo, no Intezia recomendándolo a ciegas.
5. **Retorno de inversión (ROI) en el Reporte Final**: pedido explícito del cliente
   ("Objetivo final que el cliente espera del Reporte Final: mostrar los resultados
   obtenidos, el índice de madurez y el retorno de inversión"). Se agregó como tercer
   entregable del Reporte Final junto al Índice de Madurez y la recomendación de ecosistema,
   en Objetivos, Programa, Roadmap y Beneficios.
6. **Quick win**: la ficha no lo tiene mapeado con certeza, pero flota una idea concreta: una
   skill/agente que lea currículums y arroje los mejores candidatos (ligada al Proceso 1,
   Reclutamiento y Selección). **Reubicado a la sesión de Construcción** (ajuste
   2026-09-18) — ya no es un "logro inmediato" dentro de Detección, sino el ejemplo
   ilustrativo de lo que se construye en la sesión 3, a partir de lo detectado en la sesión
   2. Se deja claro que se termina de definir en la sesión (no se compromete como entregable
   cerrado).
7. **Sin Certificado de participación INTEZIA** en Entregables ni en Programa — Detección
   pura, auditoría no curso. Ver memoria `deteccion-sin-certificado.md`.
8. **Sin slide de Mapa de Calor** — mismo criterio que el resto de las Detecciones recientes.

## Necesidad detectada

Objetivo y necesidad central citado en la ficha: *"Desean automatizar todas las tareas y
procesos manuales que realiza el equipo de talento, desde crear un agente o un proyecto para
el tema de reclutamiento de personal, modelos de análisis de compensación, estructura de
métricas de desempeño, hasta sistematizar todos los procesos en una herramienta... a pesar de
que tienen muchos procesos mapeados y regulados por ISO, desean tener esa ruta de adopción y
mapa de prioridades para saber qué abordar y cómo hacerlo."*

**3 procesos específicos (Bloque C)**, todos ya mapeados y regulados por ISO pero ejecutados
de forma manual:

1. **Reclutamiento y selección** — mensual, dato público. Candidato a logro inmediato (ver
   punto 6 arriba).
2. **Modelos de análisis de compensación** — semanal.
3. **Estructura de métricas de desempeño** — semanal.

## Stack tecnológico (contexto interno, no se afirma migración — §4.11)

- **Ecosistema**: Google Workspace.
- **Información del negocio**: mezcla de sistemas y hojas de cálculo.
- **Comunicación**: WhatsApp y Google Workspace.
- **Uso de IA hoy**: Gemini disponible por el ecosistema Google, uso informal. La directora
  de Talento usa Claude con licencia personal, "maneja lo muy básico". Sin política de
  datos/seguridad ni regulación sectorial declarada (más allá del ISO ya mencionado, que
  regula los procesos, no el uso de IA en sí).

## Universo y modalidad

- **4 a 6 personas** en el alcance, mismo grupo para auditoría y Fundamentals.
- **1 sesión grupal** para el área + Fundamentals grupal, ambas con la misma gente.
- **Modalidad**: Presencial, en las oficinas de Robin Agency. Sin sedes adicionales.
- **Nivel de partida con IA**: "de forma suelta y sin criterio". Sin formación previa.
- **Presupuesto**: en evaluación. **Apertura al cambio**: Alta. **Patrocinio ejecutivo**:
  fuerte y visible (María Silva).
- **Urgencia**: ninguna declarada como evento disparador, pero horizonte de corto plazo
  (0-3 meses) para incorporar IA.
- **Quién decide**: María Silva firma y decide directamente — es la única stakeholder.
- **Expectativa de Índice de Madurez**: el cliente quiere que el equipo "pase de 0 a 100 en
  la adopción" y que el resto de la organización se impresione con los resultados, para que
  esto se replique en otras áreas — señal de que Robin Agency ve esta Detección como un
  piloto/vitrina interna.
- **Criterio de éxito del cliente** ("qué haría que dijeran esto es exactamente lo que
  necesitábamos"): que el equipo entienda a usar la herramienta de forma autónoma y sepa
  resolver los cuellos de botella básicos que hoy le quitan tiempo.

## Hacia dónde va esto (contexto, no cotizado en este documento)

Bloque F (observaciones internas, Flavia Martínez): el cliente mostró mucho interés en el
**clon digital**, pero la asesora lo ve más apto para una fase 2 o 3, no para esta Detección.
Se menciona solo como nota interna/pendiente, no cotizado ni prometido en el deck.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Flavia Martínez.

## Notas internas

- Caso base estructural original (previo al ajuste 2026-09-18): `toyocentro/` (DET-014) —
  patrón de 4h por área con logro inmediato incluido. **Ya no aplica tras la
  reestructuración a 4 sesiones de 2h** (Fundamentos → Detección → Construcción →
  Adopción) — ver sección "Ajuste 2026-09-18" arriba. El nuevo roadmap de 2 slides (2 etapas
  + resultado cada una) sigue el patrón de `simple-tv-all002/`/`maurel-prom/`.
- Impacto (§4.9): SHRM — 2025 Talent Trends (43% de profesionales de RR.HH. ya usa IA en sus
  tareas, arriba de 26% en 2024; 51% de organizaciones usa IA para reclutamiento; 82% de
  quienes usan IA en contratación la aplican a revisión de currículos — conecta directo con
  el quick win de reclutamiento) + ITIF (mayo 2025, usuarios frecuentes de IA generativa
  ahorran 4+ horas semanales — conecta con el objetivo explícito del cliente de "optimizar
  tiempo y dejar de tener tanta carga operativa"). Ambos verificados por WebSearch.

## Nota sobre carpetas de este cliente (evitar futuras colisiones)

Robin Agency ya tiene **dos** carpetas previas en el sistema:
- `clientes/propuestas/robin-agency/` — CAP-032 (mayo/junio 2026). **Incidente 2026-09-16**:
  al construir esta propuesta DET-015 se clonó por error hacia ese slug (ya existente),
  sobrescribiendo `brief.md`, `index.html`, `programa.md`, `overrides.css`, `acroforms.json` y
  `meta.json` originales de CAP-032 con contenido de otro cliente (Toyocentro DET-014). El
  usuario confirmó que CAP-032 "ya no se usa" — no se reconstruyó. Los archivos contaminados
  se eliminaron; solo sobreviven `CAP-032 Robin Agency.pdf` (PDF final, con AcroForm vivo) y
  el `styles.css` legacy original de ese deck.
- `clientes/propuestas/robin-agency-cap080/` — CAP-080 (julio 2026), intacta, no relacionada
  con este incidente.
- **Esta propuesta (DET-015) vive en `robin-agency-det015/`**, deliberadamente con sufijo de
  código, siguiendo el mismo patrón ya usado para CAP-080. **Antes de clonar hacia cualquier
  slug de `clientes/propuestas/<slug>/`, verificar primero con `ls` que la carpeta no exista.**
