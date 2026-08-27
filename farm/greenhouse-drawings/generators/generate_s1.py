"""
Generator: S-1 - South Wall Framing Elevation
Rebuilt by TRANSCRIBING the framing geometry out of the superseded sheet
(south-wall-framing-elevation.svg @ 695a375), not by re-authoring it from the
bay table's prose. Every member position below was extracted programmatically
from that file's rect coordinates and converted to real inches, then verified
to repeat identically across all four bays and to mirror exactly about each
bay's centerline.

Changes from the superseded sheet - these four only:
  1. Rafters: 21 tails @ 24" o.c. drawn above the beam, layout per S-5.
     (The old sheet drew no rafters at all.)
  2. True 1/2" = 1'-0" scale (SC = 3.0 px/in). The old sheet was labelled
     1/2" but drawn at 2.85 px/in.
  3. Title block renumbered to DRAWING S-1 under the S-/D- scheme.
  4. Canvas sized off the wall; bay table set to a fixed column width.

Framing content is otherwise identical to the superseded sheet.

NOTE ON THE BAY TABLE: it has a GAP column between "stud against post" and
"king stud". Reading past that column shifts every stud assignment one place
and is what corrupted earlier attempts at this sheet. The gap is real and
carries no member.

Do not hand-edit the SVG - edit this generator and re-run.
"""

from fractions import Fraction as F

# ===============================================================
# GLOBAL GEOMETRY - transcribed, closes on 40'-0"
# ===============================================================
BLDG_LEN   = 480.0
POST_W     = 5.5
BAY_W      = 118.375                       # verified pitch across all 4 bays
POST_INSET = 0.5                           # post/beam face inset from exterior line
post_x0    = [POST_INSET + i * BAY_W for i in range(5)]
post_cls   = [x + POST_W / 2 for x in post_x0]
assert abs(post_x0[-1] + POST_W - (BLDG_LEN - POST_INSET)) < 0.01, "post run does not close"

# --- vertical datum, inches above grade ---
FTG_BOT      = -16.0
GRADE        =   0.0
FTG_TOP      =   6.0
SOLE_TOP     =   7.5
VENT_BOT     =   7.5
VENT_TOP     =  31.5
SILL_TOP     =  38.0        # = window sill
BEAM_BOT     =  72.5        # = window head
BEAM_TOP     =  82.5
ROOF_PLANE   =  92.25

assert BEAM_TOP - BEAM_BOT == 10.0
assert SILL_TOP - VENT_TOP == 6.5
assert VENT_TOP - VENT_BOT == 24.0
assert SOLE_TOP - FTG_TOP == 1.5

FTG_W     = 14.0
SOLE_LO, SOLE_HI = 6.0, 7.5

FULL_HT   = (SOLE_TOP, BEAM_BOT)     # 7 1/2" - 72 1/2", bears on the sole plate
WINDOW_HT = (SILL_TOP, BEAM_BOT)     # 38"    - 72 1/2"
CENTER_HT = (VENT_BOT, SILL_TOP)     # 7 1/2" - 38", backs the sill between vents

# built-up sill, three layers, sits on EACH VENT (48" wide), not on the window
SILL_LAYERS = [(31.5, 33.0), (33.0, 36.5), (36.5, 38.0)]
assert SILL_LAYERS[0][0] == VENT_TOP and SILL_LAYERS[-1][1] == SILL_TOP

# ===============================================================
# BAY PATTERN - transcribed, measured from the bay's LEFT post CL.
# Verified: identical in all 4 bays, and mirrors exactly about BAY_W/2.
# ===============================================================
STUD_AGAINST_POST = (F(11, 4),   F(17, 4))     #  2 3/4  -  4 1/4   FULL
GAP               = (F(17, 4),   F(127, 16))   #  4 1/4  -  7 15/16  (no member)
KING_STUD         = (F(127, 16), F(151, 16))   #  7 15/16-  9 7/16  FULL
TRIMMER_STYLE     = (F(151, 16), F(175, 16))   #  9 7/16 - 10 15/16 WINDOW
TRIMMER           = (F(175, 16), F(199, 16))   # 10 15/16- 12 7/16  WINDOW
VENT_1            = (F(151, 16), F(919, 16))   #  9 7/16 - 57 7/16
CENTER_STUD       = (F(935, 16), F(959, 16))   # 58 7/16 - 59 15/16
VENT_2            = (F(975, 16), F(1743, 16))  # 60 15/16-108 15/16
WINDOW_RO         = (F(199, 16), F(1695, 16))  # 12 7/16 -105 15/16, void

BW = F(BAY_W).limit_denominator(16)
def mirror(pair):
    return (BW - pair[1], BW - pair[0])

assert VENT_1[1] - VENT_1[0] == 48 and VENT_2[1] - VENT_2[0] == 48
assert CENTER_STUD[1] - CENTER_STUD[0] == F(3, 2)
assert WINDOW_RO[1] - WINDOW_RO[0] == F(187, 2)          # 93 1/2"
assert mirror(VENT_1) == VENT_2                          # vents mirror
assert mirror(CENTER_STUD) == CENTER_STUD                # center stud is centered
assert mirror(WINDOW_RO) == WINDOW_RO                    # window is centered
assert TRIMMER[1] == WINDOW_RO[0]                        # trimmer defines the RO edge

# ===============================================================
# RAFTERS - layout identical to S-5
# ===============================================================
RAFTER_SPACING, RAFTER_W = 24.0, 1.5
SIDE_WALL_THK, INBOARD_SETBACK = 5.5, 24.0
mod_xs = [i * RAFTER_SPACING
          for i in range(int(round((BLDG_LEN - INBOARD_SETBACK) / RAFTER_SPACING)) + 1)]
east_rafter = (BLDG_LEN - SIDE_WALL_THK) - RAFTER_W
rafter_xs = mod_xs + [east_rafter]
assert len(rafter_xs) == 21

# ===============================================================
# SHEET
# ===============================================================
SC   = 3.0
PX0  = 340.0
PY0  = 470.0                       # grade line
TCOL = 176.0
TABLE_W = TCOL * 10
CANVAS_W = int(max(PX0 + BLDG_LEN * SC + 200, 40 + TABLE_W + 40))
CANVAS_H = 1010

def X(i): return PX0 + float(i) * SC
def Y(i): return PY0 - float(i) * SC
def f(v): return f"{v:.2f}"

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" viewBox="0 0 {CANVAS_W} {CANVAS_H}">',
     f'<rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>']

def rect(x, y, w, h, sw=1.0, fill="none"):
    s.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{fill}" stroke="#000" stroke-width="{sw}"/>')

def member(x0, x1, lo, hi, sw=1.0, fill="none"):
    rect(X(x0), Y(hi), (float(x1) - float(x0)) * SC, (hi - lo) * SC, sw, fill)

def line(x1, y1, x2, y2, sw=0.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="#000" stroke-width="{sw}"{d}/>')

def text(x, y, t, size=8.0, bold=False, anchor="start"):
    b = ' font-weight="bold"' if bold else ''
    s.append(f'<text x="{f(x)}" y="{f(y)}" font-family="Arial" font-size="{size}"{b} fill="#000" text-anchor="{anchor}">{t}</text>')

# --- FOOTINGS: -16" to +6", mostly below grade ---
for pcl in post_cls:
    member(pcl - FTG_W / 2, pcl + FTG_W / 2, FTG_BOT, FTG_TOP, 1.1)
    fx, fw = X(pcl - FTG_W / 2), FTG_W * SC
    for i in range(7):
        hx = fx + fw * (i + 0.5) / 7
        line(hx, Y(FTG_BOT), hx + (Y(FTG_TOP) - Y(FTG_BOT)) * 0.55, Y(FTG_TOP), 0.35)

# --- GRADE ---
line(X(0) - 45, Y(GRADE), X(BLDG_LEN) + 45, Y(GRADE), 1.7)

# --- SOLE PLATE: continuous, full 40'-0" ---
member(0, BLDG_LEN, SOLE_LO, SOLE_HI, 1.2)

# --- RAFTER TAILS ---
for xv in rafter_xs:
    member(xv, xv + RAFTER_W, BEAM_TOP, ROOF_PLANE, 1.0)
RAFTER_NOTE_Y = Y(ROOF_PLANE) - 16

# --- BEAM ---
member(POST_INSET, BLDG_LEN - POST_INSET, BEAM_BOT, BEAM_TOP, 1.8)
for pcl in post_cls:                       # post bearing behind the beam
    member(pcl - 2.225, pcl + 2.225, 74.08, 81.80, 0.7)

# --- POSTS ---
for i, x0 in enumerate(post_x0, start=1):
    member(x0, x0 + POST_W, FTG_TOP, BEAM_BOT, 1.7)
    text(X(x0 + POST_W / 2), Y(BEAM_BOT) + 22, f"POST {i}", 8.5, True, "middle")
    text(X(x0 + POST_W / 2), Y(BEAM_BOT) + 32, "6x6", 7.5, False, "middle")

# --- PER-BAY FRAMING, transcribed pattern + verified mirror ---
for b in range(4):
    base = post_cls[b]
    for pair in (STUD_AGAINST_POST, KING_STUD):
        member(base + pair[0], base + pair[1], *FULL_HT, 1.0)
        m = mirror(pair)
        member(base + m[0], base + m[1], *FULL_HT, 1.0)
    for pair in (TRIMMER_STYLE, TRIMMER):
        member(base + pair[0], base + pair[1], *WINDOW_HT, 1.0)
        m = mirror(pair)
        member(base + m[0], base + m[1], *WINDOW_HT, 1.0)
    member(base + CENTER_STUD[0], base + CENTER_STUD[1], *CENTER_HT, 1.0)

    for v in (VENT_1, VENT_2):
        member(base + v[0], base + v[1], VENT_BOT, VENT_TOP, 0.9)
        for lo, hi in SILL_LAYERS:
            member(base + v[0], base + v[1], lo, hi, 0.9 if hi - lo > 2 else 1.0)

    text(X(base + BW / 2), Y((VENT_BOT + VENT_TOP) / 2) + 3,
         '4\'-0" x 2\'-0" VENT R.O. (TYP)', 7.5, False, "middle")
    text(X(base + BW / 2), Y(34.6), "SILL: 2x6 / 2x4 O.E. / 2x6", 7.0, False, "middle")
    text(X(base + BW / 2), Y((SILL_TOP + BEAM_BOT) / 2),
         '93 1/2" x 34 1/2" R.O.', 9.0, False, "middle")

# --- BEAM NOTES ---
# beam + rafter notes are placed ABOVE the rafter band, clear of the members
text(X(BLDG_LEN / 2), RAFTER_NOTE_Y,
     '(21) 2x12 RAFTER TAILS @ 24" O.C. - LAYOUT PER S-5', 8.5, True, "middle")
text(X(BLDG_LEN / 2), RAFTER_NOTE_Y - 11,
     'BEAM: 6x10 R/S DOUG FIR CONTINUOUS - 39\'-11" (ENDS 1/2" INSIDE EXTERIOR LINE) - SPLICE OVER CENTER POST (TYP)',
     8.0, False, "middle")

# ===============================================================
# DIMENSION STRINGS
# ===============================================================
D1 = Y(ROOF_PLANE) - 76
line(X(0), D1, X(BLDG_LEN), D1, 0.9)
for m in (0, BLDG_LEN):
    line(X(m), D1 - 5, X(m), D1 + 5, 0.9)
text(X(BLDG_LEN / 2), D1 - 8, '40\'-0"  OVERALL (FINISHED EXTERIOR)', 13, True, "middle")

D2 = D1 + 28
marks = [0.0] + post_cls + [BLDG_LEN]
for m in marks:
    line(X(m), D2 - 5, X(m), D2 + 5, 0.8)
for a, b in zip(marks[:-1], marks[1:]):
    line(X(a), D2, X(b), D2, 0.8)
    lbl = '3 1/4"' if (a == 0 or b == BLDG_LEN) else '9\'-10 3/8"'
    text(X((a + b) / 2), D2 - 7, lbl, 8.0, False, "middle")
text(X(post_cls[0]), D2 + 14, "CL", 7.0, False, "middle")

# --- LEFT HEIGHT CHAIN ---
LX = X(0) - 92
line(LX, Y(FTG_BOT), LX, Y(ROOF_PLANE), 0.7)
# SOLE_TOP / FTG_TOP / GRADE sit 1 1/2" apart in real terms, which collides at
# 1/2" scale - those three get stepped leaders out to clear label rows.
for yv, lab, sub, drop in [
    (ROOF_PLANE, '7\'-8 1/4"', "ROOF PLANE AT THIS WALL", 0),
    (BEAM_TOP,   '6\'-10 1/2"', "BEAM TOP", 0),
    (BEAM_BOT,   '6\'-0 1/2"', "BEAM UNDERSIDE / WINDOW HEAD", 0),
    (SILL_TOP,   '3\'-2"', "WINDOW SILL", 0),
    (VENT_TOP,   '2\'-7 1/2"', "VENT OPENING TOP", 0),
    (SOLE_TOP,   '0\'-7 1/2"', "SOLE PLATE TOP / VENT BOTTOM", -26),
    (FTG_TOP,    '0\'-6"', "FOOTING TOP", 4),
    (GRADE,      '0\'-0"', "GRADE", 34),
    (FTG_BOT,    '-1\'-4"', "FOOTING BOTTOM", 0),
]:
    yy = Y(yv)
    line(LX - 5, yy, LX + 5, yy, 0.7)
    ty = yy + drop
    if drop:
        line(LX - 5, yy, LX - 22, ty, 0.4)
        line(LX - 22, ty, LX - 30, ty, 0.4)
        tx = LX - 34
    else:
        tx = LX - 9
    text(tx, ty - 2, lab, 9.0, True, "end")
    text(tx, ty + 8, sub, 7.5, False, "end")

# ===============================================================
# TITLE BLOCK + NOTES
# ===============================================================
TB = Y(FTG_BOT) + 46
text(40, TB, "SOUTH WALL FRAMING ELEVATION", 17, True)
text(40, TB + 18, "EXTERIOR VIEW - LOOKING NORTH", 12)
text(40, TB + 34, 'SCALE:  1/2" = 1\'-0"          DRAWING S-1', 12)

BY = TB + 48
BH = 132
BWid = (TABLE_W - 40) / 3

def notebox(x0, title, items):
    rect(x0, BY, BWid, BH, 0.8)
    text(x0 + 8, BY + 15, title, 9.5, True)
    for i, t in enumerate(items):
        text(x0 + 10, BY + 28 + i * 11.6, t, 8.0)

notebox(40, "GENERAL NOTES", [
    '1. GRADE = 0\'-0"  |  FTG TOP = 0\'-6"  |  FTG BOTTOM = -1\'-4".',
    "2. POST-AND-BEAM - WALL IS INFILL ONLY, NON-BEARING.",
    "3. PROVIDE APPROVED HOLD-DOWNS AT ALL POSTS.",
    "4. WINDOW / VENT R.O.s SHOWN, UNITS NOT.",
    "5. BAY FRAMING IS SYMMETRIC ABOUT THE BAY CENTERLINE",
    "   AND IDENTICAL IN ALL 4 BAYS - SEE TABLE BELOW.",
    "6. SEE S-5 FOR RAFTER LAYOUT AND SPACING.",
    "7. NO ENGINEERED LUMBER.",
    "8. SEE FOUND. PLAN FOR FOOTING SIZE.",
])
notebox(40 + BWid + 20, "FRAMING NOTES", [
    "1. LUMBER: D.FIR / SPF No. 2 OR BETTER.",
    "2. NO HEADERS - BEAM SERVES AS HEADER.",
    '3. SOLE PLATE 2x6 PT, CONTINUOUS FULL 40\'-0".',
    "4. ALL STUDS 2x6 (U.N.O.).",
    "5. BUILT-UP SILL OVER EACH VENT:",
    "   2x6 FLAT / 2x4 ON EDGE / 2x6 FLAT.",
    "6. CENTER STUD SHARED BETWEEN THE TWO VENTS,",
    "   RUNS UP TO THE SILL.",
    '7. RAFTERS 2x12 @ 24" O.C. - SEE S-5.',
])
notebox(40 + 2 * (BWid + 20), "MATERIAL SCHEDULE", [
    "POSTS:  (5) 6x6 ROUGH-SAWN",
    "BEAM:  6x10 R/S CONTINUOUS",
    'RAFTERS:  (21) 2x12 @ 24" O.C.',
    "SOLE PLATE:  2x6 PT",
    "STUDS / KINGS / TRIMMERS:  2x6",
    "BUILT-UP SILL:  2x6 / 2x4 O.E. / 2x6",
    'GLAZING:  (4) 93 1/2" x 34 1/2" COMMERCIAL',
    'VENTS:  (8) 4\'-0" x 2\'-0" WAX-ACT.',
])

# ===============================================================
# BAY LAYOUT TABLE - all ten columns, GAP included
# ===============================================================
TY = BY + BH + 22
text(40, TY, "BAY LAYOUT - DIMENSIONS FROM EACH BAY'S LEFT POST CENTERLINE - TYP. ALL 4 BAYS, MIRRORED ABOUT BAY CL", 9.5, True)
cols = [
    ("BAY WIDTH\n(POST CL-CL)",        '118 3/8"\n(9\'-10 3/8")'),
    ("STUD AGAINST\nPOST (FULL HT)",   '2 3/4" to\n4 1/4"'),
    ("GAP\n(NO MEMBER)",               '4 1/4" to\n7 15/16"'),
    ("KING STUD\n(FULL HT)",           '7 15/16" to\n9 7/16"'),
    ("TRIMMER-STYLE\nSTUD (WDW HT)",   '9 7/16" to\n10 15/16"'),
    ("TRIMMER\n(WDW HT)",              '10 15/16" to\n12 7/16"'),
    ("WINDOW R.O.\n(CLEAR WIDTH)",     '93 1/2"\n(12 7/16" to\n105 15/16")'),
    ("VENT 1\n(CLEAR WIDTH)",          '48"\n(9 7/16" to\n57 7/16")'),
    ("CENTER STUD\n1 1/2" + '"' + " WIDE",  '58 7/16" to\n59 15/16"'),
    ("VENT 2\n(CLEAR WIDTH)",          '48"\n(60 15/16" to\n108 15/16")'),
]
TH = 104
rect(40, TY + 10, TABLE_W, TH, 0.8)
line(40, TY + 38, 40 + TABLE_W, TY + 38, 0.6)
for i, (hdr, val) in enumerate(cols):
    cx = 40 + i * TCOL
    if i:
        line(cx, TY + 10, cx, TY + 10 + TH, 0.5)
    for j, ln in enumerate(hdr.split("\n")):
        text(cx + TCOL / 2, TY + 22 + j * 10, ln, 7.2, True, "middle")
    for j, ln in enumerate(val.split("\n")):
        text(cx + TCOL / 2, TY + 56 + j * 12, ln, 8.5, False, "middle")

s.append('</svg>')
open('/home/claude/greenhouse/S-1-south-wall-framing-elevation.svg', 'w').write("\n".join(s))

full = 4 * 4
wdw  = 4 * 4
print("SVG written.")
print(f"canvas {CANVAS_W}x{CANVAS_H}")
print(f"posts {len(post_x0)}  rafters {len(rafter_xs)}  full-ht studs {full}  window-ht studs {wdw}")
print(f"center studs 4   vents 8   sill layers {4*2*3}   sole plate 1 @ {BLDG_LEN}\"")
print(f"post CLs: {[round(c,3) for c in post_cls]}")
