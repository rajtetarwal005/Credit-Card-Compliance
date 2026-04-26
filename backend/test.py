import pandas as pd

df = pd.read_csv("backend/data/data.csv")

print(df[df["billing_cycle"] == 25]["label"].value_counts())
print(df[df["min_payment"] == 5]["label"].value_counts())