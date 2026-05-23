# 🛡️ Prina Insurance — Kalkulator Aktuaria

**Individual 20-Year Endowment Life Insurance with Multiple Decrement**

## Fitur
- Perhitungan **Gross Premium** dengan expense loading dan profit target 15%
- **Multiple Decrement Model** (4 decrement): non-acc death, acc death, TPD, withdrawal
- Konversi ASDT → MDT menggunakan **UDD on each ASDT**
- **Forward Recursion Reserve** dengan iterasi konvergensi
- Validasi boundary condition: V₂₀ = SA ✓
- Download tabel cadangan dan decrement sebagai CSV
- Visualisasi interaktif (cadangan, survival probability, distribusi decrement)

## Data Aktuaria
| Sumber | Keterangan |
|---|---|
| **TMI 2019** | Tabel Mortalitas Indonesia 2019 (Laki-laki & Perempuan) |
| **BI Rate** | Input fleksibel (3–10%) |
| **Lapse rate** | 12% (Thn 1–2), 7% (Thn 3–5), 3% (Thn 6+) |

## Model
```
P^g = APV_B / (0.78·ä^(τ) - 0.33)

V[k+1] = ((V[k] + P^g)/v - D_k) / (0.5·q4[k] + p_τ[k])

D_k = q1[k]·SA + q2[k]·2SA + q3[k]·SA
```

## Cara Deploy ke Streamlit Cloud
1. Fork/upload repo ini ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Hubungkan repo → pilih `app.py` sebagai main file
4. Deploy!

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Struktur File
```
prina_insurance/
├── app.py           # Main Streamlit app
├── requirements.txt # Dependencies
└── README.md
```
