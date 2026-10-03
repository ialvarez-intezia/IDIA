# Brief — Puro Lomo · Introducción a la Inteligencia Artificial Generativa (CAP-090)

## Datos administrativos

- **Cliente**: Puro Lomo
- **Slug**: `puro-lomo-bajo`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-090`)
- **Programa**: Introducción a la Inteligencia Artificial Generativa
- **Eje temático**: fundamentos de IA Generativa, manejo de plataformas del mercado (ChatGPT, Gemini, Copilot, Claude), ingeniería de instrucciones (prompt engineering), aplicación en procesos corporativos y uso ético/seguridad de la información
- **Modalidad**: Presencial · sesión única de un día (mañana + tarde)
- **Duración**: 8 horas académicas
- **Lugar de impartición**: Edificio Principal Puro Lomo, Villa de Cura, Estado Aragua
- **Participantes**: 20 colaboradores
- **Fecha del brief**: 2026-08-03
- **Estado**: `Borrador`

> **Nota sobre el código**: el usuario pidió `CAP-089`, pero ese código ya está asignado y
> enviado hoy a Laboratorios Conspat (ver `clientes/propuestas/laboratorios-conspat/meta.json`).
> Se usa `CAP-090` (siguiente código libre en `clientes/INDEX.json`), confirmado con el usuario.

## Contacto

- **Persona/empresa contacto**: Puro Lomo — datos de contacto directo por confirmar.
- **Asesora comercial Intezia**: Flavia Martínez · +58 414-5756615 · fmartinez@intezia.com
- **Consultor / Facilitador**: NO se asigna en la propuesta inicial — INTEZIA designa un consultor senior con perfil en IA Generativa aplicada al confirmar el kick-off.

## Competencias esperadas (fuente: requerimiento del cliente)

El objetivo es que los colaboradores desarrollen habilidades prácticas y teóricas aplicables a su labor diaria:

1. **Comprensión de fundamentos**: qué es la IA Generativa, cómo funciona y en qué se diferencia de otros tipos de IA.
2. **Manejo de herramientas actuales**: interactuar con las principales plataformas del mercado (ChatGPT, Gemini, Copilot, Claude, entre otras) para generación de texto, ideas y análisis de datos.
3. **Ingeniería de instrucciones (Prompt Engineering)**: redactar prompts claros, precisos y efectivos.
4. **Aplicación en procesos corporativos**: identificar oportunidades de integración en tareas diarias — redacción de correos, resumen de documentos, potenciar creatividad en resolución de problemas.
5. **Uso ético y seguridad de la información**: limitaciones de la tecnología (alucinaciones), manejo responsable de datos de la empresa, privacidad.

**Formato pedido explícitamente por el cliente**: actividades prácticas y dinámicas en vivo con la IA (no una capacitación solo teórica).

## Estructura de la sesión (propuesta)

Sesión única presencial de 8h, dividida en dos bloques del mismo día en la sede de Villa de Cura:

- **Bloque mañana (4h) · Módulo I — Fundamentos y herramientas**: qué es la IA Generativa, diferencias con otros tipos de IA, panorama de plataformas (ChatGPT, Gemini, Copilot, Claude) y primeros usos prácticos.
- **Bloque tarde (4h) · Módulo II — Prompting, aplicación y uso ético**: ingeniería de instrucciones, aplicación en procesos corporativos (correos, resúmenes, ideación) y uso ético/seguridad de la información.

## Propuesta económica — traslado del facilitador (pedido explícito del cliente)

El cliente requiere que la capacitación sea presencial en su sede de Villa de Cura, **igual que
en una capacitación anterior con este cliente** (histórico no registrado en
`clientes/propuestas/` — fuera del sistema). Piden un espacio en la página de Propuesta
Económica para poder cotizar el **traslado del facilitador**.

- **Implementación**: se usa el campo AcroForm `Notas` de la slide `.s-price` (multiline,
  editable, ya pre-llenado con una nota de exclusión + espacio para que ventas escriba el monto
  cotizado), en línea con la política existente de "Traslados y viáticos... no incluidos, se
  cotizan aparte" (`empresa/politicas-comerciales.md`). No se agregó un campo AcroForm nuevo
  porque eso es un cambio estructural del PDF que requiere confirmación explícita y
  actualización en cascada (`plantillas/generar-pdf.md` §4.6) — si el usuario prefiere una línea
  de precio dedicada (campo numérico propio, no solo nota), avisar para implementarla como caso
  especial.
