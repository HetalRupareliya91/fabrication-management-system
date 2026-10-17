"""CRUD service for Non-Conformance Reports."""
from sqlalchemy.orm import Session

from .exceptions import NonConformanceNotFound
from .models import NonConformance
from .schemas import NonConformanceCreate, NonConformanceUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[NonConformance]:
    return db.query(NonConformance).order_by(NonConformance.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> NonConformance:
    item = db.get(NonConformance, item_id)
    if item is None:
        raise NonConformanceNotFound(item_id)
    return item


def create_item(db: Session, payload: NonConformanceCreate) -> NonConformance:
    data = validate(payload.model_dump())
    item = NonConformance(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: NonConformanceUpdate) -> NonConformance:
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
