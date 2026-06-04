# cal-widget.md — Calendar Widget Reference

**Filename convention:** `cal-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore. No wave reference in filename. `wave-4-5-widget-*` naming fully retired.
**Current version:** `cal-widget-v5.4.html`
**Cockpit URL:** `http://192.168.1.60:8080/cal-widget-current.html` — NEVER changes. `cal-widget-current.html` always mirrors latest version.
**Data sources:** `calendars.md` + `recipes-index.json` + `recipes/*.json` — all fetched live with `{cache:'no-store'}`

---

## Hard Gates

- **Stockyard S8 durability fix** — still open. No real flock data entry until fixed.
- **COCKPIT IS READ-ONLY.** No entry tool, no form, no keyboard on Cockpit. Ever.
- **NEVER patch data files to work around code bugs.** Fix the code.
- **Full rewrite only** — never surgical patches to widget HTML. Version up, full file.
- **Filename dots, never underscores.** `v5.4`, `v5.5` — no exceptions.

---

## Cockpit Hardware (locked)

- **Device:** PatientPoint P-WAL-230-ELC-02 — Android 13, 1920×1080, 4GB RAM. Kitchen, Ergotron arm.
- **Browser:** Fully Kiosk Browser. Start URL: `http://192.168.1.60:8080/cal-widget-current.html`
- **Fully Kiosk settings:** Auto-reload idle: 86400s. All 4 auto-reload triggers: ON. Cache clear on reload: ON. Web storage/history/cookies delete: OFF. Load current page on reload: OFF. Skip reload if showing start URL: OFF.
- **Server:** ThinkPad X1 Carbon `192.168.1.60`, Python HTTP server on `:8080`, repo at `C:\Users\ThinkPad X1 Carbon\Documents\family-ops`

## Cockpit Deploy Pattern (Option C, locked)

Every session close:
1. Build `cal-widget-vX.X.html`
2. `Copy-Item cal-widget-vX.X.html cal-widget-current.html`
3. `git add cal-widget-vX.X.html cal-widget-current.html` → commit → push
4. ThinkPad: `git pull`
5. Cockpit auto-refreshes via Fully Kiosk or manual reload — picks up new version. URL never changes.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.0–v2.8 | 2026-05-25/26 | Wave 4.5 — calendar core, categories, conflict detection, cook mode stub |
| v3.0 | 2026-05-27 | Cook Mode full build — tabs, recipe cards, timers, worn recipe card theme |
| v3.1–v3.5 | 2026-05-27 | Cook Mode recipe browser, manual timer, Kids Kitchen, servings, start recipe gate |
| v3.6–v3.9 | 2026-05-28 | Timer auto-pop, 2×2 layout, 3-section nav ribbon, snap-to-today, antique placard, scripture launch |
| v3.10 | 2026-05-29 | Two-layer nav family, 2-card cook center, Kids Kitchen → rail category, What's for Dinner added |
| v3.11 | 2026-05-29 | 96px bars, marquee padding, gold hardware, height parity all bottom bar buttons |
| v3.12 | 2026-05-29 | Cook Mode interior — servings bar, step layout, fonts, altitude, timer onclick, rail headers, emoji encoding |
| v4.0 | 2026-05-29 | Ingredient grid unified, snap-to-today double rAF fix, Cook Mode scroll anchor |
| v5.0 | 2026-06-01 | **Wave 6.5 — Meal Planner + Widget Integration.** [MEAL] tag parser, live recipe fetch, Meal Planner screen, What's for Dinner, Cook Mode splash, Coming Up rail, cancel= treatment, liturgical pill fix, span all-bottom stack |
| v5.1 | 2026-06-02 | **Wave 6.6 Chunk A.** `--cell-h` dynamic 5-row grid, dnum 40→28px, cell-hdr-h 54→38px, banner midpoint fix, adjacent month fill, night mode white flash fix, agent buttons 62→72px, month first/last row border suppression |
| v5.2 | 2026-06-02 | **Wave 6.6 Chunk B.** WFD rebuilt as month-view clone, week mode rebuilt (7-col events top / 7-col briefs bottom), Meal Planner rebuilt on buildWkRow, WebView sharpness CSS |
| v5.3 | 2026-06-02 | **Wave 6.6 Chunk C.** Meal Planner font 14px, timer padding reduced, auto-refresh every 3 min, rolling 4-row, conflict flag penalty removed, week/meal planner unlimited events |
| v5.4 | 2026-06-02 | **Wave 6.6 Chunk D.** Rolling 3-row / month+WFD 5-row split via `--cell-h`/`--cell-h-month`, `ROLL_MAX_EVENTS=7`, `MAX_EVENTS=4`, scroll restore on WFD/meal planner close, fixed 4-week arrow nav, refreshCalendar rolling fix |

---

## Wave Naming Convention (locked)

Wave numbers follow the **charter build order only**. No widget-specific wave numbering. Widget gets its own version number (`cal-widget-vX.X.html`) independent of wave.

- Wave 6.5 = Meal Planner + Widget Integration (shipped)
- Wave 6.6 = Cockpit hardware delivery + display optimization (shipped v5.1–v5.4)
- Wave 6.7+ = remaining open PQs (unit conversion, ALT tags, Kalea altitude override, etc.)

---

## Chunk Build Strategy (locked)

Frame changes ship and proof before interior changes. Never mix frame and interior in one build pass.

- **Frame:** top bar, bottom bar, heights, spacing, nav structure
- **Interior:** cook mode layout, timers, recipe rail, emojis, functional behavior

Build in chunks, verify on Cockpit hardware between chunks. Each chunk = one commit.

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

### Agent Buttons (v5.1)
Width: `72px` (bumped from 62px). Grid: `repeat(3, 72px)`. Labels: 6px Georgia uppercase, `white-space:nowrap`.

### Nav Arrow Buttons
`padding:5px; background:#1a1610; border-top/left:1.5px solid #54462e; border-right/bottom:solid #0c0a06; border-radius:12px;`
Face: `background:#252015; border-top:1px solid #4e4020; border-bottom:1px solid #060400; padding:10px 16px;`
Intentionally different from two-layer nav family.
**Arrow nav behavior (v5.4):** Rolling view jumps fixed 4 weeks per tap. Month view jumps by calendar month. Week view increments by 1 week.

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

### Timer Layout (v5.3)
2-column vertical. Col 1: first 6. Col 2: 7th+. State-sorted: running → idle → done → silenced. Rail: `224px` / `448px`.
Card padding reduced in v5.3 — 5 timers fit in single column before two-column expansion.

### Night Mode
`body.night-dim` covers all screens including `#week-briefs`. `filter:brightness(0.08); pointer-events:none`. `#night-wake` tap to wake.
All cells have explicit `background:var(--bg)` — no transparent cell backgrounds under filter (v5.1 fix).

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

### Per-View Cell Heights (v5.4, locked)
- **Rolling:** `--cell-h` = `floor((innerHeight - 96 - 96 - dhH) / 3)` ≈ 289px at 1080px. 3 rows visible. Set by `syncHdrH()`.
- **Month + WFD:** `--cell-h-month` = `floor((innerHeight - 96 - 96 - dhH) / 5)` ≈ 173px at 1080px. 5 rows always. Scoped via `#month-scr .cell` and `#dinner-scr .cell`.
- **Week + Meal Planner:** `height:100%` via layout class — not affected by CSS variables.
- Adjacent month days fill leading/trailing empty slots in month and WFD (dimmed date number, no events).
- First/last row border suppression: `nth-child(2)` cells no `border-top`; `nth-child(6)` row no `border-bottom`. Scoped to `#month-scr` and `#dinner-scr`.

### Per-View Event Caps (v5.4, locked)
- **Rolling:** `ROLL_MAX_EVENTS=7` — up to 7 events per cell, "+N more — tap" if exceeded
- **Month/WFD:** `MAX_EVENTS=4` — up to 4 events per cell
- **Week/Meal Planner:** `showAll=true` — all events shown, no cap, no "+N more" ever
- Conflict flag no longer penalizes event slot count (`maxEv` = `MAX_EVENTS` always, no `-1`)
- `maxEvts` param flows: `buildWkRow` → `renderCell`. Rolling passes `ROLL_MAX_EVENTS`; week/meal planner pass `undefined` (triggers `showAll`)

### Week Mode (v5.2, locked)
- **Top 50%:** `#weeks` — single `.wrow` × 7 `.cell`, same structure as rolling. Font: 14px, `white-space:normal`. Unlimited events, no truncation.
- **Bottom 50%:** `#week-briefs` — 7 `.wb-col` columns, one per day. Always visible. No tapping required. `buildBriefHtml()` populates each column.
- `applyWeekLayout()` positions `#cal-wrap` fixed, then calls `renderWeekBriefs()`. Both run on week switch and week navigation.
- Old `#week-detail` single-panel: hidden via `display:none!important` in week-layout CSS. Not removed from DOM.
- `clearWeekLayout()` removes `week-layout` class; `#week-briefs` hides automatically via CSS.

### Meal Planner (v5.2, locked)
- Rebuilt on `buildWkRow(mealPlannerWi, false, true)` — identical cell structure to rolling/week view
- Full height via `.mp-weeks{flex:1}` — no brief pane, no 55/45 split
- `[MEAL]` entries render as amber `mp-meal-evt` tiles via `isMealPlanner=true` flag in `renderCell`, appended to cell body after regular events
- Font: 14px (matching week mode), `white-space:normal` — wrapping enabled
- Day headers: `mgrid-dows` + `dhdr` — identical to month/WFD
- Banner: "Mon / Mon" for cross-month weeks; year shown
- Tap meal tile → Cook Mode with recipe (existing behavior)

### What's for Dinner (v5.2, locked)
- Rebuilt as month-view clone — identical structure: `mgrid-dows` + 5×`wrow` + `.cell`
- `renderDinnerCell(date, meals)` helper — same `.dnum`, feast days in `.hdr-slot`, today brackets identical to month view
- `#dinner-scr`: `padding:0; gap:0; overflow:hidden` — matches `#month-scr` exactly
- Meal tile uses `mp-meal-evt` class (amber, same as Meal Planner)
- Adjacent month fill: previous/next month days dimmed in leading/trailing slots
- Meals-only content — no regular events in cell body
- Read-only kids view. Left/right arrows page by month.
- Scroll position preserved when closing: `_overlayScrollY` saved on open, restored via `requestAnimationFrame` on close

### Cook Mode Splash (v5.0)
- Bible verse centered
- Today's planned meals (from [MEAL] entries) preloaded below verse as tappable recipe tiles
- Coming Up rail: next 1-2 days of planned meals live from allMeals

### Auto-Refresh (v5.3, locked)
- `refreshCalendar()` runs every 3 minutes via `setInterval`
- Re-fetches `calendars.md`, repopulates `allEvts`, `allMeals`, `allBriefs` via `parseSrc()`
- **Guards:** returns immediately if `cookOn || nightOn` — never interrupts Cook Mode or Night Mode
- Rebuilds current view **in place** — rolling preserves `window.scrollY`, no scroll reset
- Rolling refresh: rebuilds visible rows (`viewTopWi` → `viewBotWi`), restores scroll. **Does NOT call `render()`** — `render()` is week-mode-only
- Cook Mode: data updated silently in memory, no re-render until user exits Cook Mode

---

## Architecture

### Top bar
- Sticky, fixed height `--hh:96px` — enforced by `syncHdrH()`
- Left: wordmark placard
- Center: month/year banner; Cook Mode shows recipe name
- Right: egg card + agent grid (6 agents, 3×2, 72px buttons)

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

## Parked Questions (PQs)

PQs are future-session items — parked until conditions are right to address them. Never conflated with session work Items. Session Items are numbered Item 1, Item 2, etc. during intake and are worked and closed within the session.

| PQ | Description | Target |
|----|-------------|--------|
| PQ-03 | Egg count hardcoded 47 — pull from Stockyard | Wave 7 |
| PQ-04 | Agent buttons — wire to modules | Wave 6.7+ |
| PQ-06 | Saint panel — Mantel stub | Wave 6.7+ |
| PQ-22 | Liturgical data 2028-2035 | Phase 1 closeout |
| PQ-29 | Cook Mode vertical centering — requires browser devtools on live server | Cockpit phase |
| PQ-31 | Chow Hall post-cook altitude follow-up hook | Wave 6.7+ |
| PQ-32 | Phase 3 — voice timer start/stop | Phase 3 |
| PQ-34 | Unit conversion per ingredient — tap-to-convert, per-session | Wave 6.7+ |
| PQ-35 | Inline ALT tags per ingredient/step — requires recipe schema update | Wave 6.7+ |
| PQ-36 | Kalea altitude override — save per recipe, flag as user edit | Wave 6.7+ |
| PQ-PHASE2 | sessionStorage timer persistence on Home reload | Phase 2 |

**Closed this wave:** PQ-33 (WFD meal name — built v5.2), PQ-37 (week mode — rebuilt v5.2), PQ-38 (rolling rows — fixed v5.1/v5.4), PQ-39 (month 5 rows — fixed v5.1), PQ-40 (snap blip — verified non-issue on hardware)

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
- `--cell-hdr-h` — cell header height. `38px` (reduced from 54px in v5.1).
- `--cell-h` — rolling row height. Dynamic: `floor((innerHeight - 96 - 96 - dhH) / 3)`. ~289px at 1080px. Set by `syncHdrH()`.
- `--cell-h-month` — month/WFD row height. Dynamic: `floor((innerHeight - 96 - 96 - dhH) / 5)`. ~173px at 1080px. Set by `syncHdrH()`. Scoped to `#month-scr .cell` and `#dinner-scr .cell`.

`syncHdrH()` sets all variables and JS-matches left zone **minWidth** to right zone width.

### initRolling snap-to-today
Starts at `viewTopWi=-3`. Scrolls via double `requestAnimationFrame`. Snap blip verified non-issue on Cockpit hardware (PQ-40 closed).

### Overlay scroll preservation (v5.4)
`_overlayScrollY` saves `window.scrollY` when WFD or Meal Planner opens (hiding `#cal-wrap`). Restored via `requestAnimationFrame` on close. Prevents rolling view jumping to top (April) on overlay close.
