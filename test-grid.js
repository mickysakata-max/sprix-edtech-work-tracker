const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 375, height: 812 });
  await page.goto('file://' + __dirname + '/index.html', { waitUntil: 'networkidle0' });
  
  const stats = await page.evaluate(() => {
    const grid = document.querySelector('.dashboard-stats');
    if (!grid) return 'No grid';
    const rect = grid.getBoundingClientRect();
    const style = window.getComputedStyle(grid);
    const children = Array.from(grid.querySelectorAll('.status-card')).map(c => c.getBoundingClientRect().width);
    return {
      gridWidth: rect.width,
      display: style.display,
      gridTemplateColumns: style.gridTemplateColumns,
      childWidths: children
    };
  });
  console.log(JSON.stringify(stats, null, 2));
  await browser.close();
})();
