# Data cleaning utilities
import pandas as pd

def clean_data(df):
    # Drop duplicate rows
    df = df.drop_duplicates()
    # Strip whitespace from string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    # Fill missing values with empty string for object columns, 0 for numeric
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('')
        else:
            df[col] = df[col].fillna(0)
    return df
