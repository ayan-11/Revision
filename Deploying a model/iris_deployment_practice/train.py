import json
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("iris.csv")
X = df.drop(columns=["species"])
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=500, random_state=42))
])
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Test accuracy: {accuracy:.4f} ({accuracy:.2%})")
print("\\nClassification report:")
print(classification_report(y_test, predictions))
print("Confusion matrix:")
print(confusion_matrix(y_test, predictions))

with open("artifacts/iris_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("artifacts/evaluation.json", "w") as file:
    json.dump({
        "test_accuracy": accuracy,
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist()
    }, file, indent=2)

print("\\nSaved model to artifacts/iris_model.pkl")
