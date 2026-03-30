import streamlit as st
import pandas as pd
import joblib

# 1. Load Model dan Label Encoder
# Pastikan file ini ada di folder yang sama
model = joblib.load('./model/model_student_final.pkl')
le = joblib.load('./model/label_encoder.pkl')

st.set_page_config(page_title="Jaya Jaya Institut - Predictor", layout="wide")

st.title("🎓 Sistem Prediksi Kelulusan Mahasiswa")
st.markdown("""
Aplikasi ini membantu **Jaya Jaya Institut** mendeteksi risiko *dropout* mahasiswa secara dini. 
Silakan masukkan data mahasiswa di panel sebelah kiri.
""")

# --- MAPPING KATEGORIKAL (Sesuai Penjelasan Data.md) ---
marital_map = {1: 'Single', 2: 'Married', 3: 'Widower', 4: 'Divorced', 5: 'Facto Union', 6: 'Legally Separated'}
course_map = {33: 'Biofuel Production', 171: 'Animation Design', 8013: 'Social Service (E)', 9003: 'Agronomy', 
              9070: 'Communication Design', 9085: 'Veterinary Nursing', 9119: 'Informatics Engineering', 
              9130: 'Equiniculture', 9147: 'Management', 9238: 'Social Service', 9254: 'Design', 
              9500: 'Nursing', 9556: 'Oral Hygiene', 9670: 'Advertising', 9773: 'Journalism', 
              9853: 'Basic Education', 9991: 'Management (E)'}
gender_map = {1: 'Laki-laki', 0: 'Perempuan'}
yes_no_map = {1: 'Ya', 0: 'Tidak'}
attendance_map = {1: 'Siang', 0: 'Malam'}

# --- SIDEBAR INPUT ---
st.sidebar.header("📊 Input Data Mahasiswa")

def get_user_inputs():
    # Menggunakan columns untuk merapikan input di sidebar
    st.sidebar.subheader("Profil Pribadi")
    gender = st.sidebar.selectbox("Jenis Kelamin", options=list(gender_map.keys()), format_func=lambda x: gender_map[x])
    age = st.sidebar.number_input("Usia saat Mendaftar", 15, 60, 20)
    marital = st.sidebar.selectbox("Status Pernikahan", options=list(marital_map.keys()), format_func=lambda x: marital_map[x])
    displaced = st.sidebar.selectbox("Mahasiswa Rantau?", options=[1, 0], format_func=lambda x: yes_no_map[x])
    
    st.sidebar.subheader("Latar Belakang Pendidikan")
    course = st.sidebar.selectbox("Program Studi", options=list(course_map.keys()), format_func=lambda x: course_map[x])
    tuition = st.sidebar.selectbox("Pembayaran SPP Lancar?", options=[1, 0], format_func=lambda x: yes_no_map[x])
    scholarship = st.sidebar.selectbox("Penerima Beasiswa?", options=[1, 0], format_func=lambda x: yes_no_map[x])
    debtor = st.sidebar.selectbox("Memiliki Hutang?", options=[1, 0], format_func=lambda x: yes_no_map[x])
    
    st.sidebar.subheader("Performa Akademik")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        s1_app = st.number_input("SKS Lulus Semester 1", 0, 30, 5)
        s1_grade = st.number_input("IP Semester 1", 0.0, 20.0, 12.0)
    with col2:
        s2_app = st.number_input("SKS Lulus Semester 2", 0, 30, 5)
        s2_grade = st.number_input("IP Semester 2", 0.0, 20.0, 12.0)

    # Gabungkan semua data (termasuk fitur yang tidak diinput user tapi ada di dataset asli)
    # Kita gunakan nilai rata-rata/default untuk fitur pendukung lainnya agar model tidak error
    data = {
        'Marital_status': marital, 'Application_mode': 1, 'Application_order': 1, 'Course': course,
        'Daytime_evening_attendance': 1, 'Previous_qualification': 1, 'Previous_qualification_grade': 120.0,
        'Nacionality': 1, 'Mothers_qualification': 1, 'Fathers_qualification': 1, 
        'Mothers_occupation': 1, 'Fathers_occupation': 1, 'Admission_grade': 120.0,
        'Displaced': displaced, 'Educational_special_needs': 0, 'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition, 'Gender': gender, 'Scholarship_holder': scholarship,
        'Age_at_enrollment': age, 'International': 0, 
        'Curricular_units_1st_sem_credited': 0, 'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 6, 'Curricular_units_1st_sem_approved': s1_app,
        'Curricular_units_1st_sem_grade': s1_grade, 'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0, 'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 6, 'Curricular_units_2nd_sem_approved': s2_app,
        'Curricular_units_2nd_sem_grade': s2_grade, 'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 11.0, 'Inflation_rate': 1.5, 'GDP': 0.5
    }
    
    # Hitung Fitur Tambahan (Feature Engineering) agar model tidak ValueError
    df_input = pd.DataFrame(data, index=[0])
    df_input['SKS_Stability'] = s2_app - s1_app
    df_input['Grade_Improvement'] = s2_grade - s1_grade
    
    return df_input

input_data = get_user_inputs()

# --- BAGIAN DASHBOARD UTAMA ---
col_main, col_res = st.columns([2, 1])

with col_main:
    st.subheader("📋 Detail Data yang Dimasukkan")
    # Menampilkan tabel yang lebih cantik
    st.write(input_data[['Course', 'Gender', 'Scholarship_holder', 'Tuition_fees_up_to_date', 'SKS_Stability', 'Grade_Improvement']])

with col_res:
    st.subheader("🔮 Hasil Prediksi")
    if st.button("Jalankan Analisis", use_container_width=True):
        prediction = model.predict(input_data)
        prob = model.predict_proba(input_data)
        res_text = le.inverse_transform(prediction)[0]
        
        # Tampilan hasil berdasarkan status
        if res_text == 'Dropout':
            st.error(f"⚠️ Status: {res_text}")
            st.write("Siswa ini berisiko tinggi. Disarankan untuk bimbingan konseling segera.")
        elif res_text == 'Enrolled':
            st.warning(f"🟡 Status: {res_text}")
            st.write("Siswa dalam status aman namun perlu dipantau perkembangannya.")
        else:
            st.success(f"✅ Status: {res_text}")
            st.write("Siswa menunjukkan performa akademik yang sangat baik.")

        # Menampilkan Gauge atau Bar Probabilitas
        st.write("---")
        st.write("**Keyakinan Model:**")
        prob_df = pd.DataFrame(prob, columns=le.classes_).T
        st.bar_chart(prob_df)