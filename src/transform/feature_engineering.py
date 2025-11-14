# Feature engineering utilities
import pandas as pd

def add_total_price(df, quantity_col='quantity', price_col='price', new_col='total_price'):
    """Add a total price column (quantity * price) if columns exist."""
    if quantity_col in df.columns and price_col in df.columns:
        df[new_col] = df[quantity_col] * df[price_col]
    return df

def extract_date_features(df, date_col='order_date'):
    """Extract year, month, day from a date column if it exists."""
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        df['year'] = df[date_col].dt.year
        df['month'] = df[date_col].dt.month
        df['day'] = df[date_col].dt.day
    return df
# Feature engineering utilities
def engineer_features(df):
    # Implement feature engineering logic
    return df
