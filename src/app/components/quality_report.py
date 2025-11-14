# Quality report component for Streamlit app
import streamlit as st
import pandas as pd
import os

def show_quality_report():
    st.header('Customer Data Quality Report')
    processed_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'processed', 'customers_processed.csv')
    processed_path = os.path.normpath(processed_path)
    if os.path.exists(processed_path):
        df = pd.read_csv(processed_path)
        st.subheader('Missing Values by Column')
        st.write(df.isnull().sum())
        st.subheader('Duplicate Rows')
        st.write(f"{df.duplicated().sum()} duplicates found")
        st.subheader('Data Types')
        st.write(df.dtypes)
    else:
        st.warning('Processed customer data not found. Please run the ETL pipeline.')
