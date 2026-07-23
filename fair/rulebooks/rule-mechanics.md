# Rule Mechanics — Colorado State Fair as a System

Deliverable 2 of the Fair Rulebooks Charter (`fair/rulebooks/charter.md`). Standalone analysis of how CSF writes and adjudicates its own rules — who holds interpretive authority, what's mandatory vs. discretionary, what outs staff reserve, what's hard and fast — plus drafting lessons for the eventual Custer rewrite. This deliverable stands on its own; it doesn't compare against the county book (that's `divergence-map.md`).

Sources: `fair/rulebooks/extracts/csf-2026-general-competition-requirements.md` (cross-division administrative rules) and `fair/rulebooks/extracts/csf-2026-exhibitor-handbook.md` (689-page complete handbook, per-division rules).

## Authority map

**Statutory layer.** Colorado State Fair Authority ("the Authority") operates under Authority Rules adopted at 8 CCR 1208-1. Every entry is a binding contract that pulls in the entire Exhibitor Handbook, the Authority Rules, and a signed Exhibitor Code of Conduct simultaneously — three documents incorporated by a single signature, not independently.

**Executive layer, division by division.** "Management" is defined collectively as the General Manager, Section Managers, Department Directors, Show Superintendents, and Lead Clerks, "vested with the discretionary power to interpret rules, enforce safety and grooming standards, allocate physical resources, and adjudicate disputes." Violations are determined specifically by the General Manager, the Director of Agriculture and Competitive Exhibits, or the Program Manager of the relevant division — any of the three, acting alone, can make the initial call, "before, during, or after judging."

**Appellate layer.** A single, rigid chain regardless of division:
1. General Manager notifies the exhibitor in writing within 15 days of a violation determination.
2. Exhibitor has 15 days from receipt to appeal in writing to the Board.
3. Program Manager/Director/GM have 15 days to review the appeal and may unilaterally **rescind** the determination — if they do, that's final, "the exhibitor will have no further remedy available."
4. If no action within 15 days, the matter goes to the next regular Board meeting solely to schedule a hearing.
5. The Board appoints a 4-person ad hoc hearing panel: one Board member (presiding), one subject-matter expert, one member of the public, and one senior Authority employee who is not the GM.
6. Presiding officer submits findings and a recommendation within 15 days of the hearing.
7. The Board adopts a final determination at its next regular meeting.

**Grievance layer (third-party complaints).** Anyone may file a grievance against anyone else's alleged violation, sworn and in writing, with a **$300 bond** (refundable if the complaint is upheld). The Director rules on validity within 15 days; if valid, a three-person disinterested committee decides, and that decision is "final for purposes of appeal" — meaning it still feeds into the same 7-step appeal chain above if the grievant wants to keep pushing.

**Net shape:** one office (GM/Director/Program Manager, functionally interchangeable at the first-determination stage) holds nearly all initial authority; the Board is the only body that can truly overturn a decision, and it does so only through a slow, multi-week, multi-person process that exists specifically to be hard to trigger and harder to reverse.

## Language audit

Modal-verb counts across the General Competition Requirements document (whole-document, full-text search):

| Term | Count | What it does |
|---|---|---|
| must | 24 | Binds exhibitors to concrete obligations (complete entry, buy a wristband, sign the Code of Conduct, submit a correct W-9, meet appeal/grievance deadlines, indemnify the Authority) |
| may | 35 | Grants discretion almost exclusively to Authority actors (GM/Director/Program Manager/Board) — to disqualify, cancel, rescind, penalize, refuse entry, approve a vehicle, add an award |
| shall | 8 | A procedural duty on **officials**, not exhibitors — the Program Manager "shall" set a penalty, a hearing-panel Board member "shall serve" as presiding officer, the Director "shall notify" a grievant. The one exhibitor-facing "shall" is prohibitive: "No person shall direct abusive or threatening conduct." |
| should | 1 | Not used in an advisory sense at all — the single instance ("Should the Program Manager ... take no action ... within 15 days") is a conditional "if," not a softer obligation. There is effectively no soft-recommendation register in this document; it's binary must/shall vs. may. |

Same pattern holds in the 689-page Exhibitor Handbook: numeric/procedural rules (deadlines, weights, fees) are written as hard "shall/must" cutoffs, while enforcement, interpretation, and dispute resolution are written as "may"/"at its discretion"/"reserves the right," almost without exception. **Obligations flow down to exhibitors; discretion flows up to Authority staff.** A rewrite that wants CSF's level of enforceability needs that same asymmetry applied consistently, not just borrowed vocabulary.

## Escape-hatch inventory

Discretion and hardship clauses that give staff an out with no exhibitor-side counterweight:

- **Blanket interpretive authority**, stated twice in different sections: the Authority reserves the "final and absolute right to interpret" every requirement.
- **Open-ended penalty catch-all**: "The Program Manager, Director, or the General Manager may impose any other appropriate penalty" — no boundary given beyond the enumerated list it follows.
- **Undefined-standard money deductions**: when a barred animal has already sold, staff may deduct "costs attributable to the exhibitor" from the proceeds with no stated formula.
- **Unreviewable rescission**: officials "may rescind" a violation determination during the appeal window — and if they do, there's no further remedy for anyone, including a grievant who wanted the original determination to stand.
- **Subjective hardship threshold**: motorized-vehicle pre-approval turns entirely on the General Manager's judgment of "hardship," undefined anywhere in the document.
- **Self-policing conflicts of interest**: Board members, staff, and volunteers "may need to recuse" themselves from judging — a self-assessed standard, reported after the fact to a Program Manager.
- **Judge's-discretion phrasing** recurs division by division outside the general rules too (e.g., Floriculture: plant condition judged "at the Judge's discretion"; artwork condition: "Colorado State Fair Management will decide").

## Hard-and-fast list

Rules with no stated exception path anywhere in the reviewed documents, clustered by theme:

**Money:** entry fees non-refundable, no exceptions listed; no exhibitor may show until a bounced check plus its $35 fee is repaid; premium checks void if not cashed within six months, no replacements issued after December 31; no monies paid without a correct W-9 at $600+ in earnings.

**Absolute conduct bans:** "no volunteer within a State Fair division may act as a judge in any competition within such division"; non-motorized vehicles (bicycles, skateboards, scooters) "are not allowed at any time" — notably contrasted with motorized vehicles, which *do* have a General Manager waiver path, showing the drafters deliberately distinguish "absolute" bans from "absolute-unless-approved" ones; unconditional prohibition on abusive or threatening conduct toward judges and staff.

**Numeric thresholds with no give:** the >5% re-weigh deviation that disqualifies a top-5 finisher; species weight windows (beef 1,050+ lbs, swine 235–300, sheep 110–165, goat 55–115); Scrapie ID mandatory on all sexually intact sheep 18 months or older; a 4-head-per-species entry cap; quilts must be completed within the last 3 years and never previously entered at CSF; afghans must be at least 45"×45"; canning must post-date a specific cutoff, no steam-pressure canners, no paraffin; recycled-fabric garments need at least 50% recycled material; Fine Arts photography allows "20% or less" color correction and no more.

**Procedural absolutes:** "at no time will any exhibition, judging event, or other ongoing event be delayed, stopped, or interrupted" by a pending allegation — the show goes on regardless of an active investigation.

## Drafting lessons for the Custer rewrite

1. **Separate the administrative layer from the technical layer, on purpose.** CSF splits a short cross-division document (entry mechanics, fees, conduct, appeals) from a long per-division document (weights, health, judging). Custer's book currently repeats identical boilerplate — the coaching/cueing warning, for instance — inside almost every species section verbatim. Pulling shared rules into one general section once, referenced by each department, removes the risk of one copy drifting from the others during a future edit.

2. **Watch for the same copy-paste failure mode CSF itself has.** Two live examples turned up in CSF's own current handbook: the Market Goats section contains a sentence about "lamb"-holding pens, evidently pasted from the Lambs section and never corrected; the Horse Show section states the late-entry fee as both "$50 per exhibitor" and "$75.00" in two different places. A 689-page document with professional staff still has this problem — a rewrite should budget an explicit cross-reference proofing pass after any edit touches boilerplate language, not assume a one-time careful draft will stay correct.

3. **Decide the modal-verb convention on purpose, then hold it.** If Custer wants CSF's level of enforceability, reserve "shall/must" for genuine binding obligations and "may" for genuine discretion, consistently. Custer's book currently uses numbered imperative lists without a fully consistent modal pattern — worth a dedicated read-through during the rewrite specifically for this, separate from any content changes.

4. **Treat "adopt by reference" as a live link, not a citation.** All four Colorado 4-H URLs printed by name in the current county book are dead — the source site was rebuilt on a new CMS and every one of them now redirects to a generic landing page instead of erroring outright, which is exactly why nobody caught it. If the rewrite leans further into CSF's own "adopt by reference, print only the exceptions" end-state, it should link to stable hub/landing pages where the issuing organization offers one, not deep individual PDF paths, and the addendum-refresh cadence (see `volatility-inventory.md`) should include a live-link check as a standing step, not a one-time fix.

5. **The 8-hour vs. 15-day appeal-window gap (see `divergence-map.md`, ADMIN-01) is a genuine design choice, not just a number to harmonize.** CSF's slow, multi-stage appeal chain exists because the Authority is a large, semi-governmental body accountable to a wide public; Custer's board is small, known, and the fair is a third the length. A faster local process is defensible on its own terms — but "defensible" is different from "already decided," and this is exactly the kind of load-bearing mechanics question the charter intends the board conversation to resolve, not something to quietly shorten or lengthen without discussion.

6. **Specificity is a trade-off, not a free win.** CSF's numeric hard-and-fast rules (the enumerated 13-item ethics list, the 5% re-weigh threshold) reduce ambiguity and protest risk, but every one of them was also a decision to give up flexibility. Custer's shorter, more discretion-friendly lists aren't automatically worse — they're a different, defensible point on the same trade-off. The rewrite's job is to make each of those choices deliberately, department by department, rather than import CSF's specificity wholesale because it's more detailed.
