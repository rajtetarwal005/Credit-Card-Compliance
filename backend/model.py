import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

def train_model():
    # Load dataset
    df = pd.read_csv("backend/data/data.csv")

    # Split features and label
    X = df.drop("label", axis=1)
    y = df["label"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = DecisionTreeClassifier(max_depth=4)

    # Train
    model.fit(X_train, y_train)

    # Accuracy
    accuracy = model.score(X_test, y_test)
    print(f" Model Accuracy: {round(accuracy * 100, 2)}%")

    # Save model
    joblib.dump(model, "backend/model/model.pkl")
    print("Model saved at backend/model/model.pkl")

    return model


if __name__ == "__main__":
    train_model()