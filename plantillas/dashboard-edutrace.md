# Plantilla — Dashboard de Impacto Edu-Trace

> Diseño y lógica del **segundo flujo** del sistema: el reporte de cierre que convierte
> la Encuesta Edu-Trace de un cliente en un resultado medible. Paralelo al de propuestas.
> Mecánica de generación: `plantillas/generar-dashboard.md`. Flujo en `CLAUDE.md §11`.

> **Formato vigente desde 2026-10-26: 7 slides + video** (§5 y `plantillas/video-dashboard.md`). El
> ejemplo canónico es `encuestas-v2/dashboard-ejemplo/` y **reemplaza** al deck de 10 slides de
> `apb-group/`. Las secciones 2 y 3 describen la encuesta y el índice (0-100) del formato anterior;
> las del formato vigente están en 2b y 3b. Los dashboards ya entregados no se tocan.

---

## 1. Qué es

Cuando termina el proceso de un cliente (impartida la capacitación, respondida la encuesta
de cierre), se genera un **Dashboard de Impacto Edu-Trace**: un informe visual con branding
Intezia que mide el impacto de la formación. **Salidas** (desde 2026-10-26, dos por dashboard):

- **PDF cliente** (`index-cliente.html`) — entregable. En el formato vigente cierra con los
  próximos pasos del cliente y la recomendación de Intezia (§5).
- **Video vertical** de unos 20 s con el kit de Zía — aparte del PDF, sin Zía dentro del PDF
  (`plantillas/video-dashboard.md`).

> **Sin deck interno (desde 2026-06-10).** Antes se emitía además un `index-interno.html` con
> prospección de venta; se retiró por costo y eficiencia. El único dashboard es el de cara al
> cliente. Los decks internos ya generados se conservan donde estén; no se crean nuevos.

**Fuente** (formato anterior; el vigente suma Edu-Pulse, §2b): un export CSV del Google Form «Encuesta Edu-Trace» (uno por capacitación
cerrada, lo responden todos los participantes, número variable, solo de cierre).

**Disparador (v1):** el usuario sube el `encuesta.csv` a `clientes/dashboards/<slug>/` y se
genera el dashboard. (v2 futura: web con carga de CSV y dashboard interactivo con filtros.)

---

## 2. Estructura de la encuesta (4 bloques + identidad)

Edu-Trace tiene un **esqueleto fijo** (identidad + Bloques B, D, E) y un **bloque variable**
(C, preguntas técnicas a la medida del contenido de cada capacitación). Cada bloque se lee
con una lógica distinta:

| Bloque | Qué es | Tipo | Lógica de lectura |
|---|---|---|---|
| **A · Identidad** | timestamp, nombre, cédula, correo, departamento | datos | Segmentación + lista de participación. **Cédula nunca se muestra (§4.16).** |
| **B · Impacto autopercibido** | 4 ítems Likert 1-5: *Brecha de Conocimiento* (antes, retrospectivo), *Competencia Adquirida* (después), *Aplicabilidad Operativa*, *Impacto en Productividad* | escala | Se promedian. Delta = Competencia − Brecha = «salto percibido». |
| **C · Conocimiento objetivo** | 3 preguntas técnicas con respuesta correcta (cambian por capacitación) | calificable | **Se califican bien/mal**, no se promedian → % de retención objetivo. |
| **D · Calidad / Facilitador** | 4 ítems Likert 1-5: Claridad, Acompañamiento, Gestión del Tiempo, Dominio Técnico | escala | Se promedian. Nota a la experiencia. |
| **E · Inteligencia comercial** | 3 textos abiertos: área a automatizar, habilidad deseada, departamento que se beneficiaría | texto | Clustering temático → próxima venta. NO se promedia. |

### Clave del Bloque C (§4.18)
No hay hoja de respuestas formal. El consultor define las preguntas conociendo la respuesta;
al procesar, **Claude deduce la respuesta correcta por razonamiento** y la traduce en
`keywords_correctas` dentro de `mapeo.json`. Si una pregunta queda ambigua, **preguntar al
usuario antes de calificar**. El script marca acierto si la respuesta del participante
contiene las keywords (modo `todas` por defecto, `alguna` si se indica).

---

## 2b. Fuentes del formato vigente: Edu-Pulse + Edu-Trace v0.2

El dashboard vigente se alimenta de dos evaluaciones (diseño y preguntas completas:
`encuestas-v2/resumen.html` y `encuestas-v2/anexo.html`; formularios:
`encuestas-v2/crear-formularios.gs`):

| Instrumento | Cuándo | Quién | Qué evalúa |
|---|---|---|---|
| **Edu-Pulse** | En cada sesión (~1 min) | Anónimo: sin nombre ni correo | El **progreso del grupo** («Me siento capaz de repetir lo practicado sin ayuda», 1-5), la conducta en el ejercicio de la sesión, la relevancia y el buen uso del tiempo, y qué ayudó o frenó |
| **Edu-Trace** (v0.2) | Al cierre de la formación | Personal (certificado y menciones) | El **conocimiento** (5 preguntas de situación con respuesta correcta), la **aplicación real** (si ya aplica, qué lo frena, minutos antes y ahora de su tarea y veces por semana), la competencia y la aplicabilidad percibidas, la calidad del consultor, el radar de necesidades y la recomendación |

**Naturaleza de cada dato (§4.17):**

- **Medido:** solo el conocimiento (% de aciertos).
- **Declarado:** la aplicación real y el tiempo ahorrado por tarea. Horas por semana = (minutos
  antes − minutos ahora) × veces por semana ÷ 60. Se reporta la **mediana** y no se extrapola a
  toda la jornada.
- **Percibido:** competencia y aplicabilidad, el progreso del grupo (con su conducta en el
  ejercicio, tal como la reporta cada participante) y la experiencia (dominio técnico, relevancia,
  ritmo, recomendación).

> **Estado:** el rediseño es el borrador v0.2 del 2026-10-13 (documento interno, en evaluación). Si
> cambian las preguntas, se ajusta esta sección.

---

## 3. El Índice de Impacto Edu-Trace (0-100), formato anterior

Resultado medible titular, compuesto de 4 ejes ponderados **priorizando lo medido**:

```
norm(x) = (x − 1) / 4 × 100          (Likert 1-5 → 0-100)
Índice  = 0.30·E1 + 0.35·E2 + 0.20·E3 + 0.15·E4
```

| Eje | Fuente | Cálculo | Peso |
|---|---|---|---|
| **E1 · Competencia percibida** | Bloque B · «Competencia Adquirida» | `norm(media)` | 30% |
| **E2 · Retención objetiva** | Bloque C · 3 preguntas | `% aciertos global` | **35%** |
| **E3 · Aplicabilidad e impacto** | Bloque B · Aplicabilidad + Productividad | `norm(media de 2)` | 20% |
| **E4 · Calidad de la experiencia** | Bloque D · 4 ítems | `norm(media de 4)` | 15% |

- **E2 pesa más** porque es el único eje *medido*; el resto es autopercepción.
- El **salto de aprendizaje** (Competencia − Brecha) se reporta **aparte**, etiquetado
  *percibido/retrospectivo*. NO entra al Índice (evita doble conteo con E1 y no es baseline real).
- Si un eje no tiene datos, el Índice se re-pondera entre los ejes presentes.

Lo calcula `scripts/edutrace-procesar.py` → `resultados.json`. No recalcular a mano.

---

## 3b. Índice de Impacto en escala 1-5 (formato vigente)

Los cuatro ejes y sus pesos son los mismos (competencia 30%, retención 35%, aplicabilidad 20%,
calidad 15%), pero **todo va en escala 1-5**, la misma de Edu-Pulse y Edu-Trace:

```
Índice = 0.30·Competencia + 0.35·Retención + 0.20·Aplicabilidad + 0.15·Calidad     (1-5)
Retención (1-5) = 1 + 4 × % de aciertos        (84% de aciertos equivale a 4.4)
```

Los aciertos y la adopción se muestran como **% de personas**. El eje de retención sigue siendo el
único medido.

> **Pendiente:** hoy no existe un procesador para estos datos. `edutrace-procesar.py` y
> `generar-dashboard.sh` son del formato anterior (CSV de la encuesta v1, índice 0-100). El ejemplo
> se armó a mano con datos simulados. Mientras no exista el procesador, las cifras de un dashboard
> real se calculan y se verifican con el usuario: nunca se estiman ni se rellenan.

---

## 4. Reglas de copy — honestidad de medición (§4.17)

| Regla | Sí | No |
|---|---|---|
| Etiquetar la naturaleza del dato | «competencia **percibida**», «salto **percibido**», «retención **objetiva medida**» | «la competencia subió a 80», «mejoró un 40%» |
| Solo el Bloque C admite lenguaje de medición | «respondió bien el **97%** de la evaluación» | aplicar «medido» a B o D |
| El salto es retrospectivo | «cómo vive el equipo su avance» + disclaimer | «mejoró +1.5 respecto al inicio» (no hubo baseline) |
| Muestra pequeña | «con 1 participante por área, la cifra es referencial» | rankear áreas de n=1 como si fuera significativo |

Usa los tags visuales `.tag-medido` (negro/amarillo) y `.tag-percibido` (gris) para que el
lector distinga de un vistazo. Aplican el resto de reglas del sistema (§4.13 sin guion largo,
§4.10 sin overflow, §4.12 acrónimos glosados: «n8n», «CRM», «API» en lenguaje natural).

En el formato vigente hay una tercera etiqueta, `.tag-declarado` (naranja), para la aplicación real y
el tiempo ahorrado; `.tag-medido` queda para el conocimiento y `.tag-percibido` para el resto (§2b).
Las horas por semana se dan como mediana de quienes aplican; el total del grupo se rotula
«estimación conservadora: mediana por número de personas» y no se extrapola a toda la jornada.

---

## 5. Secciones de las salidas (formato vigente: 7 slides)

El deck se arma clonando `encuestas-v2/dashboard-ejemplo/` (`index.html` + `overrides.css`), que enlaza
el `_base/styles.css` de las propuestas. Al llevarlo a `clientes/dashboards/<slug>/` se ajustan las
rutas: `../../propuestas/_base/styles.css` y `../../../logos/{educacion|fundacion}/` (logo de la
división del cliente, §4.1). Clases propias: `.s-impact`, `.s-data` con `.s-real`, `.s-prog` y
`.s-know`, y `.s-reco` con `.final` y `.s-recomendacion`.

| # | Slide | Clase | Contenido |
|---|---|---|---|
| 01 | Portada | `.s-cover` | Titular-objetivo del programa, lead (N, área, cliente) y bloque «qué evalúa» de Edu-Pulse y Edu-Trace (§5.1) |
| 02 | Resultado global | `.s-impact` | Índice de Impacto Edu-Trace (1-5): gauge + 4 ejes (competencia percibida, retención objetiva medida, aplicabilidad e impacto, calidad de la experiencia) + 3 cifras clave (% que ya aplica, horas por semana en mediana, % que lo recomienda) + hook |
| 03 | Resultados reales | `.s-data` `.s-real` | `declarado`: % que ya aplica, horas por semana por persona (mediana) y estimación conservadora del total; minutos antes y ahora por tarea; frenos de quienes aún no aplican |
| 04 | Progreso del grupo | `.s-data` `.s-prog` | `percibido` (Edu-Pulse): curva por sesión (1-5), ejercicio de cada sesión (solo, con ayuda, no pudo) y lo que más ayudó y más frenó |
| 05 | Conocimiento y experiencia | `.s-data` `.s-know` | Conocimiento `medido` (% de aciertos, global y por pregunta) y experiencia `percibida` (dominio técnico, relevancia, ritmo, % que recomienda) |
| 06 | Próximos pasos | `.s-reco` `.final` | Tres rankings del radar de necesidades (áreas que piden formación, habilidades deseadas, procesos a automatizar), una cita con autorización y hook |
| 07 | Recomendación de Intezia | `.s-reco` `.s-recomendacion` | 3 pasos en orden, franja de cierre y contacto (§5.2) |

- **Datos de muestra:** el ejemplo lleva en cada slide el rótulo `.ejemplo-tag` («Ejemplo · datos
  simulados»), en la portada la línea «EJEMPLO · Datos simulados» y valores de relleno (Empresa
  Ejemplo, la cita, la asesora). En un dashboard real se quitan y se reemplazan por los datos del
  cliente; ninguna cifra se inventa.
- **Escala 1-5** en todos los ejes (§3b), contador «NN / 07» y eyebrows numerados del 01 al 06.
- **Sesiones (slide 04):** el ejemplo tiene 5. Con otro número se ajustan la grilla `.cols5` y el SVG
  de la curva y se corre `verificar-overflow.js`. Una sesión con menos de 4 respuestas no se muestra (§6).
- **Pendiente:** la slide 04 usa la conducta en el ejercicio (solo, con ayuda, no pudo), propia de
  Habilidades. Para Detección, Políticas e Innovación, cuyas preguntas propias de Edu-Pulse son otras
  (`encuestas-v2/resumen.html`), la versión de esa slide está por definir con el usuario.

### 5.1 Portada: qué evalúa cada instrumento (2026-10-26)

La portada dice desde el primer vistazo **con qué se midió** y **qué evalúa cada instrumento**
(corrección de dirección sobre el dashboard de ejemplo): quien lee el dashboard no tiene por qué
conocer Edu-Pulse ni Edu-Trace.

- **Eyebrow:** «Dashboard de Impacto · Edu-Pulse y Edu-Trace». Siempre con guion en todo el deck
  (no «EduPulse» ni «EduTrace»).
- **Lead corto** (2 líneas): quiénes respondieron (N, área, cliente) y «medidos con las dos
  evaluaciones de Intezia».
- **Bloque `.eval2`** bajo el lead, dos columnas (`.ev` con borde amarillo y etiqueta `.ev-t`):
  - *Edu-Pulse · en cada sesión*: evalúa el **progreso del grupo** (cuánto se siente capaz de
    repetir lo practicado y qué le ayudó o le frenó). Respuestas anónimas.
  - *Edu-Trace · al cierre*: evalúa **lo que quedó**: el conocimiento (medido), el uso real y el
    tiempo ahorrado en el trabajo (declarados) y la experiencia de la formación.
- **Honestidad (§4.17):** cada dimensión lleva su naturaleza entre paréntesis (medido, declarado,
  percibido). Se redacta con lo que ese cliente **realmente respondió**: sin datos de Edu-Pulse se
  omite su columna y el eyebrow queda «Dashboard de Impacto · Edu-Trace»; con la encuesta Edu-Trace
  anterior (sin las preguntas de aplicación real) no se lista «uso real» ni «tiempo ahorrado», sino
  lo que sí midió (competencia y aplicabilidad percibidas, retención medida, calidad de la experiencia).
- **Espacio (§4.10):** lead en 2 líneas y cada columna en ≤ 3 líneas. Es lo que cabe sobre la línea
  de identificación sin tocar el titular (verificado con `verificar-overflow.js`).
- **Ejemplo canónico y CSS:** `encuestas-v2/dashboard-ejemplo/` (`index.html`, slide 01; reglas
  `.s-cover .eval2`, `.ev` y `.ev-t` en `overrides.css`, que se copian al `overrides.css` del cliente).

### 5.2 Recomendación de Intezia (2026-10-26)

Última slide del deck (07). La slide 06 (próximos pasos) muestra **lo que el equipo pidió**; esta dice
**qué recomienda Intezia hacer y en qué orden**, a partir de esos próximos pasos.

- **Fuente:** solo lo que ya está en el dashboard (los próximos pasos de la slide 06, los frenos de
  quienes aún no aplican, el tiempo ahorrado declarado, las áreas que piden formación). **Ninguna
  cifra nueva**: sin dato en el deck, no se escribe.
- **Estructura:** título «Tres pasos, en este orden.»; 3 tarjetas con número, rótulo (Primero ·
  Luego · Después), título corto y 2 a 3 frases (el dato que respalda + «Proponemos…») con un
  `<strong>` en la acción; franja naranja de cierre.
- **Orden por defecto:** 1) resolver lo que frena (si hay frenos declarados), 2) escalar el proceso
  que más piden automatizar y que ya muestra el mayor ahorro, 3) ampliar al área que más pide
  formación. Un paso sin respaldo en los datos se omite o se cambia por otro que sí lo tenga.
- **Títulos de tarjeta ≤ ~25 caracteres:** uno de 2 líneas desalinea el texto de las otras tarjetas
  (§4.10). Caso del ejemplo: «Ampliar a Atención al cliente» bajaba a 2 líneas y se acortó.
- **Franja de cierre:** recomienda avanzar en ese orden y **volver a medir con Edu-Trace al cierre de
  cada paso**.
- **Honestidad (§4.17):** las cifras declaradas se rotulan como tales («ahorro declarado»); nunca
  «mejoró» sobre datos percibidos o declarados.
- **Qué no lleva:** acuerdos económicos, valores ni plazos (§4.15, §4.23). No nombra servicios de
  Intezia salvo que el usuario lo pida.
- **Contacto** (asesora + empresa): va al pie de esta slide. El formato vigente no tiene una slide de
  Cierre aparte (sigue sin link de Calendly, ver la nota de abajo).
- **Ejemplo canónico y CSS:** `encuestas-v2/dashboard-ejemplo/` (slide 07; reglas
  `.s-reco.final.s-recomendacion` en `overrides.css`).

### 5.3 Formato anterior (10 slides, solo referencia)

El piloto `clientes/dashboards/apb-group/` y los dashboards entregados con ese formato se conservan y
**no se tocan**: Portada · Hero del Índice (0-100) · Desglose por eje · Salto de aprendizaje ·
Retención objetiva · Por departamento · Calidad del facilitador · Bloque E (recomendaciones de
expansión) · Participación (nombres y área, sin puntajes) · Cierre (`.s-end`). **No se usa para
dashboards nuevos.** Su procesador (`edutrace-procesar.py`, `generar-dashboard.sh`) sigue siendo el
de ese formato. El formato vigente aplica a los dashboards nuevos o regenerados desde 2026-10-26.

---

> **Sin link de Calendly en el cierre (2026-09-14).** El `.cta-wrap` con el botón
> "Conversemos el próximo paso" → `calendly.com/intezia/30min` **no se incluye** en el
> `.s-end` de ningún Dashboard nuevo o regenerado de aquí en adelante. La slide queda con
> logo + `end-message` + `end-contact` (asesora + empresa), sin el bloque `.cta-wrap`. La
> vía de contacto es la asesora comercial listada, no un link de auto-agendamiento. Misma
> regla aplica en propuestas nuevas (`plantillas/propuesta-comercial.md` → *Reglas de
> copy*). No retroactivo: los dashboards ya entregados (incluido el piloto `apb-group/`)
> conservan su CTA tal como está. En el formato vigente (7 slides) no hay `.s-end`: el contacto
> va al pie de la slide 07, también sin CTA.

---

## 6. Privacidad (§4.16)

- **Cédula**: se descarta en `edutrace-procesar.py` antes de serializar. Nunca en
  `resultados.json` ni en los HTML/PDF.
- **Correo**: solo clave interna de deduplicación; jamás impreso.
- **`encuesta.csv`** (PII cruda): ignorado por `.gitignore` (`clientes/dashboards/*/encuesta.csv`).
  `resultados.json` (sin PII) sí se versiona.
- **Participación**: nombre + departamento, sin puntaje individual.
- **Formato vigente:** Edu-Pulse es anónimo (sin nombre ni correo) y el dashboard no muestra una
  sesión con menos de 4 respuestas. El testimonio se publica solo con autorización de la persona
  (con o sin nombre, según lo marcó). El formato no incluye lista de participación ni desglose por
  departamento.
- Verificación: grep de cédula/correo en salidas → 0 (ver `generar-dashboard.md`).

> Aprendizaje base: 2026-06-01 · APB Group (Tecnología, n8n/IA, N=11) · primer dashboard del
> sistema. Índice 86/100, retención objetiva 97%. El Bloque E señaló RRHH como #1 a formar,
> respaldando la propuesta CAP-033 ya en curso.

---

## 7. Video del dashboard

Todo dashboard se entrega, desde 2026-10-26, con un **video vertical de unos 20 s** hecho con el kit
de Zía (`plantillas/kit-zia/`), aparte del PDF. Especificación, guion, reglas de marca (Zía nunca
dentro del PDF, voz de narrador, aprobación de Jean para enviarlo a clientes) y checklist:
`plantillas/video-dashboard.md`. Carpeta de trabajo: `clientes/dashboards/<slug>/video/`.
