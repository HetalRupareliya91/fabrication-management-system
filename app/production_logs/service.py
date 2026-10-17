"""CRUD service for Production Logs."""
from sqlalchemy.orm import Session

from .exceptions import ProductionLogNotFound
from .models import ProductionLog
from .schemas import ProductionLogCreate, ProductionLogUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[ProductionLog]:
    return db.query(ProductionLog).order_by(ProductionLog.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> ProductionLog:
    item = db.get(ProductionLog, item_id)
    if item is None:
        raise ProductionLogNotFound(item_id)
    return item


def create_item(db: Session, payload: ProductionLogCreate) -> ProductionLog:
    data = validate(payload.model_dump())
    item = ProductionLog(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: ProductionLogUpdate) -> ProductionLog:
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
