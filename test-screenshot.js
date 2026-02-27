const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 375, height: 812 });
  await page.goto('file://' + __dirname + '/index.html', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: '/tmp/local-screenshot.png', fullPage: true });
  await browser.close();
  console.log('Screenshot saved to /tmp/local-screenshot.png');
})();
