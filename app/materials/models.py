"""SQLAlchemy model for Materials."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    grade = Column(String(255), nullable=False)
    thickness_mm = Column(Float, nullable=False, default=0.0)
    unit = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Material id={self.id}>"
