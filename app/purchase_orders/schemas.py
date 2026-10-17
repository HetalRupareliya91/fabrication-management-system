"""Pydantic schemas for Purchase Orders."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PurchaseOrderBase(BaseModel):
    po_number: str
    supplier_id: int
    order_date: Optional[date] = None
    total_amount: float
    status: str


class PurchaseOrderCreate(PurchaseOrderBase):
    pass


class PurchaseOrderUpdate(BaseModel):
    po_number: Optional[str] = None
    supplier_id: Optional[int] = None
    order_date: Optional[date] = None
    total_amount: Optional[float] = None
    status: Optional[str] = None


class PurchaseOrderRead(PurchaseOrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
