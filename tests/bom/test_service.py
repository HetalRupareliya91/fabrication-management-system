"""Service-layer tests for Bill of Materials."""
import pytest

from app.bom import service
from app.bom.exceptions import BomLineNotFound, BomLineValidationError
from app.bom.schemas import BomLineCreate, BomLineUpdate

PAYLOAD = {
    "parent_part": "Sample parent part",
    "component_code": "Sample component code",
    "quantity": 10.5,
    "unit": "Sample unit",
    "scrap_percent": 10.5,
}


def test_create_and_get(db):
    created = service.create_item(db, BomLineCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, BomLineCreate(**PAYLOAD))
    service.create_item(db, BomLineCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, BomLineCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, BomLineUpdate(parent_part="Updated value"))
    assert updated.parent_part == "Updated value"


def test_delete(db):
    created = service.create_item(db, BomLineCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(BomLineNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(BomLineValidationError):
        service.create_item(db, BomLineCreate(**{**PAYLOAD, "parent_part": "   "}))
