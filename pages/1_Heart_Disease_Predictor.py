import streamlit as st
import requests

st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="🫀",
    layout="wide",
)

st.title("Heart Disease Risk Predictor")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=50)
    trestbps = st.number_input("Resting Blood Pressure", value=120.0)
    chol = st.number_input("Cholesterol", value=200.0)
    thalch = st.number_input("Max Heart Rate Achieved", value=150.0)
    oldpeak = st.number_input("ST Depression (oldpeak)", value=1.0)

with col2:
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

    response = requests.post("https://heart-disease-predictor-edso.onrender.com/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        if result['prediction'] == 1:
            st.error(f"⚠️ Heart Disease Likely — {result['probability']:.1%} estimated risk")
        else:
            st.success(f"✅ No Heart Disease Likely — {result['probability']:.1%} estimated risk")
    else:
        st.error("Something went wrong contacting the API.")