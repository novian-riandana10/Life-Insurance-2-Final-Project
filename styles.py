"""Prina Insurance — Shared Styles & Components"""

GOOGLE_FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
"""

BASE_CSS = """
<style>
/* ── Reset & Base ─────────────────────────────────────────── */
:root {
  --navy-deep:   #060E1A;
  --navy-mid:    #0A1628;
  --navy-card:   #0F1F38;
  --navy-border: #1A3254;
  --gold:        #C9A84C;
  --gold-light:  #E8C97A;
  --gold-dim:    #8A6F2E;
  --text:        #F0F4F8;
  --text-muted:  #7A95B0;
  --text-dim:    #3D5A78;
  --white:       #FFFFFF;
  --radius:      12px;
  --radius-lg:   20px;
}

#MainMenu, header, footer { visibility: hidden !important; height: 0 !important; }
.stDeployButton { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }

.stApp {
  background: var(--navy-deep) !important;
  font-family: 'DM Sans', sans-serif;
}

.block-container {
  padding: 0 !important;
  max-width: 100% !important;
}

[data-testid="stSidebar"] {
  background: var(--navy-mid) !important;
  border-right: 1px solid var(--navy-border);
}
[data-testid="stSidebar"] * { color: var(--text) !important; }
[data-testid="stSidebarNav"] { padding-top: 0; }

/* ── Navbar ───────────────────────────────────────────────── */
.prina-nav {
  position: sticky; top: 0; z-index: 999;
  background: rgba(6,14,26,0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(201,168,76,0.15);
  padding: 0 60px;
  display: flex; align-items: center; justify-content: space-between;
  height: 68px;
}
.prina-nav .brand {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.55rem; font-weight: 600;
  color: var(--gold); letter-spacing: 0.04em;
  text-decoration: none;
}
.prina-nav .brand span { color: var(--text); font-weight: 300; }
.nav-links { display: flex; gap: 36px; align-items: center; }
.nav-links a {
  font-size: 0.88rem; font-weight: 500; letter-spacing: 0.04em;
  color: var(--text-muted); text-decoration: none;
  text-transform: uppercase; transition: color .2s;
}
.nav-links a:hover { color: var(--gold); }
.nav-cta {
  background: var(--gold); color: var(--navy-deep) !important;
  padding: 10px 24px; border-radius: 6px;
  font-weight: 600 !important; font-size: 0.83rem !important;
  letter-spacing: 0.05em !important;
  transition: background .2s !important;
}
.nav-cta:hover { background: var(--gold-light) !important; }

/* ── Hero ─────────────────────────────────────────────────── */
.hero-section {
  min-height: 88vh;
  background:
    radial-gradient(ellipse 80% 60% at 70% 40%, rgba(201,168,76,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 80% at 20% 80%, rgba(27,58,107,0.4) 0%, transparent 55%),
    linear-gradient(160deg, #060E1A 0%, #0A1628 50%, #060E1A 100%);
  display: flex; align-items: center;
  padding: 0 60px; position: relative; overflow: hidden;
}
.hero-section::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    radial-gradient(circle, rgba(201,168,76,0.08) 1px, transparent 1px);
  background-size: 48px 48px;
  opacity: 0.6;
}
.hero-section::after {
  content: '';
  position: absolute; right: 0; top: 0; bottom: 0; width: 45%;
  background: linear-gradient(135deg, rgba(10,22,40,0) 0%, rgba(201,168,76,0.04) 100%);
  border-left: 1px solid rgba(201,168,76,0.08);
}
.hero-content {
  position: relative; z-index: 2;
  max-width: 620px;
  animation: heroIn 0.9s ease both;
}
@keyframes heroIn {
  from { opacity:0; transform: translateY(30px); }
  to   { opacity:1; transform: translateY(0); }
}
.hero-eyebrow {
  font-size: 0.78rem; font-weight: 600; letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold);
  display: flex; align-items: center; gap: 12px;
  margin-bottom: 24px;
}
.hero-eyebrow::before {
  content: ''; display: block; width: 32px; height: 1px; background: var(--gold);
}
.hero-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3rem, 5vw, 5rem);
  font-weight: 600; line-height: 1.1;
  color: var(--text);
  margin: 0 0 24px;
}
.hero-title em {
  font-style: italic; color: var(--gold);
}
.hero-subtitle {
  font-size: 1.05rem; color: var(--text-muted);
  line-height: 1.7; margin-bottom: 40px;
  font-weight: 300;
}
.hero-actions { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 56px; }
.btn-primary {
  background: var(--gold);
  color: var(--navy-deep);
  padding: 14px 32px; border-radius: 6px;
  font-weight: 600; font-size: 0.92rem;
  letter-spacing: 0.04em; text-decoration: none;
  transition: all .2s;
  border: none; cursor: pointer;
  display: inline-block;
}
.btn-primary:hover { background: var(--gold-light); transform: translateY(-1px); }
.btn-outline {
  background: transparent;
  color: var(--text); border: 1px solid var(--navy-border);
  padding: 14px 32px; border-radius: 6px;
  font-weight: 500; font-size: 0.92rem;
  letter-spacing: 0.04em; text-decoration: none;
  transition: all .2s; display: inline-block;
}
.btn-outline:hover { border-color: var(--gold); color: var(--gold); }

.hero-stats { display: flex; gap: 40px; }
.stat-item .stat-val {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2.4rem; font-weight: 700;
  color: var(--gold); display: block; line-height: 1;
}
.stat-item .stat-lbl {
  font-size: 0.80rem; color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 0.08em;
  margin-top: 4px; display: block;
}
.stat-divider { width: 1px; background: var(--navy-border); }

/* ── Sections ─────────────────────────────────────────────── */
.section {
  padding: 96px 60px;
  position: relative;
}
.section-alt { background: var(--navy-mid); }

.section-label {
  font-size: 0.76rem; font-weight: 600;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--gold); margin-bottom: 12px;
}
.section-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2rem, 3.5vw, 3rem);
  font-weight: 600; color: var(--text);
  line-height: 1.2; margin: 0 0 16px;
}
.section-title em { font-style: italic; color: var(--gold); }
.section-desc {
  font-size: 1rem; color: var(--text-muted);
  line-height: 1.7; max-width: 520px;
  font-weight: 300;
}

/* ── Feature Cards ────────────────────────────────────────── */
.features-grid {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 20px; margin-top: 56px;
}
.feature-card {
  background: var(--navy-card);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 36px 28px;
  position: relative; overflow: hidden;
  transition: all .3s;
}
.feature-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  opacity: 0; transition: opacity .3s;
}
.feature-card:hover { border-color: rgba(201,168,76,0.3); transform: translateY(-4px); }
.feature-card:hover::before { opacity: 1; }
.feature-icon {
  font-size: 2rem; margin-bottom: 20px;
  width: 56px; height: 56px; border-radius: 14px;
  background: rgba(201,168,76,0.08);
  border: 1px solid rgba(201,168,76,0.15);
  display: flex; align-items: center; justify-content: center;
}
.feature-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.25rem; font-weight: 600;
  color: var(--text); margin-bottom: 10px;
}
.feature-desc { font-size: 0.875rem; color: var(--text-muted); line-height: 1.6; }
.feature-benefit {
  margin-top: 20px; padding-top: 20px;
  border-top: 1px solid var(--navy-border);
  font-size: 0.82rem; color: var(--gold);
  font-weight: 600; letter-spacing: 0.04em;
}

/* ── Benefits Table ───────────────────────────────────────── */
.benefits-grid {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 40px; margin-top: 56px; align-items: start;
}
.benefit-table {
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid var(--navy-border);
}
.benefit-table-header {
  background: linear-gradient(90deg, rgba(201,168,76,0.12), rgba(201,168,76,0.04));
  padding: 16px 24px;
  font-size: 0.78rem; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--gold);
  display: grid; grid-template-columns: 1fr auto;
  border-bottom: 1px solid var(--navy-border);
}
.benefit-row {
  display: grid; grid-template-columns: 1fr auto;
  padding: 13px 24px;
  border-bottom: 1px solid rgba(26,50,84,0.5);
  background: var(--navy-card);
  transition: background .15s;
  font-size: 0.88rem;
}
.benefit-row:last-child { border-bottom: none; }
.benefit-row:hover { background: rgba(201,168,76,0.04); }
.benefit-row .b-name { color: var(--text-muted); }
.benefit-row .b-pct {
  color: var(--gold); font-weight: 600;
  font-family: 'Cormorant Garamond', serif; font-size: 1rem;
}

.highlight-card {
  background: linear-gradient(135deg, rgba(201,168,76,0.08) 0%, rgba(201,168,76,0.02) 100%);
  border: 1px solid rgba(201,168,76,0.2);
  border-radius: var(--radius-lg); padding: 36px;
}
.highlight-item {
  display: flex; align-items: flex-start; gap: 16px;
  margin-bottom: 28px;
}
.highlight-item:last-child { margin-bottom: 0; }
.h-icon {
  width: 40px; height: 40px; border-radius: 10px;
  background: rgba(201,168,76,0.1);
  border: 1px solid rgba(201,168,76,0.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem; flex-shrink: 0;
}
.h-title { font-weight: 600; color: var(--text); font-size: 0.95rem; margin-bottom: 4px; }
.h-desc  { color: var(--text-muted); font-size: 0.85rem; line-height: 1.5; }

/* ── CTA Banner ───────────────────────────────────────────── */
.cta-section {
  padding: 80px 60px; text-align: center;
  background:
    radial-gradient(ellipse 60% 80% at 50% 50%, rgba(201,168,76,0.07) 0%, transparent 65%),
    var(--navy-mid);
  border-top: 1px solid var(--navy-border);
  border-bottom: 1px solid var(--navy-border);
}
.cta-section .section-title { margin: 0 auto 16px; }
.cta-section .section-desc { margin: 0 auto 36px; text-align: center; }

/* ── Footer ───────────────────────────────────────────────── */
.site-footer {
  background: #040B14;
  border-top: 1px solid var(--navy-border);
  padding: 60px;
}
.footer-grid {
  display: grid; grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 48px; margin-bottom: 48px;
}
.footer-brand {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.5rem; font-weight: 600; color: var(--gold); margin-bottom: 12px;
}
.footer-brand span { color: var(--text); font-weight: 300; }
.footer-desc { color: var(--text-muted); font-size: 0.85rem; line-height: 1.6; }
.footer-col-title {
  font-size: 0.75rem; font-weight: 600;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--text); margin-bottom: 16px;
}
.footer-links { display: flex; flex-direction: column; gap: 10px; }
.footer-links a { color: var(--text-muted); text-decoration: none; font-size: 0.875rem; }
.footer-links a:hover { color: var(--gold); }
.footer-bottom {
  padding-top: 28px; border-top: 1px solid var(--navy-border);
  display: flex; justify-content: space-between; align-items: center;
}
.footer-copy { color: var(--text-dim); font-size: 0.82rem; }
.footer-badge {
  font-size: 0.75rem; color: var(--text-dim); letter-spacing: 0.08em;
}

/* ── Divider ──────────────────────────────────────────────── */
.gold-divider {
  height: 1px;
  background: linear-gradient(90deg, transparent 0%, var(--gold-dim) 30%, var(--gold-dim) 70%, transparent 100%);
  margin: 0; opacity: 0.4;
}

/* Streamlit widget overrides */
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] input,
div[data-testid="stSlider"] { 
  color: var(--text) !important;
}

.stSlider [data-baseweb="slider"] [data-testid="stThumbValue"] {
  color: var(--gold) !important;
}

/* page padding wrapper */
.page-pad { padding: 32px 60px; }
</style>
"""

def navbar(active="home"):
    pages = {
        "home": ("🏠 Beranda", "/"),
        "calc": ("🧮 Kalkulator Premi", "/Kalkulator_Premi"),
    }
    links_html = ""
    for key, (label, href) in pages.items():
        cls = "nav-links a" if key != "calc" else ""
        links_html += f'<a href="{href}" class="{"nav-cta" if key=="calc" else ""}">{label}</a>'

    return f"""
    <nav class="prina-nav">
      <a class="brand" href="/">Prina<span>Insurance</span></a>
      <div class="nav-links">
        <a href="/">Beranda</a>
        <a href="#">Produk</a>
        <a href="#">Tentang Kami</a>
        <a href="/Kalkulator_Premi" class="nav-cta">Hitung Premi</a>
      </div>
    </nav>
    """

def hero():
    return """
    <section class="hero-section">
      <div class="hero-content">
        <div class="hero-eyebrow">Perlindungan Terpercaya</div>
        <h1 class="hero-title">
          Investasi &amp;<br><em>Perlindungan</em><br>Dalam Satu Polis
        </h1>
        <p class="hero-subtitle">
          EndoLife 20 — produk endowment 20 tahun yang memberikan perlindungan 
          jiwa komprehensif sekaligus kepastian nilai tunai di akhir masa pertanggungan.
        </p>
        <div class="hero-actions">
          <a href="/Kalkulator_Premi" class="btn-primary">Hitung Premi Saya →</a>
          <a href="#produk" class="btn-outline">Pelajari Produk</a>
        </div>
        <div class="hero-stats">
          <div class="stat-item">
            <span class="stat-val">4</span>
            <span class="stat-lbl">Perlindungan Decrement</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-val">20</span>
            <span class="stat-lbl">Tahun Pertanggungan</span>
          </div>
          <div class="stat-divider"></div>
          <div class="stat-item">
            <span class="stat-val">100%</span>
            <span class="stat-lbl">Uang Pertanggungan</span>
          </div>
        </div>
      </div>
    </section>
    """

def footer():
    return """
    <div class="gold-divider"></div>
    <footer class="site-footer">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Prina<span>Insurance</span></div>
          <p class="footer-desc">
            Memberikan ketenangan pikiran melalui produk asuransi jiwa yang 
            dirancang secara aktuaria dengan standar internasional.
          </p>
        </div>
        <div>
          <div class="footer-col-title">Produk</div>
          <div class="footer-links">
            <a href="#">EndoLife 20</a>
            <a href="#">Whole Life</a>
            <a href="#">Term Life</a>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Perusahaan</div>
          <div class="footer-links">
            <a href="#">Tentang Kami</a>
            <a href="#">Tim Aktuaria</a>
            <a href="#">Karir</a>
          </div>
        </div>
        <div>
          <div class="footer-col-title">Bantuan</div>
          <div class="footer-links">
            <a href="#">FAQ</a>
            <a href="#">Kontak</a>
            <a href="/Kalkulator_Premi">Kalkulator Premi</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <span class="footer-copy">© 2025 Prina Insurance. All rights reserved.</span>
        <span class="footer-badge">TMI 2019 · Multiple Decrement (UDD) · Net Premium Reserve</span>
      </div>
    </footer>
    """
