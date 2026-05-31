import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st

st.set_page_config(page_title="Salary Prediction App", layout="wide")
st.title("Data Science Salary Predictor")
st.markdown("Enter job details to predict salary and get AI-powered insights.")

experience = st.selectbox(
    "Experience Level",
    options=[0, 1, 2, 3],
    format_func=lambda x: {0: "Entry", 1: "Mid", 2: "Senior", 3: "Executive"}[x]
)

job_title = st.selectbox(
    "Job Title",
    options=[0, 1, 2, 3, 4, 5, 6, 7],
    format_func=lambda x: {0: "Data Analyst", 1: "Data Architect", 2: "Data Engineer", 
 3: "Data Science Manager", 4: "Data Scientist", 
 5: "Machine Learning Engineer", 6: "Other", 7: "Research Scientist"}[x]
)

work_year = st.selectbox("Work Year", 
                         options=[2020, 2021, 2022],
                            format_func=lambda x: str(x))

remote_ratio = st.selectbox(
    "Remote Work Ratio",
    options=[0, 50, 100],
    format_func=lambda x: {0: "On-site", 50: "Hybrid", 100: "Fully remote"}[x]
)   

company_location = st.selectbox(
    "Company Location",
    options=[0, 1, 2],
    format_func=lambda x: {0: "Low", 1: "Middle", 2: "High"}[x]
)

company_size = st.selectbox(
    "Company Size",
    options=[0, 1, 2],
    format_func=lambda x: {0: "Small", 1: "Medium", 2: "Large"}[x]
)       

import requests

if st.button("Predict Salary"):
    payload = {
        "experience_level": experience,
        "job_title": job_title,
        "work_year": work_year,
        "remote_ratio": remote_ratio,
        "company_location": company_location,
        "company_size": company_size
    }
    
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Salary: ${result['predicted_salary_usd']:,.2f}")
        st.markdown("### AI Analysis")
        st.write(result['analysis'])
    else:
        st.error("Something went wrong. Please try again.")


st.markdown("---")
st.markdown("### Past Predictions")

from src.database import supabase

predictions = supabase.table("predictions").select("*").execute().data

if predictions:
    st.dataframe(predictions)
else:
    st.write("No predictions yet.")