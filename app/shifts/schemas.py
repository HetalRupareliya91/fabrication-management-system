"""Pydantic schemas for Shifts."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ShiftBase(BaseModel):
    name: str
    start_time: str
    end_time: str
    supervisor: str
    is_active: bool


class ShiftCreate(ShiftBase):
    pass


class ShiftUpdate(BaseModel):
    name: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    supervisor: Optional[str] = None
    is_active: Optional[bool] = None


class ShiftRead(ShiftBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
