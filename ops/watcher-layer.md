# The Watcher Layer

**Altitude:** Project doctrine. Architecture, not session state. Current build status lives in the spin-up baton, never here.

This file describes the automated monitoring layer of Bayer Family Ops: what each watcher is, where it runs, what it stamps, and how a future Al reads it. Read this at session open alongside `ops/system-health.json`.

---

## The load-bearing fact

**Every watcher runs on the ThinkPad (192.168.1.60), as a SYSTEM scheduled task.** They share one power supply, one disk, one Task Scheduler service, one network path. If the ThinkPad dies, they ALL die in the same instant, and none of them can send a dying alert, because the thing that would send it is also dead.

A watcher inside the box can report that a sibling process died. It can never report that the box itself died.

**The only thing that catches a dead ThinkPad is the Cockpit going dark.** The Cockpit (kitchen touchscreen) runs a nightly hard-reload at 00:01 that clears cache and re-fetches from the ThinkPad. If the ThinkPad is down, that fetch fails against an empty cache and the screen goes dark. A dark Cockpit is the household's dead-man switch for the entire watcher layer. This is by design. Do not "fix" the nightly reload to fail gracefully without replacing this dead-man with something else.

Corollary: between a ThinkPad death and the next 00:01, the Cockpit keeps rendering the already-loaded page with a date from its own Android clock. It looks correct while being stale. This is why the widget must show its own data age (see PullJob below).

---

## The watchers

All tasks are named `BayerFamilyOps-<Name>` and run as SYSTEM on the ThinkPad.

### NightWatch
- **Does:** Passive LAN scan for unknown devices awake during the night window (21:30--06:00). Built to catch a school device in use after curfew.
- **Runs:** Every 5 min, time-gated inside the script. Outside the window it exits immediately (silence is correct).
- **Script:** `scripts/night-watch.ps1`
- **Stamps:** `archive/night-watch-heartbeat.txt`
- **Logs:** `logs/night-watch.jsonl` (one record per observation)
- **Session state:** `archive/night-watch-session.json` (tracks consecutive sightings between runs)
- **Observation types:** `blip` (< 3 consecutive checks, < 15 min sustained), `session` (>= 3 checks, >= 15 min sustained), `error`.

### Watchdog
- **Does:** Health checks on the other watchers plus disk and Filing Cabinet integrity. The supervisor of the on-box layer.
- **Runs:** 08:00, 14:00, 20:00 daily.
- **Script:** `scripts/watchdog.ps1`
- **Reads these heartbeats:** InboxWatcher, GraphSync, PullJob, NightWatch.
- **Writes:** `ops/system-health.json` -- the snapshot Al reads at session open.
- **Alerts:** via Microsoft Graph sendMail to matthew.bayer@outlook.com. Requires Mail.Send scope on the Graph token.
- **Cannot watch itself.** Nothing on the ThinkPad can. The Cockpit dead-man covers that gap.

### GraphSync
- **Does:** Syncs `calendars.md` to the Outlook calendar (and Kalea's shared calendar). Pre-existing.
- **Runs:** Every 3 min.
- **Stamps:** `scripts/graph-sync-heartbeat.txt`
- **Note:** Outlook is downstream of the ThinkPad. It is a second window onto the same data, NOT an independent backup. The only independent calendar copy is the repo.

### InboxWatcher
- **Does:** Monitors the OneDrive Inbox for receipts, records placeholders. Pre-existing.
- **Runs:** Continuously / on file events.
- **Stamps:** `archive/watcher-heartbeat.txt`

### PullJob
- **Does:** Pulls the repo to the ThinkPad so the Cockpit widget serves current data.
- **Runs:** Every 3 min.
- **Script:** `scripts/pull-job.ps1`
- **Writes:** `last-pull.json` (Watchdog reads this) and `data-age.json` (the widget reads this).
- **Why data-age.json matters:** A running PullJob proves the widget can reach the ThinkPad. It does NOT prove the data is fresh -- git can pull clean and pull nothing. The only ground truth for calendar freshness is `calendars.md`'s last-modified time, which PullJob writes into `data-age.json` for the widget's sync banner. Fetch-success is not data-age.

### WeeklyPush
- **Does:** Pushes the week's NightWatch log and the health snapshot from the ThinkPad up to the repo, so Al can read them.
- **Runs:** Sundays 06:05 (just after the night window closes).
- **Script:** `scripts/weekly-push.ps1`
- **Pushes:** `logs/night-watch.jsonl`, `ops/system-health.json`.
- **This is the seam.** NightWatch writes locally all week; WeeklyPush is how that data reaches the repo where Al reads it. Both files are `!`-negated in `.gitignore` so this push works -- do not remove those negations.

---

## The heartbeat map

Watchdog holds each watcher to a staleness threshold. Past the threshold = alert + `stale` status in `system-health.json`.

| Watcher      | Heartbeat file                          | Threshold | Why |
|--------------|-----------------------------------------|-----------|-----|
| InboxWatcher | `archive/watcher-heartbeat.txt`         | 6h        | Runs continuously |
| GraphSync    | `scripts/graph-sync-heartbeat.txt`      | 6h        | Runs every 3 min |
| PullJob      | `last-pull.json` (`last_ok` field)      | 6h        | Runs every 3 min |
| NightWatch   | `archive/night-watch-heartbeat.txt`     | 25h       | Only runs at night; max gap between nights ~15.5h |

---

## Session-open protocol for Al

At the start of every session:

1. Read `ops/system-health.json`.
2. If any check is `stale`, `missing`, or `parse_error`, surface it to Matt BEFORE anything else -- lead with it, plainly.
3. If `system-health.json` itself is old (check `last_updated`), that is itself a signal: Watchdog may not have run, which may mean the ThinkPad is down. Say so.
4. If everything is `ok`, do not narrate the health check. Silence is the correct output of a clean check.

The weekly synthesis (reading `logs/night-watch.jsonl` against `calendars.md` and `family.md`) is a separate, deliberate act -- Matt opens it, or a scheduled prompt does. That is where Al earns its keep: judgment against context, not arithmetic the ThinkPad already did.

---

## Phase roadmap

This is the permanent plan, not a status. Where the build actually stands lives in the spin-up baton.

- **Phase 1 -- Baseline.** NightWatch runs in logging-only mode. No digest, no alerts, no thresholds. It watches and writes. Runs for ~7 nights AFTER the target device (Chromebook) is on the network, to learn what that device does at night (background updates, sync, district pushes) before any threshold is set. Capture-as-you-go: true data beats a guessed threshold.

- **Phase 2 -- Threshold calibration.** Read the baseline log. Set the session/blip thresholds and the emergency-trigger conditions from real observed behavior, not speculation. Add household device MACs to the known-good list in `night-watch.ps1` so only the target device surfaces.

- **Phase 3 -- Live.** Enable the 06:30 morning digest (push only on a session, silent when clear). Emergency channel stays wired but disabled -- flipped on only for the weeks it's needed to establish that the system is real.

Alerting posture, locked: silent log + digest, emergency channel built and off. Delivery: push only on a detected session; a digest that arrives every morning saying nothing becomes wallpaper.

---

## What this layer does NOT do

- It does not see a device that is offline. A machine with its radio off, or in a drawer, is invisible to every network watcher. Offline use is covered by physical control (the drawer lock), not by NightWatch.
- It does not reach into the house from outside. Everything is repo-mediated. Starlink CGNAT blocks inbound access; there is no VPN server.
- It does not filter or block anything. It observes and reports. Blocking is a separate future decision (Firewalla, parked).
