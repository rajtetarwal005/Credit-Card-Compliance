from fastapi import FastAPI
from backend.schema import CardInput
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from backend.validation import validate_input
from backend.explanation import get_explanation

app = FastAPI()

# Load model
model = joblib.load("backend/model/model.pkl")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve HTML
@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/index.html", encoding="utf-8") as f:
        return f.read()


# Prediction API
@app.post("/predict")
def predict(data: CardInput):

    validate_input(data)
    input_data = np.array([[
        data.interest_rate,
        data.late_fee,
        data.annual_fee,
        data.billing_cycle,
        data.min_payment,
        data.disclosure
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0].max()

    return {
        "prediction": "Compliant" if prediction == 1 else "Non-Compliant",
        "confidence": round(probability * 100, 2),
        "reasons": get_explanation(data) if prediction == 0 else []
    }