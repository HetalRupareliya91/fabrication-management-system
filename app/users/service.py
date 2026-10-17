"""CRUD service for Users."""
from sqlalchemy.orm import Session

from .exceptions import UserNotFound
from .models import User
from .schemas import UserCreate, UserUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[User]:
    return db.query(User).order_by(User.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> User:
    item = db.get(User, item_id)
    if item is None:
        raise UserNotFound(item_id)
    return item


def create_item(db: Session, payload: UserCreate) -> User:
    data = validate(payload.model_dump())
    item = User(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: UserUpdate) -> User:
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
