# 🧠 CounselingQ — Counseling Queue Simulation Dashboard

> Dynamic discrete-event simulation for student counseling queues with CBT-based stress reduction and Monte Carlo analysis.

---

## 📋 Deskripsi

**CounselingQ** adalah aplikasi simulasi antrian layanan konseling mahasiswa berbasis **Streamlit**. Aplikasi ini mensimulasikan proses kedatangan mahasiswa, layanan konseling dengan pendekatan **Cognitive Behavioral Therapy (CBT)**, dan menganalisis performa antrian secara statistik menggunakan **simulasi Monte Carlo**.

Cocok digunakan untuk penelitian, tugas akhir, atau analisis kebijakan layanan konseling di institusi pendidikan.

---

## ✨ Fitur Utama

| Fitur | Keterangan |
|---|---|
| 🎲 **Simulasi Antrian** | Model *discrete-event* dengan multiple counselors |
| 🧘 **CBT Stress Reduction** | Hitung penurunan stres mahasiswa berdasarkan resiliensi |
| 📊 **Visualisasi Interaktif** | Chart Plotly: stress, waiting time, workload, distribusi |
| 🎰 **Monte Carlo** | Hingga 500 iterasi untuk analisis distribusi probabilistik |
| 📥 **Upload CSV** | Import dataset sendiri, validasi kolom otomatis |
| 💾 **Export** | Download hasil simulasi sebagai CSV dan PDF |
| 🤖 **AI Recommendation** | Rekomendasi otomatis jumlah konselor optimal |
| 🔐 **Login System** | Autentikasi sederhana sebelum akses dashboard |
| 👥 **Support 2.000 Siswa** | Optimasi performa menggunakan NumPy vectorized operations |

---

## 🚀 Instalasi & Menjalankan

### 1. Clone / Download

```bash
# Jika menggunakan git
git clone https://github.com/mukhamadsofyan/Pemodelan-Simulasi-Data.git
cd counselingq

# Atau letakkan file counseling_simulation.py di folder kerja
```

### 2. Install Dependensi

```bash
pip install streamlit fpdf2 plotly pandas numpy
```

### 3. Jalankan Aplikasi

```bash
streamlit run counseling_simulation.py
```

Buka browser dan akses: **http://localhost:8501**

---

## 🔐 Login

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `12345` |

---

## ⚙️ Parameter Simulasi

Semua parameter dikonfigurasi melalui **sidebar** di sebelah kiri:

| Parameter | Range | Default | Keterangan |
|---|---|---|---|
| **Number of Students** | 10 – 2000 | 50 | Jumlah mahasiswa yang disimulasikan |
| **CBT Effectiveness** | 0.10 – 1.00 | 0.50 | Kekuatan efek CBT dalam menurunkan stres |
| **Counselors** | 1 – 20 | 1 | Jumlah konselor yang aktif melayani |
| **Monte Carlo Runs** | 10 – 500 | 100 | Jumlah iterasi simulasi Monte Carlo |

---

## 📂 Format CSV Upload

Jika ingin menggunakan dataset sendiri, upload file `.csv` dengan kolom berikut:

```csv
Student,Interarrival Time,Stress Before CBT,Resilience
1,25,0.82,0.34
2,40,0.67,0.51
...
```

| Kolom | Tipe | Keterangan |
|---|---|---|
| `Student` | Integer | Nomor urut mahasiswa (1, 2, 3, …) |
| `Interarrival Time` | Integer | Selisih waktu kedatangan antar mahasiswa (menit) |
| `Stress Before CBT` | Float (0–1) | Tingkat stres awal mahasiswa |
| `Resilience` | Float (0–1) | Tingkat resiliensi mahasiswa |

> ⚠️ Kolom yang tidak sesuai akan memunculkan pesan error dan simulasi tidak akan berjalan.

---

## 📐 Model Matematis

### Waktu Layanan

Durasi sesi konseling dihitung berdasarkan tingkat stres mahasiswa:

```
Service Time = 20 + (Stress Before CBT × 35)  [menit]
```

### Reduksi Stres CBT

```
Stress After CBT = max(0, Stress Before CBT − (Resilience × CBT Power))
```

### Aturan Antrian

- Disiplin antrian: **FCFS** (First Come, First Served)
- Penjadwalan: konselor dengan **waktu tersedia paling awal** dipilih terlebih dahulu
- Jam operasional dimulai pukul **08:00**

---

## 📊 Output & Visualisasi

### Metrik KPI (8 kartu)

- Average Waiting Time
- Average Service Time
- Probability of Waiting (P(W > 0))
- Max Waiting Time
- Average Stress Before CBT
- Average Stress After CBT
- Average Stress Reduction
- Jumlah Konselor Aktif

### Chart Interaktif

| Chart | Deskripsi |
|---|---|
| **Stress Before & After CBT** | Line chart perbandingan tingkat stres per mahasiswa |
| **Waiting Time per Student** | Bar chart dengan colorscale dinamis |
| **Counselor Workload** | Total service time per konselor |
| **Stress Reduction Distribution** | Histogram penyebaran penurunan stres |
| **Monte Carlo Distribution** | Histogram rata-rata waiting time dari 10–500 iterasi |
| **Service vs Wait Scatter** | Scatter plot korelasi service time dan waiting time |

### Tabel Data

Tersedia dalam tiga tab:

1. **Input Dataset** — data mentah (generate atau upload)
2. **Simulation Result** — hasil lengkap per mahasiswa
3. **Summary** — ringkasan statistik simulasi

---

## 💾 Export

| Format | Isi | Tombol |
|---|---|---|
| **CSV** | Seluruh hasil simulasi (12 kolom) | *Download Result CSV* |
| **PDF** | Ringkasan KPI + rekomendasi AI | *Download Summary PDF* |

Nama file otomatis menyertakan timestamp, contoh:
```
counseling_simulation_20250523_1430.csv
counseling_report_20250523_1430.pdf
```

---

## 🤖 Rekomendasi AI

Sistem memberikan rekomendasi otomatis berdasarkan kondisi antrian:

| Kondisi | Status | Rekomendasi |
|---|---|---|
| `Avg Wait > 20 min` **atau** `P(Wait) > 60%` | ⚠️ Overloaded | Tambah konselor (`n + 1`) |
| `Avg Wait < 5 min` **dan** `P(Wait) < 30%` | ✅ Efficient | Staffing saat ini sudah optimal |
| Selain kondisi di atas | ℹ️ Moderate | Monitor pada jam sibuk |

---

## 🗂️ Struktur File

```
counselingq/
│
├── counseling_simulation.py   # Aplikasi utama Streamlit
├── README.md                  # Dokumentasi ini
└── sample_dataset.csv         # (Opsional) Contoh dataset
```

---

## 🛠️ Teknologi

| Library | Versi | Kegunaan |
|---|---|---|
| `streamlit` | ≥ 1.30 | Framework web app |
| `pandas` | ≥ 2.0 | Manipulasi data |
| `numpy` | ≥ 1.24 | Komputasi numerik / vectorized ops |
| `plotly` | ≥ 5.18 | Visualisasi interaktif |
| `fpdf2` | ≥ 2.7 | Generate PDF |

---

## 📌 Catatan Performa

- Dataset **≤ 200 siswa**: animasi progress real-time per mahasiswa
- Dataset **> 200 siswa**: progress di-batch otomatis agar tidak lambat
- Monte Carlo dikap **200 siswa/iterasi** untuk menjaga kecepatan; notifikasi ditampilkan jika dataset utama lebih besar

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik dan penelitian. Bebas dimodifikasi dan dikembangkan lebih lanjut dengan menyertakan atribusi.

---

<div align="center">
  Dibuat Oleh Mukhamad Sofyan 
</div>
