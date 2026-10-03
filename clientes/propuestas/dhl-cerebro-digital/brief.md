# Brief — DHL · Cerebro Digital para Miguel (CAI-005)

> Propuesta **adicional e independiente** a la de Detección para el equipo de Mantenimiento
> e Infraestructura (`clientes/propuestas/dhl/`, DET-004) — sin referencias cruzadas entre
> ambos documentos (decisión del usuario, 2026-08-30). Base clonada de
> `clon-digital-claude/` (CAP-060), producto de catálogo genérico "Crea tu Clon Digital con
> Claude", personalizado aquí para un participante único.

## Datos administrativos

- **Empresa**: DHL, división Express
- **Slug**: `dhl-cerebro-digital`
- **División Intezia**: `educacion`
- **Servicio (Modelo Intezia)**: `habilidades`
- **Tipo de documento**: Capacitación In-Company (`CAI-005` — el usuario propuso CAI-003,
  ya usado por Simple TV; siguiente correlativo libre de la serie CAI-, que ya usa desde
  Yoyokids CAI-004). Nota de catálogo: por la definición estricta (`Taller` = foco en
  participante individual, `Capacitación` = foco en equipo), esto calzaría como Taller —
  el usuario confirmó explícitamente mantener la serie CAI-/Capacitación de todas formas.
- **Eje temático**: Cerebro Digital personalizado sobre Claude (Projects, Skills,
  Conectores/Plugins/MCP, Cowork) + conocimiento organizado como grafo en Obsidian, para un
  líder ejecutivo individual (no un equipo).
- **Fecha del brief**: 2026-08-30
- **Estado**: Borrador

## Contacto

- **Asesora de ventas**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com
- **Participante / cliente**: Miguel Ángel Hernández Armijo · Head de Mantenimiento,
  división Express de DHL · miguelangel.hernandezarmijo@dhl.com. **A diferencia de DET-004,
  aquí SÍ se nombra explícitamente en el deck** (decisión del usuario): el producto es
  personalizado para él como individuo, no para su equipo.

## Qué es esta propuesta

Además de la propuesta de Detección para su equipo, se le ofrece a Miguel un producto
distinto: una IA personalizada para él como líder ejecutivo, que centraliza todo su
contexto y conocimiento, construida sobre **Claude** y **Obsidian**. Simplifica los prompts
y automatiza la selección de herramientas, dando una IA más potente y sin fricción. Se
renombra de "Clon Digital" (nombre del producto de catálogo original) a **"Cerebro
Digital"** para esta propuesta.

## Decisiones confirmadas con el usuario (2026-08-30)

1. **Código/tipo**: CAI-005, Capacitación In-Company (no Taller, pese a ser 1 solo
   participante — decisión explícita del usuario).
2. **Nombrar a Miguel**: sí, explícitamente, en todo el deck (portada, mensajes, cierre).
3. **Duración**: se mantiene igual al producto de catálogo — 6 horas en 3 sesiones de 2 h.
4. **Relación con DET-004**: documento completamente independiente, sin mencionarlo.

## Adaptación del producto de catálogo (CAP-060 → CAI-005)

- **Nombre**: "Clon Digital" → **"Cerebro Digital"** en portada, títulos y mensajes de
  venta. El término técnico "clon" se conserva donde describe el mecanismo (el Project de
  Claude que actúa como agente), ya que el Módulo II literalmente construye "el cerebro"
  (base de conocimiento) de ese Cerebro Digital — no hay contradicción.
- **Tono**: de "tú" genérico (catálogo, público amplio) a "usted" / tercera persona con el
  nombre de Miguel (propuesta personalizada, ejecutiva).
- **Esquema visual actualizado** (el genérico es de 2026-06-16, anterior al esquema nuevo de
  §4.10a): se retira la slide de Metodología ABR (`.s-orange`) y el bloque "Equipo
  facilitador" de Beneficios; Beneficios pasa a formato v3 (Resultados / Por qué Habilidades
  / Entregables / Valor inmediato); Cierre pasa a formato escalera editable con la asesora
  Verónica Rubio (el genérico no tenía asesora, era de catálogo sin cliente); cotización
  actualizada de "válido 7 días en divisas" (formato viejo) al estándar vigente: 30 días +
  bloque de términos y condiciones.
- **13 slides** (14 del genérico menos la slide de Metodología ABR retirada).
- **Impacto (§4.9)**: se mantienen las mismas fuentes del genérico (son datos generales de
  adopción de IA, no específicos de audiencia) — Stanford HAI AI Index Report 2026, McKinsey
  The State of AI 2025, Anthropic Economic Index 2025.
- **Slide a la medida `.s-graph`** ("Su segundo cerebro", grafo relacional en Obsidian) se
  conserva del genérico casi sin cambios — el copy alrededor ya personaliza el mensaje;
  las etiquetas de los nodos del grafo se mantienen genéricas (Conocimiento, Proyectos,
  Procesos, Voz y criterio, Skills, Plugins) por ser parte de un SVG decorativo de posiciones
  fijas, no texto de venta.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh dhl-cerebro-digital
python3 scripts/customize-acroforms.py dhl-cerebro-digital
python3 scripts/customize-dhl-cerebro-digital.py "clientes/propuestas/dhl-cerebro-digital/<PDF generado>.pdf"
```
