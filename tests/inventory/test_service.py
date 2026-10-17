"""Service-layer tests for Inventory."""
import pytest

from app.inventory import service
from app.inventory.exceptions import InventoryItemNotFound, InventoryItemValidationError
from app.inventory.schemas import InventoryItemCreate, InventoryItemUpdate

PAYLOAD = {
    "material_code": "Sample material code",
    "location": "Sample location",
    "quantity": 10.5,
    "reorder_level": 10.5,
    "batch_no": "Sample batch no",
}


def test_create_and_get(db):
    created = service.create_item(db, InventoryItemCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, InventoryItemCreate(**PAYLOAD))
    service.create_item(db, InventoryItemCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, InventoryItemCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, InventoryItemUpdate(material_code="Updated value"))
    assert updated.material_code == "Updated value"


def test_delete(db):
    created = service.create_item(db, InventoryItemCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(InventoryItemNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(InventoryItemValidationError):
        service.create_item(db, InventoryItemCreate(**{**PAYLOAD, "material_code": "   "}))
