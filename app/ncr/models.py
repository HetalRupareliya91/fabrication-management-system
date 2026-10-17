"""SQLAlchemy model for Non-Conformance Reports."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class NonConformance(Base):
    __tablename__ = "ncr"

    id = Column(Integer, primary_key=True, index=True)
    ncr_number = Column(String(255), nullable=False)
    job_order_id = Column(Integer, nullable=False, default=0)
    description = Column(String(255), nullable=False)
    disposition = Column(String(255), nullable=False)
    closed = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<NonConformance id={self.id}>"
