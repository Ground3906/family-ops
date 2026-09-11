# Fair Book renderer

Turns the markdown source into Word and PDF. Nothing in the book is ever
hand-formatted; change the markdown, run this, get matching Word and PDF.

**This directory exists because the renderer was lost twice.** It lived only in a
session scratch space, which is wiped when the session ends, so every new session
rebuilt it from a written spec and dropped features. It lives here now.

## What it produces

- Cover page carrying the version number, no draft banner
- Two-column Contents on one page, dot leaders, every entry hyperlinked to its target
- Real page numbers in the Contents, from a two-pass render
- A bookmark on every heading, which is what makes the PDF sidebar work on a phone
- Chapter navbar in the running header of every body page, current chapter in bold
  black, every other chapter a live link, plus a link back to Contents
- Cambria 10.5pt, US Letter, 1 inch margins, page number centered in the footer

## Requirements

Node with the `docx` package, Python with `pypdf`, and LibreOffice for PDF
conversion. Run from a directory holding `front-matter.md`, `draft.md` and
`addendum.md`.

## How to run

The page numbers in the Contents require two passes: render once, read where the
headings actually landed, render again with those numbers.

```
# pass 1
node build-book.js 1.5
soffice --headless --convert-to pdf "Custer County Fair Book v1.5.docx"

# build the page map from the PDF outline
python3 pagemap.py "Custer County Fair Book v1.5.pdf"

# pass 2
node build-book.js 1.5 pagemap.json
soffice --headless --convert-to pdf "Custer County Fair Book v1.5.docx"
```

Same shape for the Addendum with `build-addendum.js` and `pagemap-add.py`.

## Why the page map reads the PDF outline, not the text

An earlier version searched the page text for each heading. That fails, because
a heading like "CC 4 — The Livestock Sale" also appears inside the applies-to-you
index on an earlier page, so the Contents pointed at the index instead of the
chapter. The PDF outline contains only real headings, so it cannot be fooled.

## Checks worth running before shipping

- Re-derive the page map from the final PDF and confirm nothing shifted. Zero drift
  means the two passes converged.
- Count bookmarks against internal links in the docx and confirm no link points at
  a bookmark that does not exist.
- Read the rendered pages. Compiling is not the same as being right.

## The handouts

`build-summary.js` and `build-vet-agreement.js` build the two board handouts. They
carry their own content rather than reading markdown, and they use a simple footer
with the document name and Page X of Y instead of the chapter navbar, because a
navbar on a six page handout is noise.
