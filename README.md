# Prediksi Harga Mobil

Aplikasi web prediksi harga mobil menggunakan Linear Regression. Dibangun sebagai final project matakuliah Sains Data.

**Demo:** [uas-sains-data-car-price.streamlit.app](https://uas-sains-data-car-price.streamlit.app/)

## Cara Menjalankan

```bash
git clone https://github.com/padiil/uas-sains-data-car-price.git
cd uas-sains-data-car-price
pip install -r requirements.txt
streamlit run app.py
```

Buka <http://localhost:8501>.

## Isi Repository

- `app.py` — aplikasi Streamlit
- `Final_Project_Sains_Data_Fadhil_237006082.ipynb` — notebook analisis (CRISP-DM)
- `model_harga_mobil.pkl` — model terlatih + encoder + metadata
- `Car_sales.csv` — dataset (157 baris, 16 kolom)
- `requirements.txt` — daftar dependency

## Dataset

Sumber: data penjualan mobil dengan atribut pabrikan, model, harga, dimensi, spesifikasi mesin, dan efisiensi bahan bakar.

## Model

Linear Regression dengan 10 fitur prediktor. Performa pada data uji:

- R² = 0.7952
- RMSE = 6.64 ribu USD
- MAE = 4.26 ribu USD

## Penyimpanan Model

Model dan seluruh komponen pendukungnya disimpan dalam berkas `model_harga_mobil.pkl` menggunakan `joblib` (wrapper pickle yang dioptimalkan untuk array NumPy). Berkas tersebut berbentuk `dict` Python berisi lima komponen:

| Kunci | Isi |
|---|---|
| `model` | Object `LinearRegression` yang sudah dilatih (intercept dan koefisien tiap fitur) |
| `encoders` | `LabelEncoder` untuk kolom `Manufacturer` dan `Vehicle_type` |
| `fitur` | Daftar 10 nama fitur prediktor (urutan harus dipertahankan saat inference) |
| `metrik` | Nilai RMSE, MAE, dan R-squared hasil evaluasi |
| `feature_defaults` | Nilai rata-rata tiap kolom numerik untuk default form input |

Pendekatan ini memisahkan tahap pelatihan (di notebook) dari tahap prediksi (di aplikasi Streamlit). Aplikasi memuat artefak sekali melalui `joblib.load`, tanpa perlu melatih ulang model maupun membentuk ulang encoder, sehingga waktu respons cepat dan pemetaan kategori konsisten dengan saat pelatihan.

---

Fadhil Gani — 237006082 — Universitas Siliwangi
