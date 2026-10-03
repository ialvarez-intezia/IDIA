# Brief — Velas 3N (DET-013)

## Datos administrativos

- **Empresa**: Velas 3N
- **Sector**: Manufactura — producción de velas
- **Tamaño**: Mediana (50-250 empleados)
- **Slug**: `velas-3n`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `deteccion`
- **Tipo de documento**: Detección (`DET-013`) · Fundamentals (2h grupal) + auditoría de 4
  áreas, 4 horas por área (18h totales), modalidad virtual.
- **Eje temático**: Entender el nivel de madurez de IA de Velas 3N y dar a los líderes de sus
  4 áreas una inducción clara para manejarla con criterio, integrando el desarrollo de IA que
  ya construyen dentro de su ERP Odoo.
- **Fecha del brief**: 2026-09-14
- **Alianza**: no

## Fuente primaria

Este brief se construyó a partir de la **Ficha de Levantamiento Velas 3N**
(`Levantamiento_Velas_3N_2026-09-10.pdf`, registrada 2026-09-10), elaborada por la asesora
**Verónica Rubio**.

## Contacto

- **Asesora comercial Intezia**: Verónica Rubio · +58 422 3355505 · vrubio01@intezia.com.
- **Contacto cliente**: César Rondón · cargo por confirmar. Participa activamente en la
  reunión, pero **no se confirmó si es quien firma la contratación final** — las aprobaciones
  se manejan caso por caso.
- **Servicio previo con Intezia**: ninguno — primer contacto. Primer acercamiento a IA de
  cualquier proveedor (nunca recibieron una propuesta de IA, ni de Intezia ni de terceros).

## Decisiones confirmadas con el usuario (2026-09-14)

1. **4 áreas, sesión grupal por gerencia** (no 10 por coordinación individual): la ficha lista
   4 "Area priorizada" a nivel de gerencia, cada una agrupando varias coordinaciones. Se
   confirmó auditar a ese nivel (gerente + sus coordinadores juntos en una sola sesión por
   gerencia), mismo patrón de sesión grupal ya usado con `igamcor/`. Alternativa descartada:
   desglosar en las ~10 coordinaciones individuales (habría llevado a 42h en vez de 18h) —
   demasiado para una mediana empresa con presupuesto aún sin definir.
2. **4 horas de Detección por área** (16h) + **Fundamentals de 2h grupal** para los líderes y
   coordinadores de las 4 áreas (una sola sesión, dentro del máximo de 25 del lineamiento) =
   **18h totales**.
3. **Sin cifra exacta de universo/headcount**: la ficha trae un número ambiguo y sin confirmar
   específicamente para Velas 3N ("mencionan 153 y luego 200 y pico, grupo completo, varias
   empresas"). Confirmado con el usuario: el deck no compromete una cifra — habla de "los
   líderes de las 4 áreas y sus coordinadores" sin número exacto (mismo criterio de "omitir,
   no inventar" ya aplicado a otros datos sin confirmar).
4. **Herramienta: Gemini mencionado solo como contexto, sin recomendación firme** — a
   diferencia de otras Detecciones de esta sesión, aquí no hay un "campeón" personal de
   ninguna herramienta (el cliente "aún no lo sabe, espera la recomendación"). Se menciona el
   ecosistema Google Workspace ya en uso y el uso informal de Gemini por el equipo de
   Mercadeo como punto de partida natural a evaluar, sin comprometer una recomendación
   preliminar — más fiel a la metodología ABR, sobre todo habiendo ya una integración de IA
   propia en curso dentro de Odoo (ver punto 5).
5. **Punto crítico explícito de la asesora**: alinear el proceso con la persona interna
   (nómina) que ya integra IA al ERP Odoo 17 — su nombre no se identificó en la ficha, se
   sugiere incluirla en la próxima reunión. El Reporte Final debe integrar los hallazgos con
   ese desarrollo paralelo, no ignorarlo ni duplicarlo. Reflejado en el roadmap (Etapa 3).
6. **Preocupación del cliente sobre desplazamiento laboral**: el cliente "percibe que \[la IA\]
   podría llegar a sustituir parte del personal" y busca claridad antes de invertir. Se
   abordó con honestidad en Diagnóstico e Impacto, citando datos reales sobre crecimiento de
   roles técnicos en manufactura (no se promete ni se niega ningún efecto sobre el empleo,
   se ofrecen datos reales — §4.9).
7. **Sin certificado** — Detección pura, mismo criterio que `deteccion-sin-certificado.md`.
8. **Sin slide de Mapa de Calor** — mismo ajuste ya aplicado a Detecciones recientes.

## Las 4 áreas (ficha Bloque A)

1. **Dirección General**
2. **Gerencia de Ventas** (coordinaciones: Mercadeo, Ventas)
3. **Gerencia de Administración** (coordinaciones: Talento Humano, Contabilidad, Soporte
   Técnico, Compras)
4. **Gerencia de Producción** (coordinaciones: Mantenimiento, Producción, Almacenes)

**Stakeholders nombrados en la ficha**: César Rondón (contacto principal); Valeria (Mercadeo);
Elián (Diseño); Ulises (Soporte técnico); persona interna de nómina a cargo de integrar IA al
ERP Odoo (nombre no mencionado, sugerido incluirla en la próxima reunión).

## Necesidad detectada (cita textual, Bloque D)

*"No hemos escuchado ninguna propuesta. No tenemos idea de lo que es capaz de hacer la IA a
nivel del sistema de la empresa."* Necesidad central: qué inducción se le puede dar a los
líderes de cada departamento para que manejen bien la IA.

## Contexto de stack (interno, no se afirma migración — §4.11)

- **Ecosistema**: Google Workspace.
- **Información del negocio**: sistema de gestión central (ERP, probablemente Odoo 17).
- **Comunicación**: correo y WhatsApp; el ERP Odoo también trae un módulo de comunicación
  interna por documento.
- **Uso de IA hoy**: equipo de diseño de Mercadeo usa una herramienta de generación de
  imagen/video (no identificada con certeza) y Gemini en modo chat, sin licencias
  formalizadas. Una persona interna (nómina) ya integra IA al ERP Odoo 17 — esfuerzo paralelo
  a coordinar, no a duplicar.
- **Sin política de seguridad de datos** (no existe, no está en desarrollo). Regulación
  sectorial no quedó clara — el cliente mencionó a "Isabel" (posible persona/área de
  compliance) sin poder profundizar; pendiente de aclarar en la próxima reunión.

## Universo y modalidad

- **Universo sin cifra exacta confirmada** para Velas 3N (ver decisión 3). Roles: líderes de
  las gerencias y coordinadores de Talento Humano, Contabilidad, Soporte Técnico, Compras,
  Mercadeo, Ventas, Mantenimiento, Producción, Almacenes.
- **Modalidad**: Virtual (dato explícito de la ficha).
- **Sede**: una sola, Las Mercedes, Caracas (toda la operación administrativa).
- **Nivel de partida con IA**: desigual — "algunos la usan bien, otros no la usan". Sin
  formación previa.
- **Presupuesto**: no definida aún. **Apertura al cambio**: no evaluada explícitamente.
  **Patrocinio ejecutivo**: no confirmado (César Rondón participa, pero no se confirmó que
  decida o firme la contratación final).
- **Horizonte de tiempo**: corto plazo (0-3 meses).
- **Objetivo del Reporte Final**: entender el nivel de madurez de IA de la organización y
  recibir un plan claro con hitos para que los líderes apliquen y gestionen IA con criterio,
  incluyendo cómo se integra con el desarrollo de IA que ya construyen dentro de Odoo.

## Equipo asignado

- **Facilitación**: Equipo INTEZIA Education.
- **Asesora comercial**: Verónica Rubio.

## Regenerar el PDF — trío obligatorio

```bash
./scripts/generar-pdf.sh velas-3n
python3 scripts/customize-acroforms.py velas-3n
python3 scripts/customize-velas-3n.py "clientes/propuestas/velas-3n/<PDF generado>.pdf"
```

## Pendientes

- Confirmar cargo exacto y rol de decisión final de César Rondón.
- Identificar e incluir en la próxima reunión a la persona interna que integra IA al ERP Odoo.
- Aclarar la mención de "Isabel" / posible área de compliance y la regulación sectorial
  aplicable.
- Confirmar cifra exacta de universo/headcount de Velas 3N (la ficha trae un número ambiguo,
  posiblemente de un grupo de varias empresas, no solo Velas 3N).
- Confirmar presupuesto (no definido al momento del levantamiento).
