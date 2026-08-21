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
8. **Session-open arrivals hook is Al-only.** Domain agents (Punch List, Chow Hall, IFAK) gain no session-open step of their own. Al detects, classifies by direct cabinet read, and routes extraction to the owning agent via the existing handoff mechanism. (locked 2026-08-20, hook design session)
9. **No-extraction-target arrivals are an exception, not a routine skip.** The inbox is for actionable documents; a file with no home in the routing table means something is wrong upstream, and Al surfaces it to Matt rather than filing it quietly. (locked 2026-08-20)
10. **Processed-tracking lives outside the watcher's file.** `logs/arrivals-processed.jsonl` is a separate, Interactive-layer-owned, MCP-written marker log. `logs/receipts-index.jsonl` stays machine-owned and is never hand-edited through MCP. (locked 2026-08-20)

---

## Built and live — as of 2026-08-20

- Watcher detects, indexes, and files arrivals with truthful logging (commits `74a4fd28`, `efc36caa`).
- `logs/receipts-index.jsonl` live in the repo, backfilled to 2026-07-09. This is the visibility channel the original design was missing.
- Direct cabinet read proven: Tahoe RO 48460 extracted from the original PDF and logged to `punch-list/maintenance-log.jsonl` through this exact path.
- **Session-open arrivals hook — doctrine locked and written into agent files.** Full mechanics in `al.md` (Document Arrivals Hook section). Receiving-end doctrine in `punch-list.md`, `chow-hall.md`, and `first-aid/ifak.md`. Appointment intake-routing consequence in `foreman.md` (Intake Routing — Medical & Household Appointments). Default-owner fallback in `crosstalk-handoff-map.md` (Bedrock Rule 8). First live run against the backlog is the next build item below.
- **Processed-marker log created:** `logs/arrivals-processed.jsonl`, empty at creation — populates starting with the backlog sweep.
- **Medical/non-medical appointment split executed:** `first-aid/appointments-log.jsonl` is medical-only (12 records). Three non-medical records (two benefit recertifications, one school-advisory appointment) migrated to new `punch-list/appointments-log.jsonl`.

---

## To build — in order

### 1. Backlog sweep — the hook's first live run

Roughly 17 indexed arrivals predate the hook (everything in the index except Tahoe RO 48460 and the `test-smoke.pdf` watcher test artifact). One session walks the index: Al opens each via direct cabinet read, classifies, routes what has a home, surfaces as an exception what doesn't — per the Locked hook doctrine above, not the old "deliberately skipped" language, which is superseded. Gets its own session unless Matt extends this one.

---

## Routing table — LOCKED 2026-08-20

Derived from existing agent ownership, confirmed at the hook design session.

| Document type | Agent | Destination |
|---|---|---|
| Vehicle/equipment repair orders, service receipts | Punch List | `punch-list/maintenance-log.jsonl` |
| Fuel receipts | Punch List | `punch-list/fuel-log.jsonl` |
| Grocery receipts | Chow Hall | `chow-hall/buy-rate.md` (markdown pending JSONL conversion — see Open Items in `chow-hall.md`) |
| Medical documents | IFAK | Split at extraction: appointment/visit events → `first-aid/appointments-log.jsonl`; narrative, conditions, diagnoses → `first-aid/people/<INITIALS>.md`, per IFAK's own Capture Rules |
| Insurance, IDs, registrations, renewals | Punch List | `punch-list/documents.md` |
| No extraction target | Al | Surfaced to Matt as an exception — the file's presence in the inbox indicates a routing problem upstream. Not filed quietly. See Locked #9 and `al.md`. |

**Non-medical household appointments (2026-08-20 addendum):** `first-aid/appointments-log.jsonl` is medical-only as of this session. Appointments that are not medical — benefit recertifications, school-advisory sessions, and similar — route to `punch-list/appointments-log.jsonl` instead, as the default-owner fallback (`crosstalk-handoff-map.md` Bedrock Rule 8). Al makes the medical/non-medical call at intake — see `al.md` and `foreman.md`'s Intake Routing section. Applies to both document-triggered appointments and appointments Matt or Kalea enter directly in chat.

---

## What this file is not

Not session state. Live build status rides spin-up prompts, never this file. This file changes only by locked decision, recorded below.

---

## Decision log

| Date | Decision |
|---|---|
| 2026-08-20 | Map established as the single source of intent for the document pipeline. Locked section consolidates 2026-06-27 spec, 2026-07-09 build locks, and 2026-08-19/20 pipeline fixes. Root cause of the gap recorded: the 2026-07-09 session locked extraction as a stub for "a future real-extraction pass" but opened no tracking item for that pass, and the arrivals log stayed machine-local — so the Interactive layer could never see what the Automation layer filed. Both halves now closed or scheduled above. |
| 2026-08-20 | Hook design session. Session-open arrivals hook locked as Al-only (domain agents gain no session-open step). Processed-tracking locked as a separate MCP-written marker log (`logs/arrivals-processed.jsonl`), never a write to the machine-owned index. No-extraction-target arrivals reclassified from routine skip to surfaced exception, per Matt's correction that the inbox is for actionable documents only — a non-actionable file's presence signals an upstream routing problem. Routing table confirmed with two corrections against the real files: Chow Hall destination is `chow-hall/buy-rate.md` (not the vaguer "buy-rate learning"), and IFAK's medical row splits at extraction rather than naming a single "health records" destination. Medical appointment log split into medical-only (`first-aid/appointments-log.jsonl`) and a new non-medical household appointments log (`punch-list/appointments-log.jsonl`), following discovery that the original medical log held three non-medical records (WIC recert, SNAP recert, school-advisory). Default-owner fallback established: unowned items route to Punch List. |
