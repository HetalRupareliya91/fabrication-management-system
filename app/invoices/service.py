"""CRUD service for Invoices."""
from sqlalchemy.orm import Session

from .exceptions import InvoiceNotFound
from .models import Invoice
from .schemas import InvoiceCreate, InvoiceUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Invoice]:
    return db.query(Invoice).order_by(Invoice.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Invoice:
    item = db.get(Invoice, item_id)
    if item is None:
        raise InvoiceNotFound(item_id)
    return item


def create_item(db: Session, payload: InvoiceCreate) -> Invoice:
    data = validate(payload.model_dump())
    item = Invoice(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: InvoiceUpdate) -> Invoice:
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
