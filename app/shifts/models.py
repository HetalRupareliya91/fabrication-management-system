"""SQLAlchemy model for Shifts."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    start_time = Column(String(255), nullable=False)
    end_time = Column(String(255), nullable=False)
    supervisor = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<Shift id={self.id}>"
