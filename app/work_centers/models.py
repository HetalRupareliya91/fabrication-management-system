"""SQLAlchemy model for Work Centers."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class WorkCenter(Base):
    __tablename__ = "work_centers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    capacity_hours = Column(Float, nullable=False, default=0.0)
    cost_per_hour = Column(Float, nullable=False, default=0.0)
    is_active = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<WorkCenter id={self.id}>"
