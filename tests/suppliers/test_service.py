"""Service-layer tests for Suppliers."""
import pytest

from app.suppliers import service
from app.suppliers.exceptions import SupplierNotFound, SupplierValidationError
from app.suppliers.schemas import SupplierCreate, SupplierUpdate

PAYLOAD = {
    "name": "Sample name",
    "gstin": "Sample gstin",
    "contact_person": "Sample contact person",
    "phone": "Sample phone",
    "rating": 1,
}


def test_create_and_get(db):
    created = service.create_item(db, SupplierCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, SupplierCreate(**PAYLOAD))
    service.create_item(db, SupplierCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, SupplierCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, SupplierUpdate(name="Updated value"))
    assert updated.name == "Updated value"


def test_delete(db):
    created = service.create_item(db, SupplierCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(SupplierNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(SupplierValidationError):
        service.create_item(db, SupplierCreate(**{**PAYLOAD, "name": "   "}))
