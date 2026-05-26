import joblib
import numpy as np
from pathlib import Path
from api.schema import SalaryInput

BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR / "models" / "decision_tree_model.pkl")

def predict_salary(input_data: SalaryInput) -> float:
    features = np.array([[
        input_data.work_year,
        input_data.experience_level,
        input_data.job_title,
        input_data.remote_ratio,
        input_data.company_location,
        input_data.company_size
    ]])
    prediction = model.predict(features)
    return float(prediction[0])