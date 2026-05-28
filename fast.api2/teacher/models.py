#models.py
from sqlalchemy import Column, Integer, String, Float
from databases import Base
from sqlalchemy.orm import Mapped, mapped_column

class TeacherModel(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[int] = mapped_column(Integer, default=1)  
    bio: Mapped[str] = mapped_column(String(255), nullable=True)
    full_name: Mapped[str] = mapped_column(String(255))
    subject: Mapped[str] = mapped_column(String(255))
    qualification: Mapped[str] = mapped_column(String(255))
    experience_years: Mapped[int] = mapped_column(Integer, nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)