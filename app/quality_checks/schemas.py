"""Pydantic schemas for Quality Checks."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class QualityCheckBase(BaseModel):
    job_order_id: int
    stage: str
    inspector: str
    result: str
    check_date: Optional[date] = None


class QualityCheckCreate(QualityCheckBase):
    pass


class QualityCheckUpdate(BaseModel):
    job_order_id: Optional[int] = None
    stage: Optional[str] = None
    inspector: Optional[str] = None
    result: Optional[str] = None
    check_date: Optional[date] = None


class QualityCheckRead(QualityCheckBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
