# Brief — Venezolano de Crédito (CAI-018)

## Datos administrativos

- **Empresa**: Venezolano de Crédito
- **Sector**: Banca — Grande / Enterprise (más de 250 empleados)
- **Slug**: `venezolano-de-credito`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Tipo de documento**: Capacitación In-Company (`CAI-018`) · 8 sesiones de 2h · 16h
  totales · modalidad presencial (ajustado 2026-09-16, antes 9 sesiones/18h).
- **Eje temático**: Aplicar Claude a los 7 procesos reales del equipo de Mercadeo (contenido,
  campañas, diseño, marca), complementando la capacitación interna que ya lidera Andrés
  Pereira, dentro de las políticas de datos del banco.
- **Fecha del brief**: 2026-09-10
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Venezolano de Crédito**
(`Levantamiento_Venezolano_de_Credito_2026-09-10.pdf`, registrada 2026-09-10), elaborada por
la asesora **Flavia Martínez**, más precisiones directas del usuario en el mismo mensaje
(puntos del correo del cliente + imagen de restricciones del banco).

## Contacto

- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com.
- **Contacto cliente**: Andrés Pereira · Gerente de Inteligencia Artificial y Analítica de
  Datos (actualizado 2026-09-16, antes "VP. Soluciones Digitales") — lidera él mismo una
  capacitación interna, e Intezia la complementa. También es el **responsable de logística**
  durante el servicio.
- **Servicio previo con Intezia**: ninguno como servicio contratado — pero es el **tercer
  acercamiento comercial**: a inicios de año se exploró un "proyecto masivo estilo Zoom" que
  no se aprobó, y luego se ofreció Detección, que rechazaron porque en ese momento necesitaban
  un desarrollo, no un diagnóstico. Contexto interno, no se menciona en el deck.

## Decisiones confirmadas con el usuario (2026-09-10)

1. **18 horas totales originalmente** (9 sesiones de 2h) — cálculo según el lineamiento de
   Habilidades (`empresa/politicas-comerciales.md` → *Dimensionamiento por servicio*): base
   8-12h para hasta 5 procesos + 4h por cada proceso adicional sobre el quinto. Con **7
   procesos** en 1 sola área (Mercadeo): base 10h (punto medio de 8-12h) + 8h (2 procesos
   extra, el 6º y 7º) = **18h**. El usuario eligió el punto medio del rango, no el límite
   superior ni inferior. **Ajustado a 16h (8 sesiones) el 2026-09-16** — ver sección de ajuste
   más abajo.
2. **Duración de sesión: 2 horas, modalidad presencial** — dato explícito de la ficha
   ("Duración y frecuencia que les funciona: 2 horas" · "Modalidad preferida: Presencial"), no
   una inferencia — se respeta tal cual, a diferencia de otros clientes donde la duración de
   sesión es un default del sistema.
3. **Herramienta: Claude, ya decidida por el cliente** — a diferencia de las Detecciones de
   esta sesión (donde la herramienta es una recomendación preliminar nuestra), aquí el cliente
   ya eligió Claude explícitamente ("¿Cuál les gustaría tener o incorporar?: Claude
   (Anthropic)") y ya lo están empezando a usar. El deck nombra Claude con confianza en todo
   el documento, sin el framing de "recomendación preliminar a confirmar" que sí aplica en
   Detección.
4. **2 casos de uso adicionales, pendientes de revisión de seguridad**: el cliente mencionó
   "Desempeño de campañas" y "Contenidos por segmento de clientes" como casos de uso que
   quería atacar, pero él mismo los marcó como pendientes de revisión de seguridad — **no
   forman parte de los 7 procesos confirmados ni del cálculo de horas**. Se mencionan en el
   deck (Notas/Próximos pasos) como pendientes, sin prometer que se resuelven en esta
   capacitación.
5. **Pregunta directa del cliente — "¿hasta qué punto Claude los puede apoyar como CRM?"**:
   respondida por escrito en el Diagnóstico del deck. La política del banco prohíbe
   explícitamente pegar información de clientes en el asistente y pedirle cifras (ver
   restricciones abajo) — la respuesta honesta es que **Claude no reemplaza al CRM**: asiste
   la redacción y creación de contenido, pero no almacena ni gestiona registros de clientes.
   Coexiste con el CRM del banco, dentro de sus políticas de datos.
6. **Sin certificado**: **no aplica** — esto SÍ lleva certificado de participación INTEZIA,
   porque es Habilidades con un tronco real de capacitación (a diferencia de Detección pura,
   ver `deteccion-sin-certificado.md`).

## 7 procesos confirmados (base curricular, ficha Bloque C)

> Aclaración del usuario: estos procesos son las **tareas que el cliente quiere optimizar con
> IA** — de ahí que la información venga tan centralizada en la ficha (Bloque C), no una lista
> de departamentos.

1. Redacción de textos y contenidos para la operación diaria
2. Generación de ideas y conceptos de campañas
3. Generación de diseño y piezas gráficas
4. Adaptación de una misma pieza a los distintos canales
5. Asistente sobre lineamientos de marca
6. Escucha de marca y detección temprana de tendencias
7. Diseño de las visuales y experiencia UX/UI para cada una de las plataformas del banco

**Agrupación curricular usada para diseñar el programa** (no viene así en la ficha, es
elaboración propia para estructurar 3 módulos coherentes):
- Contenido y campañas: procesos 1, 2
- Diseño y adaptación visual: procesos 3, 4, 7
- Marca y tendencias: procesos 5, 6

## Restricciones del banco (Bloque E + imagen adjunta "Lo que no se hace")

- **Política de datos**: sí existe, formal. **Regulación sectorial**: Bancaria.
- **8 conductas prohibidas** (imagen adjuntada por el usuario, "Ocho conductas que no se
  admiten. Ninguna la puede impedir la herramienta"):
  1. Pegar información de clientes — ni para pedir que la resuma o la ordene.
  2. Cargar documentos internos no divulgados (informes, actas, políticas, contratos, correos).
  3. Pedirle cifras al asistente — las cifras las provee el área responsable, con fecha de corte.
  4. Publicar una pieza que traiga un `[POR VERIFICAR]` sin resolver.
  5. Usarlo como fuente sobre productos o normativa del Banco.
  6. Compartir la cuenta o la contraseña — cada puesto es nominal.
  7. Publicar sin revisión de otra persona del área.
  8. Modificar el sistema de diseño sin ser su responsable.
- **Diseño del programa**: estas restricciones se respetan en el diseño curricular (todos los
  ejercicios usan datos genéricos o de ejemplo, nunca información real de clientes; las cifras
  y el sistema de diseño del banco se tratan como recursos externos aportados por el área
  responsable, no algo que el asistente genere o modifique). No se construyó una slide
  dedicada a listar estas 8 reglas en el deck — viven como principio de diseño del programa y
  se detallan en la sesión de arranque.

## Necesidad detectada (ficha Bloque D, cita textual de Andrés Pereira)

*"El equipo va a recibir una capacitación por mi parte como Gerente de IA. Sin embargo, se
busca complementar lo que yo les pueda facilitar en conjunto con la experiencia que ustedes
pueden manejar en el uso de las mejores prácticas de IA... Dos de las personas son
autodidactas y han aprendido por su cuenta la gran mayoría de su conocimiento, hay otras tres
personas que serían su primera herramienta de IA oficial de uso laboral."*

## Universo y modalidad

- **5 colaboradores** del equipo de Mercadeo — 2 autodidactas (conocimiento previo disperso),
  3 usarán una herramienta de IA de forma oficial por primera vez.
- **Modalidad**: Presencial. **Duración de sesión**: 2 horas (dato explícito del cliente).
- **Apertura al cambio**: Alta. **Patrocinio ejecutivo**: fuerte y visible (Andrés Pereira).
- **Horizonte de tiempo**: corto plazo (0-3 meses) — el banco quiere un equipo autónomo con
  estas herramientas "al 100%" en ese plazo.
- **Presupuesto**: en evaluación.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Flavia Martínez.

## Ajuste posterior (2026-09-10) — descuento por membresía AJE

Instrucción directa del usuario: aplicar **10% de descuento por ser miembro AJE** (Asociación
de Jóvenes Empresarios). El campo AcroForm `Descuento` es numérico y alimenta un cálculo
automático (`PrecioTotal = PrecioBase − Descuento`, ver `scripts/agregar-campo-precio.py`), así
que no admite texto libre como "10% AJE" sin romper esa fórmula — y el monto en dólares no se
puede precalcular hoy porque `PrecioBase` todavía está vacío (lo llena ventas).

**Solución aplicada** (sin tocar el contrato numérico del campo):
1. La etiqueta estática junto a la caja (`.cot-label-discount`, no es un campo AcroForm) pasó
   de "Descuento" a **"Descuento · 10% AJE"** — visible de inmediato en el deck.
2. La razón completa, con la sigla expandida (§4.12), quedó en `Notas`: "Descuento del 10% por
   membresía AJE (Asociación de Jóvenes Empresarios)."
3. Ventas sigue llenando `PrecioBase` y `Descuento` (en dólares, calculando el 10% sobre la
   base) en Adobe Reader, como cualquier otro campo de precio — solo cambia que ahora sabe
   **por qué** aplica ese descuento antes de escribir el número.

**Bug encontrado al aplicar esto**: agregar la línea del descuento a `Notas` empujó el texto
existente fuera de la caja — el cierre de la frase ("...incorporarse a futuras fases.") se
cortó sin aviso del detector automático (mismo blindspot ya documentado en
`bug-notas-acroform-placeholder-visible.md` y afines: el contenido de las cajas AcroForm se
hornea después del render HTML que audita `verificar-overflow.js`). Se corrigió acortando
ambas líneas de `Notas`. Regenerado el PDF completo tras el ajuste.

## Ajuste posterior (2026-09-16) — se retira Fundamentals, cargo de Andrés Pereira

Instrucción directa del usuario, con el siguiente contexto textual del cliente:

> *"El equipo ya cuenta con una base, desde la Gerencia le facilitamos una metodología de uso
> de Claude alineada al Manual de Política de Uso Interno de IA que les enviamos resumido, y
> ya tiene una primera experiencia con ella. Por eso, más que nivelar desde el inicio, buscamos
> que ustedes partan de esa base, guíen al equipo con sus mejores prácticas y nos ayuden a
> mejorar la metodología. Asimismo, la guía de buenas prácticas de la propuesta sería una
> versión fortalecida de la nuestra, que les haremos llegar al iniciar."*

**1. Se retira la sesión de Fundamentals.** El equipo ya no arranca desde cero: ya tiene una
metodología de uso de Claude entregada por la Gerencia (alineada a su Manual de Política de
Uso Interno de IA, versión resumida ya compartida con Intezia) y una primera experiencia
aplicándola. La antigua Sesión 1 ("Fundamentos y buenas prácticas del banco", 2h) se elimina.

**2. Las primeras 2 sesiones se reformulan como "Detección Estratégica".** Las sesiones que
antes eran Fundamentals (Sesión 1) + Redacción (Sesión 2) se consolidan en 2 sesiones que
parten de la base existente (metodología + política + primera experiencia) para guiar al
equipo con mejores prácticas de Intezia sobre redacción de contenidos e ideación de campañas,
y contribuir a **fortalecer** esa metodología — no construirla desde cero. Cubren los mismos
procesos 1 y 2 que antes, solo que desde un enfoque de detección/diagnóstico estratégico en
vez de nivelación genérica.

**3. Total: de 9 sesiones/18h a 8 sesiones/16h.** Ningún proceso de los 7 confirmados se
pierde — se elimina únicamente la sesión de nivelación genérica, que ya no aplica dado el
punto de partida real del equipo. Módulo II (Diseño y Adaptación Visual, 4 sesiones/8h) y
Módulo III (Marca y Tendencias, 2 sesiones/4h) quedan sin cambios.

**4. "Guía de buenas prácticas" reformulada como versión fortalecida.** El entregable
`Entregables` en `acroforms.json` pasó de "alineada a la política de datos del banco" a
"versión fortalecida de la que ya tiene el equipo, alineada a la política de datos del banco"
— refleja que Intezia parte del documento del cliente, no que construye uno nuevo desde cero.

**5. Cargo de Andrés Pereira actualizado.** De "VP. Soluciones Digitales" a **"Gerente de
Inteligencia Artificial y Analítica de Datos"**, en todas las menciones del deck (Portada no lo
nombraba directamente; principalmente Diagnóstico/página 2, Objetivos) y de la documentación
interna (`brief.md`, `programa.md`, comentario de cabecera de `index.html`). Su rol funcional
no cambia: sigue liderando la capacitación interna que esta propuesta complementa, y sigue
siendo el responsable de logística.

**6. Ajuste económico evaluado, pendiente de que ventas complete el monto.** El usuario pidió
"evaluar un ajuste de la propuesta económica para actualizar al equipo sobre ello" — se
interpretó como: reflejar la reducción de 18h a 16h en la Propuesta Económica (slide de
Duración ya actualizada), dejando que ventas recalcule `PrecioBase` en Adobe Reader según la
nueva duración (el campo sigue vacío, como siempre — §4.14). No se asume un monto ni un
porcentaje de reducción: ese cálculo es de ventas, no de este documento.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh venezolano-de-credito
python3 scripts/customize-acroforms.py venezolano-de-credito
python3 scripts/customize-venezolano-de-credito.py "clientes/propuestas/venezolano-de-credito/<PDF generado>.pdf"
```

## Pendientes

- Confirmar fechas de las 8 sesiones con Andrés Pereira.
- **2 casos de uso adicionales pendientes de validación de seguridad** (Desempeño de campañas,
  Contenidos por segmento de clientes) — no incorporados a esta capacitación; retomar cuando
  el banco resuelva la revisión de seguridad correspondiente.
- Confirmar presupuesto (en evaluación al momento del levantamiento).
