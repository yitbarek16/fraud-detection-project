# src/feature_engineering.py

import pandas as pd
import ipaddress

def add_time_features(df):
    """
    Add time-based features such as hour of day, day of week, and time since signup.
    """
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600
    return df

def ip_to_int(ip):
    """
    Convert an IP address string to its integer representation.
    """
    return int(ipaddress.IPv4Address(ip))
