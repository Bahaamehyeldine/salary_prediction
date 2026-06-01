# Data Science Salary Prediction App

An end-to-end machine learning application that predicts data science salaries based on job details, generates AI-powered analysis using a local LLM, and displays results on a live dashboard.

## Architecture

User Input → FastAPI → Decision Tree Model → Predicted Salary
                    → Ollama LLM → Narrative Analysis
                    → Supabase → Dashboard

## Tech Stack

- ML Model: Scikit-learn Decision Tree Regressor
- API: FastAPI + Uvicorn
- LLM: Ollama (llama3.2) local inference
- Database: Supabase (PostgreSQL)
- Dashboard: Streamlit
- Deployment: Railway (API) + Streamlit Cloud (Dashboard)
- Containerization: Docker

## Live Demo

- Streamlit Dashboard: https://salaryprediction-eyh9lgxhzb7uaq28hngndc.streamlit.app
- FastAPI Endpoint: https://salaryprediction-production-3285.up.railway.app

## Project Structure

salary_prediction/
├── api/
│   ├── main.py
│   ├── model.py
│   └── schema.py
├── src/
│   ├── dashboard.py
│   ├── database.py
│   └── llm.py
├── notebooks/
│   ├── eda.ipynb
│   ├── preprocessing.ipynb
│   └── model_training.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── Dockerfile
└── requirements.txt

## Dataset

Kaggle: Data Science Job Salaries — 607 rows, 12 features. Target: salary_in_usd

## How to Run Locally

git clone https://github.com/Bahaamehyeldine/salary_prediction.git
cd salary_prediction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Add your Supabase credentials to .env file, then:

ollama serve
uvicorn api.main:app --reload
streamlit run src/dashboard.py

## API Usage

curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"experience_level": 2, "job_title": 4, "work_year": 2022, "remote_ratio": 100, "company_location": 2, "company_size": 1}'

## Input Encoding

- experience_level: 0=Entry, 1=Mid, 2=Senior, 3=Executive
- job_title: 0=Data Analyst, 1=Data Architect, 2=Data Engineer, 3=Data Science Manager, 4=Data Scientist, 5=ML Engineer, 6=Other, 7=Research Scientist
- remote_ratio: 0=On-site, 50=Hybrid, 100=Remote
- company_location: 0=Low income, 1=Middle income, 2=High income
- company_size: 0=Small, 1=Medium, 2=Large

## Model Performance

- Algorithm: Decision Tree Regressor (max_depth=4)
- R2 Score: 0.38
- MAE: ~$36,000

## Author

Bahaamehyeldine
