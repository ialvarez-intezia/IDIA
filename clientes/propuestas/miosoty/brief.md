# Brief — Miosoty Villalobos (CAI-006)

> **Confidencialidad — bloqueante, leer antes de tocar cualquier archivo de esta carpeta.**
> El nombre real de la organización **no se registra en ningún archivo de este sistema**
> (ni aquí, ni en `programa.md`, ni en `index.html`, ni en `aprendizajes.md`, ni en memoria
> persistente) — instrucción explícita de la contacto comercial, Miosoty Villalobos, dada la
> alta sensibilidad de la información que maneja su organización. Toda la documentación
> (incluida la Ficha Comercial oficial de Intezia) se registra a nombre de **Miosoty
> Villalobos**, tratándola como si fuera el nombre del cliente/empresa en todo lugar donde
> normalmente iría el nombre de la organización. Si en algún momento se necesita referirse al
> tipo de entidad, se usa únicamente la descripción genérica ya autorizada por ella en la
> Ficha Comercial: **"sector público, servicios de apoyo logístico para otras gerencias"** —
> nunca un nombre propio, sector específico más detallado, ni ninguna pista adicional.

## Datos administrativos

- **Cliente (nombre a usar en todo el sistema)**: Miosoty Villalobos
- **Sector (descripción autorizada, textual de la Ficha Comercial)**: Público, servicios de
  apoyo logístico para otras gerencias — equipo de logística dentro de una organización
  mayor (tamaño real de la organización: no se registra; el equipo objetivo es de 10 a 20
  personas dentro de un departamento de logística más amplio)
- **Slug**: `miosoty`
- **División Intezia**: `educacion` (decisión confirmada con el usuario 2026-08-30: pese a
  que el sector es "Público" según la Ficha Comercial, se trata de capacitación corporativa
  profesional pagada con roles gerenciales, no de una ONG/comunidad — encaja mejor en
  Educación que en Fundación)
- **Servicio (Modelo Intezia)**: `habilidades` — confirmado en la Ficha Comercial ("El
  cliente se orienta hacia el servicio de Habilidades")
- **Código**: `CAI-006`
- **Eje temático**: IA generativa aplicada a planificación financiera, seguimiento de
  indicadores y presentaciones gerenciales, con manejo responsable de información sensible
- **Fecha del brief**: 2026-08-30
- **Estado**: Borrador
- **Fuente primaria**: Ficha Comercial Intezia — Miosoty Villalobos (Verónica Rubio,
  2026-08-27) + minuta de reunión (instrucciones directas del usuario, 2026-08-30)

## Contacto

- **Asesora de ventas**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Contacto / cliente**: Miosoty Villalobos, líder de planificación · miosotylarte@gmail.com

## Restricción crítica — condiciona todo el diseño del programa

La alta seguridad de la información que maneja el equipo **impide usar herramientas
públicas** (ej. Gemini) por el riesgo de que la información se haga pública. Por eso el
programa recomienda **Claude** como herramienta de referencia — por instrucción del
usuario, se menciona **una sola vez**, en el módulo de fundamentos, sin repetirla a lo largo
de todo el deck. El resto del contenido usa lenguaje genérico ("IA generativa") y enmarca el
manejo de información sensible como un criterio transversal del programa, no solo como
elección de herramienta.

## Equipo y contexto (Ficha Comercial + minuta, sin datos que identifiquen la organización)

- **Universo**: 10 a 20 personas — Gerentes, Líderes, Analistas Senior.
- **Nivel de partida**: heterogéneo — algunos ya usan IA con soltura, otros no la usan.
- **Formación previa en IA**: ninguna.
- **Stack actual**: Microsoft 365 (Excel, PowerPoint), correo interno autorizado. La
  información vive principalmente en hojas de cálculo. Sin IA en uso actualmente.
- **Modalidad**: virtual en vivo (confirmada tanto en la ficha como en la minuta).

## Procesos objetivo (Bloque C de la Ficha Comercial)

1. **Planificación financiera**: 40 horas al mes consolidando datos de forma manual, con
   alto riesgo de error en los números entregados. Frecuencia mensual, 10 personas
   involucradas. Cuello de botella: % de error, control y seguimiento de tareas. Objetivos
   adicionales explícitos: mejorar las presentaciones (hacerlas "inteligentes"), mejorar los
   tiempos de entrega de indicadores, homologar formatos entre el equipo, "algo con calidad".
2. **Gestión de seguimiento**: proceso diario y continuo (finanzas, ejecutores, indicadores,
   informes), 40 horas/semana, 10 personas. Cuello de botella: tiempos de respuesta.

## Logística de la capacitación (minuta del usuario, 2026-08-30)

- **Modalidad**: virtual en vivo.
- **Frecuencia**: 2 sesiones por semana, de 2 horas cada una (4h/semana).
- **Duración total confirmada con el usuario**: 4 semanas · 8 sesiones · 16 horas totales,
  organizadas en 4 módulos (2 sesiones por módulo).
- **Presupuesto**: dato interno de negociación (el equipo lo financia de forma proactiva,
  posible escalamiento a financiamiento institucional más adelante) — **no se menciona en
  el deck** (§4.15, además de la propia política de confidencialidad de este caso).
- **Nota de proceso**: la ficha registra "tareas reales a trabajar: sí, después de firmar
  DNI" (probable acuerdo de confidencialidad interno del cliente) — dato de proceso, no se
  menciona en el deck.

## Decisiones confirmadas con el usuario (2026-08-30)

1. **Nombre en el deck**: "Miosoty Villalobos" en el lugar de cliente/empresa (portada, pie
   de página, contacto) — mismo tratamiento que ya usa la Ficha Comercial oficial.
2. **Duración total**: 4 semanas, 8 sesiones de 2h, 16h totales, 4 módulos.
3. **División**: Educación.

## Notas de diseño

- Base clonada de `cavedatos/` (mono-fase, `../_base/styles.css` + `overrides.css` local,
  Beneficios v3, Cierre escalera, sin Metodología ABR ni Equipo facilitador — §4.10a).
  Extendido de 2 sesiones (patrón cavedatos) a **8 sesiones** (2 por módulo, 4 módulos),
  dado el volumen del programa (16h).
- **Impacto (§4.9)** — fuentes reales citadas verbatim:
  - MIT Sloan (Chloe Xie) y Stanford Graduate School of Business (Jung Ho Choi), *Human + AI
    in Accounting: Early Evidence from the Field*, 2025: la IA generativa reduce hasta 7.5
    días el tiempo de cierre financiero mensual y mejora en 12% el nivel de detalle de los
    reportes.
  - LayerX, *Enterprise AI and SaaS Data Security Report*, 2025: 53% de las organizaciones
    identifica la privacidad de datos como su mayor obstáculo para adoptar IA; 40% de las
    cargas en herramientas de IA generativa incluye datos sensibles (PII/PCI).
- **Precio**: hoja estándar (`PRECIO_FIELDS`), sin variante especial.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh miosoty
python3 scripts/customize-acroforms.py miosoty
python3 scripts/customize-miosoty.py "clientes/propuestas/miosoty/<PDF generado>.pdf"
```
