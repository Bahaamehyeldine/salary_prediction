from fastapi import FastAPI
from api.schema import SalaryInput
from api.model import predict_salary
from src.llm import generate_analysis

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(input_data: SalaryInput):
    salary = predict_salary(input_data)
    analysis = generate_analysis(input_data, salary)
    return {"predicted_salary_usd": salary, "analysis": analysis}