# Guía de redacción — copy de cara al cliente

> **v1.1 · 2026-06-10 · validada con Isaac** (A/B sobre 3 slides reales: metodología y
> módulos aprobados; hook calibrado a "punto medio", ver §3.2).
> Complementa las prohibiciones de `CLAUDE.md` §4.8–4.13 (qué NO hacer) con el oficio
> positivo (qué SÍ hace que una propuesta venda). Se carga al redactar el contenido de
> cualquier deck, igual que `empresa/marca-visual.md` se carga para lo visual.
>
> **Procedencia:** auditoría de redacción de las 5 propuestas cerradas en 2026
> (venemergencia, damasco, tu-herraje, crediya, cashea). Todos los ejemplos ✓ son
> verbatim de esos decks. Los decks entregados no se tocan: esta guía aplica a futuro.

---

## 1. Principio rector

La persuasión de Intezia no es hype de vendedor: es **concreción sobre el cliente**.
Una frase persuade cuando el gerente la lee y piensa "esto lo escribió alguien que
entiende mi empresa". El tono es sobrio y ejecutivo; el músculo persuasivo es el dato
observado, nunca el adjetivo.

---

## 2. Reglas de oro (extraídas de las propuestas que cerraron)

### 2.1 Detalle observado > afirmación general

Lo que más cierra es la evidencia de que conocemos SU operación.

- ✓ Damasco: «entre 60 y 100 referencias nuevas cada viernes, precios que cambian a
  diario y del orden de 100.000 facturas al día entre 54 sucursales».
- ✓ Tu Herraje: «El equipo de Ventas se turna semanalmente para contestar Instagram y
  rompe la línea eficaz de atención».
- ✓ Cashea: «Cashea repite dos palabras en cada conversación: necesita una adopción de
  IA escalable y persistente».

**Regla:** la slide de dolor lleva 2–3 datos operativos reales del cliente (volúmenes,
frecuencias, quién hace qué hoy). Si el `brief.md` no los trae, **pedirlos antes de
redactar** — es pregunta de contenido, como las de capacidad de cajas.

### 2.2 El cliente se teje en todo el deck, no solo al inicio

Anti-patrón detectado (venemergencia): el nombre y el mundo del cliente aparecen fuerte
en portada y diagnóstico, y desaparecen desde el programa en adelante («Casos reales de
su área», «su trabajo»).

**Regla:** el nombre del cliente o el vocabulario de su sector aparece también en los
módulos, la metodología y el hook de impacto. En retail se habla de referencias y
sucursales; en emergencias, de turnos y despacho; en fintech, de operaciones y crédito.

### 2.3 Honestidad comercial como voz de marca

Las frases que más confianza generaron en el corpus son las que **limitan la promesa**:

- ✓ «la integración custom queda como roadmap a Fase 2, sin presión comercial».
- ✓ «roadmap claro de Fase 2 para integrar Claude cuando el negocio lo amerite».
- ✓ «Intezia no define el alcance de integración antes de conocer los flujos reales
  del equipo».

**Regla:** donde el deck plantea una decisión de alcance o fases, incluir UNA frase de
este tipo. Es la voz más distintiva de Intezia: consultor que entiende la compra, no
vendedor que empuja.

### 2.4 Ritmo: corto para el dolor, largo para el contexto

- Dolor y hooks: frases de 7–12 palabras. ✓ «Capacitar una vez no escala. Cada nuevo
  ingreso vuelve a empezar de cero.»
- Portada y objetivos: una frase larga con cadencia (enumera, pausa, conclusión) está
  bien; es donde el deck "narra".
- Si el dolor quedó en párrafos de 30+ palabras, reescribir en seco.

### 2.5 Resultado tangible, no adjetivo

- ✓ «Lo que se practica en la sesión se aplica al día siguiente.»
- ✓ «matriz de alineación, plantillas de prompts, Custom GPT personal y checklist de
  seguridad» (artefactos con nombre).
- ✗ «redacción profunda», «escala especializada», «nivel visual alto», «punto único de
  contacto» (adjetivo o frase corporativa sin ancla).

**Regla:** todo adjetivo de calidad (profundo, avanzado, especializado, de alto nivel)
se sustituye por el artefacto, dato o escena concreta que lo prueba.

---

## 3. Tics robóticos a vigilar (detectados en el corpus)

### 3.1 «No es X: es Y» — máximo UNO por deck

El tic número 1: apareció 3–5 veces por deck y en los 5 decks auditados. Usado una vez
es un reframe potente; repetido suena a plantilla de coaching. **Reservarlo para el hook
de impacto O el dolor, nunca ambos.** Variantes que cuentan para el cupo: «X no es Y,
es Z», «Un sistema, no un taller», «no será X, sino Y».

### 3.2 Frases viajeras — prohibido reutilizarlas (lista viva)

Frases ya vendidas a 2+ clientes distintos. Si dos clientes comparan decks, se nota; y
dentro del sistema son la principal fuente de "olor a plantilla". Cada deck nuevo redacta
su propia versión con el dato y vocabulario de SU cliente:

| Frase viajera | Vista en |
|---|---|
| «La diferencia no es la herramienta, es saber usarla» | damasco, crediya, cashea |
| «La evidencia no deja lugar a dudas» (título de Impacto) | venemergencia, crediya, cashea CAP-005 |
| «No se limita a exponer: trabaja codo a codo / contigo» | venemergencia, damasco, crediya |
| «Lo que se practica se aplica al día siguiente» | venemergencia, damasco |
| «A dónde llevamos …» (título de Objetivos, mismo armado) | los 5 decks |

**Mantenimiento:** al detectar una frase repetida en un segundo cliente, agregarla aquí.
Antes de entregar: `grep` del hook nuevo sobre `clientes/propuestas/*/index*.html` para
confirmar que no existe ya.

**Cómo se re-acuña un hook (calibrado con Isaac, A/B 2026-06-10):** la fuerza del hook
está en el **ritmo de aforismo** — un giro corto (≤ ~15 palabras) que reencuadra. Lo que
estaba mal era reciclarlo entre clientes, no su brevedad. Al re-acuñar: mantener el
formato aforismo y anclarlo con **UNA sola referencia al cliente** (nombre, cifra del
programa o un elemento de su operación). Nunca estirarlo a narrativa larga.

- ✗ Viajera (reciclada a 3 clientes): «La diferencia no es la herramienta, es saber usarla.»
- ✗ Sobre-corregida (perdió el ritmo): «Las que lo logran hicieron lo que CrediYA está
  por hacer: convertir el talento de una persona en un método que toda la operación
  puede repetir.»
- ✓ Punto medio: «La herramienta ya la tienen todos: el método es lo que CrediYA
  construye en estas 10 horas.»

### 3.3 Estrategias pedagógicas calcadas

«Demostración guiada en vivo · Preguntas socráticas · Construcción guiada paso a paso»
son **ejemplos** de las plantillas de diseño, no valores fijos; hoy se copian verbatim en
todos los decks. **Regla:** en cada sesión, al menos una de las tres estrategias nombra
material del cliente: «Análisis de casos de despacho de emergencias», no «Análisis de
casos reales».

### 3.4 Muletilla «Casos reales de [X]»

Apareció hasta 15 veces en un solo deck. Máximo 2 por deck; el resto en lenguaje
natural variado: «situaciones que viven a diario», «problemas de su operación», «sus
propios documentos».

### 3.5 Tríada Saber / Saber hacer / Saber ser

La estructura es canónica (perfil de egreso de las plantillas de diseño) y **se queda**.
Lo que no se queda es el contenido genérico: cada línea se redacta con el objeto del
cliente. ✗ «Saber hacer: aplica las herramientas a su trabajo» · ✓ «Saber hacer: conecta
Claude a los reportes de servicio que hoy arma a mano».

### 3.6 Mantra propio repetido sin variación

Si una metáfora del deck («piso común», «en cascada», «segundo cerebro») aparece más de
3 veces, variar la formulación en las siguientes apariciones. La metáfora es buena; el
calco textual la gasta.

---

## 4. Checklist de redacción (correr antes del verificador de overflow)

- [ ] ≥3 datos operativos del cliente en el deck; la slide de dolor concentra 2
- [ ] Cliente o vocabulario de su sector presente en: dolor, objetivos, ≥2 módulos, metodología, hook de impacto y cierre
- [ ] Un solo «No es X: es Y» (y variantes) en todo el deck
- [ ] Hook de impacto redactado a medida: `grep` confirma que no existe en decks anteriores
- [ ] Cero frases de la tabla §3.2
- [ ] Adjetivos sin ancla sustituidos por artefacto/dato/escena concreta
- [ ] Una frase de honestidad comercial donde haya decisión de alcance o fases
- [ ] Prueba de voz alta: leer dolor y cierre — ¿lo diría un consultor en una reunión, o suena a folleto?
