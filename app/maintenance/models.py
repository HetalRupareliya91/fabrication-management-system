"""SQLAlchemy model for Maintenance."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class MaintenanceTask(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer, nullable=False, default=0)
    maintenance_type = Column(String(255), nullable=False)
    scheduled_on = Column(Date, nullable=True)
    completed = Column(Boolean, nullable=False, default=False)
    remarks = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<MaintenanceTask id={self.id}>"
