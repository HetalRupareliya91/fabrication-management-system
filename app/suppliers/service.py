"""CRUD service for Suppliers."""
from sqlalchemy.orm import Session

from .exceptions import SupplierNotFound
from .models import Supplier
from .schemas import SupplierCreate, SupplierUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Supplier]:
    return db.query(Supplier).order_by(Supplier.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Supplier:
    item = db.get(Supplier, item_id)
    if item is None:
        raise SupplierNotFound(item_id)
    return item


def create_item(db: Session, payload: SupplierCreate) -> Supplier:
    data = validate(payload.model_dump())
    item = Supplier(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: SupplierUpdate) -> Supplier:
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
