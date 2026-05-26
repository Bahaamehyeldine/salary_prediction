from pydantic import BaseModel,  Field

class SalaryInput(BaseModel):
    experience_level: int = Field(...,ge=0, le=3)
    job_title: int = Field(...,ge=0, le=7)
    work_year: int = Field(...,ge=2020, le=2022)
    remote_ratio: int = Field(...,ge=0, le=100)
    company_location: int = Field(...,ge=0, le=2)
    company_size: int = Field(...,ge=0, le=2)
    