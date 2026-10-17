"""SQLAlchemy model for Job Orders."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class JobOrder(Base):
    __tablename__ = "job_orders"

    id = Column(Integer, primary_key=True, index=True)
    job_number = Column(String(255), nullable=False)
    sales_order_id = Column(Integer, nullable=False, default=0)
    part_number = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    status = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<JobOrder id={self.id}>"
