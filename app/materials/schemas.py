"""Pydantic schemas for Materials."""
from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MaterialBase(BaseModel):
    code: str
    description: str
    grade: str
    thickness_mm: float
    unit: str


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None
    grade: Optional[str] = None
    thickness_mm: Optional[float] = None
    unit: Optional[str] = None


class MaterialRead(MaterialBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
