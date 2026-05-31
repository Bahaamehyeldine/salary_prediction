import ollama

client = ollama.Client(host="http://host.docker.internal:11434")

def generate_analysis(input_data, predicted_salary: float) -> str:
    experience_map = {0: "Entry", 1: "Mid", 2: "Senior", 3: "Executive"}
    company_size_map = {0: "Small", 1: "Medium", 2: "Large"}
    company_location_map = {0: "Low income country", 1: "Middle income country", 2: "High income country"}
    remote_map = {0: "On-site", 50: "Hybrid", 100: "Fully remote"}

    prompt = f"""
    You are a data analyst specializing in data science compensation.
    A salary prediction model has predicted the following:

    - Experience Level: {experience_map[input_data.experience_level]}
    - Job Title Code: {input_data.job_title}
    - Work Year: {input_data.work_year}
    - Remote Work: {remote_map[input_data.remote_ratio]}
    - Company Location: {company_location_map[input_data.company_location]}
    - Company Size: {company_size_map[input_data.company_size]}
    - Predicted Salary: ${predicted_salary:,.2f}

    Please provide a concise analysis (3-4 sentences) covering:
    1. Whether this salary is competitive for this profile
    2. Which factors are most influencing this salary
    3. One actionable insight for the employee
    """
    response = client.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']
