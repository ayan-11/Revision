# Iris ML Deployment Practice

A small end-to-end classification project using the classic Iris dataset.

## What it does
Predicts one of three flower species from four measurements:
- sepal length (cm)
- sepal width (cm)
- petal length (cm)
- petal width (cm)

## Model and evaluation
- Model: StandardScaler + LogisticRegression
- Split: 80% train / 20% test
- Stratified split, random_state=42
- Test accuracy from the included trained artifact: 93.33%
- The fitted pipeline is saved at `artifacts/iris_model.pkl`.

## Setup (Windows PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Train and evaluate
```powershell
python train.py
```

## Run the API locally
```powershell
python app.py
```
Open `http://127.0.0.1:5000/health`.

## Test a prediction
In a second terminal:
```powershell
curl.exe -X POST http://127.0.0.1:5000/predict `
  -H "Content-Type: application/json" `
  -d "{\"features\":[5.1,3.5,1.4,0.2]}"
```

Expected class for this example: `setosa` (probabilities may vary slightly by library version).

## API contract
`POST /predict`
```json
{"features": [5.1, 3.5, 1.4, 0.2]}
```

## Project structure
```text
iris_deployment_practice/
├── app.py
├── train.py
├── iris.csv
├── requirements.txt
├── README.md
└── artifacts/
    ├── iris_model.pkl
    └── evaluation.json
```

For a public deployment, use a production server (for example Gunicorn) rather than Flask's development server, and do not load pickle files from untrusted sources.
