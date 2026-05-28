# wave-4-5-widget.md — Calendar Widget Reference

**Current version:** v3.7 (shipped 2026-05-28, known issues — v3.8 in design)
**Filename convention:** `wave-4-5-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore
**Status:** Wave 6.5 shipped. v3.7 has known rendering issues. v3.8 spec complete.
**Served from:** `C:\dev\family-ops` via `python -m http.server 8080`
**Data source:** `calendars.md` in same directory — fetched live on load

---

## Hard Gates

- **Stockyard S8 durability fix** — still open. No real flock data entry until fixed.
- **COCKPIT IS READ-ONLY.** No entry tool, no form, no keyboard on Cockpit. Ever.
- **NEVER patch data files to work around code bugs.** Fix the code. Log as PQ.
- **Full rewrite only** — never surgical patches to widget HTML. Version up, full file.
- **Filename dots, never underscores.** `v3.6`, `v3.7`, `v3.8` — no exceptions.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.0–v2.8 | 2026-05-25/26 | Wave 4.5 phase — calendar core, categories, conflict detection, cook mode stub |
| v3.0 | 2026-05-27 | Cook Mode full build — tabs, recipe cards, timers, worn recipe card theme |
| v3.1 | 2026-05-27 | Cook Mode recipe browser left rail, manual timer, step index |
| v3.2 | 2026-05-27 | Worn recipe card Option A locked, Kids Kitchen, float bar |
| v3.5 | 2026-05-27 | Ingredient tabs removed, recipe name bar removed, Start Recipe gates timers, servings reset |
| v3.6 | 2026-05-28 | Timer auto-pop fix, 2×2 recipe card layout, 3-section nav ribbon, rail swap (timers left/recipe browser right), farmhouse buttons, goHome snap-to-today, 5-row month cap, dual-month banner, Daily Mass zero conflict weight |
| v3.7 | 2026-05-28 | Option E antique placard on wordmark + month banner, Kids Kitchen text cream/amber, scripture launch screen, JS ribbon width matching, float bar bottom-left, tap-to-snap Cook Mode, horizontal timer flow, 🍴 float branding, recipe color accent on all 5 elements, dual-month banner fix |

---

## v3.8 Spec (26 items — next build)

### Group 1 — Critical bugs
1. Night button broken — does nothing
2. Timers stacking before horizontal expansion (z-index/layout issue)
3. Week view brief row layout didn't render — looks identical to v3.6
4. Timer cards not picking up recipe color (tab got it, timer cards didn't)

### Group 2 — Layout/structure
5. Header area — marquee made everything smaller; needs bigger, more top/bottom padding
6. Month view — doesn't fill vertical space; must auto-size center area between top and bottom ribbon
7. Timer layout — 2 fixed columns; col 1 fills top-to-bottom (5 timers); col 2 appears on 6th, collapses when empty

### Group 3 — Theming pass
8. Marquee — more 3D physical patch feel, sewn-on look, not integrated/modern
9. Wordmark — logo + wordmark in single unified marquee (logo inside, not outside)
10. Recipe card background — burnt cream, not white; timers match same color
11. Servings bar background — brownish with gold/cream border
12. Recipe accent colors — current blue too aggressive against cream; needs subtler palette

### Group 4 — Button styling
13. Servings +/−, Hide Ref, Start Recipe — exact match to Edelweiss Meal Planner button
14. Kids Kitchen button — exact match to Rolling/Week/Month button styling
15. Agent buttons top right — exact match to Rolling/Week/Month button styling
16. Manual timer strip — fixed width (no bounce), more button-y feel

### Group 5 — Typography
17. Rail headers — double current size
18. Right rail categories — double current size
19. Scripture quote — bigger

### Group 6 — Feature fixes that didn't land from v3.7
20. Ingredients card — 2-column, quantity left/name right, larger font
21. Altitude card — same treatment as ingredients
22. Tab colors persist on ALL open tabs (not just active)

### Group 7 — Launch screen
23. Remove 3 seeded recipes from center — right rail handles browsing
24. Remove "browse recipes" prompt text

### Group 8 — Float bar
25. Single boxed unit, semi-transparent, "Cook Mode Timers" label, all timers inside with color markers
26. Recipe name tag on timer cards — remove it, color band only

---

## Architecture (v3.6+)

### Nav ribbon — 3 fixed sections
- **Left (.nav-left-zone):** Kids Kitchen — width JS-matched to right section via `syncHdrH()`
- **Center (.nav-center-zone, flex:1):** ← Home **Cook Mode** Night → — Cook Mode anchored dead center always
- **Right (.nav-right-zone):** Rolling / Week / Month — sets section width ruler

### Cook Mode layout
- **Left rail (#cm-left):** Timer stack — flows horizontally, fixed 200px card width, expands to 2 columns at 6+ timers
- **Center (#cm-center):** 2×2 recipe card grid — sticky servings bar + frozen top row (Ingredients | Altitude) + method cards
- **Right rail (#cm-right):** Recipe browser

### Recipe color system
- 6 colorblind-safe accent colors (blue/orange/purple/teal family)
- Assigned dynamically when recipe tab opens, released on close, recycled
- Applies to: recipe tab, all 4 center cards (ingredients, altitude, method ×2), timer cards
- Color band: left + top border accent only

### Servings bar (v3.6)
- SERVINGS label left (dotted underline = tap to reset to Chow Hall default, half-step increments)
- FAMILY: 7 center
- Hide Ref + Start Recipe right

### Float bar (v3.7)
- Position: bottom left, fixed above nav
- Contains: all active/done timers with recipe color accent + Cook Mode return button (🍴)
- Tap any timer chip → snaps to Cook Mode on that recipe

### goHome behavior (v3.6)
- Always resets to rolling view, snaps to today
- No page reload — calls `initRolling()` only

### Month view (v3.6)
- Hard 5-row cap — overflow days appear as leading days in next month's grid
- Auto-fills vertical space between header and nav (v3.8 fix pending)

### Banner behavior (v3.7)
- Rolling/week: "Month / Month" only when visible week actually spans two calendar months
- Month view: single month only, never slash

### Daily Mass display rules (v3.6)
- `optional=true` on the CAL-RECUR entry
- Zero conflict weight — excluded from auto-conflict detection
- Bumps first when day is full — shows when space allows, drops silently when not
- Appears in daily brief regardless

---

## Pill Colors (locked)

```
D=#9a5828  K=#1a50e0  W=#cc2233  M=#9944cc  R=#f040b8
C=#2070b8  E=#156e2a  B6=#faa030  OMA=#7755cc  PAPA=#6ec898
GUEST=#E8DFC0  FAM=#7a7aaa  KIDS=#a0c840
```

`B6_ACTIVE=false` — flip post-birth (~2026-08-15). Gates B6 pill display everywhere.

---

## Category Emoji Map (locked)

| Cat key | Emoji | Use |
|---------|-------|-----|
| liturgical | ✝️ | Feast days, Holy Days, Mass |
| kids | 🚸 | Kids events, swim practice, Faith Formation |
| family | 🏠 | Whole-family events, swim meets |
| animals | 🐾 | Farm/animal events |
| appointments | ➕ | Medical, dental, therapy |
| 4h | 🍀 | 4H events, fair |
| rootstock | 🌱 | Garden, orchard |
| prompt | ⏰ | Reminders, milestone pings |
| meetings | 📋 | KoC, Fairboard, any recurring meeting |
| misc | (none) | Catch-all |

---

## calendars.md Schema

### Entry formats

```
[CAL] YYYY-MM-DD HH:MM [PILLS] Title :: category :: opt=val :: opt=val
[CAL] YYYY-MM-DD ALL-DAY [PILLS] Title :: category :: opt=val
[CAL-RECUR weekly start=YYYY-MM-DD day=dow] HH:MM [PILLS] Title :: category :: opt=val
[BRIEF] YYYY-MM-DD [AgentName] text
```

### Supported options

| Option | Values | Notes |
|--------|--------|-------|
| end= | HH:MM | Event end time. Required for auto-conflict detection |
| flag=true | boolean | Holy Days, unresolved logistics, unconfirmed dates only |
| optional=true | boolean | Zero conflict weight, bumps first, use for Daily Mass |
| travel=true | boolean | Person physically away. Triggers pill suppression |
| span= | YYYY-MM-DD | End date for multi-day span |
| tentative=true | boolean | Diagonal stripe hatching |
| stripe=appt | string | Red-tinted appointment background |
| location= | "string" | Renders in day panel detail |
| notes= | "string" | Renders in day panel detail |
| vehicle= | tahoe/dodge/nv | Punch List vehicle assignment |
| driver= | pill code | Punch List driver assignment |

### Recurring entry doctrine (LOCKED)

**Only two CAL-RECUR entries permitted:**
- Sunday Mass 08:00 — never changes, never has exceptions
- Daily Mass Wed 10:00 — optional=true, always loses to other events

**Everything else = individual [CAL] entries.**

---

## Auto-Conflict Detection (v2.4+)

Widget scans each day for family pill + time window overlap. No manual flag=true needed for scheduling conflicts. Optional events excluded from detection.

---

## Brief Color Doctrine

| Row type | Color | CSS class |
|----------|-------|-----------|
| Conflict (auto or manual) | #ff5000 orange-red | brief-conflict |
| Vehicle/driver | var(--cb) gold | brief-vehicle |
| Appointment | #c86878 muted rose | brief-appt |
| Travel/departure | #4aa8d4 blue | brief-travel |

---

## CSS Variables

- `--hh` — header height. Set by `syncHdrH()` on init + resize.
- `--nh` — nav height. Set by `syncHdrH()` on init + resize.
- `--cell-hdr-h` — cell header height (54px fixed).

---

## Open PQs (active)

| PQ | Description | Wave |
|----|-------------|------|
| PQ-22 | Liturgical data 2028-2035 | Phase 1 closeout |
| PQ-03 | Egg count hardcoded 47 — pull from stockyard:eggs-log | 4.6 |
| PQ-04 | Agent buttons — wire to modules | 4.6 |
| PQ-06 | Saint panel — Mantel stub | 4.6 |
| PQ-11 | Meal Planner full view — Chow Hall | 4.6 |
| PQ-30 | Wire RECIPES[] to live fetch from recipes/*.json | 4.6 |
| PQ-31 | Chow Hall post-cook altitude follow-up hook | 4.6 |
| PQ-32 | Phase 3 — voice timer start/stop | Phase 3 |
| PQ-33 | Nav ribbon left section width — currently JS matched, verify on resize | 3.8 |
| PQ-PHASE2 | sessionStorage timer persistence on Home reload | Phase 2 |

---

## Stockyard S8 Hook (HARD GATE)

Auto-export to repo via GitHub MCP. Blocks:
- Real flock data entry in Stockyard widget
- Wave 4.5 calendar integration

Not built. Not bypassed. Surface every session.

---

## PK Cleanup Required

- `wave-4-5-widget-v3_5.html` in PK must be renamed to `wave-4-5-widget-v3.5.html`
- Underscore filename is the root cause of v3_6 naming drift
