# 🚗 UAS Sains Data — Prediksi Harga Mobil

Final Project Matakuliah **Sains Data** — sistem prediksi harga mobil berbasis Linear Regression dengan metode CRISP-DM. Dataset: `Car_sales.csv` (157 baris, 16 kolom).

**Identitas**
- Nama : Fadhil Gani
- NIM  : 237006082
- Prodi: Informatika — Universitas Siliwangi

## 🔗 Demo

- **Aplikasi Web (Streamlit Cloud):** _(akan diisi setelah deploy)_
- **Google Colab Notebook:** _(akan diisi setelah upload ke Drive)_

## 📦 Struktur Project

| File | Deskripsi |
|---|---|
| `Final_Project_Sains_Data_Fadhil_237006082.ipynb` | Notebook utama — 11 langkah CRISP-DM (Load → EDA → Modeling → Evaluasi → Deploy) |
| `app.py` | Streamlit UI sesuai wireframe PDF (form input + card hasil) |
| `model_harga_mobil.pkl` | Pickle berisi model + LabelEncoders + metrik |
| `Car_sales.csv` | Dataset sumber |
| `requirements.txt` | Dependensi untuk Streamlit Cloud |

## 📊 Hasil Model

| Metrik | Nilai |
|---|---|
| R² Score | 0.7952 |
| RMSE | 6.64 ribu USD |
| MAE | 4.26 ribu USD |

Fitur prediksi (10): Manufacturer, Vehicle_type, Engine_size, Horsepower, Wheelbase, Width, Length, Curb_weight, Fuel_capacity, Fuel_efficiency.

## 🚀 Run Lokal

```bash
pip install -r requirements.txt
streamlit run app.py
```

Buka <http://localhost:8501>.

## ☁️ Deploy ke Streamlit Cloud

1. Push repo ini ke GitHub (public).
2. Buka <https://share.streamlit.io> → **New app**.
3. Pilih repo `uas-sains-data-car-price` → Main file: `app.py` → Deploy.
4. URL aplikasi akan tersedia ~2-3 menit kemudian.

## 📁 Dataset

`Car_sales.csv` berisi data penjualan mobil dengan atribut: manufacturer, model, sales, harga, spesifikasi teknis (engine, horsepower, dimensi), dan efisiensi BBM.

---

**🎓 Universitas Siliwangi — Informatika ISI — 2026**
