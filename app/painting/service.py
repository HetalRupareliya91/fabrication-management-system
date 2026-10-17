"""CRUD service for Painting."""
from sqlalchemy.orm import Session

from .exceptions import PaintingRecordNotFound
from .models import PaintingRecord
from .schemas import PaintingRecordCreate, PaintingRecordUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[PaintingRecord]:
    return db.query(PaintingRecord).order_by(PaintingRecord.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> PaintingRecord:
    item = db.get(PaintingRecord, item_id)
    if item is None:
        raise PaintingRecordNotFound(item_id)
    return item


def create_item(db: Session, payload: PaintingRecordCreate) -> PaintingRecord:
    data = validate(payload.model_dump())
    item = PaintingRecord(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: PaintingRecordUpdate) -> PaintingRecord:
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
