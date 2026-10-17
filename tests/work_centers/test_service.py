"""Service-layer tests for Work Centers."""
import pytest

from app.work_centers import service
from app.work_centers.exceptions import WorkCenterNotFound, WorkCenterValidationError
from app.work_centers.schemas import WorkCenterCreate, WorkCenterUpdate

PAYLOAD = {
    "code": "Sample code",
    "name": "Sample name",
    "capacity_hours": 10.5,
    "cost_per_hour": 10.5,
    "is_active": True,
}


def test_create_and_get(db):
    created = service.create_item(db, WorkCenterCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, WorkCenterCreate(**PAYLOAD))
    service.create_item(db, WorkCenterCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, WorkCenterCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, WorkCenterUpdate(code="Updated value"))
    assert updated.code == "Updated value"


def test_delete(db):
    created = service.create_item(db, WorkCenterCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(WorkCenterNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(WorkCenterValidationError):
        service.create_item(db, WorkCenterCreate(**{**PAYLOAD, "code": "   "}))
