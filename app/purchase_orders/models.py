"""SQLAlchemy model for Purchase Orders."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True, index=True)
    po_number = Column(String(255), nullable=False)
    supplier_id = Column(Integer, nullable=False, default=0)
    order_date = Column(Date, nullable=True)
    total_amount = Column(Float, nullable=False, default=0.0)
    status = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<PurchaseOrder id={self.id}>"
