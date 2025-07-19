# src/preprocessing.py
import pandas as pd
def drop_missing(df):
    return df.dropna()

def remove_duplicates(df):
    return df.drop_duplicates()

def fix_datetime(df):
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    return df
