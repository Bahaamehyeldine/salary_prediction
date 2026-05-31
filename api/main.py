from fastapi import FastAPI
from api.schema import SalaryInput
from api.model import predict_salary
from src.llm import generate_analysis
from src.database import save_prediction

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict(input_data: SalaryInput):
    salary = predict_salary(input_data)
    analysis = generate_analysis(input_data, salary)
    save_prediction(input_data, salary, analysis)
    return {"predicted_salary_usd": salary, "analysis": analysis, "input_data": input_data.model_dump()}
