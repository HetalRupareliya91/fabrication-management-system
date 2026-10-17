"""CRUD service for Job Orders."""
from sqlalchemy.orm import Session

from .exceptions import JobOrderNotFound
from .models import JobOrder
from .schemas import JobOrderCreate, JobOrderUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[JobOrder]:
    return db.query(JobOrder).order_by(JobOrder.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> JobOrder:
    item = db.get(JobOrder, item_id)
    if item is None:
        raise JobOrderNotFound(item_id)
    return item


def create_item(db: Session, payload: JobOrderCreate) -> JobOrder:
    data = validate(payload.model_dump())
    item = JobOrder(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: JobOrderUpdate) -> JobOrder:
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
