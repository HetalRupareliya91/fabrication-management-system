"""SQLAlchemy model for Quotations."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Quotation(Base):
    __tablename__ = "quotations"

    id = Column(Integer, primary_key=True, index=True)
    quote_number = Column(String(255), nullable=False)
    customer_id = Column(Integer, nullable=False, default=0)
    valid_until = Column(Date, nullable=True)
    amount = Column(Float, nullable=False, default=0.0)
    status = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Quotation id={self.id}>"
