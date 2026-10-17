"""SQLAlchemy model for Quality Checks."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class QualityCheck(Base):
    __tablename__ = "quality_checks"

    id = Column(Integer, primary_key=True, index=True)
    job_order_id = Column(Integer, nullable=False, default=0)
    stage = Column(String(255), nullable=False)
    inspector = Column(String(255), nullable=False)
    result = Column(String(255), nullable=False)
    check_date = Column(Date, nullable=True)

    def __repr__(self) -> str:
        return f"<QualityCheck id={self.id}>"
