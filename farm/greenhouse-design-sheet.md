# Greenhouse Design Sheet

**Agent:** Rootstock (definition not yet committed)
**Site:** 38.0979386, -105.2994594 - 1722 Edelweiss Dr, Westcliffe CO, 9,000 ft, zone 4a
**Status:** Design in progress. Nothing built. Nothing ordered.
**Design sessions:** 2026-08-13, 2026-08-14, 2026-08-15, 2026-08-18 (drawing/scope session - framing geometry corrected, roof and vent assemblies re-locked), 2026-08-24 (sill rebuild - built-up sill locked, south wall and west wall framing elevations drawn and committed, fixed pane window logged to glazing inventory), 2026-08-25 (north wall - design sheet body recovered after a truncated write, rafter-above-notch error corrected, south sill dropped to hold the roof plane, N-1 drawn, S-1 corrected), 2026-08-26 (roof framing - rafters relocked at 24 in o.c. on an engineered snow load, R-3 and R-4 and R-6 drawn, R-2 regenerated, wedge geometry corrected, drawing numbering collision found)

---

## MISSION

Four-season cold-hardy greenhouse. Never freezes inside. Greens, roots, brassicas through a Westcliffe winter. Produces into Chow Hall in the months when nothing else does.

**Two-phase build.** Phase 1: livestock barn, roughly two years, absorbing the garage-barn conversion program. Phase 2: vacate animals, convert to greenhouse with structure already standing.

---

## SITE

Built-up fill platform, roughly 6 ft proud of surrounding grade. **Building sits on grade on all four sides.** Ground is higher to the east; fill falls away quickly to the south and west beyond the footprint. No wall is buried. No retaining condition anywhere in the building.

Wheel-packed in lifts with the Gehl approximately 2023, three freeze-thaw cycles since. Not a tested Proctor number.

Power and water already on site. Gas reaches easily.

No shading. Confirmed by owner observation. No county building code jurisdiction.

**Ground snow load: 50 psf.** Westcliffe town rating, confirmed by Matt.

**Design roof snow load: approximately 24 psf.** Derived 2026-08-26 when the rafter spacing was reworked. The 50 psf ground figure taken straight into a prescriptive span table makes the roof look impossible; the roof does not hold ground snow, and the reduction is real:

| Factor | Value | Basis |
|---|---|---|
| Flat roof factor | 0.7 | standard |
| Exposure, Ce | 0.9 | **ASSUMED** - fully exposed terrain, no shading. Not read off a site document |
| Thermal, Ct | 1.0 | heated structure. The 0.85 greenhouse credit needs an attendant or a temperature alarm; neither exists, so it is not claimed |
| Importance, Is | 1.0 | **ASSUMED** - ordinary agricultural risk category |
| Slope, Cs | 0.761 | slippery, unobstructed, heated roof at 20.556 deg |

0.7 x 0.9 x 1.0 x 1.0 x 0.761 x 50 = **23.96 psf.**

Checked against NDS reference values for Douglas fir-larch No.2 2x12 (Fb 900 psi, E 1,600,000 psi, CD 1.15 snow, Cr 1.15 repetitive), bending governs over deflection at every spacing considered:

| Spacing | Allowable span | Margin over the 18 ft 4-1/2 in required |
|---|---|---|
| 16 in o.c. | 23 ft 7 in | +62 in |
| 19.2 in o.c. | 21 ft 6 in | +37 in |
| **24 in o.c.** | **19 ft 3 in** | **+10 in** |

19.2 in o.c. was rejected on panel alignment, not strength: 48 in poly does not divide evenly by 19.2, so panel joints land mid-bay with nothing to screw the H-profile base into.

**This is arithmetic, not a stamped calculation, and there is no county building code jurisdiction to check it.** The two assumed factors above are the exposure of the whole result. Both are the standard values for these conditions, and the 24 in margin is not knife-edge, but they were chosen rather than sourced.

**Slab pitch:** finished floor falls away from the container at 1/8 in per foot. Level dirt beyond the footprint.

**Solar geometry at this latitude, true solar noon:**

| Season | Sun altitude |
|--------|--------------|
| Winter solstice | 28.5 deg |
| Equinox | 51.9 deg |
| Summer solstice | 75.3 deg |

Winter shadow length is 1.84x object height. Design accepts off-angle glazing loss, which is cosine loss only and small across the practical pitch range.

---

## THE CONTAINER (fixed, non-negotiable)

40 ft high cube, forms the **north wall**. Runs east to west. Cargo doors at the west end. Interior height 9 ft 6 in. **Top of container above finished grade: 8 ft 10 in** - measured, not assumed. This is the datum every height in this document is built from. Exterior already white, already insulated.

Divided in thirds, roughly 13 ft 4 in per bay:

| Bay | Use | Status |
|-----|-----|--------|
| West | Feed room | Fixed. Insulated 2 in rigid foam, walls and ceiling. Receives greenhouse supply air (see Ventilation) |
| Center | Chicken coop | Fixed. Insulated 2 in rigid foam, walls and ceiling. Receives greenhouse makeup air via existing window (Item 5) |
| East | Tool room | Becomes greenhouse-centric tool storage. Receives greenhouse supply air (see Ventilation) |

**Openings in the south face (into the greenhouse):**

- Feed bay: man door, exists. Cat door with flapper, exists - doubles as relief path for new supply fan (not airtight, functions as intended)
- Coop bay: 20 in x 30 in window, exists - primary makeup-air intake per Item 5
- Tool bay: man door, future

Container sits on dirt. Any excavation along its south face risks undermining corner-casting bearing. Bird run is handled outside this design.

---

## FRAMING GEOMETRY - RAFTER AND RISER

**Locked 2026-08-18. Supersedes the birdsmouth-both-ends framing in the original Locked Geometry table below. This section governs; the table further down carries forward only the dimensions it doesn't touch.**

**The core correction:** the original design assumed birdsmouths at both rafter ends, consuming stock past the bearing heels. Reworked as a raked (beveled) bearing plate at the riser and a birdsmouth only at the beam. This is a real geometry change, not a drafting note - it moves the peak, the riser height, and every wall dimension that references them.

### Rafter stock and cut geometry

| | |
|---|---|
| Rafter member | 2x12 dimensional lumber, Douglas fir-larch No.2 (11-1/4 in actual depth) |
| Stock length, exact | 240 in (20 ft) |
| Spacing | 24 in o.c. |
| Count | 21 (20 pulled from the west at 24 in o.c., plus one east rafter set inboard of the east wall inner face) |
| Cuts | Plumb cut both ends, parallel to each other (not birdsmouth-to-birdsmouth) |

**North end (riser):** raked cap plate, beveled to 4.5:12. Rafter bottom face bears full-width on the raked plate, full 11-1/4 in depth intact, zero notch. Plumb cut flush at the riser's outside framing face.

**South end (beam):** birdsmouth notch, seat cut to the beam's full 6 in width (rough-sawn). Notch depth 2-1/4 in plumb, 2-1/8 in perpendicular to the rafter. Remaining rafter depth 9-1/8 in, clears the 2/3-depth minimum (7-1/2 in) with margin. Plumb cut flush at the beam's south face.

**Parallel-cut geometry:** because both plumb cuts are parallel (not birdsmouth-to-birdsmouth), the rafter is a parallelogram in elevation, not a rectangle. The stock arrives with square ends, cut perpendicular to its length, so each plumb cut takes a wedge off that square end. Measured along the edge the wedge is 11-1/4 in x tan(20.556 deg) = 4-7/32 in. It comes off the TOP edge at the south end and off the BOTTOM edge at the north end, because the square end passes through the top corner there. The top edge therefore loses stock only once, at the south. The top edge and bottom edge are each 240 in long but offset from each other; they are not both usable as the "rake" dimension.

**Usable rake (roof coverage dimension):** 235-1/2 in (19 ft 7-1/2 in), plane to plane, north framing face to south framing face. This is 240 in stock less the 4-7/32 in wedge consumed at the SOUTH plumb cut, leaving 235-25/32 in of usable top edge against a 235-1/2 in requirement - about 1/4 in of slack. **Corrected 2026-08-26:** the sheet previously carried 4-1/2 in at the north end, which put the wedge at the wrong end and overstated it. The old figure was the conservative one, so nothing built to it is short. This is the number the roof panels are ordered and cut against - see Roof section.

**Trig, locked:** pitch 4.5:12 = 20.556 deg. cos = 0.93633, sin = 0.35112, tan = 0.375.

| | |
|---|---|
| Rake (usable) | 235-1/2 in (19 ft 7-1/2 in) |
| Horizontal run | 220-1/2 in (18 ft 4-1/2 in) |
| Vertical rise | 82-3/4 in (6 ft 10-3/4 in) |

This reconciles with the original design's 18 ft 5 in depth and 6 ft 11 in roof fall to within half an inch - confirms the geometry, does not change the footprint. **Footprint stays 736 sq ft.**

### Riser and peak height (RERUN 2026-08-25)

| | Above grade |
|---|---|
| Footing top | 6 in |
| Footing top to sill line | 2 ft 8 in |
| **South sill** | **3 ft 2 in** |
| Window RO | + 2 ft 10-1/2 in |
| Window head, at beam underside (no header - see South Wall) | 6 ft 0-1/2 in |
| Beam depth (rough-sawn 6x10) | + 10 in |
| Beam top | 6 ft 10-1/2 in |
| Rafter above notch (12 in plumb - 2-1/4 in) | + 9-3/4 in |
| **Roof plane at south wall** | **7 ft 8-1/4 in** |
| Rise over the rake | + 6 ft 10-3/4 in |
| **Peak (rafter top edge at riser)** | **14 ft 7 in** |
| Less rafter plumb depth (sits on raked cap, no notch) | - 12 in |
| Top of riser cap plate | 13 ft 7 in |
| Less container top (fixed) | - 8 ft 10 in |
| **Riser framing (bottom plate to cap plate)** | **4 ft 9 in** |
| **Total riser + rafter above container top** | **5 ft 9 in** |

**Two errors found and closed 2026-08-25. Open Item 19 closed.**

**Error 1 - rafter above notch.** The row read `10 in - 2-1/4 in = 7-3/4 in`. The 10 in is the depth of the 6x10 **beam**. The member a notch reduces is the **rafter**, whose plumb depth at 4.5:12 is **12 in** (11-1/4 in actual over cos 20.556 deg = 12.015), which this sheet already states in the rafter cut geometry above. Correct figure is `12 - 2-1/4 = 9-3/4 in`, and it cross-checks against the 9-1/8 in remaining perpendicular depth stated in the same section (9-1/8 / 0.93633 = 9.75). Most likely introduced 2026-08-18 when the beam went 6x12 to 6x10 and a twelve got changed to a ten on a row that was never a beam row.

**Error 2 - window rough opening on S-1.** The drawing put the head 34 in above the sill. The rough opening is 34-1/2 in. Half an inch of window that did not fit.

**Resolution - the sill came down, the roof did not go up.** Together those two errors were pushing the roof plane, peak and riser 2-1/2 in higher. Owner's call was to absorb the whole 2-1/2 in at the sill instead: **south sill 3 ft 4-1/2 in to 3 ft 2 in.** The roof plane holds at 7 ft 8-1/4 in and the peak at 14 ft 7 in, which are the figures S-1, W-1 and E-1 were already drawn to. **W-1 and E-1 required no change at all.** S-1's stack from the beam down was redrawn; N-1 was rerun. The drawing set and this sheet now agree end to end.

**Supersedes:** original 5 ft 8 in riser and 14 ft 6 in peak. New peak is 3 in lower; new riser is 1 ft 6-1/2 in shorter. Both results of dropping the south sill from 4 ft 2 in to 3 ft 0 in and removing the header/doubled-plate stack under the south windows (see South Wall). Sill has since moved again to 3 ft 4-1/2 in (2026-08-24) - this paragraph describes the 4 ft 2 in to 3 ft 0 in transition only and is otherwise historical.

---

## SOUTH WALL

**Sill dropped to 3 ft 0 in, then locked at 3 ft 4-1/2 in above grade** (was 4 ft 2 in), owner's explicit target to reduce riser height. Then dropped again to 3 ft 2 in on 2026-08-25 to absorb the rafter-above-notch and window-RO corrections without moving the roof - see Framing Geometry.

**Sill construction: built-up, not solid. Locked 2026-08-24.** 2x6 flat cap / 2x4 on edge / 2x6 flat bottom cap, 6-1/2 in tall overall. A single 2x6-on-edge was tried and rejected - no bearing.

**Window head: flange lands directly on the beam underside. No header, no doubled top plate.** The south wall is non-bearing infill between posts - the header was never structural, and removing it plus the doubled plate took 8-1/2 in out of the riser stack in exchange for a trim detail: the window flange lands on a rough-sawn timber face rather than a flat framed nailer, so head casing will need to scribe to the beam. Accepted trade.

**Framing plane:** beam south face is the framing reference. All wall framing - posts, studs, sill plate - sets flush to that same plane. **Posts and beam are fully clad, no exposed timber on the south face** - UV and weathering exposure on rough-sawn Doug fir/larch at 9,000 ft is not worth the maintenance. Sheathing runs up over the beam face and continues up to cover the rafter's south plumb-cut end (full 9-1/8 in remaining depth after the notch), so the wall plane is continuous from footing to roof edge with no gap at the rafter line. See Detail D-2 for the wall-head/roof-edge assembly.

**Wall buildup outboard of the framing face:** approx 7/16 in OSB sheathing + approx 1/4 in flat-cut (rib-ripped) Pro-Panel = **approx 3/4 in total.** This buildup is identical at the north (riser) wall - see Roof section for how it factors into overhang measurements.

**South wall depth, container face to beam south face: 18 ft 4-1/2 in** (was stated 18 ft 5 in - reconciles to within half an inch, no footprint change).

---

## LOCKED GEOMETRY (legacy table - see Framing Geometry and South Wall above for superseding figures)

**Locked 2026-08-14/15. The rows below marked SUPERSEDED are carried for history; use the Framing Geometry and South Wall sections above for current numbers.**

| Element | Dimension | Status |
|---------|-----------|--------|
| Container top above grade | **8 ft 10 in** (measured) | current |
| Roof pitch | **4.5:12 (20.6 deg)** | current |
| Riser above container | ~~5 ft 8 in~~, ~~4 ft 5 in~~ | SUPERSEDED - now 4 ft 9 in (see Framing Geometry) |
| Peak above grade at the container | ~~14 ft 6 in~~, ~~14 ft 3 in~~ | SUPERSEDED - now 14 ft 7 in |
| Slope length | ~~19 ft 8 in~~ | SUPERSEDED - now 19 ft 7-1/2 in (rake), see Framing Geometry |
| Depth | 18 ft 5 in | current (reconciles to 18 ft 4-1/2 in) |
| Roof fall over the depth | 6 ft 11 in | current (reconciles to 6 ft 10-3/4 in) |
| Footing top | 6 in proud of finished grade | current |
| Slab fall, container to south wall, 1/8 in per ft | 2.3 in over the run | current |
| Beam bearing above floor at the south wall | ~~7 ft 9 in~~ | SUPERSEDED - beam now 6x10, sill dropped, see South Wall/Framing Geometry |
| Doubled top plate (south) | ~~3 in~~ | SUPERSEDED - no header/plate at south windows, see South Wall |
| Racked 2x6 header, on edge | ~~5.5 in~~ | SUPERSEDED - no header at south windows |
| South window head | ~~7 ft 1 in~~ | SUPERSEDED - now 6 ft 0-1/2 in, rerun 2026-08-25 |
| South window rough opening, vertical | 34.5 in (frame + 1/2 in shim per side) | current |
| South window sill | ~~4 ft 2 in~~, ~~3 ft 0 in~~, ~~3 ft 4-1/2 in~~ | SUPERSEDED - now 3 ft 2 in, built-up sill, locked 2026-08-25 |
| Framing below south sill (above footing) | ~~3 ft 8 in~~, ~~2 ft 6 in~~ | SUPERSEDED - now 2 ft 8 in, rerun 2026-08-25 |
| Pen ceiling at 10 ft line | 10 ft 9 in | STALE - not recalculated against new peak, open item |
| Footprint | 18 ft 5 in x 40 ft = 736 sq ft | current |

**Ceiling height by distance south of the container - STALE, not recalculated against the 14 ft 7 in peak. Open item.**

---

## LOCKED ITEMS

### Item 2 - Use
Four-season, cold-hardy. Never freezes inside. Passive solar carrying the load, mechanical heat as insurance, with powered ventilation as a third layer (see Ventilation).

### Item 3 - Footprint
18 ft 5 in x 40 ft, 736 sq ft. Container is the north wall. Building runs south off the container's full 40 ft face.

### Item 4 - Container layout
As above. Fixed and closed to design.

### Item 5 - Coop / greenhouse air relationship
Wall stays sealed and insulated. **One-way air path: greenhouse to coop.** Coop's existing exhaust fan draws makeup air through the existing 20 in x 30 in window instead of cold outdoor air. Coop stays negative pressure relative to the greenhouse. Separation enforced by pressure gradient, not filtration. No new hardware. **Unchanged and reconfirmed 2026-08-18** - this is intentional heat transfer into the coop, not incidental leakage. See Ventilation for the feed-room and tool-room extension of this same principle.

**5.1 locked:** greenhouse window is primary intake. Exterior coop windows retained as functional backup.

### Item 6 - Structure geometry
**Single-slope shed, 4.5:12.** Framed riser built up off the container top, sloping down south. Peak sits over the north wall against insulated mass, not under glass. Pitch and rake are fixed as of 2026-08-18 - see Framing Geometry.

### Item 7 - Floor
No floor drop. Building sits on the pad as-is, with a 1/8 in per ft fall away from the container. Earth-tempering does not apply - the fill berm is not stable coupled ground.

**Slab under the pens only. Individual pens. Dirt on the remainder.** Animals locked in pens at all times. Pen slabs poured separately and later, independent of the structural foundation.

### Item 8 - Foundation
**NO STEM WALL.** Monolithic perimeter footing with post piers cast integral, one continuous pour, top 6 in proud of finished grade.

| Element | Spec |
|---------|------|
| Perimeter footing width | 16 in |
| Depth | 12 in minimum, 16 in better |
| Post pads | ~30 in square, cast integral |
| Reinforcement | Two #4 continuous, chairs, corner bends |
| Anchor bolts | 0.5 in x 10 in, 6 ft o.c., within 12 in of each corner |
| Frost skirt | 2 in rigid foam, 4 ft out horizontal, 12 in below grade, wider at corners |

Monolithic because separate piers and a separate perimeter heave independently at 9,000 ft. 6 in proud keeps the treated plate out of splash and drift. Frost skirt and slab-edge foam are the entire frost defense in the absence of a stem wall - heated-building FPSF detail applies.

Slope crest setback 2-3 ft on south and west. Differential settlement is expected (north end on the long-settled container, south end on fill) - polycarbonate does not forgive racking. Post loads at 50 psf are ~5,550 lb each; bearing capacity of the wheel-packed fill was never the constraint.

**Concrete volume, reinforcement count, fastener schedules: explicitly excluded from the design/drawing scope as of the 2026-08-18 session.** Geometry (footprint, pier spacing, footing width/depth) is Ryder's to build from; quantity takeoffs are Ryder's to calculate.

### Item 9 - Bed placement
**Beds move inboard. South strip under the glass becomes walkway.** Light through a horizontal window band lands in a strip of constant width (1.84x sill to 1.84x head); raising the sill slides the strip north rather than shrinking it.

**STALE - lit-strip position not recalculated against the 3 ft 0 in sill.** Original calc assumed 4 ft 2 in sill. Open item.

---

## GLAZING

### Inventory (measured 2026-08-14)

| Unit | Glass size | Frame size | Rough opening | Qty | Disposition |
|------|-----------|------------|----------------|-----|-------------|
| Commercial windows | 32 x 91 in | **33.5 x 92.5 in** | **34.5 x 93.5 in** | 8 | **IN USE** |
| Gold walk-in cooler doors | 26 x 66 in | - | - | 6 | Set aside - solar-control low-E, wrong tool for this mission |
| Black walk-in cooler doors | 32 x 77 in | - | - | 2 | Hold in reserve - width matches commercial units |
| Full-lite door | on hand | - | - | 1 | East wall |
| Fixed pane | approx 33.5 x 45.5 in | **35.5 x 47.5 in** | **36.5 x 48.5 in** | 1 | Not used in greenhouse - spare |

**Frame confirmed with flange excluded.** Rough opening = frame + 0.5 in shim per side. Flange extension is unmeasured and does not affect the rough opening - it sets trim/flashing detail only, still open.

**Cooler doors rejected on the same logic as before:** framing cost is per opening, not per square foot, and low-E glass fights a passive-solar mission.

### Orientation

**South wall: HORIZONTAL.** 93.5 in wide x 34.5 in tall RO.

**East wall: VERTICAL**, both units, matched at one sill line. **Locked 2026-08-24, drawn on S-3** - see East Wall.

### Distribution

| Wall | Units | Orientation |
|------|-------|-------------|
| South | 4 | Horizontal, one per bay |
| East | 2 | Vertical, both north of the door, matched sill - drawn on S-3 |
| East | 1 door | Full-lite |
| **Floating** | **1** | Unassigned |
| West | none | Solid wall, by decision |

### Glazing ratio

**STALE - not recalculated against the current roof glazing plan (Phase 1 is now full metal over the north section, bare-rafter metal over the south section - no poly installed until Phase 2).** Original ratio assumed poly installed from day one. Open item, low priority since it doesn't affect Phase 1 construction.

---

## EAST WALL - LOCKED 2026-08-24 (drawn on S-3)

**Non-bearing.** Flat 2x6 nailers at all heads and sill plates, **no headers** - rough opening heads rack straight to the top plate. Full lateral wind pressure across a face that is mostly glass and door, so structural sheathing is still required. The east rafter is set inboard of this wall's inner face and the roof is carried to the wall plane on **2x12 lookout blocking, 5-1/2 in long at 24 in o.c.** - sheathing nailers only, not structural. See S-5.

Figures below read off `farm/greenhouse-drawings/S-3-east-wall-framing-elevation.svg`, not from memory. R.O. edges measured from the container (north) face.

| Element | Position from container | Sill | Head |
|---------|------------------------|------|------|
| Vertical window W1 | 0 ft 6 in to 3 ft 4-1/2 in | 2 ft 1-3/8 in | 9 ft 10-7/8 in |
| Triple stud pack (exterior trim) | between W1 and W2 | | |
| Vertical window W2 | 4 ft 0 in to 6 ft 10-1/2 in | 2 ft 1-3/8 in | 9 ft 10-7/8 in |
| Hessaire exhaust fan | 1 ft 0-3/4 in to 2 ft 9-3/4 in | 10 ft 4-7/8 in | 12 ft 1-7/8 in |
| Full-lite door | 11 ft 0 in to 14 ft 6 in, 3 ft 10-1/2 in off the south corner | grade | 7 ft 4 in |

Windows are the commercial units, 33-1/2 x 92-1/2 in frame, **34-1/2 x 93-1/2 in R.O.** Door is 3 ft 6 in x 6 ft 8 in full-lite, **3 ft 8 in x 6 ft 10 in R.O.**

**Fan rough opening is 21 in square, ASSUMED.** Verify against the actual Hessaire 16SF3-H before framing. Fan sits high and centred over the blank bay - see Ventilation, Layer 4.

**Both windows matched at one sill line, deliberately.** The wall is raked, so each unit could individually have gone higher, and the north unit gives up roughly 15 in to hold a level sill. That was traded for exterior trim reading straight across. Head height is set by clearance below the rake trim, not by a header.

**The pen problem that isn't one.** Ten-foot hog pens run their long side against this wall in Phase 1, which puts glass at animal height. Interior OSB wainscot has to go on regardless so the animals do not eat the insulation, and running it up across the lower glass is protection and pen wall in one. It comes off at conversion. The window does not have to clear pen height - it has to be there when the pigs leave. **The building is designed as a greenhouse because that is the harder condition; the barn phase borrows it.**

**The intake louver is NOT on this wall.** It moved to the west wall to stop the fan short-circuiting its own makeup air. The owner-accepted shear deviation formerly logged here is void with it.

---

## WEST WALL - bearing, solid

No glass, by decision - west glazing dumps summer heat exactly when the building is fighting to shed it and earns nothing in any season. Takes the most wind (fill falls away).

| | |
|---|---|
| Glass | None |
| Door | Insulated solid slab, 3 ft 6 in x 6 ft 8 in, **3 ft 8 in x 6 ft 10 in R.O.**, header (2) rough-sawn 2x10 |
| Intake louver | **J&D 30 in gravity shutter, 31 x 31 in R.O.**, south edge 1 ft 5-1/2 in off the south corner, sill 3 ft 11-3/8 in, head 6 ft 6-3/8 in, header (2) 2x6 on edge |
| Insulation | 5.5 in closed cell, full cavity |

**Bearing wall - real headers required**, unlike the east wall. Figures read off `farm/greenhouse-drawings/S-2-west-wall-framing-elevation.svg`.

**The louver lives here, not on the east wall.** Putting the makeup-air intake on the same face as the exhaust fan lets the fan short-circuit into its own inlet and sweep nothing. West is the far end of the run; air crosses the full building before it leaves. Locked 2026-08-24.

Natural home for thermal mass - unresolved, open item.

---

## NORTH WALL - RISER. LOCKED 2026-08-25

Stud wall standing on the container's top rail. **No posts, no bays** - the 10 ft bay module is a south wall fact and does not exist here. Studs run 2x6 at 16 in o.c. continuous the full 40 ft; rafters are at 24 in o.c. and DO NOT stack on the studs (changed 2026-08-27, see S-4/S-5); openings are framed where they land.

**Datum for this wall is the top of the container, 8 ft 10 in above grade.** S-4 dimensions off that datum on the left chain and off grade on the right.

### Height stack, above container top

| | |
|---|---|
| Steel angle horizontal leg | 1/4 in |
| Bottom plate (2x6 PT), top | 1-3/4 in |
| **R.O. bottom / vent panel bottom rail** | **1 ft 7-1/4 in** |
| R.O. top / box header bottom | 3 ft 7-1/4 in |
| Box header top = plate underside at the low (south) edge | 4 ft 3-3/4 in |
| **Cap plate top, north edge** | **4 ft 9 in** |
| Rafter top edge (peak) | 5 ft 9 in |

**Why the panel lands at 1 ft 7-1/4 in.** The cap plate is beveled 4.5:12 across its 5-1/2 in **width**, not along its 40 ft length - the peak runs dead level the whole way, zero fall east to west. The plate underside carries the same tilt, so it sits 2-1/16 in lower on the south edge, and a level header has to clear the low side. Below the cap plate top: 2-1/16 in of bevel drop, 3-3/16 in of doubled top plate, 8-1/2 in of box header = **1 ft 1-3/4 in consumed** before the panel starts. A 24 in panel then puts the bottom rail at 1 ft 7-1/4 in. **This supersedes the 26 in bottom-rail figure formerly carried in Ventilation**, which predates the box header entirely and assumed the panel hung straight off the cap plate with nothing between.

### Opening layout across the 40 ft face

Eight vent rough openings in **four pairs.** A pair is 4 ft opening / 4-1/2 in pack / 4 ft opening = 8 ft 4-1/2 in.

| Segment | Dimension |
|---|---|
| Each end | 1 ft 3-3/4 in |
| Pair | 8 ft 4-1/2 in |
| Between pairs | 1 ft 3-1/2 in |

Closes at 40 ft 0 in exactly.

### Framing at the openings

| Element | Spec |
|---|---|
| Studs | 2x6 at 16 in o.c., continuous full 40 ft. Rafters at 24 in o.c. do NOT stack on studs |
| Stud tops | Bevel cut 4.5:12, 5-7/8 in measured on the cut |
| Top plate | (2) 2x6, 3 in perpendicular to the bevel, set flush north |
| Between the pair | (3) 2x6 pack - king / stud / king, 4-1/2 in |
| Outboard of each pair | King + trimmer, 3 in |
| Header | Box header, (2) 2x6 on edge capped top and bottom, 8-1/2 in overall |
| Over the header | Cripples at every rafter, bevel-ripped to the plate slope - 2-1/16 in at the north face, tapering to nothing at the south |

**The cripples are not spacers and they are not optional.** The header top is level; the plate underside is beveled. Without them the plate touches the header along one edge only and the header never picks up the roof load.

**The top plate is 3/8 in narrower than the beveled stud top** - 5-1/2 in of plate on a 5-7/8 in cut. Plates set flush north, which puts the bare 3/8 in of stud on the interior where the closed cell buries it and keeps the exterior face flat for sheathing and drip edge.

### Snow

The panel bottom sits below the settled depth implied by a 50 psf design load. **Burial accepted, no height change** - raising the panel means growing the riser and the peak to serve a vent opening. Separate open question, not a geometry question: a top-hinged actuator trying to lift a drift on a warm spell. Mechanical stop, seasonal actuator removal, or clearing the north face. Waits until the actuators are specified (Open Item 14).

---

## STRUCTURE

### Post and beam south wall

Wall does not carry the roof - posts and a continuous beam do, which makes the south window openings non-structural infill (no header at all - see South Wall).

| Element | Spec |
|---------|------|
| Bays | 4 at 10 ft 0 in |
| Posts | 6x6, five total, galvanized standoff bases |
| Beam | **6x10 rough-sawn Doug fir or larch** (changed from 6x12 - see Beam Sizing below) |
| Studs between posts | 2x6, 16 in centers, non-bearing |
| Window head | Flange lands directly on beam underside, no header member |

**NO ENGINEERED LUMBER ANYWHERE.** LVL/glulam/LSL/PSL are interior-dry-use products and will delaminate in greenhouse humidity. Built-up beams trap water in the seams and rot from inside. Solid sawn timber only. Posts on galvanized standoff bases, never bearing directly on concrete.

**Rafters are dimensional lumber (2x12), not rough-sawn** - confirmed 2026-08-18. Only the beam and posts are rough-sawn.

### Beam sizing - CHANGED to 6x10

Required section modulus ~64 in3 for a 10 ft bay at 50 psf. **6x10 provides 83 in3 and is now the spec** - the margin the original 6x12 (121 in3) provided for ungraded rough-sawn timber was traded for riser height. 6x10 still clears the requirement with margin. Steel rejected on fabrication/coating/equipment cost at this span.

**Beam width stays 6 in** (rough-sawn) - only the depth changed, 12 in to 10 in. Birdsmouth notch dimensions at the beam are calculated against the 6 in width regardless of depth - see Framing Geometry.

### Rafters

2x12 dimensional Douglas fir-larch No.2 at 24 in o.c., 21 total, **240 in (20 ft) stock exact.** See Framing Geometry for the full cut-geometry writeup - raked plate north, birdsmouth south, parallel plumb cuts, 235-1/2 in usable rake.

**No overhang framed into the rafters at either end.** Rafters run flush to the framing plane at both walls - **all overhang is done by the roofing material itself**, not by rafter tails, sub-fascia, or outlookers. See Roof section.

**20 ft 2x12 stock confirmed workable** - the 240 in exact stock length carries a real but thin margin (the parallel-cut wedge geometry consumes stock at both ends; net usable rake is 235-1/2 in against a 235-1/2 in requirement with essentially no slack). Cull for crown/bow at delivery; order a few extra pieces to reject bad ones.

### Bearing assignment

North riser: yes (via raked plate, no notch). South (via post/beam): yes (via birdsmouth). West: yes. **East: NO - non-bearing**, east rafter set inboard of the wall inner face, roof carried to the wall plane on lookout blocking. The wall receives no roof contact at all.

Non-bearing does not mean unloaded - full lateral wind pressure across a face that's mostly glass and door. Structural sheathing required. The louver that once threatened this wall's shear moved to the west wall 2026-08-24; the deviation is void.

### Riser detail (on the container)

Stands on the container's **top side rail**, not the roof deck.

1. Continuous steel angle sill, L3x3x0.25, bolted through the top rail every 24 in with backing plates.
2. Treated bottom plate on the angle, sill seal/butyl between.
3. 2x6 stud wall, 16 in centers, **4 ft 9 in tall** (see Framing Geometry). Stud tops **bevel cut 4.5:12**, 5-7/8 in on the cut, carrying a **doubled 2x6 top plate laid on that same bevel**, 3 in perpendicular. Plates set flush north; the 3/8 in of bare stud left over sits on the interior. See North Wall.
4. Rafters bear full-width on the raked cap, plumb-cut flush at the riser's outside framing face. No notch, no hurricane-tie-at-birdsmouth condition - uplift connection method at this bearing needs its own detail, not yet drawn.
5. Sheathing, weather barrier, metal siding, full height up to and over the rafter top edge (see Detail D-4, north roof edge - NOT YET DIGITISED).

Uplift: the angle-to-rail connection is the hold-down for the entire roof. Thermal break: 2 in closed cell over the steel, inside, lapping the rail.

---

## ROOF

**Substantially re-locked 2026-08-18. Phase 1 is NOT full-slope sheathing/metal as originally written - see below.**

### Geometry
19 ft 7-1/2 in usable rake, 4.5:12 pitch, 18 ft 4-1/2 in run, 6 ft 10-3/4 in rise. See Framing Geometry for the full derivation.

### Phase 1 assembly - sheathing stops mid-slope, not full-slope

**CORRECTION to the original spec:** the original design sheet said "roof the entire slope in metal" over solid sheathing. This session determined the north (upper) section only gets sheathed in Phase 1; the south (lower) section runs metal panel directly on bare rafters, unsheathed, because that section gets stripped at Phase 2 conversion and sheathing it would be wasted material and wasted tear-down labor.

| | |
|---|---|
| Sheathing | North section only. Edge terminates at 9 ft 7-1/4 in up the rake from the south framing face - this is also the exact point where the Phase 1 upper metal panel's south edge, and the future Phase 2 poly panel's north edge, both land |
| Blocking | Continuous between rafters at the sheathing edge - backs the fastener row and the step transition (Detail D-5) |
| Upper (north) metal panel | Bears on sheathing |
| Lower (south) metal panel | Bears direct on bare rafters, 24 in o.c. span, no purlins |
| Step at sheathing edge | 7/16 in (sheathing thickness) - ramped by the lower panel's own flex as it climbs onto the deck under the lap. Closed with foam or butyl at the step line |

**No purlins anywhere on this roof** - both the Phase 1 lower metal panel and the Phase 2 poly panel bear directly on the 24 in o.c. rafters. (Poly's 4 ft panel width divides evenly into two 24 in bays with zero waste, so every panel joint still lands on a rafter - this is why no purlins are needed structurally for the poly. The 16 in module gave three bays per panel and worked for the same reason.)

### Phase 1 panel schedule (metal)

**Order:** 28 panels total at 12 ft stock (14 roof-width runs x 2 panels per run, covering 40 ft of building length at approx 3 ft net coverage per panel - confirm actual Pro-Panel coverage width before ordering, this count assumes 36 in).

**Cut:**
- Lower panel (14 required): **12 ft 0 in, no cut**
- Upper panel (14 required): **cut to 10 ft 10-1/4 in**

**Install:**
- Chalk line for the lower panel's top edge, measured DOWN the rake from the north framing face: **8 ft 4-1/4 in**
- Upper panel's bottom edge sets 20 in below the lower panel's top edge (this is the lap, and it falls entirely within the sheathed zone north of the 9 ft 7-1/4 in sheathing edge)
- North cantilever past the finished wall surface: 4 in
- South overhang past the finished wall surface: 8 in (falls out automatically from the 12 ft lower panel length, no separate cut needed)

**Ribs and orientation:** metal ribs run down-slope, parallel to rafters.

### Phase 2 conversion (metal-to-poly)

At conversion: strip the lower metal panel and the north-section sheathing above the 9 ft 7-1/4 in edge is NOT touched (sheathing only ran to that line in Phase 1 - nothing to strip there). Poly drops onto the now-bare lower rafters.

**Poly:** 8mm triple-wall, 10 panels at 4 ft x 10 ft, flutes down-slope, UV face out. Bears directly on rafters, no purlins. Panel joints at each rafter (9 joints): H-profile aluminum base-and-cap, base screwed to rafter, panels float in the cap - accommodates the ~0.25 in per 10 ft thermal movement, no fasteners through the panel field.

**Poly eave (south, bottom edge), Detail D-7 (not yet drawn):** 4 in overhang past the finished wall surface. **Termination is breather tape only - no U-profile, no clamped or snap-fit edge trim.** Locked reason: a shedding roof at 4.5:12 sends sliding snow/ice directly across this edge, and any clamp-style channel is a catch point that gets torn off by the slide. Tape seals the flute ends and allows condensation weep without presenting a catchable edge. Accepted maintenance cost: periodic re-taping.

**Poly-to-metal seam (legacy detail, now superseded by the direct-lap method below):** the north edge of the poly (at the 9 ft 7-1/4 in line) is overlapped by the Phase 1... no - by the PERMANENT upper metal panel, which never moves between phases. **The offset/transition flashing originally specced (legacy detail) is DEAD.** Replaced by a direct 6 in dry lap: metal edge (now extended 6 in past its Phase-1-only position to reach **10 ft 10-1/4 in total, see revised panel length below**) laps over the poly, bearing on the nine H-caps (which stand proud of the poly face by roughly 1/2 in) plus one mid-bay foam/spacer pad per bay (24 in module, so roughly every 2 ft) to prevent the metal from contacting and abrading the poly face under snow load between caps. No sealant, no rubber gasket, no continuous strip - dry lap, low-friction bearing only on the caps and the discrete spacer pads.

**Upper panel length revision for the 6 in poly lap:** 10 ft 10-1/4 in (10 ft 4-1/4 in original + 6 in lap allowance). This is the number that should be used for Phase 1 ordering/cutting - see Panel Schedule above, already reflects this.

**Why no purlins, no offset flashing, and dry lap only:** all three are simplifications discovered through the framing-geometry session - poly's 4 ft width matches the 24 in rafter module with zero waste, killing the purlin requirement; the 3/16 in natural height difference between the sheathed/metal side and the bare-rafter/poly side (from OSB+flat-Pro-Panel buildup vs poly thickness) means the metal edge already sits proud of the poly with no shim or bent flashing required; and sliding snow load ruled out any clamp-style edge hardware at the point of contact.

**Metal, Phase 1 north section:** solid sheathing, later gets closed-cell foam and interior finish per the Insulation section - this section stays permanent metal roofing through both phases.

**Snow shed minimums:** heated poly 20-22 deg, unheated poly 28-30 deg, heated metal 18-20 deg, unheated metal 25-30 deg. Locked 4.5:12 (20.6 deg) clears the heated-poly minimum with margin.

### Roof edge details, both ends (SPLIT 2026-08-26 - south is D-2, north is D-4)

**North (Detail D-4, not yet digitised):** riser cap plate (raked) up through rafter bearing, sheathing over the rafter's top edge, flat-ripped (rib removed) top course of wall Pro-Panel, standard drip edge with hemmed leg over the flat course, **drip edge turns down over the riser wall face** (covers the sheathing edge and flat wall course's top edge - locked over the alternative of stopping at the panel edge). Roof panel (4 in cantilever) laps over the drip edge. Outside closure strips under the roof panel ribs at this edge - required here because this is the up-slope, windward edge and wind-driven rain can push under open ribs; not required at the south eave because that edge is shedding water outward, not receiving it.

**South (Detail D-2):** beam top through rafter's remaining 9-1/8 in depth after the birdsmouth notch, sheathing over the rafter end, flat-ripped top course of wall Pro-Panel, standard drip edge with hemmed leg over the flat course, roof panel (8 in overhang, Phase 1 metal) laps over the drip edge. Order of assembly: flat wall course first, drip edge over it, roof panel over the drip edge - water sheds off roof onto drip edge, breaks clean at the hem, falls past the wall face, nothing runs behind.

### Gutters
**Not installed in Phase 1.** Metal's 8 in overhang sheds clear on its own with no substrate needed. **Phase 2, when the poly's 4 in overhang replaces the metal at the eave, is the intended point to add a gutter** - the poly eave becomes the mounting reference. Gutter mounting height at that time must keep the front lip at least 1 in below the poly's underside so sliding snow/ice passes over the top rather than catching the lip. No fascia or gutter substrate is built into Scope B framing - flagged as a Phase 2 owner addition, not a contractor scope item.

---

## VENTILATION

**Substantially expanded 2026-08-18. Original design was fully passive, wax-actuated. Now a four-layer scheme.**

### Layer 1: passive wax-actuated vents (original scheme, panels resized)

**North (riser) exhaust panels - RESIZED:**

| | |
|---|---|
| Count | 8, in four pairs - see North Wall (there are no bays on this wall) |
| Size | 4 ft wide x 2 ft (24 in) tall |
| Area | 64 sq ft |
| Hinge | Piano hinge at top, racked to the underside of the box header |
| **Bottom rail position** | **1 ft 7-1/4 in above the container top** - was 26 in, superseded 2026-08-25 |
| Clear insulated wall below panel | 1 ft 5-1/2 in |
| Actuation | Wax cylinder, fails closed |

**South (sill) intake panels - RESIZED 2026-08-18, trimmed 2026-08-24, shortened again 2026-08-25 when the sill dropped:**

| | |
|---|---|
| Count | 8 (2 per 10 ft bay) |
| Size | 4 ft wide x **24 in** tall (was 27 in, then 26-1/2 in) |
| Area | **64 sq ft** |
| Hinge | Piano hinge at top, racked to the underside of the sill plate |
| Bottom rail position | 7-1/2 in above grade - held, so the drop came out of panel height |
| Top rail position | **2 ft 7-1/2 in above grade** (was 2 ft 10 in) |
| Actuation | Wax cylinder, fails closed |

**Sizing logic, panel height:** actuators only open on heat - they're closed all winter by design, so the low bottom-rail height (7-1/2 in above grade) does not present a snow-drift-blocking condition; drifts pile against a closed, gasketed panel like any other wall section. Base gravel/splash strip noted for the south wall to manage rain splash and mud at the low bottom rail - maintenance item, not a function item.

**Intake-to-exhaust ratio: 64 sq ft / 64 sq ft = 1.000x.** Was 1.125x; the 2026-08-25 sill drop took 2-1/2 in off every south panel. Owner's call, made explicitly: hold the bottom rail at 7-1/2 in and let the panels shorten, rather than walk a moving panel down to 5 in off grade into splash and mud. Design sheet originally targeted 1.5x; the south wall has no more width to add intake, so the ratio is accepted as-is. **The lever on this system is fan runtime, not more opening** - see Layer 4.

**Absolute area check against the 15-20% of floor area passive-vent standard:** 64 sq ft exhaust against a 736 sq ft floor is 8.7%, against a 110-147 sq ft target - short by roughly half. **Accepted, not solved, because of the layered scheme below** - passive vents are one of four paths, not the sole path, and the shortfall is covered by powered ventilation on the conditions (hot, still, daytime) where passive is weakest.

### Layer 2: coop exhaust (existing hardware, no change)
Existing coop exhaust fan continues to draw makeup air through the 20 in x 30 in window per Item 5 - unchanged, now understood as intentional heat transfer into the coop as well as pressure separation.

### Layer 3: container bay supply fans (new)
**Tool room:** small continuous-run fan, greenhouse-to-container, through the container's south face. **4 in wall-termination discharge fan (crawlspace-vent-fan class)** on the container's far side for relief. Charges the tool bay as thermal mass.

**Feed room:** small continuous-run fan, greenhouse-to-container, through the container's south face. **Relief via the existing cat door flapper** - not airtight, functions as the return path, no dedicated termination needed. **Open concern, not solved:** greenhouse air is humid; stored feed can mold. Owner accepts the risk at low CFM with a leaky relief path and will address if it becomes a problem.

**Scope note:** all fan hardware and container penetrations are owner scope, not in Ryder's Scope B - the container's south face is existing construction.

**Effect on the exhaust shortfall:** modest, not decisive. These are low-CFM continuous fans; peak summer heat load is measured in the thousands of CFM, and this layer is roughly 10-15% of that peak. Their real value is winter/shoulder-season thermal mass charging (the container becomes the thermal-mass answer to Open Item 7, previously unresolved), not summer purge capacity.

### Layer 4: Hessaire powered exhaust (reassigned from garage-barn build)
**Hessaire 16SF3-H, 16 in, 1325 CFM gravity-louver shutter fan** - originally budgeted and purchased for the garage-barn conversion (see `farm/garage-barn-build-sheet.md`, item 1, $125.58, ordered/delivered 2026-08-03). **Reassigned to the greenhouse, mounted through the east wall**, timer-run during daytime hours for animal-odor purge and summer heat purge. Gravity louvers seal closed when off - no envelope penetration issue in winter.

**At 1325 CFM against a building volume of roughly 6,250 cu ft, this is a full air change every 4.7 minutes (~13 ACH) when running** - meaningfully more capacity on demand than the passive vents provide on a still day, and it directly covers the hot-still-afternoon condition where passive venting is weakest.

**Requires dedicated makeup air - cannot rely on the wax-actuated intakes**, which may be closed (below opening temperature) exactly when the timer fires on a cool morning. **Makeup air - SOURCED AND LOCATED 2026-08-24. J&D 30 in gravity shutter, 31 x 31 in rough opening**, gravity backdraft damper that seals when the fan is off. **Located in the WEST wall**, far south, 1 ft 5-1/2 in off the south corner - see West Wall. It is deliberately not on the east wall with the fan: an intake on the same face lets the fan short-circuit into its own inlet and sweep nothing. West puts the intake at the far end of the run, so air crosses the full 18 ft before it leaves.

**Garage-barn build sheet cross-reference:** the Hessaire's removal from that budget should be noted there - it is no longer a garage-barn line item. Not yet updated in this session; flag for `farm/garage-barn-build-sheet.md` maintenance.

### Vent panel construction, Detail V-1 (both wax-actuated locations)

**CHANGED 2026-08-18** from the original gasketed/aluminum-frame spec.

| Layer | Spec |
|---|---|
| Skin | Pro-Panel, ribs matched/aligned to the wall's own panel profile |
| Overlap | 1/2 in lap on all four edges - panel nests into the wall's rib pattern rather than sitting proud, using the panel's own profile as the weather seal (same principle as ordinary metal-siding laps) |
| Core | 2 in rigid polyiso, **inset from the panel edges** - stops short of the lap zone so the 1/2 in metal-to-metal overlap can actually close |
| Seal | Thin rubber strip, mounted on the WALL-SIDE FRAME, not on the moving panel (a seal on the panel abrades with every open/close cycle; on the fixed frame it just compresses) |
| Screen | **1/4 in hardware cloth**, locked 2026-08-24 across **all 16 wax-actuated panels and the intake louver.** Accepted consequence: it costs free area on a passive layer that is already thin. The lever if it bites is fan runtime, not more opening |
| Gaskets | **Not used** on the panel perimeter generally - owner's call, accepted with the note that ungasketed panels are a real infiltration path, particularly costly on the north (exhaust) panels where warm stack air collects. Owner-accepted trade for actuator weight/simplicity |
| Construction | Extra Pro-Panel siding sheets ordered specifically to cut these panels from, matching the wall's rib profile exactly |

**Weight, this construction:** approx 1.5 lb/sq ft (no OSB layer - OSB was evaluated and dropped specifically because it drove panel weight past comfortable wax-cylinder actuator capacity). South panel (4 ft x 27 in, 9 sq ft): ~14 lbs. North panel (4 ft x 24 in, 8 sq ft): ~12 lbs. Both comfortably within typical single wax-cylinder lift capacity (~20-30 lb range) - **actual cylinder spec still not verified against this figure, see Open Items.**

**VERIFY WAX CYLINDER LIFT AGAINST FINISHED PANEL WEIGHT** - still open, now with a real target weight to verify against (12-14 lbs typical).

---

## HEAT

**Modine HD100AS0111** (full spec in `farm/garage-barn-build-sheet.md`). 100,000 BTU/hr input, ~52,000 BTU/hr delivered at 9,000 ft after altitude derate. Altitude handled at the gas valve spring only, no orifice hardware needed.

**Load figures below predate the corrected envelope geometry (peak, riser, sill all changed 2026-08-18) and were already stale before this session. Recalculation remains an open item.** Headroom margin at the old, larger load figure was 2.4x - building got shorter this session, not taller, so the Modine is, if anything, more comfortably sized than before, not less.

| Loss path | BTU/hr (stale) |
|-----------|--------|
| Glazing | 12,100 |
| Insulated metal roof | 2,300 |
| End walls | 1,700 |
| Infiltration, altitude-adjusted | 6,200 |
| **Total (stale)** | **~22,000** |

**Note:** the Hessaire fan is being pulled from the garage-barn heater/fan budget for use here - see Ventilation, Layer 4. Does not affect the Modine, which remains garage-barn-then-greenhouse shared equipment per the original plan.

---

## OPEN ITEMS

1. ~~Concrete volume.~~ **Explicitly excluded from design scope 2026-08-18** - Ryder's to calculate from the locked footing/pier geometry.
2. **Pen count and size.** Blocks pen slab area.
3. **Floating window.** One of eight commercial units unassigned - west wall (breaking the no-glass decision) or held spare.
4. ~~20 ft 2x12 availability.~~ **Resolved 2026-08-18** - 240 in exact stock works, margin is thin but real. Still worth confirming yard stock/special-order status and culling for crown/bow at delivery.
5. **Window flange extension.** Unmeasured - sets trim/flashing detail, does not change the rough opening.
6. **Heat load recalculation** against the corrected 736 sq ft envelope, the 2026-08-18 height changes, and the final glazing package.
7. ~~Thermal mass.~~ **Substantially answered 2026-08-18** - the container bays (feed, coop, tool), actively charged via supply fans, serve as the thermal mass reservoir. West wall interior face remains a secondary option, unused for now.
8. **Stratification management.** Circulation fan or mass ducting - pitch does not solve it. Partially addressed by the container supply fans moving peak-height air, not fully solved.
9. **Buried utilities.** Depth and routing before any excavation.
10. **Bed layout.** STALE - not recalculated against the 3 ft 0 in sill (was 4 ft 2 in). Needs rerun.
11. **Drainage and grading** around the pad perimeter.
12. **Rootstock agent definition.** Not committed.
13. ~~East wall re-geometry.~~ **CLOSED 2026-08-24** - wall redrawn as E-1 against the corrected taper. Both windows matched at one sill, fan placed high and centred, door pinned as far south as the wall height allows. The louver that was part of this item moved to the west wall instead. See East Wall.
14. **Wax cylinder lift verification.** Carried forward, now with a real target (12-14 lb panels) to verify against.
15. ~~Gravity-close intake louver sourcing.~~ **CLOSED 2026-08-24** - J&D 30 in gravity shutter, 31 x 31 in R.O., located in the west wall. See West Wall and Ventilation Layer 4.
16. **Riser uplift/hold-down detail at the raked cap plate.** NEW - the birdsmouth-based hurricane-tie approach no longer applies at the north bearing since it's now a flat bearing on a raked plate, not a notch. Connection method not yet drawn.
17. **Ceiling height table, glazing ratio, lit-strip position** - all stale against the corrected peak/sill geometry, not recalculated this session, low priority.
18. **Garage-barn build sheet** needs a line-item update removing the Hessaire fan, now reassigned here.
19. ~~South wall riser/peak cascade recalc.~~ **CLOSED 2026-08-25** - two errors found (rafter above notch, and the window rough opening on S-1), both absorbed by dropping the south sill to 3 ft 2 in so the roof plane and peak hold at the figures the drawings already carried. Cascade, south vent panels and intake ratio all rerun. Drawing set and sheet agree. Original text follows. ~~NEW 2026-08-24 - sill locked at 3 ft 4-1/2 in above grade, built-up construction (2x6 flat cap / 2x4 on edge / 2x6 flat bottom cap, 6-1/2 in tall; single 2x6-on-edge rejected, no bearing). Window head, beam top, roof plane, peak, and riser framing in the Framing Geometry table, plus the south vent intake panel area and intake-to-exhaust ratio in Ventilation, all still reflect the old 3 ft 0 in sill and need a full rerun. South wall framing elevation drawing (`farm/greenhouse-drawings/south-wall-framing-elevation.svg`) is built and committed against the new sill - this open item is the design sheet catching up to the drawing, not a design question.~~

---

## DRAWING PRACTICE

Locked 2026-08-25 out of the north wall session retrospective. Extended 2026-08-26 out of the roof framing session.

- **Drawings get looked at before they get pushed.** Render the sheet to an image, inspect it, present it, then commit. A drawing is only correctable once it is visible, and a dimension chain running off the edge of the sheet is invisible in the source.
- **Every sheet gets a generator.** A drawing whose dimensions are hard coordinates cannot be corrected safely - the failure mode is a rect that quietly did not move, which still looks like a drawing. S-1 had no generator on 2026-08-25 and had to be corrected by coordinate surgery with the whole stack back-converted to inches afterward to prove it.
- **Structure does not transfer between walls.** The 10 ft post bays are a south wall fact. The riser has no posts and no bays. Confirm a structure exists on a given wall before laying anything out against it.
- **No coined vocabulary.** If a term is not already in this sheet, it does not get used in conversation about this sheet.
- **Layout arithmetic gets computed, not spoken.** Any spacing run that has to close on a total is checked programmatically before it is stated.
- **Read an existing sheet before drawing a new one.** Format is inherited from the set, not invented per sheet. The first roof framing plan attempt on 2026-08-26 was built without opening N-1 and had to be thrown away and redrawn - wrong tool, wrong conventions, no title block, no note boxes. The set only reads as a set if each new sheet is copied off the last one.
- **A callout describing a member is not the member.** If something is in the drawing's scope, it gets drawn. A paragraph explaining where the lookouts go, on a sheet with no lookouts drawn, is not a lookout detail.
- **Note text wraps to measured string width.** Lines are packed against the box width less padding, computed, not hand-broken. When notes overflow, the answer is a bigger box or shorter notes - never silently shrinking type to hide a wrapping bug.
- **Verified arithmetic is not a legible drawing.** The rafter spacing on R-2 was provably correct at 24 in o.c. and still read as 16 in o.c., because 21 rafter lines and 13 panel lines drawn at similar weight merge into one field. Check what the sheet communicates as a separate step from checking that the numbers close.
- **Notes are written for a framer on a ladder in bad weather.** Short lines. No explaining things a framer already knows. If a note runs to five lines it is a specification, and it belongs in this sheet rather than on the drawing.
- **The drawings outrank this sheet on anything already drawn.** This sheet is early-stage narrative; the detail sessions have overtaken it repeatedly. Where a sheet draws a thing, the sheet is authoritative and this document is a lagging description of it. This document governs only what is not yet drawn. Added 2026-08-27 after three separate turns in one session were lost to treating a loose figure here as a conflict against correct drawn geometry - the bay width being the clearest case: this sheet says four bays at 10 ft, the drawing says 9 ft 10-3/8 in centre to centre, and only the drawing closes on 40 ft.
- **Rebuild by transcription, not re-authoring.** When a sheet is redrawn with its framing locked unchanged, extract every member out of the superseded file programmatically, convert to real inches, and transcribe. Never rebuild members from a dimension table. Tables carry non-member columns - S-1's bay table has a GAP column between the stud against the post and the king stud - and reading past one shifts every assignment down the row. That error, plus never extracting the sole plate or footings at all, cost four failed rebuilds of S-1 on 2026-08-27 before the sheet was rebuilt off its own geometry.

---

## DRAWINGS

**Drawing set is consistent as of 2026-08-27.** All four wall elevations carry roof plane 7 ft 8-1/4 in at the south wall and peak 14 ft 7 in, all sheets are on the S-/D- numbering scheme, and every sheet that names rafter spacing says 24 in o.c.

`farm/greenhouse-render-prompts.md` - tested exterior render prompts (south, north, east views) plus prompting lessons.

**East elevation, dimensioned PDF** - drawn to the PRE-2026-08-18 geometry. Peak, riser, and sill heights it shows are now superseded. Do not build from it; needs a redraw once the east wall re-geometry (Open Item 13) is resolved.

**Sheet numbering, locked 2026-08-27.** Two schemes were live at once (the legacy spec list assigned R-2/R-3/R-4 to details while the drawn sheets used the same numbers for different drawings). Resolved by discipline code, wall identity moved into the title block: **S-series is structural** - framing elevations and the framing plan. **D-series is details.** No shared number space, so the collision cannot recur as the set grows.

| Sheet | File | Was |
|---|---|---|
| **S-1** | `S-1-south-wall-framing-elevation.svg` | S-1 (legacy, unprefixed file) |
| **S-2** | `S-2-west-wall-framing-elevation.svg` | W-1 |
| **S-3** | `S-3-east-wall-framing-elevation.svg` | E-1 |
| **S-4** | `S-4-north-wall-framing-elevation.svg` | N-1 |
| **S-5** | `S-5-roof-framing-plan.svg` | R-3 |
| **D-1** | `D-1-birdsmouth-detail.svg` | R-4 |
| **D-2** | `D-2-south-roof-edge-detail.svg` | R-6 |
| **D-3** | `D-3-panel-layout.svg` | R-2 |
| **D-4** | *not yet digitised* | north roof edge |
| **D-5** | `D-5-sheathing-termination.svg` | R-1 |

All legacy filenames and the four legacy generators were deleted the same session. No old-scheme reference survives anywhere in the set.

**South wall framing elevation (S-1)** - `farm/greenhouse-drawings/S-1-south-wall-framing-elevation.svg`. Rebuilt 2026-08-27 from the superseded sheet's own extracted geometry. Now carries the 21 rafter tails at 24 in o.c. above the beam (the old sheet drew no rafters at all) and is drawn at true 1/2 in = 1 ft - the old sheet was labelled 1/2 in but drawn at 0.475, now corrected. Framing content is otherwise identical to the superseded sheet: continuous sole plate the full 40 ft, footings from -1 ft 4 in to 0 ft 6 in, four jamb studs per bay both sides, built-up sill over each vent, window rough opening as a void bounded by real members. Generator at `generators/generate_s1.py`. Note the bay table's GAP column - see DRAWING PRACTICE.

**West wall framing elevation (S-2)** - `farm/greenhouse-drawings/S-2-west-wall-framing-elevation.svg`. Drawn 2026-08-24. Carries the gravity intake louver rough opening. Rafter callout corrected 16 in to 24 in o.c. on 2026-08-27.

**East wall framing elevation (S-3)** - `farm/greenhouse-drawings/S-3-east-wall-framing-elevation.svg`. Drawn 2026-08-24. Supersedes the legacy dimensioned east elevation PDF above. Lookout callout corrected 16 in to 24 in o.c. on 2026-08-27. **Fan rough opening still carries an ASSUMED 21 in square - verify before framing.**

**North wall (riser) framing elevation (S-4)** - `farm/greenhouse-drawings/S-4-north-wall-framing-elevation.svg`. Drawn 2026-08-25. Carries the riser height stack, the four-pair vent layout, box headers with bevel-ripped cripples, the beveled plate condition, and an east orientation arrow. Two dimension chains: left off the container top, right off grade. Rewritten 2026-08-27: rafters 31 at 16 in became 21 at 24 in matching S-5, and the rafter line now sits independent of the stud line. **Riser studs remain 16 in o.c. and did not move** - all 77 stud and cripple members are byte-identical to the previous version. **This sheet has no generator** - the rafter swap was done as a scripted surgical edit rather than a full transcription, deliberately, because re-authoring 147 members was the exact failure that cost four rounds on S-1 the same day. It is the one sheet in the set that cannot be regenerated. Open item.

**Roof framing plan (S-5)** - `farm/greenhouse-drawings/S-5-roof-framing-plan.svg`. Drawn 2026-08-26. Carries the 24 in o.c. rafter layout pulled from the west, the inboard east rafter, lookout blocking, the blocking line at the sheathing edge, and the snow load design basis. **This sheet is the rafter layout authority** - S-1 and S-4 both draw the same 21 rafters and refer back here rather than re-dimensioning them.

**Birdsmouth cut detail (D-1)** - `farm/greenhouse-drawings/D-1-birdsmouth-detail.svg`. Drawn 2026-08-26. Bench detail for cutting the rafter ends: both wedges dimensioned on all three sides.

**South roof edge crosscut (D-2)** - `farm/greenhouse-drawings/D-2-south-roof-edge-detail.svg`. Drawn 2026-08-26. Section through a 6x6 post: sheathing, horizontal Pro-Panel with the ripped flat top course, drip edge with kicker, roof panel at 8 in overhang. Layers drawn exploded.

**Panel layout (D-3)** - `farm/greenhouse-drawings/D-3-panel-layout.svg`. Regenerated 2026-08-26 against the 24 in o.c. layout.

**Sheathing termination and metal step (D-5)** - `farm/greenhouse-drawings/D-5-sheathing-termination.svg`. Was drawn and committed but never registered in this document until 2026-08-27, when it surfaced during the renumber - it had been sitting in the drawings folder while this sheet still listed it as an undrawn specification. Rafter spacing corrected 16 in to 24 in o.c. the same session. **Still the only sheet in the set drawn in colour rather than black-and-white line work, and it is not to scale.** Owner's call to leave both as-is. No generator.

**North roof edge (D-4) - STILL TO BE DIGITISED.** The north and south roof edges are separate details, not a shared sheet; that split was made 2026-08-26 on the owner's call. The south end is drawn as D-2. **The north end exists only as a hand drawing and is not in the repo.** It predates the beveled cap plate, the box header and the 2026-08-25 sill drop, so digitising it is a spec-walk, not a trace.

**Remaining vent and roof construction details** - locked as specifications 2026-08-18, not yet drawn. See `farm/greenhouse-roof-vent-details.md`. Under the new scheme: **D-6** metal-to-metal endlap (largely superseded by the dry-lap note), **D-7** poly eave termination, **D-8** vent panel construction (was V-1). Sheets R-3, R-4 and V-1 hand drawings are also still outside the repo.

**Locked build sequence for future drawing sessions (owner's order, spans multiple sessions):** east elevation, south elevation, west elevation, north elevation, roof framing plan, wall framing plans, aerial layout, footer/footing plan.

---

## DESIGN NOTES CARRIED FORWARD

- **Sill height does not change how much light you get. It changes where the light lands.** The lit strip is constant width; raising the sill slides it, doesn't shrink it.
- **Panel length sets depth**, not the reverse.
- **Framing cost is per opening, not per square foot** - killed the small cooler doors.
- **On a tapered wall, the south (low) jamb is always the governing clearance point** for any opening, regardless of where the opening starts.
- **The tall bay is a feature.** Warm air collecting at the peak against insulated mass under a metal roof is a reservoir and an ideal intake plenum - now literally true, since that peak-height air is what the container supply fans move.
- **A birdsmouth notch and a raked bearing plate solve the same bearing problem differently** - notch costs rafter depth and consumes stock past the heel; a raked plate costs nothing off the rafter and keeps full depth, at the cost of a beveled-cut plate/studs at that one wall.
- **Parallel plumb cuts on a rafter make a parallelogram, not a rectangle** - top and bottom edges are equal length but offset from each other. The usable rake (what the roof covers) is shorter than the stock length by one wedge, not two, when only one end is notched.
- **A short, dry material lap outperforms a fabricated flashing piece when the height difference between two roof planes is small** - discovered this session solving the metal-to-poly transition; the offset flashing (legacy detail) was engineering a solution to a gap smaller than the tolerance of the materials meeting it.
- **Sliding snow at pitch rules out any clamped or snap-fit edge hardware at a shedding roof's leading edge** - governs both the poly eave (no U-channel) and the gutter timing (Phase 2 only, poly's shallower overhang, not Phase 1's metal).
- **Wax cylinder actuators only open on heat - they are closed by design through winter**, which reframes any low-mounted panel's snow/drift exposure as a non-issue, since the panel behaves like any other closed wall section in the season when drifting occurs.
- **A bevel across a member's width is not a bevel along its length.** The riser cap plate is raked 4.5:12 across 5-1/2 in, which costs 2-1/16 in of headroom at every opening on that wall. Along the 40 ft face it costs nothing - the peak is level end to end. Getting the axis wrong turns a 2 in problem into an 18 in one.
- **A level member meeting a beveled one touches on an edge, not a face.** Line contact carries nothing. The shim that fills the wedge is what makes the load path real, and it is easy to leave off a drawing precisely because it is thin.
- **When a correction wants to push a building up, check whether it can be absorbed at the bottom instead.** The 2026-08-25 errors would have raised the roof plane, peak and riser by 2-1/2 in and invalidated three drawings. Dropping the south sill by the same 2-1/2 in absorbed all of it, held the roof, and left W-1 and E-1 untouched. The sill had room; the riser did not want the height.
- Chinese-style solar greenhouse (two-plane south face, steep glazed wall, night curtain) remains a live alternative, passed over not ruled out.
