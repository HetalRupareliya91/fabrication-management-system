"""CRUD service for Materials."""
from sqlalchemy.orm import Session

from .exceptions import MaterialNotFound
from .models import Material
from .schemas import MaterialCreate, MaterialUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[Material]:
    return db.query(Material).order_by(Material.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> Material:
    item = db.get(Material, item_id)
    if item is None:
        raise MaterialNotFound(item_id)
    return item


def create_item(db: Session, payload: MaterialCreate) -> Material:
    data = validate(payload.model_dump())
    item = Material(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: MaterialUpdate) -> Material:
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
