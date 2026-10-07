# Brief — N58 Banco Digital · Mercadeo con Claude (CAI-034)

## Actualización 2026-10-06 — reexpresada en el formato compacto de Habilidades (6 slides) · VIGENTE

Instrucción directa del usuario: «ajustar la CAI-034 hacia el nuevo formato». El deck canónico de 15
slides (enviado el 2026-10-01), su PDF y su `customize-n58-banco-digital.py` están archivados en
`_anterior-15-slides/`; `scripts/customize-n58-banco-digital.py` se retiró (el compacto usa el par
genérico `customize-acroforms.py` + `customize-habilidades-compacto.py`, igual que G-MAX y CAI-032).

**Hoy el deck es compacto de 6 slides, dirigido por `datos.json`** (fuente única; `index.html`,
`acroforms.json` y `programa.md` se generan). Flujo: `python3 scripts/generar-habilidades-compacto.py
n58-banco-digital` → `node scripts/verificar-habilidades-compacto.js n58-banco-digital` →
`bash scripts/pdf-habilidades-compacto.sh n58-banco-digital`.

> **Cuidado con el PDF de soberanía de datos:** el wrapper aparta (y ante un fallo borra) todos los
> `*.pdf` de la carpeta, y `customize-acroforms.py` exige exactamente uno. Antes de correr
> `pdf-habilidades-compacto.sh`, sacar `Soberanía de Datos - N58 (Tecnología).pdf` de esta carpeta y
> devolverlo después. `soberania-datos.html` no se ve afectado.

### Cómo se mapeó la propuesta al esquema compacto

| En el compacto | En CAI-034 |
|---|---|
| Carril | «Claude» (una sola herramienta) |
| Área (vocabulario «etapa») | Fundamentals · Construcción · Implementación (las 3 etapas con horas; el kick-off de 1 h va aparte) |
| Solución / entregable | Cada **sesión de 2 h**: 1 + 3 + 2 = 6 entregables, 12 h (misma estructura que CAI-037) |
| Fases (3 columnas) | Bases (S1, 2 h) · Piezas (S2-S4, 6 h) · Skill (S5-S6, 4 h) |
| Entregables de la Construcción | Primer avance revisado · segundo avance ajustado · entrega final (más de 50 creativos y 4 artículos publicados) |
| Entregables de la Implementación | Skill construida con la marca · Skill probada y 1 persona formada |
| 5.ª columna de la ruta | «Garantía 30-60-90» (uso real · mejoras que construye el equipo · tiempo ahorrado) |
| Slide 6 retorno (modo método) | Línea base por pieza → horas recuperadas → valor en dinero, sin cifras del cliente |

### Qué cambió respecto al deck de 15 slides

| Antes | Ahora |
|---|---|
| Certificado INTEZIA y workbook digital para la persona formada | **Retirados** (§4.21: no van por defecto). Decidir con el usuario si el cliente los espera |
| Slide de Impacto con HubSpot, Salesforce y McKinsey | Retirada (§4.9 no aplica al compacto); el retorno va en modo método |
| ROI estimado en la hoja de cotización y slide de seguimiento 30-60-90 | Hoja estándar con garantía 30-60-90; el seguimiento es la 5.ª columna de la ruta |
| Próximos pasos «Cómo arrancamos» y Cierre escalera | Retirados (el compacto no los lleva); la logística de arranque queda en el kick-off |
| 3 módulos (Creativos · SEO · Fundamentals + Skill) | 3 etapas con horas; creativos y artículos van juntos en la Construcción |
| Sin semanas | 6 semanas propuestas por el sistema (1 sesión por semana): confirmar con el calendario de lanzamiento |
| «Skill entrenada con la marca» | «Skill con la marca» (cambio de redacción, no de alcance) |
| Titular «De un equipo de una persona, a un mercadeo que no se detiene.» | Frase-objetivo: «Producción del contenido de lanzamiento de N58 con Claude y una Skill propia» |

### Se conserva del brief anterior

Encuadre «parte del calendario de lanzamiento, no un gasto de mercadeo aparte» (subtítulo de la slide 2
y primera nota de la hoja de inversión) · más de 50 creativos y 4 artículos publicados, tal como se
escuchó en la reunión · 1 persona formada · modalidad presencial · 12 h de sesión y kick-off de 1 h
aparte · sin citas textuales · sin nombres de personas del cliente · sin afirmar migración de stack
(§4.11) · sin Metodología ni Equipo facilitador (§4.10a) · documento de soberanía de datos aparte.

### Pendientes (también en `datos.json`)

Inversión, descuento y total (ventas) · fecha de arranque y calendario de lanzamiento (valida las 6
semanas) · persona a formar designada · quién publica los 4 artículos y dónde · quién contrata la
cuenta de Claude · si se esperan el certificado y el workbook · dotación de Mercadeo (3 personas según
este brief; el deck anterior decía una con apoyo) · nombres y contenido de cada avance de la Construcción
con servicio · línea base dentro de Fundamentals y «Hacia la semana 19» (aritmética).

---

> Lo que sigue es el brief original del deck de 15 slides (2026-10-01), conservado como contexto del
> cliente y trazabilidad. Donde contradice la actualización de arriba, manda la actualización.

## Datos administrativos

- **Empresa**: N58 Banco Digital
- **Sector**: Banca (banco microfinanciero 100% digital, regulado por Sudeban)
- **Tamaño**: Mediana (50-250 empleados)
- **Slug**: `n58-banco-digital`
- **División Intezia**: `educacion` (cliente corporativo — banco, mismo criterio que Banco
  Plaza, AMV Tecnología, Venezolano de Crédito).
- **Servicio (§4.1a)**: `habilidades` — confirmado en la Ficha de Levantamiento
  ("Servicios de interés: Habilidades").
- **Alianza**: `false` (confirmado con el usuario, 2026-10-01).
- **Tipo de documento**: Capacitación In-Company (`CAI-034`), presentada al cliente como **propuesta de proyecto**; formato compacto de 6 slides (con hoja de inversión, campos de precio vacíos para ventas).
<!--auto:inicio-->
- **Alcance**: 6 entregables en 3 etapas · 12 h de sesión · 6 semanas de trabajo desde el arranque · seguimiento a 30, 60 y 90 días
<!--auto:fin-->
- **Fuente**: Ficha de Levantamiento N58 (Flavia Martínez, 2026-10-01) — primer contacto,
  sin servicio previo de Intezia, sin propuesta previa.

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
  (mismos datos de contacto que Banco Plaza/Venezolano de Crédito/Puro Lomo).
- **Contacto cliente (coordinador)**: Sandokan — actúa como coordinador, no como dueño del
  problema.
- **Dueña real del área**: Mari, gerente de Mercadeo (1 persona al frente + 1 persona de
  Instagram + 1 de apoyo operativo).
- **Segundo interesado (no cubierto por esta propuesta)**: Jonathan, Tecnología — ver
  documento aparte de soberanía de datos.

## Contexto del cliente (Ficha de Levantamiento, Bloques A-G)

- Ecosistema tecnológico: Microsoft 365. Coordinación interna por WhatsApp y correo.
- Sin IA corporativa: cada persona paga la suya (Office/Copilot, Gemini, Claude a título
  personal en mercadeo, Cursor en tecnología).
- Nivel de partida del equipo con IA: la usan de forma suelta y sin criterio.
- **Prioridad declarada del banco**: terminar el lanzamiento de la cuenta para personas
  naturales (su negocio central hoy es banca para empresas) y generar recursos. Mercadeo
  entra **después** de esa prioridad, y **sin presupuesto definido todavía**.
- **Por eso**: esta propuesta se presenta como parte del calendario de lanzamiento del
  banco, no como un gasto de mercadeo aparte — encuadre explícito pedido por el usuario.
- Reto del área: llegarle a un público acostumbrado a ir a la agencia, siendo un banco
  100% digital.
- Interés explícito en SEO reputacional: que al buscar al banco aparezcan noticias
  positivas, y convertir casos de riesgo reputacional en mejoras de proceso.
- Modalidad preferida: **presencial** (dato directo de la Ficha, Bloque específico de
  Habilidades).
- En la reunión se habló de formar a **una persona del banco** y cerrar con **4 artículos
  ya publicados**; el cliente lo escuchó como compromiso — se mantiene tal cual en esta
  propuesta (confirmado con el usuario, 2026-10-01).
- Los 5 creativos de muestra del documento de creativos (adjunto como briefing, no se
  regenera aquí) funcionaron muy bien en la reunión — se usan como base de lo que ya vieron,
  sin repetirlos literalmente en el deck.

## Qué pide el cliente (resumen operativo)

- **Producción de creativos** (estáticos y video) para el lanzamiento, con la paleta y el
  tono de marca de N58 (colores con nombres criollos, botones con corte verde lima, isologo
  de montaña, personaje AlaN) — ver documento de creativos adjunto.
- **Contenido SEO reputacional**: artículos de blog para posicionamiento, con el compromiso
  de 4 publicados al cierre.
- **Formación**: 1 persona del equipo de Mercadeo, capacitada en Fundamentals de Claude y
  con una Skill propia entrenada con la marca del banco.

## Decisiones de diseño (2026-10-01, deck de 15 slides; ver la actualización de arriba para lo vigente)

1. **Caso base estructural**: `banco-plaza-mercadeo/` (CAI-024) — mismo servicio
   (Habilidades), mismo tipo (Capacitación In-Company mono-fase), mismo sector (banca). Se
   reutiliza su estructura de 4 etapas y su shell visual (Beneficios v3, Cierre escalera,
   roadmap `.rmx-linear`, slide de Seguimiento 30-60-90) **sin mencionar ni dejar rastro de
   Banco Plaza** en el documento final — instrucción directa del usuario.
2. **3 módulos** (no 2, a diferencia de Banco Plaza) en la slide "El servicio", porque el
   alcance de N58 suma un tercer frente que Banco Plaza no tenía — contenido SEO:
   - I. Producción de creativos (estáticos y video)
   - II. Contenido SEO reputacional
   - III. Fundamentals + Skill
3. **4 etapas, mismo orden que Banco Plaza**: Kick-off (1h, aparte) → Fundamentals (2h) →
   Construcción (6h, 3 sesiones de revisión de 2h — sube de 4h porque además de creativos
   hay que producir y revisar los 4 artículos SEO) → Implementación (4h, 2 sesiones).
   **Total de la propuesta: 12h** (2+6+4), kick-off por fuera. Dentro del rango de
   dimensionamiento de Habilidades por área (8-12h, `empresa/politicas-comerciales.md`).
4. **Modalidad: presencial** (dato directo de la Ficha, no hace falta preguntar).
5. **Sin `fecha_arranque_deseada` ni `resultados_esperados` confirmados** — la Ficha deja el
   horizonte de tiempo sin especificar y la disponibilidad presupuestaria "no definida aún".
   Criterio aplicado (§6 Paso 1, punto 3): **se omiten el Calendario de inicio (grid de
   fechas en "Cómo arrancamos") y el ROI numérico** en vez de inventarlos. El paso "Cómo
   arrancamos" queda con los 3 pasos de logística estándar, sin fechas ni calendario.
6. **Sin afirmar migración de stack (§4.11)**: N58 usa Microsoft 365; Claude se suma a ese
   entorno para producción de contenido, nunca se dice que el banco migra o reemplaza su
   stack.
7. **Sin citas textuales** (instrucción directa del usuario, 2026-10-01): ningún fragmento
   de la Ficha de Levantamiento se usa como cita atribuida al cliente; el Diagnóstico y los
   objetivos son síntesis, no transcripción.
8. **Con certificado de participación INTEZIA** — Habilidades con capacitación real (1
   persona formada).
9. **Garantía 30-60-90 y slide de Seguimiento**: aplican (estándar vigente para Habilidades
   desde 2026-09-23).
10. **Entregables explícitos** (mantener tal cual se escuchó en la reunión, confirmado con
    el usuario): más de 50 creativos, 4 artículos SEO publicados, 1 persona formada y
    certificada, Skill de Claude entrenada con la marca.

## Impacto (§4.9) — retirado en el compacto

El deck de 15 slides reutilizaba las cifras ya verificadas en `banco-plaza-mercadeo/` / `puro-lomo-bajo-mercadeo/`
(mismo eje: adopción de IA en tareas de mercadeo/creatividad) — HubSpot (State of AI for
Marketers, 2025), Salesforce (State of Marketing, 10ª edición, 2026), McKinsey (The Economic
Potential of Generative AI, 2023). Sin `<strong>` en `.impact-hook .hook-text` (memoria
`bug-strong-glitch-impact-hook-text.md` — el origen Banco Plaza sí lo tenía y se corrige en
este clon).

## Entregables (compromisos escuchados en la reunión; el compacto los reexpresa en 6 entregables por sesión)

- Más de 50 creativos (estáticos y video) para el lanzamiento, según la paleta y tono de
  marca de N58.
- 4 artículos de posicionamiento SEO reputacional, publicados.
- Skill de Claude entrenada con la marca de N58.
- Workbook digital y certificado de participación INTEZIA (1 persona formada).

## Notas internas

- **Documento complementario, fuera de esta propuesta**: documento de soberanía de datos
  para Tecnología (Jonathan) — no es una propuesta comercial, vive en
  `soberania-datos.html` / su PDF en esta misma carpeta. No lleva AcroForms ni precio.
- **Pendiente de confirmar con Flavia antes de enviar**: fecha de arranque real (hoy sin
  confirmar) y si la persona a formar ya está designada por Mari.
- Próximo paso acordado con el cliente: Sandokan coordina una mesa de trabajo con Mercadeo
  donde se levanta el detalle que falta (manual de marca, calendario de lanzamiento,
  aprobadores).
