from supabase import create_client
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def save_prediction(input_data, predicted_salary: float, analysis: str):
    try:
        supabase.table("predictions").insert({
            "experience_level": input_data.experience_level,
            "job_title": input_data.job_title,
            "work_year": input_data.work_year,
            "remote_ratio": input_data.remote_ratio,
            "company_location": input_data.company_location,
            "company_size": input_data.company_size,
            "predicted_salary": predicted_salary,
            "analysis": analysis
        }).execute()
    except Exception as e:
        print(f"Supabase error: {e}")
