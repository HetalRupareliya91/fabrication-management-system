"""CRUD service for Work Centers."""
from sqlalchemy.orm import Session

from .exceptions import WorkCenterNotFound
from .models import WorkCenter
from .schemas import WorkCenterCreate, WorkCenterUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[WorkCenter]:
    return db.query(WorkCenter).order_by(WorkCenter.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> WorkCenter:
    item = db.get(WorkCenter, item_id)
    if item is None:
        raise WorkCenterNotFound(item_id)
    return item


def create_item(db: Session, payload: WorkCenterCreate) -> WorkCenter:
    data = validate(payload.model_dump())
    item = WorkCenter(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: WorkCenterUpdate) -> WorkCenter:
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
