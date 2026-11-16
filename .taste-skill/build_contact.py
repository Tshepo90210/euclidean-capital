"""The contact page, from the design."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import ARROW, write  # noqa: E402

QUESTIONS = [
    ("01", "FSCA statutory disclosure &amp; licensing credentials", "Category II FSP juristic rep", "fsca"),
    ("02", "FAIS general disclaimer &amp; institutional notice", "Non-institutional viewers", "fais"),
    ("03", "POPIA privacy, data governance &amp; cookie framework", "Institutional view", "popia"),
    ("04", "PAIA section 51 compliance manual", "Access to information", "paia"),
    ("05", "Conflict of interest (COI) management policy", "Strict separation of interest", "coi"),
    ("06", "Complaints resolution &amp; treating customers fairly (TCF)", "FAIS Ombud escalation", "complaints"),
]

ROWS = "\n".join(f"""          <button class="question" type="button" id="{i}">
            <span class="question__n">{n}</span>
            <span>{t}</span>
            <span class="question__label">{l}</span>
            <span class="question__chev" aria-hidden="true"><svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="m3.5 5 3.5 3.5L10.5 5"/></svg></span>
          </button>""" for n, t, l, i in QUESTIONS)

CONTACT = f"""  <!-- 1. THE INQUIRY GATEWAY -->
  <section class="section" id="inquiry" aria-labelledby="inquiry-h">
    <div class="wrap">
      <div class="grid">
        <div class="span-6">
          <div class="section-head">
            <h1 class="display display-2" id="inquiry-h">Initiate an investment dialogue</h1>
            <p class="lede">For institutional mandates, advisory partnerships and direct asset management enquiries, our executive team is the point of contact.</p>
          </div>
          <div class="bizcard mt-6">
            <div class="bizcard__top">
              <p class="bizcard__name">Euclidean Capital</p>
              <span class="bizcard__mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/></svg></span>
            </div>
            <dl>
              <div>
                <dt>Registered head office</dt>
                <dd>First Floor, 145 Second Street, Parkmore<br>Sandton, Johannesburg, 2196<br>South Africa</dd>
              </div>
              <div>
                <dt>Direct contact lines</dt>
                <dd><a href="tel:+27646866741">+27 64 686 6741</a><br><a href="tel:+27714435132">+27 71 443 5132</a></dd>
              </div>
              <div>
                <dt>Email</dt>
                <dd><a href="mailto:contact@euclideancapital.co.za">contact@euclideancapital.co.za</a></dd>
              </div>
            </dl>
          </div>
        </div>
        <div class="span-6 start-7">
          <div class="inquiry">
            <h3>Investor inquiry</h3>
            <p class="lede">Please complete the form below, and our team will respond within two working days.</p>
            <form class="form" action="mailto:contact@euclideancapital.co.za" method="post" enctype="text/plain" data-endpoint="" data-sent="Your inquiry is with the investment team. A partner replies within two working days." novalidate>
              <div class="field">
                <label for="f-name">Your name</label>
                <input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="f-name-err">
                <p class="field__error" id="f-name-err" hidden>Write the name the inquiry is under.</p>
              </div>
              <div class="field">
                <label for="f-type">Institutional type</label>
                <select id="f-type" name="type" required aria-describedby="f-type-err">
                  <option value="">Choose one</option>
                  <option>Institutional retirement or pension fund</option>
                  <option>Asset consultant or multi-manager</option>
                  <option>Family office or endowment</option>
                  <option>Qualified private investor</option>
                  <option>Corporate or unlisted partner</option>
                </select>
                <p class="field__error" id="f-type-err" hidden>Choose the classification that describes you.</p>
              </div>
              <div class="field">
                <label for="f-org">Firm / organisation</label>
                <input id="f-org" name="organisation" type="text" autocomplete="organization" required aria-describedby="f-org-err">
                <p class="field__error" id="f-org-err" hidden>Write the organisation the inquiry is for.</p>
              </div>
              <div class="field">
                <label for="f-email">Email address</label>
                <input id="f-email" name="email" type="email" autocomplete="email" inputmode="email" required aria-describedby="f-email-err">
                <p class="field__error" id="f-email-err" hidden>Write an email address with an @, like name@example.com.</p>
              </div>
              <div class="field">
                <label for="f-interest">Investment category</label>
                <select id="f-interest" name="interest" required aria-describedby="f-interest-err">
                  <option value="">Choose one</option>
                  <option>Public securities strategy</option>
                  <option>Unlisted capital and direct real assets</option>
                  <option>Institutional co-investment opportunities</option>
                  <option>Geoeconomic and sovereign research access</option>
                </select>
                <p class="field__error" id="f-interest-err" hidden>Choose the mandate you are asking about.</p>
              </div>
              <div class="field">
                <label for="f-tel">Direct telephone</label>
                <input id="f-tel" name="telephone" type="tel" autocomplete="tel" inputmode="tel" aria-describedby="f-tel-err">
                <p class="field__error" id="f-tel-err" hidden>Write a telephone number, or leave it empty.</p>
              </div>
              <div class="field field--wide">
                <label for="f-notes">Areas of interest</label>
                <textarea id="f-notes" name="notes" aria-describedby="f-notes-err"></textarea>
                <p class="field__error" id="f-notes-err" hidden>Write the mandate, the size and the timeline you have in mind.</p>
              </div>
              <div class="consent">
                <input id="f-popia" name="popia" type="checkbox" required aria-describedby="f-popia-err">
                <label for="f-popia">I consent to Euclidean Capital (Pty) Ltd processing my personal information to respond to this inquiry in accordance with the Protection of Personal Information Act (POPIA, Act 4 of 2013).</label>
                <p class="field__error" id="f-popia-err" hidden>Consent is required before the inquiry can be sent.</p>
              </div>
              <div class="btn-row"><button class="btn btn--light" type="submit">Submit institutional inquiry {ARROW}</button></div>
              <p class="form__status" role="status" data-form-status></p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 2. THE QUESTIONS -->
  <section class="section" id="disclosures" aria-labelledby="disclosures-h">
    <div class="wrap">
      <div class="section-head section-head--center section-head--rule">
        <h2 class="display display-2" id="disclosures-h">Frequently asked questions</h2>
      </div>
      <div class="questions mt-7">
{ROWS}
      </div>
    </div>
  </section>
"""

write("contact.html", CONTACT, "contact.html",
      "Euclidean Capital: institutional contact and disclosures in Sandton",
      "Institutional inquiries for Euclidean Capital in Sandton, Johannesburg, with the firm's FSCA, FAIS, POPIA, PAIA, conflict of interest and complaints disclosures.")

print("contact written")
