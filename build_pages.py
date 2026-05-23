import os

NAV = """  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="logo-link"><img src="images/starcitylogonobackground.png" alt="Star City Roofing El Paso" class="logo" /></a>
      <nav class="main-nav"><ul>
        <li><a href="index.html">Home</a></li>
        <li class="has-dropdown"><a href="#">Services ▾</a><ul class="dropdown">
          <li><a href="roof-replacement-el-paso.html">Roof Replacement</a></li>
          <li><a href="roof-repair-el-paso.html">Roof Repair</a></li>
          <li><a href="storm-damage-roof-repair-el-paso.html">Storm Damage Repair</a></li>
          <li><a href="flat-roof-coating-el-paso.html">Flat Roof Coating</a></li>
        </ul></li>
        <li class="has-dropdown"><a href="service-areas.html">Service Areas ▾</a><ul class="dropdown">
          <li><a href="roofing-northeast-el-paso.html">Northeast El Paso</a></li>
          <li><a href="roofing-east-el-paso.html">East El Paso</a></li>
          <li><a href="roofing-west-el-paso.html">West El Paso</a></li>
          <li><a href="roofing-upper-valley-el-paso.html">Upper Valley</a></li>
          <li><a href="roofing-horizon-city.html">Horizon City</a></li>
          <li><a href="roofing-socorro-tx.html">Socorro</a></li>
        </ul></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul></nav>
      <a href="tel:9157405961" class="btn-call">📞 (915) 740-5961</a>
      <button class="hamburger" id="hamburger" aria-label="Menu">☰</button>
    </div>
    <nav class="mobile-nav" id="mobileNav"><ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="roof-replacement-el-paso.html">Roof Replacement</a></li>
      <li><a href="roof-repair-el-paso.html">Roof Repair</a></li>
      <li><a href="storm-damage-roof-repair-el-paso.html">Storm Damage Repair</a></li>
      <li><a href="flat-roof-coating-el-paso.html">Flat Roof Coating</a></li>
      <li><a href="service-areas.html">Service Areas</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li><a href="tel:9157405961" class="btn-call-mobile">📞 (915) 740-5961</a></li>
    </ul></nav>
  </header>"""

FOOTER = """  <footer class="site-footer">
    <div class="container footer-inner">
      <div class="footer-col">
        <img src="images/starcitylogonobackground.png" alt="Star City Roofing" class="footer-logo" />
        <p>El Paso's trusted roofing contractor. Locally owned, fully licensed &amp; insured. Serving all of El Paso and surrounding areas.</p>
        <a href="tel:9157405961" class="footer-phone">(915) 740-5961</a>
      </div>
      <div class="footer-col"><h4>Services</h4><ul>
        <li><a href="roof-replacement-el-paso.html">Roof Replacement El Paso</a></li>
        <li><a href="roof-repair-el-paso.html">Roof Repair El Paso</a></li>
        <li><a href="storm-damage-roof-repair-el-paso.html">Storm Damage Roof Repair</a></li>
        <li><a href="flat-roof-coating-el-paso.html">Flat Roof Coating El Paso</a></li>
      </ul></div>
      <div class="footer-col"><h4>Service Areas</h4><ul>
        <li><a href="roofing-northeast-el-paso.html">Northeast El Paso</a></li>
        <li><a href="roofing-east-el-paso.html">East El Paso</a></li>
        <li><a href="roofing-west-el-paso.html">West El Paso</a></li>
        <li><a href="roofing-upper-valley-el-paso.html">Upper Valley</a></li>
        <li><a href="roofing-horizon-city.html">Horizon City</a></li>
        <li><a href="roofing-socorro-tx.html">Socorro, TX</a></li>
        <li><a href="service-areas.html">View All Areas</a></li>
      </ul></div>
      <div class="footer-col"><h4>Company</h4><ul>
        <li><a href="about.html">About Us</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="index.html#quote">Free Estimate</a></li>
      </ul>
        <p class="footer-address">11115 Dyer St<br>El Paso, TX 79934</p>
      </div>
    </div>
    <div class="footer-bottom"><p>© 2026 Star City Roofing. All Rights Reserved. | El Paso, TX | <a href="tel:9157405961">(915) 740-5961</a></p></div>
  </footer>
  <script src="main.js"></script>"""

def page(title, meta_desc, canonical, h1, hero_p, breadcrumb_label, content_html, img1, img2="images/roof3.jpeg"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="canonical" href="https://starcityroofing.com/{canonical}" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800;900&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css" />
</head>
<body>
{NAV}
  <section class="inner-hero">
    <div class="container inner-hero-content">
      <div class="breadcrumb"><a href="index.html">Home</a><span class="sep">›</span><span>{breadcrumb_label}</span></div>
      <h1>{h1}</h1>
      <p>{hero_p}</p>
      <div class="inner-hero-ctas">
        <a href="index.html#quote" class="btn-primary">Get a Free Estimate</a>
        <a href="tel:9157405961" class="btn-secondary">📞 (915) 740-5961</a>
      </div>
    </div>
  </section>
  <section class="content-section">
    <div class="container content-grid">
      <div class="content-main">{content_html}</div>
      <div>
        <div class="sidebar-cta">
          <h3>Free Estimate</h3>
          <p>Call us or submit the form — we respond same day.</p>
          <a href="tel:9157405961" class="sidebar-phone">(915) 740-5961</a>
          <a href="index.html#quote" class="btn-primary">Get Free Estimate →</a>
        </div>
        <div style="margin-top:24px;background:white;border-radius:6px;overflow:hidden;box-shadow:0 4px 16px rgba(0,0,0,0.08);">
          <img src="{img1}" alt="{h1}" style="width:100%;height:200px;object-fit:cover;" />
          <div style="padding:12px;"><img src="{img2}" alt="Roofing El Paso TX" style="width:100%;height:150px;object-fit:cover;border-radius:4px;" /></div>
        </div>
        <div style="margin-top:24px;background:var(--charcoal);border-radius:6px;padding:20px;border-left:4px solid var(--gold);">
          <p style="color:var(--gold);font-family:var(--font-head);font-size:0.8rem;font-weight:800;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:8px;">⭐ 4.9 Google Rating · 181 Reviews</p>
          <p style="color:rgba(255,255,255,0.8);font-size:0.88rem;font-style:italic;">"Star City showed up on time, did quality work, and left everything clean. Best roofing company in El Paso."</p>
          <p style="color:rgba(255,255,255,0.5);font-size:0.8rem;margin-top:8px;">— Verified Google Review</p>
        </div>
      </div>
    </div>
  </section>
  <section class="quote-section" id="quote">
    <div class="container quote-inner">
      <div class="quote-text">
        <h2>Free Estimate — El Paso, TX</h2>
        <p>No pressure. No obligation. We'll call you same day.</p>
        <ul class="quote-perks"><li>✅ Free Inspection</li><li>✅ Same-Day Response</li><li>✅ Licensed &amp; Insured</li><li>✅ No Hidden Fees</li></ul>
        <p class="quote-phone">Or call us:<br><a href="tel:9157405961">(915) 740-5961</a></p>
      </div>
      <div class="quote-form">
        <form name="contact" method="POST" data-netlify="true" action="/thank-you.html">
          <input type="hidden" name="form-name" value="contact" />
          <div class="form-group"><label>Name *</label><input type="text" name="name" placeholder="John Smith" required /></div>
          <div class="form-group"><label>Phone *</label><input type="tel" name="phone" placeholder="(915) 000-0000" required /></div>
          <div class="form-group"><label>Email</label><input type="email" name="email" placeholder="you@email.com" /></div>
          <div class="form-group"><label>Message</label><textarea name="message" rows="3" placeholder="Tell us about your roof..."></textarea></div>
          <button type="submit" class="btn-submit">Get My Free Estimate →</button>
        </form>
      </div>
    </div>
  </section>
{FOOTER}
</body>
</html>"""

pages = {
    "roof-repair-el-paso.html": {
        "title": "Roof Repair El Paso TX | Star City Roofing – Same-Day Estimates",
        "meta": "Need roof repair in El Paso, TX? Star City Roofing fixes leaks, damaged shingles & storm damage fast. Licensed, insured, 4.9★ rated. Call (915) 740-5961.",
        "canonical": "roof-repair-el-paso.html",
        "h1": "Roof Repair in<br>El Paso, TX",
        "hero_p": "Fast, affordable roof repairs for El Paso homeowners. Leaks, cracked shingles, flashing, storm damage — we find the problem and fix it right the first time.",
        "breadcrumb": "Roof Repair El Paso",
        "img1": "images/repair1.jpg",
        "img2": "images/roof8.jpeg",
        "content": """
        <h2>El Paso Roof Repair Specialists</h2>
        <p>Not every roof problem requires a full replacement. Star City Roofing performs expert roof repairs across El Paso — from minor leaks to major storm damage. We diagnose the real problem, not just the symptom, and give you an honest recommendation.</p>
        <p>If we can fix it with a repair, we'll tell you. If we think you need a replacement, we'll tell you that too — with the evidence to back it up. No upselling.</p>
        <h2>Common Roof Repairs We Handle in El Paso</h2>
        <ul>
          <li>Roof leaks — finding the source and sealing it permanently</li>
          <li>Missing, cracked, or curling shingles</li>
          <li>Damaged or improperly installed flashing</li>
          <li>Pipe boot and vent seal failures</li>
          <li>Valley damage from monsoon runoff</li>
          <li>Hail damage — partial replacement or repair</li>
          <li>Roof deck rot or soft spots</li>
          <li>Ridge cap and hip repairs</li>
          <li>Fascia and soffit damage</li>
        </ul>
        <h2>Why Timely Roof Repair Matters in El Paso</h2>
        <p>El Paso's climate is tough on roofs. Intense UV exposure, extreme heat cycling, monsoon storms, and occasional hail all accelerate wear. A small leak ignored for one monsoon season can lead to decking rot, mold, and interior damage that turns a $500 repair into a $15,000 replacement.</p>
        <p>Call us at the first sign of trouble — we're often able to provide same-day estimates and schedule repairs within days.</p>
        <h2>Related Services</h2>
        <ul>
          <li><a href="roof-replacement-el-paso.html" style="color:var(--red);">Roof Replacement El Paso</a> — when repair isn't enough</li>
          <li><a href="storm-damage-roof-repair-el-paso.html" style="color:var(--red);">Storm Damage Roof Repair</a> — hail and wind damage</li>
          <li><a href="service-areas.html" style="color:var(--red);">Service Areas</a> — all El Paso neighborhoods served</li>
        </ul>
        """
    },
    "storm-damage-roof-repair-el-paso.html": {
        "title": "Storm Damage Roof Repair El Paso TX | Star City Roofing",
        "meta": "Hail or storm damage to your El Paso roof? Star City Roofing responds fast, documents damage, and works with insurance. Call (915) 740-5961.",
        "canonical": "storm-damage-roof-repair-el-paso.html",
        "h1": "Storm Damage Roof Repair<br>in El Paso, TX",
        "hero_p": "El Paso monsoons and hailstorms can destroy a roof fast. We respond quickly, document all damage, and restore your roof to full protection.",
        "breadcrumb": "Storm Damage Repair",
        "img1": "images/stormrepair1.jpg",
        "img2": "images/before3.jpeg",
        "content": """
        <h2>Fast Storm Damage Response in El Paso</h2>
        <p>El Paso's monsoon season — July through September — brings severe thunderstorms, high winds, and hail that can cause significant roof damage. When a storm hits your home, you need a fast, honest roofing contractor who can assess the damage and get you protected quickly.</p>
        <p>Star City Roofing responds fast to storm damage calls across El Paso. We provide thorough documentation that's useful if you need to file an insurance claim.</p>
        <h2>Types of Storm Damage We Repair</h2>
        <ul>
          <li>Hail damage — dented, cracked, or granule-stripped shingles</li>
          <li>Wind damage — lifted, blown-off, or torn shingles</li>
          <li>Monsoon debris impact — branches, debris punctures</li>
          <li>Flashing displacement from wind or water pressure</li>
          <li>Gutter damage from storm debris or ice</li>
          <li>Interior water intrusion from storm damage</li>
        </ul>
        <h2>Insurance Claims — We Can Help</h2>
        <p>If your storm damage is covered by homeowners insurance, we can assist with the process. We document the damage thoroughly with photos, provide a detailed estimate, and can be present during the adjuster's inspection to make sure nothing is missed.</p>
        <p>We don't make promises about what insurance will or won't cover — but we make sure your damage is fully and accurately documented.</p>
        <h2>Related Services</h2>
        <ul>
          <li><a href="roof-replacement-el-paso.html" style="color:var(--red);">Roof Replacement El Paso</a> — when storm damage is too extensive to repair</li>
          <li><a href="roof-repair-el-paso.html" style="color:var(--red);">Roof Repair El Paso</a> — for partial storm damage</li>
          <li><a href="service-areas.html" style="color:var(--red);">Service Areas</a> — all of El Paso and surrounding areas</li>
        </ul>
        """
    },
    "flat-roof-coating-el-paso.html": {
        "title": "Flat Roof Coating El Paso TX | Star City Roofing",
        "meta": "Flat roof coating and repair in El Paso, TX. Elastomeric coatings that reflect heat and protect flat roofs from El Paso's extreme sun. Call (915) 740-5961.",
        "canonical": "flat-roof-coating-el-paso.html",
        "h1": "Flat Roof Coating<br>in El Paso, TX",
        "hero_p": "Elastomeric and reflective coatings that extend the life of flat roofs and reduce cooling costs in El Paso's extreme summer heat.",
        "breadcrumb": "Flat Roof Coating",
        "img1": "images/flat_roof_coating_el_paso.jpeg",
        "img2": "images/roof9.jpeg",
        "content": """
        <h2>Flat Roof Coating & Repair in El Paso</h2>
        <p>Flat roofs are common in El Paso — especially on commercial buildings, older homes, and additions. They require different care than pitched roofs, and El Paso's intense UV radiation and heat accelerate their deterioration.</p>
        <p>Star City Roofing applies high-quality elastomeric coatings and TPO membranes that protect flat roofs, seal existing cracks and seams, and reflect solar heat — reducing your cooling costs significantly.</p>
        <h2>Benefits of Flat Roof Coating in El Paso</h2>
        <ul>
          <li>Extends roof life by 10–15+ years at a fraction of replacement cost</li>
          <li>Reflective coatings reduce surface temperature by 50–80°F</li>
          <li>Seals existing cracks, seams, and ponding water areas</li>
          <li>Reduces AC load and energy bills</li>
          <li>Can be reapplied — a renewable roofing solution</li>
          <li>Qualifies for energy efficiency rebates in some cases</li>
        </ul>
        <h2>Flat Roof Services We Offer</h2>
        <ul>
          <li>Elastomeric roof coatings (white reflective)</li>
          <li>Acrylic and silicone roof coatings</li>
          <li>TPO membrane installation and repair</li>
          <li>Modified bitumen repair and coating</li>
          <li>Flat roof leak repair and ponding water correction</li>
          <li>Parapet wall and coping cap repair</li>
        </ul>
        <h2>Related Services</h2>
        <ul>
          <li><a href="roof-replacement-el-paso.html" style="color:var(--red);">Roof Replacement El Paso</a></li>
          <li><a href="roof-repair-el-paso.html" style="color:var(--red);">Roof Repair El Paso</a></li>
          <li><a href="service-areas.html" style="color:var(--red);">Service Areas</a></li>
        </ul>
        """
    },
}

# Area pages
area_data = [
    ("roofing-northeast-el-paso.html", "Northeast El Paso", "79934", "images/roof1.jpeg", "images/roof2.jpeg"),
    ("roofing-east-el-paso.html", "East El Paso", "79936, 79938", "images/roof4.jpeg", "images/roof5.jpeg"),
    ("roofing-west-el-paso.html", "West El Paso", "79912, 79922, 79932", "images/roof_replacement_upper_valley_area.jpg", "images/roof6.jpeg"),
    ("roofing-upper-valley-el-paso.html", "Upper Valley El Paso", "79932, 79835", "images/roof_replacement_upper_valley_area.jpg", "images/foldpic2.jpg"),
    ("roofing-horizon-city.html", "Horizon City", "79928", "images/roof7.jpeg", "images/roof8.jpeg"),
    ("roofing-socorro-tx.html", "Socorro, TX", "79927", "images/roof10.jpeg", "images/roof11.jpeg"),
]

for fname, area_name, zips, img1, img2 in area_data:
    content = f"""
    <h2>Roofing Contractor Serving {area_name}</h2>
    <p>Star City Roofing provides full roofing services to homeowners in {area_name} (ZIP: {zips}). From roof replacements to repairs, storm damage, and flat roof coatings — we serve every neighborhood in this area.</p>
    <p>When you're looking for a roofing contractor in {area_name}, you want someone who knows El Paso construction, understands the local climate, and gives you straight answers. That's us.</p>
    <h2>Roofing Services Available in {area_name}</h2>
    <ul>
      <li><a href="roof-replacement-el-paso.html" style="color:var(--red);">Roof Replacement</a> — Full tear-off and new roof installation</li>
      <li><a href="roof-repair-el-paso.html" style="color:var(--red);">Roof Repair</a> — Leaks, shingles, flashing, and more</li>
      <li><a href="storm-damage-roof-repair-el-paso.html" style="color:var(--red);">Storm Damage Repair</a> — Hail and wind damage restoration</li>
      <li><a href="flat-roof-coating-el-paso.html" style="color:var(--red);">Flat Roof Coating</a> — Heat-reflective coatings for flat roofs</li>
    </ul>
    <h2>Why {area_name} Homeowners Choose Star City Roofing</h2>
    <ul>
      <li>Licensed &amp; fully insured — no risk to you</li>
      <li>Free same-day estimates — just call</li>
      <li>4.9★ Google rating with 181+ verified reviews</li>
      <li>7+ years serving El Paso, including {area_name}</li>
      <li>Honest recommendations — we tell you if you don't need a full replacement</li>
    </ul>
    <h2>Other Areas We Serve</h2>
    <ul>
      <li><a href="roofing-northeast-el-paso.html" style="color:var(--red);">Northeast El Paso</a></li>
      <li><a href="roofing-east-el-paso.html" style="color:var(--red);">East El Paso</a></li>
      <li><a href="roofing-west-el-paso.html" style="color:var(--red);">West El Paso</a></li>
      <li><a href="roofing-upper-valley-el-paso.html" style="color:var(--red);">Upper Valley</a></li>
      <li><a href="roofing-horizon-city.html" style="color:var(--red);">Horizon City</a></li>
      <li><a href="roofing-socorro-tx.html" style="color:var(--red);">Socorro</a></li>
      <li><a href="service-areas.html" style="color:var(--red);">View All Service Areas</a></li>
    </ul>
    """
    pages[fname] = {
        "title": f"Roofing Contractor {area_name} TX | Star City Roofing",
        "meta": f"Star City Roofing serves {area_name}, TX with roof replacement, repair & storm damage services. Licensed, insured, 4.9★ rated. Free estimates — call (915) 740-5961.",
        "canonical": fname,
        "h1": f"Roofing Contractor<br>in {area_name}, TX",
        "hero_p": f"Serving homeowners in {area_name} with roof replacement, repair, storm damage, and flat roof services. Call us for a free same-day estimate.",
        "breadcrumb": f"{area_name} Roofing",
        "img1": img1,
        "img2": img2,
        "content": content
    }

for fname, data in pages.items():
    html = page(
        data["title"], data["meta"], data["canonical"],
        data["h1"], data["hero_p"], data["breadcrumb"],
        data["content"], data["img1"], data.get("img2", "images/roof3.jpeg")
    )
    with open(f"/home/claude/starcity/{fname}", "w") as f:
        f.write(html)
    print(f"Created: {fname}")

print("All pages generated.")
