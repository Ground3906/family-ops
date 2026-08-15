# Greenhouse Render Prompts

**Purpose:** working image-generation prompts for the greenhouse design in `farm/greenhouse-design-sheet.md`. Tested against Gemini 2026-08-14. Reusable base text - change one element at a time rather than rewriting.

**Geometry these describe:** 18 ft 6 in deep x 40 ft, single-slope shed, 20 deg pitch, peak 14 ft 6 in, south wall 7 ft 9 in, container north wall at 9 ft 6 in (five feet lower than the peak).

---

## LESSONS LEARNED (read before prompting)

These took eleven attempts to work out. They are the real value of this file.

1. **Never say "peak" or "ridge."** The model builds a gable every time. Say "single flat sloping roof plane, like a ramp." Say explicitly: no ridge, no second slope, no peak of any kind.

2. **Never say "two separate structures."** It renders two images side by side. Say "one continuous structure, single image."

3. **Edit-mode gets anchored.** After two or three modification passes the model stops moving and returns the same image. Start a NEW conversation and describe the object whole rather than sending a correction list. Correction lists make it preserve what it already has.

4. **Describe the object, not the fix.** A list of corrections reads as "keep everything and adjust." A full description of the finished thing reads as "build this."

5. **State height relationships in plain comparisons.** "The container is FIVE FEET SHORTER than the roof peak" works. Giving two dimensions and expecting it to subtract does not.

6. **Do not say "the container is the tallest element"** unless it is. Said once as an overcorrection and the model lifted the entire container off the ground.

7. **Pin the camera explicitly for end views.** "Camera is positioned due EAST looking WEST at the short end wall, long axis running away from the camera." Without this it swings around and shows the long side.

8. **State proportions as ratios.** "The container must appear MORE THAN TWICE AS LONG as the end wall is wide." Feet alone get ignored.

9. **Mirroring is faster in a photo app** than asking the model to flip. It rebuilds the whole scene and loses the geometry.

10. **Say "single undivided pane"** or every window comes back with mullions.

11. **Count out loud.** "Exactly EIGHT panels, not sixteen." It defaults to filling space.

---

## PROMPT 1 - SOUTH EXTERIOR (primary view)

Best result of the session. Two-step: base prompt, then one modification.

**Step 1:**

```
Architectural photograph, Colorado meadow, mountains behind,
golden hour, viewed from the south, front right corner.

TWO SEPARATE STRUCTURES BUTTED TOGETHER.

STRUCTURE ONE, in front, is a lean-to greenhouse with a single
flat sloping roof plane. Its back wall is a tall flat vertical
white corrugated metal wall, 40 feet long and 14 feet 6 inches
tall, top edge a clean horizontal line. Nothing sits on top of
it. The roof is a single flat rectangular plane tilting down
toward the camera at 20 degrees over 18 feet, no ridge, no
peak, no second slope. Upper half red corrugated metal, lower
half clear translucent polycarbonate, one straight seam
between them.

Its front wall is 7 feet 9 inches tall, 40 feet long, white
corrugated metal, four bays divided by exposed natural timber
6x6 posts under a heavy timber beam. Each bay has one wide
horizontal window, 7 feet 8 inches across, single undivided
pane, black frame. Eight white awning panels along the base,
two per bay, hinged at top, propped open outward. No door on
this wall.

Its west end wall at far left is a right triangle following
the roof slope, with a solid white man door near the tall back
corner.

STRUCTURE TWO, directly behind it, is a white 40-foot shipping
container standing on the ground, its long ribbed side pressed
flat against the back wall of the greenhouse. Same 40-foot
length, perfectly aligned end to end.

HEIGHT RELATIONSHIP, CRITICAL: the shipping container is
FIVE FEET SHORTER than the greenhouse's tall back wall. The
container's roof is only 9 feet 6 inches high; the greenhouse
back wall is 14 feet 6 inches high. From this angle the
container is almost entirely hidden behind the greenhouse.
Only its far end and cargo doors are visible at the extreme
left edge of the frame, a short white box clearly lower than
the greenhouse.

Concrete footing 6 inches above bare dirt. Photorealistic,
wide shot.
```

**Step 2 (the container will render offset with a gap - this fixes it):**

```
Modify: the white shipping container must be moved so its long
side is pressed FLAT AGAINST the back wall of the greenhouse
with NO GAP and NO SPACE between them. The two structures
touch along their entire 40-foot length and their ends line up
exactly. The container sits directly behind the greenhouse,
not beside it and not offset to the left. Because the
container is 5 feet shorter than the greenhouse back wall,
only the container's far end and cargo doors peek out at the
extreme left edge of the frame, tight against the greenhouse
corner.

Keep everything else identical: single flat sloping roof plane
with no ridge, red upper half and clear polycarbonate lower
half, four timber bays with wide single-pane windows, eight
white awning intake panels along the base, white man door on
the left end wall, concrete footing, mountain setting.
```

---

## PROMPT 2 - NORTH EXTERIOR (container broadside, exhaust vents)

Worked first try once "two separate structures" was removed.

```
Architectural photograph of the back of a farm building.
Colorado meadow, mountains behind, golden hour. Single image,
one continuous structure, viewed from the north at a slight
angle from the right.

In the foreground, filling the width of the frame, is the long
white ribbed side of a 40-foot shipping container. It is 9
feet 6 inches tall with a flat roof deck. Its cargo doors are
at the far right end.

Rising directly behind the container, slightly set back, is a
5-foot-tall white corrugated metal wall running the same full
40-foot length. Eight large white awning vent panels are set
into this wall, evenly spaced, each 4 feet wide and 2 feet
tall, hinged along their top edges and propped open outward
toward the camera.

Above and behind that wall, only the topmost edge of a red
corrugated metal roof is visible, sloping away from the
viewer. The rest of the building is hidden on the far side.

Bare dirt ground. Photorealistic, wide shot, one image.
```

---

## PROMPT 3 - EAST END WALL (door and stacked glazing)

Hardest view. The narrow face is the subject and the model fights it. This version pins the camera and the long axis explicitly.

```
Architectural photograph, Colorado meadow, mountains, golden
hour. Single image.

Camera is positioned due EAST of a long narrow farm building,
looking WEST directly at its short end wall. The building's
long axis runs AWAY from the camera into the distance.

THE END WALL FACING THE CAMERA IS NARROW: only 18 feet 6
inches wide. It is a right triangle, 14 feet 6 inches tall at
its RIGHT edge, sloping down to 7 feet 9 inches at its LEFT
edge. White corrugated metal.

Grouped against the TALL RIGHT corner: a full-glass door at
ground level, a tall narrow window immediately to its left,
and a wide horizontal window spanning above both. Black
frames, single panes.

THE BUILDING RUNS 40 FEET AWAY FROM THE CAMERA, so its long
south side is seen in steep perspective receding to the LEFT,
showing exposed timber posts and small white awning panels
along its base, foreshortened by distance.

A white 40-foot shipping container sits immediately behind
the building, hidden from this angle except for its end,
which is flush with the end wall and 5 feet lower.

Single flat sloping roof, red at the high edge, clear
polycarbonate at the low edge. Concrete footing.
Photorealistic.
```

---

## PROMPT 4 - INTERIOR (drafted, not yet rendered)

Open to the rafters, no ceiling plane. All interior surfaces white (Snow Coat over closed cell foam).

```
Interior of a shed-roof greenhouse, open to the rafters, no
ceiling. Exposed 2x12 wood rafters run down-slope every 16
inches from 14 feet 6 inches at the far white container wall
to 7 feet 9 inches at the near glazed wall. All surfaces
between and behind the rafters are coated bright white.

Right side: four wide horizontal windows set in heavy exposed
timber post and beam framing, a massive 6x12 timber beam
overhead, low winter sunlight streaming through at a sharp
angle and landing on the floor 8 to 13 feet inboard.

Overhead: the near half of the roof is translucent multiwall
polycarbonate on exposed wood purlins, glowing with diffuse
light between the rafters. The far half is solid white-coated
insulated deck.

Left third against the white container wall: livestock pens
with metal panel gating on a concrete slab. Remaining floor is
dirt with waist-high raised growing beds in the sunlit strip.

Warm, bright, agricultural, photorealistic.
```

---

## VARIANTS TO BUILD LATER

- **West end wall view** - solid triangular wall, no glass, insulated man door near the tall north corner.
- **Phase 1 all-metal roof** - same prompts, replace the polycarbonate lower half with red corrugated metal across the full slope. This is what actually gets built first.
- **Winter light study** - south exterior with snow on the ground and low sun.
