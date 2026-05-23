"""Prina Insurance — Home Page"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from utils.styles import GOOGLE_FONTS, BASE_CSS, navbar, hero, footer

st.set_page_config(
    page_title="Prina Insurance — EndoLife 20",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GOOGLE_FONTS + BASE_CSS, unsafe_allow_html=True)

# ── Navbar ────────────────────────────────────────────────────────────────────
st.markdown(navbar("home"), unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(hero(), unsafe_allow_html=True)

# ── Divider ───────────────────────────────────────────────────────────────────
st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

# ── Features ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section" id="produk">
  <div class="section-label">4 Perlindungan Komprehensif</div>
  <h2 class="section-title">Satu Polis, <em>Empat Jaminan</em></h2>
  <p class="section-desc">
    EndoLife 20 dirancang dengan model multiple decrement aktuaria 
    — melindungi Anda dari empat risiko sekaligus dalam satu polis yang sederhana.
  </p>

  <div class="features-grid">

    <div class="feature-card">
      <div class="feature-icon">🫀</div>
      <div class="feature-title">Meninggal Non-Kecelakaan</div>
      <p class="feature-desc">
        Perlindungan atas risiko meninggal akibat penyakit seperti jantung, 
        kanker, diabetes, dan kondisi medis lainnya.
      </p>
      <div class="feature-benefit">100% Uang Pertanggungan</div>
    </div>

    <div class="feature-card">
      <div class="feature-icon">🚑</div>
      <div class="feature-title">Meninggal Kecelakaan</div>
      <p class="feature-desc">
        Manfaat ganda khusus untuk risiko meninggal akibat kecelakaan, 
        memberikan perlindungan ekstra bagi keluarga Anda.
      </p>
      <div class="feature-benefit">200% Uang Pertanggungan</div>
    </div>

    <div class="feature-card">
      <div class="feature-icon">♿</div>
      <div class="feature-title">Cacat Tetap Total</div>
      <p class="feature-desc">
        Manfaat atas kondisi cacat tetap total dengan 14 kategori berdasarkan 
        tingkat keparahan — dari 5% hingga 100% UP.
      </p>
      <div class="feature-benefit">5% – 100% Uang Pertanggungan</div>
    </div>

    <div class="feature-card">
      <div class="feature-icon">💰</div>
      <div class="feature-title">Maturity Benefit</div>
      <p class="feature-desc">
        Bila Anda sehat hingga akhir masa pertanggungan 20 tahun, 
        terima kembali penuh nilai uang pertanggungan Anda.
      </p>
      <div class="feature-benefit">100% Uang Pertanggungan</div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ── Benefits Detail ───────────────────────────────────────────────────────────
st.markdown("""
<div class="gold-divider"></div>
<div class="section section-alt">
  <div class="section-label">Rincian Manfaat</div>
  <h2 class="section-title">Tabel Manfaat <em>Cacat Tetap Total</em></h2>
  <p class="section-desc">
    Setiap kondisi cacat memiliki skala manfaat yang adil dan transparan, 
    ditetapkan berdasarkan tingkat gangguan fungsional.
  </p>

  <div class="benefits-grid">
    <div>
      <div class="benefit-table">
        <div class="benefit-table-header">
          <span>Kategori Cacat</span><span>Manfaat</span>
        </div>
        <div class="benefit-row"><span class="b-name">Kedua anggota gerak atas</span><span class="b-pct">100%</span></div>
        <div class="benefit-row"><span class="b-name">Kedua anggota gerak bawah</span><span class="b-pct">100%</span></div>
        <div class="benefit-row"><span class="b-name">Kedua mata</span><span class="b-pct">100%</span></div>
        <div class="benefit-row"><span class="b-name">Satu atas + satu bawah</span><span class="b-pct">100%</span></div>
        <div class="benefit-row"><span class="b-name">Satu atas + satu mata</span><span class="b-pct">100%</span></div>
        <div class="benefit-row"><span class="b-name">Satu bawah + satu mata</span><span class="b-pct">100%</span></div>
        <div class="benefit-row"><span class="b-name">Satu anggota gerak atas</span><span class="b-pct">65%</span></div>
        <div class="benefit-row"><span class="b-name">Satu lengan bawah &amp; tangan</span><span class="b-pct">60%</span></div>
        <div class="benefit-row"><span class="b-name">Satu tangan</span><span class="b-pct">55%</span></div>
        <div class="benefit-row"><span class="b-name">Satu anggota gerak bawah</span><span class="b-pct">50%</span></div>
        <div class="benefit-row"><span class="b-name">Satu mata</span><span class="b-pct">30%</span></div>
        <div class="benefit-row"><span class="b-name">Satu ibu jari tangan</span><span class="b-pct">25%</span></div>
        <div class="benefit-row"><span class="b-name">Satu jari tangan</span><span class="b-pct">12%</span></div>
        <div class="benefit-row"><span class="b-name">Satu jari kaki</span><span class="b-pct">5%</span></div>
      </div>
    </div>

    <div class="highlight-card">
      <div class="highlight-item">
        <div class="h-icon">📋</div>
        <div>
          <div class="h-title">Level Premium — Premi Tetap 20 Tahun</div>
          <div class="h-desc">Premi tidak berubah sepanjang masa pertanggungan, memberikan kepastian anggaran keuangan Anda.</div>
        </div>
      </div>
      <div class="highlight-item">
        <div class="h-icon">📊</div>
        <div>
          <div class="h-title">Berbasis TMI 2019</div>
          <div class="h-desc">Perhitungan premi menggunakan Tabel Mortalitas Indonesia 2019 — standar aktuaria nasional resmi.</div>
        </div>
      </div>
      <div class="highlight-item">
        <div class="h-icon">🔄</div>
        <div>
          <div class="h-title">Cash Value saat Surrender</div>
          <div class="h-desc">Peserta yang mengakhiri polis lebih awal menerima 50% dari cadangan berjalan sebagai nilai tunai.</div>
        </div>
      </div>
      <div class="highlight-item">
        <div class="h-icon">🏦</div>
        <div>
          <div class="h-title">Cadangan Prospektif Terverifikasi</div>
          <div class="h-desc">Cadangan dihitung dengan metode net premium prospektif — dijamin V₂₀ = 100% Uang Pertanggungan.</div>
        </div>
      </div>
      <div class="highlight-item">
        <div class="h-icon">👤</div>
        <div>
          <div class="h-title">Usia Masuk 20 – 60 Tahun</div>
          <div class="h-desc">Tersedia untuk peserta usia 20 hingga 60 tahun, dengan masa pertanggungan selesai paling lambat usia 80.</div>
        </div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-section">
  <div class="section-label" style="text-align:center;">Mulai Sekarang</div>
  <h2 class="section-title" style="text-align:center; max-width:600px; margin: 0 auto 16px;">
    Berapa Premi yang <em>Anda Butuhkan?</em>
  </h2>
  <p class="section-desc" style="text-align:center; margin: 0 auto 36px;">
    Gunakan kalkulator aktuaria kami untuk menghitung premi kotor dan tabel cadangan 
    secara real-time berdasarkan usia, jenis kelamin, dan uang pertanggungan Anda.
  </p>
  <div style="text-align:center;">
    <a href="/Kalkulator_Premi" class="btn-primary" style="font-size:1rem; padding:16px 40px;">
      Hitung Premi Saya →
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(footer(), unsafe_allow_html=True)
