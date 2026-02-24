import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Phosphor Icons
if 'phosphor-icons' not in content:
    content = content.replace('</head>', '  <script src="https://unpkg.com/@phosphor-icons/web"></script>\n</head>')

# Replace Sidebar Icons
content = content.replace('📊</span>', '<i class="ph ph-squares-four"></i></span>')
content = content.replace('📈</span>', '<i class="ph ph-chart-line-up"></i></span>')
content = content.replace('📅</span>', '<i class="ph ph-calendar-blank"></i></span>')
content = content.replace('👥</span>', '<i class="ph ph-users"></i></span>')
content = content.replace('📥</span>', '<i class="ph ph-export"></i></span>')
content = content.replace('⚙️</span>', '<i class="ph ph-gear"></i></span>')

# Replace Status Summary Icons
content = content.replace('<div class="status-icon">👥</div>', '<div class="status-icon"><i class="ph-fill ph-users-three" style="color: var(--sprix-blue);"></i></div>')
content = content.replace('<div class="status-icon">🏢</div>', '<div class="status-icon"><i class="ph-fill ph-buildings" style="color: var(--sprix-blue);"></i></div>')
content = content.replace('<div class="status-icon">🏠</div>', '<div class="status-icon"><i class="ph-fill ph-house-line" style="color: var(--sprix-blue);"></i></div>')
content = content.replace('<div class="status-icon">🌙</div>', '<div class="status-icon"><i class="ph-fill ph-moon" style="color: var(--sprix-blue);"></i></div>')
content = content.replace('<div class="status-icon">🏁</div>', '<div class="status-icon"><i class="ph-fill ph-flag-checkered" style="color: var(--sprix-blue);"></i></div>')

# Update Logo
logo_html = '''<div class="logo-container" style="display: flex; align-items: center; gap: 12px; margin-bottom: 24px; padding-left: 20px;">
          <img src="sprix-logo.png" alt="SPRIX" style="height: 32px; object-fit: contain;">
          <span style="font-weight: 300; font-size: 24px; color: var(--sprix-navy); letter-spacing: 1px;">EdTech</span>
        </div>'''
old_logo_regex = r'<h1 class="logo-text">.*?</h1>'
content = re.sub(old_logo_regex, logo_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
