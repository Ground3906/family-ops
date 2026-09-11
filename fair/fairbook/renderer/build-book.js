const R = require('./render.js');
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle, PageBreak,
  InternalHyperlink, TabStopType, Bookmark,
} = R;

const VERSION = R.VERSION, PM = R.PAGEMAP;
const fm = fs.readFileSync('front-matter.md', 'utf8');
const bk = fs.readFileSync('draft.v14.md', 'utf8');

// ---- split the book into chapters -------------------------------------
const lines = bk.split('\n');
const chapters = [];           // {short, title, anchor, blocks}
let pre = [];                  // How to Use This Book, before CC 1
let cur = null;
for (const l of lines) {
  const m = /^## (CC (\d+)) — (.+)$/.exec(l);
  if (m) {
    cur = { short: m[1], num: +m[2], title: m[3], anchor: 'ch' + m[2], raw: [] };
    chapters.push(cur);
    continue;
  }
  if (/^## How to Use This Book/.test(l)) { cur = { intro: true, raw: [] }; pre = cur.raw; continue; }
  if (cur) cur.raw.push(l); else if (!/^Custer County Fair Book|^This file is the book|^---\s*$|^\s*$/.test(l)) pre.push(l);
}
const chaps = chapters.filter(c => !c.intro);

// ---- collect TOC entries ----------------------------------------------
const toc = [];
for (const c of chaps) {
  toc.push({ depth: 0, label: `${c.short} — ${c.title}`, anchor: c.anchor });
  for (const l of c.raw) {
    const m = /^### (CC [\d.]+) — (.+)$/.exec(l);
    if (m) toc.push({ depth: 1, label: `${m[1]} — ${m[2]}`, anchor: 'sc' + m[1].replace(/[^0-9]/g, '_') });
    const n = /^### ([A-Z].+)$/.exec(l);
    if (n && !m) toc.push({ depth: 1, label: n[1], anchor: 'sx' + R.slug(n[1]) });
  }
}

// ---- front section: cover, about, contents ----------------------------
const front = [];
front.push(new Paragraph({ spacing: { before: 2600, after: 200 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'CUSTER COUNTY', bold: true, font: R.FONT, size: 52 })] }));
front.push(new Paragraph({ spacing: { after: 400 }, alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'FAIR BOOK', bold: true, font: R.FONT, size: 52 })] }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
  border: { top: { style: BorderStyle.SINGLE, size: 6, space: 10, color: '000000' } },
  children: [new TextRun({ text: ' ', font: R.FONT, size: 20 })] }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
  children: [new TextRun({ text: `Version ${VERSION}`, font: R.FONT, size: 28 })] }));
front.push(new Paragraph({ alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: 'Westcliffe, Colorado', font: R.FONT, size: 22, color: '444444' })] }));
front.push(new Paragraph({ children: [new PageBreak()] }));

// About pages from front-matter.md
for (const b of R.parseBlocks(fm)) {
  if (b.t === 'h1' || b.t === 'hr') continue;
  if (b.t === 'p' && /^Mission, objectives, accessibility/.test(b.text)) continue;
  if (b.t === 'h2') front.push(R.heading(b.text, 0, 'about'));
  else if (b.t === 'h3') front.push(R.heading(b.text, 1, 'fm' + R.slug(b.text)));
  else if (b.t === 'p') front.push(R.para(b.text));
}
// Contents lives in its own two-column section
const tocKids = [];
tocKids.push(new Paragraph({
  heading: R.HeadingLevel.HEADING_1, outlineLevel: 0, spacing: { after: 200 },
  children: [new Bookmark({ id: 'toc', children: [new TextRun({ text: 'Contents', bold: true, font: R.FONT, size: 30, color: '000000' })] })],
}));
for (const e of toc) {
  tocKids.push(new Paragraph({
    spacing: { after: 20, line: 240 },
    indent: { left: e.depth * 160 },
    tabStops: [{ type: TabStopType.RIGHT, position: 4480, leader: 'dot' }],
    children: [
      new InternalHyperlink({ anchor: e.anchor, children: [
        new TextRun({ text: e.label, font: R.FONT, size: e.depth ? 18 : 19, bold: !e.depth, color: '000000' })] }),
      new TextRun({ text: '\t' + (PM[e.anchor] || ''), font: R.FONT, size: 18, color: '444444' }),
    ],
  }));
}

// ---- body sections, one per chapter -----------------------------------
function chapterChildren(c) {
  const kids = [R.heading(`${c.short} — ${c.title}`, 0, c.anchor)];
  for (const b of R.parseBlocks(c.raw.join('\n'))) {
    if (b.t === 'hr') continue;
    if (b.t === 'table') { const t = R.buildTable(b.rows); if (t) kids.push(t); continue; }
    if (b.t === 'h3') {
      const m = /^(CC [\d.]+) — (.+)$/.exec(b.text);
      kids.push(R.heading(b.text, 1, m ? 'sc' + m[1].replace(/[^0-9]/g, '_') : 'sx' + R.slug(b.text)));
      continue;
    }
    if (b.t === 'h2') { kids.push(R.heading(b.text, 1, 'sx' + R.slug(b.text))); continue; }
    const rm = /^\*\*(CC [0-9.a-z]+[^*]*)\*\*$/.exec(b.text);
    if (rm) { kids.push(R.heading(rm[1], 2, 'r' + R.slug(rm[1]))); continue; }
    kids.push(R.para(b.text));
  }
  return kids;
}

const sections = [{
  properties: { page: { size: R.PAGE, margin: R.MARGIN } },
  headers: { default: R.plainHeader() },
  footers: { default: R.footerCentered() },
  children: front,
}, {
  properties: { page: { size: R.PAGE, margin: R.MARGIN }, column: { count: 2, space: 400, equalWidth: true } },
  headers: { default: R.plainHeader() },
  footers: { default: R.footerCentered() },
  children: tocKids,
}];
// How to Use This Book rides at the front of CC 1's section
const introKids = [];
if (pre.length) {
  introKids.push(R.heading('How to Use This Book', 0, 'howto'));
  for (const b of R.parseBlocks(pre.join('\n'))) {
    if (b.t === 'hr' || b.t === 'h2') continue;
    introKids.push(R.para(b.text));
  }
  introKids.push(new Paragraph({ children: [new PageBreak()] }));
}
chaps.forEach((c, idx) => {
  sections.push({
    properties: { page: { size: R.PAGE, margin: R.MARGIN } },
    headers: { default: R.navbar(c.short, chaps) },
    footers: { default: R.footerCentered() },
    children: (idx === 0 ? introKids : []).concat(chapterChildren(c)),
  });
});

const doc = new Document({
  styles: { default: { document: { run: { font: R.FONT, size: R.BODY } } } },
  sections,
});
Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('/mnt/user-data/outputs/Custer County Fair Book v' + VERSION + '.docx', b);
  fs.writeFileSync('toc-anchors.json', JSON.stringify(toc.map(t => t.anchor)));
  console.log('book written', b.length, 'bytes |', chaps.length, 'chapters |', toc.length, 'toc entries');
});
