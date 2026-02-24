import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace fonts
old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700&display=swap" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&family=Cairo:wght@400;500;600;700&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">'
html = html.replace(old_fonts, new_fonts)

# Replace auth logo
old_auth_logo = '<div class="auth-logo" data-i18n="auth.logo">🌙 Ramadan Tracker</div>'
new_auth_logo = '''<div class="auth-logo">
        <div style="background: white; padding: 12px 24px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
          <img src="sprix-logo.png" alt="SPRIX" style="height: 36px; object-fit: contain;">
        </div>
      </div>'''
html = html.replace(old_auth_logo, new_auth_logo)

# Re-arrange layout
# Remove main-layout wrapper
html = html.replace('<!-- Desktop Multi-Column Layout -->\n      <div class="main-layout">', '<!-- Desktop Multi-Column Layout Removed -->')

# Extract dashboard-stats
stats_match = re.search(r'(<div class="dashboard-stats" id="dashboardStats">.*?(?:</div>\s*){7})', html, re.DOTALL)
if stats_match:
    stats_html = stats_match.group(1)
    # Remove from sidebar
    html = html.replace(stats_html, '')
    
    # Remove right-sidebar completely
    html = re.sub(r'<!-- Right Sidebar \(Stats\) -->\s*<div class="right-sidebar">\s*</div>\s*</aside>', '', html)
    html = re.sub(r'<!-- Right Sidebar \(Stats\) -->\s*<aside class="right-sidebar">\s*</aside>', '', html)

    # Inject above page-content's view Dashboard
    insertion_point = '<div class="view active" id="viewDashboard">'
    html = html.replace(insertion_point, f'{stats_html}\n          {insertion_point}')

# Clean up leftover div
html = html.replace('      </div> <!-- /main-layout -->', '')

# Update css version
html = html.replace('style.css?v=5', 'style.css?v=6')
html = html.replace('app.js?v=5', 'app.js?v=6')
html = html.replace('i18n.js?v=5', 'i18n.js?v=6')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add Tajawal
css = css.replace("font-family: 'Poppins', sans-serif;", "font-family: 'Poppins', sans-serif;\n  --font-arabic: 'Tajawal', 'Almarai', sans-serif;")

# Remove main layout css
css = re.sub(r'\.main-layout\s*\{.*?\n\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.right-sidebar\s*\{.*?\n\}', '', css, flags=re.DOTALL)

# Dashboard Stats update
old_stats = '''.dashboard-stats {
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: sticky;
  top: 24px;
}'''

new_stats = '''.dashboard-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}'''
css = css.replace(old_stats, new_stats)

old_stat_card = '''.status-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: all var(--transition-base);
  border: 2px solid transparent;
}'''

new_stat_card = '''.status-card {
  background: var(--white);
  border-radius: var(--radius-lg);
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: all var(--transition-base);
  border: 2px solid transparent;
  flex: 1;
}'''
css = css.replace(old_stat_card, new_stat_card)


# RTL Overrides
rtl_old = '''[dir="rtl"] {
  font-family: 'Cairo', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 105%;
  line-height: 1.6;
  zoom: 1.15;
}'''

rtl_new = '''[dir="rtl"] {
  font-family: var(--font-arabic);
  font-size: 110%;
  line-height: 1.8;
  zoom: 1.15;
}

[dir="rtl"] .emp-name {
  font-size: 22px !important;
  font-weight: 700;
  margin-bottom: 8px;
}

[dir="rtl"] body {
  letter-spacing: 0.5px;
}'''

css = css.replace(rtl_old, rtl_new)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

