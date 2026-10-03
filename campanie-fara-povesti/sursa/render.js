// Randează fiecare HTML din manifest.json în png/ cu Chromium-ul preinstalat.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const only = process.argv.slice(2);
  const list = JSON.parse(fs.readFileSync('manifest.json', 'utf8')).filter(([n]) => !only.length || only.some(o => n.startsWith(o)));
  fs.mkdirSync('png', { recursive: true });
  const browser = await chromium.launch();
  for (const [name, w, h, clear] of list) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.resolve('html', name + '.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForFunction(() => !document.querySelector('.fitbox') || document.body.dataset.fit === '1'); await page.waitForTimeout(150);
    // Semnalează textul care iese din cadru
    const over = await page.evaluate(() => [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && (r.right > innerWidth + 1 || r.bottom > innerHeight + 1); }).map(e => e.tagName + ':' + (e.textContent || '').trim().slice(0, 30)).slice(0, 3));
    const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + f.weight).join(','));
    await page.screenshot({ path: `png/${name}.png`, omitBackground: clear });
    console.log(name, w + 'x' + h, over.length ? 'OVERFLOW ' + over.join(' | ') : 'ok', fonts.includes('Montserrat') ? '' : 'NO-MONTSERRAT');
    await page.close();
  }
  await browser.close();
})();
