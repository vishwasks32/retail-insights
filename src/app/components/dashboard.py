# Dashboard component for Streamlit app
import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine
from ..config.settings import settings

def show_dashboard():
    st.header('Customer Data Dashboard')
    env = os.getenv('APP_ENV', 'dev')
    
    try:
        if env == 'prod':
            # Fetch data from MySQL in production
            df = _get_data_from_mysql()
        else:
            # Fallback to CSV in dev
            df = _get_data_from_csv()
        
        if df is not None and not df.empty:
            st.dataframe(df)
            st.subheader('Summary Statistics')
            st.write(df.describe(include='all'))
        else:
            st.warning('No customer data found.')
    except Exception as e:
        st.error(f'Error loading customer data: {str(e)}')

def _get_data_from_mysql():
    """Fetch customer data from MySQL database using AWS Secrets Manager credentials."""
    db_uri = settings.db_uri
    
    if not db_uri.startswith('mysql'):
        raise ValueError('Database URI is not configured for MySQL.')
    
    engine = create_engine(db_uri)
    
    query = "SELECT * FROM customers"
    df = pd.read_sql(query, engine)
    engine.dispose()
    
    return df

def _get_data_from_csv():
    """Fallback to CSV file for development."""
    processed_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'processed', 'customers_processed.csv')
    processed_path = os.path.normpath(processed_path)
    
    if os.path.exists(processed_path):
        return pd.read_csv(processed_path)
    else:
        st.warning('Processed customer data not found. Please run the ETL pipeline.')
        return None
