# Brief — DHL (DET-004)

## Ajuste (2026-09-07) — hoja de precio vuelve al patrón estándar

Instrucción explícita del usuario: la hoja de cotización debe mostrar **solo la columna de la
derecha** (Propuesta + Inversión / Descuento / TOTAL), como se hace regularmente en el resto
del sistema — sin desglosar las 3 fases en cajas de precio separadas a la izquierda
("Inversión por fases", con `PrecioFase1/2/3`). Se revirtió al marcador estándar "Propuesta
Económica": Duración (texto de las 3 fases en una línea) + Programa (AcroForm, resume las 3
fases como bullets) + Notas + columna derecha de cotización única.

`styles.css` de este deck no tenía las reglas CSS del patrón "Propuesta Económica" (nunca las
había usado — nació directo con "Inversión por fases") — se agregaron `.block`/`.block-value`/
`.block-programa`/`.block-cotizacion`/`.programa-box`, y se movieron las posiciones de
`.block-notes-container`/`.notas-box`/`.cot-label-*`/`.base-frame`/`.discount-frame`/
`.total-frame`/`.cot-validity`/`.cot-terms-box` a las coordenadas que usa `PRECIO_FIELDS` en
`agregar-campo-precio.py` (distintas de las de `FASE_PRICE_FIELDS`) — de lo contrario las
cajas del PDF quedan desalineadas del texto visible (bug detectado y corregido en esta misma
sesión: "PROGRAMA"/"COTIZACIÓN" se montaban sobre el texto de Duración).

`customize-dhl.py` se simplificó: ya no necesita ninguna lógica de `PrecioFaseN` (ni
inyectarlos ni eliminarlos), porque el marcador nuevo no los crea.

---

> **Fuente primaria: Ficha Comercial Intezia — DHL** (levantada por Verónica Rubio,
> 2026-08-26) + precisiones directas del usuario. El código propuesto originalmente fue
> DET-005; se corrigió a DET-004 (siguiente correlativo libre — DET-001/002/003 ya usados
> por Amcor/Simple TV/Embutidos Zeus).

## Ajuste (2026-09-04) — 3 fases, menos foco exclusivo en Copilot, Claude como opción

Instrucción del usuario tras conversar con Miguel:

1. **Menos foco exclusivo en Copilot**: *"Miguel fue claro en que Copilot es la herramienta
   que ya tienen y les parece bien usarla, pero están interesados en explorar otras además
   de esa — no quieren que la propuesta quede centrada solo en Copilot."* Se revisó la
   redacción de Portada, Diagnóstico, Objetivos, Beneficios, Roadmap y Precio para que
   Copilot quede enmarcado como punto de partida, no como techo.
2. **Claude, nombrado explícitamente** (precisión posterior del usuario, misma sesión):
   *"puedes colocar que sugieres claude como otra herramienta y que hay que identificar que
   proceso va mejor con que"*. A diferencia de la corrección anterior (que dejaba la
   alternativa sin nombrar, por no inventar), aquí el usuario pidió directamente nombrar
   Claude como la herramienta a evaluar junto a Copilot — la Detección decide, proceso por
   proceso, cuál conviene. **No contradice el §4.11 de la ficha original** ("solo Microsoft,
   por ahora, sin mencionar Claude"): esa restricción reflejaba el estado del cliente en la
   ficha de agosto; esta instrucción es una actualización directa y posterior del usuario,
   con visibilidad real de la conversación con Miguel. No se afirma que DHL adopta o migra a
   Claude — se plantea como evaluación de la Detección, no como hecho consumado.
3. **Reestructuración de fases**: Fase 1 pasa a ser un solo bloque explícito de "Auditoría +
   Nivelación" (ya lo era en el cronograma real; el ajuste fue visual, en la slide 04 "El
   camino", que mostraba 3 tarjetas como si Nivelación fuera una fase aparte). Con ese
   espacio, Habilidades se divide en **Fase 2** (Automatización de compras + Análisis de
   datos, 2 sesiones/4h) y **Fase 3** (Dashboards + Seguimiento y KPIs, 2 sesiones/4h) — misma
   duración total (8h), ahora repartida en 2 fases con más foco cada una. Decisión confirmada
   con AskUserQuestion (agrupación por bloque operativo/estratégico; las 3 fases cotizadas
   ahora, mismo criterio que ya regía para las 2 anteriores).
4. **Alcance ampliado dentro de Habilidades**: Fase 3 agrega explícitamente "espacio para
   capacitar otros procesos de Mantenimiento e Infraestructura que la Fase 1 identifique" —
   no solo los 4 temas ya conocidos. No se inventan esos procesos adicionales (mismo
   principio ya aplicado en `good-latam-cai010/` y `bidzi/`): quedan como alcance abierto,
   con Copilot o Claude como opciones según lo que revele la auditoría.

**Cambio técnico de precio**: con 3 fases reales, el marcador "Inversión por fases" ya no
necesita eliminar ningún `PrecioFaseN` huérfano — `agregar-campo-precio.py` inyecta
PrecioFase1/2/3 y su cálculo por defecto ya suma las 3. `customize-dhl.py` se simplificó
(ya no elimina PrecioFase3).

**Estado**: `En corrección` (la propuesta ya estaba "Enviada"; vuelve a revisión por este
ajuste — al regenerar el PDF vuelve a "Enviada").

## Ajuste (2026-09-03) — Fase 2 ya desarrollada y cotizada

Al cliente le gustó la Fase 1 de Detección presentada y pidió ver la ruta completa hasta
Habilidades, para presentarla ante su Dirección y evaluar la aprobación del proyecto completo.
Fuente: nueva Ficha de Levantamiento Intezia — DHL (2026-09-20, Verónica Rubio, cliente Miguel
Hernandez), con el **Bloque específico de Habilidades ya lleno** (antes diferido). Se preguntó
y se confirmó:

1. **Duración de Fase 2**: 4 sesiones de 2h (8h), una por tema.
2. **Cotización**: ambas fases (Detección + Habilidades) cotizadas ya, en el mismo documento
   — reemplaza el esquema anterior de "Fase 2 se cotiza tras el diagnóstico". Esto permitió
   volver al marcador estándar "Inversión por fases" de 2 filas (mismo patrón que Simple TV
   DET-002 y Embutidos Zeus DET-003), sin necesitar campos AcroForm custom.

**4 temas de Fase 2 (ficha, Bloque específico Habilidades)**: (1) automatización de órdenes de
compra por gasto/estación, (2) análisis de datos sobre su sistema de gestión de mantenimiento,
(3) generación y actualización de dashboards de mantenimiento, (4) seguimiento y KPIs.
Modalidad: virtual, mismo equipo de Mantenimiento e Infraestructura ya auditado en Fase 1.

**Estado**: `En corrección` (la propuesta ya estaba "Enviada" el 2026-08-30; vuelve a revisión
por este ajuste — al regenerar el PDF vuelve a "Enviada").

## Datos administrativos

- **Empresa**: DHL, división Express
- **Sector**: Logística y envíos · Mediana (50-250 empleados, unidad local)
- **Slug**: `dhl`
- **División Intezia**: `educacion`
- **Servicio** (Modelo Intezia): `deteccion` — combo de 2 servicios (Detección + Habilidades)
  cotizados juntos en el mismo documento sigue siendo `deteccion`, no un valor nuevo (§4.1a
  punto 1)
- **Código**: `DET-004`
- **Eje temático**: diagnóstico y automatización de los procesos de tickets de mantenimiento y
  órdenes de compra, con Copilot, dentro del entorno Microsoft 365
- **Fecha del brief**: 2026-09-03 (ajuste de la versión anterior, 2026-08-30)
- **Estado**: `En corrección` (la propuesta ya estaba "Enviada"; vuelve a revisión por este
  ajuste — al regenerar el PDF vuelve a "Enviada")

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Cliente / interlocutor**: Miguel Ángel Hernández Armijo · Head de Mantenimiento, división
  Express de DHL · miguelangel.hernandezarmijo@dhl.com. Dato interno — **no se nombra en el
  deck** (mismo criterio que Amcor/Jomar Vizcaya: el deck habla de "el equipo de
  Mantenimiento e Infraestructura", nunca del nombre del interlocutor).
- **Servicio previo con Intezia**: no, es el primer contacto.

## Estructura del proyecto (3 fases, las 3 cotizadas)

- **Fase 1 · Detección + Nivelación, en un solo bloque.** Diagnostica procesos y madurez
  digital para identificar oportunidades de IA de alto ROI, y en paralelo nivela al equipo
  en Copilot. Entregables: matriz de madurez digital, quick wins (mejoras de valor tangible
  durante la auditoría), capacitación de nivelación (Copilot, dentro de su entorno
  Microsoft), y un roadmap priorizado que indica, proceso por proceso, si conviene Copilot o
  Claude.
- **Fase 2 · Habilidades I — Automatización y datos (2 sesiones de 2h, 4h)**: automatización
  de órdenes de compra y análisis de datos del sistema de gestión de mantenimiento.
- **Fase 3 · Habilidades II — Dashboards y más procesos (2 sesiones de 2h, 4h)**: dashboards
  de mantenimiento y seguimiento con KPIs, más espacio abierto para capacitar otros procesos
  de Mantenimiento e Infraestructura que la Fase 1 identifique (ajuste 2026-09-04, ver
  arriba) — sin inventar esos procesos, quedan como alcance a definir tras la auditoría.
  El objetivo del reporte final de Fase 1, según la ficha original, era justamente "tener en
  claro cómo empezar con el servicio de Habilidades" — la ficha de 2026-09-20 ya trae el
  contenido conocido definido (4 temas), y el ajuste 2026-09-04 deja abierto que la
  auditoría sume más.

## Contexto y pain points (Ficha Comercial, Bloques B/C/D + instrucciones del usuario)

- El equipo de Mantenimiento e Infraestructura (25-35 años) tiene conocimientos básicos de
  IA, pero le falta habilidad para automatizar procesos. Hoy usan **Microsoft Copilot
  básico**, insuficiente para automatización avanzada (agentes, análisis de datos).
- **Proceso auditado**: generación de tickets de mantenimiento a través de un sistema de
  gestión (SaaS) → la mesa de infraestructura recibe y procesa el ticket → análisis de
  costos, gestión de proveedores y generación de compra → el análisis y seguimiento se
  llevan en **Excel manual** → se generan órdenes de compra en la plataforma de compras.
  Frecuencia diaria, ~480 horas en 20 días, ~10 personas (3 ejecutores, 3 analistas, 3
  coordinadores).
- **Cuello de botella principal**: el proceso manual en Excel genera errores, pérdida de
  tiempo y resulta poco profesional para una función crítica (ej. generación de órdenes de
  compra). Tipo de dato: confidencial.
- **Objetivo de Miguel**: profesionalizar a su equipo, que pase de la ejecución técnica pura
  a roles más estratégicos y tácticos.
- Áreas priorizadas: Mantenimiento (responsable: Miguel) e Infraestructura (sin responsable
  registrado en la ficha).

## Restricciones (Ficha Comercial, Bloque E)

1. **Solo Microsoft, por ahora** (dato de la ficha original, agosto 2026). El entorno del
   cliente es Microsoft 365, ya con Copilot en uso (básico). **Actualizado 2026-09-04**: el
   usuario confirmó, tras conversar con Miguel, que sí se puede nombrar a Claude como
   herramienta a evaluar junto a Copilot — la Detección decide cuál conviene por proceso.
   Sigue sin afirmarse que DHL adopta o migra a Claude (§4.11): se plantea como evaluación
   de la Detección.
2. **Política de datos/seguridad**: sí pasa por validación de datos; cualquier plataforma
   nueva requiere aprobación legal.
3. **Regulación sectorial**: sí, procesos de aduanas.
4. **Presupuesto**: ya aprobado/asignado. **Apertura al cambio**: alta. **Patrocinio
   ejecutivo**: presente pero descrito como "tibio" — Verónica lo tiene en cuenta para el
   seguimiento comercial, no cambia el contenido del deck.
5. **Horizonte**: mediano plazo (3-12 meses).

## Bloque específico de Detección (Ficha Comercial)

- **Áreas a auditar**: solo Mantenimiento e Infraestructura.
- **Stakeholder clave**: Miguel Hernandez (Gerente de Mantenimiento). Sin nombre de los
  gerentes senior de Infraestructura.
- **Personas por área**: 12 (la ficha no aclara si es total o por área); se usa en el deck
  la cifra más concreta del inventario de procesos (~10 personas: 3 ejecutores, 3 analistas,
  3 coordinadores) para no inflar ni comprometer una cifra ambigua.
- **Diagnóstico previo**: no.
- **Modalidad de sesiones**: Virtual (a diferencia de Amcor, que era presencial).
- **Sedes**: colaboradores repartidos a nivel nacional en México.
- **Calendario por área**: 2 horas.
- **Urgencia/disparador**: presión de Miguel, como gerente senior, hacia su director.
- **Expectativa de madurez**: optimizar sus procesos con IA.
- **Quién decide**: Miguel y el director del área de Mantenimiento e Infraestructura.
- **Quick win identificado**: sin respuesta registrada en la ficha — se mantiene genérico en
  el deck ("quick wins identificados durante la auditoría"), sin comprometer uno específico.
- **Objetivo del Reporte Final**: tener en claro cómo empezar con el servicio de Habilidades.
- **Definición de éxito del cliente**: que realmente tengan una transformación.

## Bloque específico de Habilidades (Ficha de Levantamiento 2026-09-20)

- **4 temas** (una sesión de 2h por tema, 8h total): (1) automatización de órdenes de compra
  por gasto/estación, (2) análisis de datos sobre su sistema de gestión de mantenimiento, (3)
  generación y actualización de dashboards de mantenimiento, (4) seguimiento y KPIs.
- **Modalidad**: Virtual en vivo, mismo equipo de Mantenimiento e Infraestructura auditado en
  Fase 1.
- **Herramienta**: Copilot, dentro del entorno Microsoft 365 ya existente, evaluando también
  Claude según el proceso (ajuste 2026-09-04) — §4.11 sigue aplicando: no se afirma adopción
  de stack nuevo, solo evaluación caso por caso.
- **Objetivo**: que el equipo pase de ejecución técnica pura a un rol más estratégico y
  táctico, resolviendo con IA los mismos cuellos de botella que prioriza la Fase 1.

## Propuesta económica

- **Hoja "Inversión por fases"** (`.s-price`): **Fase 1, Fase 2 y Fase 3, las 3 con caja de
  precio editable** (`PrecioFase1/2/3`) — ajuste 2026-09-04. Con 3 fases reales, el marcador
  ya no necesita eliminar ningún campo huérfano: `agregar-campo-precio.py` inyecta las 3
  cajas y su cálculo por defecto (`make_fase_subtotal_js(3)`) ya las suma.
  `customize-dhl.py` se simplificó (ya no quita `PrecioFase3`).
- Vigencia: 30 días. Sin montos, anticipos ni condiciones de pago en el deck (§4.15).

## Notas de diseño

- Base: mismo archivo (esquema nuevo 2026-08-26, mismo patrón de Detección; enlaza
  `styles.css` local, no `_base/`). Ajuste 2026-09-03: Fase 2 pasa de placeholder genérico a
  contenido real. Ajuste 2026-09-04: Fase 1 se muestra como un solo bloque (Auditoría +
  Nivelación) en la slide "El camino"; Habilidades se divide en Fase 2 (Automatización y
  datos) y Fase 3 (Dashboards y más procesos, con alcance abierto); roadmap suma un 3er nodo
  (`.rmx-node-f4`/`.rmx-card-f4`, agregado a `styles.css` — antes solo soportaba 2); hoja de
  precio pasa de 2 a 3 filas reales; se suaviza el foco exclusivo en Copilot y se nombra a
  Claude como alternativa a evaluar por proceso. 13 slides (antes 12 — se agrega 1 slide de
  Cronograma para la nueva Fase 3).
- **Beneficios por servicio (Detección + Habilidades)**: label "Por qué Detección y
  Habilidades"; Entregables ahora incluye Certificado de participación INTEZIA (mismo criterio
  que Embutidos Zeus DET-003: al haber una capacitación real de 8h, ya no es Detección pura).
- **Impacto (§4.9)** — fuentes reales citadas verbatim:
  - McKinsey & Company, *Prediction at scale: How industry can get more value out of
    maintenance* (2021): el mantenimiento predictivo basado en IA puede reducir hasta 50% el
    tiempo de inactividad y entre 10% y 40% los costos de mantenimiento.
  - Microsoft, *Work Trend Index 2024* (mismo dato que Amcor, reutilizable — mismo entorno
    Microsoft/Copilot): 77% de usuarios empresariales reportó aumento medible de
    productividad; 29% más rápidos en tareas de búsqueda, redacción y resumen.
- **No expuesto en el deck**: nombre del interlocutor (Miguel), nombre del sistema de
  gestión de mantenimiento (SaaS) si no aporta a la venta, cifras internas que no sean las
  ya usadas como gancho del diagnóstico (480h/20 días, ~10 personas).

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh dhl
python3 scripts/customize-acroforms.py dhl
python3 scripts/customize-dhl.py "clientes/propuestas/dhl/<PDF generado>.pdf"
```
