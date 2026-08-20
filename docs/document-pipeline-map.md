# Document Pipeline — Map & Single Source of Intent

**Burned in:** 2026-08-20. This file is the arbiter for all document-pipeline architecture.
**Standing rule:** Any session touching document intake, extraction, or logging reads this file before proposing anything. A proposal that contradicts the Locked section gets flagged against this file and stops — locked items are never re-presented as options. The Open Items section below is the complete list of open questions. If it is not listed there, it is not open.

---

## The promise — what "working" means

Matt or Kalea drops a document into `Filing Cabinet\Inbox` from any device and forgets it. The system files it, records its arrival, and at the next session touch an agent reads it, extracts the real facts with Matt confirming the numbers in-session, and logs them in the right place with a pointer back to the original. Nobody has to remember anything — the session-open hook does the remembering.

Latency is "next session," by design. Nothing in the cabinet is time-critical; a receipt sitting until the next session touch costs nothing (locked 2026-07-09, watchdog cadence discussion). Anyone proposing faster-than-session extraction is proposing to reopen a locked decision and must say so explicitly.

---

## Locked — do not re-litigate

1. **Automation layer carries no AI.** The watcher is deterministic plumbing. Reasoning stays in the Interactive layer. (`docs/onedrive-archive-spec.md`, locked 2026-06-27)
2. **Extraction is Interactive-layer work.** Agents in chat sessions do the reading and extraction, on the existing Claude subscription. Zero per-call API cost, by design. No script ever calls a paid model API. (spec, 2026-06-27)
3. **Extract-then-file.** Agents extract facts to JSONL logs on first read; the original stays in the cabinet, pulled again only on deliberate need — warranty, resale, dispute. (spec + Profile doctrine)
4. **Watcher output is arrival records only.** The runtime log keeps its `extracted_facts: {}` stub (locked 2026-07-09); the committed arrival record is `logs/receipts-index.jsonl` — four fields, carried to the repo by weekly-push (built 2026-08-19). The watcher never reads document contents.
5. **No per-arrival notifications.** Watcher alerting is errors and stale-heartbeat only. Arrivals are caught by the session-open hook, not by email. Per-file arrival pings were explicitly rejected. (locked 2026-07-09)
6. **Direct read path.** Sessions read originals straight from the cabinet via the Filesystem connector rooted at `C:\Users\ThinkPad X1 Carbon`. No re-upload to chat. (proven end-to-end 2026-08-20, Tahoe RO 48460)
7. **Numbers get human eyes.** Extracted dollar amounts, mileage, and dates are shown to Matt in-session and confirmed before they land in any financial or fleet log. In-session confirm is the mechanism — no separate confirm infrastructure exists or is needed. (2026-08-19/20)

---

## Built and live — as of 2026-08-20

- Watcher detects, indexes, and files arrivals with truthful logging (commits `74a4fd28`, `efc36caa`).
- `logs/receipts-index.jsonl` live in the repo, backfilled to 2026-07-09. This is the visibility channel the original design was missing.
- Direct cabinet read proven: Tahoe RO 48460 extracted from the original PDF and logged to `punch-list/maintenance-log.jsonl` through this exact path.

---

## To build — in order

### 1. Session-open arrivals hook (the missing piece)

Doctrine, not code. Agent session-open routine gains one step: read `logs/receipts-index.jsonl`, identify arrivals not yet extracted to a domain log, surface them, extract via direct cabinet read, confirm with Matt, append to the correct log. Files touched: `al.md`, `punch-list.md`, `chow-hall.md` at minimum. Gets its own design session; hook language locked line-by-line there.

**Open items to lock in that session — not locked yet:**
- **Processed-tracking:** how the hook knows an arrival has been handled. Candidates: a source-reference field on domain-log records, a small processed-marker log, or date/asset inference. Pick one there.
- **Agent coverage at launch:** which agents carry the hook on day one.
- **Non-receipt arrivals:** what "deliberately skipped" looks like for files that have no extraction target (personal photos, one-off scans).

### 2. Backlog sweep — the hook's first live run

Roughly 17 indexed arrivals predate the hook (everything in the index except Tahoe RO 48460). One session walks the index: classify each, extract what has a home, deliberately skip what does not, so the board starts clean.

### 3. Routing table

Derived from existing agent ownership — confirm at the hook design session, then lock here:

| Document type | Agent | Destination |
|---|---|---|
| Vehicle/equipment repair orders, service receipts | Punch List | `punch-list/maintenance-log.jsonl` |
| Fuel receipts | Punch List | `punch-list/fuel-log.jsonl` |
| Grocery receipts | Chow Hall | buy-rate learning |
| Medical documents | First Aid Kit | health records |
| Insurance, IDs, registrations, renewals | Punch List | `punch-list/documents.md` |
| No extraction target | — | Filed only; deliberately skipped, noted in sweep |

---

## What this file is not

Not session state. Live build status rides spin-up prompts, never this file. This file changes only by locked decision, recorded below.

---

## Decision log

| Date | Decision |
|---|---|
| 2026-08-20 | Map established as the single source of intent for the document pipeline. Locked section consolidates 2026-06-27 spec, 2026-07-09 build locks, and 2026-08-19/20 pipeline fixes. Root cause of the gap recorded: the 2026-07-09 session locked extraction as a stub for "a future real-extraction pass" but opened no tracking item for that pass, and the arrivals log stayed machine-local — so the Interactive layer could never see what the Automation layer filed. Both halves now closed or scheduled above. |
