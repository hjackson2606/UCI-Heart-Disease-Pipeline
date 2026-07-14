import streamlit as st
import requests

st.title("Heart Disease Risk Predictor")

age = st.number_input("Age", min_value=0, max_value=120, value=50)
trestbps = st.number_input("Resting Blood Pressure", value=120.0)
chol = st.number_input("Cholesterol", value=200.0)
thalch = st.number_input("Max Heart Rate Achieved", value=150.0)
oldpeak = st.number_input("ST Depression (oldpeak)", value=1.0)

sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["typical angina", "asymptomatic", "non-anginal", "atypical angina"])
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [True, False])
restecg = st.selectbox("Resting ECG", ["lv hypertrophy", "normal", "st-t abnormality"])
exang = st.selectbox("Exercise Induced Angina", [True, False])
slope = st.selectbox("Slope of Peak Exercise ST Segment", ["downsloping", "flat", "upsloping"])

if st.button("Predict"):
    payload = {
        "age": age,
        "trestbps": trestbps,
        "chol": chol,
        "thalch": thalch,
        "oldpeak": oldpeak,
        "sex": sex,
        "cp": cp,
        "fbs": fbs,
        "restecg": restecg,
        "exang": exang,
        "slope": slope
    }
    
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    result = response.json()
    
    st.write(f"Prediction: {'Heart Disease Likely' if result['prediction'] == 1 else 'No Heart Disease Likely'}")
    st.write(f"Probability: {result['probability']:.2%}")