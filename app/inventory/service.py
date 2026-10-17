"""CRUD service for Inventory."""
from sqlalchemy.orm import Session

from .exceptions import InventoryItemNotFound
from .models import InventoryItem
from .schemas import InventoryItemCreate, InventoryItemUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[InventoryItem]:
    return db.query(InventoryItem).order_by(InventoryItem.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> InventoryItem:
    item = db.get(InventoryItem, item_id)
    if item is None:
        raise InventoryItemNotFound(item_id)
    return item


def create_item(db: Session, payload: InventoryItemCreate) -> InventoryItem:
    data = validate(payload.model_dump())
    item = InventoryItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: InventoryItemUpdate) -> InventoryItem:
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
