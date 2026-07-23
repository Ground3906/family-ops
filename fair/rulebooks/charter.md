# Fair Rulebooks Charter

Standing subsystem. Governance lane: what the rules say. Fully separate from operational and results data (what happened at a given fair), which lives in year files. Weight-class definitions (printed break points) are rules and live here; animals slotted into classes and results are ops data and live in year files.

## Mission

Produce the delta framework between the Colorado State Fair (CSF) rule stack and the Custer County Fair premium book, feeding a county fair book reset. Two lenses:

1. **Divergence archaeology.** Where Custer deviated from CSF, and how we likely got there. Destination: a board conversation about the reset.
2. **Rule mechanics.** How CSF writes and adjudicates rules. Who holds interpretive authority, what is mandatory vs. discretionary, what outs staff reserve, what is hard and fast.

## Posture

State baseline by default. Local deviation by exception. Every exception deliberate and defensible. Logical end-state: a county book that adopts CSF by reference and prints only the exceptions.

## Sources

- **County (source of truth):** Matt's local 2026 Custer County Fair premium book. The PDF posted on custercountygov.com is not used.
- **State:** CSF 2026 General Competition Requirements; CSF 2026 Exhibitor Handbook (verify whether the posted "Full TOC" file is the complete book, else pull per-division PDFs); CSF 2026 Livestock Schedule (publication-pattern reference for the addendum concept); Colorado 4-H State Fair Exhibit and Contest Requirements where a county department has no CSF analog.
- **Scope rule:** Custer's own department list drives the CSF pull. Nothing pulled that Custer does not operate, with two overrides: poultry and turkey are pulled full-depth as revival program source material (expect the health requirements lane to be heavy: HPAI surveillance, pullorum-typhoid testing). A county department with no CSF analog (likely shooting sports, whose state analog lives in Colorado 4-H documents) is itself a finding.

## Repo layout

```
fair/rulebooks/
  charter.md               (this file)
  archive/                 (raw source PDFs, year-stamped filenames)
  extracts/                (lean markdown extracts, one per source)
  divergence-map.md        (deliverable 1)
  rule-mechanics.md        (deliverable 2)
  volatility-inventory.md  (deliverable 3)
```

Extract-then-file: work happens on extracts; originals are pulled from archive only on deliberate need.

## Deliverable 1: divergence-map.md

Single linear markdown master. v1 audience is Matt's own parse. The board-facing line-by-line version is a later conversion pass generated from this master with no re-research.

- **Part 1, Heavy Hitters.** Posture-level comparison of load-bearing rule areas. Candidate list (final list derives from the two books at extraction): eligibility and residency, ownership and possession deadlines, weigh-in and weight-class construction, health and vet requirements, drug residue and show ethics, sale rules, judging systems, protest and appeals. Each area carries: state posture, county posture, gap size, disposition lane.
- **Part 2, Findings.** One block per finding. Fields: stable ID (e.g. BEEF-07), classification, county text, state text, archaeology note, disposition, mechanics tag where the wording itself is the gap.
- **Classification vocabulary:** DIVERGED / CONFLICT / SILENT / LOCAL-ONLY / ALIGNED.
- **Disposition lanes (tee-up only, board decides):** ADOPT-STATE / KEEP-LOCAL / DISCUSS.
- **Triage index** at top: classification counts per department, so reading time goes where the gaps are.

## Deliverable 2: rule-mechanics.md

CSF as a system, standalone analysis: authority map (who interprets, who adjudicates, appeal chain), language audit (shall/must vs. may/should), escape-hatch inventory (discretion clauses, hardship carve-outs, reserved-rights language), hard-and-fast list (rules with no exception path), and drafting lessons for the Custer rewrite.

## Deliverable 3: volatility-inventory.md

Every annually-volatile line in the county book (dates, times, deadlines, fees, names, locations) cataloged with its location in the book. Seeds the future addendum page: the book carries stable rules plus references, the addendum carries the changing layer in one spot. CSF already publishes on this pattern (standalone schedule document), so the board pitch is alignment, not novelty.

## Propagation gate

This mission ends at the three deliverables. The disposition fields make the divergence map the staging artifact. The county book rewrite is a separate future mission, gated on the board conversation, seeded by the map. The addendum page build lives in the rewrite mission. The schedule rework is a parked future mission (see fair/notes.md) and consumes the volatility inventory.

## Session state

Never here. Build status, locked items, and pending work live in session batons only.
