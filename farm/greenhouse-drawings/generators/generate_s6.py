"""
Generator: S-6 - Foundation Plan
Plan view looking down, north at top, west at left. Overlays S-5.
Datum is the container's south face (the north framing face), per the set.
Do not hand-edit the SVG - edit this generator and re-run.
"""

import math
from textwrap_arial import wrap

# ---------------------------------------------------------------
# LOCKED GEOMETRY  -  all inches
# ---------------------------------------------------------------
WIDTH = 480.0                  # 40'-0" east-west, container's full face
DEPTH = 220.5                  # 18'-4 1/2" container face to beam south face
WALL = 5.5                     # 2x6 framing

BEAM_W = 6.0                   # grade beam width
BEAM_BELOW = 6.0               # below finished grade
BEAM_ABOVE = 6.0               # above finished grade
BEAM_H = BEAM_BELOW + BEAM_ABOVE
BEAM_OUT = BEAM_W - WALL       # projection outboard of the framing plane

PIER_D = 36.0                  # below grade - this is the frost control
PIER_W = 6.0                   # plan size, nominal - matches the beam, no flare
PIER_L = 6.0
FROST = 24.0                   # owner-measured max on site

POSTS = 5
BAYS = 4
POST_W = 5.5                   # 6x6
POST_SPAN = 479.0              # S-1: post outer face to outer face
POST_OC = (POST_SPAN - POST_W) / BAYS   # S-1 draws 118 3/8, not the nominal 120
POST_X = [POST_W / 2 + i * POST_OC for i in range(POSTS)]
JB_CLR = 6.0                   # J-bolts set this far inside each post face

AB_OC = 72.0                   # J-bolts 6'-0" o.c.
AB_CNR = 12.0                  # and within 12" of each corner
FLOOR_FALL = 0.125             # per foot, away from the container

CONT_SHOW = 96.0               # container drawn full 8 ft so the wrap reads

SLAB_D = 120.0                 # 10'-0" off the container, inside the greenhouse
SLAB_T = 3.0                   # 3" slab, poured on this project

W_DOOR_S = 61.5                # west man door R.O. south edge - derived from S-2
E_DOOR_S = 174.0               # east man door R.O. south edge - S-3 opening schedule
CONT_W = 96.0                  # container 8'-0" north-south
W_DOOR_N = 17.5                # west man door R.O. north edge - from S-2
E_DOOR_N = 132.0               # east door opening north edge - as drawn on S-3
W_DOOR_RO = 44.0               # west opening as drawn on S-2
E_DOOR_RO = 42.0               # east opening as drawn on S-3 - a 3'-6" door

WALK_W = 60.0                  # west walk 5'-0" off the greenhouse wall
WALK_N = -192.0                # 16'-0" north of the container south edge
WALK_S = W_DOOR_S + 12.0       # 1'-0" past the west door

EPAD_W = 78.0                  # east slab 6'-6" off the greenhouse wall
EPAD_N = -96.0                 # 8'-0" north - flush with the container north face
EPAD_S = E_DOOR_S + 12.0       # 1'-0" past the east door

FLAT_T = 4.0                   # exterior flatwork thickness, skid and barrow duty
AB_DOOR = 6.0                  # J-bolt clear of each door gap

# beam faces, in plan coordinates (x east from the west framing plane,
# y south from the container face)
W_OUT, W_IN = -BEAM_OUT, WALL                  # west leg
E_IN, E_OUT = WIDTH - WALL, WIDTH + BEAM_OUT   # east leg
S_IN, S_OUT = DEPTH - WALL, DEPTH + BEAM_OUT   # south leg

W_CL = (W_OUT + W_IN) / 2.0
E_CL = (E_IN + E_OUT) / 2.0
S_CL = (S_IN + S_OUT) / 2.0

# piers: both ends and midspan, east and west legs only
PIER_STANDOFF = 12.0           # clear excavation from the container face
PIER_N = PIER_STANDOFF + PIER_L / 2.0
PIER_S = S_CL
PIER_M = (PIER_N + PIER_S) / 2.0
PIER_Y = [PIER_N, PIER_M, PIER_S]
PIER_SPACING = PIER_M - PIER_N

# ---------------------------------------------------------------
# CLOSURE CHECKS
# ---------------------------------------------------------------
assert abs(POST_OC - 118.375) < 1e-6, POST_OC
assert abs((POST_X[-1] + POST_W/2) - POST_SPAN) < 1e-9, "post line must close on S-1"
assert POST_SPAN < WIDTH, "S-1 post line is narrower than the container"
assert POSTS == BAYS + 1
assert abs(BEAM_H - 12.0) < 1e-9, "12x12 section"
assert abs((W_IN - W_OUT) - BEAM_W) < 1e-9
assert abs((E_OUT - E_IN) - BEAM_W) < 1e-9
assert abs((S_OUT - S_IN) - BEAM_W) < 1e-9
assert abs(BEAM_OUT - 0.5) < 1e-9, BEAM_OUT
assert BEAM_W >= WALL, "beam must be at least the wall thickness"

assert PIER_D > FROST, "piers must reach below frost"
assert SLAB_D < DEPTH, "slab must sit inside the footprint"
assert WALK_S > W_DOOR_S and EPAD_S > E_DOOR_S, "flatwork begins south of its door"
assert WALK_S < DEPTH and EPAD_S < DEPTH, "flatwork stays inside the building run"
assert CONT_SHOW <= CONT_W, "container strip drawn no deeper than the container"
assert abs((WALK_S - WALK_N) - 265.5) < 1e-9, "west walk total run"
assert abs((EPAD_S - EPAD_N) - 282.0) < 1e-9, "east slab total run"
assert abs(EPAD_N + CONT_W) < 1e-9, "east slab closes on the container north face"
assert abs(W_DOOR_S - W_DOOR_N - W_DOOR_RO) < 1e-9
assert abs(E_DOOR_S - E_DOOR_N - E_DOOR_RO) < 1e-9
assert FLAT_T > SLAB_T, "exterior is thicker than the pen slab"
assert PIER_N + PIER_L / 2 <= SLAB_D, "north pier lands beside the slab, not under it"
assert W_IN < E_IN, "slab runs wall inside face to wall inside face"
assert abs(2 * PIER_SPACING - (PIER_S - PIER_N)) < 1e-9
assert PIER_Y[0] - PIER_L / 2 >= PIER_STANDOFF - 1e-9, "north pier hole must clear the container face"
assert PIER_W == BEAM_W, "pier is a deepening of the beam, not a wider pad"
assert PIER_Y[-1] <= S_CL + 1e-9, "south pier centred on the beam"

def ft(v):
    from fractions import Fraction as F
    f = F(v).limit_denominator(64)
    neg = f < 0
    f = abs(f)
    a, r = divmod(f, 12)
    w = int(r)
    fr = r - w
    s = f"{int(a)}'-{w}"
    if fr:
        s += f" {fr.numerator}/{fr.denominator}"
    return ("-" if neg else "") + s + '"'

# ---------------------------------------------------------------
# SHEET
# ---------------------------------------------------------------
SC = 3.0                       # 1/2" = 1'-0", same as S-5
CANVAS_W, CANVAS_H = 2900, 2560
OX, OY = 500.0, 700.0

def X(v): return OX + v * SC
def Y(v): return OY + v * SC
def f(v): return f"{v:.2f}"

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">',
     f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>']

def rect(x, y, w, h, sw=1.0, fill="none", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" stroke="#000" stroke-width="{sw}"{d}/>')

def rect_in(x0, x1, y0, y1, sw=1.0, fill="none", dash=None):
    rect(X(min(x0, x1)), Y(min(y0, y1)), abs(x1 - x0) * SC, abs(y1 - y0) * SC, sw, fill, dash)

def line(x1, y1, x2, y2, sw=0.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#000" stroke-width="{sw}"{d}/>')

def poly(pts, sw=1.0, fill="none"):
    p = " ".join(f"{f(X(a))},{f(Y(b))}" for a, b in pts)
    s.append(f'<polygon points="{p}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

poly_in = poly   # poly already maps building coords through X()/Y()

def text(x, y, t, size=18.0, bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    s.append(f'<text x="{f(x)}" y="{f(y)}" font-family="Arial" font-size="{size}"{b} fill="#000" text-anchor="{anchor}">{t}</text>')

# ===============================================================
# CONTAINER - north wall, no footing this edge
# ===============================================================
rect_in(W_OUT, E_OUT, -CONT_SHOW, 0.0, 1.6, "#ffffff")
text(X(WIDTH / 2), Y(-CONT_SHOW / 2) - 2, "40 FT CONTAINER - NORTH WALL", 21, True, "middle")
text(X(WIDTH / 2), Y(-CONT_SHOW / 2) + 20, "SITS ON DIRT - NO FOOTING, NO EXCAVATION THIS EDGE", 17, False, "middle")

# ===============================================================
# EXTERIOR FLATWORK
# ===============================================================
W_OUTER = W_OUT - WALK_W
poly_in([(W_OUTER, WALK_N), (W_OUTER, WALK_S), (W_OUT, WALK_S), (W_OUT, 0.0),
         (0.0, 0.0), (0.0, WALK_N)], 1.4, "#efefef")
text(X((W_OUTER + W_OUT) / 2), Y(30.0) - 4, "5'-0\" WALK", 21, True, "middle")
text(X((W_OUTER + W_OUT) / 2), Y(30.0) + 20, "4\" THICK", 18, False, "middle")
text(X((W_OUTER + 0.0) / 2), Y(WALK_N / 2) - 4, "16'-0\" FROM", 19, True, "middle")
text(X((W_OUTER + 0.0) / 2), Y(WALK_N / 2) + 18, "CONTAINER S. EDGE", 17, False, "middle")

E_OUTER = E_OUT + EPAD_W
poly_in([(E_OUTER, EPAD_N), (E_OUTER, EPAD_S), (E_OUT, EPAD_S), (E_OUT, 0.0),
         (WIDTH, 0.0), (WIDTH, EPAD_N)], 1.4, "#efefef")
text(X((E_OUT + E_OUTER) / 2), Y(EPAD_N + 24.0) - 4, "6'-6\" SLAB", 21, True, "middle")
text(X((E_OUT + E_OUTER) / 2), Y(EPAD_N + 24.0) + 20, "4\" THICK", 18, False, "middle")

# ===============================================================
# DOOR GAPS - beam poured to grade only, slab forms the threshold
# ===============================================================
for (cl, lo, hi) in ((W_CL, W_DOOR_N, W_DOOR_S), (E_CL, E_DOOR_N, E_DOOR_S)):
    rect_in(cl - BEAM_W / 2, cl + BEAM_W / 2, lo, hi, 2.0, "#ffffff")
    line(X(cl - BEAM_W / 2), Y(lo), X(cl + BEAM_W / 2), Y(hi), 1.0)
    line(X(cl - BEAM_W / 2), Y(hi), X(cl + BEAM_W / 2), Y(lo), 1.0)

# ===============================================================
# 3" SLAB - 10'-0" off the container, wall to wall
# ===============================================================
rect_in(W_IN, E_IN, 0.0, SLAB_D, 1.6, "#d4d4d4")
text(X(WIDTH / 2), Y(SLAB_D / 2) - 6, '3" SLAB', 26, True, "middle")
text(X(WIDTH / 2), Y(SLAB_D / 2) + 18, "10'-0\" OFF THE CONTAINER, WALL TO WALL", 19, False, "middle")

# ===============================================================
# GRADE BEAM - one monolithic U, open at the north
# ===============================================================
poly([(W_OUT, 0.0), (W_OUT, S_OUT), (E_OUT, S_OUT), (E_OUT, 0.0),
      (E_IN, 0.0), (E_IN, S_IN), (W_IN, S_IN), (W_IN, 0.0)], 2.0, "#d8d8d8")

# ===============================================================
# PIERS - east and west legs only, dashed (below grade)
# ===============================================================
for cl in (W_CL, E_CL):
    for yy in PIER_Y[:-1]:
        rect_in(cl - PIER_W / 2, cl + PIER_W / 2, yy - PIER_L / 2, yy + PIER_L / 2,
                2.2, "#8f8f8f", "8,4")

# ===============================================================
# SOUTH POSTS - PIER UNDER EACH, NO PAD
# ===============================================================
for px in POST_X:
    rect_in(px - PIER_W / 2, px + PIER_W / 2, S_CL - PIER_L / 2, S_CL + PIER_L / 2,
            2.2, "#8f8f8f", "8,4")
    rect_in(px - 2.75, px + 2.75, DEPTH - WALL, DEPTH, 1.6, "#ffffff")

# ===============================================================
# J-BOLTS - 6'-0" o.c., within 12" of each corner
# ===============================================================
def bolt(x, y):
    cx, cy = X(x), Y(y)
    s.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="3.2" fill="#000"/>')

nb = 0
for cl in (W_CL, E_CL):
    yy = AB_CNR
    while yy <= S_CL - AB_CNR:
        bolt(cl, yy); nb += 1
        yy += AB_OC
    bolt(cl, S_CL - AB_CNR); nb += 1
jb = []
for k in range(BAYS):
    jb.append(POST_X[k] + POST_W / 2 + JB_CLR)
    jb.append(POST_X[k + 1] - POST_W / 2 - JB_CLR)
for xx in jb:
    bolt(xx, S_CL); nb += 1
for (cl, lo, hi) in ((W_CL, W_DOOR_N, W_DOOR_S), (E_CL, E_DOOR_N, E_DOOR_S)):
    bolt(cl, lo - AB_DOOR); nb += 1
    bolt(cl, hi + AB_DOOR); nb += 1

# ===============================================================
# NORTH ARROW
# ===============================================================
nax, nay, nar = 150.0, 120.0, 30.0
s.append(f'<circle cx="{f(nax)}" cy="{f(nay)}" r="{f(nar)}" fill="none" stroke="#000" stroke-width="1.6"/>')
s.append(f'<polygon points="{f(nax)},{f(nay-nar-13)} {f(nax-11)},{f(nay+nar*0.55)} {f(nax)},{f(nay+nar*0.18)} {f(nax+11)},{f(nay+nar*0.55)}" fill="#000" stroke="#000" stroke-width="1.0"/>')
text(nax, nay - nar - 22, "N", 26, True, "middle")

# ===============================================================
# FLOOR FALL ARROW
# ===============================================================
line(X(WIDTH / 2), Y(SLAB_D + 20.0), X(WIDTH / 2), Y(S_IN - 20.0), 1.0, "9,6")
text(X(WIDTH / 2), Y(SLAB_D + 55.0) - 8, 'DIRT FLOOR - FALL 1/8" PER FT SOUTH', 19, True, "middle")
text(X(WIDTH / 2), Y(SLAB_D + 55.0) + 14, "SOUTH OF THE SLAB", 17, False, "middle")

# ===============================================================
# DIMENSIONS
# ===============================================================
def dimh(x0, x1, ys, label, sub=None):
    line(X(x0), ys, X(x1), ys, 0.9)
    for xv in (x0, x1):
        line(X(xv), ys - 7, X(xv), ys + 7, 0.9)
    text(X((x0 + x1) / 2), ys - 9, label, 19, True, "middle")
    if sub:
        text(X((x0 + x1) / 2), ys + 24, sub, 16, False, "middle")

def dimv(y0, y1, xs, label, sub=None, side="left"):
    line(xs, Y(y0), xs, Y(y1), 0.9)
    for yv in (y0, y1):
        line(xs - 7, Y(yv), xs + 7, Y(yv), 0.9)
    a = "end" if side == "left" else "start"
    dx = -9 if side == "left" else 9
    text(xs + dx, Y((y0 + y1) / 2) - 6, label, 19, True, a)
    if sub:
        text(xs + dx, Y((y0 + y1) / 2) + 14, sub, 16, False, a)

ydim = Y(S_OUT) + 70
for i in range(BAYS):
    dimh(POST_X[i], POST_X[i + 1], ydim, ft(POST_OC))
dimh(0.0, POST_SPAN, ydim + 92, ft(POST_SPAN), "POST LINE, OUTER FACE TO OUTER FACE - PER S-1")
dimh(0.0, WIDTH, ydim + 184, ft(WIDTH), "CONTAINER - SEE NOTE 8")

xdim = X(W_OUT - WALK_W) - 62
dimv(0.0, DEPTH, xdim, ft(DEPTH), "FACE TO FRAMING")
xdim2 = X(E_OUT) + 46
for i in range(len(PIER_Y) - 1):
    dimv(PIER_Y[i], PIER_Y[i + 1], xdim2, ft(PIER_SPACING), "PIER O.C.", "right")

# ===============================================================
# CALLOUTS
# ===============================================================
RC = 2420.0

def leader(tx, ty, top, lines):
    line(tx, ty, RC - 70, top + 2, 0.5)
    line(RC - 70, top + 2, RC - 10, top + 2, 0.5)
    for i, ln in enumerate(lines):
        text(RC, top - 10 + i * 24, ln, 19 if i == 0 else 17, i == 0)

leader(X(E_CL), Y(AB_CNR + AB_OC), 300, [
    "J-BOLT - 1/2\" x 10\"",
    "EAST AND WEST LEGS ONLY.",
    "6'-0\" O.C. AND WITHIN 12\" OF EVERY CORNER."])

leader(X(E_CL), Y(PIER_M), 460, [
    "PIER - 36\" BELOW GRADE",
    "CAST INTEGRAL WITH THE BEAM.",
    "THIS IS THE FROST CONTROL."])

leader(X(E_OUT), Y(150.0), 610, [
    "GRADE BEAM - 6\" x 12\"",
    "6\" BELOW GRADE, 6\" ABOVE.",
    "FLUSH INBOARD WITH THE WALL INSIDE",
    "FACE. 1/2\" PROUD OUT."])

leader(X(jb[5]), Y(S_CL), 790, [
    "J-BOLT - SOUTH WALL, PER BAY",
    "TWO PER BAY, 6\" INSIDE EACH POST",
    "FACE. ANCHORS THE SILL PLATE",
    "BETWEEN POSTS."])

leader(X(POST_X[3]), Y(S_CL + PIER_L / 2), 970, [
    "PIER UNDER EACH POST",
    "5 POSTS, 6x6, STANDOFF BASES.",
    "NO PADS."])

# ===============================================================
# TITLE BLOCK + NOTE BOXES
# ===============================================================
TB_Y = 1680
text(30, TB_Y, "FOUNDATION AND CONCRETE PLAN", 38, True)
text(30, TB_Y + 38, "MONOLITHIC GRADE BEAM WITH INTEGRAL PIERS - PLAN LOOKING DOWN - NORTH AT TOP, WEST AT LEFT", 24)
text(30, TB_Y + 72, "SCALE:  1/2\" = 1'-0\"          DRAWING S-6", 24)

BOX_Y = TB_Y + 92
BOX_H = 700
PAD_B = 22
NOTE_PT = 30.0
NOTE_LH = 34.0

def notebox(x0, w, title, items, numbered=False):
    rect(x0, BOX_Y, w, BOX_H, 1.0)
    text(x0 + PAD_B, BOX_Y + 42, title, 28, True)
    avail = w - 2 * PAD_B
    yy = BOX_Y + 88
    n = 1
    for it in items:
        src = f"{n}. {it}" if numbered else it
        for ln in wrap(src, NOTE_PT, avail):
            text(x0 + PAD_B, yy, ln, NOTE_PT)
            yy += NOTE_LH
        n += 1

notebox(30, 1390, "GENERAL NOTES", [
    "ONE MONOLITHIC POUR. BEAM AND PIERS TOGETHER.",
    "NO FOOTING AT THE NORTH. CONTAINER CARRIES THAT EDGE.",
    "DO NOT EXCAVATE ALONG THE CONTAINER'S SOUTH FACE. NORTH PIER HOLES HELD 12\" CLEAR OF IT.",
    "PIERS REACH BELOW FROST. NO FROST SKIRT ON THIS BUILDING.",
    "PIER UNDER EVERY POST. THE CORNER POST PIER IS ALSO THE LEG CORNER DROP.",
    "PIER PLAN SIZE NOMINAL. THE 36\" DEPTH IS THE CONTROL.",
    "NO POST PADS. EACH POST BEARS ON THE BEAM WITH A PIER UNDER IT.",
    "S-1 DRAWS THE POST LINE 39'-11\" OUTER TO OUTER UNDER A 40'-0\" CONTAINER. VERIFY THE 1\" AT LAYOUT BEFORE FORMING.",
    "#4 REBAR AS TYPICAL.",
    "PEN SLAB AND EXTERIOR FLATWORK POURED THIS PROJECT, NOT PART OF THE STRUCTURAL POUR.",
    "BEAM POURED TO GRADE ONLY ACROSS BOTH DOOR OPENINGS. THE SLAB COMES UP FLUSH AT 0'-6\" AND FORMS THE THRESHOLD.",
    "J-BOLT EACH SIDE OF BOTH DOOR GAPS, 6\" CLEAR.",
], numbered=True)

notebox(1460, 1390, "SCHEDULE", [
    "GRADE BEAM:  6\" WIDE x 12\" DEEP, 6 BELOW / 6 ABOVE",
    "PIERS:  6\" SQ x 36\" DEEP",
    "PIERS:  4 EAST/WEST + 5 UNDER POSTS = 9",
    f"PIER SPACING:  {ft(PIER_SPACING)} O.C.",
    "J-BOLTS, SOUTH:  2 PER BAY, 6\" INSIDE EACH POST",
    f"POST SPACING:  {ft(POST_OC)} O.C. - PER S-1",
    "POSTS:  6x6 ON GALV. STANDOFF BASES",
    "J-BOLTS:  1/2\" x 10\" AT 6'-0\" O.C.",
    "REBAR:  (2) #4 CONTINUOUS",
    "PEN SLAB:  3\" THICK, 10'-0\" OFF THE CONTAINER",
    "WEST WALK:  5'-0\" WIDE x 4\" THICK",
    "EAST SLAB:  6'-6\" WIDE x 4\" THICK",
    "MAX FROST DEPTH ON SITE:  24\"",
    "CONCRETE VOLUME AND REBAR COUNT:  BY BUILDER",
])

s.append('</svg>')
open('/home/claude/gh/S-6-foundation-and-concrete-plan.svg', 'w').write("\n".join(s))

print("SVG written.")
print(f"beam {BEAM_W}x{BEAM_H} in, {BEAM_BELOW} below / {BEAM_ABOVE} above grade")
print(f"beam outboard projection  {BEAM_OUT} in")
print(f"pier stations (in from container face): {[round(v,2) for v in PIER_Y]}")
print(f"pier spacing  {PIER_SPACING} in = {ft(PIER_SPACING)}")
print(f"piers total   {2*(len(PIER_Y)-1)+POSTS}   posts {POSTS} in {BAYS} bays of {ft(POST_OC)}")
print(f"post line     {ft(POST_SPAN)} vs container {ft(WIDTH)} -> {WIDTH-POST_SPAN:.2f} in short")
print(f"J-bolts drawn: {nb}")
print(f"pier depth {PIER_D} vs frost {FROST} -> {PIER_D-FROST} in below frost")
