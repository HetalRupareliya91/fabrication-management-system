"""SQLAlchemy model for Sales Orders."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class SalesOrder(Base):
    __tablename__ = "sales_orders"

    id = Column(Integer, primary_key=True, index=True)
    so_number = Column(String(255), nullable=False)
    customer_id = Column(Integer, nullable=False, default=0)
    order_date = Column(Date, nullable=True)
    delivery_date = Column(Date, nullable=True)
    status = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<SalesOrder id={self.id}>"
