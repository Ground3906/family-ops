"""
Generator: R-6 - South Roof Edge and Bearing, Crosscut Detail
Section through a 6x6 post, view looking west, north at right.
Layers drawn EXPLODED with small gaps for legibility - see general notes.
Format matched to N-1 / R-3: black and white, true-scale members, dimension
chains with leaders, title block bottom-left, three note boxes underneath.
Source: farm/greenhouse-design-sheet.md
Do not hand-edit the SVG - edit this generator and re-run.
"""

import math
from textwrap_arial import wrap, w as tw

# ---------------------------------------------------------------
# LOCKED GEOMETRY
# ---------------------------------------------------------------
PITCH_DEG = 20.556
TH = math.radians(PITCH_DEG)
TAN = math.tan(TH)
COS = math.cos(TH)

RAFTER_ACTUAL = 11.25
RAFTER_PLUMB = RAFTER_ACTUAL / COS          # 12"
SEAT = 6.0
NOTCH_PLUMB = 2.25
ABOVE_SEAT = RAFTER_PLUMB - NOTCH_PLUMB     # 9-3/4"
CUT_ON_EDGE = math.hypot(SEAT, NOTCH_PLUMB) # 6-13/32"

BEAM_W, BEAM_D = 6.0, 10.0
POST_W = 6.0
POST_SHOW = 8.0                             # how far below the beam the post is drawn

OSB = 0.4375
PANEL_T = 0.25                              # flat-course buildup allowance
RIB_H = 0.75                                # Pro-Rib, locked this session
RIB_OC = 9.0                                # Pro-Rib, locked this session
RIB_FACE = 1.5                              # rib width in section, schematic

FLAT_RIP = 5.0                              # ripped flat top course, clears the drip edge
DRIP_FACE = 4.0
DRIP_TOP = 4.0                              # along the rake
DRIP_KICK = 0.5
ROOF_OVERHANG = 8.0                         # past the finished wall surface

BEAM_TOP_AG = 6 * 12 + 10.5
ROOF_PLANE_AG = BEAM_TOP_AG + ABOVE_SEAT
BEAM_BOT_AG = BEAM_TOP_AG - BEAM_D

RAFTER_RUN = 22.0
GAP = 0.9                                   # exploded separation between layers

# closure checks
assert abs(SEAT * TAN - NOTCH_PLUMB) < 1e-4
assert abs(ROOF_PLANE_AG - (7 * 12 + 8.25)) < 0.05
assert FLAT_RIP > DRIP_FACE, "drip edge face leg must land inside the ripped flat course"

# exploded layer planes, measured south (negative) from the framing face
X_SHEATH_IN = -GAP
X_SHEATH_OUT = X_SHEATH_IN - OSB
X_PANEL = X_SHEATH_OUT - GAP                # flat course plane
X_RIB = X_PANEL - RIB_H
X_DRIP = X_PANEL - GAP
X_ROOF_EDGE = X_PANEL - ROOF_OVERHANG
ROOF_OFF = 1.5 * GAP                        # roof panel lift above the rafter top

# ---------------------------------------------------------------
# SHEET
# ---------------------------------------------------------------
SC = 24.0
CANVAS_W, CANVAS_H = 2150, 1420
OX, OY = 1050.0, 606.0

def X(i): return OX + i * SC
def Y(i): return OY - i * SC
def f(v): return f"{v:.2f}"
def roof_y(x): return ABOVE_SEAT + x * TAN

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">',
     f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>']

def rect(x, y, ww, hh, sw=1.0, fill="none"):
    s.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

def line(x1, y1, x2, y2, sw=0.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#000" stroke-width="{sw}"{d}/>')

def pline(pts, sw=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    p = " ".join(f"{f(a)},{f(b)}" for a, b in pts)
    s.append(f'<polyline points="{p}" fill="none" stroke="#000" stroke-width="{sw}"{d}/>')

def poly(pts, sw=1.0, fill="none", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    p = " ".join(f"{f(a)},{f(b)}" for a, b in pts)
    s.append(f'<polygon points="{p}" fill="{fill}" stroke="#000" stroke-width="{sw}"{d}/>')

def text(x, y, t, size=8.0, bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    s.append(f'<text x="{f(x)}" y="{f(y)}" font-family="Arial" font-size="{size}"{b} fill="#000" text-anchor="{anchor}">{t}</text>')

# ===============================================================
# BEAM, POST
# ===============================================================
rect(X(0), Y(0), BEAM_W * SC, BEAM_D * SC, 1.6, "#f2f2f2")
text(X(BEAM_W / 2), Y(-BEAM_D / 2) - 4, "6x10 BEAM", 10.5, True, "middle")
text(X(BEAM_W / 2), Y(-BEAM_D / 2) + 9, "ROUGH-SAWN", 8.5, False, "middle")

rect(X(0), Y(-BEAM_D), POST_W * SC, POST_SHOW * SC, 1.4, "#f2f2f2")
text(X(POST_W / 2), Y(-BEAM_D - 3.2), "6x6 POST", 10.5, True, "middle")
# break line at the bottom of the post
by = Y(-BEAM_D - POST_SHOW)
zz = [(X(0), by)]
step = (POST_W * SC) / 6
for i in range(6):
    zz.append((X(0) + step * (i + 0.5), by + (7 if i % 2 == 0 else -7)))
zz.append((X(POST_W), by))
pline(zz, 1.2)
text(X(POST_W / 2), by + 24, "POST CONTINUES BELOW - NOT SHOWN", 8.0, False, "middle")

# ===============================================================
# RAFTER
# ===============================================================
p_seat_s = (X(0), Y(0))
p_seat_n = (X(SEAT), Y(0))
p_bot_n = (X(RAFTER_RUN), Y((RAFTER_RUN - SEAT) * TAN))
p_top_n = (X(RAFTER_RUN), Y(roof_y(RAFTER_RUN)))
p_top_s = (X(0), Y(ABOVE_SEAT))
poly([p_seat_s, p_top_s, p_top_n, p_bot_n, p_seat_n], 2.0, "#ffffff")
text(X(14), Y(5.2), "2x12 RAFTER @ 24\" O.C.", 10, True, "middle")
text(X(14), Y(5.2) + 12, "DF-L No.2", 8.5, False, "middle")

# birdsmouth wedge, dotted, with its cut sizes
line(X(0), Y(-NOTCH_PLUMB), X(SEAT), Y(0), 0.7, "5,4")
line(X(0), Y(0), X(0), Y(-NOTCH_PLUMB), 0.7, "5,4")

# ===============================================================
# WALL SHEATHING - runs up over the rafter plumb-cut end
# ===============================================================
sh_top = ABOVE_SEAT
sh_bot = -BEAM_D - POST_SHOW
rect(X(X_SHEATH_OUT), Y(sh_top), OSB * SC, (sh_top - sh_bot) * SC, 1.2, "#e8e8e8")

# ===============================================================
# WALL PRO-PANEL - horizontal, ribs schematic, top course ripped flat
# ===============================================================
pp = [(X(X_PANEL), Y(sh_top))]
y = sh_top - FLAT_RIP
while y > sh_bot:
    pp += [(X(X_PANEL), Y(y)), (X(X_RIB), Y(y)),
           (X(X_RIB), Y(y - RIB_FACE)), (X(X_PANEL), Y(y - RIB_FACE))]
    y -= RIB_OC
pp.append((X(X_PANEL), Y(sh_bot)))
pline(pp, 1.6)

# ===============================================================
# DRIP EDGE
# ===============================================================
dh = DRIP_TOP * COS
d1 = (X(dh), Y(roof_y(dh) + GAP))
d2 = (X(X_DRIP), Y(roof_y(X_DRIP) + GAP))
d3 = (X(X_DRIP), Y(roof_y(X_DRIP) + GAP - DRIP_FACE))
d4 = (X(X_DRIP - DRIP_KICK), Y(roof_y(X_DRIP) + GAP - DRIP_FACE - 0.3))
pline([d1, d2, d3, d4], 1.8)

# ===============================================================
# ROOF PANEL - straight line, ribs run down-slope, section cuts a flat pan
# ===============================================================
r1 = (X(X_ROOF_EDGE), Y(roof_y(X_ROOF_EDGE) + ROOF_OFF))
r2 = (X(RAFTER_RUN), Y(roof_y(RAFTER_RUN) + ROOF_OFF))
line(r1[0], r1[1], r2[0], r2[1], 1.8)
line(r1[0], r1[1] - 3, r2[0], r2[1] - 3, 1.0)
line(r1[0], r1[1], r1[0], r1[1] - 3, 1.4)

# ===============================================================
# CALLOUTS - wall assembly on the left, roof and bearing on the right
# ===============================================================
LC, RC = 780.0, 1650.0

def leader_L(tx, ty_, top, lines):
    line(tx, ty_, LC + 70, top + 2, 0.45)
    line(LC + 70, top + 2, LC + 8, top + 2, 0.45)
    for i, ln in enumerate(lines):
        text(LC, top - 8 + i * 11, ln, 8.5 if i == 0 else 8.0, i == 0, "end")

def leader_R(tx, ty_, top, lines):
    line(tx, ty_, RC - 70, top + 2, 0.45)
    line(RC - 70, top + 2, RC - 8, top + 2, 0.45)
    for i, ln in enumerate(lines):
        text(RC, top - 8 + i * 11, ln, 8.5 if i == 0 else 8.0, i == 0)

leader_L(d4[0], d4[1], 270, [
    "DRIP EDGE - STANDARD, HEMMED LEG",
    "NO SHEATHING HERE - FASTEN TO RAFTER TOPS.",
    "TOP LEG 4\" .  FACE LEG 4\" .  KICKER 1/2\"."])

leader_L(X(X_RIB), Y(sh_top - FLAT_RIP - RIB_FACE / 2 - RIB_OC), 490, [
    "WALL PRO-PANEL - RUN HORIZONTAL",
    "3/4\" RIB AT 9\" O.C.  TOP COURSE RIPPED FLAT.",
    "RIBS SHOWN SCHEMATIC."])

leader_L(X(X_SHEATH_OUT), Y(-8.0), 700, [
    "WALL SHEATHING - 7/16\" OSB",
    "UP OVER THE BEAM AND THE RAFTER END."])

leader_R(X(12), Y(roof_y(12) + ROOF_OFF), 215, [
    "PRO-PANEL ROOF METAL",
    "LAPS OVER THE DRIP EDGE TOP LEG.",
    "NO CLOSURE STRIPS AT THIS EDGE."])

leader_R(X(2.7), Y(-0.95), 640, [
    "BIRDSMOUTH - CHOP THE WEDGE OFF",
    "SEAT 6\" .  LEG 2 1/4\" .  HYP 6 13/32\".",
    "RAFTER ABOVE SEAT 9 3/4\" PLUMB, 9 1/8\" PERP.",
    "FULL CUT GEOMETRY ON R-4."])

# ===============================================================
# OVERHANG DIMENSION - above the panel, clear of it
# ===============================================================
oy = 300.0
for xv in (X_ROOF_EDGE, X_PANEL):
    py_panel = Y(roof_y(xv) + ROOF_OFF)
    line(X(xv), oy + 6, X(xv), py_panel - 5, 0.35)
    line(X(xv), oy - 5, X(xv), oy + 5, 0.8)
line(X(X_ROOF_EDGE), oy, X(X_PANEL), oy, 0.8)
text(X((X_ROOF_EDGE + X_PANEL) / 2), oy - 21, "8\"  ROOF PANEL OVERHANG", 9.5, True, "middle")
text(X((X_ROOF_EDGE + X_PANEL) / 2), oy - 9, "PAST THE FINISHED WALL SURFACE", 8.0, False, "middle")

# ===============================================================
# LEFT HEIGHT CHAIN
# ===============================================================
LX = 330.0
line(LX, Y(ABOVE_SEAT), LX, Y(-BEAM_D), 0.7)
text(LX - 6, Y(ABOVE_SEAT) - 28, "ABOVE GRADE", 9, True, "end")

def htick(y_in, label, sub, drop=0.0):
    yy = Y(y_in)
    line(LX - 5, yy, LX + 5, yy, 0.7)
    line(LX - 5, yy, 310, yy + drop, 0.4)
    line(310, yy + drop, 262, yy + drop, 0.4)
    text(258, yy + drop - 2, label, 9.5, True, "end")
    text(258, yy + drop + 9, sub, 8.5, False, "end")

htick(ABOVE_SEAT, "7'-8 1/4\"", "ROOF PLANE AT SOUTH WALL")
htick(0, "6'-10 1/2\"", "BEAM TOP / SEAT CUT")
htick(-BEAM_D, "6'-0 1/2\"", "BEAM BOTTOM = WINDOW HEAD", 16)

# view direction
text(262, 150, "SECTION LOOKING WEST", 9.5, True, "start")
text(262, 163, "NORTH AT RIGHT", 8.5, False, "start")

# ===============================================================
# TITLE BLOCK + NOTE BOXES
# ===============================================================
TB_Y = 1120
text(40, TB_Y, "SOUTH ROOF EDGE AND BEARING - CROSSCUT DETAIL", 17, True)
text(40, TB_Y + 18, "SECTION THROUGH A 6x6 POST - VIEW LOOKING WEST - NORTH AT RIGHT", 12)
text(40, TB_Y + 34, "SCALE:  3\" = 1'-0\"          DRAWING R-6", 12)

BOX_Y = TB_Y + 48
BOX_H = 200
PAD = 12
NOTE_PT = 11.2
NOTE_LH = 14.6

def notebox(x0, wbox, title, items, numbered=False):
    rect(x0, BOX_Y, wbox, BOX_H, 0.8)
    text(x0 + PAD, BOX_Y + 19, title, 12.5, True)
    avail = wbox - 2 * PAD
    yy = BOX_Y + 39
    n = 1
    for it in items:
        src = f"{n}. {it}" if numbered else it
        for ln in wrap(src, NOTE_PT, avail):
            text(x0 + PAD, yy, ln, NOTE_PT)
            yy += NOTE_LH
        n += 1

notebox(40, 660, "GENERAL NOTES", [
    "LAYERS DRAWN EXPLODED FOR CLARITY. AS BUILT THEY STACK TIGHT.",
    "SECTION THROUGH A 6x6 POST. INFILL BETWEEN POSTS IS NON-BEARING, NO HEADER.",
    "BEAM SOUTH FACE IS THE FRAMING PLANE. POSTS AND BEAM FULLY CLAD.",
    "PHASE 1 IS METAL. NO ROOF SHEATHING SOUTH OF THE 9'-7 1/4\" LINE. SEE R-3.",
    "NO ENGINEERED LUMBER.",
    "VENTING NOT SHOWN. SOUTH VENT PANELS ARE BUILT AS THE NORTH ONES - PANEL CUT 1\" LARGER THAN THE R.O., RIBS MATCHED TO THE WALL. SEE V-1.",
], numbered=True)

notebox(720, 660, "ASSEMBLY ORDER - BOTTOM UP", [
    "WALL SHEATHING, UP OVER THE BEAM AND RAFTER END.",
    "WALL PRO-PANEL, HORIZONTAL. TOP COURSE RIPPED FLAT.",
    "DRIP EDGE OVER THE FLAT COURSE.",
    "ROOF PANEL OVER THE DRIP EDGE TOP LEG.",
    "WATER SHEDS OFF THE ROOF, BREAKS AT THE HEM, FALLS PAST THE WALL. NOTHING RUNS BEHIND.",
], numbered=True)

notebox(1400, 660, "MATERIAL SCHEDULE", [
    "RAFTER:  2x12 DF-L No.2 @ 24\" O.C., 20'-0\" STOCK",
    "BEAM:  6x10 ROUGH-SAWN DOUG FIR OR LARCH",
    "POST:  6x6 ROUGH-SAWN, GALVANIZED STANDOFF BASE",
    "WALL SHEATHING:  7/16\" OSB",
    "WALL CLADDING:  PRO-PANEL, 3/4\" RIB AT 9\" O.C., HORIZONTAL",
    "DRIP EDGE:  STANDARD HEMMED, 4\" TOP, 4\" FACE, 1/2\" KICK",
    "ROOFING, PHASE 1:  PRO-PANEL METAL",
    "WALL BUILDUP OUTBOARD OF FRAMING FACE:  3/4\"",
])

s.append('</svg>')
open('/home/claude/greenhouse/R-6-south-roof-edge-detail.svg', 'w').write("\n".join(s))

print("SVG written.")
print(f"roof plane AG {ROOF_PLANE_AG:.3f} in")
print(f"panel edge at {X_ROOF_EDGE:.4f} in from framing face")
print(f"overhang from drawn finished surface: {X_PANEL - X_ROOF_EDGE:.3f} in")
print(f"flat rip {FLAT_RIP} in vs drip face leg {DRIP_FACE} in")
