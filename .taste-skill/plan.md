# Euclidean Capital — build plan

**The source of truth is the client's own Figma file**, "EUCLIDEAN CAPITAL MID
FIDELITY DESIGN" (file key `aSKXW1WqojPf5iP5VYevSA`, six desktop frames), read
through a headless Chrome bench (`.taste-skill/figma-shot.mjs`) and matched
frame by frame. The Homepage Research Paper remains the source of the copy; the
Figma file is the source of the layout, the imagery and the text structure.

Kind: **service** (site-kind other — a boutique asset manager selling
discretionary investment management to institutional allocators).
Page type: `service`. Site kind: `other`.

## The six frames, and the six pages

| Figma frame | Page | What it holds |
|---|---|---|
| Desktop - 1 | `index.html` | the hero (the firm's network photograph, the statement, two calls to action), The Symbiotic Fiduciary Framework (four bordered cards), Our Strategies (two bordered cards), the earth band with Euclidean Perspectives, three briefing cards, Institutional Track Record (four lineage cells), the footer |
| Desktop - 2 | `about.html` | About Euclidean Capital beside the firm's dictionary card, Our Analytical Convergence over the leather monogram, Our Team (three portraits) |
| Desktop - 3 | `insights.html` | Institutional Research & Market Intelligence, the featured briefing, six Insights cards |
| Desktop - 4 | `research.html` | one research report in full: the headline, the sections, the takeaways, the sensitivity table, the research desk, the statutory notice |
| Desktop - 5 | `contact.html` | Initiate an Investment Dialogue beside the business card and the inquiry form, Frequently Asked Questions |
| Desktop - 6 | `approach.html` | Structured Thinking Across Multi-Horizon Mandates, the firm's film, Dual Arenas of Institutional Deployment |

## Palette (pixel-sampled from the brand book's swatches and from the design)

| Token | Hex | Role |
|---|---|---|
| `--p-bg` | `#12182B` | Dark Navy — the header, the ground, the footer |
| `--p-surface` | `#222C41` | Dark Gray Blue — the inquiry panel |
| `--p-ink` | `#FFFFFF` | text |
| `--p-muted` | `#AEBBCD` | secondary text |
| `--p-accent` | `#749DCB` | Muted Blue — the one accent |
| `--p-rule` | `#476B87` | Gray Azure — the hairline |

The page ground is **one gradient** that runs the whole page, sampled off the
design: navy at the top, steel blue (`#6183AB`) through the strategies, navy
again at the foot. Crimson `#BA3D47` / `#8A3D47` is excluded everywhere (the
client has confirmed it is an error in the brand book).

Type: Cormorant Garamond (display) + Jost (text), self-hosted in
`assets/fonts/`.

## Motion

- The hero entrance (`data-enter`) and the kit's dealt moments:
  **`word-highlight` on the home page's hero statement** and **the same moment on
  the About page's convergence paragraph** — both scrubbed to the scrollbar, so
  the words turn from grey to ink as they cross the middle of the screen, and
  they run back when the visitor scrolls up.
- **The client's own film** (`assets/web/hero-globe.mp4`, re-encoded from
  `Dark_globe_rotating_in_space_29a9da04_1080p.mp4`) rides full bleed in the
  home page's "Euclidean Perspectives" band, where the design draws the earth,
  and again in the band on the Investment Strategies page. Muted, looping, with
  a 44px pause control; it rests as its poster on a phone and under reduced
  motion.
- No shader ground, no WebGL, no scroll-linked parallax, **no animation
  library**: the skill's rule is that a service page carries no animation
  library at all ("the kit's moments need none"), and GSAP ScrollTrigger is
  for tech pages only. The scrollytelling is therefore delivered by the kit's
  own moments — the same effect ScrollTrigger would be bought for.

## Assets

Everything is the firm's own material: `network-hero.jpg` (the node network),
`globe-hero.jpg` (the earth), `folio-hero.jpg` (the monogram in the leather),
`sibo/langa/bryan-800.jpg` (the three partners), `wordmark.png` (the logotype),
`hero-globe.mp4` (the film). `assets/brand-mark.svg` is the EC monogram, used
as the favicon.

## The rules the client's design overrides

The design and the taste-skill's layout rules disagree in a few places. The
design wins; each departure is recorded in `.taste-skill/waivers.json` (five
entries, the gate's limit) or reported as an open FAIL:

- the section headings are **centred** (the kit wants every heading on the left
  line or on one split line);
- the framework, strategies, briefings and pedigree sections carry **no
  photograph** — the design draws them as bordered cards with small line icons;
- the sections are **compact blocks** inside a one-screen section, so the air
  between two blocks is larger than the kit's 480px;
- the footer's shape is the client's, not the kit's `footer.closing`.

## Contacts

The address and both direct lines come from the brief and the research paper;
the waivers say why the checker is asked to leave them alone.
