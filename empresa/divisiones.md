# Divisiones de Intezia

> Intezia opera bajo **dos divisiones** que comparten metodología pero atienden públicos distintos. **Toda propuesta debe quedar adscrita a una de las dos**, y esa decisión gobierna qué logo se usa, qué tono se aplica y qué condiciones contractuales corren.

---

## Las dos divisiones

### Fundación

<!-- TODO: el usuario completará la descripción específica de la Fundación. -->

- **Misión / foco**: _Pendiente_
- **Audiencia típica**: _Pendiente_ (ej. ONGs, sector público, comunidades, beneficiarios sociales)
- **Tipos de programa que prevalecen**: _Pendiente_ (ej. Charlas, Talleres comunitarios)
- **Modelo de financiamiento**: _Pendiente_ (subsidio, cooperación, alianza)
- **Logo**: `logos/fundacion/BLANCO.png` y `logos/fundacion/NEGRO.png`

### Educación

<!-- TODO: el usuario completará la descripción específica de Educación. -->

- **Misión / foco**: _Pendiente_
- **Audiencia típica**: _Pendiente_ (ej. empresas privadas, profesionales, instituciones educativas)
- **Tipos de programa que prevalecen**: _Pendiente_ (ej. Cursos, Diplomados, Capacitaciones In-Company)
- **Modelo de financiamiento**: _Pendiente_ (cobro directo, contrato corporativo, alianza universitaria)
- **Logo**: `logos/educacion/BLANCO.png` y `logos/educacion/NEGRO.png`

---

## Cómo se elige la división

**No se asume ni se infiere.** El usuario decide al iniciar cada propuesta:

1. Cuando recibas un pedido nuevo del tipo *"arma una propuesta para X"*, **antes de generar nada** pregunta: *"¿Es una propuesta de Fundación o de Educación?"*
2. Registra la respuesta como campo obligatorio en `clientes/<empresa-slug>/brief.md` bajo el campo `division: fundacion | educacion`.
3. Esa elección **bloquea todo lo demás**: el logo, la marca visual y, en algunos casos, las políticas comerciales aplicables.
4. Si en mitad de la propuesta el usuario quiere cambiar de división, **vuelve a generar desde la portada** — no parchees. Persistir la división equivocada arruina la coherencia.

---

## Tipos de programa por división (referencia indicativa)

No es una regla dura — es una guía. La categorización oficial la confirma el usuario.

| Tipo de programa | Más común en |
|---|---|
| Charla | Ambas (más en Fundación cuando es divulgación social) |
| Taller | Ambas |
| Capacitación In-Company | Educación |
| Curso | Educación |
| Diplomado | Educación |

Si un caso no encaja con esto, prevalece la decisión del usuario.

---

## Notas para Claude

- **Nunca generes una propuesta sin tener `division` definida**. Si el `brief.md` no la tiene, pregunta y guárdala.
- Las plantillas de diseño (`plantillas/diseno-*.md`) son **agnósticas a la división**: la división solo afecta marca visual y logos.
- Si el usuario te pide hablar genéricamente de Intezia (no de un programa específico), usa el logo de Educación como default — pero pregúntale si tiene dudas.
