"""CRUD service for Shifts."""
from sqlalchemy.orm import Session

from .exceptions import ShiftNotFound
from .models import Shift
from .schemas import ShiftCreate, ShiftUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Shift]:
    return db.query(Shift).order_by(Shift.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Shift:
    item = db.get(Shift, item_id)
    if item is None:
        raise ShiftNotFound(item_id)
    return item


def create_item(db: Session, payload: ShiftCreate) -> Shift:
    data = validate(payload.model_dump())
    item = Shift(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: ShiftUpdate) -> Shift:
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
