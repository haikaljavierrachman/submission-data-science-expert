# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meskipun memiliki reputasi yang baik, institusi menghadapi tantangan signifikan berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikan mereka (dropout). Hal ini berdampak pada efisiensi operasional dan reputasi institusi.

### Permasalahan Bisnis
1. Tingginya angka dropout mahasiswa yang sulit dideteksi secara manual sejak dini.
2. Kurangnya pemahaman mengenai faktor-faktor utama (akademik maupun sosial-ekonomi) yang menyebabkan mahasiswa berhenti kuliah.
3. Kebutuhan akan alat pemantauan (dashboard) dan sistem prediksi otomatis untuk mengidentifikasi mahasiswa berisiko.

### Cakupan Proyek
1. Melakukan analisis data eksploratif (EDA) untuk mengidentifikasi tren dan pola dropout.
2. Membangun model machine learning klasifikasi untuk memprediksi status mahasiswa (Dropout, Enrolled, Graduate).
3. Membuat Business Dashboard interaktif untuk memonitor performa siswa secara keseluruhan.
4. Memberikan rekomendasi strategis (action items) bagi manajemen institut.

### Persiapan

Sumber data: Dataset Students' Performance yang mencakup data demografi, sosial-ekonomi, dan performa akademik semester 1 & 2 (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
Tools yang digunakan:

1. Python 3.13.3 (
    Library python yang dibutuhkan:
    Pandas 2.2.3, 
    NumPy 2.2.5, 
    Matplotlib 3.10.8, 
    Seaborn 0.13.2, 
    Scikit-learn 1.6.1
    streamlit 1.55.0
    )

2. Google Colab

3. Metabase (untuk dashboard)

4. Docker (untuk menjalankan Metabase & PostgreSQL)

5. Streamlit (Untuk dashboard prediksi mahasiswa)

6. List library python (requirements.txt)

7. Python virtual environment
    Setup:
    1. pip -m venv (nama_env)
    2. Masuk ke venv
        Linux : source nama_venv/bin/activate
        Windows: source name_venv/Script/activate
    3. Install library
        pip install -r requirements.txt

        jika menggunakan file requirements.txt terdapat library yang tidak ada gunakan file requirements-all.txt
        pip install -r requirements-all.txt
```

```

## Business Dashboard
Dashboard dibuat untuk memberikan gambaran visual bagi manajemen mengenai kesehatan akademik institut. Fokus utama dashboard meliputi:

- Jumlah Mahasiswa berdasarkan gender 

- Tingkat Kelulusan vs Dropout: Perbandingan persentase mahasiswa berdasarkan status & gender.

- Jumlah mahasiswa dropout per program studi

- Jumlah / persentase mahasiswa dropout berdasarkan negara

Cara menjalankan:
    1. Untuk linux : bash -x script-linux.sh
    2. Untuk Windows : run / double klik script-windows.bat

    Isi dari 2 script diatas adalah:
    1. Menjalankan docker-compose untuk running container postgresql dan metabase
    2. Menjalankan script python untuk insert data ke dalam container postgresql

    Buka di browser http://localhost:3000

    Kredensial metabase: Email: root@mail.com | Password: root123

## Menjalankan Sistem Machine Learning
Prototype dikembangkan menggunakan Streamlit untuk memungkinkan staf akademik memasukkan data mahasiswa secara individu dan mendapatkan hasil prediksi instan terkait status mahasiswa.

Cara menjalankan:
    python -m streamlit run app.py

Atau bisa akses ke 
    https://javierrachman-students-prototype.streamlit.app/

```

```

## Conclusion
Berdasarkan proyek data science ini, dapat disimpulkan bahwa:

Indikator Utama Akademik: Performa akademik pada tahun pertama merupakan prediktor paling kuat terhadap status kelulusan mahasiswa. Secara khusus, fitur Curricular_units_2nd_sem_approved (jumlah SKS yang lulus di semester 2) memiliki korelasi positif tertinggi (0.62) terhadap keberhasilan studi. Mahasiswa yang gagal menyelesaikan sebagian besar SKS di semester awal memiliki risiko dropout yang sangat signifikan.

Dampak Kondisi Finansial: Faktor ekonomi pribadi memainkan peran krusial. Mahasiswa yang memiliki status sebagai penerima beasiswa (Scholarship holder) memiliki kecenderungan jauh lebih tinggi untuk lulus. Sebaliknya, mahasiswa yang memiliki tunggakan pembayaran (Debtor) dan tidak membayar SPP tepat waktu (Tuition fees up to date) memiliki korelasi negatif yang kuat dengan status kelulusan, yang berarti mereka lebih rentan untuk berhenti kuliah.

Faktor Demografi dan Sosial: Mahasiswa yang mendaftar pada usia yang lebih dewasa (Age at enrollment) memiliki risiko dropout yang sedikit lebih tinggi dibandingkan mahasiswa yang baru lulus sekolah menengah. Hal ini kemungkinan disebabkan oleh adanya tanggung jawab lain (seperti bekerja atau keluarga). Selain itu, faktor makroekonomi (seperti tingkat inflasi dan GDP) tidak memiliki pengaruh yang signifikan secara langsung jika dibandingkan dengan faktor performa akademik internal.

Performa Model Prediksi: Model Machine Learning yang dikembangkan (menggunakan algoritma Random Forest dengan Hyperparameter Tuning) berhasil mencapai Akurasi sebesar 76.05%. Model ini sangat handal dalam mengidentifikasi calon lulusan (Precision Graduate: 0.83) dan memiliki kemampuan yang cukup baik dalam mendeteksi potensi dropout (Precision Dropout: 0.85). Namun, model masih memiliki tantangan dalam membedakan kelas 'Enrolled' secara akurat karena pola data yang tumpang tindih.

Nilai Tambah bagi Institusi: Dengan adanya model ini dan dashboard pendukung, Jaya Jaya Institut kini memiliki sistem peringatan dini (Early Warning System) berbasis data. Institusi tidak lagi hanya bereaksi setelah mahasiswa keluar, tetapi dapat memprediksi risiko tersebut sejak akhir semester pertama atau kedua untuk melakukan intervensi yang tepat sasaran.

### Rekomendasi Action Items
Pengembangan Sistem Peringatan Dini (Early Warning System)

- Tindakan: Mengintegrasikan model machine learning ke dalam sistem administrasi kampus untuk memindai data mahasiswa setiap akhir semester.

- Tujuan: Mengidentifikasi mahasiswa dengan status "Risiko Tinggi" secara otomatis. Mahasiswa yang diprediksi dropout oleh sistem harus segera mendapatkan notifikasi dan dijadwalkan untuk sesi konsultasi wajib dengan dosen pembimbing akademik.

Intervensi Akademik Terfokus pada Tahun Pertama

- Tindakan: Memberikan perhatian khusus pada mahasiswa yang gagal menyelesaikan lebih dari 50% SKS di Semester 1.

- Tujuan: Mengingat variabel Curricular_units_1st_sem_approved memiliki pengaruh besar, institusi perlu menyediakan program remedial atau bimbingan belajar tambahan (tutoring) sebelum mahasiswa memasuki Semester 2 agar beban akademik tidak menumpuk.

Program Bantuan Finansial dan Manajemen Tunggakan

- Tindakan: Membuat kebijakan fleksibilitas pembayaran SPP bagi mahasiswa yang terdeteksi sebagai Debtor.

- Tujuan: Analisis menunjukkan bahwa tunggakan biaya adalah pemicu kuat dropout. Dengan memberikan opsi cicilan atau menghubungkan mahasiswa Debtor yang berprestasi dengan sumber beasiswa baru, institusi dapat membantu mereka tetap fokus kuliah tanpa terbebani masalah finansial mendesak.

Optimalisasi dan Peninjauan Ulang Beasiswa

- Tindakan: Memperluas kriteria penerima beasiswa tidak hanya berdasarkan prestasi akademik, tetapi juga faktor risiko sosial-ekonomi.

- Tujuan: Data menunjukkan penerima beasiswa memiliki tingkat kelulusan yang sangat tinggi. Memperbanyak kuota beasiswa kecil (bantuan parsial) untuk mahasiswa di ambang dropout dapat menjadi investasi yang lebih efektif daripada kehilangan pendapatan dari mahasiswa yang berhenti kuliah.

Pendampingan Khusus Mahasiswa Non-Reguler (Pekerja/Dewasa)

- Tindakan: Menyediakan layanan konseling karir dan manajemen waktu bagi mahasiswa yang mendaftar pada usia dewasa (Age at enrollment yang tinggi).

- Tujuan: Membantu mereka menyeimbangkan antara tuntutan pekerjaan/keluarga dengan beban akademik, mengingat kelompok usia ini memiliki risiko dropout yang lebih tinggi secara statistik.
