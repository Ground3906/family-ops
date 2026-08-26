"""
Generator: R-4 - Birdsmouth at Beam, South Bearing Detail
Format matched to N-1 / R-3: black-and-white line drawing, members drawn as
true-scale rects/polygons, dimension chains with leaders, title block bottom-left,
three note boxes underneath.
Source of all dimensions: farm/greenhouse-design-sheet.md
Do not hand-edit the SVG - edit this generator and re-run.
"""

import math

# ---------------------------------------------------------------
# LOCKED GEOMETRY
# ---------------------------------------------------------------
PITCH_DEG = 20.556
TH = math.radians(PITCH_DEG)
TAN = math.tan(TH)
COS = math.cos(TH)

RAFTER_ACTUAL = 11.25                 # 2x12 actual depth, perpendicular
RAFTER_PLUMB = RAFTER_ACTUAL / COS    # 12"
SEAT = 6.0                            # beam full width
NOTCH_PLUMB = 2.25                    # notch depth at the beam south face
NOTCH_PERP = NOTCH_PLUMB * COS        # 2-1/8"
ABOVE_SEAT_PLUMB = RAFTER_PLUMB - NOTCH_PLUMB     # 9-3/4"
ABOVE_SEAT_PERP = ABOVE_SEAT_PLUMB * COS          # 9-1/8"
CUT_ON_EDGE = math.hypot(SEAT, NOTCH_PLUMB)       # 6-13/32"
TIP_EDGE = RAFTER_ACTUAL * TAN                    # 4-7/32", along the top edge
TIP_RUN = TIP_EDGE * COS                          # horizontal run of the tip wedge

BEAM_W = 6.0
BEAM_D = 10.0
POST_W = 6.0
OSB = 0.4375
PANEL = 0.25

BEAM_TOP_AG = 6 * 12 + 10.5           # 6'-10 1/2"
ROOF_PLANE_AG = BEAM_TOP_AG + ABOVE_SEAT_PLUMB    # 7'-8 1/4"
BEAM_BOT_AG = BEAM_TOP_AG - BEAM_D                # 6'-0 1/2"

RAFTER_RUN = 26.0                     # how far north the rafter is drawn
POST_STUB = 12.5                      # how far down the post is drawn

# closure checks before anything is drawn
assert abs(SEAT * TAN - NOTCH_PLUMB) < 1e-4, "notch does not close on the seat"
assert abs(round(ABOVE_SEAT_PERP, 2) - 9.14) < 0.02, "remaining depth off"
assert abs(ROOF_PLANE_AG - (7 * 12 + 8.25)) < 0.05, "roof plane does not hit 7'-8 1/4\""

# ---------------------------------------------------------------
# SHEET SETUP
# ---------------------------------------------------------------
SC = 24.0                             # px per inch -> 3" = 1'-0"
CANVAS_W, CANVAS_H = 2000, 1345
OX, OY = 690.0, 620.0                 # beam south face, beam top

def X(i):
    return OX + i * SC

def Y(i):
    return OY - i * SC

def f(v):
    return f"{v:.2f}"

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">')
s.append(f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>')

def rect(x, y, w, h, sw=1.0, fill="none"):
    s.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

def poly(pts, sw=1.0, fill="none", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    p = " ".join(f"{f(a)},{f(b)}" for a, b in pts)
    s.append(f'<polygon points="{p}" fill="{fill}" stroke="#000" stroke-width="{sw}"{d}/>')

def line(x1, y1, x2, y2, sw=0.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#000" stroke-width="{sw}"{d}/>')

def text(x, y, t, size=8.0, bold=False, anchor="start"):
    w = ' font-weight="bold"' if bold else ''
    s.append(f'<text x="{f(x)}" y="{f(y)}" font-family="Arial" font-size="{size}"{w} fill="#000" text-anchor="{anchor}">{t}</text>')

# ===============================================================
# BEAM + POST
# ===============================================================
rect(X(0), Y(0), BEAM_W * SC, BEAM_D * SC, 1.6, "#f2f2f2")
text(X(BEAM_W / 2), Y(-BEAM_D / 2), "6x10 BEAM", 11, True, "middle")
text(X(BEAM_W / 2), Y(-BEAM_D / 2) + 13, "ROUGH-SAWN", 9, False, "middle")

rect(X(0), Y(-BEAM_D), POST_W * SC, (POST_STUB - BEAM_D) * SC, 1.4, "#f2f2f2")
text(X(POST_W / 2), Y(-BEAM_D) + 26, "6x6 POST BELOW", 9, True, "middle")

# ===============================================================
# RAFTER - finished condition, birdsmouth cut
# ===============================================================
p_seat_s = (X(0), Y(0))                                             # seat, south end
p_seat_n = (X(SEAT), Y(0))                                          # seat, north end - notch closes here
p_bot_n = (X(RAFTER_RUN), Y((RAFTER_RUN - SEAT) * TAN))             # bottom edge, north
p_top_n = (X(RAFTER_RUN), Y(ABOVE_SEAT_PLUMB + RAFTER_RUN * TAN))   # top edge, north
p_top_s = (X(0), Y(ABOVE_SEAT_PLUMB))                               # tip, top

poly([p_seat_s, p_top_s, p_top_n, p_bot_n, p_seat_n], 2.0, "#ffffff")

text(X(14.5), Y(5.4), "2x12 RAFTER @ 24\" O.C.", 10, True, "middle")
text(X(14.5), Y(5.4) + 12, "DF-L No.2 - 11 1/4\" ACTUAL", 8.5, False, "middle")
text(X(RAFTER_RUN) - 8, Y(9.0), "RAFTER CONTINUES NORTH", 8.0, False, "end")

# ===============================================================
# SHEATHING + CLADDING up the south face and over the rafter end
# ===============================================================
rect(X(-OSB), Y(ABOVE_SEAT_PLUMB), OSB * SC, (ABOVE_SEAT_PLUMB + POST_STUB) * SC, 1.0)
rect(X(-OSB - PANEL), Y(ABOVE_SEAT_PLUMB), PANEL * SC, (ABOVE_SEAT_PLUMB + POST_STUB) * SC, 1.0)

WB_Y = 250.0
line(X(-OSB - PANEL) - 4, Y(ABOVE_SEAT_PLUMB) + 16, 430, WB_Y + 4, 0.5)
line(430, WB_Y + 4, 254, WB_Y + 4, 0.5)
text(250, WB_Y - 36, "WALL BUILDUP, 3/4\" TOTAL", 8.5, True, "end")
text(250, WB_Y - 25, "7/16\" OSB + 1/4\" FLAT-CUT PRO-PANEL,", 8.0, False, "end")
text(250, WB_Y - 14, "OUTBOARD OF THE FRAMING FACE. RUNS UP", 8.0, False, "end")
text(250, WB_Y - 3, "OVER THE BEAM AND COVERS THE RAFTER", 8.0, False, "end")
text(250, WB_Y + 8, "PLUMB-CUT END - NO EXPOSED TIMBER HERE.", 8.0, False, "end")

# ===============================================================
# CUT CALLOUTS
# ===============================================================
# seat cut / beam width - dimensioned below the post, clear of all members
SD = Y(-POST_STUB) + 30
line(X(0), Y(-POST_STUB), X(0), SD + 6, 0.35)
line(X(SEAT), Y(-POST_STUB), X(SEAT), SD + 6, 0.35)
line(X(0), SD, X(SEAT), SD, 0.8)
line(X(0), SD - 5, X(0), SD + 5, 0.8)
line(X(SEAT), SD - 5, X(SEAT), SD + 5, 0.8)
text(X(SEAT / 2), SD + 19, "SEAT CUT = BEAM WIDTH  6\"", 10, True, "middle")
text(X(SEAT / 2), SD + 31, "RAFTER BEARS THE FULL WIDTH", 8.0, False, "middle")

# ---- BIRDSMOUTH WEDGE, shown dotted with its three cut sizes ----
line(X(0), Y(-NOTCH_PLUMB), X(SEAT), Y(0), 0.7, "5,4")
line(X(0), Y(0), X(0), Y(-NOTCH_PLUMB), 0.7, "5,4")

line(X(SEAT * 0.45), Y(-NOTCH_PLUMB * 0.42), X(SEAT + 2.2), Y(-1.9), 0.4)
BW = X(SEAT + 2.4)
text(BW, Y(-1.9) - 4, "BIRDSMOUTH WEDGE - CHOP THIS OFF", 8.5, True)
text(BW, Y(-1.9) + 8, "VERTICAL LEG, AT THE PLUMB FACE ....  2 1/4\"", 8.0)
text(BW, Y(-1.9) + 19, "SEAT RUN, TOP OF THE WEDGE .........  6\"", 8.0)
text(BW, Y(-1.9) + 30, "HYPOTENUSE, ON THE STOCK EDGE ......  6 13/32\"", 8.0)
text(BW, Y(-1.9) + 43, "MARK THE 6\" RUN AND THE 2 1/4\" LEG, CONNECT,", 8.0)
text(BW, Y(-1.9) + 54, "AND CUT. NO TRUE BIRDSMOUTH REQUIRED.", 8.0)

# ---- PLUMB-CUT WEDGE, top edge carried dotted out through the siding ----
TA = (X(0), Y(-NOTCH_PLUMB))
TB = (X(0), Y(ABOVE_SEAT_PLUMB))
TC = (X(-TIP_RUN), Y(ABOVE_SEAT_PLUMB - TIP_RUN * TAN))
line(TB[0], TB[1], TC[0], TC[1], 0.7, "5,4")
line(TC[0], TC[1], TA[0], TA[1], 0.7, "5,4")

# notch closes to zero - leader at the seat north end
line(X(SEAT), Y(0) - 4, X(SEAT + 5.5), Y(0) - 44, 0.5)
line(X(SEAT + 5.5), Y(0) - 44, X(SEAT + 11), Y(0) - 44, 0.5)
text(X(SEAT + 11.4), Y(0) - 47, "NOTCH CLOSES TO ZERO HERE -", 8.0)
text(X(SEAT + 11.4), Y(0) - 37, "STOCK BOTTOM EDGE RESUMES.", 8.0)

# rafter depth above seat - dimensioned AT the plumb face, where it is measured
DC = X(-6.6)
line(DC, Y(ABOVE_SEAT_PLUMB), DC, Y(-NOTCH_PLUMB), 0.7)
for yv in (ABOVE_SEAT_PLUMB, 0.0, -NOTCH_PLUMB):
    line(DC - 5, Y(yv), DC + 5, Y(yv), 0.7)
    line(DC + 5, Y(yv), X(-0.75), Y(yv), 0.3, "2,3")
text(DC - 9, Y(ABOVE_SEAT_PLUMB / 2) - 8, "9 3/4\" PLUMB", 9.5, True, "end")
text(DC - 9, Y(ABOVE_SEAT_PLUMB / 2) + 3, "9 1/8\" PERPENDICULAR", 8.5, False, "end")
text(DC - 9, Y(ABOVE_SEAT_PLUMB / 2) + 14, "RAFTER REMAINING ABOVE THE SEAT,", 8.0, False, "end")
text(DC - 9, Y(ABOVE_SEAT_PLUMB / 2) + 25, "AT THIS FACE. CLEARS THE 2/3-DEPTH", 8.0, False, "end")
text(DC - 9, Y(ABOVE_SEAT_PLUMB / 2) + 36, "MINIMUM OF 7 1/2\".", 8.0, False, "end")
text(DC - 9, Y(-NOTCH_PLUMB / 2) + 3, "2 1/4\" PLUMB", 8.5, True, "end")
text(DC - 9, Y(-NOTCH_PLUMB / 2) + 14, "(2 1/8\" PERP.)", 8.0, False, "end")

# full plumb depth, dimensioned off the north end face
PD = X(RAFTER_RUN) + 12
line(PD, Y((RAFTER_RUN - SEAT) * TAN), PD, Y(ABOVE_SEAT_PLUMB + RAFTER_RUN * TAN), 0.7)
line(PD - 4, Y((RAFTER_RUN - SEAT) * TAN), PD + 4, Y((RAFTER_RUN - SEAT) * TAN), 0.7)
line(PD - 4, Y(ABOVE_SEAT_PLUMB + RAFTER_RUN * TAN), PD + 4, Y(ABOVE_SEAT_PLUMB + RAFTER_RUN * TAN), 0.7)
text(PD + 8, Y((RAFTER_RUN - SEAT) * TAN + RAFTER_PLUMB / 2) - 3, "12\" PLUMB", 8.5, True)
text(PD + 8, Y((RAFTER_RUN - SEAT) * TAN + RAFTER_PLUMB / 2) + 8, "FULL DEPTH", 8.0)

# plumb cut face
line(X(0) - 2, Y(0), X(0) - 2, Y(ABOVE_SEAT_PLUMB), 0.6)
PC = X(0.7)
PCY = Y(8.4)
text(PC, PCY, "PLUMB CUT AT THE BEAM SOUTH FACE", 8.5, True)
text(PC, PCY + 12, "WEDGE OFF THE SQUARE STOCK END:", 8.0)
text(PC, PCY + 23, "ALONG THE TOP EDGE .......  4 7/32\"", 8.0)
text(PC, PCY + 34, "SQUARE STOCK END .........  11 1/4\"", 8.0)
text(PC, PCY + 45, "PLUMB CUT, HYPOTENUSE ....  12\"", 8.0)

# pitch triangle on the top edge
pt_x = 15.0
pt_y = ABOVE_SEAT_PLUMB + pt_x * TAN
line(X(pt_x), Y(pt_y), X(pt_x + 12), Y(pt_y), 0.7)
line(X(pt_x + 12), Y(pt_y), X(pt_x + 12), Y(pt_y + 12 * TAN), 0.7)
text(X(pt_x + 6), Y(pt_y) + 12, "12\"", 8.5, False, "middle")
text(X(pt_x + 12.6), Y(pt_y + 6 * TAN) + 3, "4 1/2\"", 8.5, False)
text(X(pt_x + 6), Y(pt_y) + 24, "PITCH 4.5:12", 8.5, True, "middle")

# ===============================================================
# LEFT HEIGHT CHAIN - above grade
# ===============================================================
LX = 330.0
line(LX, Y(ABOVE_SEAT_PLUMB), LX, Y(-BEAM_D), 0.7)
text(LX - 6, Y(ABOVE_SEAT_PLUMB) - 26, "ABOVE GRADE", 9, True, "end")

def htick(y_in, label, sub, drop=0.0):
    yy = Y(y_in)
    line(LX - 5, yy, LX + 5, yy, 0.7)
    line(LX - 5, yy, 310, yy + drop, 0.4)
    line(310, yy + drop, 260, yy + drop, 0.4)
    text(256, yy + drop - 2, label, 9.5, True, "end")
    text(256, yy + drop + 9, sub, 8.5, False, "end")

htick(ABOVE_SEAT_PLUMB, "7'-8 1/4\"", "ROOF PLANE AT SOUTH WALL")
htick(0, "6'-10 1/2\"", "BEAM TOP / SEAT CUT")
htick(-BEAM_D, "6'-0 1/2\"", "BEAM BOTTOM = WINDOW HEAD", 16)

# ===============================================================
# TITLE BLOCK + NOTE BOXES
# ===============================================================
TB_Y = 1020
text(40, TB_Y, "BIRDSMOUTH AT BEAM - SOUTH BEARING DETAIL", 17, True)
text(40, TB_Y + 18, "SECTION - VIEW LOOKING WEST - NORTH AT RIGHT", 12)
text(40, TB_Y + 34, "SCALE:  3\" = 1'-0\"          DRAWING R-4", 12)

BOX_Y = TB_Y + 48
BOX_H = 205

rect(40, BOX_Y, 330, BOX_H, 0.8)
text(48, BOX_Y + 15, "GENERAL NOTES", 9.5, True)
gen = [
    "1. SOUTH BEARING ONLY. NORTH BEARING IS A RAKED",
    "   CAP PLATE, FULL WIDTH, NO NOTCH - SEE N-1.",
    "2. BEAM SOUTH FACE IS THE WALL FRAMING PLANE.",
    "3. POSTS AND BEAM FULLY CLAD - NO EXPOSED TIMBER",
    "   ON THE SOUTH FACE.",
    "4. NO HEADER AT THE SOUTH WINDOWS - THE WALL IS",
    "   NON-BEARING INFILL BETWEEN POSTS.",
    "5. WINDOW FLANGE LANDS ON THE BEAM UNDERSIDE.",
    "   HEAD CASING SCRIBES TO ROUGH-SAWN TIMBER.",
    "6. NO ENGINEERED LUMBER ANYWHERE ON THIS BUILDING.",
    "7. UPLIFT CONNECTION NOT SHOWN - NOT YET DETAILED.",
    "8. SEE R-3 FOR RAFTER LAYOUT.",
]
for i, t in enumerate(gen):
    text(50, BOX_Y + 27 + i * 11.4, t, 8.0)

rect(380, BOX_Y, 320, BOX_H, 0.8)
text(388, BOX_Y + 15, "CUT SCHEDULE - BIRDSMOUTH", 9.5, True)
cut = [
    "BIRDSMOUTH WEDGE:",
    "  SEAT RUN:  6\" - BEAM FULL WIDTH",
    "NOTCH AT SOUTH FACE:  2 1/4\" PLUMB",
    "                      2 1/8\" PERPENDICULAR",
    "NOTCH AT NORTH END OF SEAT:  ZERO",
    "  HYPOTENUSE ON STOCK EDGE:  6 13/32\"",
    "PLUMB-CUT WEDGE:",
    "  ALONG TOP EDGE:  4 7/32\"",
    "  SQUARE STOCK END:  11 1/4\"",
    "  PLUMB CUT:  12\"",
    "RAFTER ABOVE SEAT:  9 3/4\" PLUMB",
    "                    9 1/8\" PERPENDICULAR",
    "FULL RAFTER DEPTH:  12\" PLUMB",
    "                    11 1/4\" ACTUAL",
    "PLUMB CUT:  FLUSH AT BEAM SOUTH FACE",
    "PITCH:  4.5:12  (20.556 DEG)",
    "BOTH RAFTER END CUTS ARE PARALLEL.",
]
for i, t in enumerate(cut):
    text(390, BOX_Y + 27 + i * 11.4, t, 8.0)

rect(710, BOX_Y, 300, BOX_H, 0.8)
text(718, BOX_Y + 15, "MATERIAL SCHEDULE", 9.5, True)
mat = [
    "RAFTER:  2x12 DF-L No.2, 20'-0\" STOCK",
    "BEAM:  6x10 ROUGH-SAWN DOUG FIR OR LARCH",
    "POST:  6x6 ROUGH-SAWN, GALV. STANDOFF BASE",
    "SHEATHING:  7/16\" OSB",
    "CLADDING:  PRO-PANEL, FLAT-CUT TOP COURSE",
    "WALL BUILDUP:  3/4\" TOTAL OUTBOARD OF THE",
    "               FRAMING FACE",
]
for i, t in enumerate(mat):
    text(720, BOX_Y + 27 + i * 11.4, t, 8.0)

s.append('</svg>')

with open('/home/claude/greenhouse/R-4-birdsmouth-detail.svg', 'w') as fh:
    fh.write("\n".join(s))

print("SVG written.")
print(f"rafter plumb depth       {RAFTER_PLUMB:.3f}")
print(f"above seat plumb/perp    {ABOVE_SEAT_PLUMB:.3f} / {ABOVE_SEAT_PERP:.3f}")
print(f"notch plumb/perp         {NOTCH_PLUMB:.3f} / {NOTCH_PERP:.3f}")
print(f"cut length on stock edge {CUT_ON_EDGE:.3f}")
print(f"roof plane AG            {ROOF_PLANE_AG:.3f}  ({ROOF_PLANE_AG/12:.4f} ft)")
