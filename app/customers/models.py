"""SQLAlchemy model for Customers."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    gstin = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Customer id={self.id}>"
