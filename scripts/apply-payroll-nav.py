#!/usr/bin/env python3
# apply-payroll-nav.py
# Adds the Payroll nav button to cal-widget-current.html and balances the flanks.
# Run from the repo root on the ThinkPad:
#   python scripts/apply-payroll-nav.py

import os, subprocess, sys

f = 'cal-widget-current.html'
if not os.path.exists(f):
    print('ERROR: run from repo root (cal-widget-current.html not found)')
    sys.exit(1)

c = open(f, 'r', encoding='utf-8').read()
changed = 0

# 1 - left zone: flex-shrink:0 -> flex:1
old = 'nav-left-zone{display:flex;align-items:center;justify-content:flex-start;gap:6px;flex-shrink:0;padding-right:8px;border-right:0.5px solid var(--brd);}'
new = 'nav-left-zone{display:flex;align-items:center;justify-content:flex-start;gap:6px;flex:1;padding-right:8px;border-right:0.5px solid var(--brd);}'
if old in c:
    c = c.replace(old, new, 1); changed += 1; print('OK 1: left zone -> flex:1')
else:
    print('SKIP 1: left zone target not found (may already be patched)')

# 2 - right zone: flex-shrink:0 -> flex:1 + justify-content:flex-end
old = '.nav-right-zone{display:flex;align-items:center;gap:4px;flex-shrink:0;padding-left:8px;border-left:0.5px solid var(--brd);}'
new = '.nav-right-zone{display:flex;align-items:center;justify-content:flex-end;gap:4px;flex:1;padding-left:8px;border-left:0.5px solid var(--brd);}'
if old in c:
    c = c.replace(old, new, 1); changed += 1; print('OK 2: right zone -> flex:1 + flex-end')
else:
    print('SKIP 2: right zone target not found (may already be patched)')

# 3 - view buttons: add flex:1 so they expand to fill the right flank
old = '.nav-view-btn{padding:4px;'
new = '.nav-view-btn{flex:1;padding:4px;'
if old in c:
    c = c.replace(old, new, 1); changed += 1; print('OK 3: nav-view-btn -> flex:1')
else:
    print('SKIP 3: nav-view-btn target not found (may already be patched)')

# 4 - payroll CSS (copy of meal-btn / meal-face pattern)
pay_css = (
    '\n#payroll-btn{padding:4px;background:#0c0a06;border:1.5px solid #3a1e06;'
    'border-top-color:#502e0c;border-left-color:#502e0c;border-bottom-color:#000;'
    'border-right-color:#000;border-radius:10px;box-shadow:0 4px 10px rgba(0,0,0,.8);'
    'cursor:pointer;flex-shrink:0;user-select:none;}\n'
    '#payroll-face{background:#6a3e10;border-radius:6px;border-top:1px solid #c07030;'
    'border-left:1px solid #a05a20;border-bottom:1px solid #180800;'
    'border-right:1px solid #2e1004;padding:17px 14px;text-align:center;'
    'box-shadow:inset 0 0 16px rgba(0,0,0,.32);transition:background .15s;}\n'
)
if '#payroll-btn' not in c:
    c = c.replace('</style>', pay_css + '</style>', 1); changed += 1; print('OK 4: payroll CSS added')
else:
    print('SKIP 4: payroll CSS already present')

# 5 - payroll HTML button (injected after Meal Planner button, before nav-center-zone)
anchor = 'class="meal-main">Meal Planner</div>'
pay_html = (
    '\n    <div id="payroll-btn" onclick="window.location.href=\'payroll-current.html\'">'
    '\n      <div id="payroll-face">'
    '\n        <div class="meal-sub">Punch List</div>'
    '\n        <div class="meal-main">Payroll</div>'
    '\n      </div>'
    '\n    </div>'
)
close_seqs = [
    '\n      </div>\n    </div>\n  </div>\n  <div class="nav-center-zone">',
    '\r\n      </div>\r\n    </div>\r\n  </div>\r\n  <div class="nav-center-zone">',
]

if 'payroll-btn' in c:
    print('SKIP 5: payroll button already in HTML')
else:
    patched = False
    for seq in close_seqs:
        old5 = anchor + seq
        if old5 in c:
            new5 = anchor + pay_html + seq
            c = c.replace(old5, new5, 1); changed += 1
            print('OK 5: payroll button HTML added')
            patched = True
            break
    if not patched:
        idx = c.find(anchor)
        if idx >= 0:
            print('WARN 5: anchor found but close-sequence did not match. Nearby:')
            print(repr(c[idx:idx+250]))
            print('Paste this output to Al for a precise fix.')
        else:
            print('WARN 5: anchor not found at all - paste output to Al')

print(f'\n{changed} change(s) applied.')

if changed == 0:
    print('Nothing changed - already patched or targets missing. Check SKIPs above.')
    sys.exit(0)

# Write file preserving original line endings where possible
open(f, 'w', encoding='utf-8').write(c)
print('File written.')

# Git commit and push
print('Committing...')
subprocess.run(['git', 'add', 'cal-widget-current.html'], check=True)
subprocess.run(['git', 'commit', '-m', 'cal-widget: Payroll nav button + balanced flanks (v5.12.1)'], check=True)
subprocess.run(['git', 'push'], check=True)
print('Done. Force-reload the Cockpit to pick it up.')
