# cockpit.md — Bayer Family Ops Display System

**Status:** Operational. ThinkPad headless. Widget v5.8 live. Pull job active (3-min cadence). Fully Kiosk 00:01 reload set.
**Last updated:** 2026-06-17

**Tablet clock confirmed (2026-06-17):** Mountain Daylight Time, network time ON, 24h format. Device clock is not a source of timing issues. Night dim at 21:00 is working as designed — widget dims and shows wake prompt, never fully powers off. Day rollover guard added to v5.8 as code backup to the 00:01 reload.

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
| OS | Windows (headless — lid closed, always on) |
| Static IP | 192.168.1.60 |
| Server software | Python HTTP server (`python -m http.server 8080`) |
| Serves | `cal-widget-current.html`, `calendars.md`, `recipes-index.json`, `recipes/*.json` from `C:\Users\ThinkPad X1 Carbon\Documents\family-ops` |
| Cockpit reaches it via | Local LAN — Fully Kiosk Browser on Cockpit -> 192.168.1.60:8080 |
| Automation | Scheduled pull job (git pull every 3 min) — LIVE. `scripts/pull-job.ps1`, heartbeat at `logs/pull-heartbeat.log`. |

**Current state:** ThinkPad is the dedicated headless server. Pull job is live, confirmed with two consecutive OK entries. Static IP 192.168.1.60 assigned.

---

## Network Infrastructure

- ISP: Starlink / Wi-Fi: "7 Little Bears"
- **Firewalla Purple SE** targeted deploy weekend 2026-07-11/12, before homeschool starts in August.
- Cockpit must be in unrestricted device group in Firewalla — it is not a child's device.

---

## Full System Architecture

```
INTERNET -> Starlink -> Firewalla Purple SE
  -> "7 Little Bears" Wi-Fi
      -> ThinkPad X1 Carbon (192.168.1.60) [Python HTTP :8080, git pull every 3 min]
      -> PatientPoint Cockpit (Android 13) [Fully Kiosk -> 192.168.1.60:8080]
      -> Dell Precision 5690 "mbay" (Matt's primary)
      -> Kalea's device
      -> Wyatt's device [Firewalla parental rules]
```

---

## Cockpit Software Configuration

**Browser:** Fully Kiosk Browser (active)
**Start URL:** `http://192.168.1.60:8080/cal-widget-current.html`

| Setting | Value |
|---------|-------|
| Auto-reload idle | 86400s |
| Scheduled daily reload | 00:01 (confirmed set 2026-06-17) |
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
| Night mode | After 21:00 — brightness down, wake prompt on tap |
| Network | LAN only — widget fetches from ThinkPad |

---

## Software Gates

| Gate | Description | Status |
|------|-------------|--------|
| 1 | Widget loads clean — Kalea can use without instruction | GREEN — v5.8+ |
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
| Firewalla Purple SE | Planned (July 2026) | ~$329.00 |

---

## Phase 3 North Star

**Status:** Vision locked. No build until all prior gates are green.

Full Home Improvement voice cast (ElevenLabs Creator $22/mo), sound layer (local files, Web Audio API), daily liturgical briefing (Wilson/Foreman), video calling station (USB camera + WebRTC), weather integration (Foreman owns), sensor feeds (Stockyard + farm), motion-triggered wake (Fully Kiosk native).

Foundation placeholders wired in widget v2.9: `speak()`, `playSound()`, `VOICE_CAST`, `scheduleMorningBriefing()`, `ccirAlert()`, `dinnerReminder()`. All dormant. Do not activate without Phase 3 gate clearance.
