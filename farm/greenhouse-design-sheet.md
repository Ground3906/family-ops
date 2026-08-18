# Greenhouse Design Sheet

**Agent:** Rootstock (definition not yet committed)
**Site:** 38.0979386, -105.2994594 - 1722 Edelweiss Dr, Westcliffe CO, 9,000 ft, zone 4a
**Status:** Design in progress. Nothing built. Nothing ordered.
**Design sessions:** 2026-08-13, 2026-08-14

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

**Design snow load: 50 psf.** Westcliffe town rating, confirmed by Matt.

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
| West | Feed room | Fixed. Insulated 2 in rigid foam, walls and ceiling |
| Center | Chicken coop | Fixed. Insulated 2 in rigid foam, walls and ceiling |
| East | Tool room | Becomes greenhouse-centric tool storage |

**Openings in the south face (into the greenhouse):**

- Feed bay: man door, exists
- Coop bay: 20 in x 30 in window, exists
- Tool bay: man door, future

Container sits on dirt. Any excavation along its south face risks undermining corner-casting bearing. Bird run is handled outside this design.

---

## LOCKED GEOMETRY

**Locked 2026-08-14/15. Supersedes all earlier versions of this table.**

**CORRECTION LOGGED:** an intermediate version of this session stated the south sill at 4 ft 6 in. That was a hand-calculation error in the header subtraction, caught and corrected before commit. Verified figure is 4 ft 2 in. The error never reached the drawing set - the east elevation PDF was built from the correct chain throughout.

| Element | Dimension |
|---------|-----------|
| Container top above grade | **8 ft 10 in** (measured) |
| Roof pitch | **4.5:12 (20.6 deg)** |
| Riser above container | **5 ft 8 in** |
| **Peak above grade at the container** | **14 ft 6 in** |
| Slope length | 19 ft 8 in (two 10 ft panels, lapped) |
| Depth | **18 ft 5 in** |
| Roof fall over the depth | 6 ft 11 in |
| Footing top | 6 in proud of finished grade |
| Slab fall, container to south wall, 1/8 in per ft | 2.3 in over the run |
| **Beam bearing above floor at the south wall** | **7 ft 9 in** |
| Doubled top plate | 3 in |
| Racked 2x6 header, on edge | 5.5 in |
| **South window head** | **7 ft 1 in** |
| South window rough opening, vertical dimension | 34.5 in (measured frame + 1/2 in shim per side) |
| **South window sill** | **4 ft 2 in** |
| **Framing below south sill (above the 6 in footing)** | **3 ft 8 in** |
| **Pen ceiling at 10 ft line** | **10 ft 9 in** |
| Footprint | 18 ft 5 in x 40 ft = **736 sq ft** |

**Why the riser is 5 ft 8 in and not 5 ft:** the real container datum (8 ft 10 in) is 8 in lower than the 9 ft 6 in interior-height figure this design used through most of the session. At the original 5 ft riser, that 8 in loss broke two things at once: the south intake panels lost the wall height to fit, and the east wall's second vertical window collided with the roofline (clearance fell to about 0.1 in). Growing the riser by 8 in restores every downstream number - sill, intake fit, and east wall clearance - to what had already been locked and drawn.

**Ceiling height by distance south of the container (from the 14 ft 6 in peak, falling 4.5 in per ft):**

| Distance | Ceiling |
|----------|---------|
| 0 (peak, at container) | 14 ft 6 in |
| 5 ft | 12 ft 8 in |
| 10 ft (pen line) | 10 ft 9 in |
| 15 ft | 8 ft 10 in |
| 18 ft 5 in (south wall) | 7 ft 7 in |

Note the south wall figure here (7 ft 7 in) is the roofline height measured from the container-top datum. The **beam bearing** figure used for window head/sill math (7 ft 9 in) additionally accounts for the 2.3 in the slab drops over the same run - the floor is lower at the south wall than at the container, so the wall reads taller from the local floor even though the roofline itself is a fixed plane. Both figures are correct; they answer different questions. Use 7 ft 9 in for anything measured from the south wall's own floor. Use the falling-ceiling table for anything measured from the container's floor level (e.g., the pen zone).

---

## LOCKED ITEMS

### Item 2 - Use
Four-season, cold-hardy. Never freezes inside. Passive solar carrying the load, mechanical heat as insurance.

### Item 3 - Footprint
18 ft 5 in x 40 ft, 736 sq ft. Container is the north wall. Building runs south off the container's full 40 ft face.

### Item 4 - Container layout
As above. Fixed and closed to design.

### Item 5 - Coop / greenhouse air relationship
Wall stays sealed and insulated. **One-way air path: greenhouse to coop.** Coop's existing exhaust fan draws makeup air through the existing 20 in x 30 in window instead of cold outdoor air. Coop stays negative pressure relative to the greenhouse. Separation enforced by pressure gradient, not filtration. No new hardware.

**5.1 locked:** greenhouse window is primary intake. Exterior coop windows retained as functional backup.

### Item 6 - Structure geometry
**Single-slope shed, 4.5:12.** Framed riser built up off the container top, sloping down south. Peak sits over the north wall against insulated mass, not under glass.

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

### Item 9 - Bed placement
**Beds move inboard. South strip under the glass becomes walkway.** Light through a horizontal window band lands in a strip of constant width (1.84x sill to 1.84x head); raising the sill slides the strip north rather than shrinking it. A tall sill costs nothing but reach once the bed is inboard.

**Winter lit strip at the 4 ft 2 in sill:** approximately 7 ft 8 in to 12 ft 11 in south of the container. Summer beam reach approximately 1 ft 3 in; vertical south glass self-shades hard.

A waist-high bed can nest under the south glass but gets no direct winter beam - diffuse light and wall bounce only, shade-tolerant crops, treat as extra capacity not the winter workhorse.

---

## GLAZING

### Inventory (measured 2026-08-14)

| Unit | Glass size | Frame size | Rough opening | Qty | Disposition |
|------|-----------|------------|----------------|-----|-------------|
| Commercial windows | 32 x 91 in | **33.5 x 92.5 in** | **34.5 x 93.5 in** | 8 | **IN USE** |
| Gold walk-in cooler doors | 26 x 66 in | - | - | 6 | Set aside - solar-control low-E, wrong tool for this mission |
| Black walk-in cooler doors | 32 x 77 in | - | - | 2 | Hold in reserve - width matches commercial units |
| Full-lite door | on hand | - | - | 1 | East wall |

**Frame confirmed with flange excluded.** Rough opening = frame + 0.5 in shim per side. This is the dimension every wall calculation in this document now uses. Flange extension is unmeasured and does not affect the rough opening - it sets trim/flashing detail only, still open.

**Cooler doors rejected on the same logic as before:** framing cost is per opening, not per square foot, and low-E glass fights a passive-solar mission. Field test if reconsidered: flame reflection count in a dark spot; four even reflections is clear double pane, one dim/tinted reflection is low-E.

### Orientation

**South wall: HORIZONTAL.** 93.5 in wide x 34.5 in tall RO. A 91 in unit standing vertical needs 10 ft of wall, taller than the container and wrong roof direction - ruled out for this wall.

**East wall: VERTICAL**, both units. See East Wall section below for the full locked layout.

### Distribution

| Wall | Units | Orientation |
|------|-------|-------------|
| South | 4 | Horizontal, one per bay |
| East | 2 | Vertical, stacked with the door at the north end |
| East | 1 door | Full-lite |
| **Floating** | **1** | Unassigned |
| West | none | Solid wall, by decision |

### Glazing ratio

| Source | Area |
|--------|------|
| Salvaged glass, 6 assigned units | ~122 sq ft |
| Full-lite door | ~20 sq ft |
| Roof polycarbonate, 10 ft x 40 ft | 400 sq ft |
| **Total** | **~542 sq ft** |
| **Ratio against 736 sq ft floor** | **~74%** |

Four-season production wants 60-80%. Roof glazing is the only surface with enough area to reach ratio and the only surface that catches high summer sun.

---

## EAST WALL - FULLY LOCKED

Non-bearing. Runs 18 ft 5 in, tapering from the container-side height down to the south corner. (See Locked Geometry note above on which height figure applies where - the elevation drawing uses container-datum heights: 14 ft 6 in north, 7 ft 9 in south, matching the south wall's own beam-bearing datum at that shared corner.)

| Element | Position south of container | Sill | Head |
|---------|------------------------------|------|------|
| Vertical window 1 (W1) | 0 ft 6 in to 3 ft 4.5 in | 3 ft 6 in | 11 ft 4 in |
| **Gap** | 6 in | | |
| Vertical window 2 (W2) | 3 ft 10.5 in to 6 ft 9 in | 3 ft 6 in | 11 ft 4 in |
| Full-lite door | 11 ft 0 in to 14 ft 0 in | grade | 7 ft 4 in |

Both windows use the confirmed 34.5 x 93.5 in rough opening, mounted vertical.

**Clearance above W2's head at its south (low) jamb: 8.9 in.** Governing dimension for this wall - the south jamb is always the tight point on a tapered wall because the roofline is falling toward it. Header allowance: single 2x6 laid flat (1.5 in) plus a single raked top plate (1.5 in) = 3 in used, 5.9 in remaining. **This only works because the east wall is non-bearing** - no rafter load, so no doubled/on-edge header is required. If this wall's bearing status ever changes, W2 has to move or the sill has to drop.

**Shear panels, both clearing the 3 ft 6 in structural minimum:**
- Between W2 and the door: 4 ft 3 in
- South of the door: 4 ft 6 in

**Why this layout over the alternatives tried:** a stacked door/vertical/horizontal assembly does not fit this roofline at any position - the horizontal window's own width (7 ft 9 in) loses more wall height across its span than the taper can supply above an already-stacked vertical unit. Two verticals side by side, both lighting floor-to-head, was the layout that actually closed. The originally-planned horizontal unit is now the floating spare (see Glazing).

**Framing between W1 and W2:** each window is independently framed with king/jack studs; the 6 in gap between them is a single stud bay, not a shared post.

---

## WEST WALL - bearing, solid

No glass, by decision - west glazing dumps summer heat exactly when the building is fighting to shed it and earns nothing in any season. Takes the most wind (fill falls away). One chance in this building for a genuinely tight envelope.

| | |
|---|---|
| Glass | None |
| Door | Insulated, solid slab, near the north end (site constraint) |
| Insulation | 5.5 in closed cell, full cavity |

Natural home for thermal mass - the only wall where mass can stack against the interior face without blocking light. Unresolved.

---

## STRUCTURE

### Post and beam south wall

Wall does not carry the roof - posts and a continuous beam do, which makes every south window header non-structural infill.

| Element | Spec |
|---------|------|
| Bays | 4 at 10 ft 0 in |
| Posts | 6x6, five total, galvanized standoff bases |
| Beam | 6x12 solid Doug fir or larch, two 20 ft lengths spliced over the center post |
| Studs between posts | 2x6, 16 in centers, non-bearing |
| Window header | 2x6 racked to the top plate, carries nothing |

**NO ENGINEERED LUMBER ANYWHERE.** LVL/glulam/LSL/PSL are interior-dry-use products and will delaminate in greenhouse humidity. Built-up beams (triple 2x12) trap water in the seams and rot from inside. Solid sawn timber only. Posts on galvanized standoff bases, never bearing directly on concrete.

### Beam sizing at 50 psf

Required section modulus ~64 in3 for a 10 ft bay. 6x10 provides 83 in3 and would work; **6x12 (121 in3) is specified deliberately** for the margin, since rough-sawn green timber isn't graded to dimensional-lumber certainty. Steel rejected on fabrication/coating/equipment cost at this span.

### Rafters

2x12 at 16 in o.c., 31 total, 20 ft stock (bearing span 19 ft 8 in, span drives the size at either 50 or 60 psf - 2x10 does not make it). Birdsmouth bearing north on the riser top plate and south on the 6x12 beam, both cut to the roof pitch. Hurricane tie every rafter both ends. Solid 2x12 blocking at both bearing points.

**Overhang framed separately** - 20 ft stock covers the bearing span with nothing left for a tail; sub-fascia and outlookers after the roof is on.

**VERIFY 20 FT 2x12 AVAILABILITY** before the plan depends on it - likely a special order.

### Bearing assignment

North riser: yes. South (via post/beam): yes. West: yes. **East: NO - non-bearing**, easternmost rafter set inboard, roof carried past on lookouts. This is what makes the East Wall lock above possible - confirmed and load-bearing on the design now, not just convenient.

Non-bearing does not mean unloaded - full lateral wind pressure across a face that's mostly glass and door. Structural sheathing required, transferring to the roof diaphragm and foundation.

### Riser detail (on the container)

Stands on the container's **top side rail**, not the roof deck - the roof panel carries almost nothing and a rafter set on it would dent it.

1. Continuous steel angle sill, L3x3x0.25, bolted through the top rail every 24 in with backing plates.
2. Treated bottom plate on the angle, sill seal/butyl between - wood never touches steel dry.
3. 2x6 stud wall, 16 in centers, **5 ft 8 in tall**, doubled top plate.
4. Rafters birdsmouthed to 4.5:12 on the top plate, hurricane tie each.
5. Sheathing, weather barrier, metal siding.

Uplift: the angle-to-rail connection is the hold-down for the entire roof. Thermal break: 2 in closed cell over the steel, inside, lapping the rail - highest-value square footage on the job. Vent panels land in the top 2 ft of this wall.

---

## ROOF

10 ft polycarbonate south, 10 ft metal north, one lap seam, no cuts, on the 19 ft 8 in slope.

**Polycarbonate:** 8mm triple-wall, 10 panels at 4 x 10 ft, flutes running down-slope, UV face out, on purlins with oversized gasketed fastener holes for thermal movement (~0.25 in per 10 ft). Expect R-1.9 to R-2.0 - verify against the manufacturer sheet.

**Metal, north 10 ft:** solid sheathing, closed cell foam, metal panel - insulated deck, dark reservoir bay.

**Why 10 ft of poly, not the 8 ft the winter ray trace suggests:** exactly one panel, no waste, moves ratio from 65% to the mid-70s%. Buys shoulder-season/summer/diffuse light at the cost of winter night loss through R-1.9 glazing vs R-19+ metal.

**Phase 1: roof the entire slope in metal.** Poly's UV warranty clock starts at install and animal-year humidity/ammonia attacks the coating. Pull the south 10 ft of metal at conversion, drop poly into the pre-planned seam.

**Snow shed minimums:** heated poly 20-22 deg, unheated poly 28-30 deg, heated metal 18-20 deg, unheated metal 25-30 deg. Locked 4.5:12 (20.6 deg) clears the heated-poly minimum with margin, unlike the earlier 20.0 deg lock which sat exactly on the floor.

---

## INSULATION

**CLOSED CELL ONLY.** Open cell absorbs moisture in a greenhouse and rots the framing behind it.

| Surface | Depth | Result |
|---------|-------|--------|
| North riser | 5.5 in | R-35 |
| Container top rail, inside face | 2 in over the steel, lapping the rail | Kills the condensation line |
| West wall | 5.5 in | R-35 |
| Roof, north 10 ft metal | 5.5 in | R-35 |
| South wall, below sill | 3.5 in | R-22 |
| East wall, solid areas | 3.5 in | R-22 |
| Rims, plates, corners | 2 in | Seals bridges |
| Roof, south 10 ft poly | NOTHING | - |

South/east held to 3.5 in deliberately - can't out-insulate the R-2 glass directly above the framing, so the extra 2 in on those walls buys less than the same money spent on the footing/slab edge, which has nothing between it and frozen ground.

**Tell the foamer explicitly:** do not spray the south 10 ft of roof (phase-two poly section, mark it before he arrives) or the lap seam; do not skip the container top rail.

---

## INTERIOR FINISH

**Snow Coat white elastomeric over the foam, no interior metal panel, no drywall.** Bottom 4 ft gets temporary OSB wainscot for the animal years (elastomeric won't survive livestock contact or a pressure washer); everything above is two coats of Snow Coat. Fire rating not a factor - no code jurisdiction.

Trim foam flush before coating. Airless sprayer only, 3,000+ psi, 0.031-0.041 tip, Graco 390/490 class minimum. Temperature window ~50 F and rising, no freeze 24-48 hrs after - a summer application at 9,000 ft, building closed in first.

---

## VENTILATION

Fully passive, wax-cylinder actuated both ends, no power, no controls.

**Riser exhaust:** 8 panels, 4 x 2 ft, 64 sq ft, top 2 ft of the 5 ft 8 in riser, top-hinge outswing, fails closed.

**South intake:** 8 panels, 4 x 3 ft, 96 sq ft (1.5x exhaust - intake air moves slower, oversizing keeps flow from choking), below the sill in the 3 ft 8 in of framing above the footing, top-hinge outswing, fails closed. NOT placed between the south windows - the piers are too narrow and a tall intake there would short-circuit straight to the riser vents without reaching the growing zone.

**Panel construction, both locations:** Pro-Panel skin with ribs horizontal (parallel to hinge - stiffness where the bending is, and lets the gasket seal flat across the bottom rail), polyiso core with foam-safe adhesive only, aluminum perimeter frame with drip edge, EPDM gasket on the frame not the panel, cut with a nibbler or shears never an abrasive blade.

**VERIFY WAX CYLINDER LIFT AGAINST FINISHED PANEL WEIGHT** before ordering - an insulated metal panel is heavier than a typical greenhouse vent.

---

## HEAT

**Modine HD100AS0111** (full spec in `farm/garage-barn-build-sheet.md`). 100,000 BTU/hr input, ~52,000 BTU/hr delivered at 9,000 ft after altitude derate. **Altitude resolved 2026-08-14: handled at the gas valve spring only, no orifice hardware needed.**

**Load figures below predate the final envelope (736 sq ft, corrected sill/head geometry) and are NOT current** - recalculation is an open item, but the headroom margin (2.4x at the old numbers) makes it very unlikely the Modine is undersized even after correction.

| Loss path | BTU/hr |
|-----------|--------|
| Glazing | 12,100 |
| Insulated metal roof | 2,300 |
| End walls | 1,700 |
| Infiltration, altitude-adjusted | 6,200 |
| **Total (stale)** | **~22,000** |

---

## OPEN ITEMS

1. **Concrete volume.** Footing dimensions are set; calculate.
2. **Pen count and size.** Blocks pen slab area.
3. **Floating window.** One of eight commercial units unassigned - west wall (breaking the no-glass decision) or held spare.
4. **20 ft 2x12 availability.** Phone the yard.
5. **Window flange extension.** Unmeasured - sets trim/flashing detail, does not change the rough opening.
6. **Heat load recalculation** against the corrected 736 sq ft envelope and final glazing package.
7. **Thermal mass.** Design has essentially none. West wall interior face is the natural home. Unresolved.
8. **Stratification management.** Circulation fan or mass ducting - pitch does not solve it.
9. **Buried utilities.** Depth and routing before any excavation.
10. **Bed layout.** Inboard in the lit strip, walkway under the glass - exact geometry not set.
11. **Drainage and grading** around the pad perimeter.
12. **Rootstock agent definition.** Not committed.

---

## DRAWINGS

`farm/greenhouse-render-prompts.md` - tested exterior render prompts (south, north, east views) plus prompting lessons.

**East elevation, dimensioned PDF** - drawn to the geometry in this document. Not yet committed to the repo as a binary; delivered to Matt via present_files. Full elevation/section/plan set pending.

---

## DESIGN NOTES CARRIED FORWARD

- **Sill height does not change how much light you get. It changes where the light lands.** The lit strip is constant width; raising the sill slides it, doesn't shrink it.
- **Panel length sets depth**, not the reverse.
- **Framing cost is per opening, not per square foot** - killed the small cooler doors.
- **The riser translates to sill roughly one for one** and has bailed out multiple constraints across this design, including the final container-datum correction.
- **On a tapered wall, the south (low) jamb is always the governing clearance point** for any opening, regardless of where the opening starts.
- **Non-bearing wall status is now load-bearing on the design** - the East Wall's W2 clearance only works because that wall carries no rafter, and headers can stay flat/single-member.
- **The tall bay is a feature.** Warm air collecting at the peak against insulated mass under a metal roof is a reservoir and an ideal intake plenum.
- Chinese-style solar greenhouse (two-plane south face, steep glazed wall, night curtain) remains a live alternative, passed over not ruled out.
