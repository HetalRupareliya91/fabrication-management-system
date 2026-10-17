"""Service-layer tests for Dispatch."""
import pytest

from app.dispatch import service
from app.dispatch.exceptions import DispatchNotFound, DispatchValidationError
from app.dispatch.schemas import DispatchCreate, DispatchUpdate

PAYLOAD = {
    "dispatch_number": "Sample dispatch number",
    "sales_order_id": 1,
    "vehicle_number": "Sample vehicle number",
    "dispatch_date": "2026-01-15",
    "weight_kg": 10.5,
}


def test_create_and_get(db):
    created = service.create_item(db, DispatchCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, DispatchCreate(**PAYLOAD))
    service.create_item(db, DispatchCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, DispatchCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, DispatchUpdate(dispatch_number="Updated value"))
    assert updated.dispatch_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, DispatchCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(DispatchNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(DispatchValidationError):
        service.create_item(db, DispatchCreate(**{**PAYLOAD, "dispatch_number": "   "}))
