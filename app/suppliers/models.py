"""SQLAlchemy model for Suppliers."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    gstin = Column(String(255), nullable=False)
    contact_person = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<Supplier id={self.id}>"
