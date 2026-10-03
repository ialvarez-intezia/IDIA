# Brief — Venezolano de Crédito · Asesoría Gerencia (CAI-020)

## Datos administrativos

- **Empresa**: Venezolano de Crédito
- **Sector**: Banca — Grande / Enterprise (más de 250 empleados)
- **Slug**: `venezolano-de-credito-gerencia` (deliberadamente distinto de `venezolano-de-credito/`,
  que es CAI-018 para el equipo de Mercadeo — ver "Independencia de la propuesta" abajo)
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades` (por instrucción directa del usuario — ver nota abajo)
- **Tipo de documento**: Asesoría ejecutiva In-Company (`CAI-020`) · 4 sesiones de 2h · 8h
  totales · modalidad presencial.
- **Eje temático**: Validar el enfoque híbrido de gestión de IA del banco (ética, riesgo,
  seguridad, gobernanza, datos en la nube, acceso a modelos, licencias e infraestructura) para
  Andrés Pereira, Gerente de Inteligencia Artificial y Analítica de Datos.
- **Fecha del brief**: 2026-09-16
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de un mensaje directo del cliente (Andrés Pereira, vía
correo, retomado por el usuario el 2026-09-16), sin ficha de levantamiento formal. Cita
textual completa:

> *"Asesoría para la Gerencia. Retomando tu ofrecimiento de acompañarnos en ética, riesgo,
> seguridad y gobernanza, nos interesa sumar una asesoría dirigida a mí como responsable del
> área, para validar el enfoque con el que estamos organizando la gestión de la IA en el
> Banco, estrategia híbrida con prioridad en las buenas prácticas de procesamiento de datos
> en la nube (estamos realizando una DEMO con el equipo de Google para incorporar Gemini
> Enterprise como estándar empresarial para la institución), acceso centralizado a los
> modelos, control de uso y de licencias, y la infraestructura necesaria para sostenerlo.
> ¿Podrían incluirla en la propuesta revisada, con su alcance, formato y costo? Cabe destacar
> que esta propuesta es totalmente independiente a la de Mercadeo."*

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
  (misma asesora que CAI-018).
- **Contacto y único participante**: Andrés Pereira · Gerente de Inteligencia Artificial y
  Analítica de Datos · responsable del área, decisor y participante de la asesoría.

## Por qué "servicio: habilidades" y no "Políticas" (decisión explícita del usuario)

Temáticamente, esta asesoría (ética, riesgo, seguridad, gobernanza) calza con el servicio de
**Políticas**. Sin embargo, `empresa/tipos-de-documento.md §0` mantiene ese servicio
**bloqueado**: "Sigue pendiente solo la decisión de formato de la propuesta comercial (Ivana +
David: ¿deck o informe de consultoría?)... No construir la estructura de la propuesta hasta
que esa decisión de formato se resuelva." El usuario indicó explícitamente usar **Habilidades**
para esta asesoría, con una salvedad clave: **"no se construye sino que se trabaja sobre estos
puntos"** — es decir, sin el patrón de "artefacto por sesión" que sí tiene CAI-018 (Mercadeo).
Esto convierte el formato en una **asesoría ejecutiva 1:1**, no una capacitación de equipo.

## Independencia de la propuesta (instrucción explícita del cliente)

El cliente fue explícito: *"esta propuesta es totalmente independiente a la de Mercadeo"*
(CAI-018). Por eso:
- Slug y código distintos (`venezolano-de-credito-gerencia/`, CAI-020 vs. CAI-018).
- El deck es autocontenido: no depende de CAI-018 para tener sentido, aunque comparte cliente,
  asesora comercial y el mismo contacto (Andrés Pereira) que en CAI-018.
- **Antes de clonar, se verificó explícitamente con `ls` que el slug no existiera** (lección
  del incidente de sobrescritura en `robin-agency/`, 2026-09-16, mismo día).

## Decisiones de diseño (sin ficha formal, tomadas por el consultor)

1. **4 sesiones de 2h (8h totales)** — confirmado con el usuario vía pregunta directa (no hay
   lineamiento de horas para asesoría ejecutiva 1:1; el lineamiento de Habilidades está
   pensado para entrenar equipos con artefacto por sesión, no aplica igual aquí). El usuario
   eligió la opción de mayor alcance entre las 3 presentadas (2, 3 o 4 sesiones).
2. **Modalidad presencial** — sin instrucción explícita del cliente para esta asesoría en
   particular; se asumió por continuidad con el patrón ya establecido del mismo contacto en
   CAI-018 (modalidad presencial explícita en su ficha original). Confirmar con el cliente si
   prefiere modalidad virtual dado que es una asesoría 1:1, no una sesión grupal.
3. **3 módulos / 4 sesiones**, agrupando los 5 temas que trajo el cliente:
   - Módulo I (1 sesión): Ética, Riesgo, Seguridad y Gobernanza — los 4 temas de gobernanza
     agrupados en una sola sesión, dado que están estrechamente relacionados.
   - Módulo II (2 sesiones): Estrategia Híbrida de Datos y Modelos — sesión 2 (datos en la
     nube + contexto de Gemini Enterprise) y sesión 3 (acceso centralizado a modelos + control
     de licencias).
   - Módulo III (1 sesión): Infraestructura y Cierre — infraestructura necesaria +
     recomendaciones consolidadas de las 4 sesiones.
4. **Sin Certificado de participación tradicional**: para una asesoría ejecutiva 1:1 con un
   Gerente, un "certificado de participación" institucional se sentía fuera de lugar (encaja
   para capacitaciones de equipo, no para una asesoría entre pares). El entregable insignia es
   un **memo ejecutivo de recomendaciones consolidadas**, más apropiado al formato. Decisión de
   diseño propia, no instrucción explícita del usuario — reversible si se prefiere mantener el
   certificado por convención de Habilidades.
5. **Neutralidad total sobre Gemini Enterprise (§4.11 y Metodología ABR)**: el banco está en
   DEMO con Google para evaluar Gemini Enterprise como estándar empresarial — esto se menciona
   en el deck **solo como contexto** de una evaluación que el banco ya tiene en curso, nunca
   como recomendación de Intezia ni como adopción decidida. La asesoría valida el **enfoque**
   (gobernanza, datos, acceso, licencias, infraestructura), no la marca. Esto es
   estructuralmente distinto de CAI-018, donde Claude ya está decidido por el cliente y se
   nombra con confianza — aquí Gemini Enterprise sigue en evaluación, se trata con más cautela.
6. **Sin descuento AJE**: CAI-018 lleva un descuento del 10% por membresía AJE (instrucción
   específica de esa propuesta). No se asume aquí sin instrucción explícita — el campo
   `Descuento` queda vacío, sin etiqueta adicional.

## Impacto (§4.9) — datos reales verificados por WebSearch

- **EY — Encuesta de IA Responsable en Banca (mayo 2025)**: 52% de los bancos cita la
  gobernanza como su principal reto en la adopción de IA; 44% invierte en tecnología para una
  adopción ética.
- **Deloitte — encuesta global a 3.235 líderes de tecnología en 24 países (2025)**: solo 21%
  de las organizaciones tiene un modelo de gobernanza maduro para agentes de IA autónomos,
  mientras 74% espera usar agentes de IA al menos de forma moderada para 2027.

Ambos datos conectan directo con el eje de esta asesoría: la brecha entre qué tan rápido
escala la adopción de IA y qué tan madura está su gobernanza — exactamente lo que el banco
pide validar antes de escalar.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education (perfil de ética/riesgo/seguridad/gobernanza de
  IA aplicada a banca).
- **Asesora comercial**: Flavia Martínez.

## Pendientes

- Confirmar modalidad (presencial asumido por continuidad, no confirmado explícitamente para
  esta asesoría específica).
- Confirmar fechas de las 4 sesiones con Andrés Pereira.
- Confirmar presupuesto y monto de la cotización (campos de precio vacíos, los llena ventas).
- Confirmar si se mantiene la decisión de omitir el certificado de participación tradicional.
