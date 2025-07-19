# src/transformation.py
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import pandas as pd

def encode_categorical(df):
    return pd.get_dummies(df, drop_first=True)

def scale_features(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X), scaler

def apply_smote(X, y):
    smote = SMOTE(random_state=42)
    return smote.fit_resample(X, y)

def split_data(X, y, test_size=0.3):
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=42)
