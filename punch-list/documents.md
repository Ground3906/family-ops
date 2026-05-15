# Bayer Household Documents Tracker

**Schema version:** 1
**Owner:** Punch List
**Capture model:** Opportunistic. Document surfaces during a chat session (renewal letter, expiration reminder, lookup request) → Punch List captures it then. Not via systematic hunt.
**Last updated:** 2026-05-15

---

## Operating principles

1. **Renewal-watch is the primary value.** The point of this file is to surface expirations before they bite. Each tracked document has an expiration date (or "no expiration") and Foreman gets a renewal-prompt milestone derived from it.
2. **Sensitive numbers stay off-disk.** Document numbers go here only if they''re considered low-sensitivity (driver license number is fine; SSN is not). High-sensitivity numbers (SSN, account numbers, passwords) never appear in this file or anywhere in the repo.
3. **One file per fact.** Document expiration dates live here. Foreman references; doesn''t duplicate.
4. **Reflag suppression.** A document explicitly marked lapsed/dormant (e.g. CCW) does not get re-surfaced as a renewal candidate unless Matt explicitly reopens it.

---

## Driver licenses

| Person | DL number | Issuing state | Expires | Renewal lead | Notes |
|---|---|---|---|---|---|
| Matt | 03-163-0479 | CO | 2028-12-07 | 90 days | Standard CO DL |
| Kalea | 17-056-2924 | CO | 2027-05-27 | 90 days | Veteran indicator on license |

Foreman prompts at expiration minus 90 days for each.

---

## Federal IDs

| Person | Type | Expires | Renewal lead | Notes |
|---|---|---|---|---|
| Kalea | CAC (DoD ID) | 2026-07-31 | 45 days | Renewal via DEERS appointment. **Earlier-rather-than-later given Aug 2026 birth timing.** |
| Matt | (no current federal ID tracked) | — | — | Marine veteran; VA ID card not currently issued |
| Wyatt | (none) | — | — | |
| Other kids | (none) | — | — | |

**Kalea CAC — priority renewal track.** Active USMC Reserve IMA, MARFORPAC. CAC must remain current for drill access, DEERS dependent management, and travel orders. Foreman fires prompt 2026-06-15 for DEERS appointment scheduling.

---

## Concealed Carry Weapons (CCW)

| Person | Status | Notes |
|---|---|---|
| Matt | **Lapsed** | Do not re-flag as a renewal candidate. If Matt reopens the topic, this row is reactivated. Otherwise dormant. |

---

## Vehicle / trailer registrations

Cross-referenced from `fleet-state-v1.md`. This table is the renewal-date index; full vehicle records live there.

| Asset | Registration expires | Renewal lead | Notes |
|---|---|---|---|
| NV3500 | TBD | 60 days | Capture month during next renewal cycle |
| Ford F-250 | TBD | 60 days | Capture month during next renewal cycle |
| Dodge Ram 2500 | TBD | 60 days | Custer County rural — exempt from CO emissions testing |
| Chevy Tahoe | TBD | 60 days | Capture month during next renewal cycle |
| Deck trailer | 2027-05 | 60 days | May renewal cycle |
| Jackson 8-pen | 2026-10 | 60 days | ⚠️ Closest time-sensitive registration item in fleet |
| Gehl skid steer | N/A | — | Off-road equipment, no registration |
| ATV | TBD | — | Hunting asset only; off Punch List radar — Mystery Ranch owns |

---

## Insurance policies

| Policy | Carrier | Renewal cycle | Notes |
|---|---|---|---|
| Auto (all vehicles) | USAA | Semi-annual | See `Auto_Policy_Summary___USAA.pdf` in repo |
| Homeowners | USAA | Annual | See `homeownersinsurance.pdf` |
| Pen trailer | USAA | Annual | See `pentrailerinsurance.png` |
| Personal property / umbrella | USAA | Annual | See `ppinsurance.png` |
| Health (Kalea + dependents via Matt employer) | TBD | — | Capture during open enrollment |
| Life | TBD | — | Capture as discovered |
| Disability | TBD | — | Capture as discovered |

Renewal prompts: Foreman fires at policy renewal minus 30 days.

---

## Hunting licenses & draws

Cross-referenced from `mystery-ranch/draws.json` (when chartered). Mystery Ranch owns; Punch List references for renewal-date awareness.

| License | Expires / draws | Notes |
|---|---|---|
| CO Hunter Education card | (no expiration) | One-time qualification |
| Annual hunting license — Matt | Cycle TBD | Mystery Ranch tracks |
| Draw applications | Spring annually | Mystery Ranch owns |

---

## Farm / LLC (Edelweiss Farms)

| Document | Expires / renews | Notes |
|---|---|---|
| LLC registration (CO Secretary of State) | TBD | Annual periodic report — capture date |
| EIN | (no expiration) | IRS-issued, permanent |
| Sales tax license (if applicable) | TBD | Capture status |
| Cottage food / egg sales paperwork | TBD | Capture if relevant to current sales channel |

---

## Property

| Document | Notes |
|---|---|
| Deed — 1722 Edelweiss Dr | Recorded with Custer County |
| Mortgage | Cross-references Auto/Homeowners insurance carrier; capture servicer + account info offline only |
| Property tax | Annual cycle, Custer County. Capture due-date pattern during next cycle. |
| Well permit | CO Division of Water Resources. Capture permit number during next interaction. |

---

## Financial accounts

**Tracked here:** institution names and account-type categories only. Account numbers, balances, login credentials — none of those live in this repo. Ever.

| Institution | Account type | Notes |
|---|---|---|
| USAA | Banking, insurance | Primary household relationship |
| (Others) | TBD | Capture institutions only, not account numbers |

---

## Foreman prompt schedule (derived)

Foreman fires these on the calendar as renewal milestones.

| Fire date | Prompt | Source |
|---|---|---|
| 2026-06-15 | Kalea CAC renewal — schedule DEERS appointment (expires 2026-07-31) | Federal IDs |
| 2026-08-01 | Jackson trailer registration renewal (expires 2026-10) | Vehicle registrations |
| 2027-02-27 | Kalea CO DL renewal — 90 days out (expires 2027-05-27) | Driver licenses |
| 2027-03 | Deck trailer registration renewal (expires 2027-05) | Vehicle registrations |
| 2028-09-07 | Matt CO DL renewal — 90 days out (expires 2028-12-07) | Driver licenses |

Punch List re-derives this schedule whenever a document row changes. Foreman reads; doesn''t restate.

---

## Decision log

| Date | Decision | Rationale |
|---|---|---|
| 2026-05-15 | Documents tracker established under Punch List | Single index for all expiration-sensitive household documents; Foreman derives renewal prompts from this file. |
| 2026-05-15 | Opportunistic capture model adopted | Avoid up-front data-entry burden. Documents land here as they surface naturally. |
| 2026-05-15 | CCW lapsed-state preserved as dormant; do not re-flag | Matt''s explicit standing instruction. |
| 2026-05-15 | High-sensitivity numbers (SSN, account #, passwords) excluded from this file permanently | Repo security policy. |

Schema changes: bump version, log here.
