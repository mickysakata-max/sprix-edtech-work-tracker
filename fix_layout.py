import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the auth-logo
old_auth = '''    <div class="auth-card">
      <div class="sidebar-logo" style="margin-bottom: 24px;">
        <span class="logo-text">SPRI<span class="logo-x">X</span> <span class="logo-edtech">EdTech</span></span>
      </div>'''

new_auth = '''    <div class="auth-card">
      <div class="auth-logo" style="display: flex; justify-content: center; margin-bottom: 24px;">
        <div style="background: white; padding: 12px 24px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
          <img src="sprix-logo.png" alt="SPRIX" style="height: 36px; object-fit: contain;">
        </div>
      </div>'''

html = html.replace(old_auth, new_auth)

# 2. Extract and move dashboard-stats
stats_match = re.search(r'(<!-- Right Sidebar \(Stats\) -->\s*<div class="dashboard-stats".*?</div>\s*</aside>)', html, re.DOTALL)
if stats_match:
    stats_chunk = stats_match.group(1)
    
    # Clean the chunk (remove HTML comments and the rogue </aside>)
    clean_stats = stats_chunk.replace('<!-- Right Sidebar (Stats) -->', '')
    clean_stats = clean_stats.replace('</aside>', '')
    
    # Remove it from the bottom
    html = html.replace(stats_chunk, '')

    # Insert it above page-content's view Dashboard
    insertion_point = '<div class="view active" id="viewDashboard">'
    html = html.replace(insertion_point, f'{clean_stats}\n          {insertion_point}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
