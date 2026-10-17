"""CRUD service for Routings."""
from sqlalchemy.orm import Session

from .exceptions import RoutingStepNotFound
from .models import RoutingStep
from .schemas import RoutingStepCreate, RoutingStepUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[RoutingStep]:
    return db.query(RoutingStep).order_by(RoutingStep.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> RoutingStep:
    item = db.get(RoutingStep, item_id)
    if item is None:
        raise RoutingStepNotFound(item_id)
    return item


def create_item(db: Session, payload: RoutingStepCreate) -> RoutingStep:
    data = validate(payload.model_dump())
    item = RoutingStep(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: RoutingStepUpdate) -> RoutingStep:
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
