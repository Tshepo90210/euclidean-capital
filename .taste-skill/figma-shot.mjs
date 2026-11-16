/* A bench for reading the client's Figma design: a big Chrome window, trusted
   input (clicks, key chords, the wheel), and screenshots of the canvas.

   node .taste-skill/figma-shot.mjs --out .taste-skill/figma/shot.png --w 1920 --h 1200
     [--url <the file url>] [--script <a JSON array of steps>]

   A step is one of:
     {"click": [x, y]}                 a left click on the canvas
     {"key": "Shift+2"}                 a key chord
     {"wheel": [x, y, dy]}             the wheel at a point (Figma pans)
     {"shot": "name"}                  a screenshot, written beside --out
     {"wait": 1200}                    a pause
     {"url": true}                     print the current url
*/
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { spawn, execFileSync } from 'node:child_process';

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf('--' + k); return i < 0 ? d : (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true); };
const W = +opt('w', 1920), VH = +opt('h', 1200);
const out = path.resolve(String(opt('out', '.taste-skill/figma/shot.png')));
fs.mkdirSync(path.dirname(out), { recursive: true });
const url = String(opt('url', 'https://www.figma.com/design/aSKXW1WqojPf5iP5VYevSA/EUCLIDEAN-CAPITAL-MID-FIDELITY-DESIGN?node-id=0-1'));
const stepsFile = opt('scriptFile');
const steps = stepsFile && stepsFile !== true
  ? JSON.parse(fs.readFileSync(String(stepsFile), 'utf8'))
  : JSON.parse(String(opt('script', '[]')));
const profile = path.join(os.tmpdir(), 'figma-bench-' + process.pid);
const sleep = ms => new Promise(r => setTimeout(r, ms));

function findChrome() {
  const local = process.env.LOCALAPPDATA ? path.join(process.env.LOCALAPPDATA, 'Google/Chrome/Application/chrome.exe') : null;
  const c = [process.env.CHROME_PATH, 'C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', local,
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'];
  const f = c.find(p => p && fs.existsSync(p));
  if (!f) throw new Error('no Chrome found (set CHROME_PATH)');
  return f;
}

const child = spawn(findChrome(), ['--headless=new', `--user-data-dir=${profile}`, '--remote-debugging-port=0', '--no-first-run',
  '--no-default-browser-check', '--disable-extensions', '--hide-scrollbars', '--mute-audio', '--disable-gpu', '--use-angle=swiftshader', '--enable-unsafe-swiftshader',
  '--disable-blink-features=AutomationControlled',
  '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  '--lang=en-US', '--accept-lang=en-US,en;q=0.9',
  `--window-size=${W},${VH}`, 'about:blank'], { stdio: 'ignore', windowsHide: true });
const kill = () => { try { execFileSync('taskkill', ['/PID', String(child.pid), '/T', '/F'], { stdio: 'ignore' }); } catch { } };
process.on('exit', kill);

try {
  let port = null;
  const portFile = path.join(profile, 'DevToolsActivePort');
  for (let i = 0; i < 150 && !port; i++) { await sleep(100); try { port = parseInt(fs.readFileSync(portFile, 'utf8'), 10) || null; } catch { } }
  if (!port) throw new Error('Chrome did not start');
  const ver = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
  const ws = new WebSocket(ver.webSocketDebuggerUrl);
  await new Promise((r, j) => { ws.addEventListener('open', r, { once: true }); ws.addEventListener('error', j, { once: true }); });
  let id = 0; const pend = new Map();
  ws.addEventListener('message', e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } });
  const send = (method, params = {}, sessionId) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
  const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
  const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
  const S = async (m, p) => { const r = await send(m, p, sessionId); if (r.error) throw new Error(`${m}: ${r.error.message}`); return r.result; };
  const ev = async x => (await S('Runtime.evaluate', { expression: x, awaitPromise: true, returnByValue: true })).result.value;

  await S('Page.enable'); await S('Runtime.enable');
  await S('Emulation.setDeviceMetricsOverride', { width: W, height: VH, deviceScaleFactor: 1, mobile: false });
  await S('Page.navigate', { url });
  await sleep(9000);
  await ev('1');

  const shot = async (name) => {
    const { data } = await S('Page.captureScreenshot', { format: 'png' });
    const p = path.join(path.dirname(out), name + '.png');
    fs.writeFileSync(p, Buffer.from(data, 'base64'));
    console.log('shot ' + p);
  };
  const click = async (x, y) => {
    await S('Input.dispatchMouseEvent', { type: 'mouseMoved', x, y, button: 'none' });
    await sleep(120);
    await S('Input.dispatchMouseEvent', { type: 'mousePressed', x, y, button: 'left', buttons: 1, clickCount: 1 });
    await sleep(60);
    await S('Input.dispatchMouseEvent', { type: 'mouseReleased', x, y, button: 'left', buttons: 0, clickCount: 1 });
    await sleep(300);
  };
  const wheel = async (x, y, dy, mods) => {
    await S('Input.dispatchMouseEvent', { type: 'mouseWheel', x, y, deltaX: 0, deltaY: dy, button: 'none', buttons: 0, modifiers: mods || 0 });
    await sleep(350);
  };
  const move = async (x, y) => { await S('Input.dispatchMouseEvent', { type: 'mouseMoved', x, y, button: 'none' }); await sleep(200); };
  const pan = async (x, y, dx, dy) => {
    await S('Input.synthesizeScrollGesture', { x, y, xDistance: dx || 0, yDistance: dy || 0, speed: 800, gestureSourceType: 'mouse' });
    await sleep(700);
  };
  const zoomAt = async (x, y, notches) => {
    await move(x, y);
    for (let i = 0; i < Math.abs(notches); i++) {
      await S('Input.dispatchMouseEvent', { type: 'mouseWheel', x, y, deltaX: 0, deltaY: notches > 0 ? 120 : -120, button: 'none', buttons: 0, modifiers: 2 });
      await sleep(220);
    }
    await sleep(400);
  };
  const zoomNow = async () => {
    const v = await ev(`(() => { const t = [...document.querySelectorAll('button, div, span')].map(e => (e.textContent||'').trim()).filter(x => /^\\d+%$/.test(x)); return t[0] || 'n/a'; })()`);
    console.log('zoom ' + v);
    return v;
  };
  const key = async (chord) => {
    const parts = chord.split('+');
    const k = parts.pop();
    const mods = parts.reduce((a, p) => a | (p === 'Shift' ? 8 : p === 'Control' ? 2 : p === 'Alt' ? 1 : 0), 0);
    const map = { '1': { code: 'Digit1', key: '1' }, '2': { code: 'Digit2', key: '2' }, '0': { code: 'Digit0', key: '0' }, '+': { code: 'Equal', key: '+' }, '-': { code: 'Minus', key: '-' } };
    const info = map[k] || { code: 'Key' + k.toUpperCase(), key: k };
    await S('Input.dispatchKeyEvent', { type: 'rawKeyDown', key: info.key, code: info.code, modifiers: mods, windowsVirtualKeyCode: info.key.charCodeAt(0) });
    await sleep(60);
    await S('Input.dispatchKeyEvent', { type: 'keyUp', key: info.key, code: info.code, modifiers: mods, windowsVirtualKeyCode: info.key.charCodeAt(0) });
    await sleep(500);
  };

  if (!steps.length) { await shot('overview'); console.log('url ' + (await ev('location.href'))); }
  for (const st of steps) {
    if (st.click) await click(st.click[0], st.click[1]);
    if (st.move) await move(st.move[0], st.move[1]);
    if (st.zoomAt) await zoomAt(st.zoomAt[0], st.zoomAt[1], st.zoomAt[2]);
    if (st.zoomNow) await zoomNow();
    if (st.key) await key(st.key);
    if (st.wheel) await wheel(st.wheel[0], st.wheel[1], st.wheel[2], st.wheel[3]);
    if (st.pan) await pan(st.pan[0], st.pan[1], st.pan[2], st.pan[3]);
    if (st.wait) await sleep(st.wait);
    if (st.shot) await shot(st.shot);
    if (st.url) console.log('url ' + (await ev('location.href')));
    if (st.eval) console.log('eval ' + JSON.stringify(await ev(st.eval)).slice(0, 4000));
  }
} catch (e) {
  console.error('figma-shot: ' + e.message);
} finally {
  try { execFileSync('taskkill', ['/PID', String(child.pid), '/T', '/F'], { stdio: 'ignore' }); } catch { }
  try { fs.rmSync(profile, { recursive: true, force: true }); } catch { }
}
