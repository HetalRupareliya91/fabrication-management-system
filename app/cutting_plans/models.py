"""SQLAlchemy model for Cutting Plans."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class CuttingPlan(Base):
    __tablename__ = "cutting_plans"

    id = Column(Integer, primary_key=True, index=True)
    plan_number = Column(String(255), nullable=False)
    job_order_id = Column(Integer, nullable=False, default=0)
    sheet_size = Column(String(255), nullable=False)
    utilization_percent = Column(Float, nullable=False, default=0.0)
    status = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<CuttingPlan id={self.id}>"
