# Programa interno · Cartonbar · Servicio de Habilidades (CAI-113)

> Documento interno (no se muestra al cliente). **Generado** por `scripts/generar-habilidades-compacto.py` desde `datos.json`: no editar a mano.
> Fuente del insumo: Ficha de Levantamiento (18/11/2026), resumen de Ventas y transcripción de la reunión con el cliente.

## 1. Resumen

- **11 soluciones en 4 áreas**, **80 h** de trabajo, más seguimiento a 30, 60 y 90 días.
- Herramienta **Plataforma propia con IA**: 11 soluciones, 80 h.
- Horas por fase: F1 24 h (3 sol.) · F2 34 h (4 sol.) · F3 22 h (4 sol.).

## 2. Líneas de trabajo y ruta

| Línea de trabajo | Herramienta | Áreas | Horas | Soluciones |
|---|---|---|---|---|
| Ventas y facturación | Plataforma propia con IA | Ventas y facturación | 24 | 3 |
| Comunicaciones y CRM | Plataforma propia con IA | Comunicaciones y CRM | 24 | 3 |
| Packaging y autonomía | Plataforma propia con IA | Packaging a medida, Autonomía del equipo | 32 | 5 |

Sin semanas ni sesiones en la propuesta: el calendario se acuerda en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12).

| Línea de trabajo | Órdenes (órdenes de venta y bandeja única) | CRM (facturación, CRM y diseñador) | Escala (cotización, web y traspaso) |
|---|---|---|---|
| Ventas y facturación | 16 h · 2 sol. | 8 h · 1 sol. | 0 h · 0 sol. |
| Comunicaciones y CRM | 8 h · 1 sol. | 16 h · 2 sol. | 0 h · 0 sol. |
| Packaging y autonomía | 0 h · 0 sol. | 10 h · 1 sol. | 22 h · 4 sol. |

- **Arranque**: Accesos, prioridades y enlace técnico confirmados.
- **Órdenes y bandeja**: Shopify y Amazon en la plataforma y la bandeja única en uso.
- **CRM y facturación**: CRM terminado, facturación conectada y diseñador de cajas en producción.
- **Cierre**: Cotización, web y traspaso al equipo; empieza la garantía.

## 3. Soluciones y horas (C = construcción, T = pruebas, A = adopción)

### Ventas y facturación · 3 soluciones · 24 h · Plataforma propia con IA · línea A

Para qué (lo que ve el cliente): Que las órdenes y la factura lleguen a la plataforma sin teclear

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| VF-1 | Órdenes de Shopify en la plataforma | Las órdenes de Shopify se extraen y se cargan en la plataforma propia de forma automática, en lugar de procesarse a mano. | - | - | - | 8 | F1 |
| VF-2 | Órdenes de Amazon en la plataforma | Las órdenes de Amazon, hoy rescatadas a mano, llegan a la misma plataforma que las de Shopify. | - | - | - | 8 | F1 |
| VF-3 | Facturación conectada con FreshBooks | Conectar la plataforma con FreshBooks, ya mapeado, para que cada orden genere su factura. Depende de lo que permita la conexión de FreshBooks. | - | - | - | 8 | F2 |

### Comunicaciones y CRM · 3 soluciones · 24 h · Plataforma propia con IA · línea B

Para qué (lo que ve el cliente): Que las comunicaciones y el CRM dejen de pasar por una sola persona

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| CC-1 | Bandeja única de comunicaciones | WhatsApp, correo y chats reunidos en un solo lugar, separando lo personal de lo de la empresa. | - | - | - | 8 | F1 |
| CC-2 | Respuestas automáticas a consultas | Respuestas automáticas a las consultas frecuentes de clientes, con revisión de una persona en los casos que lo piden. | - | - | - | 6 | F2 |
| CC-3 | CRM propio terminado y en uso | Completar el CRM que el cliente construyó, para que cada contacto y cada conversación quede registrado en él. | - | - | - | 10 | F2 |

### Packaging a medida · 3 soluciones · 26 h · Plataforma propia con IA · línea C

Para qué (lo que ve el cliente): Que lo que el cliente diseña online llegue a producción y cotizado

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| PM-1 | Cajas diseñadas pasan a producción | Integrar la personalización online de cajas en Shopify con el flujo de preproducción e impresión. | - | - | - | 10 | F2 |
| PM-2 | Cotización automática de cajas | Cotización de las cajas personalizadas a partir de lo que el cliente diseña, por correo o WhatsApp. | - | - | - | 8 | F3 |
| PM-3 | Web integrada con Shopify | La página web centralizada en Shopify, con la parametrización de packaging conectada a pedidos y cotización. | - | - | - | 8 | F3 |

### Autonomía del equipo · 2 soluciones · 6 h · Plataforma propia con IA · línea C

Para qué (lo que ve el cliente): Que el equipo mantenga y escale la plataforma sin depender de Intezia

| ID | Entregable (nombre en el deck) | Detalle de la fuente | C | T | A | Total | Fase |
|---|---|---|---|---|---|---|---|
| AU-1 | Guía de mantenimiento y escalado | Documento de cómo mantener, ampliar y probar cada integración construida, escrito con quien la va a sostener. | - | - | - | 3 | F3 |
| AU-2 | Práctica guiada con el enlace técnico | El enlace técnico del cliente construye una mejora nueva con la guía, acompañado, para comprobar que puede hacerlo solo. | - | - | - | 3 | F3 |

## 4. Fuera de alcance

- Redes sociales y canal interno del equipo: se evalúan en una etapa 2.
- Reemplazar la plataforma propia: se completa y se conecta, no se cambia.
- Rediseño gráfico completo de la web: se integra y se parametriza lo existente.
- Licencias y suscripciones de terceros: las contrata Cartonbar.

## 5. Supuestos a confirmar (antes del método)

- Pedido de Ivana (22/11/2026): propuesta de Habilidades CAI-113 para Cartonbar con Verónica Rubio como asesora, a partir de la Ficha de Levantamiento (18/11/2026), el resumen de Ventas y la transcripción de la reunión (resumen). Primer contacto con Intezia.
- Decisiones de Ivana (22/11/2026): Educación y sin alianza; 80 h; impacto «operación»; se nombran solo las plataformas del cliente (Shopify, Amazon, FreshBooks), sin marcas de IA ni licencias de IA.
- Reparto de horas mío (Ivana pidió 80 h): Ventas y facturación 24 h (órdenes de Shopify 8, de Amazon 8, facturación con FreshBooks 8); Comunicaciones y CRM 24 h (bandeja única 8, respuestas automáticas 6, CRM terminado 10); Packaging a medida 26 h (cajas diseñadas a producción 10, cotización automática 8, web integrada con Shopify 8); Autonomía del equipo 6 h (guía 3, práctica guiada 3). Fases 24, 34 y 22 h. El orden sigue la urgencia de la ficha (órdenes y comunicaciones primero; el hueco grande que dijo Daniel es WhatsApp y CRM).
- Los entregables salen de los tres procesos de la ficha (integración e-commerce, comunicaciones y CRM, personalización y cotización) y de la transcripción (CRM propio, cotizaciones, FreshBooks, web con Shopify). «Autonomía del equipo» responde a lo que quiere el cliente: que él y su hijo mantengan y escalen la plataforma sin depender de Intezia.
- Fuera de alcance, por riesgo de scope que marca la ficha: redes sociales y canal interno del equipo (la transcripción habla de reemplazar WhatsApp personal y Trello por Slack, Teams o un módulo propio) y rediseño gráfico completo de la web. Quedan como etapa 2. Confirmar con Ivana o Verónica.
- Sin semanas, sesiones ni fechas (§4.23): la ficha habla de 2 a 3 sesiones por semana, sesiones de 2 h y resultado funcional en un mes. Nada de eso va en el deck; el ritmo se dice «acelerado, según se acuerde» y el calendario queda para el kickoff. No se promete un mes.
- Sin nombres de personas: el decisor (Daniel Díaz) y su hijo se llaman «el propietario» y «el enlace técnico». Hechos de portada tomados de la ficha: órdenes procesadas a mano, 20 a 30 comunicaciones diarias que pasan por una persona, FreshBooks mapeado y no conectado, CRM incompleto.
- No se nombra la IA que el cliente usa (Gemini, Grok, Claude y su integrador propio): ni se afirma que migre ni que cambie de stack (§4.11). No se menciona VPN (Claude no está soportado en Venezuela). La plataforma propia se dice así, sin nombrar Firestore.
- Retorno en modo método: la ficha no trae horas-hombre ni volúmenes medidos (solo «órdenes continuas» y «20 a 30 comunicaciones diarias»). No se cargan cifras.
- Seguimiento 30-60-90 incluido por ser estándar de Habilidades. Sin facilidad de pago (regla permanente; además moneda y forma de pago siguen sin definirse en la ficha). Sin certificado. Hoja de inversión con valores vacíos para ventas, en REF.
- Modalidad presencial en las oficinas del cliente (ficha). La ficha ubica a Daniel en Miami y la reunión del viernes en Caracas: el deck no dice ciudad; se acuerda en el arranque.

## 6. Cómo trabajamos (slide 4)

**Por qué en este orden:** Primero las órdenes y la bandeja única, que hoy más trabajo manual dan. Después el CRM, la facturación y el diseñador de cajas. Al final cotización, web y traspaso al equipo.

- **Construimos**: Junto a quien ejecuta el proceso, con sus casos reales.
- **Probamos**: Con ese equipo y con el equipo de tecnología de Cartonbar.
- **Adoptamos**: El equipo la usa en su trabajo diario.
- **Medimos**: El retorno en tiempo y las oportunidades de optimización para la empresa.

- En la práctica, **Sobre su plataforma**: Se completa y conecta lo que Cartonbar ya construyó: no se reemplaza ni se pasa a otras herramientas.
- En la práctica, **Con quien la mantiene**: El enlace técnico construye junto a Intezia cada integración, para poder mantenerla y ampliarla por su cuenta.
- En la práctica, **Depende de cada conexión**: Lo que se conecta depende de lo que permita cada plataforma (Shopify, Amazon, FreshBooks): se verifica en el arranque.
- Datos: Los accesos, las claves y los datos de clientes se quedan en la nube de Cartonbar y no se cargan a la IA sin su autorización: se trabaja con los ejemplos que apruebe.
- Quién construye: Intezia guía y el equipo de Cartonbar construye con IA sobre su propia plataforma, con su enlace técnico al lado. La plataforma y sus accesos son de Cartonbar.

**Logística:** modalidad: Presencial en las oficinas de Cartonbar, según se acuerde en la reunión de arranque. · participantes: El propietario y su enlace técnico; en cada frente, quien opera el proceso. · ritmo: Ritmo acelerado, según se acuerde en el arranque. · arranque: La fecha se acuerda en la reunión de arranque..

## 7. Retorno esperado (slide 6)

Modo **metodo**. La slide no cita estudios ni referencias de la web ni promete retorno.

Pasos del método: Tareas de cada línea; Tiempo actual por tarea; Tiempo con la integración; Horas recuperadas.

## 8. Impacto (cuadro de «Lo que se llevan», slide 5)

Enfoque decidido con Ivana: **operacion**. El impacto es de tiempo, calidad, servicio o ventas; no toca a las personas.

> Las órdenes, las comunicaciones y las cotizaciones fluyen sin pasar por una sola persona, y el equipo mantiene y escala la plataforma por su cuenta, lista para sostener la operación en Venezuela.

## 9. Próximos pasos (slide 8)

Asesora comercial que ve el cliente: Verónica Rubio, Asesora comercial · vrubio01@intezia.com · +58 422 3355505.

