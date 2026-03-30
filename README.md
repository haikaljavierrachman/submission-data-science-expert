# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di berbagai wilayah.

Seiring dengan pertumbuhan perusahaan, muncul permasalahan dalam pengelolaan sumber daya manusia, khususnya tingginya tingkat attrition (karyawan keluar) yang telah melebihi 10%. Tingginya attrition ini dapat berdampak negatif terhadap produktivitas, biaya rekrutmen, serta stabilitas tim dalam perusahaan.

Oleh karena itu, diperlukan analisis berbasis data untuk mengidentifikasi faktor-faktor yang mempengaruhi attrition serta membantu tim HR dalam mengambil keputusan strategis.

### Permasalahan Bisnis

Berikut adalah beberapa permasalahan bisnis yang ingin diselesaikan:

1. Tingginya attrition rate karyawan (>10%)

2. Kurangnya pemahaman faktor utama penyebab karyawan keluar

3. Tidak adanya sistem monitoring berbasis data untuk attrition

4. Sulitnya HR dalam mengidentifikasi karyawan berisiko resign

### Cakupan Proyek

1. Cakupan proyek ini meliputi:

2. Melakukan data understanding dan data cleaning

3. Melakukan exploratory data analysis (EDA)

4. Mengidentifikasi faktor-faktor yang mempengaruhi attrition

5. Membuat business dashboard untuk monitoring attrition

6. Memberikan insight dan rekomendasi bisnis

### Persiapan

Sumber data:
Dataset karyawan Jaya Jaya Maju dari github repository dicoding (https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:
Tools yang digunakan:

1. Python 3.13.3 (
    Pandas 2.2.3, 
    NumPy 2.2.5, 
    Matplotlib 3.10.8, 
    Seaborn 0.13.2, 
    Scikit-learn 1.6.1
    ) Untuk installasi library menggunakan command `pip install -r requirements.txt`

2. Google Colab

3. Metabase (untuk dashboard)

4. Docker (untuk menjalankan Metabase & PostgreSQL)

```

```

## Business Dashboard

Dashboard dibuat menggunakan Metabase untuk membantu tim HR memonitor faktor-faktor yang mempengaruhi attrition.

Running Dashboard on docker:
    Step untuk running Dashboard Metabase
    1. Untuk linux jalankan command `bash -x script-linux-sh`
    2. Untuk windows jalankan file script-windows.bat (klik 2x)

    Di dalam script
    1. Jalankan docker compose untuk container metabase & postgresql
    2. Insert file employee_data.csv ke container postgresql dengan script insert_to_postgre.py

    Buka link http://http://localhost:3000/
    Masukkan Email dan Password
    email: root@mail.com
    password: root123

Isi Dashboard:

Dashboard menampilkan beberapa visualisasi utama:

1. Jumlah employee berdasarkan gender

2. Attrition Rate (KPI utama)

3. Attrition berdasarkan Department

4. Attrition berdasarkan Job Level

Tujuan Dashboard:

1. Mempermudah HR dalam memahami pola attrition

2. Mengidentifikasi faktor risiko utama secara visual

## Conclusion

1. Attrition rate diatas threshold perusahaan (10%)

2. Dari dataset, sekitar 16–17% karyawan keluar.

3. Mayoritas karyawan tetap (kelas 0 / tidak resign) → model perlu hati-hati agar tidak bias terhadap kelas mayoritas.

Beberapa faktor mempengaruhi attrition
Berdasarkan EDA (barplot, heatmap, boxplot):

1. Departemen: Sales dan Human Resources cenderung punya attrition lebih tinggi dibanding Research & Development.

2. OverTime: Karyawan yang lembur lebih sering berisiko keluar.

3. Karyawan dengan income sangat rendah atau sedang kadang lebih berisiko keluar. Income mempengaruhi attrition, tapi bukan faktor utama. terdapat beberapa faktor seperti Environmet Satisfaction, Job Level dan Job Involvement dimana ketiga itu yang mayoritas nilai 1 lebih banyak attrition


### Rekomendasi Action Items (Optional)

Berdasarkan gabungan semua insight:

1. Insight
Fokus pada karyawan berisiko tinggi

- Target karyawan dengan:

-- JobLevel, EnvironmentSatisfaction rendah

-- OverTime tinggi

-- Departemen dengan attrition tinggi (RnD, Sales)

- Buat program retensi seperti mentoring, coaching, recognition, dan career development.

2. Action

- Perhitungkan kembali tunjangan lembur jika memang dibutuhkan overtime lebih

- Perbaiki kondisi kerja dan engagement

- Tingkatkan work-life balance → fleksibilitas jam kerja, cuti, remote work

- Tingkatkan environment satisfaction → kenyamanan kantor, budaya kerja, kolaborasi tim

- Tingkatkan job involvement & satisfaction & level → reward system, pelatihan, keterlibatan proyek penting


### Prediction (Optional)

Menjalankan prediksi:

1. Install library python (pip install -r requirements.txt)

2. Mengisi sampel data karyawan di file prediction.py

3. Jalankan script python (python prediction.py)