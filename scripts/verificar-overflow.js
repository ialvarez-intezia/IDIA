#!/usr/bin/env node
// verificar-overflow.js <slug | ruta-a-index.html>
//
// Red de seguridad anti-desborde (CLAUDE.md §4.10). Renderiza el deck en Chrome
// headless y reporta, por slide, todo contenido que:
//   - excede los límites de su .slide (se sale de la página A4), o
//   - es recortado por una caja con overflow hidden/clip (ej. una card que muestra
//     solo 2 de 5 temas), o
//   - se trunca con "…" (text-overflow: ellipsis) — chequeo dedicado, tolerancia
//     casi nula: cualquier "…" es un defecto §4.10, por pocos px que recorte.
//
// No instala dependencias: usa Chrome headless (igual que generar-pdf.sh) y el
// WebSocket nativo de Node (v22+) para hablar CDP.
//
// Uso:    node scripts/verificar-overflow.js <slug>
//         node scripts/verificar-overflow.js clientes/propuestas/<slug>/index.html
// Salida: 0 = sin desbordes | 1 = hay desbordes que corregir

'use strict';

const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawn } = require('child_process');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const ROOT = path.resolve(__dirname, '..');
// Tolerancias (px), calibradas contra el deck canónico cumbre-andina:
//   PAGE = a nivel de slide, vertical: estricto (una slide nunca debe ser más alta
//          que la página). El desborde horizontal de slide se ignora: casi siempre es
//          un elemento decorativo (cuadro rotado, banda de color) que la slide recorta
//          a propósito con overflow:hidden.
//   CLIP = cajas internas con overflow hidden: por debajo de un renglón (~18px) es
//          holgura de impresión, no una línea perdida. Un caso real de §4.10 (card que
//          muestra 2 de 5 temas) desborda decenas o cientos de px y sí se reporta.
const TOL_PAGE = 2;
const TOL_CLIP = 12;

function resolveHtml(arg) {
  if (!arg) {
    console.error('Uso: node scripts/verificar-overflow.js <slug | ruta/index.html>');
    process.exit(2);
  }
  if (arg.endsWith('.html')) return path.resolve(arg);
  return path.join(ROOT, 'clientes', 'propuestas', arg, 'index.html');
}

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

// ── Lanza Chrome headless con puerto de depuración efímero ─────────────────────
async function launchChrome() {
  if (!fs.existsSync(CHROME)) {
    console.error(`ERROR: Chrome no encontrado en ${CHROME}`);
    process.exit(2);
  }
  const userDataDir = fs.mkdtempSync(path.join(os.tmpdir(), 'overflow-chrome-'));
  const proc = spawn(CHROME, [
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    '--remote-debugging-port=0',
    `--user-data-dir=${userDataDir}`,
    'about:blank',
  ], { stdio: ['ignore', 'ignore', 'ignore'] });

  // Chrome escribe el puerto elegido en <userDataDir>/DevToolsActivePort
  const portFile = path.join(userDataDir, 'DevToolsActivePort');
  let port = null;
  for (let i = 0; i < 300; i++) {
    if (fs.existsSync(portFile)) {
      const line = fs.readFileSync(portFile, 'utf8').split('\n')[0].trim();
      if (line) { port = parseInt(line, 10); break; }
    }
    await sleep(50);
  }
  if (!port) {
    proc.kill('SIGKILL');
    console.error('ERROR: Chrome no expuso el puerto de depuración a tiempo.');
    process.exit(2);
  }
  return { proc, port, userDataDir };
}

// ── Cliente CDP mínimo sobre el WebSocket nativo de Node ───────────────────────
class CDP {
  constructor(ws) {
    this.ws = ws;
    this.id = 0;
    this.pending = new Map();
    this.listeners = new Map();
    ws.addEventListener('message', (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id != null && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        if (msg.error) reject(new Error(JSON.stringify(msg.error)));
        else resolve(msg.result);
      } else if (msg.method) {
        const cbs = this.listeners.get(msg.method) || [];
        cbs.forEach((cb) => cb(msg.params, msg.sessionId));
      }
    });
  }
  send(method, params = {}, sessionId) {
    const id = ++this.id;
    const payload = { id, method, params };
    if (sessionId) payload.sessionId = sessionId;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify(payload));
    });
  }
  on(method, cb) {
    if (!this.listeners.has(method)) this.listeners.set(method, []);
    this.listeners.get(method).push(cb);
  }
  once(method, predicate) {
    return new Promise((resolve) => {
      const cb = (params, sessionId) => {
        if (!predicate || predicate(params, sessionId)) {
          const arr = this.listeners.get(method);
          arr.splice(arr.indexOf(cb), 1);
          resolve(params);
        }
      };
      this.on(method, cb);
    });
  }
}

function connect(wsUrl) {
  return new Promise((resolve, reject) => {
    const ws = new WebSocket(wsUrl);
    ws.addEventListener('open', () => resolve(ws));
    ws.addEventListener('error', (e) => reject(new Error('WS error: ' + (e.message || e.type))));
  });
}

// ── JS que se evalúa dentro de la página para detectar desborde ────────────────
// (función serializada como string para Runtime.evaluate)
const DETECT_FN = `(async () => {
  if (document.fonts && document.fonts.ready) { try { await document.fonts.ready; } catch (e) {} }
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const TOL_PAGE = ${TOL_PAGE};
  const TOL_CLIP = ${TOL_CLIP};
  const issues = [];
  const sel = (el) => {
    let s = el.tagName.toLowerCase();
    if (el.classList && el.classList.length) s += '.' + [...el.classList].join('.');
    return s;
  };
  const slides = [...document.querySelectorAll('.slide')];
  slides.forEach((slide, i) => {
    const n = i + 1;
    const counter = slide.querySelector('.counter');
    const label = counter ? counter.textContent.trim() : '';
    // Desborde vertical a nivel de slide: contenido más alto que la página A4.
    // (El desborde horizontal de slide se ignora: decoración recortada a propósito.)
    const dvS = slide.scrollHeight - slide.clientHeight;
    if (dvS > TOL_PAGE) {
      issues.push({ slide: n, label, box: '.slide', kind: 'pagina', dv: Math.round(dvS), dh: 0 });
    }
    // Cajas internas que recortan contenido (overflow hidden/clip)
    slide.querySelectorAll('*').forEach((el) => {
      const cs = getComputedStyle(el);
      // ── Truncado con «…» (text-overflow: ellipsis) — §4.10, tolerancia ~0 ──
      // Cualquier elemento que dispare el «…» pierde texto de cara al cliente,
      // por pocos px que recorte. Defecto bloqueante propio, distinto del recorte
      // genérico (que tolera 12px de holgura de impresión). Cubre el caso de una
      // línea (nowrap → desborde a lo ancho) y multilínea (-webkit-line-clamp →
      // desborde a lo alto).
      if (cs.textOverflow && cs.textOverflow.includes('ellipsis')) {
        const exW = el.scrollWidth - el.clientWidth;
        const exH = el.scrollHeight - el.clientHeight;
        if (exW > 1 || exH > 1) {
          issues.push({ slide: n, label, box: sel(el), kind: 'ellipsis',
            dv: Math.round(Math.max(0, exH)), dh: Math.round(Math.max(0, exW)) });
        }
        return; // ya evaluado; no duplicar con el chequeo genérico de recorte
      }
      const ovY = cs.overflowY, ovX = cs.overflowX, ov = cs.overflow;
      const clipsY = ovY === 'hidden' || ovY === 'clip' || ov === 'hidden' || ov === 'clip';
      const clipsX = ovX === 'hidden' || ovX === 'clip' || ov === 'hidden' || ov === 'clip';
      let dv = 0, dh = 0;
      if (clipsY && el.scrollHeight - el.clientHeight > TOL_CLIP) dv = el.scrollHeight - el.clientHeight;
      if (clipsX && el.scrollWidth - el.clientWidth > TOL_CLIP) dh = el.scrollWidth - el.clientWidth;
      if (dv || dh) {
        issues.push({ slide: n, label, box: sel(el), kind: 'recorte', dv: Math.round(dv), dh: Math.round(dh) });
      }
    });
  });
  return JSON.stringify({ slideCount: slides.length, issues });
})()`;

async function main() {
  const html = resolveHtml(process.argv[2]);
  if (!fs.existsSync(html)) {
    console.error(`ERROR: No existe ${html}`);
    process.exit(2);
  }
  const fileUrl = 'file://' + html;

  const { proc, port, userDataDir } = await launchChrome();
  let ws;
  try {
    const version = await fetch(`http://127.0.0.1:${port}/json/version`).then((r) => r.json());
    ws = await connect(version.webSocketDebuggerUrl);
    const cdp = new CDP(ws);

    const { targetId } = await cdp.send('Target.createTarget', { url: fileUrl });
    const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });

    await cdp.send('Page.enable', {}, sessionId);
    await cdp.send('Runtime.enable', {}, sessionId);
    // El .slide es width:1123px con max-width:96vw. Si el viewport es angosto, la
    // slide se encoge mientras su contenido sigue dimensionado para 1123px → falso
    // desborde. Forzamos un viewport ancho para que 96vw ≥ 1123px (el tamaño real).
    await cdp.send('Emulation.setDeviceMetricsOverride', {
      width: 1200, height: 1000, deviceScaleFactor: 1, mobile: false,
    }, sessionId);
    // Espera el load del target adjuntado
    await Promise.race([
      cdp.once('Page.loadEventFired', (_p, sid) => sid === sessionId),
      sleep(8000),
    ]);
    await sleep(400); // margen para layout final

    const res = await cdp.send('Runtime.evaluate', {
      expression: DETECT_FN,
      returnByValue: true,
      awaitPromise: true,
    }, sessionId);

    await cdp.send('Target.closeTarget', { targetId }).catch(() => {});

    if (res.exceptionDetails) {
      console.error('ERROR al evaluar en la página:', JSON.stringify(res.exceptionDetails));
      process.exitCode = 2;
      return;
    }
    const { slideCount, issues } = JSON.parse(res.result.value);
    report(path.basename(path.dirname(html)), slideCount, issues);
    process.exitCode = issues.length ? 1 : 0;
  } finally {
    try { if (ws) ws.close(); } catch (e) {}
    proc.kill('SIGKILL');
    await sleep(150); // deja que Chrome suelte el user-data-dir
    fs.rmSync(userDataDir, { recursive: true, force: true, maxRetries: 5, retryDelay: 100 });
  }
}

function report(slug, slideCount, issues) {
  console.log(`== Verificación de desborde: ${slug} (${slideCount} slides) ==\n`);
  if (!issues.length) {
    console.log('✓  Sin desbordes. Ninguna slide se sale ni recorta contenido.');
    return;
  }
  console.log(`❌ ${issues.length} desborde(s) detectado(s):\n`);
  for (const it of issues) {
    const where = it.label ? `slide ${it.slide} (${it.label})` : `slide ${it.slide}`;
    const dims = [it.dv ? `alto +${it.dv}px` : '', it.dh ? `ancho +${it.dh}px` : ''].filter(Boolean).join(', ');
    const kind = it.kind === 'pagina' ? 'se sale de la página'
      : it.kind === 'ellipsis' ? 'TEXTO TRUNCADO con «…» (acortar el contenido)'
      : 'caja recorta contenido';
    console.log(`  • ${where} · ${it.box} · ${kind} · ${dims}`);
  }
  console.log('\nCorrige según §4.10 (acortar copy, modo compacto, reducir ítems) y vuelve a correr.');
}

main().catch((e) => {
  console.error('ERROR:', e.message);
  process.exit(2);
});
