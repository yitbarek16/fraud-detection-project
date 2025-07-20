# src/preprocessing.py

import pandas as pd

def drop_missing(df):
    """
    Remove rows with missing values from the DataFrame.
    """
    return df.dropna()

def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """
    return df.drop_duplicates()

def fix_datetime(df):
    """
    Convert 'signup_time' and 'purchase_time' columns to datetime objects.
    """
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    return df
