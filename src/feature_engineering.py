# src/feature_engineering.py
import pandas as pd
import ipaddress

def add_time_features(df):
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600
    return df

def ip_to_int(ip):
    return int(ipaddress.IPv4Address(ip))

    df['country'] = df['ip_int'].apply(lookup_country)
    return df
