"""Pydantic schemas for Painting."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PaintingRecordBase(BaseModel):
    job_order_id: int
    paint_system: str
    dft_microns: float
    coats: int
    inspected: bool


class PaintingRecordCreate(PaintingRecordBase):
    pass


class PaintingRecordUpdate(BaseModel):
    job_order_id: Optional[int] = None
    paint_system: Optional[str] = None
    dft_microns: Optional[float] = None
    coats: Optional[int] = None
    inspected: Optional[bool] = None


class PaintingRecordRead(PaintingRecordBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
