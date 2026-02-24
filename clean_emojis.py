import re

# Clean i18n.js
with open('i18n.js', 'r', encoding='utf-8') as f:
    i18n = f.read()

emojis_to_remove = ['🌙', '🏢', '🏠', '🏁', '📊', '📋', '📥', '📤', '👥']
for emoji in emojis_to_remove:
    i18n = i18n.replace(f'{emoji} ', '')
    i18n = i18n.replace(emoji, '')

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n)

# Clean index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace specific locations where icons were left behind in HTML
html = html.replace('<div class="empty-icon">👥</div>', '<div class="empty-icon"><i class="ph ph-users" style="color: var(--sprix-blossom);"></i></div>')
html = html.replace('<h3 data-i18n="export.csvTitle">📊 CSV Export</h3>', '<h3><i class="ph-fill ph-file-csv" style="color: #4CAF50;"></i> <span data-i18n="export.csvTitle">CSV Export</span></h3>')
html = html.replace('<h3 data-i18n="export.jsonTitle">📋 JSON Backup</h3>', '<h3><i class="ph-fill ph-file-code" style="color: var(--sprix-navy);"></i> <span data-i18n="export.jsonTitle">JSON Backup</span></h3>')
html = html.replace('<span style="font-size: 1.2em;">🏢</span> ', '<i class="ph-fill ph-buildings" style="color: var(--sprix-blue);"></i> ')
html = html.replace('<span style="font-size: 1.2em;">🎨</span> ', '<i class="ph-fill ph-palette" style="color: var(--sprix-red);"></i> ')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

