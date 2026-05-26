# Chow Hall — Kalea Capture Session Guide

**Owner:** Chow Hall (🍴)
**Last updated:** 2026-05-26
**Purpose:** How to run the session that brings Kalea's actual recipes into the library — in her words, not ours.

---

## What this session is

Kalea has the recipes in her head, in her cookbooks, and on her phone. The capture session turns all of that into clean recipe records. Chow Hall does the structuring work; Kalea answers questions. She is never asked to write in a format or fill in a schema.

---

## Scheduling

- **Morning or early-afternoon only.** Decision window doctrine — no Kalea-input session after 20:00.
- **Not 2026-05-27** — her birthday. Schedule after.
- **Estimate:** 60–90 minutes for an initial pass of 10–15 recipes. Split across sessions if needed.

---

## Four intake channels

### 1. Chat dictation
Kalea talks. Chow Hall listens and structures.

Opening prompt:
> "What's a recipe you make that the family always asks for again? Tell me how you make it — your way."

Follow-up elicitation (one at a time):
- "How much [ingredient] do you use? Ballpark is fine."
- "What do you cook it in — the LG, the wall oven, or the grill?"
- "Is this one you'd want locked forever, or fair game for tweaking over time?"
- "About how long does it take, start to finish?"

Output: one `recipes/<slug>.json` per recipe dictated.

---

### 2. Photo upload
Kalea photographs a recipe card, cookbook page, or handwritten note.

**Photo is raw material only — never stored as the display version of the recipe.** Chow Hall reads it and converts to a clean record, then confirms the ambiguous bits with Kalea.

Confirmation prompt:
> "I've got it. Quick confirms — [ingredient amount question], [equipment question], [heirloom?]. Does that look right?"

Output: one `recipes/<slug>.json`. Photo discarded after transcription.

---

### 3. Batch scan
A large set of photos at once — a full cookbook or recipe box.

Chow Hall converts the batch and queues a brief confirmation pass, not a full interview per recipe.

Confirmation prompt:
> "Converted 12 recipes from the batch. Here's what I have — flag anything off. We can go deeper on any of them."

Output: multiple `recipes/<slug>.json` files queued for confirmation.

---

### 4. Research
Kalea or Matt finds a recipe online and wants to try it. Goes into staging, not the active library.

Prompt:
> "Filed it as a candidate. We'll try it and decide keep or drop after the meal. Snooze it until [date], or put it on the short list now?"

Output: one `recipes-staging/<slug>.json`, status `"candidate"`.

---

## What good elicitation looks like

Chow Hall's job is to ask smart questions, not put words in Kalea's mouth. The recipe should sound like her. Always capture:

- **Fuzzy amounts** — "a big handful" needs a cup or weight estimate before filing
- **Which equipment she actually uses** — ask specifically (LG lower, LG upper, wall oven, grill)
- **Heirloom intention** — ask once, respect the answer, never re-prompt
- **Her thaw lead** — if she already knows it, capture as `thaw_override`; don't run the formula over her judgment
- **Her altitude tweaks** — if she's already adjusted a recipe for 9,000 ft, capture her version; don't layer the doctrine on top of it

---

## F1 gaps to resolve at next inventory pass

Ingredient names in recipe files must match `freezer.json` and `pantry.md` exactly.
Known gaps flagged during seed build:

| Ingredient | Missing from |
|---|---|
| Eggs (farm fresh) | freezer.json and pantry.md |
| Flour tortillas | pantry.md |
| Active dry yeast | pantry.md |

Add these at the next pantry inventory pass before the meal planner (Wave 6.3) goes live.

---

*Update this guide after each capture session with lessons learned.*
