"""CRUD service for Maintenance."""
from sqlalchemy.orm import Session

from .exceptions import MaintenanceTaskNotFound
from .models import MaintenanceTask
from .schemas import MaintenanceTaskCreate, MaintenanceTaskUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[MaintenanceTask]:
    return db.query(MaintenanceTask).order_by(MaintenanceTask.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> MaintenanceTask:
    item = db.get(MaintenanceTask, item_id)
    if item is None:
        raise MaintenanceTaskNotFound(item_id)
    return item


def create_item(db: Session, payload: MaintenanceTaskCreate) -> MaintenanceTask:
    data = validate(payload.model_dump())
    item = MaintenanceTask(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: MaintenanceTaskUpdate) -> MaintenanceTask:
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
