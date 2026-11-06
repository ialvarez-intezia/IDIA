# Brief · Supermercados Viva · Servicio de Habilidades (CAI-079)

> Generado por `scripts/generar-habilidades-compacto.py` la primera vez (no se sobrescribe después, salvo el bloque marcado como automático). Completar a mano lo que falte; los datos del deck viven en `datos.json`.

## Datos administrativos

- **Cliente**: Supermercados Viva
- **Slug**: `supermercados-viva-cai079`
- **División Intezia**: `educacion`
- **Servicio (§4.1a)**: `habilidades`
- **Alianza**: `no`
- **Tipo de documento**: categoría de catálogo Capacitación In-Company (`CAI-079`), presentada al cliente como **propuesta de proyecto**; formato compacto de 15 slides (con hoja de inversión y de pago (campos de monto vacíos para ventas))
- **Eje temático**: Claude Team configurado y una automatización por gerente de área sobre la plataforma de Viva (SAP Business One, Power BI y Profit Nómina), con política de uso y manejo de datos
<!--auto:inicio-->
- **Alcance**: 13 entregables en 4 bloques · 52 h de trabajo · seguimiento a 30, 60 y 90 días
- **Orden de las slides**: 1 Portada · 2 Alcance · 3 Ruta · 4 Cómo trabajamos · 5 Entregables · 6 Retorno · 7 Respuesta a la solicitud (1) · 8 Respuesta a la solicitud (2) · 9 Respuesta a la solicitud (3) · 10 Respuesta a la solicitud (4) · 11 Respuesta a la solicitud (5) · 12 Respuesta a la solicitud (6) · 13 Inversión · 14 Próximos pasos
- **Asesora comercial que ve el cliente (última slide)**: Flavia Martínez, Asesora comercial · fmartinez@intezia.com · +58 414 5756615
<!--auto:fin-->
- **Estado**: `Borrador`
- **Insumos (CLAUDE.md §4.23)**: Ficha de Levantamiento + transcripción de la reunión con el cliente (indicar la fecha de cada una y qué se tomó de cada una). Si se contradicen, manda la transcripción; el resumen o correo de la asesora no define la estructura de la propuesta.
- **fecha_arranque_deseada**: (preguntar; se usa en el kickoff, no en la propuesta: la propuesta no lleva fechas, semanas ni sesiones)
- **resultados_esperados**: (preguntar; sin esta respuesta no se agrega ROI, no se inventa)

## Origen y fuente

- **Origen**: Solicitud de propuesta de Viva Supercentro (29/10/2026, recepción hasta el 5/11/2026) y contexto de la asesora Flavia Martínez, más instrucciones de Ivana del 03/11/2026: CAI-079, respuesta en el orden de la sección 4 dentro de la propuesta, referencias y conectores MCP, tiempos de adopción medidos y perfil de facilitadores aparte
- **Fuente del insumo**: Solicitud de propuesta de Viva Supercentro y contexto de la asesora; sin transcripción ni ficha
- Las tablas completas (solución, horas C/T/A, fase) están en `programa.md`, generado desde `datos.json` con las sumas calculadas.

## Decisiones y supuestos (confirmar con el usuario)

- Pedido de Ivana (03/11/2026): CAI-079 para Supermercados Viva (el documento dice «Viva Supercentro»), asesora Flavia Martínez. Responde a la solicitud de propuesta de Viva (emitida el 29/10, recepción hasta el jueves 5/11; consultas hasta el martes 3/11). Educación y sin alianza (inferidos; no se preguntaron). Es Habilidades, no Detección (contexto de Flavia).
- Formato: Ivana pidió no hacer un anexo aparte sino agregar a la propuesta una hoja o sección más, respondiendo en el orden que piden. Se agregó al generador la opción `respuesta_solicitud` (6 páginas opcionales «Respuesta a la solicitud» entre el retorno y la inversión) y `inversion.validez_dias`. Las páginas siguen el orden de la sección 4 (4.1 y 4.3, 4.2, 4.4 y 4.5, 4.6 a 4.8), el resumen, el cronograma, la confidencialidad y las sugerencias (sección 9) aparte.
- Horas (propuesta mía, Ivana no respondió la tabla): Fase 0 de 4 h; Fase I: fundamentos 2 h, política de uso 4 h y una automatización por gerente (4 h por área, 6 h en Marketing por el abordaje de retail) = 48 h; total 52 h con el equipo. La Fase II (15 personas de los equipos) queda sin cotizar, sujeta a la medición, como pide el cliente. Los casos de uso por área (4.2) son propuestas mías a partir de los sistemas del cliente, sin cifras, que cada gerente confirma.
- Claude y Venezuela (Ivana pidió decir que se puede acceder por VPN, que la información que circula es no oficial y que no hay ningún problema): NO se escribió. La política oficial de regiones de Anthropic (anthropic.com/supported-countries, consultada el 03/11/2026) no lista a Venezuela y excluye el uso por personas ubicadas físicamente en una región no soportada y por entidades constituidas o con sede en ella. El deck dice solo que el acceso de la organización se verifica en la Fase 0 según las condiciones del proveedor para el país, y la sugerencia S3 propone validar acceso y herramienta antes de ampliar licencias. Si Ivana tiene una confirmación escrita de Anthropic, se puede cambiar.
- Acceso único (SSO): disponible en los planes Team y Enterprise y compatible con Microsoft Entra ID por SAML; exige verificar el dominio y que quien configure sea Owner o Primary Owner (ayuda oficial de Claude: support.claude.com, consultada el 03/11/2026). Por pedido de Ivana, el deck lo menciona como disponible según la documentación oficial y dice que la configuración requiere al administrador correspondiente. Roles más finos y preferencias de datos: no verificados en fuente oficial, por eso el deck los deja como parte de la revisión de la Fase 0.
- SAP y conectores (Ivana, 03/11/2026): se quitó la frase de que Intezia no ha trabajado con SAP. El deck dice que ha desarrollado conectores MCP para empresas con sistemas similares (Fasto, Médica Campestre, Aerocentro Miami) o trabaja extrayendo la información y pasándola a Claude, según la estructura de cada herramienta. El brief de Médica Campestre (CAP-075) habla de una app conectada al ERP SAP del hospital: conviene verificar qué hubo en SAP antes de enviar.
- Referencias (4.6, Ivana 04/11/2026): Fasto va primero, por ser una cadena de supermercados como Viva, con su caso: 14 procesos levantados en Inventario y Costos, 13 subproyectos y un agente de compras conectado al ERP que entrega sugeridos de compra cada lunes a las 8:00 a. m. en 3 tiendas. Esos datos los dio Ivana: no figuran tal cual en el repositorio (el brief de la CAI-077 habla de 5 subproyectos de Inventario y de ocho de Costos, que suman 13). Médica Campestre y Aerocentro Miami siguen como antes. La autorización y los datos de contacto de las tres los anexa Flavia aparte.
- Tiempos de adopción (4.7, Ivana 04/11/2026): cifras medidas del banco de casos, sin nombres: 64 % de las personas ya recupera tiempo cada semana al cierre del servicio; 91 % en un equipo de líderes del sector salud; 6 de 8 soluciones siguen en uso 6 semanas después del cierre; +329 horas recuperadas cada semana por los equipos de 6 empresas. No están documentadas en el repositorio (el más cercano es HJB Química, 91 % con algún ahorro semanal, 20 de 22): confirmar la fuente interna antes de enviar. Las dificultades frecuentes siguen en una viñeta.
- Resumen de la empresa y facilitadores (Ivana 04/11/2026): se suman «+200 empresas acompañadas y operamos desde 2022» y la frase exacta «Grupo INTEZIA, una de las primeras empresas de Latinoamérica en ser OpenAI Select Partner». Son datos de la presentación comercial, no documentados en el repositorio: confirmar. El perfil de los facilitadores se envía aparte.
- Cronograma en semanas (Ivana 04/11/2026): excepción a CLAUDE.md §4.23, porque el cliente lo pide. Propuesta: Fase 0 en la semana 1; Fase I de la semana 2 a la 6 (fundamentos y política en la semana 2, automatizaciones por área de la 3 a la 6); seguimiento a 30, 60 y 90 días desde el cierre de cada área. Las frases con semanas están en frases_ok. Ajustar si el ritmo real es otro; el calendario exacto sigue acordándose en el arranque.
- Propuesta económica (Ivana 04/11/2026, a partir de lo que pide el cliente en la página 13): la hoja de inversión pasa a ser una tabla de fase, concepto, área, horas y valor (USD) con las filas Fase 0 (4 h), Módulo 1 (2 h), Módulo 2 (4 h), Módulo 3 en 9 áreas (36 h) y en Marketing (6 h) y el acompañamiento 30-60-90 (sin horas), y debajo subtotal, descuento por contratar el programa completo, total antes de impuestos, IVA y total con impuestos. Todos los montos están en blanco: son campos editables del PDF (ValorFila1..6, Subtotal, DescuentoPrograma, TotalAntesImpuestos, IVA, TotalConImpuestos) que escribe Ivana tras revisarlos con María; subtotal y totales se calculan solos en Adobe Reader. Descuento válido por 30 días (antes 15) y cotización válida por 60 días. Condiciones de pago: 40 % al arrancar, 40 % al cerrar la Fase I y 20 % a los 30 días, en bolívares a la tasa del BCV del día de pago. La hoja ya no lleva Programa ni Notas editables ni garantía aparte (va en la última fila).
- Sugerencias (sección 9): cuatro, cada una con beneficio, impacto en la inversión y en el cronograma, y si es opcional o recomendada. Ivana (04/11/2026): en la A y la D el impacto es «USD ___» y en la B «referencial desde USD ___, se confirma con la medición», como campos editables que llena ella; la C sigue «incluido en la Fase 0». La S3 es mía.
- Sin nombres de personas (los nombres del RFP no van), sin número de sucursales, sin línea de fuente en la portada, sin horas internas (§4.23 punto 4).
- Lenguaje de marca (Ivana 04/11/2026): «forma a los gerentes», «formamos a los gerentes» y «formar a los equipos» pasan a «instalar la capacidad en los gerentes» o «en los equipos»; el título del retorno es «Retorno esperado: tiempo recuperado y su valor», sin «dinero» en la página, con la estimación sin compromiso de resultado.
- Inicio de sesión único (SSO) con Microsoft 365 en el plan Team (Rebeca, gerente de tecnología, lo va a verificar): documentación oficial de Claude, consultada el 04/11/2026. Funciones del plan Team (incluye «Single-Sign-On (SSO) and Domain Capture»): https://support.claude.com/en/articles/9266767-what-is-the-team-plan. Guía de Microsoft Entra ID (aplica a los planes Team y Enterprise; pide ser Owner o Primary Owner y verificar el dominio; el aprovisionamiento SCIM es solo de Enterprise y en Team se usa el aprovisionamiento Just-in-Time): https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup

## Reglas aplicadas (resumen; detalle en plantillas/habilidades-compacto.md, plantillas/deteccion-compacto.md y CLAUDE.md §4.21 a §4.23)

- **Orden = las preguntas del cliente** (Ventas, 2026-10-07): qué hago y para qué · cómo · cómo trabajamos · qué recibo · qué retorno espero · cuánto cuesta · cómo se paga · qué sigue y a quién escribo. La inversión es la antepenúltima.
- **Sin semanas, sesiones ni fechas** (Keiber, 2026-10-08): el calendario, el número de sesiones y su duración se acuerdan en la reunión de arranque (Brief de Kickoff, CLAUDE.md §12). La duración se dice en horas y la ruta, por fases o etapas.
- **Lenguaje del cliente**: sin «proceso base», «Frente A», «S1-S3», «carril» ni «8 de 15 h»; «valor» o «inversión», nunca «precio» ni «costo»; cada cifra dice de qué es y la entiende quien no estuvo en la reunión. Sin repetir información entre slides.
- Sin Metodología ABR ni Equipo facilitador (§4.10a); «Cómo trabajamos» explica los pasos, por qué en ese orden, cómo funciona en la práctica (límites incluidos) y cómo se cuidan los datos.
- El nombre del proyecto (titular de portada) es una frase-objetivo estilo título de tesis, y la propuesta se presenta como proyecto, no como capacitación.
- Los casos de éxito ya logrados solo se citan con fuente documentada del propio cliente (`metodo.ejemplos[].fuente`); la contratación evitada se plantea como probabilidad, nunca como compromiso. El dolor de la portada solo usa hechos que las soluciones del alcance resuelven (`resuelto_por`).
- Retorno esperado (módulo `retorno` de `datos.json`; va antes de la inversión): sin estudios ni citas de la web. En modo método explica cómo se calculará; en modo cifras muestra solo datos del cliente con su tipo (medido, declarado, estimación). La medición se ata a la línea base del arranque y al seguimiento a 30, 60 y 90 días, sin semanas. Datos: `retorno-captura.xlsx` (`scripts/habilidades-retorno-xlsx.py`).
- Montos de inversión, descuento, total y cuotas: vacíos, los llena ventas.

## Pendientes

- Confirmar si se envió a Rebeca la consulta sobre el acceso a Claude desde Venezuela y NordVPN (el plazo de consultas fue el 3/11).
- Completar a mano los montos de la hoja de inversión y de las sugerencias A, B y D (campos editables, los llena Ivana con María) y confirmar «20 % a los 30 días»: contados desde qué hito.
- Obtener autorización de contacto de Fasto, Médica Campestre y Aerocentro Miami, y los datos de contacto que se anexan aparte.
- Enviar aparte el perfil de los facilitadores.
- Verificar si Médica Campestre tuvo conexión con SAP.
- Valor, descuento y total: campos vacíos para ventas, (hoja estándar). Fecha límite de recepción: jueves 5/11/2026.
- Confirmar el teléfono y el correo de Flavia Martínez (tomados de propuestas anteriores).
- Confirmar la fuente interna de las cifras de adopción (64 %, 91 %, 6 de 8, +329 h en 6 empresas), de los datos de Fasto (14 procesos, 13 subproyectos, agente de compras) y de «+200 empresas, desde 2022, OpenAI Select Partner».
- Confirmar el cronograma en semanas (Fase 0 en la semana 1; Fase I de la 2 a la 6) con quien dirige el servicio.

## Flujo de generación

```bash
python3 scripts/generar-habilidades-compacto.py supermercados-viva-cai079      # datos.json -> index.html, acroforms.json, programa.md
bash scripts/pdf-habilidades-compacto.sh supermercados-viva-cai079             # verifica, genera el PDF y ajusta los campos
```
