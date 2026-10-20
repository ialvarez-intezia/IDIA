/**
 * Intezia · Crea los 4 EduPulse (Habilidades, Detección, Políticas, Innovación) y el EduTrace
 * en Google Forms, conservando el membrete (imagen, color y tipografía) de un formulario plantilla.
 *
 * CÓMO USARLO
 * 1. Abre script.google.com con tu cuenta de Intezia y crea un proyecto nuevo.
 * 2. Pega este archivo completo en Código.gs.
 * 3. Completa PLANTILLA_EDUPULSE_ID y PLANTILLA_EDUTRACE_ID (ver CONFIG). El ID es el tramo largo
 *    de la URL de EDICIÓN del formulario: docs.google.com/forms/d/<ID>/edit
 *    (no sirve el de la URL de respuesta, la que dice /e/1FAIpQ...).
 * 4. Elige la función crearTodo y pulsa Ejecutar. Acepta los permisos.
 * 5. Abre el registro de ejecución: ahí quedan los enlaces de edición y de respuesta de cada formulario.
 * 6. Para cada formulario, haz los pasos manuales que el registro lista al final.
 *
 * ENLACES PRELLENADOS (empresa, grupo y sesión ya puestos): usa enlacePrellenado() más abajo.
 *
 * Todas las escalas son 1-5. Las respuestas de los EduPulse son anónimas (no se recoge correo).
 * Lo único que se escribe por cliente: las 4 preguntas de la sección «Evaluación de conocimientos» del EduTrace.
 */

const CONFIG = {
  // ID de edición del formulario que tiene el membrete de Intezia para los EduPulse.
  PLANTILLA_EDUPULSE_ID: 'PEGA_AQUI_EL_ID_DEL_FORMULARIO_CON_EL_MEMBRETE',
  // ID de edición del EduTrace que se usará como plantilla de membrete.
  // Por defecto: el EduTrace de Zoom Mercadeo. Cámbialo por uno sin datos de cliente si prefieres.
  PLANTILLA_EDUTRACE_ID: '16AOe57IdLZ6oGJTQSlG9q5v5wKExS3dlSiHOoZdfMEE',
  // Carpeta de Drive donde quedan los formularios y sus hojas de respuestas (opcional; vacío = Mi unidad).
  CARPETA_ID: '',

  TITULO_EDUPULSE: 'EduPulse: Cuéntanos todo sobre esta sesión.',
  // Texto del membrete actual + frase de anonimato.
  DESCRIPCION_EDUPULSE:
    'Aviso de Asistencia: Completar este EduPulse toma menos de 2 minutos y es requisito indispensable ' +
    'para la validación y curaduría de tu asistencia de la sesión de hoy. ' +
    'Es anónimo: no te pedimos nombre ni correo, y tus respuestas solo se muestran agrupadas.',

  TITULO_EDUTRACE: 'EduTrace: Análisis de Impacto',
  DESCRIPCION_EDUTRACE:
    'Esta encuesta cierra tu formación y contrasta lo que logramos con lo que se ofreció en la propuesta. ' +
    'Completarla es requisito para tu certificado de participación, sujeto a la validación de asistencia por sesión.\n\n' +
    'Es personal e intransferible: respóndela tú.\n\n' +
    'Tus respuestas individuales no se comparten con tu empresa. Tu organización recibe resultados agrupados del equipo ' +
    'y la lista de participantes (nombre y área), sin puntajes. Solo citaremos un comentario tuyo si lo autorizas al final.'
};

const LIK = ['No, para nada', 'Sí, completamente'];
const LIKA = ['Totalmente en desacuerdo', 'Totalmente de acuerdo'];
const DOM = ['Deficiente', 'Excelente'];
const SESIONES = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'];

// ------------------------------------------------------------------ EDUPULSE
const TEXTO_DOMINIO = '¿Cómo evalúas el nivel de dominio técnico y la experiencia demostrada por el consultor de Intezia?';
const TEXTO_RAZONES = '¿Qué hizo la diferencia hoy? Marca todas las que apliquen.';
const TEXTO_TIEMPO = 'En general, la sesión fue un buen uso de mi tiempo.';
const TEXTO_COMENT = 'Déjanos tus comentarios.';

// k: lik (escala 1-5 de acuerdo), dom (deficiente-excelente), razones (casillas), coment (texto largo opcional)
const EDUPULSE = {
  Habilidades: [
    { k: 'lik', t: 'Lo que trabajamos hoy fue sobre una tarea real de mi trabajo.' },
    { k: 'lik', t: 'Me siento capaz de repetir lo que hicimos hoy sin ayuda.' },
    { k: 'lik', t: 'Lo que construimos hoy ya resuelve un proceso real de mi trabajo.' },
    { k: 'lik', t: 'Tengo claro qué proceso de mi trabajo voy a resolver con esto esta semana.' },
    { k: 'lik', t: TEXTO_TIEMPO },
    { k: 'dom', t: TEXTO_DOMINIO },
    { k: 'razones', t: TEXTO_RAZONES, ops: [
      'Practicar con mis propios datos o casos', 'El ejemplo del consultor', 'El material de apoyo', 'El ritmo de la sesión',
      'Trabajar junto a mis compañeros(as)', 'Faltó tiempo para practicar', 'El nivel fue muy alto para mí',
      'El nivel fue muy básico para mí', 'Problemas de acceso o con la herramienta', 'Los ejemplos no eran de mi trabajo'] },
    { k: 'coment', t: TEXTO_COMENT }
  ],
  Deteccion: [
    { k: 'lik', t: 'Las preguntas de la sesión fueron relevantes para mi día a día, no genéricas.' },
    { k: 'lik', t: 'La sesión me ayudó a ver con más claridad dónde se me va el tiempo en tareas repetitivas.' },
    { k: 'lik', t: 'El consultor entendió bien la forma en la que trabaja mi área.' },
    { k: 'lik', t: 'Me sentí cómodo(a) compartiendo cómo trabajamos realmente.' },
    { k: 'lik', t: 'Salí de la sesión con algo concreto que puedo usar esta semana.' },
    { k: 'lik', t: 'El consultor me mostró cómo resolver con IA un proceso real de mi área (por ejemplo, resumir mis correos con un conector).' },
    { k: 'lik', t: TEXTO_TIEMPO },
    { k: 'dom', t: TEXTO_DOMINIO },
    { k: 'razones', t: TEXTO_RAZONES, ops: [
      'Las preguntas estaban bien dirigidas a mi trabajo', 'Hubo tiempo suficiente para explicar mi proceso',
      'Los ejemplos de otras áreas me ayudaron a recordar tareas', 'El consultor me mostró cómo resolverlo con IA',
      'Las preguntas fueron demasiado generales', 'Faltó tiempo para explicar mi proceso',
      'No era la persona indicada para responder algunas preguntas', 'Dudé sobre para qué se usaría mi información'] },
    { k: 'coment', t: TEXTO_COMENT }
  ],
  Politicas: [
    { k: 'lik', t: 'Las preguntas de hoy reflejaron los riesgos y dudas reales de mi área sobre el uso de IA.' },
    { k: 'lik', t: 'La sesión me ayudó a entender mejor qué reglas necesitamos como equipo.' },
    { k: 'lik', t: 'El consultor explicó con claridad para qué se usará la información que compartí.' },
    { k: 'lik', t: 'Confío en que mis aportes quedarán reflejados en la política final.' },
    { k: 'lik', t: 'Las reglas que discutimos hoy son realistas para cumplirlas en mi trabajo diario.' },
    { k: 'lik', t: TEXTO_TIEMPO },
    { k: 'dom', t: TEXTO_DOMINIO },
    { k: 'razones', t: TEXTO_RAZONES, ops: [
      'Los ejemplos de situaciones reales', 'Poder expresar mis dudas y riesgos',
      'Que se explicara para qué se usa la información', 'Escuchar las posturas de otras personas del equipo',
      'Las reglas discutidas son difíciles de cumplir en mi día a día', 'No tengo claro quién decide la política final',
      'Dudo de que mi opinión cuente', 'Faltó tiempo'] },
    { k: 'coment', t: TEXTO_COMENT }
  ],
  Innovacion: [
    { k: 'lik', t: 'El tema de hoy fue relevante para lo que necesito en este momento.' },
    { k: 'lik', t: 'Me siento capaz de aplicar lo trabajado hoy sin ayuda.' },
    { k: 'lik', t: 'Aprendí algo que puedo aplicar esta semana.' },
    { k: 'lik', t: 'La sesión mantuvo mi interés de principio a fin.' },
    { k: 'lik', t: 'Después de esta sesión, tengo más ganas de seguir usando IA en mi trabajo.' },
    { k: 'lik', t: 'Salgo de la sesión con una idea o prueba concreta que voy a ejecutar.' },
    { k: 'lik', t: TEXTO_TIEMPO },
    { k: 'dom', t: TEXTO_DOMINIO },
    { k: 'razones', t: TEXTO_RAZONES, ops: [
      'Ver ejemplos de otras empresas o casos', 'Probar la idea durante la sesión',
      'Que el tema conectara con un problema que tengo', 'El ritmo de la sesión',
      'El tema estaba lejos de mi trabajo', 'El nivel fue muy alto para mí', 'El nivel fue muy básico para mí',
      'Faltó tiempo para probar'] },
    { k: 'coment', t: TEXTO_COMENT }
  ]
};

// ------------------------------------------------------------------ PRINCIPAL
function crearTodo() {
  const salida = [];
  Object.keys(EDUPULSE).forEach(function (servicio) {
    salida.push(crearEduPulse_(servicio));
  });
  salida.push(crearEduTrace_());

  Logger.log('FORMULARIOS CREADOS');
  salida.forEach(function (f) {
    Logger.log('\n' + f.nombre + '\n  Editar:   ' + f.editUrl + '\n  Responder: ' + f.publicUrl + '\n  Respuestas (hoja): ' + f.hojaUrl);
  });
  Logger.log(
    '\nPASOS MANUALES (el script no puede hacerlos):\n' +
    '1. EduTrace, sección de conocimientos: reemplaza los 4 marcadores [COMPLETAR POR CLIENTE] por las preguntas del cliente ' +
    'y activa «Barajar el orden de las opciones» (⋮ de cada pregunta). Las 4 opciones del mismo largo.\n' +
    '2. EduPulse: confirma en Configuración > Respuestas que NO está activado «Recopilar correos» ni «Limitar a 1 respuesta».\n' +
    '3. Comprueba la rama del EduTrace: «Todavía no» salta a «Lo que te frena» y «Sí» pasa por «Tu tarea» y se salta «Lo que te frena».\n' +
    '4. Revisa que el membrete (imagen, color, tipografía) se conservó. Si no, revisa que la plantilla sea el formulario correcto.'
  );
}

function crearEduPulse_(servicio) {
  const nombre = 'EduPulse · ' + servicio.replace('Deteccion', 'Detección').replace('Politicas', 'Políticas').replace('Innovacion', 'Innovación');
  const form = copiarPlantilla_(CONFIG.PLANTILLA_EDUPULSE_ID, nombre);
  form.setTitle(CONFIG.TITULO_EDUPULSE);
  form.setDescription(CONFIG.DESCRIPCION_EDUPULSE);
  configurarAnonimo_(form);

  // Cabecera: se prellena por enlace (ver enlacePrellenado)
  form.addTextItem().setTitle('Empresa').setRequired(true);
  form.addTextItem().setTitle('Grupo o área').setRequired(true);
  form.addListItem().setTitle('Número de la sesión').setChoiceValues(SESIONES).setRequired(true);

  EDUPULSE[servicio].forEach(function (s) {
    if (s.k === 'lik') escala_(form, s.t, LIK, true);
    else if (s.k === 'dom') escala_(form, s.t, DOM, true);
    else if (s.k === 'razones') form.addCheckboxItem().setTitle(s.t).setChoiceValues(s.ops).showOtherOption(true).setRequired(false);
    else if (s.k === 'coment') form.addParagraphTextItem().setTitle(s.t).setRequired(false);
  });
  return resumen_(form, nombre);
}

// ------------------------------------------------------------------ EDUTRACE
function crearEduTrace_() {
  const nombre = 'EduTrace · Plantilla';
  const form = copiarPlantilla_(CONFIG.PLANTILLA_EDUTRACE_ID, nombre);
  form.setTitle(CONFIG.TITULO_EDUTRACE);
  form.setDescription(CONFIG.DESCRIPCION_EDUTRACE);
  form.setCollectEmail(false);          // el correo se pide como pregunta (opcional), no con la cuenta de Google
  form.setLimitOneResponsePerUser(false);
  try { form.setRequireLogin(false); } catch (e) { /* el dominio puede no permitirlo */ }
  form.setProgressBar(true);

  form.addSectionHeaderItem().setTitle('Datos de identificación').setHelpText('Se usan para tu certificado y la lista de participación. Nunca se publican junto a tus respuestas.');
  form.addTextItem().setTitle('Nombre completo').setRequired(true);
  form.addTextItem().setTitle('Cédula de identidad').setRequired(true);
  form.addTextItem().setTitle('Correo electrónico corporativo').setRequired(false);
  form.addTextItem().setTitle('Departamento o área').setRequired(true);

  form.addSectionHeaderItem().setTitle('Perfil de egreso').setHelpText('Evalúa del 1 al 5, donde 1 es «Totalmente en desacuerdo» y 5 es «Totalmente de acuerdo».');
  escala_(form, 'Competencia adquirida: «Tras finalizar la formación, me siento capaz de operar las herramientas aprendidas sin supervisión.»', LIKA, true);
  escala_(form, 'Impacto en productividad: «Lo aprendido ya me permite hacer mis tareas en menos tiempo.»', LIKA, true);
  escala_(form, 'Cumplimiento de la propuesta: «La formación cumplió lo que se ofreció en la propuesta.»', LIKA, true);

  form.addSectionHeaderItem().setTitle('Evaluación de conocimientos')
    .setHelpText('Es la única sección que cambia en cada formación. Selecciona la respuesta que consideres correcta.');
  for (let i = 1; i <= 4; i++) {
    form.addMultipleChoiceItem()
      .setTitle('[COMPLETAR POR CLIENTE] Pregunta de conocimiento ' + i)
      .setChoiceValues(['Opción a', 'Opción b', 'Opción c', 'Opción d'])
      .setRequired(true);
  }

  form.addSectionHeaderItem().setTitle('Aplicación real');
  const aplicaste = form.addMultipleChoiceItem().setTitle('¿Ya aplicaste lo aprendido en tu trabajo?').setRequired(true);

  // Rama «Sí»: tu tarea
  const paginaTarea = form.addPageBreakItem().setTitle('Tu tarea').setHelpText('Piensa en la tarea de tu trabajo en la que más has usado lo aprendido.');
  form.addTextItem().setTitle('¿Cuál es esa tarea?').setRequired(true);
  numero_(form, 'Antes, ¿cuántos minutos te tomaba hacerla?', 0, 1000);
  numero_(form, 'Ahora, ¿cuántos minutos te toma?', 0, 1000);
  numero_(form, '¿Cuántas veces por semana la haces?', 0, 100);

  // Rama «Todavía no»: lo que te frena
  const paginaFrenos = form.addPageBreakItem().setTitle('Lo que te frena');
  form.addCheckboxItem().setTitle('¿Qué te lo ha impedido? Marca todas las que apliquen.')
    .setChoiceValues(['No he tenido tiempo', 'No tengo acceso o licencia de la herramienta', 'No sé cómo aplicarlo a mis tareas', 'Mi equipo o mi jefe no lo respalda'])
    .showOtherOption(true).setRequired(true);

  // Resto, común a ambas ramas
  const paginaResto = form.addPageBreakItem().setTitle('Radar de necesidades').setHelpText('Información para diseñar nuevas propuestas.');
  form.addMultipleChoiceItem().setTitle('¿Qué área de tu trabajo aún requiere más automatización?')
    .setChoiceValues(['Reportes', 'Datos y análisis', 'CRM y seguimiento de clientes', 'Contenido y comunicación', 'Atención al cliente y soporte',
      'Administración y finanzas', 'Tecnología y seguridad']).showOtherOption(true).setRequired(true);
  form.addTextItem().setTitle('¿Qué otros departamentos de tu organización se beneficiarían de una formación similar?').setRequired(true);
  form.addMultipleChoiceItem().setTitle('¿Cuál es la herramienta de IA que más usa tu equipo actualmente?')
    .setChoiceValues(['Claude (Anthropic)', 'Gemini (Google)', 'ChatGPT (OpenAI)', 'Microsoft Copilot', 'Herramientas nativas/internas', 'Ninguna']).setRequired(true);

  form.addSectionHeaderItem().setTitle('Cierre');
  escala_(form, 'Recomendaría esta formación a un colega.', LIKA, true);
  form.addTextItem().setTitle('En una frase, ¿qué fue lo más valioso de esta formación?').setRequired(false);
  form.addMultipleChoiceItem().setTitle('¿Podemos citar tu comentario?')
    .setChoiceValues(['Sí, con mi nombre', 'Sí, sin mi nombre', 'No']).setRequired(true);

  // Ramas (se fijan al final, cuando ya existen las páginas)
  aplicaste.setChoices([
    aplicaste.createChoice('Sí, varias veces', paginaTarea),
    aplicaste.createChoice('Sí, una vez', paginaTarea),
    aplicaste.createChoice('Todavía no', paginaFrenos)
  ]);
  paginaTarea.setGoToPage(paginaResto);   // quien aplicó se salta «Lo que te frena»

  return resumen_(form, nombre);
}

// ------------------------------------------------------------------ ENLACES PRELLENADOS
/**
 * Devuelve el enlace de un EduPulse con empresa, grupo y sesión ya puestos.
 * Ejemplo (ejecútalo desde el editor cambiando los valores):
 *   Logger.log(enlacePrellenado('ID_DEL_EDUPULSE', 'Empresa Ejemplo', 'Ventas', 3));
 */
function enlacePrellenado(formId, empresa, grupo, sesion) {
  const form = FormApp.openById(formId);
  const items = form.getItems();            // 0 empresa, 1 grupo, 2 sesión (así los crea crearEduPulse_)
  const r = form.createResponse();
  r.withItemResponse(items[0].asTextItem().createResponse(String(empresa)));
  r.withItemResponse(items[1].asTextItem().createResponse(String(grupo)));
  r.withItemResponse(items[2].asListItem().createResponse(String(sesion)));
  return r.toPrefilledUrl();
}

// ------------------------------------------------------------------ AUXILIARES
function copiarPlantilla_(plantillaId, nombre) {
  const copia = DriveApp.getFileById(plantillaId).makeCopy(nombre);
  if (CONFIG.CARPETA_ID) copia.moveTo(DriveApp.getFolderById(CONFIG.CARPETA_ID));
  const form = FormApp.openById(copia.getId());
  form.getItems().forEach(function (it) { form.deleteItem(it); });   // conserva membrete y tema, vacía las preguntas
  return form;
}

function configurarAnonimo_(form) {
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  try { form.setRequireLogin(false); } catch (e) { /* el dominio puede no permitirlo */ }
  form.setAllowResponseEdits(false);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(false);
}

function escala_(form, titulo, etiquetas, requerida) {
  form.addScaleItem().setTitle(titulo).setBounds(1, 5).setLabels(etiquetas[0], etiquetas[1]).setRequired(requerida !== false);
}

function numero_(form, titulo, minimo, maximo) {
  const it = form.addTextItem().setTitle(titulo).setRequired(true);
  it.setValidation(FormApp.createTextValidation()
    .setHelpText('Escribe un número entre ' + minimo + ' y ' + maximo + '.')
    .requireNumberBetween(minimo, maximo).build());
}

function resumen_(form, nombre) {
  const hoja = SpreadsheetApp.create('Respuestas · ' + nombre);
  if (CONFIG.CARPETA_ID) DriveApp.getFileById(hoja.getId()).moveTo(DriveApp.getFolderById(CONFIG.CARPETA_ID));
  form.setDestination(FormApp.DestinationType.SPREADSHEET, hoja.getId());
  return { nombre: nombre, editUrl: form.getEditUrl(), publicUrl: form.getPublishedUrl(), hojaUrl: hoja.getUrl() };
}
