# Data validation utilities
import pandas as pd

def validate_no_missing(df, columns=None):
    """Return True if no missing values in specified columns (or all if None)."""
    if columns is None:
        columns = df.columns
    return df[columns].isnull().sum().sum() == 0

def validate_column_types(df, expected_types):
    """
    expected_types: dict of column_name: type (e.g., {'price': float, 'name': str})
    Returns True if all columns match expected types.
    """
    for col, typ in expected_types.items():
        if col in df.columns:
            if not df[col].map(lambda x: isinstance(x, typ) or pd.isnull(x)).all():
                return False
    return True

def validate_value_range(df, column, min_value=None, max_value=None):
    """Return True if all values in column are within [min_value, max_value]."""
    if column not in df.columns:
        return False
    series = df[column].dropna()
    if min_value is not None and (series < min_value).any():
        return False
    if max_value is not None and (series > max_value).any():
        return False
    return True
# Data validation utilities
def validate_data(df):
    # Implement validation logic
    return True
