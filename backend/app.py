from fastapi import FastAPI
from backend.schema import CardInput
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ADD CORS MIDDLEWARE HERE (VERY IMPORTANT POSITION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load trained model
model = joblib.load("backend/model/model.pkl")


@app.get("/")
def home():
    return {"message": "Credit Card Compliance API is running 🚀"}


@app.post("/predict")
def predict(data: CardInput):
    try:
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
            "confidence": round(probability * 100, 2)
        }

    except Exception as e:
        return {"error": str(e)}