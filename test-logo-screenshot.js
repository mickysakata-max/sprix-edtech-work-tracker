const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('file://' + __dirname + '/index.html', { waitUntil: 'networkidle0' });
  
  // Wait a moment for any potential font loading (though we don't rely on fonts for the logo now)
  await new Promise(r => setTimeout(r, 500));
  
  const element = await page.$('.auth-logo-group');
  if (element) {
    await element.screenshot({ path: '/tmp/logo-geometry.png' });
    console.log('Logo screenshot saved to /tmp/logo-geometry.png');
  } else {
    console.log('Could not find .auth-logo-group element');
  }
  
  await browser.close();
})();
