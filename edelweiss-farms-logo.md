# Edelweiss Farms, LLC — Logo Reference

The botanical badge mark for Edelweiss Farms, LLC. Designed collaboratively in May 2026. This file is the canonical reference for the design and the source for future revisions.

## How to use this file

Upload this `.md` to project knowledge alongside the charter and project instructions. Any future Claude conversation can read it and:

- Show the rendered logo
- Make edits when asked ("make the moss darker", "swap the flower for a different shape", "add a snow cap")
- Generate variations for specific uses (single-color stamp, embroidery-safe simplification, horizontal wordmark, etc.)

The companion `.svg` file is the raw asset — paste it into Figma, Illustrator, Inkscape, or any browser and it renders directly.

## Design rationale

A circular badge in the creamery-stamp / feed-sack tradition. Reads as a mark that's been around a while, even if the LLC is new.

| Element | Role |
|---|---|
| Bold outer ring | Embossed feel when stamped on light surfaces. Reads cleanly at small sizes. |
| Top arc text | The brand name. Primary visual weight. |
| Bottom arc text | Place of origin. Moss green for a secondary tone and an alpine cue. Reads upright (left-to-right) so the viewer doesn't have to tilt the badge. |
| Five-point side stars | Faith reference. Anchors the seal between the two text arcs. |
| Medallion ring | Frames the central composition. |
| Two mountain ranges | Atmospheric depth behind the flower. Back range pale + outlined; front range darker + solid. Sage tones tie to the moss bottom text. |
| Edelweiss flower | Two whorls of leaf-shaped bracts (8 outer + 8 inner) radiating from a gold stamen cluster. Inner whorl offset 22.5° from the outer and scaled to 62%, peeking between the larger bracts. Based on the user-provided reference photo of a real edelweiss. |

## Color palette

| Role | Hex | Notes |
|---|---|---|
| Paper (cream) | `#f3ead5` | Bract fill, medallion fill |
| Paper-deep | `#ebdfbf` | Badge field (slightly darker than the page it sits on, gives the badge presence on a cream background) |
| Ink | `#1a1612` | Outer ring, top text, petal outlines, stars |
| Moss | `#4a6b3a` | Bottom text |
| Moss-deep | `#2f4427` | Back range outline (at 0.75 stroke-opacity) |
| Back range fill | `#b8c4a8` | Pale sage, 55% fill-opacity |
| Front range fill | `#5e7860` | Deeper sage, 82% fill-opacity |
| Stamen gold | `#c08416` | Flower center cluster |
| Rust (reserved) | `#b8492a` | Available for accent variations / single-color rust stamp |
| Rust-deep (reserved) | `#8c3418` | Available for accent variations |

## Typography

- Family: **Georgia, serif**
- Weight: **600** for both wordmarks
- Letter-spacing: **2.5**
- Top wordmark (EDELWEISS FARMS, LLC): **17px** at native size
- Bottom wordmark (WESTCLIFFE · COLORADO): **15px** at native size

## Geometry

Drawn in a 320×320 viewBox starting at (180, 20). Badge centered at (340, 180).

| Element | Value |
|---|---|
| Outer ring radius | 160 |
| Outer ring stroke | 4 (ink) |
| Inner accent radius | 152 |
| Inner accent stroke | 0.6 (ink) |
| Top text path radius | 136 |
| Bottom text path radius | 148 |
| Side star centers | (218, 180) and (462, 180) — radius 122 from center |
| Side star outer radius | 9 |
| Side star inner radius | ~3.44 |
| Medallion radius | 90 |
| Medallion stroke | 1.5 (ink) |
| Medallion inner accent | 84 |
| Mountain clip radius | 83 |
| Outer bract length | 60 |
| Outer bract max width | ~16 (at midpoint) |
| Number of outer bracts | 8 (rotated 45° each, starting at 0°) |
| Inner bract scale | 0.62 (effective length ~37, max width ~10) |
| Inner bract stroke | 1.0 (scaled stroke — visually matches outer at 0.8 × 1/0.62) |
| Number of inner bracts | 8 (rotated 45° each, starting at 22.5° offset) |

## Notes for future revisions

- **The "LLC" stays.** Part of the wordmark for legal coverage.
- **Don't drop below 8 outer bracts.** Edelweiss has 5–9 in nature; we picked 8 to match the user-provided reference photo. Going to 6 makes it look like a generic flower.
- **Inner whorl is paired with outer.** If you ever change the outer bract count, change the inner to match and recompute the rotation offset (offset = 360° / count / 2).
- **Don't swap the five-point stars for six-point stars** without thinking about it. Five points is a deliberate faith reference (Bayer family values). Six-point reads as sheriff/Star-of-David and would change the meaning.
- **At small sizes (favicon, embroidery, ≤32px)**, the mountains and text will dissolve. That's correct degradation. The flower-and-ring silhouette carries identity at any size. The inner whorl may also dissolve at very small sizes — that's fine, the outer 8 still read as an edelweiss.
- **For single-color variations** (e.g., wax stamp, brand iron, single-color print), strip the mountains and gold stamen, render the whole mark in one ink color (rust `#b8492a` or ink `#1a1612`). Consider dropping the inner whorl for single-color stamps if the bracts blur together.
- **For horizontal wordmark variations** (e.g., email signature, narrow header), pull the flower out as a small mark and place "Edelweiss Farms, LLC" next to it in serif caps.

## Version history

- **v1** — Three initial concepts explored: botanical badge, monogram + mountain, hand-carved block
- **v2** — Botanical badge selected. Added ", LLC". Thickened outer rim for embossed feel.
- **v3** — Switched ellipse petals to leaf-shaped paths (8 bracts). Added five-point stars. Moss green bottom text. Flipped bottom text to upright reading.
- **v4** — Bumped typography for stronger brand presence (top 15→17px, bottom 13→15px, weight 500→600).
- **v5** — Added two sage mountain ranges behind the flower, clipped to medallion.
- **v6** — Refined atmospheric depth: back range paler + outlined, front range darker + more solid.
- **v7** — Added inner whorl of 8 smaller bracts at 62% scale, offset 22.5° from the outer whorl. Inner bracts drawn first (behind the outer set) so their tips peek out between the larger ones. **(Current locked version.)**

---

## SVG source

```svg
<svg viewBox="180 20 320 320" xmlns="http://www.w3.org/2000/svg" role="img">
<title>Edelweiss Farms, LLC — botanical badge</title>
<desc>Circular farm seal with edelweiss flower (double whorl, 16 bracts), sage mountain ranges, and faith stars. Designed for Edelweiss Farms, LLC of Westcliffe, Colorado.</desc>
<defs>
<path id="topArc" d="M 204,180 A 136,136 0 0,1 476,180"/>
<path id="botArc" d="M 192,180 A 148,148 0 0,0 488,180"/>
<clipPath id="medClip">
<circle cx="340" cy="180" r="83"/>
</clipPath>
</defs>

<circle cx="340" cy="180" r="160" fill="#ebdfbf" stroke="#1a1612" stroke-width="4"/>
<circle cx="340" cy="180" r="152" fill="none" stroke="#1a1612" stroke-width="0.6"/>

<text font-family="Georgia, serif" font-size="17" font-weight="600" fill="#1a1612" letter-spacing="2.5">
<textPath href="#topArc" startOffset="50%" text-anchor="middle">EDELWEISS FARMS, LLC</textPath>
</text>
<text font-family="Georgia, serif" font-size="15" font-weight="600" fill="#4a6b3a" letter-spacing="2.5">
<textPath href="#botArc" startOffset="50%" text-anchor="middle">WESTCLIFFE · COLORADO</textPath>
</text>

<polygon points="218,171 220.06,177.25 226.61,177.25 221.27,181.11 223.33,187.36 218,183.5 212.67,187.36 214.73,181.11 209.39,177.25 215.94,177.25" fill="#1a1612"/>
<polygon points="462,171 464.06,177.25 470.61,177.25 465.27,181.11 467.33,187.36 462,183.5 456.67,187.36 458.73,181.11 453.39,177.25 459.94,177.25" fill="#1a1612"/>

<circle cx="340" cy="180" r="90" fill="#f3ead5" stroke="#1a1612" stroke-width="1.5"/>

<g clip-path="url(#medClip)">
<polygon transform="translate(340, 180)" points="-83,83 -83,10 -58,-22 -35,8 -12,-42 8,-2 32,-28 52,-8 75,-18 83,4 83,83" fill="#b8c4a8" fill-opacity="0.55" stroke="#2f4427" stroke-width="0.5" stroke-opacity="0.75"/>
<polygon transform="translate(340, 180)" points="-83,83 -83,30 -65,15 -45,-5 -22,18 5,-15 28,5 50,-12 70,2 83,-5 83,83" fill="#5e7860" fill-opacity="0.82"/>
</g>

<circle cx="340" cy="180" r="84" fill="none" stroke="#1a1612" stroke-width="0.4"/>

<g transform="translate(340, 180)">
<g transform="rotate(22.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(67.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(112.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(157.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(202.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(247.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(292.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>
<g transform="rotate(337.5) scale(0.62)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="1.0"/></g>

<g transform="rotate(0)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(45)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(90)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(135)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(180)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(225)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(270)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>
<g transform="rotate(315)"><path d="M 0,0 C -4,-12 -10,-25 -6,-45 C -3,-52 -1,-58 0,-60 C 1,-58 3,-52 6,-45 C 10,-25 4,-12 0,0 Z" fill="#f3ead5" stroke="#1a1612" stroke-width="0.8"/></g>

<circle cx="0" cy="0" r="5" fill="#c08416"/>
<circle cx="-7" cy="-4" r="4" fill="#c08416"/>
<circle cx="7" cy="-4" r="4" fill="#c08416"/>
<circle cx="-4" cy="6" r="3.5" fill="#c08416"/>
<circle cx="4" cy="6" r="3.5" fill="#c08416"/>
<circle cx="0" cy="-9" r="3" fill="#c08416"/>
<circle cx="-3" cy="-1" r="2" fill="#c08416"/>
<circle cx="3" cy="-1" r="2" fill="#c08416"/>
</g>
</svg>
```
