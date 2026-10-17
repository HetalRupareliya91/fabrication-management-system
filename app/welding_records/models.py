"""SQLAlchemy model for Welding Records."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class WeldingRecord(Base):
    __tablename__ = "welding_records"

    id = Column(Integer, primary_key=True, index=True)
    job_order_id = Column(Integer, nullable=False, default=0)
    welder_id = Column(Integer, nullable=False, default=0)
    wps_number = Column(String(255), nullable=False)
    joint_id = Column(String(255), nullable=False)
    passed = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<WeldingRecord id={self.id}>"
