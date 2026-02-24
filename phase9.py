import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Delete redundant right-sidebar containing duplicated status cards
html = re.sub(r'<!-- Right Sidebar \(Status Cards\) -->\s*<aside class="right-sidebar">.*?</aside>', '', html, flags=re.DOTALL)
# It might just be <aside class="right-sidebar"> without the comment
html = re.sub(r'<aside class="right-sidebar">.*?</aside>', '', html, flags=re.DOTALL)

# Update Login Branding
old_auth = '''    <div class="auth-card">
      <div class="auth-logo" style="display: flex; justify-content: center; margin-bottom: 24px;">
        <div
          style="background: white; padding: 12px 24px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
          <img src="sprix-logo.png" alt="SPRIX" style="height: 36px; object-fit: contain;">
        </div>
      </div>'''

# Or if there's arbitrary whitespace:
auth_match = re.search(r'<div class="auth-card">\s*<div class="auth-logo".*?</div>\s*</div>', html, flags=re.DOTALL)
if auth_match:
    new_auth = '''    <div class="auth-card">
      <div class="auth-logo-group" style="text-align: center; margin-bottom: 24px;">
        <div style="display: flex; align-items: center; justify-content: center; gap: 8px;">
          <div style="background: white; padding: 8px 16px; border-radius: 8px; display: inline-flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
             <img src="sprix-logo.png" alt="SPRIX" style="height: 28px; object-fit: contain;">
          </div>
          <span style="font-size: 26px; font-weight: 700; color: var(--sprix-navy); font-family: 'Poppins', sans-serif;">EdTech</span>
        </div>
        <div style="font-size: 16px; font-weight: 500; color: var(--sprix-gray); margin-top: 8px; letter-spacing: 1px;">
          Work Tracker
        </div>
      </div>'''
    html = html.replace(auth_match.group(0), new_auth)
else:
    print("Could not find auth-logo block to replace!")

# Cache busting v8
html = html.replace('?v=7', '?v=8')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add phase 9 CSS overrrides
phase9_css = '''
/* =========================================
   PHASE 9 OVERRIDES (Liquid Glass & Sticky)
   ========================================= */

/* Apple Liquid Glass Parameters */
:root {
  --glass-bg: rgba(255, 255, 255, 0.45);
  --glass-border: 1px solid rgba(255, 255, 255, 0.6);
  --glass-blur: blur(28px) saturate(200%);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
}

[data-theme="dark"] {
  --glass-bg: rgba(30, 41, 59, 0.55);
  --glass-border: 1px solid rgba(255, 255, 255, 0.1);
  --glass-blur: blur(28px) saturate(200%);
  --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

/* Apply Liquid Glass to Core Components */
.app-header, .sidebar, .status-card, .employee-card, .auth-card, .export-card, .calendar-container {
  background: var(--glass-bg) !important;
  backdrop-filter: var(--glass-blur) !important;
  -webkit-backdrop-filter: var(--glass-blur) !important;
  border: var(--glass-border) !important;
  box-shadow: var(--glass-shadow) !important;
}

/* Reset any solid backgrounds forcing on dark theme */
[data-theme="dark"] .app-header, 
[data-theme="dark"] .sidebar, 
[data-theme="dark"] .status-card, 
[data-theme="dark"] .employee-card, 
[data-theme="dark"] .auth-card {
  background: var(--glass-bg) !important;
}

/* Allow scrolling out of page content bounds */
.page-content {
  overflow: visible !important;
  padding-top: 24px;
}

/* Sticky Single-Row Top Status Cards */
.dashboard-stats {
  display: flex !important;
  flex-wrap: nowrap !important;
  overflow-x: auto !important;
  overflow-y: hidden !important;
  gap: 16px !important;
  margin-bottom: 24px !important;
  position: sticky !important;
  top: 72px !important; /* Sticks right below the header */
  z-index: 90 !important;
  padding: 12px 6px 16px 6px !important; /* Padding creates visual buffer for scrolling shadow */
  width: auto !important;
  
  /* Semi-transparent track background for aesthetic appeal and read-behind */
  background: rgba(245, 247, 250, 0.6) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-radius: 12px;
  border: var(--glass-border) !important;
  scroll-behavior: smooth;
  margin-left: -6px;
  margin-right: -6px;
}

[data-theme="dark"] .dashboard-stats {
  background: rgba(15, 23, 42, 0.6) !important;
}

/* Hide scrollbars for absolute elegant cleanliness */
.dashboard-stats::-webkit-scrollbar {
  display: none !important;
}
.dashboard-stats {
  scrollbar-width: none !important;
}

/* Force cards to never shrink below 200px width */
.dashboard-stats .status-card {
  flex: 0 0 auto !important;
  min-width: 220px !important;
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(phase9_css)

