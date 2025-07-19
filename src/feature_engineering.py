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

def merge_country(df, ip_df):
    df['ip_int'] = df['ip_address'].apply(ip_to_int)
    ip_df['lower_ip'] = ip_df['lower_bound_ip_address'].apply(ip_to_int)
    ip_df['upper_ip'] = ip_df['upper_bound_ip_address'].apply(ip_to_int)

    def lookup_country(ip):
        match = ip_df[(ip_df['lower_ip'] <= ip) & (ip_df['upper_ip'] >= ip)]
        return match['country'].values[0] if not match.empty else 'Unknown'

    df['country'] = df['ip_int'].apply(lookup_country)
    return df
