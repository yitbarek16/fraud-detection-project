# Fraud Detection Project

This project detects fraudulent transactions using machine learning and explainability techniques like SHAP. It covers data ingestion, cleaning, feature engineering, modeling, and interpretation.

## Project Structure

```
fraud-detection-project/
├── data/
│   ├── Fraud_Data.csv
│   ├── IpAddress_to_Country.csv
│   └── creditcard.csv
├── models/
├── notebooks/
│   ├── 01_data_loading_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_data_transformation.ipynb
|   └── 05_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   └── eda.py
│
├── requirements.txt
└── README.md
```

## Data Sources

- `Fraud_Data.csv`: Main dataset containing transaction records and fraud labels.
- `IpAddress_to_Country.csv`: Mapping of IP addresses to countries.
- `creditcard.csv`: Additional credit card transaction data.

## Setup

1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies** (recommended: use a virtual environment):

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure data files** are placed in the `data/` directory at the project root.

---

## Data Cleaning & Preprocessing

For cleaning, I:
- Dropped missing values
- Removed duplicate records
- Fixed datetime formats

I handled these steps using functions in `src/preprocessing.py`:

```python
from src.preprocessing import drop_missing, remove_duplicates, fix_datetime

fraud_df = drop_missing(fraud_df)
fraud_df = remove_duplicates(fraud_df)
fraud_df = fix_datetime(fraud_df)
```
---

## Exploratory Data Analysis (EDA)

- **Fraud Rates:**  
  - E-commerce fraud rate: ~9.36%  
  - Bank fraud rate: ~0.17%  
  - → E-commerce is far more vulnerable to fraud.

- **Numerical Features:**  
  - `purchase_value`, `age`, `hour_of_day`, `day_of_week`: Little difference across fraud vs non-fraud.
  - `time_since_signup`:  
    - Fraud mean: ~1330 hrs  
    - Non-fraud mean: ~2161 hrs  
    - Strong negative correlation with fraud (-0.26)  
    - → Most predictive numerical feature.

- **Categorical Features:**  
  - `source`: "Direct" traffic users show the highest fraud rate (~10.5%)
  - `browser` and `sex`: Minimal differences, limited predictive power.

- **Top Fraud-Prone Countries:**  
  | Country                | Fraud Rate |
  |------------------------|------------|
  | Virgin Islands (U.S.)  | 1.00       |
  | Turkmenistan           | 1.00       |
  | Luxembourg             | 0.56       |
  | Sri Lanka              | 0.52       |
  | Kuwait                 | 0.28       |

---

## Feature Engineering

I engineered features including:

- **Time-based:**  
  - `hour_of_day`, `day_of_week`, `time_since_signup`
- **User behavior:**  
  - `ip_user_count`, `device_user_count`
- **Risk indicators:**  
  - `country_risk`: Fraud rate per country
- **Encoding:**  
  - Categorical features encoded using `LabelEncoder` or `OneHotEncoder`

The resulting dataset is saved as:  
`data/fraud_with_features.csv`

---

## Data Transformation

I transformed the data for modeling by:

- Feature scaling (e.g., StandardScaler or MinMaxScaler)
- Encoding categorical variables
- Splitting data into train/test sets
  
###  Handling Class Imbalance

Fraud detection is inherently an imbalanced classification problem. In this dataset:

- **Non-Fraud class (0):** ~90.6%
- **Fraud class (1):** ~9.4%

This imbalance can cause models to bias heavily toward predicting the majority class (non-fraud).

To address this:

- I applied **SMOTE (Synthetic Minority Oversampling Technique)** to the training data to synthetically generate more fraud cases.
- SMOTE was applied **only on the training set** to avoid data leakage into evaluation.
- For some models (e.g., Logistic Regression), I also experimented with using `class_weight='balanced'` to account for imbalance during training.

This improves the model’s sensitivity to fraudulent transactions and ensures fairer evaluation.

I saved the transformed datasets as CSV files in the `data/` directory for use in modeling notebooks:

- `X_train_scaled.csv`
- `X_test_scaled.csv`
- `y_train_resampled.csv`
- `y_test.csv`

---
## Model Comparison and Selection

I evaluated two models on the fraud detection task:

- **Logistic Regression** (baseline model)
- **XGBoost** (ensemble model)

### Performance Summary

| Metric             | Logistic Regression | XGBoost        |
|--------------------|---------------------|----------------|
| F1 Score           | 0.5871              | **0.6010**     |
| AUC-PR             | **0.6676**          | 0.6611         |
| Accuracy           | 0.92                | **0.93**       |
| Precision (Class 1)| 0.57                | **0.63**       |
| Recall (Class 1)   | **0.61**            | 0.57           |

### Final Model Selection: **XGBoost**

Despite Logistic Regression performing slightly better in AUC-PR, **XGBoost** is chosen as the final model because:

- It achieved a higher **F1 Score**, indicating better balance between precision and recall.
- It had **higher precision**, meaning fewer false alarms.
- It captured more nuanced patterns due to its ability to handle non-linear relationships.

In fraud detection, both high precision and reasonable recall are vital, making **XGBoost the preferred model**.

---

---

## Next Steps: Model Explainability

My next step is to interpret the predictions of the final XGBoost model using SHAP (Shapley Additive Explanations):

- **Global Interpretability:**  
  I will use SHAP summary plots to visualize which features most influence fraud predictions across the dataset.

- **Local Interpretability:**  
  I will generate SHAP force plots to explain individual predictions and understand why specific transactions are flagged as fraud.

This will help me validate the model’s decisions,
