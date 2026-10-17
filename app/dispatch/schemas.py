"""Pydantic schemas for Dispatch."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DispatchBase(BaseModel):
    dispatch_number: str
    sales_order_id: int
    vehicle_number: str
    dispatch_date: Optional[date] = None
    weight_kg: float


class DispatchCreate(DispatchBase):
    pass


class DispatchUpdate(BaseModel):
    dispatch_number: Optional[str] = None
    sales_order_id: Optional[int] = None
    vehicle_number: Optional[str] = None
    dispatch_date: Optional[date] = None
    weight_kg: Optional[float] = None


class DispatchRead(DispatchBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
