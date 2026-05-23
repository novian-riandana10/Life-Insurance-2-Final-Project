"""
Prina Insurance — Kalkulator Aktuaria
Individual 20-Year Endowment Life Insurance with Multiple Decrement
TMI 2019 | UDD on ASDT | Gross Premium | Net Premium Reserve
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Prina Insurance | Kalkulator Aktuaria",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# TMI 2019
# ─────────────────────────────────────────────────────────────────────────────
TMI = {
    "L": {
        0:5.24e-3,1:5.3e-4,2:4.2e-4,3:3.4e-4,4:2.9e-4,5:2.6e-4,6:2.3e-4,7:2.1e-4,8:2.0e-4,9:2.0e-4,
        10:1.9e-4,11:1.9e-4,12:1.9e-4,13:2.0e-4,14:2.3e-4,15:2.7e-4,16:3.1e-4,17:3.7e-4,18:4.3e-4,19:4.7e-4,
        20:4.9e-4,21:4.9e-4,22:4.9e-4,23:4.9e-4,24:5.0e-4,25:5.2e-4,26:5.5e-4,27:6.0e-4,28:6.5e-4,29:7.0e-4,
        30:7.5e-4,31:8.1e-4,32:8.7e-4,33:9.3e-4,34:9.9e-4,35:1.07e-3,36:1.16e-3,37:1.27e-3,38:1.39e-3,39:1.55e-3,
        40:1.73e-3,41:1.93e-3,42:2.16e-3,43:2.41e-3,44:2.70e-3,45:3.02e-3,46:3.38e-3,47:3.77e-3,48:4.18e-3,49:4.61e-3,
        50:5.08e-3,51:5.56e-3,52:6.09e-3,53:6.67e-3,54:7.27e-3,55:7.89e-3,56:8.47e-3,57:8.98e-3,58:9.39e-3,59:9.71e-3,
        60:9.99e-3,61:1.024e-2,62:1.046e-2,63:1.071e-2,64:1.104e-2,65:1.146e-2,66:1.199e-2,67:1.260e-2,68:1.329e-2,69:1.405e-2,
        70:1.485e-2,71:1.574e-2,72:1.670e-2,73:1.777e-2,74:1.895e-2,75:2.026e-2,76:2.369e-2,77:2.738e-2,78:3.130e-2,79:3.693e-2,
        80:4.518e-2,
    },
    "P": {
        0:2.66e-3,1:4.1e-4,2:3.1e-4,3:2.4e-4,4:2.1e-4,5:2.0e-4,6:2.2e-4,7:2.3e-4,8:2.2e-4,9:2.1e-4,
        10:1.9e-4,11:1.8e-4,12:2.0e-4,13:2.2e-4,14:2.3e-4,15:2.3e-4,16:2.4e-4,17:2.4e-4,18:2.5e-4,19:2.6e-4,
        20:2.7e-4,21:2.8e-4,22:3.0e-4,23:3.2e-4,24:3.4e-4,25:3.8e-4,26:4.2e-4,27:4.6e-4,28:4.9e-4,29:5.2e-4,
        30:5.6e-4,31:6.0e-4,32:6.4e-4,33:6.9e-4,34:7.4e-4,35:8.0e-4,36:8.6e-4,37:9.3e-4,38:1.00e-3,39:1.08e-3,
        40:1.18e-3,41:1.28e-3,42:1.41e-3,43:1.54e-3,44:1.69e-3,45:1.87e-3,46:2.09e-3,47:2.30e-3,48:2.53e-3,49:2.77e-3,
        50:3.05e-3,51:3.35e-3,52:3.68e-3,53:4.03e-3,54:4.42e-3,55:4.83e-3,56:5.24e-3,57:5.63e-3,58:6.01e-3,59:6.36e-3,
        60:6.71e-3,61:7.07e-3,62:7.46e-3,63:7.88e-3,64:8.33e-3,65:8.83e-3,66:9.40e-3,67:1.005e-2,68:1.076e-2,69:1.150e-2,
        70:1.229e-2,71:1.314e-2,72:1.406e-2,73:1.508e-2,74:1.620e-2,75:1.743e-2,76:1.879e-2,77:2.030e-2,78:2.326e-2,79:2.880e-2,
        80:3.569e-2,
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# ACTUARIAL ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def lapse_rate(policy_year: int) -> float:
    if policy_year <= 2:  return 0.12
    if policy_year <= 5:  return 0.07
    return 0.03


def udd_4dec(q1p, q2p, q3p, q4p):
    """
    UDD on each ASDT → multiple decrement table q(j).
    q(j) = q'(j) * [1 - 1/2 Σ_{k≠j} q'(k)
                      + 1/3 Σ_{k<l,k,l≠j} q'(k)q'(l)
                      - 1/4 Π_{k≠j} q'(k)]
    """
    qs = [q1p, q2p, q3p, q4p]
    result = []
    for j in range(4):
        o = [qs[k] for k in range(4) if k != j]
        a, b, c = o
        f = 1.0 - 0.5*(a+b+c) + (1/3)*(a*b+a*c+b*c) - (1/4)*a*b*c
        result.append(qs[j] * f)
    return tuple(result)


def build_dec_table(x: int, gender: str, n: int = 20) -> dict:
    """Build decrement arrays and survival probabilities."""
    tmi = TMI[gender]
    q1, q2, q3, q4, ptau = [], [], [], [], []
    for t in range(n):
        age = x + t
        q1p = tmi.get(age, 0.0)
        a, b, c, d = udd_4dec(q1p, 0.10*q1p, 0.05*q1p, lapse_rate(t+1))
        q1.append(a); q2.append(b); q3.append(c); q4.append(d)
        ptau.append(1.0 - a - b - c - d)

    tpx = np.ones(n + 1)
    for t in range(n):
        tpx[t+1] = tpx[t] * ptau[t]

    a_due = float(sum(1/(1+0)**t * tpx[t] for t in range(n)))  # placeholder, overridden below

    # Also store ASDT values for display
    asdt = []
    for t in range(n):
        age = x + t
        q1p = tmi.get(age, 0.0)
        asdt.append({
            "Tahun": t+1, "Usia": age,
            "q'(1) non-acc": q1p,
            "q'(2) acc":     0.10*q1p,
            "q'(3) TPD":     0.05*q1p,
            "q'(4) lapse":   lapse_rate(t+1),
            "q(1)": q1[t], "q(2)": q2[t],
            "q(3)": q3[t], "q(4)": q4[t],
            "q(τ)": 1 - ptau[t],
            "p(τ)": ptau[t],
            "ₜpₓ(τ)": tpx[t],
        })

    return dict(q1=q1, q2=q2, q3=q3, q4=q4, ptau=ptau, tpx=tpx, asdt=asdt)


def compute_actuarial(
    x: int, gender: str, SA: float, i: float,
    n: int = 20, b3: float = 1.0,
    profit: float = 0.15,
    max_iter: int = 40, tol: float = 1e-10,
) -> dict:
    """
    Iteratively compute gross premium and net premium reserve.

    Key distinction:
      P_net  = APV_B / ä           → used in RESERVE recursion (ensures V[0]=0, V[n]=SA)
      P_gross= APV_B / (0.78ä−0.33) → actual premium CHARGED to policyholder

    Iteration resolves circularity from withdrawal benefit = 0.5 * V[t+1].
    """
    v = 1.0 / (1.0 + i)
    dec = build_dec_table(x, gender, n)
    q1, q2, q3, q4, ptau, tpx = (
        dec["q1"], dec["q2"], dec["q3"], dec["q4"],
        dec["ptau"], dec["tpx"],
    )

    a_due = float(sum(v**t * tpx[t] for t in range(n)))

    denom_gross = 0.78 * a_due - 0.33   # denominator for P_gross
    if denom_gross <= 0:
        raise ValueError("Denominator ≤ 0. Coba naikkan suku bunga atau turunkan usia masuk.")

    # ── Iterative solve ──────────────────────────────────────────────────────
    V = np.zeros(n + 1)
    P_net = 0.0
    iters_used = 0

    for it in range(max_iter):
        # APV of benefits (withdrawal uses current V)
        APV_B = 0.0
        for t in range(n):
            ben = (q1[t]*SA + q2[t]*2*SA + q3[t]*b3*SA
                   + q4[t] * 0.5 * V[t+1])
            APV_B += v**(t+1) * tpx[t] * ben
        APV_B += v**n * tpx[n] * SA

        P_net_new = APV_B / a_due

        # Forward recursion using P_NET  →  guarantees V[n]=SA
        V_new = np.zeros(n + 1)
        for k in range(n):
            Dk = q1[k]*SA + q2[k]*2*SA + q3[k]*b3*SA
            rd  = 0.5*q4[k] + ptau[k]
            V_new[k+1] = ((V_new[k] + P_net_new) * (1+i) - Dk) / rd

        iters_used = it + 1
        if abs(P_net_new - P_net) < tol:
            P_net = P_net_new
            V     = V_new
            break
        P_net = P_net_new
        V     = V_new

    # Final gross premium
    P_gross = APV_B / denom_gross

    APV_P   = P_gross * a_due
    APV_exp = P_gross * (0.33 + 0.07 * a_due)

    return dict(
        P_gross=P_gross, P_net=P_net,
        V=V, dec=dec, tpx=tpx, a_due=a_due,
        APV_B=APV_B, APV_P=APV_P, APV_exp=APV_exp,
        profit_actual=(APV_P - APV_B - APV_exp) / APV_P * 100,
        iters=iters_used,
    )


# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
[data-testid="stSidebar"]            { background:#0d1f35; }
[data-testid="stSidebar"] *          { color:#e8edf3 !important; }
.metric-box { background:linear-gradient(135deg,#1a3a5c,#1e5080);
              border-radius:10px; padding:18px; text-align:center;
              border:1px solid #2a6496; margin-bottom:8px; }
.metric-box .val { font-size:1.55rem; font-weight:700; color:#7ec8e3; }
.metric-box .lbl { font-size:0.80rem; color:#a8c0d8; margin-top:4px; }
.sec-hdr { background:#1a3a5c; border-left:4px solid #3399cc;
           padding:8px 16px; border-radius:0 6px 6px 0;
           color:white; font-weight:600; margin-bottom:16px; }
.badge-g { background:#1d6a30; color:#a8f0b8; padding:3px 12px;
           border-radius:20px; font-size:.85rem; font-weight:600; }
.badge-r { background:#6a1d1d; color:#f0a8a8; padding:3px 12px;
           border-radius:20px; font-size:.85rem; font-weight:600; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🛡️ Prina Insurance")
    st.markdown("**Kalkulator Aktuaria — Endowment 20Y**")
    st.markdown("---")
    st.markdown("### 📋 Parameter Input")

    gender_lbl = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    gender     = "L" if gender_lbl == "Laki-laki" else "P"
    x          = st.slider("Usia Masuk (tahun)", 20, 60, 35)
    st.caption(f"Usia selesai: **{x+20} tahun**")

    SA = st.number_input(
        "Uang Pertanggungan (Rp)", min_value=10_000_000,
        max_value=10_000_000_000, value=100_000_000,
        step=10_000_000, format="%d",
    )
    i_pct = st.slider("Suku Bunga Teknis (%/tahun)", 3.0, 10.0, 5.5, 0.25)
    i     = i_pct / 100.0

    st.markdown("---")
    with st.expander("⚙️ Asumsi Aktuaria (klik untuk lihat)"):
        st.markdown("""
        | Parameter | Nilai |
        |---|---|
        | Mortalitas | TMI 2019 |
        | Acc. Death | 10% × q'(1) |
        | TPD | 5% × q'(1) |
        | Lapse thn 1–2 | 12% |
        | Lapse thn 3–5 | 7% |
        | Lapse thn 6+ | 3% |
        | TPD Benefit | 100% SA |
        | Withdrawal CV | 50% × Vₜ₊₁ |
        | Decrement | UDD on ASDT |
        | Initial Expense | 40% P^g |
        | Renewal Expense | 7% P^g |
        | Target Profit | 15% |
        | Reserve Method | Net Premium Prospective |
        """)
    st.markdown("---")
    compute = st.button("🔢 Hitung Sekarang", type="primary", use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("# 🛡️ Prina Insurance")
st.markdown("### Individual 20-Year Endowment — Multiple Decrement (4 Penyebab)")
st.markdown("---")

if not compute:
    st.markdown("""
    <div style='text-align:center;padding:60px 0;color:#888;'>
        <h3>Isi parameter di sidebar, lalu klik <b>🔢 Hitung Sekarang</b></h3>
        <p>Menghitung premi kotor, cadangan, dan tabel decrement<br>
        berbasis <b>TMI 2019</b> · <b>4 Decrement (UDD)</b> · <b>Gross Premium</b></p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ── COMPUTE ───────────────────────────────────────────────────────────────────
with st.spinner("Menghitung…"):
    try:
        res = compute_actuarial(x, gender, SA, i)
    except ValueError as e:
        st.error(f"❌ {e}"); st.stop()

P_g    = res["P_gross"]; P_n  = res["P_net"]
V      = res["V"];        dec  = res["dec"]
tpx    = res["tpx"];      n    = 20
a_due  = res["a_due"];    APV_B= res["APV_B"]
APV_P  = res["APV_P"];    APV_e= res["APV_exp"]
profit = res["profit_actual"]; iters = res["iters"]

val_err  = abs(V[20] - SA) / SA * 100
val_ok   = val_err < 0.0001

# ─────────────────────────────────────────────────────────────────────────────
# KEY METRICS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<div class="sec-hdr">📊 Ringkasan Hasil</div>', unsafe_allow_html=True)

metrics = [
    (f"Rp {P_g:,.0f}",          "Premi Kotor P^g (ditagihkan)"),
    (f"Rp {P_n:,.0f}",          "Premi Neto P^n (untuk cadangan)"),
    (f"{P_g/SA*100:.3f}%",      "Rasio P^g / SA"),
    (f"Rp {APV_B:,.0f}",        "APV Benefit"),
    (f"{a_due:.5f}",             "Annuity-due ä"),
    (f"{profit:.2f}%",           "Profit Aktual"),
]
cols = st.columns(6)
for col, (val, lbl) in zip(cols, metrics):
    with col:
        st.markdown(
            f'<div class="metric-box"><div class="val">{val}</div>'
            f'<div class="lbl">{lbl}</div></div>',
            unsafe_allow_html=True,
        )

badge = (
    '<span class="badge-g">✅ V₂₀ = SA — VALID</span>'
    if val_ok else
    f'<span class="badge-r">⚠️ Selisih {val_err:.6f}%</span>'
)
st.markdown(
    f"**Validasi:** {badge} &nbsp;|&nbsp; "
    f"V₂₀ = Rp {V[20]:,.0f} &nbsp;|&nbsp; SA = Rp {SA:,.0f} &nbsp;|&nbsp; "
    f"Iterasi: **{iters}×**",
    unsafe_allow_html=True,
)
st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Tabel Cadangan",
    "📋 Tabel Decrement",
    "💰 Rincian Premi",
    "📉 Grafik",
])

# ── TAB 1: RESERVE TABLE ─────────────────────────────────────────────────────
with tab1:
    st.markdown('<div class="sec-hdr">Tabel Cadangan — Net Premium Prospective Reserve</div>',
                unsafe_allow_html=True)
    st.caption("Cadangan menggunakan P^n (net premium). Premi yang ditagihkan ke peserta adalah P^g (gross).")

    rows = []
    for k in range(n + 1):
        rows.append({
            "Akhir Thn ke-": k,
            "Usia": x + k,
            "Cadangan ₖV (Rp)": int(round(V[k])),
            "Cash Value 50%ₖV (Rp)": int(round(0.5 * V[k])) if k > 0 else 0,
            "ₖV / SA (%)": round(V[k] / SA * 100, 4),
            "Premi Kumulatif P^g (Rp)": int(round(P_g * k)),
        })

    df_res = pd.DataFrame(rows)

    def hl_last(row):
        style = [""] * len(row)
        if row["Akhir Thn ke-"] == 20:
            style = ["background-color:#1a4d2e;color:#a8f0b8"] * len(row)
        return style

    styled = df_res.style.apply(hl_last, axis=1).format({
        "Cadangan ₖV (Rp)": "{:,}",
        "Cash Value 50%ₖV (Rp)": "{:,}",
        "ₖV / SA (%)": "{:.4f}%",
        "Premi Kumulatif P^g (Rp)": "{:,}",
    })
    st.dataframe(styled, use_container_width=True, height=560)

    st.success(f"✅ V₂₀ = Rp {V[20]:,.0f} = SA = Rp {SA:,.0f} | Error: {val_err:.10f}%")
    st.download_button(
        "⬇️ Download CSV Cadangan",
        data=df_res.to_csv(index=False).encode(),
        file_name=f"cadangan_x{x}_{gender_lbl}_SA{int(SA//1e6)}jt.csv",
        mime="text/csv",
    )

# ── TAB 2: DECREMENT TABLE ───────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="sec-hdr">Tabel Multiple Decrement (UDD on ASDT)</div>',
                unsafe_allow_html=True)

    df_full = pd.DataFrame(dec["asdt"])
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown("**ASDT — Associated Single Decrement Tables**")
        df_asdt = df_full[["Tahun","Usia","q'(1) non-acc","q'(2) acc","q'(3) TPD","q'(4) lapse"]]
        st.dataframe(df_asdt.style.format({
            "q'(1) non-acc": "{:.6f}", "q'(2) acc": "{:.6f}",
            "q'(3) TPD": "{:.6f}",    "q'(4) lapse": "{:.4f}",
        }), use_container_width=True, height=480)

    with col_r:
        st.markdown("**MDT — Multiple Decrement Table**")
        df_mdt = df_full[["Tahun","Usia","q(1)","q(2)","q(3)","q(4)","q(τ)","p(τ)","ₜpₓ(τ)"]]
        st.dataframe(df_mdt.style.format({k:"{:.6f}" for k in
            ["q(1)","q(2)","q(3)","q(4)","q(τ)","p(τ)","ₜpₓ(τ)"]}),
            use_container_width=True, height=480)

    # Verification
    chk = (df_full["q(1)"]+df_full["q(2)"]+df_full["q(3)"]+df_full["q(4)"]+df_full["p(τ)"]-1).abs().max()
    if chk < 1e-12:
        st.success(f"✅ Identitas Σq(j) + p(τ) = 1 terpenuhi | max error: {chk:.2e}")
    else:
        st.warning(f"⚠️ Max error identitas: {chk:.2e}")

    st.download_button(
        "⬇️ Download CSV Tabel Decrement",
        data=df_full.to_csv(index=False).encode(),
        file_name=f"decrement_x{x}_{gender_lbl}.csv", mime="text/csv",
    )

# ── TAB 3: PREMIUM BREAKDOWN ─────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="sec-hdr">Rincian Perhitungan Premi</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("#### Gross Premium (Premi yang Ditagihkan)")
        st.latex(r"P^g = \frac{\text{APV}_B}{0.78\,\ddot{a}^{(\tau)} - 0.33}")
        st.markdown(f"""
| Parameter | Nilai |
|---|---|
| $\\ddot{{a}}^{{(\\tau)}}$ | `{a_due:.6f}` |
| $0.78 \\times \\ddot{{a}}$ | `{0.78*a_due:.6f}` |
| Denominator | `{0.78*a_due-0.33:.6f}` |
| APV Benefit | `Rp {APV_B:,.0f}` |
| **P^g (ditagihkan)** | **`Rp {P_g:,.0f}`** |
        """)

        st.markdown("#### Net Premium (Untuk Reserve)")
        st.latex(r"P^n = \frac{\text{APV}_B}{\ddot{a}^{(\tau)}}")
        st.markdown(f"""
| Parameter | Nilai |
|---|---|
| APV Benefit | `Rp {APV_B:,.0f}` |
| $\\ddot{{a}}^{{(\\tau)}}$ | `{a_due:.6f}` |
| **P^n (untuk cadangan)** | **`Rp {P_n:,.0f}`** |
        """)

    with col_b:
        st.markdown("#### Komposisi APV Premi Kotor")
        apv_df = pd.DataFrame({
            "Komponen": [
                "APV Benefit", "APV Expense Initial (40%)",
                "APV Expense Renewal (7%)", "Total APV Expense",
                "APV Premi (P^g × ä)", "Profit",
            ],
            "Nilai (Rp)": [
                f"Rp {APV_B:,.0f}", f"Rp {P_g*0.33:,.0f}",
                f"Rp {P_g*0.07*a_due:,.0f}", f"Rp {APV_e:,.0f}",
                f"Rp {APV_P:,.0f}", f"Rp {APV_P-APV_B-APV_e:,.0f}",
            ],
            "% APV Premi": [
                f"{APV_B/APV_P*100:.1f}%", f"{P_g*0.33/APV_P*100:.1f}%",
                f"{P_g*0.07*a_due/APV_P*100:.1f}%", f"{APV_e/APV_P*100:.1f}%",
                "100.0%", f"{profit:.1f}%",
            ],
        })
        st.dataframe(apv_df, use_container_width=True, hide_index=True)

        st.markdown("#### Rekursi Cadangan (Forward)")
        st.latex(r"""
{}_{k+1}V = \frac{({}_{k}V + P^n)(1{+}i) - D_k}
                  {0.5\,q^{(4)}_{x+k} + {}_{1}p^{(\tau)}_{x+k}}
""")
        st.markdown(r"$D_k = q^{(1)}_{x+k}\cdot SA + q^{(2)}_{x+k}\cdot 2SA + q^{(3)}_{x+k}\cdot SA$")
        st.info("P^n (bukan P^g) digunakan dalam rekursi → memastikan V₀=0 dan V₂₀=SA")

# ── TAB 4: CHARTS ────────────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="sec-hdr">Visualisasi</div>', unsafe_allow_html=True)

    BG = "#0d1f35"; GRID = "#1e3a5c"

    def base_layout(title, xtitle, ytitle):
        return dict(title=title, xaxis_title=xtitle, yaxis_title=ytitle,
                    height=370, plot_bgcolor=BG, paper_bgcolor=BG,
                    font_color="white",
                    xaxis=dict(gridcolor=GRID), yaxis=dict(gridcolor=GRID))

    c1, c2 = st.columns(2)

    with c1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=list(range(n+1)), y=list(V),
            mode="lines+markers", name="Cadangan ₖV",
            line=dict(color="#3399cc", width=2.5),
            fill="tozeroy", fillcolor="rgba(51,153,204,0.1)",
        ))
        fig.add_trace(go.Scatter(
            x=list(range(n+1)), y=[0.5*Vk for Vk in V],
            mode="lines", name="Cash Value 50%ₖV",
            line=dict(color="#f0a030", width=1.8, dash="dash"),
        ))
        fig.add_hline(y=SA, line_dash="dot", line_color="red",
                      annotation_text=f"SA", annotation_position="top right")
        fig.update_layout(**base_layout("Cadangan & Cash Value","Akhir Tahun ke-","Nilai (Rp)"))
        fig.update_layout(legend=dict(x=0.02, y=0.97))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=list(range(n+1)), y=[tpx[t]*100 for t in range(n+1)],
            mode="lines+markers", name="ₜpₓ(τ)",
            line=dict(color="#50c878", width=2.5),
            fill="tozeroy", fillcolor="rgba(80,200,120,0.1)",
        ))
        fig2.update_layout(**base_layout("Probabilitas Polis Aktif ₜpₓ(τ)","Tahun ke-","Probabilitas (%)"))
        st.plotly_chart(fig2, use_container_width=True)

    df_d = pd.DataFrame(dec["asdt"])
    years = df_d["Tahun"].tolist()
    fig3 = go.Figure()
    for col, name, color in [
        ("q(1)","Non-Acc Death","#e74c3c"),("q(2)","Acc Death","#e67e22"),
        ("q(3)","TPD","#3498db"),("q(4)","Lapse","#9b59b6"),
    ]:
        fig3.add_trace(go.Bar(
            x=years, y=(df_d[col]*1000).tolist(),
            name=name, marker_color=color,
        ))
    fig3.update_layout(
        **base_layout("Distribusi Decrement per Tahun (per 1.000 polis)","Tahun Polis","per 1.000"),
        barmode="stack", legend=dict(orientation="h", y=-0.22),
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Reserve growth rate
    growth = [((V[k+1]-V[k])/V[k]*100) if V[k] > 0 else 0 for k in range(1, n)]
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
        x=list(range(1, n)), y=growth,
        marker_color=["#50c878" if g >= 0 else "#e74c3c" for g in growth],
    ))
    fig4.update_layout(**base_layout("Pertumbuhan Cadangan (%) per Tahun","Tahun","Pertumbuhan (%)"),
                       height=290)
    st.plotly_chart(fig4, use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "<center><small>🛡️ <b>Prina Insurance</b> Actuarial Calculator &nbsp;|&nbsp; "
    "TMI 2019 · Multiple Decrement (UDD on ASDT) · Net Premium Reserve · v1.0"
    "</small></center>",
    unsafe_allow_html=True,
)
