"""Pydantic schemas for Suppliers."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SupplierBase(BaseModel):
    name: str
    gstin: str
    contact_person: str
    phone: str
    rating: int


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    gstin: Optional[str] = None
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    rating: Optional[int] = None


class SupplierRead(SupplierBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
