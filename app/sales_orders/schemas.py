"""Pydantic schemas for Sales Orders."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SalesOrderBase(BaseModel):
    so_number: str
    customer_id: int
    order_date: Optional[date] = None
    delivery_date: Optional[date] = None
    status: str


class SalesOrderCreate(SalesOrderBase):
    pass


class SalesOrderUpdate(BaseModel):
    so_number: Optional[str] = None
    customer_id: Optional[int] = None
    order_date: Optional[date] = None
    delivery_date: Optional[date] = None
    status: Optional[str] = None


class SalesOrderRead(SalesOrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
