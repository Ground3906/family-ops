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
- **Filename dots, never underscores.** `v3.6`, `v3.7`, `v3.8`, `v3.9` — no exceptions.

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
| v3.8 | 2026-05-29 | 26-item spec pass — night mode all layers, copper plate Option D marquee, parchment cards, 2-col timers, color unification #f0c880, servings bar amber, kids kitchen size, scripture 52px, float bar fixed unit |
| v3.9 | 2026-05-29 | Top bar fill, high-contrast palette, burn pattern randomization, inline method steps, ingredients alignment, kids kitchen compact, servings 40px, float bar vertical stack |

---

## Locked Design Decisions

### Copper Plate Marquee (Option D) — wordmark + center banner
```css
background: #2e1e0a;
border-radius: 3px;
border-top: 2px solid #c07830;
border-left: 2px solid #a05a20;
border-right: 2px solid #5a2808;
border-bottom: 3px solid #3a1404;
box-shadow: 0 4px 14px rgba(0,0,0,.8), inset 0 0 16px rgba(0,0,0,.4);
```
Corner hardware: `.hw` / `.hw9` — CSS `::before` (top bar) + `::after` (left bar) in `#8a6028`.
Wordmark text only — no logo inside. Text fills bar height. Padding minimal (4px vertical).
Month/year banner: month `58px`, year `22px`, both `#f0c880`.
Wordmark: "Edelweiss Farms" `26px`, "Family Ops" `14px`, both `#f0c880`.

### Color Anchor
All Cook Mode text: `#f0c880`. Amber accent: `#f0c060`. No divergence.

### Recipe Accent Palette (10 colors, high-contrast)
```
['#2660a8','#b86010','#287860','#803050','#c04020','#604898','#208870','#c89010','#486cb0','#386828']
```
Timer card borders: `border-left:5px solid ${rc}; border-top:4px solid ${rc}`.
Tab borders: `border-left:5px solid ${rc}; border-top:4px solid ${rc}`.
Tab colors persist on ALL open tabs — full color regardless of active state.

### Parchment Cards
SVG `feTurbulence` filter, `fractalNoise`, `baseFrequency="0.009 0.015"`, `numOctaves="4"`.
Lightness: `feColorMatrix` alpha `0.14` (C level — not dark).
Gradient base: `#f5edd8 → #eee0b8 → #e4d098 → #d4bc78`.
Burn patterns: 8 variations in `_burnPatterns[]`, assigned by `seed % 8` — different direction per card.
`_paperSeeds`, `_paperSeedIdx`, `_burnPatterns` always declared together — never split.

### Timer Layout
2-column vertical. Col 1: first 5 timers. Col 2: 6th+, collapses when empty.
State-sorted: running → idle → done.
Rail: `224px` (1 col) / `448px` (2 col).

### Night Mode
`body.night-dim` covers: `#hdr`, `#dhdrs`, `#cal-wrap`, `#bottom`, `#cook-scr`, `#kids-scr`, `#month-scr`, `#meal-scr`, `#week-detail`.
`filter:brightness(0.08); pointer-events:none` on all.
`#night-wake`: `position:fixed; inset:0; z-index:999; cursor:pointer`. Tap to wake.

### Servings Bar
Buttons (−, +, Hide Ref, Start Recipe): all amber variant.
`background:#4a3208; border-top:1px solid #c07830; border-left:1px solid #a05a20; border-right:1px solid #3a1808; border-bottom:3px solid #1e0e04; border-radius:8px; color:#f0c060;`
Servings number: `40px`. "Servings" label: `13px`. Family: `18px`. All `#f0c880`.

### Float Bar
Fixed `220px` wide. Timers stack top-to-bottom. No Cook Mode return button. Tap anywhere on bar snaps to Cook Mode. Label: "Cook Mode Timers".

### Method Steps (inline)
Step number (`26px amber`) + bold title (`18px`) + body text (`17px`) — all inline on one line, no vertical stacking per step.

### Ingredients Card
Fixed `80px` quantity column, right-aligned. `12px` gap. Ingredient names left-aligned at consistent position. Font `13px` matching altitude card.

### Manual Timer
No background shell. Raw amber buttons inside rail. Thin top border separator only.

### Week Mode
`#week-detail.visible { display:flex; flex-direction:column; }`

### Month View
`#month-scr`: `position:fixed; top:var(--hh); left:0; right:0; bottom:var(--nh); overflow:hidden; display:flex; flex-direction:column;`
`.mgrid`: `grid-template-rows:repeat(5,1fr); flex:1; min-height:0;`

### Scripture Quote
`font-size:52px`. `max-width:1050px`. Centered on launch screen. No browse-recipes prompt text.

### Kids Kitchen Cards
Match Cook Mode launch screen pick card size. `grid-auto-rows:auto`. Icon `24px`, name `19px`.

### Rail Headers / Categories
Rail headers (TIMERS, RECIPES): `28px #f0c880`.
Right rail categories: `18px #f0c880`.
Recipe entries: `14px #e2d6aa`.

---

## Architecture (v3.6+)

### Top bar
- Sticky, fixed height `--hh` — never grows vertically
- Left: wordmark placard — text only, copper plate Option D, fills bar height
- Center: month/year banner — same copper plate; Cook Mode shows recipe name; dual-month slash when rolling week spans two months
- Right: egg card + vdiv + meal planner button + vdiv + agent grid

### Nav ribbon — 3 fixed sections
- **Left (.nav-left-zone):** Kids Kitchen — width JS-matched to right section via `syncHdrH()`
- **Center (.nav-center-zone, flex:1):** ← Home **Cook Mode** Night → — Cook Mode anchored dead center always
- **Right (.nav-right-zone):** Rolling / Week / Month — sets section width ruler

### Cook Mode layout
- **Left rail (#cm-left):** Timer stack (2-col) + manual timer (fixed bottom unit, no background)
- **Center (#cm-center):** 2×2 recipe card grid — sticky servings bar + frozen top row (Ingredients | Altitude) + method cards
- **Right rail (#cm-right):** Recipe browser (categories 18px, entries 14px)

### Recipe color system
- 10 high-contrast accent colors assigned dynamically per tab
- Applies to: recipe tab, all 4 center cards, timer cards
- Border-left 5px + border-top 4px — color band only, no recipe name tag on timer cards

### Float bar
- Position: bottom left, fixed above nav, `220px` wide
- Timers stack vertically, tap snaps to Cook Mode, no return button

### Night mode
- Covers all full-screen layers — calendar zones + cook/kids/month/meal/week screens
- Wake overlay at `z-index:999`

### goHome behavior
- Always resets to rolling view, snaps to today
- No page reload — calls `initRolling()` only, clears `body.night-dim`

### Month view
- Hard 5-row grid, always fills vertical container
- `flex:1` on `.mgrid` to consume full height

### Banner behavior
- Rolling/week: "Month / Month" only when visible week actually spans two calendar months
- Month view: single month only, never slash
- Cook Mode: recipe name replaces month in center banner

### Daily Mass display rules
- `optional=true` — zero conflict weight, bumps first, shows when space allows
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
