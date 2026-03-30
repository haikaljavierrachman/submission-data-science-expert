import pandas as pd
import joblib

def run_prediction(input_data):
    # 1. Load model yang sudah diekspor tadi
    model = joblib.load('model_attrition.pkl')
    
    # 2. Melakukan prediksi
    # Data input harus memiliki kolom yang sama dengan X_train
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]
    
    return prediction, probability

# Contoh Penggunaan:
if __name__ == "__main__":
    # Masukkan data contoh (pastikan kolomnya sama persis dengan saat training)
    sample_data = pd.DataFrame([{
        "Age":51.0,
        "BusinessTravel":2,
        "DailyRate":1323.0,
        "Department":1,
        "DistanceFromHome":4.0,
        "Education":4.0,
        "EducationField":1,
        "EnvironmentSatisfaction":1.0,
        "Gender":1,
        "HourlyRate":34.0,
        "JobInvolvement":3.0,
        "JobLevel":1.0,
        "JobRole":6,
        "JobSatisfaction":3.0,
        "MaritalStatus":1,
        "MonthlyIncome":2461.0,
        "MonthlyRate":10332.0,
        "NumCompaniesWorked":9.0,
        "OverTime":1,
        "PercentSalaryHike":12.0,
        "PerformanceRating":3.0,
        "RelationshipSatisfaction":3.0,
        "StockOptionLevel":3.0,
        "TotalWorkingYears":18.0,
        "TrainingTimesLastYear":2.0,
        "WorkLifeBalance":4.0,
        "YearsAtCompany":10.0,
        "YearsInCurrentRole":0.0,
        "YearsSinceLastPromotion":2.0,
        "YearsWithCurrManager":7.0
    }])
    
    hasil, skor = run_prediction(sample_data)
    
    status = "Keluar (Exit)" if hasil[0] == 1 else "Bertahan (Stay)"
    print(f"Hasil Prediksi: {status}")
    print(f"Probabilitas: {skor[0]:.2f}")