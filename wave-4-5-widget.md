# wave-4-5-widget.md — Calendar Widget Reference

**Filename convention:** `wave-4-5-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore
**Served from:** `C:\dev\family-ops` via `python -m http.server 8080`
**Data source:** `calendars.md` in same directory — fetched live on load

---

## Hard Gates

- **Stockyard S8 durability fix** — still open. No real flock data entry until fixed.
- **COCKPIT IS READ-ONLY.** No entry tool, no form, no keyboard on Cockpit. Ever.
- **NEVER patch data files to work around code bugs.** Fix the code. Log as PQ.
- **Full rewrite only** — never surgical patches to widget HTML. Version up, full file.
- **Filename dots, never underscores.** `v3.10`, `v3.11` — no exceptions.

---

## Chunk Build Strategy (Locked)

Frame changes ship and proof before interior changes. Never mix frame and interior in one build pass.

- **Frame:** top bar, bottom bar, heights, spacing, nav structure
- **Interior:** cook mode layout, timers, recipe rail, emojis, functional behavior

Proof frame on 34" first. Interior builds on confirmed frame only.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.0–v2.8 | 2026-05-25/26 | Wave 4.5 phase — calendar core, categories, conflict detection, cook mode stub |
| v3.0 | 2026-05-27 | Cook Mode full build — tabs, recipe cards, timers, worn recipe card theme |
| v3.1 | 2026-05-27 | Cook Mode recipe browser left rail, manual timer, step index |
| v3.2 | 2026-05-27 | Worn recipe card Option A locked, Kids Kitchen, float bar |
| v3.5 | 2026-05-27 | Ingredient tabs removed, recipe name bar removed, Start Recipe gates timers, servings reset |
| v3.6 | 2026-05-28 | Timer auto-pop fix, 2×2 recipe card layout, 3-section nav ribbon, rail swap, farmhouse buttons, goHome snap-to-today, 5-row month cap, dual-month banner, Daily Mass zero conflict weight |
| v3.7 | 2026-05-28 | Option E antique placard, Kids Kitchen text, scripture launch screen, JS ribbon width matching, float bar, tap-to-snap Cook Mode, horizontal timer flow, recipe color accent |
| v3.8 | 2026-05-29 | 26-item spec pass — night mode all layers, copper plate Option D marquee, parchment cards, 2-col timers, color unification, servings bar amber |
| v3.9 | 2026-05-29 | Top bar fill, high-contrast palette, burn pattern randomization, inline method steps, ingredients alignment |
| v3.10 | 2026-05-29 | Two-layer nav family, fixed bars, 2-card cook center (ingredients+altitude / method), Kids Kitchen removed→rail category, What's for Dinner added, timer silence behavior, altitude collapsible, near-black cook buttons |
| v3.11 | 2026-05-29 | Frame pass: 96px bars, marquee 12px padding, gold corner hardware 60%, 58px month font, agent button cleanup, height parity all bottom bar buttons, arrow revert, scrollbar-gutter stable |

---

## Locked Design Decisions

### Two-Layer Nav Family Marquee (v3.10+)
Outer shell: `#0c0a06` bg, `border-top/left: 2px solid #502e0c`, `border-right/bottom: solid #000`, `border-radius:3px`, `padding:3px`.
Inner face: `#6a3e10` bg, `border-top:1px solid #c07030`, `border-left:1px solid #a05a20`, `border-bottom:1px solid #180800`, `border-right:1px solid #2e1004`, `padding:12px 18px` (wordmark) / `padding:12px 28px` (month banner).
Corner hardware: `.hw` / `.hw9` — `rgba(240,200,128,0.6)` (gold at 60%), 2px stroke.
Wordmark: "Edelweiss Farms" `28px`, "Family Ops" `14px` right-justified, both `#f0c880`. Divider: `1px #f0c880 @ 40%`.
Month/year banner: month `58px`, year `18px`, both `#f0c880`.

### Two-Layer Nav Button Family (v3.10+)
All nav/calendar buttons except Home/Cook/Night/arrows use this style:
`padding:4px; background:#0c0a06; border-top/left:1.5px solid #502e0c; border-right/bottom:solid #000; border-radius:10px;`
Inner face: `background:#6a3e10; border-top:1px solid #c07030; border-left:1px solid #a05a20; border-bottom:1px solid #180800; border-right:1px solid #2e1004;`
Covers: Rolling/Week/Month, What's for Dinner, Meal Planner, agents.

### Nav Arrow Buttons (v3.9 style, locked v3.11)
`padding:5px; background:#1a1610; border-top/left:1.5px solid #54462e; border-right/bottom:solid #0c0a06; border-radius:12px;`
Face: `background:#252015; border-top:1px solid #4e4020; border-bottom:1px solid #060400; padding:10px 16px;`
Label: `color:var(--cb); opacity:.85;`
These do NOT use the two-layer nav family. Intentionally different.

### Color Anchor
All Cook Mode text: `#f0c880`. Amber accent: `#f0c060`. No divergence.

### Recipe Accent Palette (10 colors, high-contrast)
```
['#2660a8','#b86010','#287860','#803050','#c04020','#604898','#208870','#c89010','#486cb0','#386828']
```
Timer card borders: `border-left:5px solid ${rc}; border-top:4px solid ${rc}`.
Tab borders: `border-left:5px solid ${rc}; border-top:4px solid ${rc}`.
Manual timer accent: teal `#287888`.
Tab colors persist on ALL open tabs — full color regardless of active state.

### Parchment Cards
SVG `feTurbulence` filter, `fractalNoise`, `baseFrequency="0.009 0.015"`, `numOctaves="4"`.
Lightness: `feColorMatrix` alpha `0.14`.
Gradient base: `#f5edd8 → #eee0b8 → #e4d098 → #d4bc78`.
Burn patterns: 8 variations in `_burnPatterns[]`, assigned by `seed % 8`.
`_paperSeeds`, `_paperSeedIdx`, `_burnPatterns` always declared together — never split.
Color accent bar (border-left/top) fixed to card frame — does NOT scroll with content.

### Two-Card Cook Mode Center (v3.10+)
Replaces 4-card 2×2 grid. Layout: `display:flex; flex:1; gap:10px; padding:10px; overflow:hidden; min-height:0`.
- **Left card (flex:1 ~33%):** ingredients (scrollable) + altitude collapsible (fixed bottom). Both elements inside overflow:hidden card with parchment bg.
- **Right card (flex:2 ~67%):** all method steps, full card width, scrollable. Parchment bg fixed to frame.
Frozen top row: GONE. Ingredients and altitude live in left card only.

### Servings Bar (v3.10+)
Horizontal layout: Servings label | − | count | + | spacer | Start Recipe.
Height: `52px`, same as rail headers.
Buttons: near-black Cook Mode family — `background:#0c0a06; border-top:1px solid #c07830; border-left:1px solid #a05a20; border-right:1px solid #3a1808; border-bottom:3px solid #1e0e04; border-radius:8px; color:#f0c060;`
Family:7 REMOVED. Hide References REMOVED.

### Rail Headers (v3.10+)
TIMERS and RECIPES: `height:52px`, Cook Mode family buttons (`#0c0a06`, `#c07830` copper borders).
TIMERS header inside left rail. RECIPES header inside right rail. Both 52px — visually unified row across all three columns.

### Method Steps (v3.10+)
Step number: `36px amber`. Bold title: `26px`. Body text: `24px`. All inline on one line.
Text wraps naturally when body exceeds card width.
ALT tags inline at `13px teal #287888` (pending PQ-35 recipe schema update).

### Ingredients (v3.10+)
Fixed `80px` quantity column, right-aligned, bold. `12px` gap. Names left-aligned `13px`.
Two-column layout inside left card. Scrollable independently.

### Altitude Collapsible (v3.10+)
Default: expanded (`cmAltExpanded[tabIndex] = false` on init → toggle shows content).
Strip at bottom of left card: "Altitude — 9,000 ft · N adjustments" in teal `#287888`.
Tap: toggles expanded/collapsed. Per-session per-tab state.
ALT badge: `8px`, teal background, "ALT" label. Per-step/per-ingredient inline ALT deferred to PQ-35.

### Manual Timer (v3.10+)
Dark shell restored: `background:#120e08; border-top:2px solid #c07830; border-left:2px solid #a05a20; border-right:2px solid #3a1808; border-bottom:3px solid #000; border-radius:10px;`
Buttons inside: Cook Mode near-black family (`#0c0a06`).
"Create" button — creates idle card in stack. User hits Start from card.
Timer card accent color: teal `#287888` (border-left 5px + border-top 4px).

### Timer Done Behavior (v3.10+)
Done state: shows "🔕 Silence" button (card stays visible) + X button.
Silenced state: "Silenced" text + X button.
X always visible in done/silenced states — full dismiss.
One tap on done = silence only (was: dismiss). Card persists until X.

### Timer Layout
2-column vertical. Col 1: first 6 timers. Col 2: 7th+, collapses when empty.
State-sorted: running → idle → done → silenced.
Rail: `224px` (1 col) / `448px` (2 col).

### Night Mode
`body.night-dim` covers: `#hdr`, `#dhdrs`, `#cal-wrap`, `#bottom`, `#cook-scr`, `#dinner-scr`, `#month-scr`, `#meal-scr`, `#week-detail`.
`filter:brightness(0.08); pointer-events:none` on all.
`#night-wake`: `position:fixed; inset:0; z-index:999; cursor:pointer`. Tap to wake.

### Float Bar
Fixed `220px` wide. Timers stack top-to-bottom. Tap anywhere snaps to Cook Mode. Label: "Cook Mode Timers".

### Scripture Quote
`font-size:52px`. `max-width:1050px`. Centered on launch screen.

---

## Architecture (v3.11)

### Top bar
- Sticky, fixed height `--hh:96px` — enforced by `syncHdrH()`, never measured
- Left: wordmark placard — two-layer nav family, fills bar height
- Center: month/year banner — two-layer nav family; Cook Mode shows recipe name; dual-month slash when rolling week spans two months
- Right: egg card + vdiv + agent grid (6 agents, 3×2 grid, 62px equal-width columns)
- Meal Planner button moved to bottom bar left zone (v3.10)

### Nav ribbon — 3 fixed sections
- **Left (.nav-left-zone):** What's for Dinner + Meal Planner — width JS-matched to right section via `syncHdrH()`
- **Center (.nav-center-zone, flex:1):** ← Home **Cook Mode** Night → — Cook Mode anchored dead center always
- **Right (.nav-right-zone):** Rolling / Week / Month — sets section width ruler

### Height parity (v3.11)
All bottom bar buttons match Home/Night height: What's for Dinner, Meal Planner, Rolling, Week, Month.
Cook Mode: cream face, intentionally different.
Arrows: intentionally smaller, v3.9 style.

### Cook Mode layout (v3.10+)
- **Left rail (#cm-left):** Timer stack (2-col, expands at 7) + manual timer cluster (fixed bottom, dark shell)
- **Unified visual row (52px):** TIMERS header (left rail) | servings bar (center) | RECIPES header (right rail) — all 52px, visually aligned
- **Center (#cm-center):** servings bar (sticky 52px) + 2-card area (left: ingredients+altitude | right: method steps)
- **Right rail (#cm-right):** Recipe browser (categories 18px, entries 14px); Kids Kitchen pinned bottom; Coming Up pinned top

### Recipe color system
- 10 high-contrast accent colors assigned dynamically per tab
- Applies to: recipe tab, left card, right card, timer cards
- Manual timer: teal `#287888`

### Kids Kitchen
- Page removed (v3.10). Lives as a category in the recipe rail right side (pinned bottom).
- "What's for Dinner?" nav button replaced Kids Kitchen nav button.

### Float bar
- Position: bottom left, fixed above nav, `220px` wide
- Timers stack vertically, tap snaps to Cook Mode

### goHome behavior
- Always resets to rolling view, snaps to today
- No page reload — calls `initRolling()` only, clears all overlays

### Month view
- Hard 5-row grid, fills vertical container
- `flex:1` on `.mgrid` to consume full height

### Banner behavior
- Rolling/week: "Month / Month" only when visible week actually spans two calendar months
- Month view: single month only
- Cook Mode: recipe name replaces month in center banner

### Daily Mass display rules
- `optional=true` — zero conflict weight, bumps first, shows when space allows

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

**Note:** Emoji must use Unicode escape sequences in JS (`\u{1F4CB}` etc.) or HTML entities — raw emoji characters in Python heredocs cause encoding failures.

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

- `--hh` — header height. Fixed `96px`, enforced by `syncHdrH()` on init + resize. NOT measured from content.
- `--nh` — nav height. Fixed `96px`, same enforcement.
- `--cell-hdr-h` — cell header height (`54px` fixed).

`syncHdrH()` sets both to fixed values and JS-matches left zone width to right zone width. Never measures `#hdr` or `#bottom` offsetHeight.

---

## Open PQs (active)

| PQ | Description | Wave |
|----|-------------|------|
| PQ-03 | Egg count hardcoded 47 — pull from stockyard:eggs-log | 4.6 |
| PQ-04 | Agent buttons — wire to modules | 4.6 |
| PQ-06 | Saint panel — Mantel stub | 4.6 |
| PQ-11 | Meal Planner full view — Chow Hall | 4.6 |
| PQ-22 | Liturgical data 2028-2035 | Phase 1 closeout |
| PQ-30 | Wire RECIPES[] to live fetch from recipes/*.json | 4.6 |
| PQ-31 | Chow Hall post-cook altitude follow-up hook | 4.6 |
| PQ-32 | Phase 3 — voice timer start/stop | Phase 3 |
| PQ-34 | Unit conversion per ingredient — interactive tap-to-convert, per-session | 4.6 |
| PQ-35 | Inline ALT tags per ingredient/step — requires recipe schema update | 4.6 |
| PQ-36 | Kalea altitude override — save per recipe, flag as user edit vs doctrine | 4.6 |
| PQ-37 | Week mode rendering — broken, deep dive needed | 3.12 |
| PQ-38 | Rolling view renders 6 lines on Cockpit hardware — investigate when deployed | Cockpit phase |
| PQ-39 | Month view 5 rows not filling full screen height — empty space below row 5 | 3.12 |
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
