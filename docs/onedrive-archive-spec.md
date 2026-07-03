# OneDrive Archive — Design Spec

**Locked:** 2026-06-27 — Session 1 design lock (Opus). This document is gospel for Session 2. No design decisions remain open. Session 2 builds exactly this.

**Drive spec confirmed:** 2026-07-03 — ThinkPad pre-flight complete. Hardware is Samsung MZVLW512HMJP 512GB NVMe SSD (475.57 GB usable, 226.34 GB free). Charter "2TB SSD" designation was incorrect and has been corrected in v2.9.

---

## What This Is

The binary archive transport layer for Bayer Family Ops. Matt and Kalea drop receipts, repair orders, insurance docs, scanned recipe cards, and whiteboard photos from any device into a shared OneDrive folder. The ThinkPad syncs everything down to the 512GB NVMe SSD. Agents extract facts to JSONL logs on first read; the original stays in the archive for warranty, resale, or dispute.

This is the OneDrive side only. The ThinkPad local archive, the watcher automation, and the doctrine writeup are Sessions 2, 3, and 4 respectively.

---

## Locked Architecture

### 1. Root folder

- Name: `Filing Cabinet`
- Location: Matt's OneDrive root (My Files root level)
- Owner: Matt's account
- Shared to: `kalea.bayer.co@outlook.com` (read-write)
- Synced to: ThinkPad 512GB NVMe SSD (Samsung MZVLW512HMJP, 475.57 GB usable; confirmed 2026-07-03)
- Path note: the folder name contains a space. Every script that references it quotes the path. No exceptions.

### 2. Structure

Flat. No subject subfolders. No category tree. Originals accumulate freely at the root of `Filing Cabinet`. When an agent needs a specific original it digs by filename or date. The folder is never browsed for category; it is searched on deliberate need.

Rationale: subject folders add a sorting decision at drop time, which is the one moment friction must be zero. Retrieval is rare and faster by search than by hierarchy.

### 3. Drop zone

- Subfolder: `Inbox` inside `Filing Cabinet`
- This is where every new file lands, from any device, by any person
- Location is status: a file in `Inbox` means pending processing
- A file at the `Filing Cabinet` root means processed and filed
- The watcher (Session 3) performs the move after extraction

### 4. Queue zone

None. `Inbox` doubles as the queue. There is no intermediate queue folder. A complete file sitting in `Inbox` is the ready signal. The watcher reads from `Inbox`, extracts facts to the appropriate JSONL log, then moves the original to the `Filing Cabinet` root.

### 5. Watcher trigger rules

**Grabs:** PDFs (`.pdf`) and images (`.jpg`, `.jpeg`, `.png`). These are the file types in scope: receipts, repair orders, insurance docs, scanned recipe cards, whiteboard photos.

**Ignores:** OneDrive temp files (`.tmp`, `~$*`), lock files, zero-byte files, online-only placeholders not yet downloaded to the 512GB SSD.

**Ready signal (both gates must clear before the watcher touches a file):**
1. Placeholder check: the file is marked fully downloaded locally by the OneDrive client, not online-only or still-syncing.
2. Size stability: the file's byte count holds steady across two consecutive checks. Exact interval is tuned in Session 3.

Rationale: gate 1 is cheap and kills obvious junk. Gate 2 is the backstop that guarantees nothing half-landed gets processed. This is the durability lesson applied: no silent state.

**Session 2 build note:** set `Filing Cabinet` to "Always keep on this device" in the ThinkPad OneDrive client. This forces actual local copies instead of online-only stubs, so the watcher always has real files to inspect.

### 6. Kalea's drop path (Android)

- Method: Android share sheet
- Flow: snap or open a file in any app, tap Share, pick OneDrive, navigate to the shared `Inbox`, drop
- One-time setup (Session 2): she accepts the share invite and taps "Add to my OneDrive" so the Inbox appears in her own folder tree and the share sheet can target it in two taps
- Paper receipts: OneDrive's built-in Scan function converts a photo to a clean PDF and deposits it directly, available alongside the share-sheet path
- Friction target: one share, two taps. No sorting, no naming, no decisions

---

## Session 2 Build Checklist

Run in this order. Each step has a verification before moving on.

**Pre-flight: verify drive specs on the ThinkPad** — COMPLETE 2026-07-03
Hardware confirmed: Samsung MZVLW512HMJP 512GB NVMe SSD, 475.57 GB usable, 226.34 GB free. Charter corrected to v2.9.

**Step 1. Create the folders in OneDrive** — COMPLETE 2026-07-03
- `Filing Cabinet` created at My Files root in Matt's OneDrive
- `Inbox` created inside `Filing Cabinet`
- OneDrive storage confirmed: 1TB (M365 Family, per-account, not pooled)

**Step 2. Share to Kalea** — COMPLETE (pending Kalea acceptance)
- `Filing Cabinet` shared to `kalea.bayer.co@outlook.com`, Can edit
- Kalea to accept invite on her Android and tap "Add to my OneDrive"

**Step 3. Configure ThinkPad OneDrive sync**
- On the ThinkPad, confirm OneDrive client is signed into Matt's account
- Locate `Filing Cabinet` in the OneDrive folder tree
- Right-click, "Always keep on this device"
- Wait for sync to complete, verify `Filing Cabinet` and `Inbox` exist locally on C: at the discovered OneDrive sync path (record actual path here)

**Step 4. Smoke test**
- Matt drops a test PDF into `Inbox` from his phone via the share sheet
- Kalea drops a test image into `Inbox` from her Android via the share sheet
- Verify both files appear in `Filing Cabinet\Inbox` on the ThinkPad within a few minutes
- Verify the OneDrive client shows them as fully downloaded (not cloud-only icons)
- Clean up the test files after verification

**Step 5. Update the charter**
- Add the confirmed local ThinkPad path to `Filing Cabinet` in the charter Storage Tiers section
- Commit via MCP

---

## Parked Items (Surface in Session 3)

**PQ `archive-disk-monitor`**
Free-space monitoring on the archive drive. Build note: this check rides the watcher heartbeat, not a standalone script. Alert fires via the existing Microsoft Graph email hookup when free space drops below threshold. Threshold TBD — drive capacity confirmed at 475.57 GB usable, 226.34 GB free as of 2026-07-03. Set threshold in Session 3 based on expected accumulation rate. Cloud side (1TB per account, not pooled) is already handled by Microsoft's own usage alerts.

**Watcher stability interval**
The exact number of seconds for the size-stability check is tuned in Session 3 against a real test drop. Not a lock for Session 1 or 2.

---

## What Is Not Changing

- Archive is binary-only. No structured data, no JSONL, no text files go into `Filing Cabinet`. Those live in the repo.
- The repo is still the source of truth. OneDrive only carries what the repo should never carry.
- Extract-then-file doctrine stands. Agents work from JSONL extracts; originals are pulled from the cabinet only on deliberate need (warranty, resale, dispute).
- Automation layer carries no AI. The watcher is deterministic plumbing. Reasoning stays in the Interactive layer.
