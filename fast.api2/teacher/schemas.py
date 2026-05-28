from pydantic import BaseModel
from typing import Optional


class TeacherProfile(BaseModel):
    id: int
    username: str
    email: str
    age: int
    is_active: bool = True
    bio: Optional[str] = None
    full_name: str
    address: str
    subject: str
    qualification: str
    experience_years: int
    salary: float