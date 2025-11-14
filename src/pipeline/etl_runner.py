# ETL Runner for Retail Insights

import os
import sys
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.extract.csv_extractor import CSVExtractor
from src.transform.cleaner import clean_data
from src.transform.feature_engineering import add_total_price, extract_date_features
from src.transform.validators import validate_no_missing

def run_etl(input_csv, output_path):
    # 1. Extract
    extractor = CSVExtractor()
    df = extractor.extract(input_csv)
    if df is None or df.empty:
        print(f"No data extracted from {input_csv}")
        return False

    # 2. Clean
    df = clean_data(df)

    # 3. Feature Engineering
    df = add_total_price(df)
    df = extract_date_features(df)

    # 4. Validate
    if not validate_no_missing(df):
        print("Validation failed: missing values present.")
        return False

    # 5. Ensure consistent column types (convert all object columns to string)
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"ETL completed. Output saved to {output_path}")
    return True

if __name__ == "__main__":
    # Always use the correct absolute path for raw and processed data
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    input_csv = os.path.join(base_dir, 'data', 'raw', 'customers.csv')
    output_path = os.path.join(base_dir, 'data', 'processed', 'customers_processed.csv')
    run_etl(input_csv, output_path)