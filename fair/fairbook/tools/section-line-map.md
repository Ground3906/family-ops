# County Book Section Line Map + Assembly Tooling

Supports regenerating the assembled walkthrough book (Fairbook-Complete.docx) in any session. Containers reset: the extracted sources die with each session and must be re-pulled before the generator runs.

## Source re-extraction

County book source of record: `fair/rulebooks/archive/` (raw .docx/.pdf). Session recipe:

1. curl the raw GitHub URL of the county book archive file to /home/claude
2. .docx → `pip install python-docx --break-system-packages -q`, iterate doc.paragraphs for body text (tables iterate separately via doc.tables → rows → cells)
3. Write numbered extract: one line per paragraph, `N|text` format → `/home/claude/county-book.txt` (913 lines as of the 2026 source)
4. CSF handbook: same curl + pdftotext -layout → `/home/claude/csf-handbook.txt`

## Section map (2026 county extract, file line numbers)

| Range | Content | Status 8/10 |
|---|---|---|
| 1–54 | Fair schedule | unworked (Addendum §1 target — audit Item 1) |
| 55–123 | Code of Conduct + Protest/Appeals | WORKED (replaced by draft.md General Rules) |
| 124–160 | Fair Board / Commissioners / Extension / FFA / vet / superintendents roster | unworked (Addendum §2 target — audit Item 5) |
| 161–166 | Fairgrounds cleanup | unworked |
| 167–190 | Shooting Sports | unworked |
| 191–231 | FCS & General Projects | unworked |
| 232–386 | Market Eligible Livestock & Poultry general rules + Beef/Swine/Sheep/Goat departments | unworked — FIRST department pass |
| 387–457 | Horse | unworked |
| 458–650 | Non-Market & Small Animal (Rabbit, Dog, Cat, Llama, breeding/dairy) | unworked |
| 651–674 | Companion Animal Master Showmanship | unworked |
| 675–715 | Showmanship & Master Showmanship | unworked |
| 716–749 | Livestock Sale + WMA | WORKED (replaced) |
| 750–913 | Open Division + twelve indoor divisions | unworked |

## Extraction commands (generator inputs)

```bash
cd <workdir> && mkdir -p uw
sed -n '1,54p'    county-book.txt | sed 's/^[0-9]*|//' > uw/A-schedule.txt
sed -n '124,166p' county-book.txt | sed 's/^[0-9]*|//' > uw/B-roster.txt
sed -n '167,190p' county-book.txt | sed 's/^[0-9]*|//' > uw/C-shooting.txt
sed -n '191,231p' county-book.txt | sed 's/^[0-9]*|//' > uw/D-fcs.txt
sed -n '232,386p' county-book.txt | sed 's/^[0-9]*|//' > uw/E-market.txt
sed -n '387,457p' county-book.txt | sed 's/^[0-9]*|//' > uw/F-horse.txt
sed -n '458,650p' county-book.txt | sed 's/^[0-9]*|//' > uw/G-nonmarket.txt
sed -n '651,674p' county-book.txt | sed 's/^[0-9]*|//' > uw/H-camaster.txt
sed -n '675,715p' county-book.txt | sed 's/^[0-9]*|//' > uw/I-showmanship.txt
sed -n '750,913p' county-book.txt | sed 's/^[0-9]*|//' > uw/J-open.txt
```

## Regeneration

```bash
npm ls docx || npm i docx   # docx package present in Anthropic containers
node fairbook-generator.js   # emits Fairbook-Complete.docx (expects uw/ beside it)
# render check: soffice headless convert to pdf, pdftoppm spot pages
```

The generator (`fairbook-generator.js`, this directory) hardcodes the WORKED sections at their 8/10 state — post-audit items will change that text; regenerate the hardcoded blocks from `draft.md` + delta-log after each pass locks. Known 8/10 limitations already under audit: schedule/roster still print (Items 1, 5), department volatile facts ride along (Item 9), sale-section ordering (Item 14), WMA citation (Item 15), book order (Item 16).
