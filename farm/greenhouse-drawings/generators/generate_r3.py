"""
Generator: R-3 - Greenhouse Roof Framing Plan
Format matched to N-1 / W-1 / E-1: black-and-white line drawing, members drawn
as true-scale rects, dimension strings with tick chains, leader chains left and
right, title block bottom-left, three note boxes underneath.
Source of all dimensions: farm/greenhouse-design-sheet.md
Do not hand-edit the SVG - edit this generator and re-run.
"""

import math

# ---------------------------------------------------------------
# LOCKED GEOMETRY
# ---------------------------------------------------------------
BLDG_LEN = 480.0          # 40'-0" east-west
RAFTER_SPAN = 220.5       # 18'-4 1/2" north framing face to beam south face
FOOTPRINT_DEPTH = 221.0   # 18'-5" nominal footprint

RAFTER_SPACING = 24.0     # LOCKED this session (was 16")
RAFTER_WIDTH = 1.5        # 2x12 actual
LOOKOUT_SPACING = 24.0    # nailer blocking, revised this session
INBOARD_SETBACK = 24.0    # one bay, LOCKED this session

PITCH_DEG = 20.556
THETA = math.radians(PITCH_DEG)

SHEATHING_UP_RAKE = 9 * 12 + 7.25          # 9'-7 1/4"
SHEATHING_RUN = SHEATHING_UP_RAKE * math.cos(THETA)   # horizontal projection

RISER_THK = 5.5           # 2x6 riser wall
BEAM_WIDTH = 6.0          # 6x10 rough-sawn
SIDE_WALL_THK = 5.5       # 2x6

# ---------------------------------------------------------------
# SHEET SETUP - matches N-1 conventions
# ---------------------------------------------------------------
SCALE = 3.0               # px per inch, same as N-1
CANVAS_W, CANVAS_H = 2420, 1256

PX0 = 270.0               # west edge of plan
PY0 = 250.0               # north framing face

def X(inches):
    return PX0 + inches * SCALE

def Y(inches):
    return PY0 + inches * SCALE

def f(v):
    return f"{v:.2f}"

s = []
s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">')
s.append(f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>')

def rect(x, y, w, h, sw=1.0, fill="none"):
    s.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

def line(x1, y1, x2, y2, sw=0.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#000" stroke-width="{sw}"{d}/>')

def text(x, y, txt, size=8.0, bold=False, anchor="start"):
    w = ' font-weight="bold"' if bold else ''
    s.append(f'<text x="{f(x)}" y="{f(y)}" font-family="Arial" font-size="{size}"{w} fill="#000" text-anchor="{anchor}">{txt}</text>')

# ===============================================================
# RAFTER + LOOKOUT LAYOUT
# ===============================================================
# modular run pulled from the west wall
last_mod_x = BLDG_LEN - INBOARD_SETBACK           # 456"
n_mod = int(round(last_mod_x / RAFTER_SPACING)) + 1
mod_xs = [i * RAFTER_SPACING for i in range(n_mod)]
n_spaces = n_mod - 1

# east-end rafter, set just inboard of the east wall inner face so the lookouts
# bear on two rafters instead of cantilevering the full 2'-0"
EAST_WALL_INNER = BLDG_LEN - SIDE_WALL_THK        # 474.5"
east_rafter_x = EAST_WALL_INNER - RAFTER_WIDTH    # 473.0" layout line
LAST_BAY_OC = east_rafter_x - mod_xs[-1]          # 17"
LOOKOUT_CLEAR = east_rafter_x - (mod_xs[-1] + RAFTER_WIDTH)   # 15.5"
LOOKOUT_TAIL = BLDG_LEN - EAST_WALL_INNER         # 5.5" cantilever past east rafter

rafter_xs = mod_xs + [east_rafter_x]
n_rafters = len(rafter_xs)

LOOKOUT_LEN = SIDE_WALL_THK        # 5-1/2", east rafter face to east wall outer face
lookout_ys = []
yy = 0.0
while yy <= RAFTER_SPAN - RAFTER_WIDTH:
    lookout_ys.append(yy)
    yy += LOOKOUT_SPACING
n_lookouts = len(lookout_ys)

# verify the chain closes
assert abs(mod_xs[-1] + LAST_BAY_OC + RAFTER_WIDTH + SIDE_WALL_THK - BLDG_LEN) < 1e-9, \
    "layout does not close on 40'-0\""

# ===============================================================
# WALLS
# ===============================================================
# north wall / riser - INSET, extends south from the north framing face
rect(X(0), Y(0), BLDG_LEN * SCALE, RISER_THK * SCALE, 1.6, "#f2f2f2")
text(X(BLDG_LEN / 2), Y(0) - 10,
     "NORTH WALL - RISER ON CONTAINER - BEARING - RAFTERS LAND FULL WIDTH ON RAKED CAP PLATE, NO NOTCH",
     9.5, True, "middle")

# south wall / beam - INSET, extends north from the beam south face
rect(X(0), Y(RAFTER_SPAN - BEAM_WIDTH), BLDG_LEN * SCALE, BEAM_WIDTH * SCALE, 1.6, "#f2f2f2")
text(X(BLDG_LEN / 2), Y(RAFTER_SPAN) + 15,
     "SOUTH WALL - 6x10 BEAM ON POSTS - BEARING - BIRDSMOUTH SEAT 6\", HEEL 2 1/4\"",
     9.5, True, "middle")

# west wall - bearing - INSET, outer face on the 40'-0" line
rect(X(0), Y(0), SIDE_WALL_THK * SCALE, RAFTER_SPAN * SCALE, 1.4)
# east wall - non-bearing - INSET, outer face on the 40'-0" line
rect(X(EAST_WALL_INNER), Y(0), SIDE_WALL_THK * SCALE, RAFTER_SPAN * SCALE, 1.4)

# ===============================================================
# RAFTERS - true-scale members
# ===============================================================
for x in rafter_xs:
    rect(X(x), Y(0), RAFTER_WIDTH * SCALE, RAFTER_SPAN * SCALE, 1.1)

# both rafters bounding the lookout bay, emphasised
rect(X(mod_xs[-1]), Y(0), RAFTER_WIDTH * SCALE, RAFTER_SPAN * SCALE, 1.8)
rect(X(east_rafter_x), Y(0), RAFTER_WIDTH * SCALE, RAFTER_SPAN * SCALE, 1.8)

# ===============================================================
# LOOKOUTS - drawn as real members, cantilever east to wall face
# ===============================================================
for yv in lookout_ys:
    rect(X(EAST_WALL_INNER), Y(yv), LOOKOUT_LEN * SCALE, RAFTER_WIDTH * SCALE, 1.1)

# ===============================================================
# BLOCKING at sheathing edge
# ===============================================================
block_y = RAFTER_SPAN - SHEATHING_RUN
for i in range(len(rafter_xs) - 1):
    x1 = rafter_xs[i] + RAFTER_WIDTH
    x2 = rafter_xs[i + 1]
    rect(X(x1), Y(block_y), (x2 - x1) * SCALE, RAFTER_WIDTH * SCALE, 0.9)
# blocking continues through the lookout zone
rect(X(mod_xs[-1] + RAFTER_WIDTH), Y(block_y),
     LOOKOUT_CLEAR * SCALE, RAFTER_WIDTH * SCALE, 0.9)

line(X(0), Y(block_y) + RAFTER_WIDTH * SCALE / 2, X(EAST_WALL_INNER), Y(block_y) + RAFTER_WIDTH * SCALE / 2,
     0.45, "5,4")

# sheathing edge leader
CO_X = 2050.0
line(X(BLDG_LEN) + 8, Y(block_y), 2000, Y(block_y) + 60, 0.5)
line(2000, Y(block_y) + 60, CO_X - 8, Y(block_y) + 60, 0.5)
text(CO_X, Y(block_y) + 48, "SHEATHING EDGE / BLOCKING LINE", 8.5, True)
text(CO_X, Y(block_y) + 59, "9'-7 1/4\" UP THE RAKE FROM THE SOUTH", 8.0)
text(CO_X, Y(block_y) + 70, "FRAMING FACE. CONT. 2x12 BLOCKING", 8.0)
text(CO_X, Y(block_y) + 81, "BETWEEN RAFTERS - BACKS THE FASTENER", 8.0)
text(CO_X, Y(block_y) + 92, "ROW AND THE STEP TRANSITION.", 8.0)

# zone labels
text(X(BLDG_LEN / 2), Y(block_y / 2) + 4, "SHEATHED ZONE - PHASE 1 - 7/16\" OSB", 9.0, True, "middle")
text(X(BLDG_LEN / 2), Y(block_y + (RAFTER_SPAN - block_y) / 2) + 4,
     "BARE RAFTER ZONE - METAL DIRECT ON RAFTERS - STRIPS AT PHASE 2", 9.0, True, "middle")

# ===============================================================
# LOOKOUT ZONE CALLOUT
# ===============================================================
lz_mid_x = EAST_WALL_INNER + LOOKOUT_LEN / 2
LO_Y = Y(RAFTER_SPAN * 0.16)
line(X(lz_mid_x), LO_Y, 2000, LO_Y - 30, 0.5)
line(2000, LO_Y - 30, CO_X - 8, LO_Y - 30, 0.5)
text(CO_X, LO_Y - 42, "LOOKOUT BLOCKING - SHEATHING NAILERS", 8.5, True)
text(CO_X, LO_Y - 31, f"({n_lookouts}) 2x12 BLOCKS, 5 1/2\" LONG, 24\" O.C.", 8.0)
text(CO_X, LO_Y - 20, "NAILED TO THE EAST FACE OF THE EAST RAFTER,", 8.0)
text(CO_X, LO_Y - 9, "SPANNING THE EAST WALL THICKNESS ONLY,", 8.0)
text(CO_X, LO_Y + 2, "FLUSH TO THE WALL OUTER FACE. NAILERS ONLY -", 8.0)
text(CO_X, LO_Y + 13, "NOT STRUCTURAL. NO CAP BOARD AT THIS EDGE.", 8.0)

# ===============================================================
# TOP DIMENSION STRING
# ===============================================================
DIM1_Y = PY0 - 90     # overall
DIM2_Y = PY0 - 50     # spacing run

line(X(0), DIM1_Y, X(BLDG_LEN), DIM1_Y, 0.9)
line(X(0), DIM1_Y - 5, X(0), DIM1_Y + 5, 0.9)
line(X(BLDG_LEN), DIM1_Y - 5, X(BLDG_LEN), DIM1_Y + 5, 0.9)
text(X(BLDG_LEN / 2), DIM1_Y - 6, "40'-0\"  OVERALL", 14, True, "middle")

# localised dimension at the east end only - the last bay is non-modular
for xv in [mod_xs[-1], east_rafter_x, BLDG_LEN]:
    line(X(xv), DIM2_Y - 5, X(xv), DIM2_Y + 5, 0.8)
    line(X(xv), DIM2_Y + 5, X(xv), PY0 - 8, 0.35, "2,3")
line(X(mod_xs[-1]), DIM2_Y, X(BLDG_LEN), DIM2_Y, 0.8)
text(X(mod_xs[-1] + LAST_BAY_OC / 2), DIM2_Y - 7, "1'-5\"", 9, True, "middle")
text(X(east_rafter_x) + 40, DIM2_Y + 22, "0'-7\"", 9, True, "middle")
line(X(east_rafter_x) + 34, DIM2_Y + 19, X(east_rafter_x + 3.5), DIM2_Y + 4, 0.35)
text(X(mod_xs[-1]) - 10, DIM2_Y - 7, "LAST BAY - SEE NOTES", 8, False, "end")

# ===============================================================
# LEFT DIMENSION CHAIN (depth)
# ===============================================================
LX = 210.0
line(LX, Y(0), LX, Y(RAFTER_SPAN), 0.7)

def left_tick(y_in, label, sub, drop=0.0):
    yy = Y(y_in)
    line(LX - 5, yy, LX + 5, yy, 0.7)
    line(LX - 5, yy, 190, yy + drop, 0.4)
    line(190, yy + drop, 140, yy + drop, 0.4)
    text(136, yy + drop - 2, label, 9.5, True, "end")
    text(136, yy + drop + 9, sub, 8.5, False, "end")

left_tick(0, "0'-0\"", "NORTH FRAMING FACE")
left_tick(block_y, "8'-11 7/8\"", "BLOCKING / SHEATHING EDGE")
left_tick(RAFTER_SPAN, "18'-4 1/2\"", "BEAM SOUTH FACE", 16)

# ===============================================================
# RIGHT DIMENSION CHAIN (rake / heights)
# ===============================================================
RX = 1790.0
line(RX, Y(0), RX, Y(RAFTER_SPAN), 0.7)
text(1864, Y(0) - 24, "ROOF PLANE", 9, True, "start")

def right_tick(y_in, label, sub, drop=0.0):
    yy = Y(y_in)
    line(RX - 5, yy, RX + 5, yy, 0.7)
    line(RX + 5, yy, 1810, yy + drop, 0.4)
    line(1810, yy + drop, 1860, yy + drop, 0.4)
    text(1864, yy + drop - 2, label, 9.5, True, "start")
    text(1864, yy + drop + 9, sub, 8.5, False, "start")

right_tick(0, "14'-7\"", "PEAK, ABOVE GRADE")
right_tick(block_y, "11'-1 3/8\"", "ROOF PLANE AT BLOCKING")
right_tick(RAFTER_SPAN, "7'-8 1/4\"", "ROOF PLANE AT SOUTH WALL", 16)

# ===============================================================
# WALL END LABELS + NORTH ARROW
# ===============================================================
text(X(0) - SIDE_WALL_THK * SCALE - 12, Y(RAFTER_SPAN * 0.62), "WEST WALL", 11, True, "end")
text(X(0) - SIDE_WALL_THK * SCALE - 12, Y(RAFTER_SPAN * 0.62) + 13, "BEARING", 9, False, "end")
text(X(BLDG_LEN) + SIDE_WALL_THK * SCALE + 12, Y(RAFTER_SPAN * 0.78), "EAST WALL", 11, True, "start")
text(X(BLDG_LEN) + SIDE_WALL_THK * SCALE + 12, Y(RAFTER_SPAN * 0.78) + 13, "NON-BEARING", 9, False, "start")
text(X(BLDG_LEN) + SIDE_WALL_THK * SCALE + 12, Y(RAFTER_SPAN * 0.78) + 24, "NO ROOF CONTACT", 9, False, "start")

s.append('<line x1="198.00" y1="150.00" x2="198.00" y2="96.00" stroke="#000" stroke-width="1.3"/>')
s.append('<polygon points="198.00,84.00 191.00,102.00 205.00,102.00" fill="#000"/>')
text(198, 168, "N", 13, True, "middle")
text(198, 182, "PLAN - VIEW LOOKING DOWN", 8, False, "middle")

# ===============================================================
# TITLE BLOCK + NOTE BOXES
# ===============================================================
TB_Y = 990
text(40, TB_Y, "ROOF FRAMING PLAN", 17, True)
text(40, TB_Y + 18, "PLAN VIEW - LOOKING DOWN - NORTH AT TOP, WEST AT LEFT", 12)
text(40, TB_Y + 34, "SCALE:  1/2\" = 1'-0\"          DRAWING R-3", 12)

BOX_Y = TB_Y + 48
BOX_H = 168

rect(40, BOX_Y, 310, BOX_H, 0.8)
text(48, BOX_Y + 15, "GENERAL NOTES", 9.5, True)
gen = [
    "1. RAFTER FRAMING ONLY. PANEL LAYOUT ON R-2.",
    "2. ROOF PLANE 7'-8 1/4\" AT SOUTH WALL, PEAK 14'-7\".",
    "3. PITCH 4.5:12. RAKE 19'-7 1/2\" PLANE TO PLANE.",
    "4. RAFTER LAYOUT PULLED FROM WEST WALL.",
    "5. NORTH RISER STUDS REMAIN 16\" O.C. - SEE N-1.",
    "6. RAFTERS NO LONGER STACK ON RISER STUDS.",
    "7. EAST WALL CARRIES NO ROOF LOAD.",
    "8. ALL WALLS INSET - FACES ON THE 40'-0\" LINE.",
]
for i, t in enumerate(gen):
    text(50, BOX_Y + 27 + i * 11.4, t, 8.0)

rect(360, BOX_Y, 305, BOX_H, 0.8)
text(368, BOX_Y + 15, "FRAMING NOTES", 9.5, True)
fr = [
    "1. RAFTERS 2x12 @ 24\" O.C., 20'-0\" STOCK.",
    "2. PLUMB CUT BOTH ENDS, CUTS PARALLEL.",
    "3. NORTH END: FULL BEARING ON RAKED CAP PLATE.",
    "4. SOUTH END: BIRDSMOUTH - SEAT 6\", HEEL 2 1/4\".",
    "5. MODULAR RUN STOPS 2'-0\" SHORT OF EAST WALL.",
    "6. EAST RAFTER SET INBOARD OF EAST WALL INNER FACE.",
    "7. LAST BAY 1'-5\" O.C. - 1'-3 1/2\" CLEAR.",
    "8. LOOKOUT BLOCKING 2x12, 5 1/2\" LONG, 24\" O.C.,",
    "   OFF EAST FACE OF EAST RAFTER ONLY.",
    "9. BLOCKING IS SHEATHING NAILER - NOT STRUCTURAL.",
    "10. NO CAP BOARD AT EAST EDGE - NAILS DIRECT.",
    "11. CONT. 2x12 BLOCKING AT SHEATHING EDGE.",
]
for i, t in enumerate(fr):
    text(370, BOX_Y + 27 + i * 11.4, t, 8.0)

rect(675, BOX_Y, 300, BOX_H, 0.8)
text(683, BOX_Y + 15, "MATERIAL SCHEDULE", 9.5, True)
mat = [
    f"RAFTERS:  ({n_rafters}) 2x12 DF-L No.2 @ 20'-0\"",
    f"LOOKOUT BLOCKING:  ({n_lookouts}) 2x12 @ 5 1/2\" LONG",
    "BLOCKING:  2x12 CONT. AT SHEATHING EDGE",
    "BEAM, SOUTH:  6x10 ROUGH-SAWN",
    "CAP PLATE, NORTH:  (2) 2x6 BEVEL CUT",
    "SHEATHING:  7/16\" OSB, NORTH SECTION ONLY",
    "ROOFING, PHASE 1:  PRO-PANEL METAL",
]
for i, t in enumerate(mat):
    text(685, BOX_Y + 27 + i * 11.4, t, 8.0)

s.append('</svg>')

with open('/home/claude/greenhouse/R-3-roof-framing-plan.svg', 'w') as fh:
    fh.write("\n".join(s))

print("SVG written.")
print(f"Bearing rafters: {n_rafters}")
print(f"Spaces: {n_spaces} @ 24in = {n_spaces*24}in = {n_spaces*24/12}ft")
print(f"Last bearing rafter at: {rafter_xs[-1]}in; + {INBOARD_SETBACK} = {rafter_xs[-1]+INBOARD_SETBACK}in")
print(f"Lookout blocking: {n_lookouts} @ {LOOKOUT_SPACING}in o.c., {LOOKOUT_LEN}in long")
print(f"Blocking line at {block_y:.3f}in from north face")
