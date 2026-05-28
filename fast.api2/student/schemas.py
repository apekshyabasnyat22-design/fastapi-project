from pydantic import BaseModel, EmailStr
from typing import Optional, List

class StudentProfile(BaseModel):
    student_id: int
    username: str
    full_name: str
    email: EmailStr
    age: int
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    course: str
    semester: int
    cgpa: Optional[float] = None
    skills: List[str] = []
    is_active: bool = True
    bio: Optional[str] = None