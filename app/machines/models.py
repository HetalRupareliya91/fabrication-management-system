"""SQLAlchemy model for Machines."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_code = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    work_center_id = Column(Integer, nullable=False, default=0)
    make = Column(String(255), nullable=False)
    commissioned_on = Column(Date, nullable=True)

    def __repr__(self) -> str:
        return f"<Machine id={self.id}>"
