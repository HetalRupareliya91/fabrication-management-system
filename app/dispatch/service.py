"""CRUD service for Dispatch."""
from sqlalchemy.orm import Session

from .exceptions import DispatchNotFound
from .models import Dispatch
from .schemas import DispatchCreate, DispatchUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Dispatch]:
    return db.query(Dispatch).order_by(Dispatch.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Dispatch:
    item = db.get(Dispatch, item_id)
    if item is None:
        raise DispatchNotFound(item_id)
    return item


def create_item(db: Session, payload: DispatchCreate) -> Dispatch:
    data = validate(payload.model_dump())
    item = Dispatch(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: DispatchUpdate) -> Dispatch:
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
