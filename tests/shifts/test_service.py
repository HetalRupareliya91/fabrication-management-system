"""Service-layer tests for Shifts."""
import pytest

from app.shifts import service
from app.shifts.exceptions import ShiftNotFound, ShiftValidationError
from app.shifts.schemas import ShiftCreate, ShiftUpdate

PAYLOAD = {
    "name": "Sample name",
    "start_time": "Sample start time",
    "end_time": "Sample end time",
    "supervisor": "Sample supervisor",
    "is_active": True,
}


def test_create_and_get(db):
    created = service.create_item(db, ShiftCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, ShiftCreate(**PAYLOAD))
    service.create_item(db, ShiftCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, ShiftCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, ShiftUpdate(name="Updated value"))
    assert updated.name == "Updated value"


def test_delete(db):
    created = service.create_item(db, ShiftCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(ShiftNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(ShiftValidationError):
        service.create_item(db, ShiftCreate(**{**PAYLOAD, "name": "   "}))
