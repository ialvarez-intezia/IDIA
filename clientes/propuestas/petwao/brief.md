# Brief — PetWao

---

## Datos administrativos

- **Empresa**: PetWao (administra los programas de seguro de mascotas de más de 10 aseguradoras en Venezuela)
- **Sector**: Seguros de mascotas / salud animal (administración de programas para aseguradoras)
- **Slug**: `petwao`
- **División Intezia**: `educacion`
- **Tipo de documento**: Capacitación In-Company (`CAP-063`)
- **Eje temático**: IA con Claude en dos fases — Marketing avanzado (motor de contenido) y Agente "Veterinario Virtual" interno (asistente del centro de contacto)
- **Fecha del brief**: 2026-06-17
- **Estado**: propuesta de dos fases, ambas cotizadas en el mismo deck (cotización única)

## Contacto

- **Persona contacto**: Katty (Directora de Marketing) — datos por confirmar
- **Solicitante interno (ficha)**: Isabella Palazzone (Intezia)

## Necesidad detectada

PetWao necesita IA para dos frentes críticos del negocio:

1. **Reconstruir su departamento de marketing**, que fue disuelto y debe rearmarse desde cero. La dirección quiere operar con un **modelo mixto** (su número: ~**60% IA / 40% humano**): un equipo humano pequeño (1 líder, 2 revisores de contenido) que configura las herramientas y asegura la calidad, sobre un motor de contenido impulsado por IA. Katty ya evalúa herramientas concretas (**Blotato** para publicación automatizada, **Abroad** para posicionamiento en buscadores con IA) y quiere aprender a integrarlas con Claude.
2. **Crear un agente interno de "Veterinario Virtual"** para su centro de contacto de **25 personas**. El agente asiste a los analistas con preguntas médicas y consultas de proceso, **libera al director médico** para los casos complejos y **evita un bot de cara al público** (rechazado antes por los clientes). Es viable porque PetWao cuenta con **amplia documentación médica interna** para alimentarlo.

Los servicios de desarrollo de Intezia están copados hasta agosto, así que en lugar de construir el agente por ellos, **se capacita al equipo interno para que lo construya y lo mantenga por sí mismo** (autosuficiencia, sin dependencia de un tercero).

## Perfil del cliente (clave para el tono del deck)

Equipo **avanzado y técnico**. Katty indica amplia experiencia y estar al día con las actualizaciones; **esperan una capacitación avanzada**, no fundamentos. Cliente con altas expectativas. La propuesta debe ofrecer algo de alto valor que les enseñe cosas genuinamente nuevas (capacidades actuales de Claude: Projects, Skills y creación de Skills, conectores/Plugins, MCP), no prompting básico.

## Estructura de la propuesta (dos fases, cotización única)

- **Fase 1 · Marketing avanzado con Claude** (8 h · 4 sesiones de 2 h): reconstruir el departamento como un **motor de contenido centralizado**. Clon de marca con Claude (un Project con la voz de PetWao), producción de contenido y video, automatización de publicación integrando las herramientas que ya evalúan (Blotato, Abroad) con Claude, y el modelo operativo 60/40 (qué hace la IA, qué revisa el humano).
- **Fase 2 · Agente "Veterinario Virtual" interno** (6 h · 3 sesiones de 2 h): que el perfil técnico (Katty + el programador) **construya el agente** sobre la documentación médica interna; lo conecte (Projects/Knowledge, Skills, conectores/MCP), lo ponga a disposición de los 25 analistas y lo **mantenga de forma autónoma**.

Cada fase tiene su **propio desglose instructivo** con sus horas específicas. Total: **14 h**.

## Audiencia

- **Total**: equipo reducido (~4): Katty (Directora de Marketing) + 1 programador + 2 del departamento de mercadeo. Edades 28-40.
- **Fase 1**: el trío de marketing (Katty + 2 de mercadeo).
- **Fase 2**: perfil técnico (Katty + el programador).
- **Discrepancia a confirmar**: la ficha indica "3 participantes" pero el perfil de audiencia describe 4 (Katty + 3). Se asume ~4; confirmar en arranque.

## Decisión de herramienta (del cliente)

- **Ecosistema**: **Claude** (su licencia **Claude Pro** existente). Es su ecosistema preferido; el plan vive dentro de Claude.
- **Fase 1**: Claude (Projects, Skills, conectores) como núcleo del motor de contenido; **Blotato** (publicación) y **Abroad** (posicionamiento con IA) son herramientas que el cliente ya evalúa y se integran a Claude. No se afirma que el cliente cambie de stack (§4.11).
- **Fase 2**: Claude (Projects/Knowledge, Skills, conectores / Model Context Protocol, MCP) sobre la documentación médica interna del cliente.

## Especificaciones del programa

- **Duración**: Fase 1 = 8 h (4 sesiones × 2 h) · Fase 2 = 6 h (3 sesiones × 2 h). Total 14 h.
- **Modalidad**: **Presencial**, in-company en la oficina de PetWao, **máximo 2 h/día** (confirmado en ficha).
- **Audiencia**: Fase 1 = equipo de marketing · Fase 2 = perfil técnico.
- **Aliado**: ninguno.
- **Infraestructura del cliente**: licencia de **Claude Pro**; documentación médica interna (insumo del agente de la Fase 2).
- **Entregables esperados por el cliente** (ficha): **Workbooks + Certificados + Dashboard**.
- **Fechas tentativas**: no definidas (ficha: "No"). Se fijan en la reunión de arranque.

## Equipo asignado

- **Facilitación (ambas fases)**: Equipo INTEZIA Education.
- **Asesora comercial**: Isabella Palazzone.

## Notas internas

- Slide a la medida (WAO) en la Fase 2: **"Arquitectura del agente veterinario"** (estilo s-graph): la documentación médica interna alimenta al agente que asiste a los 25 analistas, con el director médico como escalamiento de casos complejos.
- Cliente con alto potencial de recurrencia. Ambas fases se cotizan juntas; pueden contratarse en bloque o por separado.
- Clon de `colchones-regal` (bifásico, cotización única). 21 slides.
