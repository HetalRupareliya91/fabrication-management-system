"""Pydantic schemas for Invoices."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class InvoiceBase(BaseModel):
    invoice_number: str
    sales_order_id: int
    invoice_date: Optional[date] = None
    amount: float
    paid: bool


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(BaseModel):
    invoice_number: Optional[str] = None
    sales_order_id: Optional[int] = None
    invoice_date: Optional[date] = None
    amount: Optional[float] = None
    paid: Optional[bool] = None


class InvoiceRead(InvoiceBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
