"""Service-layer tests for Routings."""
import pytest

from app.routings import service
from app.routings.exceptions import RoutingStepNotFound, RoutingStepValidationError
from app.routings.schemas import RoutingStepCreate, RoutingStepUpdate

PAYLOAD = {
    "part_number": "Sample part number",
    "sequence": 1,
    "operation": "Sample operation",
    "work_center_id": 1,
    "std_minutes": 10.5,
}


def test_create_and_get(db):
    created = service.create_item(db, RoutingStepCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, RoutingStepCreate(**PAYLOAD))
    service.create_item(db, RoutingStepCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, RoutingStepCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, RoutingStepUpdate(part_number="Updated value"))
    assert updated.part_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, RoutingStepCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(RoutingStepNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(RoutingStepValidationError):
        service.create_item(db, RoutingStepCreate(**{**PAYLOAD, "part_number": "   "}))
