"""CRUD service for Bill of Materials."""
from sqlalchemy.orm import Session

from .exceptions import BomLineNotFound
from .models import BomLine
from .schemas import BomLineCreate, BomLineUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[BomLine]:
    return db.query(BomLine).order_by(BomLine.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> BomLine:
    item = db.get(BomLine, item_id)
    if item is None:
        raise BomLineNotFound(item_id)
    return item


def create_item(db: Session, payload: BomLineCreate) -> BomLine:
    data = validate(payload.model_dump())
    item = BomLine(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: BomLineUpdate) -> BomLine:
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
