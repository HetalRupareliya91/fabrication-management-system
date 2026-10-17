"""Pydantic schemas for Job Orders."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class JobOrderBase(BaseModel):
    job_number: str
    sales_order_id: int
    part_number: str
    quantity: int
    status: str


class JobOrderCreate(JobOrderBase):
    pass


class JobOrderUpdate(BaseModel):
    job_number: Optional[str] = None
    sales_order_id: Optional[int] = None
    part_number: Optional[str] = None
    quantity: Optional[int] = None
    status: Optional[str] = None


class JobOrderRead(JobOrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
