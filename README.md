# 💳 Credit Card Compliance Checker

An end-to-end machine learning system that evaluates whether a credit card is **Compliant** or **Non-Compliant** based on financial and transparency parameters.

---

## 🚀 Highlights

* 🔍 Rule-based + ML hybrid system
* 🤖 Decision Tree model for compliance prediction
* 📊 Confidence score with each prediction
* 💡 Human-readable explanation (WHY decision was made)
* 🛡️ Strong input + business validation
* 🌐 Interactive UI using FastAPI

---

## 🧠 Problem

Financial products must follow strict compliance rules to ensure fairness.

This system helps:

* Identify risky credit card configurations
* Explain violations clearly
* Improve transparency in decision-making

---

## ⚙️ System Flow

User Input → Validation → ML Model → Explanation → Output

---

## 🧪 Example

```
✖ Non-Compliant (98%)

Reasons:
• High interest rate
• Disclosure not provided
```

---

## 🧰 Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* HTML/CSS/JavaScript

---

## 📊 Model

* Decision Tree Classifier
* Criterion: Gini
* Max Depth: 4 (to prevent overfitting)
* Trained on balanced synthetic dataset

---

## 📁 Structure

```
backend/
├── app.py
├── train.py
├── validation.py
├── explanation.py
├── schema.py
├── data/
├── model/

frontend/
└── index.html
```

---

## ▶️ Run

```bash
pip install -r requirements.txt
uvicorn backend.app:app --reload
```

Open: http://127.0.0.1:8000

---

## 📌 Key Learnings

* Data quality > model complexity
* Importance of validation in ML systems
* Building explainable AI systems
* Full pipeline: data → model → API → UI

---

## ⚠️ Limitations

* Synthetic dataset
* Rule-based explanation -
