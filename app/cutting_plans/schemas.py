"""Pydantic schemas for Cutting Plans."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CuttingPlanBase(BaseModel):
    plan_number: str
    job_order_id: int
    sheet_size: str
    utilization_percent: float
    status: str


class CuttingPlanCreate(CuttingPlanBase):
    pass


class CuttingPlanUpdate(BaseModel):
    plan_number: Optional[str] = None
    job_order_id: Optional[int] = None
    sheet_size: Optional[str] = None
    utilization_percent: Optional[float] = None
    status: Optional[str] = None


class CuttingPlanRead(CuttingPlanBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
