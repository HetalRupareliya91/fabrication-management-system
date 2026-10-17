"""Service-layer tests for Customers."""
import pytest

from app.customers import service
from app.customers.exceptions import CustomerNotFound, CustomerValidationError
from app.customers.schemas import CustomerCreate, CustomerUpdate

PAYLOAD = {
    "name": "Sample name",
    "gstin": "Sample gstin",
    "email": "Sample email",
    "phone": "Sample phone",
    "city": "Sample city",
}


def test_create_and_get(db):
    created = service.create_item(db, CustomerCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, CustomerCreate(**PAYLOAD))
    service.create_item(db, CustomerCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, CustomerCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, CustomerUpdate(name="Updated value"))
    assert updated.name == "Updated value"


def test_delete(db):
    created = service.create_item(db, CustomerCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(CustomerNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(CustomerValidationError):
        service.create_item(db, CustomerCreate(**{**PAYLOAD, "name": "   "}))
