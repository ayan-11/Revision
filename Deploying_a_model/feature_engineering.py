
import pandas as pd
import numpy as np
import re

from sklearn.base import BaseEstimator, TransformerMixin


class HnMFeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def extract_features(self, text):

        text = str(text) if pd.notna(text) else ""

        def extract(pattern):
            match = re.search(pattern, text, flags=re.IGNORECASE)
            return match.group(1).strip() if match else "Unknown"

        features = {}

        features["heel_height"] = extract(
            r"Heel Height:\s*([^.]+)"
        )

        features["footwear_type"] = extract(
            r"Footwear type:\s*([^.]+)"
        )

        features["color_description"] = extract(
            r"Description:\s*([^.]+)"
        )

        features["imported"] = extract(
            r"Imported:\s*([^.]+)"
        )

        features["contains_slippers"] = int(
            "slippers" in text.lower()
        )

        features["contains_fabric"] = int(
            "fabric" in text.lower()
        )

        features["contains_seam"] = int(
            "seam" in text.lower()
        )

        features["contains_pile"] = int(
            "pile" in text.lower()
        )

        return features

    def transform(self, X):

        X = X.copy()

        # Remove columns that are not being used
        columns_to_drop = [
            "productId",
            "url",
            "brandName",
            "stockState",
            "comingSoon",
            "isOnline",
            "materials"
        ]

        X.drop(
            columns=columns_to_drop,
            errors="ignore",
            inplace=True
        )

        # Remove duplicate columns if present
        X = X.loc[:, ~X.columns.duplicated()]

        # Extract features from details
        if "details" in X.columns:

            extracted = X["details"].apply(
                self.extract_features
            )

            extracted_df = pd.DataFrame(
                extracted.tolist(),
                index=X.index
            )

            X = pd.concat(
                [X, extracted_df],
                axis=1
            )

            X.drop(
                columns=["details"],
                inplace=True
            )

        # Clean color shades
        if "colorShades" in X.columns:

            X["colorShades"] = (
                X["colorShades"]
                .astype("string")
                .str.split("|", regex=False)
                .str[0]
            )

        # Extract color type
        if "color_description" in X.columns:

            X["colorType"] = (
                X["color_description"]
                .astype("string")
                .str.split(",")
                .str[1]
            )

        # Replace empty strings with missing values
        # Replace empty strings with missing values
        
# Replace empty strings with missing values
        X = X.replace(r"^\s*$", np.nan, regex=True)

        # Normalize data types and missing values
        for col in X.columns:

            # Convert boolean columns into integers
            if pd.api.types.is_bool_dtype(X[col]):

                X[col] = X[col].astype("int64")

            # Preserve numerical columns
            elif pd.api.types.is_numeric_dtype(X[col]):

                X[col] = pd.to_numeric(
                    X[col], errors="coerce"
                ).astype("float64")

            # Convert categorical columns into standard object dtype
            else:

                X[col] = X[col].astype(object)

                X[col] = X[col].where(
                    pd.notna(X[col]),
                    np.nan
                )

        # Remove duplicate columns
        X = X.loc[:, ~X.columns.duplicated()]

        return X
