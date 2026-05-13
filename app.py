"""Streamlit UI — Prediksi Harga Mobil.

Final Project Sains Data — Fadhil Gani (237006082).
Run lokal: streamlit run app.py
"""
from __future__ import annotations

import joblib
import pandas as pd
import streamlit as st

# ──────────────────────────── Page config ────────────────────────────
st.set_page_config(
    page_title="Prediksi Harga Mobil",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────── Custom CSS ────────────────────────────
st.markdown(
    """
    <style>
    .main { background-color: #FFFFFF; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1100px; }

    h1.judul-utama {
        font-family: 'Courier New', monospace;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #1a1a1a;
    }
    h2.section-title {
        font-family: 'Courier New', monospace;
        font-size: 18px;
        font-weight: bold;
        color: #1a1a1a;
        margin: 0.5rem 0;
    }
    .card-form {
        border: 2px solid #1a1a1a;
        border-radius: 12px;
        padding: 1.5rem;
        background: #FFFFFF;
    }
    .card-hasil {
        border: 2px solid #1a1a1a;
        border-radius: 12px;
        padding: 1.5rem;
        background: #FFFFFF;
        margin-bottom: 1rem;
    }
    .card-harga {
        background: #FFE680;
        border: 2px solid #1a1a1a;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.8rem 0;
    }
    .card-identitas {
        background: #B3D9FF;
        border: 2px solid #1a1a1a;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        line-height: 1.7;
    }
    .harga-besar {
        font-family: 'Courier New', monospace;
        font-size: 38px;
        font-weight: bold;
        color: #1a1a1a;
    }
    .ringkasan-row {
        font-family: 'Courier New', monospace;
        font-size: 14px;
        color: #1a1a1a;
        margin: 4px 0;
    }
    div.stButton > button {
        background: #7FE07F;
        color: #1a1a1a;
        font-family: 'Courier New', monospace;
        font-size: 16px;
        font-weight: bold;
        border: 2px solid #1a1a1a;
        border-radius: 12px;
        padding: 0.5rem 1.5rem;
        width: 100%;
    }
    div.stButton > button:hover {
        background: #5CC95C;
        color: #1a1a1a;
        border-color: #1a1a1a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────── Load model ────────────────────────────
@st.cache_resource
def load_artefak():
    return joblib.load("model_harga_mobil.pkl")


artefak = load_artefak()
model = artefak["model"]
encoders = artefak["encoders"]
fitur = artefak["fitur"]
metrik = artefak["metrik"]
defaults = artefak["feature_defaults"]

manufacturers = sorted(encoders["Manufacturer"].classes_.tolist())
vehicle_types = sorted(encoders["Vehicle_type"].classes_.tolist())


# ──────────────────────────── Layout ────────────────────────────
st.markdown('<h1 class="judul-utama">🚗 PREDIKSI HARGA MOBIL</h1>', unsafe_allow_html=True)

col_kiri, col_kanan = st.columns([1, 1], gap="large")

# ─── Kolom Kiri: Form Input ───
with col_kiri:
    st.markdown('<h2 class="section-title">PREDIKSI HARGA MOBIL:</h2>', unsafe_allow_html=True)

    with st.container():
        manufacturer = st.selectbox(
            "VARIABLE 1 : Manufacturer",
            options=manufacturers,
            index=manufacturers.index("Toyota") if "Toyota" in manufacturers else 0,
        )

        vehicle_type = st.selectbox(
            "VARIABLE 2 : Vehicle Type",
            options=vehicle_types,
            index=vehicle_types.index("Passenger") if "Passenger" in vehicle_types else 0,
        )

        engine_size = st.number_input(
            "VARIABLE 3 : Engine Size (liter)",
            min_value=0.5, max_value=10.0,
            value=float(defaults["Engine_size"]), step=0.1, format="%.1f",
        )

        horsepower = st.number_input(
            "VARIABLE 4 : Horsepower (HP)",
            min_value=40, max_value=600,
            value=int(defaults["Horsepower"]), step=5,
        )

        wheelbase = st.number_input(
            "VARIABLE 5 : Wheelbase (inci)",
            min_value=80.0, max_value=140.0,
            value=float(defaults["Wheelbase"]), step=0.5, format="%.1f",
        )

        width = st.number_input(
            "VARIABLE 6 : Width (inci)",
            min_value=55.0, max_value=85.0,
            value=float(defaults["Width"]), step=0.5, format="%.1f",
        )

        length = st.number_input(
            "VARIABLE 7 : Length (inci)",
            min_value=140.0, max_value=240.0,
            value=float(defaults["Length"]), step=0.5, format="%.1f",
        )

        curb_weight = st.number_input(
            "VARIABLE 8 : Curb Weight (×1000 lbs)",
            min_value=1.0, max_value=7.0,
            value=float(defaults["Curb_weight"]), step=0.05, format="%.3f",
        )

        fuel_capacity = st.number_input(
            "VARIABLE 9 : Fuel Capacity (galon)",
            min_value=5.0, max_value=40.0,
            value=float(defaults["Fuel_capacity"]), step=0.5, format="%.1f",
        )

        fuel_efficiency = st.number_input(
            "VARIABLE 10 : Fuel Efficiency (MPG)",
            min_value=10, max_value=60,
            value=int(defaults["Fuel_efficiency"]), step=1,
        )

        prediksi = st.button("Hitung Harga Mobil 🧮")

# ─── Kolom Kanan: Hasil + Identitas ───
with col_kanan:
    st.markdown('<h2 class="section-title">PERKIRAAN HARGA MOBIL</h2>', unsafe_allow_html=True)

    if prediksi:
        input_df = pd.DataFrame(
            [
                {
                    "Manufacturer": manufacturer,
                    "Vehicle_type": vehicle_type,
                    "Engine_size": engine_size,
                    "Horsepower": horsepower,
                    "Wheelbase": wheelbase,
                    "Width": width,
                    "Length": length,
                    "Curb_weight": curb_weight,
                    "Fuel_capacity": fuel_capacity,
                    "Fuel_efficiency": fuel_efficiency,
                }
            ]
        )

        encoded = input_df.copy()
        for col in ["Manufacturer", "Vehicle_type"]:
            encoded[col] = encoders[col].transform(encoded[col].astype(str))

        encoded = encoded[fitur]
        harga_ribu = float(model.predict(encoded)[0])
        harga_usd = max(harga_ribu * 1000, 0)

        st.markdown(
            f"""
            <div class="card-harga">
                <div class="harga-besar">${harga_usd:,.0f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        ringkasan_items = [
            ("Manufacturer", manufacturer),
            ("Vehicle Type", vehicle_type),
            ("Engine Size", f"{engine_size:.1f} L"),
            ("Horsepower", f"{horsepower} HP"),
            ("Wheelbase", f"{wheelbase:.1f} in"),
            ("Width", f"{width:.1f} in"),
            ("Length", f"{length:.1f} in"),
            ("Curb Weight", f"{curb_weight:.3f} ×1000 lbs"),
            ("Fuel Capacity", f"{fuel_capacity:.1f} gal"),
            ("Fuel Efficiency", f"{fuel_efficiency} MPG"),
        ]
        baris_html = "".join(
            f'<div class="ringkasan-row"><b>{k}</b> : {v}</div>' for k, v in ringkasan_items
        )
        st.markdown(
            f"""
            <div class="card-hasil">
                {baris_html}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="card-harga">
                <div class="harga-besar">$ —</div>
                <div style="font-family: 'Courier New', monospace; font-size: 13px; margin-top: 8px;">
                    Isi form & tekan tombol "Hitung Harga Mobil"
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="card-hasil">
                <div class="ringkasan-row">📊 <b>Model</b>: Linear Regression</div>
                <div class="ringkasan-row">📈 <b>R² Score</b>: {metrik['r2']:.4f}</div>
                <div class="ringkasan-row">📉 <b>RMSE</b>: {metrik['rmse']:.2f} ribu USD</div>
                <div class="ringkasan-row">📊 <b>MAE</b>: {metrik['mae']:.2f} ribu USD</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="card-identitas">
            <b>SISTEM INI DIBUAT OLEH:</b><br>
            NAMA : Fadhil Gani<br>
            NPM  : 237006082<br>
            Informatika — Universitas Siliwangi
        </div>
        """,
        unsafe_allow_html=True,
    )
