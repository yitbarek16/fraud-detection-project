# src/transformation.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def encode_categorical(df):
    """Apply one-hot encoding to object columns."""
    return pd.get_dummies(df, drop_first=True)

def scale_features(X):
    """Standard scale numeric features."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return pd.DataFrame(X_scaled, columns=X.columns), scaler

def apply_smote(X, y):
    """Apply SMOTE to balance the dataset."""
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    return pd.DataFrame(X_resampled, columns=X.columns), pd.Series(y_resampled)

def split_data(X, y, test_size=0.2):
    """Split into train/test sets with stratification."""
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=42)
