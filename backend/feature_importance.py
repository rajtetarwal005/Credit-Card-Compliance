import joblib
import pandas as pd
import matplotlib.pyplot as plt


model = joblib.load("backend/model/model.pkl")

features = [
    "interest_rate",
    "late_fee",
    "annual_fee",
    "billing_cycle",
    "min_payment",
    "disclosure"
]

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

importance_df = importance_df.sort_values(by="Importance", ascending=False)

print("\nFeature Importance:\n")
for index, row in importance_df.iterrows():
    print(f"{row['Feature']}: {round(row['Importance'], 3)}")

plt.figure(figsize=(8, 5))
plt.barh(importance_df["Feature"], importance_df["Importance"])
plt.xlabel("Importance")
plt.title("Feature Importance (Decision Tree)")
plt.gca().invert_yaxis()  # highest at top
plt.show()