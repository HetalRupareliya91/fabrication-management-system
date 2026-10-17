"""CRUD service for Quality Checks."""
from sqlalchemy.orm import Session

from .exceptions import QualityCheckNotFound
from .models import QualityCheck
from .schemas import QualityCheckCreate, QualityCheckUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[QualityCheck]:
    return db.query(QualityCheck).order_by(QualityCheck.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> QualityCheck:
    item = db.get(QualityCheck, item_id)
    if item is None:
        raise QualityCheckNotFound(item_id)
    return item


def create_item(db: Session, payload: QualityCheckCreate) -> QualityCheck:
    data = validate(payload.model_dump())
    item = QualityCheck(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: QualityCheckUpdate) -> QualityCheck:
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
