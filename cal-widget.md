# cal-widget.md — Calendar Widget Reference

**Filename convention:** `cal-widget-v[MAJOR].[MINOR].html` — DOT notation always, NEVER underscore. No wave reference in filename. `wave-4-5-widget-*` naming fully retired.
**Current version:** v5.8.2 (live: `cal-widget-current.html`). Archive: `cal-widget-v5.8.html`.
**Cockpit URL:** `http://192.168.1.60:8080/cal-widget-current.html` — NEVER changes. `cal-widget-current.html` always mirrors latest version.
**Data sources:** `calendars.md` + `recipes-index.json` + `recipes/*.json` — all fetched live with `{cache:'no-store'}`

---

## Hard Gates

- **Stockyard S8 durability fix** — still open. No real flock data entry until fixed.
- **COCKPIT IS READ-ONLY.** No entry tool, no form, no keyboard on Cockpit. Ever.
- **NEVER patch data files to work around code bugs.** Fix the code.
- **Full rewrite for design/feature changes.** Version up to a new file (e.g. v5.9). Surgical PowerShell patches are permitted for infrastructure additions only (cache tags, footer, etc.) — commit as a patch version (v5.8.1, v5.8.2). Never patch data logic or UI layout surgically.
- **Large-file push via PowerShell only.** Widget HTML is too large for MCP inline push. Use PowerShell `Replace()` patches locally, commit and push from ThinkPad or Precision. MCP handles doctrine files and small scripts only. Never attempt to pass widget content as MCP inline parameter.
- **Filename dots, never underscores.** `v5.4`, `v5.5` — no exceptions.

---

## Cockpit Hardware (locked)

- **Device:** PatientPoint P-WAL-230-ELC-02 — Android 13, 1920x1080, 4GB RAM. Kitchen, Ergotron arm.
- **Browser:** Fully Kiosk Browser. Start URL: `http://192.168.1.60:8080/cal-widget-current.html`
- **Fully Kiosk settings:** Auto-reload idle: 86400s. Scheduled daily reload: 00:01. All 4 auto-reload triggers: ON. Cache clear on reload: ON. Web storage/history/cookies delete: OFF. Load current page on reload: OFF. Skip reload if showing start URL: OFF.
- **Server:** ThinkPad X1 Carbon `192.168.1.60`, Python HTTP server on `:8080`, repo at `C:\Users\ThinkPad X1 Carbon\Documents\family-ops`

## Cockpit Deploy Pattern (Option C, locked)

Every session close (full version):
1. Build `cal-widget-vX.X.html`
2. `Copy-Item cal-widget-vX.X.html cal-widget-current.html`
3. `git add cal-widget-vX.X.html cal-widget-current.html` -> commit -> push
4. ThinkPad: `git pull`
5. Cockpit auto-refreshes via Fully Kiosk or manual reload — picks up new version. URL never changes.

**Patch version deploy (v5.8.1+):** PowerShell `Replace()` patches on `cal-widget-current.html` directly. No new versioned archive file. Commit and push from local machine. MCP not used for widget file.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.0-v2.8 | 2026-05-25/26 | Wave 4.5 — calendar core, categories, conflict detection, cook mode stub |
| v3.0 | 2026-05-27 | Cook Mode full build — tabs, recipe cards, timers, worn recipe card theme |
| v3.1-v3.5 | 2026-05-27 | Cook Mode recipe browser, manual timer, Kids Kitchen, servings, start recipe gate |
| v3.6-v3.9 | 2026-05-28 | Timer auto-pop, 2x2 layout, 3-section nav ribbon, snap-to-today, antique placard, scripture launch |
| v3.10 | 2026-05-29 | Two-layer nav family, 2-card cook center, Kids Kitchen -> rail category, What's for Dinner added |
| v3.11 | 2026-05-29 | 96px bars, marquee padding, gold hardware, height parity all bottom bar buttons |
| v3.12 | 2026-05-29 | Cook Mode interior — servings bar, step layout, fonts, altitude, timer onclick, rail headers, emoji encoding |
| v4.0 | 2026-05-29 | Ingredient grid unified, snap-to-today double rAF fix, Cook Mode scroll anchor |
| v5.0 | 2026-06-01 | **Wave 6.5 — Meal Planner + Widget Integration.** [MEAL] tag parser, live recipe fetch, Meal Planner screen, What's for Dinner, Cook Mode splash, Coming Up rail, cancel= treatment, liturgical pill fix, span all-bottom stack |
| v5.1 | 2026-06-02 | **Wave 6.6 Chunk A.** `--cell-h` dynamic 5-row grid, dnum 40->28px, cell-hdr-h 54->38px, banner midpoint fix, adjacent month fill, night mode white flash fix, agent buttons 62->72px, month first/last row border suppression |
| v5.2 | 2026-06-02 | **Wave 6.6 Chunk B.** WFD rebuilt as month-view clone, week mode rebuilt (7-col events top / 7-col briefs bottom), Meal Planner rebuilt on buildWkRow, WebView sharpness CSS |
| v5.3 | 2026-06-02 | **Wave 6.6 Chunk C.** Meal Planner font 14px, timer padding reduced, auto-refresh every 3 min, rolling 4-row, conflict flag penalty removed, week/meal planner unlimited events |
| v5.4 | 2026-06-02 | **Wave 6.6 Chunk D.** Rolling 3-row / month+WFD 5-row split via `--cell-h`/`--cell-h-month`, `ROLL_MAX_EVENTS=7`, `MAX_EVENTS=4`, scroll restore on WFD/meal planner close, fixed 4-week arrow nav, refreshCalendar rolling fix |
| v5.5 | 2026-06 | Wave 6.7 intermediate |
| v5.6 | 2026-06-05 | **Wave 6.7 Bug Fixes (5).** Auto-shutoff no longer re-fires every 60s after manual wake. Month button always lands on current month. Cell-face location display reverted. Night button works from any screen/mode. Cook Mode undefined-undefined removed; lard-soap removed from index. |
| v5.7 | 2026-06-05 | **Wave 6.7 Timer Numpad.** Manual timer input replaced with number pad (1-2-3 layout). Digits fill left-to-right: 1-2 = minutes, 3-4 = hours:minutes. HH and MM labeled segments. Backspace. Create button. Rail expansion at 4 timers. Numpad fixed 200px. |
| v5.8 | 2026-06-17 | **Cook Mode recipe format fix + category rebuild.** Widget reads current recipe schema ({item,qty,unit,note} ingredients; instructions[] steps). Auto-timers extracted from step text, tappable. Right rail categories live. 3 new shelves (Seafood, Sauces, Household). Kids Kitchen wired. Short names in tabs. Undefined prefix removed. Midnight rollover guard added. |
| v5.8.1 | 2026-06-22 | No-cache meta tags (`Cache-Control`, `Pragma`, `Expires`) in `<head>` — prevents Fully Kiosk from serving stale widget after pull job updates file. |
| v5.8.2 | 2026-06-22 | Sync footer — fixed bottom strip shows "Last sync: X min ago." Amber + "Sync stale" label when last pull >10 min. `checkSyncStatus()` on load and every 60s, reads `last-pull.json`. |

---

## Wave Naming Convention (locked)

Wave numbers follow the **charter build order only**. No widget-specific wave numbering. Widget gets its own version number (`cal-widget-vX.X.html`) independent of wave.

- Wave 6.5 = Meal Planner + Widget Integration (shipped)
- Wave 6.6 = Cockpit hardware delivery + display optimization (shipped v5.1-v5.4)
- Wave 6.7+ = remaining open PQs (unit conversion, ALT tags, Kalea altitude override, etc.)

---

## Chunk Build Strategy (locked)

Frame changes ship and proof before interior changes. Never mix frame and interior in one build pass.

- **Frame:** top bar, bottom bar, heights, spacing, nav structure
- **Interior:** cook mode layout, timers, recipe rail, emojis, functional behavior

Build in chunks, verify on Cockpit hardware between chunks. Each chunk = one commit.

---

## Sync Footer (v5.8.2, locked)

Fixed strip at bottom of all screens. Shows time since last successful ThinkPad pull.

- **Normal state:** `rgba(0,0,0,0.3)` bg, `#aaa` text — "Last sync: X min ago"
- **Stale state (>10 min):** `#b8860b` amber bg, white bold — "Sync stale - X min ago"
- **Unknown:** "Sync: unknown" — `last-pull.json` not found or fetch failed (expected on first load before pull job runs)
- `checkSyncStatus()` fires on `DOMContentLoaded` and every 60 seconds
- Fetches `last-pull.json?t=[timestamp]` (cache-busted) from ThinkPad server root
- `last-pull.json` written by `pull-job.ps1` on every exit-0 pull — gitignored, runtime state only
- Colorblind-safe: distinction uses amber color + label change + text content, never color alone

---

## Cook Mode Recipe Schema (v5.8, locked)

### Recipe Index Architecture (locked)
Display metadata lives in `recipes-index.json` (repo root). Cooking data lives in individual `recipes/<id>.json` files, fetched on tap. Split is intentional — the widget loads the index at launch (display only), then fetches the full recipe file only when a recipe is opened.

**Index fields per entry:** `id`, `name`, `heirloom`, `file`, `tags`, `category`, `kids`, `short_name` (optional).

**Individual recipe file fields:** `id`, `name`, `family_baseline`, `heirloom`, `tags`, `altitude_adjustments`, `ingredients` (array), `instructions` (array of strings).

### Ingredient Schema (locked)
Current format: `{item, qty, unit, note}`. The widget's `parseQty()` function parses qty strings (fractions, mixed numbers, ranges) for scaling. Note field renders italic in parentheses after the item name.

Old format (`{name, amount, unit}`) also supported via fallback for backward compatibility.

### Steps/Instructions Schema (locked)
Current format: `instructions` — plain array of strings. Widget's `adaptInstructions()` normalizes to step objects with auto-extracted timers. Old format (`steps` array of objects with `{n, title, text, timer_seconds}`) also supported.

### Auto-Timer Doctrine (locked)
Widget reads time references from plain-text instruction strings and offers a tappable timer per step. Known to occasionally misread ambiguous text. Chow Hall owns corrections during recipe entry, applied with Kalea's guardrails at session time.

### Category Shelves (17 total, locked)
Original 14: Breakfast, Soup, Casserole, Sides, Bread, Beef, Poultry, Pasta, Pork, Dessert, Cookies, Barbecue, Pie, Canning.
Added v5.8: Seafood, Sauces, Household.

**Elk = ground beef rule (locked):** Elk dishes categorize by dish type, not by protein. Chili, burgers, enchiladas file under Beef or Barbecue. No game shelf.

**Category assignments:** All 35 current recipes assigned in `recipes-index.json`. Pork, Pie, Canning are empty shelves — room to grow.

### Kids Kitchen (locked)
`kids` boolean in `recipes-index.json`, same pattern as `heirloom`. Recipe stays in its real category shelf. Kids Kitchen displays duplicates. Flag is add/remove — Kalea manages it as kids grow. Starts with Mac & Cheese and Sloppy Joes.

### Short Names (locked)
`short_name` field in `recipes-index.json`, optional. When present: tabs use `short_name`, title bar uses full `name`. 16 recipes carry short names. Borderline cases confirmed against real tab at first load.

### Day Rollover Guard (v5.8, locked)
`refreshCalendar()` checks current date against `TODAY_STR` on every 3-minute tick. If date has drifted past midnight since page load, fires `location.reload()`. Primary fix: Fully Kiosk 00:01 scheduled reload. Code guard is backup.

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
SVG `feTurbulence` filter, `fractalNoise`, `baseFrequency="0.009 0.015"`, `numOctaves="4"`. Lightness: alpha `0.14`. Gradient: `#f5edd8 -> #eee0b8 -> #e4d098 -> #d4bc78`. 8 burn patterns.

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
Dark shell. Timer card accent: teal `#287888`. "Create" button -> idle card -> Start from card.

### Timer Done Behavior
Done state: "Silence" + X. Silenced: "Silenced" + X. X always visible in done/silenced.

### Timer Layout (v5.3)
2-column vertical. Col 1: first 6. Col 2: 7th+. State-sorted: running -> idle -> done -> silenced. Rail: `224px` / `448px`.
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
- `cancel=pending`: warm bg `#1c1814`, dashed warm border `rgba(160,120,80,.30)`, 2px amber strikethrough, no pills, no time — full opacity
- `cancel=confirmed`: filtered from parser entirely, line stays in `calendars.md` as audit trail

### Liturgical Pill Logic (v5.0, locked)
- All-day liturgical events: pills suppressed (feast days, Holy Days)
- Timed liturgical events (Serve at Mass): pills render normally

### Per-View Cell Heights (v5.4, locked)
- **Rolling:** `--cell-h` = `floor((innerHeight - 96 - 96 - dhH) / 3)` approx 289px at 1080px. 3 rows visible.
- **Month + WFD:** `--cell-h-month` = `floor((innerHeight - 96 - 96 - dhH) / 5)` approx 173px at 1080px. 5 rows always.
- **Week + Meal Planner:** `height:100%` via layout class.

### Per-View Event Caps (v5.4, locked)
- **Rolling:** `ROLL_MAX_EVENTS=7`
- **Month/WFD:** `MAX_EVENTS=4`
- **Week/Meal Planner:** `showAll=true` — no cap

### Week Mode (v5.2, locked)
Top 50%: 7-col events. Bottom 50%: `#week-briefs` — 7 brief columns, always visible.

### Meal Planner (v5.2, locked)
Rebuilt on `buildWkRow`. `[MEAL]` entries render as amber tiles. Tap tile -> Cook Mode.

### What's for Dinner (v5.2, locked)
Month-view clone. Meals-only content. Read-only kids view. Arrows page by month.

### Cook Mode Splash (v5.0)
Bible verse centered. Today's planned meals preloaded as tappable tiles. Coming Up rail: next 1-2 days.

### Auto-Refresh (v5.3, locked)
Every 3 minutes. Guards: returns immediately if `cookOn || nightOn`.

---

## Architecture

### Top bar
Sticky, fixed height `--hh:96px`. Left: wordmark placard. Center: month/year banner. Right: egg card + agent grid.

### Nav ribbon — 3 fixed sections
Left: What's for Dinner + Meal Planner. Center: <- Home Cook Mode Night ->. Right: Rolling / Week / Month.

### Cook Mode layout
Left rail: Timer stack + manual timer. Center: servings bar + 2-card area. Right rail: Recipe browser (categories + Kids Kitchen + Coming Up).

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
| liturgical | cross | Feast days, Holy Days, Mass |
| kids | children crossing | Kids events, swim practice, Faith Formation |
| family | house | Whole-family events, swim meets |
| animals | paw | Farm/animal events |
| appointments | plus | Medical, dental, therapy |
| 4h | clover | 4H events, fair |
| rootstock | seedling | Garden, orchard |
| prompt | alarm clock | Reminders, milestone pings |
| meetings | clipboard | KoC, Fairboard, any recurring meeting |
| misc | (none) | Catch-all |

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
| cancel=pending | string | Strikethrough, no pills. Awaiting confirmation. |
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

PQs are future-session items — parked until conditions are right to address them. Never conflated with session work Items.

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
| PQ-GUS | Sourdough starter feed tracker — timer-reset tap, not data entry. Cockpit read-only constraint applies. Design conversation needed. Colorblind-safe treatment required (not red-only). | Future brainstorm |
| PQ-PHASE2 | sessionStorage timer persistence on Home reload | Phase 2 |

---

## Stockyard S8 Hook (HARD GATE)

Auto-export to repo via GitHub MCP. Blocks real flock data entry. Not built. Not bypassed. Surface every session.

---

## calendars.md Reversion Watch

Three categories that have reverted across session rewrites — verify on every rewrite:
- **Knights of Columbus** -> must be `meetings`
- **Fairboard meeting** -> must be `meetings`
- **Fair cleanup** -> must be `4h`

---

## CSS Variables

- `--hh` — header height. Fixed `96px`.
- `--nh` — nav height. Fixed `96px`.
- `--cell-hdr-h` — cell header height. `38px`.
- `--cell-h` — rolling row height. Dynamic: `floor((innerHeight - 96 - 96 - dhH) / 3)`.
- `--cell-h-month` — month/WFD row height. Dynamic: `floor((innerHeight - 96 - 96 - dhH) / 5)`.
