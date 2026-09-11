/*
 * Custer County Fair Book renderer.
 * Reads front-matter.md, draft.md and addendum.md and writes Word documents
 * with a clickable table of contents, PDF sidebar bookmarks, a chapter navbar
 * in the running header, and real page numbers from a two-pass render.
 *
 * Usage:  node render.js <version> [pagemap.json]
 * Pass 1: node render.js 1.5                 -> renders with placeholder page numbers
 * Pass 2: node render.js 1.5 pagemap.json    -> renders with real page numbers
 */
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, PageBreak, AlignmentType,
  BorderStyle, Header, Footer, PageNumber, TabStopType, InternalHyperlink,
  Bookmark, Table, TableRow, TableCell, WidthType, ShadingType, LevelFormat,
} = require('docx');
const fs = require('fs');

const FONT = 'Cambria';
const BODY = 21;              // 10.5pt
const PAGE = { width: 12240, height: 15840 };
const MARGIN = { top: 1440, right: 1440, bottom: 1080, left: 1440 };
const CONTENT_W = 9360;

const VERSION = process.argv[2] || '1.5';
const PAGEMAP = process.argv[3] && fs.existsSync(process.argv[3])
  ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : {};

// ---------------------------------------------------------------- helpers
let bmId = 0;
const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '').slice(0, 38);

function runs(text, size = BODY) {
  // **bold** segments
  const out = [];
  const re = /\*\*(.+?)\*\*/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, size }));
    out.push(new TextRun({ text: m[1], bold: true, font: FONT, size }));
    last = m.index + m[0].length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, size }));
  return out.length ? out : [new TextRun({ text, font: FONT, size })];
}

const para = (text, opts = {}) => new Paragraph({
  children: runs(text), spacing: { after: 130, line: 264 }, ...opts,
});

function heading(text, level, anchor) {
  const sizes = [30, 25, 22];
  const hl = [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3][level];
  return new Paragraph({
    heading: hl,
    outlineLevel: level,
    keepNext: true,
    spacing: { before: level === 0 ? 0 : (level === 1 ? 320 : 260), after: level === 2 ? 110 : 160 },
    children: [new Bookmark({
      id: anchor,
      children: [new TextRun({ text, bold: true, font: FONT, size: sizes[level], color: '000000' })],
    })],
  });
}

// ---------------------------------------------------------------- markdown block parser
function parseBlocks(md) {
  const lines = md.split('\n');
  const blocks = [];
  let i = 0;
  while (i < lines.length) {
    const l = lines[i];
    if (/^\|/.test(l)) {                                   // table
      const rows = [];
      while (i < lines.length && /^\|/.test(lines[i])) { rows.push(lines[i]); i++; }
      blocks.push({ t: 'table', rows });
      continue;
    }
    if (/^---\s*$/.test(l)) { blocks.push({ t: 'hr' }); i++; continue; }
    if (/^### /.test(l))    { blocks.push({ t: 'h3', text: l.slice(4).trim() }); i++; continue; }
    if (/^## /.test(l))     { blocks.push({ t: 'h2', text: l.slice(3).trim() }); i++; continue; }
    if (/^# /.test(l))      { blocks.push({ t: 'h1', text: l.slice(2).trim() }); i++; continue; }
    if (/^\s*$/.test(l))    { i++; continue; }
    blocks.push({ t: 'p', text: l.trim() }); i++;
  }
  return blocks;
}

function buildTable(rows) {
  const cells = rows
    .filter(r => !/^\|[\s:|-]+\|?\s*$/.test(r))
    .map(r => r.replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
  if (!cells.length) return null;
  const n = Math.max(...cells.map(c => c.length));
  const w = Math.floor(CONTENT_W / n);
  const widths = Array(n).fill(w);
  widths[n - 1] = CONTENT_W - w * (n - 1);
  const mk = (txt, idx, head) => new TableCell({
    width: { size: widths[idx], type: WidthType.DXA },
    margins: { top: 70, bottom: 70, left: 100, right: 100 },
    shading: head ? { type: ShadingType.CLEAR, fill: 'EDEDED' } : undefined,
    children: [new Paragraph({ children: runs(txt || '', 19), spacing: { after: 0 } })],
  });
  return new Table({
    columnWidths: widths,
    width: { size: CONTENT_W, type: WidthType.DXA },
    rows: cells.map((row, ri) => new TableRow({
      tableHeader: ri === 0,
      children: Array.from({ length: n }, (_, ci) => mk(row[ci], ci, ri === 0)),
    })),
  });
}

// ---------------------------------------------------------------- navbar header
function navbar(currentChapter, chapters) {
  const kids = [];
  const push = (label, anchor, active) => {
    if (active) {
      kids.push(new TextRun({ text: label, bold: true, font: FONT, size: 17, color: '000000' }));
    } else {
      kids.push(new InternalHyperlink({
        anchor,
        children: [new TextRun({ text: label, font: FONT, size: 17, color: '444444' })],
      }));
    }
  };
  push('Contents', 'toc', currentChapter === 'toc');
  for (const ch of chapters) {
    kids.push(new TextRun({ text: '  ·  ', font: FONT, size: 17, color: '999999' }));
    push(ch.short, ch.anchor, ch.short === currentChapter);
  }
  return new Header({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 120 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, space: 6, color: 'BBBBBB' } },
      children: kids,
    })],
  });
}

const footerCentered = () => new Footer({
  children: [new Paragraph({
    alignment: AlignmentType.CENTER,
    children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18, color: '444444' })],
  })],
});

const plainHeader = () => new Header({ children: [new Paragraph({ children: [] })] });

module.exports = {
  FONT, BODY, PAGE, MARGIN, CONTENT_W, VERSION, PAGEMAP,
  runs, para, heading, parseBlocks, buildTable, navbar, footerCentered, plainHeader, slug,
  Document, Packer, Paragraph, TextRun, HeadingLevel, PageBreak, AlignmentType, BorderStyle,
  Header, Footer, PageNumber, TabStopType, InternalHyperlink, Bookmark, WidthType,
};
