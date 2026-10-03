# Plantilla operativa: Diseño de Charla

> Traducción accionable del formato oficial `fuentes/formatos-oficiales/charla.pdf`. Genera el archivo `clientes/<empresa-slug>/programa.md` siguiendo este esquema cuando el tipo de documento sea **Charla**.

> **Pre-requisitos antes de generar**: el `brief.md` del cliente debe tener `division: fundacion | educacion`. Si no, pregunta al usuario primero.

---

## Estructura del documento

```markdown
# Documento Oficial de Diseño Curricular e Instruccional

**[LOGO INTEZIA — `logos/{division}/NEGRO.png`]**  /  **[LOGO Empresa o Aliado]**

# Charla
## {{Título Oficial de la Charla}}

**Versión**: (Propuesta Optimizada)
**Elaborado por**: {{nombre_responsable}}
**Aprobado por**: {{nombre_aprobador}}
**Fecha de Aprobación**: {{YYYY-MM-DD}}

---

## 1. Información general del programa

- **Nombre de la Charla**: {{nombre_completo}}
- **Empresa**: {{empresa_cliente}}
- **Modalidad**: Presencial / Online Síncrono *(la charla típicamente no es asíncrona)*
- **Duración**: {{N}} horas académicas

---

## 2. Fundamentación

### 2.1 Planteamiento de la necesidad
{{Describir contexto actual, brecha de conocimiento en el mercado y por qué es imperativo dictar esta charla.}}

### 2.2 Objetivo
{{Verbo en infinitivo + Objeto + Condición + Finalidad.}}

> Ejemplo: "Sensibilizar a los líderes operativos sobre el impacto del feedback efectivo en el clima laboral, mediante casos reales aplicables a su gestión diaria."

---

## 3. Perfil de los participantes
{{Edad, razón social, sector, cargos típicos, motivación esperada.}}

---

## 4. Contenido de la charla

| Tópico | Tiempo | Estrategias del facilitador | Recurso y entornos |
|---|---|---|---|
| {{Tópico 1}} | {{10-20 min}} | {{Demostración guiada, interactiva, preguntas socráticas}} | {{Presentación, Meet}} |
| {{Tópico 2}} | {{...}} | {{...}} | {{...}} |
| {{...}} | {{...}} | {{...}} | {{...}} |

---

## 5. Garantía de calidad y mejora continua

- **Construcción curricular**: Adaptación del contenido para responder al interés real de la empresa.
- **Encuesta de satisfacción**: Monitoreo de la experiencia del participante.

---

## 6. Perfil del equipo facilitador

Para garantizar la calidad de la charla, los facilitadores asignados a este programa cumplen con:

- **Formación académica**: Certificación experta demostrable en el área.
- **Experiencia profesional**: ≥ 2 años trabajando activamente en el sector.
- **Competencias pedagógicas**: Experiencia en facilitación de grupos, manejo de entornos virtuales de aprendizaje y metodologías activas.
```

---

## Reglas duras (no romper)

- **Sin código de programa** (las charlas no llevan).
- **Sin objetivos específicos**, sin perfil de egreso, sin módulos. La charla es ligera.
- **Una sola tabla de contenido** con las cuatro columnas estándar.
- **Modalidad**: típicamente Presencial u Online Síncrono.
- **Facilitador**: ≥ 2 años.
- **Logo en portada**: corresponde a la división elegida (`fundacion` o `educacion`).

## Antes de entregar — checklist

- [ ] División confirmada con el usuario (logo correcto)
- [ ] Tono coherente con `empresa/identidad.md`
- [ ] Objetivo redactado con la fórmula Verbo + Objeto + Condición + Finalidad
- [ ] Tabla de contenido con tiempos que sumen la duración total
- [ ] Sin placeholders `{{...}}` sin llenar
