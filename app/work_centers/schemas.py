"""Pydantic schemas for Work Centers."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class WorkCenterBase(BaseModel):
    code: str
    name: str
    capacity_hours: float
    cost_per_hour: float
    is_active: bool


class WorkCenterCreate(WorkCenterBase):
    pass


class WorkCenterUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    capacity_hours: Optional[float] = None
    cost_per_hour: Optional[float] = None
    is_active: Optional[bool] = None


class WorkCenterRead(WorkCenterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
