from pydantic import BaseModel
from typing import List, Dict

class Student(BaseModel):
    name: str
    grades: List[float]

class StudentResult(BaseModel):
    average: float
    rank: str

class StudentResponse(BaseModel):
    name: str
    info: StudentResult
