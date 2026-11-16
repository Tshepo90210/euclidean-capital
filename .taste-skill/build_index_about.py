"""The page bodies, taken from the design."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import ARROW, icon, write  # noqa: E402

# ---------------------------------------------------------------- the home page

FRAMEWORK = [
    ("chart", "Research-Driven Alpha",
     "Top-down geoeconomics combined with bottom-up forensic balance sheet analysis to isolate structural market anomalies before consensus realisation."),
    ("scales", "Style-Agnostic Execution",
     "Unconstrained by dogmatic value or growth boxes. Dynamically allocates exposure to asset factors supported by current real-rate and liquidity environments."),
    ("layers", "Dual-Arena Coverage",
     "Unified fiduciary governance across listed liquid equities and high-conviction unlisted private enterprises to capture distinct liquidity premiums."),
    ("bank", "Executive Pedigree",
     "Steered by institutional operators with extensive tenure across Bloomberg, S&amp;P Global, Steyn Capital, and Renaissance Capital."),
]

ARENAS = [
    ("Public Securities Strategy",
     "Bi-directional long/short and core equity mandates engineered to preserve capital during systemic liquidity contractions while harvesting upside dispersion across African equity exchanges.",
     [("Systematic factor neutralisation", "Active management of beta exposure through drawdown hedging protocols."),
      ("Forensic accounting screen", "Governance risk and balance-sheet inflation eliminated before allocation."),
      ("Dynamic cash buffering", "Discretionary liquidity holding capacity through structural valuation overshoots.")],
     "Request strategy pack", "contact.html#inquiry"),
    ("Unlisted Capital &amp; Direct Real Assets",
     "Strategic deployment into non-correlated, cash-generative private enterprises, strategic infrastructure and socio-economic real property assets demonstrating competitive moats.",
     [("Direct board representation", "Institutional governance, operational optimisation and capital allocation stewardship."),
      ("Inflation-protected yields", "Contracted recurring revenue anchored in essential industrial and commercial value chains."),
      ("B-BBEE transformation value", "Ownership models that align procurement credentials with regulation.")],
     "Inquire re co-investments", "contact.html#inquiry"),
]

BRIEFINGS = [
    ("Geoeconomics", "20 Oct 2026", "Global Trade Fragmentation and South African Equity Valuations",
     "Evaluating the structural impact of Western near-shoring and BRICS+ bilateral settlement arrangements on domestic raw material exporters and trade balance dynamics.",
     "Langa Malimela", "3 min read"),
    ("Sub-Saharan Africa", "12 Oct 2026", "Sovereign Debt Restructuring Dynamics in Frontier Markets",
     "G-20 Common Framework bottlenecks, local-currency yield volatility and asymmetric debt-for-growth opportunities for long-term institutional allocators.",
     "Langa Malimela", "4 min read"),
    ("Listed Equities", "5 Oct 2026", "Style-Agnostic Execution in High Return Dispersion",
     "Why dogmatic adherence to conventional value or momentum factors leads to persistent benchmark underperformance during cyclical inflection regimes.",
     "Sibo Khumalo", "3 min read"),
]

LINEAGE = [
    ("chart", "S&amp;P Global", "Market Intelligence"),
    ("globe", "Bloomberg", "Economics Research"),
    ("bank", "Coronation", "Fund Managers"),
    ("scales", "Steyn Capital", "Hedge Fund Division"),
]


def framework_cards():
    out = []
    for name, title, copy in FRAMEWORK:
        out.append(f"""        <article class="card">
          {icon(name)}
          <h3>{title}</h3>
          <p>{copy}</p>
        </article>""")
    return "\n".join(out)


def arena_cards():
    out = []
    for title, copy, items, cta, href in ARENAS:
        bullets = "\n".join(f"""            <li><span><strong>{a}.</strong> {b}</span></li>""" for a, b in items)
        out.append(f"""        <article class="card">
          <h3>{title}</h3>
          <p>{copy}</p>
          <ul class="bullets">
{bullets}
          </ul>
          <div class="btn-row"><a class="btn btn--light" href="{href}">{cta}</a></div>
        </article>""")
    return "\n".join(out)


def briefing_cards(cards):
    out = []
    for cat, date, title, copy, author, read in cards:
        out.append(f"""        <article>
          <span class="card__mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/></svg></span>
          <div class="meta">
            <p class="cat">{cat}</p>
            <p class="date">{date}</p>
          </div>
          <h3>{title}</h3>
          <p class="excerpt">{copy}</p>
          <div class="foot">
            <span>{author} &middot; {read}</span>
            <a href="insights.html">Read briefing</a>
          </div>
        </article>""")
    return "\n".join(out)


def lineage_cells():
    out = []
    for name, title, role in LINEAGE:
        out.append(f"""        <div>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{__import__("build_pages").ICON[name]}</svg>
          <div><span class="name">{title}</span><span class="role">{role}</span></div>
        </div>""")
    return "\n".join(out)


INDEX = f"""  <!-- 1. THE HERO — the firm's own photograph, the statement over it -->
  <section class="hero hero--ec" data-enter data-moment="word-highlight" aria-labelledby="hero-h">
    <picture class="layer hero__bg" aria-hidden="true">
      <img src="assets/web/network-hero.jpg" alt="A network of linked spheres, the firm's own study of connected markets" width="1800" height="1012">
    </picture>
    <div class="wrap">
      <div class="hero-text hero__inner">
        <h1 class="hero__statement mo-wh__text" id="hero-h">Dispassionate, style-agnostic active investment management can deliver consistent <strong>alpha</strong> if and only if the appropriate research is conducted and executed efficiently, across various time horizons.</h1>
        <div class="btn-row">
          <a class="btn btn--primary" href="approach.html">Our investment approach {ARROW}</a>
          <a class="btn btn--light" href="insights.html">Read weekly insights</a>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. THE FRAMEWORK -->
  <section class="section" id="framework" style="--hm: 2" aria-labelledby="framework-h">
    <div class="wrap">
      <div class="section-head section-head--center section-head--rule">
        <h2 class="display display-2" id="framework-h">The Symbiotic Fiduciary Framework</h2>
      </div>
      <div class="card-row fill mt-7">
{framework_cards()}
      </div>
    </div>
  </section>

  <!-- 3. THE STRATEGIES -->
  <section class="section" id="strategies" style="--hm: 2" aria-labelledby="strategies-h">
    <div class="wrap">
      <div class="section-head section-head--rule">
        <h2 class="display display-2" id="strategies-h">Our Strategies</h2>
      </div>
      <div class="card-row card-row--2 fill mt-7">
{arena_cards()}
      </div>
    </div>
  </section>

  <!-- 4. THE COMMENTARY BAND — the earth, the desk's name over it -->
  <section class="band" aria-labelledby="commentary-h">
    <video class="layer band__bg" id="earth-film" poster="assets/web/globe-hero.jpg" muted autoplay playsinline loop preload="metadata" aria-label="The earth at night, seen from space">
      <source src="assets/web/hero-globe.mp4" type="video/mp4">
    </video>
    <div class="wrap">
      <h2 class="band__title" id="commentary-h">Euclidean Perspectives &middot; Geoeconomic Commentary</h2>
      <button class="ec-film__play" type="button" data-film-toggle aria-label="Pause the film">
        <svg class="icon-pause" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2.5h3v11H4zM9 2.5h3v11H9z"/></svg>
        <svg class="icon-play" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2.5v11l9-5.5z"/></svg>
      </button>
    </div>
  </section>

  <!-- 5. THE BRIEFINGS -->
  <section class="section" id="briefings" aria-label="The desk's latest briefings">
    <div class="wrap">
      <div class="briefings fill">
{briefing_cards(BRIEFINGS)}
      </div>
    </div>
  </section>

  <!-- 6. THE PEDIGREE -->
  <section class="section" id="pedigree" aria-labelledby="pedigree-h">
    <div class="wrap">
      <div class="grid">
        <div class="span-7">
          <span class="eyebrow">Institutional heritage &middot; global standards</span>
          <div class="section-head">
            <h2 class="display display-2" id="pedigree-h">Institutional Track Record Built at Global Leaders</h2>
            <p class="lede">Euclidean Capital synthesises over five decades of tier-one institutional governance, data forensics and risk management into an independent African investment boutique.</p>
          </div>
        </div>
        <div class="span-4 start-9 center">
          <a class="btn btn--light" href="about.html">Meet the leadership team</a>
        </div>
      </div>
      <div class="lineage fill mt-7">
{lineage_cells()}
      </div>
    </div>
  </section>
"""

write("index.html", INDEX, "index.html",
      "Euclidean Capital: independent asset management in Sandton",
      "Euclidean Capital is an independent, black-owned asset manager in Sandton, Johannesburg. Listed equities and unlisted capital run from one research desk across multiple time horizons.")

# ---------------------------------------------------------------- about

ABOUT = """  <!-- 1. THE FIRM AND ITS CARD -->
  <section class="section" id="about" aria-labelledby="about-h">
    <div class="wrap">
      <div class="grid">
        <div class="span-6">
          <span class="eyebrow">Institutional foundation</span>
          <div class="section-head">
            <h2 class="display display-2" id="about-h">About Euclidean Capital</h2>
            <p class="lede">Euclidean Capital was established organically in 2023 with a singularly focused institutional premise: to build an agile, unencumbered investment house deliberately liberated from the bureaucratic inertia, asset-gathering incentives, and structural conflicts endemic to legacy financial institutions.</p>
            <p class="lede">As an independent, black-owned South African asset manager, our fiduciary architecture is engineered around operational agility, intellectual independence, and structural integrity. Free from distributed consensus committees, we execute high-conviction mandates where mathematical rigor and fundamental valuation precede capital deployment.</p>
          </div>
        </div>
        <div class="span-6 start-7">
          <div class="dictionary">
            <p class="dictionary__word">euclidean capital</p>
            <p class="dictionary__pos">/ju&#720;ˈkl&#618;i.d&#601;n ˈkæp.ɪ.t&#601;l/ &middot; noun</p>
            <p class="dictionary__pos">Finance &middot; Active asset management</p>
            <p class="dictionary__quote">&ldquo;Named after Euclid, the ancient Greek mathematician known as the &lsquo;Father of Geometry&rsquo;, whose principles of logic, structure and reasoning continue to shape modern science and thought. <strong>Euclidean Capital</strong> &mdash; investment philosophy and research methodology.&rdquo;</p>
            <p class="dictionary__foot">Structured thinking &middot; Active management &middot; Enduring value</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. THE ANALYTICAL CONVERGENCE — the firm's own leather, the thesis over it -->
  <section class="band band--tall" id="convergence" data-moment="word-highlight" aria-labelledby="convergence-h">
    <img class="band__bg" src="assets/web/folio-hero.jpg" alt="The firm's monogram pressed into the leather of its portfolio" width="1800" height="1012">
    <div class="wrap">
      <div class="section-head section-head--center">
        <span class="eyebrow eyebrow--center">Our analytical convergence</span>
        <h2 class="display display-2" id="convergence-h">Two disciplines, one method</h2>
      </div>
      <div class="convergence">
        <p class="mo-wh__text">Our sustainable alpha thesis emerges from the explicit synthesis of two distinct operational disciplines: top-down sovereign macroeconomic intelligence and bottom-up institutional asset stewardship. By integrating institutional portfolio execution tested on R200bn+ mandates with sovereign risk forensic analysis, Euclidean Capital systematically isolates structural market anomalies.</p>
        <p>In Sub-Saharan African capital markets, policy shifts, currency shocks and sovereign fiscal stress are not externalities &mdash; they are fundamental valuation drivers. Our converged methodology prices macro volatility into asset cash flows before consensus realises structural dislocations.</p>
      </div>
    </div>
  </section>

  <!-- 3. THE TEAM -->
  <section class="section" id="team" aria-labelledby="team-h">
    <div class="wrap">
      <div class="section-head section-head--center">
        <span class="eyebrow eyebrow--center">Our team</span>
        <h2 class="display display-2" id="team-h">The partners behind the desk</h2>
        <p class="lede center">&ldquo;Structured thinking. Active management. Enduring value.&rdquo;</p>
      </div>
      <div class="team mt-7">
        <figure>
          <img src="assets/web/sibo-800.jpg" alt="Sibo Khumalo, Chief Executive Officer and Chief Investment Officer" width="800" height="1000" loading="lazy">
          <figcaption>
            <h3>Sibo Khumalo</h3>
            <p class="role">Chief Executive Officer &amp; Chief Investment Officer</p>
          </figcaption>
        </figure>
        <figure>
          <img src="assets/web/langa-800.jpg" alt="Langa Malimela, Chief Research Officer and Executive Director" width="800" height="1000" loading="lazy">
          <figcaption>
            <h3>Langa Malimela</h3>
            <p class="role">Chief Research Officer &amp; Executive Director</p>
          </figcaption>
        </figure>
        <figure>
          <img src="assets/web/bryan-800.jpg" alt="Bryan Shuping, Executive Chairman" width="800" height="1000" loading="lazy">
          <figcaption>
            <h3>Bryan Shuping</h3>
            <p class="role">Executive Chairman</p>
          </figcaption>
        </figure>
      </div>
    </div>
  </section>
"""

write("about.html", ABOUT, "about.html",
      "Euclidean Capital: the people behind an independent asset manager in Sandton",
      "Euclidean Capital was established in 2023 in Sandton, Johannesburg by three institutional operators from Bloomberg, S&amp;P Global and Steyn Capital. Independent, black-owned and free of consensus committees.")

print("index and about written")
