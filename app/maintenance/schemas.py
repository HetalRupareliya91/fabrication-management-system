"""Pydantic schemas for Maintenance."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MaintenanceTaskBase(BaseModel):
    machine_id: int
    maintenance_type: str
    scheduled_on: Optional[date] = None
    completed: bool
    remarks: str


class MaintenanceTaskCreate(MaintenanceTaskBase):
    pass


class MaintenanceTaskUpdate(BaseModel):
    machine_id: Optional[int] = None
    maintenance_type: Optional[str] = None
    scheduled_on: Optional[date] = None
    completed: Optional[bool] = None
    remarks: Optional[str] = None


class MaintenanceTaskRead(MaintenanceTaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
