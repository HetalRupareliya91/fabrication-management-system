"""CRUD service for Quotations."""
from sqlalchemy.orm import Session

from .exceptions import QuotationNotFound
from .models import Quotation
from .schemas import QuotationCreate, QuotationUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Quotation]:
    return db.query(Quotation).order_by(Quotation.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Quotation:
    item = db.get(Quotation, item_id)
    if item is None:
        raise QuotationNotFound(item_id)
    return item


def create_item(db: Session, payload: QuotationCreate) -> Quotation:
    data = validate(payload.model_dump())
    item = Quotation(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: QuotationUpdate) -> Quotation:
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
