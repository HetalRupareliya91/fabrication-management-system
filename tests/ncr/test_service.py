"""Service-layer tests for Non-Conformance Reports."""
import pytest

from app.ncr import service
from app.ncr.exceptions import NonConformanceNotFound, NonConformanceValidationError
from app.ncr.schemas import NonConformanceCreate, NonConformanceUpdate

PAYLOAD = {
    "ncr_number": "Sample ncr number",
    "job_order_id": 1,
    "description": "Sample description",
    "disposition": "Sample disposition",
    "closed": True,
}


def test_create_and_get(db):
    created = service.create_item(db, NonConformanceCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, NonConformanceCreate(**PAYLOAD))
    service.create_item(db, NonConformanceCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, NonConformanceCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, NonConformanceUpdate(ncr_number="Updated value"))
    assert updated.ncr_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, NonConformanceCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(NonConformanceNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(NonConformanceValidationError):
        service.create_item(db, NonConformanceCreate(**{**PAYLOAD, "ncr_number": "   "}))
