# Backup and Recovery — Bayer Family Ops

**Locked:** 2026-07-09 — OneDrive Session 3 (Opus design, Sonnet execution).
**Updated:** 2026-07-12 — Watchdog now covers six checks (was three); detection layer cross-referenced to `ops/watcher-layer.md`; "silence is health" corrected to the liveness doctrine.

---

## The Honest Model

### Sync is not backup

OneDrive sync is a two-way mirror. Every file in `Filing Cabinet` exists in two places simultaneously: Microsoft's cloud and the ThinkPad's local disk. Changes propagate in both directions, continuously. A file dropped on a phone appears on the ThinkPad within minutes. A file deleted from a phone disappears from the ThinkPad within minutes.

This is the critical property: sync propagates destruction. Ransomware encrypts local files, sync pushes the encrypted versions to the cloud. A kid deletes a folder from a phone, OneDrive deletes it everywhere. A script runs with a wrong path and wipes a directory, the wipe syncs immediately. Sync makes a mistake happen in two places instead of one.

### What Microsoft 365 gives you

M365 Family subscription (1TB per account, not pooled) includes:

| Protection | What it covers | Window |
|---|---|---|
| Files Restore | Roll back the entire OneDrive to any point in time | Last 30 days |
| Version history | Restore any previous version of any file | 500 versions per file |
| Recycle bin | Recover deleted files | 93 days |
| Ransomware detection | Automated detection + guided recovery | Notifies on attack |

These cover the ordinary disasters: the wrong-phone delete, the accidental overwrite, a bad sync. They do not require any action until disaster strikes.

### What Microsoft 365 does not cover

1. The ThinkPad itself. Windows, scheduled tasks, scripts, Graph tokens, static IP config, the repo clone. None of it is in OneDrive. ThinkPad SSD dies: receipts survive in the cloud, the server is a weekend of rebuilding from memory. (This is the same single-point-of-failure noted in `cockpit.md` and `ops/watcher-layer.md` — the whole watcher layer shares this machine's fate.)
2. Subscription lapse. Card expires, nobody notices, Microsoft enforces the free 5 GB tier. This is the most likely way the archive gets compromised. Not dramatic, not sudden.
3. Account compromise. Attacker owns `matthew.bayer@outlook.com`, they own both OneDrive copies simultaneously.
4. The 30-day window closing. A quiet corruption on an unwatched headless machine has 30 days to become permanent. The watchdog file-count check is the mitigation.

---

## External Archive Drive (2TB SSD)

**Role: cold backup target for the ThinkPad.** Not overflow. Not a receipt guard. Those are handled by OneDrive.

**What it backs up:** Full bare-metal system image of the ThinkPad. This captures Windows, all scheduled tasks, all scripts, all configuration, all Graph tokens, the repo clone, and the Filing Cabinet as a byproduct (it lives on the same disk).

**Connection posture: physically disconnected between runs.** The drive stays unplugged except during a backup session. A drive with no power and no USB connection cannot be reached by ransomware, bad scripts, or anything else running on the ThinkPad.

**Cadence: quarterly.** The ThinkPad system layer barely changes after initial setup. It is a static machine running a handful of scripts. A quarterly image of a static machine is a fresh image.

**Imaging tool:** A third-party bare-metal imaging tool is required. Do not use PowerShell for this. See PQ `backup-imaging-tool` below.

**Capacity note:** The `(2TB SSD)` designation is a claimed capacity, not a verified one. Confirm actual usable capacity before the first backup run and update this file if different.

### Quarterly backup ritual

Owned by Punch List (voice and reminder). Calendar slot written by Foreman.

1. Punch List prompts: time to run the quarterly ThinkPad backup.
2. Matt plugs in the External Archive Drive (2TB SSD).
3. Matt runs the imaging tool (bare-metal capture of ThinkPad C: drive).
4. Matt confirms to Punch List: backup done.
5. Punch List logs completion.
6. Matt unplugs the drive.

The drive does not stay plugged in between runs. Unplugged means unreachable.

---

## Detection Layer

The watchdog (`scripts/watchdog.ps1`) runs at 08:00, 14:00, 20:00 daily via the `BayerFamilyOps-Watchdog` scheduled task. As of 2026-07-12 it runs **six checks** per run — it supervises the entire on-box watcher layer, not just the receipt watcher. Full architecture in `ops/watcher-layer.md`.

| Check | Condition | Action |
|---|---|---|
| InboxWatcher staleness | `archive/watcher-heartbeat.txt` older than 6h | Email alert |
| GraphSync staleness | `scripts/graph-sync-heartbeat.txt` older than 6h | Email alert |
| PullJob staleness | `last-pull.json` `last_ok` older than 6h | Email alert |
| NightWatch staleness | `archive/night-watch-heartbeat.txt` older than 25h | Email alert |
| Disk free space | C: drive below 75 GB free | Email alert |
| File count | Filing Cabinet root loses files since last check | Email alert |

Each run also writes `ops/system-health.json`, the snapshot Al reads at session open.

**Silence is not health.** A watcher that has stopped is silent, and an always-on process's silence must be indistinguishable from failure and treated as such — which is why every watcher stamps a heartbeat and the watchdog alarms on staleness rather than trusting quiet. The one thing the watchdog cannot catch is its own machine dying (it runs on the ThinkPad it watches); that gap is covered by the Cockpit going dark at 00:01. See `ops/watcher-layer.md` for the full liveness model.

### Disk threshold context

475.57 GB usable on the Samsung MZVLW512HMJP 512GB NVMe. 226.34 GB free as of 2026-07-03. The Filing Cabinet accumulates a few GB per year at most. The 75 GB threshold is a ThinkPad health alarm, not a Filing Cabinet capacity alarm. The thing that will cross it is Windows updates, log sprawl, or unexpected accumulation, not receipts.

---

## Storage Tiers

| Tier | What lives here | Protection |
|---|---|---|
| Cloud (OneDrive, 1TB) | Filing Cabinet (primary copy) | M365: 30-day rollback, 500 versions, 93-day recycle bin |
| ThinkPad local disk (512GB NVMe) | Filing Cabinet (sync mirror) + all server config | Watchdog detection only, not independently protected |
| External Archive Drive (2TB SSD) | Quarterly bare-metal image of ThinkPad | Air gap: drive unplugged between runs |

The cloud tier is the protected one. The local tier is a sync mirror that enables the watcher to operate on real bytes. The external drive catches the failure mode OneDrive cannot: total ThinkPad loss or account compromise.

---

## What Is Explicitly Ruled Out

- Cloud purge: never purge files from OneDrive to free space. The cloud is the protected copy. Local fills first and will not for decades at current accumulation rate.
- Overflow use of the external drive: not needed. See `archive-local-capacity` PQ.
- Daily or nightly external backup: the drive stays unplugged. A plugged-in drive is a reachable drive.
- Ubuntu Server conversion of the ThinkPad: struck 2026-07-09. ThinkPad stays Windows. Cockpit gate C closed. OneDrive has no first-party Linux client; the machine runs stably headless on Windows.

---

## Parked Questions

**PQ `backup-imaging-tool`**
A third-party bare-metal imaging tool is required. No tool has been selected or installed. Before the first quarterly backup: evaluate Macrium Reflect Free and at least one alternative, confirm free-tier bare-metal and bootable recovery media capability, install, run a test image, confirm restore works. Add the selected tool and version to this file when locked.

**PQ `archive-local-capacity`**
ThinkPad local disk fills before cloud does, roughly 20 years out at current accumulation rate. Resolution paths when threshold approaches: larger internal drive, or unpin cold material via OneDrive Files On-Demand (accepting it drops out of image coverage). Cloud purge is explicitly ruled out. Surfaces if the 75 GB watchdog threshold fires for archive growth rather than system bloat.

**PQ `archive-overflow-target`**
Resolved and closed 2026-07-09. Overflow concept retired. External Archive Drive (2TB SSD) is the cold backup target only, not an overflow volume.

---

## File Map

| File | Purpose |
|---|---|
| `scripts/inbox-watcher.ps1` | Polls Filing Cabinet Inbox, gates and files receipts |
| `scripts/watchdog.ps1` | Health checks: supervises all watchers + disk + file count; writes `ops/system-health.json` |
| `scripts/night-watch.ps1` | LAN activity monitor, night window (see `ops/watcher-layer.md`) |
| `scripts/weekly-push.ps1` | Sunday push of NightWatch log + health snapshot to repo |
| `scripts/pull-job.ps1` | Cockpit git pull every 3 min; writes `last-pull.json` + `data-age.json` |
| `scripts/setup-watcher-tasks.ps1` | Registers InboxWatcher + Watchdog. Run once as Admin. |
| `scripts/setup-nightwatch-task.ps1` | Registers NightWatch + WeeklyPush. Run once as Admin. |
| `ops/system-health.json` | Watchdog health snapshot; Al reads at session open |
| `ops/watcher-layer.md` | Full watcher-layer architecture, heartbeat map, session-open protocol |
| `archive/receipts-log.jsonl` | Append-only log of every filed receipt |
| `archive/watcher-heartbeat.txt` | Timestamp written by InboxWatcher on every 60-second cycle |
| `archive/night-watch-heartbeat.txt` | Timestamp written by NightWatch each run |
| `archive/watcher-error.log` | Processing errors logged by watcher |
| `archive/watchdog-state.json` | Persistent watchdog state: last file count, last run |
| `archive/watchdog-log.jsonl` | Append-only health check log |
| `logs/night-watch.jsonl` | Append-only LAN activity observations |
