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

---

Fadhil Gani — 237006082 — Universitas Siliwangi
