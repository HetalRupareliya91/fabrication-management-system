"""Pydantic schemas for Drawings."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DrawingBase(BaseModel):
    drawing_number: str
    revision: str
    title: str
    approved: bool
    customer_id: int


class DrawingCreate(DrawingBase):
    pass


class DrawingUpdate(BaseModel):
    drawing_number: Optional[str] = None
    revision: Optional[str] = None
    title: Optional[str] = None
    approved: Optional[bool] = None
    customer_id: Optional[int] = None


class DrawingRead(DrawingBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
