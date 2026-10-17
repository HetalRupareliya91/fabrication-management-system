"""Pydantic schemas for Routings."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RoutingStepBase(BaseModel):
    part_number: str
    sequence: int
    operation: str
    work_center_id: int
    std_minutes: float


class RoutingStepCreate(RoutingStepBase):
    pass


class RoutingStepUpdate(BaseModel):
    part_number: Optional[str] = None
    sequence: Optional[int] = None
    operation: Optional[str] = None
    work_center_id: Optional[int] = None
    std_minutes: Optional[float] = None


class RoutingStepRead(RoutingStepBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
