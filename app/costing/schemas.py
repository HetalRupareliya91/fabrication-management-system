"""Pydantic schemas for Job Costing."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class JobCostBase(BaseModel):
    job_order_id: int
    currency: str
    material_cost: float
    labour_cost: float
    total_cost: float


class JobCostCreate(JobCostBase):
    pass


class JobCostUpdate(BaseModel):
    job_order_id: Optional[int] = None
    currency: Optional[str] = None
    material_cost: Optional[float] = None
    labour_cost: Optional[float] = None
    total_cost: Optional[float] = None


class JobCostRead(JobCostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
