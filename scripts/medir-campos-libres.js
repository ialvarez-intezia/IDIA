#!/usr/bin/env node
// medir-campos-libres.js <ruta/index.html>
//
// Mide con Chrome headless (media print, 1123x794, el mismo tamaño de la impresión) la caja de cada «.campo-libre» del deck compacto
// y la escribe en JSON por la salida estándar: {slide (0 = primera página), name, tip, calc, x, y, w, h} con x, y, w, h en px de la slide.
// Lo usa scripts/agregar-campos-libres.py para crear los campos editables del PDF sin coordenadas escritas a mano.
'use strict';
const fs = require('fs'), os = require('os'), path = require('path');
const { spawn } = require('child_process');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const MEDIR = `(async () => {
  if (document.fonts && document.fonts.ready) { try { await document.fonts.ready; } catch (e) {} }
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const slides = [...document.querySelectorAll('.slide')];
  const out = [];
  slides.forEach((s, i) => {
    const sr = s.getBoundingClientRect();
    s.querySelectorAll('.campo-libre').forEach((el) => {
      const r = el.getBoundingClientRect();
      out.push({ slide: i, name: el.dataset.campo, tip: el.dataset.tip || '', calc: el.dataset.calc || '',
        x: r.left - sr.left, y: r.top - sr.top, w: r.width, h: r.height, sw: sr.width, sh: sr.height });
    });
  });
  return JSON.stringify(out);
})()`;
async function main() {
  const arg = process.argv[2];
  if (!arg) { console.error('Uso: node scripts/medir-campos-libres.js <ruta/index.html>'); process.exit(2); }
  const html = path.resolve(arg);
  if (!fs.existsSync(html)) { console.error('ERROR: no existe ' + html); process.exit(2); }
  if (!fs.existsSync(CHROME)) { console.error('ERROR: Chrome no encontrado en ' + CHROME); process.exit(2); }
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'campos-libres-'));
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
    if (!r.result || !r.result.result || typeof r.result.result.value !== 'string') { console.error('ERROR al medir:', JSON.stringify(r.result || r.error)); process.exit(2); }
    process.stdout.write(r.result.result.value);
  } finally {
    proc.kill('SIGKILL');
  }
}
main().then(() => process.exit(0)).catch((e) => { console.error(e); process.exit(2); });
