#!/usr/bin/env node
// verificar-habilidades-compacto.js <slug | ruta/index.html>
//
// Mide con Chrome headless (media print, 1123x794) las holguras exactas del deck compacto de Habilidades
// que el detector estándar (verificar-overflow.js) NO ve: colisiones entre bloques con posición absoluta,
// texto que se sale de su tarjeta (scrollHeight) y distancia al pie de página. Complementa a
// verificar-overflow.js (corre los dos). Spec: plantillas/habilidades-compacto.md.
//
// Salida: 0 = todo con holgura | 1 = algún bloque choca o queda a menos del mínimo.
//   Mínimo de holgura: 8 px (pie de página) · 10 px (catálogo contra la franja inferior) · 4 px (Duración/Programa).
'use strict';
const fs = require('fs'), os = require('os'), path = require('path');
const { spawn } = require('child_process');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const ROOT = path.resolve(__dirname, '..');
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function resolveHtml(arg) {
  if (!arg) { console.error('Uso: node scripts/verificar-habilidades-compacto.js <slug | ruta/index.html>'); process.exit(2); }
  if (arg.endsWith('.html')) return path.resolve(arg);
  return path.join(ROOT, 'clientes', 'propuestas', arg, 'index.html');
}

const MEDIR = `(async () => {
  if (document.fonts && document.fonts.ready) { try { await document.fonts.ready; } catch (e) {} }
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const out = [];   // {slide, check, valor, minimo, ok}
  const slides = [...document.querySelectorAll('.slide')];
  const top = (s, el) => el.getBoundingClientRect().top - s.getBoundingClientRect().top;
  const bot = (s, el) => el.getBoundingClientRect().bottom - s.getBoundingClientRect().bottom + s.getBoundingClientRect().height;
  const add = (n, check, holgura, minimo, detalle, unidad) => out.push({ slide: n, check, holgura: Math.round(holgura * 10) / 10, minimo, ok: holgura >= minimo, detalle: detalle || '', unidad: unidad === undefined ? 'px' : unidad });
  const overflowEls = (n, s, sel, label) => {
    s.querySelectorAll(sel).forEach((el, i) => {
      const ex = el.scrollHeight - el.clientHeight;
      if (ex > 1) out.push({ slide: n, check: label + ' #' + (i + 1) + ' desborda su caja', holgura: -ex, minimo: 0, ok: false });
    });
  };
  slides.forEach((s, i) => {
    const n = i + 1;
    const foot = s.querySelector('.foot');
    const footTop = foot ? top(s, foot) : s.getBoundingClientRect().height - 40;
    if (s.classList.contains('s-cover')) {
      const src = s.querySelector('.pain-src') || s.querySelector('.pain-strip');
      const idl = s.querySelector('.id-line');
      if (src && idl) add(n, 'portada: fuente/datos de dolor vs línea de código', top(s, idl) - bot(s, src), 8);
      const hire = s.querySelector('.hire-note'); const strip = s.querySelector('.pain-strip');
      if (hire && strip) add(n, 'portada: datos de dolor vs franja de contratación', top(s, hire) - bot(s, strip), 6);
      if (hire && src) add(n, 'portada: franja de contratación vs fuente', top(s, src) - bot(s, hire), 4);
      const h1 = s.querySelector('h1'); const lead = s.querySelector('.lead');
      if (h1 && lead) add(n, 'portada: titular vs lead', top(s, lead) - bot(s, h1), 6);
    }
    if (s.classList.contains('s-scope')) {
      const paneles = s.querySelector('.scope-panels'), fuera = s.querySelector('.scope-out');
      const ultimo = fuera || paneles;
      const filas = s.querySelectorAll('.scope-rows li').length;
      add(n, 'alcance: ' + (fuera ? 'franja «Fuera de este alcance»' : 'paneles') + ' vs pie', footTop - bot(s, ultimo), 8,
        'paneles ' + Math.round(paneles.getBoundingClientRect().height) + ' px (' + filas + ' filas)' + (fuera ? ', franja de fuera de alcance ' + Math.round(fuera.getBoundingClientRect().height) + ' px' : '') + '. Acortar subtitulo, para_que o fuera_alcance, o usar alcance.compacto');
      if (fuera) add(n, 'alcance: paneles vs franja «Fuera de este alcance»', top(s, fuera) - bot(s, paneles), 8);
      overflowEls(n, s, '.scope-panel', 'panel de herramienta'); overflowEls(n, s, '.scope-out', 'franja de fuera de alcance');
      s.querySelectorAll('.scope-rows li').forEach((li, i) => {
        const a = li.querySelector('.area'), nn = li.querySelector('.n');
        const ar = a.getBoundingClientRect(), nr = nn.getBoundingClientRect();
        if (ar.right > nr.left + 1 && ar.bottom > nr.top + 1 && ar.top < nr.bottom - 1) out.push({ slide: n, check: 'alcance: fila ' + (i + 1) + ' (' + a.textContent.trim().slice(0, 30) + ') pisa la píldora de soluciones', holgura: -Math.round(ar.right - nr.left), minimo: 0, ok: false, detalle: 'acortar el nombre del área (≤ 38 caracteres con una herramienta, ≤ 46 con dos)' });
      });
    }
    if (s.classList.contains('s-route')) {
      const nota = s.querySelector('.route-note'), sig = s.querySelector('.route-next');
      const ultimo = sig || nota;
      if (ultimo) add(n, 'ruta: ' + (sig ? 'siguiente etapa' : 'nota inferior') + ' vs pie', footTop - bot(s, ultimo), 8);
      if (nota && sig) add(n, 'ruta: nota vs siguiente etapa', top(s, sig) - bot(s, nota), 3);
      overflowEls(n, s, '.rg-cell', 'celda'); overflowEls(n, s, '.rg-front', 'línea de trabajo');
      s.querySelectorAll('.rg-front').forEach((fr, i) => {
        const lim = fr.getBoundingClientRect().right - 8;
        let peor = 0, quien = '';
        fr.querySelectorAll('.rg-front-h, .rg-front-tool, .rg-front-n, .rg-front-meta').forEach((el) => { const ex = el.getBoundingClientRect().right - lim; if (ex > peor) { peor = ex; quien = el.textContent.trim().slice(0, 40); } });
        add(n, 'ruta: línea de trabajo #' + (i + 1) + ' dentro de su tarjeta (ancho)', -peor, 0, peor ? 'sobresale ' + Math.round(peor) + ' px: «' + quien + '». Acortar frentes[].nombre (≤ 36 caracteres con 3 líneas de trabajo) o carriles[].nombre_corto' : '');
        const h = fr.querySelector('.rg-front-h'); const lineas = Math.round(h.getBoundingClientRect().height / parseFloat(getComputedStyle(h).lineHeight));
        add(n, 'ruta: nombre de la línea de trabajo #' + (i + 1) + ' (máx. 2 líneas)', 2 - lineas, 0, 'el nombre ocupa ' + lineas + ' líneas: acortar frentes[].nombre', 'líneas de margen');
      });
      overflowEls(n, s, '.rg-phase', 'cabecera de fase'); overflowEls(n, s, '.rg-follow', 'garantía');
      s.querySelectorAll('.rg-phase').forEach((ph, i) => {
        const pr = ph.getBoundingClientRect().right - 10; let peor = 0, quien = '';
        ph.querySelectorAll('.rg-phase-tag, .rg-phase-n').forEach((el) => { const ex = el.getBoundingClientRect().right - pr; if (ex > peor) { peor = ex; quien = el.textContent.trim().slice(0, 30); } });
        const tg = ph.querySelector('.rg-phase-tag'); const partida = tg && tg.getBoundingClientRect().height > 24;
        add(n, 'ruta: rótulo y conteo de la fase #' + (i + 1) + ' en una línea dentro de su cabecera', partida ? -1 : -peor, 0, (peor || partida) ? 'sobresale o se parte: «' + quien + '». Acortar fases[].titulo (≤ 6 caracteres con 3 fases y una sola línea de trabajo)' : '');
      });
      const grid = s.querySelector('.route-grid'); const miles = s.querySelector('.route-miles');
      if (grid && miles) add(n, 'ruta: grilla vs línea de hitos', top(s, miles) - bot(s, grid), 8);
      if (miles && nota) add(n, 'ruta: hitos vs nota', top(s, nota) - bot(s, miles), 3);
    }
    if (s.classList.contains('s-method')) {
      const logi = s.querySelector('.mt-logi');
      if (logi) add(n, 'método: logística vs pie', footTop - bot(s, logi), 8, 'Acortar los textos de cada bloque (prácticas, datos, casos ya logrados) o los 4 datos de logística');
      const bloques = ['.mt-steps', '.mt-strips', '.mt-proof', '.mt-info', '.mt-logi'].map((q) => s.querySelector(q)).filter(Boolean);
      for (let k = 1; k < bloques.length; k++) add(n, 'método: bloque ' + (k + 1) + ' vs bloque ' + k, top(s, bloques[k]) - bot(s, bloques[k - 1]), 4);
      overflowEls(n, s, '.mt-steps li', 'paso'); overflowEls(n, s, '.mt-case', 'caso ya logrado'); overflowEls(n, s, '.mt-card', 'tarjeta de información');
      overflowEls(n, s, '.mt-tile', 'dato de logística'); overflowEls(n, s, '.mt-why', 'franja «por qué»'); overflowEls(n, s, '.mt-who', 'franja «quién construye»');
      const h2m = s.querySelector('h2'); const subm = s.querySelector('.sub');
      if (h2m && subm) add(n, 'método: título vs subtítulo', top(s, subm) - bot(s, h2m), 2);
    }
    if (s.classList.contains('s-price')) {
      const dur = s.querySelector('.block-value'); const prog = s.querySelector('.block-programa');
      if (dur && prog) add(n, 'inversión: Duración vs etiqueta Programa', top(s, prog) - bot(s, dur), 4);
      const lic = s.querySelector('.lic-wrap');
      if (lic) {
        add(n, 'inversión: licenciamiento vs pie', footTop - bot(s, lic), 8);
        const notas = s.querySelector('.notas-box');
        if (notas) add(n, 'inversión: licenciamiento vs caja Notas', top(s, lic) - bot(s, notas), 4);
        overflowEls(n, s, '.lic-card', 'tarjeta de licencia');
      }
      const partes = s.querySelector('.partes-wrap');
      if (partes) {
        add(n, 'inversión: valor por parte vs pie', footTop - bot(s, partes), 8);
        const notas = s.querySelector('.notas-box');
        if (notas) add(n, 'inversión: valor por parte vs caja Notas', top(s, partes) - bot(s, notas), 4);
        overflowEls(n, s, '.parte-card', 'tarjeta de parte');
        // las cajas de monto deben caer donde scripts/agregar-campo-precio.py → precio_fields() pone PrecioParte1..N (tolerancia 1 px)
        const marcos = [...s.querySelectorAll('.parte-frame')]; const k = marcos.length; const gap = 12, w = (480 - gap * (k - 1)) / k;
        const sr = s.getBoundingClientRect();
        marcos.forEach((m, i) => {
          const r = m.getBoundingClientRect(); const left = 56 + i * (w + gap);
          const dif = Math.max(Math.abs(r.left - sr.left - (left + 13)), Math.abs(r.right - sr.left - (left + w - 13)), Math.abs(r.top - sr.top - 603), Math.abs(r.bottom - sr.top - 639));
          add(n, 'inversión: caja de la parte ' + (i + 1) + ' coincide con su campo del PDF', 1 - dif, 0, 'desfase de ' + dif.toFixed(1) + ' px: sincronizar habilidades-compacto.css (.parte-frame) con agregar-campo-precio.py → precio_fields()');
        });
      }
      const terms = s.querySelector('.cot-terms-box'); const gar = s.querySelector('.cot-garantia-badge');
      if (terms && gar) add(n, 'inversión: términos vs garantía', top(s, gar) - bot(s, terms), 6);
      if (gar) add(n, 'inversión: garantía vs pie', footTop - bot(s, gar), 8);
    }
    if (s.classList.contains('s-deliv')) {
      const band = s.querySelector('.deliv-band');
      const bandTop = top(s, band);
      s.querySelectorAll('.deliv-col').forEach((c, k) => {
        const das = c.querySelectorAll('.da'); const last = das[das.length - 1];
        const desglose = [...das].map(da => da.querySelector('.da-name').textContent.trim().replace(/\\s+\\d+$/, '').slice(0, 22) + ' ' + Math.round(da.getBoundingClientRect().height) + ' px').join(' · ');
        const hol = bandTop - bot(s, last) - 4;
        add(n, 'entregables: columna ' + (k + 1) + ' vs franja inferior', hol, 10,
          'áreas: ' + desglose + (hol < 10 ? '. Sobran ' + Math.round(10 - hol) + ' px: acortar nombres a 1 línea (≤ 36 car.), entregables.compacto, o título/subtítulo más cortos' : ''));
      });
      const sub = s.querySelector('.deliv-sub'); const h2 = s.querySelector('.deliv-head h2');
      if (sub) add(n, 'entregables: ancho del subtítulo (mín. 260 px)', sub.getBoundingClientRect().width - 260, 0, 'el subtítulo mide ' + Math.round(sub.getBoundingClientRect().width) + ' px: título demasiado largo, definir entregables.titulo o nombre_pie corto');
      if (h2) add(n, 'entregables: líneas del título (máx. 3)', 3 - Math.round(h2.getBoundingClientRect().height / 38), 0, 'el título ocupa ' + Math.round(h2.getBoundingClientRect().height / 38) + ' línea(s): definir entregables.titulo más corto', 'líneas de margen');
      // el marcador «Lo que se llevan» debe quedar en UNA línea (agregar-campo-precio.py lo busca como texto contiguo)
      const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
      let nodo; let marcador = null;
      while ((nodo = w.nextNode())) { const i = nodo.textContent.toLowerCase().indexOf('lo que se llevan'); if (i >= 0) { marcador = [nodo, i]; break; } }
      if (marcador) { const r = document.createRange(); r.setStart(marcador[0], marcador[1]); r.setEnd(marcador[0], marcador[1] + 16); add(n, 'entregables: marcador «Lo que se llevan» en una sola línea', 1 - (r.getClientRects().length - 1), 1, 'el marcador se parte en ' + r.getClientRects().length + ' líneas: el PDF quedaría sin los campos Entregables/Acreditacion', 'líneas'); }
      add(n, 'entregables: franja vs pie', footTop - bot(s, band), 8);
      const head = s.querySelector('.deliv-carriles');
      const cols = s.querySelector('.deliv-cols');
      if (head && cols) add(n, 'entregables: barras de carril vs columnas', top(s, cols) - bot(s, head), 2);
    }
    if (s.classList.contains('s-pay')) {
      const nota = s.querySelector('.pay-note');
      if (nota) add(n, 'pago: nota vs pie', footTop - bot(s, nota), 8);
      const pasos = [...s.querySelectorAll('.pay-step')], marcos = [...s.querySelectorAll('.pay-frame')];
      add(n, 'pago: una caja de monto por cuota', Math.min(pasos.length, marcos.length) - Math.max(pasos.length, marcos.length), 0, pasos.length + ' cuotas y ' + marcos.length + ' cajas de monto', '');
      pasos.forEach((p, i) => {
        const hito = p.querySelector('.ps-hito'), pct = p.querySelector('.ps-pct'), cuando = p.querySelector('.ps-when');
        if (hito && pct) add(n, 'pago: hito de la cuota ' + (i + 1) + ' vs porcentaje', top(s, pct) - bot(s, hito), 4, 'acortar el hito (≤ 70 caracteres) o usar menos cuotas');
        if (cuando) { const ex = cuando.scrollWidth - cuando.clientWidth; if (ex > 1) out.push({ slide: n, check: 'pago: «cuándo» de la cuota ' + (i + 1) + ' no cabe en una línea', holgura: -ex, minimo: 0, ok: false, detalle: 'acortar pago.cuotas[].cuando (≤ 12 caracteres)' }); }
        const m = marcos[i];
        if (m) {
          const pr = p.getBoundingClientRect(), mr = m.getBoundingClientRect();
          add(n, 'pago: caja de monto de la cuota ' + (i + 1) + ' dentro de su tarjeta', Math.min(mr.left - pr.left, pr.right - mr.right, mr.top - pr.top, pr.bottom - mr.bottom), 6, 'las cajas deben coincidir con scripts/agregar-campo-precio.py → plan_pago_fields()');
        }
      });
      overflowEls(n, s, '.pay-step', 'tarjeta de cuota'); overflowEls(n, s, '.pay-note', 'nota del plan de pago');
    }
    if (s.classList.contains('s-next')) {
      const ct = s.querySelector('.nx-contact');
      if (ct) add(n, 'próximos pasos: contacto vs pie', footTop - bot(s, ct), 8);
      const st = s.querySelector('.nx-steps');
      if (st && ct) add(n, 'próximos pasos: pasos vs contacto', top(s, ct) - bot(s, st), 8);
      overflowEls(n, s, '.nx-step', 'paso'); overflowEls(n, s, '.nx-card', 'tarjeta de contacto');
    }
    if (s.classList.contains('s-roi')) {
      const rbody = s.querySelector('.roi-body'), dest = s.querySelector('.roi-dest-wrap'), hook = s.querySelector('.roi-hook');
      const bajo = dest || rbody;
      if (dest && rbody) add(n, 'retorno: bloque principal vs franja de destino', top(s, dest) - bot(s, rbody), 8);
      if (hook && bajo) add(n, 'retorno: ' + (dest ? 'franja de destino' : 'bloque principal') + ' vs banda final', top(s, hook) - bot(s, bajo), 8,
        'Acortar pasos, metas, destino o el gancho' + (dest ? '' : ', o reducir filas de la tabla'));
      if (hook && foot) add(n, 'retorno: banda final vs pie', top(s, foot) - bot(s, hook), 4);
      overflowEls(n, s, '.roi-card', 'tarjeta de meta');
      overflowEls(n, s, '.rd-item', 'tarjeta de destino');
      overflowEls(n, s, '.roi-panel', 'panel de cálculo');
      const h2r = s.querySelector('h2'); const subr = s.querySelector('.sub');
      if (h2r && subr) add(n, 'retorno: título vs subtítulo', top(s, subr) - bot(s, h2r), 2);
    }
    // Ningún texto puede salirse por la derecha de la slide (verificar-overflow.js ignora este caso)
    const sr = s.getBoundingClientRect();
    let peor = 0, quien = '';
    s.querySelectorAll('h1,h2,p,li,span,b,strong,em,i').forEach((el) => {
      if (el.children.length || !el.textContent.trim()) return;
      const r = el.getBoundingClientRect();
      if (r.width === 0) return;
      const exceso = r.right - (sr.right - 16);
      if (exceso > peor) { peor = exceso; quien = el.textContent.trim().slice(0, 40); }
    });
    add(n, 'texto dentro del margen derecho', -peor, 0, peor ? 'sobresale ' + Math.round(peor) + ' px: «' + quien + '»' : '');
  });
  return JSON.stringify({ slides: slides.length, checks: out });
})()`;

async function main() {
  const html = resolveHtml(process.argv[2]);
  if (!fs.existsSync(html)) { console.error('ERROR: no existe ' + html); process.exit(2); }
  if (!fs.existsSync(CHROME)) { console.error('ERROR: Chrome no encontrado en ' + CHROME); process.exit(2); }
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'hab-compacto-'));
  const proc = spawn(CHROME, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    '--window-size=1300,1000', '--remote-debugging-port=0', '--user-data-dir=' + dir, 'about:blank'], { stdio: 'ignore' });
  let port = null;
  for (let i = 0; i < 300; i++) {
    const f = path.join(dir, 'DevToolsActivePort');
    if (fs.existsSync(f)) { const l = fs.readFileSync(f, 'utf8').split('\n')[0].trim(); if (l) { port = +l; break; } }
    await sleep(50);
  }
  if (!port) { proc.kill('SIGKILL'); console.error('ERROR: Chrome no expuso el puerto de depuración.'); process.exit(2); }
  try {
    const list = await (await fetch('http://127.0.0.1:' + port + '/json')).json();
    const page = list.find((t) => t.type === 'page');
    const ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise((r) => ws.addEventListener('open', r));
    let id = 0; const pend = new Map();
    ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } });
    const send = (method, params = {}) => new Promise((r) => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
    await send('Page.enable');
    await send('Emulation.setEmulatedMedia', { media: 'print' });
    await send('Page.navigate', { url: 'file://' + html });
    await sleep(2500);
    const r = await send('Runtime.evaluate', { expression: MEDIR, awaitPromise: true, returnByValue: true });
    if (!r.result || !r.result.result || typeof r.result.result.value !== 'string') {
      console.error('ERROR al medir:', JSON.stringify(r.result || r.error)); process.exit(2);
    }
    const res = JSON.parse(r.result.result.value);
    if (!res.slides) { console.error('ERROR: el HTML no tiene ninguna <section class="slide">: ¿archivo equivocado o vacío? ' + html); process.exit(2); }
    console.log('== Holguras del deck compacto de Habilidades: ' + path.relative(ROOT, html) + ' (' + res.slides + ' slides) ==');
    let bad = 0;
    res.checks.forEach((c) => {
      if (!c.ok) bad++;
      console.log((c.ok ? '✓ ' : '✗ ') + 'slide ' + c.slide + ' · ' + c.check + ': ' + c.holgura + ' ' + c.unidad + (c.unidad === 'px' ? ' (mín. ' + c.minimo + ')' : ''));
      if (!c.ok && c.detalle) console.log('    → ' + c.detalle);
    });
    console.log(bad ? '\n❌ ' + bad + ' bloque(s) sin holgura suficiente: acortar contenido (no el diseño).' : '\n✅ Todas las holguras OK.');
    process.exitCode = bad ? 1 : 0;
  } finally {
    proc.kill('SIGKILL');
  }
}
main().then(() => process.exit(process.exitCode || 0)).catch((e) => { console.error(e); process.exit(2); });
