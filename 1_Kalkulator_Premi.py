"""Prina Insurance — Kalkulator Premi"""
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from utils.styles import GOOGLE_FONTS, BASE_CSS, navbar, footer
from utils.actuarial import compute

st.set_page_config(
    page_title="Kalkulator Premi — Prina Insurance",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GOOGLE_FONTS + BASE_CSS, unsafe_allow_html=True)

# Extra CSS for calculator page
st.markdown("""
<style>
.calc-hero {
  background:
    radial-gradient(ellipse 70% 60% at 30% 50%, rgba(201,168,76,0.05) 0%, transparent 60%),
    linear-gradient(160deg, #060E1A 0%, #0A1628 100%);
  padding: 64px 60px 48px;
  border-bottom: 1px solid var(--navy-border);
}
.calc-hero-label { font-size:0.75rem; letter-spacing:0.16em; text-transform:uppercase; color:var(--gold); margin-bottom:10px; }
.calc-hero-title {
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(2rem,3.5vw,3rem); font-weight:600; color:var(--text);
  margin:0 0 10px; line-height:1.15;
}
.calc-hero-title em { font-style:italic; color:var(--gold); }
.calc-hero-sub { font-size:0.95rem; color:var(--text-muted); font-weight:300; max-width:500px; }

.calc-layout { display:grid; grid-template-columns:320px 1fr; min-height:70vh; }

.input-panel {
  background:var(--navy-mid);
  border-right:1px solid var(--navy-border);
  padding:40px 32px;
}
.input-section-title {
  font-size:0.72rem; font-weight:600; letter-spacing:0.14em;
  text-transform:uppercase; color:var(--gold);
  padding-bottom:12px; margin-bottom:20px;
  border-bottom:1px solid rgba(201,168,76,0.15);
}
.results-panel { padding:40px 48px; }
.results-panel-empty {
  display:flex; align-items:center; justify-content:center;
  height:100%; flex-direction:column; gap:12px;
  color:var(--text-dim); text-align:center;
}
.results-panel-empty h3 { font-family:'Cormorant Garamond',serif; font-size:1.8rem; color:var(--text-muted); }
.results-panel-empty p  { font-size:0.9rem; max-width:280px; line-height:1.6; }

/* result metrics */
.r-metrics { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:32px; }
.r-metric {
  background:var(--navy-card); border:1px solid var(--navy-border);
  border-radius:var(--radius); padding:20px;
}
.r-metric.gold-metric { border-color:rgba(201,168,76,0.3); background:rgba(201,168,76,0.05); }
.r-metric .r-val {
  font-family:'Cormorant Garamond',serif; font-size:1.6rem; font-weight:700;
  color:var(--gold); display:block; line-height:1.1; margin-bottom:4px;
}
.r-metric .r-lbl { font-size:0.78rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.06em; }
.r-metric .r-sub { font-size:0.75rem; color:var(--text-dim); margin-top:4px; }

.val-badge {
  display:inline-flex; align-items:center; gap:8px;
  padding:8px 16px; border-radius:20px;
  font-size:0.82rem; font-weight:600;
  background:rgba(29,106,48,0.25); color:#a8f0b8;
  border:1px solid rgba(29,106,48,0.4);
  margin-bottom:28px;
}

.rtab-btns { display:flex; gap:8px; margin-bottom:24px; flex-wrap:wrap; }
.rtab-btn {
  padding:8px 18px; border-radius:6px; border:1px solid var(--navy-border);
  background:transparent; color:var(--text-muted); cursor:pointer;
  font-size:0.82rem; font-family:'DM Sans',sans-serif;
  transition:all .2s;
}
.rtab-btn.active { background:rgba(201,168,76,0.1); border-color:rgba(201,168,76,0.4); color:var(--gold); }

/* Streamlit widget polish */
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stNumberInput"] label {
  font-size:0.82rem !important; color:var(--text-muted) !important;
  text-transform:uppercase; letter-spacing:0.08em; font-family:'DM Sans',sans-serif;
}
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] input {
  background:rgba(6,14,26,0.7) !important;
  border:1px solid var(--navy-border) !important;
  border-radius:8px !important; color:var(--text) !important;
}
div[data-testid="stSlider"] [data-baseweb="slider"] { margin-top:4px; }

.stButton > button {
  background:var(--gold) !important; color:var(--navy-deep) !important;
  border:none !important; border-radius:8px !important;
  font-weight:700 !important; font-size:0.9rem !important;
  padding:14px 28px !important; width:100% !important;
  letter-spacing:0.04em !important; font-family:'DM Sans',sans-serif !important;
  transition:all .2s !important;
}
.stButton > button:hover { background:var(--gold-light) !important; }
</style>
""", unsafe_allow_html=True)

BG    = "#060E1A"
GRID  = "#1A3254"
GOLD  = "#C9A84C"
MUTED = "#7A95B0"
TEXT  = "#F0F4F8"

# ── Navbar ────────────────────────────────────────────────────────────────────
st.markdown(navbar("calc"), unsafe_allow_html=True)

# ── Page Hero ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="calc-hero">
  <div class="calc-hero-label">Kalkulator Aktuaria</div>
  <h1 class="calc-hero-title">Hitung <em>Premi Anda</em></h1>
  <p class="calc-hero-sub">
    Masukkan data Anda dan dapatkan ilustrasi premi kotor, 
    tabel cadangan, dan tabel decrement secara instan.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Layout ────────────────────────────────────────────────────────────────────
st.markdown('<div class="calc-layout">', unsafe_allow_html=True)

# ── Left: Input Panel via Streamlit columns ────────────────────────────────────
col_input, col_result = st.columns([1, 2.6])

with col_input:
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    st.markdown('<div class="input-section-title">Data Peserta</div>', unsafe_allow_html=True)

    gender_lbl = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"], key="gender")
    gender     = "L" if gender_lbl == "Laki-laki" else "P"

    x = st.slider("Usia Masuk", 20, 60, 35, key="age")
    st.caption(f"Usia selesai pertanggungan: **{x+20} tahun**")

    SA = st.number_input(
        "Uang Pertanggungan (Rp)",
        min_value=10_000_000, max_value=10_000_000_000,
        value=100_000_000, step=10_000_000, format="%d",
    )

    st.markdown('<div class="input-section-title" style="margin-top:28px;">Asumsi Teknis</div>', unsafe_allow_html=True)
    i_pct = st.slider("Suku Bunga (%/tahun)", 3.0, 10.0, 5.5, 0.25)
    i = i_pct / 100.0

    st.markdown("""
    <div style="margin-top:24px; padding:16px; background:rgba(201,168,76,0.04); border:1px solid rgba(201,168,76,0.12); border-radius:10px; font-size:0.78rem; color:var(--text-muted); line-height:1.6;">
    <strong style="color:var(--gold); display:block; margin-bottom:6px;">Asumsi Aktuaria</strong>
    TMI 2019 · Acc Death = 10%×q(1) · TPD = 5%×q(1)<br>
    Lapse: 12% (Thn 1–2) · 7% (3–5) · 3% (6+)<br>
    Initial Expense: 40% · Renewal: 7% · Profit: 15%
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    hitung = st.button("Hitung Premi →", key="hitung")
    st.markdown('</div>', unsafe_allow_html=True)

# ── Right: Results Panel ──────────────────────────────────────────────────────
with col_result:
    st.markdown('<div class="results-panel">', unsafe_allow_html=True)

    if not hitung:
        st.markdown("""
        <div class="results-panel-empty">
          <div style="font-size:3rem;">🛡️</div>
          <h3>Siap Menghitung</h3>
          <p>Isi parameter di sebelah kiri, lalu klik <strong>Hitung Premi</strong> untuk melihat ilustrasi lengkap.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        with st.spinner(""):
            try:
                res = compute(x, gender, SA, i)
            except ValueError as e:
                st.error(f"❌ {e}")
                st.stop()

        P_g   = res["P_gross"]; P_n = res["P_net"]
        V     = res["V"];       n   = 20
        tpx   = res["tpx"];     iters = res["iters"]
        a_due = res["a_due"];   APV_B = res["APV_B"]
        APV_P = res["APV_P"];   APV_e = res["APV_exp"]
        profit= res["profit_actual"]
        v     = 1/(1+i)

        val_err = abs(V[20]-SA)/SA*100
        val_ok  = val_err < 0.0001

        # Validation badge
        badge_color = "#a8f0b8" if val_ok else "#f0a8a8"
        badge_bg    = "rgba(29,106,48,0.25)" if val_ok else "rgba(106,29,29,0.25)"
        badge_bdr   = "rgba(29,106,48,0.4)" if val_ok else "rgba(106,29,29,0.4)"
        badge_txt   = f"✅ V₂₀ = SA — Tervalidasi ({iters} iterasi)" if val_ok else f"⚠️ Selisih {val_err:.6f}%"
        st.markdown(
            f'<div class="val-badge" style="background:{badge_bg};color:{badge_color};border-color:{badge_bdr};">'
            f'{badge_txt}</div>',
            unsafe_allow_html=True,
        )

        # Key metrics
        st.markdown(f"""
        <div class="r-metrics">
          <div class="r-metric gold-metric">
            <span class="r-val">Rp {P_g/1e6:.3f} jt</span>
            <span class="r-lbl">Premi Kotor / Tahun</span>
            <span class="r-sub">yang ditagihkan ke peserta</span>
          </div>
          <div class="r-metric">
            <span class="r-val">Rp {P_n/1e6:.3f} jt</span>
            <span class="r-lbl">Premi Neto / Tahun</span>
            <span class="r-sub">dasar perhitungan cadangan</span>
          </div>
          <div class="r-metric">
            <span class="r-val">{P_g/SA*100:.3f}%</span>
            <span class="r-lbl">Rasio Premi / SA</span>
            <span class="r-sub">profit aktual: {profit:.2f}%</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📈 Cadangan",
            "📋 Decrement",
            "💰 APV",
            "📉 Grafik",
        ])

        # ── Tab 1: Reserve Table ──────────────────────────────────────────
        with tab1:
            rows = []
            for k in range(n+1):
                rows.append({
                    "Thn": k, "Usia": x+k,
                    "Cadangan ₖV": int(round(V[k])),
                    "Cash Value (50%)": int(round(0.5*V[k])) if k > 0 else 0,
                    "ₖV / SA": f"{V[k]/SA*100:.4f}%",
                    "Premi Kumulatif": int(round(P_g*k)),
                })
            df_r = pd.DataFrame(rows)

            def hl(row):
                if row["Thn"] == 20:
                    return ["background-color:rgba(29,106,48,0.3);color:#a8f0b8"]*len(row)
                return [""]*len(row)

            st.dataframe(
                df_r.style.apply(hl, axis=1).format({
                    "Cadangan ₖV":"{:,}",
                    "Cash Value (50%)":"{:,}",
                    "Premi Kumulatif":"{:,}",
                }),
                use_container_width=True, height=480,
            )
            st.download_button(
                "⬇️ Download CSV",
                data=df_r.to_csv(index=False).encode(),
                file_name=f"cadangan_x{x}_{gender_lbl}_SA{int(SA//1e6)}jt.csv",
                mime="text/csv",
            )

        # ── Tab 2: Decrement Table ────────────────────────────────────────
        with tab2:
            df_d = pd.DataFrame(res["asdt"])
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**ASDT (Single Decrement)**")
                st.dataframe(
                    df_d[["Tahun","Usia","q'(1)","q'(2)","q'(3)","q'(4)"]].style.format(
                        {"q'(1)":"{:.6f}","q'(2)":"{:.6f}","q'(3)":"{:.6f}","q'(4)":"{:.4f}"}
                    ), use_container_width=True, height=400,
                )
            with c2:
                st.markdown("**MDT (Multiple Decrement)**")
                st.dataframe(
                    df_d[["Tahun","Usia","q(1)","q(2)","q(3)","q(4)","q(τ)","p(τ)"]].style.format(
                        {k:"{:.6f}" for k in ["q(1)","q(2)","q(3)","q(4)","q(τ)","p(τ)"]}
                    ), use_container_width=True, height=400,
                )
            chk = (df_d["q(1)"]+df_d["q(2)"]+df_d["q(3)"]+df_d["q(4)"]+df_d["p(τ)"]-1).abs().max()
            if chk < 1e-11:
                st.success(f"✅ Identitas UDD terpenuhi: Σq(j) + p(τ) = 1 | max error = {chk:.2e}")

        # ── Tab 3: APV Breakdown ──────────────────────────────────────────
        with tab3:
            ca, cb = st.columns(2)
            with ca:
                st.markdown("**Formula Premi Kotor**")
                st.latex(r"P^g = \frac{\text{APV}_B}{0.78\,\ddot{a}^{(\tau)} - 0.33}")
                st.markdown(f"""
| Parameter | Nilai |
|---|---|
| ä (annuity-due) | `{a_due:.6f}` |
| 0.78 × ä | `{0.78*a_due:.6f}` |
| Denominator | `{0.78*a_due-0.33:.6f}` |
| APV Benefit | `Rp {APV_B:,.0f}` |
| **P^g** | **`Rp {P_g:,.0f}`** |
| **P^n** | **`Rp {P_n:,.0f}`** |
                """)

            with cb:
                st.markdown("**Komposisi APV Premi**")
                apv_df = pd.DataFrame({
                    "Komponen": ["APV Benefit","Expense Initial (40%)","Expense Renewal (7%)","Total Expense","APV Premi","Profit"],
                    "Nilai (Rp)": [f"Rp {APV_B:,.0f}",f"Rp {P_g*0.33:,.0f}",f"Rp {P_g*0.07*a_due:,.0f}",
                                   f"Rp {APV_e:,.0f}",f"Rp {APV_P:,.0f}",f"Rp {APV_P-APV_B-APV_e:,.0f}"],
                    "% APV P": [f"{APV_B/APV_P*100:.1f}%",f"{P_g*0.33/APV_P*100:.1f}%",
                                f"{P_g*0.07*a_due/APV_P*100:.1f}%",f"{APV_e/APV_P*100:.1f}%",
                                "100.0%",f"{profit:.1f}%"],
                })
                st.dataframe(apv_df, use_container_width=True, hide_index=True)

        # ── Tab 4: Charts ─────────────────────────────────────────────────
        with tab4:
            def layout(title, xt, yt, h=340):
                return dict(title=dict(text=title, font=dict(family="Cormorant Garamond",size=18,color=TEXT)),
                            xaxis_title=xt, yaxis_title=yt, height=h,
                            plot_bgcolor=BG, paper_bgcolor="rgba(0,0,0,0)",
                            font=dict(color=TEXT, family="DM Sans"),
                            xaxis=dict(gridcolor=GRID, zerolinecolor=GRID),
                            yaxis=dict(gridcolor=GRID, zerolinecolor=GRID),
                            margin=dict(t=48,b=32,l=16,r=16))

            cc1, cc2 = st.columns(2)

            with cc1:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=list(range(n+1)), y=list(V),
                    mode="lines+markers", name="Cadangan ₖV",
                    line=dict(color=GOLD, width=2.5),
                    marker=dict(size=6, color=GOLD),
                    fill="tozeroy", fillcolor="rgba(201,168,76,0.07)",
                ))
                fig.add_trace(go.Scatter(
                    x=list(range(n+1)), y=[0.5*Vk for Vk in V],
                    mode="lines", name="Cash Value",
                    line=dict(color="#5B8DB8", width=1.8, dash="dash"),
                ))
                fig.add_hline(y=SA, line_dash="dot", line_color="#e74c3c",
                              annotation_text="SA", annotation_font_color="#e74c3c")
                fig.update_layout(**layout("Perkembangan Cadangan", "Akhir Tahun ke-", "Nilai (Rp)"))
                fig.update_layout(legend=dict(x=0.02,y=0.97,bgcolor="rgba(0,0,0,0)"))
                st.plotly_chart(fig, use_container_width=True)

            with cc2:
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=list(range(n+1)), y=[tpx[t]*100 for t in range(n+1)],
                    mode="lines+markers", name="ₜpₓ(τ)",
                    line=dict(color="#50c878", width=2.5),
                    fill="tozeroy", fillcolor="rgba(80,200,120,0.07)",
                    marker=dict(size=6, color="#50c878"),
                ))
                fig2.update_layout(**layout("Probabilitas Polis Aktif", "Tahun ke-", "Probabilitas (%)"))
                st.plotly_chart(fig2, use_container_width=True)

            # Stacked bar decrement
            df_da = pd.DataFrame(res["asdt"])
            years = df_da["Tahun"].tolist()
            fig3  = go.Figure()
            for col, name, color in [
                ("q(1)","Non-Acc Death","#e74c3c"),
                ("q(2)","Acc Death","#e67e22"),
                ("q(3)","TPD","#3498db"),
                ("q(4)","Lapse","#9b59b6"),
            ]:
                fig3.add_trace(go.Bar(x=years, y=(df_da[col]*1000).tolist(),
                                       name=name, marker_color=color))
            fig3.update_layout(
                **layout("Distribusi Decrement per Tahun (per 1.000 polis)", "Tahun Polis", "per 1.000", h=320),
                barmode="stack",
                legend=dict(orientation="h", y=-0.25, bgcolor="rgba(0,0,0,0)"),
            )
            st.plotly_chart(fig3, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(footer(), unsafe_allow_html=True)
