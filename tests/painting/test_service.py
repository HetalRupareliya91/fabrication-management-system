"""Service-layer tests for Painting."""
import pytest

from app.painting import service
from app.painting.exceptions import PaintingRecordNotFound, PaintingRecordValidationError
from app.painting.schemas import PaintingRecordCreate, PaintingRecordUpdate

PAYLOAD = {
    "job_order_id": 1,
    "paint_system": "Sample paint system",
    "dft_microns": 10.5,
    "coats": 1,
    "inspected": True,
}


def test_create_and_get(db):
    created = service.create_item(db, PaintingRecordCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, PaintingRecordCreate(**PAYLOAD))
    service.create_item(db, PaintingRecordCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, PaintingRecordCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, PaintingRecordUpdate(paint_system="Updated value"))
    assert updated.paint_system == "Updated value"


def test_delete(db):
    created = service.create_item(db, PaintingRecordCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(PaintingRecordNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(PaintingRecordValidationError):
        service.create_item(db, PaintingRecordCreate(**{**PAYLOAD, "paint_system": "   "}))
