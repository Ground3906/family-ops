# Fairbook Charter — Custer County Fair Book Rewrite

Standing subsystem. Product lane: the new county fair book and its annual update system. Built by the rewrite mission; outlives it. Governance analysis (the delta framework, what the rules say) lives in `fair/rulebooks/`. This tree carries the book itself.

## Mission

Produce a revised Custer County Fair book aligned to the Colorado State Fair rule stack, plus the delta documentation that lets Matt lead a working-group walkthrough of every change. Sequence is draft-first: the stripped-down aligned draft and its delta log are the vehicle for the board conversation, not gated on it. Custer flavor returns through the working group, sponsored in one item at a time.

## Political frame

- The book is a communication document as much as a legal one. Primary walkthrough audience: parents, exhibitors, team members. The lead-in adoption sentence makes the alignment argument on every page — "we follow the standard, we are not making things up." Repetition is the feature.
- Nothing is silently dropped. Every local mechanism pulled out of rule text is preserved as a FLAVOR-CANDIDATE with its home paragraph identified. The old guard sponsors flavor back in; they never defend against deletions.
- Model for the board pitch: county adoption of building and fire codes — model code by reference, local amendments printed as exceptions. Alignment, not novelty.

## Paragraph template (load-bearing)

Every adopted rule paragraph carries two layers:

1. Lead-in adoption sentence: "Custer County acknowledges and adopts CSF Rule X.X:" followed by the rule text, verbatim CSF.
2. **Custer Exceptions** block at the bottom of the paragraph: county additions, subtractions, clarifications. No exceptions = no block printed. Local flavor lives ONLY in exception blocks, never woven into rule text.

Verbatim rules:

- Entity/scale swaps are mandatory on adoption, not optional: CSF staff titles, CSU Extension nomination machinery, "the Fair" meaning Pueblo — all swap to Custer equivalents. Every swap logged in the delta entry.
- Numbers are never verbatim by default. Fees, weights, windows, deadlines are each a decision in the pass, not a copy.
- REWORDED only where CSF's own wording genuinely fails; logged with reason.
- The draft is a Matt-authored public document: the em-dash ban applies to `draft.md` and the addendum (see `fair/charter.md` content rules).

## Annual update cycle (the point of the structure)

When CSF publishes a new year: diff the verbatim layer against the new state text, re-adopt by the same references, exceptions carry forward untouched unless their parent rule moved. Volatile county data updates in the addendum only. One spot to update, never comb the book.

## Files

```
fair/fairbook/
  charter.md        (this file)
  draft.md          (the clean book — reads exactly as it prints)   [lands via execution passes, not yet committed]
  delta-log.md      (every change; the walkthrough document)        [lands via execution passes, not yet committed]
  addendum-2026.md  (volatile layer: dates, times, fees, names, locations) [lands via execution passes, not yet committed]
```

## Delta entry schema (delta-log.md)

Per change: stable ID · exact old Custer text · exact new text · CSF cite · one-line reason · status flag ADOPTED / FLAVOR-CANDIDATE / DISCUSS-AT-WALKTHROUGH · cross-reference to the divergence-map finding ID where one exists. Filtering to DISCUSS-AT-WALKTHROUGH produces the working-group docket.

## Staging

- `draft.md` ships stripped: exception blocks empty, all local flavor held as FLAVOR-CANDIDATE entries in the delta log.
- Walkthrough copy is a generated conversion pass, not committed structure: each FLAVOR-CANDIDATE prints grayed directly beneath its home paragraph so the group sees exactly where each would land when sponsored in.

## Addendum

Built during the passes with `fair/rulebooks/volatility-inventory.md` in hand: volatile lines replaced in `draft.md` with pointers ("see Fair Schedule Addendum"), the data lands in `addendum-2026.md`. Future years add `addendum-YYYY.md`; the book itself stays untouched.

## Execution pattern

- Sonnet execution chats run section passes in book order, general rules first — department paragraphs lean on that layer for definitions, eligibility, and the disciplinary ladder.
- Each pass locks dispositions paragraph by paragraph; each locked section commits its draft text and delta entries together. Repo-first, no local staging.
- Sources: county extract and CSF extracts in `fair/rulebooks/extracts/`; `divergence-map.md` pre-answers the load-bearing calls.
- Cowork: optional final .docx assembly only, after all content locks.

## Session state

Never here. Build status, current pass position, and pending work live in session batons only.
