# cockpit.md — Bayer Family Ops Display System

**Status:** Operational. ThinkPad headless. Pull job active (3-min cadence), writes `last-pull.json` and `data-age.json` on each OK. Fully Kiosk 00:01 reload set.
**Last updated:** 2026-07-12

**Tablet clock confirmed:** Mountain Daylight Time, network time ON, 24h format. Device clock is not a source of timing issues. Night dim at 21:00 is working as designed — widget dims and shows wake prompt, never fully powers off. Day rollover guard exists as code backup to the 00:01 reload.

**Night mode wake is manual-only, permanently.** Engaging is clock-based (21:00). Waking is never clock-based, under any circumstance — no morning cutoff hour, no auto-relight, ever. Deliberate: an empty house on vacation stays dark, not burning the screen and power on a schedule nobody asked for. As of 2026-08-19, night state persists across any reload (midnight or otherwise) via local device storage, closing a bug where the day-rollover reload was wiping the dark state and lighting the screen back up at 12:01 AM with no way to re-darken until 9 PM that night.

---

## What The Cockpit Is

The Cockpit is the Bayer household command display — a wall-mounted 32" touchscreen in the kitchen, always on, always visible, always current. It replaces the paper whiteboard calendar that currently spans the right wall of the kitchen.

It is the family's single source of truth for the day, the week, and what's coming. Kalea sees it from the stove. Kids see it from the bar stools. Matt sees it walking through. It is never turned off. It asks nothing of the viewer. It just shows the truth.

**Vocabulary lock:** Always THE COCKPIT. Never kiosk, tablet, display, screen, or kitchen monitor. The vocabulary is intentional.

---

## Core Doctrine

- **READ-ONLY DISPLAY.** No keyboard, no form, no data entry on the Cockpit. Ever.
- **No user accounts, no login screen.** Boots straight to the widget. Full stop.
- **Always on.** Night mode after 21:00 (brightness down), never powered off.
- **Kalea adoption is the bar.** If she won't use it without instruction, it failed.
- **Touch is the only input.** Tap targets minimum 44px. Kids will use this.

### Silence is not health

Any always-on process must assert liveness, or its silence must be indistinguishable from failure and treated as such. A screen that has stopped updating but still renders is worse than a dark screen: a dark screen is honest, a stale screen lies. This principle drives two design facts on the Cockpit:

1. **The 00:01 hard-reload is the dead-man switch for the entire watcher layer.** It clears cache and re-fetches from the ThinkPad. If the ThinkPad is down, the fetch fails against an empty cache and the Cockpit goes dark. A dark Cockpit is how the household learns the ThinkPad died — because nothing on the ThinkPad can report its own death. Do NOT change the reload to "fail gracefully to cached state" without replacing this dead-man with something else. See `ops/watcher-layer.md`.

2. **The widget must show its own data age.** A running pull job proves the widget can reach the ThinkPad; it does not prove the data is fresh. The sync banner reads `data-age.json` (calendars.md's true last-modified time) and shows how old the calendar actually is — in text and shape, never color alone (Matt is red-green colorblind). Fetch-success is not data-age.

---

## Physical Location

- **Room:** Kitchen
- **Wall:** The corner where wall meets wall — left of the right window, right of the center post, above the counter, below the sconce
- **Mount approach:** Corner float — arm anchors to one wall (or corner bracket), monitor floats diagonally into the room on the arm
- **Sightlines:** Visible simultaneously from bar stools (8-10ft) AND cooking position at the stove (2-4ft). The corner placement is what makes this work.

---

## Hardware — LOCKED

### Display — PatientPoint P-WAL-230-ELC-02

| Spec | Value |
|------|-------|
| Brand/Model | PatientPoint P-WAL-230-ELC-02 |
| Screen size | 32" |
| Resolution | 1920x1080 FHD |
| Touch | Multi-point capacitive touchscreen |
| OS | Android 13 |
| CPU | Quad-core 2.30 GHz |
| RAM | 4GB |
| Storage | 64GB |
| VESA | 100x100 confirmed |
| Condition | Very Good — Refurbished (eBay certified) |
| Seller | Sunnking Sustainable Solutions |
| eBay item | 205826242798 |
| Price | $349.99 + shipping |
| Warranty | 1 year |

### Mount — Ergotron LX 45-243-026

| Spec | Value |
|------|-------|
| Model | Ergotron LX Single Monitor Arm Wall Mount |
| Part number | 45-243-026 |
| Type | Friction-based articulating arm |
| Capacity | 25 lbs (monitor ~8 lbs — well within spec) |
| VESA | 75x75 and 100x100 compatible |
| Extension | 15-21" — sufficient for corner float |
| Price | $64.99 + shipping |

**Why friction not gas spring:** Touchscreens require constant arm actuation on every tap. Gas spring arms move — screen wobbles on touch. Friction arms stay exactly where placed. Ergotron LX is the industry standard for touchscreen installations.

### Thin Client

**None needed.** The PatientPoint unit IS the computer. Android 13 onboard. Fully Kiosk Browser runs the widget directly.

---

## Server Infrastructure

### ThinkPad X1 Carbon — Headless Server

| Spec | Value |
|------|-------|
| Machine | ThinkPad X1 Carbon |
| Windows user | ThinkPad X1 Carbon (with spaces — legacy) |
| Role | Dedicated headless server — Cockpit host + automation host |
| OS | Windows (PowerShell 5.1, headless — lid closed, always on) |
| Static IP | 192.168.1.60 |
| Server software | Python HTTP server (`python -m http.server 8080`) |
| Serves | `cal-widget-current.html`, `calendars.md`, `recipes-index.json`, `recipes/*.json`, `last-pull.json`, `data-age.json` from `C:\Users\ThinkPad X1 Carbon\Documents\family-ops` |
| Cockpit reaches it via | Local LAN — Fully Kiosk Browser on Cockpit -> 192.168.1.60:8080 |
| Automation | ThinkPad is the automation host for the entire watcher layer. See `ops/watcher-layer.md` for the full roster (PullJob, GraphSync, InboxWatcher, Watchdog, NightWatch, WeeklyPush). |

**The ThinkPad is a single point of failure for everything.** Cockpit data, calendar sync, receipt filing, and all monitoring run on this one machine. If it dies, they all die together, and the only signal is the Cockpit going dark at 00:01. This is a known and accepted architecture — the Cockpit dead-man is the mitigation. Bare-metal imaging of this machine is an open PQ (`backup-imaging-tool`).

**Pull job:** `scripts/pull-job.ps1`, runs every 3 min via `BayerFamilyOps-PullJob`. Heartbeat at `logs/pull-heartbeat.log`. On every exit-0 pull, writes `last-pull.json` (Watchdog reads this for staleness) and `data-age.json` (widget reads this for the sync banner — carries `calendars.md`'s true last-modified time). Both are gitignored runtime state.

---

## Network Infrastructure

- **ISP:** Starlink. **Wi-Fi:** "7 Little Bears" (5 GHz) / "7LittleBears 2.4" (2.4 GHz).
- **Topology:** Starlink Gen 2 Standard Actuated dish -> Gen 2 router (main, office) -> second Gen 2 router running as a mesh node (kitchen). Wireless backhaul, no wired link between them (~-72 dBm). House is ~25x70 ft; main router serves the office half, mesh node serves the kitchen half. Cockpit is on the kitchen/mesh side.
- **Subnet:** 192.168.1.0/24, gateway .1. Starlink app CAN change the subnet (confirmed 2026-07-12: options include 192.168.x.1/24 and 10.x.0.1/16). This matters for any future router-in-front deployment — moving Starlink's subnet is how the ThinkPad keeps 192.168.1.60.
- **CGNAT:** Starlink public IP is carrier-grade NAT (100.64.x.x/10). No inbound reach, no port forwarding, no VPN server. All remote access is repo-mediated by design.
- **No cell service at the property.** Wi-Fi is the only internet path. Mobile-data bypass of any network control is physically impossible here — a real advantage for parental control, and the reason NightWatch (network monitoring) is viable at all.

### Starlink hardware is US-made — FCC-exempt

Starlink routers are manufactured at SpaceX's Bastrop, Texas facility. The March 2026 FCC action added all *foreign-produced* consumer routers to the Covered List, with firmware/security updates on previously authorized foreign models cut off after **March 1, 2027**. Starlink hardware is domestic and exempt from that cliff. Practical consequence: the two Starlink routers are the safest networking hardware in the house and are NOT disposable. Any third-party security appliance (e.g. Firewalla — see below) must be checked for production origin before purchase, because a security box that stops receiving patches in March 2027 is not a security box.

### Firewalla — evaluated, deferred (NOT purchased, NOT spec-confirmed)

A Firewalla was evaluated for per-device parental control and network security. It is **deferred**, not planned-imminent. Corrections to prior notes in this file, all verified 2026-07-12:

- **Purple SE does NOT have built-in Wi-Fi.** It needs a separate access point (Firewalla AP7, or a third-party AP in bridge mode). Earlier claims of built-in Wi-Fi were wrong.
- **CPU is 4-core, not 6-core.** (The non-SE Purple is 6-core.)
- **Price is not "~$329."** Verified direct: Purple SE $279, Orange $389, AP7 $369 each. Never quote from memory.
- **It cannot "work alongside" the Starlink routers.** Putting any third-party router in front requires Starlink Bypass mode, which kills BOTH Starlink routers' Wi-Fi (the Gen 2 router has no Ethernet port — needs the Starlink Ethernet Adapter) AND kills the mesh node (mesh nodes only work with the Starlink router). So a Firewalla deploy means it must supply 100% of household Wi-Fi. On a no-wired-backhaul house, that's ~$600+ in hardware.
- **VPN server does not work behind CGNAT.** The listed "VPN for remote access" benefit is dead on this connection (inbound). Outbound VPN *client* on a laptop is unaffected but is software on the laptop, not a Firewalla function.
- **Regulatory status unconfirmed.** Firewalla's production origin and whether it holds an FCC Conditional Approval are unverified. Email them before any purchase. (Open PQ.)

**Why deferred:** The actual need is one school Chromebook, inbound, remote-school, that the district's MDM leaves unrestricted at night. The cheap controls all fail because Wyatt knows the house Wi-Fi password and Android devices display it in plain text, and because ChromeOS randomizes its MAC per network (defeating MAC filtering and Starlink's per-device Pause). The chosen path is NightWatch (detect) + a physical drawer lock (control offline use) — not a $600 network rebuild five weeks before a baby, on a part-time income. Firewalla revisits in ~2 years when more kids have school machines and the money is easier.

**If Firewalla is ever deployed:** the Cockpit MUST be placed in an unrestricted device group — it is not a child's device and must reach 192.168.1.60 without interference.

---

## Full System Architecture

```
INTERNET -> Starlink dish (Gen 2) -> Starlink Gen 2 router (main, office) [CGNAT, 192.168.1.0/24]
  -> "7 Little Bears" Wi-Fi (office half)
  -> Starlink Gen 2 mesh node (kitchen half, wireless backhaul)
      -> ThinkPad X1 Carbon (192.168.1.60) [Python HTTP :8080; watcher layer host]
      -> PatientPoint Cockpit (Android 13) [Fully Kiosk -> 192.168.1.60:8080]
      -> Dell Precision 5690 "mbay" (Matt's primary)
      -> Kalea's device
      -> Wyatt's school Chromebook [NightWatch observes; drawer lock controls offline]
```

---

## Cockpit Software Configuration

**Browser:** Fully Kiosk Browser (active)
**Start URL:** `http://192.168.1.60:8080/cal-widget-current.html`

| Setting | Value |
|---------|-------|
| Auto-reload idle | 86400s |
| Scheduled daily reload | 00:01 |
| All 4 auto-reload triggers | ON |
| Cache clear on reload | ON |
| Web storage/history/cookies delete | OFF |
| Load current page on reload | OFF |
| Skip reload if showing start URL | OFF |

**Admin access:** Three-finger long press on glass. Or browser: `http://192.168.1.60:2323`

---

## Widget Design Constraints

| Constraint | Value |
|------------|-------|
| Resolution | 1920x1080 |
| Screen size | 32" |
| OS | Android 13 / Fully Kiosk Browser — standard HTML/CSS/JS only |
| Touch | Capacitive multi-touch — minimum 44px tap targets |
| Always-on | Dark theme default |
| Night mode | After 21:00 — brightness down, wake prompt on tap (manual-only, no auto-relight) |
| Network | LAN only — widget fetches from ThinkPad |
| Colorblind | Never red-vs-green alone for meaning — pair with brightness, shape, or label (Matt is red-green deficient) |

**Widget MCP limit:** The widget HTML is ~167KB and CANNOT be pushed via MCP. It is patched manually on the Precision (PowerShell) and pushed via git in a dedicated commit, separate from repo writes. Precision has a history of overwriting MCP commits — always `git pull --rebase` on Precision before pushing. See `cal-widget.md`.

---

## Software Gates

| Gate | Description | Status |
|------|-------------|--------|
| 1 | Widget loads clean — Kalea can use without instruction | GREEN |
| 2 | At least 2 agents writing to `calendars.md` reliably via Foreman handoff | OPEN |
| 3 | Stockyard S8 durability fix shipped | OPEN |
| 4 | ThinkPad running headless clean for 1 full week without babysitting | GREEN |

**S8 gate discipline:** No real flock data entry until S8 is resolved. Stockyard runs display-only until then.

---

## Budget Summary

| Item | Status | Price |
|------|--------|-------|
| PatientPoint 32" Android Wallboard | PURCHASED | $349.99 |
| Ergotron LX Wall Mount (used) | PURCHASED | $64.99 |
| **Cockpit total** | | **$414.98** |
| Firewalla | Deferred (~2 years) | — |
| Habit Control drawer lock (Wyatt) | Planned | $81 (standalone lock) |

---

## Phase 3 North Star

**Status:** Vision locked. No build until all prior gates are green.

Full Home Improvement voice cast (ElevenLabs Creator $22/mo), sound layer (local files, Web Audio API), daily liturgical briefing (Wilson/Foreman), video calling station (USB camera + WebRTC), weather integration (Foreman owns), sensor feeds (Stockyard + farm), motion-triggered wake (Fully Kiosk native).

Foundation placeholders wired in widget: `speak()`, `playSound()`, `VOICE_CAST`, `scheduleMorningBriefing()`, `ccirAlert()`, `dinnerReminder()`. All dormant. Do not activate without Phase 3 gate clearance.
