"""Pydantic schemas for Customers."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    name: str
    gstin: str
    email: str
    phone: str
    city: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    gstin: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None


class CustomerRead(CustomerBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
