"""SQLAlchemy model for Operators."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Operator(Base):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True, index=True)
    employee_code = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    skill = Column(String(255), nullable=False)
    certification = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<Operator id={self.id}>"
