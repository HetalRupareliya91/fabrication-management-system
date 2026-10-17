"""Pydantic schemas for Quotations."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class QuotationBase(BaseModel):
    quote_number: str
    customer_id: int
    valid_until: Optional[date] = None
    amount: float
    status: str


class QuotationCreate(QuotationBase):
    pass


class QuotationUpdate(BaseModel):
    quote_number: Optional[str] = None
    customer_id: Optional[int] = None
    valid_until: Optional[date] = None
    amount: Optional[float] = None
    status: Optional[str] = None


class QuotationRead(QuotationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
