"""SQLAlchemy model for Job Costing."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class JobCost(Base):
    __tablename__ = "costing"

    id = Column(Integer, primary_key=True, index=True)
    job_order_id = Column(Integer, nullable=False, default=0)
    currency = Column(String(255), nullable=False)
    material_cost = Column(Float, nullable=False, default=0.0)
    labour_cost = Column(Float, nullable=False, default=0.0)
    total_cost = Column(Float, nullable=False, default=0.0)

    def __repr__(self) -> str:
        return f"<JobCost id={self.id}>"
