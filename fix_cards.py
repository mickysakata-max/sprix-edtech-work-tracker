with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

cards_html = '''
          <!-- Dashboard Horizontal Stats -->
          <div class="dashboard-stats" id="dashboardStats">
            <div class="status-card" onclick="filterByStatus('total')">
              <div class="status-icon"><i class="ph-fill ph-users-three" style="color: var(--sprix-blue);"></i></div>
              <div class="status-info">
                <h3 id="globalTotal">0</h3>
                <p data-i18n="status.total">Total Employees</p>
              </div>
            </div>
            <div class="status-card office" onclick="filterByStatus('office')">
              <div class="status-icon"><i class="ph-fill ph-buildings" style="color: var(--sprix-blue);"></i></div>
              <div class="status-info">
                <h3 id="globalOffice">0</h3>
                <p data-i18n="status.inOffice">In Office</p>
              </div>
            </div>
            <div class="status-card remote" onclick="filterByStatus('remote')">
              <div class="status-icon"><i class="ph-fill ph-house-line" style="color: var(--sprix-blue);"></i></div>
              <div class="status-info">
                <h3 id="globalRemote">0</h3>
                <p data-i18n="status.remote">Remote Work</p>
              </div>
            </div>
            <div class="status-card leave" onclick="filterByStatus('leave')">
              <div class="status-icon"><i class="ph-fill ph-moon" style="color: var(--sprix-blue);"></i></div>
              <div class="status-info">
                <h3 id="globalLeave">0</h3>
                <p data-i18n="status.leave">Leave / Off</p>
              </div>
            </div>
            <div class="status-card finished" onclick="filterByStatus('finished')">
              <div class="status-icon"><i class="ph-fill ph-flag-checkered" style="color: var(--sprix-blue);"></i></div>
              <div class="status-info">
                <h3 id="globalFinished">0</h3>
                <p data-i18n="analytics.finished">Finished</p>
              </div>
            </div>
          </div>
'''

insertion_point = '<div class="view active" id="viewDashboard">'
# Only insert if it's not already there
if 'dashboardStats' not in html:
    html = html.replace(insertion_point, f'{cards_html}\n          {insertion_point}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
