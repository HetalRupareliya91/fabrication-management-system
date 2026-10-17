"""Service-layer tests for Drawings."""
import pytest

from app.drawings import service
from app.drawings.exceptions import DrawingNotFound, DrawingValidationError
from app.drawings.schemas import DrawingCreate, DrawingUpdate

PAYLOAD = {
    "drawing_number": "Sample drawing number",
    "revision": "Sample revision",
    "title": "Sample title",
    "approved": True,
    "customer_id": 1,
}


def test_create_and_get(db):
    created = service.create_item(db, DrawingCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, DrawingCreate(**PAYLOAD))
    service.create_item(db, DrawingCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, DrawingCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, DrawingUpdate(drawing_number="Updated value"))
    assert updated.drawing_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, DrawingCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(DrawingNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(DrawingValidationError):
        service.create_item(db, DrawingCreate(**{**PAYLOAD, "drawing_number": "   "}))
