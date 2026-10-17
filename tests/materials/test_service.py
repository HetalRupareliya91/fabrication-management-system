"""Service-layer tests for Materials."""
import pytest

from app.materials import service
from app.materials.exceptions import MaterialNotFound, MaterialValidationError
from app.materials.schemas import MaterialCreate, MaterialUpdate

PAYLOAD = {
    "code": "Sample code",
    "description": "Sample description",
    "grade": "Sample grade",
    "thickness_mm": 10.5,
    "unit": "Sample unit",
}


def test_create_and_get(db):
    created = service.create_item(db, MaterialCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, MaterialCreate(**PAYLOAD))
    service.create_item(db, MaterialCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, MaterialCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, MaterialUpdate(code="Updated value"))
    assert updated.code == "Updated value"


def test_delete(db):
    created = service.create_item(db, MaterialCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(MaterialNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(MaterialValidationError):
        service.create_item(db, MaterialCreate(**{**PAYLOAD, "code": "   "}))
