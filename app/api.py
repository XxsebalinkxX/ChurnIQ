from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="ChurnIQ – Churn Prediction API")

model = joblib.load("app/churn_model.pkl")

class CustomerData(BaseModel):
    age: int
    subscription_months: int
    login_freq: int

@app.post("/predict_churn")
def predict_churn(data: CustomerData):
    features = np.array([[data.age, data.subscription_months, data.login_freq]])
    probability = float(model.predict_proba(features)[0][1])
    return {"churn_probability": round(probability, 3)}
