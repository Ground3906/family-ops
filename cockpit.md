# cockpit.md — Bayer Family Ops Display System

**Status:** Hardware PURCHASED. Software gates open. Installation pending.
**Last updated:** 2026-05-27

---

## What The Cockpit Is

The Cockpit is the Bayer household command display — a wall-mounted 32" touchscreen
in the kitchen, always on, always visible, always current. It replaces the paper
whiteboard calendar that currently spans the right wall of the kitchen.

It is the family's single source of truth for the day, the week, and what's coming.
Kalea sees it from the stove. Kids see it from the bar stools. Matt sees it walking
through. It is never turned off. It asks nothing of the viewer. It just shows the truth.

**Vocabulary lock:** Always THE COCKPIT. Never kiosk, tablet, display, screen, or
kitchen monitor. The vocabulary is intentional.

---

## Core Doctrine

- **READ-ONLY DISPLAY.** No keyboard, no form, no data entry on the Cockpit. Ever.
- **No user accounts, no login screen.** Boots straight to the widget. Full stop.
- **Always on.** Night mode after 21:00 (brightness down), never powered off.
- **Kalea adoption is the bar.** If she won't use it without instruction, it failed.
- **Touch is the only input.** Tap targets minimum 44px. Kids will use this.

---

## Physical Location

- **Room:** Kitchen
- **Wall:** The corner where wall meets wall — left of the right window, right of
  the center post, above the counter, below the sconce
- **Reference point:** Approximately the height of the blue/green plate currently
  on that wall panel
- **Mount approach:** Corner float — arm anchors to one wall (or corner bracket),
  monitor floats diagonally into the room on the arm
- **Sightlines:** Visible simultaneously from bar stools (8–10ft) AND cooking
  position at the stove (2–4ft). The corner placement is what makes this work.

---

## Hardware — LOCKED

### Display — PaitentPoint P-WAL-230-ELC-02

| Spec | Value |
|------|-------|
| Brand/Model | PaitentPoint P-WAL-230-ELC-02 |
| Screen size | 32" |
| Resolution | 1920×1080 FHD |
| Panel | LCD (IPS not confirmed — exam-room origin suggests wide angles) |
| Touch | Multi-point capacitive touchscreen |
| OS | Android 13 |
| CPU | Quad-core 2.30 GHz |
| RAM | 4GB |
| Storage | 64GB |
| Connectivity | HDMI, USB, Ethernet, Bluetooth, Wi-Fi |
| Audio | Integrated speakers (future: agent audio prompts) |
| VESA | 100×100 confirmed |
| Power | Charger included |
| Condition | Very Good — Refurbished (eBay certified) |
| Seller | Sunnking Sustainable Solutions |
| Seller rating | 167,377 ratings, 99.7% positive, R2/RIOS certified recycler |
| eBay item | 205826242798 |
| Price | $349.99 + shipping |
| Warranty | 1 year |

**Origin:** Originally deployed in doctor's office exam rooms by PatientPoint /
ContextMedia for patient education. Built for 24/7 wall display, multi-angle
viewing by patients and doctors simultaneously, and continuous touch interaction.
Sunnking liquidates decommissioned commercial hardware. 148 units of this model
sold by this seller alone.

**Verified real-world use case:** One buyer review states verbatim:
*"Great kiosk display. I used it to build a digital wall calendar."* — exact match.

**Setup flag:** Older ContextMedia wallboards (Android 4.4) had locked-down kiosk
firmware that was difficult to escape. The P-WAL-230-ELC-02 runs Android 13 and
Sunnking refurbishes to general-purpose use — this should be a clean Android 13
install. Verify on first boot that standard Android settings are accessible and
Chrome/browser can be installed. If the unit boots into a locked PatientPoint app,
contact Sunnking immediately — they are responsive and this is covered under warranty.

---

### Mount — Ergotron LX 45-243-026

| Spec | Value |
|------|-------|
| Model | Ergotron LX Single Monitor Arm Wall Mount |
| Part number | 45-243-026 |
| Type | Friction-based articulating arm |
| Capacity | 25 lbs (monitor ~8 lbs — well within spec) |
| VESA | 75×75 and 100×100 compatible |
| Extension | 15–21" — sufficient for corner float |
| Tilt | ±70° |
| Pan | 360° |
| Condition | Used — removed from professional working environment |
| Missing | Decorative cable management covers only — cosmetic, irrelevant for corner install |
| All functional hardware | Confirmed intact |
| Seller | EFE SALES |
| Seller rating | 47,229 ratings, 99.7% positive |
| Price | $64.99 + shipping |
| Warranty | 30 days seller warranty |

**Why friction not gas spring:** Touchscreens require constant arm actuation on
every tap. Gas spring arms move easily by design — screen wobbles on every touch.
Friction arms stay exactly where placed until deliberately repositioned. For a
family display that gets tapped dozens of times daily, friction is the only correct
choice. Ergotron LX is the industry standard for touchscreen installations.

**Install note:** Ergotron LX anchors to a single wall stud. Verify stud location
in that corner before drilling. If no stud is reachable from the ideal position,
use a toggle bolt rated for 30+ lbs or mount a backing board across two studs first.

---

### Thin Client

**None needed.** The PaitentPoint unit IS the computer. Android 13 onboard.
Chrome browser runs the widget directly. No separate thin client, no separate
computer, no additional hardware. One box on the wall, one power cable, done.

---

## Server Infrastructure

### ThinkPad X1 Carbon — Headless Server

The Cockpit doesn't run standalone. It pulls live data from the ThinkPad.

| Spec | Value |
|------|-------|
| Machine | ThinkPad X1 Carbon |
| Machine name | strayhawk-pc |
| Windows user | ThinkPad X1 Carbon (with spaces — legacy) |
| Role | Headless server — Cockpit host + Phase 2 automation host |
| OS | Windows (transitioning to headless post-Precision validation) |
| Location | Office |
| Network | "7 Little Bears" Wi-Fi + wired Ethernet option |
| Server software | Python HTTP server (`python -m http.server 8080`) Phase 1 |
| Serves | `wave-4-5-widget-vX.X.html` and `calendars.md` from `C:\dev\family-ops` |
| Cockpit reaches it via | Local LAN — Android Chrome on Cockpit → ThinkPad IP:8080 |
| Phase 2 role | Hosts automation agents, GitHub MCP writes, scheduled jobs |

**Transition path:** ThinkPad is currently active as primary machine (being replaced
by Dell Precision 5690 "mbay"). Once Precision is validated and ThinkPad is
demoted, it goes headless — lid closed, always on, always serving. Cockpit host
is its permanent role. Cockpit Phase 1 runs before ThinkPad goes headless;
Phase 2 automation runs after.

**Static IP:** Before going headless, assign the ThinkPad a static local IP
(or DHCP reservation in the router) so the Cockpit's bookmark never breaks.
Suggested: `192.168.X.100` — easy to remember, outside DHCP pool.

---

## Network Infrastructure

### Current State
- ISP: Starlink
- Wi-Fi network: "7 Little Bears"
- All devices on single flat network

### Planned Addition — Firewalla (Wyatt + household security)

Firewalla sits between Starlink and the home network. Provides:
- Per-device parental controls (Wyatt's devices — time limits, content filtering,
  safe search enforcement, social media schedules)
- Network-level ad blocking for all devices
- Intrusion detection/prevention (IDS/IPS)
- Full traffic visibility via mobile app — see every device, every connection
- VPN server built in — secure remote access
- VLAN segmentation — isolate IoT devices, farm equipment, guest network
- No monthly fee

**Recommended unit:** **Firewalla Purple SE** — ~$329 Amazon

| Spec | Value |
|------|-------|
| Model | Firewalla Purple SE |
| IPS throughput | 500 Mbps (Starlink rarely exceeds this in Westcliffe) |
| CPU | 6-core |
| RAM | 2GB DDR4 |
| Wi-Fi | Built-in (can replace or work alongside existing router) |
| Parental controls | Per-device rules, schedules, content categories, safe search |
| Management | Android app — Matt's phone |
| Monthly fee | None |
| Price | ~$329 Amazon |

**Why Purple SE and not Gold Plus:**
The Gold Plus at $569 features four 2.5 gigabit interfaces and 5 gigabits
of inspection capability — likely overkill for home users. Starlink in Westcliffe
at 9,000ft elevation runs 50–200 Mbps realistically. Purple SE's 500 Mbps IPS
ceiling is never hit. Gold Plus is for small businesses. Purple SE is for the Bayer
household. Save $240.

**Firewalla + Cockpit integration:**
The Cockpit (PaitentPoint Android device) must be assigned to an UNRESTRICTED
device group in Firewalla. It is not a child's device — it should have full
unfiltered LAN access to the ThinkPad server at all times. Set this on day one.

**Important Firewalla caveat:** A child with a phone could circumvent
Wi-Fi restrictions by turning off Wi-Fi and using mobile data. Firewalla
controls Wi-Fi only. Device-level controls (Google Family Link on Wyatt's Android)
are the complement for mobile data situations. Both layers needed.

**Wyatt's device profile — suggested rules:**
- Safe search enforced (Google, YouTube, Bing)
- Adult content blocked (Family Protect on)
- Social media: blocked 06:00–15:00 school days (adjust for summer)
- Gaming: blocked after 21:00 daily
- All internet: blocked 22:00–06:00
- Alarms: notify Matt when Wyatt's phone comes online after 22:00

---

## Full System Architecture

```
INTERNET
    │
    ▼
Starlink Dish + Router
    │
    ▼
Firewalla Purple SE  ←── Matt's Android (Firewalla app — management)
    │
    ├── "7 Little Bears" Wi-Fi
    │       │
    │       ├── ThinkPad X1 Carbon (headless, static IP)
    │       │   ├── Python HTTP server :8080 → serves widget HTML + calendars.md
    │       │   ├── GitHub MCP → writes calendars.md from agent calls
    │       │   └── Phase 2 automation agents (scheduled jobs)
    │       │
    │       ├── PaitentPoint Cockpit (Android 13, UNRESTRICTED in Firewalla)
    │       │   └── Chrome → ThinkPad:8080/wave-4-5-widget-vX.X.html
    │       │
    │       ├── Dell Precision 5690 "mbay" (Matt's primary machine)
    │       ├── Kalea's device
    │       ├── Wyatt's device  ←── Firewalla parental rules applied
    │       └── [all other household devices]
    │
    └── Wired Ethernet (optional — ThinkPad server for stability)
```

---

## Physical Installation Checklist

Pre-order:
- [ ] Measure corner wall space — confirm arm reach puts monitor in sightline
- [ ] Locate wall stud in target corner
- [ ] Confirm power outlet accessible above counter (behind cabinet or in corner)

Day of install:
- [ ] Mount Ergotron LX to stud — use provided hardware + level
- [ ] VESA-mount PaitentPoint to Ergotron plate
- [ ] Route single power cable down arm and into corner / behind counter
- [ ] Connect to "7 Little Bears" Wi-Fi on first boot
- [ ] Verify Android 13 is accessible (not locked into PatientPoint app)
- [ ] Install Chrome if not present
- [ ] Navigate to ThinkPad:8080/[widget filename] — confirm widget loads
- [ ] Enable Android kiosk / pinned screen mode (Settings → Security → Screen Pinning)
- [ ] Set display to "Never sleep" (Settings → Display → Screen timeout → Never)
- [ ] Set brightness to comfortable always-on level
- [ ] Add Cockpit to Firewalla unrestricted group

---

## Android Kiosk Setup (Phase 1)

Phase 1 uses Android's native Screen Pinning — no MDM software needed.

1. Open Chrome, navigate to widget URL, go full screen
2. Settings → Security → Screen Pinning → ON
3. Open Recents, tap the pin icon on Chrome
4. Screen is now pinned — exits only with Back + Recents held simultaneously
5. Set as the boot default: add Chrome shortcut to home screen, set as default
   launcher action if available

**Phase 2 option:** Fully Kiosk Browser — runs best on Android 6–16,
supports Android 13. Provides remote management, auto-restart, motion-triggered
display wake, brightness scheduling, and lockdown to single URL.
Free tier is sufficient for Cockpit use. Phase 2 upgrade if Phase 1 Screen Pinning
proves insufficient.

---

## Phase 2 Widget Design Constraints

Every Phase 2 UI decision must be validated against these specs:

| Constraint | Value | Design implication |
|------------|-------|--------------------|
| Resolution | 1920×1080 | Design at 1080p exactly. No 4K assumptions ever. |
| Screen size | 32" | Text must be legible at 8–10ft from bar stools |
| OS | Android 13 / Chrome | No Windows APIs. Standard HTML/CSS/JS only. |
| Touch | Capacitive multi-touch | Minimum 44px tap targets. Finger use, not stylus. |
| Close viewing | 2–4ft (counter) | Font must not be overwhelming at arm's length |
| Far viewing | 8–10ft (bar stools) | Key info must read without stepping closer |
| Viewing angle | Wide — corner mount | Wide-angle legibility required from both walls |
| Orientation | Landscape, fixed | Portrait mode never considered |
| Input | Touch only | No keyboard, no mouse, no forms. Ever. |
| Always-on | Yes | Dark theme default. Low burn-in risk. |
| Night mode | After 21:00 | Reduced brightness. Minimal stimulation. |
| Audio | Integrated speakers | Phase 2: agent audio prompts are viable |
| Network | LAN only | Widget fetches from ThinkPad over local network |
| Offline behavior | Must fail gracefully | Show last cached state if ThinkPad unreachable |

---

## Software Gates — Install Readiness

Hardware is purchased and in hand. Installation proceeds when software gates are green.
Gates 1 and 4 cleared. Gates 2 and 3 still open — install can begin in parallel;
real operational data entry holds until S8 durability fix ships.

| Gate | Description | Status |
|------|-------------|--------|
| 1 | Wave 4.5 widget loads clean — Kalea can use without instruction | ✅ GREEN — v2.9 |
| 2 | At least 2 agents writing to `calendars.md` reliably via Foreman handoff | 🔲 OPEN |
| 3 | Stockyard S8 durability fix shipped | 🔲 OPEN |
| 4 | ThinkPad running headless clean for 1 full week without babysitting | ✅ GREEN |

**S8 gate discipline:** Cockpit can go on the wall and run the widget. No real flock
data entry until S8 is resolved. Stockyard runs display-only until then.

---

## Budget Summary

| Item | Status | Price |
|------|--------|-------|
| PaitentPoint 32" Android Wallboard (eBay 205826242798) | **PURCHASED** | $349.99 |
| Ergotron LX Wall Mount (used) | **PURCHASED** | $64.99 |
| **Cockpit total** | | **$414.98** |
| Firewalla Purple SE (separate purchase — Wyatt/network) | Planned | ~$329.00 |
| **Full infrastructure total** | | **~$743.98** |

Firewalla is a separate decision with separate timing — it's not a Cockpit gate.
It should be purchased and configured before Wyatt gets significant device freedom
(before driver's licensing phase, at minimum).

---

## Phase 3 North Star

**Status:** Vision locked. No build until all Phase 1/2 gates are green.
**Last captured:** 2026-05-27

This section documents the full end-state vision for the Cockpit. Every Phase 1 and
Phase 2 build decision should point toward this north star without overbuilding ahead
of its time.

---

### Voice Layer — ElevenLabs

Full Home Improvement cast. One voice per agent. Nobody sounds like anyone else.
Budget: **ElevenLabs Creator plan — $22/month, Flash model.**

| Agent | Character | Voice profile |
|-------|-----------|---------------|
| 🔧 Al | Al Borland | Deep, dry, measured male |
| 📅 Foreman | Wilson | Warm, slightly cryptic — never rushes |
| 🍳 Chow Hall | Jill Taylor | Warm, practical female |
| 🏠 Punch List | Tim Taylor | Enthusiastic, direct male |
| 📚 Whetstone | Binford announcer | Authoritative, broadcaster male |
| 🎒 Mystery Ranch | Bud | Gruff, outdoorsman |
| 🐷 Stockyard | Marty | Working-class, no-nonsense |
| 🌱 Rootstock | Al's mom | Warm, earthy female |

Voice IDs assigned in Phase 3. `VOICE_CAST` constants are in the widget, dormant.

---

### Sound Layer — Local Files, Web Audio API, Zero Cost

`playSound()` hook wired in widget v2.9. Files live in `/sounds/` on ThinkPad server.
No ElevenLabs dependency. No API calls. Instant playback.

| Event | Sound |
|-------|-------|
| Widget boot / morning load | Home Improvement theme riff |
| Morning briefing start | Al voice reads the day |
| Saints of the day | Wilson — Foreman reads over the fence |
| Calendar write confirmed | "More power" |
| CCIR critical alert | Argh argh argh |
| Anomaly detected | Tool grunt |
| 17:15 dinner warning | Binford Tools jingle |
| Task complete | Argh of approval |
| System error | "I don't think so Tim" |
| Flock anomaly | Stockyard / Marty voice |
| Frost alert | Rootstock voice |

---

### Daily Liturgical Briefing — Wilson / Foreman

Every morning. Wilson comes to the fence. Reads the saint of the day — name, feast,
one line of genuine wisdom in character. Bayer household is Catholic. This is doctrine
surfacing daily in the kitchen where the whole family hears it. Kids at the bar stools.
Kalea at the stove. Matt walking through.

Sequence: `playSound('boot')` → `speak(dayBriefText, 'foreman')`

Saints data source: `calendars.md` liturgical entries + Mantel stub (Wave 4.6+).

---

### Video Calling Station

USB camera mounted to Cockpit frame. One tap on a family member's pill. Call opens.
Kalea deploys — kids walk up to the wall. No phone handed to a six-year-old.
No hunting for a device. The wall is the phone.

**Why this matters:** USMC Reserve household. Kalea deploys. This is operational,
not decorative.

Implementation: Android WebRTC or Google Meet link pinned to pill tap. Phase 3 design TBD.

---

### Weather Integration — Foreman Owns

Permanent Westcliffe current conditions panel on the widget. Always visible.

**Who taps it:**
- **Foreman** — reads destination from calendar entry, pre-loads weather for that
  location and time in the day brief. "Rainy. 52°F in Colorado Springs. Bring a jacket."
- **Mystery Ranch** — wind, precip, temp, sunrise/sunset for the hunt unit.
- **Punch List** — road conditions on the 160 over Hardscrabble before vehicle goes out.
- **Rootstock** — first/last freeze alerts at 9000ft.

No new agent. Weather is a utility layer. All agents borrow the feed. Foreman surfaces it.

---

### Sensor Feeds — Stockyard + Farm

USB or Bluetooth sensors feeding live into the widget. Stockyard gets a nervous system.

Planned sensors:
- Freezer alarm — temperature threshold alert
- Coop temperature — live feed on Stockyard panel
- Gate alerts — farm perimeter
- Additional TBD based on Phase 3 farm build

Cockpit shows real farm state, not just calendar state.

---

### Motion-Triggered Wake

Screen sleeps at 21:00. Someone enters the kitchen — it wakes. No tap required.
Fully Kiosk Browser handles this natively (free tier sufficient).

Phase 2 upgrade: swap Android Screen Pinning for Fully Kiosk Browser if Phase 1
proves insufficient. Motion wake is a Fully Kiosk feature.

---

### Foundation Placeholders — Wired in v2.9

These are in the widget now. Dormant. Do not activate without Phase 3 gate clearance.

| Hook | Location | Status |
|------|----------|--------|
| `speak()` | widget v2.9 JS | WIRED, DORMANT |
| `playSound()` | widget v2.9 JS | WIRED, DORMANT |
| `VOICE_CAST` constants | widget v2.9 JS | WIRED, DORMANT |
| `SOUNDS` constants | widget v2.9 JS | WIRED, DORMANT |
| `scheduleMorningBriefing()` | widget v2.9 JS | WIRED, DORMANT |
| `ccirAlert()` | widget v2.9 JS | WIRED, DORMANT |
| `dinnerReminder()` | widget v2.9 JS | WIRED, DORMANT |
| Weather panel stub | Phase 3 widget pass | NOT YET |
| Video call button stub | Phase 3 widget pass | NOT YET |

---

### Phase 3 Budget Flag

| Item | Cost | Notes |
|------|------|-------|
| ElevenLabs Creator plan | $22/mo | Flash model, ~100K chars/mo, full cast |
| Sound library files | $0 | Local ThinkPad, Web Audio API |
| Weather API | $0 | Open-Meteo or NWS free tier |
| Video calling | $0 | Android WebRTC / Google Meet |
| USB camera | ~$30 one-time | Phase 3 hardware add |
| **Phase 3 recurring** | **$22/mo** | |

