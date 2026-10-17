"""Pydantic schemas for Operators."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OperatorBase(BaseModel):
    employee_code: str
    name: str
    skill: str
    certification: str
    is_active: bool


class OperatorCreate(OperatorBase):
    pass


class OperatorUpdate(BaseModel):
    employee_code: Optional[str] = None
    name: Optional[str] = None
    skill: Optional[str] = None
    certification: Optional[str] = None
    is_active: Optional[bool] = None


class OperatorRead(OperatorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
