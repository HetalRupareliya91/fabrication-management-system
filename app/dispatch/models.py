"""SQLAlchemy model for Dispatch."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Dispatch(Base):
    __tablename__ = "dispatch"

    id = Column(Integer, primary_key=True, index=True)
    dispatch_number = Column(String(255), nullable=False)
    sales_order_id = Column(Integer, nullable=False, default=0)
    vehicle_number = Column(String(255), nullable=False)
    dispatch_date = Column(Date, nullable=True)
    weight_kg = Column(Float, nullable=False, default=0.0)

    def __repr__(self) -> str:
        return f"<Dispatch id={self.id}>"
