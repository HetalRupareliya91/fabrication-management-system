"""SQLAlchemy model for Production Logs."""
from sqlalchemy import Boolean, Column, Date, Float, Integer, String

from app.core.database import Base


class ProductionLog(Base):
    __tablename__ = "production_logs"

    id = Column(Integer, primary_key=True, index=True)
    job_order_id = Column(Integer, nullable=False, default=0)
    operator_id = Column(Integer, nullable=False, default=0)
    quantity_done = Column(Integer, nullable=False, default=0)
    remarks = Column(String(255), nullable=False)
    log_date = Column(Date, nullable=True)

    def __repr__(self) -> str:
        return f"<ProductionLog id={self.id}>"
