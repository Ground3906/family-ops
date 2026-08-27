"""
Generator: R-2 - Roof Panel Layout (Phase 1 metal)
Reproduces the committed R-2 sheet. The ONLY design change from the version at
45f6e39 is the rafter layout: 31 at 16" o.c. becomes 21 at 24" o.c. to match R-3.
Sheet format, colours, panel runs, chalk line and title block are unchanged -
this sheet's look is not being reworked.
Source: farm/greenhouse-design-sheet.md and R-3.
Do not hand-edit the SVG - edit this generator and re-run.
"""

BLDG_LEN = 480.0
RAFTER_SPACING = 24.0          # locked this session, was 16"
INBOARD_SETBACK = 24.0
SIDE_WALL_THK = 5.5
RAFTER_WIDTH = 1.5

PX0, PX1 = 150.0, 950.0
SC = (PX1 - PX0) / BLDG_LEN    # 1.66667 px per inch
TOP, CHALK, BOT = 200.0, 367.1, 599.6

def X(i):
    return PX0 + i * SC

# --- rafter layout, pulled from the west, east rafter inboard of the wall ---
last_mod = BLDG_LEN - INBOARD_SETBACK                 # 456"
mod_xs = [i * RAFTER_SPACING for i in range(int(round(last_mod / RAFTER_SPACING)) + 1)]
east_wall_inner = BLDG_LEN - SIDE_WALL_THK            # 474.5"
east_rafter = east_wall_inner - RAFTER_WIDTH          # 473"
rafter_xs = mod_xs + [east_rafter]
last_bay_oc = east_rafter - mod_xs[-1]                # 17"

assert abs(mod_xs[-1] + last_bay_oc + RAFTER_WIDTH + SIDE_WALL_THK - BLDG_LEN) < 1e-9, \
    "rafter chain does not close on 40'-0\""
assert len(rafter_xs) == 21, f"expected 21 rafters, built {len(rafter_xs)}"

# --- panel run divisions, 14 equal runs, unchanged from the committed sheet ---
panel_div = [PX0 + (PX1 - PX0) * i / 14.0 for i in range(1, 14)]

s = []
s.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 880" width="1100" height="880" font-family="Arial">')
s.append('  <rect width="1100" height="880" fill="#ffffff"/>')
s.append('')
s.append('  <text x="60" y="88" font-size="12" fill="#777" font-style="italic">Not to scale.</text>')
s.append('  <line x1="60" y1="102" x2="1040" y2="102" stroke="#1a1a1a" stroke-width="2"/>')
s.append('')
s.append('  <!-- North arrow -->')
s.append('  <g transform="translate(90,140)">')
s.append('    <polygon points="0,-20 8,6 0,-1 -8,6" fill="#333"/>')
s.append('    <text x="0" y="24" font-size="13" font-weight="bold" text-anchor="middle" fill="#333">N</text>')
s.append('  </g>')
s.append('')
s.append('  <!-- ROOF / PANEL AREA -->')
s.append(f'  <rect x="150" y="200" width="800" height="{CHALK-TOP:.1f}" fill="#2b6cb0" opacity="0.55"/>')
s.append(f'  <rect x="150" y="{CHALK}" width="800" height="{BOT-CHALK:.1f}" fill="#1e4d7b" opacity="0.55"/>')
s.append(f'  <rect x="150" y="200" width="800" height="{BOT-TOP:.1f}" fill="none" stroke="#1a1a1a" stroke-width="1.5"/>')
s.append('')
s.append(f'  <!-- RAFTER LINES - dashed, pulled from the west (bearing) side at 24" o.c.,')
s.append(f'       east rafter set inboard of the east wall inner face -->')
s.append('  <g stroke="#000000" stroke-width="1.1" stroke-dasharray="4 4" opacity="1">')
for xv in rafter_xs:
    s.append(f'    <line x1="{X(xv):.1f}" y1="{TOP:.0f}" x2="{X(xv):.1f}" y2="{BOT}"/>')
s.append('  </g>')
s.append(f'  <text x="545" y="628" font-size="11" fill="#333" text-anchor="middle">rafters (dashed), 24" o.c., pulled from the west &#8212; {len(rafter_xs)} total, last bay 1\'-5"</text>')
s.append('')
s.append('  <!-- East inboard callout -->')
s.append('  <text x="1035" y="150" font-size="11" fill="#333" text-anchor="end">east wall non-bearing &#8212;</text>')
s.append('  <text x="1035" y="165" font-size="11" fill="#333" text-anchor="end">east rafter set inboard of the wall</text>')
s.append('  <text x="1035" y="180" font-size="11" fill="#333" text-anchor="end">inner face, 5 1/2" lookout blocking</text>')
s.append('  <text x="1035" y="195" font-size="11" fill="#333" text-anchor="end">to the wall face &#8212; see R-3</text>')
s.append('  <polyline points="1000,205 970,205 970,340" fill="none" stroke="#333" stroke-width="1"/>')
s.append(f'  <circle cx="{X(east_rafter):.1f}" cy="340" r="3" fill="#333"/>')
s.append(f'  <line x1="{X(east_rafter):.1f}" y1="340" x2="970" y2="340" stroke="#333" stroke-width="1"/>')
s.append('')
s.append('  <!-- panel run divisions, 14 runs across the width -->')
s.append('  <g stroke="#ffffff" stroke-width="2.4" opacity="0.95">')
for xp in panel_div:
    s.append(f'    <line x1="{xp:.1f}" y1="{TOP:.0f}" x2="{xp:.1f}" y2="{BOT}"/>')
s.append('  </g>')
s.append('')
s.append('  <!-- Legend for the two line systems -->')
s.append('  <line x1="150" y1="700" x2="182" y2="700" stroke="#ffffff" stroke-width="2.4"/>')
s.append('  <line x1="150" y1="700" x2="182" y2="700" stroke="#1a1a1a" stroke-width="0.5"/>')
s.append('  <text x="190" y="704" font-size="11" fill="#333">panel run divisions &#8212; 14 runs</text>')
s.append('  <line x1="380" y1="700" x2="412" y2="700" stroke="#000000" stroke-width="1.1" stroke-dasharray="4 4"/>')
s.append('  <text x="420" y="704" font-size="11" fill="#333">rafters below &#8212; reference only</text>')
s.append('')
s.append('  <!-- CHALK LINE -->')
s.append(f'  <line x1="150" y1="{CHALK}" x2="950" y2="{CHALK}" stroke="#c2410c" stroke-width="3" stroke-dasharray="10 5"/>')
s.append(f'  <text x="965" y="371" font-size="14" font-weight="bold" fill="#1a1a1a">CHALK LINE</text>')
s.append('')
s.append('  <!-- panel labels -->')
s.append('  <text x="250" y="235" font-size="15" font-weight="bold" fill="#ffffff">UPPER PANELS</text>')
s.append('  <text x="250" y="253" font-size="12" fill="#ffffff">14 required, each cut to 10\'-10 1/4"</text>')
s.append('  <text x="250" y="269" font-size="12" fill="#ffffff">north: 4" overhang past finished wall</text>')
s.append('')
s.append('  <text x="250" y="520" font-size="15" font-weight="bold" fill="#ffffff">LOWER PANELS</text>')
s.append('  <text x="250" y="538" font-size="12" fill="#ffffff">14 required, each 12\'-0"</text>')
s.append('  <text x="250" y="554" font-size="12" fill="#ffffff">south: 8" overhang past finished wall</text>')
s.append('')
s.append('  <text x="550" y="470" font-size="12" font-weight="bold" fill="#1a1a1a" text-anchor="middle">overlap &#8212; see Detail R-1</text>')
s.append('')
s.append('  <!-- Width dimension across the bottom -->')
s.append('  <line x1="150" y1="662" x2="950" y2="662" stroke="#1a1a1a" stroke-width="1"/>')
s.append('  <line x1="150" y1="655" x2="150" y2="669" stroke="#1a1a1a" stroke-width="1"/>')
s.append('  <line x1="950" y1="655" x2="950" y2="669" stroke="#1a1a1a" stroke-width="1"/>')
s.append('  <text x="550" y="685" font-size="13" fill="#333" text-anchor="middle">40\'-0" building length</text>')
s.append('')
s.append('  <!-- Depth / chalk line offset dimension on the west side, close to the roof -->')
s.append(f'  <line x1="125" y1="200" x2="125" y2="{CHALK}" stroke="#333" stroke-width="1"/>')
s.append('  <line x1="118" y1="200" x2="132" y2="200" stroke="#333" stroke-width="1"/>')
s.append(f'  <line x1="118" y1="{CHALK}" x2="132" y2="{CHALK}" stroke="#333" stroke-width="1"/>')
s.append('  <text x="110" y="288" font-size="12" font-weight="bold" fill="#333" text-anchor="end" transform="rotate(-90 110 288)">8\'-4 1/4" to chalk line</text>')
s.append('')
s.append(f'  <line x1="55" y1="200" x2="55" y2="{BOT}" stroke="#333" stroke-width="1"/>')
s.append('  <line x1="48" y1="200" x2="62" y2="200" stroke="#333" stroke-width="1"/>')
s.append(f'  <line x1="48" y1="{BOT}" x2="62" y2="{BOT}" stroke="#333" stroke-width="1"/>')
s.append('  <text x="37" y="404" font-size="12" font-weight="bold" fill="#333" text-anchor="end" transform="rotate(-90 37 404)">total rake 19\'-7 1/2"</text>')
s.append('')
s.append('  <line x1="60" y1="722" x2="1040" y2="722" stroke="#1a1a1a" stroke-width="1.5"/>')
s.append('')
s.append('  <text x="60" y="746" font-size="15" font-weight="bold" fill="#1a1a1a">INSTALL SEQUENCE</text>')
s.append('  <text x="60" y="768" font-size="13" fill="#333">1. Snap chalk line at 8\'-4 1/4"</text>')
s.append('  <text x="60" y="788" font-size="13" fill="#333">2. Install lower panels to the line</text>')
s.append('  <text x="60" y="808" font-size="13" fill="#333">3. Install upper panels to measurements (4" overhang, lap per Detail R-1)</text>')
s.append('<text x="600" y="746" font-family="Arial" font-size="16" font-weight="bold" fill="#000">PANEL LAYOUT</text>')
s.append('<text x="600" y="768" font-family="Arial" font-size="11" fill="#000">(ROOF PLAN &#x2014; PHASE 1 METAL PANEL LAYOUT)</text>')
s.append('<text x="600" y="788" font-family="Arial" font-size="11" fill="#000">SCALE:  NOT TO SCALE       DRAWING R-2</text>')
s.append('</svg>')

open('/home/claude/greenhouse/R-2-panel-layout.svg', 'w').write("\n".join(s))
print("SVG written.")
print(f"rafters: {len(rafter_xs)} at {RAFTER_SPACING}\" o.c.")
print(f"last modular rafter {mod_xs[-1]}\", east rafter {east_rafter}\", last bay {last_bay_oc}\" o.c.")
print(f"panel run divisions: {len(panel_div)} lines / 14 runs")
