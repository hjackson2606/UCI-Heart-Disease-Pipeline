from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pandas as pd
import joblib

app = FastAPI()
model = joblib.load("heart_disease_model.pkl")

class PatientData(BaseModel):
    age: int
    trestbps: float
    chol: float
    thalch: float
    oldpeak: float
    sex: Literal["Male", "Female"]
    cp: Literal["typical angina", "asymptomatic", "non-anginal", "atypical angina"]
    fbs: bool
    restecg: Literal["lv hypertrophy", "normal", "st-t abnormality"]
    exang: bool
    slope: Literal["downsloping", "flat", "upsloping"]

@app.post("/predict")
def predict(patient: PatientData):
    input_df = pd.DataFrame([patient.dict()])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }