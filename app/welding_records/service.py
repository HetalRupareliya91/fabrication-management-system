"""CRUD service for Welding Records."""
from sqlalchemy.orm import Session

from .exceptions import WeldingRecordNotFound
from .models import WeldingRecord
from .schemas import WeldingRecordCreate, WeldingRecordUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[WeldingRecord]:
    return db.query(WeldingRecord).order_by(WeldingRecord.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> WeldingRecord:
    item = db.get(WeldingRecord, item_id)
    if item is None:
        raise WeldingRecordNotFound(item_id)
    return item


def create_item(db: Session, payload: WeldingRecordCreate) -> WeldingRecord:
    data = validate(payload.model_dump())
    item = WeldingRecord(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: WeldingRecordUpdate) -> WeldingRecord:
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
