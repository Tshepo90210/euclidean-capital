"""Build the five pages of the site from the client's own Figma design.

Six frames in the design file, six pages here:
    Desktop - 1  index.html      the home page
    Desktop - 2  about.html      about the firm and the team
    Desktop - 3  insights.html   the weekly research
    Desktop - 4  research.html   one research report, in full
    Desktop - 5  contact.html    the inquiry gateway and the disclosures
    Desktop - 6  approach.html   the investment strategies

The header, the footer and the head are shared, so they are written once here.
"""
import io
import os
import sys

ROOT = r"C:\Users\kwena\Downloads\euclidean capital"

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

NAV = [("index.html", "Home"), ("about.html", "About"), ("approach.html", "Investment Strategies"),
       ("insights.html", "Insights"), ("contact.html", "Contact")]


def head(page, title, description, extra=""):
    links = "\n".join(
        f'      <div class="nav__item"><a class="nav__link" href="{href}"'
        + (' aria-current="page"' if href == page else "")
        + f">{label}</a></div>"
        for href, label in NAV)
    return f"""<!doctype html>
<!-- {title} — Euclidean Capital.
     Built from the client's Figma file "EUCLIDEAN CAPITAL MID FIDELITY DESIGN"
     (frame: {page}). Kind: service (site-kind other).
     Palette: the brand book's own swatches; crimson is deliberately absent. -->
<html lang="en" data-type="service" data-radius="soft" data-buttons="solid" data-motion>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="assets/web/globe-hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/brand-mark.svg" type="image/svg+xml">
<meta name="theme-color" content="#12182B">
<meta name="site-kind" content="other">
<meta name="page-type" content="service">
<link rel="preload" href="assets/fonts/CormorantGaramond-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/Jost-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/system.css">
<link rel="stylesheet" href="assets/ui/cards.css">
<link rel="stylesheet" href="assets/motion/motion.css">
<link rel="stylesheet" href="assets/layout/layout.css">
<link rel="stylesheet" href="assets/icons/icon.css">
<link rel="stylesheet" href="assets/brand.css">
<script>document.documentElement.classList.add('m-enter');setTimeout(()=>document.documentElement.classList.add('m-enter-done'),700)</script>
<script>document.documentElement.classList.add('mo-js');setTimeout(()=>document.documentElement.classList.add('mo-safe'),2500)</script>
<link rel="modulepreload" href="assets/moments/moments.js">
<link rel="modulepreload" href="assets/moments/lib.js">
<link rel="modulepreload" href="assets/moments/word-highlight/moment.js">
</head>
<body>

<header class="nav">
  <div class="wrap nav__bar">
    <a class="skip-link" href="#top">Skip to content</a>
    <a class="nav__logo" href="index.html" aria-label="Euclidean Capital, home"><img src="assets/web/wordmark.png" alt="Euclidean Capital"></a>
    <nav class="nav__links" aria-label="Main">
{links}
    </nav>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-label="Menu">
      <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>

<main id="top">
"""

FOOT = """</main>

<footer class="footer closing" id="contact">
  <div class="wrap">
    <div class="footer__top">
      <div>
        <p class="footer__firm">Euclidean Capital (Pty) Ltd</p>
        <address class="footer__address">First Floor, 145 Second Street, Parkmore<br>Sandton, Johannesburg, 2196<br>South Africa</address>
      </div>
      <div>
        <p class="footer__label">Direct contact lines</p>
        <address class="footer__lines"><a href="tel:+27646866741">+27 64 686 6741</a><br><a href="tel:+27714435132">+27 71 443 5132</a></address>
      </div>
      <div>
        <p class="footer__label">Email</p>
        <address class="footer__lines"><a href="mailto:contact@euclideancapital.co.za">contact@euclideancapital.co.za</a></address>
      </div>
    </div>
    <nav class="footer__links" aria-label="Regulatory">
      <a href="contact.html#fsca">Regulatory links</a>
      <a href="contact.html#fais">Privacy policy</a>
      <a href="contact.html#popia">POPIA policy</a>
      <a href="contact.html#paia">PAIA section 51 manual</a>
      <a href="contact.html#coi">COI policy</a>
      <a href="contact.html#complaints">Complaints procedure</a>
    </nav>
    <div class="footer__legal">
      <span>&copy; 2026 Euclidean Capital (Pty) Ltd. All rights reserved.</span>
      <span>Developed by YaYa Developments</span>
    </div>
  </div>
</footer>

<script type="module" src="assets/system.js"></script>
<script type="module" src="assets/motion/motion.js"></script>
<script type="module" src="assets/layout/layout.js"></script>
<script type="module" src="assets/brand.js"></script>
</body>
</html>
"""

ARROW = ('<svg class="m-arrow" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.4" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path class="m-arrow__stem" d="M1 6h9"/><path class="m-arrow__head" d="M6.5 2.5 10 6l-3.5 3.5"/></svg>')

ICON = {
    "chart": '<path d="M4 20V4"/><path d="M4 20h16"/><path d="m8 16 4-5 3 3 4-6"/>',
    "scales": '<path d="M12 3v18"/><path d="M5 7h14"/><path d="m5 7-3 6a3 3 0 0 0 6 0z"/><path d="m19 7-3 6a3 3 0 0 0 6 0z"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "bank": '<path d="M4 21h16"/><path d="M2 9h20"/><path d="M12 3v6"/><path d="M4 9v12"/><path d="M9 9v12"/><path d="M15 9v12"/><path d="M20 9v12"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.6 4 5.6 4 9s-1.5 6.4-4 9c-2.5-2.6-4-5.6-4-9s1.5-6.4 4-9z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 2 4 5v6c0 5 3.4 9.2 8 11 4.6-1.8 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
}


def icon(name, cls="card__mark"):
    return (f'<span class="{cls}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg></span>')


def write(name, body, page, title, description):
    html = head(page, title, description) + body + FOOT
    with io.open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", name, len(html), "bytes")
