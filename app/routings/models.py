"""SQLAlchemy model for Routings."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class RoutingStep(Base):
    __tablename__ = "routings"

    id = Column(Integer, primary_key=True, index=True)
    part_number = Column(String(255), nullable=False)
    sequence = Column(Integer, nullable=False, default=0)
    operation = Column(String(255), nullable=False)
    work_center_id = Column(Integer, nullable=False, default=0)
    std_minutes = Column(Float, nullable=False, default=0.0)

    def __repr__(self) -> str:
        return f"<RoutingStep id={self.id}>"
