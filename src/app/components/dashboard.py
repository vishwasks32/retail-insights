# Dashboard component for Streamlit app
import streamlit as st
import pandas as pd
import os

def show_dashboard():
    st.header('Customer Data Dashboard')
    processed_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'processed', 'customers_processed.csv')
    processed_path = os.path.normpath(processed_path)
    if os.path.exists(processed_path):
        df = pd.read_csv(processed_path)
        st.dataframe(df)
        st.subheader('Summary Statistics')
        st.write(df.describe(include='all'))
    else:
        st.warning('Processed customer data not found. Please run the ETL pipeline.')
