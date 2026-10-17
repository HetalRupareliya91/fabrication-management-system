"""SQLAlchemy model for Bill of Materials."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class BomLine(Base):
    __tablename__ = "bom"

    id = Column(Integer, primary_key=True, index=True)
    parent_part = Column(String(255), nullable=False)
    component_code = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False, default=0.0)
    unit = Column(String(255), nullable=False)
    scrap_percent = Column(Float, nullable=False, default=0.0)

    def __repr__(self) -> str:
        return f"<BomLine id={self.id}>"
