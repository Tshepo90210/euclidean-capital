"""The remaining four pages, taken from the design."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import ARROW, icon, write  # noqa: E402
from build_index_about import briefing_cards  # noqa: E402

# ---------------------------------------------------------------- the strategies page

LISTED = [("Systematic risk parity", "Macro factor exposure"),
          ("Tactical alpha", "Long/short discretion"),
          ("Macroeconomic bottom-up", "Earnings quality focus"),
          ("Concentrated beta", "Country risk allocation")]

UNLISTED = [("Structured private equity", "Control and governance"),
            ("Inflation-protected real assets", "Essential cash flow"),
            ("B-BBEE value realisation", "Transformation credentials"),
            ("Direct board governance", "Active stewardship")]


def arena_list(items):
    return "\n".join(f"""            <li><strong>{a}</strong>{b}</li>""" for a, b in items)


APPROACH = f"""  <!-- 1. THE PREMISE -->
  <section class="section" id="approach" aria-labelledby="approach-h">
    <div class="wrap">
      <span class="eyebrow">Investment approach</span>
      <div class="section-head">
        <h1 class="display display-1" id="approach-h">Structured Thinking Across Multi-Horizon Mandates</h1>
        <p class="lede">Dispassionate active management decomposes the market into three distinct horizons &mdash; tactical, fundamental and structural &mdash; and sizes every position to the horizon it belongs to, holding it only while the evidence behind it stands.</p>
      </div>
    </div>
  </section>

  <!-- 2. THE FILM -->
  <section class="band band--film" aria-label="The firm's film">
    <picture class="layer band__bg">
      <video id="hero-film" poster="assets/web/hero-globe.jpg" muted playsinline loop preload="metadata" aria-hidden="true">
        <source src="assets/web/hero-globe.mp4" type="video/mp4">
      </video>
    </picture>
    <div class="wrap"></div>
  </section>

  <!-- 3. THE TWO ARENAS -->
  <section class="section" id="arenas" aria-labelledby="arenas-h">
    <div class="wrap">
      <div class="section-head section-head--center section-head--rule">
        <h2 class="display display-2" id="arenas-h">Dual Arenas of Institutional Deployment</h2>
      </div>
      <div class="grid mt-7">
        <div class="span-6 arena">
          <h3>Listed Securities &amp; Public Equities</h3>
          <p>Active long/short with structural research on South African and regional equities, allocating to divergent sectors and the specific catalysts within them.</p>
          <ul>
{arena_list(LISTED)}
          </ul>
          <div class="rules">
            <span>Systematic &middot; Discretionary &middot; Multi-horizon</span>
            <span>Listed process &middot; Deep fundamental review</span>
          </div>
          <div class="btn-row"><a class="btn btn--light" href="contact.html#inquiry">Request strategy details {ARROW}</a></div>
        </div>
        <div class="span-6 arena">
          <h3>Private Companies &amp; Unlisted Capital</h3>
          <p>Direct deployment into non-correlated, cash-generative private enterprises and strategic infrastructure, with governance at the board table and transformational value creation built in.</p>
          <ul>
{arena_list(UNLISTED)}
          </ul>
          <div class="rules">
            <span>Control &middot; Governance &middot; Value creation</span>
            <span>Direct ownership &middot; Private market access</span>
          </div>
          <div class="btn-row"><a class="btn btn--light" href="contact.html#inquiry">Request private market analysis {ARROW}</a></div>
        </div>
      </div>
    </div>
  </section>
"""

write("approach.html", APPROACH, "approach.html",
      "Euclidean Capital: investment strategies for institutions in Sandton",
      "Structured thinking across multi-horizon mandates: listed securities and public equities, private companies and unlisted capital, deployed from one research desk.")

# ---------------------------------------------------------------- the insights page

ALL_BRIEFINGS = [
    ("Geopolitics", "28 Sep 2026", "Critical Minerals and Geopolitical Realignment",
     "The impact of Western and Asian resource competition on African mining equity valuations and downstream beneficiation policy frameworks.",
     "Policy archive", "3 min read"),
    ("Listed Equities", "14 Sep 2026", "Forensic Balance Sheet Scrutiny in Inflationary Environments",
     "Detecting cash-flow distortion and inventory bloating in consumer goods stocks through rigorous restatements of capitalised lease commitments.",
     "Forensic audit", "5 min read"),
    ("Sub-Saharan Africa", "2 Sep 2026", "Currency Volatility and Cross-Border Capital Flows",
     "Managing foreign exchange liquidity risks when investing in pan-African equity markets and evaluating central bank swap channel mechanisms.",
     "Macro FX", "4 min read"),
    ("Private Markets", "20 Sep 2026", "Active Capital in Mid-Market South African Enterprises",
     "A case study on operational capital deployment in unlisted commercial real assets, governance restructuring and working capital optimisation.",
     "Case note 12", "5 min read"),
    ("Geopolitics", "5 Sep 2026", "Sovereign Debt Restructuring Across African Markets",
     "Evaluating yield compression and sovereign debt dynamics in Sub-Saharan capital markets following multi-lateral bilateral debt perimeter realignments.",
     "Research desk", "4 min read"),
    ("Listed Equities", "22 Aug 2026", "Style-Agnostic Execution During High Market Dispersion",
     "Why fixed investment styles fail during macro transitions and how multi-horizon screening protects capital across asymmetric cyclical shifts.",
     "Equity strategy", "4 min read"),
]

INSIGHTS = f"""  <!-- 1. THE DESK -->
  <section class="section" id="desk" aria-labelledby="desk-h">
    <div class="wrap">
      <div class="section-head section-head--center">
        <h1 class="display display-1" id="desk-h">Institutional Research &amp; Market Intelligence</h1>
        <p class="lede center">Decoding the transmission of macroeconomic variables, geopolitical realignments and sovereign fiscal stress into actionable equity and fixed income insights.</p>
      </div>
    </div>
  </section>

  <!-- 2. THE FEATURED BRIEFING -->
  <section class="section" id="featured" aria-labelledby="featured-h">
    <div class="wrap">
      <div class="grid">
        <div class="span-8">
          <span class="eyebrow">Institutional research &middot; Markets analysis &middot; Geopolitics</span>
          <div class="section-head">
            <h2 class="display display-2" id="featured-h">Global Trade Fragmentation, US Tariff Shifts, and SA Equity Valuations</h2>
            <p class="lede">An analysis of how emerging market supply chains are adjusting to shifting trade policies, and where asymmetric equity opportunities are emerging on the JSE. Forensic evaluation reveals deep mispricings across defensive industrial export platforms facing structurally decoupled demand.</p>
          </div>
          <div class="report__meta mt-5">
            <img src="assets/web/langa-800.jpg" alt="Langa Malimela" width="800" height="1000" loading="lazy">
            <p><strong>Langa Malimela</strong>Chief Research Officer &amp; Executive Director</p>
            <p>20 Oct 2026 &middot; 4 min read</p>
          </div>
          <hr class="rule mt-5">
          <div class="foot-links mt-5">
            <span>&copy; 2026 Euclidean Capital (Pty) Ltd. All rights reserved.</span>
            <a href="#all">View all insights {ARROW}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3. ALL THE BRIEFINGS -->
  <section class="section" id="all" aria-labelledby="all-h">
    <div class="wrap">
      <div class="section-head section-head--center section-head--rule">
        <h2 class="display display-2" id="all-h">Insights</h2>
      </div>
      <div class="briefings fill mt-7">
{briefing_cards(ALL_BRIEFINGS)}
      </div>
    </div>
  </section>
"""

write("insights.html", INSIGHTS, "insights.html",
      "Euclidean Capital: institutional research and market intelligence in Sandton",
      "Weekly geoeconomic research from the Euclidean Capital desk: geopolitics, global trade shifts, sovereign risk and African capital market briefings for institutional allocators.")

# ---------------------------------------------------------------- the research report page

TAKEAWAYS = [
    ("01", "Asymmetric duration exposure",
     "Yes, but the engagement is tighter and the alpha is structurally more fragile than historic models assume. High-duration frontier sovereigns, facing funding differentials, are increasingly compromised by capital flight dynamics."),
    ("02", "Forensic balance sheet de-risking",
     "Companies characterised by short-duration unhedged US-dollar liabilities face severe rollover refi. Currency-denominated debts and foreign revenue streams show margin resilience."),
    ("03", "Actionable portfolio orientation",
     "We maintain a concentrated, style-agnostic tilt toward mission-critical South African infrastructure and high-quality liquid consumer staples capable of dynamic pricing pass-through."),
]

METRICS = [("PGM &amp; Strategic Heavy Metals", "0.24", "92.4%", "11.8%", "Uncorrelated"),
           ("Mid-Market Logistics Intermediaries", "0.41", "68.1%", "14.2%", "Uncorrelated"),
           ("Discretionary Retail Imports", "1.18", "34.0%", "6.1%", "Uncorrelated")]

ROWS = "\n".join(f"""            <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>""" for a, b, c, d, e in METRICS)
ITEMS = "\n".join(f"""            <li><strong>{n}</strong>{t}</li>""" for n, t, _ in TAKEAWAYS)

RESEARCH = f"""  <!-- 1. THE REPORT -->
  <section class="section" id="report" aria-labelledby="report-h">
    <div class="wrap">
      <article class="report">
        <p class="report__strip">Euclidean Capital Research &middot; September 2026</p>
        <p class="eyebrow">Institutional research report &middot; 24 pages</p>
        <p><span class="tag">Geopolitical outlook</span> <span class="tag">October 2026</span></p>
        <h1 class="display display-2" id="report-h">Global Trade Fragmentation, US Tariff Shifts, and SA Equity Valuations</h1>
        <div class="report__meta">
          <img src="assets/web/langa-800.jpg" alt="Langa Malimela" width="800" height="1000" loading="lazy">
          <p><strong>Langa Malimela</strong>Chief Research Officer &amp; Executive Director</p>
          <p>20 Oct 2026 &middot; 4 min read</p>
        </div>
        <hr class="rule">
        <p>The core thesis of fragmentation is complex. Advanced economies face a multi-layered realignment of trade and capital flows, with fragmentation, not globalisation, defining the decade. The transition from a rules-based trading system to a highly fragmented, bilateral transactional model requires a specific cognitive shift.</p>
        <h3>I. Structural decoupling and emerging market supply chains</h3>
        <p>South America stands in sharp relief. The regional value chain represents the purpurious reality of international trade in an era of increasing fragmentation. The transition from a rules-based trading system to a highly fragmented, bilateral transactional model requires a specific cognitive shift that market participants have yet to fully absorb.</p>
        <blockquote class="report__pull">Market efficiency assumes stable capital flows. Fragmentation invalidates both the transmission mechanism and the timing of the dislocation.<cite>&mdash; Euclidean Capital Research Desk</cite></blockquote>
        <h3>II. Key refined institutional takeaways</h3>
        <ul class="takeaways">
{ITEMS}
        </ul>
        <hr class="rule">
        <p class="table-label">Table 1.1: Comparative sensitivity metrics (JSE sectoral dispersion)</p>
        <table>
          <thead><tr><th>Sub-sector asset class</th><th>Tariff beta</th><th>FX pass-through</th><th>FCF yield</th><th>Value</th></tr></thead>
          <tbody>
{ROWS}
          </tbody>
        </table>
        <hr class="rule">
        <div class="report__desk">
          <div>
            <p class="report__desk-name">Euclidean Capital Research Desk</p>
            <p class="report__desk-line">Inquiries: research@euclideancapital.co.za &middot; Verified reference #EC-2026-881</p>
          </div>
          <a class="btn btn--light" href="contact.html#inquiry">Request access</a>
        </div>
        <div class="report__notice">
          <strong>Mandatory statutory regulatory notice</strong>
          FAIS notice: this commentary is published for informational purposes only and does not constitute financial or investment advice. Euclidean Capital (Pty) Ltd is an authorized Juristic Representative operating under an approved Financial Services Provider license. All investors should seek fiduciary and legal counsel before executing capital repositioning based on systemic macroeconomic indices.
        </div>
      </article>
    </div>
  </section>
"""

write("research.html", RESEARCH, "approach.html",
      "Global Trade Fragmentation, US Tariff Shifts, and SA Equity Valuations: Euclidean Capital Research",
      "Euclidean Capital institutional research report: global trade fragmentation, US tariff shifts and South African equity valuations, with comparative sensitivity metrics.")

print("approach, insights and research written")
