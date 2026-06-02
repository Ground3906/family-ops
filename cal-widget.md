# cal-widget.md — Calendar Widget Reference

**Filename convention:** `cal-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore. No wave reference in filename. `wave-4-5-widget-*` naming fully retired.
**Current version:** `cal-widget-v5.0.html`
**Served from:** `C:\dev\family-ops` via `python -m http.server 8080`
**Data sources:** `calendars.md` + `recipes-index.json` + `recipes/*.json` — all fetched live with `{cache:'no-store'}`

---

## Hard Gates

- **Stockyard S8 durability fix** — still open. No real flock data entry until fixed.
- **COCKPIT IS READ-ONLY.** No entry tool, no form, no keyboard on Cockpit. Ever.
- **NEVER patch data files to work around code bugs.** Fix the code.
- **Full rewrite only** — never surgical patches to widget HTML. Version up, full file.
- **Filename dots, never underscores.** `v5.0`, `v5.1` — no exceptions.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.0–v2.8 | 2026-05-25/26 | Wave 4.5 phase — calendar core, categories, conflict detection, cook mode stub |
| v3.0 | 2026-05-27 | Cook Mode full build — tabs, recipe cards, timers, worn recipe card theme |
| v3.1–v3.5 | 2026-05-27 | Cook Mode recipe browser, manual timer, Kids Kitchen, servings, start recipe gate |
| v3.6–v3.9 | 2026-05-28 | Timer auto-pop, 2×2 layout, 3-section nav ribbon, snap-to-today, antique placard, scripture launch |
| v3.10 | 2026-05-29 | Two-layer nav family, 2-card cook center, Kids Kitchen → rail category, What's for Dinner added |
| v3.11 | 2026-05-29 | 96px bars, marquee padding, gold hardware, height parity all bottom bar buttons |
| v3.12 | 2026-05-29 | Cook Mode interior — servings bar, step layout, fonts, altitude, timer onclick, rail headers, emoji encoding |
| v4.0 | 2026-05-29 | Ingredient grid unified, snap-to-today double rAF fix, Cook Mode scroll anchor |
| v5.0 | 2026-06-01 | **Wave 6.5 — Meal Planner + Widget Integration.** [MEAL] tag parser, live recipe fetch (empty fallback), Meal Planner screen (7-col week grid, Sunday anchor, amber meal tiles, cat emojis), What's for Dinner (calendar-native cells, amber tiles, feast days + birthdays), Cook Mode splash preloads today's meals, Coming Up rail live from [MEAL] entries, cancel=pending treatment, cancel=confirmed filter, skip= on CAL-RECUR, liturgical pill fix (timed events show pills), span all-bottom stack with _startDate sort, drop connectors at row level, wave naming unified to charter build order |

---

## Wave Naming Convention (locked)

Wave numbers follow the **charter build order only**. No widget-specific wave numbering. Widget gets its own version number (`cal-widget-vX.X.html`) independent of wave.

- Wave 6.5 = Meal Planner + Widget Integration (this wave)
- Wave 6.6+ = remaining widget items (unit conversion, ALT tags, week mode fix, etc.)

---

## Chunk Build Strategy (locked)

Frame changes ship and proof before interior changes. Never mix frame and interior in one build pass.

- **Frame:** top bar, bottom bar, heights, spacing, nav structure
- **Interior:** cook mode layout, timers, recipe rail, emojis, functional behavior

---

## Locked Design Decisions

### Two-Layer Nav Family Marquee
Outer shell: `#0c0a06` bg, `border-top/left: 2px solid #502e0c`, `border-right/bottom: solid #000`, `border-radius:3px`, `padding:3px`.
Inner face: `#6a3e10` bg, `border-top:1px solid #c07030`, `border-left:1px solid #a05a20`, `border-bottom:1px solid #180800`, `border-right:1px solid #2e1004`, `padding:12px 18px` (wordmark) / `padding:12px 28px` (month banner).
Corner hardware: `.hw` / `.hw9` — `rgba(240,200,128,0.6)` (gold at 60%), 2px stroke.
Wordmark: "Edelweiss Farms" `28px`, "Family Ops" `14px` right-justified, both `#f0c880`. Divider: `1px #f0c880 @ 40%`.
Month/year banner: month `58px`, year `18px`, both `#f0c880`.

### Two-Layer Nav Button Family
All nav/calendar buttons except Home/Cook/Night/arrows use this style.
Covers: Rolling/Week/Month, What's for Dinner, Meal Planner, agents.

### Nav Arrow Buttons
`padding:5px; background:#1a1610; border-top/left:1.5px solid #54462e; border-right/bottom:solid #0c0a06; border-radius:12px;`
Face: `background:#252015; border-top:1px solid #4e4020; border-bottom:1px solid #060400; padding:10px 16px;`
Intentionally different from two-layer nav family.

### Color Anchor
All Cook Mode text: `#f0c880`. Amber accent: `#f0c060`. No divergence.

### Recipe Accent Palette (10 colors)
```
['#2660a8','#b86010','#287860','#803050','#c04020','#604898','#208870','#c89010','#486cb0','#386828']
```

### Parchment Cards
SVG `feTurbulence` filter, `fractalNoise`, `baseFrequency="0.009 0.015"`, `numOctaves="4"`. Lightness: alpha `0.14`. Gradient: `#f5edd8 → #eee0b8 → #e4d098 → #d4bc78`. 8 burn patterns.

### Two-Card Cook Mode Center
Left card (flex:1 ~33%): ingredients + altitude collapsible. Right card (flex:2 ~67%): method steps.

### Servings Bar
Height: `52px`. Buttons: near-black Cook Mode family.

### Rail Headers
TIMERS and RECIPES: `height:52px`, Cook Mode family buttons. Visually unified 52px row across all three columns.

### Method Steps
Step number: `36px amber`. Bold title: `26px`. Body text: `24px`.

### Ingredients
Fixed `80px` quantity column. Two-column layout inside left card. Scrollable independently.

### Altitude Collapsible
Default: expanded. Strip at bottom of left card: teal `#287888`. Per-session per-tab state.

### Manual Timer
Dark shell. Timer card accent: teal `#287888`. "Create" button → idle card → Start from card.

### Timer Done Behavior
Done state: "🔕 Silence" + X. Silenced: "Silenced" + X. X always visible in done/silenced.

### Timer Layout
2-column vertical. Col 1: first 6. Col 2: 7th+. State-sorted: running → idle → done → silenced. Rail: `224px` / `448px`.

### Night Mode
`body.night-dim` covers all screens. `filter:brightness(0.08); pointer-events:none`. `#night-wake` tap to wake.

### Float Bar
Fixed `220px`. Timers stack top-to-bottom. Tap snaps to Cook Mode.

### Scripture Quote
`font-size:52px`. `max-width:1050px`. Centered on launch screen.

### Span Rendering — All-Bottom Stack (v5.0, locked)
- All spans stack at bottom, sorted by `_startDate` ascending — oldest span = s0 (very bottom)
- Mid days: thin bar (7px) at slot position, stacked tight, black separator between slots
- Departure day: full bracket at slot position, bars above may overlap visually
- Return day: bracket at slot, higher bars pass through at higher z-index (opaque pass-through)
- Drop connectors: 4px vertical colored line on right cell border when bar changes slot between adjacent days — rendered at row level in `buildWkRow`, never clipped
- `_startDate` preserved on all expanded span events
- `_spanSlotMap` populated per-day for connector calculation

### cancel= Treatment (v5.0, locked)
- `cancel=pending`: warm bg `#1c1814`, dashed warm border `rgba(160,120,80,.30)`, 2px amber strikethrough, ⊘ right, no pills, no time — full opacity
- `cancel=confirmed`: filtered from parser entirely, line stays in `calendars.md` as audit trail

### Liturgical Pill Logic (v5.0, locked)
- All-day liturgical events: pills suppressed (feast days, Holy Days)
- Timed liturgical events (Serve at Mass): pills render normally

### Meal Planner (v5.0, locked)
- 7-column week grid, full height, no brief pane
- Sunday anchor, current week on open, left/right arrows page by week
- Calendar events in normal treatment; [MEAL] entries in amber (meals) or teal (prep steps)
- Recipe title prefix on prep steps: "Bread: proof 07:00"
- Tap meal → Cook Mode preloaded with that recipe
- All event text: 20px. Pills: 14px, padding bumped (MP-scoped only)
- Category emojis render on calendar events
- Today column: highlighted background + cream date number

### What's for Dinner (v5.0, locked)
- Calendar-native cells — same date header (40px dnum), feast days + birthdays in header slot, today bracket corners
- Dinner meals only (meal-type=dinner); one entry max for now
- Amber raised tile: `background:#201c18; border-left:3px solid #c87818`
- Meal name: `font-family:Georgia,serif; font-size:15px; font-weight:700; color:#f0c880; white-space:normal; word-break:break-word`
- Empty days: blank — no placeholder
- Left/right arrows page by month
- Read-only — kids view

### Cook Mode Splash (v5.0)
- Bible verse centered
- Today's planned meals (from [MEAL] entries) preloaded below verse as tappable recipe tiles
- Coming Up rail: next 1-2 days of planned meals live from allMeals

---

## Architecture

### Top bar
- Sticky, fixed height `--hh:96px` — enforced by `syncHdrH()`
- Left: wordmark placard
- Center: month/year banner; Cook Mode shows recipe name
- Right: egg card + agent grid (6 agents, 3×2)

### Nav ribbon — 3 fixed sections
- **Left:** What's for Dinner + Meal Planner
- **Center:** ← Home **Cook Mode** Night →
- **Right:** Rolling / Week / Month

### Cook Mode layout
- **Left rail:** Timer stack + manual timer (fixed bottom)
- **Center:** servings bar (52px sticky) + 2-card area
- **Right rail:** Recipe browser (categories 18px, entries 14px); Kids Kitchen pinned bottom; Coming Up pinned top

---

## Pill Colors (locked)

```
D=#9a5828  K=#1a50e0  W=#cc2233  M=#9944cc  R=#f040b8
C=#2070b8  E=#156e2a  B6=#faa030  OMA=#7755cc  PAPA=#6ec898
GUEST=#E8DFC0  FAM=#7a7aaa  KIDS=#a0c840
```

`B6_ACTIVE=false` — flip post-birth (~2026-08-15).

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

Emoji must use Unicode escape sequences in JS or HTML entities — never raw emoji in Python heredocs.

---

## calendars.md Schema

### Entry formats

```
[CAL] YYYY-MM-DD HH:MM [PILLS] Title :: category :: opt=val
[CAL] YYYY-MM-DD ALL-DAY [PILLS] Title :: category :: opt=val
[CAL-RECUR weekly start=YYYY-MM-DD day=dow skip=YYYY-MM-DD,...] HH:MM [PILLS] Title :: category :: opt=val
[BRIEF] YYYY-MM-DD [AgentName] text
[MEAL] YYYY-MM-DD HH:MM Title :: recipe-id=X :: meal-type=dinner/breakfast/lunch/prep
```

### Supported options

| Option | Values | Notes |
|--------|--------|-------|
| end= | HH:MM | Required for auto-conflict detection |
| flag=true | boolean | Holy Days, unresolved logistics only |
| optional=true | boolean | Zero conflict weight. Daily Mass only. |
| travel=true | boolean | Person physically away. Triggers pill suppression. |
| span= | YYYY-MM-DD | End date for multi-day span |
| tentative=true | boolean | Diagonal amber stripe hatching |
| cancel=pending | string | Strikethrough, ⊘, warm bg, no pills. Awaiting confirmation. |
| cancel=confirmed | string | Filtered from parser. Line preserved as audit trail. |
| skip= | YYYY-MM-DD,... | CAL-RECUR only. Suppresses specific dates. |
| stripe=appt | string | Red-tinted appointment background |
| location= | "string" | Day panel detail |
| notes= | "string" | Day panel detail |
| vehicle= | tahoe/dodge/nv | Punch List vehicle assignment |
| driver= | pill code | Punch List driver assignment |

### Recurring entry doctrine (locked)
Only two CAL-RECUR entries permitted: Sunday Mass 08:00 and Daily Mass Wed 10:00. Everything else = individual [CAL] entries. CAL-RECUR for seasonal events is forbidden.

---

## Open Items (active)

| Item | Description | Target |
|------|-------------|--------|
| Item-03 | Egg count hardcoded 47 — pull from Stockyard | Wave 7 |
| Item-04 | Agent buttons — wire to modules | Wave 6.6+ |
| Item-06 | Saint panel — Mantel stub | Wave 6.6+ |
| Item-22 | Liturgical data 2028-2035 | Phase 1 closeout |
| Item-31 | Chow Hall post-cook altitude follow-up hook | Wave 6.6+ |
| Item-32 | Phase 3 — voice timer start/stop | Phase 3 |
| Item-34 | Unit conversion per ingredient — tap-to-convert, per-session | Wave 6.6 |
| Item-35 | Inline ALT tags per ingredient/step — requires recipe schema update | Wave 6.6 |
| Item-36 | Kalea altitude override — save per recipe, flag as user edit | Wave 6.6 |
| Item-37 | Week mode rendering — broken, deep dive needed | Wave 6.6 |
| Item-38 | Rolling view too many rows on Cockpit hardware — diagnose on final hardware | Cockpit phase |
| Item-39 | Month view 5 rows not filling full screen height | Wave 6.6 |
| Item-40 | Home/Rolling snap blip — cosmetic, diagnose on final hardware | Cockpit phase |
| Item-PHASE2 | sessionStorage timer persistence on Home reload | Phase 2 |
| Item-DN-1 | What's for Dinner meal name font/style — render and lock | Wave 6.6 |

---

## Stockyard S8 Hook (HARD GATE)

Auto-export to repo via GitHub MCP. Blocks real flock data entry. Not built. Not bypassed. Surface every session.

---

## calendars.md Reversion Watch

Three categories that have reverted across session rewrites — verify on every rewrite:
- **Knights of Columbus** → must be `meetings`
- **Fairboard meeting** → must be `meetings`
- **Fair cleanup** → must be `4h`

---

## CSS Variables

- `--hh` — header height. Fixed `96px`, enforced by `syncHdrH()`.
- `--nh` — nav height. Fixed `96px`.
- `--cell-hdr-h` — cell header height (`54px` fixed).

`syncHdrH()` sets both to fixed values and JS-matches left zone **minWidth** to right zone width. Never measures `#hdr` or `#bottom` offsetHeight.

### initRolling snap-to-today
Starts at `viewTopWi=-3`. Scrolls via double `requestAnimationFrame`. Single cosmetic blip remains (Item-40).
