
import os
import json
import joblib
import numpy as np
import pandas as pd

from xgboost import XGBRegressor

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from feature_engineering import HnMFeatureEngineer


# ==========================================
# 1. LOAD DATASET
# ==========================================

data = pd.read_csv("handm.csv")

print("Original dataset shape:", data.shape)


# ==========================================
# 2. CLEAN TARGET VARIABLE
# ==========================================

# Remove rows where target is missing
data = data.dropna(subset=["price"]).copy()

# Convert price to numeric
data["price"] = pd.to_numeric(
    data["price"].astype(str).str.replace(
        r"[^\d.\-]", "", regex=True
    ),
    errors="coerce"
)

data = data.dropna(subset=["price"])

print("Dataset after cleaning:", data.shape)


# ==========================================
# 3. SEPARATE FEATURES AND TARGET
# ==========================================

X = data.drop(columns=["price"])

y = data["price"]


# ==========================================
# 4. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)


# ==========================================
# 5. PREPROCESSING PIPELINES
# ==========================================

# Numerical columns
numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)


# Categorical columns
categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(
            missing_values=np.nan,
            strategy="most_frequent"
        )),

        ("encoder", OneHotEncoder(
            handle_unknown="ignore"
        ))
    ]
)


# Combine numerical and categorical preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "numerical",
            numeric_pipeline,
            make_column_selector(dtype_include=np.number)
        ),
        (
            "categorical",
            categorical_pipeline,
            make_column_selector(dtype_include=["object", "category", "bool"])
        )
    ],
    remainder="drop"
)


# ==========================================
# 6. COMPLETE ML PIPELINE
# ==========================================

pipeline = Pipeline(
    steps=[

        # Feature engineering
        ("feature_engineering", HnMFeatureEngineer()),

        # Missing value handling and encoding
        ("preprocessor", preprocessor),

        # ML model
        ("model", XGBRegressor(
            random_state=42,
            objective="reg:squarederror",
            n_jobs=1
        ))
    ]
)


# ==========================================
# 7. HYPERPARAMETER TUNING
# ==========================================

params = {

    "model__n_estimators": [100, 200, 300],

    "model__max_depth": [3, 6, 9],

    "model__learning_rate": [0.01, 0.1, 0.2],

    "model__subsample": [0.8, 1],

    "model__colsample_bytree": [0.8, 1]

}


grid_search = GridSearchCV(

    estimator=pipeline,

    param_grid=params,

    scoring="neg_mean_absolute_error",

    cv=3,

    verbose=1,

    n_jobs=-1

)


# ==========================================
# 8. TRAIN MODEL
# ==========================================

print("\nStarting model training...")
X_debug = HnMFeatureEngineer().fit_transform(X_train)

print("\nNumerical columns:")
print(X_debug.select_dtypes(include=np.number).columns.tolist())

print("\nCategorical columns:")
print(X_debug.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist())

print("\nProduct name dtype:")
print(X_debug["productName"].dtype)
grid_search.fit(X_train, y_train)

# ==========================================
# 9. GET BEST MODEL
# ==========================================

best_model = grid_search.best_estimator_

print("\nBest Hyperparameters:")

print(grid_search.best_params_)


# ==========================================
# 10. MODEL EVALUATION
# ==========================================

y_pred = best_model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


print("\n========== MODEL PERFORMANCE ==========")

print(f"MAE: {mae:.2f}")

print(f"MSE: {mse:.2f}")

print(f"RMSE: {rmse:.2f}")

print(f"R2 Score: {r2:.4f}")


# ==========================================
# 11. SAVE COMPLETE PIPELINE
# ==========================================

os.makedirs("artifacts", exist_ok=True)

joblib.dump(
    best_model,
    "artifacts/model.pkl"
)


# Save the original input column names
with open("artifacts/input_columns.json", "w") as file:

    json.dump(
        X.columns.tolist(),
        file
    )


print("\nModel successfully saved!")

print("Location: artifacts/model.pkl")
