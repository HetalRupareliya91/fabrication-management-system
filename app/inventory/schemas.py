"""Pydantic schemas for Inventory."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class InventoryItemBase(BaseModel):
    material_code: str
    location: str
    quantity: float
    reorder_level: float
    batch_no: str


class InventoryItemCreate(InventoryItemBase):
    pass


class InventoryItemUpdate(BaseModel):
    material_code: Optional[str] = None
    location: Optional[str] = None
    quantity: Optional[float] = None
    reorder_level: Optional[float] = None
    batch_no: Optional[str] = None


class InventoryItemRead(InventoryItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
