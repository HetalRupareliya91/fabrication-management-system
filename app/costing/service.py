"""CRUD service for Job Costing."""
from sqlalchemy.orm import Session

from .exceptions import JobCostNotFound
from .models import JobCost
from .schemas import JobCostCreate, JobCostUpdate
from .validators import validate


def list_items(db: Session, skip: int = 0, limit: int = 50) -> list[JobCost]:
    return db.query(JobCost).order_by(JobCost.id).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int) -> JobCost:
    item = db.get(JobCost, item_id)
    if item is None:
        raise JobCostNotFound(item_id)
    return item


def create_item(db: Session, payload: JobCostCreate) -> JobCost:
    data = validate(payload.model_dump())
    item = JobCost(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item_id: int, payload: JobCostUpdate) -> JobCost:
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
