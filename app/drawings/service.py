"""CRUD service for Drawings."""
from sqlalchemy.orm import Session

from .exceptions import DrawingNotFound
from .models import Drawing
from .schemas import DrawingCreate, DrawingUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Drawing]:
    return db.query(Drawing).order_by(Drawing.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Drawing:
    item = db.get(Drawing, item_id)
    if item is None:
        raise DrawingNotFound(item_id)
    return item


def create_item(db: Session, payload: DrawingCreate) -> Drawing:
    data = validate(payload.model_dump())
    item = Drawing(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: DrawingUpdate) -> Drawing:
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
