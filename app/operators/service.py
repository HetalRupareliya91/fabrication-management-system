"""CRUD service for Operators."""
from sqlalchemy.orm import Session

from .exceptions import OperatorNotFound
from .models import Operator
from .schemas import OperatorCreate, OperatorUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Operator]:
    return db.query(Operator).order_by(Operator.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Operator:
    item = db.get(Operator, item_id)
    if item is None:
        raise OperatorNotFound(item_id)
    return item


def create_item(db: Session, payload: OperatorCreate) -> Operator:
    data = validate(payload.model_dump())
    item = Operator(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: OperatorUpdate) -> Operator:
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
