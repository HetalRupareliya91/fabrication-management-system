"""SQLAlchemy model for Drawings."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Drawing(Base):
    __tablename__ = "drawings"

    id = Column(Integer, primary_key=True, index=True)
    drawing_number = Column(String(255), nullable=False)
    revision = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    approved = Column(Boolean, nullable=False, default=False)
    customer_id = Column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<Drawing id={self.id}>"
