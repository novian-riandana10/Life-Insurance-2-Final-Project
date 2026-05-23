# 🛡️ Prina Insurance — Website Profesional

Individual 20-Year Endowment Life Insurance with Multiple Decrement

## Struktur
```
prina_web/
├── Home.py                    # Landing page (hero + fitur + benefit + CTA)
├── pages/
│   └── 1_Kalkulator_Premi.py  # Kalkulator aktuaria
├── utils/
│   ├── actuarial.py           # Engine: TMI 2019, UDD 4-dec, iterative solve
│   └── styles.py              # CSS, navbar, footer
├── .streamlit/
│   └── config.toml            # Dark theme config
└── requirements.txt
```

## Run Lokal
```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Deploy ke Streamlit Cloud
1. Upload folder ini ke GitHub
2. [share.streamlit.io](https://share.streamlit.io) → New App
3. Main file: `Home.py`
4. Deploy ✓

## Model Aktuaria
- **Mortalitas**: TMI 2019 (L & P)
- **Decrement**: UDD on each ASDT (4 decrements)
- **Premi**: Gross Premium dengan expense loading (40%/7%) dan profit 15%
- **Cadangan**: Net Premium Prospective Reserve (forward recursion)
- **Validasi**: V₂₀ = SA ✓ (error < 0.0001%)
