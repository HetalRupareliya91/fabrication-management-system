"""Pydantic schemas for Machines."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MachineBase(BaseModel):
    machine_code: str
    name: str
    work_center_id: int
    make: str
    commissioned_on: Optional[date] = None


class MachineCreate(MachineBase):
    pass


class MachineUpdate(BaseModel):
    machine_code: Optional[str] = None
    name: Optional[str] = None
    work_center_id: Optional[int] = None
    make: Optional[str] = None
    commissioned_on: Optional[date] = None


class MachineRead(MachineBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
