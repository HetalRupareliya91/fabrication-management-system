"""Pydantic schemas for Non-Conformance Reports."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class NonConformanceBase(BaseModel):
    ncr_number: str
    job_order_id: int
    description: str
    disposition: str
    closed: bool


class NonConformanceCreate(NonConformanceBase):
    pass


class NonConformanceUpdate(BaseModel):
    ncr_number: Optional[str] = None
    job_order_id: Optional[int] = None
    description: Optional[str] = None
    disposition: Optional[str] = None
    closed: Optional[bool] = None


class NonConformanceRead(NonConformanceBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
