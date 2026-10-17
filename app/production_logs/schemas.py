"""Pydantic schemas for Production Logs."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProductionLogBase(BaseModel):
    job_order_id: int
    operator_id: int
    quantity_done: int
    remarks: str
    log_date: Optional[date] = None


class ProductionLogCreate(ProductionLogBase):
    pass


class ProductionLogUpdate(BaseModel):
    job_order_id: Optional[int] = None
    operator_id: Optional[int] = None
    quantity_done: Optional[int] = None
    remarks: Optional[str] = None
    log_date: Optional[date] = None


class ProductionLogRead(ProductionLogBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
