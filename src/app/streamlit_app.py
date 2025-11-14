# Streamlit app entry point
import streamlit as st


from app.components.dashboard import show_dashboard
from app.components.quality_report import show_quality_report

def main():
    st.title('Retail Insights Dashboard')
    menu = ["Dashboard", "Quality Report"]
    choice = st.sidebar.selectbox("Select View", menu)
    if choice == "Dashboard":
        show_dashboard()
    elif choice == "Quality Report":
        show_quality_report()

if __name__ == '__main__':
    main()
