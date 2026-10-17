"""Pydantic schemas for Bill of Materials."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BomLineBase(BaseModel):
    parent_part: str
    component_code: str
    quantity: float
    unit: str
    scrap_percent: float


class BomLineCreate(BomLineBase):
    pass


class BomLineUpdate(BaseModel):
    parent_part: Optional[str] = None
    component_code: Optional[str] = None
    quantity: Optional[float] = None
    unit: Optional[str] = None
    scrap_percent: Optional[float] = None


class BomLineRead(BomLineBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
