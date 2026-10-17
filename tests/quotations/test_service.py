"""Service-layer tests for Quotations."""
import pytest

from app.quotations import service
from app.quotations.exceptions import QuotationNotFound, QuotationValidationError
from app.quotations.schemas import QuotationCreate, QuotationUpdate

PAYLOAD = {
    "quote_number": "Sample quote number",
    "customer_id": 1,
    "valid_until": "2026-01-15",
    "amount": 10.5,
    "status": "Sample status",
}


def test_create_and_get(db):
    created = service.create_item(db, QuotationCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, QuotationCreate(**PAYLOAD))
    service.create_item(db, QuotationCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, QuotationCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, QuotationUpdate(quote_number="Updated value"))
    assert updated.quote_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, QuotationCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(QuotationNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(QuotationValidationError):
        service.create_item(db, QuotationCreate(**{**PAYLOAD, "quote_number": "   "}))
