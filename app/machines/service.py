"""CRUD service for Machines."""
from sqlalchemy.orm import Session

from .exceptions import MachineNotFound
from .models import Machine
from .schemas import MachineCreate, MachineUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Machine]:
    return db.query(Machine).order_by(Machine.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Machine:
    item = db.get(Machine, item_id)
    if item is None:
        raise MachineNotFound(item_id)
    return item


def create_item(db: Session, payload: MachineCreate) -> Machine:
    data = validate(payload.model_dump())
    item = Machine(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: MachineUpdate) -> Machine:
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
