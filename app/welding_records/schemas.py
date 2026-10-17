"""Pydantic schemas for Welding Records."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class WeldingRecordBase(BaseModel):
    job_order_id: int
    welder_id: int
    wps_number: str
    joint_id: str
    passed: bool


class WeldingRecordCreate(WeldingRecordBase):
    pass


class WeldingRecordUpdate(BaseModel):
    job_order_id: Optional[int] = None
    welder_id: Optional[int] = None
    wps_number: Optional[str] = None
    joint_id: Optional[str] = None
    passed: Optional[bool] = None


class WeldingRecordRead(WeldingRecordBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
