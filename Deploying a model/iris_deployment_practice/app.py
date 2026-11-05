from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("artifacts/iris_model.pkl", "rb") as file:
    model = pickle.load(file)

FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

@app.get("/")
def home():
    return jsonify({
        "message": "Iris prediction API is running",
        "usage": "POST /predict with four numeric flower measurements"
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"})

@app.post("/predict")
def predict():
    payload = request.get_json(silent=True)
    if not payload or "features" not in payload:
        return jsonify({"error": "Send JSON with a 'features' list"}), 400

    values = payload["features"]
    if not isinstance(values, list) or len(values) != 4:
        return jsonify({"error": "features must contain exactly 4 numbers"}), 400

    try:
        row = np.array(values, dtype=float).reshape(1, -1)
        prediction = model.predict(row)[0]
        probabilities = model.predict_proba(row)[0]
        return jsonify({
            "predicted_species": prediction,
            "class_probabilities": {
                name: round(float(prob), 4)
                for name, prob in zip(model.classes_, probabilities)
            }
        })
    except (TypeError, ValueError):
        return jsonify({"error": "All feature values must be numeric"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
