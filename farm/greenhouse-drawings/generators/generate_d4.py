"""
Generator: D-4 - North Roof Edge and Riser Bearing, Crosscut Detail
Section through a vent bay, view looking EAST, north at LEFT.
Layers drawn EXPLODED with small gaps for legibility - see general notes.
Datum is the top of the container, per S-4.
Do not hand-edit the SVG - edit this generator and re-run.
"""

import math
from textwrap_arial import wrap, w as tw

# ---------------------------------------------------------------
# LOCKED GEOMETRY
# ---------------------------------------------------------------
TAN = 4.5 / 12.0
TH = math.atan(TAN)
COS, SIN = math.cos(TH), math.sin(TH)

STUD_D = 5.5
PLATE_T = 1.5
PLATE_W = 5.5
PLATE_STACK = 3.0

RAFTER_PLUMB = 12.0
RAFTER_RUN = 26.0

OSB = 0.4375
RIB_H = 0.75
RIB_OC = 9.0
RIB_FACE = 1.5
FLAT_RIP = 5.0
DRIP_TOP = 4.0
DRIP_FACE = 4.0
DRIP_KICK = 0.5
ROOF_OVERHANG = 4.0

ANGLE_LEG_LEN = 4.0                  # L4x4x1/4
ANGLE_T = 0.25
SH_BOT = 1.0                         # wall sheathing stops 1" off the container

HDR_PACK = 3.0
HDR_CAP = 1.5

FLAP_LEN = 26.0
FLAP_OPEN = math.radians(50.0)
FLAP_LAP = 1.0

BPLATE_TOP = 1.75
SILL_BOT = 17.75
SILL_TOP = 19.25
RO_TOP = 43.25
HDR_TOP = 51.75
CAP_TOP = 57.0
PEAK = 69.0

STUD_TOP_N = CAP_TOP - PLATE_STACK / COS
BEVEL_DROP = STUD_D * TAN

def roof_y(x):  return PEAK + TAN * x
def under_y(x): return CAP_TOP + TAN * x

nx, ny = -SIN, COS
def pl(i):
    a = (0.0 + i * PLATE_T * nx, STUD_TOP_N + i * PLATE_T * ny)
    b = (a[0] - PLATE_W * COS, a[1] - PLATE_W * SIN)
    c = (b[0] + PLATE_T * nx, b[1] + PLATE_T * ny)
    d = (a[0] + PLATE_T * nx, a[1] + PLATE_T * ny)
    return [a, b, c, d]

P1, P2 = pl(0), pl(1)
RAKE_BACK = -P2[3][0]
CRIPPLE_DIE = (STUD_TOP_N - HDR_TOP) / TAN

GAP = 0.9
X_SH_IN = GAP
X_SH_OUT = X_SH_IN + OSB
X_PANEL = X_SH_OUT + GAP
X_RIB = X_PANEL + RIB_H
X_DRIP = X_PANEL + GAP
X_ROOF_EDGE = X_PANEL + ROOF_OVERHANG
X_HINGE = X_RIB + 0.35
EP = 0.35

RSH_LO, RSH_HI = GAP, GAP + OSB
DRIP_OFF = RSH_HI + 0.45 * GAP
PANEL_OFF = RSH_HI + GAP

CONT_N, CONT_D = 18.0, 6.0
CONT_S = -STUD_D                     # container edge on the wall inside plane

# angle: heel at the inside plane, horizontal leg under the plate, LEG UP
ANGLE_OUT_X = CONT_S - ANGLE_T       # outer face of the vertical leg
ANGLE_TOE_X = ANGLE_OUT_X + ANGLE_LEG_LEN
ANGLE_SHY = 0.0 - ANGLE_TOE_X

FLAP_TIP = (X_HINGE + FLAP_LEN * math.sin(FLAP_OPEN),
            RO_TOP + FLAP_LAP - FLAP_LEN * math.cos(FLAP_OPEN))

# ---------------------------------------------------------------
# CLOSURE CHECKS
# ---------------------------------------------------------------
assert abs(BEVEL_DROP - 2.0625) < 1e-9
assert abs(under_y(0.0) - CAP_TOP) < 1e-9
assert abs(PEAK - CAP_TOP - RAFTER_PLUMB) < 1e-9
assert abs(RAKE_BACK - PLATE_STACK * SIN) < 1e-9
assert abs(RO_TOP - SILL_TOP - 24.0) < 1e-9
assert abs(HDR_TOP - RO_TOP - (2 * HDR_CAP + 5.5)) < 1e-9
assert HDR_PACK < STUD_D
assert HDR_TOP < STUD_TOP_N
assert 0 < CRIPPLE_DIE < STUD_D + 0.1
assert abs(ANGLE_SHY - 1.75) < 1e-9, ANGLE_SHY
assert ANGLE_TOE_X < 0.0, "angle toe must stay under the plate"
assert ANGLE_LEG_LEN > BPLATE_TOP, "vertical leg must reach past the plate top"
assert X_DRIP < X_ROOF_EDGE
WRAP_DEV = (SILL_TOP - SILL_BOT) + OSB + PLATE_W
assert abs(WRAP_DEV - 7.4375) < 1e-9

# ---------------------------------------------------------------
# SHEET - north at LEFT
# ---------------------------------------------------------------
SC = 13.0
CANVAS_W, CANVAS_H = 2200, 2200
OX, OY = 1160.0, 1210.0

def X(i): return OX - i * SC
def Y(i): return OY - i * SC
def f(v): return f"{v:.2f}"

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">',
     f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>']

def rect(x, y, ww, hh, sw=1.0, fill="none"):
    s.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

def rect_in(x0, x1, y0, y1, sw=1.0, fill="none"):
    sx0, sx1 = X(x0), X(x1)
    rect(min(sx0, sx1), Y(max(y0, y1)), abs(sx1 - sx0), abs(y1 - y0) * SC, sw, fill)

def line(x1, y1, x2, y2, sw=0.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#000" stroke-width="{sw}"{d}/>')

def pline(pts, sw=1.6):
    p = " ".join(f"{f(a)},{f(b)}" for a, b in pts)
    s.append(f'<polyline points="{p}" fill="none" stroke="#000" stroke-width="{sw}"/>')

def poly(pts, sw=1.0, fill="none"):
    p = " ".join(f"{f(a)},{f(b)}" for a, b in pts)
    s.append(f'<polygon points="{p}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

def poly_in(pts, sw=1.0, fill="none"):
    poly([(X(a), Y(b)) for a, b in pts], sw, fill)

def text(x, y, t, size=18.0, bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    s.append(f'<text x="{f(x)}" y="{f(y)}" font-family="Arial" font-size="{size}"{b} fill="#000" text-anchor="{anchor}">{t}</text>')

# ===============================================================
# CONTAINER
# ===============================================================
rect_in(CONT_S, CONT_N, -CONT_D, 0.0, 1.6, "#ededed")
text(X((CONT_S + CONT_N) / 2), Y(-CONT_D / 2), "40 FT CONTAINER", 22, True, "middle")
text(X((CONT_S + CONT_N) / 2), Y(-CONT_D / 2) + 26, "TOP SIDE RAIL", 18, False, "middle")
text(X((CONT_S + CONT_N) / 2), Y(-CONT_D) + 34, "CONTINUES NORTH AND BELOW - NOT SHOWN", 18, False, "middle")

# ===============================================================
# STEEL ANGLE  L4x4x1/4  -  leg UP the plate's inside face
# ===============================================================
poly_in([(ANGLE_TOE_X, 0.0), (ANGLE_TOE_X, ANGLE_T), (CONT_S, ANGLE_T),
         (CONT_S, ANGLE_LEG_LEN), (ANGLE_OUT_X, ANGLE_LEG_LEN), (ANGLE_OUT_X, 0.0)],
        1.4, "#c9c9c9")

# ===============================================================
# FRAMING
# ===============================================================
rect_in(0.0, -STUD_D, ANGLE_T, BPLATE_TOP, 1.4, "#f2f2f2")
rect_in(0.0, -STUD_D, BPLATE_TOP, SILL_BOT, 1.4, "#f2f2f2")
rect_in(0.0, -STUD_D, SILL_BOT, SILL_TOP, 1.6, "#e2e2e2")

rect_in(0.0, -STUD_D, RO_TOP, RO_TOP + HDR_CAP, 1.4, "#f2f2f2")
rect_in(0.0, -STUD_D, HDR_TOP - HDR_CAP, HDR_TOP, 1.4, "#f2f2f2")
rect_in(0.0, -1.5, RO_TOP + HDR_CAP, HDR_TOP - HDR_CAP, 1.4, "#f2f2f2")
rect_in(-1.5, -HDR_PACK, RO_TOP + HDR_CAP, HDR_TOP - HDR_CAP, 1.4, "#f2f2f2")
line(X(0.0), Y(HDR_TOP), X(0.0), Y(RO_TOP), 1.6)
line(X(-STUD_D), Y(HDR_TOP), X(-STUD_D), Y(RO_TOP), 1.6)

poly_in([(0.0, HDR_TOP), (0.0, STUD_TOP_N), (-CRIPPLE_DIE, HDR_TOP)], 1.4, "#f2f2f2")

poly_in(P1, 1.6, "#ffffff")
poly_in(P2, 1.6, "#ffffff")

# ===============================================================
# RAFTER
# ===============================================================
poly_in([(0.0, CAP_TOP), (0.0, PEAK),
         (-RAFTER_RUN, roof_y(-RAFTER_RUN)), (-RAFTER_RUN, under_y(-RAFTER_RUN))], 2.0, "#ffffff")
rbx = X(-RAFTER_RUN)
rz = [(rbx, Y(under_y(-RAFTER_RUN)))]
rstep = (RAFTER_PLUMB * SC) / 6
for i in range(6):
    rz.append((rbx + (7 if i % 2 == 0 else -7), Y(under_y(-RAFTER_RUN)) - rstep * (i + 0.5)))
rz.append((rbx, Y(roof_y(-RAFTER_RUN))))
pline(rz, 1.2)
text(X(-16.5), Y(under_y(-16.5) + 5.6), "2x12 RAFTER @ 24\" O.C.", 22, True, "middle")
text(X(-16.5), Y(under_y(-16.5) + 5.6) + 24, "DF-L No.2", 18, False, "middle")

# ===============================================================
# WALL SHEATHING
# ===============================================================
rect_in(X_SH_IN, X_SH_OUT, SH_BOT, SILL_TOP, 1.2, "#e8e8e8")
rect_in(X_SH_IN, X_SH_OUT, RO_TOP, PEAK, 1.2, "#e8e8e8")

# ===============================================================
# WALL PRO-PANEL
# ===============================================================
pp = [(X(X_PANEL), Y(PEAK))]
y = PEAK - FLAT_RIP
while y > RO_TOP:
    pp += [(X(X_PANEL), Y(y)), (X(X_RIB), Y(y)),
           (X(X_RIB), Y(y - RIB_FACE)), (X(X_PANEL), Y(y - RIB_FACE))]
    y -= RIB_OC
pp.append((X(X_PANEL), Y(RO_TOP)))
pline(pp, 1.6)

# ===============================================================
# EPDM
# ===============================================================
pline([(X(CONT_N - 0.5), Y(EP)),
       (X(X_SH_OUT + EP), Y(EP)),
       (X(X_SH_OUT + EP), Y(SILL_TOP + EP)),
       (X(X_SH_IN - EP), Y(SILL_TOP + EP)),
       (X(0.0), Y(SILL_TOP + EP)),
       (X(-STUD_D), Y(SILL_TOP + EP))], 3.0)

# ===============================================================
# VENT FLAP - shown open
# ===============================================================
ux, uy = math.sin(FLAP_OPEN), -math.cos(FLAP_OPEN)
px_, py_ = -uy, ux
hx, hy = X_HINGE, RO_TOP + FLAP_LAP
fp = [(X(hx), Y(hy))]
d = RIB_OC / 2.0
while d < FLAP_LEN - RIB_FACE:
    a = (hx + ux * d, hy + uy * d)
    b = (a[0] + px_ * RIB_H, a[1] + py_ * RIB_H)
    c2 = (b[0] + ux * RIB_FACE, b[1] + uy * RIB_FACE)
    e = (a[0] + ux * RIB_FACE, a[1] + uy * RIB_FACE)
    fp += [(X(a[0]), Y(a[1])), (X(b[0]), Y(b[1])), (X(c2[0]), Y(c2[1])), (X(e[0]), Y(e[1]))]
    d += RIB_OC
fp.append((X(FLAP_TIP[0]), Y(FLAP_TIP[1])))
pline(fp, 1.8)
line(X(hx), Y(hy), X(hx) - 11, Y(hy) - 11, 1.2)
text(X(hx) - 14, Y(hy) - 14, "PIANO HINGE", 18, True, "end")

# ===============================================================
# ROOF SHEATHING
# ===============================================================
poly_in([(0.0, roof_y(0.0) + RSH_LO), (0.0, roof_y(0.0) + RSH_HI),
         (-RAFTER_RUN, roof_y(-RAFTER_RUN) + RSH_HI),
         (-RAFTER_RUN, roof_y(-RAFTER_RUN) + RSH_LO)], 1.2, "#e8e8e8")

# ===============================================================
# DRIP EDGE
# ===============================================================
dxs = X_DRIP - DRIP_TOP * COS
d1 = (X(dxs), Y(roof_y(dxs) + DRIP_OFF))
d2 = (X(X_DRIP), Y(roof_y(X_DRIP) + DRIP_OFF))
d3 = (X(X_DRIP), Y(roof_y(X_DRIP) + DRIP_OFF - DRIP_FACE))
d4 = (X(X_DRIP + DRIP_KICK), Y(roof_y(X_DRIP) + DRIP_OFF - DRIP_FACE - 0.3))
pline([d1, d2, d3, d4], 1.8)

# ===============================================================
# ROOF PANEL
# ===============================================================
r1 = (X(X_ROOF_EDGE), Y(roof_y(X_ROOF_EDGE) + PANEL_OFF))
r2 = (X(-RAFTER_RUN), Y(roof_y(-RAFTER_RUN) + PANEL_OFF))
line(r1[0], r1[1], r2[0], r2[1], 1.8)
line(r1[0], r1[1] - 3, r2[0], r2[1] - 3, 1.0)
line(r1[0], r1[1], r1[0], r1[1] - 3, 1.4)

# ===============================================================
# CALLOUTS
# ===============================================================
LC, RC = 760.0, 1560.0
CH, CB, CLH = 21.0, 20.0, 27.0

def leader_L(tx, ty_, top, lines):
    line(tx, ty_, LC + 70, top + 2, 0.5)
    line(LC + 70, top + 2, LC + 10, top + 2, 0.5)
    for i, ln in enumerate(lines):
        text(LC, top - 12 + i * CLH, ln, CH if i == 0 else CB, i == 0, "end")

def leader_R(tx, ty_, top, lines):
    line(tx, ty_, RC - 70, top + 2, 0.5)
    line(RC - 70, top + 2, RC - 10, top + 2, 0.5)
    for i, ln in enumerate(lines):
        text(RC, top - 12 + i * CLH, ln, CH if i == 0 else CB, i == 0)

leader_L(r1[0] + 20, r1[1], 250, [
    "PRO-PANEL ROOF METAL",
    "LAPS OVER THE DRIP EDGE TOP LEG.",
    "OUTSIDE CLOSURES UNDER THE RIBS."])

leader_L(d3[0], d3[1] + 10, 400, [
    "DRIP EDGE - STANDARD, HEMMED",
    "FASTEN TOP LEG TO ROOF SHEATHING.",
    "TURNS DOWN OVER THE WALL FACE.",
    "COVERS SHEATHING EDGE + FLAT COURSE.",
    "LEG SIZE NOMINAL."])

leader_L(X(X_RIB), Y(52.0), 580, [
    "WALL PRO-PANEL - HORIZONTAL",
    "3/4\" RIB AT 9\" O.C.",
    "TOP COURSE RIPPED FLAT."])

leader_L(X(X_SH_OUT), Y(46.5), 720, [
    "WALL SHEATHING - 7/16\" OSB",
    "FULL HEIGHT. THIS IS THE SHEAR.",
    "DOWN TO 1\" OFF THE CONTAINER.",
    "CUT OUT AT THE VENT R.O. ONLY."])

leader_L(X(FLAP_TIP[0] - 4.0), Y(FLAP_TIP[1] + 3.2), 880, [
    "VENT FLAP - SHOWN OPEN",
    "PRO-PANEL, RIBS MATCH THE WALL.",
    "4'-0\" x 2'-0\" R.O., 1\" LAP ALL ROUND.",
    "WAX ACTUATED, FAILS CLOSED."])

leader_L(X(X_SH_OUT + EP), Y(SILL_TOP + EP), 1040, [
    "EPDM MEMBRANE",
    "UP THE SHEATHING, OVER ITS CUT EDGE,",
    "ACROSS THE FULL SILL TOP.",
    "APPROX 7 1/2\" DEVELOPED AT THE SILL."])

leader_L(X(6.0), Y(EP), 1190, [
    "EPDM ONTO THE CONTAINER",
    "CONTAINER IS NOT LEVEL.",
    "WATER WILL POND HERE.",
    "LAP OUT AND SEAL."])

leader_R(X(-3.4), Y(P2[1][1] + 1.5), 500, [
    "(2) 2x6 TOP PLATE - LAID FLAT",
    "PLAIN STOCK ON BEVEL-CUT STUDS.",
    "NOTHING ON THE PLATE IS RIPPED.",
    "SET FLUSH NORTH, ONE ON THE OTHER."])

leader_R(X(-2.0), Y(HDR_TOP + 0.9), 660, [
    "CRIPPLE - BEVEL-RIPPED",
    "2 1/16\" AT THE FACE.",
    "DIES TO NOTHING SOUTH.",
    "AT EVERY RAFTER."])

leader_R(X(-4.2), Y((RO_TOP + HDR_TOP) / 2), 820, [
    "BOX HEADER - 8 1/2\" OVERALL",
    "(2) 2x6 ON EDGE TOGETHER,",
    "TIGHT TO THE EXTERIOR FACE.",
    "CAPS TOP AND BOTTOM.",
    "GAP FALLS ON THE INTERIOR."])

leader_R(X(-3.0), Y(SILL_BOT + 0.75), 1010, [
    "SILL - 2x6 FLAT",
    "THIS FACE IS THE BOTTOM OF THE R.O."])

leader_R(X(ANGLE_OUT_X), Y(2.6), 1120, [
    "L4x4x1/4 ANGLE, PT PLATE ON IT",
    "LEG UP THE PLATE'S INSIDE FACE.",
    "BOLT DOWN THROUGH THE RAIL @ 24\" O.C.",
    "SILL SEAL OR BUTYL UNDER THE PLATE.",
    "TOE 1 3/4\" SHY - SHIM OUTBOARD."])

# ===============================================================
# ROOF OVERHANG DIMENSION
# ===============================================================
oy = 190.0
for xv in (X_PANEL, X_ROOF_EDGE):
    line(X(xv), oy + 6, X(xv), Y(roof_y(xv) + PANEL_OFF) - 5, 0.4)
    line(X(xv), oy - 6, X(xv), oy + 6, 0.9)
line(X(X_PANEL), oy, X(X_ROOF_EDGE), oy, 0.9)
text(X((X_PANEL + X_ROOF_EDGE) / 2), oy - 32, "4\"  ROOF PANEL OVERHANG", 21, True, "middle")
text(X((X_PANEL + X_ROOF_EDGE) / 2), oy - 12, "PAST THE FINISHED WALL SURFACE", 18, False, "middle")

# ===============================================================
# HEIGHT CHAIN
# ===============================================================
LX = 60.0
line(LX, Y(PEAK), LX, Y(0.0), 0.8)
text(LX + 50, Y(PEAK) - 38, "ABOVE CONTAINER TOP", 19, True, "start")

def htick(y_in, label, sub, drop=0.0):
    yy = Y(y_in)
    line(LX - 6, yy, LX + 6, yy, 0.8)
    line(LX + 6, yy, LX + 26, yy + drop, 0.45)
    line(LX + 26, yy + drop, LX + 46, yy + drop, 0.45)
    text(LX + 50, yy + drop - 4, label, 21, True, "start")
    text(LX + 50, yy + drop + 17, sub, 18, False, "start")

htick(PEAK, "5'-9\"", "PEAK")
htick(CAP_TOP, "4'-9\"", "CAP PLATE TOP")
htick(HDR_TOP, "4'-3 3/4\"", "HEADER TOP")
htick(RO_TOP, "3'-7 1/4\"", "R.O. TOP")
htick(SILL_TOP, "1'-7 1/4\"", "R.O. BOTTOM")
htick(SILL_BOT, "1'-5 3/4\"", "SILL BOTTOM", 48)
htick(BPLATE_TOP, "0'-1 3/4\"", "PLATE TOP")
htick(0.0, "0'-0\"", "CONTAINER TOP", 44)

text(30, 70, "SECTION LOOKING EAST", 21, True, "start")
text(30, 96, "NORTH AT LEFT", 18, False, "start")

# ===============================================================
# TITLE BLOCK + NOTE BOXES
# ===============================================================
TB_Y = 1400
text(30, TB_Y, "NORTH ROOF EDGE AND RISER BEARING - CROSSCUT DETAIL", 36, True)
text(30, TB_Y + 36, "SECTION THROUGH A VENT BAY - LOOKING EAST - NORTH AT LEFT", 25)
text(30, TB_Y + 70, "SCALE:  1 1/2\" = 1'-0\"          DRAWING D-4", 25)

BOX_Y = TB_Y + 90
BOX_H = 650
PAD = 22
NOTE_PT = 28.0
NOTE_LH = 37.0

def notebox(x0, wbox, title, items, numbered=False):
    rect(x0, BOX_Y, wbox, BOX_H, 1.0)
    text(x0 + PAD, BOX_Y + 44, title, 30, True)
    avail = wbox - 2 * PAD
    yy = BOX_Y + 92
    n = 1
    for it in items:
        src = f"{n}. {it}" if numbered else it
        for ln in wrap(src, NOTE_PT, avail):
            text(x0 + PAD, yy, ln, NOTE_PT)
            yy += NOTE_LH
        n += 1

notebox(30, 700, "GENERAL NOTES", [
    "LAYERS SHOWN EXPLODED. AS BUILT THEY STACK TIGHT.",
    "ONLY CUT ON THE NORTH WALL.",
    "RAFTERS PLUMB CUT FLUSH AT THE FRAMING FACE. NO NOTCH.",
    "STUD TOPS BEVEL CUT 4.5:12. PLATES ARE FLAT 2x6.",
    "OUTSIDE CLOSURES UNDER THE ROOF PANEL RIBS.",
    "DRIP EDGE LEG NOMINAL. ANY STOCK SIZE WORKS.",
    "FLAP SHOWN OPEN. NO INSULATION ON THIS SHEET.",
], numbered=True)

notebox(760, 700, "ASSEMBLY ORDER - BOTTOM UP", [
    "ANGLE ON THE RAIL, LEG UP. SILL SEAL, THEN THE PT PLATE.",
    "STUDS, TOPS BEVEL CUT. SILL, HEADER, CRIPPLES.",
    "FLAT 2x6 PLATES ON THE BEVEL. RAFTERS ON THE PLATES.",
    "WALL SHEATHING FULL HEIGHT, NAILED TO THE RAFTERS.",
    "EPDM UP AND OVER THE SILL TOP.",
    "SIDING FROM THE SILL UP. TOP COURSE RIPPED FLAT.",
    "ROOF SHEATHING, DRIP EDGE, THEN ROOF PANEL.",
    "VENT FLAP LAST.",
], numbered=True)

notebox(1490, 680, "MATERIAL SCHEDULE", [
    "ANGLE SILL:  L4x4x1/4 CONTINUOUS",
    "BOTTOM PLATE:  2x6 PT",
    "STUDS / CRIPPLES:  2x6, BEVEL 4.5:12",
    "TOP PLATE:  (2) 2x6 FLAT, 3\" PERP.",
    "BOX HEADER:  (2) 2x6 O.E. + CAPS",
    "RAFTERS:  2x12 DF-L No.2 @ 24\" O.C.",
    "SHEATHING:  7/16\" OSB",
    "CLADDING:  PRO-PANEL, 3/4\" RIB",
    "MEMBRANE:  EPDM, CONTINUOUS",
    "DRIP EDGE:  HEMMED, NOMINAL 4\"",
    "ROOFING:  PRO-PANEL METAL",
])

s.append('</svg>')
open('/home/claude/gh/D-4-north-roof-edge-detail.svg', 'w').write("\n".join(s))

print("SVG written.")
print(f"note type / sheet width  {NOTE_PT / CANVAS_W:.4f}")
print(f"angle vertical leg  x {ANGLE_OUT_X} to {CONT_S},  up to {ANGLE_LEG_LEN}\"")
print(f"angle toe at x {ANGLE_TOE_X}, shy of framing face by {ANGLE_SHY}\"")
print(f"plate rake-back {RAKE_BACK:.4f} in, cripple dies at {CRIPPLE_DIE:.4f} in")
