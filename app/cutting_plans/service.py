"""CRUD service for Cutting Plans."""
from sqlalchemy.orm import Session

from .exceptions import CuttingPlanNotFound
from .models import CuttingPlan
from .schemas import CuttingPlanCreate, CuttingPlanUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[CuttingPlan]:
    return db.query(CuttingPlan).order_by(CuttingPlan.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> CuttingPlan:
    item = db.get(CuttingPlan, item_id)
    if item is None:
        raise CuttingPlanNotFound(item_id)
    return item


def create_item(db: Session, payload: CuttingPlanCreate) -> CuttingPlan:
    data = validate(payload.model_dump())
    item = CuttingPlan(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: CuttingPlanUpdate) -> CuttingPlan:
    item = get_item(db, item_id)
    data = validate(payload.model_dump(exclude_unset=True))
    for key, value in data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int) -> None:
    item = get_item(db, item_id)
    db.delete(item)
    db.commit()
