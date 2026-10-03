# Plantilla — Dashboard de Impacto Edu-Trace

> Diseño y lógica del **segundo flujo** del sistema: el reporte de cierre que convierte
> la Encuesta Edu-Trace de un cliente en un resultado medible. Paralelo al de propuestas.
> Mecánica de generación: `plantillas/generar-dashboard.md`. Flujo en `CLAUDE.md §11`.

---

## 1. Qué es

Cuando termina el proceso de un cliente (impartida la capacitación, respondida la encuesta
de cierre), se genera un **Dashboard de Impacto Edu-Trace**: un informe visual con branding
Intezia que mide el impacto de la formación. **Salida única** del motor de datos:

- **PDF cliente** (`index-cliente.html`) — entregable. Bloque E reformulado como
  «recomendaciones de expansión».

> **Sin deck interno (desde 2026-06-10).** Antes se emitía además un `index-interno.html` con
> prospección de venta; se retiró por costo y eficiencia. El único dashboard es el de cara al
> cliente. Los decks internos ya generados se conservan donde estén; no se crean nuevos.

**Fuente única:** un export CSV del Google Form «Encuesta Edu-Trace» (uno por capacitación
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

## 3. El Índice de Impacto Edu-Trace (0-100)

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

---

## 5. Secciones de las salidas (10 slides)

El deck clona el stack visual de las propuestas: enlaza `../../propuestas/_base/styles.css`
+ `overrides.css` local (clases `.s-data`, `.s-ejes`, `.s-salto`, `.s-reten`, `.s-reco`, `.s-part`
y barras `.hbars`). Reutiliza `.s-cover`, `.s-impact` (gauge + barras) y `.s-end` del `_base`.

| # | Slide | Clase | Contenido |
|---|---|---|---|
| 01 | Portada | `.s-cover` | Cliente, capacitación, eje |
| 02 | Hero del Índice | `.s-impact` | Gauge 0-100 + 4 barras de eje + hook honesto |
| 03 | Desglose por eje | `.s-ejes` | 4 cards (E1-E4) con peso y tag medido/percibido |
| 04 | Salto de aprendizaje | `.s-salto` | antes→después (1-5) + disclaimer retrospectivo (no afirmar mejora medida) |
| 05 | Retención objetiva | `.s-reten` | % global + 3 preguntas calificadas (único bloque «medido») |
| 06 | Por departamento | `.s-data` + `.hbars` | Índice por área + nota de muestra pequeña |
| 07 | Calidad / facilitador | `.s-data` + `.hbars` | 4 ítems del Bloque D |
| 08 | **Bloque E** | `.s-reco` | «recomendaciones de expansión» de valor para el cliente |
| 09 | Participación | `.s-part` | Nombres + área, **sin puntajes, sin cédula** |
| 10 | Cierre | `.s-end` | Mensaje de cierre + contacto (**sin CTA a Calendly**, ver nota) |

---

> **Sin link de Calendly en el cierre (2026-09-14).** El `.cta-wrap` con el botón
> "Conversemos el próximo paso" → `calendly.com/intezia/30min` **no se incluye** en el
> `.s-end` de ningún Dashboard nuevo o regenerado de aquí en adelante. La slide queda con
> logo + `end-message` + `end-contact` (asesora + empresa), sin el bloque `.cta-wrap`. La
> vía de contacto es la asesora comercial listada, no un link de auto-agendamiento. Misma
> regla aplica en propuestas nuevas (`plantillas/propuesta-comercial.md` → *Reglas de
> copy*). No retroactivo: los dashboards ya entregados (incluido el piloto `apb-group/`)
> conservan su CTA tal como está.

---

## 6. Privacidad (§4.16)

- **Cédula**: se descarta en `edutrace-procesar.py` antes de serializar. Nunca en
  `resultados.json` ni en los HTML/PDF.
- **Correo**: solo clave interna de deduplicación; jamás impreso.
- **`encuesta.csv`** (PII cruda): ignorado por `.gitignore` (`clientes/dashboards/*/encuesta.csv`).
  `resultados.json` (sin PII) sí se versiona.
- **Participación**: nombre + departamento, sin puntaje individual.
- Verificación: grep de cédula/correo en salidas → 0 (ver `generar-dashboard.md`).

> Aprendizaje base: 2026-06-01 · APB Group (Tecnología, n8n/IA, N=11) · primer dashboard del
> sistema. Índice 86/100, retención objetiva 97%. El Bloque E señaló RRHH como #1 a formar,
> respaldando la propuesta CAP-033 ya en curso.
