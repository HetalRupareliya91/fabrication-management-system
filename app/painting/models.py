"""SQLAlchemy model for Painting."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class PaintingRecord(Base):
    __tablename__ = "painting"

    id = Column(Integer, primary_key=True, index=True)
    job_order_id = Column(Integer, nullable=False, default=0)
    paint_system = Column(String(255), nullable=False)
    dft_microns = Column(Float, nullable=False, default=0.0)
    coats = Column(Integer, nullable=False, default=0)
    inspected = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<PaintingRecord id={self.id}>"
