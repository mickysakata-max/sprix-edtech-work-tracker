import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace font-size: 14px; with font-size: calc(var(--text-scale, 1) * 14px);
# We need to handle optional spaces, important tags etc.
# Actually, the simplest regex:
# font-size:\s*(\d+)px; -> font-size: calc(var(--text-scale, 1) * \1px);

new_css = re.sub(r'font-size:\s*(\d+)px\s*(?:!important)?\s*;', r'font-size: calc(var(--text-scale, 1) * \1px);', css)

# Also need to remove the layout-breaking zoom and transform rules for text-large and text-xlarge
new_css = re.sub(r'body\.text-large\s*\{[^}]+\}', 'body.text-large {\n  --text-scale: 1.15;\n}', new_css)
new_css = re.sub(r'body\.text-xlarge\s*\{[^}]+\}', 'body.text-xlarge {\n  --text-scale: 1.25;\n}', new_css)

# Remove the firefox fallback block that scales the layout
firefox_fallback = r'/\* Firefox compatibility fallback \*/\s*@-moz-document url-prefix\(\)\s*\{[\s\S]*?width:\s*80%;\s*\}\s*\}'
new_css = re.sub(firefox_fallback, '', new_css)

# Inject the thin Sprix stripe at the top of the header
stripe_css = """
/* Phase 9.3: Sprix Brand Accent Stripe */
.header {
  position: relative;
}
.header::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, var(--sprix-navy) 0%, var(--sprix-navy) 30%, var(--sprix-magenta) 100%);
  z-index: 100;
}
"""
new_css += stripe_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

print("Font scaling converted and Sprix stripe injected.")
