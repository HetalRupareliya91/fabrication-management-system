"""SQLAlchemy model for Invoices."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(255), nullable=False)
    sales_order_id = Column(Integer, nullable=False, default=0)
    invoice_date = Column(Date, nullable=True)
    amount = Column(Float, nullable=False, default=0.0)
    paid = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<Invoice id={self.id}>"
