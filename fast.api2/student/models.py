from sqlalchemy import Column, Integer, String, Float, Boolean
from databases import Base

class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    course = Column(String, nullable=False)
    gpa = Column(Float, nullable=False)