"""SQLAlchemy model for Inventory."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    material_code = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False, default=0.0)
    reorder_level = Column(Float, nullable=False, default=0.0)
    batch_no = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<InventoryItem id={self.id}>"
