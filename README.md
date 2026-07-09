# 🎓 Simulasi Antrian Layanan Konseling Mahasiswa

**Agent Based Modeling (ABM) untuk Analisis Waktu Tunggu dan Efisiensi Sistem**

Aplikasi web interaktif berbasis **Streamlit** yang mensimulasikan sistem antrian layanan konseling mahasiswa menggunakan pendekatan **Agent Based Modeling**. Aplikasi ini memodelkan mahasiswa dan konselor sebagai *agent* otonom yang saling berinteraksi dalam sebuah *environment* antrian, lengkap dengan analisis statistik, validasi teori antrian klasik (Erlang-C), dan simulasi Monte Carlo.

---

## 📋 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Konsep Agent Based Modeling](#-konsep-agent-based-modeling)
- [Struktur Aplikasi](#-struktur-aplikasi)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Instalasi](#-instalasi)
- [Cara Menjalankan](#-cara-menjalankan)
- [Login Demo](#-login-demo)
- [Parameter Simulasi](#-parameter-simulasi)
- [Format Dataset](#-format-dataset-upload-opsional)
- [Alur Kerja Simulasi](#-alur-kerja-simulasi)
- [Validasi Teoritis (Erlang-C)](#-validasi-teoritis-erlang-c)
- [Analisis Monte Carlo](#-analisis-monte-carlo)
- [Output & Export](#-output--export)
- [Asumsi dan Keterbatasan Model](#-asumsi-dan-keterbatasan-model)
- [Pengembangan Lanjutan](#-pengembangan-lanjutan)
- [Penulis](#-penulis)

---

## 📖 Tentang Proyek

Layanan konseling mahasiswa kerap menghadapi tantangan berupa antrian panjang dan waktu tunggu yang tidak pasti, yang dapat memperburuk kondisi psikologis mahasiswa yang sedang menunggu layanan. Proyek ini membangun sebuah **simulasi berbasis agent** untuk memahami dinamika sistem antrian tersebut — bagaimana perilaku individual mahasiswa (tingkat stres, resilience, toleransi menunggu) dan konselor (fatigue, kapasitas layanan) saling memengaruhi efisiensi sistem secara keseluruhan.

Berbeda dari model antrian analitik konvensional (mis. M/M/c), pendekatan ABM memungkinkan setiap entitas memiliki **atribut dan aturan perilaku sendiri**, sehingga hasil simulasi lebih merepresentasikan kompleksitas dunia nyata — sekaligus tetap dapat divalidasi terhadap formula **Erlang-C** sebagai pembanding teoritis.

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|---|---|
| 🔐 **Autentikasi Login** | Sistem login sederhana dengan sesi persisten via query parameter URL |
| 👥 **Agent Mahasiswa** | Setiap mahasiswa memiliki stres awal, resilience, prioritas risiko, dan toleransi tunggu individual |
| 👨‍⚕️ **Agent Konselor** | Konselor memiliki *fatigue* yang meningkat seiring beban layanan, memengaruhi waktu layanan berikutnya |
| ⏳ **Proses Kedatangan Poisson** | Interarrival time dibangkitkan dari distribusi eksponensial, sesuai asumsi model antrian M/M/c |
| 🧠 **Simulasi CBT (Cognitive Behavioral Therapy)** | Efektivitas CBT terhadap penurunan stres mahasiswa dapat diatur secara dinamis |
| 📊 **Dashboard KPI Interaktif** | Ringkasan indikator kinerja utama dalam bentuk kartu visual |
| 📈 **Visualisasi SVG Kustom** | Grafik garis, batang, dan histogram dibuat manual (tanpa library chart eksternal) untuk performa ringan |
| 🎲 **Simulasi Monte Carlo** | Ratusan iterasi acak untuk mengukur ketidakpastian dan interval kepercayaan hasil simulasi |
| 📐 **Validasi Erlang-C** | Membandingkan hasil ABM dengan model antrian teoritis M/M/c |
| 📁 **Upload Dataset Sendiri** | Mendukung dataset CSV kustom sebagai pengganti data sintetis |
| ⬇️ **Export Hasil** | Unduh hasil simulasi (CSV) dan laporan ringkasan (PDF/TXT) |
| 🔁 **Reproducibility** | Opsi random seed agar hasil simulasi dapat direplikasi persis |

---

## 🧩 Konsep Agent Based Modeling

Aplikasi ini dibangun di atas tiga komponen inti ABM:

### 1. `StudentAgent` — Agent Mahasiswa
Merepresentasikan mahasiswa sebagai entitas otonom dengan atribut dan perilaku:
- **Interarrival time** — waktu antar kedatangan (menit, bilangan bulat)
- **Stress Before/After CBT** — tingkat stres sebelum dan sesudah layanan
- **Resilience** — kemampuan individu mengelola tekanan
- **Priority Score** — skor risiko dari kombinasi stres tinggi & resilience rendah
- **Wait Tolerance** — batas toleransi menunggu (dipengaruhi resilience & stres awal)
- **Perilaku adaptif**: stres meningkat selama menunggu, dan agent dapat "memutuskan" keluar dari antrian jika waktu tunggu jauh melampaui toleransinya

### 2. `CounselorAgent` — Agent Konselor
Merepresentasikan konselor sebagai entitas pelayanan dengan:
- **Available time** — waktu konselor siap melayani berikutnya
- **Fatigue** — kelelahan yang meningkat seiring jumlah mahasiswa yang dilayani, memperlambat waktu layanan berikutnya
- **Idle time** & **total service time** — metrik efisiensi konselor

### 3. `CounselingEnvironment` — Lingkungan Simulasi
Mengatur interaksi antar-agent:
- Membentuk agent mahasiswa dari dataset (arrival time kumulatif)
- Aturan pemilihan konselor: **FIFO**, mahasiswa diarahkan ke konselor yang paling cepat tersedia (tie-breaker: fatigue terendah, lalu jumlah layanan tersedikit)
- Mencatat seluruh hasil interaksi menjadi dataframe akhir

```
StudentAgent  ──┐
                ├──►  CounselingEnvironment  ──►  DataFrame Hasil Simulasi
CounselorAgent ─┘
```

---

## 🗂️ Struktur Aplikasi

Meski disusun sebagai satu file (`app.py`) agar mudah dijalankan, kode diorganisasikan secara modular secara logis:

```
├── style.py            → Tema visual kustom (CSS) untuk Streamlit
├── sim_engine.py        → Inti logika ABM (StudentAgent, CounselorAgent, Environment)
│                          + generator dataset & validasi Erlang-C
├── export_utils.py      → Ekspor laporan ke PDF (fpdf) / fallback TXT
├── svg_charts.py        → Generator grafik SVG kustom (line, bar, histogram)
├── ui_helpers.py        → Komponen UI reusable (KPI card, section header, chart panel)
└── app.py               → Aplikasi utama Streamlit (login, sidebar, dashboard, hasil)
```

---

## 🛠️ Teknologi yang Digunakan

- **[Streamlit](https://streamlit.io/)** — framework aplikasi web interaktif
- **[Pandas](https://pandas.pydata.org/)** & **[NumPy](https://numpy.org/)** — manipulasi data & komputasi numerik
- **[SciPy](https://scipy.org/)** — statistik inferensial (t-distribution, skewness, SEM)
- **[fpdf](https://pyfpdf.github.io/)** *(opsional)* — pembuatan laporan PDF
- **SVG native** — visualisasi grafik tanpa dependensi chart library eksternal

---

## ⚙️ Instalasi

### Prasyarat
- Python 3.9 atau lebih baru

### Langkah instalasi

```bash
# 1. Clone / unduh proyek ini
git clone <repository-url>
cd <nama-folder-proyek>

# 2. (Opsional) Buat virtual environment
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install streamlit pandas numpy scipy fpdf2
```

> 💡 Jika `fpdf2` tidak terinstal, aplikasi tetap berjalan normal — laporan ringkasan akan otomatis diekspor dalam format **TXT** sebagai fallback.

---

## 🚀 Cara Menjalankan

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`.

---

## 🔑 Login Demo

| Field | Nilai |
|---|---|
| **Username** | `admin` |
| **Password** | `123456` |

> Sesi login bersifat **persisten** — status login disimpan melalui query parameter URL (`?auth=1`) sehingga tidak hilang saat halaman browser di-refresh. Klik tombol **Keluar** pada sidebar untuk logout.

---

## 🎛️ Parameter Simulasi

Seluruh parameter dapat diatur melalui **sidebar**:

| Parameter | Rentang | Default | Keterangan |
|---|---|---|---|
| Jumlah Mahasiswa | 10 – 5.000 | 50 | Jumlah agent mahasiswa yang disimulasikan |
| Efektivitas CBT | 0.10 – 1.00 | 0.50 | Besarnya pengurangan stres akibat sesi CBT |
| Jumlah Konselor | 1 – 20 | 1 | Jumlah agent konselor yang melayani |
| Iterasi Monte Carlo | 10 – 500 | 100 | Jumlah pengulangan simulasi untuk analisis ketidakpastian |
| Random Seed | 0 – 999.999 | — (opsional) | Mengaktifkan hasil simulasi yang dapat direproduksi |
| Upload Dataset CSV | — | — | Menggantikan dataset sintetis dengan data mahasiswa nyata |

Klik **▶ Jalankan Simulasi** untuk memulai proses.

---

## 📁 Format Dataset Upload (Opsional)

Jika ingin menggunakan dataset sendiri, file CSV **wajib** memiliki kolom berikut:

| Kolom | Tipe | Keterangan |
|---|---|---|
| `Student` | integer | ID unik mahasiswa |
| `Interarrival Time` | integer | Waktu antar kedatangan (menit) — otomatis dibulatkan |
| `Stress Before CBT` | float (0–1) | Tingkat stres awal mahasiswa |
| `Resilience` | float (0–1) | Tingkat resiliensi/ketahanan mental mahasiswa |

Contoh:

```csv
Student,Interarrival Time,Stress Before CBT,Resilience
1,12,0.75,0.30
2,8,0.62,0.45
3,20,0.90,0.20
```

> Mengunggah file baru akan **otomatis memicu** simulasi ulang tanpa perlu menekan tombol "Jalankan Simulasi".

---

## 🔄 Alur Kerja Simulasi

1. **Pembentukan Dataset** — dataset sintetis dibangkitkan (interarrival time dari distribusi eksponensial/Poisson) atau dimuat dari file upload
2. **Inisialisasi Agent** — setiap baris data menjadi satu `StudentAgent`, konselor diinisialisasi sebanyak parameter yang ditentukan
3. **Interaksi Agent (FIFO)** — setiap mahasiswa diarahkan ke konselor paling cepat tersedia; waktu tunggu, idle time, dan waktu layanan dihitung berdasarkan interaksi tersebut
4. **Efek Stres & CBT** — stres mahasiswa diperbarui selama menunggu, lalu direduksi setelah menerima CBT
5. **Agregasi Hasil** — seluruh hasil interaksi agent dikonsolidasikan menjadi dataframe akhir
6. **Analisis Statistik** — KPI, visualisasi SVG, simulasi Monte Carlo, dan validasi Erlang-C dihitung dan ditampilkan
7. **Export** — hasil dapat diunduh dalam format CSV dan PDF/TXT

---

## 📐 Validasi Teoritis (Erlang-C)

Karena waktu antar-kedatangan dibangkitkan dari distribusi eksponensial (proses Poisson), hasil simulasi ABM dapat divalidasi terhadap model antrian klasik **M/M/c** menggunakan formula **Erlang-C**:

- Menghitung **utilisasi sistem (ρ)** dan **waktu tunggu teoritis (Wq)**
- Membandingkan hasil simulasi ABM vs. estimasi teoritis, termasuk persentase selisih
- Jika ρ ≥ 1, sistem dinyatakan **tidak stabil** secara teoritis (laju kedatangan melebihi kapasitas layanan)

Selisih antara hasil ABM dan model M/M/c murni adalah **wajar**, karena ABM memasukkan faktor tambahan seperti fatigue konselor, penyesuaian waktu layanan berbasis stres/prioritas, dan potensi mahasiswa batal antre — yang tidak dimodelkan pada M/M/c klasik.

---

## 🎲 Analisis Monte Carlo

Untuk mengukur **ketidakpastian** hasil simulasi, aplikasi menjalankan puluhan hingga ratusan iterasi independen dan menghitung:

- **Interval kepercayaan 95%** dari rata-rata waktu tunggu
- **Persentil 50/90/95** waktu tunggu
- **Probabilitas waktu tunggu > 20 menit** (indikator risiko antrian panjang)
- **Skewness** distribusi waktu tunggu
- **Analisis konvergensi** — rata-rata kumulatif seiring bertambahnya iterasi, dibandingkan dengan estimasi Erlang-C

> Untuk efisiensi performa, jika jumlah mahasiswa > 200, setiap iterasi Monte Carlo dibatasi menjadi maksimum 200 agent — simulasi utama tetap memakai seluruh data.

---

## 📤 Output & Export

| Output | Format | Isi |
|---|---|---|
| **Hasil Simulasi** | CSV | Data lengkap seluruh agent mahasiswa hasil simulasi (waktu tunggu, layanan, stres, prioritas, dll.) |
| **Laporan Ringkasan** | PDF *(atau TXT jika `fpdf` tidak tersedia)* | Ringkasan indikator kinerja utama + rekomendasi sistem otomatis |

Rekomendasi sistem dihasilkan otomatis berdasarkan kondisi antrian:
- 🟠 **Padat** → disarankan menambah konselor
- 🟢 **Efisien** → jumlah konselor saat ini sudah memadai
- 🔵 **Beban Sedang** → perlu pemantauan pada jam sibuk

---

## ⚠️ Asumsi dan Keterbatasan Model

- Proses kedatangan mahasiswa diasumsikan mengikuti **distribusi eksponensial** (Poisson), sesuai standar model antrian M/M/c
- Nilai `Interarrival Time`, `Counselor Idle Time`, dan `Wait Tolerance` **dibulatkan ke bilangan bulat** agar perhitungan manual (mis. untuk keperluan akademik) lebih mudah diverifikasi
- Antrian dilayani murni secara **FIFO** berdasarkan urutan kedatangan
- Validasi Erlang-C mengasumsikan seluruh konselor **homogen** dan tidak ada mahasiswa yang batal antre — sedangkan ABM memodelkan fatigue konselor dan potensi keluar antrian, sehingga selisih kecil terhadap hasil teoritis adalah hal yang wajar
- Simulasi Monte Carlo membatasi ukuran sampel per iterasi untuk dataset besar demi menjaga responsivitas aplikasi

---

## 🔮 Pengembangan Lanjutan

Beberapa arah pengembangan yang dapat dieksplorasi:

- Pola kedatangan **non-stasioner** (mis. lonjakan menjelang periode UAS)
- Antrian berbasis **prioritas risiko** (bukan murni FIFO)
- **Heterogenitas skill** antar konselor (kecepatan/efektivitas layanan berbeda-beda)
- Analisis **periode warm-up** untuk memisahkan kondisi transien di awal simulasi
- Integrasi dashboard **real-time** dengan data operasional layanan konseling yang sesungguhnya

---

## 👤 Penulis

**Mukhamad Sofyan**
NIM: `202310370311135`

*Dikembangkan untuk memenuhi tugas besar mata kuliah Pemodelan & Simulasi Data — Simulasi Antrian Layanan Konseling Mahasiswa Menggunakan Agent Based Modeling untuk Analisis Waktu Tunggu dan Efisiensi Sistem.*

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan **akademik/edukasi**. Silakan gunakan dan modifikasi sesuai kebutuhan pembelajaran dengan tetap mencantumkan atribusi kepada penulis asli.