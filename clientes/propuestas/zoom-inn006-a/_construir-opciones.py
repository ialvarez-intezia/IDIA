#!/usr/bin/env python3
"""Construye las tres propuestas de Zoom INN-006-A (Bootcamp), INN-006-B (Por área) e INN-006-C (Híbrido).

Fuente única de los números: los cambios (base de personas, totales por área, supuesto de ausencia, facilitadores, horas internas)
se hacen aquí y se regenera. Corre el generador compacto (scripts/generar-habilidades-compacto.py) para cada opción.

Uso (desde la raíz del repositorio):  python3 clientes/propuestas/zoom-inn006-a/_construir-opciones.py [--sin-generar]

Pedido de Ivana (26/10/2026), con el texto de la dirección: un solo código INN-006 con sufijo A, B o C; sesiones de 2 horas; inventario,
priorización, migración en vivo, reglas, medición de un caso y actualización del ecosistema en cada una; sección «Qué está cambiando»;
fechas de Google con fuente; arranque la semana del 2 de noviembre, hasta 3 por semana, grueso antes de diciembre; Brand Kit v2.1.
"""
import datetime
import json
import math
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
PROPUESTAS = RAIZ / "clientes" / "propuestas"
CONSULTA = "26/10/2026"          # fecha en que se consultó la documentación de Google

# --- Números (provisionales; Ivana: «coloca estos números mientras y después podemos corregir») -------------------------------------
BASE_A = 510                      # base del bootcamp según el texto de la dirección (21 encuentros de hasta 25 personas)
TOPE = 25                         # personas por encuentro
AUSENCIA = 0.15                   # supuesto de ausencia en las sesiones por área, para calcular el bootcamp de la opción C
AREAS = [                         # (id, nombre, personas) según los registros de Ivana; las áreas grandes primero
    ("OPE", "Operaciones", 40),
    ("COM", "Comercial", 27),
    ("LEG", "Legal", 8),
    ("MIA", "Zoom Miami", 11),
    ("GHU", "Gestión Humana", 17),
    ("TEC", "Tecnología", 18),
]
INICIO = datetime.date(2026, 11, 2)
DIAS = ["lun", "mie", "vie"]      # hasta 3 por semana
FIN_NOV = datetime.date(2026, 11, 27)      # el grueso cierra antes de diciembre
REINICIO = datetime.date(2027, 1, 11)      # enero y febrero: margen para rezagados, antes del tope del 1 de marzo de 2027

# Horas internas para cotizar (estimación del sistema, por confirmar): preparación fija, por área, coordinación con TI, seguimiento
H_PREP_FIJA, H_PREP_AREA = 8, 1             # formulario de inventario 2 h, material 4 h, guía de nombres 2 h; +1 h por área para adaptar el material
H_TI_A, H_TI_AREAS = 4, 6                   # coordinación con TI (A: una reunión de requisitos y verificación; B y C: accesos por área)
H_SEG_CIERRE = 3                            # cierre y entrega de la medición; más 0,5 h por encuentro de medición del caso (redondeado hacia arriba)


def fechas_omitidas(desde, hasta):
    d, out = desde, []
    while d <= hasta:
        out.append(d.isoformat())
        d += datetime.timedelta(days=1)
    return out


def grupos(n):
    return max(1, math.ceil(n / TOPE))


def calcular():
    ses_areas = [(i, nom, n, grupos(n)) for i, nom, n in AREAS]
    total_areas = sum(n for _, _, n in AREAS)
    n_a = math.ceil(BASE_A / TOPE)
    n_b = sum(g for _, _, _, g in ses_areas)
    ausentes = math.ceil(total_areas * AUSENCIA)
    n_boot_c = math.ceil(ausentes / TOPE)
    n_c = n_b + n_boot_c
    nov_a = 12                                    # 4 semanas × 3 por semana antes de diciembre
    r = {}
    seg = lambda n: math.ceil(n * 0.5) + H_SEG_CIERRE
    r["A"] = dict(n=n_a, nov=min(nov_a, n_a), ene=max(0, n_a - nov_a), h_ses=2 * n_a, fac=2, h_fac=2 * n_a * 2,
                  prep=H_PREP_FIJA, ti=H_TI_A, seg=seg(n_a))
    r["B"] = dict(n=n_b, h_ses=2 * n_b, fac=1, h_fac=2 * n_b, prep=H_PREP_FIJA + H_PREP_AREA * len(AREAS), ti=H_TI_AREAS, seg=seg(n_b))
    r["C"] = dict(n=n_c, n_areas=n_b, n_boot=n_boot_c, ausentes=ausentes, h_ses=2 * n_c, fac=1, h_fac=2 * n_b + 2 * n_boot_c * 2,
                  prep=H_PREP_FIJA + H_PREP_AREA * len(AREAS), ti=H_TI_AREAS, seg=seg(n_c))
    for k in r:
        r[k]["total"] = r[k]["h_fac"] + r[k]["prep"] + r[k]["ti"] + r[k]["seg"]
    return ses_areas, total_areas, r


# --- Contenido común ----------------------------------------------------------------------------------------------------------------


def cambios():
    return {
        "titulo": "Qué está cambiando y cómo les afecta.",
        "subtitulo": "Google reemplaza los Gems por Skills. Esto es lo que cambia y por qué conviene migrar con tiempo.",
        "etiqueta_fechas": "Qué cambia en Google",
        "fechas": [
            {"cuando": "13 oct 2026", "texto": "Las Skills llegan a la app de Gemini y conviven con los Gems hasta mediados de noviembre."},
            {"cuando": "17 nov 2026", "texto": "Los Gems pasan a Configuración en la app de Gemini; se pueden seguir usando."},
            {"cuando": "1 mar 2027", "texto": "Google no los retira antes de esta fecha: después, nadie podrá crear, editar ni usar Gems."},
            {"cuando": "1 mar 2027", "texto": "El mismo día dejan de funcionar los flujos de Workspace Studio con el paso «Ask a Gem»."},
        ],
        "etiqueta_riesgo": "Si no se hace nada",
        "riesgo": [
            {"titulo": "Gems inactivos", "texto": "Google los convierte en borradores de skills inactivos: cada creador debe revisarlos y activarlos."},
            {"titulo": "Workspace va aparte", "texto": "Una Skill de la app de Gemini no pasa sola a las apps de Workspace; los Gems que se usan allí se recrean en Workspace Studio."},
            {"titulo": "Flujos detenidos", "texto": "Los flujos de Studio con «Ask a Gem» siguen hasta el 1 de marzo de 2027 y después se detienen."},
        ],
        "etiqueta_porque": "Por qué con Intezia",
        "porque": [
            {"titulo": "Resultados propios de Zoom", "texto": "Índice de impacto de 87/100 en la encuesta de cierre de seis áreas (83 personas) y 89 % de aciertos en la evaluación técnica."},
            {"titulo": "Ya trabajan con Gemini", "texto": "El 88 % de esas personas usa Gemini como su herramienta de IA principal (73 de 83): se parte de lo que ya armaron."},
            {"titulo": "Tecnología ya lo adoptó", "texto": "Al seguimiento a 30 días (16/10/2026), Tecnología usaba a diario lo aprendido con Intezia."},
        ],
    }


DESTACADOS = {
    "A": ("Por qué un bootcamp", [
        ("Un solo criterio", "Personas de áreas distintas acuerdan los mismos nombres y reglas para todas las Skills."),
        ("Se aprende del vecino", "Quien ve el Gem de otra área descubre usos que puede reutilizar en el suyo."),
        ("Una sola migración", "Si varias personas usan el mismo Gem, se migra una vez y se comparte."),
        ("Más gente, antes de diciembre", "Hasta 25 personas por encuentro: se llega a más personas antes de que termine el año."),
    ]),
    "B": ("Por qué un encuentro por área", [
        ("Ejemplos del propio trabajo", "Cada área ve sus Gems, con su vocabulario y sus procesos, sin mezclarlos con otros."),
        ("Reglas a la medida", "Cada área acuerda cómo nombra, mantiene y comparte sus Skills."),
        ("Grupos de hasta 25", "Las áreas más grandes se dividen para que todas las personas practiquen en vivo."),
        ("Un caso medido por área", "Cada área cierra con su propio dato de tiempo recuperado."),
    ]),
    "C": ("Por qué un bootcamp para quienes faltaron", [
        ("Cada área, a lo suyo", "Su encuentro usa su vocabulario y sus procesos, sin mezclarlos con otros."),
        ("Nadie se queda atrás", "Quien no pudo asistir a su encuentro se une al bootcamp abierto."),
        ("Cabe aunque falten más", "Un solo bootcamp alcanza aun si la ausencia supera lo previsto, hasta el 20 %."),
        ("Un caso medido por área", "Cada área cierra con su propio dato de tiempo recuperado."),
    ]),
}


def metodo(opcion, part):
    return {
        "titulo": "Qué pasa en cada encuentro de 2 horas.",
        "subtitulo": "La misma agenda en las tres opciones: se llega con el inventario hecho y las 2 horas son de práctica.",
        "quien_construye": "Intezia guía cada encuentro en vivo, con las personas de Zoom aportando sus Gems: no se entrega nada hecho.",
        "por_que_orden": "Primero se llega con el inventario hecho; después se prioriza y se migra en vivo; al final se acuerdan las reglas y se mide un caso.",
        "pasos": [
            {"titulo": "Antes", "texto": "Cada persona cuenta sus Gems en un formulario corto, para llegar con el dato."},
            {"titulo": "Priorizamos", "texto": "Se eligen los Gems que de verdad se usan. 15 minutos."},
            {"titulo": "Migramos", "texto": "Esos Gems pasan a Skills, en vivo, con Intezia al lado. 55 minutos."},
            {"titulo": "Medimos", "texto": "Un caso: el tiempo de hoy contra el tiempo con la Skill. 20 minutos."},
        ],
        "practica": [
            {"titulo": "Reglas comunes", "texto": "Se acuerda cómo nombrar y compartir las Skills. 15 minutos."},
            {"titulo": "Al día con Google", "texto": "Qué cambió en Gemini y Workspace estos meses y qué le sirve a Zoom. 15 minutos."},
            {"titulo": "Cabe en 2 horas", "texto": "El inventario va antes y la medición se completa con la Skill ya en uso: así las 2 horas son práctica."},
        ],
        "datos": "Se migran solo los Gems que cada persona comparte y se respetan los permisos de Drive: nada confidencial se carga sin permiso.",
    }


def logistica(part):
    return {
        "modalidad": "A acordar con el equipo de TI de Zoom: en línea o presencial.",
        "participantes": part,
        "arranque": "TI activa las Skills antes del primer encuentro; Zoom confirma asistentes y horarios.",
        "ritmo": "Encuentros de 2 horas, con hasta tres en cada ciclo de cinco días hábiles.",
    }


def retorno():
    return {
        "modo": "metodo",
        "posiciones": False,
        "titulo": "Retorno esperado: tiempo recuperado con Skills.",
        "subtitulo": "No son cifras de Zoom: es el método con el que cada grupo mide su propio caso.",
        "etiqueta_pasos": "Cómo se calcula el retorno",
        "pasos": [
            {"titulo": "Caso real", "texto": "Cada grupo elige un procedimiento que repite con frecuencia."},
            {"titulo": "Tiempo de hoy", "texto": "Se anota cuánto tarda con el Gem actual, con quien lo hace."},
            {"titulo": "Con la Skill", "texto": "Se prueba la Skill en el mismo caso y se anota cuánto tarda."},
            {"titulo": "Diferencia", "texto": "La diferencia, por las veces que se repite, es el tiempo que se recupera."},
        ],
        "etiqueta_metas": "Qué queda definido al cerrar",
        "metas": [
            {"dias": "Inventario", "texto": "Los Gems de cada persona, contados y priorizados."},
            {"dias": "Reglas", "texto": "Cómo se nombran y se comparten las Skills."},
            {"dias": "Caso", "texto": "La comparación de tiempos, hecha con un caso real del grupo."},
        ],
        "etiqueta_destino": "Hacia dónde va el proyecto",
        "destino": [
            {"rotulo": "Skills compartidas", "texto": "Lo que cada grupo migra se **reutiliza** en otros equipos de Zoom."},
            {"rotulo": "Lo que se usa", "texto": "Se priorizan los Gems que **de verdad** se usan, no todos."},
            {"rotulo": "Equipo al día", "texto": "Quienes ya trabajaron con Intezia se ponen al día con lo que cambió en Google."},
        ],
        "gancho": "Al cierre, Zoom tendrá sus Gems más usados como Skills y un caso medido de tiempo recuperado.",
    }


def proximos():
    return {
        "etiqueta_contacto": "¿Dudas? Escribe a tu directora comercial",
        "asesora": {"nombre": "María Iribarren", "cargo": "Directora comercial", "correo": "miribarren@intezia.com", "telefono": "+58 414 0570056"},
        "pasos": [
            {"titulo": "Fecha y asistentes", "texto": "Confirmamos con Zoom el arranque a partir del 2 de noviembre y quiénes asisten a cada encuentro."},
            {"titulo": "TI activa y revisa", "texto": "Activa las Skills en la consola y revisa edición, canal de lanzamiento, flujos con «Ask a Gem» y permisos de Drive."},
            {"titulo": "Formulario previo", "texto": "Antes de cada encuentro, cada persona llena el formulario de inventario de sus Gems."},
        ],
    }


def calendario(omitir, encuentro, intro, subtitulo):
    return {
        "inicio": INICIO.isoformat(), "dias": DIAS, "hora": "horario por acordar", "horas_por_encuentro": 2,
        "omitir_fechas": omitir, "encuentro": encuentro,
        "titulo": "Calendario de los encuentros.", "subtitulo": subtitulo, "intro": intro,
    }


INTRO_BASE = ("Las sesiones arrancan la semana del 2 de noviembre, con hasta tres por semana, para abordar a la mayor cantidad de personas antes de diciembre. "
              "Diciembre es temporada alta de Zoom: no hay encuentros. Enero y febrero quedan de margen para rezagados, siempre antes del 1 de marzo de 2027.")


def supuestos_comunes(r):
    return [
        "Pedido de Ivana (26/10/2026), con el texto de la dirección (Jean y María; Emma pidió la sección «Qué está cambiando»): tres propuestas de Innovación para Zoom bajo un solo código, INN-006, con sufijo A (Bootcamp), B (Por área) y C (Híbrido), cada una en su carpeta. Educación, sin alianza, María Iribarren como directora comercial, sin mencionar Claude (solo Gems a Skills) (confirmado por Ivana).",
        "Qué reemplaza: INN-003 e INN-004 (Zoom, 19/10/2026, Borrador) llevaban Claude Fundamentals; estas tres solo migran Gems a Skills con Gemini. Confirmar con Ivana que INN-003 e INN-004 se archivan.",
        "Personas: la base de la dirección es 510 (Fase 1 de Intezia Fundamentals alcanzó a unas 500 personas, según el informe de casos de éxito). Los registros de Ivana (26/10/2026) por área suman 121: Comercial 27, Legal 8, Zoom Miami 11, Operaciones 40, Gestión Humana 17, Tecnología (sistemas o IT) 18. Ivana pidió usarlos «mientras» y corregirlos después. La opción A usa 510 y las opciones B y C usan las áreas de Ivana (121), así que las tres NO son comparables hasta cruzar los registros. Con 121 personas, la opción A serían %d encuentros (%d h)." % (math.ceil(sum(n for _, _, n in AREAS) / TOPE), 2 * math.ceil(sum(n for _, _, n in AREAS) / TOPE)),
        "Cruce con los registros de asistencia y certificados (Fase 1, Zoom Miami y Fase 2): no están en el repositorio (solo los dashboards con 83 respuestas, sin cédulas), así que no se pudo hacer el cruce.",
        "Encuentros de 2 horas, hasta 25 personas. Calendario: arranque la semana del 2 de noviembre (Ivana), hasta 3 por semana (lunes, miércoles y viernes: días propuestos por el sistema), grueso antes de diciembre (temporada alta de Zoom) y margen de enero y febrero para rezagados, antes del 1 de marzo de 2027. Horario: por acordar (no lo dio nadie). Que las sesiones arranquen antes del 17 de noviembre.",
        "Excepción a CLAUDE.md §4.23 (Keiber, 8/10/2026: sin semanas, sesiones ni fechas): el calendario con fechas va en la propuesta por pedido expreso de Ivana («coloca todo en la propuesta»). Solo la slide de calendario usa «sesiones» y «semana»; el resto del deck dice «encuentros».",
        "Fechas de Google (documentación oficial, consultada el %s): skills en Workspace desde el 5/10/2026 (Rapid Release hasta el 12/10; Scheduled Release del 19/10 a mediados de noviembre); skills en la app de Gemini desde el 13/10/2026 (hasta mediados de noviembre); 17/11/2026 los Gems pasan a Configuración; no antes del 1/3/2027 Business y Enterprise no podrán crear, editar ni usar Gems (Education, no antes del 1/6/2027). Google publicará más información al menos 30 días antes de la migración automática. Ivana pidió planificar el 1/3/2027 como fecha fija aunque Google diga «no antes de»: el deck lo dice con «no antes de»." % CONSULTA,
        "Dos puntos de la prensa, confirmados en la documentación oficial de Google para administradores (22/10/2026): los flujos de Workspace Studio con el paso «Ask a Gem» dejan de funcionar desde el 1/3/2027 (no se pueden añadir a flujos nuevos), y una Skill de la app de Gemini no se sincroniza con las apps de Workspace (se recrea en Workspace Studio). Los Gems que se usan en Workspace tampoco se transfieren solos.",
        "Requisito previo de TI (de la documentación de Google; PENDIENTE de confirmar con David): activar el ajuste «Allow people to use skills in Studio and Gemini in Workspace»; edición con skills en Workspace (Business Starter, Standard o Plus; Enterprise Standard o Plus; Google AI Pro for Education o AI Expanded Access); personas de 18 años o más; canal de lanzamiento (Rapid o Scheduled Release: el despliegue en Scheduled llega a mediados de noviembre, y el primer encuentro es el 2 de noviembre); lista de flujos de Workspace Studio con «Ask a Gem»; permisos de uso compartido de Drive de los Gems (se transfieren a las Skills).",
        "«Por qué con nosotros»: resultados propios de Zoom del informe de casos de éxito (clientes/casos-de-exito-zoom, 19/10/2026) y de los dashboards de impacto (Encuesta Edu-Trace de cierre, 83 respuestas de seis áreas): índice de impacto promedio 87/100, 89 % de aciertos en la evaluación técnica (222 de 249, medido), 88 % usa Gemini como herramienta principal (73 de 83, autopercibido) y el seguimiento a 30 días de Tecnología (16/10/2026, la herramienta ya adoptada). Son datos de cierre y percepción: el deck no los presenta como ahorro medido (§4.17). Sin nombres de personas.",
        "Horas para cotizar (María cotiza con cuotas de pago; el deck no lleva precios): estimación del sistema, por confirmar. Encuentros: %d h (A), %d h (B), %d h (C). Facilitadores: 2 en los bootcamps (varias áreas, 25 personas migrando en vivo) y 1 en los encuentros por área; con eso las horas de trabajo de encuentro son %d (A), %d (B) y %d (C). Preparación (formulario de inventario 2 h, material 4 h, guía de nombres 2 h; más 1 h por área para adaptar el material en B y C): %d, %d y %d h. Coordinación con TI: %d, %d y %d h. Seguimiento (medición del caso a 0,5 h por encuentro y cierre de 3 h): %d, %d y %d h. Total: %d (A), %d (B) y %d (C) horas de trabajo." % (
            r["A"]["h_ses"], r["B"]["h_ses"], r["C"]["h_ses"], r["A"]["h_fac"], r["B"]["h_fac"], r["C"]["h_fac"],
            r["A"]["prep"], r["B"]["prep"], r["C"]["prep"], r["A"]["ti"], r["B"]["ti"], r["C"]["ti"], r["A"]["seg"], r["B"]["seg"], r["C"]["seg"],
            r["A"]["total"], r["B"]["total"], r["C"]["total"]),
        "Agenda de 2 horas: no cabe todo a la vez; propuesta del sistema: el inventario va antes con un formulario (fuera de las 2 horas), la actualización del ecosistema se reduce a 15 minutos con lo que le sirve a Zoom, y la medición del caso se inicia en el encuentro (tiempo de hoy) y se completa con la Skill ya en uso. Reparto: priorización 15 min, migración en vivo 55, reglas 15, actualización 15 y medición 20.",
        "Pago: cuotas ligadas a hitos con los montos vacíos (María cotiza); los porcentajes son propuesta del sistema (A y C: 40/30/30; B: 50/50), por confirmar con María. Sin garantía ni seguimiento 30-60-90.",
        "Marca: Brand Kit Intezia v2.1 (13/10/2026, adjunto de Ivana): amarillo #FFD300, negro #0A0A0A, naranja #E58423 y Poppins (OFL, descargada de fontsource). Los archivos del logo v2 («Brand Kit v2 2026-10 / archivos») no están en el repositorio: el deck usa los logos actuales de `logos/` (el amarillo del arte es el #F4BA1A anterior). El CSS compacto, las cajas de la hoja de cotización y los campos del PDF conservan tintes del amarillo anterior. Falta canonizar la marca v2.1 en `empresa/marca-visual.md` y en las plantillas.",
    ]


def pendientes_comunes():
    return [
        "Confirmar la base: 510 (A) frente a los totales por área de Ivana (121, para B y C). Pasar los registros reales de asistencia y certificados (Fase 1, Zoom Miami y Fase 2) para el cruce y el total por área.",
        "Confirmar con David la lista de requisitos de TI (activación de Skills, edición, canal de lanzamiento, flujos con «Ask a Gem», permisos de Drive).",
        "Confirmar el horario de los encuentros y los días (se propusieron lunes, miércoles y viernes) y que TI pueda activar las Skills antes del 2 de noviembre.",
        "Confirmar las horas internas (preparación, coordinación con TI, seguimiento) y los facilitadores por encuentro (1 por área, 2 en bootcamp).",
        "Confirmar con María los porcentajes de las cuotas, la moneda y los impuestos de facturación y las cifras de cotización (el deck no lleva precios).",
        "Revisar con Ivana los logos de la marca v2.1 (archivos del Brand Kit) y la canonización de la marca nueva.",
        "Confirmar con Ivana que INN-003 e INN-004 se archivan y que el contacto con Zoom sigue siendo María (Anaís y Ricardo no van en el deck).",
        "Las fechas de Google pueden cambiar: reconsultar la página oficial antes de enviar.",
    ]


# --- Opciones ------------------------------------------------------------------------------------------------------------------------
def opcion_A(r, ses_areas, total_areas):
    x = r["A"]
    omitir = fechas_omitidas(FIN_NOV + datetime.timedelta(days=3), REINICIO - datetime.timedelta(days=1))
    areas = [{
        "id": "BOO", "nombre": "Bootcamp de varias áreas", "carril": "gw", "frente": "A",
        "para_que": "Hasta 25 personas de varias áreas por encuentro migran sus Gems a Skills en vivo.",
        "soluciones": [
            {"id": "BOO-1", "entregable": "Bootcamps de noviembre", "h": 2 * x["nov"], "fase": "F1",
             "detalle": "Referencia interna: %d encuentros de 2 horas en noviembre, hasta 25 personas de varias áreas por encuentro." % x["nov"]},
            {"id": "BOO-2", "entregable": "Bootcamps de enero y febrero", "h": 2 * x["ene"], "fase": "F2",
             "detalle": "Referencia interna: %d encuentros de 2 horas en enero y febrero, de margen para rezagados." % x["ene"]},
        ]}]
    return dict(
        slug="zoom-inn006-a", codigo="INN-006-A", nombre_opcion="Bootcamp",
        meta_tipo="Plan de Innovación · Opción A, bootcamp: %d encuentros de 2 h (%d h de encuentro) para %d personas de varias áreas, hasta 25 por encuentro · migración de Gems a Skills · calendario con fechas · formato compacto v3" % (x["n"], x["h_ses"], BASE_A),
        eje="Migrar a Skills los Gems de %d personas de Zoom en bootcamps de 2 horas, hasta 25 de varias áreas por encuentro, antes de que Google retire los Gems" % BASE_A,
        titulo_lineas=["Gems a Skills en un bootcamp", "de varias áreas"],
        lead="Las personas de Zoom llevan sus **Gems** a **Skills** en bootcamps de 2 horas, hasta 25 por encuentro, antes de que Google deje de ofrecer los Gems.",
        areas=areas, omitir_fechas=omitir, encuentro="encuentro",
        fases=[{"id": "F1", "titulo": "Noviembre", "descripcion": "**%d encuentros antes de diciembre**" % x["nov"], "destacada": True},
               {"id": "F2", "titulo": "Enero y febrero", "descripcion": "**%d encuentros de margen**" % x["ene"]}],
        frente_nombre="Bootcamps de Gems a Skills",
        celdas={"F1": "%d encuentros de 2 horas, antes de diciembre, para llegar a más personas." % x["nov"],
                "F2": "%d encuentros de margen para rezagados, siempre antes del 1 de marzo de 2027." % x["ene"]},
        alcance_titulo="Gems a Skills en bootcamps de varias áreas.",
        alcance_sub="%d encuentros de 2 horas, de hasta 25 personas, para migrar los Gems en vivo." % x["n"],
        hechos_resuelto=["BOO-1", "BOO-2"],
        participantes="Hasta 25 personas de varias áreas por encuentro; %d personas en total." % BASE_A,
        ruta_titulo="Del arranque con TI a los bootcamps.",
        ruta_nota="Los %d encuentros suman 42 horas de encuentro: %d antes de diciembre y %d en enero y febrero, con 2 facilitadores por encuentro." % (x["n"], x["nov"], x["ene"]),
        hitos=[{"titulo": "TI activa las Skills", "texto": "Antes del primer encuentro, en la consola de administración."},
               {"titulo": "Primer encuentro", "texto": "Arranca antes del 17 de noviembre, cuando los Gems pasan a Configuración."},
               {"titulo": "Cierre del grueso", "texto": "Los primeros %d encuentros terminan antes de diciembre." % x["nov"]},
               {"titulo": "Rezagados", "texto": "Los últimos %d encuentros, en enero y febrero." % x["ene"]},
               {"titulo": "Cierre", "texto": "Casos medidos y Skills compartidas, antes del 1 de marzo."}],
        duracion="%d encuentros de 2 horas en bootcamps de hasta 25 personas, de noviembre a febrero. %d horas de encuentro." % (x["n"], x["h_ses"]),
        programa=["Servicio de Innovación para Zoom (INN-006-A): Gems a Skills en bootcamps de varias áreas.",
                  "%d encuentros de 2 horas: %d horas de encuentro, con 2 facilitadores (%d horas de trabajo)." % (x["n"], x["h_ses"], x["h_fac"]),
                  "Preparación %d h, coordinación con TI %d h y seguimiento %d h." % (x["prep"], x["ti"], x["seg"]),
                  "Total: %d horas de trabajo." % x["total"]],
        cuotas=[{"cuando": "Al aprobar", "hito": "Reserva del calendario y del equipo de facilitadores.", "pct": 40},
                {"cuando": "Fin de noviembre", "hito": "Los %d encuentros de noviembre realizados." % x["nov"], "pct": 30},
                {"cuando": "Cierre", "hito": "Todos los encuentros realizados y los casos medidos.", "pct": 30}],
        intro=INTRO_BASE + " Son %d encuentros: %d antes de diciembre y %d en enero." % (x["n"], x["nov"], x["ene"]),
        extra_supuestos=["Opción A: %d personas (base de la dirección) en %d encuentros de 2 h, hasta 25 de varias áreas; 12 antes de diciembre (4 semanas × 3) y %d en enero (11 al 29 de enero)." % (BASE_A, x["n"], x["ene"])],
    )


def filas_areas_B(ses_areas, ini_f1=True):
    sol, areas = [], []
    for i, nom, n, g in ses_areas:
        fase = "F1" if g > 1 else "F2"
        areas.append({
            "id": i, "nombre": nom, "carril": "gw", "frente": "A",
            "para_que": "%d personas en %s de hasta 25: migran sus Gems a Skills en vivo." % (n, ("%d grupos" % g) if g > 1 else "un grupo"),
            "soluciones": [{"id": i + "-1", "entregable": "%s · %d personas" % (nom, n), "h": 2 * g, "fase": fase,
                            "detalle": "Referencia interna: %d encuentro(s) de 2 horas con %s (%d personas), con 1 facilitador." % (g, nom, n)}]})
    return areas


def opcion_B(r, ses_areas, total_areas):
    x = r["B"]
    n_f1 = sum(g for _, _, _, g in ses_areas if g > 1)
    n_f2 = sum(g for _, _, _, g in ses_areas if g == 1)
    return dict(
        slug="zoom-inn006-b", codigo="INN-006-B", nombre_opcion="Por área",
        meta_tipo="Plan de Innovación · Opción B, por área: %d encuentros de 2 h (%d h de encuentro) en %d áreas (%d personas), con grupos de hasta 25 · migración de Gems a Skills · calendario con fechas · formato compacto v3" % (x["n"], x["h_ses"], len(AREAS), total_areas),
        eje="Migrar a Skills los Gems de las seis áreas de Zoom (%d personas) con un encuentro de 2 horas por área, en grupos de hasta 25, antes de que Google retire los Gems" % total_areas,
        titulo_lineas=["Gems a Skills con un encuentro", "por área"],
        lead="Cada área de Zoom lleva sus **Gems** a **Skills** en un encuentro de 2 horas, en grupos de hasta 25 personas, antes de que Google los retire.",
        areas=filas_areas_B(ses_areas), omitir_fechas=[], encuentro="grupo",
        fases=[{"id": "F1", "titulo": "En grupos", "descripcion": "**áreas de más de 25 personas**", "destacada": True},
               {"id": "F2", "titulo": "Un grupo", "descripcion": "**áreas de hasta 25 personas**"}],
        frente_nombre="Un encuentro por área",
        celdas={"F1": "Operaciones y Comercial pasan de 25 personas: se dividen en grupos de hasta 25.",
                "F2": "Legal, Zoom Miami, Gestión Humana y Tecnología migran en un solo encuentro por área."},
        alcance_titulo="Gems a Skills con un encuentro por área.",
        alcance_sub="%d encuentros de 2 horas en seis áreas: %d personas, en grupos de hasta 25." % (x["n"], total_areas),
        hechos_resuelto=[i + "-1" for i, _, _, _ in ses_areas],
        participantes="Una sola área por encuentro, en grupos de hasta 25 personas; %d personas en total." % total_areas,
        ruta_titulo="Del arranque con TI a un encuentro por área.",
        ruta_nota="Los %d encuentros suman 16 horas de encuentro, con 1 facilitador por encuentro; todos se hacen antes de diciembre." % x["n"],
        hitos=[{"titulo": "TI activa las Skills", "texto": "Antes del primer encuentro, en la consola de administración."},
               {"titulo": "Áreas en grupos", "texto": "Operaciones y Comercial, en %d encuentros de hasta 25 personas." % n_f1},
               {"titulo": "Áreas de un grupo", "texto": "Legal, Zoom Miami, Gestión Humana y Tecnología, en %d encuentros." % n_f2},
               {"titulo": "Cierre", "texto": "Casos medidos y reglas de las Skills acordadas por área."}],
        duracion="%d encuentros de 2 horas, uno por área o por grupo de hasta 25 personas, antes de diciembre. %d horas de encuentro." % (x["n"], x["h_ses"]),
        programa=["Servicio de Innovación para Zoom (INN-006-B): Gems a Skills con un encuentro por área.",
                  "%d encuentros de 2 horas: %d horas de encuentro, con 1 facilitador (%d horas de trabajo)." % (x["n"], x["h_ses"], x["h_fac"]),
                  "Preparación %d h, coordinación con TI %d h y seguimiento %d h." % (x["prep"], x["ti"], x["seg"]),
                  "Total: %d horas de trabajo." % x["total"]],
        cuotas=[{"cuando": "Al aprobar", "hito": "Reserva del calendario y del equipo de facilitadores.", "pct": 50},
                {"cuando": "Cierre", "hito": "Todos los encuentros realizados y los casos medidos.", "pct": 50}],
        intro=INTRO_BASE + " Las áreas de más de 25 personas se dividen en grupos de hasta 25.",
        extra_supuestos=["Opción B: totales por área de Ivana (26/10/2026), provisionales: " + ", ".join("%s %d (%d %s)" % (nom, n, g, "grupos" if g > 1 else "grupo") for _, nom, n, g in ses_areas) + "; suman %d personas y %d encuentros. Las áreas de más de 25 se dividen en grupos de hasta 25 (Operaciones 20 + 20, Comercial 14 + 13)." % (total_areas, x["n"])],
    )


def opcion_C(r, ses_areas, total_areas):
    x = r["C"]
    areas = filas_areas_B(ses_areas)
    for a in areas:
        for s in a["soluciones"]:
            s["fase"] = "F1"
    areas.append({
        "id": "BOO", "nombre": "Bootcamp abierto", "carril": "gw", "frente": "A",
        "para_que": "Quienes no estuvieron en el encuentro de su área migran sus Gems a Skills en vivo.",
        "soluciones": [{"id": "BOO-1", "entregable": "Bootcamp abierto para quienes no estuvieron", "h": 2 * x["n_boot"], "fase": "F2",
                        "detalle": "Referencia interna: %d encuentro(s) de 2 horas, hasta 25 personas de varias áreas, con 2 facilitadores; se calcula con un supuesto de ausencia del %d %%." % (x["n_boot"], round(AUSENCIA * 100))}]})
    return dict(
        slug="zoom-inn006-c", codigo="INN-006-C", nombre_opcion="Híbrido",
        meta_tipo="Plan de Innovación · Opción C, híbrido: %d encuentros por área de 2 h y %d bootcamp abierto para quienes no estuvieron (supuesto de ausencia del %d %%, %d personas) · calendario con fechas · formato compacto v3" % (x["n_areas"], x["n_boot"], round(AUSENCIA * 100), x["ausentes"]),
        eje="Migrar a Skills los Gems de las seis áreas de Zoom con un encuentro por área y un bootcamp abierto para quienes no estuvieron, antes de que Google retire los Gems",
        titulo_lineas=["Gems a Skills por área y un", "bootcamp para quienes faltaron"],
        lead="Cada área migra sus **Gems** a **Skills** en su propio encuentro, y un bootcamp abierto recibe a quienes no pudieron asistir, antes de que Google los retire.",
        areas=areas, omitir_fechas=fechas_omitidas(datetime.date(2026, 11, 19), REINICIO - datetime.timedelta(days=1)), encuentro="grupo",
        fases=[{"id": "F1", "titulo": "Por área", "descripcion": "**un encuentro por área o grupo**", "destacada": True},
               {"id": "F2", "titulo": "Bootcamp", "descripcion": "**abierto, para quienes no estuvieron**"}],
        frente_nombre="Áreas y bootcamp",
        celdas={"F1": "%d encuentros por área antes de diciembre, en grupos de hasta 25 personas." % x["n_areas"],
                "F2": "%d bootcamp abierto en enero: supuesto de ausencia del %d %% (%d personas)." % (x["n_boot"], round(AUSENCIA * 100), x["ausentes"])},
        alcance_titulo="Gems a Skills por área y un bootcamp abierto.",
        alcance_sub="Un encuentro por área y un bootcamp abierto para quienes no estuvieron, de 2 horas cada uno.",
        hechos_resuelto=[i + "-1" for i, _, _, _ in ses_areas] + ["BOO-1"],
        participantes="Una sola área por encuentro; el bootcamp abierto, hasta 25 personas de varias áreas.",
        ruta_titulo="Del arranque con TI a los encuentros por área.",
        ruta_nota="%d encuentros por área (16 horas, 1 facilitador) más %d bootcamp de 2 horas con 2 facilitadores, para %d personas que se estima faltarán (%d %% de ausencia)." % (x["n_areas"], x["n_boot"], x["ausentes"], round(AUSENCIA * 100)),
        hitos=[{"titulo": "TI activa las Skills", "texto": "Antes del primer encuentro, en la consola de administración."},
               {"titulo": "Encuentros por área", "texto": "Seis áreas, con grupos de hasta 25 personas, antes de diciembre."},
               {"titulo": "Bootcamp abierto", "texto": "Para quienes no estuvieron, en enero, antes del tope de Google."},
               {"titulo": "Cierre", "texto": "Casos medidos y Skills compartidas, antes del 1 de marzo."}],
        duracion="%d encuentros por área y %d bootcamp abierto, de 2 horas cada uno, de noviembre a enero. %d horas de encuentro." % (x["n_areas"], x["n_boot"], x["h_ses"]),
        programa=["Servicio de Innovación para Zoom (INN-006-C): Gems a Skills por área y un bootcamp abierto.",
                  "%d encuentros: %d horas de encuentro; %d h con 1 facilitador por área y %d h con 2 en el bootcamp (%d horas de trabajo)." % (x["n"], x["h_ses"], 2 * x["n_areas"], 2 * x["n_boot"], x["h_fac"]),
                  "Preparación %d h, coordinación con TI %d h y seguimiento %d h." % (x["prep"], x["ti"], x["seg"]),
                  "Total: %d horas de trabajo." % x["total"]],
        cuotas=[{"cuando": "Al aprobar", "hito": "Reserva del calendario y del equipo de facilitadores.", "pct": 40},
                {"cuando": "Fin de noviembre", "hito": "Los encuentros por área realizados.", "pct": 30},
                {"cuando": "Cierre", "hito": "El bootcamp abierto realizado y los casos medidos.", "pct": 30}],
        intro=INTRO_BASE + " El bootcamp abierto para quienes no estuvieron va en enero.",
        extra_supuestos=["Opción C: los mismos %d encuentros por área de la opción B y %d bootcamp abierto en enero. Supuesto de ausencia: %d %% de las %d personas de las áreas no estarán en el encuentro de su área (%d personas), que caben en %d bootcamp de hasta 25; con hasta un 20 %% de ausencia (25 personas) sigue siendo 1 bootcamp." % (x["n_areas"], x["n_boot"], round(AUSENCIA * 100), total_areas, x["ausentes"], x["n_boot"])],
    )


# --- Armado del datos.json -------------------------------------------------------------------------------------------------------------
def datos(o, r, ses_areas, total_areas):
    sup = supuestos_comunes(r) + o["extra_supuestos"]
    return {
        "version": 3,
        "cliente": {"nombre": "Zoom", "slug": o["slug"], "codigo": o["codigo"], "nombre_pie": "Zoom"},
        "division": "educacion",
        "alianza": False,
        "meta_servicio": "innovacion",
        "servicio_rotulo": "Servicio de Innovación",
        "meta_tipo": o["meta_tipo"],
        "omitir": ["entregables"],
        "siglas_ok": ["IA", "TI"],
        "frases_ok": ["Las sesiones arrancan la semana del 2 de noviembre"],   # la excepción del calendario (Ivana, 26/10/2026)
        "vocabulario": {"solucion": ["encuentro", "encuentros"], "area": ["área", "áreas"]},
        "eje": o["eje"],
        "origen": "Pedido de Ivana del 26/10/2026 con el texto de la dirección de Intezia (tres opciones, A, B y C, bajo el código INN-006), la documentación oficial de Google para administradores (consultada el " + CONSULTA + "), los dashboards de impacto y el informe de casos de éxito de Zoom, los totales por área de Ivana y el Brand Kit Intezia v2.1. Sin Ficha de Levantamiento ni transcripción",
        "fuente_insumo": "Texto de la dirección y respuestas de Ivana (26/10/2026); documentación de Google para administradores (" + CONSULTA + "); dashboards y casos de éxito de Zoom",
        "supuestos": sup,
        "pendientes": pendientes_comunes(),
        "portada": {
            "titulo_lineas": o["titulo_lineas"],
            "titulo_destacado": "en Zoom",
            "lead": o["lead"],
            "hechos": [
                {"num": "Mar 2027", "texto": "Google deja de permitir crear, editar y usar Gems, no antes del 1 de marzo de 2027.", "resuelto_por": o["hechos_resuelto"]},
                {"num": "Inactivos", "texto": "es el estado en que quedan los Gems al convertirse en skills: cada creador debe activarlos.", "resuelto_por": o["hechos_resuelto"]},
                {"num": "Aparte", "texto": "van las skills de la app de Gemini y las de Workspace: no se sincronizan entre sí.", "resuelto_por": o["hechos_resuelto"]},
            ],
        },
        "cambios": cambios(),
        "carriles": [{"id": "gw", "nombre": "Gemini y Google Workspace", "nombre_corto": "Gemini y Workspace", "color": "amarillo"}],
        "areas": o["areas"],
        "alcance": {
            "titulo": o["alcance_titulo"], "subtitulo": o["alcance_sub"], "sin_conteo_por_fila": True,
            **({"etiqueta_destacados": DESTACADOS["A"][0],
                "destacados": [{"titulo": t, "texto": x} for t, x in DESTACADOS["A"][1]]} if o["codigo"].endswith("A") else {}),
            "fuera_alcance": [
                "Licencias de Google y activación de las Skills: las gestiona el equipo de TI de Zoom antes del primer encuentro.",
                "Construir Skills nuevas: se migran los Gems que ya existen y se acuerdan las reglas; lo nuevo es otra etapa.",
                "Rehacer los flujos de Workspace Studio con «Ask a Gem»: se señalan, y los rehace TI con la guía de Google.",
            ],
        },
        "fases": o["fases"],
        "frentes": [{"id": "A", "carril": "gw", "nombre": o["frente_nombre"], "celdas": o["celdas"]}],
        "seguimiento": {"tipo": "ninguno"},
        "ruta": {"titulo": o["ruta_titulo"], "subtitulo": "El horario de cada encuentro se acuerda con Zoom; las fechas están en el calendario.", "nota": o["ruta_nota"], "hitos": o["hitos"]},
        "calendario": calendario(o["omitir_fechas"], o["encuentro"], o["intro"], "%d encuentros de 2 horas, los lunes, miércoles y viernes: %d horas de encuentro." % (r[o["codigo"][-1]]["n"], r[o["codigo"][-1]]["h_ses"])),
        "metodo": metodo(o["nombre_opcion"], o["participantes"]),
        "logistica": logistica(o["participantes"]),
        "retorno": retorno(),
        "inversion": {
            "duracion": o["duracion"], "programa": o["programa"], "sin_garantia": True,
            "notas": ["Licencias de Google y accesos de TI: los gestiona Zoom y no se incluyen en esta inversión.",
                      "Valores y cuotas de pago: los define el equipo comercial de Intezia con Zoom.",
                      "Términos y condiciones: los del enlace de «Importante», que ambas partes aceptan al avanzar con esta propuesta."],
        },
        "pago": {"cuotas": o["cuotas"], "mensaje": "Los montos de cada cuota los acuerda el equipo comercial de Intezia con Zoom antes de arrancar."},
        "proximos_pasos": proximos(),
    }


CSS_MARCA = """/* Ajustes propios de esta propuesta (se enlaza después de habilidades-compacto.css). */

/* ===========================================================================
   Marca: Brand Kit Intezia v2.1 (13/10/2026). Amarillo #FFD300, Negro Noche #0A0A0A, Naranja Brasa #E58423 y Poppins (OFL).
   Sobreescribe los tokens de ../_base/styles.css para este deck. Fuentes en ../_base/fonts/ (fontsource, latin).
   =========================================================================== */
@font-face { font-family: 'Poppins'; src: url('../_base/fonts/poppins-400.woff2') format('woff2'); font-weight: 400; font-style: normal; }
@font-face { font-family: 'Poppins'; src: url('../_base/fonts/poppins-600.woff2') format('woff2'); font-weight: 600; font-style: normal; }
@font-face { font-family: 'Poppins'; src: url('../_base/fonts/poppins-700.woff2') format('woff2'); font-weight: 700; font-style: normal; }
@font-face { font-family: 'Poppins'; src: url('../_base/fonts/poppins-800.woff2') format('woff2'); font-weight: 800; font-style: normal; }
:root {
  --black: #0A0A0A;
  --yellow: #FFD300;
  --orange: #E58423;
  --font-display: "Poppins", "Inter", system-ui, sans-serif;
  --font-body: "Poppins", "Inter", system-ui, sans-serif;
  --gradient-warm: linear-gradient(135deg, #FFD300 0%, #E58423 100%);
  --gradient-warm-rev: linear-gradient(135deg, #E58423 0%, #FFD300 100%);
}
body { background: var(--black); }
.slide h1, .slide h2 { letter-spacing: -0.015em; }

/* ===========================================================================
   Zoom · Innovación con encuentros: las horas se calculan por encuentro y no por entregable, así que se ocultan los totales
   de «entregables» y los conteos de la cabecera. Base: zoom-innovacion-skills/overrides.css (INN-004).
   =========================================================================== */
.s-scope .scope-total { display: none; }
.s-route .rg-phase-n, .s-route .rg-front-n { display: none; }

/* Slide de ruta: una sola línea de trabajo y dos fases */
.s-route .route-grid { --rowh: 236px !important; }
.s-route .rg-cell { padding: 28px 30px; }
.s-route .rg-cell p { font-size: 22px; line-height: 1.42; }
.s-route .rg-front-h { font-size: 26px; }
.s-route .route-miles { margin-top: 38px; }
.s-route .mile b { font-size: 18px; margin-bottom: 8px; }
.s-route .mile p { font-size: 15px; line-height: 1.45; }
.s-route .route-note { margin-top: 20px; font-size: 14.5px; }

/* Cómo trabajamos */
.s-method .mt-steps { gap: 16px; margin-bottom: 14px; }
.s-method .mt-steps li { min-height: 104px; padding: 14px 16px 14px 62px; }
.s-method .mt-steps li::before { left: 16px; top: 15px; width: 32px; height: 32px; line-height: 32px; font-size: 16px; }
.s-method .mt-steps b { font-size: 17px; margin-bottom: 5px; }
.s-method .mt-steps span { font-size: 13px; }
.s-method .mt-strips { gap: 16px; margin-bottom: 14px; }
.s-method .mt-why, .s-method .mt-who { padding: 13px 18px; font-size: 13px; }
.s-method .mt-why b, .s-method .mt-who b { font-size: 13px; }
.s-method .mt-info { gap: 16px; margin-bottom: 14px; }
.s-method .mt-card { padding: 17px 22px 15px; }
.s-method .mt-card-label { margin-bottom: 10px; font-size: 11.5px; }
.s-method .mt-card p, .s-method .mt-card li { font-size: 14px; line-height: 1.42; }
.s-method .mt-card li { padding-bottom: 8px; }
.s-method .mt-tile { padding: 13px 16px 14px; }
.s-method .mt-tile span { font-size: 10px; margin-bottom: 6px; }
.s-method .mt-tile b { font-size: 13px; }

/* Letra más grande y sin espacios en blanco: retorno, pago y próximos pasos (zoom escala texto y espacios juntos) */
.s-roi .roi-body, .s-roi .roi-dest-wrap { zoom: 1.2; }
.s-roi .roi-dest-wrap { margin-top: 24px; }
.s-pay .sub { font-size: 17px; max-width: 980px; }
.s-pay .ps-tag { font-size: 12px; padding: 4px 12px; }
.s-pay .ps-when { font-size: 30px; margin-top: 16px; }
.s-pay .ps-hito { font-size: 15px; line-height: 1.4; margin-top: 8px; }
.s-pay .ps-lbl { font-size: 12px; }
.s-pay .pn-main { font-size: 22px; max-width: 1000px; line-height: 1.4; }
.s-pay .pn-sub { font-size: 14.5px; max-width: 980px; }
.s-next .nx-steps { margin-top: 44px; }
.s-next .nx-step { padding-top: 6px; padding-bottom: 12px; }
.s-next .nx-contact { margin-top: 36px; }
.s-next .nx-card { padding: 34px 38px 36px; }
.s-next .nx-line { font-size: 19px; }
.s-method .mt-card p, .s-method .mt-card li { font-size: 15px; }
.s-method .mt-steps span { font-size: 14px; }
.s-method .mt-why, .s-method .mt-who { font-size: 14px; padding: 15px 20px; }
.s-method .mt-tile b { font-size: 14.5px; }
.s-method .mt-tile { padding: 15px 18px 16px; }
.s-method .mt-steps li { min-height: 124px; }

/* Qué está cambiando: letra más grande para llenar la lámina */
.s-chg .sub { font-size: 18px; }
.s-chg .chg-tl, .s-chg .chg-cols { zoom: 1.2; }
.s-chg .chg-tl { margin-top: 22px; }

/* Alcance: datos de interés (alcance.destacados, solo en la opción A) y letra más grande para no dejar espacio en blanco */
.s-scope .sub { font-size: 18px; max-width: 980px; }
.s-scope.roomy:has(.scope-facts) .scope-panel { padding: 20px 28px 12px; }
.s-scope.roomy:has(.scope-facts) .scope-rows .area { font-size: 22px; }
.s-scope.roomy:has(.scope-facts) .scope-rows .para { font-size: 17px; line-height: 1.4; }
.s-scope.roomy:has(.scope-facts) .scope-panels.one .scope-rows li { grid-template-columns: 340px 1fr auto; padding: 16px 0 18px; }
.s-scope .scope-facts { margin-top: 22px; }
.s-scope .scope-facts .scope-card-label { font-size: 12px; padding: 5px 12px; }
.s-scope .scope-facts ul { list-style: none; margin: 12px 0 0; padding: 0; display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
.s-scope .scope-facts li { border-top: 4px solid var(--yellow); background: rgba(10, 10, 10, 0.045); border-radius: 0 0 11px 11px; padding: 14px 18px 16px; min-height: 128px; }
.s-scope .scope-facts li:nth-child(even) { border-top-color: var(--orange); }
.s-scope .scope-facts b { display: block; font-family: var(--font-display); font-weight: 700; font-size: 17px; line-height: 1.2; margin-bottom: 8px; color: var(--black); }
.s-scope .scope-facts span { font-family: var(--font-body); font-size: 14px; line-height: 1.45; color: rgba(10, 10, 10, 0.82); }
.s-scope.roomy:has(.scope-facts) .scope-out { margin-top: 18px; padding: 14px 24px; grid-template-columns: 170px 1fr; }
.s-scope.roomy:has(.scope-facts) .scope-out li { font-size: 14px; line-height: 1.45; padding: 4px 0 4px 16px; }
.s-scope.roomy:has(.scope-facts) .scope-out li::before { top: 12px; }
.s-scope.roomy:not(:has(.scope-facts)) .scope-out li { font-size: 14px; line-height: 1.45; }
.s-scope.roomy:not(:has(.scope-facts)) .scope-card-label { font-size: 12px; }
.s-scope.roomy:not(:has(.scope-facts)) .scope-panel { padding: 16px 24px 8px; }
.s-scope.roomy:not(:has(.scope-facts)) .scope-panels.one .scope-rows li { padding: 11px 0 12px; grid-template-columns: 300px 1fr auto; }
.s-scope.roomy:not(:has(.scope-facts)) .scope-rows .area { font-size: 18px; }
.s-scope.roomy:not(:has(.scope-facts)) .scope-rows .para { font-size: 15px; }

/* Calendario con pocas filas (B y C): letra más grande y filas más altas */
.s-cal:not(:has(.cal-col li:nth-child(8))) .cal-box { padding: 26px 34px 20px; }
.s-cal:not(:has(.cal-col li:nth-child(8))) .cal-label { font-size: 16px; margin-bottom: 12px; }
.s-cal:not(:has(.cal-col li:nth-child(8))) .cal-intro { font-size: 16px; line-height: 1.45; margin-bottom: 14px; }
.s-cal:not(:has(.cal-col li:nth-child(8))) .cal-col li { height: 78px !important; grid-template-columns: 112px 1fr; }
.s-cal:not(:has(.cal-col li:nth-child(8))) .cal-d { font-size: 18px; }
.s-cal:not(:has(.cal-col li:nth-child(8))) .cal-t { font-size: 17px; line-height: 1.25; }
.s-cal:not(:has(.cal-col li:nth-child(5))) .cal-col li { height: 100px !important; }
.s-cal:not(:has(.cal-col li:nth-child(5))) .cal-box { padding-top: 32px; }
.s-scope.roomy:not(:has(.scope-facts)):not(:has(.scope-rows li:nth-child(7))) .scope-panels.one .scope-rows li { padding: 14px 0 15px; }
.s-scope.roomy:not(:has(.scope-facts)):not(:has(.scope-rows li:nth-child(7))) .scope-out { margin-top: 22px; padding: 16px 24px; }

/* ===========================================================================
   Slide de calendario (s-cal): opción del generador (ESTEI CAI-058, 20/10/2026). Pendiente de pasar al CSS canónico.
   =========================================================================== */
.s-cal { background: var(--black); color: var(--white); padding: 44px 56px 0; }
.s-cal .counter { color: var(--yellow); }
.s-cal .eyebrow { color: var(--orange); margin-bottom: 6px; }
.s-cal h2 { font-family: var(--font-display); font-weight: 700; font-size: 36px; line-height: 1.05; margin-bottom: 8px; }
.s-cal .sub { font-family: var(--font-body); font-size: 15px; line-height: 1.4; max-width: 940px; color: rgba(255, 255, 255, 0.82); }
.s-cal .foot .meta { color: rgba(255, 255, 255, 0.65); }
.s-cal .cal-box { margin-top: 22px; padding: 20px 30px 14px; border-left: 6px solid var(--yellow); background: rgba(255, 255, 255, 0.04); border-radius: 0 10px 10px 0; }
.s-cal .cal-label { font-family: var(--font-display); font-weight: 700; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--yellow); margin-bottom: 8px; }
.s-cal .cal-intro { font-family: var(--font-body); font-size: 13.5px; line-height: 1.4; color: rgba(255, 255, 255, 0.85); margin-bottom: 8px; }
.s-cal .cal-cols { display: grid; grid-template-columns: 1fr 1fr; column-gap: 28px; margin-top: 6px; }
.s-cal .cal-col { list-style: none; margin: 0; padding: 0; }
.s-cal .cal-col li { display: grid; grid-template-columns: 84px 1fr; align-items: center; column-gap: 10px; height: var(--cal-rowh); border-bottom: 1px solid rgba(255, 255, 255, 0.14); }
.s-cal .cal-col li:last-child { border-bottom: none; }
.s-cal .cal-d { font-family: var(--font-display); font-weight: 700; font-size: 14px; color: var(--yellow); white-space: nowrap; }
.s-cal .cal-h { display: none; }
.s-cal .cal-t { font-family: var(--font-display); font-weight: 600; font-size: 12.5px; line-height: 1.2; color: var(--white); }

/* ===========================================================================
   Slide «Qué está cambiando» (s-chg): opción del generador (Zoom INN-006, 26/10/2026). Slide oscura: fechas del proveedor,
   qué pasa si no se hace nada y por qué con Intezia. Pendiente de pasar al CSS canónico.
   =========================================================================== */
.s-chg { background: var(--black); color: var(--white); padding: 40px 56px 0; }
.s-chg .counter { color: var(--yellow); }
.s-chg .eyebrow { color: var(--orange); margin-bottom: 6px; }
.s-chg h2 { font-family: var(--font-display); font-weight: 700; font-size: 34px; line-height: 1.05; margin-bottom: 8px; }
.s-chg .sub { font-family: var(--font-body); font-size: 14.5px; line-height: 1.4; max-width: 940px; color: rgba(255, 255, 255, 0.82); }
.s-chg .foot .meta { color: rgba(255, 255, 255, 0.65); }
.s-chg .chg-label { font-family: var(--font-display); font-weight: 700; font-size: 12px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--yellow); margin-bottom: 8px; }
.s-chg .chg-tl { margin-top: 18px; }
.s-chg .chg-events { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(var(--chg-n), 1fr); gap: 12px; }
.s-chg .chg-events li { border-top: 3px solid var(--yellow); background: rgba(255, 255, 255, 0.05); border-radius: 0 0 8px 8px; padding: 11px 14px 13px; }
.s-chg .chg-d { display: block; font-family: var(--font-display); font-weight: 800; font-size: 18px; line-height: 1.1; color: var(--yellow); margin-bottom: 6px; }
.s-chg .chg-t { font-family: var(--font-body); font-size: 12.5px; line-height: 1.4; color: rgba(255, 255, 255, 0.9); }
.s-chg .chg-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }
.s-chg .chg-box { padding: 15px 20px 8px; border-radius: 10px; background: rgba(255, 255, 255, 0.05); border-left: 5px solid var(--orange); }
.s-chg .chg-why { border-left-color: var(--yellow); }
.s-chg .chg-box ul { list-style: none; margin: 0; padding: 0; }
.s-chg .chg-box li { font-family: var(--font-body); font-size: 12.5px; line-height: 1.4; margin-bottom: 9px; color: rgba(255, 255, 255, 0.88); }
.s-chg .chg-box li b { display: block; font-family: var(--font-display); font-weight: 700; font-size: 13.5px; color: var(--white); margin-bottom: 1px; }
.s-chg .chg-src { margin-top: 12px; font-family: var(--font-body); font-size: 10.5px; line-height: 1.4; color: rgba(255, 255, 255, 0.6); max-width: 960px; }
"""


def correr(cmd):
    r = subprocess.run(cmd, cwd=str(RAIZ), text=True, capture_output=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    generar = "--sin-generar" not in sys.argv
    ses_areas, total_areas, r = calcular()
    print("Totales: base A = %d; áreas B/C = %d personas; encuentros A=%d B=%d C=%d; horas totales A=%d B=%d C=%d" % (
        BASE_A, total_areas, r["A"]["n"], r["B"]["n"], r["C"]["n"], r["A"]["total"], r["B"]["total"], r["C"]["total"]))
    for fn in (opcion_A, opcion_B, opcion_C):
        o = fn(r, ses_areas, total_areas)
        carpeta = PROPUESTAS / o["slug"]
        carpeta.mkdir(parents=True, exist_ok=True)
        d = datos(o, r, ses_areas, total_areas)
        (carpeta / "datos.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (carpeta / "overrides.css").write_text(CSS_MARCA, encoding="utf-8")
        if generar:
            rc, out = correr([sys.executable, "scripts/generar-habilidades-compacto.py", o["slug"]])
            print("== %s (%s) · rc=%d" % (o["codigo"], o["slug"], rc))
            print("\n".join(l for l in out.splitlines() if l.startswith(("⚠", "✗", "✓", "  ✗")) or "error" in l.lower()))
            css = carpeta / "habilidades-compacto.css"
            if css.exists():   # amarillo de la marca v2.1 en los tintes del CSS compacto (copia congelada de este deck)
                t = css.read_text(encoding="utf-8")
                t2 = t.replace("rgba(244, 186, 26", "rgba(255, 211, 0").replace("rgba(244,186,26", "rgba(255,211,0")
                if t2 != t:
                    css.write_text(t2, encoding="utf-8")


if __name__ == "__main__":
    main()
