// Print an HTML file to an A4 PDF with the bundled Chromium.
// Usage: NODE_PATH=$(npm root -g) node tools/html2pdf.cjs input.html output.pdf
const { chromium } = require('playwright');
const path = require('node:path');

(async () => {

const [input, output] = process.argv.slice(2);
const browser = await chromium.launch();
const page = await browser.newPage();
await page.emulateMedia({ media: 'print', colorScheme: 'light' });
await page.goto('file://' + path.resolve(input));
await page.addStyleTag({ content: `
  nav.toc { display:none !important; }
  body { font-size:11.5px; background:#fff; }
  main { max-width:none; padding:0; }
  h1 { font-size:20px; } h2 { font-size:15px; margin:16px 0 6px; padding-top:6px; }
  h3 { font-size:13px; margin:12px 0 4px; }
  table { font-size:10.5px; } th, td { padding:4px 6px; }
  blockquote { padding:6px 10px; margin:6px 0; }
  h2, h3 { break-after:avoid; } tr, blockquote { break-inside:avoid; }
  mark.fill { background:#fef08a; }
` });
await page.pdf({ path: output, format: 'A4', printBackground: true,
  margin: { top: '14mm', bottom: '14mm', left: '14mm', right: '14mm' } });
await browser.close();
console.log(`${input} -> ${output}`);
})();
