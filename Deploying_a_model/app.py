
import json
import joblib
import pandas as pd

from flask import Flask, request, jsonify


app = Flask(__name__)


# ==========================================
# 1. LOAD TRAINED PIPELINE
# ==========================================

model = joblib.load("artifacts/model.pkl")


# Load original input column names
with open("artifacts/input_columns.json", "r") as file:

    input_columns = json.load(file)


# ==========================================
# 2. HOME ROUTE
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "H&M Product Price Prediction API",
        "status": "Running",
        "endpoint": "/predict"
    })


# ==========================================
# 3. HEALTH CHECK
# ==========================================

@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy",
        "model_loaded": True
    })


# ==========================================
# 4. PREDICTION ROUTE
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Receive JSON data
        request_data = request.get_json()

        if not isinstance(request_data, dict):
            return jsonify({
                "error": "Please provide a JSON object."
            }), 400

        # Accept either a direct JSON object
        # or an object wrapped inside "data"
        input_data = request_data.get("data", request_data)

        if not isinstance(input_data, dict):
            return jsonify({
                "error": "Invalid input format."
            }), 400

        # Convert input into DataFrame
        input_df = pd.DataFrame([input_data])

        # Maintain the same original feature columns
        input_df = input_df.reindex(
            columns=input_columns
        )

        # Generate prediction
        prediction = model.predict(input_df)

        predicted_price = float(prediction[0])

        # Return response
        return jsonify({

            "predicted_price": round(predicted_price, 2),

            "currency": "INR",

            "status": "success"

        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 400


# ==========================================
# 5. RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
